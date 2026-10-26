---
ku_id: KU-GS-platform-overview-and-solutions
title: Pismo platform overview, main solutions and where to start
category: getting_started
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/pismo-platform-overview.md
  sha256: 2b50f2bc5b7d214d8d0fa1d1b7c9b0452dde3c3f4ca3c12608ed55938df8af70
  url: https://developers.pismo.io/pismo-docs/docs/pismo-platform-overview
  role: primary_guide
  updated_at: '2026-06-29T22:20:57.000Z'
- path: docs/get-started/main-solutions.md
  sha256: 1e14f44aa424f56f495f47ee92e1a1abb3f36322a1e049c76eb59fd8c97d8c40
  url: https://developers.pismo.io/pismo-docs/docs/main-solutions
  role: primary_guide
  updated_at: '2026-06-29T21:57:11.000Z'
- path: docs/get-started/start-building.md
  sha256: e40667c128618db79d4b7e22ebc61699da9329dc9c751c4b9ab4eff24af97a01
  url: https://developers.pismo.io/pismo-docs/docs/start-building
  role: primary_guide
  updated_at: '2026-06-29T19:49:07.000Z'
operations: []
related_kus:
- KU-AUTH-security-programme
- KU-BANK-banking-overview
- KU-BANK-get-started-building-banking
- KU-BANK-transaction-banking-accounts
- KU-CARD-digital-wallets
- KU-CARD-get-started-card-issuing
- KU-CC-get-started-control-center
- KU-EVT-data-events-concepts
- KU-GS-ai-assisted-documentation
- KU-GS-environments
- KU-GS-pismo-platform-onboarding
- KU-GS-program-types
- KU-GS-setup-overview
- KU-GS-welcome
- KU-LEND-get-started-lending
- KU-LEND-lending-overview
- KU-SELL-get-started-seller-management
- KU-SELL-seller-management-overview-and-onboarding
grouping_rationale: Orientation pages that link to each other.
---

# Pismo platform overview, main solutions and where to start

**KU ID:** `KU-GS-platform-overview-and-solutions` · **Category:** Getting started · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Orientation pages that link to each other.

Scope as stated in `docs/get-started/pismo-platform-overview.md`:

> Use this set of guides to understand the key pieces of the Pismo platform. They walk you through what the main solutions do, how core objects and programs work, and how environments and data events fit into your development and operations workflow.

Scope as stated in `docs/get-started/main-solutions.md`:

> Pismo offers cloud-based platform solutions that enable banks, fintechs, and non-financial institutions to deliver cutting edge global financial products. These solutions share the following features:

Scope as stated in `docs/get-started/start-building.md`:

> Explore and start building your payment, banking, and lending programs with help from our suite of get started guides. Whether you’re a new customer setting up access or an existing customer enabling new capabilities, these guides walk you through the essential concepts, prerequisites, and first steps.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/pismo-platform-overview.md`: Learn about the Pismo platform
- `docs/get-started/main-solutions.md`: Main solutions; Card issuing; Digital wallets; Core banking; Transaction banking; Online marketplaces; Lending
- `docs/get-started/start-building.md`: Start building; &#x20;New to Pismo?; Already a Pismo customer but looking to do more?; Need more help using the Developers Portal?

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/pismo-platform-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pismo-platform-overview · updatedAt: 2026-06-29T22:20:57.000Z

<!-- source:begin path=docs/get-started/pismo-platform-overview.md part=0-end -->

# Learn about the Pismo platform  

Use this set of guides to understand the key pieces of the Pismo platform. They walk you through what the main solutions do, how core objects and programs work, and how environments and data events fit into your development and operations workflow.

[Main solutions](https://developers.pismo.io/pismo-docs/docs/main-solutions)—Explore Pismo’s solutions and the capabilities they provide.

[Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview)—Get an overview of core objects, the building blocks of the Pismo platform.

[Program types](https://developers.pismo.io/pismo-docs/docs/program-types)—Discover program types to learn how each one defines the accounts and products your customers can open.

[Environments](https://developers.pismo.io/pismo-docs/docs/environments)—Understand how Pismo separates testing and production environments, enabling you to validate changes safely before they affect live customers and systems.

[Data events](https://developers.pismo.io/pismo-docs/docs/event-data)—Learn how Pismo sends you a stream of event data about what’s happening on the platform so you can monitor activity and integrate it into your own systems.

<br />
<!-- source:end -->

### Source 2: `docs/get-started/main-solutions.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/main-solutions · updatedAt: 2026-06-29T21:57:11.000Z

