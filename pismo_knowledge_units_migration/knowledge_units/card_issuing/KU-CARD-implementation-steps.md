---
ku_id: KU-CARD-implementation-steps
title: Card issuing implementation steps 1 to 7
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/step-1-plan.md
  sha256: 4215b62a0e30996c0bde08b5d62bef74fda38563185df8eeadb6a33cd64da511
  url: https://developers.pismo.io/pismo-docs/docs/step-1-plan
  role: primary_guide
  updated_at: '2026-04-27T17:55:17.000Z'
- path: docs/card-issuing/step-2-establish-a-framework.md
  sha256: b131d6a1b1ef7f289cc6df4f6fd6ca64f9b5f2a6e836a5eff70b4c4e5a00b2dc
  url: https://developers.pismo.io/pismo-docs/docs/step-2-establish-a-framework
  role: primary_guide
  updated_at: '2026-06-28T23:10:44.000Z'
- path: docs/card-issuing/step-3-create-your-programs.md
  sha256: 804b5a0f4473f932500983df0642ad7afa348c972f059df467571b7cd79a7a2f
  url: https://developers.pismo.io/pismo-docs/docs/step-3-create-your-programs
  role: primary_guide
  updated_at: '2026-09-01T18:06:39.000Z'
- path: docs/card-issuing/step-4-create-accounts-and-customers.md
  sha256: 7a18491202524295a939befee8c0dbee6ae47b7036ea68c25530a50b319f0a50
  url: https://developers.pismo.io/pismo-docs/docs/step-4-create-accounts-and-customers
  role: primary_guide
  updated_at: '2026-04-03T20:46:23.000Z'
- path: docs/card-issuing/step-5-create-cards.md
  sha256: dde2c446bd053710437c0de005ec81f813af801998f063229bb2d6a5c56596b7
  url: https://developers.pismo.io/pismo-docs/docs/step-5-create-cards
  role: primary_guide
  updated_at: '2026-04-03T20:46:23.000Z'
- path: docs/card-issuing/step-5-test.md
  sha256: d7350f565083e1a947f7da15292ebcfd7f19209c692b54ebfe778e09ce202441
  url: https://developers.pismo.io/pismo-docs/docs/step-5-test
  role: primary_guide
  updated_at: '2026-04-29T12:33:59.000Z'
- path: docs/card-issuing/step-6-monitor.md
  sha256: f0561b41b6c078ec11e5df6cf0354899bf3558305e3fae1ace50b50884b70f5f
  url: https://developers.pismo.io/pismo-docs/docs/step-6-monitor
  role: primary_guide
  updated_at: '2026-04-03T20:46:23.000Z'
operations:
- CopyProgram
- CreateProgramBasedOnTemplate
- customerV2Post
- getProgramExportDownload
- post-acquisitions-v3-s2s-applications
- post-v2-card
- postProgramExport
- postProgramImport
related_kus:
- KU-API-card-issuing-cards--cards
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--customers
- KU-API-platform-setup-programs--export-and-import
- KU-API-platform-setup-programs--programs-part-01
- KU-CARD-anti-fraud-integration
- KU-CARD-card-network-integration
- KU-CARD-cards-overview-1
- KU-CARD-disputes-overview
- KU-CARD-full-balance-versus-zero-balance
- KU-CARD-physical-card-embossing
- KU-CC-accounts
- KU-CC-programs
- KU-CORE-accounting-overview
- KU-CORE-accounts-overview
- KU-CORE-exchange-rate
- KU-CORE-flex-controls
- KU-CORE-platform-setup-holidays
- KU-CORE-processing-codes-and-transaction-types
- KU-CORE-program-parameters-reference-table
- KU-CORE-transactiontypes
- KU-CRED-understanding-statements
- KU-EVT-catalogue-account
- KU-EVT-catalogue-cards
- KU-EVT-catalogue-other-domains
- KU-GS-pismo-platform-onboarding
- KU-GS-program-types
- KU-RPT-scheduled-reports
grouping_rationale: One ordered implementation series (file step-5-test is titled Step 6; step-6-monitor is titled Step 7).
---

