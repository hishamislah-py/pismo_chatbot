---
ku_id: KU-CARD-card-issuing-basics
title: Card issuing reference
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/card-issuing-basics.md
  sha256: cf3906cc470a5c8a0d2936f8016b2c76b998bb8706b48b6d1cfb603f636e8df2
  url: https://developers.pismo.io/pismo-docs/docs/card-issuing-basics
  role: primary_guide
  updated_at: '2026-03-18T15:19:52.000Z'
operations:
- patch-accounts-v2-accounts-accountId-status
- post-acquisitions-v3-s2s-applications
- post-v1-networkauthorization-disputes
related_kus:
- KU-API-card-issuing-disputes--disputes-part-01
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-CARD-card-network-integration
- KU-CARD-cards-overview-1
- KU-CARD-disputes-overview
- KU-CORE-flex-controls
- KU-CRED-understanding-statements
- KU-EVT-catalogue-account
- KU-EVT-catalogue-disputes
- KU-EVT-catalogue-other-domains
- KU-GS-setup-overview
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Card issuing reference

**KU ID:** `KU-CARD-card-issuing-basics` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/card-issuing-basics.md`:

> The following are essential concepts and terms for card issuing.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/card-issuing-basics.md`: Card issuing reference; Roles; Account management; Card network certification and integration; Card management; Reconciliations; Statements; Dispute management; Data and reporting

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/card-issuing-basics.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/card-issuing-basics · updatedAt: 2026-03-18T15:19:52.000Z

<!-- source:begin path=docs/card-issuing/card-issuing-basics.md part=0-end -->

# Card issuing reference

The following are essential concepts and terms for card issuing.

## Roles

The following table describes the key participants in the card payment ecosystem and their respective roles in processing transactions.

| Participant            | Role                                                                                                                                                                                                                                                                                                              |
| :--------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cardholder             | Person authorized to use a card.                                                                                                                                                                                                                                                                                  |
| Merchant               | Store or vendor authorized to receive card payments from its customers pursuant to an agreement with card brands.                                                                                                                                                                                                 |
| Network                | Company that processes card payments worldwide such as Visa and Mastercard. Networks are also called *card schemes*.                                                                                                                                                                                              |
| Issuer                 | Financial institution that issued the card used in a transaction. Issuers are usually banks, but they can be other types of financial entities, such as fintechs.                                                                                                                                                 |
| Acquirer               | Financial institution that receives the payment authorization request from the merchant. Acquirers are usually banks, but they can be other types of financial entities, such as fintechs. For simplicity, the acquirer is sometimes referred to as the *merchant's bank*, although it doesn't have to be a bank. |
| Third party processors | Companies that help banks and other organizations to set themselves up as card issuers. They often handle much of the processing that would otherwise fall on the shoulders of their clients. Pismo falls into this category.                                                                                     |

Different financial institutions offer different sets of services. A financial institution can be both an issuer and an acquirer, but that's not always the case. For example, most banks need to handle credit card transactions, but many do not issue credit cards.

## Account management

