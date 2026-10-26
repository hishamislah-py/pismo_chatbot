---
ku_id: KU-BANK-get-started-core-banking
title: Get started with core banking
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/get-started-with-core-banking.md
  sha256: 4f5c1af26df140e38487d285f30639c85113924c011580ded5c87a392881dca2
  url: https://developers.pismo.io/pismo-docs/docs/get-started-with-core-banking
  role: primary_guide
  updated_at: '2026-06-10T18:18:56.000Z'
- path: docs/get-started/get-started-building-core-banking.md
  sha256: 4b3b581152c24b11bc31f01bc78a90ba28483d557bfed5b13ca8550d2b0dd63e
  url: https://developers.pismo.io/pismo-docs/docs/get-started-building-core-banking
  role: primary_guide
  updated_at: '2026-06-29T19:37:33.000Z'
operations:
- CreateProgramBasedOnTemplate
- post-acquisitions-v3-s2s-applications
- post-credentials
- post-save-provider-configuration
related_kus:
- KU-API-banking-authentication--provider-credentials
- KU-API-banking-ted-configuration--configurations
- KU-API-core-platform-accounts--accounts
- KU-API-platform-setup-programs--programs-part-01
- KU-BANK-banking-overview
- KU-EVT-catalogue-other-domains
- KU-GS-pismo-platform-onboarding
grouping_rationale: Identical bodies (duplicate pages).
---

# Get started with core banking

**KU ID:** `KU-BANK-get-started-core-banking` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Identical bodies (duplicate pages).

Scope as stated in `docs/core-banking/get-started-with-core-banking.md`:

> Core banking refers to the essential systems and processes that financial institutions use to manage customer accounts and transactions. These systems handle day-to-day operations such as deposits, withdrawals, payments, loans, and account maintenance. Core banking platforms ensure that banking services are available to customers in real-time across branches and digital channels.

Scope as stated in `docs/get-started/get-started-building-core-banking.md`:

> Core banking refers to the essential systems and processes that financial institutions use to manage customer accounts and transactions. These systems handle day-to-day operations such as deposits, withdrawals, payments, loans, and account maintenance. Core banking platforms ensure that banking services are available to customers in real-time across branches and digital channels.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/get-started-with-core-banking.md`: Get started with core banking; Step 1: Create your organization (tenant); Step 2: Create token; Step 3: Create programs; Step 4: Create an account; Step 5: Provide credentials (when needed); Endpoints usage
- `docs/get-started/get-started-building-core-banking.md`: Get started with core banking; Step 1: Create your organization (tenant); Step 2: Create token; Step 3: Create programs; Step 4: Create an account; Step 5: Provide credentials (when needed); Endpoints usage

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/get-started-with-core-banking.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-with-core-banking · updatedAt: 2026-06-10T18:18:56.000Z

<!-- source:begin path=docs/core-banking/get-started-with-core-banking.md part=0-end -->

# Get started with core banking

Core banking refers to the essential systems and processes that financial institutions use to manage customer accounts and transactions. These systems handle day-to-day operations such as deposits, withdrawals, payments, loans, and account maintenance. Core banking platforms ensure that banking services are available to customers in real-time across branches and digital channels.

On the Pismo platform, you access core banking functionality through APIs that support account creation, transaction processing, ledger management, and more. You can use the Pismo platform to build a suite of products—from deposits and savings to loans and overdrafts. Refer to [Banking overview](https://developers.pismo.io/pismo-docs/docs/banking-overview) for more information.

Banking with Pismo offers:

* Complete banking functionality:
  * Ledgers
  * Savings accounts
  * Current accounts
  * Deposits and overdrafts
  * Spending limits and controls at the account level
* Integrations with credit card networks, anti-fraud services, card embossers, and other third-party providers

This guide outlines the essential steps for setting up a new banking customer on the Pismo platform. Using a fictional banking scenario, it presents a series of steps that illustrate the configuration workflow.

<Callout icon="📘" theme="info">
  **Note**

  Before you make API requests to the Pismo platform, make sure you’ve installed Postman and have configured all required certificates and keys. For more information, refer to [Test Pismo API Endpoints with Postman](https://developers.pismo.io/pismo-docs/docs/testing-pismo-api-endpoints-with-postman).
</Callout>

Getting started with core banking involves these steps.

![Illustration of a step by step list to get started with core banking](https://files.readme.io/3ea9d3e22e7b928a8319c78aa90972829797fc9e9e66330b3693080107d3e4d7-image.png)

# Step 1: Create your organization (tenant)

**Fictional Scenario**: FinBank is a financial institution that operates in Brazil. They have reached out to Pismo to support their product expansion in the local market. After connecting with a pre-sales representative and signing a work agreement, FinBank initiates the onboarding process with the Pismo platform. The Pismo support team creates their organization (org), sometimes called the tenant. An org is an object that represents an organization on the Pismo platform. For more information about org creation and all other onboarding tasks, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding) .

# Step 2: Create token

To call any Pismo API endpoint, FinBank must first generate an authentication token using its `org_id`. With help from their Pismo support team, they select their authentication method. For more information, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

# Step 3: Create programs

FinBank decides to launch a new banking product for brand-new digital accounts on the Pismo platform. The accounts they create under this program are entirely branchless, meaning they are fully digital and operate in real-time through online channels. Refer to [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) for more information.

# Step 4: Create an account

After completing the previous steps, FinBank can create the necessary accounts. They created accounts for customer A and customer B. Refer to [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) for more information.

# Step 5: Provide credentials (when needed)

Because FinBank plans to offer bill issuance, bill payment, and direct wire transfers to its customers, it enters into a service agreement with a third-party partner of Pismo to provide these capabilities. For more information on bank accounts, Pix, bill payment, bill issuance, e-Bill, and indirect wire transfers, refer to the [Create provider credential](https://developers.pismo.io/pismo-docs/reference/post-credentials) guide. For more information on direct wire transfers, refer to [Register for TED transfers](https://developers.pismo.io/pismo-docs/reference/post-save-provider-configuration).

# Endpoints usage

For information on endpoints usage, refer to [Banking overview](https://developers.pismo.io/pismo-docs/docs/banking-overview).

<br />
<!-- source:end -->

### Source 2: `docs/get-started/get-started-building-core-banking.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-building-core-banking · updatedAt: 2026-06-29T19:37:33.000Z

<!-- source:begin path=docs/get-started/get-started-building-core-banking.md part=0-end -->

# Get started with core banking  

Core banking refers to the essential systems and processes that financial institutions use to manage customer accounts and transactions. These systems handle day-to-day operations such as deposits, withdrawals, payments, loans, and account maintenance. Core banking platforms ensure that banking services are available to customers in real-time across branches and digital channels.

