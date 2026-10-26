---
ku_id: KU-EVT-disputes-endpoint-generated-events
title: Card issuing - Disputes
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/disputes-endpoint-generated-events.md
  sha256: cf0f60e832c254c454ff7740a4c4e5a65e34ba74b6d945a995ea2951e00b85e5
  url: https://developers.pismo.io/pismo-docs/docs/disputes-endpoint-generated-events
  role: primary_guide
  updated_at: '2026-03-18T15:14:56.000Z'
operations:
- post-v1-disputes-disputeId-event
- post-v1-disputes-disputeId-installment
- post-v1-disputes-fraud-report
- post-v1-fee
- post-v1-networkauthorization-disputes
- put-v2-fraud-report
related_kus:
- KU-API-card-issuing-disputes--disputes-part-01
- KU-API-card-issuing-disputes--fees
- KU-API-card-issuing-disputes--fraud-report
- KU-API-card-issuing-disputes--installments
- KU-API-card-issuing-disputes--supporting-forms
- KU-EVT-catalogue-disputes
- KU-EVT-catalogue-other-domains
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Card issuing - Disputes

**KU ID:** `KU-EVT-disputes-endpoint-generated-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/disputes-endpoint-generated-events.md`:

> This table lists the disputes endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/disputes-endpoint-generated-events.md`: Card issuing - Disputes

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/disputes-endpoint-generated-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/disputes-endpoint-generated-events · updatedAt: 2026-03-18T15:14:56.000Z

<!-- source:begin path=docs/data-and-reporting/disputes-endpoint-generated-events.md part=0-end -->

# Card issuing - Disputes

This table lists the disputes endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

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
        [Create dispute installment](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-installment)
      </td>

      <td style={{ textAlign: "left" }}>
        [Dispute installment created](https://developers.pismo.io/events/docs/disputes-dispute-installment-creation-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create dispute](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes)
      </td>

      <td style={{ textAlign: "left" }}>
        [Dispute installment created](https://developers.pismo.io/events/docs/disputes-dispute-installment-creation-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event)\
        This event also occurs when a dispute status changes through other means, like network processing.
      </td>

      <td style={{ textAlign: "left" }}>
        [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create dispute fee](https://developers.pismo.io/pismo-docs/reference/post-v1-fee)
      </td>

      <td style={{ textAlign: "left" }}>
        [Dispute fee status created](https://developers.pismo.io/events/docs/disputes-dispute-fee-events-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        When authorization fraud report status changes via network processing
      </td>

      <td style={{ textAlign: "left" }}>
        [Authorization fraud report status changed](https://developers.pismo.io/events/docs/disputes-authorization-fraud-report-status-change-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create fraud report](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-fraud-report)
      </td>

      <td style={{ textAlign: "left" }}>
        [Fraud report created](https://developers.pismo.io/events/docs/fraud-report-fraud-report-creation-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update fraud report](https://developers.pismo.io/pismo-docs/reference/put-v2-fraud-report)
      </td>

      <td style={{ textAlign: "left" }}>
        [Fraud report updated](https://developers.pismo.io/events/docs/fraud-report-fraud-report-change-1)
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/disputes/{disputeId}/installment` | `post-v1-disputes-disputeId-installment` | Create dispute installment | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--installments |
| `POST /v1/networkauthorization-disputes` | `post-v1-networkauthorization-disputes` | Create dispute | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01 |
| `POST /v1/disputes/{disputeId}/event` | `post-v1-disputes-disputeId-event` | Update dispute status | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01 |
| `POST /v1/fee` | `post-v1-fee` | Create dispute fee | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--fees |
| `POST /v1/disputes/{disputeId}/fraud-report` | `post-v1-disputes-fraud-report` | Create dispute fraud report | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--supporting-forms |
| `PUT /v2/fraud-report/{fraudReportId}` | `put-v2-fraud-report` | Update fraud report | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--fraud-report |

