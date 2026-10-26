---
ku_id: KU-EVT-catalogue-corporate
title: 'Event catalogue: corporate'
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
- cash-management-v2-post-scheduled-payments
- corporate-v2-delete-scheduled-payment
- corporate-v2-post-multileg-payments
- corporate-v2-post-scheduled-payments
- corporate-v3-post-multileg-payments
- patch-account
- patch-cash-management-v2-earmarks-earmarkid
- patch-corporate-v1-restricted-funds
- patch-corporate-v2-earmarks-earmarkid
- patch-corporate-v2-restricted-funds
- patch-division-v2
- patch-dormancy-config-v2
- post-account
- post-accounts-accountId-force-close
- post-cash-management-v2-earmarks
- post-cash-management-v2-earmarks-earmarkid-cancel
- post-corporate-v1-restricted-funds
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-division-v2
- post-dormancy-config-v2
- post-hierarchies
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--dormancy
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--earmarking-pismo-account-id
- KU-API-banking-transaction-banking--hierarchies
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--payments-pismo-account-id
- KU-API-banking-transaction-banking--restricted-funds
- KU-EVT-corporate-banking-data-events
events:
- corporate-corporate-account-change-1
- corporate-corporate-account-creation-1
- corporate-division-change-2
- corporate-division-creation-2
- corporate-dormancy-config-change-1
- corporate-dormancy-config-creation-1
- corporate-earmark-1
- corporate-force-account-closure-1
- corporate-hierarchy-creation-1
- corporate-multi-leg-creation-1
- corporate-multi-leg-creation-2
- corporate-multi-leg-status-change-1
- corporate-multi-leg-status-change-2
- corporate-restricted-funds-1
- corporate-schedule-payment-1
---

# Event catalogue: corporate

