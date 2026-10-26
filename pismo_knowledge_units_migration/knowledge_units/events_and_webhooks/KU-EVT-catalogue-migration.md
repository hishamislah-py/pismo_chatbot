---
ku_id: KU-EVT-catalogue-migration
title: 'Event catalogue: migration'
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
- PostAccountsV2
- PostAccrualsV1
- PostAuthorizationsV1
- PostBalanceControlV1
- PostCardsV1
- PostCustomersV1
- PostFeeModelV1
- PostGoLiveV1
- PostMerchantTransactionsV1
- PostMerchantsV1
- PostOnUsAuthorizationsV1
- PostPciCardsV1
- PostPreGoLiveV1
- PostRecurringChargeLinksV1
- PostRecurringChargePlansV1
- PostStatementsV1
- PostTokensV1
- PostTransactionsV1
related_kus:
- KU-API-migrations--account-migration
- KU-API-migrations--accrual-migration
- KU-API-migrations--authorization-migration
- KU-API-migrations--balance-migration
- KU-API-migrations--card-migration
- KU-API-migrations--customer-migration
- KU-API-migrations--fee-model-migration
- KU-API-migrations--merchant-migration
- KU-API-migrations--merchant-transaction-migration
- KU-API-migrations--on-us-authorization-migration
- KU-API-migrations--recurring-charge-link-migration
- KU-API-migrations--recurring-charge-plan-migration
- KU-API-migrations--statement-migration
- KU-API-migrations--token-migration
- KU-API-migrations--transaction-migration
- KU-CORE-migrations-overview
- KU-EVT-migrations-data-events
events:
- migration-account-go-live-outgoing-1
- migration-account-incoming-2
- migration-account-outgoing-2
- migration-account-pre-go-live-outgoing-1
- migration-accrual-incoming-1
- migration-accrual-outgoing-1
- migration-authorization-incoming-1
- migration-authorization-outgoing-1
- migration-balance-control-incoming-1
- migration-balance-control-outgoing-1
- migration-card-incoming-1
- migration-card-mode-outgoing-1
- migration-card-outgoing-1
- migration-customer-incoming-1
- migration-customer-outgoing-1
- migration-fee-model-account-incoming-1
- migration-fee-model-account-outgoing-1
- migration-instant-payment-outgoing-1
- migration-merchant-incoming-1
- migration-merchant-outgoing-1
- migration-merchant-transaction-incoming-1
- migration-merchant-transaction-outgoing-1
- migration-on-us-authorization-incoming-1
- migration-on-us-authorization-outgoing-1
- migration-organize-statement-outgoing-1
- migration-payment-agreements-outgoing-1
- migration-pci-card-outgoing-1
- migration-pre-go-live-outgoing-1
- migration-recurring-charge-link-incoming-1
- migration-recurring-charge-link-outgoing-1
- migration-recurring-charge-plan-incoming-1
- migration-recurring-charge-plan-outgoing-1
- migration-statement-incoming-1
- migration-statement-outgoing-1
- migration-token-incoming-1
- migration-token-outgoing-1
- migration-transaction-incoming-1
- migration-transaction-outgoing-1
---

# Event catalogue: migration

