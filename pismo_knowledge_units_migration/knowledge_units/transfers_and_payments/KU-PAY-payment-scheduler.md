---
ku_id: KU-PAY-payment-scheduler
title: Payment scheduler
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/payment-scheduler.md
  sha256: 4ed7237f16c82471211f60198cf775be3410783cbeb499e41577c1593a1a6d7f
  url: https://developers.pismo.io/pismo-docs/docs/payment-scheduler
  role: primary_guide
  updated_at: '2026-06-15T21:44:04.000Z'
operations:
- post-pre-schedules
- post-v1-create-single-schedule
- post-v1-create-transfer-schedules
related_kus:
- KU-API-core-platform-payment-scheduler-beta--schedules
- KU-EVT-catalogue-scheduler
grouping_rationale: single source page
---

# Payment scheduler

**KU ID:** `KU-PAY-payment-scheduler` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/payment-scheduler.md`:

> The [payment scheduler](https://developers.pismo.io/pismo-docs/reference/post-pre-schedules) feature allows you to configure payment schedules of different types and frequencies. Scheduling is essential for managing recurring billing cycles, subscription payments, payroll distributions, and liquidity optimization.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/payment-scheduler.md`: Payment scheduler; Schedule types; Single; Transfer; Pre-schedule; Scheduler flow; Scheduler events; Possible execution statuses

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/payment-scheduler.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/payment-scheduler · updatedAt: 2026-06-15T21:44:04.000Z

<!-- source:begin path=docs/core-platform/payment-scheduler.md part=0-end -->

# Payment scheduler

