---
ku_id: KU-CC-cards
title: 'Control Center cards: card information and card network tokenization'
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/card-information.md
  sha256: e540fe876db22c6870b011bb242c3726ef75285b413553cc449b47dbb0d8dc5e
  url: https://developers.pismo.io/pismo-docs/docs/card-information
  role: primary_guide
  updated_at: '2026-07-27T15:30:24.000Z'
- path: docs/control-center/card-network-tokenization.md
  sha256: c526056886c5957fa1588284d4188ce8c20c1a80a9501b92abbdc71eb1405e74
  url: https://developers.pismo.io/pismo-docs/docs/card-network-tokenization
  role: primary_guide
  updated_at: '2026-03-18T15:10:07.000Z'
operations:
- post-v1-cards-card-id-network-tokens-profile
related_kus:
- KU-API-card-issuing-tokenization--network-card-profile
- KU-CARD-card-lifecycle-and-statuses
- KU-CARD-card-tokenization-flow-and-events
- KU-CARD-card-tokenization-process-and-onboarding
- KU-CARD-cards-overview-1
- KU-CARD-digital-wallets
- KU-CC-dual-approval
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
grouping_rationale: Card screens.
---

# Control Center cards: card information and card network tokenization

**KU ID:** `KU-CC-cards` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Card screens.

Scope as stated in `docs/control-center/card-information.md`:

> The **Cards** view lists every card that was issued for the account. Each card has its own card information view that shows:

Scope as stated in `docs/control-center/card-network-tokenization.md`:

> A card network token is an encrypted digital token that can be used for payments and other card operations. Using a token prevents exposing sensitive card data, such as the Card Verification Value (CVV) or Primary Account Number (PAN).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/card-information.md`: Card information; View and edit card information; Reissue a card; Change card status; Unblock card when PIN try count has been exceeded
- `docs/control-center/card-network-tokenization.md`: Card network tokenization; View card network tokenization configurations; Create a card network tokenization configuration; Edit a card network tokenization configuration; Clone a card network tokenization configuration

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/card-information.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/card-information · updatedAt: 2026-07-27T15:30:24.000Z

<!-- source:begin path=docs/control-center/card-information.md part=0-end -->

# Card information

The **Cards** view lists every card that was issued for the account. Each card has its own card information view that shows:

* **Transactions**—List of purchases and related transactions made using the card
* **Details**—Detailed card information. You can use Control Center to edit some details and to reissue a card.
* **History**—List of all card status changes

The Pismo platform handles different types of cards, including credit, debit, prepaid, private label, and more. Every card is associated with one customer and one account. For more information about cards on the Pismo platform, refer to the [Cards management](https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses) guide.

# View and edit card information

Each card has its own card information view with its own set of views for its transactions, card details, and status changes history.

> 📘 Dual approval
>
> If your company is using the dual approval feature, this change requires approval. With dual approval, you initiate the change and submit a request for approval. A second person must review and approve it. The change doesn't take effect until it's been approved.
>
> For more information about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).

To view and edit card information, do the following:

1. On the account screen, select the **Cards** view, and select a card.
2. Select **Manage card** > **Edit**.
3. In the **Edit card details** dialog, edit the card details, and select **Save**.

# Reissue a card

Control Center does not support adding cards. However, you can request a replacement card using this feature. For information about adding cards on the Pismo platform, refer to the [Cards management](https://developers.pismo.io/pismo-docs/docs/cards-overview-1) guide.

> 📘 Dual approval
>
> If your company is using the dual approval feature, this change requires approval. With dual approval, you initiate the change and submit a request for approval. A second person must review and approve it. The change doesn't take effect until it's been approved.
>
> For more information about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).

To reissue a card, do the following:

1. On the account screen, select the **Cards** view, and select a card.
2. Select **Manage card** > **Reissue card**.
3. In the **Reissue card** dialog, configure the reissue details, and select **Reissue card**.

# Change card status

For information about card status on the Pismo platform, refer to the [Card lifecycle and statuses](https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses) guide.

To change the card status, do the following:

1. On the account screen, select the **Cards** view, and select a card.
2. Select **Manage card** > **Change status**.
3. In the **Change card status** dialog, select a status.
4. Select **Done** and confirm.

# Unblock card when PIN try count has been exceeded

When a cardholder has too many unsuccessful PIN attempts, their card is temporarily blocked. If they request immediate access instead of waiting for the timeout to expire, you can reset the PIN try count to unblock the card.

> 📘 Dual approval
>
> If your company is using the dual approval feature, this change requires approval. With dual approval, you initiate the change and submit a request for approval. A second person must review and approve it. The change doesn't take effect until it's been approved.
>
> For more information about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).

To unblock a card with too many PIN attempts, do the following:

1. On the account screen, select the **Cards** view, and select a card.\
   A highlighted warning banner indicates the card was blocked due to excessive PIN tries.\
   You can also check the **PIN try count** field on the **Details** tab, which shows the current number of PIN tries (for example, **3/3**).
2. Either select **Reset PIN try count** in the warning banner or, select **Manage card** > **Reset PIN try count (unblock)**, and confirm.
<!-- source:end -->

### Source 2: `docs/control-center/card-network-tokenization.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/card-network-tokenization · updatedAt: 2026-03-18T15:10:07.000Z

