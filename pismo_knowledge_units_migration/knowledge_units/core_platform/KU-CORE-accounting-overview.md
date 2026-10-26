---
ku_id: KU-CORE-accounting-overview
title: Accounting overview and accounting event types
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/accounting-overview.md
  sha256: be3a406fb84b5150c75b9727e5720d915b636a3fca96d618cac6efb1bccf1359
  url: https://developers.pismo.io/pismo-docs/docs/accounting-overview
  role: primary_guide
  updated_at: '2026-03-18T15:14:14.000Z'
- path: docs/core-platform/search-for-accounting-event-types.md
  sha256: 70c549bca4fb0bdab8102e8ef76921ed13ffd6098dc65e3d0c501c6b5c4b16eb
  url: https://developers.pismo.io/pismo-docs/docs/search-for-accounting-event-types
  role: primary_guide
  updated_at: '2026-03-18T15:14:15.000Z'
operations:
- CreateAccountingAccount
- CreateAccountingEntry
- GetAccountingScriptById
- GetEntryTypeById
- GetEventTypeById
- SearchEvents
related_kus:
- KU-API-core-platform-accounting--accounting-accounts
- KU-API-core-platform-accounting--accounting-entry
- KU-API-core-platform-accounting--accounting-entry-types
- KU-API-core-platform-accounting--accounting-event-types
- KU-API-core-platform-accounting--accounting-scripts-v1
- KU-CORE-accounting-accounts-and-entries
- KU-CORE-transactions-overview
- KU-EVT-catalogue-other-domains
- KU-EVT-data-events-concepts
- KU-EVT-real-time-event-delivery
- KU-EVT-setting-up-event-file-delivery
- KU-GS-setup-overview
grouping_rationale: Overview and its lookup task.
---

# Accounting overview and accounting event types

**KU ID:** `KU-CORE-accounting-overview` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Overview and its lookup task.

Scope as stated in `docs/core-platform/accounting-overview.md`:

> Accounting is the recordkeeping of business and financial transactions. You would then analyze, summarize, and report these transaction records to ensure the company’s activities are achieving their purpose. When you use the Pismo platform, you can perform the accounting after processing a transaction.

Scope as stated in `docs/core-platform/search-for-accounting-event-types.md`:

