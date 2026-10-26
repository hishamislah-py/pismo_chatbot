---
ku_id: KU-EVT-depositary-data-events
title: Banking - Credit receivables
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/depositary-data-events.md
  sha256: 9fc3a9a2940dc0ba944c603b9a1040870a2866beeaf8ae2e2dcadb6bd51746c2
  url: https://developers.pismo.io/pismo-docs/docs/depositary-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:15:07.000Z'
operations:
- create-receivable
- delete-receivable
- findByAccessKey
- update
- validateUnicity
related_kus:
- KU-API-banking-credit-receivables--invoices
- KU-API-banking-credit-receivables--receivable
- KU-EVT-catalogue-depositary
grouping_rationale: single source page
---

# Banking - Credit receivables

**KU ID:** `KU-EVT-depositary-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/depositary-data-events.md`:

> Endpoint

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/depositary-data-events.md`: Banking - Credit receivables

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/depositary-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/depositary-data-events · updatedAt: 2026-03-18T15:15:07.000Z

<!-- source:begin path=docs/data-and-reporting/depositary-data-events.md part=0-end -->

# Banking - Credit receivables

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
        [Register receivable](https://developers.pismo.io/pismo-docs/reference/create-receivable)
      </td>

      <td style={{ textAlign: "left" }}>
        [Credit rights receivable registration failure](https://developers.pismo.io/events/docs/depositary-credit-rights-registration-failure-1)\
        [Credit rights receivable registration succeeded](https://developers.pismo.io/events/docs/depositary-credit-rights-registration-success-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update receivable](https://developers.pismo.io/pismo-docs/reference/update)
      </td>

      <td style={{ textAlign: "left" }}>
        [Credit rights receivable change failed](https://developers.pismo.io/events/docs/depositary-credit-rights-change-failure-1)\
        [Credit rights receivable change succeeded](https://developers.pismo.io/events/docs/depositary-credit-rights-change-success-1)\
        [Credit rights receivable status change failed](https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-failure-1)\
        [Credit rights receivable status change succeeded](https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-success-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Delete receivable](https://developers.pismo.io/pismo-docs/reference/delete-receivable)
      </td>

      <td style={{ textAlign: "left" }}>
        [Credit rights receivable status change failed](https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-failure-1)\
        [Credit rights receivable status change succeeded](https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-success-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Get invoice](https://developers.pismo.io/pismo-docs/reference/findbyaccesskey)
      </td>

      <td style={{ textAlign: "left" }}>
        [Validate invoice request failed](https://developers.pismo.io/events/docs/depositary-invoice-validation-request-failure-1)\
        [Validate invoice request succeeded](https://developers.pismo.io/events/docs/depositary-invoice-validation-request-success-1)\
        [Invoice validation failed](https://developers.pismo.io/events/docs/depositary-invoice-validation-failure-1)\
        [Invoice validation succeeded](https://developers.pismo.io/events/docs/depositary-invoice-validation-success-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Validate receivable](https://developers.pismo.io/pismo-docs/reference/validateunicity)
      </td>

      <td style={{ textAlign: "left" }}>
        [Unicity credit rights receivable validation failed](https://developers.pismo.io/events/docs/depositary-credit-rights-unicity-validation-failure-1)\
        [Unicity credit rights receivable validation succeeded](https://developers.pismo.io/events/docs/depositary-credit-rights-unicity-validation-success-1)
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/credit-rights` | `create-receivable` | Register receivable | `api-specs/Banking_-_Credit_receivables.yaml` | no | KU-API-banking-credit-receivables--receivable |
| `PATCH /v1/credit-rights/{internalNumber}` | `update` | Update receivable | `api-specs/Banking_-_Credit_receivables.yaml` | no | KU-API-banking-credit-receivables--receivable |
| `DELETE /v1/credit-rights/{internalNumber}` | `delete-receivable` | Delete receivable | `api-specs/Banking_-_Credit_receivables.yaml` | no | KU-API-banking-credit-receivables--receivable |
| `GET /v1/invoices/{access_key}` | `findByAccessKey` | Get invoice | `api-specs/Banking_-_Credit_receivables.yaml` | no | KU-API-banking-credit-receivables--invoices |
| `POST /v1/credit-rights/unicity` | `validateUnicity` | Validate receivable | `api-specs/Banking_-_Credit_receivables.yaml` | no | KU-API-banking-credit-receivables--receivable |

### Operation essentials

