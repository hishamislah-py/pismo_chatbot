---
ku_id: KU-CRED-how-payments-are-applied-to-accruals
title: How payments are applied to accruals
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/how-payments-are-applied-to-accruals.md
  sha256: 6625c97c7673979aa874d2952517921b3f1e6a2a6dac40708eca0eab550a70b2
  url: https://developers.pismo.io/pismo-docs/docs/how-payments-are-applied-to-accruals
  role: primary_guide
  updated_at: '2026-04-16T10:06:32.000Z'
operations: []
related_kus:
- KU-CRED-full-balance-credit-program
grouping_rationale: single source page
---

# How payments are applied to accruals

**KU ID:** `KU-CRED-how-payments-are-applied-to-accruals` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/how-payments-are-applied-to-accruals.md`:

> When a cardholder makes a payment, it can affect not only how debit transactions are paid off, but how they accrue interest. The following examples demonstrate how the Pismo platform handles payments in various situations.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/how-payments-are-applied-to-accruals.md`: How payments are applied to accruals; Example 1: Full payment before payment due date; Example 2: Full payment between payment due date and real due date; Step 1: Calculates the daily rate.; Step 2: Calculates daily accruals for each transaction.; Step 3: When the payment is received, the platform generates negative accruals to compensate for the accrued interest.; Example 3: Full payment after real due date; Step 1: Calculates the daily rate.; Step 2: Calculates daily accruals for each transaction.; Step 3: When the payment is received, the account stops accumulating accruals.; Example 4: Partial payment between payment due date and real due date; Step 1: Calculates the daily rate.; Step 2: Calculates daily accruals for each transaction.; Step 3: Applies the payment to the unpaid balances.; Step 4: When the payment is received, the platform generates negative accruals to compensate for the accrued interest.; Example 5: Partial payment after the real due date; Step 1: Applies the payment to the unpaid balances.; Step 2: Calculates the daily accruals for the remaining balance.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/how-payments-are-applied-to-accruals.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/how-payments-are-applied-to-accruals · updatedAt: 2026-04-16T10:06:32.000Z

<!-- source:begin path=docs/card-issuing/how-payments-are-applied-to-accruals.md part=0-end -->

# How payments are applied to accruals

When a cardholder makes a payment, it can affect not only how debit transactions are paid off, but how they accrue interest. The following examples demonstrate how the Pismo platform handles payments in various situations.

For all examples, assume the following:

* The cycle closing date happens on day 30 of each cycle (Cycle 1 and Cycle 2).

* The payment due date for Cycle 1 falls on day 20 of the following cycle (Cycle 2).

