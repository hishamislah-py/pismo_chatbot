---
ku_id: KU-EVT-lending-data-events
title: Lending events
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/lending-data-events.md
  sha256: cb5e706edb92372549310ca3a117e9f7ee3affa447a3ab18676625444a2e692f
  url: https://developers.pismo.io/pismo-docs/docs/lending-data-events
  role: primary_guide
  updated_at: '2026-08-10T14:59:58.000Z'
operations:
- bookLoanV2
- cancelLoanV2
- createLoanAdjustmentV2
- createLoanProductV2
- createPrepayment
- disburseLoanV2
- updateLoanProductV2
related_kus:
- KU-API-lending--disbursements
- KU-API-lending--loan-products
- KU-API-lending--loans
- KU-API-lending--prepayment
- KU-EVT-catalogue-lending
- KU-EVT-catalogue-other-domains
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Lending events

**KU ID:** `KU-EVT-lending-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/lending-data-events.md`:

> This table lists the lending endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/lending-data-events.md`: Lending events

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/lending-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/lending-data-events · updatedAt: 2026-08-10T14:59:58.000Z

<!-- source:begin path=docs/data-and-reporting/lending-data-events.md part=0-end -->

# Lending events

This table lists the lending endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint                                             | Event                            |
| :--------------------------------------------------- | :------------------------------- |
| [Create loan product](https://developers.pismo.io/pismo-docs/reference/createloanproductv2)       | Loan product created             |
| [Update loan products](https://developers.pismo.io/pismo-docs/reference/updateloanproductv2)      | Loan product updated             |
| [Book loan](https://developers.pismo.io/pismo-docs/reference/bookloanv2)                          | Loan booked                      |
| [Cancel loan](https://developers.pismo.io/pismo-docs/reference/cancelloanv2)                      | Loan cancellation error occurred |
| [Create loan adjustment](https://developers.pismo.io/pismo-docs/reference/createloanadjustmentv2) | Loan cancellation error occurred |
| [Disburse loan](https://developers.pismo.io/pismo-docs/reference/disburseloanv2)                  | Loan disbursement status changed |
| [Restructure a loan](https://developers.pismo.io/pismo-docs/reference/restrutureloan)             | Loan updated                     |
| [Create prepayment record](https://developers.pismo.io/pismo-docs/reference/createprepayment)     | Lending prepayment created       |

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v2/loan-products` | `createLoanProductV2` | Create loan product | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `PATCH /v2/loan-products/{productId}` | `updateLoanProductV2` | Update loan product | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `POST /v2/loans` | `bookLoanV2` | Book loan | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v2/loans/{loanId}/cancel` | `cancelLoanV2` | Cancel loan | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v2/loans/{loanId}/adjustment` | `createLoanAdjustmentV2` | Create loan adjustment | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v2/loans/{loanId}/disburse` | `disburseLoanV2` | Disburse loan | `api-specs/Lending.yaml` | no | KU-API-lending--disbursements |
| `POST /v2/prepayments` | `createPrepayment` | Create prepayment record | `api-specs/Lending.yaml` | no | KU-API-lending--prepayment |

### Operation essentials

- **`POST /v2/loan-products`** (`createLoanProductV2`): security `BearerAuth`; required parameters none declared; required body fields `collateral`, `currency`, `disbursement_method`, `processing_codes`, `product_name`, `product_type`; response statuses 201, 202, 400, 500; error codes in examples `ELND1501`, `ELND0350`, `ELND0351`, `ELND0352`, `ELND0353`, `ELND0354`, `ELND0355`, `ELND0356`, `ELND0357`, `ELND0358`, `ELND0359`, `ELND0360`, `ELND0361`, `ELND0362`, `ELND0363`, `ELND0380`, `ELND0011`, `ELND0012`, `ELND0379`, `ELND0001`; events `lending-loan-product-creation-3`.
- **`PATCH /v2/loan-products/{productId}`** (`updateLoanProductV2`): security `BearerAuth`; required parameters `productId` (path); required body fields none declared; response statuses 200, 202, 400, 404, 500; error codes in examples `ELND1501`, `ELND0002`, `ELND0352`, `ELND0354`, `ELND0360`, `ELND0366`, `ELND0369`, `ELND0376`, `ELND0379`, `ELND0380`, `ELND0005`, `ELND0001`; events `lending-loan-product-update-1`.
- **`POST /v2/loans`** (`bookLoanV2`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `installment_plan_id`, `loan_product_id`, `number_of_installments`; response statuses 202, 400, 500; error codes in examples `ELND0004`, `ELND0001`; events `lending-loan-booked-1`, `platform-authorization-platform-authorization-1`.
- **`POST /v2/loans/{loanId}/cancel`** (`cancelLoanV2`): security `BearerAuth`; required parameters `loanId` (path), `Idempotency-Key` (header); required body fields `tracking_id`; response statuses 202, 400, 500; error codes in examples `ELND0010`, `ELND0004`, `ELND0001`; events `lending-lending-loan-update-1`.
- **`POST /v2/loans/{loanId}/adjustment`** (`createLoanAdjustmentV2`): security `BearerAuth`; required parameters `loanId` (path), `Idempotency-Key` (header); required body fields `adjustment_amount`, `loan_balance_impact`, `processing_code`, `repayment_id`; response statuses 202, 400; error codes in examples none; events none listed.
- **`POST /v2/loans/{loanId}/disburse`** (`disburseLoanV2`): security `BearerAuth`; required parameters `loanId` (path), `Idempotency-Key` (header); required body fields `disbursement_account`; response statuses 202, 400, 500; error codes in examples `ELND0003`, `ELND0004`, `ELND0001`; events none listed.
- **`POST /v2/prepayments`** (`createPrepayment`): security `BearerAuth`; required parameters none declared; required body fields `repayment_ids`; response statuses 201, 400, 500; error codes in examples `ELND0002`, `ELND0005`, `ELND0003`, `ELND0001`; events `lending-prepayment-creation-1`.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `restrutureloan` | Restructure a loan | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `cancelLoanV2` | `lending-lending-loan-update-1` |
| `bookLoanV2` | `lending-loan-booked-1` |
| `createLoanProductV2` | `lending-loan-product-creation-3` |
| `updateLoanProductV2` | `lending-loan-product-update-1` |
| `createPrepayment` | `lending-prepayment-creation-1` |
| `bookLoanV2` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/lending-data-events.md`: updatedAt 2026-08-10T14:59:58.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Operation link `restrutureloan` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/lending-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/lending-data-events | `cb5e706edb923725…` | 2026-08-10T14:59:58.000Z |

## Related knowledge units

- `KU-API-lending--disbursements` — API reference: Lending — Disbursements
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-lending--prepayment` — API reference: Lending — Prepayment
- `KU-EVT-catalogue-lending` — Event catalogue: lending
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
