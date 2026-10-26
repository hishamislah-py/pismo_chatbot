---
ku_id: KU-BANK-dated-transactions
title: Business-dated and value-dated transactions
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/biz-dated-txns.md
  sha256: 15e29b77ff15822e6ffd374f5288964db94524b0e7d52e246ceb7ca19a87db75
  url: https://developers.pismo.io/pismo-docs/docs/biz-dated-txns
  role: primary_guide
  updated_at: '2026-04-24T21:59:18.000Z'
- path: docs/core-banking/back-biz-dated-txns.md
  sha256: 5c581152fb4fb0293a869c059381622ed01e385165055a4e8e833c9bc1f3d1fd
  url: https://developers.pismo.io/pismo-docs/docs/back-biz-dated-txns
  role: primary_guide
  updated_at: '2026-04-24T21:59:18.000Z'
- path: docs/core-banking/future-biz-dated-txns.md
  sha256: e5282d034fedfce41142ee2173b3f1c6b2d4105cf57c8d4aae491cd62d757d8d
  url: https://developers.pismo.io/pismo-docs/docs/future-biz-dated-txns
  role: primary_guide
  updated_at: '2026-04-24T21:59:18.000Z'
- path: docs/core-banking/back-value-dated-txns.md
  sha256: cd8cdca1a43e627be0c66f12a22c8bffceca01ca7edc264671626264d1a582b0
  url: https://developers.pismo.io/pismo-docs/docs/back-value-dated-txns
  role: primary_guide
  updated_at: '2026-05-04T15:53:20.000Z'
- path: docs/core-banking/future-value-dated-txns.md
  sha256: 839de48196c85ae3f8f674897c73d67dc1541e5b8cdefb6d65b440064b2ef6a2
  url: https://developers.pismo.io/pismo-docs/docs/future-value-dated-txns
  role: primary_guide
  updated_at: '2026-05-04T15:50:00.000Z'
- path: docs/core-banking/channel-control-for-back-business-date-and-cutoff-exceptions.md
  sha256: dd70b4e49a5607a26619e9999f58d1b8462ad0cf39eb1c9e0b77e570e6288719
  url: https://developers.pismo.io/pismo-docs/docs/channel-control-for-back-business-date-and-cutoff-exceptions
  role: primary_guide
  updated_at: '2026-04-16T19:35:25.000Z'
operations:
- corporate-v2-post-confirm-payments
- corporate-v2-post-multileg-payments
- corporate-v2-post-payments
- delete-corporate-v1-channels
- patch-account-balances-history-configuration
- post-acceptance-by-tenant
- post-account-balance-history-configuration
- post-bulk-settlement
- post-corporate-v1-channels
related_kus:
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--bulk-settlement
- KU-API-banking-transaction-banking--channels
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-core-platform-balance-watcher--limit-acceptance-configurations
- KU-API-core-platform-payment-configurations--payment-method-acceptances
- KU-BANK-calendars-and-holidays
- KU-BANK-dormancy
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
grouping_rationale: Variants of the same dating mechanism plus its channel control.
---

# Business-dated and value-dated transactions

**KU ID:** `KU-BANK-dated-transactions` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 6 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Variants of the same dating mechanism plus its channel control.

Scope as stated in `docs/core-banking/biz-dated-txns.md`:

> Transactions sometimes need to be processed as if they were received on a different date than when they were actually processed. For instance, a transaction might be processed after the business day has ended, but must be treated as if it was received during that business day due to an error. Conversely, a transaction received on a particular day might need to be recorded as if it was received on a later date, such as when it arrives on a day the bank is closed.

Scope as stated in `docs/core-banking/back-biz-dated-txns.md`:

> Back-business-dated transactions are financial transactions that have a business date earlier than the actual transaction date. Back business-dating a transaction ensures that financial statements and records are precise and aligned with actual economic events, maintaining the integrity and accuracy of financial reporting. It is crucial for compliance with accounting standards and regulations, providing a true and fair view of an organization's financial position and is commonly used for error correction, compensation for payment delays, and regulatory compliance.

Scope as stated in `docs/core-banking/future-biz-dated-txns.md`:

> Future-business-dated transactions, also known as postdated transactions, are financial transactions recorded with a business date later than the actual date of processing. This means the transaction is registered in the financial records on the specified future date. Postdating is commonly used for transactions occurring on non-work days to ensure payment recording happens on the next work day rather than immediately.

Scope as stated in `docs/core-banking/back-value-dated-txns.md`:

> Back-value-dated transactions are essential for maintaining accurate account balances. They play a crucial role in adjusting account values to correct errors, provide timely compensation to customers, and meet regulatory requirements. By ensuring that the back-value-dated balance accurately reflects the correct payment date, even if the transaction was processed later, these transactions help maintain the integrity of financial records and ensure compliance with regulations.

Scope as stated in `docs/core-banking/future-value-dated-txns.md`:

