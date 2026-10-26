---
ku_id: KU-LEND-book-a-loan
title: Book loans
category: lending
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/lending/book-a-loan.md
  sha256: e336ae00d08a24ee2597c82b93a0e0351f5129a42ab76681f9258150f6997ec4
  url: https://developers.pismo.io/pismo-docs/docs/book-a-loan
  role: primary_guide
  updated_at: '2026-09-29T17:33:53.000Z'
operations:
- bookLoanV2
- getLoanProductV2
- getLoanV2
- post-v1-simulation
related_kus:
- KU-API-core-platform-payment-methods-admin--simulation
- KU-API-lending--loan-products
- KU-API-lending--loans
- KU-EVT-catalogue-lending
- KU-EVT-catalogue-other-domains
- KU-LEND-loan-products
- KU-LEND-loan-statuses-overview
- KU-LEND-simulate-loans
grouping_rationale: single source page
---

# Book loans

**KU ID:** `KU-LEND-book-a-loan` · **Category:** Lending · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/lending/book-a-loan.md`:

> You can book a loan by finalizing the borrower’s approval and officially creating the loan, which makes the loan active and ready for them to use.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/lending/book-a-loan.md`: Book loans; Prerequisites; Book a loan; Troubleshooting; What does the `ELND0004 Authorization failed` error mean?; Why did booking fail with a validation error (`ELND0002`, `ELND0003`, or `ELND0005`)?; What can I do if the simulation or installment plan has expired?; Why is my loan `BOOKED` but not `ACTIVE`?; Booking returned `202 Accepted` but the loan never becomes active

## Prerequisites and dependencies

- Prerequisites are described in `docs/lending/book-a-loan.md` section "Prerequisites".
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/lending/book-a-loan.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/book-a-loan · updatedAt: 2026-09-29T17:33:53.000Z

<!-- source:begin path=docs/lending/book-a-loan.md part=0-end -->

# Book loans

You can book a loan by finalizing the borrower’s approval and officially creating the loan, which makes the loan active and ready for them to use.

# Prerequisites

