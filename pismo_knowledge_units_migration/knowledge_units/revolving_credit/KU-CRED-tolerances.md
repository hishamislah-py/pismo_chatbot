---
ku_id: KU-CRED-tolerances
title: Overdue tolerance and payment tolerance
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/overdue-tolerance.md
  sha256: 683d264be35f12bee496d49aa9544135aceda0213204c1f7648dc85de4a15d77
  url: https://developers.pismo.io/pismo-docs/docs/overdue-tolerance
  role: primary_guide
  updated_at: '2026-03-20T19:57:11.000Z'
- path: docs/card-issuing/payment-tolerance.md
  sha256: e94a55682d958c40a36d0120527e83dec4d74a5682aa4bc449dbc3a47eafc95e
  url: https://developers.pismo.io/pismo-docs/docs/payment-tolerance
  role: primary_guide
  updated_at: '2026-03-19T12:47:50.000Z'
operations: []
related_kus:
- KU-CC-get-started-control-center
- KU-CRED-calculating-interest-accruals
grouping_rationale: Two tolerance mechanisms.
---

# Overdue tolerance and payment tolerance

**KU ID:** `KU-CRED-tolerances` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Two tolerance mechanisms.

Scope as stated in `docs/card-issuing/overdue-tolerance.md`:

> By default, an account becomes overdue if the minimum amount due (MAD) is not paid by the due date. The **overdue tolerance** feature enables you to set up additional rules that tell the Pismo platform to ignore overdue amounts if they fall within a tolerance range. In other words, if the overdue amount is within a specific range, the platform does not consider the account to be overdue, and overdue charges are not applied.

Scope as stated in `docs/card-issuing/payment-tolerance.md`:

