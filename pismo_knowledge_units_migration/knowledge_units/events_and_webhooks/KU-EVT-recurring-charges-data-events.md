---
ku_id: KU-EVT-recurring-charges-data-events
title: Revolving credit - Recurring charges
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/recurring-charges-data-events.md
  sha256: 4fd50194bce74f441437cbaea91d5859f9573b800ddcfd2279b9c0e8f8c2e531
  url: https://developers.pismo.io/pismo-docs/docs/recurring-charges-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:15:02.000Z'
operations:
- create-recurring-charge-link
- create-recurring-charge-plan
- delete-recurring-charge-link
- disable-recurring-charge-plan
- update-scheduled-charge
related_kus:
- KU-API-revolving-credit-recurring-charges--recurring-charge-links
- KU-API-revolving-credit-recurring-charges--recurring-charge-plans
- KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges
- KU-EVT-catalogue-balance
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Revolving credit - Recurring charges

**KU ID:** `KU-EVT-recurring-charges-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/recurring-charges-data-events.md`:

> This table lists the endpoints or other sources for recurring charges and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/recurring-charges-data-events.md`: Revolving credit - Recurring charges

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/recurring-charges-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/recurring-charges-data-events · updatedAt: 2026-03-18T15:15:02.000Z

<!-- source:begin path=docs/data-and-reporting/recurring-charges-data-events.md part=0-end -->

# Revolving credit - Recurring charges

This table lists the endpoints or other sources for recurring charges and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint/Trigger                                                                                                                   | Event                                                                                                                                         |
| :--------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| [Create recurring charge plan](https://developers.pismo.io/pismo-docs/reference/create-recurring-charge-plan)                                                                   | [Recurring charge plan created](https://developers.pismo.io/events/docs/balance-recurring-charge-plan-created-1)                              |
| [Disable recurring charge plan](https://developers.pismo.io/pismo-docs/reference/disable-recurring-charge-plan)                                                                 | [Recurring charge plan disabled](https://developers.pismo.io/events/docs/balance-recurring-charge-plan-disabled-1)                            |
| [Create link](https://developers.pismo.io/pismo-docs/reference/create-recurring-charge-link)                                                                                    | [Recurring charge plan linked to account](https://developers.pismo.io/events/docs/balance-recurring-charge-plan-linked-to-account-1)          |
| [Delete recurring charge link](https://developers.pismo.io/pismo-docs/reference/delete-recurring-charge-link)                                                                   | [Recurring charge plan unlinked from account](https://developers.pismo.io/events/docs/balance-recurring-charge-plan-unlinked-from-account-1)  |
| [Update scheduled charge](https://developers.pismo.io/pismo-docs/reference/update-scheduled-charge)                                                                             | [Recurring scheduled charge updated](https://developers.pismo.io/events/docs/balance-recurring-scheduled-charge-updated-1)                    |
| Link terminated because the last charge was incurred                                                                               | [Recurring charge plan link terminated](https://developers.pismo.io/events/docs/balance-recurring-charge-plan-linked-to-account-terminated-1) |
| Generated when a link is canceled. Can also be generated when a charge plan is canceled, if `disable_all_accounts` is set to true. | [Recurring scheduled charge canceled](https://developers.pismo.io/events/docs/balance-recurring-scheduled-charge-cancelled-1)                 |
| Generated with every charge that's created                                                                                         | [Recurring scheduled charge created](https://developers.pismo.io/events/docs/balance-recurring-scheduled-charge-created-1)                    |
| Recurring charge settled without being applied                                                                                     | [Recurring scheduled charge settled](https://developers.pismo.io/events/docs/balance-recurring-scheduled-charge-settled-1)                    |
| Recurring charge applied to account as part of the cycle closing operation                                                         | [Recurring scheduled charge processed](https://developers.pismo.io/events/docs/balance-recurring-scheduled-charge-processed-1)                |
| Interest accrual rolled back from migrated account                                                                                 | [Interest Accrual Rollback](https://developers.pismo.io/events/docs/balance-interest-accrual-rollback-1)                                      |
| Generated whenever one of the following properties changes: `CurrentCycle`, `CollectionStatus`, `OpenDueDate`, or `ProgramDueDate` | [Balance account changed](https://developers.pismo.io/events/docs/balance-balance-account-change-1)                                           |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/recurring-charge-plans` | `create-recurring-charge-plan` | Create recurring charge plan | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-charge-plans |
| `DELETE /v1/recurring-charge-plans/{recurring_charge_plan_id}` | `disable-recurring-charge-plan` | Disable recurring charge plan | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-charge-plans |
| `POST /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id}` | `create-recurring-charge-link` | Create link | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-charge-links |
| `DELETE /v1/recurring-charge-links/{recurring_charge_link_id}` | `delete-recurring-charge-link` | Delete recurring charge link | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-charge-links |
| `PATCH /v1/accounts/{account_id}/scheduled-charges/{recurring_scheduled_charge_id}` | `update-scheduled-charge` | Update scheduled charge | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges |

### Operation essentials

- **`POST /v1/recurring-charge-plans`** (`create-recurring-charge-plan`): security `BearerAuth`; required parameters none declared; required body fields `processing_code`, `installment_amount`, `number_of_cycles`, `tracking_id`; response statuses 200, 400, 409, 500; error codes in examples none; events `balance-recurring-charge-plan-created-1`.
- **`DELETE /v1/recurring-charge-plans/{recurring_charge_plan_id}`** (`disable-recurring-charge-plan`): security `BearerAuth`; required parameters `recurring_charge_plan_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events `balance-recurring-charge-plan-disabled-1`.
- **`POST /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id}`** (`create-recurring-charge-link`): security `BearerAuth`; required parameters `recurring_charge_plan_id` (path), `account_id` (path); required body fields `tracking_id`; response statuses 200, 400, 404, 500; error codes in examples none; events `balance-recurring-charge-plan-linked-to-account-1`.
- **`DELETE /v1/recurring-charge-links/{recurring_charge_link_id}`** (`delete-recurring-charge-link`): security `BearerAuth`; required parameters `recurring_charge_link_id` (path); required body fields none declared; response statuses 200, 400, 409, 500; error codes in examples none; events `balance-recurring-charge-plan-unlinked-from-account-1`.
- **`PATCH /v1/accounts/{account_id}/scheduled-charges/{recurring_scheduled_charge_id}`** (`update-scheduled-charge`): security `BearerAuth`; required parameters `account_id` (path), `recurring_scheduled_charge_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events `balance-recurring-scheduled-charge-updated-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `create-recurring-charge-plan` | `balance-recurring-charge-plan-created-1` |
| `disable-recurring-charge-plan` | `balance-recurring-charge-plan-disabled-1` |
| `create-recurring-charge-link` | `balance-recurring-charge-plan-linked-to-account-1` |
| `delete-recurring-charge-link` | `balance-recurring-charge-plan-unlinked-from-account-1` |
| `update-scheduled-charge` | `balance-recurring-scheduled-charge-updated-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `balance-balance-account-change-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-balance-account-change-1 | 1 | KU-EVT-catalogue-balance |
| `balance-recurring-charge-plan-created-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-created-1 | 1 | KU-EVT-catalogue-balance |
| `balance-recurring-charge-plan-disabled-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-disabled-1 | 1 | KU-EVT-catalogue-balance |
| `balance-recurring-charge-plan-linked-to-account-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-linked-to-account-1 | 1 | KU-EVT-catalogue-balance |
| `balance-recurring-charge-plan-unlinked-from-account-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-unlinked-from-account-1 | 1 | KU-EVT-catalogue-balance |
| `balance-recurring-scheduled-charge-updated-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-recurring-scheduled-charge-updated-1 | 1 | KU-EVT-catalogue-balance |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/recurring-charges-data-events.md`: updatedAt 2026-03-18T15:15:02.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 12 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/recurring-charges-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/recurring-charges-data-events | `4fd50194bce74f44…` | 2026-03-18T15:15:02.000Z |

## Related knowledge units

- `KU-API-revolving-credit-recurring-charges--recurring-charge-links` — API reference: Revolving credit - Recurring charges — Recurring charge links
- `KU-API-revolving-credit-recurring-charges--recurring-charge-plans` — API reference: Revolving credit - Recurring charges — Recurring charge plans
- `KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges` — API reference: Revolving credit - Recurring charges — Recurring scheduled charges
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
