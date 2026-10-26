---
ku_id: KU-EVT-timeline-overview
title: Timeline events
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/timeline-overview.md
  sha256: 41b9b77a7ef28bb185c0dafdb7983df67b8c5b9dc2830e92dfeff99443bab248
  url: https://developers.pismo.io/pismo-docs/docs/timeline-overview
  role: primary_guide
  updated_at: '2026-03-18T17:00:57.000Z'
operations:
- list-timeline-events
related_kus:
- KU-API-data-and-reporting-timeline--timeline
- KU-EVT-data-events-concepts
grouping_rationale: single source page
---

# Timeline events

**KU ID:** `KU-EVT-timeline-overview` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/timeline-overview.md`:

> Timeline events deliver information about account activity to your end users.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/timeline-overview.md`: Timeline events; Example list events response

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/timeline-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/timeline-overview · updatedAt: 2026-03-18T17:00:57.000Z

<!-- source:begin path=docs/data-and-reporting/timeline-overview.md part=0-end -->

# Timeline events

Timeline events deliver information about account activity to your end users.

> 📘 Timeline events versus data events
>
> [Timeline events](https://developers.pismo.io/pismo-docs/docs/timeline-overview) are meant to deliver messages to your end users, such as a credit-limit notification in a mobile banking app. These are not the same as [data events](https://developers.pismo.io/pismo-docs/docs/event-data).

Timeline events are defined with a **type** and a **category**. Your Pismo representative works with you to define the categories and types for your organization. The following table illustrates an example configuration.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Type
      </th>

      <th>
        Category
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Card
      </td>

      <td>
        Events related to physical cards.\
        `ACTIVATION` – Physical card was activated.\
        `BLOCK` – Physical card was (temporarily) blocked by the user.\
        `CREATION` – Card object for an account was created in the system.\
        `DELIVERY` – Delivery event for a physical card was filed by the courier company.\
        `PRODUCTION` – Card information was successfully sent to the embossing company and the card is being manufactured.\
        `UNBLOCK` – Physical card was unblocked by the user.
      </td>
    </tr>

    <tr>
      <td>
        Cash in
      </td>

      <td>
        Events related to platform authorizations.\
        `AUTHORIZATION` – Operation was authorized.\
        `CANCELLATION` – Operation was cancelled.\
        `CONFIRMATION` – Operation was confirmed.\
        `DENIED` – Operation was denied.\
        `DENIED_CANCELLATION` – Operation cancellation was denied.\
        `PARTIAL_CANCELLATION` – Operation was partially cancelled.
      </td>
    </tr>

    <tr>
      <td>
        Cash out
      </td>

      <td>
        Events related to platform authorizations.\
        `AUTHORIZATION` – Operation was authorized\
        `CANCELLATION` – Operation was cancelled.\
        `CONFIRMATION` – Operation was confirmed.\
        `PARTIAL_CANCELLATION` – Operation was partially cancelled.\
        `DENIED` – Operation was denied.\
        `DENIED_CANCELLATION` – Operation cancellation was denied.
      </td>
    </tr>

    <tr>
      <td>
        Confirmation
      </td>

      <td>
        Events related to transaction confirmations.\
        `AUTHORIZE` – Operation was authorized.\
        `CANCELLATION` – Operation was cancelled.\
        `REPLACEMENT`– Operation was replaced.\
        `REFUSAL` – Transaction was not authorized and was refused.
      </td>
    </tr>

    <tr>
      <td>
        Credit
      </td>

      <td>
        Events from account's credit monitoring service.\
        `LIMIT_NEAR` – Credit balance has exceeded 80 percent of its limit.\
        `LIMIT_REACHED` – Credit balance has reached its credit limit.
      </td>
    </tr>

    <tr>
      <td>
        Dispute
      </td>

      <td>
        Events related to transaction disputes. There is only one status for this category.\
        `CREATE` – A dispute was filed for a transaction.
      </td>
    </tr>

    <tr>
      <td>
        Statement
      </td>

      <td>
        Events pertaining to credit card account billing cycle.\
        `CARD_BLOCK` – Physical card was blocked due to a past overdue statement.\
        `CLOSE` – Current statement was closed.\
        `PARTIAL_PAYMENT` – Partial payment was confirmed.\
        `PAYMENT` – Payment for the current statement was confirmed.\
        `OVERDUE` – Statement due date passed without payment.
      </td>
    </tr>

    <tr>
      <td>
        Tokenization
      </td>

      <td>
        Events for **tokenized** cards (when the card number is registered with a mobile payments system, such as Apple Pay or Google Pay). There is only one status for this category:\
        `ACCEPTED` – Card tokenization was accepted.
      </td>
    </tr>

    <tr>
      <td>
        Transaction
      </td>

      <td>
        Events related to authorizing transactions.\
        `AUTHORIZE` – Transaction was authorized (for example, a purchase was made).\
        `CANCELLATION` – Transaction was not authorized and was canceled.\
        `CANCELLATION_REFUSAL`– Cancellation was not authorized and was refused.\
        `CANCELLATION_REVERSAL`– Cancellation was reversed.\
        `INCREMENTAL`–  Incremental amount was added to the transaction.\
        `PARTIAL_CANCELLATION`– Operation was partially cancelled.\
        `REFERRAL`– Operation was referred.\
        `REFUSAL` – Transaction was not authorized and was refused (for example, due to lack of credit).\
        `REPLACEMENT`– Operation was replaced.
      </td>
    </tr>
  </tbody>
</Table>

# Example list events response

Below is an example response from the [List account timeline events](https://developers.pismo.io/pismo-docs/reference/list-timeline-events) endpoint. The example has three events:

* Transaction event (type: REFUSAL)
* Confirmation event (type: AUTHORIZE)
* Cash-in event (type: TED \[electronic transfer available])

<details>
  <summary>Example list events response</summary>

  ```json
  {
     "has_next": false,
     "next_cursor": null,
     "count": 3,
     "items": [
         {
             "type": "TRANSACTION",
             "account_id": 100697199,
             "category": "REFUSAL",
             "tenant_account_timestamp": "TN-6aec613f-44ba-4184-9488-bf0343e74734::100697199::2022-02-15T20:27:02.151790540Z",
             "data": {
                 "item": {
                     "contract_amount": 123.77,
                     "response_code": "12",
                     "merchant_city": "MERCHANT CITY",
                     "dcc": true,
                     "org_operation": {
                         "processing_code": "003100"
                     },
                     "entry_mode": "001",
                     "number_of_installments": 1,
                     "principal_amount": 14,
                     "settlement_currency_literal": "USD",
                     "currency_code": "986",
                     "cardholderbilling_amount": 14,
                     "settlement_currency_code": "840",
                     "network": "MASTERCARD",
                     "pre_authorization": false,
                     "merchant_category_group": "SUPPLIES",
                     "soft_descriptor": "MERCHANT NAME",
                     "currency_literal": "BRL",
                     "cash_back_amount": 0,
                     "airport_tax": 0,
                     "interest_rate": 0,
                     "id": 3642614,
                     "mti": "0100",
                     "installment_amount": 14,
                     "to_name": "MERCHANT NAME",
                     "merchant_category_code": "5199",
                     "settlement_currency_rate": 1,
                     "merchant_state_or_country": "USA",
                     "card_id": 877427,
                     "cardholder_currency_rate": 0,
                     "local_amount": 14,
                     "entry_mode_literal": "UNKNOWN",
                     "customer_id": 16162789,
                     "settlement_currency_amount": 0.2,
                     "custom_code": "IAT"
                 }
             },
             "correlation_id": "606a7dad-6f84-44a2-862b-58aed51d14c1",
             "timestamp": "2022-02-15T20:27:02.151790540Z"
         },
         {
             "type": "CONFIRMATION",
             "account_id": 100697199,
             "category": "AUTHORIZE",
             "tenant_account_timestamp": "TN-6aec613f-44ba-4184-9488-bf0343e74734::100697199::2022-02-15T20:26:56.151790540Z",
             "data": {
                 "item": {
                     "contract_amount": 123.77,
                     "response_code": "00",
                     "merchant_city": "MERCHANT CITY",
                     "dcc": true,
                     "org_operation": {
                         "processing_code": "003100"
                     },
                     "entry_mode": "001",
                     "number_of_installments": 1,
                     "principal_amount": 14,
                     "settlement_currency_literal": "USD",
                     "currency_code": "986",
                     "cardholderbilling_amount": 14,
                     "ledger_update_id": "eb55fc5c-4c4c-4fa0-9188-87388483b1ca",
                     "settlement_currency_code": "840",
                     "network": "MASTERCARD",
                     "pre_authorization": false,
                     "merchant_category_group": "SUPPLIES",
                     "soft_descriptor": "MERCHANT NAME",
                     "currency_literal": "BRL",
                     "authorization_code": "TLT3S1",
                     "cash_back_amount": 0,
                     "airport_tax": 0,
                     "interest_rate": 0,
                     "id": 3642614,
                     "mti": "1240",
                     "installment_amount": 14,
                     "to_name": "MERCHANT NAME",
                     "merchant_category_code": "5199",
                     "settlement_currency_rate": 1,
                     "merchant_state_or_country": "USA",
                     "card_id": 877427,
                     "cardholder_currency_rate": 0,
                     "local_amount": 14,
                     "entry_mode_literal": "UNKNOWN",
                     "customer_id": 16162789,
                     "settlement_currency_amount": 0.2
                 }
             },
             "correlation_id": "7365faa8-28e2-403d-a953-8a9ba5fa6ea2",
             "timestamp": "2022-02-15T20:26:56.151790540Z"
         },
         {
             "type": "CASHIN",
             "account_id": 100697199,
             "category": "TED",
             "tenant_account_timestamp": "TN-6aec613f-44ba-4184-9488-bf0343e74734::100697199::2022-02-15T14:09:12.151790540Z",
             "data": {
                 "item": {
                     "to_account_number": "6531359",
                     "amount": 20,
                     "to_name": "Tinashe Sashi Ren",
                     "to_bank": "631",
                     "to_branch": "5536",
                     "from_document_number": "632698736583",
                     "entry_mode": "QRCODE",
                     "from_branch": "4114",
                     "from_name": "Shams Veasna Aaren",
                     "to_check_digit": "5",
                     "to_entity_type": "F",
                     "from_account_number": "6345373",
                     "from_bank": "512",
                     "from_check_digit": "9",
                     "to_document_number": "437599086325",
                     "context": "TED",
                     "to_phone": "5135551352",
                     "id": 1235123,
                     "status": "PROCESSED",
                     "authentication": "GRz5wv3vLQz9WP"
                 }
             },
             "correlation_id": "9abfa807-61f2-4e1d-8e2b-5d4e4e8bc57a",
             "timestamp": "2022-02-15T14:09:12.151790540Z"
         }
     ]
  }
  ```
</details>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /timeline/v1/timeline` | `list-timeline-events` | List account timeline events | `api-specs/Data_and_reporting_-_Timeline.yaml` | no | KU-API-data-and-reporting-timeline--timeline |

### Operation essentials

- **`GET /timeline/v1/timeline`** (`list-timeline-events`): security `S2SAuthentication`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/data-and-reporting/timeline-overview.md`: updatedAt 2026-03-18T17:00:57.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/timeline-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/timeline-overview | `41b9b77a7ef28bb1…` | 2026-03-18T17:00:57.000Z |

## Related knowledge units

- `KU-API-data-and-reporting-timeline--timeline` — API reference: Data and reporting - Timeline — Timeline
- `KU-EVT-data-events-concepts` — Data events: concepts and event-generating APIs