> By default, an account with an unpaid balance accrues interest according to the rules laid out in [Calculating interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals). The **payment tolerance** feature enables you to set up additional rules to specify that an account should not accrue interest if the outstanding balance is less than a certain amount.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/overdue-tolerance.md`: Overdue tolerance; Examples; Example 1; Example 2; Example 3; Example 4; Example 5
- `docs/card-issuing/payment-tolerance.md`: Payment tolerance; Examples; Example 1; Example 2

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/overdue-tolerance.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/overdue-tolerance · updatedAt: 2026-03-20T19:57:11.000Z

<!-- source:begin path=docs/card-issuing/overdue-tolerance.md part=0-end -->

# Overdue tolerance

By default, an account becomes overdue if the minimum amount due (MAD) is not paid by the due date. The **overdue tolerance** feature enables you to set up additional rules that tell the Pismo platform to ignore overdue amounts if they fall within a tolerance range. In other words, if the overdue amount is within a specific range, the platform does not consider the account to be overdue, and overdue charges are not applied.

To configure overdue tolerance, set the following program parameters.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter name
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Overdue tolerance percentage**
      </td>

      <td>
        A percentage of the overdue amount that is used by the **Overdue tolerance method** to determine if the account should be considered overdue. Must be greater than 0 and less than or equal to 100.
      </td>
    </tr>

    <tr>
      <td>
        **Overdue tolerance amount**
      </td>

      <td>
        A fixed amount that is used by the **Overdue tolerance method** to determine if the account should be considered overdue. For example, $70.
      </td>
    </tr>

    <tr>
      <td>
        **Overdue tolerance method**
      </td>

      <td>
        The method to apply:

        * *0* — Do not use.
        * *1* — Maximum value. Between the **Overdue tolerance amount** and (MAD x **Overdue tolerance percentage**), use whichever value is greater. If the difference between the payment and the overdue amount is less than or equal to this value, the account is not considered overdue.
        * *2* — Minimum  value. Between the **Overdue tolerance amount** and (MAD x **Overdue tolerance percentage**), use whichever value is lower. If the difference between the payment and the overdue amount is less than or equal to this value, the account is not considered overdue.
      </td>
    </tr>
  </tbody>
</Table>

# Examples

## Example 1

Suppose you set the program parameters as follows.

| Parameter name                   | Value       |
| :------------------------------- | :---------- |
| **Overdue tolerance percentage** | 10%         |
| **Overdue tolerance amount**     | $70         |
| **Overdue tolerance method**     | 1 (Maximum) |

Suppose that:

* Minimum amount due (MAD) is $100.
* A payment is made of $80.
* Payment is received after the due date.

The overdue amount is:\
minimum amount due - the payment = 100 - 80 = $20.

Since the tolerance method is set to 1, the platform uses the higher of the following values:

* **Overdue tolerance amount** : $70
* Calculated tolerance percentage: MAD x **Overdue tolerance percentage** = 100 x 10% = 100 x 0.1 = $10

Because $70 is greater than $10, the platform uses $70 as the actual tolerance value. The overdue amount is $20, which is less than $70, so the Pismo platform **does not** consider the account overdue.

## Example 2

Suppose you set the program parameters to the same values as in Example 1, except that **Overdue tolerance method** is set to 2.

| Parameter name                   | Value       |
| :------------------------------- | :---------- |
| **Overdue tolerance percentage** | 10%         |
| **Overdue tolerance amount**     | $70         |
| **Overdue tolerance method**     | 2 (Minimum) |

Suppose that:

* Minimum amount due (MAD) is $100.
* A payment is made of $80.
* Payment is received after the due date.

The overdue amount is:\
minimum amount due - the payment = 100 - 80 = $20.

Since **Overdue tolerance method** is set to 2, the Pismo platform uses the lower of the following values:

* **Overdue tolerance amount** : $70
* Calculated tolerance percentage: MAD x **Overdue tolerance percentage** = 100 x 10% = 100 x 0.1 = $10

Because $10 is lower than $70, the platform uses $10 as the actual tolerance value. The overdue amount is $20, which is greater than $10, so the Pismo platform **does** consider the account overdue.

## Example 3

Suppose `Overdue tolerance amount` is set to $70, and `Overdue tolerance percentage` is not set. In this case, `Overdue tolerance method` is not applicable and is ignored by the platform.

**Note:** Table entries marked **N/A** indicate **Not Applicable**.

| Parameter name                   | Value   |
| :------------------------------- | :------ |
| **Overdue tolerance percentage** | Not set |
| **Overdue tolerance amount**     | $70     |
| **Overdue tolerance method**     | N/A     |

Suppose that:

* Minimum amount due (MAD) is $100.
* A payment is made of $80.
* Payment is received after the due date.

The overdue amount is:\
minimum amount due - the payment = 100 - 80 = $20.

The overdue amount is $20, which is less than $70, so the Pismo platform **does not** consider the account overdue.

## Example 4

Suppose `Overdue tolerance percentage` is set to 10%, and `Overdue tolerance amount` is not set. In this case, `Overdue tolerance methods` is not applicable and is ignored by the platform.

**Note:** Table entries marked **N/A** indicate **Not Applicable**.

| Parameter name                   | Value   |
| :------------------------------- | :------ |
| **Overdue tolerance percentage** | 10%     |
| **Overdue tolerance amount**     | Not set |
| **Overdue tolerance method**     | N/A     |

Suppose that:

* Minimum amount due (MAD) is $100.
* A payment is made of $80.
* Payment is received after the due date.

The overdue amount is:\
minimum amount due - the payment = 100 - 80 = $20.

Calculated tolerance percentage: MAD x **Overdue tolerance percentage** = 100 x 10% = 100 x 0.1 = $10

The overdue amount is $20, which is greater than $10, so the Pismo platform **does** consider the account overdue.

## Example 5

Suppose you set the program parameters as follows.

| Parameter name                   | Value       |
| :------------------------------- | :---------- |
| **Overdue tolerance percentage** | 10%         |
| **Overdue tolerance amount**     | $70         |
| **Overdue tolerance method**     | 1 (Maximum) |

Suppose that:

* Minimum amount due (MAD) is $50.
* No payment is made.

The overdue amount is:\
minimum amount due - the payment = 50 - 0 = $50.

Since **Overdue tolerance method** is set to 2, the Pismo platform uses the greater of the following values:

* **Overdue tolerance amount** : $70
* Calculated tolerance percentage: MAD x **Overdue tolerance percentage** = 50 x 10% = 50 x 0.1 = $5

Because $70 is greater than $5, the platform uses $70 as the actual tolerance value. The overdue amount is $50, which is less than $70, so the Pismo platform **does not** consider the account overdue.

<br />
<!-- source:end -->

### Source 2: `docs/card-issuing/payment-tolerance.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/payment-tolerance · updatedAt: 2026-03-19T12:47:50.000Z

