---
ku_id: KU-CRED-negotiating-credit-card-debt
title: Credit card refinancing
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/negotiating-credit-card-debt.md
  sha256: 14f76157694dbb54e3d577487a5c85aa7ca8bc81f3237f4582a6fe02ffb20c8e
  url: https://developers.pismo.io/pismo-docs/docs/negotiating-credit-card-debt
  role: primary_guide
  updated_at: '2026-09-01T18:58:45.000Z'
operations: []
related_kus:
- KU-CRED-agreements
- KU-CRED-installment-advancements-guide
grouping_rationale: single source page
---

# Credit card refinancing

**KU ID:** `KU-CRED-negotiating-credit-card-debt` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/negotiating-credit-card-debt.md`:

> While billing periods are organized in cycles, some cardholders might miss due dates and build up a debt that becomes hard to pay off in a single cycle. On the other hand, some account holders might have extra income that allows them to pay off their future debt, alleviating the impact of interest on their finances.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/negotiating-credit-card-debt.md`: Credit card refinancing; Payment agreements; Installment advancements

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/negotiating-credit-card-debt.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/negotiating-credit-card-debt · updatedAt: 2026-09-01T18:58:45.000Z

<!-- source:begin path=docs/card-issuing/negotiating-credit-card-debt.md part=0-end -->

# Credit card refinancing

While billing periods are organized in cycles, some cardholders might miss due dates and build up a debt that becomes hard to pay off in a single cycle. On the other hand, some account holders might have extra income that allows them to pay off their future debt, alleviating the impact of interest on their finances.

The statements displayed in the following figure can serve as a base scenario for examples of how you can renegotiate credit card debt on the Pismo platform. To keep things simple, the examples ignore interest accrual on overdue payments.

<Image align="center" alt="Credit statement illustration" caption="Three billing cycles, where one has an overdue amount (shown in red). Assume all values are in US dollars." title="Credit card refinancing overview - 1.png" src="https://files.readme.io/9699a17-Credit_card_refinancing_overview_-_1.png" width="smart" />

Cycle 1 shows a statement with an overdue transaction amount of $100. Cycle 2 shows two transactions in the current statement for $100 and $50. Cycle 3 shows one transaction of $40 in a future statement, plus $10 interest. The card has a total balance of $300.

If necessary, refer back to this figure when reading the guides linked to in the following sections.

## Payment agreements

Payment agreements let you give your customers options to manage their cash flow and negotiate payment conditions. The Pismo platform offers the following types of payment agreements.

* [Installment agreements](https://developers.pismo.io/pismo-docs/docs/installment-agreements)—Used to renegotiate the overdue debt for a credit card account
* [Statement agreements](https://developers.pismo.io/pismo-docs/docs/statement-agreements)—Used to renegotiate *all*  debt for a credit card account
* [Compulsory agreements](https://developers.pismo.io/pismo-docs/docs/compulsory-agreements)—A compulsory agreement is the same as an installment agreement, except that the `compulsory` field is set to `true`, indicating that it's the result of a renegotiation that was made independently of the customer.

## Installment advancements

Endpoints are available to create and manage installment advancements. For more information, refer to the [Installment advancements](https://developers.pismo.io/pismo-docs/docs/installment-advancements-guide) guide.

<br />
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/negotiating-credit-card-debt.md`: updatedAt 2026-09-01T18:58:45.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/negotiating-credit-card-debt.md` | whole document | https://developers.pismo.io/pismo-docs/docs/negotiating-credit-card-debt | `14f76157694dbb54…` | 2026-09-01T18:58:45.000Z |

## Related knowledge units

- `KU-CRED-agreements` — Agreements: compulsory, statement, installment and payment agreements
- `KU-CRED-installment-advancements-guide` — Installment advancements
