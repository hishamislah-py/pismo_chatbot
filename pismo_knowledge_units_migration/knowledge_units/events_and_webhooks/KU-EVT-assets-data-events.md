---
ku_id: KU-EVT-assets-data-events
title: Banking - Assets
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/assets-data-events.md
  sha256: 224a75f139ded5aa88214ddea8b4fd6ad4dd2d362138f78559d8345cbbde2719
  url: https://developers.pismo.io/pismo-docs/docs/assets-data-events
  role: primary_guide
  updated_at: '2026-03-20T19:08:15.000Z'
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
- KU-EVT-catalogue-assets
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Banking - Assets

**KU ID:** `KU-EVT-assets-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/assets-data-events.md`:

> This table lists the asset endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](doc:data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/assets-data-events.md`: Banking - Assets

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/assets-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/assets-data-events · updatedAt: 2026-03-20T19:08:15.000Z

<!-- source:begin path=docs/data-and-reporting/assets-data-events.md part=0-end -->

# Banking - Assets

This table lists the asset endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](doc:data-reporting-overview).

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Endpoint
      </th>

      <th style={{ textAlign: "left" }}>
        Event
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        [Register asset](https://developers.pismo.io/pismo-docs/reference/assetregistration)
      </td>

      <td style={{ textAlign: "left" }}>
        [Asset registration succeeded](https://developers.pismo.io/events/docs/assets-asset-registration-success-2) - Success\
        [Asset registration failed](https://developers.pismo.io/events/docs/assets-asset-registration-failure-1) - Failure
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update asset](https://developers.pismo.io/pismo-docs/reference/updateasset)
      </td>

      <td style={{ textAlign: "left" }}>
        [Asset updated](https://developers.pismo.io/events/docs/assets-asset-update-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Delete asset](https://developers.pismo.io/pismo-docs/reference/assetcancellation)
      </td>

      <td style={{ textAlign: "left" }}>
        [Asset status changed](https://developers.pismo.io/events/docs/assets-asset-status-change-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create asset redemption](https://developers.pismo.io/pismo-docs/reference/assetredemptionv2)
      </td>

      <td style={{ textAlign: "left" }}>
        [Asset redeemed](https://developers.pismo.io/events/docs/assets-asset-redemption-1) - Success\
        [Asset status changed](https://developers.pismo.io/events/docs/assets-asset-status-change-1) - Success\
        [Asset redemption failed](https://developers.pismo.io/events/docs/assets-asset-redemption-failure-1) - Failure
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Block/unblock asset](https://developers.pismo.io/pismo-docs/reference/assetblock)
      </td>

      <td style={{ textAlign: "left" }}>
        [Asset blocked](https://developers.pismo.io/events/docs/assets-asset-block-1) - Success\
        [Asset block failed](https://developers.pismo.io/events/docs/assets-asset-block-failure-1) - Failure
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update quota](https://developers.pismo.io/pismo-docs/reference/updatequota)
      </td>

      <td style={{ textAlign: "left" }}>
        [Quota updated](https://developers.pismo.io/events/docs/assets-quota-update-1)
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/issuer/{issuer_id}/assets` | `AssetRegistration` | Register banking asset | `api-specs/Banking_-_Assets.yaml` | no | KU-API-banking-assets--assets |
| `PATCH /v1/issuer/{issuer_id}/assets/{asset_id}` | `UpdateAsset` | Update banking asset | `api-specs/Banking_-_Assets.yaml` | no | KU-API-banking-assets--assets |
| `DELETE /v1/issuer/{issuer_id}/assets/{asset_id}` | `AssetCancellation` | Delete banking asset | `api-specs/Banking_-_Assets.yaml` | no | KU-API-banking-assets--assets |
| `PUT /v2/issuer/{issuer_id}/assets/{asset_id}/redemption` | `AssetRedemptionV2` | Create banking asset redemption | `api-specs/Banking_-_Assets.yaml` | no | KU-API-banking-assets--assets |
| `POST /v1/issuer/{issuer_id}/assets/{asset_id}/block` | `AssetBlock` | Block/unblock banking asset | `api-specs/Banking_-_Assets.yaml` | no | KU-API-banking-assets--assets |
| `PATCH /v1/issuer/{issuer_id}/assets/{asset_id}/quotas/{quota_id}` | `UpdateQuota` | Update quota | `api-specs/Banking_-_Assets.yaml` | no | KU-API-banking-assets--quotas |

### Operation essentials

- **`POST /v1/issuer/{issuer_id}/assets`** (`AssetRegistration`): security `BearerAuth`; required parameters `issuer_id` (path); required body fields `asset_id`, `registration_mode`, `asset_type`, `issuing_date`, `maturity_date`, `issued_units`, `unit_value`, `index_type`, `index_rate`, `customer_type`, `document_number`, `deposit_number`, `early_redemption_terms`, `currency`; response statuses 202, 400, 401, 404, 500; error codes in examples none; events `assets-asset-registration-failure-1`, `assets-asset-registration-success-1`.
- **`PATCH /v1/issuer/{issuer_id}/assets/{asset_id}`** (`UpdateAsset`): security `BearerAuth`; required parameters `issuer_id` (path), `asset_id` (path); required body fields `operation_type`; response statuses 200; error codes in examples none; events `assets-asset-update-1`.
- **`DELETE /v1/issuer/{issuer_id}/assets/{asset_id}`** (`AssetCancellation`): security `BearerAuth`; required parameters `issuer_id` (path), `asset_id` (path); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `assets-asset-status-change-1`.
- **`PUT /v2/issuer/{issuer_id}/assets/{asset_id}/redemption`** (`AssetRedemptionV2`): security `BearerAuth`; required parameters `issuer_id` (path), `asset_id` (path); required body fields `units`, `document_number`, `external_id`; response statuses 202, 400, 401, 404, 500; error codes in examples none; events `assets-asset-redemption-1`, `assets-asset-redemption-failure-1`, `assets-asset-status-change-1`.
- **`POST /v1/issuer/{issuer_id}/assets/{asset_id}/block`** (`AssetBlock`): security `BearerAuth`; required parameters `issuer_id` (path), `asset_id` (path); required body fields `units`, `document_number`; response statuses 202, 400, 401, 404, 500; error codes in examples none; events `assets-asset-block-1`, `assets-asset-block-failure-1`.
- **`PATCH /v1/issuer/{issuer_id}/assets/{asset_id}/quotas/{quota_id}`** (`UpdateQuota`): security `BearerAuth`; required parameters `issuer_id` (path), `asset_id` (path), `quota_id` (path); required body fields `operation_type`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `assets-quota-update-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `AssetBlock` | `assets-asset-block-1` |
| `AssetBlock` | `assets-asset-block-failure-1` |
| `AssetRedemptionV2` | `assets-asset-redemption-1` |
| `AssetRedemptionV2` | `assets-asset-redemption-failure-1` |
| `AssetRegistration` | `assets-asset-registration-failure-1` |
| `AssetRegistration` | `assets-asset-registration-success-1` |
| `AssetCancellation` | `assets-asset-status-change-1` |
| `AssetRedemptionV2` | `assets-asset-status-change-1` |
| `UpdateAsset` | `assets-asset-update-1` |
| `UpdateQuota` | `assets-quota-update-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `assets-asset-block-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-block-1 | 1 | KU-EVT-catalogue-assets |
| `assets-asset-block-failure-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-block-failure-1 | 1 | KU-EVT-catalogue-assets |
| `assets-asset-redemption-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-redemption-1 | 1 | KU-EVT-catalogue-assets |
| `assets-asset-redemption-failure-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-redemption-failure-1 | 1 | KU-EVT-catalogue-assets |
| `assets-asset-registration-failure-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-registration-failure-1 | 1 | KU-EVT-catalogue-assets |
| `assets-asset-status-change-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-status-change-1 | 2 | KU-EVT-catalogue-assets |
| `assets-asset-update-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-asset-update-1 | 1 | KU-EVT-catalogue-assets |
| `assets-quota-update-1` | assets | 1 | https://developers.pismo.io/events/docs/assets-quota-update-1 | 1 | KU-EVT-catalogue-assets |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/assets-data-events.md`: updatedAt 2026-03-20T19:08:15.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 9 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/assets-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/assets-data-events | `224a75f139ded5aa…` | 2026-03-20T19:08:15.000Z |

## Related knowledge units

- `KU-API-banking-assets--assets` — API reference: Banking - Assets — Assets
- `KU-API-banking-assets--quotas` — API reference: Banking - Assets — Quotas
- `KU-EVT-catalogue-assets` — Event catalogue: assets
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
