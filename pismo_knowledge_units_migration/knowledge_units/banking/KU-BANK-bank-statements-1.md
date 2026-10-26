---
ku_id: KU-BANK-bank-statements-1
title: Bank statements
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/bank-statements-1.md
  sha256: f5fcd4a1062cce8bd58b77d8ec3b9faaa1b43d7680c4cf43fccc01e0055fd08c
  url: https://developers.pismo.io/pismo-docs/docs/bank-statements-1
  role: primary_guide
  updated_at: '2026-04-24T21:53:36.000Z'
operations:
- get-account-balance-history
- get-account-balance-history-configuration
- patch-account-balances-history-configuration
- post-account-balance-history-configuration
- post-v2-admin-division
- post-v2-holiday
related_kus:
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated
- KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat
- KU-BANK-calendars-and-holidays
- KU-EVT-catalogue-account
grouping_rationale: single source page
---

# Bank statements

**KU ID:** `KU-BANK-bank-statements-1` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/bank-statements-1.md`:

> A bank statement is a detailed summary of an account’s transactions and balances for specific business dates. These statements are directly tied to "cycles," which define the start and end dates for recording activity. On the Pismo platform, cycles are automated so that as soon as one closes, the next one automatically begins, ensuring a continuous record.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/bank-statements-1.md`: Bank statements; Cycle closing; Configure cycle closing; Update cycle closing; Skip cycle closing; Trigger reason

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/bank-statements-1.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/bank-statements-1 · updatedAt: 2026-04-24T21:53:36.000Z

<!-- source:begin path=docs/core-banking/bank-statements-1.md part=0-end -->

# Bank statements

A bank statement is a detailed summary of an account’s transactions and balances for specific business dates. These statements are directly tied to "cycles," which define the start and end dates for recording activity. On the Pismo platform, cycles are automated so that as soon as one closes, the next one automatically begins, ensuring a continuous record.

# Cycle closing

Cycle closing is the Pismo platform's process for marking the operational end of the day for accounts. Unlike traditional "End of Day" routines that require system downtime, cycle closing enables 24/7 platform operation and continuous transaction processing. At the designated closing moment, the Pismo platform captures a balance snapshot for each account, creating an official record for that business date. This consistent and auditable history is essential for accurate reporting, reconciliation, and interest calculations.

