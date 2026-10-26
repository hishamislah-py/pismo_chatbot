---
ku_id: KU-CARD-full-and-zero-balance-workflows
title: Full and Zero balance transaction workflows
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/full-and-zero-balance-workflows.md
  sha256: 625f5062dd2b18cc8947389b66482b6d56f760466bf3e583cbe5dae215b41655
  url: https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows
  role: primary_guide
  updated_at: '2026-06-08T15:37:46.000Z'
operations: []
related_kus:
- KU-CARD-anti-fraud-integration
- KU-CARD-authorization-events
- KU-CARD-authorization-validation-rules-for-card-network-operations
- KU-CARD-clearing
- KU-CARD-zero-balance-integration
- KU-EVT-catalogue-other-domains
- KU-EVT-client-webhooks-part-01
- KU-EVT-client-webhooks-part-02
- KU-EVT-client-webhooks-part-03
- KU-EVT-client-webhooks-part-04
- KU-EVT-client-webhooks-part-05
- KU-EVT-client-webhooks-part-06
- KU-EVT-client-webhooks-part-07
- KU-EVT-client-webhooks-part-08
- KU-EVT-client-webhooks-part-09
- KU-EVT-client-webhooks-part-10
- KU-EVT-client-webhooks-part-11
- KU-EVT-client-webhooks-part-12
- KU-EVT-client-webhooks-part-13
- KU-EVT-client-webhooks-part-14
grouping_rationale: single source page
---

# Full and Zero balance transaction workflows

**KU ID:** `KU-CARD-full-and-zero-balance-workflows` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/full-and-zero-balance-workflows.md`:

> This guide explains how fund transfers are processed on the Pismo platform through Full balance and Zero balance integration models. These workflows involve three key components: authorization, clearing, and transaction creation.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/full-and-zero-balance-workflows.md`: Full and Zero balance transaction workflows; Authorization/Base I; Clearing/Base II; Transaction creation

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/full-and-zero-balance-workflows.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows · updatedAt: 2026-06-08T15:37:46.000Z

<!-- source:begin path=docs/card-issuing/full-and-zero-balance-workflows.md part=0-end -->

# Full and Zero balance transaction workflows

<Image alt="Full and zero balance workflows" align="center" src="https://files.readme.io/068018e-diagram-authorization-workflow.png" />

<br />

This guide explains how fund transfers are processed on the Pismo platform through Full balance and Zero balance integration models. These workflows involve three key components: authorization, clearing, and transaction creation.

Authorization (Base I): The initial step where a transaction request is validated and approved by the issuer.\
Clearing (Base II): The process of finalizing and posting the transaction after authorization.\
Transaction Creation: Recording the transaction details for accounting and reporting purposes.

Throughout this guide, you’ll learn how these steps differ between Full balance and Zero balance integrations, including validation rules, anti-fraud checks, and issuer responsibilities.

Fund transfers into or out of an account generate two types of records:

* **Authorization**—A record stating that a given amount was authorized for adding to, or taking from, an account. It contains information about its nature, such as the amount, local currency, date and time, and applicable fees.\
  In the Pismo authorization workflow:
  * Authorization/Base I—The initial request to the issuer to approve a transaction process.
  * [Clearing/Base II](https://developers.pismo.io/pismo-docs/docs/clearingbase)—Finalizing and posting the transaction process.

* **Transaction**— Belongs to one particular authorization - part of a complete purchase or funds transfer. It can correspond to a purchase installment, a fee amount, a statement payment, or a transfer between accounts, among other things.

## Authorization/Base I

The following is the Authorization/Base I workflow for both Full balance and Zero balance integrations.

**Note**: This guide details the events that Pismo generates during the authorization and clearing process, for more information on these events, refer to [Authorization events](https://developers.pismo.io/pismo-docs/docs/authorization-events).

1. User provides merchant with card information.
2. Merchant's point-of-sale (POS) device or payment gateway formats a message with an authorization request and sends it to the acquirer. Acquirers own most POS devices.
3. Acquirer sends a message to the card network which then sends a message to the processor, the Pismo platform.
4. Pismo removes sensitive data from the message and generates a [Network authorization ISO8583 message received](https://developers.pismo.io/events/docs/networktransactions-iso8583-message-1) event.

   **Zero balance** receives this event and it also receives the raw message when Pismo calls the issuer's webhook in Step 5. Refer to the [Zero balance validations request](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook) details to review this call's details.
5. Pismo performs validations and, for **Full balance**, does anti-fraud and account and balance checks.

* **Full balance**—Card validations (stateful) plus balance and account checks (stateless) and anti-fraud checks. Pismo calls issuer's anti-fraud webhook with its results which the issuer can override. For more information, refer to [Anti-fraud integration](https://developers.pismo.io/pismo-docs/docs/anti-fraud-integration). Note that this integration is **optional**. if you do not provide a webhook, Pismo responds to the network with its own results.
* **Zero balance**—Basic validations - Primary Account Number (PAN),  Card Verification Value (CVV), etc. (stateless). If card  validation fails, go to step 6, Pismo does not need to call the issuer in this case. Otherwise, Pismo calls the issuer's webhook so they can do their own anti-fraud checks and account and balance checks.  Refer to [Zero balance anti-fraud and validations integration](https://developers.pismo.io/pismo-docs/docs/zero-balance-anti-fraud-integration-1) for more information.
* **Response time**—For both Full and Zero balance customers, the issuer has 2 seconds to respond to a customer webhook call.
* **Validations**—For more information on validations, refer to [Authorization validation rules](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations).

6. Pismo gets response message from issuer (if called) and responds to network. Pismo generates a [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event and a [Card network authorization return sent](https://developers.pismo.io/events/docs/networktransactions-network-message-1) event.
7. The card network sends back the response to the acquirer, who then sends the message to the merchant.

## Clearing/Base II

Pismo downloads the Clearing/Base II files and generates a [Network authorization clearing message received](https://developers.pismo.io/events/docs/networktransactions-clearing-1) and additional `raw_` messages. Refer to [clearing messages](https://developers.pismo.io/pismo-docs/docs/authorization-events#clearingbase-ii-events) for more information.

* For **Full balance** customers, Pismo does all accounting, ledger, and credit and debit settlement. It also generates a confirmation [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event.
* **Zero balance** customers get the clearing events, but have to do their own account and balance settlement.

For more information, refer to [Clearing/Base II](https://developers.pismo.io/pismo-docs/docs/clearingbase).

## Transaction creation

* **Full balance**—For an approved authorization, Pismo creates a transaction and generates a create transaction event.
* **Zero balance**—Issuers need to create the transaction themselves.
<!-- source:end -->

## Events

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `networktransactions-network-authorization-1` | networktransactions | 1 | https://developers.pismo.io/events/docs/networktransactions-network-authorization-1 | 2 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/full-and-zero-balance-workflows.md`: updatedAt 2026-06-08T15:37:46.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 4 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/full-and-zero-balance-workflows.md` | whole document | https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows | `625f5062dd2b18cc…` | 2026-06-08T15:37:46.000Z |

## Related knowledge units

- `KU-CARD-anti-fraud-integration` — Anti-fraud integration
- `KU-CARD-authorization-events` — Authorization events
- `KU-CARD-authorization-validation-rules-for-card-network-operations` — Authorization validation rules for card network operations
- `KU-CARD-clearing` — Clearing: Base II and the clearing rules engine
- `KU-CARD-zero-balance-integration` — Zero balance integration and anti-fraud validations
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-EVT-client-webhooks-part-02` — Client webhooks (part 2 of 14)
- `KU-EVT-client-webhooks-part-03` — Client webhooks (part 3 of 14)
- `KU-EVT-client-webhooks-part-04` — Client webhooks (part 4 of 14)
- `KU-EVT-client-webhooks-part-05` — Client webhooks (part 5 of 14)
- `KU-EVT-client-webhooks-part-06` — Client webhooks (part 6 of 14)
- `KU-EVT-client-webhooks-part-07` — Client webhooks (part 7 of 14)
- `KU-EVT-client-webhooks-part-08` — Client webhooks (part 8 of 14)
- `KU-EVT-client-webhooks-part-09` — Client webhooks (part 9 of 14)
- `KU-EVT-client-webhooks-part-10` — Client webhooks (part 10 of 14)
- `KU-EVT-client-webhooks-part-11` — Client webhooks (part 11 of 14)
- `KU-EVT-client-webhooks-part-12` — Client webhooks (part 12 of 14)
- `KU-EVT-client-webhooks-part-13` — Client webhooks (part 13 of 14)
- `KU-EVT-client-webhooks-part-14` — Client webhooks (part 14 of 14)