> Future-value-dated transactions, are transactions that are scheduled to occur on a specific future date, meaning funds are only available when that date arrives. This type of transaction is useful for recurring payments, delayed payments, and other scenarios outlined in the  [Key benefits](#key-benefits) section.

Scope as stated in `docs/core-banking/channel-control-for-back-business-date-and-cutoff-exceptions.md`:

> Channel control is a cash management feature that lets you define transaction posting rules based on a transaction’s channel, or origin. It allows you to configure exceptions to standard end‑of‑day (EOD) cutoff rules for specific channels, such as ATM, while transactions from all other channels follow standard cutoff processing.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/biz-dated-txns.md`: Business-dated transactions; Cutoffs, EOD, and product processors; Cycle closing versus EOD; Other key terms for understanding business dates; How Pismo handles business-dated transactions
- `docs/core-banking/back-biz-dated-txns.md`: Back-business-dated transactions; Reasons and scenarios for backdating business transactions; Effects of back-valued transactions on account balances; How back-business-date transactions work
- `docs/core-banking/future-biz-dated-txns.md`: Future-business-dated transactions; Overview of balance types and their effects; How future-dated-business transactions work; Scenario 1: Credit; Scenario 2: Debit; Custom processing codes
- `docs/core-banking/back-value-dated-txns.md`: Back-value-dated transactions; Objectives of back-value-dated transactions; How to post a back-value-dated transaction; Impact on account balances; Examples; Rules for performing a back-value-dated transaction
- `docs/core-banking/future-value-dated-txns.md`: Future-value-dated transactions; Key benefits; Use cases; Transaction process; Posting; Clearing; Future-valued-dated transactions versus scheduled payments; Guidelines for future-value-dated transactions
- `docs/core-banking/channel-control-for-back-business-date-and-cutoff-exceptions.md`: Channel control for back-business-date and cutoff exceptions; How channel control works; Channel control extension to past-business-date toggle; Safeguards; Create channel control; Endpoints; Channel Rules; Channel‑based business date exceptions; Using channels in transactions; Common use cases; Post transactions after cutoff; Remove a previously allowed channel; Bulk payments with mixed channels; Channel events

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 10 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/biz-dated-txns.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/biz-dated-txns · updatedAt: 2026-04-24T21:59:18.000Z

<!-- source:begin path=docs/core-banking/biz-dated-txns.md part=0-end -->

# Business-dated transactions

Transactions sometimes need to be processed as if they were received on a different date than when they were actually processed. For instance, a transaction might be processed after the business day has ended, but must be treated as if it was received during that business day due to an error. Conversely, a transaction received on a particular day might need to be recorded as if it was received on a later date, such as when it arrives on a day the bank is closed.

To manage these situations, the Pismo platform uses business dates. A business date is a substitute date used in calculations instead of the actual transaction date and is the date that appears on the customer statement. Transactions with a populated `business_date` field are referred to as business-dated transactions.

Another important concept to understand is the value date. The value date is when the value of a financial transaction becomes effective and determines when the funds are valid for interest accrual purposes. Unlike the business date, the value date specifically indicates when interest calculations begin, as interest accrual only starts when the funds are actually available.

# Cutoffs, EOD, and product processors

To understand business-dated transactions, you must first understand how cutoffs are defined. In traditional banking, cutoffs refer to moments in time when the activities for a given branch are closed for that business day, with any new operations recorded on the next business day.

A commonly-used term for one type of cutoff is **EOD (End Of Day)**, which signifies the time when daily operations are concluded. This concept is used by banking systems across the market to support operations in different time zones and locations.

Some banking institutions use third-party systems that offer customized options to trigger cutoffs. These institutions might employ multiple cutoffs for various operational reasons. A cutoff is triggered when the product processors complete their EOD processes. A product processor is a system or application that manages specific financial products or services within an organization. Product processors typically handle tasks such as calculating interest rates, processing transactions, generating reports, and maintaining records, ensuring that these financial operations are carried out accurately and efficiently.

If any processes take longer than expected, a human operator waits and triggers the cutoff only when all processes are finished.

For business-dated transactions, product processors need to know the end of the cycle date and the specified business date in order to start calculating interest rates and preparing financial reports for that specific date.

# Cycle closing versus EOD

Traditionally, the EOD is used to represent the conclusion of the business day. The primary goal of EOD operations is to finalize all financial operations for the day and prepare the system for the next business day. Usually, EOD operations for a branch can begin only after all the transactions for that business day have been cleared and settled. This means the Start of Day (SOD) process can only begin after the EOD processes are completed, resulting in downtime for transaction processing.

The Pismo platform, however, adopts cycle closing, which ensures continuous operation, 24/7, to replace the traditional EOD process. At business closing, each account transitions smoothly between business days, minimizing transaction processing downtime to nearly zero. Other routines typically associated with EOD, such as [dormancy evaluation](https://developers.pismo.io/pismo-docs/docs/dormancy-overview), are configured to run independently and on their own schedules.

# Other key terms for understanding business dates

| Term                                   | Definition                                                                                                                                              |
| :------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Value date**                         | The datetime when funds are considered for interest calculation in an account. This is the datetime that you specified in the `payment_datetime` field. |
| **Business date**                      | Working day or interval of the transaction posting. This appears in the statement.                                                                      |
| **Current date**                       | Date the request was received by the Pismo platform.                                                                                                    |
| **Cycle closing datetime**             | Datetime that marks the end of a business day.                                                                                                          |
| **Regular transactions**               | A transaction is considered regular if you do not specify a business date or value date, or if both dates equal the current date.                       |
| **Back-business-dated transactions**   | Back-business-dated transactions are those where the business date precedes the transaction date.                                                       |
| **Future-business-dated transactions** | Future-business-dated transactions are those where the business date is later than the transaction date.                                                |
| **Back-value-dated transactions**      | A back-value-dated transaction is a transaction that has a value date that is earlier than its business date.                                           |
| **Future-value-dated transactions**    | A future-value-dated transaction is a transaction that has a value date that is later than its business date.                                           |

# How Pismo handles business-dated transactions

Use the [Create account balance history configuration](https://developers.pismo.io/pismo-docs/reference/post-account-balance-history-configuration) and [Update account balance history configuration](https://developers.pismo.io/pismo-docs/reference/patch-account-balances-history-configuration) endpoints to configure cycle closing for an account at the division level by providing a value for the `cycle_closing_time` field. Transactions posted before a division's `cycle_closing_time` are included in the account's balance history for the business date.

At the `cycle_closing_time` of a given business date, the Pismo platform sends the account balance history event for each account. Note that if `cycle_closing_time` is not specified, it defaults to 23:59:59 UTC.\
Use the following endpoints to manage cutoffs.

| Description                                                                                      | Usage instruction                                                                                                                                                                                                                                             |
| :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Create account balance history configuration](https://developers.pismo.io/pismo-docs/reference/post-account-balance-history-configuration)   | Use this endpoint to define a cutoff by specifying a value for `cycle_closing_time`. After executing the request, the Pismo platform starts the cycle based on the provided value. If `cycle_closing_time` is not specified, it defaults to 23:59:59.999 UTC. |
| [Update account balance history configuration](https://developers.pismo.io/pismo-docs/reference/patch-account-balances-history-configuration) | Use this endpoint to update a cutoff by specifying a value for `cycle_closing_time`. The Pismo platform uses the new value to start future cycles. If no value is specified in `cycle_closing_datetime`, it defaults to 23:59:59.999 UTC.                     |
<!-- source:end -->

### Source 2: `docs/core-banking/back-biz-dated-txns.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/back-biz-dated-txns · updatedAt: 2026-04-24T21:59:18.000Z

<!-- source:begin path=docs/core-banking/back-biz-dated-txns.md part=0-end -->

# Back-business-dated transactions

Back-business-dated transactions are financial transactions that have a business date earlier than the actual transaction date. Back business-dating a transaction ensures that financial statements and records are precise and aligned with actual economic events, maintaining the integrity and accuracy of financial reporting. It is crucial for compliance with accounting standards and regulations, providing a true and fair view of an organization's financial position and is commonly used for error correction, compensation for payment delays, and regulatory compliance.

Similarly, transaction back value dating is also essential for ensuring the accuracy of accounts in banking systems, protecting banks from fraud and errors, ensuring customers are neither overcharged nor underpaid, and maintaining the integrity of the banking system.

# Reasons and scenarios for backdating business transactions

| Reason                              | Scenario                                                                                                                                                                                                                                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                                      |
| :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Error correction**                | If a bank makes a mistake in processing a payment, it might backdate the funds to the correct date. For instance, if a bank credits a customer's account with USD 100 on the 1st of the month, but the payment was actually made on the 15th of the previous month, the bank might backdate the funds to the 15th of the previous month to ensure the customer's account balance is accurate.                                                        | On 15th August, a bank mistakenly debits USD 100.00 from a customer's account. The bank realizes the mistake on 16th August and backdates the correction to 31st July. This results in the customer's balance on 31st July being USD 100.00 higher than it should have been. |
| **Compensation for payment delays** | If a bank takes two weeks to process a payment, it might backdate the funds to the original payment date. This helps compensate the customer for the interest they would have earned if the funds had been available sooner.                                                                                                                                                                                                                         | A client is issued a refund of USD 450.00 on 30th May. However, it takes 7 days for the bank to process the refund, which is completed on 7th June with a value date of 30th May.                                                                                            |
| **Regulatory compliance**           | There are cases where banks are required by law to backdate funds. For instance, in the United States, banks must backdate funds to the correct date if they make an error in processing a payment. This ensures customers are neither overcharged nor underpaid. A payment made or received after the agreed settlement date can significantly impact the account balance, often resulting in delay-interest that might need to be paid or claimed. | On 1st August, a bank makes a significant error with a client's payment. To compensate, the bank offers USD 150.00 on 15th September, backdated to 1st August. The compensation is posted on 15th September with a value date of 1st August.                                 |

<Callout icon="📘">
  **About value dates**

  A value date is the date on which the value of a financial transaction becomes effective. It determines when the funds involved in the transaction are valid for interest accrual purposes. The value date is important for adjusting interest calculations and ensuring accurate financial reporting.
</Callout>

# Effects of back-valued transactions on account balances

The value dated balance is adjusted to reflect back-valued funds. This means the balance is higher if credited funds are back-valued and lower if debited funds are back-valued, as the interest earned on the account might be adjusted. This process is closely tied to balance history developments and the management of the bank's close-of-business process. The effect on Pismo balances is as follows.

| Balance type            | Impact                                                                                                                                                                                                                                                                                                   |
| :---------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ledger balance**      | The ledger balance reflects all financial operations in an account. It is calculated by adding the book balance for today's business date to the uncleared funds. When transactions are back-valued, the ledger balance is adjusted solely for the current business date.                                |
| **Available balance**   | The available balance is the amount of money immediately accessible to the account holder. This is the actual balance used to authorize transactions as they occur. When a transaction is back-valued, the available balance is adjusted online only for the current business date.                      |
| **Book balance**        | The book balance is the total amount of money that has been cleared and settled into the account, including any held funds. When a transaction is back-valued, the book balance is adjusted online only for the current business date.                                                                   |
| **Value-dated balance** | Back-valued transactions impact the account's value-dated balance from the past value date. Therefore, balances from that point onward must be recalculated to reflect the updated value-dated balance. During this period, balance events need to be re-emitted to indicate adjustments or corrections. |

# How back-business-date transactions work

The Pismo platform allows you to send payments to a past date by using the `business_date` and `payment_datetime` fields in [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) and [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments). This feature ensures that transactions missing the cycle end are processed as though they occurred before the cycle ended, maintaining accurate balance history. The `business_date` field specifies the balance history cycle in which a payment is recorded, while the `payment_datetime` field enables you to backdate or postdate payments.

> 🚧 Things to know
>
> * `business_date` can only represent the current, the next, or the previous business day for performance and compliance reasons.
> * You must send `business_date` along with the `payment_datetime` field, and the latter must be before the `business_date`.
> * Backdating earmark creations is not supported; however, you can execute a valid (non-expired) earmark using a back-business-dated payment. Note that the earmark creation date must be earlier than or equal to `business_date`.
> * `business_date` earlier than the previous work day (D-1) is not allowed.

Here is a detailed illustration of how back-business-dating works.

<Image align="center" alt="Back-business-dated transaction workflow" caption="Figure 1: Back-business-dated transaction workflow" src="https://files.readme.io/f58f0b8bd971bf20b3e9193ba65812d932b2c29f507c9e299d356633cadedd20-back_biz_dated_txn_workflow.png" />

Here is what the preceding diagram illustrates:

1. You send a new `business_date` to Pismo, which verifies if it's a backdated business payment.
2. Pismo determines if the specified date is either the current date or before the previous work day (D-1).
3. Pismo confirms if it's a back-value-dated payment and is before your `business_date`. If so, update the transaction's business date to the value received.
4. Pismo updates all balances (value-dated) from the payment date until the payment business date.
5. Finally, Pismo checks if the `business_date` is before the current business date. If so, it updates all balances of newer business dates; otherwise, the process completes.
<!-- source:end -->

### Source 3: `docs/core-banking/future-biz-dated-txns.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/future-biz-dated-txns · updatedAt: 2026-04-24T21:59:18.000Z

<!-- source:begin path=docs/core-banking/future-biz-dated-txns.md part=0-end -->

# Future-business-dated transactions

Future-business-dated transactions, also known as postdated transactions, are financial transactions recorded with a business date later than the actual date of processing. This means the transaction is registered in the financial records on the specified future date. Postdating is commonly used for transactions occurring on non-work days to ensure payment recording happens on the next work day rather than immediately.

Here are some key points about future-business-dated transactions.

* **Purpose**: They are often used to manage accounting entries so that financial events align with accounting  timelines.
* **Recording**: The transaction is not confirmed in the accounting records until the postdated date. This means that the financial impact is deferred.
* **Legal considerations**: Depending on jurisdiction, there might be legal implications or restrictions on postdated financial instruments.
* **Examples**: Postdated checks, postdated invoices, or any other financial commitments that specify a future date for their execution.

It's important for businesses to handle future-business-dated transactions carefully to ensure that their financial records are accurate and compliant with accounting principles and regulations.

Pismo allows you to request a transaction to be processed on the next business date using `payment_datetime` in [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) or [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments); however, it is limited to only 1 business day to mitigate operational risks.

# Overview of balance types and their effects

Details about balance types and the effect of future-business-dated transactions on balances are as follows.

| Balance type        | Effect                                                                                                                                                                                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Value-dated balance | This balance is used as the basis for interest calculations in an interest-bearing account. This is the balance where funds are available for immediate use.                                                                                                       |
| Value date          | This is equivalent to the `payment_datetime` in [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) or [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments), and refers to the date from which interest is calculated for either credit or debit balances. |
| Ledger balance      | This is a consolidate balance of all incoming transaction. It's calculated as **book balance** + **uncleared funds**.                                                                                                                                              |
| Book balance        | This is the running balance shown on account statements. This might sometimes include uncleared funds.                                                                                                                                                             |
| Available balance   | This is the balance in the account that is validated every time a transaction is carried out. It is calculated as **Book balance** + **overdrafts** - **earmark amount/blocked funds** - **uncleared funds**.                                                      |
| Uncleared funds     | These are funds that are still under clearance. On the **value date**, these funds are removed from the uncleared balance and impact other relevant balances.                                                                                                      |

# How future-dated-business transactions work

To demonstrate how future-dated-business transactions works, consider the following scenarios.

## Scenario 1: Credit

1. Begin with an account that has a zero balance, as indicated by the following account details.

```json
{
  "account_id": 1234,
  "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab",
  "program_id": 8674,
  "ledger_balance": 0,
  "book_balance": 0,
  "available_balance": 0,
  "credit_balance": 0,
  "debit_balance": 0,
  "uncleared_funds": 0,
  "earmarked_balance": 0,
  "overdraft_limit": 0,
  "value_dated_balance": 0
}
```

2. When a bank or financial institution credits $100 to the account, the balances change.

```json
{
  "account_id": 1234,
  "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab",
  "program_id": 8674,
  "ledger_balance": 100,
  "book_balance": 100,
  "available_balance": 0,
  "credit_balance": 0,
  "debit_balance": 0,
  "uncleared_funds": 100,
  "earmarked_balance": 0,
  "overdraft_limit": 0,
  "value_dated_balance": 0
}
```

In the preceding example, the $100 credit is reflected as **book balance** and **uncleared funds**. Note that once the amount in uncleared funds is settled, the amount is reduced to 0.

On the other hand, if the bank decides to cancel the $100 credit after it has been issued, the bank initiates a cancellation request, and the balances revert to their original state.

```json
{
  "account_id": 1234,
  "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab",
  "program_id": 8674,
  "ledger_balance": 0,
  "book_balance": 0,
  "available_balance": 0,
  "credit_balance": 0,
  "debit_balance": 0,
  "uncleared_funds": 0,
  "earmarked_balance": 0,
  "overdraft_limit": 0,
  "value_dated_balance": 0
}
```

## Scenario 2: Debit

1. Start with the following account details, which represent an account with $100 in book balance, credit balance, and value-dated balance.

```json
{
  "account_id": 1234,
  "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab",
  "program_id": 8674,
  "ledger_balance": 100,
  "book_balance": 100,
  "available_balance": 100,
  "credit_balance": 100,
  "debit_balance": 0,
  "uncleared_funds": 0,
  "earmarked_balance": 0,
  "overdraft_limit": 0,
  "value_dated_balance": 100
}
```

2. When a debit is initiated using [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) with a specified future date in `payment_datetime`, the balances change as follows.

```json
{
  "account_id": 1234,
  "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab",
  "program_id": 8674,
  "leger_balance": -100,
  "book_balance": 0,
  "available_balance": 0,
  "credit_balance": 0,
  "debit_balance": 0,
  "uncleared_funds": -100,
  "earmarked_balance": 0,
  "overdraft_limit": 0,
  "value_dated_balance": 100
}
```

As shown above, the book balance and credit balance are reduced to 0, while `uncleared_funds` shows a negative value of $-100, indicating a pending debit. The `value_dated_balance` remains unchanged, as it awaits the specified date in `payment_datetime` to clear.

3. When the bank decides to clear the funds, a request to clear is sent, resulting in the following balances.

```json
{
  "account_id": 1234,
  "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab",
  "program_id": 8674,
  "ledger_balance": 0,
  "book_balance": 0,
  "available_balance": 0,
  "credit_balance": 0,
  "debit_balance": 0,
  "uncleared_funds": 0,
  "earmarked_balance": 0,
  "overdraft_limit": 0,
  "value_dated_balance": 0
}
```

In the account details, both `uncleared_funds` and `value_dated_balance` are reduced to 0.

# Custom processing codes

To use custom processing codes for future-dated payments, you must contact Pismo to create the necessary configurations for all environments to ensure proper functionality. Failure to do so can result in the following error:

```json
{ 
    "message": "Future dated payments only support default debit processing code",
    "code":"WPMT0005"
}
```
<!-- source:end -->

### Source 4: `docs/core-banking/back-value-dated-txns.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/back-value-dated-txns · updatedAt: 2026-05-04T15:53:20.000Z

<!-- source:begin path=docs/core-banking/back-value-dated-txns.md part=0-end -->

# Back-value-dated transactions

Back-value-dated transactions are essential for maintaining accurate account balances. They play a crucial role in adjusting account values to correct errors, provide timely compensation to customers, and meet regulatory requirements. By ensuring that the back-value-dated balance accurately reflects the correct payment date, even if the transaction was processed later, these transactions help maintain the integrity of financial records and ensure compliance with regulations.

# Objectives of back-value-dated transactions

Banks use back-value-dated transactions for the following reasons.

* **Correcting errors**: Banks use back-value-dated transactions to rectify processing mistakes by adjusting the funds to the correct date. For example, if a bank erroneously credits USD 100 to a customer's account on the 1st of the month, but the payment was actually made on the 15th of the previous month, the bank can back-value-date the funds to the 15th to ensure that the account balance is correct.
* **Customer compensation**: Banks sometimes back-value-date transactions to compensate customers for processing delays. For example, if a bank takes two weeks to process a payment, it might back-value-date the funds to the original payment date. This compensates the customer for the lost interest they would have earned if the funds had been available sooner.
* **Regulatory compliance**: Regulatory requirements might mandate that banks back-value-date transactions. For example, in the United States, banks are required to back-value-date funds if a processing error occurs to ensure that customer balances are accurate.

# How to post a back-value-dated transaction

Use the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) or the [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments) endpoint to post a back-value-dated transaction by setting the `payment_datetime` field to the past date.