The following table outlines key topics and responsibilities involved in account management, including regulatory compliance, onboarding, credit evaluation, and security protocols.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Topic
      </th>

      <th>
        Description
      </th>

      <th>
        Responsibilities
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        KYC, AML, CFT, KYB
      </td>

      <td>
        * \*Know Your Customer (KYC)**is a set of mandatory regulations for customer identity verification. Its purpose is fraud prevention,**anti-money laundering (AML)**, and**combating the financing of terrorism (CFT)\*\*. KYC regulations require you to verify that a customer is who they say they are. Customers should provide proof of their identity and address. This can be done through ID card verification, biometric verification, and/or document verification.

        KYC has three components:

        1. **Customer Identification Program (CIP)** – You must verify that a customer is who they say they are. You do this by requiring them to provide information that verifies their identity.
        2. **Customer Due Diligence (CDD)** – Conducting detailed risk assessments.
        3. **Continuous monitoring** – You must closely monitor transactions for patterns of suspicious activity and report any that you find. Similar to KYC, **Know Your Business (KYB)** is a set of regulations for verifying the identity of the businesses you deal with. You must conduct due diligence to ensure that a company is legitimate and is not just a shell company. This includes identifying the ultimate company owner and major shareholders.
      </td>

      <td>
        You are responsible for following KYC and KYB rules and regulations.
      </td>
    </tr>

    <tr>
      <td>
        Onboarding
      </td>

      <td>
        * \*Onboarding\*\* refers to creating customer accounts.
      </td>

      <td>
        The [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoint enables new customer onboarding.
      </td>
    </tr>

    <tr>
      <td>
        Credit engine (credit cards only)
      </td>

      <td>
        A **credit engine** (or credit decision engine) is a software platform that makes credit decisions based on the policies and rules you set up.
      </td>

      <td>
        If you plan to issue credit cards, you must provide your own method for making credit decisions.
      </td>
    </tr>

    <tr>
      <td>
        Credit score, behavior score (credit cards only)
      </td>

      <td>
        You can assess a potential customer's credit risk by reviewing their **credit score**.

        Some issuers also set up an internal, proprietary scoring system to produce **behavior scores** for their existing customers. To do this, they mine a customer's payment history, their credit utilization over time, and sometimes even the amounts and types of products they purchase.
      </td>

      <td>
        If you plan to issue credit cards, you need to purchase a credit score for each potential customer from a credit bureau.

        In addition to this, you can set up your own additional proprietary scoring system to produce a behavior score for each customer.
      </td>
    </tr>

    <tr>
      <td>
        Account lifecycle
      </td>

      <td>
        The **account lifecycle** refers to the different statuses an account can go through after creation.
      </td>

      <td>
        Use the [Update an account’s status](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v2-accounts-accountid-status) endpoint to update any account's status.
      </td>
    </tr>

    <tr>
      <td>
        Web security
      </td>

      <td>
        A vital part of security is ensuring that the data you transmit over the web is encrypted and stored securely. The Pismo platform operates on **Amazon Web Services (AWS)**. All data storage, whether relational, non-relational, or files, are encrypted using the **AWS Key Management Service (AWS KMS)**.
      </td>

      <td />
    </tr>

    <tr>
      <td>
        3DS, ACS
      </td>

      <td>
        * \*3D Secure (3DS)\*\* is a protocol that adds an additional layer of security for online credit and debit card transactions. The name refers to the three domains that are involved in transactions:
        * \*Acquirer domain\*\*–The financial institution that accepts the card payments (the merchant's bank).
        * \*Issuer domain\*\*–The organization that issued the card used in the transaction.
        * \*Interoperability domai&#x6E;**–The payment systems that connect the acquirer and issuer domains. A 3DS implementation usually uses an**Access Control System (ACS)\*\* to authorize transactions. ACS is a security system that uses a wide array of details to manage the authentication process. Only cardholders who can submit legitimate credentials are allowed to complete transactions. Visa and Mastercard offer 3DS card brands called Visa Consumer Authentication Service (VCAS) and SecureCode, respectively.
      </td>

      <td>
        3DS and ACS are mandatory in some countries, such as India. In other countries they are not mandatory, but most Pismo customers choose to implement them anyway.
      </td>
    </tr>
  </tbody>
</Table>

## Card network certification and integration

The following table provides an overview of key processes related to card network certification and integration, including issuer responsibilities and available implementation models.

| Topic                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Card network certification | Network certification for a card issuer refers to the process of obtaining approval from a payment network, such as Visa or Mastercard, to issue credit or debit cards that can be used within their network. Though you are responsible for getting network certified, a Pismo representative will help guide you through the process. Refer to [Card network certification](https://developers.pismo.io/pismo-docs/docs/network-certification)  for more information. |
| Card network integration   | The Pismo platform offers card issuers two card network integration models they can implement - full and zero balance. Refer to [Card network integration](https://developers.pismo.io/pismo-docs/docs/card-network-integration) for more information.                                                                                                                                                                                                                  |

## Card management

The following table outlines key components of transaction processing and account management on the Pismo platform, including message handling, validations, ledger tracking, and fraud prevention tools.

| Topic             | Description                                                                                                                                                                                                                                   |
| :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Message parsing   | Card networks send two types of authorization messages, created by two types of messaging systems: a **single-message system (SMS)** and a **dual-message system (DMS)**. The clearing/base II reconciliation process handles these messages. |
| Validations       | A credit card is valid if the account that it's associated with is active. An account is active if its status is NORMAL.                                                                                                                      |
| Ledger            | The Pismo platform uses [accounts](https://developers.pismo.io/pismo-docs/docs/setup-overview#account) to keep track of money flowing into and out of a company's general ledger.                                                                                                     |
| Anti-fraud        | The Pismo platform integrates with your anti-fraud system.                                                                                                                                                                                    |
| Spending controls | The Pismo platform provides [flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls) that enable you to restrict a customer's financial operations. For example, you can set a maximum amount allowed for a certain transaction type.               |

Refer to [Cards management](https://developers.pismo.io/pismo-docs/docs/cards-overview-1) for more information.

## Reconciliations

The following table summarizes key financial operations on the Pismo platform, including fund transfers, balance adjustments, and accounting-related events.

| Topic                    | Description                                                                                                                                                                                                                 |
| :----------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clearing parsing         | The correct and timely transfer of funds from a customer's account to the merchant's account.                                                                                                                               |
| Adjustments (edge cases) | It's sometimes necessary to add or remove money from a customer's account in order to reconcile balance inconsistencies (to credit an account when a transaction fails to be delivered or to return money to the customer). |
| Accounting events        | Events on the Pismo platform that impact a company's records.                                                                                                                                                               |

## Statements

The following table outlines key credit card operations managed on the Pismo platform, including transaction creation, billing cycles, refinancing options, and payment handling.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Topic
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Transaction creation
      </td>

      <td>
        A **transaction** is a record of a purchase, transfer, payment, or manual adjustment. In most cases, the creation of a transaction is triggered by a cleared authorization.
      </td>
    </tr>

    <tr>
      <td>
        Statement lifecycle
      </td>

      <td>
        Credit card balances and interest accruals are managed in **cycles** (billing periods). A statement corresponds to a single cycle. The first cycle begins the moment the card is activated. After that, the first full day of each cycle follows the closing date of the previous cycle. On the last day of a cycle, the cycle is closed, and a grace period begins. This grace period belongs to the next cycle. When the grace period ends, if the card balance has not been paid off, charges begin to accrue.
      </td>
    </tr>

    <tr>
      <td>
        Refinancing
      </td>

      <td>
        You must have processes in place that allow cardholders to refinance their credit card debt. To that end, your program must make the following options available:

        * \*Installment advances\*\*–Used to settle future debt on the current cycle, rather than on a future cycle.
        * \*Installment agreement\*\*–Used to refinance an existing credit card debt.
        * \*Statement agreement\*\*–A contract that renegotiates all debt – past, present, and future.
      </td>
    </tr>

    <tr>
      <td>
        Payments
      </td>

      <td>
        A customer's credit card debt must be adjusted whenever they make a payment.
      </td>
    </tr>
  </tbody>
</Table>

Refer to [Understanding statements](https://developers.pismo.io/pismo-docs/docs/understanding-statements) for more information.

## Dispute management

The following table outlines the chargeback process, including how chargebacks are created and the stages they go through after initiation.

| Topic                | Description                                                                                           | Responsibilities                                                                                                                                   |
| :------------------- | :---------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chargeback creation  | A chargeback is initiated with the card network.                                                      | You can use the Pismo API's [Create dispute](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes)  endpoint to create a chargeback dispute with the network. |
| Chargeback lifecycle | The chargeback lifecycle refers to the different statuses a chargeback can go through after creation. |                                                                                                                                                    |

Refer to the [Disputes overview](https://developers.pismo.io/pismo-docs/docs/disputes-overview)  for more information.

## Data and reporting

The following table highlights how the Pismo platform supports data delivery through real-time streaming and downloadable reports.

| Topic     | Description                                                                                                   |
| :-------- | :------------------------------------------------------------------------------------------------------------ |
| Streaming | Pismo APIs can stream event notifications and data to your cloud storage in real-time.                        |
| Reports   | Event notifications and other data can be stored in files as reports and sent to cloud storage or downloaded. |

Refer to the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview) for more information.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `PATCH /accounts/v2/accounts/{accountId}/status` | `patch-accounts-v2-accounts-accountId-status` | Update status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `POST /v1/networkauthorization-disputes` | `post-v1-networkauthorization-disputes` | Create dispute | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01 |

### Operation essentials

- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`PATCH /accounts/v2/accounts/{accountId}/status`** (`patch-accounts-v2-accounts-accountId-status`): security `BearerAuth`; required parameters `accountId` (path); required body fields `status`; response statuses 204, 400, 404, 500; error codes in examples none; events `account-status-change-2`.
- **`POST /v1/networkauthorization-disputes`** (`post-v1-networkauthorization-disputes`): security `BearerAuth`; required parameters `Authorization` (header); required body fields `modality`, `disputed_amount`, `is_partial`, `network_brand_type`; response statuses 200, 400, 401, 422, 500; error codes in examples none; events `disputes-dispute-installment-creation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-accounts-v2-accounts-accountId-status` | `account-status-change-2` |
| `post-v1-networkauthorization-disputes` | `disputes-dispute-installment-creation-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/card-issuing-basics.md`: updatedAt 2026-03-18T15:19:52.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/card-issuing-basics.md` | whole document | https://developers.pismo.io/pismo-docs/docs/card-issuing-basics | `cf3906cc470a5c8a…` | 2026-03-18T15:19:52.000Z |

## Related knowledge units

- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-CARD-card-network-integration` — Card network integration and certification
- `KU-CARD-cards-overview-1` — Cards management
- `KU-CARD-disputes-overview` — Disputes overview
- `KU-CORE-flex-controls` — Flexible transaction controls: concepts, examples and simulation
- `KU-CRED-understanding-statements` — Understanding statements
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-disputes` — Event catalogue: disputes
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-setup-overview` — Core objects
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
