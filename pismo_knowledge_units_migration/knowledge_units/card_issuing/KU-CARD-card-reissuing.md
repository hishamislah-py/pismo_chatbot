---
ku_id: KU-CARD-card-reissuing
title: Card reissuing
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/card-reissuing.md
  sha256: 3b620f98ac7204da88d5389a33b4c528e21f307896c4c44b1be4c18b5277a379
  url: https://developers.pismo.io/pismo-docs/docs/card-reissuing
  role: primary_guide
  updated_at: '2026-05-20T23:25:13.000Z'
operations:
- create-reissue-reason
- get-reissue-reasons
- get-v1-card-reissue-reasons
- get-v2-card-password
- post-v1-card-reissue
- post-v2-card-bind
- put-v2-card-password
- transfertokens
related_kus:
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-cards--noname
- KU-API-card-issuing-cards--pci
- KU-API-card-issuing-tokenization--card-lifecycle
- KU-EVT-catalogue-cards
- KU-GS-program-types
grouping_rationale: single source page
---

# Card reissuing

**KU ID:** `KU-CARD-card-reissuing` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/card-reissuing.md`:

> Similar to your embossing configuration, you need to personalize the card reissuing configuration and process for your brand as every brand has different reissue reasons and associated costs. After setting up your [card program](https://developers.pismo.io/pismo-docs/docs/program-types), meet with your Pismo representative to configure this.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/card-reissuing.md`: Card reissuing; Transferring PIN, tokens,  and PAN when a card is reissued; Card reissue scenarios and statuses; Card reissue reasons; Mastercard automatic card reissue updates

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 8 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/card-reissuing.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/card-reissuing · updatedAt: 2026-05-20T23:25:13.000Z

<!-- source:begin path=docs/card-issuing/card-reissuing.md part=0-end -->

# Card reissuing

