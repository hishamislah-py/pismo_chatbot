---
ku_id: KU-CARD-card-scripts
title: Card scripts
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/card-scripts.md
  sha256: 11b7742d5476034cc4e7d6562a135be954f628ac9a1676753571bb976eca7937
  url: https://developers.pismo.io/pismo-docs/docs/card-scripts
  role: primary_guide
  updated_at: '2026-03-18T15:21:51.000Z'
operations:
- post-v1-append-update-pin-script
related_kus:
- KU-API-card-issuing-cards--pci
grouping_rationale: single source page
---

# Card scripts

**KU ID:** `KU-CARD-card-scripts` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/card-scripts.md`:

> As an issuer, you have the option to run configured scripts for physical, embossed cards that will be applied at the card's next authorization. Contact your Pismo representative to set this up.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/card-scripts.md`: Card scripts; Script scenario; Notes; Card script endpoints

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/card-scripts.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/card-scripts · updatedAt: 2026-03-18T15:21:51.000Z

<!-- source:begin path=docs/card-issuing/card-scripts.md part=0-end -->

# Card scripts

As an issuer, you have the option to run configured scripts for physical, embossed cards that will be applied at the card's next authorization. Contact your Pismo representative to set this up.

Pismo currently supports the following scripts:

**Mastercard**

* PIN change/unblock (Support: Cryptographic Version Number (CVN) 10 - We support the execution of script to change password offline, the password contained in the chip, only for CVN 10.)

**Visa**

* PIN change/unblock (Support: CVN10) - Same as Mastercard )

## Script scenario

**Update card password**

Another scenario is for customers who work with an offline password validated directly at the point-of-sale (POS). In this scenario, customers work with the [CMV](https://www.emv-connection.com/cardholder-verification-methods-concepts-implementations-and-impacts/)  (Card Method Verification) using an offline password first and then online password validation, that is, after 3 wrong cardholder attempts, the 4th transaction will have online password validation, making it possible to execute a script directly on the chip to change the password offline.

For this, the issuer **must** pre-register a card password that includes a script for changing the password that is added to the card's chip. The next time the cardholder executes a transaction, the script is returned in the message to the POS and executed, which changes the password to the pre-registered one.

## Notes

* For any script option, the card must support it and during configuration you will need to define these points.
* For any issuer wishing to work with a script, a physical card generated and embossed for the EXT environment must be sent to Pismo to carry out the necessary validations and tests.

## Card script endpoints

* [Append update PIN issuer script](https://developers.pismo.io/pismo-docs/reference/post-v1-append-update-pin-script)—Append issuer script to update the card PIN that will be applied at the next authorization.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /pcicards/v1/pcicards/{cardId}/scripts/pin-update` | `post-v1-append-update-pin-script` | Append update PIN script | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |

### Operation essentials

- **`POST /pcicards/v1/pcicards/{cardId}/scripts/pin-update`** (`post-v1-append-update-pin-script`): security `BearerAuth`; required parameters `cardId` (path), `x-account-id` (header); required body fields `script_id`; response statuses 200, 400, 401, 403, 404, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/card-issuing/card-scripts.md`: updatedAt 2026-03-18T15:21:51.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/card-scripts.md` | whole document | https://developers.pismo.io/pismo-docs/docs/card-scripts | `11b7742d5476034c…` | 2026-03-18T15:21:51.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--pci` — API reference: Card issuing - Cards — PCI