- **`POST /v1/credit-rights`** (`create-receivable`): security `bearerAuth`; required parameters none declared; required body fields `credit_rights_receivable_type`, `debtor_name`, `debtor_document_number`, `face_value`, `holding_number`, `ibge_code`, `internal_number`, `invoice_number`, `invoice_serie`, `invoice_total_value`, `issuing_date`, `lender_name`, `lender_document_number`, `maturity_date`, `payment_method`, `payment_status`, `recorder_account`; response statuses 202, 400, 401, 500; error codes in examples none; events `depositary-credit-rights-registration-failure-1`, `depositary-credit-rights-registration-success-1`.
- **`PATCH /v1/credit-rights/{internalNumber}`** (`update`): security `bearerAuth`; required parameters `internalNumber` (path); required body fields none declared; response statuses 202, 400, 401, 500; error codes in examples none; events `depositary-credit-rights-change-failure-1`, `depositary-credit-rights-change-success-1`, `depositary-credit-rights-status-change-failure-1`, `depositary-credit-rights-status-change-success-1`.
- **`DELETE /v1/credit-rights/{internalNumber}`** (`delete-receivable`): security `bearerAuth`; required parameters `internalNumber` (path); required body fields none declared; response statuses 202, 400, 401, 500; error codes in examples none; events `depositary-credit-rights-status-change-failure-1`, `depositary-credit-rights-status-change-success-1`.
- **`GET /v1/invoices/{access_key}`** (`findByAccessKey`): security `bearerAuth`; required parameters `access_key` (path); required body fields none declared; response statuses 202, 400, 401, 500; error codes in examples none; events `depositary-invoice-validation-failure-1`, `depositary-invoice-validation-request-failure-1`, `depositary-invoice-validation-request-success-1`, `depositary-invoice-validation-success-1`.
- **`POST /v1/credit-rights/unicity`** (`validateUnicity`): security `bearerAuth`; required parameters none declared; required body fields `params`; response statuses 202, 400, 401, 500; error codes in examples none; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `update` | `depositary-credit-rights-change-failure-1` |
| `update` | `depositary-credit-rights-change-success-1` |
| `create-receivable` | `depositary-credit-rights-registration-failure-1` |
| `create-receivable` | `depositary-credit-rights-registration-success-1` |
| `delete-receivable` | `depositary-credit-rights-status-change-failure-1` |
| `update` | `depositary-credit-rights-status-change-failure-1` |
| `delete-receivable` | `depositary-credit-rights-status-change-success-1` |
| `update` | `depositary-credit-rights-status-change-success-1` |
| `findByAccessKey` | `depositary-invoice-validation-failure-1` |
| `findByAccessKey` | `depositary-invoice-validation-request-failure-1` |
| `findByAccessKey` | `depositary-invoice-validation-request-success-1` |
| `findByAccessKey` | `depositary-invoice-validation-success-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `depositary-credit-rights-change-failure-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-change-failure-1 | 1 | KU-EVT-catalogue-depositary |
| `depositary-credit-rights-change-success-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-change-success-1 | 1 | KU-EVT-catalogue-depositary |
| `depositary-credit-rights-registration-failure-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-registration-failure-1 | 1 | KU-EVT-catalogue-depositary |
| `depositary-credit-rights-registration-success-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-registration-success-1 | 1 | KU-EVT-catalogue-depositary |
| `depositary-credit-rights-status-change-failure-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-failure-1 | 2 | KU-EVT-catalogue-depositary |
| `depositary-credit-rights-status-change-success-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-success-1 | 2 | KU-EVT-catalogue-depositary |
| `depositary-invoice-validation-failure-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-invoice-validation-failure-1 | 1 | KU-EVT-catalogue-depositary |
| `depositary-invoice-validation-request-failure-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-invoice-validation-request-failure-1 | 1 | KU-EVT-catalogue-depositary |
| `depositary-invoice-validation-request-success-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-invoice-validation-request-success-1 | 1 | KU-EVT-catalogue-depositary |
| `depositary-invoice-validation-success-1` | depositary | 1 | https://developers.pismo.io/events/docs/depositary-invoice-validation-success-1 | 1 | KU-EVT-catalogue-depositary |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/depositary-data-events.md`: updatedAt 2026-03-18T15:15:07.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 12 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/depositary-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/depositary-data-events | `9fc3a9a2940dc0ba…` | 2026-03-18T15:15:07.000Z |

## Related knowledge units

- `KU-API-banking-credit-receivables--invoices` — API reference: Banking - Credit receivables — Invoices
- `KU-API-banking-credit-receivables--receivable` — API reference: Banking - Credit receivables — Receivable
- `KU-EVT-catalogue-depositary` — Event catalogue: depositary
