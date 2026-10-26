---
ku_id: KU-LEND-loan-statuses-overview
title: Loan statuses overview
category: lending
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/lending/loan-statuses-overview.md
  sha256: 84c03ea400db817e4832aa251f4bb743481852134b60e859de8f516f1ebcd966
  url: https://developers.pismo.io/pismo-docs/docs/loan-statuses-overview
  role: primary_guide
  updated_at: '2026-08-05T18:04:47.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# Loan statuses overview

**KU ID:** `KU-LEND-loan-statuses-overview` · **Category:** Lending · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/lending/loan-statuses-overview.md`:

> Use this guide to understand loan statuses and how they reflect a loan’s position within its lifecycle, from origination through closure.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/lending/loan-statuses-overview.md`: Loan statuses overview; Loan statuses; Disbursement statuses; Installment statuses; Paid before the grace period has passed; Paid during the grace period; Paid after the grace period has passed

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/lending/loan-statuses-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/loan-statuses-overview · updatedAt: 2026-08-05T18:04:47.000Z

<!-- source:begin path=docs/lending/loan-statuses-overview.md part=0-end -->

# Loan statuses overview

Use this guide to understand loan statuses and how they reflect a loan’s position within its lifecycle, from origination through closure.

# Loan statuses

Loans can have the following statuses.

<Image align="center" alt="Statuses that loans can have" border={true} src="https://files.readme.io/d68cc22-loan_states2.jfif" className="border" />

* **PENDING**—The loan is created but not yet booked. Terms may still be under review.
* **BOOKED**—The loan is approved and booked. The payment schedule is set and the loan is ready for disbursement. No transfers (repayments or disbursements) related to the loan account have been executed yet.
* **ACTIVE**—The loan is considered active based on the configuration of the loan product. Depending on lender requirements, this status can mean that at least one transfer related to the loan has been registered or simply that the loan has been booked.
* **CANCELED**—Operations on this loan are no longer supported and all the expected transfers have been canceled. No repayment is expected.
* **RENEGOTIATED**—The lender and borrower have agreed to new terms, resulting in a new loan; the original loan is no longer active for new transactions. This status is final and cannot be changed because a new loan is created during the restructure.
* **SETTLED**—The loan has been fully repaid and is now closed, with a zero balance remaining. This status occurs when the borrower completes all scheduled payments or settles the loan early.

# Disbursement statuses

Disbursements can have the following statuses.

<Image align="center" alt="Statuses that loan disbursements can have" border={true} src="https://files.readme.io/46f8be9-disbursment_statuses.png" className="border" />

* **SCHEDULED**—A disbursement is due on or before its scheduled date.
* **PROCESSING**—A temporary state while a status change is in progress. A common use case is when a disbursement request has been submitted and is being processed (Scheduled → Processing → Paid)
* **PAID**—This disbursement was paid in full on or before the expected disbursement date.
* **NOT PAID**—The disbursement was not paid.
* **EXPIRED**—The scheduled disbursement expired before it was processed, so it can no longer be processed.
* **CANCELED**—A disbursement is no longer expected to be paid.

# Installment statuses

Installments (repayments) can have the following statuses.

* **PENDING**—This installment was created as part of the repayment schedule but is not yet active.
* **PROCESSING**—A temporary state while a status change is in progress.
* **SCHEDULED**—The repayment for this installment is due on or before its due date.
* **PAST\_DUE**—The due date has passed, and the repayment for this installment was not paid in full.
* **PAID**—The repayment for this installment was paid in full on or before the due date.
* **PARTIALLY\_PAID**—Only part of the repayment for this installment was made, and the due date has not passed. The borrower can still make the payment on time.
* **CANCELED**—The repayment for this installment is not expected to be paid.
* **PENDING**—A payment for this installment was initiated and is being processed.
* **PAST\_DUE\_PENDING\_PAYMENT**—The due date for this installment has passed but a payment was initiated and is being processed.
* **ACTIVE**—Funds have been disbursed and repayment for this installment is in progress.
* **OVERDUE**—The repayment for this installment has remained past due beyond configured thresholds and is now overdue.
* **OVERDUE\_PENDING\_PAYMENT**—The repayment for this installment is overdue but a payment was initiated and is being processed.
* **IN\_GRACE\_PERIOD**—The installment is within the configured grace period after the due date.
* **IN\_GRACE\_PERIOD\_PENDING\_PAYMENT**—The installment is in the grace period and a payment attempt is currently pending.
* **PAID\_WITHIN\_GRACE**—The installment was paid in full during the grace period.

<Image align="center" alt="Statuses that loan installments can have" border={true} src="https://files.readme.io/da0b1f27ef5164e8095ded31a6b3ac5d29863c525556da66a1aad483957bf85c-installment_status_all.png" className="border" />

Three paths exist for installments based on whether the grace period has passed.

## Paid before the grace period has passed

<Image align="center" alt="Statuses that loan installments can have after the grace period " border={true} width="50% " src="https://files.readme.io/84cab895bec5239ee5a0a236905fd59d338afe55c4548f3713156cb288a4014d-happy_path.png" className="border" />

## Paid during the grace period

<Image align="center" alt="Statuses that loan installments can have during the grace period " border={true} width="50% " src="https://files.readme.io/9370232ead3e93fe362af6e16f7507d54b2906a957f96b5c7f1ec74d34aa0c8f-paid_within_grace.png" className="border" />

## Paid after the grace period has passed

<Image align="center" alt="Statuses that loan installments can have after the grace period " border={true} width="50% " src="https://files.readme.io/7e0af88e7004794e0275f61e751e2e4ba91776910436b2b3c1ed95eeffd441e1-paid_after_overdue.png" className="border" />

<br />

<br />

<br />
<!-- source:end -->

## Lifecycle status

- `docs/lending/loan-statuses-overview.md`: updatedAt 2026-08-05T18:04:47.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/lending/loan-statuses-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/loan-statuses-overview | `84c03ea400db817e…` | 2026-08-05T18:04:47.000Z |

## Related knowledge units

- None.
