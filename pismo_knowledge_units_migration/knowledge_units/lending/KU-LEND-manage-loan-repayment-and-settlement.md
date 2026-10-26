---
ku_id: KU-LEND-manage-loan-repayment-and-settlement
title: Manage loan repayment and settlement
category: lending
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/lending/manage-loan-repayment-and-settlement.md
  sha256: 5156e428f91d34c31c4e80c6df3a90ca3dc16eaf5467a92253b14002b77c9081
  url: https://developers.pismo.io/pismo-docs/docs/manage-loan-repayment-and-settlement
  role: primary_guide
  updated_at: '2026-09-22T17:42:19.000Z'
operations:
- cancelLoanV2
- createLoanAdjustmentV2
- getLoanV2
- registerEarlyFinalSettlementV2
- restructureLoan
- simulateEarlyFinalSettlementV2
related_kus:
- KU-API-lending--early-final-settlement
- KU-API-lending--loans
- KU-CC-lending
- KU-EVT-catalogue-lending
- KU-LEND-loan-products
- KU-LEND-loan-statuses-overview
- KU-LEND-simulate-loans
grouping_rationale: single source page
---

# Manage loan repayment and settlement

**KU ID:** `KU-LEND-manage-loan-repayment-and-settlement` · **Category:** Lending · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/lending/manage-loan-repayment-and-settlement.md`:

> Loan repayment and settlement are the stages where borrowers pay down what they owe until the loan is fully repaid and Pismo automatically settles it.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/lending/manage-loan-repayment-and-settlement.md`: Manage loan repayment and settlement; Manage loan repayment; View a loan repayment schedule; Create loan adjustment; Restructure a loan; Cancel a loan; Manage settlement

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/lending/manage-loan-repayment-and-settlement.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/manage-loan-repayment-and-settlement · updatedAt: 2026-09-22T17:42:19.000Z

<!-- source:begin path=docs/lending/manage-loan-repayment-and-settlement.md part=0-end -->

# Manage loan repayment and settlement

Loan repayment and settlement are the stages where borrowers pay down what they owe until the loan is fully repaid and Pismo automatically settles it.

# Manage loan repayment

When you book a loan, the Pismo platform generates a repayment schedule based on the configurations of the associated loan product.

## View a loan repayment schedule

View payment progress and track the status of each individual repayment. You can use Control Center or the API.

