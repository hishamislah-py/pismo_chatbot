---
ku_id: KU-CC-disputes
title: Disputes
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/disputes.md
  sha256: d35228f356e9e4acbd19d1fbda39bb1c7f66a7d3065cd597756a806d01e46a43
  url: https://developers.pismo.io/pismo-docs/docs/disputes
  role: primary_guide
  updated_at: '2026-06-08T16:10:15.000Z'
operations:
- post-v1-networkauthorization-disputes
related_kus:
- KU-API-card-issuing-disputes--disputes-part-01
- KU-CARD-disputes-overview
- KU-CARD-disputes-state-machine
- KU-EVT-catalogue-disputes
grouping_rationale: single source page
---

# Disputes

**KU ID:** `KU-CC-disputes` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/control-center/disputes.md`:

> Create, view, and manage cardholder transaction disputes.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/disputes.md`: Disputes; View disputes; Dispute a transaction; Manage disputes; Open a dispute; Cancel a dispute; Reopen a dispute; Provide supporting evidence; Create a fraud report; Create an EBDF; Upload an attachment

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/disputes.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/disputes · updatedAt: 2026-06-08T16:10:15.000Z

<!-- source:begin path=docs/control-center/disputes.md part=0-end -->

# Disputes

Create, view, and manage cardholder transaction disputes.

<Embed typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=hPaMZ5ZMMjM" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FhPaMZ5ZMMjM%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DhPaMZ5ZMMjM%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FhPaMZ5ZMMjM%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22800%22%20height%3D%22450%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" href="https://www.youtube.com/watch?v=hPaMZ5ZMMjM" providerUrl="https://www.youtube.com/" providerName="YouTube" />

> 📘 Mastercard only
>
> Control Center currently only supports Mastercard transaction dispute management. To manage disputes for other card networks, [use the API](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes).

> 📘 Access by role
>
> * Users with the **Backoffice operator** role can create, view, and manage disputes.
> * Users with the **Backoffice viewer** role can view disputes only.

