---
ku_id: KU-EVT-statement-data-events
title: Revolving credit - Statements
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/statement-data-events.md
  sha256: b3be110f455887163891fec4d38219c480729e2b4fa5e96c0b28db88fac4bc82
  url: https://developers.pismo.io/pismo-docs/docs/statement-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:15:03.000Z'
operations:
- CancelInstallmentsAdvanceV2
- InstallmentAdvancedV2
- InstallmentPaymentsv4
related_kus:
- KU-API-revolving-credit-statements--advancements
- KU-API-revolving-credit-statements--refinancing
- KU-EVT-catalogue-balance
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Revolving credit - Statements

**KU ID:** `KU-EVT-statement-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/statement-data-events.md`:

> This table lists the endpoints or other sources for statements and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/statement-data-events.md`: Revolving credit - Statements

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/statement-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/statement-data-events · updatedAt: 2026-03-18T15:15:03.000Z

<!-- source:begin path=docs/data-and-reporting/statement-data-events.md part=0-end -->

# Revolving credit - Statements

This table lists the endpoints or other sources for statements and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Endpoint/Trigger
      </th>

      <th style={{ textAlign: "left" }}>
        Event
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        [Cancel installments advance](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentsadvancev2)
      </td>

      <td style={{ textAlign: "left" }}>
        [Installment advanced](https://developers.pismo.io/events/docs/balance-installment-advancement-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create installment advance](https://developers.pismo.io/pismo-docs/reference/installmentadvancedv2)
      </td>

      <td style={{ textAlign: "left" }}>
        [Installment advanced](https://developers.pismo.io/events/docs/balance-installment-advancement-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4)
      </td>

      <td style={{ textAlign: "left" }}>
        [Installment payment processed](https://developers.pismo.io/events/docs/balance-installment-payment-processed-1)\
        Issued when the credit transaction for a statement refinancing/installment is created.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Statement cycle closing
      </td>

      <td style={{ textAlign: "left" }}>
        [Statement cycle closed](https://developers.pismo.io/events/docs/statements-cycle-closing-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Statement cycle opening
      </td>

      <td style={{ textAlign: "left" }}>
        [Statement cycle opened](https://developers.pismo.io/events/docs/statements-cycle-opening-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Statement cycle due date
      </td>

      <td style={{ textAlign: "left" }}>
        [Statement cycle real due date reached](https://developers.pismo.io/events/docs/statements-cycle-due-date-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Accrual generated
      </td>

      <td style={{ textAlign: "left" }}>
        [Accrual created](https://developers.pismo.io/events/docs/balance-accrual-data-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Account accrual status change
      </td>

      <td style={{ textAlign: "left" }}>
        [Accrual status changed](https://developers.pismo.io/events/docs/balance-accrual-status-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Credit transaction
      </td>

      <td style={{ textAlign: "left" }}>
        [Credit transaction used for discharge](https://developers.pismo.io/events/docs/balance-discharge-1)
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `DELETE /statements/v2/accounts/{accountId}/installment-advance/{id}` | `CancelInstallmentsAdvanceV2` | Cancel installments advancement (no cancellation event) (deprecated) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |
| `POST /statements/v2/accounts/{accountId}/installment-advance` | `InstallmentAdvancedV2` | Create installment advancement (no cancellation event) (deprecated) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |
| `POST /statements/v4/accounts/{accountId}/installment-payments` | `InstallmentPaymentsv4` | Create payment agreement | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |

### Operation essentials

- **`DELETE /statements/v2/accounts/{accountId}/installment-advance/{id}`** (`CancelInstallmentsAdvanceV2`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path), `id` (path); required body fields none declared; response statuses 200, 400, 404, 423, 500; error codes in examples `GN0001`; events `balance-installment-advancement-1`.
- **`POST /statements/v2/accounts/{accountId}/installment-advance`** (`InstallmentAdvancedV2`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields none declared; response statuses 200, 400, 423, 500; error codes in examples `GN0001`; events `balance-installment-advancement-1`.
- **`POST /statements/v4/accounts/{accountId}/installment-payments`** (`InstallmentPaymentsv4`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `statement_agreement`, `installments`; response statuses 201, 400, 404, 423, 500; error codes in examples `GN0001`; events `balance-installment-payment-processed-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `CancelInstallmentsAdvanceV2` | `balance-installment-advancement-1` |
| `InstallmentAdvancedV2` | `balance-installment-advancement-1` |
| `InstallmentPaymentsv4` | `balance-installment-payment-processed-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `balance-installment-advancement-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-installment-advancement-1 | 5 | KU-EVT-catalogue-balance |
| `balance-installment-payment-processed-1` | balance | 1 | https://developers.pismo.io/events/docs/balance-installment-payment-processed-1 | 2 | KU-EVT-catalogue-balance |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/statement-data-events.md`: updatedAt 2026-03-18T15:15:03.000Z.
- Links to `CancelInstallmentsAdvanceV2`, which is marked `deprecated: true` in `api-specs/Revolving_credit_-_Statements.yaml`.
- Links to `InstallmentAdvancedV2`, which is marked `deprecated: true` in `api-specs/Revolving_credit_-_Statements.yaml`.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 8 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/statement-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/statement-data-events | `b3be110f45588716…` | 2026-03-18T15:15:03.000Z |

## Related knowledge units

- `KU-API-revolving-credit-statements--advancements` — API reference: Revolving credit - Statements — Advancements
- `KU-API-revolving-credit-statements--refinancing` — API reference: Revolving credit - Statements — Refinancing
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
