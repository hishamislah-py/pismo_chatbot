---
ku_id: KU-CC-configuration-menus
title: 'Control Center configuration menus: platform, banking and card configurations'
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/platform-configurations.md
  sha256: bb5f7f8976969b093be905a1b17e58f102a92055cc2fd3349e0f00c816b0743a
  url: https://developers.pismo.io/pismo-docs/docs/platform-configurations
  role: primary_guide
  updated_at: '2026-08-26T13:01:12.000Z'
- path: docs/control-center/banking-configurations.md
  sha256: d9dba1b0a5e68ca7c31fb4b3fc31ae4960bffa6ff0b06b0fe74beda3905b33a7
  url: https://developers.pismo.io/pismo-docs/docs/banking-configurations
  role: primary_guide
  updated_at: '2026-03-30T20:46:18.000Z'
- path: docs/control-center/cards-configurations.md
  sha256: 16bd2387f1fb98eb38fbff30bc2db2d7d17277b531170220a288de8691f7d7dd
  url: https://developers.pismo.io/pismo-docs/docs/cards-configurations
  role: primary_guide
  updated_at: '2026-07-28T13:08:35.000Z'
- path: docs/control-center/cc-enable-card-issuing.md
  sha256: aa9ffb12e03b52ce047e8a7a130aa0a84c9f53d7f33a22024d42ddce0f6a3f0e
  url: https://developers.pismo.io/pismo-docs/docs/cc-enable-card-issuing
  role: primary_guide
  updated_at: '2026-04-03T20:49:11.000Z'
operations: []
related_kus:
- KU-CARD-get-started-card-issuing
- KU-CC-balance-configurations
- KU-CC-cards
- KU-CC-copy-configurations
- KU-CC-deposit-products
- KU-CC-embossing-in-control-center
- KU-CC-exchange-rates
- KU-CC-fee-models
- KU-CC-holidays
grouping_rationale: Menu landing pages.
---

# Control Center configuration menus: platform, banking and card configurations

**KU ID:** `KU-CC-configuration-menus` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 4 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Menu landing pages.

Scope as stated in `docs/control-center/platform-configurations.md`:

> Platform configurations are settings that apply across your payment and banking products. For example, you can create programs for both card and deposit products. Similarly, with flex controls, you can set restrictions on credit and debit cards as well as deposit products.

Scope as stated in `docs/control-center/banking-configurations.md`:

> Banking configurations in Control Center are settings specific to banking products, such as savings and checking accounts. When creating these products, you might also need to use [platform-wide configurations](https://developers.pismo.io/pismo-docs/docs/platform-configurations), which apply to all product types.

Scope as stated in `docs/control-center/cards-configurations.md`:

> Card configurations are settings specific to card products like debit, credit, and prepaid cards. When creating your card issuing products, you might also need to use [platform-wide configurations](https://developers.pismo.io/pismo-docs/docs/platform-configurations), which apply to all product types.

Scope as stated in `docs/control-center/cc-enable-card-issuing.md`:

> You can enable card issuing using Control Center. Card issuing is only for debit programs. For information about card issuing on the Pismo platform, refer to [Get started with card issuing](https://developers.pismo.io/pismo-docs/docs/get-started-with-card-issuing).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/platform-configurations.md`: Platform configurations
- `docs/control-center/banking-configurations.md`: Banking configurations
- `docs/control-center/cards-configurations.md`: Card configurations
- `docs/control-center/cc-enable-card-issuing.md`: Enable card issuing

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/platform-configurations.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/platform-configurations · updatedAt: 2026-08-26T13:01:12.000Z

<!-- source:begin path=docs/control-center/platform-configurations.md part=0-end -->

# Platform configurations

Platform configurations are settings that apply across your payment and banking products. For example, you can create programs for both card and deposit products. Similarly, with flex controls, you can set restrictions on credit and debit cards as well as deposit products.

Platform configurations include:

* [Balance configurations](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center)—Balance configurations are a flexible set of rules that define how account balances and limits are impacted based on transaction activity. You can use balance configurations to proactively manage risk, encourage responsible spending, and deliver personalized experiences to your customers.
* [Copy configurations](https://developers.pismo.io/pismo-docs/docs/copy-configurations)—The copy configurations feature enables you to reuse existing configurations across Control Center environments without having to recreate them manually.
* [Exchange rates](https://developers.pismo.io/pismo-docs/docs/exchange-rates)—The Pismo platform supports multi-currency exchange rates for international transactions. Create up to 100 exchange rates at once for your entire organization or specific programs.
* [Fee models](https://developers.pismo.io/pismo-docs/docs/fee-models-in-control-center)—Fee models are customizable structures that groups together different types of fees and define how each one is calculated. You can choose how each fee is applied—whether it’s a fixed amount, a percentage, or another method that fits your needs.
* [Flex controls](https://developers.pismo.io/pismo-docs/docs/flex-controls-in-control-center)—Flex controls are rules that restrict your customers' financial operations, such as spending limits or time-based restrictions.
* [General ledger accounts](https://developers.pismo.io/pismo-docs/docs/general-ledger-accounts-in-control-center)—General ledger accounts maintain a comprehensive record of all financial transactions that occur within an organization.
* [Holidays](https://developers.pismo.io/pismo-docs/docs/holidays)—Holiday calendars define your organization’s working and non-working days.
* [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types-cc)—Processing codes identify financial operations on the Pismo platform. They're defined at the organization level, so you can apply them across all programs and their associated accounts.
* [Programs](https://developers.pismo.io/pismo-docs/docs/programs-in-control-center)—Programs define a set of parameters for a group of accounts. A program has a  type, such as credit, debit, or prepaid. Within programs you create accounts and customers.

<br />
<!-- source:end -->

### Source 2: `docs/control-center/banking-configurations.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/banking-configurations · updatedAt: 2026-03-30T20:46:18.000Z

<!-- source:begin path=docs/control-center/banking-configurations.md part=0-end -->

# Banking configurations

Banking configurations in Control Center are settings specific to banking products, such as savings and checking accounts. When creating these products, you might also need to use [platform-wide configurations](https://developers.pismo.io/pismo-docs/docs/platform-configurations), which apply to all product types.

Banking configurations include:

* [Deposit products](https://developers.pismo.io/pismo-docs/docs/deposit-products-in-control-center)—These are interest-bearing accounts to which you can apply interest, fees, taxes, and so on. In Control Center, you can only attach debit accounts.
* [Interest plans](https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center)—Interest plans are configurations that define how interest is calculated and applied to a specific product. These settings can include the interest rate, the compounding period (for example, daily, monthly, or quarterly), tax implications, and more. You can use interest plans for deposit and loan products.

<br />
<!-- source:end -->

### Source 3: `docs/control-center/cards-configurations.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cards-configurations · updatedAt: 2026-07-28T13:08:35.000Z

<!-- source:begin path=docs/control-center/cards-configurations.md part=0-end -->

# Card configurations

Card configurations are settings specific to card products like debit, credit, and prepaid cards. When creating your card issuing products, you might also need to use [platform-wide configurations](https://developers.pismo.io/pismo-docs/docs/platform-configurations), which apply to all product types.

Card configurations include:

* [Card network tokenization](https://developers.pismo.io/pismo-docs/docs/card-network-tokenization)—Protect transactions by replacing sensitive card data with encrypted tokens.
* [Embossing](https://developers.pismo.io/pismo-docs/docs/embossing-in-control-center)—Manage embossing configurations, such as the embossing schedule and the programs associated with specific configurations.
* [Transaction categories](https://developers.pismo.io/pismo-docs/docs/transaction-categories-in-control-center)—Use transaction categories to group transaction types and set properties for the group. Transaction types, in combination with processing codes, define how financial operations are implemented on the Pismo platform.
<!-- source:end -->

### Source 4: `docs/control-center/cc-enable-card-issuing.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cc-enable-card-issuing · updatedAt: 2026-04-03T20:49:11.000Z

<!-- source:begin path=docs/control-center/cc-enable-card-issuing.md part=0-end -->

# Enable card issuing

You can enable card issuing using Control Center. Card issuing is only for debit programs. For information about card issuing on the Pismo platform, refer to [Get started with card issuing](https://developers.pismo.io/pismo-docs/docs/get-started-with-card-issuing).

To enable card issuing for a debit program that doesn't already have it enabled:

1. From the main menu, select **Configurations** > **Programs**.

2. On the **Programs** screen, select the debit program you want to edit.

3. On the **Program information** screen, select **BIN range**.

4. Select **Issue card**. <p>Note: This button displays only if card issuing isn't already enabled for the program.</p>

5. Select **Continue**.

6. Enter the values for **Brand**, **BIN**, and **BIN range** as required and select **Save**.
<!-- source:end -->

## Lifecycle status

- `docs/control-center/platform-configurations.md`: updatedAt 2026-08-26T13:01:12.000Z.
- `docs/control-center/banking-configurations.md`: updatedAt 2026-03-30T20:46:18.000Z.
- `docs/control-center/cards-configurations.md`: updatedAt 2026-07-28T13:08:35.000Z.
- `docs/control-center/cc-enable-card-issuing.md`: updatedAt 2026-04-03T20:49:11.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/platform-configurations.md` | whole document | https://developers.pismo.io/pismo-docs/docs/platform-configurations | `bb5f7f8976969b09…` | 2026-08-26T13:01:12.000Z |
| `docs/control-center/banking-configurations.md` | whole document | https://developers.pismo.io/pismo-docs/docs/banking-configurations | `d9dba1b0a5e68ca7…` | 2026-03-30T20:46:18.000Z |
| `docs/control-center/cards-configurations.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cards-configurations | `16bd2387f1fb98eb…` | 2026-07-28T13:08:35.000Z |
| `docs/control-center/cc-enable-card-issuing.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cc-enable-card-issuing | `aa9ffb12e03b52ce…` | 2026-04-03T20:49:11.000Z |

## Related knowledge units

- `KU-CARD-get-started-card-issuing` — Get started with card issuing
- `KU-CC-balance-configurations` — Control Center balance configurations
- `KU-CC-cards` — Control Center cards: card information and card network tokenization
- `KU-CC-copy-configurations` — Copy configurations
- `KU-CC-deposit-products` — Control Center deposit products and interest plans
- `KU-CC-embossing-in-control-center` — Embossing
- `KU-CC-exchange-rates` — Exchange rates in Control Center
- `KU-CC-fee-models` — Control Center fee models: manage and link fee models
- `KU-CC-holidays` — Holidays
