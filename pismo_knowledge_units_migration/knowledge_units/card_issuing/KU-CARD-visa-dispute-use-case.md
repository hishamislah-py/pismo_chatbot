---
ku_id: KU-CARD-visa-dispute-use-case
title: Visa dispute use case
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/visa-dispute-use-case.md
  sha256: 9585e8994ea79570b6bd7a5910716a38563cffc2ca676a6c6b80a4c511d5ec9d
  url: https://developers.pismo.io/pismo-docs/docs/visa-dispute-use-case
  role: primary_guide
  updated_at: '2026-09-11T18:47:05.000Z'
operations:
- post-v1-disputes-disputeId-event
- post-v1-disputes-disputeId-file
- post-v1-networkauthorization-disputes
- post-v2-fraud-report
related_kus:
- KU-API-card-issuing-disputes--disputes-part-01
- KU-API-card-issuing-disputes--evidence-files
- KU-API-card-issuing-disputes--fraud-report
- KU-EVT-catalogue-disputes
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Visa dispute use case

**KU ID:** `KU-CARD-visa-dispute-use-case` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/visa-dispute-use-case.md`:

> Below is a detailed, real-world walkthrough of a Visa fraud dispute going through the full lifecycle on the Pismo platform, including every API call, state machine transition, and event generated. For more information, refer to <a href="https://www.visa.com/en-us/support/business/dispute-resolution" target="_blank">Visa dispute resolution</a>.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/visa-dispute-use-case.md`: Visa dispute use case; Visa fraud dispute (reason code 10); Scenario; Step 1: Create the dispute; Step 2: Create fraud report (Visa TC40); Step 3: Upload evidence file (optional); Step 4: Open dispute and send to Visa; &#x20;Visa accepts or rejects chargeback; Visa accepts chargeback; Visa rejects chargeback; Dispute resolution; Chargeback accepted (dispute closed - Issuer wins); Second presentment; &#x20;Acquirer contests dispute (second presentment); Issuer accepts second presentment (dispute closed - Acquirer wins); Issuer rejects second presentment (pre-arbitration); Pre-arbitration; Pre-arbitration accepted (dispute closed - Issuer wins); Pre-arbitration rejected (dispute closed - Acquirer wins); Acquirer skips second presentment; Acquirer initiates pre-arbitration; Pre-arbitration accepted (dispute closed - Acquirer wins); Pre-arbitration rejected (dispute closed - Issuer wins); Pre-arbitration fails; Simple fraud use case progression

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/visa-dispute-use-case.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/visa-dispute-use-case · updatedAt: 2026-09-11T18:47:05.000Z

<!-- source:begin path=docs/card-issuing/visa-dispute-use-case.md part=0-end -->

# Visa dispute use case

<br />

<Embed typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=5cLMwoY-6yA&feature=youtu.be" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F5cLMwoY-6yA%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D5cLMwoY-6yA%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252F5cLMwoY-6yA%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" href="https://www.youtube.com/watch?v=5cLMwoY-6yA&feature=youtu.be" providerUrl="https://www.youtube.com/" providerName="YouTube" />

# Visa fraud dispute (reason code 10)

Below is a detailed, real-world walkthrough of a Visa fraud dispute going through the full lifecycle on the Pismo platform, including every API call, state machine transition, and event generated. For more information, refer to <a href="https://www.visa.com/en-us/support/business/dispute-resolution" target="_blank">Visa dispute resolution</a>.

## Scenario

Maria contacts her issuer's call center to report that her Visa credit card was used for a fraudulent online purchase of $250.00 USD at `Shady_store.com` that she did not authorize. The card was not present (CNP fraud).

The issuer investigates and decides to proceed with a chargeback.

## Step 1: Create the dispute

Issuer calls Pismo's [Create dispute](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes)  endpoint:

`POST /v1/networkauthorization-disputes`