Before booking a loan, you must show a potential borrower the loan terms though a loan simulation. Once they agree to the terms and conditions, you reference this simulation in the payload when booking the loan. For more information, refer to [Simulate loans](https://developers.pismo.io/pismo-docs/docs/simulate-loans).

# Book a loan

Use the [Book loan](https://developers.pismo.io/pismo-docs/reference/bookloanv2) endpoint to book a loan with a payload that includes the required `account_id`, `installment_plan_id`, `loan_product_id`, and `number_of_installments` values:

<Accordion title="Request payload">
  ```json
  {
    "account_id": 514751581,
    "loan_product_id": "0ea4fe62-5512-4494-baf5-13a3044b7f7b",
    "installment_plan_id": "PL-20250708200752",
    "number_of_installments": 5,
    "metadata": {
      "risk_factor": "low"
    }
  }
  ```
</Accordion>

A successful request returns a `loan_id` and the loan status transitions to `ACTIVE` or `BOOKED` depending on configuration. You can later retrieve the `loan_id` with listing or individual retrieval endpoints. The Pismo platform generates a [Loan booked](https://developers.pismo.io/events/docs/lending-loan-booked-1) event:

<Accordion title="Loan booked event">
  ```json
  {
      "org_id": "TN-89e56522-726a-453e-ba6d-796b03245128",
      "external_id": "cca6041c-b57d-44cf-a203-eeea22723878",
      "loan_id": "ded913af-abc9-4769-b179-068ed6181ec5",
      "status": "BOOKED",
      "loan_product_id": "0ea4fe62-5512-4494-baf5-13a3044b7f7b",
      "account_id": 514751581,
      "amount": 1000.0,
      "start_date": "2026-05-24",
      "created_at": "2026-05-24T21:34:47"
  }
  ```
</Accordion>

<br />

# Troubleshooting

Use this section to troubleshoot errors that can occur when booking a loan and understand how to resolve them.

Because the [Book loan](https://developers.pismo.io/pismo-docs/reference/bookloanv2) endpoint is asynchronous, it returns `202 Accepted` with a `loan_id` while booking. Meanwhile, interest calculation and authorization continue in the background.

Common problems can fall into two groups: validation and authorization errors returned synchronously as a `400` or `500` *before* the `202`, and problems that surface only *after* the `202`, which you diagnose by inspecting the loan and its events.

## What does the `ELND0004 Authorization failed` error mean?

Booking authorizes the loan against the account, and this `400` means that authorization was denied. The response includes `response_code` and `denial_code` values that identify the reason:

```json
{
  "code": "ELND0004",
  "message": "Authorization failed",
  "response_code": "62",
  "denial_code": "IAD"
}
```

Common causes are an account status that doesn't permit the posting, insufficient limits, or an anti-fraud rejection.

To resolve:

1. Read the `denial_code` and `response_code`to identify the reason.
2. Retrieve the loan with [Get loan](https://developers.pismo.io/pismo-docs/reference/getloanv2) to confirm its state.
3. Check the account's status and limits, and confirm the `account_id` in the payload matches the account you intend to debit.
4. Correct the reason for the denial and retry the booking.

## Why did booking fail with a validation error (`ELND0002`, `ELND0003`, or `ELND0005`)?

These `400` errors mean the request failed validation before booking started:

* `ELND0002`—a required header or body field wasn't passed.
* `ELND0003`—a body field was passed but isn't valid.
* `ELND0005`—a referenced entity (related data) couldn't be found.

A frequent cause of `ELND0005` is a `loan_product_id` that belongs to a different organization (tenant), or a `number_of_installments` value that the referenced installment plan doesn't offer.

To resolve:

1. Confirm all required fields are present: `account_id`, `loan_product_id`, `installment_plan_id`, and `number_of_installments`.
2. Verify the loan product resolves for your tenant using [Get loan product](https://developers.pismo.io/pismo-docs/reference/getloanproductv2). If it returns a "Not found" error, the `loan_product_id` or the tenant header is mismatched.
3. Confirm `number_of_installments` matches one of the installment counts your simulation offered for that plan.

## What can I do if the simulation or installment plan has expired?

Loan booking references a loan simulation, and loan simulations are valid for one day only. If the simulation has expired, you can't book against it. The system is designed to always reflect current rates, fees, and balances.

If the customer still wants the loan, create a new simulation with [Create simulation](https://developers.pismo.io/pismo-docs/reference/post-v1-simulation) and use the new `installment_plan_id` for booking. If the simulation applies an unexpected plan ID, verify the account, program, and organization simulation attachments. Refer to [Simulate loans](https://developers.pismo.io/pismo-docs/docs/simulate-loans) for the full configuration-resolution procedure.

## Why is my loan `BOOKED` but not `ACTIVE`?

A successful booking transitions the loan to `BOOKED` or `ACTIVE` depending on the loan product's configuration, so a loan resting at `BOOKED` may be correct rather than a failure. The `loan_activation_method` on the loan product determines when the loan becomes `ACTIVE`; for example, on booking, on disbursement, or on repayment.

To resolve:

1. Review what each status represents in [Loan statuses overview](https://developers.pismo.io/pismo-docs/docs/loan-statuses-overview).
2. Check the loan product's activation method with [Get loan product](https://developers.pismo.io/pismo-docs/reference/getloanproductv2); refer to [Create loan products](https://developers.pismo.io/pismo-docs/docs/create-loan-products) for how the activation method is configured.
3. If the method expects a later trigger (such as disbursement), the loan correctly remains `BOOKED` until that event occurs.

## Booking returned `202 Accepted` but the loan never becomes active

Because booking is asynchronous, the `202` is returned before booking and authorization finish. If the loan never reaches `BOOKED` or `ACTIVE`:

1. Retrieve the loan with [Get loan](https://developers.pismo.io/pismo-docs/reference/getloanv2) and check its `status`. A "Not found" response means the loan was never persisted so you must recheck the payload and retry.
2. Confirm the platform generated both the [Loan booked](https://developers.pismo.io/events/docs/lending-loan-booked-1) and [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) events. When you are missing an authorization event you can check if the authorization leg failed.
3. Track subsequent status changes through the [Lending loan update](https://developers.pismo.io/events/docs/lending-lending-loan-update-1) event.
4. Correlate all requests and events by noting the `x-cid`. If you receive a `500 ELND0001` (unexpected error), check the `x-cid` and escalate to Pismo support.

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v2/loans` | `bookLoanV2` | Book loan | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `GET /v2/loans/{loanId}` | `getLoanV2` | Get loan | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `GET /v2/loan-products/{productId}` | `getLoanProductV2` | Get loan product | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `POST /v1/simulations` | `post-v1-simulation` | Create simulation | `api-specs/Core_platform_-_Payment_methods_admin.yaml` | no | KU-API-core-platform-payment-methods-admin--simulation |

### Operation essentials

- **`POST /v2/loans`** (`bookLoanV2`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `installment_plan_id`, `loan_product_id`, `number_of_installments`; response statuses 202, 400, 500; error codes in examples `ELND0004`, `ELND0001`; events `lending-loan-booked-1`, `platform-authorization-platform-authorization-1`.
- **`GET /v2/loans/{loanId}`** (`getLoanV2`): security `BearerAuth`; required parameters `loanId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `ELND0002`, `ELND0005`, `ELND0003`, `ELND1807`, `ELND0005`, `ELND0001`; events none listed.
- **`GET /v2/loan-products/{productId}`** (`getLoanProductV2`): security `BearerAuth`; required parameters `productId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `ELND0002`, `ELND0005`, `ELND0005`, `ELND0001`; events none listed.
- **`POST /v1/simulations`** (`post-v1-simulation`): security not declared; required parameters none declared; required body fields `amount`, `authorization_mode`; response statuses 200, 400, 422, 500; error codes in examples `DO0002`, `SI001`, `SI003`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `bookLoanV2` | `lending-loan-booked-1` |
| `bookLoanV2` | `platform-authorization-platform-authorization-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `lending-lending-loan-update-1` | lending | 1 | https://developers.pismo.io/events/docs/lending-lending-loan-update-1 | 2 | KU-EVT-catalogue-lending |
| `lending-loan-booked-1` | lending | 1 | https://developers.pismo.io/events/docs/lending-loan-booked-1 | 1 | KU-EVT-catalogue-lending |
| `platform-authorization-platform-authorization-1` | platform | 1 | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 | 32 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/lending/book-a-loan.md`: updatedAt 2026-09-29T17:33:53.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 3 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/lending/book-a-loan.md` | whole document | https://developers.pismo.io/pismo-docs/docs/book-a-loan | `e336ae00d08a24ee…` | 2026-09-29T17:33:53.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods-admin--simulation` — API reference: Core platform - Payment methods admin — Simulation
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-EVT-catalogue-lending` — Event catalogue: lending
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-LEND-loan-products` — Loan products: overview and creation
- `KU-LEND-loan-statuses-overview` — Loan statuses overview
- `KU-LEND-simulate-loans` — Simulate loans
