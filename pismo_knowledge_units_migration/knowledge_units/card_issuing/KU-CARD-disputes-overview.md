---
ku_id: KU-CARD-disputes-overview
title: Disputes overview
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/disputes-overview.md
  sha256: 323e45b68b62e4a63c38d21c6db5c377fb711cf9369b3bd56b4a4e8672ab9fb2
  url: https://developers.pismo.io/pismo-docs/docs/disputes-overview
  role: primary_guide
  updated_at: '2026-07-16T21:51:51.000Z'
operations:
- create-fee-v2
- get-v1-disputes-disputeId-possible-status
- get-v1-fee
- get-v1-fee-disputeFeeId
- post-migration-installment
- post-migration-with-auth
- post-v1-disputes-disputeId-event
- post-v1-disputes-disputeId-file
- post-v1-disputes-disputeId-forms
- post-v1-disputes-disputeId-installment
- post-v1-disputes-fraud-report
- post-v1-fee
- post-v1-networkauthorization-disputes
- put-update-migration
- put-v1-disputes-disputeId
- put-v1-fee-disputeFeeId
related_kus:
- KU-API-card-issuing-disputes--disputes-part-01
- KU-API-card-issuing-disputes--evidence-files
- KU-API-card-issuing-disputes--fees
- KU-API-card-issuing-disputes--fees-v2
- KU-API-card-issuing-disputes--installments
- KU-API-card-issuing-disputes--migration
- KU-API-card-issuing-disputes--state-check
- KU-API-card-issuing-disputes--supporting-forms
- KU-CARD-disputes-setup-and-on-us
- KU-CARD-disputes-state-machine
- KU-CARD-visa-colloboration-questionaire-part-01
- KU-CARD-visa-colloboration-questionaire-part-02
- KU-CARD-visa-colloboration-questionaire-part-03
- KU-CARD-visa-colloboration-questionaire-part-04
- KU-CARD-visa-colloboration-questionaire-part-05
- KU-CARD-visa-colloboration-questionaire-part-06
- KU-CARD-visa-colloboration-questionaire-part-07
- KU-CORE-transactions-overview
- KU-EVT-catalogue-disputes
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Disputes overview

**KU ID:** `KU-CARD-disputes-overview` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/disputes-overview.md`:

> A dispute happens when a cardholder calls the bank or card issuer to report an unrecognized or suspicious [transaction](https://developers.pismo.io/pismo-docs/docs/transactions-overview), and requests a cancellation or refund. The following table shows different types of disputes.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/disputes-overview.md`: Disputes overview; Disputes glossary; Chargeback lifecycle; Opening a dispute with Pismo versus the network; How Pismo handles disputes; Dispute cycle stages covered; Pismo's dispute API; Using Pismo API endpoints to resolve a dispute; Step 1 - Create dispute; Step 2 - Upload dispute forms; Step 3 - Multiple installments; Step 4 - Upload evidence; Step 5 - Initiate dispute process; Step 1 - Create dispute; Step 2 - Multiple installments; Step 3 - Upload evidence and dispute forms; Step 4 - Initiate dispute process; Step 1 - Create dispute; Step 2 - Multiple installments; Step 3 - Upload evidence via ELO portal; Step 4 - Initiate dispute process; Processing codes and transaction types; Dispute migration; Dispute migration endpoints; Dispute fees; Dispute fee scenarios; Dispute fee terms; Dispute fee process; &#x20;Setting up TQR4 and TC33; Automated dispute installment control; Dispute fee API endpoints; V1 endpoints; V2 endpoints

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 16 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/disputes-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/disputes-overview · updatedAt: 2026-07-16T21:51:51.000Z

<!-- source:begin path=docs/card-issuing/disputes-overview.md part=0-end -->

# Disputes overview

