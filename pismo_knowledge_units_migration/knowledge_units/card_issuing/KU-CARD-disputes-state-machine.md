---
ku_id: KU-CARD-disputes-state-machine
title: Disputes state machine
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/disputes-state-machine.md
  sha256: 01ea668d76d7d0837c4503e815316bda04686a65722e6aebf030939813c5a7fb
  url: https://developers.pismo.io/pismo-docs/docs/disputes-state-machine
  role: primary_guide
  updated_at: '2026-06-11T19:00:30.000Z'
operations:
- get-v1-disputes-disputeId-possible-status
- get-v1-disputes-possible-status
- post-v1-disputes-disputeId-event
related_kus:
- KU-API-card-issuing-disputes--disputes-part-01
- KU-API-card-issuing-disputes--state-check
- KU-EVT-catalogue-disputes
grouping_rationale: single source page
---

# Disputes state machine

**KU ID:** `KU-CARD-disputes-state-machine` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/disputes-state-machine.md`:

> A state machine is a programming architecture that allows dynamic flow to states depending on values from previous states or user inputs. Pismo uses a state machine it calls the *PRIMITIVE* state machine to guide customers through the dispute process.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/disputes-state-machine.md`: Disputes state machine; PRIMITIVE state machine statuses; Events and statuses; Migration statuses and events; State machine API endpoints; PRIMITIVE state machine diagram

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/disputes-state-machine.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/disputes-state-machine · updatedAt: 2026-06-11T19:00:30.000Z

<!-- source:begin path=docs/card-issuing/disputes-state-machine.md part=0-end -->

# Disputes state machine

A state machine is a programming architecture that allows dynamic flow to states depending on values from previous states or user inputs. Pismo uses a state machine it calls the *PRIMITIVE* state machine to guide customers through the dispute process.

The PRIMITIVE state machine provides a framework for opening a dispute and resolving it through the card network system. Customers can use this framework to build their own state machine on top of that, though it is not necessary.

The PRIMITIVE state machine  covers all aspects of chargeback, second presentment,  pre-arbitration, and Visa allocation.

## PRIMITIVE state machine statuses

The following table provides a brief explanation of PRIMITIVE state machine statuses. Each status also has a group status.