<!-- source:begin path=docs/card-issuing/payment-tolerance.md part=0-end -->

# Payment tolerance

By default, an account with an unpaid balance accrues interest according to the rules laid out in [Calculating interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals). The **payment tolerance** feature enables you to set up additional rules to specify that an account should not accrue interest if the outstanding balance is less than a certain amount.

To configure payment tolerance, use [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) to set the following program parameters.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter name
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Payment tolerance percentage**
      </td>

      <td>
        A percentage of the total amount due (TAD) that is used by the **Payment tolerance method** to determine if the account should accrue interest. Must be greater than 0 and less than or equal to 100.
      </td>
    </tr>

    <tr>
      <td>
        **Payment tolerance amount**
      </td>

      <td>
        A fixed amount that is used by the **Payment tolerance method** to determine if the account should accrue interest. For example, $70.
      </td>
    </tr>

    <tr>
      <td>
        **Payment tolerance method**
      </td>

      <td>
        The method to apply:

        * **0**—Do not use.
        * **1**—Maximum value. Between the **Payment tolerance amount** and (**Payment tolerance percentage** x TAD), use whichever value is higher. If the difference between the payment and the total amount due is less than or equal to this value, no interest is accrued.
        * **2**—Minimum value. Between the **Payment tolerance amount** and (**Payment tolerance percentage** x TAD), use whichever value is lower. If the difference between the payment and the total amount due is less than or equal to this value, no interest is accrued.
      </td>
    </tr>
  </tbody>
</Table>

# Examples

## Example 1

Suppose you set up the program parameters as follows.

| Parameter name                   | Value       |
| :------------------------------- | :---------- |
| **Payment tolerance percentage** | 10%         |
| **Payment tolerance amount**     | $70         |
| **Payment tolerance method**     | 1 (Maximum) |

Suppose also that TAD = $250.

Since **Payment tolerance method** is set to 1, the Pismo platform uses the higher of the following values:

* **Payment tolerance amount**: $70
* **Payment tolerance percentage** x TAD: 10% x 250 = 0.1 x 250 = $25

$70 is greater than $25, so the platform uses $70 as the actual tolerance value. So, after the due date, **if TAD - payment\<= $70, no interest is accrued.**

## Example 2

Suppose the program parameters are set to the same values as in Example 1, except that `Payment tolerance method` is set to 2:

| Parameter name                   | Value       |
| :------------------------------- | :---------- |
| **Payment tolerance percentage** | 10%         |
| **Payment tolerance amount**     | $70         |
| **Payment tolerance method**     | 2 (Minimum) |

Since **Payment tolerance method** is set to 2, the Pismo platform uses the lower of the following values:

* **Payment tolerance amount**: $70
* **Payment tolerance percentage** x TAD: 10% x 250 = 0.1 x 250 = $25

$25 is less than $70, so the platform uses $25 as the actual tolerance value. So, after the due date, **If TAD - payment\<= $25, no interest is accrued.**
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/overdue-tolerance.md`: updatedAt 2026-03-20T19:57:11.000Z.
- `docs/card-issuing/payment-tolerance.md`: updatedAt 2026-03-19T12:47:50.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/overdue-tolerance.md` | whole document | https://developers.pismo.io/pismo-docs/docs/overdue-tolerance | `683d264be35f12be…` | 2026-03-20T19:57:11.000Z |
| `docs/card-issuing/payment-tolerance.md` | whole document | https://developers.pismo.io/pismo-docs/docs/payment-tolerance | `e94a55682d958c40…` | 2026-03-19T12:47:50.000Z |

## Related knowledge units

- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CRED-calculating-interest-accruals` — Calculating interest accruals
