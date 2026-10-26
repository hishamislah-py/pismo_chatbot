---
ku_id: KU-CARD-cards-overview-1
title: Cards management
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/cards-overview-1.md
  sha256: f2f4feee7abf09dc269a8ca936964871f1401df268d6d7edb0d6ab967fc38582
  url: https://developers.pismo.io/pismo-docs/docs/cards-overview-1
  role: primary_guide
  updated_at: '2026-07-22T22:25:46.000Z'
operations:
- create-bulk
- delete-v2-card-validity
- get-v1-card-mode
- get-v1-pin-as-pinblock
- get-v2-card-info
- get-v2-card-password
- patch-v2-card
- patch-v2-card-validity-renew
- post-v1-card-mode
- post-v1-card-reissue
- post-v2-card
- post-v2-card-bind
- post-v2-card-password-reset
- post-v2-reset-cvv
- put-v1-card-activate
- put-v1-card-mode-status
- put-v1-update-pan-nominal
- put-v1-update-pan-noname
- put-v1-update-pin-from-pinblock
- put-v2-card-password
related_kus:
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-cards--card-validity
- KU-API-card-issuing-cards--cards
- KU-API-card-issuing-cards--cvv-rotation
- KU-API-card-issuing-cards--issuer-pan-pin
- KU-API-card-issuing-cards--modes
- KU-API-card-issuing-cards--noname
- KU-API-card-issuing-cards--pci
- KU-CARD-card-on-file-and-automatic-updater
- KU-CARD-card-tokenization-process-and-onboarding
- KU-CARD-digital-wallets
- KU-CARD-get-started-card-issuing
- KU-CARD-physical-card-embossing
- KU-CC-get-started-control-center
- KU-EVT-catalogue-cards
- KU-GS-environments
grouping_rationale: single source page
---

# Cards management

**KU ID:** `KU-CARD-cards-overview-1` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/cards-overview-1.md`:

> The Pismo platform offers you many different types of cards (credit, debit, prepaid, private label, and more) you can issue. These cards allow transactions to occur in almost all conceivable locations and circumstances -  retail stores, online e-commerce, ATM withdrawals, recurring subscriptions, and so on.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/cards-overview-1.md`: Cards management; Card data; Card types; Configuring temporary cards; Branded and private label cards; Issuer-defined PAN/PIN; Custom expiration for virtual and physical cards; Create a combination card with card modes; Mode object; Card mode API endpoints; Digital wallets - Pismo, Apple Pay, Google Pay, and others; Mastercard's Automatic Billing Updater option

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 20 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/cards-overview-1.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cards-overview-1 · updatedAt: 2026-07-22T22:25:46.000Z

<!-- source:begin path=docs/card-issuing/cards-overview-1.md part=0-end -->

# Cards management

The Pismo platform offers you many different types of cards (credit, debit, prepaid, private label, and more) you can issue. These cards allow transactions to occur in almost all conceivable locations and circumstances -  retail stores, online e-commerce, ATM withdrawals, recurring subscriptions, and so on.

