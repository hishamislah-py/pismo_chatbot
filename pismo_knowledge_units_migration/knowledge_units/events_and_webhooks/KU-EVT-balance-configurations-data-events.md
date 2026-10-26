---
ku_id: KU-EVT-balance-configurations-data-events
title: Core platform - Balance configurations
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/balance-configurations-data-events.md
  sha256: 5a9293c058fa866ca2367f814030531482119096e816c0b3013cec17021315bc
  url: https://developers.pismo.io/pismo-docs/docs/balance-configurations-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:14:50.000Z'
operations: []
related_kus:
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Core platform - Balance configurations

**KU ID:** `KU-EVT-balance-configurations-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/balance-configurations-data-events.md`:

> This table lists the balance configurations data events that the platform generates asynchronously. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/balance-configurations-data-events.md`: Core platform - Balance configurations

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/balance-configurations-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/balance-configurations-data-events · updatedAt: 2026-03-18T15:14:50.000Z

<!-- source:begin path=docs/data-and-reporting/balance-configurations-data-events.md part=0-end -->

# Core platform - Balance configurations

This table lists the balance configurations data events that the platform generates asynchronously. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint                                                      | Event                                                                                              |
| :------------------------------------------------------------ | :------------------------------------------------------------------------------------------------- |
| [Create balance configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config-1) | [Balance configuration created](https://developers.pismo.io/events/docs/balances-config-created-1) |
| [Replace balance configuration](https://developers.pismo.io/pismo-docs/reference/put-v1-balances-config-1) | [Balance configuration updated](https://developers.pismo.io/events/docs/balances-config-updated-1) |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.


### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `post-v1-balances-config-1` | API; Balance configurations API; Create balance configuration; balance configuration | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `put-v1-balances-config-1` | Replace balance configuration | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Lifecycle status

- `docs/data-and-reporting/balance-configurations-data-events.md`: updatedAt 2026-03-18T15:14:50.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.
- Operation link `post-v1-balances-config-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)
- Operation link `put-v1-balances-config-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/balance-configurations-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/balance-configurations-data-events | `5a9293c058fa866c…` | 2026-03-18T15:14:50.000Z |

## Related knowledge units

- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