# Card issuing implementation steps 1 to 7

**KU ID:** `KU-CARD-implementation-steps` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 7 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: One ordered implementation series (file step-5-test is titled Step 6; step-6-monitor is titled Step 7).

Scope as stated in `docs/card-issuing/step-1-plan.md`:

> Use this planning section to identify the integration decisions to consider when building your card issuing program.

Scope as stated in `docs/card-issuing/step-2-establish-a-framework.md`:

> The Pismo support team works closely with you to establish a framework for your card issuing program. This framework consists of onboarding tasks and getting card network certification.

Scope as stated in `docs/card-issuing/step-3-create-your-programs.md`:

> Now that you have a basic framework, you can create your card issuing program. You might want to create multiple programs. For example, to use both Visa and Mastercard as your card providers, create two programs, one for Visa and another for Mastercard. Or if you want to issue debit and credit cards, you’ll need to create two programs.

Scope as stated in `docs/card-issuing/step-4-create-accounts-and-customers.md`:

> You've set up your card issuing programs, so now you're ready to create accounts and customers.

Scope as stated in `docs/card-issuing/step-5-create-cards.md`:

> At this point, you’re ready to create your cards. You’ll use [Pismo APIs](https://developers.pismo.io/pismo-docs/reference/post-v2-card)  and endpoints to create cards, with help from the Pismo support team.

Scope as stated in `docs/card-issuing/step-5-test.md`:

> Your Pismo support team will work with you to test the integrated system to verify that it meets all security and functionality requirements. Together, we’ll build test plans and scripts, then execute them to ensure that you’ve tested transactions, card activations, and other key features.

Scope as stated in `docs/card-issuing/step-6-monitor.md`:

> After creating your card issuing program, you’ll continuously monitor its performance and value against your business objectives. We partner with you, helping you optimize processes, resolve issues, and introduce new products and features to your customers.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/step-1-plan.md`: Step 1: Plan; 1. Build your business case; 2. Build a project team; 3. Ensure you meet all regulatory, compliance, and legal requirements; 4. Define your card issuing strategy; 5. Create your governance model
- `docs/card-issuing/step-2-establish-a-framework.md`: Step 2: Establish a framework; Complete onboarding tasks; Get card network certification
- `docs/card-issuing/step-3-create-your-programs.md`: Step 3: Create your programs; Choose your program type; Create a program; Define program features
- `docs/card-issuing/step-4-create-accounts-and-customers.md`: Step 4: Create accounts and customers; Create an account; Create additional customers
- `docs/card-issuing/step-5-create-cards.md`: Step 5: Create cards
- `docs/card-issuing/step-5-test.md`: Step 6: Test the integrated setup; Oversee your program with data events and reports; Test Pismo API endpoints with Postman
- `docs/card-issuing/step-6-monitor.md`: Step 7: Track performance and support users; Minimize fraud; Manage cardholder disputes; Administer statements

## Prerequisites and dependencies

- Prerequisites are described in `docs/card-issuing/step-1-plan.md` section "3. Ensure you meet all regulatory, compliance, and legal requirements".
- Depends on 8 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/step-1-plan.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-1-plan · updatedAt: 2026-04-27T17:55:17.000Z

<!-- source:begin path=docs/card-issuing/step-1-plan.md part=0-end -->

# Step 1: Plan

Use this planning section to identify the integration decisions to consider when building your card issuing program.

# 1. Build your business case

Start by identifying your business objectives. Develop a comprehensive business plan that outlines your goals, target market, revenue model, and growth strategy.

<h2>Considerations</h2>

**Which countries will you offer your product in?**

* [ ] Research the country’s tax laws affecting card products.
* [ ] If you’re using ATMs, decide how you will integrate with each country’s ATMs.
* [ ] Determine which currencies you’ll support and if you’ll impose cross-border fees.

**What’s your target market?**

* [ ] Consider whether you’re targeting a corporate audience, consumers, or both.
* [ ] Understand your market segmentation. Research the market and your competition, which can help you find a new niche, create innovative products, or leverage an existing business.
* [ ] Define your go-to-market strategy.

**What’s your sales strategy?**

* [ ] Create your customer profiles or personas.
* [ ] Decide on the type of product you want to offer (for example, standard or premium).
* [ ] Consider whether you’ll offer loyalty or reward programs.
* [ ] Decide if your product is part of a special promotion.
* [ ] Decide whether you want to offer introductory pricing and bonuses.

**What’s your marketing strategy?**

* [ ] Create your card design and imagery.
* [ ] Design your card packaging and whether you’ll include promotional materials, terms and conditions, and so on.
* [ ] Define how you’ll use your marketing materials (in store, online, booths, trade shows, and so on).
* [ ] Define your advertising campaign (print, media, promotional, and so on).

**What's your customer communication and support model?**

* [ ] Determine how you’ll manage incoming customer inquiries. Will you use a call center, web-based chat, conversational chatbots, or some combination of these?
* [ ] Determine how you’ll communicate to cardholders, such as sending statements and other required notifications.

# 2. Build a project team

Assemble a strong project team to coordinate the development and deployment of your card issuing program

<h2>Considerations</h2>

**Does your team have strong executive management support and the right personnel?**

* [ ] Verify that you have a senior management sponsor who strongly backs the effort. This advocacy is critical to success.
* [ ] Include representatives from many different functional areas, including program management, product, legal, compliance, process design, sales, marketing, and finance.
* [ ] Ideally, ensure these team members have expertise and experience in card issuing.

# 3. Ensure you meet all regulatory, compliance, and legal requirements

All countries have specific laws and regulations governing financial services, and there are global rules as well. You must ensure relevant authorities have approved you for card issuing where you plan to operate.

# 4. Define your card issuing strategy

Define a comprehensive strategy for your card issuing programs.

<h2>Considerations</h2>

**What types of cards will you offer?**

* [ ] Pismo offers [three program types](https://developers.pismo.io/pismo-docs/docs/program-types) for cards: debit, credit, and prepaid. Determine which ones you’ll offer.
* [ ] We offer [two card types](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#card-types): physical cards (plastic or metal) and virtual cards. Decide what you’ll offer.

**What card network will you use?**

* [ ] Pismo supports Visa and Mastercard worldwide, RuPay in India, and ELO for Brazilian-based clients (but with an international reach through association with Discover). Decide if you’ll use one or more network.

**What card network integration model will you use?**

* [ ] Pismo supports two [card network integration models](https://developers.pismo.io/pismo-docs/docs/card-network-integration): Full balance integration and Zero balance integration. With Full balance integration, we handle most of the processes. With Zero balance integration, you’re responsible for managing your customers’ balances and credit limits.

[Compare the models](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance)  to find the one that works best for you. The Pismo support team can help.

# 5. Create your governance model

Build an organizational framework and establish processes to support your card issuing program. Even if you already have card issuing programs, you should plan for how these new programs will impact your current organization and processes.

<h2>Considerations</h2>

**How will your organizational structure and processes support the new program?**

* [ ] Define program ownership and a reporting structure.
* [ ] Define new roles and a training plan for those who will support the program, including marketing, sales, legal, customer support, IT, and so on.
* [ ] Create or modify processes to manage the program.
* [ ] Create change management processes to introduce the new program.
* [ ] Ensure all compliance and regulatory requirements are built into the program.

**Does the program have an oversight function?**

* [ ] Set up a governance committee to oversee your card issuing program for the long term.
* [ ] Ensure that compliance and legal have a clear understanding of their responsibilities. Define communication channels between them and the governance committee.
<!-- source:end -->

### Source 2: `docs/card-issuing/step-2-establish-a-framework.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-2-establish-a-framework · updatedAt: 2026-06-28T23:10:44.000Z

<!-- source:begin path=docs/card-issuing/step-2-establish-a-framework.md part=0-end -->

# Step 2: Establish a framework

The Pismo support team works closely with you to establish a framework for your card issuing program. This framework consists of onboarding tasks and getting card network certification.

# Complete onboarding tasks

<Callout icon="📘" theme="info">
  If you’re already a Pismo customer, you’ve probably completed these onboarding steps. You can skip this step and go right to getting network certification.
</Callout>

As a new customer, you'll follow an onboarding process to create your organization, access required tools and systems, and configure authentication. For more information, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding) .

# Get card network certification

Work with your Pismo support team to get [card network certified](https://developers.pismo.io/pismo-docs/docs/network-certification). Network certification is the process of obtaining approval from a payment network, such as Visa or Mastercard, to issue credit or debit cards that can be used within their network. Though you are responsible for getting network certified, we’ll guide you through this process.

<Callout icon="🚧" theme="warn">
  Be aware that this process can take up to six months to complete—especially the first time. Strong project management and skilled card network engineers will help minimize this timeline.
</Callout>

<br />
<!-- source:end -->

### Source 3: `docs/card-issuing/step-3-create-your-programs.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-3-create-your-programs · updatedAt: 2026-09-01T18:06:39.000Z

<!-- source:begin path=docs/card-issuing/step-3-create-your-programs.md part=0-end -->

# Step 3: Create your programs

Now that you have a basic framework, you can create your card issuing program. You might want to create multiple programs. For example, to use both Visa and Mastercard as your card providers, create two programs, one for Visa and another for Mastercard. Or if you want to issue debit and credit cards, you’ll need to create two programs.

# Choose your program type

Pismo offers three [card issuing program types](https://developers.pismo.io/pismo-docs/docs/program-types):

* **Credit**—Customers borrow up to a credit limit, repay over time, and borrow again.
* **Debit** —Money is immediately withdrawn upon making a purchase.
* **Prepaid**—Funds are loaded in advance to pay for a specific service.

Within each of these programs, you must also choose your card network integration model. [Compare each model ](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance)and decide what works for you.

# Create a program

There are three methods available for creating your program. You can use Control Center or APIs with each method.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Method
      </th>

      <th>
        Explanation
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Use a template
      </td>

      <td>
        Choose a program from one of our templates, enter the basic details about your program, and submit. We then create the program, and you can customize it when you’re ready.

        This method is the default.

        * **Control Center**—[Create a program from a template](https://developers.pismo.io/pismo-docs/docs/add-a-program-from-a-template)
        * **APIs**—[Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate)
      </td>
    </tr>

    <tr>
      <td>
        Copy an existing program
      </td>

      <td>
        If you have existing programs, you can copy (or clone) a program and change some of the details. Be aware that you can’t change all the details.

        * **Control Center**—[Clone a program](https://developers.pismo.io/pismo-docs/docs/clone-a-program)
        * **APIs**—[Copy program](https://developers.pismo.io/pismo-docs/reference/copyprogram)
      </td>
    </tr>

    <tr>
      <td>
        Import a program
      </td>

      <td>
        You can use this method if you have programs in an existing test environment or another organization defined on the Pismo platform.

        * **Control Center**—[Export and import a program](https://developers.pismo.io/pismo-docs/docs/export-and-import-a-program)
        * **APIs:**\
          [Export program ](https://developers.pismo.io/pismo-docs/reference/postprogramexport)\
          [Download exported program](https://developers.pismo.io/pismo-docs/reference/getprogramexportdownload)\
          [Import program](https://developers.pismo.io/pismo-docs/reference/postprogramimport)
      </td>
    </tr>
  </tbody>
</Table>

# Define program features

Given the extensive range of features available, your Pismo support team works closely with you to identify the most suitable configurations for your card issuing program. Together, you define these features using both Control Center and APIs.

Though not a comprehensive list of features, here are some of the most important ones available.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Feature
      </th>

      <th>
        Capability
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Program parameters
      </td>

      <td>
        There are over 60 parameters to choose from. Define the required ones with your Pismo support team and consider using optional parameters to meet your business needs.

        [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table)
      </td>
    </tr>

    <tr>
      <td>
        Processing codes and transaction types
      </td>

      <td>
        Processing codes identify financial operations, such as purchases or withdrawals.

        Transaction types identify a transaction, such as a purchase, as either a credit or a debit operation and determine whether the transaction has a financial impact on the customer account.

        Transaction types are mapped to processing codes to create transaction flows. Work with your Pismo support team to build the flows that support your business needs.

        [Processing codes ](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types)\
        [Transaction types](https://developers.pismo.io/pismo-docs/docs/transactiontypes)
      </td>
    </tr>

    <tr>
      <td>
        Non-working days and administrative divisions
      </td>

      <td>
        The Pismo platform operates 24 x 7 x 365 and allows platform activities to occur at any time. But you might want to designate specific holidays or non-working days, which impact several areas (for example, statement due dates).

        Additionally, your business might operate in multiple locations (countries, states, or territories), with each using different calendars. You can define divisions to separate your organization into groups by geography. By using divisions, you can define specific schedules for selected locations.

        [Holidays and administrative divisions](https://developers.pismo.io/pismo-docs/docs/platform-setup-holidays)
      </td>
    </tr>

    <tr>
      <td>
        Statement cycle calendars
      </td>

      <td>
        Set the days of the month that statements are provided to account holders. **Note:** Statement cycle calendars only apply to credit programs.

        [Understanding statements](https://developers.pismo.io/pismo-docs/docs/understanding-statements)
      </td>
    </tr>

    <tr>
      <td>
        Flexible transaction controls (flex controls)
      </td>

      <td>
        Build rules that restrict your customers' financial operations, such as how much or where they can spend.

        You can use flex controls to set rules such as a minimum balance that the account must maintain, the maximum transaction amount a cardholder can make, and so on.

        [Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls)
      </td>
    </tr>

    <tr>
      <td>
        Fee models
      </td>

      <td>
        Define a collection of fees with custom calculations and when they should apply. For example, you can apply a percentage fee to cash advances.

        [Fee models](https://developers.pismo.io/pismo-docs/docs/fee-model#processing-codes)
      </td>
    </tr>

    <tr>
      <td>
        Accounting scripts
      </td>

      <td>
        Use accounting scripts to specify how the Pismo platform generates accounting entries for different types of financial operations. For example, use them to designate which debit or credit account money should flow into.

        [Accounting overview](https://developers.pismo.io/pismo-docs/docs/accounting-overview#accounting-script)
      </td>
    </tr>

    <tr>
      <td>
        Exchange rates
      </td>

      <td>
        Define the exchange rates to use for international transactions.

        [Exchange rates](https://developers.pismo.io/pismo-docs/docs/exchange-rate)
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

### Source 4: `docs/card-issuing/step-4-create-accounts-and-customers.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-4-create-accounts-and-customers · updatedAt: 2026-04-03T20:46:23.000Z

<!-- source:begin path=docs/card-issuing/step-4-create-accounts-and-customers.md part=0-end -->

# Step 4: Create accounts and customers

You've set up your card issuing programs, so now you're ready to create accounts and customers.

> 📘 Some technical context
>
> An account is the foundational object for all financial operations. It's what transactions, fees, payments, and so on are all attached to. The ledger is based on it.
>
> An account can have multiple customers, such as joint checking accounts and credit cards that share the account balance.

For an overview of accounts and customers, refer to [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview).

# Create an account

To create a new account, use the [Create account application endpoint](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications). Each account must have at least one customer, which can be a person or company. You must designate one customer as the owner of the account.

Once you’ve created your accounts, you can use [Control Center](https://developers.pismo.io/pismo-docs/docs/accounts-management-in-control-center) or APIs to manage them.

# Create additional customers

To add an additional customer to an account, use the [Create a new customer endpoint](https://developers.pismo.io/pismo-docs/reference/customerv2post).
<!-- source:end -->

### Source 5: `docs/card-issuing/step-5-create-cards.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-5-create-cards · updatedAt: 2026-04-03T20:46:23.000Z

<!-- source:begin path=docs/card-issuing/step-5-create-cards.md part=0-end -->

# Step 5: Create cards

At this point, you’re ready to create your cards. You’ll use [Pismo APIs](https://developers.pismo.io/pismo-docs/reference/post-v2-card)  and endpoints to create cards, with help from the Pismo support team.

Some of the key details you’ll define include:

* **Card data:** The data includes the card name, expiration date, CVV, and so on.
* **Card type:** You can issue physical cards (plastic or metal) or virtual cards.
* **Digital wallets:** Pismo provides its own digital wallet and supports those of other payment apps like Samsung Pay or Google Pay.
* **[Physical card embossing](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing):** If you issue physical cards, you must choose one or more embossing providers, define embossing rules, configure the providers, and create embossing schedules. Your Pismo support team will help you with this step.

For more information about creating cards, refer to [Cards management](https://developers.pismo.io/pismo-docs/docs/cards-overview-1).
<!-- source:end -->

### Source 6: `docs/card-issuing/step-5-test.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-5-test · updatedAt: 2026-04-29T12:33:59.000Z

<!-- source:begin path=docs/card-issuing/step-5-test.md part=0-end -->

# Step 6: Test the integrated setup

Your Pismo support team will work with you to test the integrated system to verify that it meets all security and functionality requirements. Together, we’ll build test plans and scripts, then execute them to ensure that you’ve tested transactions, card activations, and other key features.

# Oversee your program with data events and reports

During testing—and after—it’s important to see what’s happening with your data events. Pismo manages the data events that occur during normal card processing. These events include account actions, transactions, payments, auditing, and so on. You might know them as notifications or alerts.

Pismo can deliver this information to you in real-time events or via downloadable files. You use this data to monitor product usage, create metrics, send notifications, and generate business intelligence. You can also build your own dashboard to monitor these data events.

For more information, refer to [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

# Test Pismo API endpoints with Postman

Use the Pismo Postman collections and environment to test Pismo REST APIs. While you can test all these APIs through the Pismo Developers Portal, Postman helps you customize and streamline your testing environment. Pismo has a public workspace with shared collections and an environment on the Postman Public API network.

For more information, refer to [Test Pismo API endpoints with Postman](https://developers.pismo.io/pismo-docs/docs/testing-pismo-api-endpoints-with-postman).

<br />
<!-- source:end -->

### Source 7: `docs/card-issuing/step-6-monitor.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-6-monitor · updatedAt: 2026-04-03T20:46:23.000Z

<!-- source:begin path=docs/card-issuing/step-6-monitor.md part=0-end -->

# Step 7: Track performance and support users

After creating your card issuing program, you’ll continuously monitor its performance and value against your business objectives. We partner with you, helping you optimize processes, resolve issues, and introduce new products and features to your customers.

# Minimize fraud

Issuing cards carries potential fraud risks and liabilities. To mitigate these risks, Pismo offers anti-fraud services and can integrate with your existing systems.

For more information, refer to [Anti-fraud integration](https://developers.pismo.io/pismo-docs/docs/anti-fraud-integration).

# Manage cardholder disputes

A cardholder can open a dispute to report an unrecognized or suspicious transaction and request a cancellation or refund. Pismo helps you manage the entire disputes lifecycle.

For more information, refer to [Disputes overview](https://developers.pismo.io/pismo-docs/docs/disputes-overview).

# Administer statements

Statements provide detailed information about the balances resulting from credit card transactions. Pismo gives you the data for statements via APIs if you’re using Full balance integration. With Zero balance integration, you’re responsible for managing statements.

For more information, refer to [Understanding statements](https://developers.pismo.io/pismo-docs/docs/understanding-statements).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /programs/v1/programs/copy` | `CopyProgram` | Copy program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /programs/v1/programs/export` | `postProgramExport` | Export program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--export-and-import |
| `GET /programs/v1/programs/export/{id}/download` | `getProgramExportDownload` | Download exported program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--export-and-import |
| `POST /programs/v1/programs/import` | `postProgramImport` | Import program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--export-and-import |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /accounts/v2/customers` | `customerV2Post` | Create customer | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |
| `POST /wallet/v2/cards` | `post-v2-card` | Create card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |

### Operation essentials

- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /programs/v1/programs/copy`** (`CopyProgram`): security `S2SAuthentication`; required parameters none declared; required body fields `base_program_id`, `name`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0064`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /programs/v1/programs/export`** (`postProgramExport`): security `S2SAuthentication`; required parameters none declared; required body fields `program_id`; response statuses 201, 400; error codes in examples none; events none listed.
- **`GET /programs/v1/programs/export/{id}/download`** (`getProgramExportDownload`): security `S2SAuthentication`; required parameters `id` (path); required body fields none declared; response statuses 200, 400; error codes in examples none; events none listed.
- **`POST /programs/v1/programs/import`** (`postProgramImport`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `file`; response statuses 201, 400; error codes in examples none; events `programs-creation-1`.
- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /accounts/v2/customers`** (`customerV2Post`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `entity`, `customer`; response statuses 201, 400, 409, 500; error codes in examples none; events `account-account-owner-change-1`, `account-customer-creation-1`.
- **`POST /wallet/v2/cards`** (`post-v2-card`): security `BearerAuth`; required parameters `x-customer-id` (header); required body fields `name`, `type`; response statuses 200, 201, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `customerV2Post` | `account-account-owner-change-1` |
| `customerV2Post` | `account-customer-creation-1` |
| `post-v2-card` | `cards-create-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |
| `CopyProgram` | `programs-creation-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |
| `postProgramImport` | `programs-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/step-1-plan.md`: updatedAt 2026-04-27T17:55:17.000Z.
- `docs/card-issuing/step-2-establish-a-framework.md`: updatedAt 2026-06-28T23:10:44.000Z.
- `docs/card-issuing/step-3-create-your-programs.md`: updatedAt 2026-09-01T18:06:39.000Z.
- `docs/card-issuing/step-4-create-accounts-and-customers.md`: updatedAt 2026-04-03T20:46:23.000Z.
- `docs/card-issuing/step-5-create-cards.md`: updatedAt 2026-04-03T20:46:23.000Z.
- `docs/card-issuing/step-5-test.md`: updatedAt 2026-04-29T12:33:59.000Z.
- `docs/card-issuing/step-6-monitor.md`: updatedAt 2026-04-03T20:46:23.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/step-1-plan.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-1-plan | `4215b62a0e30996c…` | 2026-04-27T17:55:17.000Z |
| `docs/card-issuing/step-2-establish-a-framework.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-2-establish-a-framework | `b131d6a1b1ef7f28…` | 2026-06-28T23:10:44.000Z |
| `docs/card-issuing/step-3-create-your-programs.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-3-create-your-programs | `804b5a0f4473f932…` | 2026-09-01T18:06:39.000Z |
| `docs/card-issuing/step-4-create-accounts-and-customers.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-4-create-accounts-and-customers | `7a18491202524295…` | 2026-04-03T20:46:23.000Z |
| `docs/card-issuing/step-5-create-cards.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-5-create-cards | `dde2c446bd053710…` | 2026-04-03T20:46:23.000Z |
| `docs/card-issuing/step-5-test.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-5-test | `d7350f565083e1a9…` | 2026-04-29T12:33:59.000Z |
| `docs/card-issuing/step-6-monitor.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-6-monitor | `f0561b41b6c078ec…` | 2026-04-03T20:46:23.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--customers` — API reference: Core platform - Accounts — Customers
- `KU-API-platform-setup-programs--export-and-import` — API reference: Platform setup - Programs — Export and import
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-CARD-anti-fraud-integration` — Anti-fraud integration
- `KU-CARD-card-network-integration` — Card network integration and certification
- `KU-CARD-cards-overview-1` — Cards management
- `KU-CARD-disputes-overview` — Disputes overview
- `KU-CARD-full-balance-versus-zero-balance` — Full balance versus Zero balance integration
- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-CC-accounts` — Control Center accounts: overview, management, actions and configurations
- `KU-CC-programs` — Control Center programs: create, edit, clone, export and import
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
- `KU-CORE-accounts-overview` — Accounts
- `KU-CORE-exchange-rate` — Exchange rates
- `KU-CORE-flex-controls` — Flexible transaction controls: concepts, examples and simulation
- `KU-CORE-platform-setup-holidays` — Platform setup - Holidays and administrative divisions
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-CORE-transactiontypes` — Transaction types
- `KU-CRED-understanding-statements` — Understanding statements
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-pismo-platform-onboarding` — Onboarding for new customers
- `KU-GS-program-types` — Program types
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