Similar to your embossing configuration, you need to personalize the card reissuing configuration and process for your brand as every brand has different reissue reasons and associated costs. After setting up your [card program](https://developers.pismo.io/pismo-docs/docs/program-types), meet with your Pismo representative to configure this.

You can call the following card API endpoints to view your reissuing configuration and reissue a card:

* [Get card reissue reasons](https://developers.pismo.io/pismo-docs/reference/get-v1-card-reissue-reasons)—Issuer-defined card reissue reasons and actions
* [Reissue card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue)—Reissue a card. Reissuing a physical card initiates the embossing process.

# Transferring PIN, tokens,  and PAN when a card is reissued

When creating or reissuing a Pismo card, a new PAN and PIN are generated randomly. For a new card's PIN to be the same as the old card's, you **must** manually change the new card's password to the old card's password.

**To transfer a card's password (PIN):**

1. Call [Get card password](https://developers.pismo.io/pismo-docs/reference/get-v2-card-password) to get the old card's password.
2. Call [Change card password ](https://developers.pismo.io/pismo-docs/reference/put-v2-card-password)to update the new card's password to the old card's password.

**To transfer a card's tokens:**

1. Call [Reissue card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue)  and set the `update_tokens` parameter to `true`.
2. Alternatively, reissue the card and then call [Transfer card tokens ](https://developers.pismo.io/pismo-docs/reference/transfertokens).

There currently is no way to transfer a card's PAN to a reissued card.

# Card reissue scenarios and statuses

**Scenario 1 - physical**:

1. Card created (`CREATED`) and activated (`NORMAL`)
2. Card reissued with `must_block` = `true`(`CANCELLED`). (The reissue reason object contains the `must_block` field).
3. New card created (`CREATED`) and activated (`NORMAL`)

**Scenario 2 - physical**:

1. Card created (`CREATED`) and activated (`NORMAL`)
2. Card reissued with `must_block` = `false`(`REISSUED`)
3. New card created (`CREATED`) and activated (`NORMAL`)
4. Old card cancelled (`REISSUED`,`NORMAL`, `BLOCKED`, `PENDING`, or `WARNING`) > (`CANCELLED`)

**Scenario 3 - physical**:

1. Card created (`CREATED`), activated (`NORMAL`), and blocked (`BLOCKED`)
2. Card reissued with `must_block` = `false`, card remains with the same status (`BLOCKED`)
3. New card created (`CREATED`) and activated (`NORMAL`)
4. Old card canceled (`REISSUED`, `NORMAL`, `BLOCKED`, `PENDING`, or `WARNING`) > (`CANCELED`)

**Scenario 4 - virtual**:

1. Card created and activated automatically (`NORMAL`)
2. Card reissued with `must_block = true` or `must_block` = `false`(`CANCELLED`). (The `must_block` flag is a field in the reissue reason object.)
3. New card created (`CREATED`) and activated (`NORMAL`)

**Scenario 5 - physical**:

1. Card created (`CREATED`) and activated (`NORMAL`)
2. Card in some final status (for example, `THEFT`)
3. Card reissued
4. New card created (`CREATED`) and activated (`NORMAL`)
5. Old card stays with the same status (`THEFT`)

**Scenario 6 - physical:**

1. Card created (`CREATED`)
2. Card reissued with `must_block` = `true` or `must_block` = `false` (`CANCELED`). (The `must_block` flag is a field in the reissue reason object.) .
3. New card created (`CREATED`) and activated `(NORMAL`) .
4. Old card stays with the same status (`CANCELED`).

**Note:** For reissued cards that remain in the same status, the card update event is not sent, i.e., scenarios 3, 5 and 6.

> 📘 Reissuing card to a noname card
>
> You can use the [Associate noname card with customer ](https://developers.pismo.io/pismo-docs/reference/post-v2-card-bind)endpoint to reissue a card to a noname card as long as that noname card has not previously been associated and still has an `UNBOUND` status.

# Card reissue reasons

You can call [Create reissue reason](https://developers.pismo.io/pismo-docs/reference/create-reissue-reason) to create your own reasons for reissuing a card. Each reason has a `reason_id`field identifier that you can pass when calling the [Reissue card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue)  endpoint. You can configure your initial reasons as part of the beginning setup process with your Pismo representative. To get your organization's reasons, call [List reissue reasons](https://developers.pismo.io/pismo-docs/reference/get-reissue-reasons).

# Mastercard automatic card reissue updates

This service is offered in partnership with **Mastercard** to simplify a customer's life.  When a new customer card number is issued, it is automatically updated on the various websites, applications, and digital services where the customer already has a record with the old card.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /wallet/v1/cards/reissue/reasons` | `get-v1-card-reissue-reasons` | Get card reissue reasons (outdated) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` | `post-v1-card-reissue` | Reissue card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `GET /pcicards/v2/pcicards/password/{cardId}` | `get-v2-card-password` | Get card password | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |
| `PUT /pcicards/v2/pcicards/card/{cardId}` | `put-v2-card-password` | Change card password | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |
| `POST /v1/cards/{cardId}/network-tokens/pan-update` | `transfertokens` | Transfer card tokens to other card | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--card-lifecycle |
| `PUT /wallet/v2/cards/{cardId}/noname/bind` | `post-v2-card-bind` | Associate noname card with customer | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--noname |
| `POST /cards/v1/reissue/reasons` | `create-reissue-reason` | Create reissue reason | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `GET /cards/v1/reissue/reasons` | `get-reissue-reasons` | List reissue reasons | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |

### Operation essentials

- **`GET /wallet/v1/cards/reissue/reasons`** (`get-v1-card-reissue-reasons`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 401, 403, 404, 500; error codes in examples none; events none listed.
- **`POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue`** (`post-v1-card-reissue`): security `BearerAuth`; required parameters `customerId` (path), `accountId` (path), `cardId` (path); required body fields `reason_id`; response statuses 200, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`, `cards-update-1`.
- **`GET /pcicards/v2/pcicards/password/{cardId}`** (`get-v2-card-password`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 401, 404, 409, 500; error codes in examples none; events none listed.
- **`PUT /pcicards/v2/pcicards/card/{cardId}`** (`put-v2-card-password`): security `BearerAuth`; required parameters `cardId` (path); required body fields `pin`; response statuses 201, 401, 403, 404, 500; error codes in examples none; events `cards-update-password-1`.
- **`POST /v1/cards/{cardId}/network-tokens/pan-update`** (`transfertokens`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 202, 400, 401, 500; error codes in examples `ERR93836`, `ERR9786`, `ERR5446`; events `cards-tokenization-pan-update-1`.
- **`PUT /wallet/v2/cards/{cardId}/noname/bind`** (`post-v2-card-bind`): security `BearerAuth`; required parameters `cardId` (path), `x-account-id` (header), `x-customer-id` (header); required body fields none declared; response statuses 202, 400, 401, 403, 409, 500; error codes in examples none; events `cards-bind-card-1`, `cards-create-1`, `cards-update-1`.
- **`POST /cards/v1/reissue/reasons`** (`create-reissue-reason`): security `BearerAuth`; required parameters none declared; required body fields `description`, `must_block`, `must_charge`, `cost`, `type`, `enabled`; response statuses 201, 400, 401, 500; error codes in examples none; events none listed.
- **`GET /cards/v1/reissue/reasons`** (`get-reissue-reasons`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 500; error codes in examples none; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v2-card-bind` | `cards-bind-card-1` |
| `post-v1-card-reissue` | `cards-create-1` |
| `post-v2-card-bind` | `cards-create-1` |
| `transfertokens` | `cards-tokenization-pan-update-1` |
| `post-v1-card-reissue` | `cards-update-1` |
| `post-v2-card-bind` | `cards-update-1` |
| `put-v2-card-password` | `cards-update-password-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/card-reissuing.md`: updatedAt 2026-05-20T23:25:13.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/card-reissuing.md` | whole document | https://developers.pismo.io/pismo-docs/docs/card-reissuing | `3b620f98ac7204da…` | 2026-05-20T23:25:13.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-cards--noname` — API reference: Card issuing - Cards — Noname
- `KU-API-card-issuing-cards--pci` — API reference: Card issuing - Cards — PCI
- `KU-API-card-issuing-tokenization--card-lifecycle` — API reference: Card issuing - Tokenization — Card lifecycle
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-GS-program-types` — Program types