<HTMLBlock>
  {`
  <table border="1">
      <thead>
      <tr><th>Status/Group status</th><th > Description</th></tr>
      </thead>
      <tbody>
      <tr><td>PENDING<br>Group status: OPEN</td><td>Dispute created, but card network requires further information from issuer.</td></tr>
      <tr><td>OPENED<br>Group status: CARDNETWORK_CHARGEBACK</td><td> Dispute was opened with a case ID or claim ID.</td></tr>
      <tr><td>CANCELED<br>Group status: DENIED</td><td> Issuer did not proceed with creating the chargeback.</td></tr>
      <tr><td>FAILED<br>Group status: FAILED</td><td> Issuer must provide correct information</td></tr>
      <tr><td>EXPIRED<br>Group status: LOSS</td><td> Issuer did not meet the deadline and has, therefore, lost the dispute.</td></tr>
      
      <tr><td>CHARGEBACK_CREATED<br>Group status: CARDNETWORK_CHARGEBACK</td><td> Dispute initiated with success. Issuer can open a chargeback with forms and documents.</td></tr>
      <tr><td>CHARGEBACK_ACCEPTED<br>Group status: WON</td><td> Acquirer gives up the chargeback. Specific for Mastercard disputes.</td></tr>
      <tr><td>CHARGEBACK_REJECTED<br>Group status: LOSS</td><td> Card network rejected chargeback creation.</td></tr>

      <tr><td>CHARGEBACK_CLOSED<br>Group status: LOSS</td><td> Issuer wants to accept second presentment or give up the chargeback.</td></tr>
      <tr><td>CHARGEBACK_REJECT_COLLABORATION<br>Group status: WON</td><td>Acquirer gives up the chargeback. Specific for Disputes with Mastercard cardnetwork</td></tr>
      <tr><td>CHARGEBACK_PENDING_DOCUMENTATION<br>Group status: CARDNETWORK_CHARGEBACK</td><td>Issuer pending attach documentation.</td></tr>

      <tr><td>SECOND_PRESENTMENT<br>Group status: CARDNETWORK_SECOND_PRESENTMENT</td><td> Acquirer didn't accept the chargeback and wants to prove why. Issuer receives the document from acquirer with the amount and the new reason code.</td></tr>
      
      <tr><td>FAILED_PRE_ARBITRATION<br>Group status: FAILED</td><td> The pre-arbitration, for some reason, could not be created. </td></tr>
      <tr><td>FAILED_DOCUMENTATION<br>Group status: FAILED</td><td> Card network considered the documentation invalid </td></tr>
      <tr><td>FILED_IN_ERROR<br>Group status: FAILED</td><td> The pre-arbitration, for some reason, could not be created. </td></tr>
      <tr><td>PRE_ARBITRATION_OPENED<br>Group status: CARDNETWORK_PREARBITRATION</td><td> Issuer didn't accept the second presentment and wants to proceed with the dispute. Issuer can upload new documents, a new amount (partial), and new information text.</td></tr>
      <tr><td>PRE_ARBITRATION_ACCEPTED<br>Group status: WON</td><td> Acquirer accepts dispute loss.</td></tr>
      <tr><td>PRE_ARBITRATION_DECLINED<br>Group status: LOSS</td><td> Acquirer didn't accept the dispute loss. Issuer receives the documents that the acquirer uses to decline.</td></tr>
      <tr><td>ISSUER_LOSS<br>Group status: LOSS</td><td> Issuer accepts dispute loss after a failed or chargeback rejected status.</td></tr>
      
      <tr><td>FAILED_ON_CLOSE<br>Group status: FAILED</td><td>The chargeback could not, for some reason, be closed.</td></tr>
      
      <tr><td>PRE_ARB_ALLOCATION_OPENED<br>Group status: CARDNETWORK_PREARBITRATION</td><td> Acquirer initiated a pre-arbitration. Visa allocation workflow.</td></tr>
      <tr><td>PRE_ARB_ALLOCATION_ACCEPTED<br>Group status: LOSS</td><td> Issuer didn't accept dispute loss. Visa allocation workflow.</td></tr>
      <tr><td>PRE_ARB_ALLOCATION_DECLINED<br>Group status: WON</td><td> Issuer didn't accept acquirer claims. Visa allocation workflow.</td></tr>
      <tr><td>PRE_ARB_ ALLOCATION_RECALLED<br>Group status: WON</td><td> Acquirer accepts the loss after opening a pre-arbitration. Visa allocation workflow.</td></tr>
      <tr><td>FAILED_ACCEPT_PRE_ARB<br>Group status: FAILED</td><td> Network couldn’t accept pre-arbitration. Visa allocation workflow.</td></tr>
      <tr><td>FAILED_DECLINE_PRE_ARB<br>Group status: FAILED</td><td> Network couldn’t decline pre-arbitration. Visa allocation workflow.</td></tr>
      </tbody>
      </table>
  `}
</HTMLBlock>

## Events and statuses

The PRIMITIVE state machine works through *events* and *statuses*. An event occurs and transitions the dispute status to a new status. For example, an `ISSSUER_LOSS` event occurs, meaning the issuer accepts the loss, moves the dispute status to `ISSUER_LOSS` and the group status to `LOSS`.

Events can come from the network or from the [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) endpoint.

During the dispute status process, you are notified of dispute status updates  via the [dispute status change event](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1). The `dispute_status` object contains fields indicating the status (`description`), the state machine (`type`) and dispute group status.

The following table shows how events transition a dispute status in the PRIMITIVE state machine:

<HTMLBlock>
  {`
  <table border="0" style="background-color:#FFFFE0;">

  <thead>
  <tr><th>Dispute status</th><th> Event</th><th> New status</th></tr>
  </thead>
  <tbody>
  <tr style="background-color:#FED8B1;font-weight:bold" ><td>PENDING</td><td>OPEN</td><td>OPENED</td></tr>
  <tr><td colspan="3">If the dispute was <a href="https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes">created</a> and has a PENDING status, the issuer must send the OPEN event (via <a href="https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event">Update dispute status</a>) to move the dispute to OPENED. When that happens, Pismo sends the request to create a chargeback to the card network.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold" ><td>PENDING</td><td>CANCEL</td><td>CANCELED</tr>
  <tr><td colspan="3">The dispute was opened, but then cancelled</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>OPENED </td><td>ISSUER_WORKED</td><td>CHARGEBACK_CREATED</td></tr>
  <tr><td colspan="3">The card network has responded to Pismo with an ISSUER_WORKED event, meaning it has accepted and opened the chargeback dispute. Pismo then transitions the dispute status to CHARGEBACK_CREATED.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>OPENED</td><td>FAILED_ON_CREATION</td><td>FAILED</td></tr>
  <tr><td colspan="3">The network failed to create the dispute for some reason.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>FAILED</td><td>RESEND</td><td>OPENED</td></tr>
  <tr><td colspan="3">The dispute failed to be created, but has been reopened with possible changes or additional information.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>FAILED</td><td>ISSUER_LOSS</td><td>ISSUER_LOSS</td></tr>
  <tr><td colspan="3">The dispute failed to be created, and the issuer accepts the loss.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>CANCELED</td><td>REOPEN</td><td>PENDING</td></tr>
  <tr><td colspan="3">The dispute was cancelled, but has been reopened and is now in a PENDING state.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>CHARGEBACK_REJECTED</td><td>ISSUER_LOSS</td><td>ISSUER_LOSS</td></tr>
  <tr><td colspan="3">The network has rejected the chargeback - issuer loss.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>CHARGEBACK_REJECTED</td><td>RESEND</td><td>OPENED</td></tr>
  <tr><td colspan="3">If the chargeback is rejected, you can use the Update dispute status endpoint to send the RESEND event after, for example, uploading additional evidence files. Pismo tries again to create the chargeback with the network and transitions the status to OPENED.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>CHARGEBACK_CREATED</td><td>REJECTS</td><td>CHARGEBACK_REJECTED</tr>
  <tr><td colspan="3">After a chargeback is created, the card network can reject the chargeback (check Mastercard and VISA rejection rules) and Pismo transitions the status to CHARGEBACK_REJECTED. If you still want to pursue this dispute, you will need to change the dispute status to RESEND.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>CHARGEBACK_CREATED</td><td>FAILED_ON_CLOSE</td><td>FAILED_ON_CLOSE</td></tr>
  <tr><td colspan="3">The chargeback failed to close.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>CHARGEBACK_CREATED</td><td>CLOSED_PROCESSED</td><td>CHARGEBACK_CLOSED</td></tr>
  <tr><td colspan="3">Chargeback processing closed, issuer loss.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>CHARGEBACK_CREATED</td><td>CLOSED</td><td>CHARGEBACK_ACCEPTED</td></tr>
  <tr><td colspan="3">If a chargeback is created and the acquirer doesn't contest the dispute and accepts the chargeback, the network sends the CLOSED event to Pismo, who then transitions the status to CHARGEBACK_ACCEPTED.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>CHARGEBACK_CREATED</td><td>REJECTS_5000_5001</td><td>CHARGEBACK_ACCEPTED</td></tr>
  <tr><td colspan="3">Mastercard sends this event in a specific case. The issuer is refunded the dispute loss.</td></tr>

  <tr style="background-color:#FED8B1;font-weight:bold"><td>CHARGEBACK_CREATED</td><td>ISSUER_REPRESENTMENT_UNWORKED</td><td>SECOND_PRESENTMENT</td></tr>
  <tr><td colspan="3">If the chargeback is created and the acquirer decides to contest the dispute, then the card network sends Pismo an ISSUER_REPRESENTMENT_UNWORKED event and Pismo transitions the status to SECOND_PRESENTMENT.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>FAILED_ON_CLOSE</td><td>CLOSED_PROCESSED</td><td>CHARGEBACK_CLOSED</td></tr>
  <tr><td colspan="3">Dispute closed.</td></tr>

  <tr style="background-color:#FED8B1;font-weight:bold"><td>SECOND_PRESENTMENT</td><td>CLOSED_PROCESSED</td><td>CHARGEBACK_CLOSED</td></tr>
  <tr><td colspan="3">Network has closed the dispute for some reason. </td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>SECOND_PRESENTMENT</td><td>FAILED_ON_CLOSE</td><td>FAILED_ON_CLOSE</td></tr>
  <tr><td colspan="3">Second presentment failed.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>SECOND_PRESENTMENT</td><td>EXPIRE</td><td>EXPIRED</td></tr>
  <tr><td colspan="3">Issuer missed deadline.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>SECOND_PRESENTMENT</td><td>SEND_PRE_ARBITRATION</td><td>PRE_ARBITRATION_OPENED</td></tr>
  <tr><td colspan="3">After a dispute status changes to SECOND_PRESENTMENT, the issuer can use the SEND_PRE_ARBITRATION event in Update dispute status to initiate a pre-arbitration. This endpoint has a number of fields specifically for pre-arbitration.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>SECOND_PRESENTMENT</td><td>CLOSED</td><td>CHARGEBACK_ACCEPTED</td></tr>
  <tr><td colspan="3">If  the acquirer doesn't contest the dispute and accepts the chargeback, the network sends the CLOSED event to Pismo, who then transitions the status to CHARGEBACK_ACCEPTED</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>PRE_ARBITRATION_OPENED</td><td>FAILED_ON_CREATION</td><td>FAILED_PRE_ARBITRATION</td></tr>
  <tr><td colspan="3">Network failed to create the pre-arbitration</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>PRE_ARBITRATION_OPENED</td><td>ACCEPTED_PRE_ARBITRATION</td><td>PRE_ARBITRATION_ACCEPTED</td></tr>
  <tr><td colspan="3">Network has accepted the pre-arbitration</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>PRE_ARBITRATION_OPENED</td><td>REJECT_PRE_ARBITRATION</td><td>PRE_ARBITRATION_DECLINED</td></tr>
  <tr><td colspan="3">Network rejected pre-arbitration</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>PRE_ARBITRATION_OPENED</td><td>REJECTS</td><td>PRE_ARBITRATION_REJECTED</td></tr>
  <tr><td colspan="3">Network rejects pre-arbitration</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>PRE_ARBITRATION_OPENED</td><td>RECALL_PRE_ARBITRATION</td><td>PRE_ARBITRATION_RECALL</td></tr>
  <tr><td colspan="3">Arbitration recalled</td></tr>


  <tr style="background-color:#FED8B1;font-weight:bold"><td>FAILED_PRE_ARBITRATION</td><td>SEND_PRE_ARBITRATION</td><td>PRE_ARBITRATION_OPENED</td></tr>
  <tr><td colspan="3">Pre-arbitration reopened after failure.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>FAILED_PRE_ARBITRATION</td><td>CLOSED_PROCESSED</td><td>CHARGEBACK_CLOSED</td></tr>
  <tr><td colspan="3">Network pre-arbitration failure, issuer loss.</td></tr>
  <tr style="background-color:#FED8B1;font-weight:bold"><td>FAILED_PRE_ARBITRATION</td><td>FAILED_ON_CLOSE</td><td>FAILED_ON_CLOSE</td></tr>
  <tr><td colspan="3">Network failure. Issuer loss</td></tr>


  <tr><td colspan="3" align="center"><h3><b>VISA Allocation Workflow</b></h3></td></tr>
  <tr style="background-color:LightBlue;font-weight:bold"><td>CHARGEBACK_CREATED</td><td>SEND_PRE_ARBITRATION</td><td>PRE_ARB_ALLOCATION_OPENED</td></tr>
  <tr><td colspan="3">In Visa’s allocation workflow, the acquirer sends a pre-arbitration instead of a second presentment. Once the card network system receives this, the dispute status changes automatically to PRE_ARB_ALLOCATION_OPENED. When this happens, the issuer must respond, either accepting the dispute loss or reject it.</td></tr>
  <tr style="background-color:LightBlue;font-weight:bold"><td>PRE_ARB_ALLOCATION_OPENED</td><td>FAILED_ON_CREATION</td><td>FAILED_PRE_ARBITRATION</td></tr>
  <tr><td colspan="3">Network failure.</td></tr>

  <tr style="background-color:LightBlue;font-weight:bold"><td>PRE_ARB_ALLOCATION_OPENED</td><td>ACCEPT_PRE_ARBITRATION</td><td>PRE_ARB_ALLOCATION_ACCEPTED</td></tr>
  <tr><td colspan="3">If issuer wants to accept the pre-arbitration allocation they can send the event ACCEPT_PRE_ARBITRATION. This close the dispute permanently and they accept the loss. VISA allocation workflow</td></tr>
  <tr style="background-color:LightBlue;font-weight:bold"><td>PRE_ARB_ALLOCATION_OPENED</td><td>DECLINE_PRE_ARBITRATION</td><td>PRE_ARB_ALLOCATION_DECLINED</td></tr>
  <tr><td colspan="3">If the acquirer wants to proceed with the dispute they can send the event   DECLINE_PRE_ARBITRATION. This requires the issuer to attach more pre-arbitratipn information. The new document can be uploaded using the Create dispute endpoint but, this time, the category field must have the pre-arbitration information. VISA allocation workflow.</td></tr>
  <tr style="background-color:LightBlue;font-weight:bold"><td>PRE_ARB_ALLOCATION_OPENED</td><td>RECALL_PRE_ARBITRATION</td><td>PRE_ARB_ALLOCATION_RECALLED</td></tr>
  <tr><td colspan="3">Network failure. VISA allocation workflow</td></tr>

  <tr style="background-color:LightBlue;font-weight:bold"><td>FAILED_PRE_ARBITRATION</td><td>ACCEPT_PRE_ARBITRATION</td><td>PRE_ARB_ALLOCATION_ACCEPTED</td></tr>
  <tr><td colspan="3"> After initial failure, network has accepted the pre-arbitration. VISA allocation workflow</td></tr>
  <tr style="background-color:LightBlue;font-weight:bold"><td>FAILED_PRE_ARBITRATION</td><td>CLOSED_PROCESSED</td><td>CHARGEBACK_CLOSED</td></tr>
  <tr><td colspan="3"> Arbitration failed. VISA allocation workflow</td></tr>
  <tr style="background-color:LightBlue;font-weight:bold"><td>FAILED_PRE_ARBITRATION</td><td>FAILED_ON_CLOSE</td><td>FAILED_ON_CLOSE</td></tr>
  <tr><td colspan="3">Aribitration faied,  VISA allocation workflow</td></tr>

  <tr style="background-color:LightBlue;font-weight:bold"><td>PRE_ARB_ALLOCATION_DECLINED</td><td>FAILED_ON_CREATION</td><td>FAILED_DECLINE_PRE_ARB</td></tr>
  <tr><td colspan="3">Network failure. VISA allocation workflow</td></tr>
  <tr style="background-color:LightBlue;font-weight:bold"><td>PRE_ARB_ALLOCATION_ACCEPTED</td><td>FAILED_ON_CREATION</td><td>FAILED_ACCEPT_PRE_ARB</td></tr>
  <tr><td colspan="3">Network failure. VISA allocation workflow</td></tr>


  <tr style="background-color:LightBlue;font-weight:bold"><td>FAILED_DECLINE_PRE_ARB</td><td>DECLINE_PRE_ARBITRATION</td><td>PRE_ARB_ALLOCATION_DECLINED</td></tr>
  <tr><td colspan="3">Network declines pre-arbitration. VISA allocation workflow</td></tr>
  <tr style="background-color:LightBlue;font-weight:bold"><td>FAILED_ACCEPT_PRE_ARB</td><td>ACCEPT_PRE_ARBITRATION</td><td>PRE_ARB_ALLOCATION_ACCEPTED</td></tr>
  <tr><td colspan="3">Issuer didn't accept dispute loss. VISA allocation workflow.</td></tr>
  </tbody>
  </table>
  `}
