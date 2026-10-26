---
ku_id: KU-CRED-projected-accruals
title: Projected accruals
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/projected-accruals.md
  sha256: 9ed4f9246ab739ef525a0a075d7615b5bc9a9bd37bc622af707ce9cbf9b59f51
  url: https://developers.pismo.io/pismo-docs/docs/projected-accruals
  role: primary_guide
  updated_at: '2026-03-18T15:22:26.000Z'
operations:
- updateAccrualTypePostConfig
related_kus:
- KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations
- KU-CC-get-started-control-center
grouping_rationale: single source page
---

# Projected accruals

**KU ID:** `KU-CRED-projected-accruals` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/projected-accruals.md`:

> Since some clients need to estimate revenue in advance, the Pismo platform provides a way to automatically project the accruals on an unpaid balance at statement closing time. The platform uses the refinancing rate and overdue rate to calculate the accruals that would be charged between the cycle closing date plus one day and the due date (assuming the cardholder doesn't make any payments before the due date). It does this for each debit transaction separately. For each transaction type, it adds up the projected accruals for the refinancing rate and posts one transaction for that amount to the statement. It then adds up the projected accruals for the overdue rate and posts another transaction for that amount.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/projected-accruals.md`: Projected accruals; Projected accruals example; Reversing projected accruals

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/projected-accruals.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/projected-accruals · updatedAt: 2026-03-18T15:22:26.000Z

<!-- source:begin path=docs/card-issuing/projected-accruals.md part=0-end -->

# Projected accruals

