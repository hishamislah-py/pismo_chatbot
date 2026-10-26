---
ku_id: KU-CRED-delinquency-buckets
title: Delinquency buckets
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/delinquency-buckets.md
  sha256: 8e1374410f440969cdce597ce41beffce4d448c04c71bad3f40ff3c5e3500b68
  url: https://developers.pismo.io/pismo-docs/docs/delinquency-buckets
  role: primary_guide
  updated_at: '2026-06-04T14:22:22.000Z'
operations:
- getdelinquencybuckets
- listdelinquencybuckets
- updateProgramParamenter
related_kus:
- KU-API-revolving-credit-delinquency--delinquency
- KU-API-revolving-credit-statements--multivalue-program-parameters
grouping_rationale: single source page
---

# Delinquency buckets

**KU ID:** `KU-CRED-delinquency-buckets` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/delinquency-buckets.md`:

> In credit terms, an **overdue amount** refers to the unpaid amount (after the real due date) that a customer owes if they paid less than the minimum amount due (MAD) on their last closed statement. In addition, if the  customer keeps doing this—paying less than MAD over and over—their overdue amount continues to increase due to interest accruals and probably fines/fees.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/delinquency-buckets.md`: Delinquency buckets; Configuring delinquency buckets; Example; Delinquency bucket API endpoints; Delinquency bucket events

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/delinquency-buckets.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/delinquency-buckets · updatedAt: 2026-06-04T14:22:22.000Z

<!-- source:begin path=docs/card-issuing/delinquency-buckets.md part=0-end -->

# Delinquency buckets

In credit terms, an **overdue amount** refers to the unpaid amount (after the real due date) that a customer owes if they paid less than the minimum amount due (MAD) on their last closed statement. In addition, if the  customer keeps doing this—paying less than MAD over and over—their overdue amount continues to increase due to interest accruals and probably fines/fees.

Credit card issuers are often only concerned with the total overdue amount. In some countries, however, regulations require **delinquency buckets**, which categorize overdue amounts by billing cycle.

# Configuring delinquency buckets