The [payment scheduler](https://developers.pismo.io/pismo-docs/reference/post-pre-schedules) feature allows you to configure payment schedules of different types and frequencies. Scheduling is essential for managing recurring billing cycles, subscription payments, payroll distributions, and liquidity optimization.

The platform orchestrates the timing and structure of automated financial operations, serving as the backbone for recurring payment systems. It defines both the frequency and execution model of scheduled transactions, enabling you to automate disbursements, collections, and internal fund movements with precision and control.

The Pismo platform supports the following scheduling types:

* [Single](payment-scheduler#single)
* [Transfer](https://developers.pismo.io/pismo-docs/docs/payment-scheduler#transfer)
* [Pre-schedule](https://developers.pismo.io/pismo-docs/docs/payment-scheduler#pre-schedule)

Each scheduling type includes detailed configuration options such as retry logic, execution intervals, and account-level restrictions, ensuring compliance, efficiency, and resilience in high-volume payment environments.

> 📘 Next day schedule execution
>
> In some cases, there may be a delay between the scheduled date and the actual execution of the schedule. This delay may result in the operation being executed on the following day instead of the originally scheduled date, which could lead to issues such as interest charges or unmet expectations. To reduce the likelihood of this occurring, it is recommended that the schedule's execution time is set for no later than 11:30 PM. This time buffer helps ensure that execution takes place on the same day, without rolling over into the next.
>
> To manage this behavior more precisely, you can decide whether to pre-authorize  execution of the scheduled transaction on the following day and set it in the `allow_execution_after_day_change` flag in the request. The flag applies to both [single](payment-scheduler#single)   and [transfer](https://developers.pismo.io/pismo-docs/docs/payment-scheduler#transfer) types of scheduling. This flag must be set to `true` for schedules that are set to be executed at the end of the day (after 11:30pm UTC). If the schedule is not executed on the expected day, and this field isn't set to `true`, the schedule will not be executed and will be marked as `EXECUTED_WITH_ERROR_NEXT_DAY_NOT_ALLOWED`.

# Schedule types

## Single

The single schedule type executes one configured payment operation for a single account. To create a single schedule, call the [Create single schedule](https://developers.pismo.io/pismo-docs/reference/post-v1-create-single-schedule) endpoint.

Depending on business requirements, you can configure the schedule to run only once or on a recurring basis in the `type` field.

* `ONCE`—Executed only once on the date specified in `start_date`.
* `RECURRING`—Executed repeatedly according to the interval defined in the `interval` field, within the period between `start_date` and `end_date`. A recurring schedule can run daily, weekly, monthly, or yearly, which is set in the `interval` field.

In addition to configuring the schedule recurrence, you can set the retry interval and number of attempts in case the schedule execution fails due to insufficient balance, timeout, or other system errors. The Pismo platform places these scheduled transactions in a queue and reprocesses them according to the configured retry logic. You configure the retry logic in the `retries` field, which contains two subfields:

* `interval_recurrence`—Specifies the time interval (in minutes) between each retry attempt.
* `number_of_attempts`—Defines the maximum number of retry attempts allowed.

You can also set conditions that must be met before a scheduled payment or transfer can be executed in the `restrictions` field. Restrictions help ensure account eligibility by enforcing rules such as minimum balance, average monthly availability, or inactivity thresholds.

| Restriction                       | Description                                                                                                     |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| Minimum daily available           | Compares the account balance with a defined daily minimum threshold.                                            |
| Minimum monthly average available | Calculates the monthly average balance up to the day before execution and compares it with the current balance. |
| Minimum days account inactivity   | Prevents execution if the account has been inactive for more days than the defined value.                       |

Refer to the following sample payload for a single schedule type.

```json Single schedule payload example
{
  "schedule_id": "eec3df75-629d-43dc-8eb7-e3b186188341",
  "schedule_details": {
    "type": "RECURRING",
    "interval": "DAILY",
    "day_type": "CALENDAR_DAY",
    "start_date": "2023-01-02T07:00:00.000Z",
    "end_date": "2023-01-02T07:00:00.000Z",
    "retries": {
      "interval_recurrence": 5,
      "number_of_attempts": 5
    },
    "allow_execution_after_day_change": true
  },
  "account_id": 8675309,
  "amount": 100.23,
  "currency_code": "BRL",
  "processing_code": "219803",
  "description": "Custom purchase",
  "restrictions": {
    "minimum_daily_available": 100.23,
    "minimum_monthly_average_available": 100.23,
    "minimum_days_account_inactivity": 5
  },
  "metadata": {
    "any-key": "any-value"
  }
}
```

## Transfer

The transfer schedule type performs transfer operations from a main account to one or more associated accounts. This configuration is designed for scenarios involving fund distribution or consolidation, such as sweeping balances or covering overdrafts. To create a transfer schedule, call the [Create transfer schedule](https://developers.pismo.io/pismo-docs/reference/post-v1-create-transfer-schedules) endpoint.

Transfer amounts can be set as follows:

* If you don't fill out the `strategy` field, you must specify the `amount` field for each transfer in the `transfers` array.
* If you fill out the `strategy` field, transfer amounts are determined dynamically at execution time by the strategy logic. The supported strategies are:
  * `SWEEP`—Transfers the entire balance from the child account to the parent (main) account.
  * `OVERDRAFT_SWEEP`—Transfers only the necessary funds from the parent account to child accounts to cover negative balances.

Refer to the following sample payload for a transfer schedule type.

```json Trransfer schedule payload example
{
  "schedule_id": "eec3df75-629d-43dc-8eb7-e3b186188341",
  "schedule_details": {
    "type": "RECURRING",
    "interval": "DAILY",
    "day_type": "CALENDAR_DAY",
    "end_date": "2023-01-02T07:00:00.000Z",
    "start_date": "2023-01-02T07:00:00.000Z",
    "allow_execution_after_day_change": false
  },
  "account_id": 8675309,
  "description": "Custom purchase",
  "strategy": "SWEEP",
  "transfers": [
    {
      "description": "Transfer to savings account",
      "amount": 100.23,
      "metadata": {
        "any-key": "any-value"
      },
      "to": {
        "account_id": 8675309,
        "processing_code": "219803"
      },
      "from": {
        "account_id": 8675309,
        "processing_code": "219803"
      }
    }
  ]
}
```

## Pre-schedule

A pre-schedule executes an operation by a direct call from the Pismo platform at the end of the closing cycle. When closing a statement, the platform checks if there is a pre-schedule configured on this account and, if there is one, executes the configured operation. To create a pre-schedule, set the **Post the pre-scheduled transactions when the cycle closes** program parameter to `true` and call the [Create pre-schedule](https://developers.pismo.io/pismo-docs/reference/post-pre-schedules) endpoint.

The pre-schedule type differs from the single and transfer schedules by requiring an external trigger to initiate execution. While single and transfer schedules are triggered automatically based on their configuration, pre-schedules are executed only when explicitly invoked via an API call.

A pre-schedule is executed only once and does not support recurrence. It behaves similarly to the single schedule type but does not require a `start_date`.

If an error occurs during pre-schedule registration:

* Inspect the `schedule_status` field in the event payload.
* Identify and correct the invalid record.
* Resend the request with the corrected data.

Upon successful registration:

* A bulk event is sent summarizing the operation.
* An individual event is sent for each successfully registered `schedule_id`, included within the bulk.

Refer to the following sample payload for a pre-schedule.

```json Pre-schedule payload example
{ 
   "schedule_id": "eec3df75-629d-43dc-8eb7-e3b186188341", 
   "schedule_details": { 
     "statement": { 
       "id": 1234455 
     } 
   }, 
   "account_id": 8675309, 
   "amount": 100.23, 
   "currency": "BRL", 
   "processing_code": "219803", 
   "description": "Custom purchase", 
   "metadata": { 
     "any-key": "any-value" 
   } 
 }
```

# Scheduler flow

## Scheduler events

This scheduler flow consists of two main stages, each generating specific events.

1. **Schedule creation**\
   When a schedule is created (whether single, transfer, or pre-scheduled), the platform generates a [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event automatically. This event contains configuration details of the schedule.
2. **Schedule execution**\
   When the schedule is executed, the platform generates the [Scheduled payment executed](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1) event containing the authorization attempt data, execution result, and final status.

## Possible execution statuses

| Status                     | Description                                                                                                                                                                                                     |
| :------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Executed                   | When execution occurs without errors. It must include the authorization data for payments or transfers returned from the Payment methods API. Authorization may be denied, which could lead to retry scenarios. |
| Executed with restrictions | When at least one restriction is detected. In this case, execution must be halted and no authorization attempt should be made.                                                                                  |

Additionally, when the Pismo platform completes a multiple transfer process which was triggered by the schedule of the transfer type, the platform generates a [Payment methods multiple transfers completed](https://developers.pismo.io/events/docs/payment-methods-multiple-transfers-1) event.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/pre-schedules` | `post-pre-schedules` | Create pre-schedule | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /v1/schedules` | `post-v1-create-single-schedule` | Create single schedule | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /v1/transfers` | `post-v1-create-transfer-schedules` | Create transfer schedule | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |

### Operation essentials

- **`POST /v1/pre-schedules`** (`post-pre-schedules`): security `BearerAuth`; required parameters none declared; required body fields `schedule_id`, `schedule_details`, `account_id`, `amount`, `currency_code`, `processing_code`; response statuses 200, 201, 400, 403, 500; error codes in examples none; events `scheduler-payments-scheduled-payments-1`, `scheduler-payments-scheduled-payments-execution-1`.
- **`POST /v1/schedules`** (`post-v1-create-single-schedule`): security `BearerAuth`; required parameters none declared; required body fields `schedule_id`, `schedule_details`, `account_id`, `amount`, `currency_code`, `processing_code`; response statuses 200, 201, 400, 403, 500; error codes in examples none; events `scheduler-payments-scheduled-payments-1`, `scheduler-payments-scheduled-payments-execution-1`.
- **`POST /v1/transfers`** (`post-v1-create-transfer-schedules`): security `BearerAuth`; required parameters none declared; required body fields `schedule_id`, `schedule_details`, `transfers`; response statuses 200, 201, 400, 403, 500; error codes in examples none; events `scheduler-payments-scheduled-payments-1`, `scheduler-payments-scheduled-payments-execution-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-pre-schedules` | `scheduler-payments-scheduled-payments-1` |
| `post-v1-create-single-schedule` | `scheduler-payments-scheduled-payments-1` |
| `post-v1-create-transfer-schedules` | `scheduler-payments-scheduled-payments-1` |
| `post-pre-schedules` | `scheduler-payments-scheduled-payments-execution-1` |
| `post-v1-create-single-schedule` | `scheduler-payments-scheduled-payments-execution-1` |
| `post-v1-create-transfer-schedules` | `scheduler-payments-scheduled-payments-execution-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `scheduler-payments-scheduled-payments-1` | scheduler | 1 | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1 | 7 | KU-EVT-catalogue-scheduler |
| `scheduler-payments-scheduled-payments-execution-1` | scheduler | 1 | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1 | 7 | KU-EVT-catalogue-scheduler |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/payment-scheduler.md`: updatedAt 2026-06-15T21:44:04.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 3 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/payment-scheduler.md` | whole document | https://developers.pismo.io/pismo-docs/docs/payment-scheduler | `4ed7237f16c82471…` | 2026-06-15T21:44:04.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-scheduler-beta--schedules` — API reference: Core platform - Payment scheduler — Schedules
- `KU-EVT-catalogue-scheduler` — Event catalogue: scheduler
