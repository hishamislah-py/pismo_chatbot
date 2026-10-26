---
ku_id: KU-CARD-card-network-integration
title: Card network integration and certification
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/card-network-integration.md
  sha256: 91e202e68a01586cd5bd0bb32eefa49a8c9fcabe1d0191181e8eb03c33b3266d
  url: https://developers.pismo.io/pismo-docs/docs/card-network-integration
  role: primary_guide
  updated_at: '2026-03-18T15:20:04.000Z'
- path: docs/card-issuing/network-certification.md
  sha256: 4019538ba481ce4fdfa6e5702f5282f7278e5e7528a1c838d0dbadca94c227f8
  url: https://developers.pismo.io/pismo-docs/docs/network-certification
  role: primary_guide
  updated_at: '2026-03-18T15:19:54.000Z'
operations: []
related_kus:
- KU-CARD-authorization-events
- KU-CARD-cryptographic-keys
- KU-CARD-full-and-zero-balance-workflows
- KU-CARD-full-balance-versus-zero-balance
- KU-RPT-scheduled-reports
grouping_rationale: Integration and certification.
---

# Card network integration and certification

**KU ID:** `KU-CARD-card-network-integration` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Integration and certification.

Scope as stated in `docs/card-issuing/card-network-integration.md`:

> The Pismo platform can handle  Visa, Mastercard, or private label issuing of credit, debit, and prepaid cards. Pismo acts as a transaction processor that integrates with the card networks and the card issuers and guarantees the integrity of card network transactions. The Pismo native-cloud platform can handle up to 15,000 authorizations/transactions per second for multiple accounts.

Scope as stated in `docs/card-issuing/network-certification.md`:

> Network certification for a card issuer refers to the process of obtaining approval from a payment network, such as Visa or Mastercard, to issue credit or debit cards that can be used within their network. Though you are responsible for getting network certified, a Pismo representative will help guide you through the process.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/card-network-integration.md`: Card network integration; Full versus Zero balance integration; Full versus Zero balance workflow; Data and reporting; Card network authorizations and transactions
- `docs/card-issuing/network-certification.md`: Card network certification; Certification process

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/card-network-integration.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/card-network-integration · updatedAt: 2026-03-18T15:20:04.000Z

<!-- source:begin path=docs/card-issuing/card-network-integration.md part=0-end -->

# Card network integration

The Pismo platform can handle  Visa, Mastercard, or private label issuing of credit, debit, and prepaid cards. Pismo acts as a transaction processor that integrates with the card networks and the card issuers and guarantees the integrity of card network transactions. The Pismo native-cloud platform can handle up to 15,000 authorizations/transactions per second for multiple accounts.

Pismo processes all event-dependent functions asynchronously so your customers can see everything changing in real time in their apps. This means all impacts to your accounting, regulatory reports, and treasury also happen in real time.

For details on the various suported card networks, refer to <a href="https://developers.pismo.io/pismo-docs/docs/card-issuing-with-pismo#card-networks-pismo-supports">card networks Pismo supports</a>.

## Full versus Zero balance integration

The Pismo platform supports two card network integration models:

**Full balance integration** —Pismo performs all the necessary card and account validations to authorize or reject a transaction. In addition, the Pismo platform performs all the processing that controls the balance for an account in its life cycle, hence the name *Full* balance.

**Zero balance integration**—Pismo performs some card validations. It also integrates with a card issuer that performs the necessary account validations to authorize or reject a transaction. In this model, the issuer does their own limit/fraud checks, and account management.

For more information, refer to  [Full balance versus Zero balance integration](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance). This guide details the features that come with each option.

## Full versus Zero balance workflow

The two integration models have slightly different workflows when  interacting with the networks and Pismo. For details on these workflows, refer to [Full and Zero balance transaction workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).

## Data and reporting

The workflows for the two models generate a number of *events*, the data these events generate provide you with comprehensive information for reporting and analytics. You can receive event notifications and data  in real-time (streaming event delivery) or periodically via batch files. For more details on this and how to set up event notification delivery, refer to [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

To learn about events specific to card network integration, refer to [Authorization events](https://developers.pismo.io/pismo-docs/docs/authorization-events).

## Card network authorizations and transactions

The Pismo platform supports the following card network authorization/transaction types:

* Purchase
* International purchase
* Installments without interest
* Installments with interest
* Withdrawal
* International withdrawal
* Purchase return
* Payment transaction
<!-- source:end -->

### Source 2: `docs/card-issuing/network-certification.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/network-certification · updatedAt: 2026-03-18T15:19:54.000Z