**KU ID:** `KU-EVT-catalogue-corporate` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 15 event type(s) whose inventory domain is corporate, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `corporate-corporate-account-change-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-corporate-account-change-1 | 1 | Banking_-_Transaction_banking |
| `corporate-corporate-account-creation-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-corporate-account-creation-1 | 1 | Banking_-_Transaction_banking |
| `corporate-division-change-2` | corporate | 2 | https://developers.pismo.io/events/docs/corporate-division-change-2 | 1 | Banking_-_Transaction_banking |
| `corporate-division-creation-2` | corporate | 2 | https://developers.pismo.io/events/docs/corporate-division-creation-2 | 1 | Banking_-_Transaction_banking |
| `corporate-dormancy-config-change-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-dormancy-config-change-1 | 1 | Banking_-_Transaction_banking |
| `corporate-dormancy-config-creation-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-dormancy-config-creation-1 | 1 | Banking_-_Transaction_banking |
| `corporate-earmark-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-earmark-1 | 6 | Banking_-_Transaction_banking |
| `corporate-force-account-closure-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-force-account-closure-1 | 1 | Banking_-_Transaction_banking |
| `corporate-hierarchy-creation-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-hierarchy-creation-1 | 1 | Banking_-_Transaction_banking |
| `corporate-multi-leg-creation-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-multi-leg-creation-1 | 1 | Banking_-_Transaction_banking |
| `corporate-multi-leg-creation-2` | corporate | 2 | https://developers.pismo.io/events/docs/corporate-multi-leg-creation-2 | 1 | Banking_-_Transaction_banking |
| `corporate-multi-leg-status-change-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-multi-leg-status-change-1 | 1 | Banking_-_Transaction_banking |
| `corporate-multi-leg-status-change-2` | corporate | 2 | https://developers.pismo.io/events/docs/corporate-multi-leg-status-change-2 | 1 | Banking_-_Transaction_banking |
| `corporate-restricted-funds-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-restricted-funds-1 | 3 | Banking_-_Transaction_banking |
| `corporate-schedule-payment-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-schedule-payment-1 | 3 | Banking_-_Transaction_banking |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `corporate-corporate-account-change-1` | `PATCH /corporate/v1/corporate-accounts/{externalAccountId}` | `patch-account` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--accounts |
| `corporate-corporate-account-creation-1` | `POST /corporate/v1/corporate-accounts` | `post-account` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--accounts |
| `corporate-division-change-2` | `PATCH /corporate/v2/divisions/{divisionCode}` | `patch-division-v2` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--divisions |
| `corporate-division-creation-2` | `POST /corporate/v2/divisions` | `post-division-v2` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--divisions |
| `corporate-dormancy-config-change-1` | `PATCH /corporate/v2/dormancy-config/{dormancyConfigId}` | `patch-dormancy-config-v2` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--dormancy |
| `corporate-dormancy-config-creation-1` | `POST /corporate/v2/dormancy-config` | `post-dormancy-config-v2` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--dormancy |
| `corporate-earmark-1` | `POST /corporate/v2/earmarks` | `post-corporate-v2-earmarks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `corporate-earmark-1` | `PATCH /corporate/v2/earmarks/{earmarkId}` | `patch-corporate-v2-earmarks-earmarkid` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `corporate-earmark-1` | `POST /corporate/v2/earmarks/{earmarkId}/cancel` | `post-corporate-v2-earmarks-earmarkid-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `corporate-earmark-1` | `POST /cash-management/v2/earmarks` | `post-cash-management-v2-earmarks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `corporate-earmark-1` | `PATCH /cash-management/v2/earmarks/{earmarkId}` | `patch-cash-management-v2-earmarks-earmarkid` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `corporate-earmark-1` | `POST /cash-management/v2/earmarks/{earmarkId}/cancel` | `post-cash-management-v2-earmarks-earmarkid-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `corporate-force-account-closure-1` | `POST /corporate/v1/corporate-accounts/{externalAccountId}/force-close` | `post-accounts-accountId-force-close` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--accounts |
| `corporate-hierarchy-creation-1` | `POST /corporate/v1/hierarchies` | `post-hierarchies` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--hierarchies |
| `corporate-multi-leg-creation-1` | `POST /corporate/v2/payments/multileg` | `corporate-v2-post-multileg-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-03 |
| `corporate-multi-leg-creation-2` | `POST /corporate/v3/payments/multileg` | `corporate-v3-post-multileg-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `corporate-multi-leg-status-change-1` | `POST /corporate/v2/payments/multileg` | `corporate-v2-post-multileg-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-03 |
| `corporate-multi-leg-status-change-2` | `POST /corporate/v3/payments/multileg` | `corporate-v3-post-multileg-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `corporate-restricted-funds-1` | `POST /corporate/v1/restricted-funds` | `post-corporate-v1-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `corporate-restricted-funds-1` | `PATCH /corporate/v1/restricted-funds/{restrictedFundsId}` | `patch-corporate-v1-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `corporate-restricted-funds-1` | `PATCH /corporate/v2/restricted-funds/{restrictedFundsId}` | `patch-corporate-v2-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `corporate-schedule-payment-1` | `POST /corporate/v2/scheduled-payments` | `corporate-v2-post-scheduled-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-02 |
| `corporate-schedule-payment-1` | `DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId}` | `corporate-v2-delete-scheduled-payment` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-03 |
| `corporate-schedule-payment-1` | `POST /cash-management/v2/scheduled-payments` | `cash-management-v2-post-scheduled-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |

## Guides that link to these events

- `corporate-corporate-account-creation-1`: `KU-EVT-corporate-banking-data-events`
- `corporate-dormancy-config-change-1`: `KU-EVT-corporate-banking-data-events`
- `corporate-dormancy-config-creation-1`: `KU-EVT-corporate-banking-data-events`
- `corporate-earmark-1`: `KU-EVT-corporate-banking-data-events`
- `corporate-hierarchy-creation-1`: `KU-EVT-corporate-banking-data-events`
- `corporate-schedule-payment-1`: `KU-EVT-corporate-banking-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: corporate-corporate-account-change-1, corporate-corporate-account-creation-1, corporate-division-change-2, corporate-division-creation-2, corporate-dormancy-config-change-1, corporate-dormancy-config-creation-1, corporate-earmark-1, corporate-force-account-closure-1, corporate-hierarchy-creation-1, corporate-multi-leg-creation-1, corporate-multi-leg-creation-2, corporate-multi-leg-status-change-1, corporate-multi-leg-status-change-2, corporate-restricted-funds-1, corporate-schedule-payment-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--earmarking-pismo-account-id` — API reference: Banking - Transaction banking — Earmarking (Pismo account ID)
- `KU-API-banking-transaction-banking--hierarchies` — API reference: Banking - Transaction banking — Hierarchies
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--payments-pismo-account-id` — API reference: Banking - Transaction banking — Payments (Pismo account ID)
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
