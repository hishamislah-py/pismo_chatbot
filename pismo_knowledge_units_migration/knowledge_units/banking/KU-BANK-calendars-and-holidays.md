---
ku_id: KU-BANK-calendars-and-holidays
title: Calendars, holidays and posting transactions on holidays in transaction banking
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/calendars-and-holidays-in-transaction-banking.md
  sha256: 878e704cb20b3089055897aed9099f85cc29ea82639230798da3046cfd0d7e17
  url: https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-transaction-banking
  role: primary_guide
  updated_at: '2026-04-24T21:57:10.000Z'
- path: docs/core-banking/posting-transactions-on-holidays.md
  sha256: 045a6b02bf22cebe6faf5ac1a580d72e4f2356b9e529e9f200f5c99e7127f5d3
  url: https://developers.pismo.io/pismo-docs/docs/posting-transactions-on-holidays
  role: primary_guide
  updated_at: '2026-04-28T17:14:26.000Z'
operations:
- corporate-v2-post-confirm-payments
- corporate-v2-post-payments
- patch-division-v2
- post-bulk-settlement
- post-division-v2
- post-v2-admin-division
- post-v2-holiday
related_kus:
- KU-API-banking-transaction-banking--bulk-settlement
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated
- KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
grouping_rationale: One topic.
---

# Calendars, holidays and posting transactions on holidays in transaction banking

**KU ID:** `KU-BANK-calendars-and-holidays` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: One topic.

Scope as stated in `docs/core-banking/calendars-and-holidays-in-transaction-banking.md`:

> The Pismo platform, by default, supports uninterrupted transactions. However, banks often need to limit transactions on certain days, such as holidays, weekends, non-working days, and so on. The Pismo platform defines a holiday as any day the bank or financial institution does not allow transactions. Errors setting up holidays can prevent customers or businesses from accessing funds or executing payments, so careful planning of holidays and calendars are essential. Banks require a detailed calendar, marking out various types of days as holidays, to ensure proper transaction processing. To aid this process, the Pismo platform enables banks to define administrative divisions and assign division-specific holidays.

Scope as stated in `docs/core-banking/posting-transactions-on-holidays.md`:

