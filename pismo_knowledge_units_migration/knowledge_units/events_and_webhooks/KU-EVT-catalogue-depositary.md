---
ku_id: KU-EVT-catalogue-depositary
title: 'Event catalogue: depositary'
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
- create-receivable
- delete-receivable
- findByAccessKey
- update
related_kus:
- KU-API-banking-credit-receivables--invoices
- KU-API-banking-credit-receivables--receivable
- KU-EVT-depositary-data-events
events:
- depositary-credit-rights-change-failure-1
- depositary-credit-rights-change-success-1
- depositary-credit-rights-registration-failure-1
- depositary-credit-rights-registration-success-1
- depositary-credit-rights-status-change-failure-1
- depositary-credit-rights-status-change-success-1
- depositary-invoice-validation-failure-1
- depositary-invoice-validation-request-failure-1
- depositary-invoice-validation-request-success-1
- depositary-invoice-validation-success-1
---

# Event catalogue: depositary

**KU ID:** `KU-EVT-catalogue-depositary` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 10 event type(s) whose inventory domain is depositary, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `depositary-credit-rights-change-failure-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-change-failure-1 | 1 | Banking_-_Credit_receivables |
| `depositary-credit-rights-change-success-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-change-success-1 | 1 | Banking_-_Credit_receivables |
| `depositary-credit-rights-registration-failure-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-registration-failure-1 | 1 | Banking_-_Credit_receivables |
| `depositary-credit-rights-registration-success-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-registration-success-1 | 1 | Banking_-_Credit_receivables |
| `depositary-credit-rights-status-change-failure-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-failure-1 | 2 | Banking_-_Credit_receivables |
| `depositary-credit-rights-status-change-success-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-success-1 | 2 | Banking_-_Credit_receivables |
| `depositary-invoice-validation-failure-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-invoice-validation-failure-1 | 1 | Banking_-_Credit_receivables |
| `depositary-invoice-validation-request-failure-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-invoice-validation-request-failure-1 | 1 | Banking_-_Credit_receivables |
| `depositary-invoice-validation-request-success-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-invoice-validation-request-success-1 | 1 | Banking_-_Credit_receivables |
| `depositary-invoice-validation-success-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-invoice-validation-success-1 | 1 | Banking_-_Credit_receivables |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `depositary-credit-rights-change-failure-1` | `PATCH /v1/credit-rights/{internalNumber}` | `update` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--receivable |
| `depositary-credit-rights-change-success-1` | `PATCH /v1/credit-rights/{internalNumber}` | `update` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--receivable |
| `depositary-credit-rights-registration-failure-1` | `POST /v1/credit-rights` | `create-receivable` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--receivable |
| `depositary-credit-rights-registration-success-1` | `POST /v1/credit-rights` | `create-receivable` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--receivable |
| `depositary-credit-rights-status-change-failure-1` | `PATCH /v1/credit-rights/{internalNumber}` | `update` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--receivable |
| `depositary-credit-rights-status-change-failure-1` | `DELETE /v1/credit-rights/{internalNumber}` | `delete-receivable` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--receivable |
| `depositary-credit-rights-status-change-success-1` | `PATCH /v1/credit-rights/{internalNumber}` | `update` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--receivable |
| `depositary-credit-rights-status-change-success-1` | `DELETE /v1/credit-rights/{internalNumber}` | `delete-receivable` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--receivable |
| `depositary-invoice-validation-failure-1` | `GET /v1/invoices/{access_key}` | `findByAccessKey` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--invoices |
| `depositary-invoice-validation-request-failure-1` | `GET /v1/invoices/{access_key}` | `findByAccessKey` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--invoices |
| `depositary-invoice-validation-request-success-1` | `GET /v1/invoices/{access_key}` | `findByAccessKey` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--invoices |
| `depositary-invoice-validation-success-1` | `GET /v1/invoices/{access_key}` | `findByAccessKey` | `Banking_-_Credit_receivables` | KU-API-banking-credit-receivables--invoices |

## Guides that link to these events

- `depositary-credit-rights-change-failure-1`: `KU-EVT-depositary-data-events`
- `depositary-credit-rights-change-success-1`: `KU-EVT-depositary-data-events`
- `depositary-credit-rights-registration-failure-1`: `KU-EVT-depositary-data-events`
- `depositary-credit-rights-registration-success-1`: `KU-EVT-depositary-data-events`
- `depositary-credit-rights-status-change-failure-1`: `KU-EVT-depositary-data-events`
- `depositary-credit-rights-status-change-success-1`: `KU-EVT-depositary-data-events`
- `depositary-invoice-validation-failure-1`: `KU-EVT-depositary-data-events`
- `depositary-invoice-validation-request-failure-1`: `KU-EVT-depositary-data-events`
- `depositary-invoice-validation-request-success-1`: `KU-EVT-depositary-data-events`
- `depositary-invoice-validation-success-1`: `KU-EVT-depositary-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: depositary-credit-rights-change-failure-1, depositary-credit-rights-change-success-1, depositary-credit-rights-registration-failure-1, depositary-credit-rights-registration-success-1, depositary-credit-rights-status-change-failure-1, depositary-credit-rights-status-change-success-1, depositary-invoice-validation-failure-1, depositary-invoice-validation-request-failure-1, depositary-invoice-validation-request-success-1, depositary-invoice-validation-success-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-credit-receivables--invoices` — API reference: Banking - Credit receivables — Invoices
- `KU-API-banking-credit-receivables--receivable` — API reference: Banking - Credit receivables — Receivable
- `KU-EVT-depositary-data-events` — Banking - Credit receivables
