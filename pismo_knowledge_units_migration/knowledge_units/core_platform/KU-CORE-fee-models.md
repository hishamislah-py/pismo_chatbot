---
ku_id: KU-CORE-fee-models
title: Fee management and fee models
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/fee-management.md
  sha256: 5237a0ba5b912e95586412d0089ea9fb172389fbce0dd99b30bb27e84a5cbc89
  url: https://developers.pismo.io/pismo-docs/docs/fee-management
  role: primary_guide
  updated_at: '2026-04-24T02:15:11.000Z'
- path: docs/core-platform/fee-models.md
  sha256: e818fb2c5f3d8689349b163e91ad51d4e72a78f3d6073ca860f0c31189e1a785
  url: https://developers.pismo.io/pismo-docs/docs/fee-models
  role: primary_guide
  updated_at: '2026-04-28T01:49:22.000Z'
operations: []
related_kus:
- KU-CORE-fee-models-create-and-simulate
- KU-CORE-over-limit-fee
grouping_rationale: Overview and fee-model concepts.
---

# Fee management and fee models

**KU ID:** `KU-CORE-fee-models` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Overview and fee-model concepts.

Scope as stated in `docs/core-platform/fee-management.md`:

> The Pismo platform has solutions to help financial institutions and fintechs manage a growing set of fees, taxes, and exceptions across multiple products and customer segments. In particular, Pismo offers:

Scope as stated in `docs/core-platform/fee-models.md`:

> A fee model is a framework that defines a collection of fees and interest with custom calculations. It is a governed, centralized rule set for fees and taxes. It consolidates all fee policies in one place, including both the calculation logic and the conditions under which the fee is applied. You can define the method used to calculate the fee, such as a fixed value or a percentage. Fees can originate from various origins, such as local taxes or business fees applicable to specific types of transactions. The Pismo platform enables you to define all taxes, interest, and fees you need into one fee model and apply them to your operations, according to the hierarchy of account, program, or organization.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/fee-management.md`: Fee management
- `docs/core-platform/fee-models.md`: Fee models; Fee model overview; Business benefits; Rules and triggers; Calculation rules; Triggers (processing codes); Hierarchy of control; Next steps

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/fee-management.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/fee-management · updatedAt: 2026-04-24T02:15:11.000Z

<!-- source:begin path=docs/core-platform/fee-management.md part=0-end -->

# Fee management

The Pismo platform has solutions to help financial institutions and fintechs manage a growing set of fees, taxes, and exceptions across multiple products and customer segments. In particular, Pismo offers:

* **Fee models**—The Pismo platform offers a configurable fee model framework that allows you to define all fees applied during authorization. Fee models provide a centralized fee logic (calculation and event triggers), enabling rapid change with strong control and reduced engineering dependency. Fees are applied in a hierarchy where one fee can override another fee, where the hierarchy is account > program > organization. For example, a fee model attached to an organization is only used if there is no program or account level fee model overriding the organization.

  For full details on creating and using fee models, refer to the [Fee models](https://developers.pismo.io/pismo-docs/docs/fee-models) guide.
* **Over-limit fees**—Over-limit fees help offset the added risk of approving transactions beyond the original credit limit. The Pismo platform allows you to configure your accounts to allow account holders to go over their maximum credit limit when making purchases. You can define an over-limit percentage and an optional fee to be charged at the end of the cycle whenever the account goes over the maximum credit limit during that cycle. These fees apply outside of transaction events and are applied from a balance perspective. The Pismo platform offers a [Balance watcher](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant-1) API for you to enable and configure over-limit fees. This API listens for platform and card network events and triggers actions based on these events.

  For details on configuring and enabling over-limit fees, refer to the [Over-limit fees](https://developers.pismo.io/pismo-docs/docs/over-limit-fee) guide.

<br />
<!-- source:end -->

### Source 2: `docs/core-platform/fee-models.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/fee-models · updatedAt: 2026-04-28T01:49:22.000Z

<!-- source:begin path=docs/core-platform/fee-models.md part=0-end -->

# Fee models

A fee model is a framework that defines a collection of fees and interest with custom calculations. It is a governed, centralized rule set for fees and taxes. It consolidates all fee policies in one place, including both the calculation logic and the conditions under which the fee is applied. You can define the method used to calculate the fee, such as a fixed value or a percentage. Fees can originate from various origins, such as local taxes or business fees applicable to specific types of transactions. The Pismo platform enables you to define all taxes, interest, and fees you need into one fee model and apply them to your operations, according to the hierarchy of account, program, or organization.

Fee models enable the flexible, centralized, and automated definition, grouping, and application of fees during transaction processing. A fee model is a mechanism that determines which fees will be charged, how they will be calculated, and to which transactions they apply.

<Embed typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=fnbQeFZpQj8" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FfnbQeFZpQj8%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DfnbQeFZpQj8%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FfnbQeFZpQj8%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22800%22%20height%3D%22450%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" href="https://www.youtube.com/watch?v=fnbQeFZpQj8" providerUrl="https://www.youtube.com/" providerName="YouTube" />

<br />

# Fee model overview

<Image align="center" alt="Graphic showing the linking hierarchy and basic rules of fee model management" src="https://files.readme.io/5eefd227e7f6b3d0a314b1ea17dd021fe3d9ef6a31fde27f8a3ed8026067b7bf-Fee_models6.png" />

## Business benefits

Centralizing fee policy into configurable models improves pricing agility and governance. Teams can introduce and adjust fees faster, apply them consistently across products and segments, and manage exceptions with clear controls—reducing operational risk while supporting revenue optimization.