> When posting transactions, all configured calendars, holidays, and parameters are taken into consideration. The transaction types available for posting on holidays include:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/calendars-and-holidays-in-transaction-banking.md`: Calendars and holidays in transaction banking; Creating a calendar; Creating administrative divisions; Setting up holidays within administrative divisions; Linking administrative divisions; Calendar inheritance
- `docs/core-banking/posting-transactions-on-holidays.md`: Posting transactions on holidays; Parameters; Future-business-dated transactions; Holiday transaction handling; Cycle closing; Submitting future-business-dated transactions; Understanding regular clearing; Impacted balances; Impacted balance history; Credit and debit transactions; Credit and debit clearing; Understanding instant clearing; How instant clearing works

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/calendars-and-holidays-in-transaction-banking.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-transaction-banking · updatedAt: 2026-04-24T21:57:10.000Z

<!-- source:begin path=docs/core-banking/calendars-and-holidays-in-transaction-banking.md part=0-end -->

# Calendars and holidays in transaction banking

The Pismo platform, by default, supports uninterrupted transactions. However, banks often need to limit transactions on certain days, such as holidays, weekends, non-working days, and so on. The Pismo platform defines a holiday as any day the bank or financial institution does not allow transactions. Errors setting up holidays can prevent customers or businesses from accessing funds or executing payments, so careful planning of holidays and calendars are essential. Banks require a detailed calendar, marking out various types of days as holidays, to ensure proper transaction processing. To aid this process, the Pismo platform enables banks to define administrative divisions and assign division-specific holidays.

Here are some factors to keep in mind when setting up holidays and weekends on the Pismo platform.

| Factors to consider      | Description and impact                                                                                                                                                                                                                                                                                                                                                                                                     |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Country's legal holidays | Days designated as holidays by the country's government.                                                                                                                                                                                                                                                                                                                                                                   |
| Weekends                 | Weekends are defined differently in different countries. Different days might be included, and the number of days in a weekend can also vary.                                                                                                                                                                                                                                                                              |
| Regional holidays        | Certain holidays might be observed only in a specific state or region.                                                                                                                                                                                                                                                                                                                                                     |
| Customer considerations  | A holiday might be defined for the convenience of customers. For example, consider a bank that is typically closed on Saturdays and Sundays. If a bank holiday occurs on a Friday, the bank can choose to close its branch on the following Monday. Additionally, the bank can configure to allow transactions to proceed without any interruptions over the weekend, ensuring access to funds for customers at all times. |
| Business considerations  | When setting up holidays, various business considerations might come into play. For example, if a bank holiday coincides with a day when many businesses are closed, the bank might consider extending its operating hours the following day, allowing businesses to deposit their cash.                                                                                                                                   |
| Transactions             | For a bank or branch, there is a need to take into account transactions such as interest accruals and maturities. If such transactions coincide with a day when the bank or branch is closed, the bank staff should be allowed to configure their system to process them on a date before, after, or even on the closure date.                                                                                             |

# Creating a calendar

For transaction banking, **an administrative division functions as a calendar**. The process of setting holidays on your calendar involves these steps.

1. [Creating administrative divisions](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-transaction-banking#creating-administrative-divisions).
2. [Setting up holidays within administrative divisions](#setting-up-holidays-within-administrative-divisions).
3. [Linking the administrative divisions](#linking-administrative-divisions).

## Creating administrative divisions

Set up administrative divisions using the [Create administrative division](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) endpoint. This provides you with the flexibility to shape your calendar structure to match that of your administrative divisions. For example, if your divisions are organized as **Region > Country > State > City > Branch**, you can configure your calendar in a similar manner. This approach is beneficial as it accommodates regional, national, state, and even branch-specific holidays. However, it's crucial to create your division structure prior to creating calendars. This is necessary because of the administrative division's inherent hierarchy, in which holidays trickle down from parent to child calendars.

## Setting up holidays within administrative divisions

Use [Create holiday](https://developers.pismo.io/pismo-docs/reference/post-v2-holiday) to establish holidays within an administrative division. If a holiday is not specifically configured using the transaction banking [parameters](https://developers.pismo.io/pismo-docs/docs/posting-transactions-on-holidays#parameters), the Pismo platform defaults to the settings in the administrative division metadata when processing transactions. Note that **the holiday metadata always takes precedence over the administrative division settings**.

## Linking administrative divisions

After establishing administrative divisions and holidays, you can connect them with their respective transaction banking divisions. This connection enables your divisions to "inherit" the holidays from the linked administrative division. To set up and manage these connections, use the [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) or [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoints. In both endpoints, you must provide the `administrative_division_id` field with the correct administrative division ID.

## Calendar inheritance

The following diagram provides a visual representation of how divisions inherit holidays from the administrative divisions they are linked to.

<Image alt="Figure 1: Calendar inheritance" align="center" width="80% " src="https://files.readme.io/268fbbfdedef33a7ae0189cf50705044813cfb860a7971dd93de9facad6fa463-calendar_inheritance.png">
  Figure 1: Calendar inheritance
</Image>

In Figure 1, the parent division is linked to the parent administrative division. This means that Account 1 in this division observes Holiday 1. The child division, on the other hand, is linked to the child administrative division, so Account 2 in this division inherit Holidays 1 and 2 from both the parent and child administrative divisions.

> 🚧 A child division not linked to any administrative division does not inherit holidays from its parent.
<!-- source:end -->

### Source 2: `docs/core-banking/posting-transactions-on-holidays.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/posting-transactions-on-holidays · updatedAt: 2026-04-28T17:14:26.000Z

<!-- source:begin path=docs/core-banking/posting-transactions-on-holidays.md part=0-end -->

