---
ku_id: KU-CARD-application-transaction-counter-atc
title: Application Transaction Counter (ATC)
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/application-transaction-counter-atc.md
  sha256: f7d5f128b4a4fc5cce15dac93f19b49ac9aa1e8ceacdfc6a1fc3a43afb43d1e9
  url: https://developers.pismo.io/pismo-docs/docs/application-transaction-counter-atc
  role: primary_guide
  updated_at: '2026-03-18T15:21:48.000Z'
operations:
- post-v2-card-atc-reset
related_kus:
- KU-API-card-issuing-cards--cards
- KU-CC-get-started-control-center
- KU-ERR-validation-code-definitions
- KU-GS-program-types
grouping_rationale: single source page
---

# Application Transaction Counter (ATC)

**KU ID:** `KU-CARD-application-transaction-counter-atc` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/application-transaction-counter-atc.md`:

> The Application Transaction Counter (ATC), is an EMV (Europay, Mastercard and Visa) field defined in the following specification—EMV 4.4 Book 2 - Security and Key Management—as a two-byte counter incremented at the start of a transaction, ranging in  value from 0x0000 to 0xFFFF.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/application-transaction-counter-atc.md`: Application Transaction Counter (ATC); Authorization flow; Examples; ATC denial scenarios; Pismo platform ATC parameters and endpoints

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/application-transaction-counter-atc.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/application-transaction-counter-atc · updatedAt: 2026-03-18T15:21:48.000Z

<!-- source:begin path=docs/card-issuing/application-transaction-counter-atc.md part=0-end -->

# Application Transaction Counter (ATC)

The Application Transaction Counter (ATC), is an EMV (Europay, Mastercard and Visa) field defined in the following specification—EMV 4.4 Book 2 - Security and Key Management—as a two-byte counter incremented at the start of a transaction, ranging in  value from 0x0000 to 0xFFFF.

The card chip processor  checks if a given transaction has an ATC lower than the one currently stored; if so, it may deny the transaction as a <a href="https://www.investopedia.com/terms/c/cloning.asp" target="_blank">cloned card</a> issue or <a href="https://usa.kaspersky.com/resource-center/definitions/replay-attack?srsltid=AfmBOooWHqIPGXV5LnGfSW98x6DWwjZhr9zD2dkR4b4pqHlBsIu1MUSV" target="_blank">replay attack</a>.

> 📘 ATC is required
>
> Using an ATC on the Pismo platform is mandatory.

Internally, the Pismo platform stores an ATC as a string containing an array of around 2000 transaction sequence numbers. For example: "\[5, 4, 3, 2, 1]".  Pismo allocates 10,000 characters for this, so the actual amount of numbers may vary.   If, in an incoming transaction,  the received ATC value repeats a past sequence number, the transaction is denied.

The rationale to store an ATC as a string containing an array of numbers instead of the latest incoming value is to allow for ATC synchronization in situations such as offline purchases. For example—offline purchases on a cruise ship where a few values can be lost until the card is used again on an online machine. Keeping the list of previous ATC numbers helps the Pismo platform determine whether a given transaction fits such a case.

> 📘 Combination cards
>
> For Pismo combination cards, an ATC is kept for each [program type](https://developers.pismo.io/pismo-docs/docs/program-types) —debit and credit. If you call [Reset card ATC](https://developers.pismo.io/pismo-docs/reference/post-v2-card-atc-reset) for a combination card, the access token needs to be encoded with the ID of the account (credit or debit) whose ATC you want to reset.

# Authorization flow

An incoming ATC value, received in a Authorization/Base I <a href="https://en.wikipedia.org/wiki/ISO_8583" target="_blank">ISO8583</a> message, is compared with the last value stored in Pismo's database. The difference between the values, received and stored, must be within the allowed range that is configured for the card with the `ATC MIN OFFSET` and `ATC MAX OFFSET` program parameters.

* `ATC MIN OFFSET`—Number that must be subtracted from the last ATC registered in the database to make up the lower range bound
* `ATC MAX OFFSET`—Number that must be added to the last ATC registered in the database to make up the upper range bound

### Examples

```
Database ATC (Pismo): [64, 63, 62, 61, 60]  
ATC max offset (Pismo): 15  
ATC min offset (Pismo): 5  
Current ATC (incoming from the card network): 81 -> Denied (81 > 64 + 15)  
Current ATC (incoming from the card network): 58 -> Denied (58 < 64 - 5)  
Current ATC (incoming from the card network): 70 -> Approved (64 + 15 > 70 > 64 - 5)  
```

The Pismo platform does not increment the ATC stored on the card chip, the Point of Sale (POS) terminal or ATM does that where the card is used. This information is received from the network and we use the value received to validate it with the previously stored values. In case of success, we store the new ATC received in our database after we receive a message from the authorizer. Otherwise, the transaction is denied with the [custom code `FAT`](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#fat---atc-validation) . E-commerce transactions do not increment the ATC and this information is not present in the message, so we do not validate or update it in our database.

# ATC denial scenarios

For each card swipe at a POS, a new ATC is counted. The ATC can lose synchronization in the situations below, for example, causing a card block and consequently not allowing a transaction.

* If you make purchases with the wrong type (debit type, with credit mode and vice versa), the POS can sometimes deny this and the transaction will not even reach Pismo.
* Installment purchase or withdrawal that is not configured for the program. For example,  when it is configured only for cash purchases.
* Repeated retries in the scenarios above
* An invalid ATC may come (same as the last currently stored or older, due to a buyer shipping error or even fraud)
* From the moment you lose the ATC synchronization, the next purchases will also come with the ATC unsynchronized. In this case you need to reset the ATC (below).

# Pismo platform ATC parameters and endpoints

The ATC minimum and maximum parameters—`ATC MAX OFFSET` and `ATC MIN OFFSET`—can be configured as program parameters via the [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center).

You can use the [Reset card ATC](https://developers.pismo.io/pismo-docs/reference/post-v2-card-atc-reset) endpoint to reset the ATC array. In this case, we continue to validate the ATC parameters (min and max) and store further incoming values starting from the next purchase.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /wallet/v2/cards/{cardId}/atc/reset` | `post-v2-card-atc-reset` | Reset card ATC | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |

### Operation essentials

- **`POST /wallet/v2/cards/{cardId}/atc/reset`** (`post-v2-card-atc-reset`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 403, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/card-issuing/application-transaction-counter-atc.md`: updatedAt 2026-03-18T15:21:48.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/application-transaction-counter-atc.md` | whole document | https://developers.pismo.io/pismo-docs/docs/application-transaction-counter-atc | `f7d5f128b4a4fc5c…` | 2026-03-18T15:21:48.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-ERR-validation-code-definitions` — Validation code definitions
- `KU-GS-program-types` — Program types