</HTMLBlock>

## Migration statuses and events

Pismo can migrate a dispute from VISA and Mastercard onto the Pismo platform where the customer can continue with the dispute.

| Dispute status | Event                                | New status                     |
| :------------- | :----------------------------------- | :----------------------------- |
| MIGRATION      | FAILED\_ON\_CREATION                 | FAILED\_MIGRATION              |
| MIGRATION      | ISSUER\_REPRESENTMENT\_UNWORKED      | SECOND\_PRESENTMENT            |
| MIGRATION      | ISSUER\_WORKED                       | CHARGEBACK\_CREATED            |
| MIGRATION      | SEND\_PRE\_ARBITRATION\_ALLOCATION   | PRE\_ARB\_ALLOCATION\_OPENED   |
| MIGRATION      | SEND\_PRE\_ARBITRATION               | PRE\_ARBITRATION\_OPENED       |
| MIGRATION      | UNASSIGNED                           | UNASSIGNED                     |
| MIGRATION      | ACCEPTED\_PRE\_ARBITRATION           | PRE\_ARBITRATION\_ACCEPTED     |
| MIGRATION      | REJECT\_PRE\_ARBITRATION             | PRE\_ARBITRATION\_DECLINED     |
| MIGRATION      | PRE\_ARBITRATION\_REJECTS            | PRE\_ARBITRATION\_REJECTED     |
| MIGRATION      | RECALL\_PRE\_ARBITRATION             | PRE\_ARBITRATION\_RECALL       |
| MIGRATION      | ACCEPT\_PRE\_ARBITRATION             | PRE\_ARB\_ALLOCATION\_ACCEPTED |
| MIGRATION      | DECLINE\_PRE\_ARBITRATION            | PRE\_ARB\_ALLOCATION\_DECLINED |
| MIGRATION      | RECALL\_ALLOCATION\_PRE\_ARBITRATION | PRE\_ARB\_ALLOCATION\_RECALLED |
| MIGRATION      | EXPIRE                               | EXPIRED                        |
| MIGRATION      | CLOSED                               | CHARGEBACK\_ACCEPTED           |
| MIGRATION      | REJECTS                              | CHARGEBACK\_REJECTED           |
| MIGRATION      | REJECTS\_5000\_5001                  | CHARGEBACK\_ACCEPTED           |
| MIGRATION      | CLOSED\_PROCESSED                    | CHARGEBACK\_CLOSE              |