| Method         | Description                                                                            | For more information                                                 |
| :------------- | :------------------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| Control Center | You can view repayment schedule as part of account management.                         | [Manage loans in Control Center](https://developers.pismo.io/pismo-docs/docs/manage-loans-in-control-center) |
| API            | Use the **Get loan** endpoint. Look for the **repayment schedule** object for details. | [Get loan ](https://developers.pismo.io/pismo-docs/reference/getloanv2)                                           |

## Create loan adjustment

You can adjust a loan's repayment details for several reasons, such as providing discounts on repayments or including previously disputed amounts. When you make an adjustment, your changes update the repayment schedule and affect the overall loan balance.

You can use Control Center or the API.

| Method         | Description                                          | For more information                                                 |
| :------------- | :--------------------------------------------------- | :------------------------------------------------------------------- |
| Control Center | You can adjust a loan as part of account management. | [Manage loans in Control Center](https://developers.pismo.io/pismo-docs/docs/manage-loans-in-control-center) |
| API            | Use the **Create loan adjustment** endpoint.         | [Create loan adjustment](https://developers.pismo.io/pismo-docs/reference/createloanadjustmentv2)                 |

Use the [Create loan adjustment](https://developers.pismo.io/pismo-docs/reference/createloanadjustmentv2) endpoint to adjust the loan. In the following request payload example, the `adjustment_amount` applies to the loan principal because `loan_balance_impact` is set to `PRINCIPAL`. Other options for adjusting the loan include `INTEREST`, `TAX`, `PENALTY`, or `FEE`.

<Accordion title="Request payload">
  ```json Create loan adjustment sample
  {
    "loan_balance_impact": "PRINCIPAL",
    "adjustment_amount": 1000,
    "processing_code": "12345",
    "repayment_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834"
  }
  ```
</Accordion>

This endpoint returns an `idempotency_key` and `authorization_id` in the response body.

<Accordion title="Response payload">
  ```json
  {
    "idempotency_key": "4df987e3-8179-11ed-8209-06c7b022d1ee",
    "authorization_id": 123456789
  }
  ```
</Accordion>

## Restructure a loan

Loan restructuring (also called renegotiation) replaces an existing active loan with a new loan on different terms, such as a different number of installments or a different loan product. Unlike a loan adjustment, which modifies the repayment schedule of the existing loan in place, restructuring does not change the original loan. Instead, the platform books a brand-new loan for the outstanding balance and moves the original loan to the `RENEGOTIATED` status. Once you have restructured a loan, not only is a particular repayment changed, but the full loan is changed.

Use a **loan adjustment** to correct or amend the current loan's existing schedule (see [Create loan adjustment](#create-loan-adjustment)). Use **restructuring** when the repayment terms need to change going forward and the loan should be replaced by a new one.

Restructuring works as follows:

1. Restructuring applies to an `ACTIVE` loan. The loan's outstanding balance becomes the amount carried into the new loan.
2. The new number of installments must be one of the values allowed by the installment plan configuration. To preview the terms of the new loan first, refer to [Simulate loans](https://developers.pismo.io/pismo-docs/docs/simulate-loans).
3. Call the [Restructure a loan](https://developers.pismo.io/pismo-docs/reference/restructureloan) endpoint with the target loan product, installment plan, and number of installments. A restructure can reuse the same loan product or move to a different one.
4. Processing is asynchronous. The endpoint returns a `tracking_id` and processing continues in the background. The new loan is not returned in the response.
5. When processing completes, the original loan transitions to `RENEGOTIATED` and a new loan is booked from the outstanding balance using the selected terms. The original loan cannot have any further actions taken once the transition happens.
6. To retrieve the new loan, use [Get loan](https://developers.pismo.io/pismo-docs/reference/getloanv2) on the original loan, confirm that its status is `RENEGOTIATED`, and read the linked `restructure_loan_id`. Then retrieve the new loan using that ID.

The following example shows a request payload for the [Restructure a loan](https://developers.pismo.io/pismo-docs/reference/restructureloan) endpoint with 24 installments.

<Accordion title="Request payload">
  ```json Restructure a loan sample
  {
    "loan_product_id": "b1f2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    "installment_plan_id": "8ac0e5f1-2b3c-4d5e-6f7a-8b9c0d1e2f3a",
    "number_of_installments": 24
  }
  ```
</Accordion>

This endpoint returns a `tracking_id` that you can use to correlate the asynchronous processing.

<Accordion title="Response payload">
  ```json
  {
    "tracking_id": "4df987e3-8179-11ed-8209-06c7b022d1ee"
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  The original and new loans are linked for traceability. On the original (`RENEGOTIATED`) loan, the `restructure_loan_id` field holds the new loan's ID. On the new loan, the `original_loan_id` field points back to the original loan.
</Callout>

## Cancel a loan

If you cancel a loan before disbursement, the borrower might not be charged. If you cancel a loan after disbursement, the borrower is responsible for repaying the disbursed amount. When a loan is canceled, all expected transfers are canceled and the loan moves to the `CANCELED` status. For more information, refer to [Loan statuses overview](https://developers.pismo.io/pismo-docs/docs/loan-statuses-overview).

To cancel a loan, use the [Cancel loan](https://developers.pismo.io/pismo-docs/reference/cancelloanv2) endpoint. You must send the `Idempotency-Key` header with the request payload. The `tracking_id` is required; `processing_code` and `metadata` are optional.

<Accordion title="Request payload">
  ```json Cancel loan sample
  {
    "tracking_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
    "processing_code": {
      "booking": "7DJ8L",
      "repayment": "I1I7J",
      "penalty_waiver": "80Y39"
    },
    "metadata": {
      "cancellation_reason": "Write-off"
    }
  }
  ```
</Accordion>

Cancellation is processed asynchronously. The endpoint returns the `cancelled_loan_id` along with a `reversal_authorization_id` and `reversal_tracking_id` that you can use to correlate the reversal.

<Accordion title="Response payload">
  ```json
  {
    "cancelled_loan_id": "73e45fd5-759f-4e04-a88a-7172fa948afa",
    "reversal_authorization_id": 123456789,
    "reversal_tracking_id": "4df987e3-8179-11ed-8209-06c7b022d1ee"
  }
  ```
</Accordion>

The Pismo platform generates a [Loan updated](https://developers.pismo.io/events/docs/lending-lending-loan-update-1) event that reflects the transition to the `CANCELED` status:

<Accordion title="Loan updated event">
  ```json
  {
    "cid": "7da3db3b-400d-4851-a362-2022dab27284",
    "loan_id": "73e45fd5-759f-4e04-a88a-7172fa948afa",
    "org_id": "TN-89e56522-726a-453e-ba6d-796b03245128",
    "account_id": 12176,
    "product_id": "89e56522-726a-453e-ba6d-796b03245128",
    "program_id": 9000,
    "currency": "USD",
    "amount": 1000.00,
    "previous_status": "ACTIVE",
    "current_status": "CANCELED",
    "created_at": "2026-10-24T21:34:47.000Z",
    "updated_at": "2026-10-24T21:34:47.000Z",
    "authorization_cancellation_id": 123456789,
    "authorization_cancellation_tracking_id": "4df987e3-8179-11ed-8209-06c7b022d1ee"
  }
  ```
</Accordion>

# Manage settlement

The Pismo platform generates settlement rules based on the configurations of the associated loan product when a loan is booked.

If the borrower wants to repay the full amount of a loan plus any charges before the final scheduled payment date, you'll need to initiate early final settlement (EFS).

1. You must first simulate the details of the final settlement payment. The simulation calculates any repayment penalties that must be repaid in the final payment. To simulate an early settlement, use the [Simulate EFS](https://developers.pismo.io/pismo-docs/reference/simulateearlyfinalsettlementv2) endpoint.
2. After the borrower has reviewed the details of the simulation, use the [Register EFS](https://developers.pismo.io/pismo-docs/reference/registerearlyfinalsettlementv2) endpoint to confirm and apply the simulation details to the loan and accept the early settlement payment.

Depending on the loan product, borrowers might be restricted from initiating an early settlement for a set period. They might also incur a penalty fee when making the final payment. The loan product defines these rules and penalties. For more information, refer to [Create loan products](https://developers.pismo.io/pismo-docs/docs/create-loan-products).

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /v2/loans/{loanId}` | `getLoanV2` | Get loan | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v2/loans/{loanId}/adjustment` | `createLoanAdjustmentV2` | Create loan adjustment | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v2/loans/{originalLoanId}/restructure` | `restructureLoan` | Restructure a loan | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v2/loans/{loanId}/cancel` | `cancelLoanV2` | Cancel loan | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v2/loans/{loanId}/early-settlement/simulate` | `simulateEarlyFinalSettlementV2` | Simulate early final settlement | `api-specs/Lending.yaml` | no | KU-API-lending--early-final-settlement |
| `POST /v2/loans/{loanId}/early-settlement/{efsId}/register` | `registerEarlyFinalSettlementV2` | Register early final settlement | `api-specs/Lending.yaml` | no | KU-API-lending--early-final-settlement |

### Operation essentials

- **`GET /v2/loans/{loanId}`** (`getLoanV2`): security `BearerAuth`; required parameters `loanId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `ELND0002`, `ELND0005`, `ELND0003`, `ELND1807`, `ELND0005`, `ELND0001`; events none listed.
- **`POST /v2/loans/{loanId}/adjustment`** (`createLoanAdjustmentV2`): security `BearerAuth`; required parameters `loanId` (path), `Idempotency-Key` (header); required body fields `adjustment_amount`, `loan_balance_impact`, `processing_code`, `repayment_id`; response statuses 202, 400; error codes in examples none; events none listed.
- **`POST /v2/loans/{originalLoanId}/restructure`** (`restructureLoan`): security `BearerAuth`; required parameters `originalLoanId` (path), `Idempotency-Key` (header); required body fields `installment_plan_id`, `loan_product_id`, `number_of_installments`; response statuses 200, 400, 500; error codes in examples none; events none listed.
- **`POST /v2/loans/{loanId}/cancel`** (`cancelLoanV2`): security `BearerAuth`; required parameters `loanId` (path), `Idempotency-Key` (header); required body fields `tracking_id`; response statuses 202, 400, 500; error codes in examples `ELND0010`, `ELND0004`, `ELND0001`; events `lending-lending-loan-update-1`.
- **`POST /v2/loans/{loanId}/early-settlement/simulate`** (`simulateEarlyFinalSettlementV2`): security `BearerAuth`; required parameters `loanId` (path); required body fields none declared; response statuses 201, 400, 404, 500; error codes in examples `ELND0400`, `ELND0401`, `ELND0402`, `ELND0405`, `ELND0406`, `ELND2000`, `ELND3000`, `ELND0001`; events none listed.
- **`POST /v2/loans/{loanId}/early-settlement/{efsId}/register`** (`registerEarlyFinalSettlementV2`): security `BearerAuth`; required parameters `loanId` (path), `efsId` (path); required body fields none declared; response statuses 202, 400, 404, 500; error codes in examples `ELND0400`, `ELND0403`, `ELND0404`, `ELND2000`, `ELND0005`, `ELND0001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `cancelLoanV2` | `lending-lending-loan-update-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `lending-lending-loan-update-1` | lending | 1 | https://developers.pismo.io/events/docs/lending-lending-loan-update-1 | 2 | KU-EVT-catalogue-lending |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/lending/manage-loan-repayment-and-settlement.md`: updatedAt 2026-09-22T17:42:19.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/lending/manage-loan-repayment-and-settlement.md` | whole document | https://developers.pismo.io/pismo-docs/docs/manage-loan-repayment-and-settlement | `5156e428f91d34c3…` | 2026-09-22T17:42:19.000Z |

## Related knowledge units

- `KU-API-lending--early-final-settlement` — API reference: Lending — Early final settlement
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-CC-lending` — Control Center lending: loan products and loan management
- `KU-EVT-catalogue-lending` — Event catalogue: lending
- `KU-LEND-loan-products` — Loan products: overview and creation
- `KU-LEND-loan-statuses-overview` — Loan statuses overview
- `KU-LEND-simulate-loans` — Simulate loans
