---
ku_id: KU-EVT-catalogue-audit
title: 'Event catalogue: audit'
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
- customerV1patch
- patch-accounts-v1-accounts-accountId-addresses-addressId
- patch-accounts-v1-accounts-accountId-phones-phoneId
- patch-v1-accounts-flex-control
- patch-v1-customers-flex-control
- post-accounts-v1-accounts-accountId-addresses
- post-accounts-v1-accounts-accountId-phones
- post-v1-accounts-flex-controls
- post-v1-customers-flex-controls
related_kus:
- KU-API-core-platform-accounts--addresses
- KU-API-core-platform-accounts--customers
- KU-API-core-platform-accounts--phones
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-flex-controls--customer-flex-controls-part-01
- KU-API-core-platform-flex-controls--customer-flex-controls-part-02
- KU-EVT-accounts-data-events
- KU-EVT-flex-controls-data-events
events:
- audit-account-spending-limit-created-1
- audit-account-spending-limit-updated-1
- audit-address-change-1
- audit-address-creation-1
- audit-customer-spending-limit-created-1
- audit-customer-spending-limit-updated-1
- audit-entity-change-1
- audit-phone-change-1
- audit-phone-creation-1
---

# Event catalogue: audit

**KU ID:** `KU-EVT-catalogue-audit` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 9 event type(s) whose inventory domain is audit, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `audit-account-spending-limit-created-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-account-spending-limit-created-1 | 1 | Core_platform_-_Flex_controls |
| `audit-account-spending-limit-updated-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-account-spending-limit-updated-1 | 1 | Core_platform_-_Flex_controls |
| `audit-address-change-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-address-change-1 | 1 | Core_platform_-_Accounts |
| `audit-address-creation-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-address-creation-1 | 1 | Core_platform_-_Accounts |
| `audit-customer-spending-limit-created-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-customer-spending-limit-created-1 | 1 | Core_platform_-_Flex_controls |
| `audit-customer-spending-limit-updated-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-customer-spending-limit-updated-1 | 1 | Core_platform_-_Flex_controls |
| `audit-entity-change-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-entity-change-1 | 1 | Core_platform_-_Accounts |
| `audit-phone-change-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-phone-change-1 | 1 | Core_platform_-_Accounts |
| `audit-phone-creation-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-phone-creation-1 | 1 | Core_platform_-_Accounts |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `audit-account-spending-limit-created-1` | `POST /v1/accounts/{accountId}/flex-controls` | `post-v1-accounts-flex-controls` | `Core_platform_-_Flex_controls` | KU-API-core-platform-flex-controls--account-flex-controls |
| `audit-account-spending-limit-updated-1` | `PATCH /v1/accounts/{accountId}/flex-controls/{flexControlId}` | `patch-v1-accounts-flex-control` | `Core_platform_-_Flex_controls` | KU-API-core-platform-flex-controls--account-flex-controls |
| `audit-address-change-1` | `PATCH /accounts/v1/accounts/{accountId}/addresses/{addressId}` | `patch-accounts-v1-accounts-accountId-addresses-addressId` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--addresses |
| `audit-address-creation-1` | `POST /accounts/v1/accounts/{accountId}/addresses` | `post-accounts-v1-accounts-accountId-addresses` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--addresses |
| `audit-customer-spending-limit-created-1` | `POST /v1/customers/{customerId}/flex-controls` | `post-v1-customers-flex-controls` | `Core_platform_-_Flex_controls` | KU-API-core-platform-flex-controls--customer-flex-controls-part-01 |
| `audit-customer-spending-limit-updated-1` | `PATCH /v1/customers/{customerId}/flex-controls/{flexControlId}` | `patch-v1-customers-flex-control` | `Core_platform_-_Flex_controls` | KU-API-core-platform-flex-controls--customer-flex-controls-part-02 |
| `audit-entity-change-1` | `PATCH /accounts/v1/accounts/{accountId}/customers/{customerId}/detail` | `customerV1patch` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--customers |
| `audit-phone-change-1` | `PATCH /accounts/v1/accounts/{accountId}/phones/{phoneId}` | `patch-accounts-v1-accounts-accountId-phones-phoneId` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--phones |
| `audit-phone-creation-1` | `POST /accounts/v1/accounts/{accountId}/phones` | `post-accounts-v1-accounts-accountId-phones` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--phones |

## Guides that link to these events

- `audit-account-spending-limit-created-1`: `KU-EVT-flex-controls-data-events`
- `audit-account-spending-limit-updated-1`: `KU-EVT-flex-controls-data-events`
- `audit-address-change-1`: `KU-EVT-accounts-data-events`
- `audit-address-creation-1`: `KU-EVT-accounts-data-events`
- `audit-customer-spending-limit-created-1`: `KU-EVT-flex-controls-data-events`
- `audit-customer-spending-limit-updated-1`: `KU-EVT-flex-controls-data-events`
- `audit-entity-change-1`: `KU-EVT-accounts-data-events`
- `audit-phone-change-1`: `KU-EVT-accounts-data-events`
- `audit-phone-creation-1`: `KU-EVT-accounts-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: audit-account-spending-limit-created-1, audit-account-spending-limit-updated-1, audit-address-change-1, audit-address-creation-1, audit-customer-spending-limit-created-1, audit-customer-spending-limit-updated-1, audit-entity-change-1, audit-phone-change-1, audit-phone-creation-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-core-platform-accounts--addresses` — API reference: Core platform - Accounts — Addresses
- `KU-API-core-platform-accounts--customers` — API reference: Core platform - Accounts — Customers
- `KU-API-core-platform-accounts--phones` — API reference: Core platform - Accounts — Phones
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-01` — API reference: Core platform - Flex controls — Customer flex controls (part 1 of 2)
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-02` — API reference: Core platform - Flex controls — Customer flex controls (part 2 of 2)
- `KU-EVT-accounts-data-events` — Core platform - Accounts
- `KU-EVT-flex-controls-data-events` — Core platform - Flex controls