You can configure cycle closing time using the `cycle_closing_time` field in the [Create account balance history configuration](https://developers.pismo.io/pismo-docs/reference/post-account-balance-history-configuration) endpoint. To update `cycle_closing_time`, use [Update account balance history configuration](https://developers.pismo.io/pismo-docs/reference/patch-account-balances-history-configuration).

When a cycle closes for an account, three key events occur.

* A balance history event is generated and emitted.
* A new record is created in the balance history table, provided there has been activity or movement in the account.
* The account's balance for that day becomes accessible through the [Get account balance history](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history) endpoint, if there is any account movement.

## Configure cycle closing

You can configure cycle closing at the division or organization level, and each level can follow its own rules. These are the main settings.

* **Cycle closing time**: Specify the exact time the cycle ends, using the division’s time zone.
* **Cycle event delay**:  Add an optional buffer period before the Pismo platform emits the cycle closing event.

The timezone used for cycle closing depends on where it is configured. For division-level configurations, the Pismo platform first looks for a timezone set for that division. If none exists, it inherits the timezone from the parent division, moving up the hierarchy until one is found. If no timezone is found, it defaults to UTC.

In contrast, cycle closings configured at the organization level always use the organization’s timezone, regardless of the settings in any individual divisions.

## Update cycle closing

When you update the cycle closing time, the timing of your request determines when the change takes effect. There are two scenarios.

* **Update made before the next cycle validity**: If you submit the update **before** the next cycle validity is scheduled to start, the new configuration takes effect **at the very next cycle closing**. This change is immediate for the upcoming cycle.
* **Update made after the current cycle validity**: If you submit an update while the current cycle is already in progress, the new closing time only takes effect **after two full cycles have completed**. The Pismo platform finishes the current cycle and the following cycle using the existing configuration. After both cycles complete, it applies the updated configuration. This ensures consistent processing across active cycles.

For traceability, the Pismo platform generates an [Account balance history configuration changed](https://developers.pismo.io/events/docs/account-balances-balance-history-config-change-1) event every time you update a cycle-closing configuration.

For details about cycle validity, refer to the `cycle_config_validity` field of [Get account balance history configuration](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history-configuration).

## Skip cycle closing

Skip cycle closing is a feature controlled by a boolean parameter in the [administrative division](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) or [Create holiday](https://developers.pismo.io/pismo-docs/reference/post-v2-holiday) endpoints. When set to `true`, the Pismo platform bypasses the cycle‑closing process for that division on non‑business days. As a result, the [Get account balance history](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history) endpoint returns only business days, omitting weekends and holidays. With `skip_cycle_closing` enabled, any transaction that occurs on a non‑business day is automatically recorded on the next business day, ensuring that both event generation and balance history follow the division’s business calendar.

This configuration is especially useful for back‑value‑dated transactions—transactions posted with a past value date—because balance recalculations and balance‑history events are generated only on business days. This avoids unnecessary entries and maintains consistency with the defined business calendar.

For a list of parameters and how you can use them to configure back- and future-business-dated transactions, including `skip_cycle_closing`, refer to [Posting transactions on holidays](https://developers.pismo.io/pismo-docs/docs/posting-transactions-on-holidays#parameters).

## Trigger reason

The `trigger_reason` field in the [Account balance history generated](https://developers.pismo.io/events/docs/account-balances-balance-history-1) event indicates the specific condition or action that caused an account balance history event to be generated, providing clear context for why the event was emitted.

You can find a list of trigger reasons and their details in the [Account balance history generated](https://developers.pismo.io/events/docs/account-balances-balance-history-1) event. Here are some trigger reason examples.

| Trigger reason                            | Description                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CYCLE_CLOSING`                           | Generated at the end of a business date, based on the cycle closing time defined in [Account balance history configuration changed](https://developers.pismo.io/events/docs/account-balances-balance-history-config-change-1). Not produced on non‑working days when `skip_cycle_closing = true` is in the administrative division. |
| `BACK_VALUE_DATED_OPERATION`              | Occurs when the business date derived from a transaction’s `payment_datetime` is earlier than the current business date, even if the transaction’s own `business_date` is current. Events are generated for past days only, not for the current business day.                                                                       |
| `BACK_VALUE_AND_BUSINESS_DATED_OPERATION` | Applies when two conditions are met: the transaction’s `business_date` is earlier than the current business date, and the business date derived from its `payment_datetime` is even earlier than that. Events are recorded for all impacted past business days.                                                                     |
| `BACK_VALUE_DATED_OPERATION_CURRENT_DATE` | Same condition as `BACK_VALUE_DATED_OPERATION`, but the event is logged **only** for the current business date.                                                                                                                                                                                                                     |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /bank-statements/v1/account-balances/history/config` | `post-account-balance-history-configuration` | Create account balance history config v1 | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `PATCH /bank-statements/v1/account-balances/history/config/{divisionCode}` | `patch-account-balances-history-configuration` | Update account balance history config v1 | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `GET /bank-statements/v1/account-balances/{externalAccountId}/history` | `get-account-balance-history` | Get transaction banking account balance history | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `GET /bank-statements/v1/account-balances/history/config/{divisionCode}` | `get-account-balance-history-configuration` | Get account balance history config v1 | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `POST /divisions-core/v2/administrative-division` | `post-v2-admin-division` | Create administrative division (deprecated) | `api-specs/Platform_setup_-_Divisions.yaml` | **yes** | KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated |
| `POST /holidays-core/v2/holiday` | `post-v2-holiday` | Create holiday (deprecated) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat |

### Operation essentials

- **`POST /bank-statements/v1/account-balances/history/config`** (`post-account-balance-history-configuration`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `cycle_closing_time`, `cycle_event_delay`; response statuses 201, 400, 404, 409, 500; error codes in examples `WCFG0002`, `WCFG0001`, `WCFG0003`, `WCFG0004`, `ECMN9999`; events `account-balances-balance-history-config-creation-1`.
- **`PATCH /bank-statements/v1/account-balances/history/config/{divisionCode}`** (`patch-account-balances-history-configuration`): security `BearerAuth`; required parameters `divisionCode` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `WCFG0002`, `WCFG0001`, `WCFG0003`, `WCFG0005`, `ECMN9999`; events `account-balances-balance-history-config-change-1`.
- **`GET /bank-statements/v1/account-balances/{externalAccountId}/history`** (`get-account-balance-history`): security `BearerAuth`; required parameters `externalAccountId` (path); required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples `CMN0002`, `WHIS0002`, `WHIS0003`, `WHIS0004`, `WHIS0006`, `WHIS0007`, `WHIS0008`, `WHIS0001`, `WHIS0005`, `CMN9999`, `EABL0001`; events none listed.
- **`GET /bank-statements/v1/account-balances/history/config/{divisionCode}`** (`get-account-balance-history-configuration`): security `BearerAuth`; required parameters `divisionCode` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `WCFG0002`, `WCFG0003`, `WCFG0005`, `ECMN9999`; events none listed.
- **`POST /divisions-core/v2/administrative-division`** (`post-v2-admin-division`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`; response statuses 201, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /holidays-core/v2/holiday`** (`post-v2-holiday`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `holiday_date`; response statuses 201, 400, 401, 404, 500; error codes in examples `EHLD0016`, `EHLD0028`, `EHLD0030`, `EHLD0031`, `EHLD0027`, `EHLD0001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-account-balances-history-configuration` | `account-balances-balance-history-config-change-1` |
| `post-account-balance-history-configuration` | `account-balances-balance-history-config-creation-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `account-balances-balance-history-config-change-1` | account | 1 | https://developers.pismo.io/events/docs/account-balances-balance-history-config-change-1 | 2 | KU-EVT-catalogue-account |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/bank-statements-1.md`: updatedAt 2026-04-24T21:53:36.000Z.
- Links to `post-v2-admin-division`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Divisions.yaml`.
- Links to `post-v2-holiday`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Holidays.yaml`.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/bank-statements-1.md` | whole document | https://developers.pismo.io/pismo-docs/docs/bank-statements-1 | `f5fcd4a1062cce8b…` | 2026-04-24T21:53:36.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated` — API reference: Platform setup - Divisions — Administrative divisions V2 (deprecated)
- `KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat` — API reference: Platform setup - Holidays — Holidays v2 - Transaction banking (deprecated)
- `KU-BANK-calendars-and-holidays` — Calendars, holidays and posting transactions on holidays in transaction banking
- `KU-EVT-catalogue-account` — Event catalogue: account
