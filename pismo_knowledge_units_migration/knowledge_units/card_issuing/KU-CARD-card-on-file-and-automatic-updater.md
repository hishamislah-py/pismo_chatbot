---
ku_id: KU-CARD-card-on-file-and-automatic-updater
title: Card-on-file and automatic updater
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/pismo-card-on-file.md
  sha256: 3213b82d3d411f0564d570b4cad1bd40049b4a88d476ba5dc551eb5d0e3a0936
  url: https://developers.pismo.io/pismo-docs/docs/pismo-card-on-file
  role: primary_guide
  updated_at: '2026-05-28T17:12:58.000Z'
- path: docs/card-issuing/automatic-updater.md
  sha256: a05d26eea97670b716b86cd346e955d74fdc3085c9cce36b2e2941f67dd9bf32
  url: https://developers.pismo.io/pismo-docs/docs/automatic-updater
  role: primary_guide
  updated_at: '2026-07-22T22:27:33.000Z'
operations:
- create-a-cardsonfile
- post-vau-opt-in
- post-vau-opt-out
related_kus:
- KU-API-card-issuing-cards--automatic-updater
- KU-API-card-issuing-cards-on-file--cards-on-file
- KU-CARD-card-tokenization-process-and-onboarding
- KU-EVT-catalogue-cards
- KU-EVT-catalogue-cardsonfile
- KU-SUP-service-desk-requests
grouping_rationale: Card-on-file service and its updater.
---

# Card-on-file and automatic updater

**KU ID:** `KU-CARD-card-on-file-and-automatic-updater` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Card-on-file service and its updater.

Scope as stated in `docs/card-issuing/pismo-card-on-file.md`:

