---
ku_id: KU-PAY-bank-slips
title: Bank slips
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/bank-slips.md
  sha256: 841b9ff1192d69537efd28b7cca1768caf8b9642e046e1ef209cc6ea7e880740
  url: https://developers.pismo.io/pismo-docs/docs/bank-slips
  role: primary_guide
  updated_at: '2026-04-25T02:54:44.000Z'
operations:
- delete-integrated-payments-api-v1-bankslips-issue
- get-integrated-payments-api-v1-bankslips-issue-retrieve
- get-integrated-payments-api-v1-bankslips-receipts
- post-integrated-payments-api-v1-bankslips-issue
- post-integrated-payments-api-v1-bankslips-pay
- post-integrated-payments-api-v1-bankslips-validate
related_kus:
- KU-API-banking-integrated-payments--bank-slip
- KU-API-banking-integrated-payments--bank-slip-issuance
- KU-EVT-catalogue-integrated
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Bank slips

**KU ID:** `KU-PAY-bank-slips` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/bank-slips.md`:

> Bank slips, either in printed or virtual form, are a common method used for bill payments such as utilities, taxes, and rent. These slips can be paid at multiple financial institutions and are widely used in countries like Brazil, Argentina, and Chile.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/bank-slips.md`: Bank slips; Payment flow; Issue bank slips; Issuing bank slips; Retrieving issued bank slips; Deleting bank slips; Bank slips in different countries; Brazil

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/bank-slips.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/bank-slips · updatedAt: 2026-04-25T02:54:44.000Z

<!-- source:begin path=docs/core-banking/bank-slips.md part=0-end -->

# Bank slips

Bank slips, either in printed or virtual form, are a common method used for bill payments such as utilities, taxes, and rent. These slips can be paid at multiple financial institutions and are widely used in countries like Brazil, Argentina, and Chile.

To validate and pay a bank slip, you can scan a barcode (if possible) or enter the digitable line (numbers on the bank slip that represent the barcode information). Pismo then connects with the charge holder and returns to you payment confirmation or an error message.

# Payment flow

