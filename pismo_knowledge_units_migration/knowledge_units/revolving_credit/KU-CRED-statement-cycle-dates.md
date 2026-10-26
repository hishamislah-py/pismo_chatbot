---
ku_id: KU-CRED-statement-cycle-dates
title: Credit cycle dates and time periods
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/statement-cycle-dates.md
  sha256: 8d04d31453406baa039a5df89977f8c770aa021c7936ef1a98e6416ecd08f8d2
  url: https://developers.pismo.io/pismo-docs/docs/statement-cycle-dates
  role: primary_guide
  updated_at: '2026-06-08T16:33:55.000Z'
operations:
- get-v2-holidays
related_kus:
- KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat
- KU-CRED-calendar-management-strategies
grouping_rationale: single source page
---

# Credit cycle dates and time periods

**KU ID:** `KU-CRED-statement-cycle-dates` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/statement-cycle-dates.md`:

> Credit cycles have several important dates and time periods associated with them.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/statement-cycle-dates.md`: Credit cycle dates and time periods; Adding additional grace days; Calculating the real due date

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/statement-cycle-dates.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/statement-cycle-dates · updatedAt: 2026-06-08T16:33:55.000Z

<!-- source:begin path=docs/card-issuing/statement-cycle-dates.md part=0-end -->

# Credit cycle dates and time periods

Credit cycles have several important dates and time periods associated with them.

* **Cycle closing date**—This is the day of the month that the cycle closes. If the cardholder initiates a debit or credit after this date, it goes on the next cycle. How this day is set depends on the [calendar management strategy](https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies) used.
* **Due date**—This is the *nominal* date by which the cardholder must pay at least the minimum amount due (MAD) in order to avoid late charges. How the due date is set depends on the [calendar management strategy](https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies) used.
* **Grace period**—The period between the cycle closing date and the due date.
* **Real due date**—This is the *actual* date by which the cardholder must pay the MAD to avoid late charges. For example, if a due date falls on a non-business day, such as a weekend or a public holiday, the cardholder should be able to pay on the next business day without incurring a penalty. An institution might also choose to [add  additional grace days](https://developers.pismo.io/pismo-docs/docs/statement-cycle-dates#adding-additional-grace-days) after the due date. For more information, refer to [Calculating the real due date](https://developers.pismo.io/pismo-docs/docs/statement-cycle-dates#calculating-the-real-due-date).

<Callout icon="📘" theme="info">
  The real due date can be the same as the due date if the due date does not fall on a non-business day, and no additional grace days are defined.
</Callout>

# Adding additional grace days

You have the option of giving the cardholder some extra time after the due date to pay the MAD without incurring late charges. To do this, set the program parameter **Defines the number of additional grace days granted to the program**. There's usually no need to let account holders know about this extra time—it's just a way of giving them a little more leeway before they start to accrue charges, effectively extending the grace period. Officially, though, the grace period still refers only to the period between the cycle closing date and the due date.

<Callout icon="📘" theme="info">
  **Defines the number of additional grace days granted to the program**works with all [calendar management strategies](https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies).
</Callout>

# Calculating the real due date

To calculate the real due date, the Pismo platform must take into account:

* **Weekends**—Countries differ in how they define weekends. Use the **Non-business days** program parameter to set which days of the week your program should treat as non-business days. For example, if you want to designate Saturday and Sunday as the weekend, set **Non-business days** to 67, since Saturday and Sunday are the sixth and seventh day of the week, respectively.
* **Public holidays**—Use the [List holidays](https://developers.pismo.io/pismo-docs/reference/get-v2-holidays) endpoint to define public holidays.
* **Additional grace days**—You can add additional grace days by setting the program parameter **Defines the number of additional grace days granted to the program** to a number above zero. This gives customers an extra few days after their designated due date before interest and penalties start accruing.

The Pismo platform uses the following steps to calculate the real due date.

1. The platform adds the value of any additional grace days to the due date.
2. If the result of the last step is a business day, this is the real due date. If it's a non-business day, the real due date is the next available business day.

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /holidays-core/v2/holiday` | `get-v2-holidays` | List holidays (deprecated) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat |

### Operation essentials

- **`GET /holidays-core/v2/holiday`** (`get-v2-holidays`): security `S2SAuthentication`; required parameters `administrativeDivisionId` (query); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples `EHLD0016`, `EHLD0001`; events none listed.

## Lifecycle status

- `docs/card-issuing/statement-cycle-dates.md`: updatedAt 2026-06-08T16:33:55.000Z.
- Links to `get-v2-holidays`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Holidays.yaml`.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/statement-cycle-dates.md` | whole document | https://developers.pismo.io/pismo-docs/docs/statement-cycle-dates | `8d04d31453406baa…` | 2026-06-08T16:33:55.000Z |

## Related knowledge units

- `KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat` — API reference: Platform setup - Holidays — Holidays v2 - Transaction banking (deprecated)
- `KU-CRED-calendar-management-strategies` — Calendar management strategies (cycle closing and due dates)
