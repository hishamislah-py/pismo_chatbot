---
ku_id: KU-BANK-transaction-banking-accounts
title: Transaction banking and transaction banking accounts
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/corporate-banking-overview.md
  sha256: b2aa7de0b7798ad8929340921131065c89879afd647d79b47c6b29f7aebcf153
  url: https://developers.pismo.io/pismo-docs/docs/corporate-banking-overview
  role: primary_guide
  updated_at: '2026-04-30T15:01:13.000Z'
- path: docs/core-banking/corporate-accounts.md
  sha256: 8b9d8798890e2c89f5ecf801f32dade2e68efbf17d6630ea699edeff340918fe
  url: https://developers.pismo.io/pismo-docs/docs/corporate-accounts
  role: primary_guide
  updated_at: '2026-08-03T16:08:09.000Z'
operations:
- patch-corporate-v2-earmarks-earmarkid
- patch-division-v2
- post-account
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-division-v2
- post-hierarchies
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--hierarchies
- KU-BANK-divisions-and-hierarchies
- KU-BANK-earmarks
- KU-BANK-get-started-demand-deposit-accounts
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-GS-platform-overview-and-solutions
grouping_rationale: Overview and its account page.
---

# Transaction banking and transaction banking accounts

**KU ID:** `KU-BANK-transaction-banking-accounts` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Overview and its account page.

Scope as stated in `docs/core-banking/corporate-banking-overview.md`:

> Transaction banking focuses on transactions between a bank and a large organization, such as a multinational corporation, lending for short-term expenses and long-term investments. Pismo’s transaction banking solution enables you to tailor lending and practices specifically to your organizational structure. These services include detailed, custom hierarchies and divisional structures, accounts with features that reflect your needs, and earmarking of funds for a variety of options.

Scope as stated in `docs/core-banking/corporate-accounts.md`:

> The Pismo platform allows you to define relationships between you and your clients and manage account details differently based on those relationships. The platform provides an API that enables you to create, define, and manage client accounts and relationships based on specific requirements.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/corporate-banking-overview.md`: Transaction banking; Prerequisites; Hierarchies and divisions; Accounts; Earmarks
- `docs/core-banking/corporate-accounts.md`: Transaction banking accounts; Transaction banking account for clients using different currencies; Transaction banking account and its dependents; Granular account details

## Prerequisites and dependencies

- Prerequisites are described in `docs/core-banking/corporate-banking-overview.md` section "Prerequisites".
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/corporate-banking-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/corporate-banking-overview · updatedAt: 2026-04-30T15:01:13.000Z

<!-- source:begin path=docs/core-banking/corporate-banking-overview.md part=0-end -->

# Transaction banking

Transaction banking focuses on transactions between a bank and a large organization, such as a multinational corporation, lending for short-term expenses and long-term investments. Pismo’s transaction banking solution enables you to tailor lending and practices specifically to your organizational structure. These services include detailed, custom hierarchies and divisional structures, accounts with features that reflect your needs, and earmarking of funds for a variety of options.

# Prerequisites

The Pismo transaction banking API extends the Pismo platform core APIs. For more information, see [Main solutions](https://developers.pismo.io/pismo-docs/docs/main-solutions).

Teams experienced with the Pismo platform can skip directly to the [Corporate banking launch reference](https://developers.pismo.io/pismo-docs/docs/corporate-banking-launch-reference).

<Callout icon="📘" theme="info">
  **Note**

  Pismo is a technology company that provides services for banking operations. When you use Pismo technology, you must have applicable licenses and comply with regulations with the countries/regions in which you operate.
</Callout>

# Hierarchies and divisions

Many major organizations structure geographically, with corporate headquarters, country satellite offices, regional offices, and so on. The [Create hierarchy levels](https://developers.pismo.io/pismo-docs/reference/post-hierarchies) endpoint enables extensive customization that matches your organization. A hierarchy represents one or more levels of your organization. On the Pismo platform, your corporate hierarchy is represented as an array, with each member of the array representing a single level.

Corporations also differentiate with various departments, divisions, and so on. The [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) endpoint enables fine control over your setup, to match your organization precisely. Each division is associated with a specific hierarchy and level. For more information, refer to [Hierarchies](https://developers.pismo.io/pismo-docs/docs/hierarchies-2).

# Accounts

The various corporate account endpoints provide the tools to map corporate interactions. The [Create corporate accounts](https://developers.pismo.io/pismo-docs/reference/post-account) endpoint, for example, enables you to make precise delineations among your internal accounts and customer accounts. You can create and associate an account based on location (e.g., hierarchy), division, program, applicant (e.g., government document number, applicant name, and so on). For more information, refer to [Corporate accounts](https://developers.pismo.io/pismo-docs/docs/corporate-accounts).

# Earmarks

Earmarks enable your organization to balance transactions at a granular level to match organizational needs in a nimble fashion. The [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint, for example, set aside funds in reserve for transactional needs. This helps ensure the availability of sufficient funds for a cash-out operation directly from the earmarked balance (using a unique “earmark ID” of a specific earmark). You can set specific times and dates for funds to return to the account balance automatically. Additionally, they can hold funds for indefinite periods to draw upon as needed.

The [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid) endpoint enables you to increase or decrease the amount of an earmark. You can use the endpoint to change the scheduled release date and time as well. Finally, the [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel) endpoint enables you to cancel an earmark, releasing held funds and invalidating the release schedule.

For more information, see [Earmarks](https://developers.pismo.io/pismo-docs/docs/earmarks).
<!-- source:end -->

### Source 2: `docs/core-banking/corporate-accounts.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/corporate-accounts · updatedAt: 2026-08-03T16:08:09.000Z