<!-- source:begin path=docs/control-center/card-network-tokenization.md part=0-end -->

# Card network tokenization

A card network token is an encrypted digital token that can be used for payments and other card operations. Using a token prevents exposing sensitive card data, such as the Card Verification Value (CVV) or Primary Account Number (PAN).

For more information on tokenization, refer to the following:

* [Digital wallets](https://developers.pismo.io/pismo-docs/docs/wallet-overview)
* [Card tokenization process and onboarding](https://developers.pismo.io/pismo-docs/docs/card-tokenization-process-and-onboarding)
* [Card tokenization flow and events](https://developers.pismo.io/pismo-docs/docs/card-tokenization-flow-and-events)
* [Card tokenization API](https://developers.pismo.io/pismo-docs/reference/post-v1-cards-card-id-network-tokens-profile)
* [Client anti-fraud webhook for card tokenization](https://developers.pismo.io/pismo-docs/docs/client-webhooks#client-anti-fraud-webhook-for-card-tokenization)

From Control Center, you can:

* [View card network tokenization configurations ](https://developers.pismo.io/pismo-docs/docs/card-network-tokenization#view-card-network-tokenization-configurations)
* [Edit a card network tokenization configuration](https://developers.pismo.io/pismo-docs/docs/card-network-tokenization#edit-a-card-network-tokenization-configuration)
* [Clone a card network tokenization configuration](https://developers.pismo.io/pismo-docs/docs/card-network-tokenization#clone-a-card-network-tokenization-configuration)

# View card network tokenization configurations

To view the list of card network tokenizations at the program level:

1. From the main menu, select **Configurations** > **Card network tokenization**.
2. On the **Card network tokenization** screen, select a program to review its details. Use the **Filter** drop-down menu to find a specific program.

# Create a card network tokenization configuration

To create a card network tokenization configuration at the program level:

1. From the main menu, select **Configurations** > **Card network tokenization**.
2. On the **Card network tokenization** screen, select **Create configuration**.
3. On the **Define details** screen that appears, select the program you want to configure. You can select only one program. Select **Next**.
4. Once you've selected your program, the **Card network tokenization details** screen that appears has three tabs, one for each configuration type available:
   1. **Cardholder verification methods**—Configure cardholder challenge delivery methods that can occur during the tokenization process: email, SMS (text message), application to application (App2App) or call center. You can activate or deactivate each method.
   2. **Acceptance criteria**—Select the options for what is allowed for possible tokenization. For example, you can allow or not allow virtual card tokenization.
   3. **Anti-fraud verification**—You can code an anti-fraud webhook that gets called during the tokenization process. Note: to configure the webhook within Control Center, you must open a Service Desk request for help. To create an anti-fraud webhook outside of Control Center, refer to the [Client webhooks](https://developers.pismo.io/pismo-docs/docs/client-webhooks#client-anti-fraud-webhook-for-card-tokenization) guide.

# Edit a card network tokenization configuration

To edit a card network tokenization configuration at the program level:

1. From the main menu, select **Configurations** > **Card network tokenization**.
2. Select the program you would like to edit.
3. Follow the instructions detailed in step 4 for  **Create a card network tokenization configuration**.

# Clone a card network tokenization configuration

To clone a card network tokenization at the program level:

1. From the main menu, select **Configurations** > **Card network tokenization**.
2. Select the program whose configuration you would like to clone.
3. Select the **Clone** button on the upper-right.
4. On the **Clone tokenization** screen, select the program you would like to clone and select **Next**.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/cards/{cardId}/network-tokens/profile` | `post-v1-cards-card-id-network-tokens-profile` | Assign network card profile | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--network-card-profile |

### Operation essentials

- **`POST /v1/cards/{cardId}/network-tokens/profile`** (`post-v1-cards-card-id-network-tokens-profile`): security `BearerAuth`; required parameters `cardId` (path); required body fields `network_card_profile`; response statuses 204, 400, 401, 500; error codes in examples `ERR93836`, `ERR9786`, `ERR5446`; events none listed.

## Lifecycle status

- `docs/control-center/card-information.md`: updatedAt 2026-07-27T15:30:24.000Z.
- `docs/control-center/card-network-tokenization.md`: updatedAt 2026-03-18T15:10:07.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/card-information.md` | whole document | https://developers.pismo.io/pismo-docs/docs/card-information | `e540fe876db22c68…` | 2026-07-27T15:30:24.000Z |
| `docs/control-center/card-network-tokenization.md` | whole document | https://developers.pismo.io/pismo-docs/docs/card-network-tokenization | `c526056886c5957f…` | 2026-03-18T15:10:07.000Z |

## Related knowledge units

- `KU-API-card-issuing-tokenization--network-card-profile` — API reference: Card issuing - Tokenization — Network card profile
- `KU-CARD-card-lifecycle-and-statuses` — Card lifecycle and statuses
- `KU-CARD-card-tokenization-flow-and-events` — Card tokenization flow and events
- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-CARD-cards-overview-1` — Cards management
- `KU-CARD-digital-wallets` — Digital wallets, MDES Token Connect and Click to Pay
- `KU-CC-dual-approval` — Dual approval
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
