---
ku_id: KU-LEND-lending-overview
title: Lending overview and participants
category: lending
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/lending/lending-overview.md
  sha256: dc3e9985d33ab8b0ee4c9c24ffa6ea105797a3e38069e1de23c6244390043228
  url: https://developers.pismo.io/pismo-docs/docs/lending-overview
  role: primary_guide
  updated_at: '2026-08-05T19:01:14.000Z'
- path: docs/lending/lending-participants-and-responsibilities.md
  sha256: 602ef2e37243018323046067e71cf1de1e267915781408d078b0c0a503c95d01
  url: https://developers.pismo.io/pismo-docs/docs/lending-participants-and-responsibilities
  role: primary_guide
  updated_at: '2026-08-04T23:29:17.000Z'
operations: []
related_kus:
- KU-LEND-get-started-lending
- KU-LEND-loan-management
- KU-LEND-loan-products
- KU-LEND-loan-statuses-overview
grouping_rationale: Overview and roles.
---

# Lending overview and participants

**KU ID:** `KU-LEND-lending-overview` · **Category:** Lending · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Overview and roles.

Scope as stated in `docs/lending/lending-overview.md`:

> Use Pismo's lending solution to build loan products for your customers and manage those loans throughout their lifecycle. Our solution supports a wide range of lending scenarios, gives you control over loan terms and business rules, and integrates with regulated lenders and intermediaries so you can manage lending operations through a single, consistent platform.

Scope as stated in `docs/lending/lending-participants-and-responsibilities.md`:

> Lending involves multiple participants with the following responsibilities.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/lending/lending-overview.md`: Lending overview; Learn the foundational concepts; Start building and managing loans
- `docs/lending/lending-participants-and-responsibilities.md`: Lending participants and responsibilities

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/lending/lending-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/lending-overview · updatedAt: 2026-08-05T19:01:14.000Z

<!-- source:begin path=docs/lending/lending-overview.md part=0-end -->

# Lending overview

Use Pismo's lending solution to build loan products for your customers and manage those loans throughout their lifecycle. Our solution supports a wide range of lending scenarios, gives you control over loan terms and business rules, and integrates with regulated lenders and intermediaries so you can manage lending operations through a single, consistent platform.

<Callout icon="📘" theme="info">
  Pismo does not originate loans. Instead, it connects to regulated lenders and intermediaries—such as banks, fintech lenders, and third‑party originators—that provide the loans. If you need help finding or setting up a partnership with a loan originator, contact your Pismo representative.
</Callout>

## Learn the foundational concepts

Use these guides to understand how lending works in Pismo.

* [Loan product overview](https://developers.pismo.io/pismo-docs/docs/loan-product-overview)—Explore how loan products help you configure the terms, pricing, and rules that apply to your customers’ loans.
* [Loan management overview](https://developers.pismo.io/pismo-docs/docs/loan-management-overview)—Discover how you can oversee your customers’ loans throughout their lifecycle.
* [Lending participants and responsibilities](https://developers.pismo.io/pismo-docs/docs/lending-participants-and-responsibilities)—Understand how lenders and other participants share roles and responsibilities.
* [Loan statuses overview](https://developers.pismo.io/pismo-docs/docs/loan-statuses-overview)—Review the key status values that indicate where a loan stands in its lifecycle.

## Start building and managing loans

Use these guides to implement lending solutions.

* [Get started with lending](https://developers.pismo.io/pismo-docs/docs/get-started-with-lending)—Define and set up core lending configurations.
* [Create loan products](https://developers.pismo.io/pismo-docs/docs/create-loan-products)—Build loan products with the terms, pricing, and rules that match your business requirements.
* [Manage loans](https://developers.pismo.io/pismo-docs/docs/manage-loans)—Administer existing loans by simulating, booking, disbursing, and handling repayment and settlement.

<br />
<!-- source:end -->

### Source 2: `docs/lending/lending-participants-and-responsibilities.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/lending-participants-and-responsibilities · updatedAt: 2026-08-04T23:29:17.000Z

