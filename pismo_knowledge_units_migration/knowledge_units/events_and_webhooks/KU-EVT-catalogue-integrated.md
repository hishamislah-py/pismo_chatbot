---
ku_id: KU-EVT-catalogue-integrated
title: 'Event catalogue: integrated'
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
- delete-integrated-payments-api-v1-bankslips-issue
- delete-integrated-payments-api-v1-ebill-registration-accounts-accountId
- post-integrated-payments-api-v1-bankslips-cashout
- post-integrated-payments-api-v1-bankslips-issue
- post-integrated-payments-api-v1-bankslips-pay
- post-integrated-payments-api-v1-ebill-registration-accounts-accountId
related_kus:
- KU-API-banking-integrated-payments--bank-slip
- KU-API-banking-integrated-payments--bank-slip-issuance
- KU-API-banking-integrated-payments--ebill-registration
- KU-API-banking-integrated-payments--transfer
- KU-BANK-banking-overview
- KU-EVT-bank-slips-data-events
- KU-PAY-bank-slips
events:
- integrated-payments-bankslip-issue-cancel-1
- integrated-payments-bankslip-issue-register-1
- integrated-payments-bankslip-status-change-1
- integrated-payments-ebill-status-change-1
- integrated-payments-financial-reconciliation-1
- integrated-payments-transaction-status-change-1
- integrated-payments-transfer-out-created-1
---

# Event catalogue: integrated

**KU ID:** `KU-EVT-catalogue-integrated` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 7 event type(s) whose inventory domain is integrated, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `integrated-payments-bankslip-issue-cancel-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-bankslip-issue-cancel-1 | 1 | Banking_-_Integrated_payments |
| `integrated-payments-bankslip-issue-register-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-bankslip-issue-register-1 | 1 | Banking_-_Integrated_payments |
| `integrated-payments-bankslip-status-change-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-bankslip-status-change-1 | 1 | Banking_-_Integrated_payments |
| `integrated-payments-ebill-status-change-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-ebill-status-change-1 | 2 | Banking_-_Integrated_payments |
| `integrated-payments-financial-reconciliation-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-financial-reconciliation-1 | 2 | Banking_-_Integrated_payments |
| `integrated-payments-transaction-status-change-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-transaction-status-change-1 | 1 | Banking_-_Integrated_payments |
| `integrated-payments-transfer-out-created-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-transfer-out-created-1 | 1 | Banking_-_Integrated_payments |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `integrated-payments-bankslip-issue-cancel-1` | `DELETE /v1/bankslips-issue/client-requests/{clientRequestId}` | `delete-integrated-payments-api-v1-bankslips-issue` | `Banking_-_Integrated_payments` | KU-API-banking-integrated-payments--bank-slip-issuance |
| `integrated-payments-bankslip-issue-register-1` | `POST /v1/bankslips-issue` | `post-integrated-payments-api-v1-bankslips-issue` | `Banking_-_Integrated_payments` | KU-API-banking-integrated-payments--bank-slip-issuance |
| `integrated-payments-bankslip-status-change-1` | `POST /v1/bankslips/pay` | `post-integrated-payments-api-v1-bankslips-pay` | `Banking_-_Integrated_payments` | KU-API-banking-integrated-payments--bank-slip |
| `integrated-payments-ebill-status-change-1` | `POST /v1/ebill-registration/accounts/{accountId}` | `post-integrated-payments-api-v1-ebill-registration-accounts-accountId` | `Banking_-_Integrated_payments` | KU-API-banking-integrated-payments--ebill-registration |
| `integrated-payments-ebill-status-change-1` | `DELETE /v1/ebill-registration/accounts/{accountId}` | `delete-integrated-payments-api-v1-ebill-registration-accounts-accountId` | `Banking_-_Integrated_payments` | KU-API-banking-integrated-payments--ebill-registration |
| `integrated-payments-financial-reconciliation-1` | `POST /v1/bankslips/pay` | `post-integrated-payments-api-v1-bankslips-pay` | `Banking_-_Integrated_payments` | KU-API-banking-integrated-payments--bank-slip |
| `integrated-payments-financial-reconciliation-1` | `POST /v1/transfers/cashout` | `post-integrated-payments-api-v1-bankslips-cashout` | `Banking_-_Integrated_payments` | KU-API-banking-integrated-payments--transfer |
| `integrated-payments-transaction-status-change-1` | `POST /v1/transfers/cashout` | `post-integrated-payments-api-v1-bankslips-cashout` | `Banking_-_Integrated_payments` | KU-API-banking-integrated-payments--transfer |
| `integrated-payments-transfer-out-created-1` | `POST /v1/transfers/cashout` | `post-integrated-payments-api-v1-bankslips-cashout` | `Banking_-_Integrated_payments` | KU-API-banking-integrated-payments--transfer |

## Guides that link to these events

- `integrated-payments-bankslip-issue-cancel-1`: `KU-PAY-bank-slips`
- `integrated-payments-bankslip-issue-register-1`: `KU-PAY-bank-slips`
- `integrated-payments-bankslip-status-change-1`: `KU-EVT-bank-slips-data-events`, `KU-PAY-bank-slips`
- `integrated-payments-ebill-status-change-1`: `KU-BANK-banking-overview`
- `integrated-payments-financial-reconciliation-1`: `KU-EVT-bank-slips-data-events`
- `integrated-payments-transaction-status-change-1`: `KU-EVT-bank-slips-data-events`
- `integrated-payments-transfer-out-created-1`: `KU-BANK-banking-overview`, `KU-EVT-bank-slips-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: integrated-payments-bankslip-issue-cancel-1, integrated-payments-bankslip-issue-register-1, integrated-payments-bankslip-status-change-1, integrated-payments-ebill-status-change-1, integrated-payments-financial-reconciliation-1, integrated-payments-transaction-status-change-1, integrated-payments-transfer-out-created-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-integrated-payments--bank-slip` — API reference: Banking - Integrated payments — Bank slip
- `KU-API-banking-integrated-payments--bank-slip-issuance` — API reference: Banking - Integrated payments — Bank slip issuance
- `KU-API-banking-integrated-payments--ebill-registration` — API reference: Banking - Integrated payments — eBill registration
- `KU-API-banking-integrated-payments--transfer` — API reference: Banking - Integrated payments — Transfer
- `KU-BANK-banking-overview` — Banking overview
- `KU-EVT-bank-slips-data-events` — Banking - Integrated payments
- `KU-PAY-bank-slips` — Bank slips