Since some clients need to estimate revenue in advance, the Pismo platform provides a way to automatically project the accruals on an unpaid balance at statement closing time. The platform uses the refinancing rate and overdue rate to calculate the accruals that would be charged between the cycle closing date plus one day and the due date (assuming the cardholder doesn't make any payments before the due date). It does this for each debit transaction separately. For each transaction type, it adds up the projected accruals for the refinancing rate and posts one transaction for that amount to the statement. It then adds up the projected accruals for the overdue rate and posts another transaction for that amount.

To enable the Accrual projection feature, use [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) to set `Accrual projection calculation method` to 1.

# Projected accruals example

Suppose the cardholder makes two purchase transactions during Cycle 1 — one for $100.00 and another for $150.00. Suppose also:

* Both transactions have transaction type ID 7001.
* The cycle closing date for Cycle 1 is the 10th day of the month.
* There are 10 days between the Cycle 1 closing date and the Cycle 1 due date. So, the Cycle 1 due date falls on the 20th day of the month.
* There are 19 days between the Cycle 1 due date plus 1 day and the Cycle 2 closing date.
* The refinancing rate is %1.
* The overdue rate is %2.
* Accrual projection is enabled.

If the cardholder makes no payments, daily charges begin to accrue the day after the due date (Day 21). Assume that the cardholder makes no payments for the rest of the cycle. The following table shows the daily charges that the transactions accrue during Cycle 2.

**Daily charges for the $100 transaction:**

|                 | Unpaid balance | Accrual rate | Day 21 | Day 22 | Day 23 | Day 24 | Day 25 | Day 26 | Day 27 | Day 28 | Day 29 | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 | Day 8 | Day 9 | Day 10 | Total |
| :-------------- | :------------- | :----------- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :----- | :---- |
| **Refinancing** | $100           | 0.01         | 1      | 1      | 1      | 1      | 1      | 1      | 1      | 1      | 1      | 1     | 1     | 1     | 1     | 1     | 1     | 1     | 1     | 1     | 1      | $19   |
| **Overdue**     | $100           | 0.02         | 2      | 2      | 2      | 2      | 2      | 2      | 2      | 2      | 2      | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2      | $38   |

**Daily charges for the $150 transaction:**

|                 | Unpaid balance | Accrual rate | Day 21 | Day 22 | Day 23 | Day 24 | Day 25 | Day 26 | Day 27 | Day 28 | Day 29 | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 | Day 8 | Day 9 | Day 10 | Total |
| :-------------- | :------------- | :----------- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :----- | :---- |
| **Refinancing** | $150           | 0.01         | 1.5    | 1.5    | 1.5    | 1.5    | 1.5    | 1.5    | 1.5    | 1.5    | 1.5    | 1.5   | 1.5   | 1.5   | 1.5   | 1.5   | 1.5   | 1.5   | 1.5   | 1.5   | 1.5    | $28.5 |
| **Overdue**     | $150           | 0.02         | 3      | 3      | 3      | 3      | 3      | 3      | 3      | 3      | 3      | 3     | 3     | 3     | 3     | 3     | 3     | 3     | 3     | 3     | 3      | $57   |

At the end of Cycle 2, the Pismo platform calculates the projected charges for the two transactions.

**Projected charges for the $100 transaction:**

|                 | Unpaid balance | Accrual rate | Day 11 | Day 12 | Day 13 | Day 14 | Day 15 | Day 16 | Day 17 | Day 18 | Day 19 | Day 20 | Total |
| :-------------- | :------------- | :----------- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :---- |
| **Refinancing** | $100           | 0.01         | 1      | 1      | 1      | 1      | 1      | 1      | 1      | 1      | 1      | 1      | $10   |
| **Overdue**     | $100           | 0.02         | 2      | 2      | 2      | 2      | 2      | 2      | 2      | 2      | 2      | 2      | $20   |

**Projected charges for the $150 transaction:**

|                 | Unpaid balance | Accrual rate | Day 11 | Day 12 | Day 13 | Day 14 | Day 15 | Day 16 | Day 17 | Day 18 | Day 19 | Day 20 | Total |
| :-------------- | :------------- | :----------- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :---- |
| **Refinancing** | $150           | 0.01         | 1.5    | 1.5    | 1.5    | 1.5    | 1.5    | 1.5    | 1.5    | 1.5    | 1.5    | 1.5    | $15   |
| **Overdue**     | $150           | 0.02         | 3      | 3      | 3      | 3      | 3      | 3      | 3      | 3      | 3      | 3      | $30   |

On the Cycle 2 closing date, the Pismo platform must post a transaction with transaction type ID 401 for the **refinancing** accruals. To calculate the amount of the transaction, the platform adds up the following values:

* Daily refinancing accruals from the $100 transaction: 19
* Daily refinancing accruals from the $150 transaction: 28.5
* Projected refinancing accruals from the $100 transaction: 10
* Projected refinancing accruals from the $150 transaction: 15

19 + 28.5 + 10 + 15 = $72.5. So, the platform posts a transaction with transaction type ID 401 for $72.5.

On the same day, the platform must post a transaction with transaction type ID 402 for the **overdue** accruals. To calculate the amount of the transaction, the platform adds up the following values:&#x9;

* Daily overdue accruals from the $100 transaction: 38
* Daily overdue accruals from the $150 transaction: 57
* Projected overdue accruals from the $100 transaction: 20
* Projected overdue accruals from the $150 transaction: 30

38 + 57 + 20 + 30 = $145. So, the platform posts a transaction with transaction type ID 402 for $145.

# Reversing projected accruals

If the cardholder makes a payment between the closing date and the due date, any refinancing or overdue projected accruals should be reduced by that amount. To enable this feature, use [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) to set `Interest projection reversal` to 1.

The Pismo platform creates reversal transactions to reduce the projected accruals. Projected accrual reversal, in part or in whole, occurs when the cardholder's account is credited.

The Pismo platform reverses projected accruals for refinancing and overdue transactions automatically. By default, other types of accruals are projected, but not reversed. To enable projection reversal for other accrual types, use the [Update accrual type post configuration](https://developers.pismo.io/pismo-docs/reference/updateaccrualtypepostconfig) endpoint to configure reversal processing codes for them.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PATCH /v1/programs/{programId}/accrual-type-post-config/{accrualTypePostConfigId}` | `updateAccrualTypePostConfig` | Update accrual type post configuration | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations |

### Operation essentials

- **`PATCH /v1/programs/{programId}/accrual-type-post-config/{accrualTypePostConfigId}`** (`updateAccrualTypePostConfig`): security `BearerAuth`; required parameters `programId` (path), `accrualTypePostConfigId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EIAC0002`, `EX0001`, `GN0001`; events none listed.

## Lifecycle status

- `docs/card-issuing/projected-accruals.md`: updatedAt 2026-03-18T15:22:26.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/projected-accruals.md` | whole document | https://developers.pismo.io/pismo-docs/docs/projected-accruals | `9ed4f9246ab739ef…` | 2026-03-18T15:22:26.000Z |

## Related knowledge units

- `KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations` — API reference: Revolving credit - Interest accruals — Accrual type post configurations
- `KU-CC-get-started-control-center` — Get started with Control Center
