---
ku_id: KU-EVT-merchants-data-events
title: Seller management - Merchants
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/merchants-data-events.md
  sha256: 6be84d77626169f881428099c1101f7c36b5ba78da7e03ba58030cf8b7f5fab2
  url: https://developers.pismo.io/pismo-docs/docs/merchants-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:15:23.000Z'
operations: []
related_kus:
- KU-EVT-catalogue-merchants
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Seller management - Merchants

**KU ID:** `KU-EVT-merchants-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/merchants-data-events.md`:

> This table lists the merchants and marketplaces endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/merchants-data-events.md`: Seller management - Merchants

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/merchants-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/merchants-data-events · updatedAt: 2026-03-18T15:15:23.000Z

<!-- source:begin path=docs/data-and-reporting/merchants-data-events.md part=0-end -->

# Seller management - Merchants

This table lists the merchants and marketplaces endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint                                                          | Event                                                                                                            |
| :---------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| [Create merchant transactions](https://developers.pismo.io/pismo-docs/reference/createmerchantusingmerchantid) | [Merchant transaction created](https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1) |
| [Create a reversal transaction](https://developers.pismo.io/pismo-docs/reference/createreversaltransaction)    | [Merchant transaction settled](https://developers.pismo.io/events/docs/merchants-merchant-transaction-settled-1) |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.


### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `createmerchantusingmerchantid` | Create merchant transaction; Create merchant transactions | not found in the current OpenAPI specifications. Name-based inference: link text "Create merchant transaction" equals the endpoint name "Create merchant transaction" in the removed-endpoints list (row Seller Management / Merchant transactions, date removed `7/24/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`post-merchant-transaction-sale` (POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions)); no source states that it replaces the removed endpoint. |
| `createreversaltransaction` | Create a reversal transaction; Create reversal transaction | not found in the current OpenAPI specifications. Name-based inference: link text "Create reversal transaction" equals the endpoint name "Create reversal transaction" in the removed-endpoints list (row Seller Management / Merchant transactions, date removed `7/24/2026`). This is a match on the endpoint name, not on an identifier. |

## Events

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `merchants-merchant-transaction-created-1` | merchants | 1 | https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1 | 5 | KU-EVT-catalogue-merchants |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/merchants-data-events.md`: updatedAt 2026-03-18T15:15:23.000Z.
- Links to `createmerchantusingmerchantid`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "Create merchant transaction" equals the endpoint name "Create merchant transaction" in the removed-endpoints list (row Seller Management / Merchant transactions, date removed `7/24/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`post-merchant-transaction-sale` (POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions)); no source states that it replaces the removed endpoint.
- Links to `createreversaltransaction`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "Create reversal transaction" equals the endpoint name "Create reversal transaction" in the removed-endpoints list (row Seller Management / Merchant transactions, date removed `7/24/2026`). This is a match on the endpoint name, not on an identifier.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/merchants-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/merchants-data-events | `6be84d77626169f8…` | 2026-03-18T15:15:23.000Z |

## Related knowledge units

- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