This approach delivers these primary business outcomes:

* **High configurability**—Support a wide range of fee and tax structures to match diverse product and market needs.
* **Granular control**—Apply pricing policies at the organization, program, or individual account level to support segmentation and exceptions.
* **Faster time-to-market**—Launch, test, and adjust fees with reduced engineering dependency, enabling quicker product iteration and pricing optimization.

In addition, fee models are unique and flexible and have these key advantages:

* **Temporality**—Using a fee model ensures that the same fee condition will be applied on authorization and confirmation even if the fee model has changed between those events.
* **Autonomy**—Fee models have all configurations available through external endpoints and also through Pismo  Control Center, giving you even more autonomy.
* **Variety of settings**—Fee models allow you to create different fees, with multiple calculation types, including options to add or deduct fees from transaction amount. You can also configure aging, amounts accumulators, and other options to support most business cases.

# Rules and triggers

Each fee is defined by a calculation rule or method (what to charge) and a processing code trigger (when to charge). This separates policy from execution and supports consistent application at scale. Calculation rules specify the amount or rate and any conditional logic. Triggers define the event types that activate the fee.

## Calculation rules

Fee calculations can be configured as a flat amount, a percentage of a transaction, conditional logic (for example,  greater of, fixed, or percentage), and credit-specific constructs such as a daily percentage. This flexibility supports diverse product pricing strategies without custom code for each scenario.

The following are the available calculation methods. For details and examples, refer to the [Creating and applying fee models](https://developers.pismo.io/pismo-docs/docs/create-fee-model) guide.

* **FIXED**—Applies fixed amount fees to specified transactions
* **PERCENTAGE**—Applies a percentage fee amount to specified transactions
* **GREATER**—Applies a fixed or percentage fee amount to specified transactions depending on which is greater
* **DAILY\_PERCENTAGE**—Applies a daily simple interest percentage to things like credit card cash advances and other loan type products until the next cycle closing
* **COMPOUND\_INTEREST**—Defines when interest is compounded on loan type products
* **ACCUMULATOR**—Collects totals based on specified transaction types and applies a fixed or percentage fee on a scheduled basis
* **DYNAMIC BY AMOUNT**—Calculation strategy that allows you to apply "automatic" fees over DC accounts for situations such as withdrawal before due date
* **EQUAL INSTALLMENTS**—Calculates loan repayments (or installment plans) so that all installments have the same total amount throughout the life of the contract

The following methods apply to Brazil only:

* **PRICE TABLE**—Calculates loan repayments (installment plans) so that all installments have the same total amount throughout the life of the contract, adding some specific fee calculations including the IOF amount being financed
* **AGING**—Determines how fees are calculated and applied to investments over time
* **IOF**—Determines how Brazilian IOF taxes are calculated for investments

## Triggers (processing codes)

Once you've created a fee model, use processing codes to link each fee included in the fee model to financial operations. Processing codes identify an operation, such as purchases or debits. Each financial operation within the platform has its own processing code. You can configure some processing codes, while others are fixed in the card network flow. Talk to your Pismo representative to get or create processing codes.

Processing codes act as discrete triggers. Each financial operation is represented by a unique code that can activate a fee when matched. By linking each fee from your fee model to a specific processing code, the platform applies fees with high precision—ensuring charges are assessed only for the intended transaction types and reducing disputes and reconciliation effort.

<Callout icon="📘" theme="info">
  The operation must match the processing code

  The fee is ignored if the operation doesn't match the defined processing codes.
</Callout>

# Hierarchy of control

Fees are applied through a hierarchy to balance global governance with product and customer-level customization. The Pismo platform applies fee models using a three-level hierarchy, enabling standardization while supporting targeted overrides.

At the most basic level, you have the organization level. This is the big global default. It's the baseline fee model that applies to every single account across your entire business.

The next level up is the program level. Imagine you have a gold card or maybe a student account with its own unique fees. A fee model at this level overrides the global default, but only for accounts that are part of that specific product.

Finally, for the ultimate level of precision, you can go all the way down to a single account.

**Override rule:** The system applies exactly one fee model—the most specific model available. Account-level overrides take precedence over program-level models, which take precedence over the organization default.

<Callout icon="📘" theme="info">
  Cloned programs

  When you clone a program, the fee model links are not cloned automatically. You must link the applicable fee model to the cloned program.
</Callout>

# Next steps

Now that you have a basic understanding of what fee models are and how they can help fulfill your business needs, you can start creating your own fee models. Refer to the [Creating and applying fee models](create-fee-model) guide to get started.

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.


### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `post-config-by-tenant-1` | Authorization configurations; Balance watcher; Create configuration by org; Limit configurations | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Lifecycle status

- `docs/core-platform/fee-management.md`: updatedAt 2026-04-24T02:15:11.000Z.
- `docs/core-platform/fee-models.md`: updatedAt 2026-04-28T01:49:22.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Operation link `post-config-by-tenant-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/fee-management.md` | whole document | https://developers.pismo.io/pismo-docs/docs/fee-management | `5237a0ba5b912e95…` | 2026-04-24T02:15:11.000Z |
| `docs/core-platform/fee-models.md` | whole document | https://developers.pismo.io/pismo-docs/docs/fee-models | `e818fb2c5f3d8689…` | 2026-04-28T01:49:22.000Z |

## Related knowledge units

- `KU-CORE-fee-models-create-and-simulate` — Creating, applying and simulating fee models
- `KU-CORE-over-limit-fee` — Over-limit fees