Paying a bank slip at Pismo is a three-step process.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Endpoint
      </th>

      <th>
        Step
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        [Validate bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-validate)
      </td>

      <td>
        Validation
      </td>

      <td>
        As required before payment, the customer submits the bank slip for validation, either using an app to scan a QR code or entering the digitable line manually.

        Pismo transmits the data to the payer’s banking provider to get information about the bill and return it to the client. This information includes the bill amount and to whom the client is paying.

        * \*Note: **This endpoint might return an`external_authorization` field. If so, it**must\*\* be passed in the Pay bank slip endpoint.
      </td>
    </tr>

    <tr>
      <td>
        [Pay bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-pay)
      </td>

      <td>
        Payment
      </td>

      <td>
        Pismo calls the payment provider to execute the payment and settle the transaction. Provider notifies Pismo that the payment is settled. Pismo returns confirmation to the client or an error message if it fails.

        This endpoint generates an [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) event and a [Financial bankslip status changed](https://developers.pismo.io/events/docs/integrated-payments-bankslip-status-change-1) event.
      </td>
    </tr>

    <tr>
      <td>
        [List bank slip receipts](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-bankslips-receipts)
      </td>

      <td>
        Proof of payment (receipt)
      </td>

      <td>
        When a customer requests a payment receipt, Pismo forwards the request to the provider, who then generates the receipt, which Pismo returns to the customer.
      </td>
    </tr>
  </tbody>
</Table>

# Issue bank slips

Similar to an invoice, a bank slip can be generated and issued to the client for completing a payment. The slip specifies the payment amount required from the payer to finalize a transaction. These bank slips can be paid at multiple places, such as ATMs, physical branches, and digital platforms.

Issuing bank slips involves these steps:

1. Generating the bank slip with the charged amount.
2. Forwarding the bank slip to the provider for processing.

The Pismo platform provides three endpoints that allow you to issue, view, and delete bank slips:

* [Issue bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-issue) to generate a charged amount.
* [Retrieve issued bank slip](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-bankslips-issue-retrieve) to fetch information about the created charge.
* [Delete issued bank slip](https://developers.pismo.io/pismo-docs/reference/delete-integrated-payments-api-v1-bankslips-issue) to revoke the charge. Note that only the charge's creator has the ability to revoke it.

These endpoints are used in combination with the [Pay bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-pay) endpoints to process payments. In essence, you generate a bank slip with the charge to the payer, and the payer pays it to complete the transaction.

**NOTE**: Pismo is partnering with Celcoin to implement the issue bank slip feature.

## Issuing bank slips

<Image alt="Figure 1: Issuing bank slips" align="center" src="https://files.readme.io/e267c6cb034ff2179b912f114dba0ccccecd395e4f55d2cfc0d0de5e06f5a445-Issue_bank_slip_guide_-_Post.png">
  Figure 1: Issuing bank slips
</Image>

1. The client calls [Issue bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-issue) to create a charge, which generates a bank slip.
2. Pismo sends the request to the provider for processing.
3. If the processing is successful, a [Bank slip issuance registered](https://developers.pismo.io/events/docs/integrated-payments-bankslip-issue-register-1) event is generated with a `CREATED` status and the requested data is returned to the client.
4. However, if processing fails, Pismo records the status as `PROCESSING`, and returns the status back to the client. Pismo continues to resend the request until it's successfully processed. When successful, Pismo generates a [Bank slip issuance registered](https://developers.pismo.io/events/docs/integrated-payments-bankslip-issue-register-1) event with a `CREATED` status and sends it back to the client.

## Retrieving issued bank slips

<Image alt="Figure 2: Retrieving issued bank slips" align="center" src="https://files.readme.io/acfb52a377556bcf9f8eda931b8b720592ed2b66e8d452469105ed21ee88b622-Issue_bank_slip_guide_-_Get.png">
  Figure 2: Retrieving issued bank slips
</Image>

1. The client calls [Retrieve issued bank slip](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-bankslips-issue-retrieve) to get information about a previously issued bank slip.
2. The request is forwarded to the provider.
3. If the provider receives the request and is able to locate the specified bank slip, the information is returned to the client in the response.
4. In case of failure, an error message is returned.

## Deleting bank slips

<Image alt="Figure 3: Deleting bank slips" align="center" src="https://files.readme.io/14c0057a603cd33efb3ad04f155a12e2445d24cb268f873ee30a6a2f911aac82-Issue_bank_slip_guide_-_Delete.png">
  Figure 3: Deleting bank slips
</Image>

1. The client calls [Delete issued bank slip](https://developers.pismo.io/pismo-docs/reference/delete-integrated-payments-api-v1-bankslips-issue) to delete an existing bank slip.
2. The request is forwarded to the provider.
3. If the deletion is successful, the bank slip is deleted, and a [Bank slip issuance canceled](https://developers.pismo.io/events/docs/integrated-payments-bankslip-issue-cancel-1) event with a `CANCELED` status is returned to the client.
4. However, in case of failure, an error message is returned.

# Bank slips in different countries

## Brazil

In Brazil, bank slips are called **boletos** and there are two types:

* **Boletos de Concessionárias**  - Also known as  “consumer bills.” The most popular are electricity bills, water bills, gas bills, etc.  These bills have digitable lines that start with an "8".  They can be paid through our endpoints and include taxes levied in Brazil ([DARF](https://thebrazilbusiness.com/article/all-about-darf), [FGTS](https://thebrazilbusiness.com/article/introduction-to-fgts), [GRU](https://thebrazilbusiness.com/article/all-about-gru), [GPS](https://thebrazilbusiness.com/article/all-about-gru)).
* **Boletos Bancários** - Bank generated slips.

Both types have digitable line fields that are usually between 44 and 48 digits.

Pismo works with providers such as [BTG Pactual](https://www.btgpactual.us), [Celcoin](https://celcoin.com.br/), and [Itaú](https://www.itau.com.br/) to implement the bank slip payment feature in Brazil.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/bankslips/validate` | `post-integrated-payments-api-v1-bankslips-validate` | Validate bank slip | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip |
| `POST /v1/bankslips/pay` | `post-integrated-payments-api-v1-bankslips-pay` | Pay bank slip | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip |
| `GET /v1/bankslips/receipts` | `get-integrated-payments-api-v1-bankslips-receipts` | List bank slip receipt | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip |
| `POST /v1/bankslips-issue` | `post-integrated-payments-api-v1-bankslips-issue` | Issue bank slip | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip-issuance |
| `GET /v1/bankslips-issue/client-requests/{clientRequestId}` | `get-integrated-payments-api-v1-bankslips-issue-retrieve` | Get issued bank slip | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip-issuance |
| `DELETE /v1/bankslips-issue/client-requests/{clientRequestId}` | `delete-integrated-payments-api-v1-bankslips-issue` | Delete issued bank slip | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip-issuance |

### Operation essentials

- **`POST /v1/bankslips/validate`** (`post-integrated-payments-api-v1-bankslips-validate`): security `BearerAuth`; required parameters `Authorization` (header); required body fields `type`; response statuses 200, 400, 403, 404, 409, 500, 502; error codes in examples `EIP0008`, `EIP0010`, `EIP0023`, `EIP0005`, `EIP0006`, `EIP0049`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0022`, `EIP0070`, `EIP0024`; events none listed.
- **`POST /v1/bankslips/pay`** (`post-integrated-payments-api-v1-bankslips-pay`): security `BearerAuth`; required parameters `Authorization` (header), `x-idempotency-key` (header); required body fields `account_id`, `amount`; response statuses 202, 400, 403, 404, 409, 500, 502, 504; error codes in examples `EIP0005`, `EIP0006`, `EIP0008`, `EIP0010`, `EIP0012`, `EIP0013`, `EIP0017`, `EIP0023`, `EIP0020`, `EIP0061`, `EIP0005`, `EIP0006`, `EIP0009`, `EIP0030`, `EIP0049`, `EIP0063`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0011`, `EIP0015`, `EIP0019`, `EIP0022`, `EIP0028`, `EIP0041`, `EIP0051`, `EIP0053`, `EIP0069`, `EIP0070`, `EIP0018`, `EIP0021`, `EIP0024`, `EIP0002`; events `authorization-authorization-event-1`, `integrated-payments-bankslip-status-change-1`, `integrated-payments-financial-reconciliation-1`.
- **`GET /v1/bankslips/receipts`** (`get-integrated-payments-api-v1-bankslips-receipts`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 403, 500; error codes in examples `EIP0010`, `EIP0012`, `EIP0013`, `EIP0045`, `EIP0046`, `EIP0047`, `EIP0005`, `EIP0006`, `EIP0029`, `EIP0004`, `EIP0011`, `EIP0014`, `EIP0041`; events none listed.
- **`POST /v1/bankslips-issue`** (`post-integrated-payments-api-v1-bankslips-issue`): security `BearerAuth`; required parameters `x-idempotency-key` (header); required body fields `amount`, `due_date`; response statuses 202, 400, 403, 409, 500, 502; error codes in examples `EIP0010`, `EIP0012`, `EIP0013`, `EIP0016`, `EIP0017`, `EIP0023`, `EIP0077`, `EIP0005`, `EIP0006`, `EIP0009`, `EIP0029`, `EIP0042`, `EIP0065`, `EIP0015`, `EIP0014`, `EIP0007`, `EIP0004`, `EIP0011`, `EIP0028`, `EIP0022`, `EIP0070`, `EIP0074`, `EIP0018`, `EIP0024`; events `integrated-payments-bankslip-issue-register-1`.
- **`GET /v1/bankslips-issue/client-requests/{clientRequestId}`** (`get-integrated-payments-api-v1-bankslips-issue-retrieve`): security `BearerAuth`; required parameters `clientRequestId` (path), `x-idempotency-key` (header); required body fields none declared; response statuses 200, 400, 403, 404, 409, 500, 502; error codes in examples `EIP0072`, `EIP0010`, `EIP0023`, `EIP0005`, `EIP0006`, `EIP0073`, `EIP0062`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0022`, `EIP0074`, `EIP0070`, `EIP0024`; events none listed.
- **`DELETE /v1/bankslips-issue/client-requests/{clientRequestId}`** (`delete-integrated-payments-api-v1-bankslips-issue`): security `BearerAuth`; required parameters `clientRequestId` (path); required body fields none declared; response statuses 204, 400, 403, 404, 409, 422, 500, 502, 504; error codes in examples `EIP0025`, `EIP0010`, `EIP0023`, `EIP0003`, `EIP0005`, `EIP0006`, `EIP0043`, `EIP0062`, `EIP0065`, `EIP0076`, `EIP0007`, `EIP0041`, `EIP0004`, `EIP0022`, `EIP0070`, `EIP0053`, `EIP0074`, `EIP0024`, `EIP0024`; events `integrated-payments-bankslip-issue-cancel-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-integrated-payments-api-v1-bankslips-pay` | `authorization-authorization-event-1` |
| `delete-integrated-payments-api-v1-bankslips-issue` | `integrated-payments-bankslip-issue-cancel-1` |
| `post-integrated-payments-api-v1-bankslips-issue` | `integrated-payments-bankslip-issue-register-1` |
| `post-integrated-payments-api-v1-bankslips-pay` | `integrated-payments-bankslip-status-change-1` |
| `post-integrated-payments-api-v1-bankslips-pay` | `integrated-payments-financial-reconciliation-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `authorization-authorization-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-event-1 | 9 | KU-EVT-catalogue-other-domains |
| `integrated-payments-bankslip-issue-cancel-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-bankslip-issue-cancel-1 | 1 | KU-EVT-catalogue-integrated |
| `integrated-payments-bankslip-issue-register-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-bankslip-issue-register-1 | 1 | KU-EVT-catalogue-integrated |
| `integrated-payments-bankslip-status-change-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-bankslip-status-change-1 | 1 | KU-EVT-catalogue-integrated |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/bank-slips.md`: updatedAt 2026-04-25T02:54:44.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 4 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/bank-slips.md` | whole document | https://developers.pismo.io/pismo-docs/docs/bank-slips | `841b9ff1192d6953…` | 2026-04-25T02:54:44.000Z |

## Related knowledge units

- `KU-API-banking-integrated-payments--bank-slip` — API reference: Banking - Integrated payments — Bank slip
- `KU-API-banking-integrated-payments--bank-slip-issuance` — API reference: Banking - Integrated payments — Bank slip issuance
- `KU-EVT-catalogue-integrated` — Event catalogue: integrated
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