## State machine API endpoints

* [Get possible dispute states](https://developers.pismo.io/pismo-docs/reference/get-v1-disputes-disputeid-possible-status) - Get possible dispute statuses for a dispute.
* [Get possible states](https://developers.pismo.io/pismo-docs/reference/get-v1-disputes-possible-status) -  Get possible dispute statuses given a current status and event

## PRIMITIVE state machine diagram

<Image align="center" alt="Disputes state machine graphic" src="https://files.readme.io/0aa08ca-PRIMITIVE_State_Machine_-_Disputes.svg" />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/disputes/{disputeId}/event` | `post-v1-disputes-disputeId-event` | Update dispute status | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01 |
| `GET /v1/disputes/{disputeId}/possible-status` | `get-v1-disputes-disputeId-possible-status` | Get possible dispute states | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--state-check |
| `GET /v1/disputes/possible-status` | `get-v1-disputes-possible-status` | Get possible states | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--state-check |

### Operation essentials

- **`POST /v1/disputes/{disputeId}/event`** (`post-v1-disputes-disputeId-event`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `event`, `reason`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `disputes-dispute-installment-status-change-1`.
- **`GET /v1/disputes/{disputeId}/possible-status`** (`get-v1-disputes-disputeId-possible-status`): security `BearerAuth`; required parameters `disputeId` (path); required body fields none declared; response statuses 200; error codes in examples none; events none listed.
- **`GET /v1/disputes/possible-status`** (`get-v1-disputes-possible-status`): security `BearerAuth`; required parameters `type` (header), `source` (header); required body fields none declared; response statuses 200, 400, 401, 500; error codes in examples none; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-disputes-disputeId-event` | `disputes-dispute-installment-status-change-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `disputes-dispute-installment-status-change-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1 | 4 | KU-EVT-catalogue-disputes |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/disputes-state-machine.md`: updatedAt 2026-06-11T19:00:30.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/disputes-state-machine.md` | whole document | https://developers.pismo.io/pismo-docs/docs/disputes-state-machine | `01ea668d76d7d083…` | 2026-06-11T19:00:30.000Z |

## Related knowledge units

- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-API-card-issuing-disputes--state-check` — API reference: Card issuing - Disputes — State check
- `KU-EVT-catalogue-disputes` — Event catalogue: disputes
