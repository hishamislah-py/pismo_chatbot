---
ku_id: KU-CARD-protection-bulletin
title: Protection Bulletin
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/protection-bulletin.md
  sha256: c44ae1d3dc53d714914b007be1b1635a4e93961f61047e969344f2ed493cc54f
  url: https://developers.pismo.io/pismo-docs/docs/protection-bulletin
  role: primary_guide
  updated_at: '2026-06-11T18:14:28.000Z'
operations:
- post-v1-bulletin
- post-v1-bulletin-setup
related_kus:
- KU-API-card-issuing-protection-bulletin--bulletin
- KU-API-card-issuing-protection-bulletin--rules
- KU-EVT-catalogue-cards
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Protection Bulletin

**KU ID:** `KU-CARD-protection-bulletin` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/protection-bulletin.md`:

> Occasionally, a card issuer could go offline or be otherwise unavailable. A mechanism known as the *Protection Bulletin* is used in this situation.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/protection-bulletin.md`: Protection Bulletin; Add a card to the Protection Bulletin

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/protection-bulletin.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/protection-bulletin · updatedAt: 2026-06-11T18:14:28.000Z

<!-- source:begin path=docs/card-issuing/protection-bulletin.md part=0-end -->

# Protection Bulletin

Occasionally, a card issuer could go offline or be otherwise unavailable. A mechanism known as the *Protection Bulletin* is used in this situation.

The Protection Bulletin is consulted before a transaction takes place in cases where the issuer is temporarily offline and unable to authorize or decline an authorization. In a process known as *stand-in*, the card network authorizes or declines the transaction to avoid creating problems for the cardholder and merchant based on how the card was added to the Protection Bulletin. Once the issuer is back online, the card network lets them know what was authorized or declined while they were down.

Pismo provides a [Protection Bulletin API](https://developers.pismo.io/pismo-docs/reference/post-v1-bulletin)  to register and manage cards with the Protection Bulletin.

# Add a card to the Protection Bulletin

You can add a card to the Protection Bulletin in two ways:

* Directly with the [Register card with Protection Bulletin](https://developers.pismo.io/pismo-docs/reference/post-v1-bulletin)  endpoint.
* Set a[ card rule ](https://developers.pismo.io/pismo-docs/reference/post-v1-bulletin-setup)—when  a card status changes to the rule's configured status, it is automatically added to the Protection Bulletin.\
  When a card status is updated, it generates a [Card updated](https://developers.pismo.io/events/docs/cards-update-1)   event. The Pismo platform then adds the card to the Protection Bulletin if it meets a rule's status change condition.

For both the [register](https://developers.pismo.io/pismo-docs/reference/post-v1-bulletin) and [rule](https://developers.pismo.io/pismo-docs/reference/post-v1-bulletin-setup) endpoints, parameter objects are provided for each network brand—ELO, Mastercard, and Visa.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/bulletin` | `post-v1-bulletin` | Register card with Protection Bulletin | `api-specs/Card_issuing_-_Protection_Bulletin.yaml` | no | KU-API-card-issuing-protection-bulletin--bulletin |
| `POST /v1/bulletin/setup` | `post-v1-bulletin-setup` | Create Protection Bulletin rule | `api-specs/Card_issuing_-_Protection_Bulletin.yaml` | no | KU-API-card-issuing-protection-bulletin--rules |

### Operation essentials

- **`POST /v1/bulletin`** (`post-v1-bulletin`): security `BearerAuth`; required parameters `Authorization` (header), `x-customer-id` (header); required body fields none declared; response statuses 201, 400, 401, 404, 422, 500, 504; error codes in examples `EBLT0003`, `EBLT0005`, `EBLT0006`, `EBLT0007`, `EBLT0009`, `BBLT0001`, `BBLT0003`, `BBLT0004`, `BBLT0005`, `EBLT9998`, `EBLT9999`, `EBLT0001`; events none listed.
- **`POST /v1/bulletin/setup`** (`post-v1-bulletin-setup`): security `BearerAuth`; required parameters `Authorization` (header); required body fields none declared; response statuses 202, 400, 401, 404, 422, 500, 504; error codes in examples `EBLT0003`, `EBLT0005`, `EBLT0006`, `EBLT0007`, `EBLT0009`, `BBLT0001`, `BBLT0006`, `EBLT9998`, `EBLT9999`, `EBLT0001`; events `bulletin-bulletin-rule-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-bulletin-setup` | `bulletin-bulletin-rule-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `cards-update-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-update-1 | 11 | KU-EVT-catalogue-cards |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/protection-bulletin.md`: updatedAt 2026-06-11T18:14:28.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/protection-bulletin.md` | whole document | https://developers.pismo.io/pismo-docs/docs/protection-bulletin | `c44ae1d3dc53d714…` | 2026-06-11T18:14:28.000Z |

## Related knowledge units

- `KU-API-card-issuing-protection-bulletin--bulletin` — API reference: Card issuing - Protection Bulletin — Bulletin
- `KU-API-card-issuing-protection-bulletin--rules` — API reference: Card issuing - Protection Bulletin — Rules
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
