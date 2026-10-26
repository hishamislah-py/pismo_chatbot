---
ku_id: KU-CRED-calendar-management-strategies
title: Calendar management strategies (cycle closing and due dates)
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/calendar-management-strategies.md
  sha256: 3201d1da637e35258793e0e9cceb7561b26c9f641f661e1c3710aadc086ddbb0
  url: https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies
  role: primary_guide
  updated_at: '2026-07-28T16:51:38.000Z'
- path: docs/card-issuing/daily-cycle-closing-calendar-management-strategy.md
  sha256: f62d0e020b2f5261b10f3ad7e70fae90562c256f1877f6dc11bb24534fa0831d
  url: https://developers.pismo.io/pismo-docs/docs/daily-cycle-closing-calendar-management-strategy
  role: primary_guide
  updated_at: '2026-07-24T20:17:59.000Z'
- path: docs/card-issuing/daily-due-date-calendar-management-strategy.md
  sha256: c7c863e547d2ab225bcc2da5d9b2ee75a6fd9bb934593b7b68ed72429d4a3691
  url: https://developers.pismo.io/pismo-docs/docs/daily-due-date-calendar-management-strategy
  role: primary_guide
  updated_at: '2026-07-24T20:07:38.000Z'
- path: docs/card-issuing/fixed-cycle-closing-calendar-management-strategy.md
  sha256: 20c70a0b612c3ff1895d773d2300e5e5768f3276df22f8f43ecb3dea7710adff
  url: https://developers.pismo.io/pismo-docs/docs/fixed-cycle-closing-calendar-management-strategy
  role: primary_guide
  updated_at: '2026-07-24T18:42:59.000Z'
- path: docs/card-issuing/fixed-due-date-calendars.md
  sha256: 109230d111dae4a626e4bddbd1e03fae1b5bf498eb19952e218dc5606d83d64d
  url: https://developers.pismo.io/pismo-docs/docs/fixed-due-date-calendars
  role: primary_guide
  updated_at: '2026-06-05T15:26:59.000Z'
- path: docs/card-issuing/monthly-cycle-closing-calendar-management-strategy.md
  sha256: 456c1bcf577108f21476762d645635bf08a89077197a1bd11c23a1c9a0303010
  url: https://developers.pismo.io/pismo-docs/docs/monthly-cycle-closing-calendar-management-strategy
  role: primary_guide
  updated_at: '2026-07-24T18:56:59.000Z'
- path: docs/card-issuing/monthly-due-date-calendar-management-strategy.md
  sha256: 149fa25fcf6119fb518d32ffa83e392a21839dff32be8bab9c906f777eb3a189
  url: https://developers.pismo.io/pismo-docs/docs/monthly-due-date-calendar-management-strategy
  role: primary_guide
  updated_at: '2026-07-28T16:53:23.000Z'
- path: docs/card-issuing/weekly-cycle-closing-calendar-management-strategy.md
  sha256: c89eed664d9df43f871c2d572aa69311a7e1bcfa8534e2befc59081248ed1c5f
  url: https://developers.pismo.io/pismo-docs/docs/weekly-cycle-closing-calendar-management-strategy
  role: primary_guide
  updated_at: '2026-07-24T19:02:12.000Z'
- path: docs/card-issuing/weekly-due-date-calendar-management-strategy.md
  sha256: 410b33f54ba3854299b0ab787e69d42ffae9b99369c09c3b63d24ccaa1e13d84
  url: https://developers.pismo.io/pismo-docs/docs/weekly-due-date-calendar-management-strategy
  role: primary_guide
  updated_at: '2026-07-24T19:02:27.000Z'
- path: docs/card-issuing/reproducing-the-behavior-of-the-fixed-due-date-strategy.md
  sha256: ee817c31fa8713986470e28b3ba943842726b2fceef180a0b18deac56c685b8d
  url: https://developers.pismo.io/pismo-docs/docs/reproducing-the-behavior-of-the-fixed-due-date-strategy
  role: primary_guide
  updated_at: '2026-07-28T16:51:00.000Z'
operations:
- CreateProgramBasedOnTemplate
- CreateProgramBasedOnTemplateAsync
- CreateProgramCalendarStrategy
- UpdateAcountCalendarStrategy
- UpdateStatementsDueDate
- saveProgramDueDate
- updateProgramDueDate
- validate-v1-holiday
related_kus:
- KU-API-platform-setup-holidays--holidays-deprecated
- KU-API-platform-setup-programs--programs-part-01
- KU-API-revolving-credit-calendar-management--account-calendar-strategies
- KU-API-revolving-credit-calendar-management--program-calendar-strategies
- KU-API-revolving-credit-statements--due-date
- KU-CC-get-started-control-center
- KU-CRED-statement-cycle-dates
- KU-EVT-catalogue-balance
- KU-EVT-catalogue-other-domains
grouping_rationale: Overview plus each strategy variant.
---

# Calendar management strategies (cycle closing and due dates)

