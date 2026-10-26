---
ku_id: KU-CARD-card-lifecycle-and-statuses
title: Card lifecycle and statuses
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/card-lifecycle-and-statuses.md
  sha256: 65ef8c6e26590b0ba8ca102963cf7ee42ca29dbd542bc14543b58104f42d88d5
  url: https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses
  role: primary_guide
  updated_at: '2026-04-17T12:05:07.000Z'
operations:
- post-v1-card-reissue
- post-v2-card-bind
- post-v2-card-password-reset
- put-v1-card-activate
- put-v1-card-status
related_kus:
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-cards--card-status
- KU-API-card-issuing-cards--cards
- KU-API-card-issuing-cards--noname
- KU-CARD-card-reissuing
- KU-CARD-cards-overview-1
- KU-EVT-catalogue-cards
grouping_rationale: single source page
---

# Card lifecycle and statuses

**KU ID:** `KU-CARD-card-lifecycle-and-statuses` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/card-lifecycle-and-statuses.md`:

> The following graphic shows the card lifecycle and statuses for nominal (physical - plastic or metal) cards, noname cards, and reissued cards. Card termination statuses are on the right.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/card-lifecycle-and-statuses.md`: Card lifecycle and statuses; Card status enums; Card reissues

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/card-lifecycle-and-statuses.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses · updatedAt: 2026-04-17T12:05:07.000Z

<!-- source:begin path=docs/card-issuing/card-lifecycle-and-statuses.md part=0-end -->

# Card lifecycle and statuses

The following graphic shows the card lifecycle and statuses for nominal (physical - plastic or metal) cards, noname cards, and reissued cards. Card termination statuses are on the right.

<Image align="center" src="https://files.readme.io/edd9dcf263826661c3330d8cfdb1d8f7a56dbe6559345b30663a26c8c2557bcd-image_3.png" />

**Note**: Termination statuses **cannot** be changed to an active or temporarily blocked status. A termination status can be updated to another termination status though, and a temporary status can also be updated to another temporary status.

The following table shows the initial (default) statuses for Pismo issued cards.