> Accounting events on the Pismo platform tell you which financial [transaction](https://developers.pismo.io/pismo-docs/docs/transactions-overview) produced the event along with its type. For example, event type id 124  represents International Withdrawal. This means when the Pismo platform creates a financial transaction for an international withdrawal, an accounting event occurs and its type is 124.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/accounting-overview.md`: Accounting overview; Accounting elements in the Pismo platform; Accounting script; Accounting accounts; Cost centers; Accounting events; Accounting entries; How Pismo handles accounting
- `docs/core-platform/search-for-accounting-event-types.md`: Search for accounting event types; Search for an accounting event type

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/accounting-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accounting-overview · updatedAt: 2026-03-18T15:14:14.000Z

<!-- source:begin path=docs/core-platform/accounting-overview.md part=0-end -->

# Accounting overview

Accounting is the recordkeeping of business and financial transactions. You would then analyze, summarize, and report these transaction records to ensure the company’s activities are achieving their purpose. When you use the Pismo platform, you can perform the accounting after processing a transaction.

# Accounting elements in the Pismo platform

Here are the five accounting elements in the Pismo platform:

* Accounting scripts
* Accounting events
* Accounting entries
* Accounting accounts
* Cost centers (optional)

## Accounting script

The accounting script is the most important accounting element in the Pismo platform. It represents how the platform generates accounting entries when an event type occurs. For example, it shows which debit account and credit account an amount flows into.

The following shows the usual elements of the accounting script.

<Image title="Accounting Script.png" alt="Image shows the usual elements of the accounting script." align="center" src="https://files.readme.io/df625aa-Accounting_Script.png">
  The accounting script and its elements
</Image>

The following table explains these elements.

| Element                                                                                             | Description                                                                                                                                                                  |
| :-------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Org](https://developers.pismo.io/pismo-docs/docs/setup-overview)                                   | The company's ID in the Pismo platform.                                                                                                                                      |
| [Program](https://developers.pismo.io/pismo-docs/docs/setup-overview)                               | The product that the accounting script belongs to.                                                                                                                           |
| [Accounting Accounts](https://developers.pismo.io/pismo-docs/reference/createaccountingaccount)                                                  | Accounts that work as debit and credit accounts in the accounting script.                                                                                                    |
| [Event Type](https://developers.pismo.io/pismo-docs/docs/event-data#understanding-pismo-event-data) | The type of accounting event that makes the accounting script perform the accounting entries. For example, 112 - amount due date.                                            |
| [Entry Type](https://developers.pismo.io/pismo-docs/reference/getentrytypebyid)                                                                  | The type of accounting entry the accounting script produces. For example, 2100 - Installment - Without Interest - DUE DATE; 2101 - Installment - Without Interest - Base II. |

The accounting script allows you to set up for double-entry or single-entry accounting systems.

## Accounting accounts

The [accounting accounts](https://developers.pismo.io/pismo-docs/reference/createaccountingaccount) are the basis of the company’s accounting plan.  They represent where the money flows into a company's general ledger. In the Pismo platform, they are set by program. They are informed twice in the accounting scripts, since each accounting script has an account working as a credit and another one as a debit.

> 📘
>
> For Brazilian companies, you can link the accounting accounts to their corresponding Chart of Accounts for Financial Institutions (COSIF).

## Cost centers

Cost centers are entities that cost an organization money or resources. For example, a human resources department or a revenue center. Cost centers are optional in the Pismo platform. Only include cost centers if your organization requires it.

## Accounting events

Accounting events are business events in the Pismo platform that impact the company's records. The impact of these events are based on the accounting script's setup.

The Pismo platform has accounting events originated from different business events, such as:

* Financial: purchases and payments.
* Interest rate appropriation.
* Clearing events: confirmation, cancellation, and interchange.
* Time events: due-date or cycle closing date.
* Account events: account opening or limit changes.
* Chargeback events: chargeback opening, confirmation, and rejection.

## Accounting entries

[Accounting entries](https://developers.pismo.io/pismo-docs/reference/createaccountingentry) are the final product of the accounting events processing. These entries affect the company’s accounting records.

Here are the main attributes of an accounting entry:

* The org identification.
* An event identification that indicates which event produced this accounting entry.
* Debit and credit accounts affected by the amount of money flowing into them.
* The amount of money corresponding to the financial movement in the settlement currency.
* The creation date.
* The entry type identification that gives this accounting entry a description.

> 📘
>
> The accounting entries are delivered both in a [JSON format](https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery) through an [S3 bucket](https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery) and as a message in a [SNS topic](https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery).

## How Pismo handles accounting

The following shows how the Pismo platform handles these accounting elements and enters them into a customer application.

<Image title="Accounting Journey_02.png" alt="Image shows how the Pismo platform handles these accounting elements and enters them into a customer application." align="center" src="https://files.readme.io/90b0563-Accounting_Journey_02.png">
  The  journey of how accounting records flow into a customer application
</Image>
<!-- source:end -->

### Source 2: `docs/core-platform/search-for-accounting-event-types.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/search-for-accounting-event-types · updatedAt: 2026-03-18T15:14:15.000Z

<!-- source:begin path=docs/core-platform/search-for-accounting-event-types.md part=0-end -->

# Search for accounting event types

Accounting events on the Pismo platform tell you which financial [transaction](https://developers.pismo.io/pismo-docs/docs/transactions-overview) produced the event along with its type. For example, event type id 124  represents International Withdrawal. This means when the Pismo platform creates a financial transaction for an international withdrawal, an accounting event occurs and its type is 124.

Accounting events then use the [accounting scripts](https://developers.pismo.io/pismo-docs/docs/accounting-overview#accounting-script) to create [accounting entries](https://developers.pismo.io/pismo-docs/docs/create-accounting-entries). You can search for these accounting events on the Pismo platform.

## Search for an accounting event type

There are two ways you can search for an accounting event type. You can either search for an event type by its ID or search for all types.

To search for an event  type by its ID:

1. Copy the `event_type_id` number from the response in the [Accounting script](https://developers.pismo.io/pismo-docs/reference/getaccountingscriptbyid).
2. Paste this number into the **eventTypeId** field of the [Search event by ID endpoint](https://developers.pismo.io/pismo-docs/reference/geteventtypebyid).
3. Run the endpoint.

The event type ID and its description appear in the response.

To see all accounting event types:

1. Go to [Search Event types](https://developers.pismo.io/pismo-docs/reference/searchevents).
2. Set the amount of event types that appear per page in the **pageSize** field.
3. Set the page offset of accounting events in the **pageOffset** field.
4. Run the endpoint.

The paginated list of all event types appear in the response.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/accounting-accounts` | `CreateAccountingAccount` | Create accounting account | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-accounts |
| `GET /v1/entry-types/{entryTypeId}` | `GetEntryTypeById` | Get accounting entry type (outdated) | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-entry-types |
| `POST /v1/accounting-entries` | `CreateAccountingEntry` | Create accounting entry | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-entry |
| `GET /v1/accounting-scripts/{accountingScriptId}` | `GetAccountingScriptById` | Get accounting script V1 | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-scripts-v1 |
| `GET /v1/event-types/{eventTypeId}` | `GetEventTypeById` | Get accounting event type | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-event-types |
| `GET /v1/event-types` | `SearchEvents` | List accounting event types | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-event-types |

### Operation essentials

- **`POST /v1/accounting-accounts`** (`CreateAccountingAccount`): security `BearerAuth`; required parameters none declared; required body fields `description`, `account`, `program_id`; response statuses 201, 400, 409; error codes in examples none; events none listed.
- **`GET /v1/entry-types/{entryTypeId}`** (`GetEntryTypeById`): security `BearerAuth`; required parameters `entryTypeId` (path); required body fields none declared; response statuses 200, 404; error codes in examples none; events none listed.
- **`POST /v1/accounting-entries`** (`CreateAccountingEntry`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `entry_type_id`, `event_date`, `program_id`; response statuses 202, 400, 409; error codes in examples none; events `accounting-entry-creation-1`.
- **`GET /v1/accounting-scripts/{accountingScriptId}`** (`GetAccountingScriptById`): security `BearerAuth`; required parameters `accountingScriptId` (path); required body fields none declared; response statuses 200, 404; error codes in examples none; events none listed.
- **`GET /v1/event-types/{eventTypeId}`** (`GetEventTypeById`): security `BearerAuth`; required parameters `eventTypeId` (path); required body fields none declared; response statuses 200, 404; error codes in examples none; events none listed.
- **`GET /v1/event-types`** (`SearchEvents`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400; error codes in examples none; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `CreateAccountingEntry` | `accounting-entry-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/accounting-overview.md`: updatedAt 2026-03-18T15:14:14.000Z.
- `docs/core-platform/search-for-accounting-event-types.md`: updatedAt 2026-03-18T15:14:15.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/accounting-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accounting-overview | `be3a406fb84b5150…` | 2026-03-18T15:14:14.000Z |
| `docs/core-platform/search-for-accounting-event-types.md` | whole document | https://developers.pismo.io/pismo-docs/docs/search-for-accounting-event-types | `70c549bca4fb0bda…` | 2026-03-18T15:14:15.000Z |

## Related knowledge units

- `KU-API-core-platform-accounting--accounting-accounts` — API reference: Core platform - Accounting — Accounting accounts
- `KU-API-core-platform-accounting--accounting-entry` — API reference: Core platform - Accounting — Accounting entry
- `KU-API-core-platform-accounting--accounting-entry-types` — API reference: Core platform - Accounting — Accounting entry types
- `KU-API-core-platform-accounting--accounting-event-types` — API reference: Core platform - Accounting — Accounting event types
- `KU-API-core-platform-accounting--accounting-scripts-v1` — API reference: Core platform - Accounting — Accounting scripts V1
- `KU-CORE-accounting-accounts-and-entries` — Creating accounting accounts and accounting entries
- `KU-CORE-transactions-overview` — Transactions overview
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-data-events-concepts` — Data events: concepts and event-generating APIs
- `KU-EVT-real-time-event-delivery` — Real-time event delivery: setup, additional subscribers and event filtering
- `KU-EVT-setting-up-event-file-delivery` — Setting up event batch file delivery
- `KU-GS-setup-overview` — Core objects
