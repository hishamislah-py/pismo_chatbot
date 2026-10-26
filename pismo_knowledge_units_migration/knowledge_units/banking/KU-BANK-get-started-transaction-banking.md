---
ku_id: KU-BANK-get-started-transaction-banking
title: Get started with transaction banking
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/get-started-with-transaction-banking.md
  sha256: 66ce4c582ee67a29709e415280d121247455849d35b06b3d33fc2233e00c82b2
  url: https://developers.pismo.io/pismo-docs/docs/get-started-with-transaction-banking
  role: primary_guide
  updated_at: '2026-06-10T18:32:41.000Z'
- path: docs/get-started/get-started-building-transaction-banking.md
  sha256: 64441f4e5a61cbff19b7efa9042e5cea8b36ce821b127feef39943600d02aed4
  url: https://developers.pismo.io/pismo-docs/docs/get-started-building-transaction-banking
  role: primary_guide
  updated_at: '2026-06-29T19:37:33.000Z'
operations:
- CreateProgramBasedOnTemplate
- post-account
- post-account-balance-history-configuration
- post-division-v2
- post-dormancy-config-v2
- post-hierarchies
- post-v2-admin-division
- post-v2-holiday
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--dormancy
- KU-API-banking-transaction-banking--hierarchies
- KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated
- KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat
- KU-API-platform-setup-programs--programs-part-01
- KU-BANK-calendars-and-holidays
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-GS-pismo-platform-onboarding
grouping_rationale: Identical bodies (duplicate pages).
---

# Get started with transaction banking

**KU ID:** `KU-BANK-get-started-transaction-banking` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Identical bodies (duplicate pages).

Scope as stated in `docs/core-banking/get-started-with-transaction-banking.md`:

> Transaction banking demands precise control of global and local operations and a clear view of each account’s cash-flow history. The Pismo platform meets these requirements with a distributed microservices architecture that lets you activate only the components your business needs. You can build anything from a simple virtual-account ledger to a sophisticated corporate structure with customized hierarchies. The platform also offers scheduled and file-based transaction processing, earmarking, value-dating, and other financial functions.

Scope as stated in `docs/get-started/get-started-building-transaction-banking.md`:

> Transaction banking demands precise control of global and local operations and a clear view of each account’s cash-flow history. The Pismo platform meets these requirements with a distributed microservices architecture that lets you activate only the components your business needs. You can build anything from a simple virtual-account ledger to a sophisticated corporate structure with customized hierarchies. The platform also offers scheduled and file-based transaction processing, earmarking, value-dating, and other financial functions.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/get-started-with-transaction-banking.md`: Get started with transaction banking; Step 1: Create your organization (org); Step 2: Select authentication method; Step 3: Create programs; Step 4: Create an organizational hierarchy; Step 5: Create administrative divisions; Step 6: Create holidays; Step 7: Create divisions; Step 8: Configure cycle closing time; Step 9: Configure dormancy; Step 10: Create transaction banking accounts
- `docs/get-started/get-started-building-transaction-banking.md`: Get started with transaction banking; Step 1: Create your organization (org); Step 2: Select authentication method; Step 3: Create programs; Step 4: Create an organizational hierarchy; Step 5: Create administrative divisions; Step 6: Create holidays; Step 7: Create divisions; Step 8: Configure cycle closing time; Step 9: Configure dormancy; Step 10: Create transaction banking accounts

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 8 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/get-started-with-transaction-banking.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-with-transaction-banking · updatedAt: 2026-06-10T18:32:41.000Z

<!-- source:begin path=docs/core-banking/get-started-with-transaction-banking.md part=0-end -->

# Get started with transaction banking

Transaction banking demands precise control of global and local operations and a clear view of each account’s cash-flow history. The Pismo platform meets these requirements with a distributed microservices architecture that lets you activate only the components your business needs. You can build anything from a simple virtual-account ledger to a sophisticated corporate structure with customized hierarchies. The platform also offers scheduled and file-based transaction processing, earmarking, value-dating, and other financial functions.

Follow these steps to onboard a new client to the transaction banking platform. Each step is illustrated using a fictional financial conglomerate named VeryLarge Bank that operates in more than 30 countries.

<Callout icon="📘" theme="info">
  **Note**

  You can use Postman to test the endpoints linked to in the steps. For more information, refer to [Testing Pismo API endpoints with Postman](https://developers.pismo.io/pismo-docs/docs/testing-pismo-api-endpoints-with-postman).
</Callout>

Get started with transaction banking involves these steps.

<Image align="center" alt="How to get started with transacction banking" caption="Figure 1: Get started with transaction banking" src="https://files.readme.io/4985ec52180d5d73039386a6a667defd245ccb6e2126030e048ebd7473827464-How_to_get_started_with_transaction_banking.png" />

# Step 1: Create your organization (org)

VeryLarge Bank asks Pismo to modernize its North American banking operations. A Pismo pre-sales representative responds and finalizes the agreement. VeryLarge Bank initiates the onboarding process with the Pismo platform. The Pismo support team creates their organization (org). An org is an object that represents an organization on the Pismo platform. For more information about org creation and all other onboarding tasks, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

# Step 2: Select authentication method

To call any Pismo API endpoint, VeryLarge Bank must first generate an authentication token using its `org_id`. With help from their Pismo support team, they select their authentication method. For more information, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

# Step 3: Create programs

VeryLarge Bank plans to roll out a next-generation product on the Pismo platform for green-field accounts (brand-new accounts created from scratch on a new platform). Every account in this program is fully digital and branchless, offering online real-time service. VeryLarge Bank uses the [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) endpoint to create a program.

# Step 4: Create an organizational hierarchy

VeryLarge Bank reviews its branch hierarchy and, given the dominance of digital banking in North America, chooses not to replicate physical branches in Pismo. Instead, the hierarchy reflects geography: Holding at the top, followed by Country, then Region. To create an organizational hierarchy, VeryLarge Bank uses the [Create hierarchy](https://developers.pismo.io/pismo-docs/reference/post-hierarchies) endpoint.

# Step 5: Create administrative divisions

Administrative divisions functions as a  [calendar](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-transaction-banking#creating-a-calendar), it's used to divide an organization's territory into separate areas. An organization covering Great Britain, for example, is a separate administrative division within an organization.

The bank uses the [Create administrative division](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) endpoint to create a separate administrative division for each of the 30+ countries it operates in. This allows it to capture the local holidays for each country, as well as, differences in how each country defines weekends. With the hierarchy in place, VeryLarge Bank configures its calendars, designates the working weekdays, and sets rules for handling transactions on non-working days. Since the bank operates in 30+ countries, it creates a separate calendar for each one to capture local holidays. [Create administrative division](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) endpoint is used for this purpose.

# Step 6: Create holidays

For every calendar, VeryLarge Bank establishes [holidays](https://developers.pismo.io/pismo-docs/reference/post-v2-holiday) and sets the parameters that determine how transactions should behave on those specific days.

# Step 7: Create divisions

The next thing VeryLarge Bank needs to do is to create [divisions](https://developers.pismo.io/pismo-docs/reference/post-division-v2) . VeryLarge Bank operates its businesses in four geographic locations—Pacific, Mountain, Central, and Eastern—so it needs to create four divisions with each representing their respective location. Branches in each location must open and close at the same time, therefore, in every division, VeryLarge Bank must define the [programs](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) to which bank accounts belong and specify the calendar that the division follows.

# Step 8: Configure cycle closing time

Looking ahead, if VeryLarge Bank wants to define divisions by their daily closing times—the point at which each cycle ends. It must configure a separate [balance history](https://developers.pismo.io/pismo-docs/reference/post-account-balance-history-configuration) for each division. If no cycle‑closing configuration is set, the cycle closes at midnight in the division’s time zone.

# Step 9: Configure dormancy

To guard against fraud, VeryLarge Bank keeps a close eye on all idle accounts. Accordingly, it has defined, for each account program, the number of transaction-free days after which an account is deemed dormant, inactive, or unclaimed. VeryLarge Bank uses the [Create dormancy](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) endpoint to establish dormancy rules for each account.

# Step 10: Create transaction banking accounts

Once the configurations are complete, VeryLarge Bank proceeds to open  [accounts](https://developers.pismo.io/pismo-docs/reference/post-account) for its customers.

<br />
<!-- source:end -->

### Source 2: `docs/get-started/get-started-building-transaction-banking.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-building-transaction-banking · updatedAt: 2026-06-29T19:37:33.000Z

<!-- source:begin path=docs/get-started/get-started-building-transaction-banking.md part=0-end -->

# Get started with transaction banking

Transaction banking demands precise control of global and local operations and a clear view of each account’s cash-flow history. The Pismo platform meets these requirements with a distributed microservices architecture that lets you activate only the components your business needs. You can build anything from a simple virtual-account ledger to a sophisticated corporate structure with customized hierarchies. The platform also offers scheduled and file-based transaction processing, earmarking, value-dating, and other financial functions.

Follow these steps to onboard a new client to the transaction banking platform. Each step is illustrated using a fictional financial conglomerate named VeryLarge Bank that operates in more than 30 countries.