| Card                     | Initial status | Notes                                                                                                                        |
| :----------------------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| Virtual                  | NORMAL         | Does not have to be activated.                                                                                               |
| Physical (plastic/metal) | CREATED        | Can be overridden in program configuration to be NORMAL. After [activation](https://developers.pismo.io/pismo-docs/reference/put-v1-card-activate), it changes to NORMAL. |
| Noname                   | UNBOUND        | When [assigned to a customer](https://developers.pismo.io/pismo-docs/reference/post-v2-card-bind) its status becomes CREATED. Once activated, it becomes NORMAL.          |
| Reissued                 |                | Depends. Refer to the [Card reissuing](https://developers.pismo.io/pismo-docs/docs/card-reissuing)  guide.                                                           |

## Card status enums

The following table contains current card status enums. "**Type**" here is an unofficial grouping.

<Table align={[null,"left",null]}>
  <thead>
    <tr>
      <th>
        Enum
      </th>

      <th>
        Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        CREATED
      </td>

      <td>
        Initial
      </td>

      <td>
        Created in the system.
      </td>
    </tr>

    <tr>
      <td>
        UNBOUND
      </td>

      <td>
        Initial
      </td>

      <td>
        Noname card not yet assigned to customer.
      </td>
    </tr>

    <tr>
      <td>
        NORMAL
      </td>

      <td>
        Active
      </td>

      <td>
        Active and eligible for transactions. Default for virtual cards. The transition from `CREATED` to `NORMAL` is for physical cards and can **only** be done through the [Activate physical card](https://developers.pismo.io/pismo-docs/reference/put-v1-card-activate)
      </td>
    </tr>

    <tr>
      <td>
        REISSUED
      </td>

      <td>
        Active
      </td>

      <td>
        Card has been [reissued](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue).
      </td>
    </tr>

    <tr>
      <td>
        UNNUMBERED
      </td>

      <td>
        Initial
      </td>

      <td>
        Card created without a PAN or a PIN that the issuer needs to define. Once the PAN is defined for a nominal card, the card's status becomes `CREATED`, for a noname card, its status becomes `UNBOUND`
      </td>
    </tr>

    <tr>
      <td>
        BLOCKED
      </td>

      <td>
        Temporary\
        block
      </td>

      <td>
        Temporarily blocked until further status changes.

        A card could be blocked, for example, if the cardholder has exceeded their allowed tries to enter a password. You can reset this for a cardholder with the [Reset password try count](https://developers.pismo.io/pismo-docs/reference/post-v2-card-password-reset) endpoint.
      </td>
    </tr>

    <tr>
      <td>
        PENDING
      </td>

      <td>
        Temporary\
        block
      </td>

      <td>
        Created and is pending until further processing, such as account verification. Until then, transactions are disabled.
      </td>
    </tr>

    <tr>
      <td>
        WARNING
      </td>

      <td>
        Temporary\
        block
      </td>

      <td>
        A general alert flag is set and transactions are disabled. After investigation, it could, typically, transition to `FRAUD` or revert back to \`\`NORMAL\`.
      </td>
    </tr>

    <tr>
      <td>
        INOPERATIVE
      </td>

      <td>
        Maybe permanent
      </td>

      <td>
        Applies to physical, virtual, or temporary cards whose defined validity period has been exceeded. For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards) and [Custom expiration for virtual and physical cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#custom-expiration-for-virtual-and-physical-cards)
      </td>
    </tr>

    <tr>
      <td>
        LOST
      </td>

      <td>
        Terminated
      </td>

      <td>
        Reported lost
      </td>
    </tr>

    <tr>
      <td>
        ROBBED
      </td>

      <td>
        Terminated
      </td>

      <td>
        Reported stolen
      </td>
    </tr>

    <tr>
      <td>
        EXPIRED
      </td>

      <td>
        Terminated
      </td>

      <td>
        Card date expiration reached. While card transactions are denied when this date is reached, it is the card issuer's responsibility to [update the status.](https://developers.pismo.io/pismo-docs/reference/put-v1-card-status)
      </td>
    </tr>

    <tr>
      <td>
        DAMAGED
      </td>

      <td>
        Terminated
      </td>

      <td>
        Damaged
      </td>
    </tr>

    <tr>
      <td>
        FRAUD
      </td>

      <td>
        Terminated
      </td>

      <td>
        Suspected fraud
      </td>
    </tr>

    <tr>
      <td>
        CANCELED
      </td>

      <td>
        Terminated
      </td>

      <td>
        Canceled
      </td>
    </tr>

    <tr>
      <td>
        DELETED
      </td>

      <td>
        Terminated
      </td>

      <td>
        Deleted
      </td>
    </tr>

    <tr>
      <td>
        BROKEN
      </td>

      <td>
        Terminated
      </td>

      <td>
        No longer physically usable
      </td>
    </tr>

    <tr>
      <td>
        THEFT
      </td>

      <td>
        Terminated
      </td>

      <td>
        Stolen
      </td>
    </tr>

    <tr>
      <td>
        DEFECT
      </td>

      <td>
        Terminated
      </td>

      <td>
        Has defect
      </td>
    </tr>
  </tbody>
</Table>

Call the [Update card status](https://developers.pismo.io/pismo-docs/reference/put-v1-card-status) endpoint to change a card's status.

## Card reissues

Card reissuing has been moved to its own guide, refer to [Card reissuing](https://developers.pismo.io/pismo-docs/docs/card-reissuing).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/activate` | `put-v1-card-activate` | Activate physical card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `PUT /wallet/v2/cards/{cardId}/noname/bind` | `post-v2-card-bind` | Associate noname card with customer | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--noname |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` | `post-v1-card-reissue` | Reissue card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `POST /wallet/v2/cards/{cardId}/password-tries/reset` | `post-v2-card-password-reset` | Reset password try count | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/status` | `put-v1-card-status` | Update card status | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-status |

### Operation essentials

- **`PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/activate`** (`put-v1-card-activate`): security `BearerAuth`; required parameters `customerId` (path), `accountId` (path), `cardId` (path), `x-customer-id` (header); required body fields none declared; response statuses 200, 204, 401, 403, 500; error codes in examples none; events `cards-update-1`.
- **`PUT /wallet/v2/cards/{cardId}/noname/bind`** (`post-v2-card-bind`): security `BearerAuth`; required parameters `cardId` (path), `x-account-id` (header), `x-customer-id` (header); required body fields none declared; response statuses 202, 400, 401, 403, 409, 500; error codes in examples none; events `cards-bind-card-1`, `cards-create-1`, `cards-update-1`.
- **`POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue`** (`post-v1-card-reissue`): security `BearerAuth`; required parameters `customerId` (path), `accountId` (path), `cardId` (path); required body fields `reason_id`; response statuses 200, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`, `cards-update-1`.
- **`POST /wallet/v2/cards/{cardId}/password-tries/reset`** (`post-v2-card-password-reset`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 403, 406, 500; error codes in examples none; events `cards-update-1`.
- **`PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/status`** (`put-v1-card-status`): security `BearerAuth`; required parameters `cardId` (path), `accountId` (path), `customerId` (path); required body fields none declared; response statuses 200, 401, 403, 500; error codes in examples none; events `cards-update-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v2-card-bind` | `cards-bind-card-1` |
| `post-v1-card-reissue` | `cards-create-1` |
| `post-v2-card-bind` | `cards-create-1` |
| `post-v1-card-reissue` | `cards-update-1` |
| `post-v2-card-bind` | `cards-update-1` |
| `post-v2-card-password-reset` | `cards-update-1` |
| `put-v1-card-activate` | `cards-update-1` |
| `put-v1-card-status` | `cards-update-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/card-lifecycle-and-statuses.md`: updatedAt 2026-04-17T12:05:07.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/card-lifecycle-and-statuses.md` | whole document | https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses | `65ef8c6e26590b0b…` | 2026-04-17T12:05:07.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-cards--card-status` — API reference: Card issuing - Cards — Card status
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-card-issuing-cards--noname` — API reference: Card issuing - Cards — Noname
- `KU-CARD-card-reissuing` — Card reissuing
- `KU-CARD-cards-overview-1` — Cards management
- `KU-EVT-catalogue-cards` — Event catalogue: cards