For more information, refer to [Disputes overview](https://developers.pismo.io/pismo-docs/docs/disputes-overview).

From Control Center, you can do the following:

* [View disputes](#view-disputes)
* [Dispute a transaction](#dispute-a-transaction)
* [Manage disputes](#manage-disputes)

# View disputes

To view the list of disputes, do the following:

* From the main menu, select **Customer operations** > **Disputes**.\
  The **Disputes** screen is displayed.

Refer to the following table for a description of the columns.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Column
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **ID**
      </td>

      <td>
        The ID of the dispute
      </td>
    </tr>

    <tr>
      <td>
        **OPENED ON**
      </td>

      <td>
        The date when the dispute was opened
      </td>
    </tr>

    <tr>
      <td>
        **AUTHORIZATION**
      </td>

      <td>
        The authorization ID of the disputed transaction
      </td>
    </tr>

    <tr>
      <td>
        **REASON**
      </td>

      <td>
        The reason for the dispute
      </td>
    </tr>

    <tr>
      <td>
        **STATUS**
      </td>

      <td>
        The status of the dispute

        For more information, refer to [Disputes state machine](https://developers.pismo.io/pismo-docs/docs/disputes-state-machine).
      </td>
    </tr>

    <tr>
      <td>
        **ACTION**
      </td>

      <td>
        The action status indicating if your input is required to move the dispute forward
      </td>
    </tr>

    <tr>
      <td>
        **AMOUNT**
      </td>

      <td>
        The disputed transaction amount
      </td>
    </tr>
  </tbody>
</Table>

To view a specific dispute, do the following:

1. From the main menu, select **Customer operations** > **Disputes**.
2. On the **Disputes** screen, select a dispute.\
   The **Dispute details** screen is displayed.\
   This screen contains key information about the dispute. Additional sections are included based on the supporting evidence provided for the dispute, for example, **Fraud report**, **Expedited Billing Dispute Forms (EBDF)**, or **Attachments**.\
   For disputed transactions with multiple installments, you can find information about each individual installment in its tab.

The **Disputes** screen provides filtering options for refining your search. You can do the following:

* To list all disputes created for a specific account, in **Search by account ID**, enter the account ID.
* To filter by start date, end date, or status, select the filter icon, configure your filters, and select **Apply filter**.

# Dispute a transaction

In Control Center, you can create dispute requests for disputes raised by your cardholders to send to the card network.

To dispute a transaction, do the following:

1. From the main menu, select **Customer operations** > **Accounts**.\
   The **Accounts management** screen is displayed.
2. On the **Accounts management** screen, search for the cardholder's account.
3. On the cardholder's account screen, select **Transactions**, and select the transaction you want to dispute.
4. Select **Dispute transaction**.\
   The **Dispute a transaction** dialog is displayed.
5. In **Dispute amount**, enter the dispute amount.
6. From **Reason for the dispute**, select a reason for the dispute.\
   For more information, refer to this <Anchor label="quick reference" target="_blank" href="https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide">quick reference</Anchor> for chargeback codes or consult the [Mastercard chargeback guide](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf).
7. In **Leave a comment**, enter any supplementary information about the dispute.
8. Select **Submit dispute**.
9. Select **Submit**.\
   The dispute is created and its status is set to **Pending**.\
   **Note**: When you create a dispute, it's not automatically sent to the card network. You must send it yourself. For more information, refer to [Open a dispute](#open-a-dispute).

> 📘 Multiple installment disputes
>
> If you enabled automated dispute installment control for your program, for transactions with multiple installments, you only need to dispute the first installment. The dispute automatically applies to all subsequent installments.
>
> For more information, refer to [Automated dispute installment control](https://developers.pismo.io/pismo-docs/docs/disputes-overview#automated-dispute-installment-control).

# Manage disputes

From Control Center, you can do the following:

* [Open a dispute](#open-a-dispute)
* [Cancel a dispute](#cancel-a-dispute)
* [Reopen a dispute](#reopen-a-dispute)
* [Provide supporting evidence](#provide-supporting-evidence)

## Open a dispute

To open a dispute, you must send a request to the card network. Depending on the card network's decision, your request can be either approved or rejected.

To open a dispute, do the following:

1. From the main menu, select **Customer operations** > **Disputes**.
2. Select a pending dispute.
3. On the **Dispute details** screen, if applicable, add supporting evidence.\
   For more information, refer to [Provide supporting evidence](#provide-supporting-evidence).
4. Select the more options icon and select **Open dispute**.\
   The **Send request to open dispute** dialog is displayed.
5. Select **Send request**.\
   The request is sent to the card network and the dispute status changes to **Opened**.

Refer to the following table for a description of the possible dispute lifecycle scenarios.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Card network response
      </th>

      <th>
        Resulting dispute status
      </th>

      <th>
        What you can do
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Card network approves your request
      </td>

      <td>
        **Chargeback created**
      </td>

      <td>
        Wait for the card network to process the request
      </td>
    </tr>

    <tr>
      <td>
        Card network accepts the chargeback
      </td>

      <td>
        **Chargeback accepted**
      </td>

      <td>
        No further action required
      </td>
    </tr>

    <tr>
      <td>
        Card network rejects the chargeback
      </td>

      <td>
        **Chargeback rejected**
      </td>

      <td>
        Review the request, update your supporting evidence, and resend the request
      </td>
    </tr>

    <tr>
      <td>
        Card network requests additional supporting evidence
      </td>

      <td>
        **Chargeback pending documentation**
      </td>

      <td>
        You can do one of the following:

        * To close the dispute, select the more options icon, and select **Close dispute**.\
          The dispute is closed and the status changes to **Chargeback closed**.
        * To resend the dispute request after providing additional supporting evidence, select the more options icon, and select **Resend dispute**.\
          The dispute is resent to the card network and the status changes to **Chargeback created**.
      </td>
    </tr>

    <tr>
      <td>
        Card network schedules the transaction to be voided in 20 days
      </td>

      <td>
        **Chargeback reject collaboration**
      </td>

      <td>
        No further action required
      </td>
    </tr>

    <tr>
      <td>
        Card network rejects the request immediately
      </td>

      <td>
        **Failed**
      </td>

      <td>
        You can do one of the following:

        * To accept an issuer loss, select the more options icon, and select **Accept issuer loss**.\
          The dispute is closed and the status changes to **Issuer loss**.
        * To resend the dispute request, select the more options icon, and select **Resend dispute**.\
          The request is resent to the card network and the dispute status changes to **Opened**.
      </td>
    </tr>
  </tbody>
</Table>

## Cancel a dispute

To cancel a dispute, do the following:

1. From the main menu, select **Customer operations** > **Disputes**.
2. Select a pending dispute.
3. On the **Dispute details** screen, select the more options icon, and select **Cancel dispute**.\
   The request is canceled, and the dispute status changes to **Canceled**.

## Reopen a dispute

To reopen a canceled dispute, do the following:

1. From the main menu, select **Customer operations** > **Disputes**.
2. Select a canceled dispute.
3. On the **Dispute details** screen, select the more options icon, and select **Reopen dispute**.\
   The **Send request to reopen dispute** dialog is displayed.
4. Select **Send request**.\
   The request is sent to the card network, and the dispute status changes to **Pending**.

## Provide supporting evidence

To support a dispute request, you can do one of the following:

* [Create a fraud report](#create-a-fraud-report)
* [Create an EBDF](#create-an-ebdf)
* [Upload an attachment](#upload-an-attachment)

> 📘 Supporting evidence for Mastercard disputes
>
> Mastercard does not allow more than one type of supporting evidence per dispute request. When sending a request, make sure you include only one evidence document type.

### Create a fraud report

For disputes that are a result of fraud, for example, stolen identity or a lost card, you can create a fraud report to include with the dispute request.

> 📘 Fraud report availability
>
> You can create a fraud report only when the dispute is in one of the following states:
>
> * CHARGEBACK\_CREATED
> * CHARGEBACK\_PENDING\_DOCUMENTATION
> * SECOND\_PRESENTMENT

> 📘 Updating a fraud report
>
> You can't update an existing fraud report directly. Instead, you must create a new report, which replaces the existing one.

To create a fraud report, do the following:

1. From the main menu, select **Customer operations** > **Disputes**.
2. Select the required dispute.
3. On the **Dispute details** screen, select **Create fraud report**.\
   The **Create fraud report** screen is displayed.
4. From **Account status**, select the status of the cardholder's account.
5. From **Chargeback indicator**, select whether the fraudulent transaction is associated with a chargeback.
6. From **CVC invalid indicator**, select the outcome of CVC verification.
7. From **Device type**, select the device used to make the fraudulent transaction.
8. From **Fraud type**, select the primary category of fraud associated with the transaction.
9. From **Fraud subtype**, select a specific fraud classification.\
   If you are unsure, select **Unknown**.
10. From **Report date**, select the date when the cardholder identified and reported the fraud.
11. Select **Create fraud report**.\
    The fraud report is created and added to the dispute.

### Create an EBDF

An EBDF is a Mastercard-specific dispute document for submitting required dispute information in a standardized format.

> 📘 Updating an EBDF
>
> You can't update an existing EBDF directly. Instead, you must create a new EBDF, which replaces the existing one.

You can create the following types of EBDF:

* **Fraud**—Fraud-related disputes, for example, stolen identity or a lost card
* **Cardholder dispute**—Cardholder-initiated disputes
* **Point of interaction errors**—Errors occurring during point of interaction, for example, the seller charging the wrong amount, charging twice for the same purchase, or failing to confirm a refund

#### Create a fraud EBDF

To create a fraud EBDF, do the following:

1. From the main menu, select **Customer operations** > **Disputes**.
2. Select the required dispute.
3. On the **Dispute details** screen, select **Create EBDF**.\
   The **Select EBDF type** screen is displayed.
4. On the **Select EBDF type** screen, select **Fraud**, and select **Next**.
5. In **Card holder verification method**, order the verification methods used by the merchant during the transaction.
6. In **Number of items**, enter the number of transactions disputed.
7. From **Types**, select the fraud-related actions and conditions associated with the transaction, cardholder account, or both.
8. In **Chargeback representative**, enter the name of the party responsible for managing the chargeback.
9. From **Card issuer region**, select the geographic region where the card issuer is based.
10. In **Additional information**, enter any supplementary details related to the fraudulent transaction dispute.
11. Select **Next**.
12. Review the EBDF details.\
    If you want to make changes, select **Back** until you reach the required page.
13. Select **Create**.\
    The EBDF is created and added to the dispute.

#### Create a cardholder dispute EBDF

To create a cardholder dispute EBDF, do the following:

1. From the main menu, select **Customer operations** > **Disputes**.
2. Select the required dispute.
3. On the **Dispute details** screen, select **Create EBDF**.\
   The **Select EBDF type** screen is displayed.
4. On the **Select EBDF type** screen, select **Cardholder dispute**, and select **Next**.
5. In **Transaction amount**, enter the dispute amount.
6. From **Type**, select the cardholder dispute type.
7. From **Actual delivery date of goods or service**, select the date when the goods or service was delivered to the cardholder.\
   **Note**: This field is only available if you selected the **PRODUCT\_DISPUTE** dispute type.
8. From **Expected delivery date of goods or service**, select the date when the goods or service was expected to be delivered.\
   **Note**: This field is only available if you selected the **NOT\_PROVIDED** dispute type.
9. From **Return date**, select the date when the cardholder returned or canceled the goods or service.\
   **Note**: This field is only available if you selected the **DIGITAL\_GOODS** dispute type.
10. From **Cancellation date**, select the date when the cardholder canceled a recurring transaction.\
    **Note**: This field is only available if you selected the **RECURRING\_CANCELLED** dispute type.
11. From **Cardholder participation?**, select whether the cardholder participated in the disputed transaction.
12. In **Dispute details**, enter any additional information related to the dispute.
13. In **Chargeback representative**, enter the name of the party responsible for managing the chargeback.
14. Select **Next**.
15. Review the EBDF details.\
    If you want to make changes, select **Back** until you reach the required page.
16. Select **Create**.\
    The EBDF is created and added to the dispute.

#### Create a point of interaction errors EBDF

To create a point of interaction errors EBDF, do the following:

1. From the main menu, select **Customer operations** > **Disputes**.
2. Select the required dispute.
3. On the **Dispute details** screen, select **Create EBDF**.\
   The **Select EBDF type** screen is displayed.
4. On the **Select EBDF type** screen, select **Point of interaction errors**, and select **Next**.
5. In **Transaction amount**, enter the dispute amount.
6. From **Type**, select the point of interaction errors dispute type.
7. In **Alternate means of payment details**, enter additional details about the alternative payment method used by the cardholder.\
   **Note**: This field is only available if you selected the **DUPLICATE\_DEBIT** dispute type. The details help the card network clarify how the transaction was paid and confirm that only one valid payment should remain.
8. In **Dispute details**, enter any additional information related to the dispute.
9. In **Chargeback representative**, enter the name of the party responsible for managing the chargeback.
10. Select **Next**.
11. Review the EBDF details.\
    If you want to make changes, select **Back** until you reach the required page.
12. Select **Create**.\
    The EBDF is created and added to the dispute.

### Upload an attachment

You can upload attachments to include as supporting evidence when sending a dispute request to the card network.

> 📘 File constraints
>
> To upload an attachment, make sure your file meets the following requirements:
>
> * The filename:
>   * Can have a maximum of nine characters
>   * Must include at least one number and one letter
>   * Cannot contain any special characters
> * The file size must not exceed 14Mb
> * Only the following file types are supported:
>   * JPG
>   * JPEG
>   * TIF
>   * TIFF
>   * PDF

To upload an attachment, do the following:

1. From the main menu, select **Customer operations** > **Disputes**.
2. Select the required dispute.
3. On the **Dispute details** screen, select the more options icon, and select **Upload attachment**.\
   The **Upload attachment** dialog is displayed.
4. Select the upload area and select the files you want to attach.\
   **Note**: To remove a file, select the trash icon.
5. Select **Upload**.\
   The files are uploaded and attached to the dispute.\
   **Note**: To download an attachment, select the download icon.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/networkauthorization-disputes` | `post-v1-networkauthorization-disputes` | Create dispute | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01 |

### Operation essentials

- **`POST /v1/networkauthorization-disputes`** (`post-v1-networkauthorization-disputes`): security `BearerAuth`; required parameters `Authorization` (header); required body fields `modality`, `disputed_amount`, `is_partial`, `network_brand_type`; response statuses 200, 400, 401, 422, 500; error codes in examples none; events `disputes-dispute-installment-creation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-networkauthorization-disputes` | `disputes-dispute-installment-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/control-center/disputes.md`: updatedAt 2026-06-08T16:10:15.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/disputes.md` | whole document | https://developers.pismo.io/pismo-docs/docs/disputes | `d35228f356e9e4ac…` | 2026-06-08T16:10:15.000Z |

## Related knowledge units

- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-CARD-disputes-overview` — Disputes overview
- `KU-CARD-disputes-state-machine` — Disputes state machine
- `KU-EVT-catalogue-disputes` — Event catalogue: disputes