> 📘 Getting started with card issuing
>
> Refer to the [Get started with card issuing](https://developers.pismo.io/pismo-docs/docs/get-started-with-card-issuing) guide.

Every card is associated with a single customer and account. Accounts can have multiple customers, typically to accommodate primary and additional cardholders, but only one owner. Customers can also have more than one account.

Pismo infrastructure handles all card information including sensitive data, which is stored in a dedicated, secure and <Anchor label="Payment Card Industry (PCI)" target="_blank" href="https://www.investopedia.com/terms/p/pci-compliance.asp">Payment Card Industry (PCI)</Anchor> compliant environment.

<Image align="center" alt="Card management workflow" src="https://files.readme.io/e224c33-pismoCards.png" title="pismoCards.png" />

> 📘 PCI endpoints
>
> Certain endpoints are designated PCI endpoints and should be called in a PCI environment. For more information, refer to [Environments](https://developers.pismo.io/pismo-docs/docs/environments) and, specifically, [PCI vs non-PCI endpoints](https://developers.pismo.io/pismo-docs/docs/environments#pci-endpoints-vs-non-pci-endpoints).

**Pismo enables you to:**

* Choose [card types](#card-types) that best suit your customers' needs.
* Customize a card’s attributes, behaviors, and lifecycle, including limits on spending, the number of card uses, and the number of active cards.
* [Work with the card embosser of your choice](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing).
* [Tokenize card data](https://developers.pismo.io/pismo-docs/reference/create-a-cardsonfile-v3) for use in a [digital wallet](https://developers.pismo.io/pismo-docs/docs/wallet-overview).

## Card data

Cards store the data necessary to complete a merchant transaction. In the table below,  the **expiration date** and **name** are not considered sensitive PCI  data.

| Field                                                                                               | Description                                                                                                                                                                                                                                                                                |
| :-------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                                                                                                | Card name, can be nickname or alias the cardholder wishes to use. Though a card is associated with one customer and account, a customer can have multiple accounts and cards.                                                                                                              |
| Expiration date                                                                                     | Date when card is no longer valid. You can set this value during program configuration. If not set, the default is 72 months.                                                                                                                                                              |
| [Primary Account Number](https://www.investopedia.com/terms/p/primary-account-number-pan.asp) (PAN) | Unique number that IDs the card network, issuing bank, and cardholder account. For Visa and Mastercard, this is a 16-19 digit string. The PAN is generated from program settings, including the [BIN](https://www.investopedia.com/terms/b/bank-identification-number.asp) and BIN ranges. |
| [Card Verification Value](https://www.investopedia.com/terms/v/validation-code.asp) (CVV or CVV2)   | Verification number that appears on the card's back, usually used for **[card not present](https://squareup.com/us/en/townsquare/what-is-a-card-not-present-transaction)** transactions.                                                                                                   |
| Personal Identification Number (PIN)                                                                | Encrypted card password. Pismo randomly generates the initial PIN at [card creation](https://developers.pismo.io/pismo-docs/reference/post-v2-card) time. Can be 4 or 6 digits.                                                                                                                                                         |

The PIN, PAN, and expiration date are automatically generated at card creation time.

You can call the following API endpoints for a card's PIN:

* [Get card password](https://developers.pismo.io/pismo-docs/reference/get-v2-card-password)
* [Change card password](https://developers.pismo.io/pismo-docs/reference/put-v2-card-password)
* [Reset password try count](https://developers.pismo.io/pismo-docs/reference/post-v2-card-password-reset)
* [Get PIN as PINBlock](https://developers.pismo.io/pismo-docs/reference/get-v1-pin-as-pinblock)
* [Update PIN from PINBlock](https://developers.pismo.io/pismo-docs/reference/put-v1-update-pin-from-pinblock)

## Card types

Pismo offers the following card types.

<Table align={["left","left"]}>
  <thead>
    <tr>
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
        **Physical (plastic/metal)**
      </td>

      <td>
        You can use *physical* or plastic/metal cards at terminals to not only make purchases and withdrawals from ATMs, but also online in e-commerce using the card's data.<br />

        **Pismo offers two ways to issue physical cards**:

        **Nominal** - At [card creation](https://developers.pismo.io/pismo-docs/reference/post-v2-card) , the customer is designated the cardholder.

        **Noname** - Noname cards are [batch-generated](https://developers.pismo.io/pismo-docs/reference/create-bulk)  and not initially associated with customers, which occurs later. Noname cards work well for special use cases like gift cards or in countries or scenarios where a password or chip might be required but not necessarily a printed card name.  When you are ready, you can [assign a noname card to a customer and account](https://developers.pismo.io/pismo-docs/reference/post-v2-card-bind) . Refer to **Cards Management**  > **Noname** for more APIs and endpoints in the [API Reference documentation](https://developers.pismo.io/pismo-docs/reference/create-bulk).

        **The following applies to physical cards**:\
        Only one per customer and account.\
        Customers can have more than one account and card.\
        Can be [tokenized](https://developers.pismo.io/pismo-docs/docs/wallet-overview)  for use in a [digital wallet](https://developers.pismo.io/pismo-docs/docs/wallet-overview)\
        Have a fixed PAN and CVV\
        Have to be [activated](https://developers.pismo.io/pismo-docs/reference/put-v1-card-activate)  before use\
        Can be both a [credit and debit](#create-a-combination-card-with-card-modes)  card

        ***Contactless* physical card** Contact transactions require inserting a card into a terminal. With **contactless** transactions, you can simply hold or tap the card on a contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have [Near Field Communication (NFC)](https://en.wikipedia.org/wiki/Near-field_communication) technology. All  APIs that generate an embossed card have a contactless card option and Pismo sends this information to your [configured embosser](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing).
      </td>
    </tr>

    <tr>
      <td>
        **Virtual**
      </td>

      <td>
        A card that exists digitally, used in e-commerce and subscriptions. You can change a virtual card's [CVV](https://developers.pismo.io/pismo-docs/reference/post-v2-reset-cvv) periodically, increasing its security. Virtual cards provide greater customer flexibility to make a purchase as you can offer them via an application.

        **The following applies to virtual cards:**\
        Can have multiple active cards per customer, but the card name needs to be different. Can be [tokenized](https://developers.pismo.io/pismo-docs/docs/wallet-overview) for use in a [digital wallet](https://developers.pismo.io/pismo-docs/docs/wallet-overview).\
        Have a fixed PAN and dynamic CVV. (When you [create a virtual card](https://developers.pismo.io/pismo-docs/reference/post-v2-card), be aware that the `cvv_rotation_interval_hours` is a **required** field.) Have a **transaction limit** you set at card creation. If not set, the account limit is used. Later, you can change the transaction limit with the [Update card information](https://developers.pismo.io/pismo-docs/reference/patch-v2-card) endpoint. Are created with the same [endpoint](https://developers.pismo.io/pismo-docs/reference/post-v2-card) as a physical card. Do not need to be activated before use.
      </td>
    </tr>

    <tr>
      <td>
        **Temporary (virtual)**
      </td>

      <td>
        A virtual card with a fixed PAN and CVV originally meant for short-term use, typically 24 hours (default). By default, it is renewable. For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards)  below.
      </td>
    </tr>

    <tr>
      <td>
        **Recurring (virtual)**
      </td>

      <td>
        A virtual card with a fixed PAN and CVV originally meant for use with recurring subscriptions. This type is being DEPRECATED and it is recommended you use **Virtual** instead.
      </td>
    </tr>
  </tbody>
</Table>

> 🚧 CVV rotation for virtual cards
>
> The logic for virtual card CVV rotation belongs to Pismo. The card networks are not updated every time this happens. This might impact  scenarios where the card network validates the CVV before sending a transaction to Pismo.

### Configuring temporary cards

As stated in the table above, temporary cards are virtual cards with a fixed PAN and CVV originally meant for short-term use, typically 24 hours (default). By default, it is also renewable.

Through [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) program parameter configuration, you can  define:

* Validity period (in hours) for temporary cards. The default is 24, but can be configured differently.
* Transactions limit  for temporary cards. Only authorized transactions are counted.
* Skip auto-renewal for temporary cards.

#### Temporary card renewal

Temporary cards can have an `INOPERATIVE` status , which occurs automatically when the validity period expires. You can call the [Get PCI card info](https://developers.pismo.io/pismo-docs/reference/get-v2-card-info)  endpoint to renew it. However, the following applies if you do this:

* If the "Skip auto-renewal for temporary cards" program parameter is `true`, the card is not renewed. In this case, the card's status becomes permanently `INOPERATIVE`.
* If the Skip parameter is `false` (default), then the card is renewed. In this case, the card's status becomes `NORMAL`.

**Note**: A temporary card's validity date is different from a card's expiration date. The expiration date applies to all  card types—only temporary cards have a validity date.

### Branded and private label cards

You need to contact your Pismo representative to set up branded and private label cards.

* **Branded**—Visa and Mastercard cards that allow customers to make purchases at all establishments accepting these brands.

* **Private label** —For companies seeking customer loyalty, private label cards are a good option as you can provide benefits such as discounts and better payment terms. They are usually only accepted at stores in the same network. With a private label, it is possible to control and monitor issuer transactions.

## Issuer-defined PAN/PIN

As of October, 2025, Issuers can create cards without a Pismo-generated Primary Account Number (PAN) or Personal Identification Number (PIN). They can then set the value for these fields themselves via Pismo endpoints as described below.

**To create a card without a PAN/PIN**

1. Call [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card) or [Reissue card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue) with `status` set to `UNNUMBERED` and `brand` set to the card network's brand (`VISA`, `MASTERCARD`, `ELO`, or `RUPAY`).
2. Call either [Update nominal card PAN/PIN](https://developers.pismo.io/pismo-docs/reference/put-v1-update-pan-nominal) (nominal cards) or [Update noname card PAN/PIN](https://developers.pismo.io/pismo-docs/reference/put-v1-update-pan-noname) (noname cards) to update the PAN and, optionally, the PIN.\
   This changes the card's status to `UNBOUND` for noname cards and `CREATED` for normal cards.

**Note:** Before calling the update endpoints, talk to your Pismo representative about setting up encryption for them.

## Custom expiration for virtual and physical cards

As of October, 2025, plastic and virtual cards can have a custom expiration date and time. Prior to this, only temporary cards could. To support this, a `validity_period_hours` field has been added to the following endpoints:

* [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card)
* [Reissue card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue)
* [Create noname card bulk](https://developers.pismo.io/pismo-docs/reference/create-bulk)

You can use this field to set how long, in hours, a plastic or virtual card is valid. Once this time is exceeded, and the card has a `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`.

Two new endpoints have been added to support this feature:

* [Renew card validity](https://developers.pismo.io/pismo-docs/reference/patch-v2-card-validity-renew)—Renew a card's validity period in hours.
* [Delete card validity period](https://developers.pismo.io/pismo-docs/reference/delete-v2-card-validity)—Delete a card's previously scheduled validity period.

## Create a combination card with card modes

You can use a combination card for both debit and credit transactions. What makes this possible are ***modes*** . A card can have a credit mode or a debit mode or both (combination cards).  A mode is derived from a program/account, which can be either credit or debit.

A card's initial mode comes from the program/account it is issued with but, if you [create a card](https://developers.pismo.io/pismo-docs/reference/post-v2-card) with the parameter `mode_type` set to `COMBO`,  you can add an additional mode to the card with the [Add card mode](https://developers.pismo.io/pismo-docs/reference/post-v1-card-mode) API endpoint at a later time to create a combination card.

> 📘 Removing a card mode
>
> A card mode can't be removed, but it can be suspended and made inactive with the [Change card mode status](https://developers.pismo.io/pismo-docs/reference/put-v1-card-mode-status) endpoint.

### Mode object

A card mode has an object and an identifier:

```json
{
  "modes": [
    {
      "id": 128876,
      "mode": "CREDIT",
      "program_id": 88490,
      "customer_id": 102377856,
      "account_id": 102378693,
      "password_tries": 3,
      "transaction_limit": 750.05,
      "number_of_transactions": 40,
      "status": "SUSPENDED",
      "card_owner": "TN-f878e4a1-2879-48ba-be16-821e73ac98db"
    }
  ]
}
```

### Card mode API endpoints

The following endpoints pertain to modes:

* [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card)—Issue a card setting mode parameters.
* [Add card mode](https://developers.pismo.io/pismo-docs/reference/post-v1-card-mode)—Add a mode (credit or debit account) to a card.
* [Get card modes](https://developers.pismo.io/pismo-docs/reference/get-v1-card-mode)—Get information about a specific card's modes. Each mode has an ID and an object.
* [Change card mode status](https://developers.pismo.io/pismo-docs/reference/put-v1-card-mode-status)—Change a card mode's status - active or suspended.

## Digital wallets - Pismo, Apple Pay, Google Pay, and others

Cards you issue through Pismo can be stored in digital wallets, which let you  *tokenize* cards and use them for payments without exposing sensitive data such as the CVV or PAN. Pismo provides its own digital wallet and supports those of other payment apps like Samsung Pay or Google Pay.

For more information refer to:

* [Pismo digital wallet](https://developers.pismo.io/pismo-docs/docs/wallet-overview)
* [Third-party wallets (such as Apple Pay)](https://developers.pismo.io/pismo-docs/docs/card-tokenization-process-and-onboarding)

## Mastercard's Automatic Billing Updater option

The information in this section has been moved to a new guide - [Automatic updater.](https://developers.pismo.io/pismo-docs/docs/automatic-updater)

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /wallet/v2/cards` | `post-v2-card` | Create card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `GET /pcicards/v2/pcicards/password/{cardId}` | `get-v2-card-password` | Get card password | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |
| `PUT /pcicards/v2/pcicards/card/{cardId}` | `put-v2-card-password` | Change card password | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |
| `POST /wallet/v2/cards/{cardId}/password-tries/reset` | `post-v2-card-password-reset` | Reset password try count | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `GET /pcicards/v1/pcicards/{cardId}/pinblock` | `get-v1-pin-as-pinblock` | Get PIN as PINblock | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |
| `PUT /pcicards/v1/pcicards/{cardId}/pinblock` | `put-v1-update-pin-from-pinblock` | Update PIN from PINblock | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |
| `POST /cards/v1/bulks` | `create-bulk` | Create noname card bulk | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--noname |
| `PUT /wallet/v2/cards/{cardId}/noname/bind` | `post-v2-card-bind` | Associate noname card with customer | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--noname |
| `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/activate` | `put-v1-card-activate` | Activate physical card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `POST /pcicards/v2/pcicards/cvv/{cardId}/reset` | `post-v2-reset-cvv` | Rotate virtual card CVV | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cvv-rotation |
| `PATCH /wallet/v2/cards/{cardId}` | `patch-v2-card` | Update card information | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `GET /pcicards/v2/pcicards/info/{cardId}` | `get-v2-card-info` | Get card PCI information | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` | `post-v1-card-reissue` | Reissue card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `PUT /pcicards/v1/pcicards/cards/{cardId}/pan` | `put-v1-update-pan-nominal` | Update nominal card PAN/PIN [beta] | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--issuer-pan-pin |
| `PUT /pcicards/v1/pcicards/cards/noname/{cardId}/pan` | `put-v1-update-pan-noname` | Update noname card PAN/PIN [beta] | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--issuer-pan-pin |
| `PATCH /wallet/v2/cards/{cardId}/validity/renew` | `patch-v2-card-validity-renew` | Renew card validity | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-validity |
| `DELETE /wallet/v2/cards/{cardId}/validity` | `delete-v2-card-validity` | Delete card validity period | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-validity |
| `POST /wallet/v2/cards/{cardId}/modes` | `post-v1-card-mode` | Add card mode | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--modes |
| `PUT /wallet/v2/cards/{cardId}/modes/{modeId}/status` | `put-v1-card-mode-status` | Change card mode status | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--modes |
| `GET /wallet/v2/cards/{cardId}/modes` | `get-v1-card-mode` | Get card modes | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--modes |

### Operation essentials

- **`POST /wallet/v2/cards`** (`post-v2-card`): security `BearerAuth`; required parameters `x-customer-id` (header); required body fields `name`, `type`; response statuses 200, 201, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`.
- **`GET /pcicards/v2/pcicards/password/{cardId}`** (`get-v2-card-password`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 401, 404, 409, 500; error codes in examples none; events none listed.
- **`PUT /pcicards/v2/pcicards/card/{cardId}`** (`put-v2-card-password`): security `BearerAuth`; required parameters `cardId` (path); required body fields `pin`; response statuses 201, 401, 403, 404, 500; error codes in examples none; events `cards-update-password-1`.
- **`POST /wallet/v2/cards/{cardId}/password-tries/reset`** (`post-v2-card-password-reset`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 403, 406, 500; error codes in examples none; events `cards-update-1`.
- **`GET /pcicards/v1/pcicards/{cardId}/pinblock`** (`get-v1-pin-as-pinblock`): security `BearerAuth`; required parameters `key-id` (query), `cardId` (path); required body fields none declared; response statuses 200, 401, 403, 404, 409, 500; error codes in examples none; events none listed.
- **`PUT /pcicards/v1/pcicards/{cardId}/pinblock`** (`put-v1-update-pin-from-pinblock`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 204, 401, 403, 404, 500; error codes in examples none; events `cards-update-password-1`.
- **`POST /cards/v1/bulks`** (`create-bulk`): security `BearerAuth`; required parameters none declared; required body fields `external_ids`, `program_id`; response statuses 201, 400, 409, 500; error codes in examples none; events none listed.
- **`PUT /wallet/v2/cards/{cardId}/noname/bind`** (`post-v2-card-bind`): security `BearerAuth`; required parameters `cardId` (path), `x-account-id` (header), `x-customer-id` (header); required body fields none declared; response statuses 202, 400, 401, 403, 409, 500; error codes in examples none; events `cards-bind-card-1`, `cards-create-1`, `cards-update-1`.
- **`PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/activate`** (`put-v1-card-activate`): security `BearerAuth`; required parameters `customerId` (path), `accountId` (path), `cardId` (path), `x-customer-id` (header); required body fields none declared; response statuses 200, 204, 401, 403, 500; error codes in examples none; events `cards-update-1`.
- **`POST /pcicards/v2/pcicards/cvv/{cardId}/reset`** (`post-v2-reset-cvv`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 401, 403, 404, 500; error codes in examples none; events `cards-rotate-cvv-1`.
- **`PATCH /wallet/v2/cards/{cardId}`** (`patch-v2-card`): security `BearerAuth`; required parameters `cardId` (path), `x-customer-id` (header); required body fields none declared; response statuses 200, 401, 403, 409, 500; error codes in examples none; events `cards-update-1`.
- **`GET /pcicards/v2/pcicards/info/{cardId}`** (`get-v2-card-info`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue`** (`post-v1-card-reissue`): security `BearerAuth`; required parameters `customerId` (path), `accountId` (path), `cardId` (path); required body fields `reason_id`; response statuses 200, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`, `cards-update-1`.
- **`PUT /pcicards/v1/pcicards/cards/{cardId}/pan`** (`put-v1-update-pan-nominal`): security `BearerAuth`; required parameters `cardId` (path), `x-customer-id` (header); required body fields `pan`; response statuses 202, 400, 401, 403, 404, 406, 500; error codes in examples none; events `cards-update-1`.
- **`PUT /pcicards/v1/pcicards/cards/noname/{cardId}/pan`** (`put-v1-update-pan-noname`): security `BearerAuth`; required parameters `cardId` (path); required body fields `pan`; response statuses 202, 400, 401, 403, 404, 406, 500; error codes in examples none; events `cards-update-1`.
- **`PATCH /wallet/v2/cards/{cardId}/validity/renew`** (`patch-v2-card-validity-renew`): security `BearerAuth`; required parameters `cardId` (path); required body fields `validity_period_hours`; response statuses 200, 401, 403, 500; error codes in examples none; events `cards-update-1`.
- **`DELETE /wallet/v2/cards/{cardId}/validity`** (`delete-v2-card-validity`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 204, 401, 403, 500; error codes in examples none; events `cards-update-1`.
- **`POST /wallet/v2/cards/{cardId}/modes`** (`post-v1-card-mode`): security `BearerAuth`; required parameters `cardId` (path), `x-customer-id` (header); required body fields none declared; response statuses 201, 401, 403, 409, 500; error codes in examples none; events none listed.
- **`PUT /wallet/v2/cards/{cardId}/modes/{modeId}/status`** (`put-v1-card-mode-status`): security `BearerAuth`; required parameters `cardId` (path), `modeId` (path), `x-customer-id` (header); required body fields none declared; response statuses 204, 401, 403, 409, 500; error codes in examples none; events none listed.
- **`GET /wallet/v2/cards/{cardId}/modes`** (`get-v1-card-mode`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 401, 403, 409, 500; error codes in examples none; events none listed.

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
| `post-v2-reset-cvv` | `cards-rotate-cvv-1` |
| `delete-v2-card-validity` | `cards-update-1` |
| `patch-v2-card` | `cards-update-1` |
| `patch-v2-card-validity-renew` | `cards-update-1` |
| `post-v1-card-reissue` | `cards-update-1` |
| `post-v2-card-bind` | `cards-update-1` |
| `post-v2-card-password-reset` | `cards-update-1` |
| `put-v1-card-activate` | `cards-update-1` |
| `put-v1-update-pan-nominal` | `cards-update-1` |
| `put-v1-update-pan-noname` | `cards-update-1` |
| `put-v1-update-pin-from-pinblock` | `cards-update-password-1` |
| `put-v2-card-password` | `cards-update-password-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/cards-overview-1.md`: updatedAt 2026-07-22T22:25:46.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- Operation link `create-a-cardsonfile-v3` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/cards-overview-1.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cards-overview-1 | `f2f4feee7abf09dc…` | 2026-07-22T22:25:46.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-cards--card-validity` — API reference: Card issuing - Cards — Card validity
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-card-issuing-cards--cvv-rotation` — API reference: Card issuing - Cards — CVV rotation
- `KU-API-card-issuing-cards--issuer-pan-pin` — API reference: Card issuing - Cards — Issuer PAN/PIN
- `KU-API-card-issuing-cards--modes` — API reference: Card issuing - Cards — Modes
- `KU-API-card-issuing-cards--noname` — API reference: Card issuing - Cards — Noname
- `KU-API-card-issuing-cards--pci` — API reference: Card issuing - Cards — PCI
- `KU-CARD-card-on-file-and-automatic-updater` — Card-on-file and automatic updater
- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-CARD-digital-wallets` — Digital wallets, MDES Token Connect and Click to Pay
- `KU-CARD-get-started-card-issuing` — Get started with card issuing
- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-GS-environments` — Environments