> A card stored and tokenized in a digital wallet is known as a *card-on-file*. To add a card to a Pismo digital wallet, call the [Create card on file](https://developers.pismo.io/pismo-docs/reference/create-a-cardsonfile) endpoint, which validates the card with an acquirer. This endpoint lets you execute a card owner validation/verification and returns a token representing the card you can use for payments and other card operations on the Pismo platform.

Scope as stated in `docs/card-issuing/automatic-updater.md`:

> Mastercard's ABU (Automatic Billing Updater) and Visa's VAU (Visa Account Updater) are proprietary backend services that securely and automatically update a cardholder’s stored payment information (like new card numbers or expiration dates) with participating merchants and subscription services. These programs run seamlessly behind the scenes to reduce payment declines and prevent accidental service interruptions for recurring billing and "card-on-file" transactions.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/pismo-card-on-file.md`: Pismo card-on-file
- `docs/card-issuing/automatic-updater.md`: Automatic updater; How they work; Getting started; Mastercard's ABU; Visa Account Updater (VAU); Key aspects; VAU implementation; Step 1 : Contact Visa and initiate a Visa project; Step 2: Set up Initial environment; Endpoints

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/pismo-card-on-file.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pismo-card-on-file · updatedAt: 2026-05-28T17:12:58.000Z

<!-- source:begin path=docs/card-issuing/pismo-card-on-file.md part=0-end -->

# Pismo card-on-file

A card stored and tokenized in a digital wallet is known as a *card-on-file*. To add a card to a Pismo digital wallet, call the [Create card on file](https://developers.pismo.io/pismo-docs/reference/create-a-cardsonfile) endpoint, which validates the card with an acquirer. This endpoint lets you execute a card owner validation/verification and returns a token representing the card you can use for payments and other card operations on the Pismo platform.

**Note**: This product is not related to card network E-commerce/card-on-file tokens (such as Google Pay, Netflix, and so on). This is strictly internal to the Pismo platform. If you want to use network card-on-file tokens, please refer to [Card tokenization process and onboarding](https://developers.pismo.io/pismo-docs/docs/card-tokenization-process-and-onboarding).

> 📘 Acquirers
>
> Pismo is fully integrated with a number of acquirers (banks representing merchants). Check your acquiring options with your Pismo representative.
<!-- source:end -->

### Source 2: `docs/card-issuing/automatic-updater.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/automatic-updater · updatedAt: 2026-07-22T22:27:33.000Z

<!-- source:begin path=docs/card-issuing/automatic-updater.md part=0-end -->

# Automatic updater

Mastercard's ABU (Automatic Billing Updater) and Visa's VAU (Visa Account Updater) are proprietary backend services that securely and automatically update a cardholder’s stored payment information (like new card numbers or expiration dates) with participating merchants and subscription services. These programs run seamlessly behind the scenes to reduce payment declines and prevent accidental service interruptions for recurring billing and "card-on-file" transactions.

### How they work

* **Card issuance**: When you issue a replacement or renewed card, they securely transmit the new Primary Account Number (PAN) and expiration date to Mastercard or Visa.
* **Merchant Inquiries:** Merchants and payment gateways regularly query the ABU or VAU databases to check if a customer’s stored card information has changed.
* **Automatic updates**: If a match is found, the merchant’s billing files are updated automatically so a cardholder's subscriptions (e.g., streaming services, gym memberships) can continue without you needing to manually update the card.

### Getting started

To enable ABU or VAU for a program, create a [Service Desk](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket)  ticket with request type = `Settings/Configuration`.

# Mastercard's ABU

For a Mastercard card, you have the option to enable their Automatic Billing Updater (ABU) feature. When account credentials change, it’s challenging for consumers to inform all of their merchants. As a result, their card-not-present payments may be declined. This creates service disruptions for consumers, as well as lost revenue and decreased customer loyalty for merchants.

When a card is created, reissued, or a card's account credentials change, such as the card being lost, stolen, or closed, Pismo automatically notifies Mastercard if this feature is enabled. Mastercard, in turn, notifies the merchants it has on file for that card. Update notifications are sent to Mastercard on a daily basis.

For more information, refer to Mastercard's <Anchor label="Automatic Billing Updater" target="_blank" href="https://developer.mastercard.com/product/automatic-billing-updater-abu/">Automatic Billing Updater</Anchor> documentation.

# Visa Account Updater (VAU)

Visa Account Updater (VAU) is a free, automated Visa service provided that securely shares updated card information—such as new card numbers or expiration dates—with participating merchants. It is designed to prevent service disruptions for recurring payments and subscriptions when your debit or credit card expires, is lost, or is reissued.

### Key aspects

* **Merchant participation**: Not all merchants participate in the VAU program. A cardholder may still need to manually update their information with smaller businesses or services that do not subscribe to the service.
* **Opt-out option**: While a cardholder is typically enrolled in VAU automatically when they receive a new card, you can opt them out of the service at any time via the Pismo [opt-out endpoint](https://developers.pismo.io/pismo-docs/reference/post-vau-opt-out) .

For more information about VAU, refer to  <a href="https://developer.visa.com/capabilities/vau" target="_blank">Visa Account Updater Overview</a>.

## VAU implementation

To start the implementation of VAU for a customer/environment, follow these steps:

### Step 1 : Contact Visa and initiate a Visa project

* **Multi-tenant environments** - Request the project as Multi-Issuer.
* **Single-tenant environments** - Request the project as Single-Issuer.

### Step 2: Set up Initial environment

Once the project request is submitted, VISA will provide a set of forms you need to complete. These forms are required for:

* Visa Issuer configuration
* File transmission set up via SFTP (VFT/VFES).

The **Cards team** can assist with:

* Providing the PCI environment IP addresses to be associated with the account, those can be found on this doc: Pismo Outbound Public IPs
* Generating the SSH key (VISA requirement) for SFTP connection setup. [Support ticket](https://pismolabs.atlassian.net/browse/ISD-44509) example for SSH key creation: ISD-44509 – please note that GRC action is required

1. Receive configuration data from VISA, example:

```
Service(s):  VAU  
Bank Name: Pismo Labs Inc  
BID/PID/SID: BID: XXXXXX, NCN ID: XXXXXX, Multi-issuer ID: XXXX  
VFT ID:  VFTXXXXXXXX
```

The Cards team can then support with:

* Testing in the sandbox environment, as usually requested by VISA.
* Configuration in the production environment.

# Endpoints

* [Visa automatic updater opt-in](https://developers.pismo.io/pismo-docs/reference/post-vau-opt-in)  — Opt a card back into VAU after it has been opted out
* [Automatic updater opt-out](https://developers.pismo.io/pismo-docs/reference/post-vau-opt-out)  — Opt a card out of VAU or ABU
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /cardsonfile/v2/cardsonfile/cards` | `create-a-cardsonfile` | Create card on file | `api-specs/Card_issuing_-_Cards_on_file.yaml` | no | KU-API-card-issuing-cards-on-file--cards-on-file |
| `POST /cards/v1/automatic-updater/{cardID}/opt-out` | `post-vau-opt-out` | Automatic updater opt-out | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--automatic-updater |
| `POST /cards/v1/automatic-updater/{cardID}/opt-in` | `post-vau-opt-in` | Visa automatic updater opt-in | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--automatic-updater |

### Operation essentials

- **`POST /cardsonfile/v2/cardsonfile/cards`** (`create-a-cardsonfile`): security not declared; required parameters `Authorization` (header); required body fields `card_name`, `cvv`, `expiration_date`, `name`, `pan`; response statuses 200, 400, 500; error codes in examples none; events `cardsonfile-provision-1`.
- **`POST /cards/v1/automatic-updater/{cardID}/opt-out`** (`post-vau-opt-out`): security `BearerAuth`; required parameters `cardID` (path); required body fields none declared; response statuses 200, 401, 403, 404, 500; error codes in examples none; events `cards-automatic-updater-1`.
- **`POST /cards/v1/automatic-updater/{cardID}/opt-in`** (`post-vau-opt-in`): security `BearerAuth`; required parameters `cardID` (path); required body fields none declared; response statuses 200, 401, 403, 404, 500; error codes in examples none; events `cards-automatic-updater-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-vau-opt-in` | `cards-automatic-updater-1` |
| `post-vau-opt-out` | `cards-automatic-updater-1` |
| `create-a-cardsonfile` | `cardsonfile-provision-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/pismo-card-on-file.md`: updatedAt 2026-05-28T17:12:58.000Z.
- `docs/card-issuing/automatic-updater.md`: updatedAt 2026-07-22T22:27:33.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/pismo-card-on-file.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pismo-card-on-file | `3213b82d3d411f05…` | 2026-05-28T17:12:58.000Z |
| `docs/card-issuing/automatic-updater.md` | whole document | https://developers.pismo.io/pismo-docs/docs/automatic-updater | `a05d26eea97670b7…` | 2026-07-22T22:27:33.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--automatic-updater` — API reference: Card issuing - Cards — Automatic updater
- `KU-API-card-issuing-cards-on-file--cards-on-file` — API reference: Card issuing - Cards on file — Cards on file
- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-EVT-catalogue-cardsonfile` — Event catalogue: cardsonfile
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
