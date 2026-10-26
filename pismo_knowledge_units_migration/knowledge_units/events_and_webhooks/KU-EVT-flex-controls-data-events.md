---
ku_id: KU-EVT-flex-controls-data-events
title: Core platform - Flex controls
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/flex-controls-data-events.md
  sha256: 259145c1ba1e1af7d3bc946e25c4c1e863ccb7aebd054ce45df01e7113c0584e
  url: https://developers.pismo.io/pismo-docs/docs/flex-controls-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:14:49.000Z'
operations:
- patch-v1-accounts-flex-control
- patch-v1-customers-flex-control
- post-v1-accounts-flex-controls
- post-v1-customers-flex-controls
related_kus:
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-flex-controls--customer-flex-controls-part-01
- KU-API-core-platform-flex-controls--customer-flex-controls-part-02
- KU-EVT-catalogue-audit
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Core platform - Flex controls

**KU ID:** `KU-EVT-flex-controls-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/flex-controls-data-events.md`:

> This table lists the flex controls data events that the platform generates asynchronously. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/flex-controls-data-events.md`: Core platform - Flex controls

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/flex-controls-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/flex-controls-data-events · updatedAt: 2026-03-18T15:14:49.000Z

<!-- source:begin path=docs/data-and-reporting/flex-controls-data-events.md part=0-end -->

# Core platform - Flex controls

This table lists the flex controls data events that the platform generates asynchronously. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint                                                                                                                                                                        | Event                                                                                                                |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------- |
| [Create account flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls)                                                                                                               | [Account flex control created](https://developers.pismo.io/events/docs/audit-account-spending-limit-created-1)       |
| [Update account flex control](https://developers.pismo.io/pismo-docs/reference/patch-v1-accounts-flex-control)                                                                                                               | [Account flex control updated](https://developers.pismo.io/events/docs/audit-account-spending-limit-updated-1)       |
| [Create customer flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-customers-flex-controls)                                                                                                             | [Customer spending limit created](https://developers.pismo.io/events/docs/audit-customer-spending-limit-created-1)   |
| [Update customer flex control](https://developers.pismo.io/pismo-docs/reference/patch-v1-customers-flex-control)                                                                                                             | [Customer spending limit updated](https://developers.pismo.io/events/docs/audit-customer-spending-limit-updated-1)   |
| This event occurs asynchronously when the platform completes an evaluation request of a flex control.                                                                           | [Evaluation requested](https://developers.pismo.io/events/docs/audit-evaluation-requested-1)                         |
| This event occurs asynchronously when the platform completes a rollback request of the flex control evaluation.                                                                 | [Evaluation rollback request created](https://developers.pismo.io/events/docs/audit-evaluation-rollback-requested-1) |
| This event occurs when the platform creates a flex controls template. To create a flex controls template, use Pismo Control Center or contact the Pismo support representative. | [Flex control template created](https://developers.pismo.io/events/docs/audit-template-created-1)                    |
| This event occurs when the platform updates a flex controls template. To update a flex controls template, use Pismo Control Center or contact the Pismo support representative. | [Flex control template updated](https://developers.pismo.io/events/docs/audit-template-updated-1)                    |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/accounts/{accountId}/flex-controls` | `post-v1-accounts-flex-controls` | Create account flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `PATCH /v1/accounts/{accountId}/flex-controls/{flexControlId}` | `patch-v1-accounts-flex-control` | Update account flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /v1/customers/{customerId}/flex-controls` | `post-v1-customers-flex-controls` | Create customer flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--customer-flex-controls-part-01 |
| `PATCH /v1/customers/{customerId}/flex-controls/{flexControlId}` | `patch-v1-customers-flex-control` | Update customer flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--customer-flex-controls-part-02 |

### Operation essentials

- **`POST /v1/accounts/{accountId}/flex-controls`** (`post-v1-accounts-flex-controls`): security `BearerAuth`; required parameters `accountId` (path); required body fields `type`, `name`, `deny_code`; response statuses 201, 400, 403, 409, 500; error codes in examples `ERUL0701`, `RULVAL0400`, `ERUL0702`, `ERUL0703`, `ERUL0704`, `ERUL0706`, `ERUL0004`, `ERUL0002`, `RULVAL0403`, `WRUL0707`, `RULVAL0409`, `ERUL0001`, `RULREP0500`; events `audit-account-spending-limit-created-1`.
- **`PATCH /v1/accounts/{accountId}/flex-controls/{flexControlId}`** (`patch-v1-accounts-flex-control`): security `BearerAuth`; required parameters `accountId` (path), `flexControlId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `ERUL1001`, `RULVAL0400`, `ERUL1002`, `ERUL1003`, `ERUL1004`, `ERUL1005`, `ERUL1006`, `ERUL1007`, `ERUL0003`, `RULREP0404`, `ERUL0001`, `RULREP0500`; events `audit-account-spending-limit-updated-1`.
- **`POST /v1/customers/{customerId}/flex-controls`** (`post-v1-customers-flex-controls`): security `BearerAuth`; required parameters `customerId` (path); required body fields `type`, `name`, `account_id`; response statuses 201, 400, 403, 409, 500; error codes in examples `ERUL1101`, `RULVAL0400`, `ERUL1102`, `ERUL1106`, `ERUL0002`, `RULVAL0403`, `WRUL1207`, `RULVAL0409`, `ERUL0005`, `RULREP0500`, `ERUL1105`; events `audit-customer-spending-limit-created-1`.
- **`PATCH /v1/customers/{customerId}/flex-controls/{flexControlId}`** (`patch-v1-customers-flex-control`): security `BearerAuth`; required parameters `customerId` (path), `flexControlId` (path); required body fields none declared; response statuses 200, 400, 403, 404, 500; error codes in examples `ERUL1401`, `RULVAL0400`, `ERUL1402`, `ERUL1403`, `ERUL1406`, `ERUL0002`, `RULVAL0403`, `ERUL1204`, `RULREP0404`, `ERUL1205`, `RULVAL0400`, `ERUL1203`, `RULREP0500`; events `audit-customer-spending-limit-updated-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-accounts-flex-controls` | `audit-account-spending-limit-created-1` |
| `patch-v1-accounts-flex-control` | `audit-account-spending-limit-updated-1` |
| `post-v1-customers-flex-controls` | `audit-customer-spending-limit-created-1` |
| `patch-v1-customers-flex-control` | `audit-customer-spending-limit-updated-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `audit-account-spending-limit-created-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-account-spending-limit-created-1 | 1 | KU-EVT-catalogue-audit |
| `audit-account-spending-limit-updated-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-account-spending-limit-updated-1 | 1 | KU-EVT-catalogue-audit |
| `audit-customer-spending-limit-created-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-customer-spending-limit-created-1 | 1 | KU-EVT-catalogue-audit |
| `audit-customer-spending-limit-updated-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-customer-spending-limit-updated-1 | 1 | KU-EVT-catalogue-audit |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/flex-controls-data-events.md`: updatedAt 2026-03-18T15:14:49.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 8 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/flex-controls-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/flex-controls-data-events | `259145c1ba1e1af7…` | 2026-03-18T15:14:49.000Z |

## Related knowledge units

- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-01` — API reference: Core platform - Flex controls — Customer flex controls (part 1 of 2)
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-02` — API reference: Core platform - Flex controls — Customer flex controls (part 2 of 2)
- `KU-EVT-catalogue-audit` — Event catalogue: audit
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