<!-- source:begin path=docs/get-started/main-solutions.md part=0-end -->

# Main solutions

Pismo offers cloud-based platform solutions that enable banks, fintechs, and non-financial institutions to deliver cutting edge global financial products. These solutions share the following features:

* Extensive RESTful API library with more than 600 integration endpoints
* Auto-scaling cloud-based infrastructure
* High-availability (24 × 7 × 365), multi-region processing
* Cloud infrastructure certified for PCI, ISO 27001, and SOC II compliance
* Control Center, the web-based interface you can use to complete many tasks without using REST APIs

# Card issuing

Issue debit, credit, pre-paid, white-label, and private label cards. Pismo's [card issuing system](https://developers.pismo.io/pismo-docs/docs/get-started-with-card-issuing) offers native integrations with major card networks with high security and resilience.

Card features include:

* Instant **tokenized** (virtual) card creation with flexible expiration and dynamic CVV
* Card production integration with current templates
* Life cycle management (billing, refinancing, revolving credit, and debt restructuring)

# Digital wallets

Create your own [digital wallets](https://developers.pismo.io/pismo-docs/docs/wallet-overview) to manage both buyers and sellers. You can use cards or tokens to pay from a Pismo wallet. Other features include:

* Network and proprietary tokenizations for cards
* QR codes and other forms of token encoding
* Granular event-based information for user behavior analysis

# Core banking

Build a suite of [digital banking](https://developers.pismo.io/pismo-docs/docs/banking-overview) products—from deposits and savings to overdrafts. Digital banking with Pismo offers:

* Complete banking functionality, including ledgers, savings accounts, current accounts, deposits, and overdrafts
* Spending limits and controls at the account level
* Native integrations with credit card networks, anti-fraud services, card embossers, and other third-party providers

# Transaction banking

While retail banks are designed to serve individuals, transaction banking focuses on transactions between a bank and a large organization, such as a multinational corporation, lending for short-term expenses and long-term investments. The [transaction banking](https://developers.pismo.io/pismo-docs/docs/corporate-banking-overview) solution extends core banking features to meet the needs of institutional customers. Highlights include:

* Model the bank's organizational structure using a flexible hierarchy of levels and divisions.
* Manage holidays and weekends for different divisions.
* Create accounts with parent/child relationships.
* Create earmarks.
* Automatically change account statuses based on inactivity.
* Create a suspense transaction record upon authorization denial.

# Online marketplaces

Create a complete transaction-processing and seller-management infrastructure for both e-commerce and in-store purchases. The platform offers a complete solution for acquiring and settlement in a multi-country, multi-currency environment. Other benefits of Pismo [digital marketplaces](https://developers.pismo.io/pismo-docs/docs/seller-management-overview) include:

* Ability to manage vendors and buyers on the same platform
* Capabilities to handle transactions from on-us and off-us merchants and settle them
* Functions for sellers to pay their creditors using their merchant accounts

# Lending

Create loan products tailored for your customers. With [lending](https://developers.pismo.io/pismo-docs/docs/lending-overview), you can:

* Create personal loan products.
* Create **Buy Now, Pay Later (BNPL)** loan products. BNPL divides the total purchase amount into a series of equal installment payments, with only the first installment due at checkout.
* Manage the complete lifecycle of a loan.
* Create loan simulations.
* Perform instant booking.
* Perform instant disbursement.
* Perform loan repayment and settlement.
<!-- source:end -->

### Source 3: `docs/get-started/start-building.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/start-building · updatedAt: 2026-06-29T19:49:07.000Z

<!-- source:begin path=docs/get-started/start-building.md part=0-end -->

# Start building

Explore and start building your payment, banking, and lending programs with help from our suite of get started guides. Whether you’re a new customer setting up access or an existing customer enabling new capabilities, these guides walk you through the essential concepts, prerequisites, and first steps.

### &#x20;New to Pismo?

Start with [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

### Already a Pismo customer but looking to do more?

Explore these additional guides.

| Guide                                                                             | Description                                                                                                                                                |
| :-------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Get started with Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-building-control-center)        | Introduces Control Center, a web-based interface you can use to complete many tasks without using REST APIs.                                               |
| [Get started with banking ](https://developers.pismo.io/pismo-docs/docs/get-started-building-banking)                     | Outlines the steps for setting up the full suite of banking products for your customers, including both core banking and transaction banking capabilities. |
| [Get started with card issuing ](https://developers.pismo.io/pismo-docs/docs/get-started-building-card-issuing)           | Details how to set up and manage card-issuing programs, from integration and program setup to card creation and monitoring.                                |
| [Get started with lending ](https://developers.pismo.io/pismo-docs/docs/get-started-building-lending)                     | Explains how to configure the core components for lending, including products, processing codes, and repayment structures.                                 |
| [Get started with Seller management ](https://developers.pismo.io/pismo-docs/docs/get-started-building-seller-management) | Shows how to set up marketplaces, merchants, receivables, fees, advances, and settlements.                                                                 |

### Need more help using the Developers Portal?

Refer to the following guides for more in-depth support.

| Guide                                                          | Description                                                                                                                           |
| :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| [Get started with the Pismo Developers Portal](https://developers.pismo.io/pismo-docs/docs/welcome)    | Introduces how to use the Pismo Developer Portal and where to find key guides and reference. Includes an introductory video.          |
| [Get started with Ask AI](https://developers.pismo.io/pismo-docs/docs/get-started-with-ask-ai)         | Describes how to use AI-powered search in the Developers Portal to find answers and related content.                                  |
| [Get started with Pismo APIs](https://developers.pismo.io/pismo-docs/reference/get-started-with-pismo-apis) | Explains how to integrate Pismo solutions into your applications and configure them using Pismo’s 700+ integration endpoints.         |
| [Learn about the Pismo platform](https://developers.pismo.io/pismo-docs/docs/pismo-platform-overview)  | Gives an overview of Pismo’s main solutions, core objects and programs, and how environments and data events fit into your workflows. |
| [Security](https://developers.pismo.io/pismo-docs/docs/security)                                       | Details how Pismo helps protect your business assets through a robust set of security technologies, controls, and practices.          |

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.


### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `get-started-with-pismo-apis` | Get started with Pismo APIs | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Lifecycle status

- `docs/get-started/pismo-platform-overview.md`: updatedAt 2026-06-29T22:20:57.000Z.
- `docs/get-started/main-solutions.md`: updatedAt 2026-06-29T21:57:11.000Z.
- `docs/get-started/start-building.md`: updatedAt 2026-06-29T19:49:07.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Operation link `get-started-with-pismo-apis` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/pismo-platform-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pismo-platform-overview | `2b50f2bc5b7d214d…` | 2026-06-29T22:20:57.000Z |
| `docs/get-started/main-solutions.md` | whole document | https://developers.pismo.io/pismo-docs/docs/main-solutions | `1e14f44aa424f56f…` | 2026-06-29T21:57:11.000Z |
| `docs/get-started/start-building.md` | whole document | https://developers.pismo.io/pismo-docs/docs/start-building | `e40667c128618db7…` | 2026-06-29T19:49:07.000Z |

## Related knowledge units

- `KU-AUTH-security-programme` — Security programme: compliance, certifications, audits and incident response
- `KU-BANK-banking-overview` — Banking overview
- `KU-BANK-get-started-building-banking` — Get started with banking
- `KU-BANK-transaction-banking-accounts` — Transaction banking and transaction banking accounts
- `KU-CARD-digital-wallets` — Digital wallets, MDES Token Connect and Click to Pay
- `KU-CARD-get-started-card-issuing` — Get started with card issuing
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-EVT-data-events-concepts` — Data events: concepts and event-generating APIs
- `KU-GS-ai-assisted-documentation` — AI-assisted documentation: Ask AI and LLM access
- `KU-GS-environments` — Environments
- `KU-GS-pismo-platform-onboarding` — Onboarding for new customers
- `KU-GS-program-types` — Program types
- `KU-GS-setup-overview` — Core objects
- `KU-GS-welcome` — Get started with the Pismo Developers Portal
- `KU-LEND-get-started-lending` — Get started with lending
- `KU-LEND-lending-overview` — Lending overview and participants
- `KU-SELL-get-started-seller-management` — Get started with seller management
- `KU-SELL-seller-management-overview-and-onboarding` — Seller management overview and onboarding