<!-- source:begin path=docs/card-issuing/network-certification.md part=0-end -->

# Card network certification

Network certification for a card issuer refers to the process of obtaining approval from a payment network, such as Visa or Mastercard, to issue credit or debit cards that can be used within their network. Though you are responsible for getting network certified, a Pismo representative will help guide you through the process.

> 📘 Previous network certification
>
> You must certify with the card network with Pismo even if you have already certified with another processor or you have internal processing.

To obtain network certification, you must meet specific payment network requirements, which typically involve compliance with security and processing standards, such as the Payment Card Industry Data Security Standard ([PCI DSS](https://listings.pcisecuritystandards.org/documents/PCI_DSS-QRG-v3_2_1.pdf)). You must also establish a relationship with an acquiring bank that is a payment network member, which enables merchants, who have relationships with the acquiring bank,  to accept the cards.

Once you have received network certification, you can begin issuing credit or debit cards that are branded with the payment network's logo and can be used at merchants that accept the network's cards. You are responsible for complying with the payment network's rules and regulations, including those related to card acceptance, transaction processing, and dispute resolution.

Also, refer to <a href="https://developers.pismo.io/pismo-docs/docs/card-issuing-with-pismo#card-networks-pismo-supports">card networks Pismo supports</a>.

## Certification process

The card network certification process ensures that your cards meet the card network's technical, security and operational requirements, and all  the network's member institutions can process them.

To become card network-certified, you must first submit an application to the card network that includes detailed information about your business, operations, and technical capabilities. The card network then conducts a thorough review of your application, including an assessment of your ability to comply with the card network's rules and regulations, and your ability to ensure cardholder data's security and privacy.

Once you have passed the initial review process, you must complete a series of technical tests to ensure that your card processing systems are compatible with the card network. These tests typically cover a range of areas, including card authorization and settlement, transaction processing, and data security.

> 📘 Cryptography
>
> Part of certification involves a [Cryptographic process with Pismo and the card network](https://developers.pismo.io/pismo-docs/docs/cryptographic-keys).

Finally, you must demonstrate your ability to meet the card network's operational and customer service standards, including your ability to provide timely and accurate reporting, manage fraud and chargebacks, and maintain customer satisfaction.

Upon successfully completing the card network certification process, you are granted a card network <a href="https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp" target="_blank">Issuer Identification Number</a> (IIN), which enables you to issue cards that can be used on the card network. You are also required to maintain ongoing compliance with the card network's rules and regulations, and to undergo periodic reviews and audits to ensure continued compliance.
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/card-network-integration.md`: updatedAt 2026-03-18T15:20:04.000Z.
- `docs/card-issuing/network-certification.md`: updatedAt 2026-03-18T15:19:54.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/card-network-integration.md` | whole document | https://developers.pismo.io/pismo-docs/docs/card-network-integration | `91e202e68a01586c…` | 2026-03-18T15:20:04.000Z |
| `docs/card-issuing/network-certification.md` | whole document | https://developers.pismo.io/pismo-docs/docs/network-certification | `4019538ba481ce4f…` | 2026-03-18T15:19:54.000Z |

## Related knowledge units

- `KU-CARD-authorization-events` — Authorization events
- `KU-CARD-cryptographic-keys` — Cryptographic process with Pismo and the card network
- `KU-CARD-full-and-zero-balance-workflows` — Full and Zero balance transaction workflows
- `KU-CARD-full-balance-versus-zero-balance` — Full balance versus Zero balance integration
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
