---
ku_id: KU-LEND-disburse-loan
title: Disburse loans
category: lending
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/lending/disburse-loan.md
  sha256: eabe700e5566b5b9987ef77c92ebc7c93d14ee4c4fb419777dba2c00181a4160
  url: https://developers.pismo.io/pismo-docs/docs/disburse-loan
  role: primary_guide
  updated_at: '2026-09-22T17:42:19.000Z'
operations:
- disburseLoanV2
- getLoanV2
- getLoansByAccountIdV2
related_kus:
- KU-API-lending--disbursements
- KU-API-lending--loans
- KU-CC-lending
- KU-EVT-catalogue-lending
- KU-LEND-loan-products
- KU-LEND-simulate-loans
grouping_rationale: single source page
---

# Disburse loans

**KU ID:** `KU-LEND-disburse-loan` · **Category:** Lending · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/lending/disburse-loan.md`:

> Loan disbursement is the step where you release the approved funds to the borrower’s account according to the agreed terms, turning a booked loan into money the borrower can actually use. You can disburse the loan in a single lump sum (single disbursement) or over several payments (multiple disbursement). The loan product defines disbursement rules. For more information, refer to [Create loan products](https://developers.pismo.io/pismo-docs/docs/create-loan-products).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/lending/disburse-loan.md`: Disburse loans; Disburse a loan; Single disbursement; Multiple disbursements; Validation rules; Example; Example request; View disbursement information; Events

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/lending/disburse-loan.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/disburse-loan · updatedAt: 2026-09-22T17:42:19.000Z

<!-- source:begin path=docs/lending/disburse-loan.md part=0-end -->

# Disburse loans

