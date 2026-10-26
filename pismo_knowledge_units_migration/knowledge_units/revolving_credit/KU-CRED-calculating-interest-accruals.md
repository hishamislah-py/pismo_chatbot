---
ku_id: KU-CRED-calculating-interest-accruals
title: Calculating interest accruals
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/calculating-interest-accruals.md
  sha256: 6191c83c0c52aad8314f53e64fa424b5664ceb7fb6b681d3c08b3deb3a171a2a
  url: https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals
  role: primary_guide
  updated_at: '2026-03-18T15:22:14.000Z'
operations:
- createTransactionCategory
- updateProgramParameter
related_kus:
- KU-API-platform-setup-programs--parameters
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-CORE-processing-codes-and-transaction-types
- KU-CRED-accrual-rate-types-and-limits
- KU-CRED-minimum-amount-due-calculation
grouping_rationale: single source page
---

# Calculating interest accruals

**KU ID:** `KU-CRED-calculating-interest-accruals` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/calculating-interest-accruals.md`:

> At cycle closing time, the Pismo platform verifies a set of scenarios that determine whether the account accrues interest in the next cycle.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/calculating-interest-accruals.md`: Calculating interest accruals; Minimum amount; Setting transaction types to block accrual charges; Additional program parameters for interest accruals

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/calculating-interest-accruals.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals · updatedAt: 2026-03-18T15:22:14.000Z

<!-- source:begin path=docs/card-issuing/calculating-interest-accruals.md part=0-end -->

# Calculating interest accruals

At cycle closing time, the Pismo platform verifies a set of scenarios that determine whether the account accrues interest in the next cycle.

### Minimum amount

The Pismo platform enables you to configure a minimum amount, below which the unpaid balance does not accrue charges. You can set this value using the program parameter `MINIMO BOLETO`, which is applicable to programs in all regions. If the closing statement's unpaid balance is greater than or equal to this value, the account can accrue charges.

The following business rules apply:

* If the minimum amount is not set, the account accrues interest in the next cycle.
* If the minimum amount is set, then:
  * If the unpaid balance is greater than or equal to the minimum amount, the account accrues interest in the next cycle.
  * If the unpaid balance is less than the minimum amount, the account does not accrue interest in the next cycle. In this case, if the collection status is `OVERDUE`, the platform updates it to `NORMAL` on the cycle closing date.

> 🚧
>
> Note that the **minimum amount** is different from the [minimum amount due (MAD)](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation). The minimum amount refers to the amount of unpaid balance, below which, the account does not accrue interest. The minimum amount **due** is the minimum amount the cardholder must pay to avoid incurring overdue charges.

### Setting transaction types to block accrual charges

You can designate specific [transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) (fees, for example) that block accrual charges when they're the only transactions on a statement. If, at cycle closing time, the statement only has transactions of those types, the next cycle is marked to not accrue. For more information, refer to [Setting transaction types to block accrual charges](https://developers.pismo.io/pismo-docs/docs/configuring-transaction-types-to-not-accrue-charges).

## Additional program parameters for interest accruals

In addition to `MINIMO BOLETO`, [you can set](https://developers.pismo.io/pismo-docs/reference/updateprogramparameter) the following program parameters that are directly related to interest accruals.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Program parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Accrual calculation strategy
      </td>

      <td>
        Defines the start date for daily accruals.\
        0 - Normal (Due date +1)\
        1 - Calculation goes back to debit date. (First installment: transaction date + 1. Other installments: corresponding cycle start date + 1).

        The Pismo platform uses the date defined in this parameter to calculate interest charges for each program transaction category. If the parameter is set to start interest from the due date, but you want cash withdrawals to accrue interest from the transaction date instead, use the [Create program transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory) endpoint.
      </td>
    </tr>

    <tr>
      <td>
        Accrual reversal strategy
      </td>

      <td>
        Parameter responsible for configuring the accrual reversal strategy in the event of a purchase cancellation.
      </td>
    </tr>

    <tr>
      <td>
        Ignore grace days on pending accruals reversal for revolving accounts
      </td>

      <td>
        Ignore the grace period when reversing pending accruals for revolving accounts. If an account has been revolving for more than one cycle and receives a payment within the grace period, the platform reverses the pending accruals from the date of payment instead of from the due date.
      </td>
    </tr>

    <tr>
      <td>
        Interest projection reversal
      </td>

      <td>
        Defines whether the projected interest between the cut (closing) and the due date of the invoice should be reversed if any payment occurs before the due date.\
        0 - Default (do not reverse)\
        1 - Reverse
      </td>
    </tr>

    <tr>
      <td>
        Number of days to block the account for unpaid statement
      </td>

      <td>
        Number of days after due date to block the account for nonpayment.
      </td>
    </tr>

    <tr>
      <td>
        Stop accrual # of days
      </td>

      <td>
        Maximum days in overdue for which the calculation of fees, interest, and fines should be posted. The platform won’t post any accrued amount that was calculated after the **Stop accrual # of days** number of days. You can still post these accruals manually using the Statements API.
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PUT /programs/v1/programs/{program_id}/parameters/{program_parameter_id}` | `updateProgramParameter` | Update program parameter | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `POST /statements-v2/v1/transactions-categories` | `createTransactionCategory` | Create program transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |

### Operation essentials

- **`PUT /programs/v1/programs/{program_id}/parameters/{program_parameter_id}`** (`updateProgramParameter`): security `S2SAuthentication`; required parameters `program_id` (path), `program_parameter_id` (path); required body fields `value`; response statuses 200, 400; error codes in examples none; events none listed.
- **`POST /statements-v2/v1/transactions-categories`** (`createTransactionCategory`): security `BearerAuth`; required parameters `Authorization` (header), `program-id` (header); required body fields `default_rate`, `fine_rate`, `minimum_value`, `overdue_rate_after_due_date`, `refinancing_rate_after_due_date`; response statuses 201, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.

## Lifecycle status

- `docs/card-issuing/calculating-interest-accruals.md`: updatedAt 2026-03-18T15:22:14.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/calculating-interest-accruals.md` | whole document | https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals | `6191c83c0c52aad8…` | 2026-03-18T15:22:14.000Z |

## Related knowledge units

- `KU-API-platform-setup-programs--parameters` — API reference: Platform setup - Programs — Parameters
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CRED-accrual-rate-types-and-limits` — Accrual rate types, accrual-free transaction types and accrual-day limits
- `KU-CRED-minimum-amount-due-calculation` — Minimum amount due calculation
