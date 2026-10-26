---
ku_id: KU-BANK-get-started-building-banking
title: Get started with banking
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/get-started-building-banking.md
  sha256: fa0e1d4976d1c5f22c0747b12a2eb44cb1459b7eb947a15e398b9c904e12851d
  url: https://developers.pismo.io/pismo-docs/docs/get-started-building-banking
  role: primary_guide
  updated_at: '2026-06-29T19:44:43.000Z'
operations: []
related_kus:
- KU-BANK-banking-overview
- KU-BANK-get-started-core-banking
- KU-BANK-get-started-demand-deposit-accounts
- KU-BANK-get-started-transaction-banking
grouping_rationale: single source page
---

# Get started with banking

**KU ID:** `KU-BANK-get-started-building-banking` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/get-started/get-started-building-banking.md`:

> You can use the Pismo platform to build and operate a full suite of banking products for your customers, including both core banking and transaction banking capabilities. **Core banking** provides the foundational accounts, ledgers, and processes, while **transaction banking** extends these foundations to support complex payments and cash‑management needs for corporate and institutional clients.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/get-started-building-banking.md`: Get started with banking

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/get-started-building-banking.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-building-banking · updatedAt: 2026-06-29T19:44:43.000Z

<!-- source:begin path=docs/get-started/get-started-building-banking.md part=0-end -->

# Get started with banking  

You can use the Pismo platform to build and operate a full suite of banking products for your customers, including both core banking and transaction banking capabilities. **Core banking** provides the foundational accounts, ledgers, and processes, while **transaction banking** extends these foundations to support complex payments and cash‑management needs for corporate and institutional clients.

Refer to the following table to better understand these concepts and how they relate to typical customer use cases. For a comprehensive overview, refer to [Banking overview](https://developers.pismo.io/pismo-docs/docs/banking-overview).

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Concept
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Customers
      </th>

      <th style={{ textAlign: "left" }}>
        Use cases
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Core banking
      </td>

      <td style={{ textAlign: "left" }}>
        The essential systems and processes that financial institutions use to manage customer accounts and transactions, including deposits, withdrawals, payments, loans, and account maintenance.
      </td>

      <td style={{ textAlign: "left" }}>
        Core banking serves all customer types by keeping their accounts and products consistent and up to date.

        Examples include:

        * A retail customer checking their balance
        * A small business receiving card settlements
        * A bank updating credit card statements
      </td>

      <td style={{ textAlign: "left" }}>
        * Opening a new checking account
        * Updating balances after interest accrual
        * Posting a card purchase to an account
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Transaction banking
      </td>

      <td style={{ textAlign: "left" }}>
        The set of instruments and services that enable corporate and institutional clients to execute and manage day‑to‑day financial transactions, such as payments, cash management, and account‑to‑account operations.

        Core banking provides the underlying accounts and ledgers those transactions post to.

        <br />

        <br />
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction banking typically focuses on large corporate and institutional clients. It helps them manage operational cash flows, liquidity, and risk by extending core banking accounts and ledgers into specialized services.

        Examples include:

        * A treasurer consolidating cash positions across accounts
        * A company using letters of credit for international trade
        * A bank defining calendars and holidays to control when corporate transactions can be executed and settled
      </td>

      <td style={{ textAlign: "left" }}>
        * A bank creating and managing DDAs for corporate clients to hold operational cash
        * A multinational corporation paying suppliers in multiple countries

        <br />
      </td>
    </tr>
  </tbody>
</Table>

The following guides help you get started:

[Get started with core banking](https://developers.pismo.io/pismo-docs/docs/get-started-building-core-banking)

[Get started with transaction banking](https://developers.pismo.io/pismo-docs/docs/get-started-building-transaction-banking)

[Get started with demand deposit accounts (DDAs)](https://developers.pismo.io/pismo-docs/docs/get-started-building-demand-deposit-accounts)

<br />
<!-- source:end -->

## Lifecycle status

- `docs/get-started/get-started-building-banking.md`: updatedAt 2026-06-29T19:44:43.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/get-started-building-banking.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-building-banking | `fa0e1d4976d1c5f2…` | 2026-06-29T19:44:43.000Z |

## Related knowledge units

- `KU-BANK-banking-overview` — Banking overview
- `KU-BANK-get-started-core-banking` — Get started with core banking
- `KU-BANK-get-started-demand-deposit-accounts` — Get started with demand deposit accounts (DDAs)
- `KU-BANK-get-started-transaction-banking` — Get started with transaction banking
