---
ku_id: KU-CARD-bin-override-feature
title: BIN override - shared account option
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/bin-override-feature.md
  sha256: bb15a30b65696fee8211355c3bf0373bdea07cf27af4d34662e6005fbe02b344
  url: https://developers.pismo.io/pismo-docs/docs/bin-override-feature
  role: primary_guide
  updated_at: '2026-03-18T15:21:50.000Z'
operations:
- get-card-template-by-id
- get-card-templates
- post-v1-card-reissue
- post-v2-card
related_kus:
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-cards--cards
- KU-API-card-issuing-cards--templates
- KU-EVT-catalogue-cards
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# BIN override - shared account option

**KU ID:** `KU-CARD-bin-override-feature` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/bin-override-feature.md`:

> BIN (bank identification number) values, used to generate a card's Primary Account Number (PAN) at [card creation](https://developers.pismo.io/pismo-docs/reference/post-v2-card), are currently configured at the program level along with type (credit or debit). Accounts and cards created under a program share the same type.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/bin-override-feature.md`: BIN override - shared account option; Create a BIN override template; Override API endpoints

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/bin-override-feature.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/bin-override-feature · updatedAt: 2026-03-18T15:21:50.000Z

<!-- source:begin path=docs/card-issuing/bin-override-feature.md part=0-end -->

# BIN override - shared account option

BIN (bank identification number) values, used to generate a card's Primary Account Number (PAN) at [card creation](https://developers.pismo.io/pismo-docs/reference/post-v2-card), are currently configured at the program level along with type (credit or debit). Accounts and cards created under a program share the same type.

With BIN override, different cards can be tied to the same account and jointly consume the same account balance. For example, a prepaid virtual card could consume the same balance as a debit card.

The BIN override feature is implemented through templates, refer to the [Create a BIN override template](https://developers.pismo.io/pismo-docs/docs/bin-override-feature#create-a-bin-override-template) below.

**BIN override example**

1. You have a program Y and account configured as type debit with  BIN = 123456.

2. You have a program X configured for prepaid virtual cards with BIN = 867654.

3. You create a template with BIN=867654.

4. Using your new template, you issue a prepaid virtual card under the program Y account that will share that account's balances. The template is used to override the program/account's default BIN values (123456).

**Range override example**

1. You have a program X with BIN = 123456 and range= 0 - 500000000.

2. You create a template  with BIN = 123456 and range= 500000001 - 999999999.

3. You create a card with the template for a program X account - the BIN will be the same as program X's but the range will be different. For example, the PAN could be 1234566879541234, where 123456 is the BIN, 687954123 is the range and 4 is the check digit.

**Program override example**

A template is created that points to an existing program, but with  different BIN and ranges.

1. You have a program Y with BIN = 852456 and range from 0 to 699999999.

2. You have a program X with BIN = 123456 and range from 0 to 500000000.

3. You create a template with BIN = 852456 (same as program Y) and range from 700000000 to 999999999.

4. You create a card with the template for a program X account - the BIN will be the same as program Y's but the range will be different. For example, the PAN could be 8524567854625815, where  852456 is the BIN, 785462581 is the range and 5 is the check digit. The card's program is Y, while its account is linked to program X.

***

For all override scenarios, as much as the PANs are different from the program's configuration, whether for BIN or range reasons, the card is always linked to the same account and consumes the same balance or limit.

The fees used for withdrawal for example, are always those of the program linked to the card. For the program override example, even though the card is linked to a program X account, the fees used will be from program Y. In the BIN and range override examples, the fees will be from program X.

***

## Create a BIN override template

To create a BIN override template, contact the Pismo [Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk) and request one. The ticket type should be **Settings**.

**Template fields**

| Field                 | Type   | Description         | Example                                   |
| :-------------------- | :----- | :------------------ | :---------------------------------------- |
| `template_id`         | string | Template ID         | "EAFA693A-57B2-4029-97F3-D20D6F06D79B"    |
| `org_id`              | string | Organization ID     | "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `override_program_id` | number | Program ID          | 8675                                      |
| `bin`                 | string | BIN number          | "86753092"                                |
| `bin_range_beginning` | string | Beginning BIN range | "100"                                     |
| `bin_range_end`       | string | End BIN range       | "1500000"                                 |

### Override API endpoints

The following endpoints pertain to the BIN override feature:

* [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card)—You can specify a template to override BIN values when creating a card.
* [Get card template](https://developers.pismo.io/pismo-docs/reference/get-card-template-by-id)—Get a specific template.
* [Get card templates](https://developers.pismo.io/pismo-docs/reference/get-card-templates)—Get all your organization's templates with paging options.
* [Reissue card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue)—Reissue card with template option.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /wallet/v2/cards` | `post-v2-card` | Create card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `GET /cards/v1/templates/{templateID}` | `get-card-template-by-id` | Get card template | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--templates |
| `GET /cards/v1/templates` | `get-card-templates` | List card templates | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--templates |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` | `post-v1-card-reissue` | Reissue card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |

### Operation essentials

- **`POST /wallet/v2/cards`** (`post-v2-card`): security `BearerAuth`; required parameters `x-customer-id` (header); required body fields `name`, `type`; response statuses 200, 201, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`.
- **`GET /cards/v1/templates/{templateID}`** (`get-card-template-by-id`): security `BearerAuth`; required parameters `templateID` (path); required body fields none declared; response statuses 200, 400, 404, 409, 500; error codes in examples none; events none listed.
- **`GET /cards/v1/templates`** (`get-card-templates`): security `BearerAuth`; required parameters `page_size` (query); required body fields none declared; response statuses 200, 400, 404, 409, 500; error codes in examples none; events none listed.
- **`POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue`** (`post-v1-card-reissue`): security `BearerAuth`; required parameters `customerId` (path), `accountId` (path), `cardId` (path); required body fields `reason_id`; response statuses 200, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`, `cards-update-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-card-reissue` | `cards-create-1` |
| `post-v2-card` | `cards-create-1` |
| `post-v1-card-reissue` | `cards-update-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/bin-override-feature.md`: updatedAt 2026-03-18T15:21:50.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/bin-override-feature.md` | whole document | https://developers.pismo.io/pismo-docs/docs/bin-override-feature | `bb15a30b65696fee…` | 2026-03-18T15:21:50.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-card-issuing-cards--templates` — API reference: Card issuing - Cards — Templates
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
