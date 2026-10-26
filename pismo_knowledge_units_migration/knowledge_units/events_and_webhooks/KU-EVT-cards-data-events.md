---
ku_id: KU-EVT-cards-data-events
title: Card issuing - Cards
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/cards-data-events.md
  sha256: 209c9c8d8269d830f1d236e27e04680a383f44aa20677402621a41e4f7684996
  url: https://developers.pismo.io/pismo-docs/docs/cards-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:14:57.000Z'
operations:
- create-a-new-validation-for-a-given-card
- patch-v2-card
- post-v1-append-update-pin-script
- post-v1-card-reissue
- post-v2-card
- post-v2-card-bind
- post-v2-card-password-reset
- post-v2-reset-cvv
- put-v1-card-activate
- put-v1-card-status
- put-v1-update-pin-from-pinblock
- put-v2-card-password
- start-bulk
- updates-a-cardsonfile
related_kus:
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-cards--card-status
- KU-API-card-issuing-cards--cards
- KU-API-card-issuing-cards--cvv-rotation
- KU-API-card-issuing-cards--noname
- KU-API-card-issuing-cards--pci
- KU-API-card-issuing-cards-on-file--cards-on-file
- KU-API-card-issuing-cards-on-file--validation
- KU-CARD-card-tokenization-flow-and-events
- KU-CARD-cards-overview-1
- KU-CARD-physical-card-embossing
- KU-EVT-catalogue-cards
- KU-EVT-catalogue-cardsonfile
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Card issuing - Cards

**KU ID:** `KU-EVT-cards-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/cards-data-events.md`:

> This table lists the cards endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/cards-data-events.md`: Card issuing - Cards

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 14 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/cards-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cards-data-events · updatedAt: 2026-03-18T15:14:57.000Z

<!-- source:begin path=docs/data-and-reporting/cards-data-events.md part=0-end -->

# Card issuing - Cards

This table lists the cards endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Endpoint
      </th>

      <th style={{ textAlign: "left" }}>
        Event
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **Cards API**
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card created](https://developers.pismo.io/events/docs/cards-create-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Associate noname card with customer](https://developers.pismo.io/pismo-docs/reference/post-v2-card-bind)
      </td>

      <td style={{ textAlign: "left" }}>
        [Customer bound to noname card](https://developers.pismo.io/events/docs/cards-bind-card-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update card information](https://developers.pismo.io/pismo-docs/reference/patch-v2-card)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card updated](https://developers.pismo.io/events/docs/cards-update-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update card status](https://developers.pismo.io/pismo-docs/reference/put-v1-card-status)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card updated](https://developers.pismo.io/events/docs/cards-update-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Reissue physical card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card updated](https://developers.pismo.io/events/docs/cards-update-1) (old card)\
        [Card created](https://developers.pismo.io/events/docs/cards-create-1) (new card)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Activate physical card](https://developers.pismo.io/pismo-docs/reference/put-v1-card-activate)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card updated](https://developers.pismo.io/events/docs/cards-update-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Change card password](https://developers.pismo.io/pismo-docs/reference/put-v2-card-password)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card password changed](https://developers.pismo.io/events/docs/cards-update-password-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Reset password try count](https://developers.pismo.io/pismo-docs/reference/post-v2-card-password-reset)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card updated](https://developers.pismo.io/events/docs/cards-update-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Rotate virtual card CVV](https://developers.pismo.io/pismo-docs/reference/post-v2-reset-cvv)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card CVV updated](https://developers.pismo.io/events/docs/cards-rotate-cvv-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Start noname card bulk process](https://developers.pismo.io/pismo-docs/reference/start-bulk)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card created](https://developers.pismo.io/events/docs/cards-update-1)\
        [Card can be added to next scheduled embossing](https://developers.pismo.io/events/docs/cards-embossing-card-ingress-1)\
        [Card embossing notification received](https://developers.pismo.io/events/docs/cards-embossing-1)\
        [Embossing rejection file processed](https://developers.pismo.io/events/docs/cards-card-rejection-1)\
        [Embossing summary received](https://developers.pismo.io/events/docs/cards-embossing-summary-1)

        See [Embossing events](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing#embossing-events) for more information.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update PIN from PINBlock](https://developers.pismo.io/pismo-docs/reference/put-v1-update-pin-from-pinblock)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card password changed](https://developers.pismo.io/events/docs/cards-update-password-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Append issuer script
      </td>

      <td style={{ textAlign: "left" }}>
        [Card issuer script notification received](https://developers.pismo.io/events/docs/cards-issuer-script-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Append update PIN script](https://developers.pismo.io/pismo-docs/reference/post-v1-append-update-pin-script)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card issuer script notification received](https://developers.pismo.io/events/docs/cards-issuer-script-1)\
        [Card password updated](https://developers.pismo.io/events/docs/cards-update-password-1) - When script executes
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Automatic Billing Update](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#mastercards-automatic-billing-updater-option) file sent to Mastercard
      </td>

      <td style={{ textAlign: "left" }}>
        [ABU notification file sent](https://developers.pismo.io/events/docs/cards-automatic-updater-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **Cards on file API**
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create card on file](https://developers.pismo.io/pismo-docs/reference/create-a-cardsonfile-v3)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card on file created](https://developers.pismo.io/events/docs/cardsonfile-provision-1)\
        [Card on file validation result received](https://developers.pismo.io/events/docs/cardsonfile-verification-1)\
        [Card excluded](https://developers.pismo.io/events/docs/cardsonfile-exclusion-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update card on file](https://developers.pismo.io/pismo-docs/reference/updates-a-cardsonfile)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card on file updated](https://developers.pismo.io/events/docs/cardsonfile-patch-cards-1)\
        If the card status is being changed to `SUSPENDED`, it also generates an [Card excluded](https://developers.pismo.io/events/docs/cardsonfile-exclusion-1) event
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create card validation](https://developers.pismo.io/pismo-docs/reference/create-a-new-validation-for-a-given-card)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card on file validation result received](https://developers.pismo.io/events/docs/cardsonfile-verification-1)

        If validation fails, an [Card excluded](https://developers.pismo.io/events/docs/cardsonfile-exclusion-1) event is generated.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Submit validation try](https://developers.pismo.io/pismo-docs/reference/create-a-new-validation-for-a-given-card)
      </td>

      <td style={{ textAlign: "left" }}>
        [Card on file validation result received](https://developers.pismo.io/events/docs/cardsonfile-verification-1) event with `PENDING` status.

        If the verification/validation fails, an [Card excluded](https://developers.pismo.io/events/docs/cardsonfile-exclusion-1) event is generated and the card is deleted from the customer's wallet.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **Card tokenization API**
      </td>

      <td style={{ textAlign: "left" }}>
        None directly via endpoints, though the tokenization process itself generates a number of events:\
        [Token provisioning response received](https://developers.pismo.io/events/docs/cards-tokenization-notification-1)\
        [Token provisioning rejected](https://developers.pismo.io/events/docs/cards-tokenization-notification-refusal-1)\
        [Tokenization challenge sent](https://developers.pismo.io/events/docs/cards-tokenization-send-challenge-1)

        See [Card tokenization flow and events](https://developers.pismo.io/pismo-docs/docs/card-tokenization-flow-and-events) for more information.
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /wallet/v2/cards` | `post-v2-card` | Create card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `PUT /wallet/v2/cards/{cardId}/noname/bind` | `post-v2-card-bind` | Associate noname card with customer | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--noname |
| `PATCH /wallet/v2/cards/{cardId}` | `patch-v2-card` | Update card information | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/status` | `put-v1-card-status` | Update card status | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-status |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` | `post-v1-card-reissue` | Reissue card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/activate` | `put-v1-card-activate` | Activate physical card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `PUT /pcicards/v2/pcicards/card/{cardId}` | `put-v2-card-password` | Change card password | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |
| `POST /wallet/v2/cards/{cardId}/password-tries/reset` | `post-v2-card-password-reset` | Reset password try count | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `POST /pcicards/v2/pcicards/cvv/{cardId}/reset` | `post-v2-reset-cvv` | Rotate virtual card CVV | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cvv-rotation |
| `POST /cards/v1/bulks/{bulkID}/start` | `start-bulk` | Start noname card bulk process | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--noname |
| `PUT /pcicards/v1/pcicards/{cardId}/pinblock` | `put-v1-update-pin-from-pinblock` | Update PIN from PINblock | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |
| `POST /pcicards/v1/pcicards/{cardId}/scripts/pin-update` | `post-v1-append-update-pin-script` | Append update PIN script | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |
| `PATCH /cardsonfile/v2/cardsonfile/cards` | `updates-a-cardsonfile` | Update card on file | `api-specs/Card_issuing_-_Cards_on_file.yaml` | no | KU-API-card-issuing-cards-on-file--cards-on-file |
| `POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations` | `create-a-new-validation-for-a-given-card` | Create card validation | `api-specs/Card_issuing_-_Cards_on_file.yaml` | no | KU-API-card-issuing-cards-on-file--validation |

### Operation essentials

- **`POST /wallet/v2/cards`** (`post-v2-card`): security `BearerAuth`; required parameters `x-customer-id` (header); required body fields `name`, `type`; response statuses 200, 201, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`.
- **`PUT /wallet/v2/cards/{cardId}/noname/bind`** (`post-v2-card-bind`): security `BearerAuth`; required parameters `cardId` (path), `x-account-id` (header), `x-customer-id` (header); required body fields none declared; response statuses 202, 400, 401, 403, 409, 500; error codes in examples none; events `cards-bind-card-1`, `cards-create-1`, `cards-update-1`.
- **`PATCH /wallet/v2/cards/{cardId}`** (`patch-v2-card`): security `BearerAuth`; required parameters `cardId` (path), `x-customer-id` (header); required body fields none declared; response statuses 200, 401, 403, 409, 500; error codes in examples none; events `cards-update-1`.
- **`PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/status`** (`put-v1-card-status`): security `BearerAuth`; required parameters `cardId` (path), `accountId` (path), `customerId` (path); required body fields none declared; response statuses 200, 401, 403, 500; error codes in examples none; events `cards-update-1`.
- **`POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue`** (`post-v1-card-reissue`): security `BearerAuth`; required parameters `customerId` (path), `accountId` (path), `cardId` (path); required body fields `reason_id`; response statuses 200, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`, `cards-update-1`.
- **`PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/activate`** (`put-v1-card-activate`): security `BearerAuth`; required parameters `customerId` (path), `accountId` (path), `cardId` (path), `x-customer-id` (header); required body fields none declared; response statuses 200, 204, 401, 403, 500; error codes in examples none; events `cards-update-1`.
- **`PUT /pcicards/v2/pcicards/card/{cardId}`** (`put-v2-card-password`): security `BearerAuth`; required parameters `cardId` (path); required body fields `pin`; response statuses 201, 401, 403, 404, 500; error codes in examples none; events `cards-update-password-1`.
- **`POST /wallet/v2/cards/{cardId}/password-tries/reset`** (`post-v2-card-password-reset`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 403, 406, 500; error codes in examples none; events `cards-update-1`.
- **`POST /pcicards/v2/pcicards/cvv/{cardId}/reset`** (`post-v2-reset-cvv`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 401, 403, 404, 500; error codes in examples none; events `cards-rotate-cvv-1`.
- **`POST /cards/v1/bulks/{bulkID}/start`** (`start-bulk`): security `BearerAuth`; required parameters `bulkID` (path); required body fields none declared; response statuses 202, 400, 404, 409, 500; error codes in examples none; events `cards-create-1`.
- **`PUT /pcicards/v1/pcicards/{cardId}/pinblock`** (`put-v1-update-pin-from-pinblock`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 204, 401, 403, 404, 500; error codes in examples none; events `cards-update-password-1`.
- **`POST /pcicards/v1/pcicards/{cardId}/scripts/pin-update`** (`post-v1-append-update-pin-script`): security `BearerAuth`; required parameters `cardId` (path), `x-account-id` (header); required body fields `script_id`; response statuses 200, 400, 401, 403, 404, 500; error codes in examples none; events none listed.
- **`PATCH /cardsonfile/v2/cardsonfile/cards`** (`updates-a-cardsonfile`): security not declared; required parameters `Authorization` (header); required body fields `card_stored_uuid`; response statuses 200, 400, 500; error codes in examples none; events `cardsonfile-exclusion-1`, `cardsonfile-patch-cards-1`.
- **`POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations`** (`create-a-new-validation-for-a-given-card`): security not declared; required parameters `uuid` (path), `Authorization` (header); required body fields none declared; response statuses 201, 400, 500; error codes in examples none; events `cardsonfile-exclusion-1`, `cardsonfile-verification-1`.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `create-a-cardsonfile-v3` | Create card on file; Tokenize card data | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v2-card-bind` | `cards-bind-card-1` |
| `post-v1-card-reissue` | `cards-create-1` |
| `post-v2-card` | `cards-create-1` |
| `post-v2-card-bind` | `cards-create-1` |
| `start-bulk` | `cards-create-1` |
| `post-v2-reset-cvv` | `cards-rotate-cvv-1` |
| `patch-v2-card` | `cards-update-1` |
| `post-v1-card-reissue` | `cards-update-1` |
| `post-v2-card-bind` | `cards-update-1` |
| `post-v2-card-password-reset` | `cards-update-1` |
| `put-v1-card-activate` | `cards-update-1` |
| `put-v1-card-status` | `cards-update-1` |
| `put-v1-update-pin-from-pinblock` | `cards-update-password-1` |
| `put-v2-card-password` | `cards-update-password-1` |
| `create-a-new-validation-for-a-given-card` | `cardsonfile-exclusion-1` |
| `updates-a-cardsonfile` | `cardsonfile-exclusion-1` |
| `updates-a-cardsonfile` | `cardsonfile-patch-cards-1` |
| `create-a-new-validation-for-a-given-card` | `cardsonfile-verification-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `cards-automatic-updater-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-automatic-updater-1 | 2 | KU-EVT-catalogue-cards |
| `cards-bind-card-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-bind-card-1 | 1 | KU-EVT-catalogue-cards |
| `cards-create-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-create-1 | 4 | KU-EVT-catalogue-cards |
| `cards-embossing-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-embossing-1 | 5 | KU-EVT-catalogue-cards |
| `cards-embossing-card-ingress-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-embossing-card-ingress-1 | 2 | KU-EVT-catalogue-cards |
| `cards-embossing-summary-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-embossing-summary-1 | 1 | KU-EVT-catalogue-cards |
| `cards-issuer-script-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-issuer-script-1 | 1 | KU-EVT-catalogue-cards |
| `cards-rotate-cvv-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-rotate-cvv-1 | 3 | KU-EVT-catalogue-cards |
| `cards-update-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-update-1 | 11 | KU-EVT-catalogue-cards |
| `cards-update-password-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-update-password-1 | 2 | KU-EVT-catalogue-cards |
| `cardsonfile-exclusion-1` | cardsonfile | 1 | https://developers.pismo.io/events/docs/cardsonfile-exclusion-1 | 3 | KU-EVT-catalogue-cardsonfile |
| `cardsonfile-patch-cards-1` | cardsonfile | 1 | https://developers.pismo.io/events/docs/cardsonfile-patch-cards-1 | 1 | KU-EVT-catalogue-cardsonfile |
| `cardsonfile-provision-1` | cardsonfile | 1 | https://developers.pismo.io/events/docs/cardsonfile-provision-1 | 1 | KU-EVT-catalogue-cardsonfile |
| `cardsonfile-verification-1` | cardsonfile | 1 | https://developers.pismo.io/events/docs/cardsonfile-verification-1 | 2 | KU-EVT-catalogue-cardsonfile |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/cards-data-events.md`: updatedAt 2026-03-18T15:14:57.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 18 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.
- Operation link `create-a-cardsonfile-v3` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/cards-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cards-data-events | `209c9c8d8269d830…` | 2026-03-18T15:14:57.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-cards--card-status` — API reference: Card issuing - Cards — Card status
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-card-issuing-cards--cvv-rotation` — API reference: Card issuing - Cards — CVV rotation
- `KU-API-card-issuing-cards--noname` — API reference: Card issuing - Cards — Noname
- `KU-API-card-issuing-cards--pci` — API reference: Card issuing - Cards — PCI
- `KU-API-card-issuing-cards-on-file--cards-on-file` — API reference: Card issuing - Cards on file — Cards on file
- `KU-API-card-issuing-cards-on-file--validation` — API reference: Card issuing - Cards on file — Validation
- `KU-CARD-card-tokenization-flow-and-events` — Card tokenization flow and events
- `KU-CARD-cards-overview-1` — Cards management
- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-EVT-catalogue-cardsonfile` — Event catalogue: cardsonfile
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
