---
ku_id: KU-CARD-disputes-setup-and-on-us
title: Disputes access setup and on-us disputes
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/set-up-disputes.md
  sha256: 2eba082578fb704e897c661a35e5807508d33c1f6325683ac7f489be13d89f6e
  url: https://developers.pismo.io/pismo-docs/docs/set-up-disputes
  role: primary_guide
  updated_at: '2026-07-15T21:30:38.000Z'
- path: docs/card-issuing/on-us-disputes.md
  sha256: 8992abc0e141dec96b8f3ed9d8fa2752b0e431a8a8a79e992bed05fc6b180036
  url: https://developers.pismo.io/pismo-docs/docs/on-us-disputes
  role: primary_guide
  updated_at: '2026-09-10T18:41:56.000Z'
operations:
- post-create-on-us-dispute
- post-update-on-us-dispute
related_kus:
- KU-API-card-issuing-disputes--on-us
- KU-EVT-catalogue-disputes
- KU-SUP-service-desk-requests
grouping_rationale: Short disputes pages.
---

# Disputes access setup and on-us disputes

**KU ID:** `KU-CARD-disputes-setup-and-on-us` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Short disputes pages.

Scope as stated in `docs/card-issuing/set-up-disputes.md`:

> 1. Let Pismo know the card network you’ll be using and request access to the Dispute API in EXT (test environment). To do this, go to the Pismo [Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk), select **Settings** then, from the drop-down menu, select **Disputes Configuration**.
> 2. Contact your card network account manager and inform them that Pismo will process your disputes on their network.
> 3. Submit forms to the card network to request access to Disputes UI, API key, and certificates.

Scope as stated in `docs/card-issuing/on-us-disputes.md`:

> An on-us transaction is a payment, card purchase, or check where the issuing bank (the customer's bank) and the acquiring bank (the merchant's or receiver's bank) are the same financial institution. Because the payment stays inside a single bank, it does not need to go through outside card networks like Visa or Mastercard. Any on-us transaction dispute is resolved within that bank, without the need for card network involvement or extra fees.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/set-up-disputes.md`: Set up disputes access; General setup (all card networks); &#x20;Visa setup; Mastercard setup
- `docs/card-issuing/on-us-disputes.md`: On-us disputes; Create on-us dispute endpoint; On-us state machine

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/set-up-disputes.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/set-up-disputes · updatedAt: 2026-07-15T21:30:38.000Z

<!-- source:begin path=docs/card-issuing/set-up-disputes.md part=0-end -->

# Set up disputes access

# General setup (all card networks)

1. Let Pismo know the card network you’ll be using and request access to the Dispute API in EXT (test environment). To do this, go to the Pismo [Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk), select **Settings** then, from the drop-down menu, select **Disputes Configuration**.
2. Contact your card network account manager and inform them that Pismo will process your disputes on their network.
3. Submit forms to the card network to request access to Disputes UI, API key, and certificates.

# &#x20;Visa setup

1. Go to <a href="https://www.visaonline.com/" target="_blank">Visa online</a>
2. Create a Persona ID with Visa for both sandbox and production environments. Reach out to your Visa account manager
3. Send the Persona IDs to your Pismo account manager.

Pismo will open a request with Visa to link the Issuer's persona ID to Pismo's persona ID.

After Visa confirms the linkage, Pismo can perform Visa dispute API calls on an issuer's behalf.

# Mastercard setup

1. Go to <a href="https://www.mastercardconnect.com/-/sign-in" target="_blank">Mastercard connect</a>
2. Create a project in Mastercard Developers for the Mastercom application.
3. Generate sandbox and/or production credentials within the project.
4. Choose one of the following options:
   * **Option A**: Create the credentials and securely share them with Pismo.
   * **Option B**: Grant access to Pismo's security team so they can create and manage the credentials for you. Once the credentials are validated, Pismo can perform Mastercard dispute API calls on an issuer's behalf.

Once the credentials are validated, Pismo can perform Mastercard dispute API calls on an issuer's behalf.

<br />
<!-- source:end -->

### Source 2: `docs/card-issuing/on-us-disputes.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/on-us-disputes · updatedAt: 2026-09-10T18:41:56.000Z

<!-- source:begin path=docs/card-issuing/on-us-disputes.md part=0-end -->

# On-us disputes

An on-us transaction is a payment, card purchase, or check where the issuing bank (the customer's bank) and the acquiring bank (the merchant's or receiver's bank) are the same financial institution. Because the payment stays inside a single bank, it does not need to go through outside card networks like Visa or Mastercard. Any on-us transaction dispute is resolved within that bank, without the need for card network involvement or extra fees.

# Create on-us dispute endpoint

Sample [Create on-us dispute](https://developers.pismo.io/pismo-docs/reference/post-create-on-us-dispute)  payload

```json
curl --location 'https://disputes-core-api-ext.internal.pismolabs.io/v1/on-us-dispute' 
--header 'Content-Type: application/json' 
--header 'x-cid: e0000000-0000-0000-0000-000000000000' 
--header 'x-tenant: TN-7364948a-cf8c-423b-bc3b-1fbc251c1301' 
--header 'x-account-id: 327313629' \
--data '{
      "source_identifier": { "id": "10007209824", "type": "AUTHORIZATION" },
      "metadata": { "test_run": "PISMO-349906-sandbox-1" },
      "modality": 1,
      "disputed_amount": 10.00,
      "is_partial": true,
      "comment": "PISMO-349906 sandbox smoke",
      "protocol": "PISMO-349906-sandbox-1"
}'
```

# On-us state machine

Like card network disputes, on-us disputes at Pismo use a state machine to progress the dispute to completion. An `event` enum is typically passed to [Update on-us dispute](https://developers.pismo.io/pismo-docs/reference/post-update-on-us-dispute)  to transition the dispute status to a new status.

<Image align="center" src="https://files.readme.io/c7cf995f1c0e79679b62f3d8e0f4349dbacfe2ff34047c8fa388f451d802972a-Dispute_State_Machine.png" />

<br />

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Event
      </th>

      <th>
        Valid from states
      </th>

      <th>
        Target state
      </th>

      <th>
        Descriptiom
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `OPEN`
      </td>

      <td>
        `PENDING` \`
      </td>

      <td>
        `OPENED`
      </td>

      <td>
        Open the dispute for analysis
      </td>
    </tr>

    <tr>
      <td>
        `PENDING_DOCUMENTATION`
      </td>

      <td>
        `OPENED`
      </td>

      <td>
        `PENDING_DOCUMENTATION`
      </td>

      <td>
        Request additional documentation
      </td>
    </tr>

    <tr>
      <td>
        `ISSUER_LOSS`
      </td>

      <td>
        `OPENED`
      </td>

      <td>
        `ISSUER_LOSS`
      </td>

      <td>
        Close dispute - issuer loses
      </td>
    </tr>

    <tr>
      <td>
        `STORE_OWNER_LOSS`
      </td>

      <td>
        `OPENED`
      </td>

      <td>
        `STORE_OWNER_LOSS`
      </td>

      <td>
        Close dispute - store owner loses
      </td>
    </tr>

    <tr>
      <td>
        `CARDHOLDER_LOSS`
      </td>

      <td>
        `OPENED`
      </td>

      <td>
        `CARDHOLDER_LOSS`
      </td>

      <td>
        Close dispute - cardholder loses
      </td>
    </tr>

    <tr>
      <td>
        `REOPEN`
      </td>

      <td>
        `CANCELLED`\
        `REJECTED`
      </td>

      <td>
        `PENDING`
      </td>

      <td>
        Reopen a closed dispute
      </td>
    </tr>

    <tr>
      <td>
        `RESEND`
      </td>

      <td>
        `PENDING_DOCUMENTATION`
      </td>

      <td>
        `RESEND`
      </td>

      <td>
        Documentation received, resume analysis
      </td>
    </tr>

    <tr>
      <td>
        `CANCEL`
      </td>

      <td>
        `PENDING`\
        `OPENED` `PENDING_DOCUMENTATION`
      </td>

      <td>
        `CANCELED`
      </td>

      <td>
        Cancel the dispute
      </td>
    </tr>

    <tr>
      <td>
        `EXPIRE`
      </td>

      <td>
        `PENDING`\
        `OPENED` `PENDING_DOCUMENTATION`
      </td>

      <td>
        `EXPIRED`
      </td>

      <td>
        Mark dispute as expired
      </td>
    </tr>

    <tr>
      <td>
        `REJECTS`
      </td>

      <td>
        `PENDING`\
        `PENDING_DOCUMENTATION`
      </td>

      <td>
        `REJECTED`
      </td>

      <td>
        Reject the dispute
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
| `POST /v1/on-us-dispute` | `post-create-on-us-dispute` | Create on-us dispute | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--on-us |
| `POST /v1/disputes-on-us/{disputeId}/event` | `post-update-on-us-dispute` | Update on-us dispute | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--on-us |

### Operation essentials

- **`POST /v1/on-us-dispute`** (`post-create-on-us-dispute`): security `BearerAuth`; required parameters none declared; required body fields `source_identifier`, `modality`, `is_partial`, `disputed_amount`; response statuses 201, 400, 401, 404, 422, 500, 504; error codes in examples `EDPT0004`, `EDPT0005`, `EDPT0009`, `BDPT0006`, `BDPT0001`, `BDPT0026`, `BDPT0027`, `EDPT9997`, `EDPT9998`, `EDPT9999`, `EDPT0001`; events `disputes-disputes-creation-1`.
- **`POST /v1/disputes-on-us/{disputeId}/event`** (`post-update-on-us-dispute`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `event`; response statuses 200, 400, 401, 404, 422, 423, 500, 504; error codes in examples none; events `disputes-dispute-installment-status-change-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-update-on-us-dispute` | `disputes-dispute-installment-status-change-1` |
| `post-create-on-us-dispute` | `disputes-disputes-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/set-up-disputes.md`: updatedAt 2026-07-15T21:30:38.000Z.
- `docs/card-issuing/on-us-disputes.md`: updatedAt 2026-09-10T18:41:56.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/set-up-disputes.md` | whole document | https://developers.pismo.io/pismo-docs/docs/set-up-disputes | `2eba082578fb704e…` | 2026-07-15T21:30:38.000Z |
| `docs/card-issuing/on-us-disputes.md` | whole document | https://developers.pismo.io/pismo-docs/docs/on-us-disputes | `8992abc0e141dec9…` | 2026-09-10T18:41:56.000Z |

## Related knowledge units

- `KU-API-card-issuing-disputes--on-us` — API reference: Card issuing - Disputes — On-Us
- `KU-EVT-catalogue-disputes` — Event catalogue: disputes
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