<!-- source:begin path=docs/core-banking/corporate-accounts.md part=0-end -->

# Transaction banking accounts

The Pismo platform allows you to define relationships between you and your clients and manage account details differently based on those relationships. The platform provides an API that enables you to create, define, and manage client accounts and relationships based on specific requirements.

The following examples describe some common transaction banking scenarios where you can configure transaction accounts and divisions using the Pismo platform.

# Transaction banking account for clients using different currencies

For example, you might want to create an account for a company in Berlin that deals primarily in euros and interacts with customers in Croatia and Serbia. In this case, you use the [Create accounts](https://developers.pismo.io/pismo-docs/reference/post-account) endpoint to create accounts in those countries that transact in euros.

<Image align="center" alt="Account created for customers in the Euro zone" caption="Figure1: Transaction account (Berlin 1) created for customers using euros" src="https://files.readme.io/fb4fa76-Corporate_Accounts_1.png" />

Similarly, you can create an account for a different Berlin-based company that interacts with North and South American firms, interchanging funds based on U.S. dollars.

<Image align="center" alt="Account created for Central and South American customers ealing in US dollars" caption="Figure 2: Transaction account (Berlin 2) created for customers dealing in US dollars" src="https://files.readme.io/41ac9e2-Corporate_Accounts_2.png" />

# Transaction banking account and its dependents

You might want to create child accounts in smaller geographic locations, such as cities, to better serve clients there. Using the example from *Figure 2*, you can create child accounts for clients based on the city they reside (see *Figure 3*). Although an account can have multiple children, it can only have one parent. A group of one parent and all its child accounts is called an **account family**.

If you don't configure details for child accounts, such as timezone and program binding, the child accounts you create for those divisions automatically inherit all details from the parent.

<Image align="center" alt="Parent company " caption="Figure 3: Account family" src="https://files.readme.io/d3beec9-Corporate_Accounts_3.png" />

# Granular account details

Depending on local regulations and business rules, a customer might need to store account information beyond the basic customer document number, name, phone, and address. For transaction banking applications, this information might include details such as the account manager's name, internal credit rating, relationship length, and so on. For this, use the custom fields available in the [Create corporate account](https://developers.pismo.io/pismo-docs/reference/post-account) endpoint, inside the applicant object.

<Image align="center" alt="Define fine-grained details using custom fields" caption="Figure 4: Configure granular account details" src="https://files.readme.io/d2418a5-Corporate_Accounts_4.png" />

If any specific validations need to be performed on those custom fields, you can do so by attaching a JSON schema to the division through the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint.

For more information, refer to [Corporate banking API Reference documentation](https://developers.pismo.io/pismo-docs/reference/post-account).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /corporate/v1/hierarchies` | `post-hierarchies` | Create hierarchy | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--hierarchies |
| `POST /corporate/v2/divisions` | `post-division-v2` | Create division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `POST /corporate/v1/corporate-accounts` | `post-account` | Create transaction banking account | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /corporate/v2/earmarks` | `post-corporate-v2-earmarks` | Create earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/earmarks/{earmarkId}` | `patch-corporate-v2-earmarks-earmarkid` | Update earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` | `post-corporate-v2-earmarks-earmarkid-cancel` | Cancel earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/divisions/{divisionCode}` | `patch-division-v2` | Update division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |

### Operation essentials

- **`POST /corporate/v1/hierarchies`** (`post-hierarchies`): security `BearerAuth`; required parameters none declared; required body fields `name`, `levels`; response statuses 201, 400, 401, 403, 500; error codes in examples `WHIE0001`, `WHIE0002`, `WHIE0003`, `WHIE0004`, `WHIE0005`, `WHIE0007`, `ECMN9999`; events `corporate-hierarchy-creation-1`.
- **`POST /corporate/v2/divisions`** (`post-division-v2`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `hierarchy_id`, `level_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WDIV0015`, `WDIV0011`, `WDIV0005`, `WDIV0007`, `WDIV0006`, `WDIV0012`, `WDIV0018`, `WDIV0019`, `WDIV0017`, `WDIV0016`, `ECMN9999`; events `corporate-division-creation-2`.
- **`POST /corporate/v1/corporate-accounts`** (`post-account`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `program_id`, `applicant`, `external_account_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WCAC0013`, `WCAC0005`, `WCAC0006`, `WCAC0004`, `WCAC0016`, `WCAC0009`, `WDIV0002`, `WCAC0011`, `WCAC0014`, `ECMN9999`; events `corporate-corporate-account-creation-1`, `onboarding-succeeded-1`.
- **`POST /corporate/v2/earmarks`** (`post-corporate-v2-earmarks`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `internal_operation`; response statuses 201, 400, 401, 403, 409, 423, 500; error codes in examples `WOBK0007`, `WEAM0014`, `WEAM0015`, `WEAM0005`, `WEAM0006`, `WEAM0017`, `WEAM0019`, `WEAM0026`, `WEAM0036`, `WEAM0037`, `WEAM0039`, `WEAM0040`, `WEAM0047`, `WEAM0042`, `WEAM0043`, `WEAM0044`, `WEAM0045`, `WEAM0046`, `WEAM0016`, `WEAM0018`, `WEAM0009`, `WEAM0020`, `WEAM0023`, `WEAM0024`, `WEAM0001`, `WEAM0025`, `WEAM0034`, `WEAM0033`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-earmark-1`, `platform-authorization-platform-authorization-1`, `transaction-creation-1`.
- **`PATCH /corporate/v2/earmarks/{earmarkId}`** (`patch-corporate-v2-earmarks-earmarkid`): security `BearerAuth`; required parameters `earmarkId` (path); required body fields `internal_operation`; response statuses 200, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WEAM0014`, `WEAM0015`, `WEAM0016`, `WEAM0017`, `WEAM0018`, `WEAM0019`, `WEAM0026`, `WEAM0027`, `WEAM0030`, `WEAM0031`, `WEAM0036`, `WEAM0038`, `WEAM0039`, `WEAM0040`, `WEAM0047`, `WEAM0041`, `WEAM0042`, `WEAM0043`, `WEAM0044`, `WEAM0045`, `WEAM0046`, `WEAM0023`, `WEAM0024`, `WEAM0025`, `WEAM0034`, `WEAM0049`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-earmark-1`, `platform-authorization-platform-authorization-1`, `transaction-creation-1`.
- **`POST /corporate/v2/earmarks/{earmarkId}/cancel`** (`post-corporate-v2-earmarks-earmarkid-cancel`): security `BearerAuth`; required parameters `earmarkId` (path); required body fields `internal_operation`; response statuses 200, 400, 401, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WEAM0014`, `WEAM0015`, `WEAM0008`, `WEAM0017`, `WEAM0018`, `WEAM0019`, `WEAM0022`, `WCAC0012`, `WEAM0036`, `WEAM0039`, `WEAM0040`, `WEAM0047`, `WEAM0041`, `WEAM0042`, `WEAM0043`, `WEAM0044`, `WEAM0045`, `WEAM0046`, `WEAM0024`, `WEAM0007`, `WEAM0025`, `WEAM0034`, `WEAM0049`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-earmark-1`, `platform-authorization-platform-authorization-1`, `transaction-creation-1`.
- **`PATCH /corporate/v2/divisions/{divisionCode}`** (`patch-division-v2`): security `BearerAuth`; required parameters `divisionCode` (path); required body fields none declared; response statuses 204, 400, 401, 403, 404, 500; error codes in examples `WDIV0015`, `WDIV0011`, `WDIV0005`, `WDIV0007`, `WDIV0006`, `WDIV0008`, `WDIV0009`, `WDIV0010`, `WDIV0012`, `WDIV0018`, `WDIV0019`, `WDIV0002`, `WDIV0017`, `ECMN9999`; events `corporate-division-change-2`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-corporate-v2-earmarks-earmarkid` | `account-balances-balance-change-1` |
| `post-corporate-v2-earmarks` | `account-balances-balance-change-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `account-balances-balance-change-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `availables-change-available-1` |
| `post-corporate-v2-earmarks` | `availables-change-available-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `availables-change-available-1` |
| `post-account` | `corporate-corporate-account-creation-1` |
| `patch-division-v2` | `corporate-division-change-2` |
| `post-division-v2` | `corporate-division-creation-2` |
| `patch-corporate-v2-earmarks-earmarkid` | `corporate-earmark-1` |
| `post-corporate-v2-earmarks` | `corporate-earmark-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `corporate-earmark-1` |
| `post-hierarchies` | `corporate-hierarchy-creation-1` |
| `post-account` | `onboarding-succeeded-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v2-earmarks` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `platform-authorization-platform-authorization-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `transaction-creation-1` |
| `post-corporate-v2-earmarks` | `transaction-creation-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `transaction-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/corporate-banking-overview.md`: updatedAt 2026-04-30T15:01:13.000Z.
- `docs/core-banking/corporate-accounts.md`: updatedAt 2026-08-03T16:08:09.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/corporate-banking-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/corporate-banking-overview | `b2aa7de0b7798ad8…` | 2026-04-30T15:01:13.000Z |
| `docs/core-banking/corporate-accounts.md` | whole document | https://developers.pismo.io/pismo-docs/docs/corporate-accounts | `8b9d8798890e2c89…` | 2026-08-03T16:08:09.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--hierarchies` — API reference: Banking - Transaction banking — Hierarchies
- `KU-BANK-divisions-and-hierarchies` — Divisions and hierarchies
- `KU-BANK-earmarks` — Earmarks
- `KU-BANK-get-started-demand-deposit-accounts` — Get started with demand deposit accounts (DDAs)
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-GS-platform-overview-and-solutions` — Pismo platform overview, main solutions and where to start