**KU ID:** `KU-EVT-catalogue-migration` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 38 event type(s) whose inventory domain is migration, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `migration-account-go-live-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-account-go-live-outgoing-1 | 1 | Migrations |
| `migration-account-incoming-2` | migration | 2 | https://developers.pismo.io/events/docs/migration-account-incoming-2 | 1 | Migrations |
| `migration-account-outgoing-2` | migration | 2 | https://developers.pismo.io/events/docs/migration-account-outgoing-2 | 1 | Migrations |
| `migration-account-pre-go-live-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-account-pre-go-live-outgoing-1 | 1 | Migrations |
| `migration-accrual-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-accrual-incoming-1 | 1 | Migrations |
| `migration-accrual-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-accrual-outgoing-1 | 1 | Migrations |
| `migration-authorization-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-authorization-incoming-1 | 1 | Migrations |
| `migration-authorization-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-authorization-outgoing-1 | 1 | Migrations |
| `migration-balance-control-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-balance-control-incoming-1 | 1 | Migrations |
| `migration-balance-control-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-balance-control-outgoing-1 | 1 | Migrations |
| `migration-card-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-card-incoming-1 | 1 | Migrations |
| `migration-card-mode-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-card-mode-outgoing-1 | 1 | Migrations |
| `migration-card-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-card-outgoing-1 | 1 | Migrations |
| `migration-customer-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-customer-incoming-1 | 1 | Migrations |
| `migration-customer-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-customer-outgoing-1 | 1 | Migrations |
| `migration-fee-model-account-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-fee-model-account-incoming-1 | 1 | Migrations |
| `migration-fee-model-account-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-fee-model-account-outgoing-1 | 1 | Migrations |
| `migration-instant-payment-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-instant-payment-outgoing-1 | 1 | Migrations |
| `migration-merchant-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-merchant-incoming-1 | 1 | Migrations |
| `migration-merchant-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-merchant-outgoing-1 | 1 | Migrations |
| `migration-merchant-transaction-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-merchant-transaction-incoming-1 | 1 | Migrations |
| `migration-merchant-transaction-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-merchant-transaction-outgoing-1 | 1 | Migrations |
| `migration-on-us-authorization-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-on-us-authorization-incoming-1 | 1 | Migrations |
| `migration-on-us-authorization-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-on-us-authorization-outgoing-1 | 1 | Migrations |
| `migration-organize-statement-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-organize-statement-outgoing-1 | 4 | Migrations |
| `migration-payment-agreements-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-payment-agreements-outgoing-1 | 1 | Migrations |
| `migration-pci-card-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-pci-card-outgoing-1 | 1 | Migrations |
| `migration-pre-go-live-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-pre-go-live-outgoing-1 | 1 | Migrations |
| `migration-recurring-charge-link-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-recurring-charge-link-incoming-1 | 1 | Migrations |
| `migration-recurring-charge-link-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-recurring-charge-link-outgoing-1 | 1 | Migrations |
| `migration-recurring-charge-plan-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-recurring-charge-plan-incoming-1 | 1 | Migrations |
| `migration-recurring-charge-plan-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-recurring-charge-plan-outgoing-1 | 1 | Migrations |
| `migration-statement-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-statement-incoming-1 | 1 | Migrations |
| `migration-statement-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-statement-outgoing-1 | 1 | Migrations |
| `migration-token-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-token-incoming-1 | 1 | Migrations |
| `migration-token-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-token-outgoing-1 | 1 | Migrations |
| `migration-transaction-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-transaction-incoming-1 | 1 | Migrations |
| `migration-transaction-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-transaction-outgoing-1 | 1 | Migrations |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `migration-account-go-live-outgoing-1` | `POST /v1/migrations/go-live` | `PostGoLiveV1` | `Migrations` | KU-API-migrations--account-migration |
| `migration-account-incoming-2` | `POST /v2/migrations/accounts` | `PostAccountsV2` | `Migrations` | KU-API-migrations--account-migration |
| `migration-account-outgoing-2` | `POST /v2/migrations/accounts` | `PostAccountsV2` | `Migrations` | KU-API-migrations--account-migration |
| `migration-account-pre-go-live-outgoing-1` | `POST /v1/migrations/pre-go-live` | `PostPreGoLiveV1` | `Migrations` | KU-API-migrations--account-migration |
| `migration-accrual-incoming-1` | `POST /v1/migrations/accruals` | `PostAccrualsV1` | `Migrations` | KU-API-migrations--accrual-migration |
| `migration-accrual-outgoing-1` | `POST /v1/migrations/accruals` | `PostAccrualsV1` | `Migrations` | KU-API-migrations--accrual-migration |
| `migration-authorization-incoming-1` | `POST /v1/migrations/authorizations` | `PostAuthorizationsV1` | `Migrations` | KU-API-migrations--authorization-migration |
| `migration-authorization-outgoing-1` | `POST /v1/migrations/authorizations` | `PostAuthorizationsV1` | `Migrations` | KU-API-migrations--authorization-migration |
| `migration-balance-control-incoming-1` | `POST /v1/migrations/balance-control` | `PostBalanceControlV1` | `Migrations` | KU-API-migrations--balance-migration |
| `migration-balance-control-outgoing-1` | `POST /v1/migrations/balance-control` | `PostBalanceControlV1` | `Migrations` | KU-API-migrations--balance-migration |
| `migration-card-incoming-1` | `POST /v1/migrations/cards` | `PostCardsV1` | `Migrations` | KU-API-migrations--card-migration |
| `migration-card-mode-outgoing-1` | `POST /v1/migrations/cards` | `PostCardsV1` | `Migrations` | KU-API-migrations--card-migration |
| `migration-card-outgoing-1` | `POST /v1/migrations/cards` | `PostCardsV1` | `Migrations` | KU-API-migrations--card-migration |
| `migration-customer-incoming-1` | `POST /v1/migrations/customers` | `PostCustomersV1` | `Migrations` | KU-API-migrations--customer-migration |
| `migration-customer-outgoing-1` | `POST /v1/migrations/customers` | `PostCustomersV1` | `Migrations` | KU-API-migrations--customer-migration |
| `migration-fee-model-account-incoming-1` | `POST /v1/migrations/fee-model-account` | `PostFeeModelV1` | `Migrations` | KU-API-migrations--fee-model-migration |
| `migration-fee-model-account-outgoing-1` | `POST /v1/migrations/fee-model-account` | `PostFeeModelV1` | `Migrations` | KU-API-migrations--fee-model-migration |
| `migration-instant-payment-outgoing-1` | `POST /v1/migrations/transactions` | `PostTransactionsV1` | `Migrations` | KU-API-migrations--transaction-migration |
| `migration-merchant-incoming-1` | `POST /v1/migrations/merchants` | `PostMerchantsV1` | `Migrations` | KU-API-migrations--merchant-migration |
| `migration-merchant-outgoing-1` | `POST /v1/migrations/merchants` | `PostMerchantsV1` | `Migrations` | KU-API-migrations--merchant-migration |
| `migration-merchant-transaction-incoming-1` | `POST /v1/migrations/merchants/transactions` | `PostMerchantTransactionsV1` | `Migrations` | KU-API-migrations--merchant-transaction-migration |
| `migration-merchant-transaction-outgoing-1` | `POST /v1/migrations/merchants/transactions` | `PostMerchantTransactionsV1` | `Migrations` | KU-API-migrations--merchant-transaction-migration |
| `migration-on-us-authorization-incoming-1` | `POST /v1/migrations/on-us-authorizations` | `PostOnUsAuthorizationsV1` | `Migrations` | KU-API-migrations--on-us-authorization-migration |
| `migration-on-us-authorization-outgoing-1` | `POST /v1/migrations/on-us-authorizations` | `PostOnUsAuthorizationsV1` | `Migrations` | KU-API-migrations--on-us-authorization-migration |
| `migration-organize-statement-outgoing-1` | `POST /v1/migrations/pre-go-live` | `PostPreGoLiveV1` | `Migrations` | KU-API-migrations--account-migration |
| `migration-organize-statement-outgoing-1` | `POST /v1/migrations/accruals` | `PostAccrualsV1` | `Migrations` | KU-API-migrations--accrual-migration |
| `migration-organize-statement-outgoing-1` | `POST /v1/migrations/balance-control` | `PostBalanceControlV1` | `Migrations` | KU-API-migrations--balance-migration |
| `migration-organize-statement-outgoing-1` | `POST /v1/migrations/transactions` | `PostTransactionsV1` | `Migrations` | KU-API-migrations--transaction-migration |
| `migration-payment-agreements-outgoing-1` | `POST /v1/migrations/transactions` | `PostTransactionsV1` | `Migrations` | KU-API-migrations--transaction-migration |
| `migration-pci-card-outgoing-1` | `POST /v1/migrations/cards-pci` | `PostPciCardsV1` | `Migrations` | KU-API-migrations--card-migration |
| `migration-pre-go-live-outgoing-1` | `POST /v1/migrations/pre-go-live` | `PostPreGoLiveV1` | `Migrations` | KU-API-migrations--account-migration |
| `migration-recurring-charge-link-incoming-1` | `POST /v1/migrations/recurring-charge-links` | `PostRecurringChargeLinksV1` | `Migrations` | KU-API-migrations--recurring-charge-link-migration |
| `migration-recurring-charge-link-outgoing-1` | `POST /v1/migrations/recurring-charge-links` | `PostRecurringChargeLinksV1` | `Migrations` | KU-API-migrations--recurring-charge-link-migration |
| `migration-recurring-charge-plan-incoming-1` | `POST /v1/migrations/recurring-charge-plans` | `PostRecurringChargePlansV1` | `Migrations` | KU-API-migrations--recurring-charge-plan-migration |
| `migration-recurring-charge-plan-outgoing-1` | `POST /v1/migrations/recurring-charge-plans` | `PostRecurringChargePlansV1` | `Migrations` | KU-API-migrations--recurring-charge-plan-migration |
| `migration-statement-incoming-1` | `POST /v1/migrations/statements` | `PostStatementsV1` | `Migrations` | KU-API-migrations--statement-migration |
| `migration-statement-outgoing-1` | `POST /v1/migrations/statements` | `PostStatementsV1` | `Migrations` | KU-API-migrations--statement-migration |
| `migration-token-incoming-1` | `POST /v1/migrations/tokens` | `PostTokensV1` | `Migrations` | KU-API-migrations--token-migration |
| `migration-token-outgoing-1` | `POST /v1/migrations/tokens` | `PostTokensV1` | `Migrations` | KU-API-migrations--token-migration |
| `migration-transaction-incoming-1` | `POST /v1/migrations/transactions` | `PostTransactionsV1` | `Migrations` | KU-API-migrations--transaction-migration |
| `migration-transaction-outgoing-1` | `POST /v1/migrations/transactions` | `PostTransactionsV1` | `Migrations` | KU-API-migrations--transaction-migration |