<!-- source:begin path=docs/lending/lending-participants-and-responsibilities.md part=0-end -->

# Lending participants and responsibilities

Lending involves multiple participants with the following responsibilities.

<Table align={["left","left","left","center","center"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Participants
      </th>

      <th style={{ textAlign: "left" }}>
        Responsibilities
      </th>

      <th style={{ textAlign: "left" }}>
        Examples
      </th>

      <th style={{ textAlign: "center" }}>
        Offer loans
      </th>

      <th style={{ textAlign: "center" }}>
        Manage loans
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Borrower
      </td>

      <td style={{ textAlign: "left" }}>
        Person or organization that accepts funds and repays these funds based on agreed terms
      </td>

      <td style={{ textAlign: "left" }}>
        * Someone taking out a large personal loan to buy a boat
        * Someone taking out a Buy Now, Pay Later loan at checkout to buy a couch
      </td>

      <td style={{ textAlign: "center" }}>
        N
      </td>

      <td style={{ textAlign: "center" }}>
        Y
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Lender
      </td>

      <td style={{ textAlign: "left" }}>
        Institution or entity that defines products, approves loans, disburses funds, and receives repayments
      </td>

      <td style={{ textAlign: "left" }}>
        A licensed lender, such as a bank or retailer
      </td>

      <td style={{ textAlign: "center" }}>
        Y
      </td>

      <td style={{ textAlign: "center" }}>
        Y
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Regulator
      </td>

      <td style={{ textAlign: "left" }}>
        Public or private authority that defines lending, disclosure, and consumer protection requirements
      </td>

      <td style={{ textAlign: "left" }}>
        In the US:

        * Office of the Comptroller of the Currency (OCC)
        * Federal Reserve
        * Federal Deposit Insurance Corporation (FDIC)
      </td>

      <td style={{ textAlign: "center" }}>
        N
      </td>

      <td style={{ textAlign: "center" }}>
        N
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Authorized intermediaries, such as banking correspondents, loan brokers, and originators
      </td>

      <td style={{ textAlign: "left" }}>
        Intermediary that helps originate and distribute loan offers through lender partnerships
      </td>

      <td style={{ textAlign: "left" }}>
        * A commercial bank

        * A mortgage company
      </td>

      <td style={{ textAlign: "center" }}>
        Y
      </td>

      <td style={{ textAlign: "center" }}>
        N
      </td>
    </tr>
  </tbody>
</Table>

In Pismo lending, both lenders and authorized intermediaries can offer loans, while lenders manage loans  and their configurations booking.

<Callout icon="📘" theme="info">
  Pismo does not originate loans. Instead, it connects to regulated lenders and intermediaries—such as banks, fintech lenders, and third‑party originators—that provide the loans. If you need help finding or setting up a partnership with a loan originator, contact your Pismo representative.
</Callout>

<br />

<br />
<!-- source:end -->

## Lifecycle status

- `docs/lending/lending-overview.md`: updatedAt 2026-08-05T19:01:14.000Z.
- `docs/lending/lending-participants-and-responsibilities.md`: updatedAt 2026-08-04T23:29:17.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/lending/lending-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/lending-overview | `dc3e9985d33ab8b0…` | 2026-08-05T19:01:14.000Z |
| `docs/lending/lending-participants-and-responsibilities.md` | whole document | https://developers.pismo.io/pismo-docs/docs/lending-participants-and-responsibilities | `602ef2e372430183…` | 2026-08-04T23:29:17.000Z |

## Related knowledge units

- `KU-LEND-get-started-lending` — Get started with lending
- `KU-LEND-loan-management` — Loan management overview
- `KU-LEND-loan-products` — Loan products: overview and creation
- `KU-LEND-loan-statuses-overview` — Loan statuses overview