<details>
  <summary>Request payload</summary>

  ```json

  {
      "authorization_id": 14123,
      "modality": 10,
      "network_brand_type": "Visa",
      "disputed_amount": 250.00,
      "currency_code": "USD",
      "is_partial": false,
      "fraud_type": "B"
      "comment": "Cardholder reported an unauthorized card-not-present purchase at Shady_store.com for USD 250.00.",
      "transaction_date": "2026-07-10"
  }
  ```

  **Key fields**

  * `modality` = Enter category, aka *Reason*: `10` (fraud - card not present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).
  * `dispute_due_to` = Pick best enum reason for dispute. **Required**  if `modality` = `12` or `13`. Not necessary for  `10` or  `11`.
  * `first_installment_amount` - Enter value for this field if the dispute has more than one installment
  * `is_partial` - Set to `true` if the dispute is for a partial transaction amount and not the full amount.
  * `comment` - Add explanation if dispute is partial and not full
</details>

<details>
  <summary>Response payload</summary>

  ```json
  {
    "id": 48670,  // Dispute ID
    "authorization_id": 14123,
    "account_id": 12314,
    "airport_tax": false,
    "airport_tax_partial": false,
    "airport_tax_amount": null,
    "comment": "Cardholder reported an unauthorized card-not-present purchase.",
    "dispute_installment_id": 8675309,
    "reason": {
      "dispute_reason_id": 1,
      "description": "Fraudulent transaction - no cardholder authorization",
      "reason_code": 10,
      "type": "Visa"
    },
    "status": {
      "id": 316,
      "description": "PENDING", // Initial status
      "type": "PRIMITIVE_ON_US",
      "group": "OPEN"  // Initial group status
    },
    "protocol": "20251128111532456",
    "disputed_amount": 250.00,
    "created_at": "2026-03-26 12:48:01",
    "created_at_utc": "2026-03-26T12:48:01.532292494Z",
    "is_partial": false,
    "network_brand_type": "Visa",
    "transaction_date": "2026-07-10",
    "transaction_amount": 250.00,
    "currency_code": "USD"
  }
  ```

  **Key fields**

  * `id` - dispute ID
  * `status.description` - initial status - `PENDING`
  * `status.group` - initial group status - `CREATED`.
</details>

The Create dispute call generates a [Dispute installment created]()  event.

<details>
  <summary>Generated Dispute installment created event</summary>

  ```json
  {
    "id": 1,
    "dispute_id": 48670,
    "installment": 1,
    "arn": "test-arn",
    "chargeback_id": null,
    "claim_id": null,
    "installment_disputed_amount": 250.0,
    "network_return_reason_code": null,
    "reason_code": 10,
    "network_return_reject_reason": null,
    "network_response_error": null,
    "is_first_installment": false,
    "network_return_reject_reason_code": null,
    "dispute_status": {
      "id": 4,
      "description": "OPENED",
      "type": "PRIMITIVE",
      "group": "OPEN"
    },
    "account_id": 12314,
    "authorization_id": 14123,
    "internal_transaction_id": 123456789,
    "tracking_id": "9cd6485a-5680-4df0-a1f1-507e21d3428c",
    "network_brand_type": "Visa",
    "fraud_type": "1",
    "document_indicator": false,
    "network_response": [],
    "network_response_amount": 250.0,
    "network_response_currency": "USD",
    "network_status": "Authorization Dispute - Accepted by Acq",
    "reversal_reason": null,
    "transaction_id": "TI:example-network-transaction-id"
  }
  ```
</details>

**Initial state machine:**

* dispute status: `PENDING`
* group status: `OPEN`

## Step 2: Create fraud report (Visa TC40)