## Guides that link to these events

- `migration-account-incoming-2`: `KU-CORE-migrations-overview`
- `migration-account-outgoing-2`: `KU-CORE-migrations-overview`
- `migration-account-pre-go-live-outgoing-1`: `KU-CORE-migrations-overview`
- `migration-card-incoming-1`: `KU-EVT-migrations-data-events`
- `migration-card-outgoing-1`: `KU-EVT-migrations-data-events`
- `migration-statement-incoming-1`: `KU-EVT-migrations-data-events`
- `migration-statement-outgoing-1`: `KU-EVT-migrations-data-events`
- `migration-transaction-incoming-1`: `KU-EVT-migrations-data-events`
- `migration-transaction-outgoing-1`: `KU-EVT-migrations-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: migration-account-go-live-outgoing-1, migration-account-incoming-2, migration-account-outgoing-2, migration-account-pre-go-live-outgoing-1, migration-accrual-incoming-1, migration-accrual-outgoing-1, migration-authorization-incoming-1, migration-authorization-outgoing-1, migration-balance-control-incoming-1, migration-balance-control-outgoing-1, migration-card-incoming-1, migration-card-mode-outgoing-1, migration-card-outgoing-1, migration-customer-incoming-1, migration-customer-outgoing-1, migration-fee-model-account-incoming-1, migration-fee-model-account-outgoing-1, migration-instant-payment-outgoing-1, migration-merchant-incoming-1, migration-merchant-outgoing-1, migration-merchant-transaction-incoming-1, migration-merchant-transaction-outgoing-1, migration-on-us-authorization-incoming-1, migration-on-us-authorization-outgoing-1, migration-organize-statement-outgoing-1, migration-payment-agreements-outgoing-1, migration-pci-card-outgoing-1, migration-pre-go-live-outgoing-1, migration-recurring-charge-link-incoming-1, migration-recurring-charge-link-outgoing-1, migration-recurring-charge-plan-incoming-1, migration-recurring-charge-plan-outgoing-1, migration-statement-incoming-1, migration-statement-outgoing-1, migration-token-incoming-1, migration-token-outgoing-1, migration-transaction-incoming-1, migration-transaction-outgoing-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-migrations--account-migration` — API reference: Migrations — Account migration
- `KU-API-migrations--accrual-migration` — API reference: Migrations — Accrual migration
- `KU-API-migrations--authorization-migration` — API reference: Migrations — Authorization migration
- `KU-API-migrations--balance-migration` — API reference: Migrations — Balance migration
- `KU-API-migrations--card-migration` — API reference: Migrations — Card migration
- `KU-API-migrations--customer-migration` — API reference: Migrations — Customer migration
- `KU-API-migrations--fee-model-migration` — API reference: Migrations — Fee model migration
- `KU-API-migrations--merchant-migration` — API reference: Migrations — Merchant migration
- `KU-API-migrations--merchant-transaction-migration` — API reference: Migrations — Merchant transaction migration
- `KU-API-migrations--on-us-authorization-migration` — API reference: Migrations — On-us authorization migration
- `KU-API-migrations--recurring-charge-link-migration` — API reference: Migrations — Recurring charge link migration
- `KU-API-migrations--recurring-charge-plan-migration` — API reference: Migrations — Recurring charge plan migration
- `KU-API-migrations--statement-migration` — API reference: Migrations — Statement migration
- `KU-API-migrations--token-migration` — API reference: Migrations — Token migration
- `KU-API-migrations--transaction-migration` — API reference: Migrations — Transaction migration
- `KU-CORE-migrations-overview` — Migrations
- `KU-EVT-migrations-data-events` — Migrations events
