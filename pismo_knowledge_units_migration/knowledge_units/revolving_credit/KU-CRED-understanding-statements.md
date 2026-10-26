---
ku_id: KU-CRED-understanding-statements
title: Understanding statements
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/understanding-statements.md
  sha256: 9121b03742ef3cd15a37496635843b915f7a3120bea6291ae49dbc1a343459f5
  url: https://developers.pismo.io/pismo-docs/docs/understanding-statements
  role: primary_guide
  updated_at: '2026-09-01T18:44:25.000Z'
operations:
- GetAccountAccrualsV2
- getAccountAccrualsV3
- getAccountsTransactionsInterest
- getInterestAccrualSummarization
related_kus:
- KU-API-revolving-credit-statements--accruals
- KU-CORE-transactions-overview
- KU-CRED-accrual-rate-types-and-limits
- KU-CRED-full-balance-credit-program
- KU-EVT-catalogue-transaction
- KU-GS-setup-overview
grouping_rationale: single source page
---

# Understanding statements

**KU ID:** `KU-CRED-understanding-statements` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/understanding-statements.md`:

> Statements are the groups of balances that result from credit card transactions. This article explains how Pismo manages the different routines necessary to maintain a simple and reliable credit card balance management function.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/understanding-statements.md`: Understanding statements; Statement management; Credit card cycles (billing periods); Calendars; Balances; Accruals; Accrual management; Daily accrual routine; Cycle closing routine; Reactive routines

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/understanding-statements.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/understanding-statements · updatedAt: 2026-09-01T18:44:25.000Z

<!-- source:begin path=docs/card-issuing/understanding-statements.md part=0-end -->

# Understanding statements

Statements are the groups of balances that result from credit card transactions. This article explains how Pismo manages the different routines necessary to maintain a simple and reliable credit card balance management function.

You should have some understanding of the following.