**KU ID:** `KU-CRED-calendar-management-strategies` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 10 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Overview plus each strategy variant.

Scope as stated in `docs/card-issuing/calendar-management-strategies.md`:

> The term **calendar** is used for the standard set of dates and time periods associated with a credit cycle. These include the due date, real due date, and cycle closing date. For more information, refer to [Credit cycle dates and time periods](https://developers.pismo.io/pismo-docs/docs/statement-cycle-dates).

Scope as stated in `docs/card-issuing/daily-cycle-closing-calendar-management-strategy.md`:

> To create a **daily cycle closing** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `DAILY_CYCLE_CLOSING`, and specify values for the following body parameters.

Scope as stated in `docs/card-issuing/daily-due-date-calendar-management-strategy.md`:

> To create a **daily due date** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `DAILY_DUE_DATE`, and specify values for the following body parameters.

Scope as stated in `docs/card-issuing/fixed-cycle-closing-calendar-management-strategy.md`:

> To create a **fixed cycle closing** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `FIXED_CYCLE_CLOSING`, and specify values for the following body parameters.

Scope as stated in `docs/card-issuing/fixed-due-date-calendars.md`:

> In the fixed due date calendar management strategy, the due date is fixed, and the Pismo platform uses it to calculate the cycle closing date. When you create a program using [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) or [Create program (async)](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplateasync), you set the `due_dates` field to an array of due date objects. When you create an account in the program, you assign one of these due date objects to it.

Scope as stated in `docs/card-issuing/monthly-cycle-closing-calendar-management-strategy.md`:

> To create a **monthy cycle closing** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `MONTHLY_CYCLE_CLOSING`, and specify values for the following body parameters.

Scope as stated in `docs/card-issuing/monthly-due-date-calendar-management-strategy.md`:

> To create a **monthly due date** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `MONTHLY_DUE_DATE`, and specify values for the following body parameters.

Scope as stated in `docs/card-issuing/weekly-cycle-closing-calendar-management-strategy.md`:

> To create a **weekly cycle closing** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `WEEKLY_CYCLE_CLOSING`, and specify values for the following body parameters.

Scope as stated in `docs/card-issuing/weekly-due-date-calendar-management-strategy.md`:

> To create a **weekly due date** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `WEEKLY_DUE_DATE`, and specify values for the following body parameters.

Scope as stated in `docs/card-issuing/reproducing-the-behavior-of-the-fixed-due-date-strategy.md`:

> Because the default [fixed due date calendar management strategy](https://developers.pismo.io/pismo-docs/docs/fixed-due-date-calendars) and the [program calendar strategies](https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies) are implemented differently on the Pismo platform, you can't revert an account back to using the default strategy after assigning a program calendar strategy to it. However, you can use the [Monthly due date calendar management strategy ](https://developers.pismo.io/pismo-docs/docs/monthly-due-date-calendar-management-strategy) to reproduce the behavior of the default strategy.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/calendar-management-strategies.md`: Calendar management strategies
- `docs/card-issuing/daily-cycle-closing-calendar-management-strategy.md`: Daily cycle closing calendar management strategy; Example
- `docs/card-issuing/daily-due-date-calendar-management-strategy.md`: Daily due date calendar management strategy; Example
- `docs/card-issuing/fixed-cycle-closing-calendar-management-strategy.md`: Fixed cycle closing calendar management strategy
- `docs/card-issuing/fixed-due-date-calendars.md`: Fixed due date calendar management strategy; Examples; Example 1; Example 2; Example 3
- `docs/card-issuing/monthly-cycle-closing-calendar-management-strategy.md`: Monthly cycle closing calendar management strategy
- `docs/card-issuing/monthly-due-date-calendar-management-strategy.md`: Monthly due date calendar management strategy
- `docs/card-issuing/weekly-cycle-closing-calendar-management-strategy.md`: Weekly cycle closing calendar management strategy
- `docs/card-issuing/weekly-due-date-calendar-management-strategy.md`: Weekly due date calendar management strategy
- `docs/card-issuing/reproducing-the-behavior-of-the-fixed-due-date-strategy.md`: Reproducing the behavior of the fixed due date strategy

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 8 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/calendar-management-strategies.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies · updatedAt: 2026-07-28T16:51:38.000Z

<!-- source:begin path=docs/card-issuing/calendar-management-strategies.md part=0-end -->

# Calendar management strategies

The term **calendar** is used for the standard set of dates and time periods associated with a credit cycle. These include the due date, real due date, and cycle closing date. For more information, refer to [Credit cycle dates and time periods](https://developers.pismo.io/pismo-docs/docs/statement-cycle-dates).

Their are two types of calendar management strategies available for use with your programs and accounts.

* **Fixed due date**—This is the default calendar management strategy. The due date is fixed, and the Pismo platform uses it to calculate the cycle closing date. The [Fixed due date calendar management strategy](https://developers.pismo.io/pismo-docs/docs/fixed-due-date-calendars) guide explains how to create due date objects for a program and assign them to accounts.
* **Program calendar strategy**—This is an alternative type of calendar strategy that doesn't use a program due date object. The following program calendar strategies are available.
  * [Fixed cycle closing](https://developers.pismo.io/pismo-docs/docs/fixed-cycle-closing-calendar-management-strategy)—Cycle closing date is fixed, and the Pismo platform uses it to calculate the due date.
  * [Monthly cycle closing](https://developers.pismo.io/pismo-docs/docs/monthly-cycle-closing-calendar-management-strategy)—Specify the cycle closing date as either a day of the month or an "nth" weekday of the month, and the Pismo platform uses it to calculate the due date. A single cycle can span multiple months from 1 to 12.
  * [Monthly due date](https://developers.pismo.io/pismo-docs/docs/monthly-due-date-calendar-management-strategy)—Specify the due date as either a day of the month or an nth weekday each month. The Pismo platform derives the cycle close date backward from the due date. A single cycle can span multiple months from 1 to 12.
  * [Weekly cycle closing](https://developers.pismo.io/pismo-docs/docs/weekly-cycle-closing-calendar-management-strategy)—Cycle closes on a specific weekday every n weeks. The Pismo platform derives the due date forward from the cycle close date.
  * [Weekly due date](https://developers.pismo.io/pismo-docs/docs/weekly-due-date-calendar-management-strategy)—Due date falls on a specific weekday every n weeks. The Pismo platform derives the cycle close date backward from the due date.
  * [Daily cycle closing](https://developers.pismo.io/pismo-docs/docs/daily-cycle-closing-calendar-management-strategy)—Cycle closes every n days. The Pismo platform derives the due date forward from the cycle close date.
  * [Daily due date](https://developers.pismo.io/pismo-docs/docs/daily-due-date-calendar-management-strategy)—Due date falls every N days. The Pismo platform derives the cycle close date backward from the due date.

<Callout icon="🚧" theme="warn">
  Once you assign a program calendar strategy to an account, it's not possible to revert the account back to using the default strategy. However, you can use a program calendar strategy to reproduce the behavior of the default strategy. For more information, refer to [Reproducing the behavior of the fixed due date strategy](https://developers.pismo.io/pismo-docs/docs/reproducing-the-behavior-of-the-fixed-due-date-strategy).
</Callout>

<br />
<!-- source:end -->

### Source 2: `docs/card-issuing/daily-cycle-closing-calendar-management-strategy.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/daily-cycle-closing-calendar-management-strategy · updatedAt: 2026-07-24T20:17:59.000Z

<!-- source:begin path=docs/card-issuing/daily-cycle-closing-calendar-management-strategy.md part=0-end -->

# Daily cycle closing calendar management strategy

To create a **daily cycle closing** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `DAILY_CYCLE_CLOSING`, and specify values for the following body parameters.

* **Interval in days between cycles.** Set this using the `every_x_days` field. The default value is 1, which creates a one-day cycle. However, you can set `every_x_days` to any integer between 1 and 365. For example, set `every_x_days` to 365 to create a cycle that spans one year.
* **Number of days between the cycle closing date and the due date.** Set this using the `days_between_cycle_closing_and_due_date` field.

After creating the management strategy, use the [Update account calendar strategy](https://developers.pismo.io/pismo-docs/reference/updateacountcalendarstrategy) endpoint to assign it to an account.

# Example

On March 3, you create a new program calendar strategy with the following settings.

* `strategy` = `DAILY_CYCLE_CLOSING`
* `every_x_days` = 5
* `days_between_cycle_closing_and_due_date` = 2

Now, suppose you wait until April 3 to attach the strategy to an account. The Pismo platform uses the following process to determine what to use for the first cycle closing date and due date for the account. (Use the table at the end to help you follow along.)

The Pismo platform starts calculating due dates on the day after the strategy is created. This is March 4, so the platform adds 5 to March 4 to get March 9 for the first possible cycle closing date. It adds 2 to March 9 to get March 11 for the first possible due date. However, these dates have already passed. (Remember, you didn't assign the strategy to the account until April 3.) The platform can't create a statement that's already closed, so these dates don't work.

Next, the platform adds 5 to March 9 to get March 14 for the next possible cycle closing date and adds 2 to that to get March 16 for the next possible due date. These dates are still in the past.

The platform keeps going like this until it get to a cycle closing date of April 3. This is the same day that you assigned the strategy to the account. The platform can't create a cycle and close it on the same day, so these dates also don't work.

Finally, the platform calculates a cycle closing date of April 8 and a due date of April 10. Both of these dates are after April 3, so they work. The platform starts generating statements for the account.

| Cycle closing date | Due date | Do these dates work?               |
| :----------------- | :------- | :--------------------------------- |
| March 9            | March 11 | No                                 |
| March 14           | March 16 | No                                 |
| March 19           | March 21 | No                                 |
| March 24           | March 26 | No                                 |
| March 29           | March 31 | No                                 |
| April 3            | April 5  | No (closing must be after April 3) |
| April 8            | April 10 | Yes (first statement)              |
| April 13           | April 15 | Yes (next statement)               |
| April 18           | April 29 | Yes (and so on)                    |
| ...                | ...      | ...                                |
<!-- source:end -->

### Source 3: `docs/card-issuing/daily-due-date-calendar-management-strategy.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/daily-due-date-calendar-management-strategy · updatedAt: 2026-07-24T20:07:38.000Z

<!-- source:begin path=docs/card-issuing/daily-due-date-calendar-management-strategy.md part=0-end -->

# Daily due date calendar management strategy

To create a **daily due date** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `DAILY_DUE_DATE`, and specify values for the following body parameters.

* **Interval in days between cycles.** Set this using the `every_x_days` field. The default value is 1, which creates a one-day cycle. However, you can set `every_x_days` to any integer between 1 and 365. For example, set `every_x_days` to 365 to create a cycle that spans one year.
* **Number of days between the cycle closing date and the due date.** Set this using the `days_between_cycle_closing_and_due_date` field.

After creating the management strategy, use the [Update account calendar strategy](https://developers.pismo.io/pismo-docs/reference/updateacountcalendarstrategy) endpoint to assign it to an account.

# Example

On March 3, you create a new program calendar strategy with the following settings.

* `strategy` = `DAILY_DUE_DATE`
* `every_x_days` = 5
* `days_between_cycle_closing_and_due_date` = 2

Now, suppose you wait until April 1 to attach the strategy to an account. The Pismo platform uses the following process to determine what to use for the first due date and cycle closing date for the account. (Use the table at the end to help you follow along.)

The Pismo platform starts calculating due dates on the day after the strategy is created. This is March 4, so the platform adds 5 to March 4 to get March 9 for the first possible due date. It subtracts 2 from that to get March 7 for the first possible cycle closing date. However, these dates have already passed. (Remember, you didn't assign the strategy to the account until April 1.) The platform can't create a statement that's already closed, so these dates don't work.

Next, the platform adds 5 to March 9 to get March 14 for the next possible due date and subtracts 2 from that to get March 12 for the next possible cycle closing date. These dates are still in the past.

The platform keeps going like this until it get to a due date of April 3. This date is after April 1. However, the corresponding cycle closing date is April 1. This is the same day that you assigned the strategy to the account. The platform can't create a cycle and close it on the same day, so these dates also don't work.

Finally, the platform calculates a due date of April 8 and a cycle closing date of April 6. Both of these dates are after April 1, so they work. The platform starts generating statements for the account.

| Cycle closing date | Due date | Do these dates work?               |
| :----------------- | :------- | :--------------------------------- |
| March 7            | March 9  | No                                 |
| March 12           | March 14 | No                                 |
| March 17           | March 19 | No                                 |
| March 22           | March 24 | No                                 |
| March 27           | March 29 | No                                 |
| April 1            | April 3  | No (closing must be after April 1) |
| April 6            | April 8  | Yes (first statement)              |
| April 11           | April 13 | Yes (next statement)               |
| April 16           | April 18 | Yes (and so on)                    |
| ...                | ...      | ...                                |
<!-- source:end -->

### Source 4: `docs/card-issuing/fixed-cycle-closing-calendar-management-strategy.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/fixed-cycle-closing-calendar-management-strategy · updatedAt: 2026-07-24T18:42:59.000Z

<!-- source:begin path=docs/card-issuing/fixed-cycle-closing-calendar-management-strategy.md part=0-end -->

# Fixed cycle closing calendar management strategy

To create a **fixed cycle closing** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `FIXED_CYCLE_CLOSING`, and specify values for the following body parameters.

* **Cycle closing date as a fixed day of the month.** For example, you could specify that the cycle closing date should be the tenth day of the month (`cycle_closing_day` = 10).
* **Number of days between the cycle closing date and the due date.** Set this using the `days_between_cycle_closing_and_due_date` field.

After creating the management strategy, use the [Update account calendar strategy](https://developers.pismo.io/pismo-docs/reference/updateacountcalendarstrategy) endpoint to assign it to an account.

<br />
<!-- source:end -->

### Source 5: `docs/card-issuing/fixed-due-date-calendars.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/fixed-due-date-calendars · updatedAt: 2026-06-05T15:26:59.000Z

<!-- source:begin path=docs/card-issuing/fixed-due-date-calendars.md part=0-end -->

# Fixed due date calendar management strategy

In the fixed due date calendar management strategy, the due date is fixed, and the Pismo platform uses it to calculate the cycle closing date. When you create a program using [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) or [Create program (async)](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplateasync), you set the `due_dates` field to an array of due date objects. When you create an account in the program, you assign one of these due date objects to it.

<Callout icon="📘" theme="info">
  You can also create a program using [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center). This method also enables you to set up an array of due date objects to be used by accounts in the program.
</Callout>

Each due date object contains a `day` field, which represents the day of the month for the due date. This is the nominal date by which the cardholder must pay the minimum amount due (MAD) to avoid accruing late charges. In some cases, a later date, called the **real due date** is used in place of the due date. For information about how the real due date is determined, refer to the [Credit cycle dates and time periods](https://developers.pismo.io/pismo-docs/docs/statement-cycle-dates) guide.

The day of the month that a cycle ends is called the [cycle closing date](https://developers.pismo.io/pismo-docs/docs/statement-cycle-dates). This is specified using the **Number of days before due date to set the closing date of the statement** program parameter, which you set in [Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center). The value of this parameter is subtracted from the due date to determine the cycle closing date. In other words,

`day` - **Number of days before due date to set the closing date of the statement** = cycle closing date

**Number of days before due date to set the closing date of the statement** represents the **grace period**—the number of days after the cycle closing that the customer has to pay the minimum amount due (MAD) without incurring a penalty.

It's possible to override the value of this default parameter for certain accounts. For example, you might wish to offer some customers a longer grace period than the program standard. To do this, set the`grace-period-days` field of the account's assigned due date object to the new value.

Since multiple accounts can share the same due date object, there are several possible scenarios. In the following scenarios, assume that you want to set the grace period of each account to X number of days.

* **You want to override the grace period for all the accounts that share a certain due date object.**—Use the [Update program due date](https://developers.pismo.io/pismo-docs/reference/updateprogramduedate) endpoint to set the `grace-period-days` field to X in the due date object that all the accounts share. In this case, you are done, because the due dates are already assigned to the accounts.
* **All other scenarios**—Create a new due date object for the account(s). Use the [Save program due date](https://developers.pismo.io/pismo-docs/reference/saveprogramduedate) endpoint to create a new due data object with its `grace-period-days` field set to X. Then use the [Change due date](https://developers.pismo.io/pismo-docs/reference/updatestatementsduedate) endpoint to assign the due date object to each account.

<Callout icon="📘" theme="info">
  Notes

  * It's best to set cycle date parameters at program and account initiation. You should only use the [Save program due date](https://developers.pismo.io/pismo-docs/reference/saveprogramduedate) , [Update program due date](https://developers.pismo.io/pismo-docs/reference/updateprogramduedate), and [Change due date](https://developers.pismo.io/pismo-docs/reference/updatestatementsduedate) endpoints to modify these parameters at a later date if absolutely necessary.
  * You can add "addition grace days" to give the cardholder extra time to pay the MAD. For more information, refer to [Adding "additional grace days".](https://developers.pismo.io/pismo-docs/docs/statement-cycle-dates#adding-additional-grace-days)
  * The fixed due date calendar management strategy is the default strategy. An alternative is to use a **program calendar strategy**. Program calendar strategies don't use the program due date objects. However, they still calculate a due date and the Pismo platform uses this due date in the same way it uses the program due date object for the fixed due date strategy. For more information, refer to [Fixed cycle closing calendar management strategy.](https://developers.pismo.io/pismo-docs/docs/fixed-cycle-closing-calendar-management-strategy)
</Callout>

# Examples

## Example 1

Suppose you have the following settings.

* **Number of days before due date to set the closing date of the statement** is set to 10.
* **Defines the number of additional grace days granted to the program** is set to 3.
* In the due date object assigned to the program, `day` = 5, and `grace_period_days` is not set.

For the month of June 2025, the due date is the fifth day of the month: 2025-06-05.

Since **Number of days before due date to set the closing date of the statement** = 10, the cycle closing date is 10 days prior to the due date, which would be 2025-05-26.

Since **Defines the number of additional grace days granted to the program** = 3, you calculate the real due date by adding 3 to the due date: 5 + 3 = 8. So, the real due date is 2025-06-08, assuming this is a business day. If it's not a business day, then the real due date is the next date after the 8th that *is* a business day.

## Example 2

Suppose you have the following settings.

* **Number of days before due date to set the closing date of the statement** is set to 10.
* **Defines the number of additional grace days granted to the program** is set to 3.
* In the due date object assigned to the program, `day` = 5, and `grace_period_days` = 7.

Setting `grace_period_days` to 7 overrides the setting in **Number of days before due date to set the closing date of the statement**, so you can ignore that parameter for this example.

For the month of June 2025, the due date is the 5th day of the month: 2025-06-05.

Since `grace-period-days` = 7, and **Number of days before due date to set the closing date of the statement** is ignored, the cycle closing date is 7 days prior to the due date, which would be 2025-05-30.

Since **Defines the number of additional grace days granted to the program** = 3, you calculate the real due date by adding 3 to the due date: 5 + 3 = 8. So, the real due date is 2025-06-8, assuming this is a business day. If it's not a business day, then the real due date is the next date after the 8th that *is* a business day.

## Example 3

Suppose you have the following settings.

* **Defines the number of additional grace days granted to the program** is set to 2.
* **Non-business days** is set to 67 (Saturday and Sunday).
* In the due date object assigned to the program, `day` = 5, and `grace_period_days` = 0.

For the month of June 2025, the due date is the 5th day of the month: 2025-06-05.

To get the real due date, you follow these steps.

1. 2025-06-05  + 2 additional grace days = 2025-06-07.
2. 2025-06-07 is a Saturday, so this date must be adjusted to the following Monday, which is 2025-06-09.
3. Run 2025-06-09 through the [Get holiday](https://developers.pismo.io/pismo-docs/reference/validate-v1-holiday) endpoint to find out if it's a holiday. Assume the call returns a non-empty response, and that `next_business_date` is 2025-06-10 in the response. This means 2025-06-09 is a holiday, and the next business day that isn't a holiday is 2025-06-10. So, the real due date is 2025-06-10.
<!-- source:end -->

### Source 6: `docs/card-issuing/monthly-cycle-closing-calendar-management-strategy.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/monthly-cycle-closing-calendar-management-strategy · updatedAt: 2026-07-24T18:56:59.000Z

<!-- source:begin path=docs/card-issuing/monthly-cycle-closing-calendar-management-strategy.md part=0-end -->

# Monthly cycle closing calendar management strategy

To create a **monthy cycle closing** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `MONTHLY_CYCLE_CLOSING`, and specify values for the following body parameters.

* **Cycle closing date, either as a fixed day of the month or as the nth weekday of each month.** For example, you could specify that the cycle closing date should be the tenth day of the month (`cycle_closing_day` = 10) or the second Monday of the month (`day_of_week` = `MONDAY` and `week_of_month` = 2).
* **Number of months that a cycle spans.** Set this using the `every_x_months` field. The default value is 1, which creates a one-month cycle. However, you can set `every_x_months` to any integer between 1 and 12. For example, set `every_x_months` to 12 to create a cycle that spans one year.
* **Number of days between the cycle closing date and the due date.** Set this using the `days_between_cycle_closing_and_due_date` field.

After creating the management strategy, use the [Update account calendar strategy](https://developers.pismo.io/pismo-docs/reference/updateacountcalendarstrategy) endpoint to assign it to an account.

<br />
<!-- source:end -->

### Source 7: `docs/card-issuing/monthly-due-date-calendar-management-strategy.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/monthly-due-date-calendar-management-strategy · updatedAt: 2026-07-28T16:53:23.000Z

<!-- source:begin path=docs/card-issuing/monthly-due-date-calendar-management-strategy.md part=0-end -->

# Monthly due date calendar management strategy

To create a **monthly due date** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `MONTHLY_DUE_DATE`, and specify values for the following body parameters.

* **Due day, either as a fixed day of the month or as the nth weekday of each month.** For example, you could specify the due day as the tenth day of the month (`due_day` = 10) or the second Monday of the month (`day_of_week` = `MONDAY` and `week_of_month` = 2).
* **Number of months that a cycle spans.** Set this using the `every_x_months` field. The default value is 1, which creates a one-month cycle. However, you can set `every_x_months` to any integer between 1 and 12. For example, set `every_x_months` to 12 to create a cycle that spans one year.
* **Number of days between the cycle closing date and the due date.** Set this using the `days_between_cycle_closing_and_due_date` field.

After creating the management strategy, use the [Update account calendar strategy](https://developers.pismo.io/pismo-docs/reference/updateacountcalendarstrategy) endpoint to assign it to an account.

<Callout icon="📘" theme="info">
  If you ever need to go back to the default behavior after you've applied a custom management strategy to an account, you can use the **monthly due date** calendar management strategy to reproduce that behavior. For more information, refer to the [Reproducing the behavior of the fixed due date strategy](https://developers.pismo.io/pismo-docs/docs/reproducing-the-behavior-of-the-fixed-due-date-strategy) guide.
</Callout>
<!-- source:end -->

### Source 8: `docs/card-issuing/weekly-cycle-closing-calendar-management-strategy.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/weekly-cycle-closing-calendar-management-strategy · updatedAt: 2026-07-24T19:02:12.000Z

<!-- source:begin path=docs/card-issuing/weekly-cycle-closing-calendar-management-strategy.md part=0-end -->

# Weekly cycle closing calendar management strategy

To create a **weekly cycle closing** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `WEEKLY_CYCLE_CLOSING`, and specify values for the following body parameters.

* **Cycle closing day as a fixed day of the month.** For example, you could specify the cycle closing day as the tenth day of the month (`day_of_week` = 10).
* **Interval in weeks between cycles.** Set this using the `every_x_weeks` field. The default value is 1, which creates a one-week cycle. However, you can set `every_x_weeks` to any integer between 1 and 52. For example, set `every_x_weeks` to 52 to create a cycle that spans one year.
* **Number of days between the cycle closing date and the due date.** Set this using the `days_between_cycle_closing_and_due_date` field.

After creating the management strategy, use the [Update account calendar strategy](https://developers.pismo.io/pismo-docs/reference/updateacountcalendarstrategy) endpoint to assign it to an account.

<br />
<!-- source:end -->

### Source 9: `docs/card-issuing/weekly-due-date-calendar-management-strategy.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/weekly-due-date-calendar-management-strategy · updatedAt: 2026-07-24T19:02:27.000Z

<!-- source:begin path=docs/card-issuing/weekly-due-date-calendar-management-strategy.md part=0-end -->

# Weekly due date calendar management strategy

To create a **weekly due date** calendar management strategy, run the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint with the `strategy` field set to `WEEKLY_DUE_DATE`, and specify values for the following body parameters.

* **Due day as a fixed day of the month.** For example, you could specify the due day as the tenth day of the month (`day_of_week` = 10).
* **Interval in weeks between cycles.** Set this using the `every_x_weeks` field. The default value is 1, which creates a one-week cycle. However, you can set `every_x_weeks` to any integer between 1 and 52. For example, set `every_x_weeks` to 52 to create a cycle that spans one year.
* **Number of days between the cycle closing date and the due date.** Set this using the `days_between_cycle_closing_and_due_date` field.

After creating the management strategy, use the [Update account calendar strategy](https://developers.pismo.io/pismo-docs/reference/updateacountcalendarstrategy) endpoint to assign it to an account.

<br />
<!-- source:end -->

### Source 10: `docs/card-issuing/reproducing-the-behavior-of-the-fixed-due-date-strategy.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/reproducing-the-behavior-of-the-fixed-due-date-strategy · updatedAt: 2026-07-28T16:51:00.000Z

<!-- source:begin path=docs/card-issuing/reproducing-the-behavior-of-the-fixed-due-date-strategy.md part=0-end -->

# Reproducing the behavior of the fixed due date strategy

<br />

Because the default [fixed due date calendar management strategy](https://developers.pismo.io/pismo-docs/docs/fixed-due-date-calendars) and the [program calendar strategies](https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies) are implemented differently on the Pismo platform, you can't revert an account back to using the default strategy after assigning a program calendar strategy to it. However, you can use the [Monthly due date calendar management strategy ](https://developers.pismo.io/pismo-docs/docs/monthly-due-date-calendar-management-strategy) to reproduce the behavior of the default strategy.

To do this, create a monthly due date calendar management strategy with the following settings.

* Set `due_day` to the fixed day of the month that you want to use for the due day.
* Set `every_x_months` to 1.
* Set `days_between_cycle_closing_and_due_date` to the number of days between the cycle closing date and the due date.

Use the [Update account calendar strategy](https://developers.pismo.io/pismo-docs/reference/updateacountcalendarstrategy) endpoint to assign it to an account.

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/programs/{programId}/calendar-strategies` | `CreateProgramCalendarStrategy` | Create program calendar strategy | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `PUT /v1/accounts/{accountId}/calendar-strategies` | `UpdateAcountCalendarStrategy` | Update account calendar strategy | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--account-calendar-strategies |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /programs/v2/programs/template` | `CreateProgramBasedOnTemplateAsync` | Create program (async) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `PATCH /statements-v2/v1/programs/{programId}/due-dates/{programDueDateId}` | `updateProgramDueDate` | Update program due date | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /statements-v2/v1/programs/{programId}/due-dates` | `saveProgramDueDate` | Save program due date | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `PUT /statements/v1/accounts/{accountId}/statements/due-date` | `UpdateStatementsDueDate` | Change due date | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /holidays-core/v1/holiday/validate` | `validate-v1-holiday` | Get holiday (deprecated) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-deprecated |

### Operation essentials

- **`POST /v1/programs/{programId}/calendar-strategies`** (`CreateProgramCalendarStrategy`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 202, 400, 500; error codes in examples `EX0002`, `GN0001`; events `balance-program-calendar-strategy-created-1`.
- **`PUT /v1/accounts/{accountId}/calendar-strategies`** (`UpdateAcountCalendarStrategy`): security `BearerAuth`; required parameters `accountId` (path), `x-tenant` (header); required body fields `program_calendar_strategy_id`; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events `balance-balance-account-change-1`.
- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /programs/v2/programs/template`** (`CreateProgramBasedOnTemplateAsync`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 201, 400, 404, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0031`, `EOA0030`, `EOA0009`, `EOA0008`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`PATCH /statements-v2/v1/programs/{programId}/due-dates/{programDueDateId}`** (`updateProgramDueDate`): security `BearerAuth`; required parameters `programId` (path), `programDueDateId` (path); required body fields `active`; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.
- **`POST /statements-v2/v1/programs/{programId}/due-dates`** (`saveProgramDueDate`): security `BearerAuth`; required parameters `Authorization` (header), `programId` (path); required body fields `day`, `active`; response statuses 201, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.
- **`PUT /statements/v1/accounts/{accountId}/statements/due-date`** (`UpdateStatementsDueDate`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `id`; response statuses 200, 400, 404, 409, 500; error codes in examples `GN0001`; events none listed.
- **`POST /holidays-core/v1/holiday/validate`** (`validate-v1-holiday`): security `S2SAuthentication`; required parameters none declared; required body fields `date`, `division_id`; response statuses 200, 400, 401, 404, 500; error codes in examples `EHLD0016`, `EHLD0050`, `EHLD0028`, `EHLD0052`, `EHLD0001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `UpdateAcountCalendarStrategy` | `balance-balance-account-change-1` |
| `CreateProgramCalendarStrategy` | `balance-program-calendar-strategy-created-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |
| `CreateProgramBasedOnTemplateAsync` | `programs-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/calendar-management-strategies.md`: updatedAt 2026-07-28T16:51:38.000Z.
- `docs/card-issuing/daily-cycle-closing-calendar-management-strategy.md`: updatedAt 2026-07-24T20:17:59.000Z.
- `docs/card-issuing/daily-due-date-calendar-management-strategy.md`: updatedAt 2026-07-24T20:07:38.000Z.
- `docs/card-issuing/fixed-cycle-closing-calendar-management-strategy.md`: updatedAt 2026-07-24T18:42:59.000Z.
- `docs/card-issuing/fixed-due-date-calendars.md`: updatedAt 2026-06-05T15:26:59.000Z.
- `docs/card-issuing/monthly-cycle-closing-calendar-management-strategy.md`: updatedAt 2026-07-24T18:56:59.000Z.
- `docs/card-issuing/monthly-due-date-calendar-management-strategy.md`: updatedAt 2026-07-28T16:53:23.000Z.
- `docs/card-issuing/weekly-cycle-closing-calendar-management-strategy.md`: updatedAt 2026-07-24T19:02:12.000Z.
- `docs/card-issuing/weekly-due-date-calendar-management-strategy.md`: updatedAt 2026-07-24T19:02:27.000Z.
- `docs/card-issuing/reproducing-the-behavior-of-the-fixed-due-date-strategy.md`: updatedAt 2026-07-28T16:51:00.000Z.
- Links to `validate-v1-holiday`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Holidays.yaml`.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/calendar-management-strategies.md` | whole document | https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies | `3201d1da637e3525…` | 2026-07-28T16:51:38.000Z |
| `docs/card-issuing/daily-cycle-closing-calendar-management-strategy.md` | whole document | https://developers.pismo.io/pismo-docs/docs/daily-cycle-closing-calendar-management-strategy | `f62d0e020b2f5261…` | 2026-07-24T20:17:59.000Z |
| `docs/card-issuing/daily-due-date-calendar-management-strategy.md` | whole document | https://developers.pismo.io/pismo-docs/docs/daily-due-date-calendar-management-strategy | `c7c863e547d2ab22…` | 2026-07-24T20:07:38.000Z |
| `docs/card-issuing/fixed-cycle-closing-calendar-management-strategy.md` | whole document | https://developers.pismo.io/pismo-docs/docs/fixed-cycle-closing-calendar-management-strategy | `20c70a0b612c3ff1…` | 2026-07-24T18:42:59.000Z |
| `docs/card-issuing/fixed-due-date-calendars.md` | whole document | https://developers.pismo.io/pismo-docs/docs/fixed-due-date-calendars | `109230d111dae4a6…` | 2026-06-05T15:26:59.000Z |
| `docs/card-issuing/monthly-cycle-closing-calendar-management-strategy.md` | whole document | https://developers.pismo.io/pismo-docs/docs/monthly-cycle-closing-calendar-management-strategy | `456c1bcf577108f2…` | 2026-07-24T18:56:59.000Z |
| `docs/card-issuing/monthly-due-date-calendar-management-strategy.md` | whole document | https://developers.pismo.io/pismo-docs/docs/monthly-due-date-calendar-management-strategy | `149fa25fcf6119fb…` | 2026-07-28T16:53:23.000Z |
| `docs/card-issuing/weekly-cycle-closing-calendar-management-strategy.md` | whole document | https://developers.pismo.io/pismo-docs/docs/weekly-cycle-closing-calendar-management-strategy | `c89eed664d9df43f…` | 2026-07-24T19:02:12.000Z |
| `docs/card-issuing/weekly-due-date-calendar-management-strategy.md` | whole document | https://developers.pismo.io/pismo-docs/docs/weekly-due-date-calendar-management-strategy | `410b33f54ba38542…` | 2026-07-24T19:02:27.000Z |
| `docs/card-issuing/reproducing-the-behavior-of-the-fixed-due-date-strategy.md` | whole document | https://developers.pismo.io/pismo-docs/docs/reproducing-the-behavior-of-the-fixed-due-date-strategy | `ee817c31fa871398…` | 2026-07-28T16:51:00.000Z |

## Related knowledge units

- `KU-API-platform-setup-holidays--holidays-deprecated` — API reference: Platform setup - Holidays — Holidays (deprecated)
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-revolving-credit-calendar-management--account-calendar-strategies` — API reference: Revolving credit - Calendar management — Account calendar strategies
- `KU-API-revolving-credit-calendar-management--program-calendar-strategies` — API reference: Revolving credit - Calendar management — Program calendar strategies
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CRED-statement-cycle-dates` — Credit cycle dates and time periods
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
