---
ku_id: KU-EVT-catalogue-account
title: 'Event catalogue: account'
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
- PostMigrationProgram
- cash-management-v2-post-cancel-payments
- cash-management-v2-post-confirm-payments
- cash-management-v2-post-payments
- corporate-v2-post-cancel-payments
- corporate-v2-post-confirm-payments
- corporate-v2-post-multileg-payments
- corporate-v2-post-payments
- customerV1patch
- customerV2Post
- customerV2Put
- patch-account
- patch-account-balances-history-configuration
- patch-account-balances-history-configv2
- patch-accounts-accountId-entity
- patch-accounts-accountId-status-rollback-v2
- patch-accounts-accountId-status-v2
- patch-accounts-v1-accounts
- patch-accounts-v2-accounts-accountId-status
- patch-cash-management-v2-earmarks-earmarkid
- patch-corporate-v1-restricted-funds
- patch-corporate-v2-earmarks-earmarkid
- patch-corporate-v2-restricted-funds
- patch-v2-accounts-accountId-status-rollback
- post-account-balance-history-configuration
- post-account-balance-history-configv2
- post-accounts-accountId-close
- post-cash-management-v2-earmarks
- post-cash-management-v2-earmarks-earmarkid-cancel
- post-corporate-v1-restricted-funds
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- v4-post-account-reason
- v4-post-account-status
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--bank-statements-part-02
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--earmarking-pismo-account-id
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--payments-pismo-account-id
- KU-API-banking-transaction-banking--restricted-funds
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--customers
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-API-core-platform-accounts--transfer-account
- KU-BANK-bank-statements-1
- KU-BANK-banking-overview
- KU-EVT-accounts-data-events
- KU-EVT-corporate-banking-data-events
events:
- account-account-change-2
- account-account-owner-change-1
- account-balances-balance-change-1
- account-balances-balance-history-config-change-1
- account-balances-balance-history-config-creation-1
- account-customer-change-2
- account-customer-creation-1
- account-owner-change-1
- account-program-migration-1
- account-reason-creation-1
- account-status-change-2
- account-status-creation-1
---

# Event catalogue: account

