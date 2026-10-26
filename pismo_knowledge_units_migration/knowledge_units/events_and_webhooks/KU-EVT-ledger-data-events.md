---
ku_id: KU-EVT-ledger-data-events
title: Core platform - Ledger
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/ledger-data-events.md
  sha256: 901b313eda9577f43765ce9a8c87145fda125818669584c67f0f35d61985c745
  url: https://developers.pismo.io/pismo-docs/docs/ledger-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:14:52.000Z'
operations:
- patch-v1-account-limit
related_kus:
- KU-API-core-platform-ledger--account-limits
- KU-EVT-catalogue-other-domains
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Core platform - Ledger

**KU ID:** `KU-EVT-ledger-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/ledger-data-events.md`:

> This table lists the ledger endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/ledger-data-events.md`: Core platform - Ledger

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/ledger-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/ledger-data-events · updatedAt: 2026-03-18T15:14:52.000Z

<!-- source:begin path=docs/data-and-reporting/ledger-data-events.md part=0-end -->

# Core platform - Ledger

This table lists the ledger endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint                                                                                            | Event                                                                                                     |
| :-------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit)                                                 | [Account limit changed](https://developers.pismo.io/events/docs/ledger-limit-changed-1)                   |
| This event occurs asynchronously when account balance changes due to any relevant account activity. | [Available ledger balance changed](https://developers.pismo.io/events/docs/availables-change-available-1) |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limit` | Update account limits (outdated) | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |

### Operation essentials

- **`PATCH /v1/accounts/{accountId}/limits`** (`patch-v1-account-limit`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `WLDG0021`, `WLDG0010`, `WLDG0025`, `WLDG0022`, `ELDG9999`; events `ledger-limit-changed-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-v1-account-limit` | `ledger-limit-changed-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `availables-change-available-1` | availables | 1 | https://developers.pismo.io/events/docs/availables-change-available-1 | 22 | KU-EVT-catalogue-other-domains |
| `ledger-limit-changed-1` | ledger | 1 | https://developers.pismo.io/events/docs/ledger-limit-changed-1 | 2 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/ledger-data-events.md`: updatedAt 2026-03-18T15:14:52.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/ledger-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/ledger-data-events | `901b313eda9577f4…` | 2026-03-18T15:14:52.000Z |

## Related knowledge units

- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