After posting, balance history events are generated for all days affected by the balance adjustment. No clearing process is needed.

<Callout icon="📘" theme="info">
  **Notes**

  * If the administrative division of the account has the `skip_cycle_closing` parameter set to `true`, no balance history is sent on non-business days or holidays.
  * If the `deny_value_date` parameter is true and the `payment_datetime` falls on a non-business day or holiday, the transaction is denied.
  * For details about `skip_cycle_closing` and `deny_value_date`, refer to the [Parameters](https://developers.pismo.io/pismo-docs/docs/posting-transactions-on-holidays#parameters) section of *Posting transactions on holidays*.
  * Before performing back-value-dated transactions, ensure you check the number of days specified in the `retroactive_payment_time_restriction` field of [Create acceptance configuration by Org](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant). The transactions are processed based on the date you provided.
</Callout>

# Impact on account balances

When back-value-dated transactions occur, account balances are adjusted accordingly. This has the following results.

* The account balance is higher if funds received are back-value-dated.
* The account balance is lower if funds paid are back-value-dated.

This adjustment happens because the interest earned or owed on the account is **recalculated**, as the **value-dated balance is adjusted for a longer period of time**. This process is closely linked to the management of balance history and the bank's end-of-day procedures. The effects on various types of balances are detailed in the following table.

| Balance type        | Description                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ledger balance      | The ledger balance is the balance at the close of the business day, carried forward to the next business day. It is shown in statements as the **running balance** and is calculated as the book balance for the current date, plus any uncleared funds. When a transaction is back-value-dated, the ledger balance is adjusted online to reflect the back-value-dated credit or debit. |
| Available balance   | The available balance is the amount of money immediately accessible to the account holder. It’s used to validate new transactions. When a transaction is back-value-dated, the available balance is adjusted online to reflect the back-value-dated credit or debit.                                                                                                                    |
| Book balance        | The book balance is the total amount of money in the account, **excluding earmarked or hold funds and uncleared funds**. When a transaction is back-value-dated, the book balance is adjusted online to reflect the back-value-dated credit or debit.                                                                                                                                   |
| Value dated balance | Back-value-dated transactions affect the back-value-dated balance of the account for the past date when the transaction was posted. Subsequent balances must be recalculated according to the new back-value-dated balance from that day to the present. During this process, balance events are issued to indicate the adjustments or corrections.                                     |

## Examples

Here are some examples of how you use back-value-dated transactions in different scenarios.

| Scenario          | Description                                                                                                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Error correction  | A bank mistakenly debits USD 100 from a customer's account on August 15th. On August 16th, the bank corrects the error by back-value-dating the transaction to July 31st, adjusting the customer's balance accordingly. |
| Refund processing | A customer receives a USD 450 refund on May 30th. The bank processes the refund on June 7th with a back-value date of May 30th, compensating the customer for the processing delay.                                     |
| Compensation      | On September 15th, a bank compensates a customer USD 150 for an error made on August 1st by posting a payment backdated to August 1st.                                                                                  |
| Late settlement   | A bank receives a trade-related payment of USD 550,000 one day late on August 15th, instead of August 14th. The funds are credited and an interest claim is generated for the delay.                                    |

# Rules for performing a back-value-dated transaction

Here are the key rules to remember when you perform back-value-dated transactions.

| Rule                                    | Description                                                                                                                                                                                         |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configurable days                       | The number of days allowed for back-value-dated transactions can be configured in the payments settings.                                                                                            |
| Balance history events                  | Balance history events are generated for all days affected by the balance recalculations when you set `trigger_reason` to `BACK_VALUE_DATED_OPERATION` or `BACK_VALUE_DATED_OPERATION_CURRENT_DATE` |
| Calendar and holidays - cycle closing   | If `skip_cycle_closing` is `true`, no balance history is sent on non-business days or holidays.                                                                                                     |
| Calendar and holidays - deny value date | If `deny_value_date` is set to `true` and the `payment_datetime` is a non-business day or holiday, the transaction is denied.                                                                       |
| Custom rejection rules                  | If `reject_back_value_dating` is `true` and the provided `payment_datetime` back‑values the payment, the Pismo platform rejects the transaction.                                                    |
<!-- source:end -->

### Source 5: `docs/core-banking/future-value-dated-txns.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/future-value-dated-txns · updatedAt: 2026-05-04T15:50:00.000Z

<!-- source:begin path=docs/core-banking/future-value-dated-txns.md part=0-end -->

# Future-value-dated transactions

Future-value-dated transactions, are transactions that are scheduled to occur on a specific future date, meaning funds are only available when that date arrives. This type of transaction is useful for recurring payments, delayed payments, and other scenarios outlined in the  [Key benefits](#key-benefits) section.

To schedule a future-value-dated transaction, set a future date in the `payment_datetime` field of the  [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) or [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments) endpoint.  For more information, refer to the [Transaction process](#transaction-process)  section.

# Key benefits

Here are some key benefits of future-value-dated transactions.

| Benefit                | Description                                                                                                                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Cashflow planning      | Future-value-dated transactions enable better liquidity planning, ensuring that funds are available when needed. This helps customers manage their cashflow more efficiently.                                      |
| Contractual agreements | For contract-based transactions that require specifying a future payment date, such as financing agreements and leases, you can schedule these transactions for specific future dates as outlined in the contract. |
| Risk reduction         | Future-value-dated transactions can mitigate risks associated with currency and interest rate fluctuations by fixing the value date in the future, thus protecting against adverse market volatility.              |

## Use cases

The following are some possible use cases for future-value-dated transactions.

* **Foreign exchange**: You can initiate a foreign exchange transaction with a specified future date for clearing. This way, the book balance is adjusted on the future date, while the transaction is recorded immediately.
* **Escrow payments**: Escrow payments are typically predated. Although Pismo doesn’t manage the conditions for confirming escrow payments, you can schedule the operation with a future value date and confirm it according to your business requirements.

# Transaction process

Future-value-dated transactions are a two-stage process: posting and clearing.

## Posting

The transaction is first recorded in the system with a future payment date. In this stage, the following balance impacts are observed.

| Balance type            | Debit transactions | Credit transactions |
| ----------------------- | ------------------ | ------------------- |
| Uncleared funds balance | ✔                  | ✔                   |
| Ledger balance          | ✔                  | ✔                   |
| Available balance       | ✔                  | ✘                   |

## Clearing

When the payment date arrives, the transaction is finalized. The client can confirm the payment through the  [Confirm payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-confirm-payments) or the [Request bulk settlement](https://developers.pismo.io/pismo-docs/reference/post-bulk-settlement) endpoint. In this stage, the following balance impacts occur.

| Balance type        | Debit transactions | Credit transactions |
| ------------------- | ------------------ | ------------------- |
| Book balance        | ✔                  | ✔                   |
| Available balance   | ✘                  | ✔                   |
| Value-dated balance | ✔                  | ✔                   |

# Future-valued-dated transactions versus scheduled payments

Scheduled payment transactions are planned to occur on a specified future date. These transactions typically involve two steps: initial scheduling and execution on the scheduled date. Unlike future-value-dated payments, the availability of funds is not checked at the time of scheduling, nor are any balances affected. These checks and adjustments only take place on the scheduled date.

# Guidelines for future-value-dated transactions

Here are some guidelines to remember when you configure future-value-dated transactions.

| Parameters             | Guidelines                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configurable days      | By default, future-value-dated transactions are allowed for up to 10 days into the future.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Balance history events | Balance history events are not sent for future-value-dated transactions.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Holidays               | By default, future-value-dated transactions can occur on holidays. You can change this by setting `deny_value_date` to `true`. For more information about `deny_value_date`, refer to the [future-business-dated transaction](https://developers.pismo.io/pismo-docs/docs/posting-transactions-on-holidays#future-business-dated-transactions)  section in *Posting transactions on holidays*. For how to configure holidays, refer to  [Calendar and holidays in transaction banking](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-transaction-banking). |
| Custom rejection rules | If `reject_future_value_dating` is set to `true` and the `payment_datetime` places the payment on a future value date, the Pismo platform rejects the payment.                                                                                                                                                                                                                                                                                                                                     |
<!-- source:end -->

### Source 6: `docs/core-banking/channel-control-for-back-business-date-and-cutoff-exceptions.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/channel-control-for-back-business-date-and-cutoff-exceptions · updatedAt: 2026-04-16T19:35:25.000Z

<!-- source:begin path=docs/core-banking/channel-control-for-back-business-date-and-cutoff-exceptions.md part=0-end -->

# Channel control for back-business-date and cutoff exceptions

Channel control is a cash management feature that lets you define transaction posting rules based on a transaction’s channel, or origin. It allows you to configure exceptions to standard end‑of‑day (EOD) cutoff rules for specific channels, such as ATM, while transactions from all other channels follow standard cutoff processing.

You manage channels by creating or deleting them as needed. Each channel is assigned a unique code when it's created and that code can't be changed afterward. When you delete a channel, the Pismo platform keeps it in the historical record and marks it as inactive. Channels aren’t created automatically and must be explicitly set up by your organization.

## How channel control works

### Channel control extension to past-business-date toggle

The past-business-date toggle determines whether a transaction can use a business date other than the current date. Channel control extends this behavior with channel-based exceptions, letting you choose which channels may bypass cutoff restrictions.

When you configure the toggle with allowed channel codes, transactions submitted through an allowed channel may bypass cutoff restrictions. If you remove a channel from the allowed list, the Pismo platform rejects any new transactions that violate cutoff rules. If a transaction references a deleted or unknown channel, the Pismo platform returns a `4XX` validation error.

### Safeguards

Channels must exist before you can use them. If a toggle update includes an invalid channel, the Pismo platform rejects the request.

# Create channel control

## Endpoints

You can use the following channel control endpoints to create and delete channels.

| Endpoint                                           | Description                                                                                            |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [Create channel](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-channels)   | Establishes an operation block for a specific division.                                                |
| [Delete channel](https://developers.pismo.io/pismo-docs/reference/delete-corporate-v1-channels) | Deletes an existing channel. This operation prevents the channel from being used for new transactions. |

## Channel Rules

| Rule         | Description                                                                                                                                                                                                                               |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Immutability | The channel code cannot be changed.                                                                                                                                                                                                       |
| Deletion     | Channels are soft‑deleted. A hard delete permanently removes data from a database, making it unrecoverable without backups. A soft delete merely marks the data as inactive using a `deleted_at` flag, allowing it to be easily restored. |
| History      | Historical references are preserved.                                                                                                                                                                                                      |

# Channel‑based business date exceptions

You can configure channels that are exempt from business‑date cutoff rules or remove a channel from exemptions by using the <Anchor label="Past business date toggle " target="_blank" href="ref:put-back-business-toggle">Past business date toggle </Anchor>endpoint.

## Using channels in transactions

Transactions may include one of the following channel identifiers, which determines how business-date and cutoff rules are applied during validation.

| Scenario         | Behavior                                                                                                                               |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Channel provided | The transaction is validated using channel-specific rules, including any configured exemptions from business-date cutoff restrictions. |
| Channel omitted  | The transaction follows the legacy cutoff behavior, applying standard business-date validation with no channel-based exceptions.       |

Each transaction in a bulk request is validated independently. Clients can include a channel identifier on a transaction to apply channel-specific validation rules, including any cutoff exemptions. In bulk requests, clients can provide a channel identifier per transaction to apply channel-specific business-date and cutoff rules during validation.

## Common use cases

### Post transactions after cutoff

On the Pismo platform, channel control defines the rules that determine which actions are allowed through each access channel, under which conditions, and within which limits. In some cases, a client may need to bypass specific rules, such as cutoff restrictions. This feature enables that behavior.

For example, a client may allow transactions from the ATM channel. Because ATM transactions can arrive after the cutoff date using a back business date, the Pismo platform accepts the request. Transactions from any other channels that are not explicitly allowed remain restricted.

### Remove a previously allowed channel

If the client removes the ATM channel from the exception list, any new ATM transactions violating cutoff rules are rejected.

### Bulk payments with mixed channels

When a bulk file includes entries with and without a channel:

* Entries with a valid channel follow exception rules.

* Entries without a channel follow standard cutoff behavior.

* Each entry is evaluated independently.

# Channel events

The Pismo platform emits the following events, which you can use to manage channel creation and update descriptions as needed.

* <Anchor label="Channel created, updated, or deleted" target="_blank" href="https://developers.pismo.io/events/docs/cash-management-channel-1">Channel created, updated, or deleted</Anchor>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /bank-statements/v1/account-balances/history/config` | `post-account-balance-history-configuration` | Create account balance history config v1 | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `PATCH /bank-statements/v1/account-balances/history/config/{divisionCode}` | `patch-account-balances-history-configuration` | Update account balance history config v1 | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `POST /corporate/v2/payments` | `corporate-v2-post-payments` | Post payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `POST /corporate/v2/payments/multileg` | `corporate-v2-post-multileg-payments` | Post multi-leg payment (deprecated) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-03 |
| `POST /v1/acceptance/processing-code/{processingCode}` | `post-acceptance-by-tenant` | Create limit acceptance config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-acceptance-configurations |
| `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `post-acceptance-by-tenant` | Create org acceptance configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-acceptances |
| `POST /corporate/v2/payments/confirm` | `corporate-v2-post-confirm-payments` | Confirm payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `POST /corporate/v1/bulk-settlement` | `post-bulk-settlement` | Request bulk settlement | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-settlement |
| `POST /corporate/v1/channels` | `post-corporate-v1-channels` | Create channel | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--channels |
| `DELETE /corporate/v1/channels/{channel}` | `delete-corporate-v1-channels` | Delete channel | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--channels |

### Operation essentials

- **`POST /bank-statements/v1/account-balances/history/config`** (`post-account-balance-history-configuration`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `cycle_closing_time`, `cycle_event_delay`; response statuses 201, 400, 404, 409, 500; error codes in examples `WCFG0002`, `WCFG0001`, `WCFG0003`, `WCFG0004`, `ECMN9999`; events `account-balances-balance-history-config-creation-1`.
- **`PATCH /bank-statements/v1/account-balances/history/config/{divisionCode}`** (`patch-account-balances-history-configuration`): security `BearerAuth`; required parameters `divisionCode` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `WCFG0002`, `WCFG0001`, `WCFG0003`, `WCFG0005`, `ECMN9999`; events `account-balances-balance-history-config-change-1`.
- **`POST /corporate/v2/payments`** (`corporate-v2-post-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`; response statuses 201, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WPMT0017`, `WPMT0011`, `WPMT0053`, `WPMT0018`, `WPMT0029`, `WPMT0030`, `WPMT0031`, `WPMT0062`, `WPMT0063`, `WCAC0010`, `WPMT0001`, `WPMT0061`, `WPMT0015`, `WPMT0016`, `WPMT0003`, `WPMT0004`, `WPMT0005`, `WPMT0006`, `WPMT0009`, `WPMT0010`, `WPMT0021`, `WEAM0008`, `WEAM0006`, `WPMT0050`, `WEAM0017`, `WEAM0019`, `WPMT0022`, `WPMT0023`, `WPMT0024`, `WPMT0025`, `WPMT0026`, `WCMN0002`, `WPMT0028`, `WPMT0045`, `WPMT0049`, `WPMT0036`, `WPMT0044`, `WPMT0051`, `WPMT0035`, `WPMT0046`, `WPMT0054`, `WPMT0055`, `WPMT0056`, `WPMT0058`, `WPMT0008`, `WPMT0014`, `WPMT0019`, `WCAC0002`, `WCAC0012`, `WPMT0002`, `WCAC0001`, `WEAM0007`, `WPMT0007`, `WPMT0052`, `WEAM0049`, `WPMT0047`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`POST /corporate/v2/payments/multileg`** (`corporate-v2-post-multileg-payments`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`; response statuses 202, 400, 403, 500; error codes in examples `WMLP0001`, `WMLP0002`, `WMLP0003`, `WMLP0004`, `WMLP0006`, `WMLP0005`, `WMLP1026`, `WMLP1028`, `WMLP1027`, `WMLP1002`, `WMLP1003`, `WMLP1004`, `WMLP1005`, `WMLP1039`, `WMLP1006`, `WMLP1022`, `WMLP1007`, `WMLP1008`, `WMLP1009`, `WMLP1010`, `WMLP1011`, `WMLP1013`, `WMLP1014`, `WMLP1015`, `WMLP1016`, `WMLP1017`, `WMLP1019`, `WMLP1048`, `WMLP1023`, `WMLP1036`, `WMLP1034`, `WMLP1035`, `WMLP1024`, `WMLP1037`, `WMLP1038`, `WMLP1030`, `WMLP1041`, `WMLP1042`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `corporate-multi-leg-creation-1`, `corporate-multi-leg-status-change-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`POST /v1/acceptance/processing-code/{processingCode}`** (`post-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}`** (`post-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /corporate/v2/payments/confirm`** (`corporate-v2-post-confirm-payments`): security `BearerAuth`; required parameters none declared; required body fields `original_tracking_id`, `tracking_id`; response statuses 201, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WPMT0017`, `WPMT0018`, `WPMT0001`, `WPMT0061`, `WPMT0003`, `WPMT0004`, `WPMT0028`, `WPMT0038`, `WPMT0039`, `WPMT0044`, `WPMT0049`, `WCAC0001`, `WPMT0037`, `WPMT0007`, `WPMT0052`, `WPMT0047`, `WPMT0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `platform-authorization-platform-authorization-1`.
- **`POST /corporate/v1/bulk-settlement`** (`post-bulk-settlement`): security `BearerAuth`; required parameters none declared; required body fields `operation_type`, `settlement_date`, `division_code`, `bulk_id`; response statuses 202, 400, 401, 403, 409, 429, 500; error codes in examples `WSTM0001`, `WSTM0002`, `WSTM0003`, `WSTM0004`, `WSTM0005`, `WSTM0006`, `WSTM0010`, `WSTM0011`, `WSTM0007`, `WSTM0009`, `WSTM0008`, `ECMN9999`; events none listed.
- **`POST /corporate/v1/channels`** (`post-corporate-v1-channels`): security `BearerAuth`; required parameters none declared; required body fields `channel`; response statuses 201, 400, 401, 403, 409, 500; error codes in examples `WCCL0001`, `WCCL0002`, `WCCL0003`, `ECMN9999`; events `cash-management-channel-1`.
- **`DELETE /corporate/v1/channels/{channel}`** (`delete-corporate-v1-channels`): security `BearerAuth`; required parameters `channel` (path); required body fields none declared; response statuses 204, 400, 401, 403, 404, 500; error codes in examples `WCCL0005`, `WCCL0004`, `ECMN9999`; events `cash-management-channel-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-v2-post-confirm-payments` | `account-balances-balance-change-1` |
| `corporate-v2-post-multileg-payments` | `account-balances-balance-change-1` |
| `corporate-v2-post-payments` | `account-balances-balance-change-1` |
| `patch-account-balances-history-configuration` | `account-balances-balance-history-config-change-1` |
| `post-account-balance-history-configuration` | `account-balances-balance-history-config-creation-1` |
| `corporate-v2-post-multileg-payments` | `accounting-entry-creation-1` |
| `corporate-v2-post-payments` | `accounting-entry-creation-1` |
| `corporate-v2-post-confirm-payments` | `availables-change-available-1` |
| `corporate-v2-post-multileg-payments` | `availables-change-available-1` |
| `corporate-v2-post-payments` | `availables-change-available-1` |
| `delete-corporate-v1-channels` | `cash-management-channel-1` |
| `post-corporate-v1-channels` | `cash-management-channel-1` |
| `corporate-v2-post-multileg-payments` | `corporate-multi-leg-creation-1` |
| `corporate-v2-post-multileg-payments` | `corporate-multi-leg-status-change-1` |
| `corporate-v2-post-confirm-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-multileg-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-multileg-payments` | `rules-evaluation-requested-1` |
| `corporate-v2-post-payments` | `rules-evaluation-requested-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `cash-management-channel-1` | cash | 1 | https://developers.pismo.io/events/docs/cash-management-channel-1 | 3 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/biz-dated-txns.md`: updatedAt 2026-04-24T21:59:18.000Z.
- `docs/core-banking/back-biz-dated-txns.md`: updatedAt 2026-04-24T21:59:18.000Z.
- `docs/core-banking/future-biz-dated-txns.md`: updatedAt 2026-04-24T21:59:18.000Z.
- `docs/core-banking/back-value-dated-txns.md`: updatedAt 2026-05-04T15:53:20.000Z.
- `docs/core-banking/future-value-dated-txns.md`: updatedAt 2026-05-04T15:50:00.000Z.
- `docs/core-banking/channel-control-for-back-business-date-and-cutoff-exceptions.md`: updatedAt 2026-04-16T19:35:25.000Z.
- Links to `corporate-v2-post-multileg-payments`, which is marked `deprecated: true` in `api-specs/Banking_-_Transaction_banking.yaml`.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/biz-dated-txns.md` | whole document | https://developers.pismo.io/pismo-docs/docs/biz-dated-txns | `15e29b77ff15822e…` | 2026-04-24T21:59:18.000Z |
| `docs/core-banking/back-biz-dated-txns.md` | whole document | https://developers.pismo.io/pismo-docs/docs/back-biz-dated-txns | `5c581152fb4fb029…` | 2026-04-24T21:59:18.000Z |
| `docs/core-banking/future-biz-dated-txns.md` | whole document | https://developers.pismo.io/pismo-docs/docs/future-biz-dated-txns | `e5282d034fedfce4…` | 2026-04-24T21:59:18.000Z |
| `docs/core-banking/back-value-dated-txns.md` | whole document | https://developers.pismo.io/pismo-docs/docs/back-value-dated-txns | `cd8cdca1a43e627b…` | 2026-05-04T15:53:20.000Z |
| `docs/core-banking/future-value-dated-txns.md` | whole document | https://developers.pismo.io/pismo-docs/docs/future-value-dated-txns | `839de48196c85ae3…` | 2026-05-04T15:50:00.000Z |
| `docs/core-banking/channel-control-for-back-business-date-and-cutoff-exceptions.md` | whole document | https://developers.pismo.io/pismo-docs/docs/channel-control-for-back-business-date-and-cutoff-exceptions | `dd70b4e49a5607a2…` | 2026-04-16T19:35:25.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--bulk-settlement` — API reference: Banking - Transaction banking — Bulk settlement
- `KU-API-banking-transaction-banking--channels` — API reference: Banking - Transaction banking — Channels
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-core-platform-balance-watcher--limit-acceptance-configurations` — API reference: Core platform - Balance watcher — Limit acceptance configurations
- `KU-API-core-platform-payment-configurations--payment-method-acceptances` — API reference: Core platform - Payment configurations — Payment method acceptances
- `KU-BANK-calendars-and-holidays` — Calendars, holidays and posting transactions on holidays in transaction banking
- `KU-BANK-dormancy` — Dormancy and dormancy reactivation exceptions
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
