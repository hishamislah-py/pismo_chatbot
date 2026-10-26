---
ku_id: KU-EVT-bank-slips-data-events
title: Banking - Integrated payments
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/bank-slips-data-events.md
  sha256: ba31d4f122c6c26b4fd6342115aa7520cd82e627f3089002295548c1a494a17a
  url: https://developers.pismo.io/pismo-docs/docs/bank-slips-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:15:08.000Z'
operations:
- post-integrated-payments-api-v1-bankslips-cashout
- post-integrated-payments-api-v1-bankslips-pay
related_kus:
- KU-API-banking-integrated-payments--bank-slip
- KU-API-banking-integrated-payments--transfer
- KU-EVT-catalogue-integrated
- KU-EVT-catalogue-other-domains
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Banking - Integrated payments

**KU ID:** `KU-EVT-bank-slips-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/bank-slips-data-events.md`:

> This table lists the integrated payments (bank slips) endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/bank-slips-data-events.md`: Banking - Integrated payments

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/bank-slips-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/bank-slips-data-events · updatedAt: 2026-03-18T15:15:08.000Z

<!-- source:begin path=docs/data-and-reporting/bank-slips-data-events.md part=0-end -->

# Banking - Integrated payments

This table lists the integrated payments (bank slips) endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

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
        [Pay bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-pay)
      </td>

      <td style={{ textAlign: "left" }}>
        [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1)\
        [Financial bankslips status change](https://developers.pismo.io/events/docs/integrated-payments-bankslip-status-change-1)\
        [Integrated payments financial reconciliation](https://developers.pismo.io/events/docs/integrated-payments-financial-reconciliation-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Cash-out transfer](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-cashout)
      </td>

      <td style={{ textAlign: "left" }}>
        [Transfer-out created](https://developers.pismo.io/events/docs/integrated-payments-transfer-out-created-1)\
        [Transfer-in created](https://developers.pismo.io/events/docs/integrated-payments-transfer-in-created-1)\
        [Financial transaction status updated](https://developers.pismo.io/events/docs/integrated-payments-transaction-status-change-1)\
        [Integrated payments financial reconciliation](https://developers.pismo.io/events/docs/integrated-payments-financial-reconciliation-1)
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/bankslips/pay` | `post-integrated-payments-api-v1-bankslips-pay` | Pay bank slip | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip |
| `POST /v1/transfers/cashout` | `post-integrated-payments-api-v1-bankslips-cashout` | Perform cash-out | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--transfer |

### Operation essentials

- **`POST /v1/bankslips/pay`** (`post-integrated-payments-api-v1-bankslips-pay`): security `BearerAuth`; required parameters `Authorization` (header), `x-idempotency-key` (header); required body fields `account_id`, `amount`; response statuses 202, 400, 403, 404, 409, 500, 502, 504; error codes in examples `EIP0005`, `EIP0006`, `EIP0008`, `EIP0010`, `EIP0012`, `EIP0013`, `EIP0017`, `EIP0023`, `EIP0020`, `EIP0061`, `EIP0005`, `EIP0006`, `EIP0009`, `EIP0030`, `EIP0049`, `EIP0063`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0011`, `EIP0015`, `EIP0019`, `EIP0022`, `EIP0028`, `EIP0041`, `EIP0051`, `EIP0053`, `EIP0069`, `EIP0070`, `EIP0018`, `EIP0021`, `EIP0024`, `EIP0002`; events `authorization-authorization-event-1`, `integrated-payments-bankslip-status-change-1`, `integrated-payments-financial-reconciliation-1`.
- **`POST /v1/transfers/cashout`** (`post-integrated-payments-api-v1-bankslips-cashout`): security `BearerAuth`; required parameters `Authorization` (header), `x-idempotency-key` (header); required body fields `account_id`, `amount`, `processing_code`; response statuses 202, 400, 403, 409, 500, 502, 504; error codes in examples `EIP0003`, `EIP0008`, `EIP0010`, `EIP0012`, `EIP0013`, `EIP0016`, `EIP0017`, `EIP0020`, `EIP0005`, `EIP0006`, `EIP0009`, `EIP0029`, `EIP0030`, `EIP0031`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0011`, `EIP0015`, `EIP0019`, `EIP0022`, `EIP0028`, `EIP0053`, `EIP0069`, `EIP0070`, `EIP0018`, `EIP0021`, `EIP0024`, `EIP0002`; events `integrated-payments-financial-reconciliation-1`, `integrated-payments-transaction-status-change-1`, `integrated-payments-transfer-out-created-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-integrated-payments-api-v1-bankslips-pay` | `authorization-authorization-event-1` |
| `post-integrated-payments-api-v1-bankslips-pay` | `integrated-payments-bankslip-status-change-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-financial-reconciliation-1` |
| `post-integrated-payments-api-v1-bankslips-pay` | `integrated-payments-financial-reconciliation-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-transaction-status-change-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-transfer-out-created-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `authorization-authorization-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-event-1 | 9 | KU-EVT-catalogue-other-domains |
| `integrated-payments-bankslip-status-change-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-bankslip-status-change-1 | 1 | KU-EVT-catalogue-integrated |
| `integrated-payments-financial-reconciliation-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-financial-reconciliation-1 | 2 | KU-EVT-catalogue-integrated |
| `integrated-payments-transaction-status-change-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-transaction-status-change-1 | 1 | KU-EVT-catalogue-integrated |
| `integrated-payments-transfer-out-created-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-transfer-out-created-1 | 1 | KU-EVT-catalogue-integrated |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/bank-slips-data-events.md`: updatedAt 2026-03-18T15:15:08.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 6 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/bank-slips-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/bank-slips-data-events | `ba31d4f122c6c26b…` | 2026-03-18T15:15:08.000Z |

## Related knowledge units

- `KU-API-banking-integrated-payments--bank-slip` — API reference: Banking - Integrated payments — Bank slip
- `KU-API-banking-integrated-payments--transfer` — API reference: Banking - Integrated payments — Transfer
- `KU-EVT-catalogue-integrated` — Event catalogue: integrated
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