* The [real due date](https://developers.pismo.io/pismo-docs/docs/managing-grace-period#calculating-the-real-due-date) falls five days later (day 25 of Cycle 2).

* Two debit transactions occur in Cycle 1:\
  The first transaction (TXN1) for $200 is posted on day 5 of Cycle 1.\
  The second transaction (TXN2) for $50 is posted on day 15 of Cycle 1.

* Both transactions (TXN1 and TXN2) are in the same program transaction category, and the refinancing rate for that category is 6%.

* The Pismo platform divides the refinancing rate by 30 to get the daily rate.

* On the closing date for Cycle 1, the total amount due is the total of the two transactions ($250), and the minimum amount due (MAD) is $25.

There are two ways the Pismo platform can calculate and apply daily accruals, depending on the client’s market:

**Scenario 1:** In some markets, daily accruals are calculated and applied each day, beginning on the payment due date plus one day (PDD + 1). Accruals continue to accumulate until the charges are paid off.

**Scenario 2:** In other markets, daily accruals for the period between the transaction day plus one day (TD + 1) and the payment due date (PDD) are calculated on PDD + 1 and applied retroactively. Daily accruals then continue to be applied beginning on PDD + 1, just as in Scenario 1. **Note that this is true for both cash advance and purchase transactions.**

Check with your Pismo representative to find out which scenario is used in your market.

<Callout icon="📘" theme="info">
  In the following examples (where applicable), separate diagrams are used for each of the two scenarios described above.
</Callout>

## Example 1: Full payment before payment due date

If the cardholder makes a payment for the full amount owed before or on the payment due date, then no accruals are generated.

<Image align="center" alt="Full payment before payment due date" src="https://files.readme.io/587a9c7-interest-accrual-1_both_markets.png" />

## Example 2: Full payment between payment due date and real due date

Suppose the cardholder pays off the total amount due after the payment due date, but before the real due date. On the day after the payment due date, the platform calculates (but does not post) the accrued interest. On the day the payment is made, since it's before the real due date, the platform creates negative accruals to offset the already calculated positive accruals. At the next cycle closing, the platform summarizes the positive and negative accruals. In this case, since the payment was for the full amount, the result is zero, and no accruals are posted to the statement.

Assume the cardholder makes a payment of $250 on day 22 of Cycle 2. The Pismo platform performs the following steps.

### Step 1: Calculates the daily rate.

Daily rate = 6% / 30 days = 0.2% per day (a 0.002 multiplication factor)

### Step 2: Calculates daily accruals for each transaction.

Daily rate for TXN1 = 200 x 0.002 = $0.4\
Daily rate forTXN2 = 50 x 0.002 = $0.1

(These accruals are calculated, but not posted.)

### Step 3: When the payment is received, the platform generates negative accruals to compensate for the accrued interest.

When the payment is received, the platform generates negative accruals to offset the positive accruals. These accruals are calculated differently, depending on whether you are using scenario 1 or 2 (the scenarios described just before Example 1):

**Scenario 1**: Positive accruals only occur from the payment due date plus 1 (day 21 of Cycle 2) until the payment is made. The payment was made on day 22, so only one positive accrual (on day 21) was made before the payment. (Assume the payment was made before the accrual calculation for the day. The accrual calculation starts right after midnight, but it takes some time to complete.)
1 day of accruals on TXN1: 1 x 0.4 = $0.4\
1 day of accruals on TXN2: 1 x 0.1 = $0.1

The platform calculates the negative accrual: 0.4 + 0.1 = $0.5

When Cycle 2 closes, the Pismo platform sums the positive and negative accruals ($0.5 - $0.5), resulting in a net accrual of $0.

**Scenario 2:** TXN1 was posted on day 5 of Cycle 1, and the cycle closed on day 30. That's 25 days of accruals. The payment was made on day 22 of Cycle 2. Assume the payment was made after the Pismo platform calculated accruals for that day. That's another 22 days. (If it was made before the platform calculated the accruals for that day, it would be 21 days.)
So, 25 + 22 = 47: "
46 days of accruals on TXN1: 47 x 0.4 = $18.8

TXN2 was posted on day 15 of Cycle 1. That's 30 - 15 = 15 days of accruals, plus the 22 days of accruals from Cycle 2: 15 + 22 = 37. So:\
37 days of accruals on TXN2: 37 x 0.1 = $3.7

The platform calculates the negative accrual: 18.8 + 3.7 = $22.2

When Cycle 2 closes, the Pismo platform sums the positive and negative accruals ($22 - $22.2), resulting in a net accrual of $0.2.

<Callout icon="📘" theme="info">
  In both Scenario 1 and Scenario 2, no accruals end up being posted to the statement. So, from the customer's point of view, these scenarios are almost identical. The only difference is that the platform generates an [Accrual created](https://developers.pismo.io/events/docs/balance-accrual-data-1) event for each positive daily accrual and a [Reversal accrual created](https://developers.pismo.io/events/docs/balance-reversal-accrual-data-1) event for each negative daily accrual, so, if the issuer wants to use these events, they need to understand what the platform is doing "behind the scenes".
</Callout>

**Scenario 1:**

<Image align="center" alt="Full payment between payment due date and real due date (Scenario 1)" src="https://files.readme.io/6ba5b4e-interest-accrual-2_Brazilian.png" />

**Scenario 2:**

<Image align="center" alt="Full payment between payment due date and real due date (Scenario 2)" src="https://files.readme.io/5fd7454-interest-accrual-3_Indian.png" />

## Example 3: Full payment after real due date

The Pismo platform performs the following steps.

### Step 1: Calculates the daily rate.

Daily rate = 6% / 30 days = 0.2% per day (a 0.002 multiplication factor)

### Step 2: Calculates daily accruals for each transaction.

Daily accrual for TXN1 = 200 x 0.002 = $0.4\
Daily accrual for TXN2 = 50 x 0.002 = $0.1

(These accruals are calculated, but not posted.)

### Step 3: When the payment is received, the account stops accumulating accruals.

Since the payment was received after the real due date, the platform does **not** offset them by posting a negative accrual. The platform posts the full amount of the accruals on the statement..

**Scenario 1:**

<Image align="center" alt="Full payment after real due date (Scenario 1)" src="https://files.readme.io/0a571b1-interest-accrual-4_Brazilian.png" />

**Scenario 2:**

<Image align="center" alt="Full payment after real due date (Scenario 2)" src="https://files.readme.io/d1f9308-interest-accrual-5_Indian.png" />

## Example 4: Partial payment between payment due date and real due date

Suppose the cardholder pays $210 on day 22 of Cycle 2. The Pismo platform performs the following steps.

### Step 1: Calculates the daily rate.

Daily rate = 6% / 30 days = 0.2% per day (a 0.002 multiplication factor)

### Step 2: Calculates daily accruals for each transaction.

Daily accrual for TXN1 = 200 x 0.002 = $0.4\
Daily accrual for TXN2 = 50 x 0.002 = $0.1

(These accruals are calculated, but not posted.)

### Step 3: Applies the payment to the unpaid balances.

Since transactions TXN1 and TXN2 belong to the same category, and TXN1 was posted before TXN2, the payment is first used to pay off TXN1. (See [How the program discharges transactions](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-discharges-transactions) for more information about how the Pismo platform determines payment order.)

The platform uses $200 of the $210 paid to pay off TXN1:\
Balance for TXN1 = 200 - 200 (from the $210 paid) = $0.

This leaves $10 to apply to TXN2:\
Balance for TXN2 = 50 - 10 = $40.

### Step 4: When the payment is received, the platform generates negative accruals to compensate for the accrued interest.

When the payment is received, the platform gets the accrued totals and generates a negative accrual to compensate for the positive accruals that have already been calculated.

Since TXN1 is paid off, the negative accrual must compensate for the full 46 days of positive accruals for that transaction:\
46 days of accruals on TXN1: 46 x 0.4 = $18.4

For TXN2, only the $10 that was paid off must be compensated for. The daily accruals for the paid and unpaid portions of TXN2 are calculated as follows:\
Daily accrual for the part of TXN2 that was paid off: 10 x 0.002 = 0.02\
Daily accrual for the unpaid balance of TXN2: 40 x 0.002 = 0.08\
(Note that 0.02 + 0.08 = 0.1, which is the daily rate for the entire amount of TXN2.)

So, the negative accrual must compensate for 36 x 0.02  = $0.72, which is the total accrual for the portion of TXN2 that was paid off.

The total negative accrual is the sum of the negative accruals calculated for TXN1 and TXN2: 18.4 + 0.72 = $19.12

**Scenario 1:**

<Image align="center" alt="Partial payment between payment due date and real due date (Scenario 1)" src="https://files.readme.io/33d4585-interest-accrual-6_Brazilian.png" />

**Scenario 2:**

<Image align="center" alt="Partial payment between payment due date and real due date (Scenario 2)" src="https://files.readme.io/52a0721-interest-accrual-7_Indian.png" />

## Example 5: Partial payment after the real due date

Suppose the cardholder pays $210 on day 27 of Cycle 2, which is after the real due date. The Pismo platform performs the following steps.

### Step 1: Applies the payment to the unpaid balances.

Since transaction TXN1 was posted before TXN2, the payment is first used to pay off TXN1:\
Balance for TXN1 = 200 - 200 (from the $210 paid) = $0.

This leaves $10 to apply to TXN2:\
Balance for TXN2 = 50 - 10 = $40.

### Step 2: Calculates the daily accruals for the remaining balance.

Recall that the daily accruals for the two transactions were calculated like this:\
Daily accrual for TXN1 = 200 x 0.002 = $0.4\
Daily accrual for TXN2 = 50 x 0.002 = $0.1

These are the accruals that were calculated for each day ( beginning the day after each transaction was posted and ending the day before the payment). Since TXN1 is now totally paid off, no further accruals are posted for that transaction. For TXN2, however, there is still a balance of $40. The platform must calculate a new value for future accruals:\
New daily accrual for TXN2: 40 x 0.002 = $0.08

The platform starts applying this daily accrual amount on day 27 of Cycle 2.

**Scenario 1:**

<Image align="center" alt="Partial payment after the real due date (Scenario 1)" src="https://files.readme.io/37a43a0-interest-accrual-8_Brazilian.png" />

**Scenario 2:**

<Image align="center" alt="Partial payment after the real due date (Scenario 2)" src="https://files.readme.io/6618792-interest-accrual-9_Indian.png" />
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/how-payments-are-applied-to-accruals.md`: updatedAt 2026-04-16T10:06:32.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/how-payments-are-applied-to-accruals.md` | whole document | https://developers.pismo.io/pismo-docs/docs/how-payments-are-applied-to-accruals | `6625c97c7673979a…` | 2026-04-16T10:06:32.000Z |

## Related knowledge units

- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