Loan disbursement is the step where you release the approved funds to the borrower’s account according to the agreed terms, turning a booked loan into money the borrower can actually use. You can disburse the loan in a single lump sum (single disbursement) or over several payments (multiple disbursement). The loan product defines disbursement rules. For more information, refer to [Create loan products](https://developers.pismo.io/pismo-docs/docs/create-loan-products).

# Disburse a loan

You can use Control Center or the API to disburse a loan.

| Method         | Description                                            | For more information                                                 |
| :------------- | :----------------------------------------------------- | :------------------------------------------------------------------- |
| Control Center | You can disburse a loan as part of account management. | [Manage loans in Control Center](https://developers.pismo.io/pismo-docs/docs/manage-loans-in-control-center) |
| API            | Use the **Disburse loans** endpoint.                   | [Disburse loan](https://developers.pismo.io/pismo-docs/reference/disburseloanv2)                                  |

Use the [Disburse loans](https://developers.pismo.io/pismo-docs/reference/disburseloanv2) endpoint with the following example payload, which must include the `loan_id` and `disbursement_account`  (either for `INTERNAL` or `EXTERNAL` `account_type`).

<Accordion title="Request payload">
  ```json
  {
   "disbursement_date": "2026-06-24",
   "disbursement_amount": 1000.00,
   "disbursement_account": {
     "account_type": "INTERNAL",
     "account_id": 103614168
   }
  }
  ```
</Accordion>

You can find the `disbursement_date` and `disbursement_amount` in the loan simulation. For more information, refer to [Simulate loans](https://developers.pismo.io/pismo-docs/docs/simulate-loans).

After you disburse the loan, the API response includes the `disbursement_id`. This ID confirms that the loan disbursement was successful.

<Accordion title="Response payload">
  ```json
  {
     "loan_id": "5d9d9339-3b5e-4c33-b129-8155e4d4946b",
     "authorization_id": 123456789,
     "authorization_tracking_id": "4df987e3-8179-11ed-8209-06c7b022d1ee",
     "disbursement_id": "c1eb9f28-e1c9-4705-b2b5-f986b3bc7455",
     "disbursement_amount": 1000.00
  }
  ```
</Accordion>

## Single disbursement

For single disbursement, call the [Disburse loans](https://developers.pismo.io/pismo-docs/reference/disburseloanv2) endpoint once. In the following example request, the `loanId` path parameter is "2717a296-124a-47cc-b2a1-91e80dc723eb":

<Accordion title="Request payload">
  ```curl
  curl --request POST \
       --url https://sandbox.pismolabs.io/lending/v2/loans/2717a296-124a-47cc-b2a1-91e80dc723eb/disburse \
       --header 'accept: application/json' \
       --header 'content-type: application/json' \
       --data '
  {
    "disbursement_account": {
      "account_type": "INTERNAL",
      "account_id": 221123
  	}
  }
  '
  ```
</Accordion>

The Pismo platform generates a [Loan disbursement status changed](https://developers.pismo.io/events/docs/lending-loan-disbursement-status-change-2) event:

<Accordion title="Loan disbursement status changed event">
  ```json
  {
      "loan_id": "2717a296-124a-47cc-b2a1-91e80dc723eb",
      "org_id": "TN-89e56522-726a-453e-ba6d-796b03245128",
      "disbursement_id": "89e56522-726a-453e-ba6d-796b03245128",
      "idempotency_key": "48704d83-0412-431f-816a-50ba81451148",
      "currency": "USD",
      "created_at": "2026-10-24T21:34:47",
      "updated_at": "2026-10-24T21:34:47",
      "previous_disbursement_status": "SCHEDULED",
      "current_disbursement_status": "PROCESSING",
      "disbursement_amount": 1234.56,
      "disbursement_account": {
          "account_type": "INTERNAL",
          "account_id": 221123
      },
      "authorization_id": 1231231,
      "authorization_tracking_id": "ded913af-abc9-4769-b179-068ed6181ec5",
      "disbursement_date": "2026-10-24"
  }
  ```
</Accordion>

The current disbursement status is stored in the loan object under `disbursement.schedule[].status`. The status can be `SCHEDULED`, `PROCESSING`, `CANCELED`, `EXPIRED`, or `PAID`. Each schedule entry also includes the date of the scheduled or actual disbursement.

## Multiple disbursements

You can disburse a loan in multiple parts (tranches) instead of a single release. Use this approach when funds are released over time or tied to conditions, such as project milestones.

<Callout icon="📘" theme="info">
  Loan product prerequisites

  Since the loan product defines disbursement rules, ensure the associated product has these settings for multiple disbursements:

  * The  `disbursement_method` object is set to `MULTIPLE`
  * The `processing_codes` object is configured with internal arrays, external arrays, or both

  If either parameter is missing, the Pismo platform treats the loan as a single-disbursement loan.

  For more information, refer to [Create loan products](https://developers.pismo.io/pismo-docs/docs/create-loan-products).
</Callout>

For multiple disbursements, call the [Disburse loan ](https://developers.pismo.io/pismo-docs/reference/disburseloanv2) endpoint multiple times.

For each request, you must provide:

* `disbursement_amount`
* `disbursement_id`

# Validation rules

The Pismo platform ensures that the total disbursed amount does not exceed the loan principal. With each disbursement, the platform compares the amount required for the disbursement with the remaining principal amount. If the disbursement amount would cause the remaining principal to be depleted, the platform rejects the disbursement.

## Example

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Scenario
      </th>

      <th>
        Amount
      </th>

      <th>
        Remaining principal
      </th>

      <th>
        Result
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Loan principal
      </td>

      <td>
        Loan origination (1,000)
      </td>

      <td>
        1,000
      </td>

      <td>
        No disbursements made at start
      </td>
    </tr>

    <tr>
      <td>
        First disbursement
      </td>

      <td>
        450
      </td>

      <td>
        550
      </td>

      <td>
        ✅ Disbursement accepted
      </td>
    </tr>

    <tr>
      <td>
        Second disbursement
      </td>

      <td>
        550
      </td>

      <td>
        0
      </td>

      <td>
        ✅ Disbursement accepted
      </td>
    </tr>

    <tr>
      <td>
        Third disbursement
      </td>

      <td>
        100
      </td>

      <td>
        0
      </td>

      <td>
        ❌ Disbursement rejected\
        (exceeds principal)
      </td>
    </tr>
  </tbody>
</Table>

This example shows the first disbursement for 400, so the remaining principal allows the platform to accept the disbursement. Any response other than 202 means the disbursement was rejected.

## Example request

<Accordion title="Request payload">
  ```json
  {
    "disbursement_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
    "disbursement_date": "2026-06-24",
    "disbursement_amount": 400.00,
    "disbursement_account": {
      "account_type": "INTERNAL",
      "account_id": 784165
    }
  }
  ```
</Accordion>

# View disbursement information

You can use Control Center or the API to view loan disbursement information:

| Method         | Description                                                          | For more information                                                                                                                                                              |
| :------------- | :------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Control Center | You can view disbursement information as part of account management. | [Manage loans in Control Center](https://developers.pismo.io/pismo-docs/docs/manage-loans-in-control-center)                                                                                                              |
| API            | Use the **Get loan** or **List account loans** endpoints.            | [Get loan](https://developers.pismo.io/pismo-docs/reference/getloanv2) <br /><br />  [List account loans](https://developers.pismo.io/pismo-docs/reference/getloansbyaccountidv2) |

Lists can be appended with new list items, but existing list items are immutable. This restriction means you can add new items to the list, but you can't change or remove existing items.

# Events

Each disbursement generates these events:

* [Loan disbursement status changed](https://developers.pismo.io/events/docs/lending-loan-disbursement-status-change-2)—Shows the progress and outcome of the specific disbursement
* [Loan status changed](https://developers.pismo.io/events/docs/lending-lending-loan-update-1)—Reflects updates to the loan; for example, total amount disbursed or modified balances

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v2/loans/{loanId}/disburse` | `disburseLoanV2` | Disburse loan | `api-specs/Lending.yaml` | no | KU-API-lending--disbursements |
| `GET /v2/loans/{loanId}` | `getLoanV2` | Get loan | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `GET /v2/accounts/{accountId}/loans` | `getLoansByAccountIdV2` | List account loans | `api-specs/Lending.yaml` | no | KU-API-lending--loans |

### Operation essentials

- **`POST /v2/loans/{loanId}/disburse`** (`disburseLoanV2`): security `BearerAuth`; required parameters `loanId` (path), `Idempotency-Key` (header); required body fields `disbursement_account`; response statuses 202, 400, 500; error codes in examples `ELND0003`, `ELND0004`, `ELND0001`; events none listed.
- **`GET /v2/loans/{loanId}`** (`getLoanV2`): security `BearerAuth`; required parameters `loanId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `ELND0002`, `ELND0005`, `ELND0003`, `ELND1807`, `ELND0005`, `ELND0001`; events none listed.
- **`GET /v2/accounts/{accountId}/loans`** (`getLoansByAccountIdV2`): security `BearerAuth`; required parameters `accountId` (path), `nextCursor` (query); required body fields none declared; response statuses 200, 400, 500; error codes in examples `ELND1802`, `ELND1803`, `ELND1804`, `ELND1807`, `ELND1808`, `ELND1809`; events none listed.

## Events

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `lending-lending-loan-update-1` | lending | 1 | https://developers.pismo.io/events/docs/lending-lending-loan-update-1 | 2 | KU-EVT-catalogue-lending |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/lending/disburse-loan.md`: updatedAt 2026-09-22T17:42:19.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/lending/disburse-loan.md` | whole document | https://developers.pismo.io/pismo-docs/docs/disburse-loan | `eabe700e5566b5b9…` | 2026-09-22T17:42:19.000Z |

## Related knowledge units

- `KU-API-lending--disbursements` — API reference: Lending — Disbursements
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-CC-lending` — Control Center lending: loan products and loan management
- `KU-EVT-catalogue-lending` — Event catalogue: lending
- `KU-LEND-loan-products` — Loan products: overview and creation
- `KU-LEND-simulate-loans` — Simulate loans