On the Pismo platform, you access core banking functionality through APIs that support account creation, transaction processing, ledger management, and more. You can use the Pismo platform to build a suite of products—from deposits and savings to loans and overdrafts. Refer to [Banking overview](https://developers.pismo.io/pismo-docs/docs/banking-overview) for more information.

Banking with Pismo offers:

* Complete banking functionality:
  * Ledgers
  * Savings accounts
  * Current accounts
  * Deposits and overdrafts
  * Spending limits and controls at the account level
* Integrations with credit card networks, anti-fraud services, card embossers, and other third-party providers

This guide outlines the essential steps for setting up a new banking customer on the Pismo platform. Using a fictional banking scenario, it presents a series of steps that illustrate the configuration workflow.

<Callout icon="📘" theme="info">
  **Note**

  Before you make API requests to the Pismo platform, make sure you’ve installed Postman and have configured all required certificates and keys. For more information, refer to [Test Pismo API Endpoints with Postman](https://developers.pismo.io/pismo-docs/docs/testing-pismo-api-endpoints-with-postman).
</Callout>

Getting started with core banking involves these steps.

![Illustration of a step by step list to get started with core banking](https://files.readme.io/3ea9d3e22e7b928a8319c78aa90972829797fc9e9e66330b3693080107d3e4d7-image.png)

# Step 1: Create your organization (tenant)

**Fictional Scenario**: FinBank is a financial institution that operates in Brazil. They have reached out to Pismo to support their product expansion in the local market. After connecting with a pre-sales representative and signing a work agreement, FinBank initiates the onboarding process with the Pismo platform. The Pismo support team creates their organization (org), sometimes called the tenant. An org is an object that represents an organization on the Pismo platform. For more information about org creation and all other onboarding tasks, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding) .

# Step 2: Create token

To call any Pismo API endpoint, FinBank must first generate an authentication token using its `org_id`. With help from their Pismo support team, they select their authentication method. For more information, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

# Step 3: Create programs

FinBank decides to launch a new banking product for brand-new digital accounts on the Pismo platform. The accounts they create under this program are entirely branchless, meaning they are fully digital and operate in real-time through online channels. Refer to [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) for more information.

# Step 4: Create an account

After completing the previous steps, FinBank can create the necessary accounts. They created accounts for customer A and customer B. Refer to [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) for more information.

# Step 5: Provide credentials (when needed)

Because FinBank plans to offer bill issuance, bill payment, and direct wire transfers to its customers, it enters into a service agreement with a third-party partner of Pismo to provide these capabilities. For more information on bank accounts, Pix, bill payment, bill issuance, e-Bill, and indirect wire transfers, refer to the [Create provider credential](https://developers.pismo.io/pismo-docs/reference/post-credentials) guide. For more information on direct wire transfers, refer to [Register for TED transfers](https://developers.pismo.io/pismo-docs/reference/post-save-provider-configuration).

# Endpoints usage

For information on endpoints usage, refer to [Banking overview](https://developers.pismo.io/pismo-docs/docs/banking-overview).

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /banking-auth/v1/credentials` | `post-credentials` | Create provider credential | `api-specs/Banking_-_Authentication.yaml` | no | KU-API-banking-authentication--provider-credentials |
| `POST /v1/provider-configuration` | `post-save-provider-configuration` | Register for TED transfers | `api-specs/Banking_-_TED_configuration.yaml` | no | KU-API-banking-ted-configuration--configurations |

### Operation essentials

- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /banking-auth/v1/credentials`** (`post-credentials`): security `bearerAuth`; required parameters `account_token` (header); required body fields `key`, `provider`, `type`; response statuses 201, 400, 500, 502, 504; error codes in examples `EBAA0004`, `BA00005`, `EBAA0007`, `EPIX0005`, `EBAA0009`, `EBAA0010`, `EBAA0011`, `EBAA0012`, `EBAA0014`, `EBAA0002`, `EBAA0003`; events none listed.
- **`POST /v1/provider-configuration`** (`post-save-provider-configuration`): security `BearerAuth`; required parameters none declared; required body fields `branch`, `code`, `document_number`, `password`, `provider`, `url`, `user`; response statuses 201, 400, 403, 404, 500; error codes in examples `EBS0009`, `EBS0065`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/get-started-with-core-banking.md`: updatedAt 2026-06-10T18:18:56.000Z.
- `docs/get-started/get-started-building-core-banking.md`: updatedAt 2026-06-29T19:37:33.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The grouped source pages have identical bodies (published twice under different URLs); both are kept verbatim for traceability.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/get-started-with-core-banking.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-with-core-banking | `4f5c1af26df140e3…` | 2026-06-10T18:18:56.000Z |
| `docs/get-started/get-started-building-core-banking.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-building-core-banking | `4b3b581152c24b11…` | 2026-06-29T19:37:33.000Z |

## Related knowledge units

- `KU-API-banking-authentication--provider-credentials` — API reference: Banking - Authentication — Provider credentials
- `KU-API-banking-ted-configuration--configurations` — API reference: Banking - TED configuration — Configurations
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-BANK-banking-overview` — Banking overview
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-pismo-platform-onboarding` — Onboarding for new customers
