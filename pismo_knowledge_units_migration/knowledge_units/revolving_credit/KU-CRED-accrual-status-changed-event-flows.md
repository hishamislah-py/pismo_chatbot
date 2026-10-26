---
ku_id: KU-CRED-accrual-status-changed-event-flows
title: Accrual status changed event flows
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/accrual-status-changed-event-flows.md
  sha256: 0a29939498238a2ad4fc39212948d335685911c0cc6ddb7b549b455daef5b5ab
  url: https://developers.pismo.io/pismo-docs/docs/accrual-status-changed-event-flows
  role: primary_guide
  updated_at: '2026-03-18T15:22:33.000Z'
operations: []
related_kus:
- KU-CC-get-started-control-center
grouping_rationale: single source page
---

# Accrual status changed event flows

**KU ID:** `KU-CRED-accrual-status-changed-event-flows` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/accrual-status-changed-event-flows.md`:

> The Pismo platform generates an [Accrual status changed](https://developers.pismo.io/events/docs/balance-accrual-status-1) event in response to any change in an account's accrual status. This event includes an `accrual status` field with the following possible values:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/accrual-status-changed-event-flows.md`: Accrual status changed event flows; Event flows; Scenario 1: Client pays less than the MAD by the due date; Scenario 2: Client pays the MAD by the due date but does not pay the TAD; Scenario 3: Client pays less than the MAD by the due date. Later, they make another payment that fulfills the MAD but not the TAD.; Scenario 4: Client pays the MAD by the due date but does not pay the TAD. No additional payments are made by the next due date.; Scenario 5: Client pays the MAD by the due date but does not pay the TAD. No additional payment is made until after the next due date, when a payment is made that is greater then the MAD, but still less than the TAD.; Scenario 6: For two cycles, the client pays the MAD by the due date but does not pay the TAD; Scenario 7: Client doesn't pay anything until `STOP_ACCRUAL`, then pays the TAD; Scenario 8: Client pays less than MAD after account is already overdue; Scenario 9: Amount paid less than TAD after refinancing starts

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/accrual-status-changed-event-flows.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accrual-status-changed-event-flows · updatedAt: 2026-03-18T15:22:33.000Z

<!-- source:begin path=docs/card-issuing/accrual-status-changed-event-flows.md part=0-end -->

# Accrual status changed event flows