<Callout icon="📘" theme="info">
  **Note**

  You can use Postman to test the endpoints linked to in the steps. For more information, refer to [Testing Pismo API endpoints with Postman](https://developers.pismo.io/pismo-docs/docs/testing-pismo-api-endpoints-with-postman).
</Callout>

Get started with transaction banking involves these steps.

<Image align="center" alt="How to get started with transacction banking" caption="Figure 1: Get started with transaction banking" src="https://files.readme.io/4985ec52180d5d73039386a6a667defd245ccb6e2126030e048ebd7473827464-How_to_get_started_with_transaction_banking.png" />

# Step 1: Create your organization (org)

VeryLarge Bank asks Pismo to modernize its North American banking operations. A Pismo pre-sales representative responds and finalizes the agreement. VeryLarge Bank initiates the onboarding process with the Pismo platform. The Pismo support team creates their organization (org). An org is an object that represents an organization on the Pismo platform. For more information about org creation and all other onboarding tasks, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

# Step 2: Select authentication method

To call any Pismo API endpoint, VeryLarge Bank must first generate an authentication token using its `org_id`. With help from their Pismo support team, they select their authentication method. For more information, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

# Step 3: Create programs

VeryLarge Bank plans to roll out a next-generation product on the Pismo platform for green-field accounts (brand-new accounts created from scratch on a new platform). Every account in this program is fully digital and branchless, offering online real-time service. VeryLarge Bank uses the [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) endpoint to create a program.

# Step 4: Create an organizational hierarchy

VeryLarge Bank reviews its branch hierarchy and, given the dominance of digital banking in North America, chooses not to replicate physical branches in Pismo. Instead, the hierarchy reflects geography: Holding at the top, followed by Country, then Region. To create an organizational hierarchy, VeryLarge Bank uses the [Create hierarchy](https://developers.pismo.io/pismo-docs/reference/post-hierarchies) endpoint.

# Step 5: Create administrative divisions

Administrative divisions functions as a  [calendar](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-transaction-banking#creating-a-calendar), it's used to divide an organization's territory into separate areas. An organization covering Great Britain, for example, is a separate administrative division within an organization.

The bank uses the [Create administrative division](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) endpoint to create a separate administrative division for each of the 30+ countries it operates in. This allows it to capture the local holidays for each country, as well as, differences in how each country defines weekends. With the hierarchy in place, VeryLarge Bank configures its calendars, designates the working weekdays, and sets rules for handling transactions on non-working days. Since the bank operates in 30+ countries, it creates a separate calendar for each one to capture local holidays. [Create administrative division](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) endpoint is used for this purpose.

# Step 6: Create holidays

For every calendar, VeryLarge Bank establishes [holidays](https://developers.pismo.io/pismo-docs/reference/post-v2-holiday) and sets the parameters that determine how transactions should behave on those specific days.

# Step 7: Create divisions

The next thing VeryLarge Bank needs to do is to create [divisions](https://developers.pismo.io/pismo-docs/reference/post-division-v2) . VeryLarge Bank operates its businesses in four geographic locations—Pacific, Mountain, Central, and Eastern—so it needs to create four divisions with each representing their respective location. Branches in each location must open and close at the same time, therefore, in every division, VeryLarge Bank must define the [programs](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) to which bank accounts belong and specify the calendar that the division follows.

# Step 8: Configure cycle closing time

Looking ahead, if VeryLarge Bank wants to define divisions by their daily closing times—the point at which each cycle ends. It must configure a separate [balance history](https://developers.pismo.io/pismo-docs/reference/post-account-balance-history-configuration) for each division. If no cycle‑closing configuration is set, the cycle closes at midnight in the division’s time zone.

# Step 9: Configure dormancy

To guard against fraud, VeryLarge Bank keeps a close eye on all idle accounts. Accordingly, it has defined, for each account program, the number of transaction-free days after which an account is deemed dormant, inactive, or unclaimed. VeryLarge Bank uses the [Create dormancy](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) endpoint to establish dormancy rules for each account.

# Step 10: Create transaction banking accounts

Once the configurations are complete, VeryLarge Bank proceeds to open  [accounts](https://developers.pismo.io/pismo-docs/reference/post-account) for its customers.

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /corporate/v1/hierarchies` | `post-hierarchies` | Create hierarchy | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--hierarchies |
| `POST /divisions-core/v2/administrative-division` | `post-v2-admin-division` | Create administrative division (deprecated) | `api-specs/Platform_setup_-_Divisions.yaml` | **yes** | KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated |
| `POST /holidays-core/v2/holiday` | `post-v2-holiday` | Create holiday (deprecated) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat |
| `POST /corporate/v2/divisions` | `post-division-v2` | Create division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `POST /bank-statements/v1/account-balances/history/config` | `post-account-balance-history-configuration` | Create account balance history config v1 | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `POST /corporate/v2/dormancy-config` | `post-dormancy-config-v2` | Create dormancy configuration | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `POST /corporate/v1/corporate-accounts` | `post-account` | Create transaction banking account | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |

### Operation essentials

- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /corporate/v1/hierarchies`** (`post-hierarchies`): security `BearerAuth`; required parameters none declared; required body fields `name`, `levels`; response statuses 201, 400, 401, 403, 500; error codes in examples `WHIE0001`, `WHIE0002`, `WHIE0003`, `WHIE0004`, `WHIE0005`, `WHIE0007`, `ECMN9999`; events `corporate-hierarchy-creation-1`.
- **`POST /divisions-core/v2/administrative-division`** (`post-v2-admin-division`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`; response statuses 201, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /holidays-core/v2/holiday`** (`post-v2-holiday`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `holiday_date`; response statuses 201, 400, 401, 404, 500; error codes in examples `EHLD0016`, `EHLD0028`, `EHLD0030`, `EHLD0031`, `EHLD0027`, `EHLD0001`; events none listed.
- **`POST /corporate/v2/divisions`** (`post-division-v2`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `hierarchy_id`, `level_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WDIV0015`, `WDIV0011`, `WDIV0005`, `WDIV0007`, `WDIV0006`, `WDIV0012`, `WDIV0018`, `WDIV0019`, `WDIV0017`, `WDIV0016`, `ECMN9999`; events `corporate-division-creation-2`.
- **`POST /bank-statements/v1/account-balances/history/config`** (`post-account-balance-history-configuration`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `cycle_closing_time`, `cycle_event_delay`; response statuses 201, 400, 404, 409, 500; error codes in examples `WCFG0002`, `WCFG0001`, `WCFG0003`, `WCFG0004`, `ECMN9999`; events `account-balances-balance-history-config-creation-1`.
- **`POST /corporate/v2/dormancy-config`** (`post-dormancy-config-v2`): security `BearerAuth`; required parameters none declared; required body fields `check_time`, `target_type`, `target_id`, `statuses`; response statuses 201, 400, 401, 403, 404, 500; error codes in examples `WDOR0001`, `WDOR0002`, `WDOR0010`, `WDOR0011`, `WDOR0005`, `WDOR0006`, `WDOR0008`, `WDOR0009`, `WDOR0004`, `WDOR0003`, `ECMN9999`; events `corporate-dormancy-config-creation-1`.
- **`POST /corporate/v1/corporate-accounts`** (`post-account`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `program_id`, `applicant`, `external_account_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WCAC0013`, `WCAC0005`, `WCAC0006`, `WCAC0004`, `WCAC0016`, `WCAC0009`, `WDIV0002`, `WCAC0011`, `WCAC0014`, `ECMN9999`; events `corporate-corporate-account-creation-1`, `onboarding-succeeded-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-account-balance-history-configuration` | `account-balances-balance-history-config-creation-1` |
| `post-account` | `corporate-corporate-account-creation-1` |
| `post-division-v2` | `corporate-division-creation-2` |
| `post-dormancy-config-v2` | `corporate-dormancy-config-creation-1` |
| `post-hierarchies` | `corporate-hierarchy-creation-1` |
| `post-account` | `onboarding-succeeded-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/get-started-with-transaction-banking.md`: updatedAt 2026-06-10T18:32:41.000Z.
- `docs/get-started/get-started-building-transaction-banking.md`: updatedAt 2026-06-29T19:37:33.000Z.
- Links to `post-v2-admin-division`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Divisions.yaml`.
- Links to `post-v2-holiday`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Holidays.yaml`.

## Conflicts, caveats and evidence gaps

- The grouped source pages have identical bodies (published twice under different URLs); both are kept verbatim for traceability.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/get-started-with-transaction-banking.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-with-transaction-banking | `66ce4c582ee67a29…` | 2026-06-10T18:32:41.000Z |
| `docs/get-started/get-started-building-transaction-banking.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-building-transaction-banking | `64441f4e5a61cbff…` | 2026-06-29T19:37:33.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-banking-transaction-banking--hierarchies` — API reference: Banking - Transaction banking — Hierarchies
- `KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated` — API reference: Platform setup - Divisions — Administrative divisions V2 (deprecated)
- `KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat` — API reference: Platform setup - Holidays — Holidays v2 - Transaction banking (deprecated)
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-BANK-calendars-and-holidays` — Calendars, holidays and posting transactions on holidays in transaction banking
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-pismo-platform-onboarding` — Onboarding for new customers