# Posting transactions on holidays

When posting transactions, all configured calendars, holidays, and parameters are taken into consideration. The transaction types available for posting on holidays include:

* Regular posting
* Back-dated transaction
* Future-dated transaction
* Scheduled payment
* Earmark
* Multi-leg payment
* Bulk payment

For back-dated transactions, you must provide `business_date` and `payment_datetime` fields in [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) with a past date. For future-dated transactions, you can provide `business_date` and `payment_datetime` or specify desired parameter values in the metadata fields of [administrative division](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) or [holidays](https://developers.pismo.io/pismo-docs/reference/post-v2-holiday). Note that the parameters set in the holiday or administrative division metadata can affect transaction approval as well as posting dates.

# Parameters

To process dated transactions, you must specify the following parameters in the metadata when creating an administrative division or setting up holidays. Note that the metadata object does not have schema validation, so when there's a typographical error or a field isn't sent, the parameter value defaults to `false`.

| Parameter name               | Data type | Purpose                                                                                                                                                                                                                                      |
| :--------------------------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `defer_transaction`          | boolean   | Indicates if transactions that occur on a holiday are deferred to the next business day. If not specified, defaults to `false` and transactions are not deferred.                                                                            |
| `deny_business_date`         | boolean   | Determines whether transactions with a business date on a holiday are rejected. Defaults to `false`, permitting such transactions if not specified.                                                                                          |
| `deny_value_date`            | boolean   | Specifies whether to reject transactions with `payment_datetime` on a holiday. If not specified, defaults to `false`, allowing such transactions.                                                                                            |
| `instant_clearing`           | boolean   | Determines whether balances are immediately affected when a future business transaction is posted on a holiday. Defaults to `false`, indicating that if left unspecified, such transactions are allowed.                                     |
| `skip_cycle_closing`         | boolean   | Defines whether cycle closing is skipped on non-business days. If not specified, defaults to `false` and cycle closing is executed as usual.                                                                                                 |
| `reject_back_value_dating`   | boolean   | Prevents back‑value‑dated transactions for the target when set to `true`. If the provided `payment_datetime` back-values the transaction, and `reject_back_value_dating` is enabled, the Pismo platform rejects the transaction.             |
| `reject_future_value_dating` | boolean   | Blocks future value‑dated transactions for the target when set to `true`. If the provided `payment_datetime` sets the transaction to a future value and `reject_future_value_dating` is enabled, the Pismo platform rejects the transaction. |

# Future-business-dated transactions

To configure future business dated transactions on holidays, you add the following boolean parameters to the administrative [division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) or [holiday](https://developers.pismo.io/pismo-docs/reference/post-v2-holiday) metadata. By default, these parameters are set to `false`:

* `defer_transaction`
* `deny_business_date`
* `deny_value_date`
* `reject_future_value_dating`

<Callout icon="📘" theme="info">
  **Notes**

  * The settings designated for holidays always supersede those in the administrative division.
  * If you do not specify a value for `reject_future_value_dating`, the Pismo platform treats it as `null`, which is equivalent to `false`.
</Callout>

## Holiday transaction handling

If a transaction occurs on a holiday with defined holiday metadata parameters, **these parameters take precedence over identical ones in the administrative division metadata**. The Pismo platform uses the administrative division metadata for holidays when there is no associated holiday metadata or when the day is not included in the `working_day` array in the [administrative division](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division).

### Cycle closing

To configure how [cycle closing](https://developers.pismo.io/pismo-docs/docs/managing-grace-period) and transactions respond to holidays and weekends, you must set `skip_cycle_closing` to either `true` or `false` in the metadata field when setting up [administrative divisions](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) or [holidays](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division). This enables the system to determine whether to run a cycle closing or evaluate if a particular transaction is permissible.

## Submitting future-business-dated transactions

There are two methods to submit a future business-dated transaction. One approach is to designate the next business date in the payment request's `business_date` field (in [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)). Another method is to set the following parameters and their corresponding values in the metadata field of [Create holiday](https://developers.pismo.io/pismo-docs/reference/post-v2-holiday). For example:

* `deny_business_date` = `false`
* `defer_transaction` = `true`

With this configuration, any transactions posted on holidays or weekends are automatically deferred to the next  business day.

# Understanding regular clearing

Transactions scheduled for future business dates that undergo regular clearing (as opposed to instant clearing) require confirmation on the settlement date. You can use [Confirm payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-confirm-payments) or [Request bulk settlements](https://developers.pismo.io/pismo-docs/reference/post-bulk-settlement) to confirm these transactions. Running balances and balance history are impacted only after the transaction has been successfully cleared.

## Impacted balances

Credit or debit transactions impact these balances respectively.

| Transaction type    | Impacted balances       |
| ------------------- | ----------------------- |
| Credit transactions | Ledger balance          |
|                     | Uncleared funds balance |
|                     |                         |
| Debit transactions  | Ledger balance          |
|                     | Uncleared funds balance |
|                     | Available balance       |

## Impacted balance history

### Credit and debit transactions

Different process days for credit and debit transactions impact different types of balance.

| Transaction process | Process date                   | Impacted balances       |
| ------------------- | ------------------------------ | ----------------------- |
| Credit transactions | Post date                      | None                    |
|                     | Between post and business date | None                    |
|                     | Business date                  | Ledger balance          |
|                     |                                | Uncleared funds balance |
|                     |                                |                         |
| Debit transactions  | Post date                      | None                    |
|                     | Between post and business date | None                    |
|                     | Business date                  | Ledger balance          |
|                     |                                | Uncleared funds balance |
|                     |                                | Available balance       |

### Credit and debit clearing

The processing dates of credits and debits can affect how these are applied to balances. Note that both credit and debit clearing transactions require calling [Confirm payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-confirm-payments) or [Request bulk settlement](https://developers.pismo.io/pismo-docs/reference/post-bulk-settlement) to confirm transactions.

| Transaction process | Process date                            | Impacted balances and amount | Resulting amount       |
| ------------------- | --------------------------------------- | ---------------------------- | :--------------------- |
| Credit clearing     | After confirmation on the business date | Ledger balance               | Same as ledger balance |
|                     |                                         | Uncleared funds balance      | Amount decreased       |
|                     |                                         | Book balance                 | Amount increased       |
|                     |                                         | Available balance            | Amount increased       |
|                     |                                         | Value-dated balance          | Amount increased       |
|                     |                                         | Credit or debit balance      |                        |
|                     |                                         |                              |                        |
| Debit clearing      | After confirmation on the business date | Ledger balance               | Same as ledger balance |
|                     |                                         | Uncleared funds balance      | Amount increased       |
|                     |                                         | Book balance                 | Amount decreased       |
|                     |                                         | Value-dated balance          | Amount decreased       |
|                     |                                         | Credit or debit balance      |                        |

<Callout icon="📘" theme="info">
  **Note**

  If a transaction is not cleared within 10 days, the transaction is canceled and all balance impacts are reverted.
</Callout>

# Understanding instant clearing

Contrary to regular clearing, instant clearing does not require confirmation on the settlement date, because the funds are immediately accessible upon posting. Balances impacted by instant clearing include:

* Ledger balance
* Book balance
* Available balance
* Value-dated balance
* Credit or debit balance

For balance history, process dates have an impact on different balance types.

| Process date                   | Impacted balances       |
| ------------------------------ | ----------------------- |
| Post date                      | None                    |
| Between post and business date | None                    |
| Business date                  | Ledger balance          |
|                                | Book balance            |
|                                | Available balance       |
|                                | Value-dated balance     |
|                                | Credit or debit balance |

For dated transactions, include the `business_date` and `payment_datetime` fields in [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) with future dates. Be aware of holiday or administrative division metadata parameters, as they can affect transaction approval or posting date.

To keep the [value-dated balance](https://www.investopedia.com/terms/v/valuedate.asp#:~:text=A%20value%20date%20refers%20to,is%20fully%20cleared%20and%20settled.) in the balance history updated for weekends and maintain the running balance for available, book, and ledger balances, you must specify a value in `payment_datetime` of [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments). The value must align with the cycle closing date (`skip_cycle_closing`), and its timestamp must correspond to either the present or some time in the past, but never a future date.

## How instant clearing works

Specifying either `true` or `false` in the `instant_clearing` field in [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) determines whether the balances are affected immediately at the time of transaction posting or on the settlement date.

To post a future business-dated transaction with instant clearing, the `instant_clearing` field in the request must be set to `true`. If this field is omitted, the default value becomes `false`, implying that the future business-dated transaction undergoes regular clearing.

You can also post future business-dated transactions by specifying `instant_clearing` = `true` in the metadata field of [Create administrative division](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) or [Create holiday](https://developers.pismo.io/pismo-docs/reference/post-v2-holiday). In such instances, all future business transactions are instantly settled for the specified administrative division or on the defined holiday. Note that the `instant_clearing` field in a [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) request always overrides both the holiday and administrative division configurations.

<Callout icon="📘" theme="info">
  **Note**

  The Pismo platform only checks the `instant_clearing` parameter for future business-dated transactions and future business and back value-dated transactions, the parameter is ignored in all other cases.
</Callout>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /divisions-core/v2/administrative-division` | `post-v2-admin-division` | Create administrative division (deprecated) | `api-specs/Platform_setup_-_Divisions.yaml` | **yes** | KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated |
| `POST /holidays-core/v2/holiday` | `post-v2-holiday` | Create holiday (deprecated) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat |
| `POST /corporate/v2/divisions` | `post-division-v2` | Create division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `PATCH /corporate/v2/divisions/{divisionCode}` | `patch-division-v2` | Update division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `POST /corporate/v2/payments` | `corporate-v2-post-payments` | Post payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `POST /corporate/v2/payments/confirm` | `corporate-v2-post-confirm-payments` | Confirm payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `POST /corporate/v1/bulk-settlement` | `post-bulk-settlement` | Request bulk settlement | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-settlement |

### Operation essentials

- **`POST /divisions-core/v2/administrative-division`** (`post-v2-admin-division`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`; response statuses 201, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /holidays-core/v2/holiday`** (`post-v2-holiday`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `holiday_date`; response statuses 201, 400, 401, 404, 500; error codes in examples `EHLD0016`, `EHLD0028`, `EHLD0030`, `EHLD0031`, `EHLD0027`, `EHLD0001`; events none listed.
- **`POST /corporate/v2/divisions`** (`post-division-v2`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `hierarchy_id`, `level_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WDIV0015`, `WDIV0011`, `WDIV0005`, `WDIV0007`, `WDIV0006`, `WDIV0012`, `WDIV0018`, `WDIV0019`, `WDIV0017`, `WDIV0016`, `ECMN9999`; events `corporate-division-creation-2`.
- **`PATCH /corporate/v2/divisions/{divisionCode}`** (`patch-division-v2`): security `BearerAuth`; required parameters `divisionCode` (path); required body fields none declared; response statuses 204, 400, 401, 403, 404, 500; error codes in examples `WDIV0015`, `WDIV0011`, `WDIV0005`, `WDIV0007`, `WDIV0006`, `WDIV0008`, `WDIV0009`, `WDIV0010`, `WDIV0012`, `WDIV0018`, `WDIV0019`, `WDIV0002`, `WDIV0017`, `ECMN9999`; events `corporate-division-change-2`.
- **`POST /corporate/v2/payments`** (`corporate-v2-post-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`; response statuses 201, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WPMT0017`, `WPMT0011`, `WPMT0053`, `WPMT0018`, `WPMT0029`, `WPMT0030`, `WPMT0031`, `WPMT0062`, `WPMT0063`, `WCAC0010`, `WPMT0001`, `WPMT0061`, `WPMT0015`, `WPMT0016`, `WPMT0003`, `WPMT0004`, `WPMT0005`, `WPMT0006`, `WPMT0009`, `WPMT0010`, `WPMT0021`, `WEAM0008`, `WEAM0006`, `WPMT0050`, `WEAM0017`, `WEAM0019`, `WPMT0022`, `WPMT0023`, `WPMT0024`, `WPMT0025`, `WPMT0026`, `WCMN0002`, `WPMT0028`, `WPMT0045`, `WPMT0049`, `WPMT0036`, `WPMT0044`, `WPMT0051`, `WPMT0035`, `WPMT0046`, `WPMT0054`, `WPMT0055`, `WPMT0056`, `WPMT0058`, `WPMT0008`, `WPMT0014`, `WPMT0019`, `WCAC0002`, `WCAC0012`, `WPMT0002`, `WCAC0001`, `WEAM0007`, `WPMT0007`, `WPMT0052`, `WEAM0049`, `WPMT0047`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`POST /corporate/v2/payments/confirm`** (`corporate-v2-post-confirm-payments`): security `BearerAuth`; required parameters none declared; required body fields `original_tracking_id`, `tracking_id`; response statuses 201, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WPMT0017`, `WPMT0018`, `WPMT0001`, `WPMT0061`, `WPMT0003`, `WPMT0004`, `WPMT0028`, `WPMT0038`, `WPMT0039`, `WPMT0044`, `WPMT0049`, `WCAC0001`, `WPMT0037`, `WPMT0007`, `WPMT0052`, `WPMT0047`, `WPMT0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `platform-authorization-platform-authorization-1`.
- **`POST /corporate/v1/bulk-settlement`** (`post-bulk-settlement`): security `BearerAuth`; required parameters none declared; required body fields `operation_type`, `settlement_date`, `division_code`, `bulk_id`; response statuses 202, 400, 401, 403, 409, 429, 500; error codes in examples `WSTM0001`, `WSTM0002`, `WSTM0003`, `WSTM0004`, `WSTM0005`, `WSTM0006`, `WSTM0010`, `WSTM0011`, `WSTM0007`, `WSTM0009`, `WSTM0008`, `ECMN9999`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-v2-post-confirm-payments` | `account-balances-balance-change-1` |
| `corporate-v2-post-payments` | `account-balances-balance-change-1` |
| `corporate-v2-post-payments` | `accounting-entry-creation-1` |
| `corporate-v2-post-confirm-payments` | `availables-change-available-1` |
| `corporate-v2-post-payments` | `availables-change-available-1` |
| `patch-division-v2` | `corporate-division-change-2` |
| `post-division-v2` | `corporate-division-creation-2` |
| `corporate-v2-post-confirm-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-payments` | `rules-evaluation-requested-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/calendars-and-holidays-in-transaction-banking.md`: updatedAt 2026-04-24T21:57:10.000Z.
- `docs/core-banking/posting-transactions-on-holidays.md`: updatedAt 2026-04-28T17:14:26.000Z.
- Links to `post-v2-admin-division`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Divisions.yaml`.
- Links to `post-v2-holiday`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Holidays.yaml`.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/calendars-and-holidays-in-transaction-banking.md` | whole document | https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-transaction-banking | `878e704cb20b3089…` | 2026-04-24T21:57:10.000Z |
| `docs/core-banking/posting-transactions-on-holidays.md` | whole document | https://developers.pismo.io/pismo-docs/docs/posting-transactions-on-holidays | `045a6b02bf22cebe…` | 2026-04-28T17:14:26.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--bulk-settlement` — API reference: Banking - Transaction banking — Bulk settlement
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated` — API reference: Platform setup - Divisions — Administrative divisions V2 (deprecated)
- `KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat` — API reference: Platform setup - Holidays — Holidays v2 - Transaction banking (deprecated)
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