Issuer calls [Create fraud report](https://developers.pismo.io/pismo-docs/reference/post-v2-fraud-report)  endpoint. A Visa TC40 report is a fraud notification document generated when a cardholder reports an unauthorized or fraudulent transaction to their issuing bank.

**Note:** A fraud report is automatically generated for a Visa fraud dispute so calling this endpoint for our example is not necessary. A [Fraud report created](https://developers.pismo.io/events/docs/fraud-report-fraud-report-creation-1) event is also automatically generated.

`POST /v1/disputes/{disputeId}/fraud-report`

Note that the `dispute_id` is in the path.

<details>
  <summary>Request payload</summary>

  ```json
  {
      "report_type": "visa",
      "transaction_id": 1234567890,
      "report": {
        "fraud_type": "1",
        "fraud_type_category": "CARDTXN",
        "notification_cd": 1,
        "close_fraud_case_ind": false
      }
    }'
  ```

  **Key fields:**

  * `fraud_type` - `1` = stolen
  * `fraud_type_category` - `CARDTXN` = Card transaction
</details>

<details>
  <summary>Response payload</summary>

  ```json
  {
    "fraud_report_id": 10,
    "org_id": "TN-123xxxxxxxxxxxxxxxxx",
    "status": "PENDING",
    "network": "Visa",
    "report": {
      "close_fraud_case_ind": false,
      "fraud_type": "1",
      "fraud_type_category": "CARDTXN",
      "notification_cd": 1
    },
    "created_at": "2024-10-18T11:20:22.000Z",
    "network_authorization_id": 1234567890,
    "authorization_code": "F0JR9H",
    "transaction_id": 1234567890,
    "account_id": 12314,
    "card_id": 123456,
    "report_type": "visa"
  }
  ```

  <br />
</details>

This call generates a [Fraud report created](https://developers.pismo.io/events/docs/fraud-report-fraud-report-creation-1) event.

<details>
  <summary>Create fraud report generated event</summary>

  ```json
  {
    "org_id": "TN-123",
    "report_type": "visa",
    "report": {
      "fraud_type": "1",
      "fraud_type_category": "CARDTXN",
      "notification_cd": 1,
      "close_fraud_case_ind": false
    },
    "status": "PENDING",
    "network": "Visa",
    "fraud_report_id": 10,
    "dispute_id": 48670,
    "dispute_installment_id": 8675309,
    "account_id": 12314,
    "card_id": 123456,
    "customer_id": 89345,
    "network_authorization_id": 14123,
    "authorization_code": "A1B2C3",
    "created_at": "2024-10-01 13:19:28",
    "updated_at": null,
    "case_number": null,
    "fraud_report_network_id": null,
    "network_response": null
  }
  ```

  <br />
</details>

## Step 3: Upload evidence file (optional)

Issuer decides to upload Maria's police report via the [Upload evidence file](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-file)  endpoint as additional support for the dispute.

`POST /v1/disputes/{disputeId}/file`

<details>
  <summary>Request payload</summary>

  ```json
  curl --request POST 'https://sandbox.pismolabs.io/disputes/v1/disputes/48670/file' \
    --header 'Authorization: Bearer <account-token>' \
    --form 'name=Police Report' \
    --form 'category=CARD' \
    --form 'file=@/path/to/police_report.pdf;type=application/pdf' \
    --form 'dispute_installment_id=8675309'
  ```
</details>

<details>
  <summary>Response payload</summary>

  ```json
  {
    "id": 1,
    "org_id": "TN-123",
    "dispute_id": 48670,
    "dispute_installment_id": 8675309,
    "installment": 1,
    "path": "/path/of/directory/",
    "file_name": "police_report.pdf",
    "category": "CARD"
  }
  ```

  <br />
</details>

This call generates a [Dispute file uploaded](https://developers.pismo.io/events/docs/audit-dispute-upload-file-1) audit event.

<details>
  <summary>Upload evidence file generated event</summary>

  ```json
  {
      "method": "POST",
      "uri": "/v1/disputes/{disputeId}/file",
      "email": "mail@mail.com",
      "object": {
          "dispute_id": 48670,
          "path": "path/to/file/",
          "file_name": "police_report.pdf",
          "category": "CARD",
          "created_at_utc": "2026-05-10 11:09:08",
          "dispute_file_id": 1,
          "file_extension": "pdf",
          "dispute_installment_id": 8675309,
          "status": "PENDING",
          "updated_at": "2026-05-20 13:05:07"
      }
  }
  ```
</details>

## Step 4: Open dispute and send to Visa

Issuer passes the `OPEN` event to initiate the chargeback with Visa via the [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) endpoint.

`POST /v1/disputes/{disputeId}/event`

Note that the dispute's ID is passed in the endpoint path.

<details>
  <summary>Request payload</summary>

  ```json
  curl --request POST \
       --url https://sandbox.pismolabs.io/disputes/v1/disputes/48670/event \
       --header 'accept: application/json' \
       --header 'content-type: application/json' \
       --data '
  {
    "event": "OPEN"
  }
  '
  ```
</details>

<details>
  <summary>Response payload</summary>

  ```json
  {
    "id": 48670,
    "org_id": "TN-123xxxxxxxxx",
    "account_id": 12314,
    "authorization_id": 14123,
    "comment": "Cardholder reported an unauthorized card-not-present purchase at Shady_store.com for USD 250.00.",
    "dispute_reason": 10,
    "modality": 10,
    "dispute_status": "OPENED",
    "dispute_status_group": "OPEN",
    "timeline": {
      "data": "test"
    },
    "protocol": "20190321L123456"
  }
  ```

  Note that the dispute status is now `OPENED` and the dispute status group is `OPEN`.
</details>

This call generates a [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event.

<details>
  <summary>Update dispute status generated event</summary>

  ```json
  {
    "id": 184740,
    "dispute_id": 48670,
    "installment": 1,
    "arn": "05131054165000000048149",
    "chargeback_id": null,
    "claim_id": null,
    "installment_disputed_amount": 250.0,
    "network_return_reason_code": null,
    "reason_code": 10,
    "network_return_reject_reason": null,
    "network_response_error": null,
    "is_first_installment": true,
    "network_return_reject_reason_code": null,
    "dispute_status": {
      "id": 4,
      "description": "OPENED",
      "type": "PRIMITIVE",
      "group": "CREATED"
    },
    "chargeback_ref_num": null,
    "dispute_due_to": null,
    "dispute_form": null,
    "dispute_fraud_report": null,
    "fraud_type": null,
    "document_indicator": true,
    "network_response": [],
    "network_response_amount": null,
    "network_response_currency": null,
    "network_status": null,
    "reversal_reason": null,
    "account_id": 12314,
    "authorization_id": 14123,
    "internal_transaction_id": 987654321,
    "tracking_id": "9cd6485a-5680-4df0-a1f1-507e21d3428c",
    "network_brand_type": "Visa"
  }
  ```
</details>

**Event:**   [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `OPEN`[Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

**State machine transition:**

* dispute status: `PENDING`to `OPENED`
* group status: `OPEN`to `CARDNETWORK_CHARGEBACK`

# &#x20;Visa accepts or rejects chargeback

Visa processes the request and either accepts or rejects the requested chargeback.

## Visa accepts chargeback

Visa processes the request and accepts the chargeback. At this point, the chargeback has been officially filed. **The acquirer has been notified.**

**Event:**   [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `ISSUER WORKED`[Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

**State machine transition:**

* dispute status: `OPENED` to `CHARGEBACK_CREATED`
* group status: `CARDNETWORK_CHARGEBACK`

## Visa rejects chargeback

Visa processes the request and rejects the chargeback. Issuer has the chance to correct what's wrong and re-submit.

**Event:**   [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `FAILED_ON_CREATION`[Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

**State machine transition:**

* dispute status: `OPENED` to `FAILED`
* group status: `CARDNETWORK_CHARGEBACK`` to`FAILED\`

# Dispute resolution

A number of different scenarios can occur at this point.

## Chargeback accepted (dispute closed - Issuer wins)

The acquirer does not contest the dispute. Visa notifies Pismo that the dispute is resolved. The $250.00 is returned to the issuer/cardholder through Visa's network settlement process.

**Event:** [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `CLOSED`[Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

**State machine transition:**

* dispute status: `CHARGEBACK_CREATED`to `CHARGEBACK_ACCEPTED`
* group status: `CARDNETWORK_CHARGEBACK` to `WON`

## Second presentment

In a **second presentment** the merchant's acquiring bank resubmits the transaction with new evidence (e.g., signed receipts, proof of delivery) to prove the charge is valid.

**Note:** For a Visa fraud dispute, the second presentment is skipped and goes straight to [pre-arbitration](https://developers.pismo.io/pismo-docs/docs/draft-disputes-use-cases#pre-arbitration) .

### &#x20;Acquirer contests dispute (second presentment)

The acquirer rejects chargeback and escalates dispute to **second presentment**

**Event:** [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `ISSUER_REPRESENTMENT_UNWORKED`[Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

**State machine transition:**

* dispute status: `CHARGEBACK_CREATED`to `SECOND_PRESENTMENT`
* group status: `CARDNETWORK_CHARGEBACK` to `CARDNETWORK_SECOND_PRESENTMENT`

### Issuer accepts second presentment (dispute closed - Acquirer wins)

Issuer reviews the acquirer's evidence and agrees.

**Event:** [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `CLOSED_PROCESSED` [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

* dispute status: `CHARGEBACK_CREATED`to `CHARGEBACK_CLOSED`
* group status: `CARDNETWORK_CHARGEBACK` to `LOSS`

### Issuer rejects second presentment (pre-arbitration)

Issuer reviews the acquirer's evidence and still disagrees. The dispute is escalated to **pre-arbitration**.

**Event:** [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `SEND_PRE_ARBITRATION` [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

**State machine transition:**

* dispute status: `SECOND_PRESENTMENT`to `PRE_ARBITRATION_OPENED`
* group status: `CARDNETWORK_SECOND_PRESENTMENT` to `CARDNETWORK_PREARBITRATION`

## Pre-arbitration

In a pre-arbitration, the Issuer has rejected the acquirer's second presentment.

### Pre-arbitration accepted (dispute closed - Issuer wins)

Visa reviews and the acquirer accepts the pre-arbitration.

**Event:** [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `ACCEPT_PRE_ARBITRATION` [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

**State machine transition:**

* dispute status: `PRE_ARBITRATION_OPENED`to `PRE_ARBITRATION_ACCEPTED`
* group status: `CARDNETWORK_PREARBITRATION` to `WON`

### Pre-arbitration rejected (dispute closed - Acquirer wins)

Visa reviews and decides the acquirer is right.

**Event:** [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `DECLINE_PRE_ARBITRATION` [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

**State machine transition:**

* dispute status: `PRE_ARBITRATION_OPENED`to `PRE_ARBITRATION_DECLINED`
* group status: `CARDNETWORK_PREARBITRATION` to `LOSS`

## Acquirer skips second presentment

This is specific to Visa disputes where the acquirer initiates a pre-arbitration directly from `CHARGEBACK_CREATED` (skipping second presentment).

### Acquirer initiates pre-arbitration

Acquirer skips second presentment and goes directly to pre-arbitration reviews.

**Event:** [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `SEND_PRE_ARBITRATION` [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

**State machine transition:**

* dispute status: `CHARGEBACK_CREATED`to `PRE_ARBITRATION_OPENED`
* group status: `CARDNETWORK_CHARGEBACK` to `CARDNETWORK_PREARBITRATION`

### Pre-arbitration accepted (dispute closed - Acquirer wins)

Visa reviews and the Issuer accepts the pre-arbitration.

**Event:** [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `ACCEPT_PRE_ARBITRATION` [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

**State machine transition:**

* dispute status: `PRE_ARBITRATION_OPENED`to `PRE_ARBITRATION_ACCEPTED`
* group status: `CARDNETWORK_PREARBITRATION` to `LOSS`

### Pre-arbitration rejected (dispute closed - Issuer wins)

Visa reviews and decides the Issuer is right.

**Event:** [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called with event `DECLINE_PRE_ARBITRATION` [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event generated.

**State machine transition:**

* dispute status: `PRE_ARBITRATION_OPENED`to `PRE_ARBITRATION_DECLINED`
* group status: `CARDNETWORK_PREARBITRATION` to `WON`

## Pre-arbitration fails

If pre-arbitration fails—meaning the issuing bank and merchant cannot reach an agreement—the dispute is escalated to formal Visa Arbitration. Visa will review the case files and make a binding final ruling.The losing party of this final decision is typically responsible for hefty network arbitration filing fees, which can exceed $500 per transaction

# Simple fraud use case progression

The following table details actions, events, and status changes in a simple fraud use case.

<br />

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action
      </th>

      <th>
        Event
      </th>

      <th>
        Dispute Status
      </th>

      <th>
        Group Status
      </th>

      <th>
        Pismo Event
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        [Create dispute](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes) called
      </td>

      <td>
        ***
      </td>

      <td>
        `PENDING`
      </td>

      <td>
        `OPEN`
      </td>

      <td>
        [Dispute installment created](https://developers.pismo.io/events/docs/disputes-dispute-installment-creation-1)
      </td>
    </tr>

    <tr>
      <td>
        [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) called to open dispute with Visa
      </td>

      <td>
        `OPEN`
      </td>

      <td>
        `OPENED`
      </td>

      <td>
        `CARDNETWORK_CHARGEBACK`
      </td>

      <td>
        [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1)
      </td>
    </tr>

    <tr>
      <td>
        Dispute opened with Visa
      </td>

      <td>
        `ISSUER_WORKED`
      </td>

      <td>
        `CHARGEBACK_CREATED`
      </td>

      <td>
        `CARDNETWORK_CHARGEBACK`
      </td>

      <td>
        [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1)
      </td>
    </tr>

    <tr>
      <td>
        Chargeback accepted. Issuer wins.
      </td>

      <td>
        `CLOSED`
      </td>

      <td>
        `CARDNETWORK_ACCEPTED`
      </td>

      <td>
        `WON`
      </td>

      <td>
        [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1)
      </td>
    </tr>
  </tbody>
</Table>

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/networkauthorization-disputes` | `post-v1-networkauthorization-disputes` | Create dispute | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01 |
| `POST /v2/fraud-report` | `post-v2-fraud-report` | Create fraud report | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--fraud-report |
| `POST /v1/disputes/{disputeId}/file` | `post-v1-disputes-disputeId-file` | Upload evidence file | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--evidence-files |
| `POST /v1/disputes/{disputeId}/event` | `post-v1-disputes-disputeId-event` | Update dispute status | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01 |

### Operation essentials

- **`POST /v1/networkauthorization-disputes`** (`post-v1-networkauthorization-disputes`): security `BearerAuth`; required parameters `Authorization` (header); required body fields `modality`, `disputed_amount`, `is_partial`, `network_brand_type`; response statuses 200, 400, 401, 422, 500; error codes in examples none; events `disputes-dispute-installment-creation-1`.
- **`POST /v2/fraud-report`** (`post-v2-fraud-report`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 404, 409, 422, 500, 504; error codes in examples `EDPT0002`, `EDPT0005`, `BDPT0006`, `BDPT0007`, `BDPT0001`, `BDPT0002`, `EDPT9999`, `EDPT0001`; events `fraud-report-fraud-report-creation-1`.
- **`POST /v1/disputes/{disputeId}/file`** (`post-v1-disputes-disputeId-file`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `name`, `category`, `file`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /v1/disputes/{disputeId}/event`** (`post-v1-disputes-disputeId-event`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `event`, `reason`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `disputes-dispute-installment-status-change-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-networkauthorization-disputes` | `disputes-dispute-installment-creation-1` |
| `post-v1-disputes-disputeId-event` | `disputes-dispute-installment-status-change-1` |
| `post-v2-fraud-report` | `fraud-report-fraud-report-creation-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `disputes-dispute-installment-creation-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-dispute-installment-creation-1 | 4 | KU-EVT-catalogue-disputes |
| `disputes-dispute-installment-status-change-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1 | 4 | KU-EVT-catalogue-disputes |
| `fraud-report-fraud-report-creation-1` | fraud | 1 | https://developers.pismo.io/events/docs/fraud-report-fraud-report-creation-1 | 1 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/visa-dispute-use-case.md`: updatedAt 2026-09-11T18:47:05.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 4 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.
- `docs/card-issuing/visa-dispute-use-case.md` line 101: `[Dispute installment created]()` (empty link target, kept as published)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/visa-dispute-use-case.md` | whole document | https://developers.pismo.io/pismo-docs/docs/visa-dispute-use-case | `9585e8994ea79570…` | 2026-09-11T18:47:05.000Z |

## Related knowledge units

- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-API-card-issuing-disputes--evidence-files` — API reference: Card issuing - Disputes — Evidence files
- `KU-API-card-issuing-disputes--fraud-report` — API reference: Card issuing - Disputes — Fraud report
- `KU-EVT-catalogue-disputes` — Event catalogue: disputes
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
