---
ku_id: KU-PAY-payments
title: Payments and transfers
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/payments.md
  sha256: 44e82fd2260e2ca445522bbbb65cb5e10bcf7bde6581658d7168f5a69664cd6b
  url: https://developers.pismo.io/pismo-docs/docs/payments
  role: primary_guide
  updated_at: '2026-04-29T19:05:25.000Z'
operations:
- post-payments-v1-payments
- post-payments-v2-cancel
related_kus:
- KU-API-core-platform-payment-methods--payments
- KU-CARD-digital-wallets
- KU-EVT-catalogue-other-domains
- KU-PAY-payment-methods
- KU-PAY-payment-requests
- KU-PAY-transfers-make-and-cancel
grouping_rationale: single source page
---

# Payments and transfers

**KU ID:** `KU-PAY-payments` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/payments.md`:

> For any new deployments, the recommendation is to use the enhanced [Payment methods](https://developers.pismo.io/pismo-docs/docs/payment-methods) API instead of the  [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) and [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-payments-v2-cancel) endpoints described in this guide. All new feature developments will be available only in the Payment methods API. For more information, contact your Pismo representative.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/payments.md`: Payments and transfers; Anatomy of a transfer request; Payment method; Processing code; Examples; P2P with COF example; Cash-out with processing code example; Cash-in with metadata example

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/payments.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/payments · updatedAt: 2026-04-29T19:05:25.000Z

<!-- source:begin path=docs/core-platform/payments.md part=0-end -->

# Payments and transfers

