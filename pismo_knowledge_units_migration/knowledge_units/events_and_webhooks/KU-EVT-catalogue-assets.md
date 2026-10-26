---
ku_id: KU-EVT-catalogue-assets
title: 'Event catalogue: assets'
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
- AssetBlock
- AssetCancellation
- AssetRedemptionV2
- AssetRegistration
- UpdateAsset
- UpdateQuota
related_kus:
- KU-API-banking-assets--assets
- KU-API-banking-assets--quotas
- KU-EVT-assets-data-events
events:
- assets-asset-block-1
- assets-asset-block-failure-1
- assets-asset-redemption-1
- assets-asset-redemption-failure-1
- assets-asset-registration-failure-1
- assets-asset-registration-success-1
- assets-asset-status-change-1
- assets-asset-update-1
- assets-quota-update-1
---

# Event catalogue: assets

**KU ID:** `KU-EVT-catalogue-assets` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 9 event type(s) whose inventory domain is assets, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `assets-asset-block-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-block-1 | 1 | Banking_-_Assets |
| `assets-asset-block-failure-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-block-failure-1 | 1 | Banking_-_Assets |
| `assets-asset-redemption-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-redemption-1 | 1 | Banking_-_Assets |
| `assets-asset-redemption-failure-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-redemption-failure-1 | 1 | Banking_-_Assets |
| `assets-asset-registration-failure-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-registration-failure-1 | 1 | Banking_-_Assets |
| `assets-asset-registration-success-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-registration-success-1 | 1 | Banking_-_Assets |
| `assets-asset-status-change-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-status-change-1 | 2 | Banking_-_Assets |
| `assets-asset-update-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-update-1 | 1 | Banking_-_Assets |
| `assets-quota-update-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-quota-update-1 | 1 | Banking_-_Assets |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `assets-asset-block-1` | `POST /v1/issuer/{issuer_id}/assets/{asset_id}/block` | `AssetBlock` | `Banking_-_Assets` | KU-API-banking-assets--assets |
| `assets-asset-block-failure-1` | `POST /v1/issuer/{issuer_id}/assets/{asset_id}/block` | `AssetBlock` | `Banking_-_Assets` | KU-API-banking-assets--assets |
| `assets-asset-redemption-1` | `PUT /v2/issuer/{issuer_id}/assets/{asset_id}/redemption` | `AssetRedemptionV2` | `Banking_-_Assets` | KU-API-banking-assets--assets |
| `assets-asset-redemption-failure-1` | `PUT /v2/issuer/{issuer_id}/assets/{asset_id}/redemption` | `AssetRedemptionV2` | `Banking_-_Assets` | KU-API-banking-assets--assets |
| `assets-asset-registration-failure-1` | `POST /v1/issuer/{issuer_id}/assets` | `AssetRegistration` | `Banking_-_Assets` | KU-API-banking-assets--assets |
| `assets-asset-registration-success-1` | `POST /v1/issuer/{issuer_id}/assets` | `AssetRegistration` | `Banking_-_Assets` | KU-API-banking-assets--assets |
| `assets-asset-status-change-1` | `DELETE /v1/issuer/{issuer_id}/assets/{asset_id}` | `AssetCancellation` | `Banking_-_Assets` | KU-API-banking-assets--assets |
| `assets-asset-status-change-1` | `PUT /v2/issuer/{issuer_id}/assets/{asset_id}/redemption` | `AssetRedemptionV2` | `Banking_-_Assets` | KU-API-banking-assets--assets |
| `assets-asset-update-1` | `PATCH /v1/issuer/{issuer_id}/assets/{asset_id}` | `UpdateAsset` | `Banking_-_Assets` | KU-API-banking-assets--assets |
| `assets-quota-update-1` | `PATCH /v1/issuer/{issuer_id}/assets/{asset_id}/quotas/{quota_id}` | `UpdateQuota` | `Banking_-_Assets` | KU-API-banking-assets--quotas |

## Guides that link to these events

- `assets-asset-block-1`: `KU-EVT-assets-data-events`
- `assets-asset-block-failure-1`: `KU-EVT-assets-data-events`
- `assets-asset-redemption-1`: `KU-EVT-assets-data-events`
- `assets-asset-redemption-failure-1`: `KU-EVT-assets-data-events`
- `assets-asset-registration-failure-1`: `KU-EVT-assets-data-events`
- `assets-asset-status-change-1`: `KU-EVT-assets-data-events`
- `assets-asset-update-1`: `KU-EVT-assets-data-events`
- `assets-quota-update-1`: `KU-EVT-assets-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: assets-asset-block-1, assets-asset-block-failure-1, assets-asset-redemption-1, assets-asset-redemption-failure-1, assets-asset-registration-failure-1, assets-asset-registration-success-1, assets-asset-status-change-1, assets-asset-update-1, assets-quota-update-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-assets--assets` — API reference: Banking - Assets — Assets
- `KU-API-banking-assets--quotas` — API reference: Banking - Assets — Quotas
- `KU-EVT-assets-data-events` — Banking - Assets