The Pismo platform generates an [Accrual status changed](https://developers.pismo.io/events/docs/balance-accrual-status-1) event in response to any change in an account's accrual status. This event includes an `accrual status` field with the following possible values:

* `REFINANCING_START`—Refinancing has started.
* `REFINANCING_CHANGE`—Account went from overdue to refinancing.
* `REFINANCING_STOP`—Refinancing has stopped.
* `OVERDUE_START`—Account is overdue.
* `OVERDUE_CHANGE`—Account went from refinancing to overdue.
* `OVERDUE_UNDERPAID`—Account started out in either overdue or refinancing, and a payment was made that did not cover the total amount due. This is meant to serve as a notification that a payment occurred, but it did not change the account status from overdue or refinancing.\ <b>Note:</b> This status can occur without the account ever being overdue. It's enough for it to be in refinancing when the new payment is made.
* `OVERDUE_STOP`—Account is no longer overdue and is not being refinanced.
* `STOP_ACCRUAL`—This status is triggered when the account has been in overdue status (that is, `OVERDUE_START` or `OVERDUE_CHANGE`) for the number of days specified in the `Stop accrual # of days` program parameter. Use [Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) to view or set this parameter.

# Event flows

Accruals begin to accumulate the day after the statement due date. The amount of an accrual depends on the relationship between the total amount due (TAD), the amount paid, and the minimum amount due (MAD). The following scenarios illustrate various event flows for Accrual status changed events.

> 📘
>
> To make the following sections easier to read, the account statuses are used as shorthand for the events. For example, "OVERDUE\_STOP was emitted" is shorthand for "An Accrual status changed event with `account_status` set to `OVERDUE_STOP` was emitted".

## Scenario 1: Client pays less than the MAD by the due date

When a client does not pay the MAD by the due date, `OVERDUE_START` is emitted on the day after the due date. If the client later pays the TAD, `OVERDUE_STOP` is emitted.

In the following example, the client had a $5000 TAD, a $750 MAD, and they did not pay anything by the due date. So, on the day after the due date (DD1 + 1), `OVERDUE_START` was emitted. Later, the client paid the $5000 TAD, and `OVERDUE_STOP` was emitted.

<Image alt="Scenario 1: Client pays less than the MAD by the due date" align="center" src="https://files.readme.io/ccfd589f7be928bf45e68cf26aafc310b1a4a00ecdc2a08710f45701bf89f09a-Scenario_1__Client_pays_less_than_the_MAD_by_the_due_date.png" />

## Scenario 2: Client pays the MAD by the due date but does not pay the TAD

When the client pays at least the MAD by the due date, but the amount paid is less than the TAD, `REFINANCING START` is emitted on the day after the due date. If the client later pays the TAD, `REFINANCING STOP` is emitted.

In the following example, the client had a $5000 TAD, a $750 MAD, and they paid $1000 before the due date. So, on DD1 + 1, `REFINANCING_START` was emitted. Later, the client paid $5000, and `REFINANCING_STOP` was emitted.

<Image alt="Scenario 2: Client pays the MAD by the due date but does not pay the TAD" align="center" src="https://files.readme.io/a64105acc4a7f1c6b2344776f3242b13a3a8d7e75907274df3884d98c65f18ef-Scenario_2__Client_pays_the_MAD_by_the_due_date_but_does_not_pay_the_TAD.png" />

## Scenario 3: Client pays less than the MAD by the due date. Later, they make another payment that fulfills the MAD but not the TAD.

As explained in Scenario 1, when the client does not pay the MAD by the due date, `OVERDUE_START` is emitted on the day after the due date. If the client later makes another payment that makes the total amount paid greater than the MAD, but less than the TAD, `REFINANCING_CHANGE` is emitted. If the client later pays the TAD, `REFINANCING STOP` is emitted.

In the following example, the client had a $5000 TAD, a $750 MAD, and they did not pay anything by the due date. So, `OVERDUE_START` was emitted on DD1 + 1. Later, the client paid $1000. This was greater than the MAD, but less than the TAD, so `REFINANCING_CHANGE` was emitted. Later, the client paid the remainder of the TAD, so `REFINANCING STOP` was emitted.

<Image alt="Scenario 3: Client pays less than the MAD by the due date. Later, they make another payment that fulfills the MAD but not the TAD." align="center" src="https://files.readme.io/2a06e445d7b1929208d0dce1e08d03cf18066ce654245ac70bfe7b45a54af062-Scenario_3__Client_pays_less_than_the_MAD_by_the_due_date._Later_they_make_another_payment_that_fulfills_the_MAD_but_not_the_TAD..png" />

## Scenario 4: Client pays the MAD by the due date but does not pay the TAD. No additional payments are made by the next due date.

This scenario starts out like scenario 2. When client pays at least the MAD by the due date, but the amount paid is less than the TAD, `REFINANCING START` is emitted on the day after the due date. If the client has not made another payment by the following due date, `OVERDUE_CHANGE` is emitted on the day after the second due date. If the client later pays the TAD, `OVERDUE_STOP` is emitted.

In the following example, the client had a $5000 TAD, a $750 MAD, and they paid $1000 before the due date. So, on DD1 + 1, the `REFINANCING_START` was emitted. The client didn't make any more payments before the next due date passed, so an `OVERDUE_CHANGE` was emitted on DD2 + 1. Later, the client paid the TAD, and an `OVERDUE_STOP` was emitted.

<Image alt="Scenario 4: Client pays the MAD by the due date but does not pay the TAD. No additional payments are made by the next due date." align="center" src="https://files.readme.io/4d2f2cd80b55e1fa8bcafed13fd0e6c4ccee1de3b27a6eafd27258813b98eafa-Scenario_4__Client_pays_the_MAD_by_the_due_date_but_does_not_pay_the_TAD._No_additional_payments_are_made_by_the_next_due_date..png" />

## Scenario 5: Client pays the MAD by the due date but does not pay the TAD. No additional payment is made until after the next due date, when a payment is made that is greater then the MAD, but still less than the TAD.

This scenario also starts out like Scenario 2. When the client pays at least the MAD by the due date, but the amount paid is less than the TAD, `REFINANCING START` is emitted on the day after the due date. If the client has not made any additional payments when the next due date passes, `OVERDUE_CHANGE` is emitted on the day after the second due date. If the client later makes a payment that is greater than the MAD, but still less than the TAD, `REFINANCING_CHANGE` is emitted.

In the following example, the client had a $5000 TAD, a $750 MAD, and paid $1000 before the due date. So, on DD1 + 1, `REFINANCING_START` was emitted. The client had not made any additional payments when DD2 passed, so `OVERDUE_CHANGE` was emitted on DD2 + 1. Later, the client paid $2500. This was greater than the MAD, but it did not pay off the TAD, so `REFINANCING_CHANGE` was emitted.

<Image alt="Scenario 5: Client pays the MAD by the due date but does not pay the TAD. No additional payment is made until after the next due date, when a payment is made that is greater then the MAD, but still less than the TAD." align="center" src="https://files.readme.io/44358d4bad390717a73a4cc1719e1f248ef895ad668d3d4cc49977188a3b5bf4-Scenario_5__Client_pays_the_MAD_by_the_due_date_but_does_not_pay_the_TAD._No_additional_payment_is_made_until_after_the_next_due_date_when_a_payment_is_made_that_is_greater_then_the_MAD_but_still_less_than_the_TAD..png" />

## Scenario 6: For two cycles, the client pays the MAD by the due date but does not pay the TAD

This scenario also starts out like Scenario 2. When the client pays at least the MAD by the due date, but the amount paid is less than the TAD, `REFINANCING START` is emitted on the day after the due date. If, in the next cycle, the client again pays at least the MAD, but less than the TAD, no event is emitted on the day after the second due date, because the account status has not changed.

In the following example, the client had a $5000 TAD, a $750 MAD, and paid $1000 before the due date, so `REFINANCING_START` is emitted on DD1 + 1. In the next cycle, the client paid $1000 before the due date. No event is emitted on DD2 + 1.

<Image alt="Scenario 6: For two cycles, the client pays the MAD by the due date but does not pay the TAD" align="center" src="https://files.readme.io/f86ec130486fd22446496b4f40155c381ca2002e3b8d7753dfd47a8feefa9239-Scenario_6__For_two_cycles_the_client_pays_the_MAD_by_the_due_date_but_does_not_pay_the_TAD.png" />

## Scenario 7: Client doesn't pay anything until `STOP_ACCRUAL`, then pays the TAD

When the client does not pay anything before the due date, `OVERDUE_START` is emitted on the day after the due date. If they still don't pay anything for the number of days configured in the **Stop accrual # of days** program parameter, `STOP ACCRUAL` is emitted. If the client later pays the TAD, `OVERDUE_STOP` is emitted.

In the following example, the client has a $5000 TAD, a $750 MAD, and did not pay anything before the due date. So, on DD1 + 1, `OVERDUE_START` was emitted. The client still did not pay anything for the next two cycles. On DD3 +1, `STOP ACCRUAL` was emitted. Later, the client paid $6000, and `OVERDUE_STOP` was emitted.

<Image alt="Scenario 7: Client doesn't pay anything until `STOP_ACCRUAL`, then pays the TAD" align="center" src="https://files.readme.io/2662d8c10ed3266b4e1203b0197608576e85ac9d90d7659e830b3927ef945bfb-Scenario_7__Client_doesnt_pay_anything_until_STOP_ACCRUAL_then_pays_the_TAD.png" />

When an account is already overdue (`OVERDUE_START` or `OVERDUE_CHANGE` has been emitted), and the client pays less than the MAD before the due date passes, `OVERDUE_UNDERPAID` is emitted.

## Scenario 8: Client pays less than MAD after account is already overdue

When an account is already overdue (`OVERDUE_START` or `OVERDUE_CHANGE` has been emitted), and the client pays less than the MAD before the due date passes, `OVERDUE_UNDERPAID` is emitted.

In the first example that follows, the client had a $5000 TAD,  and the client didn't make a payment by the due date, so `OVERDUE_START` was emitted on DD1 + 1. Later, the client made a payment, but the amount paid was less than the MAD, so `OVERDUE_UNDERPAID` was emitted.

In the second example, the client had a $5000 TAD, a $750 MAD, and paid $1000 before the due date, so `REFINANCING_START` was emitted on the DD1 + 1. The client did not make another payment by DD2, so `OVERDUE_CHANGE` was emitted on DD2 + 1. Later, the client made a payment, but the amount paid was less than the MAD, so `OVERDUE_UNDERPAID` was emitted.

<Image alt="Scenario 8: Client pays less than MAD after account is already overdue" align="center" src="https://files.readme.io/2976bbc386fea59f6074335b7cd6db5c5f1c1511baabf2f41a31c7ec3f61f70d-Scenario_8__Client_pays_less_than_MAD_after_account_is_already_overdue.png" />

## Scenario 9: Amount paid less than TAD after refinancing starts

When `REFINANCING_START` or `REFINANCING_CHANGE` has already been emitted, and the client pays less than the TAD by the due date, `OVERDUE_UNDERPAID` is emitted.

In the first example that follows, the client had a $5000 TAD, a $750 MAD, and paid $1000 before the due date, so `REFINANCING_START` was emitted on DD1 + 1. After this event to be emitted, the client makes a payment, but the amount paid was less than the TAD, so `OVERDUE_UNDERPAID` was emitted.

In the second example, the client had a $5000 TAD and didn't pay the MAD by the due date, so `OVERDUE_START `was emitted on DD1 + 1.  Later, the client paid $1000. This was greater than the MAD, but less than the TAD, so `REFINANCING_CHANGE` was emitted. Later, the client paid $300. This was less than the TAD, so `OVERDUE_UNDERPAID` was emitted.

<Image alt="Scenario 9: Amount paid less than TAD after refinancing starts" align="center" src="https://files.readme.io/b707e2ca6ab0235b1c47ee24acccabfda6637e3ca010ce4523cdfc3c6d9f07da-Scenario_9__Amount_paid_less_than_TAD_after_refinancing_starts.png" />
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/accrual-status-changed-event-flows.md`: updatedAt 2026-03-18T15:22:33.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/accrual-status-changed-event-flows.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accrual-status-changed-event-flows | `0a29939498238a2a…` | 2026-03-18T15:22:33.000Z |

## Related knowledge units

- `KU-CC-get-started-control-center` — Get started with Control Center