* [Network transactions](https://developers.pismo.io/pismo-docs/docs/transactions-overview): Statement balances are calculated according to transaction balances.
* [Pismo core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview): All configurations for statements are at the program or account level. The different statuses at all levels of the hierarchy can change the behavior of statements applications.

> 📘 Statement API endpoints
>
> Statement API endpoints require an account-specific token, not a regular access token. Account tokens are embedded with an account ID.

## Statement management

The endpoints under the "Statements" header in the API menu enable you to manage statements. For example, you can use the <Anchor label="List statements" target="_blank" href="ref:getbystatementid">List statements</Anchor> endpoint to list account statements and the [List transaction balances](https://developers.pismo.io/pismo-docs/docs/gettransactionsbalance) endpoint to get transaction balances.

## Credit card cycles (billing periods)

Credit card contracts always carry a risk of default or delay in payments. To weather this risk, the Pismo platform manages credit card balances and [interest accruals](https://developers.pismo.io/pismo-docs/docs/understanding-statements#accruals) in cycles (billing periods). Every statement corresponds to a single cycle. When a cycle ends, another cycle begins. The relationship between transactions and statements can change, but the relationship between a statement and a cycle doesn’t change. This is because statements are ordered through their cycle number.

![Illustation of credit cycles](https://files.readme.io/4f613f0-creditCardCycles2x.png "creditCardCycles@2x.png")

Every new account, upon creation, has a moving window of 43 cycles. Cycle numbers start at 1 and increment by 1 for each additional cycle. They continue to increment for the life of the account. Every time a cycle is closed, a new one is created in the future, so each account always has one current cycle and 120 future cycles.

## Calendars

Every statement is associated with a calendar, which is a group of dates that are used to determine various things, such as when payments are due. For more information, refer to [Calendar management strategies](https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies-overview).

## Balances

A statement summarizes transaction balances. The statement balance types are:

* previous balance
* debits
* credits
* current balance
* minimum amount due (MAD)

On the cycle closing date, the Pismo platform opens the next statement and uses the old statement's current balance as the previous balance for the next one. The debits and credits balances receive the sum of the amounts of the debit and credit transactions, respectively. A statement’s current balance should equal its previous balance, plus its debits, and less its credits. After the cycle closing date, the balances on a statement cannot be changed.

![Credit cycle balance statement](https://files.readme.io/2d5e030-balances-table.png "balances-table.png")

The Pismo platform updates the debits, credits and current balance values live for each new transaction as it occurs.

Cycle dynamics imply the possibility that a transaction occurs in one cycle, but nets out another transaction that happened in a different cycle. For example, a credit on Statement 2 could compensate for a debit on Statement 1.

The Pismo platform calculates the minimum amount due (MAD) for a statement at the cycle closing date. On this date, the platform assigns an open due date to the account, which equals the closed statement due date and marks the first day of **debt** in cases where an account goes into default.

## Accruals

The MAD determines whether the Pismo platform considers the debits as **paid**, **refinanced** or **overdue**.

* If the sum of the payments made within the grace period (that is, before or on the due date) are greater than or equal to the MAD, but less than the previous balance (that is, the TAD), the debits are discharged in the order determined by the payment hierarchy, and any remaining debits are considered refinanced. They can be identified by their transaction balance being greater than zero.
* If the payments made within the grace period are less than the MAD, the debits are discharged in the order determined by the payment hierarchy, and any remaining debits are considered both refinanced and overdue.
* If the sum of the payments made within the grace period before or on the due date are greater than or equal to the previous balance, the debits are considered paid.

![Illustration showing accruals](https://files.readme.io/3e8bf92-diagram-cycles.png)

One day after the due date, if the credits received are less than the previous balance, the account starts to accrue interest charges, penalties, and taxes. The Pismo platform posts these accruals as transactions, sets their transaction dates equal to the closing date, and adds them to the total amount due. Note that accruals are posted on the statement being closed.

<Image align="center" alt="Illustration showing accruals and statement date in a timeline" src="https://files.readme.io/90e3981b981034757f150bc9da2f6454c142004280ada222d3d5c756fd3451fe-diagram-accruals.png" />

Revolving financial contracts charge tax and interest rates, so they generate the **refinancing** accrual type. The Pismo platform considers default rates and penalties to be overdue debt charges, so these generate the **overdue** accrual type.  The rates can be set at a program or account level.

Each transaction has one accrued value for each accrual instance per day, per accrual type. All accruals are proportional to the debit balance due. This means that, if the customer makes a partial payment, the next accrual instance is generated based only on the remaining balance. Accruals are posted on the next cycle closing date.

### Accrual management

The endpoints under the "Accruals" header in the API menu enable you to manage accruals. For example, you can get a summary of the interest accruals for an account using the [Get interest accrual summary](https://developers.pismo.io/pismo-docs/reference/getinterestaccrualsummarization) endpoint, and you can list account accruals using the [List account accruals v3](https://developers.pismo.io/pismo-docs/reference/getaccountaccrualsv3) or [List account accruals v2](https://developers.pismo.io/pismo-docs/reference/getaccountaccrualsv2) endpoints. (Pismo recommends that you use [List account accruals v3](https://developers.pismo.io/pismo-docs/reference/getaccountaccrualsv3), which is the more advanced version.)

You can also use the [Update interest accrual statuses](https://developers.pismo.io/pismo-docs/reference/getaccountstransactionsinterest) endpoint to update the status of interest accruals. However, you should only do this for accruals created in the current cycle. For more information, refer to [Limiting the number of days accruals can be charged](https://developers.pismo.io/pismo-docs/docs/limiting-the-number-of-days-accruals-can-be-charged).

## Daily accrual routine

A scheduler triggers the daily accrual routine. The Pismo platform calculates accruals every day for all debit transactions that are overdue and that have a balance greater than zero. The routine runs through the following steps, by account, so multiple instances of the same application can run separately for different sets of accounts.

| Step                       | Description                                                                                                                                                                          |
| :------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account lock key acquiring | Obtain the key to perform operations on a credit account. Each credit account can only receive operations from one routine at a time.                                                |
| Accrual rate selection     | The accrual rates can be selected on a program, account or contract level. Program rates are overwritten by account rates, and account rates are overwritten by contract rates.      |
| Interest accrual           | Calculates interest amounts for balances both before and after their due date. You can set different rates on a program or on an account level for refinancing and overdue accruals. |
| Default interest accrual   | Calculates additional interest amounts for balances after their due date in case of default. You can set the rate on a program or account level.                                     |
| Fine accrual               | Calculates the fine for balances after their due date in case of default. You can set the fine on a program or account level.                                                        |
| Taxes accrual              | Calculates the fixed and daily taxes applied to arrears. You can configure the fixed and the daily rate on a program level.                                                          |
| Account lock key return    | Return the key to perform operations on the credit account. The key becomes available for other routines to manipulate the credit account.                                           |

The routine selects only accounts that have debit transactions that are overdue and have a balance greater than zero. This means that the routine could run every day for each account.

## Cycle closing routine

A scheduler triggers the cycle closing routine. This routine runs through the following steps  for each account. Each step is part of the process that revolves cycles.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Step
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Annual fee processing
      </td>

      <td>
        The Pismo platform processes the annual fee into statements by cycle. Each annual fee's installment  is registered as a scheduled transaction and won't affect the account limit until it is processed into the statement. You can configure the annual fee amount at the program level.
      </td>
    </tr>

    <tr>
      <td>
        Foreign exchange adjustments
      </td>

      <td>
        If you configure the program to settle foreign purchases on the cycle closing date (instead of on the transaction date), the Pismo platform processes the converted amount of the transaction into the statement. The platform converts the amount into the currency of the program, using the commercial rate of the cycle closing date.
      </td>
    </tr>

    <tr>
      <td>
        Accrual transactions creation
      </td>

      <td>
        The Pismo platform processes accrual registries into statements, grouped by their type (interest, default interest, or fine).
      </td>
    </tr>

    <tr>
      <td>
        Tax transactions creation
      </td>

      <td>
        The Pismo platform processes taxes accrual registries into statements. You can set this to happen on the cycle closing date or on the first day of each month.
      </td>
    </tr>

    <tr>
      <td>
        Pending credit processing
      </td>

      <td>
        The Pismo platform compensates any credit balance that wasn't discharged upon receipt with debit balances from the current statement. The platform manages balances on a transaction level, using a discharge routine that follows a payment hierarchy.
      </td>
    </tr>

    <tr>
      <td>
        MAD evaluation
      </td>

      <td>
        The Pismo platform calculates the MAD for each transaction category, sums the results, and posts the sum to the closing statement. You can set the categories on a program or account level.
      </td>
    </tr>

    <tr>
      <td>
        Cycle closing
      </td>

      <td>
        The Pismo platform closes the current cycle. When a cycle ends, the next one begins, so any transactions that happen on the cycle closing date, after the cycle closing routine, are registered in the new cycle, not the cycle that was just closed.
      </td>
    </tr>

    <tr>
      <td>
        Cycle opening
      </td>

      <td>
        The Pismo platform opens the next future statement, which becomes the current statement. The platform creates all new transactions in the current statement. For installment contracts, the platform creates the first installment on the current statement.
      </td>
    </tr>

    <tr>
      <td>
        Debt opening date setting
      </td>

      <td>
        The Pismo platform sets the open due date (which is the same as the due date) for the closed cycle's account.
      </td>
    </tr>

    <tr>
      <td>
        Statement events messaging
      </td>

      <td>
        The Pismo platform sends the [Statement cycle closed](https://developers.pismo.io/events/docs/statements-cycle-closing-1), [Transaction created,](https://developers.pismo.io/events/docs/transaction-creation-1) and [Credit transaction used for discharge](https://developers.pismo.io/events/docs/balance-discharge-1) events.

        If the **Indicates whether the cycle opening event should be sent to the first cycle** program parameter is set to `true`, the platform sends the [Statement cycle opened](https://developers.pismo.io/events/docs/statements-cycle-opening-1) event when the first cycle is opened. This event is only sent for the first cycle. If the parameter is `false`, it's never sent.
      </td>
    </tr>

    <tr>
      <td>
        New statement creation
      </td>

      <td>
        The Pismo platform creates a new account statement.
      </td>
    </tr>

    <tr>
      <td>
        New calendar creation
      </td>

      <td>
        The Pismo platform creates a new account calendar.
      </td>
    </tr>
  </tbody>
</Table>

The cycle closing routine runs daily. The routine selects only accounts that have statements on their cycle closing date for processing. This means that, for each account, the routine runs once every cycle.

## Reactive routines

The Pismo platform triggers reactive routines in response to events (usually a transaction creation or update). Each step is triggered separately. The following table describes the routines triggered in the statement management scope.

| Routine                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Payments and purchases processing | The Pismo platform recognizes credit or debit transactions created and, according to their transaction configuration, triggers internal routines.                                                                                                                                                                                                                                                                                              |
| Discharge                         | The Pismo platform receives credits and discharges them into previous debits. You can set up the charge order on the program level through program transaction categories. You can also set up an inner charge order for each transaction type registered within each transaction category. See [How the program uses configurable entities](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-uses-configurable-entities) for more information. |
| Debt status normalization         | The Pismo platform evaluates an account's debt status and, if the credits are more than the MAD, sets the account's collection status to **Normal** and its open due date to "Null".                                                                                                                                                                                                                                                           |
| Balance update                    | The Pismo platform adjusts debit, credit, and current balance values in the statement according to the new transaction amounts.                                                                                                                                                                                                                                                                                                                |
| Accrual reversal                  | The Pismo platform identifies a credit received for a retroactive date and reverses any accrual that isn't due. Credits that represent a partial payment cause accruals to be reversed proportionally. For the case that credits are more than the MAD, all overdue accruals are reversed.                                                                                                                                                     |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /statements-v2/v3/accounts/{accountId}/interest-accruals/summarization` | `getInterestAccrualSummarization` | Get interest accrual summary | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `GET /statements-v2/v3/accounts/{accountId}/interest-accruals` | `getAccountAccrualsV3` | List account accruals v3 | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `GET /statements/v2/accounts/{accountId}/interest-accruals` | `GetAccountAccrualsV2` | List account accruals v2 | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `PATCH /statements-v2/v3/accounts/{accountId}/interest-accruals` | `getAccountsTransactionsInterest` | Update interest accrual statuses | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |

### Operation essentials

- **`GET /statements-v2/v3/accounts/{accountId}/interest-accruals/summarization`** (`getInterestAccrualSummarization`): security `BearerAuth`; required parameters `beginDate` (query), `endDate` (query), `accountId` (path), `status` (query); required body fields none declared; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.
- **`GET /statements-v2/v3/accounts/{accountId}/interest-accruals`** (`getAccountAccrualsV3`): security `BearerAuth`; required parameters `beginDate` (query), `endDate` (query), `accountId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.
- **`GET /statements/v2/accounts/{accountId}/interest-accruals`** (`GetAccountAccrualsV2`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields none declared; response statuses 200, 500; error codes in examples `GN0001`; events none listed.
- **`PATCH /statements-v2/v3/accounts/{accountId}/interest-accruals`** (`getAccountsTransactionsInterest`): security `BearerAuth`; required parameters `accountId` (path); required body fields `accruals`; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.

## Events

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `transaction-creation-1` | transaction | 1 | https://developers.pismo.io/events/docs/transaction-creation-1 | 7 | KU-EVT-catalogue-transaction |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/understanding-statements.md`: updatedAt 2026-09-01T18:44:25.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 4 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/understanding-statements.md` | whole document | https://developers.pismo.io/pismo-docs/docs/understanding-statements | `9121b03742ef3cd1…` | 2026-09-01T18:44:25.000Z |

## Related knowledge units

- `KU-API-revolving-credit-statements--accruals` — API reference: Revolving credit - Statements — Accruals
- `KU-CORE-transactions-overview` — Transactions overview
- `KU-CRED-accrual-rate-types-and-limits` — Accrual rate types, accrual-free transaction types and accrual-day limits
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-GS-setup-overview` — Core objects
