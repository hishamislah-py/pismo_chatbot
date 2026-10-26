---
ku_id: KU-EVT-catalogue-balance
title: 'Event catalogue: balance'
category: events_and_webhooks
ku_type: event_catalogue
lifecycle: current
sources:
- path: api-reference-data/event_type_inventory.csv
  sha256: 7eed7e3056f6f22e154bae7f22d25760a66c9e243ee0367953d1e935f823aed5
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- CancelInstallmentAdvancement
- CancelInstallmentsAdvanceV2
- CreateInstallmentAdvancement
- CreateProgramCalendarStrategy
- GetInstallmentsAdvanceV2
- InstallmentAdvancedV2
- InstallmentPaymentsv4
- SimulateInstallmentAdvancement
- UpdateAcountCalendarStrategy
- UpdateProgramCalendarStrategy
- create-payment-agreement-simulation
- create-recurring-charge-link
- create-recurring-charge-plan
- delete-recurring-charge-link
- disable-recurring-charge-plan
- post-shift-transactions
- postRevolvingStatementSummary
- update-scheduled-charge
related_kus:
- KU-API-revolving-credit-calendar-management--account-calendar-strategies
- KU-API-revolving-credit-calendar-management--program-calendar-strategies
- KU-API-revolving-credit-installment-management--installment-advancements
- KU-API-revolving-credit-installment-management--simulations
- KU-API-revolving-credit-recurring-charges--recurring-charge-links
- KU-API-revolving-credit-recurring-charges--recurring-charge-plans
- KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges
- KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation
- KU-API-revolving-credit-statements--advancements
- KU-API-revolving-credit-statements--refinancing
- KU-API-revolving-credit-statements--statement
- KU-API-revolving-credit-statements--transaction-shift
- KU-EVT-recurring-charges-data-events
- KU-EVT-statement-data-events
events:
- balance-balance-account-change-1
- balance-installment-advancement-1
- balance-installment-advancement-cancelled-1
- balance-installment-payment-processed-1
- balance-program-calendar-strategy-created-1
- balance-program-calendar-strategy-updated-1
- balance-recurring-charge-plan-created-1
- balance-recurring-charge-plan-disabled-1
- balance-recurring-charge-plan-linked-to-account-1
- balance-recurring-charge-plan-unlinked-from-account-1
- balance-recurring-scheduled-charge-updated-1
- balance-revolving-statement-summary-1
- balance-shift-transactions-1
---

# Event catalogue: balance