**KU ID:** `KU-EVT-catalogue-account` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 12 event type(s) whose inventory domain is account, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `account-account-change-2` | account | 2 | https://developers.pismo.io/events/docs/account-account-change-2 | 1 | Core_platform_-_Accounts |
| `account-account-owner-change-1` | account | 1 | https://developers.pismo.io/events/docs/account-account-owner-change-1 | 2 | Banking_-_Transaction_banking;Core_platform_-_Accounts |
| `account-balances-balance-change-1` | account | 1 | https://developers.pismo.io/events/docs/account-balances-balance-change-1 | 16 | Banking_-_Transaction_banking |
| `account-balances-balance-history-config-change-1` | account | 1 | https://developers.pismo.io/events/docs/account-balances-balance-history-config-change-1 | 2 | Banking_-_Transaction_banking |
| `account-balances-balance-history-config-creation-1` | account | 1 | https://developers.pismo.io/events/docs/account-balances-balance-history-config-creation-1 | 2 | Banking_-_Transaction_banking |
| `account-customer-change-2` | account | 2 | https://developers.pismo.io/events/docs/account-customer-change-2 | 1 | Core_platform_-_Accounts |
| `account-customer-creation-1` | account | 1 | https://developers.pismo.io/events/docs/account-customer-creation-1 | 1 | Core_platform_-_Accounts |
| `account-owner-change-1` | account | 1 | https://developers.pismo.io/events/docs/account-owner-change-1 | 1 | Core_platform_-_Accounts |
| `account-program-migration-1` | account | 1 | https://developers.pismo.io/events/docs/account-program-migration-1 | 1 | Core_platform_-_Accounts |
| `account-reason-creation-1` | account | 1 | https://developers.pismo.io/events/docs/account-reason-creation-1 | 1 | Core_platform_-_Accounts |
| `account-status-change-2` | account | 2 | https://developers.pismo.io/events/docs/account-status-change-2 | 6 | Banking_-_Transaction_banking;Core_platform_-_Accounts |
| `account-status-creation-1` | account | 1 | https://developers.pismo.io/events/docs/account-status-creation-1 | 1 | Core_platform_-_Accounts |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `account-account-change-2` | `PATCH /accounts/v1/accounts/{accountId}` | `patch-accounts-v1-accounts` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--accounts |
| `account-account-owner-change-1` | `PATCH /corporate/v1/corporate-accounts/{externalAccountId}/entity` | `patch-accounts-accountId-entity` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--accounts |
| `account-account-owner-change-1` | `POST /accounts/v2/customers` | `customerV2Post` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--customers |
| `account-balances-balance-change-1` | `POST /corporate/v2/earmarks` | `post-corporate-v2-earmarks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `account-balances-balance-change-1` | `PATCH /corporate/v2/earmarks/{earmarkId}` | `patch-corporate-v2-earmarks-earmarkid` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `account-balances-balance-change-1` | `POST /corporate/v2/earmarks/{earmarkId}/cancel` | `post-corporate-v2-earmarks-earmarkid-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `account-balances-balance-change-1` | `POST /corporate/v2/payments` | `corporate-v2-post-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `account-balances-balance-change-1` | `POST /corporate/v2/payments/confirm` | `corporate-v2-post-confirm-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `account-balances-balance-change-1` | `POST /corporate/v2/payments/cancel` | `corporate-v2-post-cancel-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `account-balances-balance-change-1` | `POST /corporate/v2/payments/multileg` | `corporate-v2-post-multileg-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-03 |
| `account-balances-balance-change-1` | `POST /corporate/v1/restricted-funds` | `post-corporate-v1-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `account-balances-balance-change-1` | `PATCH /corporate/v1/restricted-funds/{restrictedFundsId}` | `patch-corporate-v1-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `account-balances-balance-change-1` | `PATCH /corporate/v2/restricted-funds/{restrictedFundsId}` | `patch-corporate-v2-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `account-balances-balance-change-1` | `POST /cash-management/v2/payments` | `cash-management-v2-post-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `account-balances-balance-change-1` | `POST /cash-management/v2/payments/confirm` | `cash-management-v2-post-confirm-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `account-balances-balance-change-1` | `POST /cash-management/v2/payments/cancel` | `cash-management-v2-post-cancel-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `account-balances-balance-change-1` | `POST /cash-management/v2/earmarks` | `post-cash-management-v2-earmarks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `account-balances-balance-change-1` | `PATCH /cash-management/v2/earmarks/{earmarkId}` | `patch-cash-management-v2-earmarks-earmarkid` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `account-balances-balance-change-1` | `POST /cash-management/v2/earmarks/{earmarkId}/cancel` | `post-cash-management-v2-earmarks-earmarkid-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `account-balances-balance-history-config-change-1` | `PATCH /bank-statements/v1/account-balances/history/config/{divisionCode}` | `patch-account-balances-history-configuration` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `account-balances-balance-history-config-change-1` | `PATCH /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId}` | `patch-account-balances-history-configv2` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--bank-statements-part-02 |
| `account-balances-balance-history-config-creation-1` | `POST /bank-statements/v1/account-balances/history/config` | `post-account-balance-history-configuration` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `account-balances-balance-history-config-creation-1` | `POST /bank-statements/v2/account-balances/history/config` | `post-account-balance-history-configv2` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--bank-statements-part-02 |
| `account-customer-change-2` | `PUT /accounts/v2/customers/{customerId}` | `customerV2Put` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--customers |
| `account-customer-creation-1` | `POST /accounts/v2/customers` | `customerV2Post` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--customers |
| `account-owner-change-1` | `PATCH /accounts/v1/accounts/{accountId}/customers/{customerId}/detail` | `customerV1patch` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--customers |
| `account-program-migration-1` | `POST /accounts/v1/accounts/programs/migration` | `PostMigrationProgram` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--transfer-account |
| `account-reason-creation-1` | `POST /accounts/v4/reasons` | `v4-post-account-reason` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--statuses-and-reasons |
| `account-status-change-2` | `POST /corporate/v1/corporate-accounts/{externalAccountId}/close` | `post-accounts-accountId-close` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--accounts |
| `account-status-change-2` | `PATCH /corporate/v1/corporate-accounts/{externalAccountId}` | `patch-account` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--accounts |
| `account-status-change-2` | `PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status` | `patch-accounts-accountId-status-v2` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--accounts |
| `account-status-change-2` | `PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback` | `patch-accounts-accountId-status-rollback-v2` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--accounts |
| `account-status-change-2` | `PATCH /accounts/v2/accounts/{accountId}/status` | `patch-accounts-v2-accounts-accountId-status` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--statuses-and-reasons |
| `account-status-change-2` | `PATCH /accounts/v2/accounts/{accountId}/status/rollback` | `patch-v2-accounts-accountId-status-rollback` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--statuses-and-reasons |
| `account-status-creation-1` | `POST /accounts/v4/statuses` | `v4-post-account-status` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--statuses-and-reasons |

## Guides that link to these events

- `account-account-change-2`: `KU-EVT-accounts-data-events`
- `account-account-owner-change-1`: `KU-EVT-accounts-data-events`
- `account-balances-balance-change-1`: `KU-EVT-corporate-banking-data-events`
- `account-balances-balance-history-config-change-1`: `KU-BANK-bank-statements-1`, `KU-EVT-corporate-banking-data-events`
- `account-balances-balance-history-config-creation-1`: `KU-EVT-corporate-banking-data-events`
- `account-customer-change-2`: `KU-EVT-accounts-data-events`
- `account-customer-creation-1`: `KU-EVT-accounts-data-events`
- `account-program-migration-1`: `KU-EVT-accounts-data-events`
- `account-status-change-2`: `KU-BANK-banking-overview`, `KU-EVT-accounts-data-events`, `KU-EVT-corporate-banking-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: account-account-change-2, account-account-owner-change-1, account-balances-balance-change-1, account-balances-balance-history-config-change-1, account-balances-balance-history-config-creation-1, account-customer-change-2, account-customer-creation-1, account-owner-change-1, account-program-migration-1, account-reason-creation-1, account-status-change-2, account-status-creation-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--bank-statements-part-02` — API reference: Banking - Transaction banking — Bank statements (part 2 of 2)
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--earmarking-pismo-account-id` — API reference: Banking - Transaction banking — Earmarking (Pismo account ID)
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--payments-pismo-account-id` — API reference: Banking - Transaction banking — Payments (Pismo account ID)
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--customers` — API reference: Core platform - Accounts — Customers
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-API-core-platform-accounts--transfer-account` — API reference: Core platform - Accounts — Transfer account
- `KU-BANK-bank-statements-1` — Bank statements
- `KU-BANK-banking-overview` — Banking overview
- `KU-EVT-accounts-data-events` — Core platform - Accounts
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