### Operation essentials

- **`POST /v1/disputes/{disputeId}/installment`** (`post-v1-disputes-disputeId-installment`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `installment`, `arn`, `installment_disputed_amount`; response statuses 200, 400, 401, 404, 422, 500; error codes in examples none; events `disputes-dispute-installment-creation-1`.
- **`POST /v1/networkauthorization-disputes`** (`post-v1-networkauthorization-disputes`): security `BearerAuth`; required parameters `Authorization` (header); required body fields `modality`, `disputed_amount`, `is_partial`, `network_brand_type`; response statuses 200, 400, 401, 422, 500; error codes in examples none; events `disputes-dispute-installment-creation-1`.
- **`POST /v1/disputes/{disputeId}/event`** (`post-v1-disputes-disputeId-event`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `event`, `reason`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `disputes-dispute-installment-status-change-1`.
- **`POST /v1/fee`** (`post-v1-fee`): security `BearerAuth`; required parameters `Authorization` (header); required body fields `amount`, `card_id`, `credit_sender`, `credit_receiver`, `currency`, `destination_member`, `fee_date`, `network_brand_type`, `reason_code`; response statuses 200, 400, 401, 422, 500; error codes in examples none; events `disputes-dispute-fee-events-1`.
- **`POST /v1/disputes/{disputeId}/fraud-report`** (`post-v1-disputes-fraud-report`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `report`; response statuses 200, 401, 404, 422, 500; error codes in examples none; events none listed.
- **`PUT /v2/fraud-report/{fraudReportId}`** (`put-v2-fraud-report`): security `BearerAuth`; required parameters `fraudReportId` (path); required body fields none declared; response statuses 200, 400, 401, 404, 409, 422, 500, 504; error codes in examples `EDPT0002`, `EDPT0005`, `BDPT0006`, `BDPT0007`, `BDPT0001`, `BDPT0002`, `EDPT9999`, `EDPT0001`; events `fraud-report-fraud-report-change-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-fee` | `disputes-dispute-fee-events-1` |
| `post-v1-disputes-disputeId-installment` | `disputes-dispute-installment-creation-1` |
| `post-v1-networkauthorization-disputes` | `disputes-dispute-installment-creation-1` |
| `post-v1-disputes-disputeId-event` | `disputes-dispute-installment-status-change-1` |
| `put-v2-fraud-report` | `fraud-report-fraud-report-change-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `disputes-dispute-fee-events-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-dispute-fee-events-1 | 1 | KU-EVT-catalogue-disputes |
| `disputes-dispute-installment-creation-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-dispute-installment-creation-1 | 4 | KU-EVT-catalogue-disputes |
| `disputes-dispute-installment-status-change-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1 | 4 | KU-EVT-catalogue-disputes |
| `fraud-report-fraud-report-change-1` | fraud | 1 | https://developers.pismo.io/events/docs/fraud-report-fraud-report-change-1 | 1 | KU-EVT-catalogue-other-domains |
| `fraud-report-fraud-report-creation-1` | fraud | 1 | https://developers.pismo.io/events/docs/fraud-report-fraud-report-creation-1 | 1 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/disputes-endpoint-generated-events.md`: updatedAt 2026-03-18T15:14:56.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 6 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/disputes-endpoint-generated-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/disputes-endpoint-generated-events | `cf0f60e832c254c4…` | 2026-03-18T15:14:56.000Z |

## Related knowledge units

- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-API-card-issuing-disputes--fees` — API reference: Card issuing - Disputes — Fees
- `KU-API-card-issuing-disputes--fraud-report` — API reference: Card issuing - Disputes — Fraud report
- `KU-API-card-issuing-disputes--installments` — API reference: Card issuing - Disputes — Installments
- `KU-API-card-issuing-disputes--supporting-forms` — API reference: Card issuing - Disputes — Supporting forms
- `KU-EVT-catalogue-disputes` — Event catalogue: disputes
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