<Callout icon="📘" theme="info">
  For any new deployments, the recommendation is to use the enhanced [Payment methods](https://developers.pismo.io/pismo-docs/docs/payment-methods) API instead of the  [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) and [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-payments-v2-cancel) endpoints described in this guide. All new feature developments will be available only in the Payment methods API. For more information, contact your Pismo representative.
</Callout>

The Pismo Payments API allows you to transfer funds between accounts inside the platform, perform cash-in and cash-out operations between accounts or external entities, use the customer's balance or credit cards to pay invoices, and more.

The transactions that can take place on the Pismo platform can be grouped into three categories:

* **cash-in**, where money is deposited to the platform account from an external environment
* **internal transfer**, where money is transferred between the platform accounts
* **cash-out**, where money is withdrawn from the platform account to an external environment

Here some examples of common fund transfers you can make in the Pismo platform:

* [transfer between two Pismo platform accounts (P2P)](https://developers.pismo.io/pismo-docs/docs/make-transfer#transfer-p2p)
* [transfer using a card on file](https://developers.pismo.io/pismo-docs/docs/make-transfer#transfer-from-card)
* [cash-in from an external entity into a Pismo account](https://developers.pismo.io/pismo-docs/docs/make-transfer#cash-in)
* [cash-out from a Pismo account to an external entity](https://developers.pismo.io/pismo-docs/docs/make-transfer#cash-out)
* [payment responding to a payment request](https://developers.pismo.io/pismo-docs/docs/payment-requests)

# Anatomy of a transfer request

In the request, the `from` array determines the sending party and the `to` array determines the receiving party. Both arrays can contain one of the objects: `account`, `card`, `custom_info`, or `merchant`. The structure of these arrays determines the type of transfer operation to be performed. You can pass along any additional information using the `metadata` object.

When requesting a transfer, two structures are worth noting: the **payment method** and the **processing code**.

## Payment method

The transfer data structure that is sent as a payload to the Payments API has two fundamental objects that determine what operation is being made. The `from` and `to` objects describe the source of the funds and its destination, and can contain one of the following nested structures:

| Object        | Description                                                                                                                                                                                           |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account`     | Identifies an account inside the Pismo platform.                                                                                                                                                      |
| `card`        | Contains details of a tokenized credit card previously stored in a wallet in the Pismo PCI environment. Go to [Wallet overview](https://developers.pismo.io/pismo-docs/docs/wallet-overview) if you want to learn more about tokenized cards. |
| `custom_info` | Describes custom payment information, usually about an external entity, which can be a checking account, debit card, or any other source destination.                                                 |
| `merchant`    | Identifies a merchant account inside the Pismo platform. The merchant receives the money on the receivable schedule according to the agreement between the marketplace and the merchant.              |

Combining these objects in the `from` and `to` properties determines if the funds are being collected in an account, transferred between the two of them, or sent to an external entity.

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th />

      <th>
        To: account
      </th>

      <th>
        To: card
      </th>

      <th>
        To: custom\_info
      </th>

      <th>
        To: merchant
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **From: account**
      </td>

      <td>
        Pismo account to Pismo account (P2P)
      </td>

      <td>
        Not available
      </td>

      <td>
        Cash-out of unregistered partnerships (for example, withdrawal or pay invoices)
      </td>

      <td>
        Pismo account to Pismo merchant account (P2M)
      </td>
    </tr>

    <tr>
      <td>
        **From: card**
      </td>

      <td>
        Transfers with tokenized cards (wallet):

        * P2P with card on file (COF), where the account IDs are different
        * Cash-in with COF, where the account IDs are the same
      </td>

      <td>
        Not available
      </td>

      <td>
        Cash-out of unregistered partnerships with COF (for example, slip payment)
      </td>

      <td>
        Pismo account to Pismo merchant account (P2M) with COF
      </td>
    </tr>

    <tr>
      <td>
        **From: custom\_info**
      </td>

      <td>
        Cash-in of unregistered partnerships (for example, pay invoice)
      </td>

      <td>
        Not available
      </td>

      <td>
        Not available
      </td>

      <td>
        Not available
      </td>
    </tr>

    <tr>
      <td>
        **From: merchant**
      </td>

      <td>
        Not available
      </td>

      <td>
        Not available
      </td>

      <td>
        Not available
      </td>

      <td>
        Merchant to merchant account (M2M)
      </td>
    </tr>
  </tbody>
</Table>

## Processing code

If the source (`from`) and destination (`to`) structure defines what kind of operation is being made (a cash-in, a peer-to-peer, or a cash-out), the processing code describes how this operation is treated internally and the type of transaction that will be generated. For instance, the way that the balance account will be impacted and if the operation needs to involve a validation by an external acquirer are operational pieces of information associated with a processing code. Processing code also defines the type of associated transaction generated and how it will be handled in accounting.

## Examples

### P2P with COF example

```json P2P with COF example
{
    "from":[{
        "amount":150,
        "currency":"USD",
        "card": {
            "id": "a9081236-58de-4ce2-9918-8440ede19032",
            "account_id": 123
        }
    }],
    "to":[{
        "account":{
            "id":125487
        }
    }]
}
```

### Cash-out with processing code example

```json Cash-out with processing code example
{
    "from":[{
        "amount":150,
        "currency":"USD",
        "processing_code": "007000",
        "account":{
            "id":125487
        }
    }],
    "to":[{
        "custom_info": {
            "external_id": "721-00047551-4",
            "type": "Bank transfer",
            "name": "John Doe",
            "description": "Transfer to National Bank"
        }
    }]
}
```

### Cash-in with metadata example

```json Cash-in with metadata example
{
    "from":[{
        "custom_info": {
            "external_id": "5512990-642",
            "type": "Deposit"
        }
    }],
    "to":[{
        "amount":100,
        "currency":"USD",
        "account":{
            "id":342485
        }
    }],
    "metadata":{
        "sender": "Andrew Foster",
        "bank": "OneBank",
        "branch_code": "0089",
        "account_id": "13000-7"
    }
}
```

For detailed reference information on how to create different transfers in the Pismo platform, go to [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments).\
For examples of different transfers, go to [Make transfer](https://developers.pismo.io/pismo-docs/docs/make-transfer).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /payments/v1/payments` | `post-payments-v1-payments` | Transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /payments/v2/cancel` | `post-payments-v2-cancel` | Cancel transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |

### Operation essentials

- **`POST /payments/v1/payments`** (`post-payments-v1-payments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `from`, `to`; response statuses 201, 202, 400, 409, 422, 500, 502; error codes in examples `WP2P0000`, `WP2P0019`, `EP2P9999`, `WP2P0005`, `WP2P0006`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WP2P0020`, `WP2P0013`, `WLDG0006`, `WP2P0010`, `WP2P0000`, `WP2P0000`, `ELDG500`, `EPCG501`, `EP2P9999`, `EP2P0001`, `EP2P0002`; events `authorization-authorization-event-1`.
- **`POST /payments/v2/cancel`** (`post-payments-v2-cancel`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `amount`; response statuses 200, 202, 208, 400, 404, 409, 500, 502; error codes in examples `AMON0004`, `WP2P0009`, `WP2P0000`, `AMON0000`, `WP2P0000`, `WP2P1005`, `EP2P0005`, `WP2P1111`, `EP2P0011`, `EP2P0013`, `WP2P0003`, `EP2P9999`, `WP2P3003`, `WP2P0033`, `WP2P0008`, `WP2P0000`, `WLDG0019`, `WLDG0004`, `WLDG0006`, `WLDG0005`, `WP2P0010`, `AMON0004`, `WP2P0009`, `WP2P0000`, `WP2P0000`, `ACQ0001`, `ACQ0000`, `EP2P9999`, `ELDG500`, `EP2P0001`; events `authorization-authorization-cancellation-event-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v2-cancel` | `authorization-authorization-cancellation-event-1` |
| `post-payments-v1-payments` | `authorization-authorization-event-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/payments.md`: updatedAt 2026-04-29T19:05:25.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/payments.md` | whole document | https://developers.pismo.io/pismo-docs/docs/payments | `44e82fd2260e2ca4…` | 2026-04-29T19:05:25.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-CARD-digital-wallets` — Digital wallets, MDES Token Connect and Click to Pay
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-payment-methods` — Payment methods
- `KU-PAY-payment-requests` — Payment requests
- `KU-PAY-transfers-make-and-cancel` — Transfers: making and cancelling transfers