A dispute happens when a cardholder calls the bank or card issuer to report an unrecognized or suspicious [transaction](https://developers.pismo.io/pismo-docs/docs/transactions-overview), and requests a cancellation or refund. The following table shows different types of disputes.

| Dispute              | Description                                                                                                                                                                                                                                            |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Merchant error**   | When a seller charges a different price for the product/service or charges twice for the same product/service by mistake. It's also when the seller doesn't confirm a refund.                                                                          |
| **Identity fraud**   | When a dispute is the result of a stolen identity, stolen data, or a lost or stolen card. Also known as ***true fraud*** .                                                                                                                             |
| **Chargeback fraud** | When the cardholder requests a refund because they’re unsatisfied with purchased goods or services by calling the bank or the network responsible for the transaction, instead of contacting the original seller. Also known as ***friendly fraud*** . |

# Disputes glossary

| Term                                        | Description                                                                                                                                                                                                                                                                       |
| :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Dispute**                                 | The process between an acquirer, an issuer, and the card network that takes place when the cardholder or the issuer initiates a chargeback.                                                                                                                                       |
| **First presentment**                       | The initial submission of a disputed transaction.                                                                                                                                                                                                                                 |
| **Chargeback**                              | When a  transaction is contested for reasons of fraud, disagreement, processing error, or authorization.                                                                                                                                                                          |
| **Second presentment** or **representment** | When the acquirer does not agree with the chargeback and its reason and wants to provide evidence that the transaction (the first presentment) is still valid.                                                                                                                    |
| **Pre-arbitration**                         | The step before arbitration that happens when the issuer and cardholder do not agree with the second presentment and want to proceed with the dispute.                                                                                                                            |
| **Arbitration**                             | When the card network has been asked to mediate a dispute. The card networks charge a hefty fee for this, so, in many cases, the transaction is not significant or expensive enough to make this worthwhile for the issuer to contest.                                            |
| **Visa Allocation**                         | Allocation is a process for Visa disputes that attempts to weed out some illegitimate chargebacks and shorten the time affected disputes take to resolve. Visa uses internal data and processes to automatically block disputes that don't meet Visa's requirements for validity. |
| **Visa Collaboration**                      | Collaboration is the new name for Visa's old chargeback process, where each party has several chances to investigate and submit evidence in order to determine whether a chargeback is legitimate                                                                                 |

# Chargeback lifecycle

When a cardholder has a dispute, they're asking for a chargeback to their card. The following shows how a chargeback returns to the cardholder, if they win the dispute.

![Illustration of the Chargeback lifecycle.](https://files.readme.io/daa4495-diagram-ChargebackLifeCycle2x.png "diagram-ChargebackLifeCycle@2x.png")  **The chargeback lifecycle when a cardholder wins a dispute**

❶ The cardholder disputes a purchase and notifies the card issuer.\
❷ The card issuer reviews the dispute and sends it to the card network.\
❸ The card network reviews the dispute and sends it to the card acquirer.\
❹ The card acquirer reviews the dispute and notifies the merchant.\
❺ The bank reviews the dispute.\
❻ The card acquirer forwards the dispute to the card network.\
❼ The card network resubmits the dispute to the issuer.\
❽ After reviewing the dispute, the issuer decides which side wins. If no sides agree, then they go through arbitration.\
❾ If the cardholder wins the dispute, then they get a chargeback.

# Opening a dispute with Pismo versus the network

When a dispute is opened directly with the card network (e.g., Visa, Mastercard), without going through Pismo APIs, this dispute exists only with the card network. Therefore, when making any type of query in our APIs, there will be no information about it. In reconciliation reports (TC33 and TQR4), this dispute will appear as usual – since these reports are extracted directly from the card network, parsed and sent to the Issuer.

# How Pismo handles disputes

Pismo handles disputes in the following order:

1. The cardholder disputes a transaction with the card issuer.
2. The issuer makes [dispute API calls](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes) to the Pismo platform.
3. Pismo opens dispute with the card network.
4. Once there's a response from the network, Pismo informs the issuer and cardholder about the dispute status. To see how to get the status on a dispute, go to [Get possible dispute states](https://developers.pismo.io/pismo-docs/reference/get-v1-disputes-disputeid-possible-status).
5. If the issuer loses the dispute, they can either accept the loss or file a case with the card network.

## Dispute cycle stages covered

Pismo covers the stages of chargeback creation, second presentation, and pre-arbitration. The following stages are not covered: pre-compliance, compliance, and arbitration.

## Pismo's dispute API

You can use the Pismo platform to provide the context and reasons for a dispute. Pismo endpoints allow you to do the following after you [Create a dispute](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes)

* [Create dispute form](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-forms)—Create a dispute form to be sent to the network
* [Create fraud report ](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-fraud-report)—Create a fraud report for cases of fraud. For information on filing a fraud report for Visa, see [Visa collaboration and allocation questionnaires](https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire).
* [Upload evidence file](post-v1-disputes-disputeid-file)—Upload a supporting evidence file
* [Create dispute installment](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-installment)—Dispute an installment for a transaction composed of multiple installments.

# Using Pismo API endpoints to resolve a dispute

Before you begin, make sure you are [set up with disputes access](https://developers.pismo.io/pismo-docs/docs/set-up-disputes).

> 📘 Disputes state machine
>
> Pismo provides a [state machine](https://developers.pismo.io/pismo-docs/docs/disputes-state-machine) as a framework to help guide clients through the dispute process.

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>Opening a dispute with Visa</summary>

  ### Step 1 - Create dispute

  Call [Create dispute](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes) with Visa required data:

  * `modality` = Enter category, aka *Reason*: `10` (fraud - card not present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).
  * `dispute_due_to` = Pick best enum reason for dispute. **Required**  if `modality` = `12` or `13`. Not necessary for  `10` or  `11`.
  * `first_installment_amount` - Enter value for this field if the dispute has more than one installment
  * `is_partial` - Set to `true` if the dispute is for a partial transaction amount and not the full amount.
  * `comment` - Add explanation if dispute is partial and not full

  This endpoint returns a dispute ID you need for all other calls related to this dispute.

  ### Step 2 - Upload dispute forms

  Call [Create dispute form](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-forms) and fill out and upload a collaboration form  (`collaborationQuestionnaire`) if Reason `12` or `13`or the allocation questionnaire (`allocationQuestionnaire`) if Reason `11`.

  ### Step 3 - Multiple installments

  Call [Create dispute installment](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-installment) for each subsequent installment if you have not opted in to [automated dispute installment control](https://developers.pismo.io/pismo-docs/docs/disputes-overview#automated-dispute-installment-control) .

  **Note**: To disable automated dispute installment control for this dispute call [Update dispute](https://developers.pismo.io/pismo-docs/reference/put-v1-disputes-disputeid) with `stop_automated_installment` = `true`.

  ### Step 4 - Upload evidence

  Call [Upload evidence file](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-file) to upload any files with information pertaining to this dispute.

  ### Step 5 - Initiate dispute process

  Call [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event)  with `event` = `OPEN` along with other required fields to begin the dispute process with Visa.
</details>

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>Opening a dispute with Mastercard</summary>

  ### Step 1 - Create dispute

  Call [Create dispute](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes) with Mastercard required data:

  * `modality` = Reason code (example: `4853` - cardholder dispute). For more information, refer to this <a href="https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide" target="_blank">quick reference</a> for chargeback codes or consult the <a href="https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf" target="_blank">Mastercard chargeback guide</a>.
  * `first_installment_amount` - Enter value for this field if the dispute has more than one installment

  This endpoint returns a dispute ID you need for all other calls related to this dispute.

  ### Step 2 - Multiple installments

  Call [Create dispute installment](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-installment) for each subsequent installment if you have not opted in to [automated dispute installment control](https://developers.pismo.io/pismo-docs/docs/disputes-overview#automated-dispute-installment-control) .

  **Note**: To disable automated dispute installment control for this dispute call [Update dispute](https://developers.pismo.io/pismo-docs/reference/put-v1-disputes-disputeid) with `stop_automated_installment` = `true`.

  ### Step 3 - Upload evidence and dispute forms

  Call [Create dispute form](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-forms) and fill out and upload a EBDF form. However, If there are files to be uploaded, the client should **only use** the  [Upload evidence file](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-file) endpoint. Mastercard does not allow you to send two evidence files on the same dispute (EBDF and evidence file).

  ### Step 4 - Initiate dispute process

  Call [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event)  with `event` = `OPEN` along with other required fields to begin the dispute process with Mastercard.
</details>

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>Opening a dispute with ELO</summary>

  ### Step 1 - Create dispute

  Call [Create dispute](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes) with ELO required data:

  * `modality` = Enter dispute code (example: `72` ELO - denied authorization).
  * `comment`- Same as ELO field 32 which is a custom message field that issuing banks can include on card statement or transacton descriptions.
  * `document_indicator` - If there is any evidence to be uploaded, set this field to `true` so ELO will allow you to attach documents for this dispute through the ELO portal.
  * `first_installment_amount` - Enter value for this field if the dispute has more than one installment

  This endpoint returns a dispute ID you need for all other calls related to this dispute.

  ### Step 2 - Multiple installments

  Call [Create dispute installment](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-installment) for each subsequent installment if you have not opted in to [automated dispute installment control](https://developers.pismo.io/pismo-docs/docs/disputes-overview#automated-dispute-installment-control) .

  **Note**: To disable automated dispute installment control for this dispute call [Update dispute](https://developers.pismo.io/pismo-docs/reference/put-v1-disputes-disputeid) with `stop_automated_installment` = `true`.

  `document_indicator` - If there is any evidence to be uploaded for this installment, set this field to `true` so ELO will allow you to attach documents for this dispute through the ELO portal.

  ### Step 3 - Upload evidence via ELO portal

  Upload any evidence files for this dispute via the ELO portal.

  ### Step 4 - Initiate dispute process

  Call [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event)  with `event` = `OPEN` along with other required fields to begin the dispute process with ELO.
</details>

> 📘 Dispute status change notification
>
> You are notified when there's a dispute status change if you have signed up to receive [event notifications](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview), either in real-time or via files. The status event is called [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1). This event occurs if the [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) endpoint is called or if the status changes through other means like network processing. If you submit files with unsupported formats or disregard any card network rule, the card network will reject the dispute. Pismo then notifies you with a `FAILED_ON_CREATION` [status event](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1). If this occurs, update the dispute to correct the data and resend your case by [ updating the dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) to `RESEND`.

If an acquirer’s response doesn’t end the dispute, check if it’s compliant with the card network's rules.

Assess the time, operational cost, and disputed amount to determine if going through pre-arbitration or arbitration is appropriate. If not, call  [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) to change the dispute status to `ISSUER_LOSS` and close the dispute.

If the acquirer accepts the dispute and its corresponding chargebacks, then you won the dispute. When Pismo notices the status change at the card network, it changes the dispute status to `ACCEPTED`.

# Processing codes and transaction types

Issuers should configure their processing codes and transaction types according to their own rules as the configuration can vary from issuer to issuer. Pismo enables each client to have  flexibility in terms of configuration.

# Dispute migration

Pismo can migrate an already created Mastercard or Visa dispute to the Pismo platform with a case number (Visa) or a claim ID (Mastercard) and allow a customer to continue the chargeback process.

## Dispute migration endpoints

* [Create dispute migration](https://developers.pismo.io/pismo-docs/reference/post-migration-with-auth)
* [Create installment migration](https://developers.pismo.io/pismo-docs/reference/post-migration-installment)
* [Update dispute migration](https://developers.pismo.io/pismo-docs/reference/put-update-migration)

# Dispute fees

A dispute fee is a way for an acquirer and issuer to exchange money outside the normal chargeback process. Typically, this means reversing a settled chargeback, but not always.

**Note**: Currently, Pismo only works with **Mastercard** on processing dispute fees.

## Dispute fee scenarios

**Issuer realizes chargeback is invalid**

An issuer creates a chargeback which the acquirer accepts and pays. Later, the issuer notices that the chargeback is invalid because, for example, the cardholder recognizes the transaction now or because the cardholder reached an agreement with the merchant. At this point, the issuer must give back the disputed amount. This can be done through Pismo's dispute fee process.

**Acquirer realizes chargeback is invalid**

An acquirer realizes a chargeback was invalid and initiates the dispute fee process with the issuer through Pismo.

**Deadline for chargeback missed**

An issuer misses the deadline for opening a  chargeback. However, the cardholder is still complaining about the transaction. Through email, phone, or other means, the issuer contacts the acquirer and they agree that the acquirer should send a credit for the issuer even though there is no chargeback.  In this case, the dispute fee process can take place without a chargeback having occurred.

## Dispute fee terms

* **Fee collection** - How Mastercard refers to the dispute fee.
* **Sender** - The party sending the amount (credit or debit).
* **Receiver** - The party receiving the amount (credit or debit).
* **TQR4** - The TQR4 file is generated as a result of Mastercard generating dispute items on behalf of the customer, as requested by the customer. Pismo receives this report, also known as a *reconciliation report*, and sends it to you, usually within two days after  a dispute fee is created.

## Dispute fee process

1. A dispute fee is [created](https://developers.pismo.io/pismo-docs/reference/post-v1-fee) and sent to Mastercard.
2. Mastercard processes the dispute fee and resolves or rejects it. Resolution includes crediting or debiting the sender and receiver accounts.
3. Mastercard sends a TQR4/TQR6 reconciliation report to Pismo who then sends it to the parties involved. Details about what's included in these reports can be found in the <a href="https://pismoassets.pismo.io/pismo-docs/mc_mstrcm_ug.pdf" target="_blank">Mastercom User Guide</a> on page 166.

### &#x20;Setting up TQR4 and TC33

To set up receipt of TQR4, you need to open a Settings ticket for the Disputes team indicating your interest. For TC33, you must also let your Client Success manager know of your interest.

## Automated dispute installment control

If an  issuer opens a dispute for a transaction that has more than one installment, with installments that can still be posted, the issuer will need to open a dispute for subsequent installments as well. With automated dispute installment control,  once you open a chargeback for the first installment, the same information can be used for subsequent transaction installments. You, as an issuer, only have to open a dispute for the first installment. The option for this is configured at the program level, see your Pismo representative if you would like to have this feature implemented for your program.

To stop automated dispute installment control for a specific dispute, call the [Update dispute](https://developers.pismo.io/pismo-docs/reference/put-v1-disputes-disputeid) endpoint and set the `stop_automated_installment` flag to `true`.

## Dispute fee API endpoints

There are two types of dispute fees - V1 and V2.  The main differences between fees V2 and V1 are:

* V1—Associated with the dispute/installment. Currently for Mastercard and Elo disputes.
* V2—Currently for Visa. Can only be created with transaction ID (Full balance), transaction information (Zero balance), card ID and customer ID, or NetworkCaseID (VisaCaseNumber).

### V1 endpoints

* [Create dispute fee](https://developers.pismo.io/pismo-docs/reference/post-v1-fee)—Create a dispute fee with Mastercard or ELO. This generates a [Dispute fee status created](https://developers.pismo.io/events/docs/disputes-dispute-fee-events-1) event.
* [Get dispute fee](https://developers.pismo.io/pismo-docs/reference/get-v1-fee-disputefeeid)—The get and list endpoints return all the same information you can find in the TQR4 report plus the `message` field that describes the reason for creating the dispute fee.
* [List dispute fees](https://developers.pismo.io/pismo-docs/reference/get-v1-fee) —List Mastercard or Elo dispute fees.
* [Update dispute fee](https://developers.pismo.io/pismo-docs/reference/put-v1-fee-disputefeeid)—Update a Mastercard of Elo dispute fee.

### V2 endpoints

* [Create fee V2](https://developers.pismo.io/pismo-docs/reference/create-fee-v2) - Create a dispute fee with Visa.
* [Get dispute fee](https://developers.pismo.io/pismo-docs/reference/get-v1-fee-disputefeeid)—Get Visa dispute fee.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/networkauthorization-disputes` | `post-v1-networkauthorization-disputes` | Create dispute | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01 |
| `GET /v1/disputes/{disputeId}/possible-status` | `get-v1-disputes-disputeId-possible-status` | Get possible dispute states | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--state-check |
| `POST /v1/disputes/{disputeId}/forms` | `post-v1-disputes-disputeId-forms` | Create dispute form | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--supporting-forms |
| `POST /v1/disputes/{disputeId}/fraud-report` | `post-v1-disputes-fraud-report` | Create dispute fraud report | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--supporting-forms |
| `POST /v1/disputes/{disputeId}/installment` | `post-v1-disputes-disputeId-installment` | Create dispute installment | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--installments |
| `PUT /v1/disputes/{disputeId}` | `put-v1-disputes-disputeId` | Update dispute | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01 |
| `POST /v1/disputes/{disputeId}/file` | `post-v1-disputes-disputeId-file` | Upload evidence file | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--evidence-files |
| `POST /v1/disputes/{disputeId}/event` | `post-v1-disputes-disputeId-event` | Update dispute status | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01 |
| `POST /v1/migration` | `post-migration-with-auth` | Create dispute migration | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--migration |
| `POST /v1/migration/{disputeId}/installment` | `post-migration-installment` | Create installment migration | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--migration |
| `PUT /v1/migration/{disputeId}` | `put-update-migration` | Update dispute migration | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--migration |
| `POST /v1/fee` | `post-v1-fee` | Create dispute fee | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--fees |
| `GET /v1/fee/{disputeFeeId}` | `get-v1-fee-disputeFeeId` | Get dispute fee | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--fees |
| `GET /v1/fee` | `get-v1-fee` | List dispute fees | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--fees |
| `PUT /v1/fee/{disputeFeeId}` | `put-v1-fee-disputeFeeId` | Update dispute fee | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--fees |
| `POST /v2/fee` | `create-fee-v2` | Create fee V2 | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--fees-v2 |

### Operation essentials

- **`POST /v1/networkauthorization-disputes`** (`post-v1-networkauthorization-disputes`): security `BearerAuth`; required parameters `Authorization` (header); required body fields `modality`, `disputed_amount`, `is_partial`, `network_brand_type`; response statuses 200, 400, 401, 422, 500; error codes in examples none; events `disputes-dispute-installment-creation-1`.
- **`GET /v1/disputes/{disputeId}/possible-status`** (`get-v1-disputes-disputeId-possible-status`): security `BearerAuth`; required parameters `disputeId` (path); required body fields none declared; response statuses 200; error codes in examples none; events none listed.
- **`POST /v1/disputes/{disputeId}/forms`** (`post-v1-disputes-disputeId-forms`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `form`; response statuses 200, 401, 404, 422, 500; error codes in examples none; events none listed.
- **`POST /v1/disputes/{disputeId}/fraud-report`** (`post-v1-disputes-fraud-report`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `report`; response statuses 200, 401, 404, 422, 500; error codes in examples none; events none listed.
- **`POST /v1/disputes/{disputeId}/installment`** (`post-v1-disputes-disputeId-installment`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `installment`, `arn`, `installment_disputed_amount`; response statuses 200, 400, 401, 404, 422, 500; error codes in examples none; events `disputes-dispute-installment-creation-1`.
- **`PUT /v1/disputes/{disputeId}`** (`put-v1-disputes-disputeId`): security `BearerAuth`; required parameters `disputeId` (path); required body fields none declared; response statuses 200, 400, 401, 404, 422, 500; error codes in examples none; events none listed.
- **`POST /v1/disputes/{disputeId}/file`** (`post-v1-disputes-disputeId-file`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `name`, `category`, `file`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /v1/disputes/{disputeId}/event`** (`post-v1-disputes-disputeId-event`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `event`, `reason`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `disputes-dispute-installment-status-change-1`.
- **`POST /v1/migration`** (`post-migration-with-auth`): security `BearerAuth`; required parameters none declared; required body fields `chargeback_id`, `claim_id`, `disputed_amount`, `network_brand_type`; response statuses 200, 400, 401, 422, 500; error codes in examples none; events `disputes-dispute-installment-creation-1`, `disputes-dispute-installment-status-change-1`.
- **`POST /v1/migration/{disputeId}/installment`** (`post-migration-installment`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `installment_number`, `claim_id`, `chargeback_id`, `installment_disputed_amount`; response statuses 200, 400, 401, 404, 422, 500; error codes in examples none; events `disputes-dispute-installment-creation-1`, `disputes-dispute-installment-status-change-1`.
- **`PUT /v1/migration/{disputeId}`** (`put-update-migration`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `claim_id`, `chargeback_id`, `disputed_amount`, `dispute_installment_id`, `network_brand_type`; response statuses 200, 400, 401, 422, 500; error codes in examples none; events none listed.
- **`POST /v1/fee`** (`post-v1-fee`): security `BearerAuth`; required parameters `Authorization` (header); required body fields `amount`, `card_id`, `credit_sender`, `credit_receiver`, `currency`, `destination_member`, `fee_date`, `network_brand_type`, `reason_code`; response statuses 200, 400, 401, 422, 500; error codes in examples none; events `disputes-dispute-fee-events-1`.
- **`GET /v1/fee/{disputeFeeId}`** (`get-v1-fee-disputeFeeId`): security `BearerAuth`; required parameters `disputeFeeId` (path); required body fields none declared; response statuses 200, 400, 401, 404, 422, 500; error codes in examples none; events none listed.
- **`GET /v1/fee`** (`get-v1-fee`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields none declared; response statuses 200, 400, 401, 404, 422, 500; error codes in examples none; events none listed.
- **`PUT /v1/fee/{disputeFeeId}`** (`put-v1-fee-disputeFeeId`): security `BearerAuth`; required parameters `disputeFeeId` (path); required body fields `amount`, `card_id`, `credit_sender`, `credit_receiver`, `currency`, `destination_member`, `fee_date`, `network_brand_type`, `reason_code`; response statuses 200, 400, 401, 404, 422, 500; error codes in examples none; events none listed.
- **`POST /v2/fee`** (`create-fee-v2`): security `BearerAuth`; required parameters `Authorization` (header); required body fields none declared; response statuses 201, 400, 401, 404, 422, 500, 504; error codes in examples `EDPT0003`, `BDPT0019`, `EDPT0005`, `EDPT0009`, `BDPT0001`, `BDPT0021`, `BDPT0022`, `EDPT9998`, `EDPT0001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-fee` | `disputes-dispute-fee-events-1` |
| `post-migration-installment` | `disputes-dispute-installment-creation-1` |
| `post-migration-with-auth` | `disputes-dispute-installment-creation-1` |
| `post-v1-disputes-disputeId-installment` | `disputes-dispute-installment-creation-1` |
| `post-v1-networkauthorization-disputes` | `disputes-dispute-installment-creation-1` |
| `post-migration-installment` | `disputes-dispute-installment-status-change-1` |
| `post-migration-with-auth` | `disputes-dispute-installment-status-change-1` |
| `post-v1-disputes-disputeId-event` | `disputes-dispute-installment-status-change-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `disputes-dispute-fee-events-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-dispute-fee-events-1 | 1 | KU-EVT-catalogue-disputes |
| `disputes-dispute-installment-status-change-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1 | 4 | KU-EVT-catalogue-disputes |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/disputes-overview.md`: updatedAt 2026-07-16T21:51:51.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/disputes-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/disputes-overview | `323e45b68b62e4a6…` | 2026-07-16T21:51:51.000Z |

## Related knowledge units

- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-API-card-issuing-disputes--evidence-files` — API reference: Card issuing - Disputes — Evidence files
- `KU-API-card-issuing-disputes--fees` — API reference: Card issuing - Disputes — Fees
- `KU-API-card-issuing-disputes--fees-v2` — API reference: Card issuing - Disputes — Fees V2
- `KU-API-card-issuing-disputes--installments` — API reference: Card issuing - Disputes — Installments
- `KU-API-card-issuing-disputes--migration` — API reference: Card issuing - Disputes — Migration
- `KU-API-card-issuing-disputes--state-check` — API reference: Card issuing - Disputes — State check
- `KU-API-card-issuing-disputes--supporting-forms` — API reference: Card issuing - Disputes — Supporting forms
- `KU-CARD-disputes-setup-and-on-us` — Disputes access setup and on-us disputes
- `KU-CARD-disputes-state-machine` — Disputes state machine
- `KU-CARD-visa-colloboration-questionaire-part-01` — Visa collaboration and allocation questionnaires (part 1 of 7)
- `KU-CARD-visa-colloboration-questionaire-part-02` — Visa collaboration and allocation questionnaires (part 2 of 7)
- `KU-CARD-visa-colloboration-questionaire-part-03` — Visa collaboration and allocation questionnaires (part 3 of 7)
- `KU-CARD-visa-colloboration-questionaire-part-04` — Visa collaboration and allocation questionnaires (part 4 of 7)
- `KU-CARD-visa-colloboration-questionaire-part-05` — Visa collaboration and allocation questionnaires (part 5 of 7)
- `KU-CARD-visa-colloboration-questionaire-part-06` — Visa collaboration and allocation questionnaires (part 6 of 7)
- `KU-CARD-visa-colloboration-questionaire-part-07` — Visa collaboration and allocation questionnaires (part 7 of 7)
- `KU-CORE-transactions-overview` — Transactions overview
- `KU-EVT-catalogue-disputes` — Event catalogue: disputes
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