To configure delinquency buckets for your program, use the [Update multivalue program parameter values](https://developers.pismo.io/pismo-docs/reference/updateprogramparamenter)  endpoint to set the program parameter `DELINQUENCY_BUCKETS_PAYMENTS_TRANSACTIONS_TYPES` to an array of transaction type IDs. These IDs specify the acceptable transaction types for discharging a delinquency bucket balance.

## Example

Suppose a statement closes on the 10th day of each month and the due date is the 15th. To keep it simple, assume this is the real due date. Also, assume that the ID for the purchase transaction type is included in the `DELINQUENCY_BUCKETS_PAYMENTS_TRANSACTIONS_TYPES` array.

Suppose that, after two cycles, the following scenario occurs.

<Callout icon="📘" theme="info">
  In the following tables, the date format is MM/DD/YY (month/day/year).
</Callout>

**Transactions for Cycle 3 - February 16th**

| Transaction ID | Amount  | Balance | Transaction type | Event date | Cycle |
| :------------- | :------ | :------ | :--------------- | :--------- | :---- |
| 20             | $700.00 | $665.00 | Purchase         | 1/13/22    | 2     |
| 21             | $350.00 | $350.00 | Purchase         | 1/13/22    | 2     |
| 22             | $35.00  | $0.00   | Payment          | 2/15/22    | 3     |
| 23             | $100.00 | $100.00 | Purchase         | 2/16/22    | 3     |
| 24             | $200.00 | $200.00 | Purchase         | 2/16/22    | 3     |
| 25             | $27.21  | $27.21  | Interest         | 2/16/22    | 3     |

**Statement:** (Key: C = Cycle, OA=Overdue amount, DA=Delinquent amount)

<Table align={["left","left","left","left","left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        C
      </th>

      <th>
        Previous

        balance
      </th>

      <th>
        Debits
      </th>

      <th>
        Credits
      </th>

      <th>
        Balance
      </th>

      <th>
        MAD
      </th>

      <th>
        Closing date
      </th>

      <th>
        Due

        Date
      </th>

      <th>
        OA
      </th>

      <th>
        DA
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        $0
      </td>

      <td>
        $1,050
      </td>

      <td>
        $0
      </td>

      <td>
        $1,050
      </td>

      <td>
        $52.50
      </td>

      <td>
        1/10/22
      </td>

      <td>
        1/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        $1,050
      </td>

      <td>
        $700
      </td>

      <td>
        $1,050
      </td>

      <td>
        $700
      </td>

      <td>
        $35
      </td>

      <td>
        2/10/22
      </td>

      <td>
        2/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        $700
      </td>

      <td>
        $327.21
      </td>

      <td>
        $35.00
      </td>

      <td>
        $992.21
      </td>

      <td>
        $49.61
      </td>

      <td>
        3/10/22
      </td>

      <td>
        3/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>
  </tbody>
</Table>

**Transactions for Cycle 4 - March 16**

| Transaction ID | Amount  | Balance | Transaction type | Event date | Cycle |
| :------------- | :------ | :------ | :--------------- | :--------- | :---- |
| 23             | $100.00 | $100.00 | Purchase         | 2/16/22    | 3     |
| 24             | $200.00 | $200.00 | Purchase         | 2/16/22    | 3     |
| 25             | $27.21  | $27.21  | Interest         | 2/16/22    | 3     |
| 26             | $0.00   | $0.00   | Payment          | 3/15/22    | 3     |
| 27             | $100.00 | $100.00 | Purchase         | 3/16/22    | 4     |
| 28             | $31.53  | $31.53  | Interest         | 3/16/22    | 4     |
| 29             | $25.00  | $25.00  | Late Fee         | 3/16/22    | 4     |

**Statement** (Key: C = Cycle, OA=Overdue amount, DA=Delinquent amount)

<Table align={["left","left","left","left","left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        C
      </th>

      <th>
        Previous

        balance
      </th>

      <th>
        Debits
      </th>

      <th>
        Credits
      </th>

      <th>
        Balance
      </th>

      <th>
        MAD
      </th>

      <th>
        Closing Date
      </th>

      <th>
        Due

        Date
      </th>

      <th>
        OA
      </th>

      <th>
        DA
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        $0
      </td>

      <td>
        $1,050
      </td>

      <td>
        $0
      </td>

      <td>
        $1,050
      </td>

      <td>
        $52.50
      </td>

      <td>
        1/20/22
      </td>

      <td>
        1/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        $1,050
      </td>

      <td>
        $700
      </td>

      <td>
        $1,050
      </td>

      <td>
        $700
      </td>

      <td>
        $35
      </td>

      <td>
        10/2/22
      </td>

      <td>
        2/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        $700
      </td>

      <td>
        $327.21
      </td>

      <td>
        $35
      </td>

      <td>
        $992.21
      </td>

      <td>
        $49.61
      </td>

      <td>
        10/3/22
      </td>

      <td>
        3/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        $992.21
      </td>

      <td>
        $156.53
      </td>

      <td>
        $0
      </td>

      <td>
        $1,148.74
      </td>

      <td>
        $104.57
      </td>

      <td>
        10/4/22
      </td>

      <td>
        4/15/22
      </td>

      <td>
        $49.61
      </td>

      <td>
        $49.61
      </td>
    </tr>
  </tbody>
</Table>

The due date for cycle 1 was in cycle 2 and the customer fully paid the amount due, so the overdue amount and delinquency bucket for cycle 2 are zero.

On the due date for cycle 2 (which was in cycle 3) the MAD was $35.00. The customer paid exactly that amount, so the overdue amount and delinquency bucket for cycle 3 are zero.

At cycle 4 however, customer finances seem to run out of control. The cycle 3 due date has come and its MAD amount is $49.61. This time, the customer does not pay anything. Now, the customer has an overdue amount of $49.61 and the first greater than zero delinquency bucket—also $49.61.

In cycle 5, the cycle 4 closed statement due date occurs, and the corresponding MAD is $104.57. Once more, the customer does not pay any amount, so their updated overdue amount is $104.57. Part of it is the $49.61 delinquency bucket for cycle 4. Another part of it is exactly the difference between the total overdue amount and the previous delinquency bucket, that is, the delinquency bucket for cycle 5 is $54.96.

**Transactions for Cycle 5 - April 16**

| Transaction ID | Amount  | Balance | Transaction type | Event date | Cycle |
| :------------- | :------ | :------ | :--------------- | :--------- | :---- |
| 27             | $100.00 | $100.00 | Purchase         | 3/16/22    | 4     |
| 28             | $31.53  | $31.53  | Interest         | 3/16/22    | 4     |
| 29             | $25.00  | $25.00  | Late Fee         | 3/16/22    | 4     |
| 30             | $0.00   | $0.00   | Payment          | 4/15/22    | 5     |
| 31             | $35.12  | $35.12  | Interest         | 4/16/22    | 5     |
| 32             | $25.00  | $25.00  | Late Fee         | 4/16/22    | 5     |

**Statement**  (Key: C = Cycle, OA=Overdue amount, DA=Delinquent amount)

<Table align={["left","left","left","left","left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        C
      </th>

      <th>
        Previous

        balance
      </th>

      <th>
        Debits
      </th>

      <th>
        Credits
      </th>

      <th>
        Balance
      </th>

      <th>
        MAD
      </th>

      <th>
        Closing

        Date
      </th>

      <th>
        Due

        Date
      </th>

      <th>
        OA
      </th>

      <th>
        DA
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        $0
      </td>

      <td>
        $1,050
      </td>

      <td>
        $0
      </td>

      <td>
        $1,050
      </td>

      <td>
        $52.50
      </td>

      <td>
        1/10/22
      </td>

      <td>
        1/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        $1,050
      </td>

      <td>
        $700
      </td>

      <td>
        $1,050
      </td>

      <td>
        $700
      </td>

      <td>
        $35
      </td>

      <td>
        2/10/22
      </td>

      <td>
        2/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        $700
      </td>

      <td>
        $327.21
      </td>

      <td>
        $35
      </td>

      <td>
        $992.21
      </td>

      <td>
        $49.61
      </td>

      <td>
        3/10/22
      </td>

      <td>
        3/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        $992.21
      </td>

      <td>
        $156.53
      </td>

      <td>
        $0
      </td>

      <td>
        $1,148.74
      </td>

      <td>
        $104.57
      </td>

      <td>
        4/10/22
      </td>

      <td>
        4/15/22
      </td>

      <td>
        $49.61
      </td>

      <td>
        $49.61
      </td>
    </tr>

    <tr>
      <td>
        5
      </td>

      <td>
        $1,148.74
      </td>

      <td>
        $60.12
      </td>

      <td>
        $0
      </td>

      <td>
        $1.208.86
      </td>

      <td>
        $168.20
      </td>

      <td>
        5/10/22
      </td>

      <td>
        5/15/22
      </td>

      <td>
        $104.57
      </td>

      <td>
        $54.96
      </td>
    </tr>
  </tbody>
</Table>

Notice that the total overdue amount is equal to $104.57, composed of two delinquency buckets—$49.61 (cycle 4) and $54.96 (cycle 5).

As with cycles 4 and 5, the customer made no payment for cycle 6  which led them to an updated overdue amount of $168.20, out of which, $63.63 corresponds to the cycle 6 delinquency bucket and the remaining amount as previously summarized.

So this is the current state:

**Transactions for Cycle 6 - May 16**

| Transaction ID | Amount | Balance | Transaction type | Event date | Cycle |
| :------------- | :----- | :------ | :--------------- | :--------- | :---- |
| 31             | $35.12 | $35.12  | Interest         | 4/16/22    | 5     |
| 32             | $25.00 | $25.00  | Late Fee         | 4/16/22    | 5     |
| 33             | $0.00  | $0.00   | Payment          | 5/15/22    | 6     |
| 34             | $36.96 | $36.96  | Interest         | 5/16/22    | 6     |
| 35             | $25.00 | $25.00  | Late Fee         | 5/16/22    | 6     |

**Statement**  (Key: C = Cycle, OA=Overdue amount, DA=Delinquent amount)

<Table align={["left","left","left","left","left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        C
      </th>

      <th>
        Previous

        balance
      </th>

      <th>
        Debits
      </th>

      <th>
        Credits
      </th>

      <th>
        Balance
      </th>

      <th>
        MAD
      </th>

      <th>
        Closing

        Date
      </th>

      <th>
        Due

        Date
      </th>

      <th>
        OA
      </th>

      <th>
        DA
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        $0
      </td>

      <td>
        $1,050
      </td>

      <td>
        $0
      </td>

      <td>
        $1,050
      </td>

      <td>
        $52.50
      </td>

      <td>
        1/10/22
      </td>

      <td>
        1/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        $1,050
      </td>

      <td>
        $700
      </td>

      <td>
        $1,050
      </td>

      <td>
        $700
      </td>

      <td>
        $35
      </td>

      <td>
        2/10/22
      </td>

      <td>
        2/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        $700
      </td>

      <td>
        $327.21
      </td>

      <td>
        $35
      </td>

      <td>
        $992.21
      </td>

      <td>
        $49.61
      </td>

      <td>
        3/10/22
      </td>

      <td>
        3/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        $992.21
      </td>

      <td>
        $156.53
      </td>

      <td>
        $0
      </td>

      <td>
        $1,148.74
      </td>

      <td>
        $104.57
      </td>

      <td>
        4/10/22
      </td>

      <td>
        4/15/22
      </td>

      <td>
        $49.61
      </td>

      <td>
        $49.61
      </td>
    </tr>

    <tr>
      <td>
        5
      </td>

      <td>
        $1,148.74
      </td>

      <td>
        $60.12
      </td>

      <td>
        $0
      </td>

      <td>
        $1.208.86
      </td>

      <td>
        $168.20
      </td>

      <td>
        5/10/22
      </td>

      <td>
        5/15/22
      </td>

      <td>
        $104.57
      </td>

      <td>
        $54.97
      </td>
    </tr>

    <tr>
      <td>
        6
      </td>

      <td>
        $1,208.86
      </td>

      <td>
        $61.96
      </td>

      <td>
        $0
      </td>

      <td>
        $1,270.82
      </td>

      <td>
        $282.19
      </td>

      <td>
        6/10/22
      </td>

      <td>
        6/15/22
      </td>

      <td>
        $168.20
      </td>

      <td>
        $63.63
      </td>
    </tr>
  </tbody>
</Table>

In cycle 7 something new happens, the customer pays an amount that matches precisely the first greater than zero delinquency bucket (cycle 4, $49.61). As a result, that delinquency bucket is fully cleared and the current one is calculated as follows: the overdue amount minus the sum of previous non-cleared delinquency buckets’ amounts. Customer payments must clear delinquency buckets from oldest to newest.

**Transactions for Cycle 7 - June 16**

| Transaction ID | Amount | Balance | Transaction type | Event date | Cycle |
| :------------- | :----- | :------ | :--------------- | :--------- | :---- |
| 34             | $36.96 | $36.96  | Interest         | 5/16/22    | 6     |
| 35             | $25.00 | $25.00  | Late Fee         | 5/16/22    | 6     |
| 36             | $49.61 | $0.00   | Payment          | 5/15/22    | 7     |
| 37             | $37.36 | $37.36  | Interest         | 5/16/22    | 7     |
| 38             | $25.00 | $25.00  | Late Fee         | 5/16/22    | 7     |

**Statement**  (Key: C = Cycle, OA=Overdue amount, DA=Delinquent amount)

<Table align={["left","left","left","left","left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        C
      </th>

      <th>
        Previous

        balance
      </th>

      <th>
        Debits
      </th>

      <th>
        Credits
      </th>

      <th>
        Balance
      </th>

      <th>
        MAD
      </th>

      <th>
        Closing

        Date
      </th>

      <th>
        Due

        Date
      </th>

      <th>
        OA
      </th>

      <th>
        DA
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        $0
      </td>

      <td>
        $1,050
      </td>

      <td>
        $0
      </td>

      <td>
        $1,050
      </td>

      <td>
        $52.50
      </td>

      <td>
        1/10/22
      </td>

      <td>
        1/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        $1,050
      </td>

      <td>
        $700
      </td>

      <td>
        $1,050
      </td>

      <td>
        $700
      </td>

      <td>
        $35
      </td>

      <td>
        2/10/22
      </td>

      <td>
        2/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        $700
      </td>

      <td>
        $327.21
      </td>

      <td>
        $35
      </td>

      <td>
        $992.21
      </td>

      <td>
        $49.61
      </td>

      <td>
        3/10/22
      </td>

      <td>
        3/15/22
      </td>

      <td>
        $0
      </td>

      <td>
        $0
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        $992.21
      </td>

      <td>
        $156.53
      </td>

      <td>
        $0
      </td>

      <td>
        $1,148.74
      </td>

      <td>
        $104.57
      </td>

      <td>
        4/10/22
      </td>

      <td>
        4/15/22
      </td>

      <td>
        $49.61
      </td>

      <td>
        $49.61
      </td>
    </tr>

    <tr>
      <td>
        5
      </td>

      <td>
        $1,148.74
      </td>

      <td>
        $60.12
      </td>

      <td>
        $0
      </td>

      <td>
        $1.208.86
      </td>

      <td>
        $168.20
      </td>

      <td>
        5/10/22
      </td>

      <td>
        5/15/22
      </td>

      <td>
        $104.57
      </td>

      <td>
        $54.97
      </td>
    </tr>

    <tr>
      <td>
        6
      </td>

      <td>
        $1,208.86
      </td>

      <td>
        $61.96
      </td>

      <td>
        $0
      </td>

      <td>
        $1,270.82
      </td>

      <td>
        $282.19
      </td>

      <td>
        6/10/22
      </td>

      <td>
        6/15/22
      </td>

      <td>
        $168.20
      </td>

      <td>
        $63.63
      </td>
    </tr>

    <tr>
      <td>
        7
      </td>

      <td>
        $1,270.82
      </td>

      <td>
        $62.36
      </td>

      <td>
        $49.61
      </td>

      <td>
        $1,283.57
      </td>

      <td>
        $344.37
      </td>

      <td>
        7/10/22
      </td>

      <td>
        7/15/22
      </td>

      <td>
        $232.58
      </td>

      <td>
        $113.98
      </td>
    </tr>
  </tbody>
</Table>

In conclusion, delinquency buckets are only for the issuer to follow up on the existing overdue amounts and are meant to be completely transparent to account holders, unless the platform customer wants to make them visible or is obligated to do so by regulations.

# Delinquency bucket API endpoints

* [Get delinquency bucket](https://developers.pismo.io/pismo-docs/reference/getdelinquencybuckets)
* [List delinquency buckets](https://developers.pismo.io/pismo-docs/reference/listdelinquencybuckets)

# Delinquency bucket events

Delinquency buckets are automatically created and updated, there are no endpoints for doing that.

* [Delinquency bucket created](https://developers.pismo.io/events/docs/balance-statements-delinquency-bucket-created-1)
* [Delinquency bucket updated](https://developers.pismo.io/events/docs/balance-statements-delinquency-bucket-updated-1)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}` | `updateProgramParamenter` | Update multivalue program parameter values | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--multivalue-program-parameters |
| `GET /v1/accounts/{accountId}/buckets/{delinquencyBucketId}` | `getdelinquencybuckets` | Get delinquency bucket | `api-specs/Revolving_credit_-_Delinquency.yaml` | no | KU-API-revolving-credit-delinquency--delinquency |
| `GET /v1/accounts/{accountId}/buckets` | `listdelinquencybuckets` | List delinquency buckets | `api-specs/Revolving_credit_-_Delinquency.yaml` | no | KU-API-revolving-credit-delinquency--delinquency |

### Operation essentials

- **`PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}`** (`updateProgramParamenter`): security `BearerAuth`; required parameters `programId` (path), `parameterId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `CE0001`, `GN0001`; events none listed.
- **`GET /v1/accounts/{accountId}/buckets/{delinquencyBucketId}`** (`getdelinquencybuckets`): security `BearerAuth`; required parameters `accountId` (path), `delinquencyBucketId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.
- **`GET /v1/accounts/{accountId}/buckets`** (`listdelinquencybuckets`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.

## Lifecycle status

- `docs/card-issuing/delinquency-buckets.md`: updatedAt 2026-06-04T14:22:22.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/delinquency-buckets.md` | whole document | https://developers.pismo.io/pismo-docs/docs/delinquency-buckets | `8e1374410f440969…` | 2026-06-04T14:22:22.000Z |

## Related knowledge units

- `KU-API-revolving-credit-delinquency--delinquency` — API reference: Revolving credit - Delinquency — Delinquency
- `KU-API-revolving-credit-statements--multivalue-program-parameters` — API reference: Revolving credit - Statements — Multivalue program parameters