**KU ID:** `KU-EVT-catalogue-balance` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 13 event type(s) whose inventory domain is balance, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `balance-balance-account-change-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-balance-account-change-1 | 1 | Revolving_credit_-_Calendar_management |
| `balance-installment-advancement-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-installment-advancement-1 | 5 | Revolving_credit_-_Installment_management;Revolving_credit_-_Statements |
| `balance-installment-advancement-cancelled-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-installment-advancement-cancelled-1 | 1 | Revolving_credit_-_Installment_management |
| `balance-installment-payment-processed-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-installment-payment-processed-1 | 2 | Revolving_credit_-_Statement_refinancing_API;Revolving_credit_-_Statements |
| `balance-program-calendar-strategy-created-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-program-calendar-strategy-created-1 | 1 | Revolving_credit_-_Calendar_management |
| `balance-program-calendar-strategy-updated-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-program-calendar-strategy-updated-1 | 1 | Revolving_credit_-_Calendar_management |
| `balance-recurring-charge-plan-created-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-created-1 | 1 | Revolving_credit_-_Recurring_charges |
| `balance-recurring-charge-plan-disabled-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-disabled-1 | 1 | Revolving_credit_-_Recurring_charges |
| `balance-recurring-charge-plan-linked-to-account-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-linked-to-account-1 | 1 | Revolving_credit_-_Recurring_charges |
| `balance-recurring-charge-plan-unlinked-from-account-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-unlinked-from-account-1 | 1 | Revolving_credit_-_Recurring_charges |
| `balance-recurring-scheduled-charge-updated-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-recurring-scheduled-charge-updated-1 | 1 | Revolving_credit_-_Recurring_charges |
| `balance-revolving-statement-summary-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-revolving-statement-summary-1 | 1 | Revolving_credit_-_Statements |
| `balance-shift-transactions-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-shift-transactions-1 | 1 | Revolving_credit_-_Statements |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `balance-balance-account-change-1` | `PUT /v1/accounts/{accountId}/calendar-strategies` | `UpdateAcountCalendarStrategy` | `Revolving_credit_-_Calendar_management` | KU-API-revolving-credit-calendar-management--account-calendar-strategies |
| `balance-installment-advancement-1` | `GET /v1/accounts/{accountId}/installment-advance/simulations` | `SimulateInstallmentAdvancement` | `Revolving_credit_-_Installment_management` | KU-API-revolving-credit-installment-management--simulations |
| `balance-installment-advancement-1` | `POST /v1/accounts/{accountId}/installment-advance` | `CreateInstallmentAdvancement` | `Revolving_credit_-_Installment_management` | KU-API-revolving-credit-installment-management--installment-advancements |
| `balance-installment-advancement-1` | `POST /statements/v2/accounts/{accountId}/installment-advance` | `InstallmentAdvancedV2` | `Revolving_credit_-_Statements` | KU-API-revolving-credit-statements--advancements |
| `balance-installment-advancement-1` | `GET /statements/v2/accounts/{accountId}/installment-advance/{id}` | `GetInstallmentsAdvanceV2` | `Revolving_credit_-_Statements` | KU-API-revolving-credit-statements--advancements |
| `balance-installment-advancement-1` | `DELETE /statements/v2/accounts/{accountId}/installment-advance/{id}` | `CancelInstallmentsAdvanceV2` | `Revolving_credit_-_Statements` | KU-API-revolving-credit-statements--advancements |
| `balance-installment-advancement-cancelled-1` | `DELETE /v1/accounts/{accountId}/installment-advance/{advancementId}` | `CancelInstallmentAdvancement` | `Revolving_credit_-_Installment_management` | KU-API-revolving-credit-installment-management--installment-advancements |
| `balance-installment-payment-processed-1` | `POST /v1/accounts/{accountId}/payment-agreement-simulations` | `create-payment-agreement-simulation` | `Revolving_credit_-_Statement_refinancing_API` | KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation |
| `balance-installment-payment-processed-1` | `POST /statements/v4/accounts/{accountId}/installment-payments` | `InstallmentPaymentsv4` | `Revolving_credit_-_Statements` | KU-API-revolving-credit-statements--refinancing |
| `balance-program-calendar-strategy-created-1` | `POST /v1/programs/{programId}/calendar-strategies` | `CreateProgramCalendarStrategy` | `Revolving_credit_-_Calendar_management` | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `balance-program-calendar-strategy-updated-1` | `PATCH /v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId}` | `UpdateProgramCalendarStrategy` | `Revolving_credit_-_Calendar_management` | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `balance-recurring-charge-plan-created-1` | `POST /v1/recurring-charge-plans` | `create-recurring-charge-plan` | `Revolving_credit_-_Recurring_charges` | KU-API-revolving-credit-recurring-charges--recurring-charge-plans |
| `balance-recurring-charge-plan-disabled-1` | `DELETE /v1/recurring-charge-plans/{recurring_charge_plan_id}` | `disable-recurring-charge-plan` | `Revolving_credit_-_Recurring_charges` | KU-API-revolving-credit-recurring-charges--recurring-charge-plans |
| `balance-recurring-charge-plan-linked-to-account-1` | `POST /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id}` | `create-recurring-charge-link` | `Revolving_credit_-_Recurring_charges` | KU-API-revolving-credit-recurring-charges--recurring-charge-links |
| `balance-recurring-charge-plan-unlinked-from-account-1` | `DELETE /v1/recurring-charge-links/{recurring_charge_link_id}` | `delete-recurring-charge-link` | `Revolving_credit_-_Recurring_charges` | KU-API-revolving-credit-recurring-charges--recurring-charge-links |
| `balance-recurring-scheduled-charge-updated-1` | `PATCH /v1/accounts/{account_id}/scheduled-charges/{recurring_scheduled_charge_id}` | `update-scheduled-charge` | `Revolving_credit_-_Recurring_charges` | KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges |
| `balance-revolving-statement-summary-1` | `POST /statements-v2/v1/accounts/{accountId}/revolving-statement-summary` | `postRevolvingStatementSummary` | `Revolving_credit_-_Statements` | KU-API-revolving-credit-statements--statement |
| `balance-shift-transactions-1` | `POST /statements-v2/v1/accounts/{accountId}/transactions/shifts` | `post-shift-transactions` | `Revolving_credit_-_Statements` | KU-API-revolving-credit-statements--transaction-shift |

## Guides that link to these events

- `balance-balance-account-change-1`: `KU-EVT-recurring-charges-data-events`
- `balance-installment-advancement-1`: `KU-EVT-statement-data-events`
- `balance-installment-payment-processed-1`: `KU-EVT-statement-data-events`
- `balance-recurring-charge-plan-created-1`: `KU-EVT-recurring-charges-data-events`
- `balance-recurring-charge-plan-disabled-1`: `KU-EVT-recurring-charges-data-events`
- `balance-recurring-charge-plan-linked-to-account-1`: `KU-EVT-recurring-charges-data-events`
- `balance-recurring-charge-plan-unlinked-from-account-1`: `KU-EVT-recurring-charges-data-events`
- `balance-recurring-scheduled-charge-updated-1`: `KU-EVT-recurring-charges-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: balance-balance-account-change-1, balance-installment-advancement-1, balance-installment-advancement-cancelled-1, balance-installment-payment-processed-1, balance-program-calendar-strategy-created-1, balance-program-calendar-strategy-updated-1, balance-recurring-charge-plan-created-1, balance-recurring-charge-plan-disabled-1, balance-recurring-charge-plan-linked-to-account-1, balance-recurring-charge-plan-unlinked-from-account-1, balance-recurring-scheduled-charge-updated-1, balance-revolving-statement-summary-1, balance-shift-transactions-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-revolving-credit-calendar-management--account-calendar-strategies` — API reference: Revolving credit - Calendar management — Account calendar strategies
- `KU-API-revolving-credit-calendar-management--program-calendar-strategies` — API reference: Revolving credit - Calendar management — Program calendar strategies
- `KU-API-revolving-credit-installment-management--installment-advancements` — API reference: Revolving credit - Installment management — Installment advancements
- `KU-API-revolving-credit-installment-management--simulations` — API reference: Revolving credit - Installment management — Simulations
- `KU-API-revolving-credit-recurring-charges--recurring-charge-links` — API reference: Revolving credit - Recurring charges — Recurring charge links
- `KU-API-revolving-credit-recurring-charges--recurring-charge-plans` — API reference: Revolving credit - Recurring charges — Recurring charge plans
- `KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges` — API reference: Revolving credit - Recurring charges — Recurring scheduled charges
- `KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation` — API reference: Revolving credit - Statement refinancing — Payment agreement simulation
- `KU-API-revolving-credit-statements--advancements` — API reference: Revolving credit - Statements — Advancements
- `KU-API-revolving-credit-statements--refinancing` — API reference: Revolving credit - Statements — Refinancing
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-API-revolving-credit-statements--transaction-shift` — API reference: Revolving credit - Statements — Transaction shift
- `KU-EVT-recurring-charges-data-events` — Revolving credit - Recurring charges
- `KU-EVT-statement-data-events` — Revolving credit - Statements
