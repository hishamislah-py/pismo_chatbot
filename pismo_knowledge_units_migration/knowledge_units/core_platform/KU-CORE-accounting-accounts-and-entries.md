---
ku_id: KU-CORE-accounting-accounts-and-entries
title: Creating accounting accounts and accounting entries
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/create-an-accounting-account.md
  sha256: 8ca125323455bfa7939102f538eabf6263a96c5495c0f9dd182ece7d7bb79fef
  url: https://developers.pismo.io/pismo-docs/docs/create-an-accounting-account
  role: primary_guide
  updated_at: '2026-05-27T17:04:15.000Z'
- path: docs/core-platform/create-accounting-entries.md
  sha256: 82b8674fa0611ef8c2e3162eab0d5079e605f0cc188a352b615ff066c6a7d35f
  url: https://developers.pismo.io/pismo-docs/docs/create-accounting-entries
  role: primary_guide
  updated_at: '2026-05-27T17:03:41.000Z'
operations:
- CreateAccountingAccount
- CreateAccountingEntry
- CreateAccountingScript
- DeleteAccountingAccount
- GetAccountingAccountById
- GetAccountingScriptById
- GetEntryTypeById
- SearchAccountingAccounts
- UpdateAccountingAccount
related_kus:
- KU-API-core-platform-accounting--accounting-accounts
- KU-API-core-platform-accounting--accounting-entry
- KU-API-core-platform-accounting--accounting-entry-types
- KU-API-core-platform-accounting--accounting-scripts-v1
- KU-CORE-accounting-overview
- KU-EVT-catalogue-other-domains
- KU-EVT-real-time-event-delivery
- KU-EVT-setting-up-event-file-delivery
- KU-GS-setup-overview
grouping_rationale: Sequential accounting setup tasks.
---

# Creating accounting accounts and accounting entries

**KU ID:** `KU-CORE-accounting-accounts-and-entries` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Sequential accounting setup tasks.

Scope as stated in `docs/core-platform/create-an-accounting-account.md`:

> You can create an [accounting account](https://developers.pismo.io/pismo-docs/reference/createaccountingaccount) on the Pismo platform, so you can add it to your [accounting script](https://developers.pismo.io/pismo-docs/reference/createaccountingscript). In the accounting script, you set an accounting account as a debit and another accounting account as a credit. When you run the accounting script, the Pismo platform creates an accounting entry using the accounting account’s information.

Scope as stated in `docs/core-platform/create-accounting-entries.md`:

> You can manually [create accounting entries using the Pismo platform](https://developers.pismo.io/pismo-docs/reference/createaccountingentry). You might need to create accounting entries to:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/create-an-accounting-account.md`: Create accounting accounts; Create an accounting account; Example; Search for an accounting account; Example; Update an accounting account description; Example; Deactivate an accounting account; Example
- `docs/core-platform/create-accounting-entries.md`: Create accounting entries; Create an accounting entry; Search for accounting entry types

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 9 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/create-an-accounting-account.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/create-an-accounting-account · updatedAt: 2026-05-27T17:04:15.000Z

<!-- source:begin path=docs/core-platform/create-an-accounting-account.md part=0-end -->

# Create accounting accounts

You can create an [accounting account](https://developers.pismo.io/pismo-docs/reference/createaccountingaccount) on the Pismo platform, so you can add it to your [accounting script](https://developers.pismo.io/pismo-docs/reference/createaccountingscript). In the accounting script, you set an accounting account as a debit and another accounting account as a credit. When you run the accounting script, the Pismo platform creates an accounting entry using the accounting account’s information.

## Create an accounting account

To create an accounting account:

1. Go to [Create accounting account](https://developers.pismo.io/pismo-docs/reference/createaccountingaccount).
2. Enter the description of this account in the **description** field.
3. Enter the account number in the account field.
4. Enter your [program ID](https://developers.pismo.io/pismo-docs/docs/setup-overview) in the **program\_id** field.
5. Run the endpoint.

The response shows when you created the accounting account in the `created_at` field.

## Example

This response shows a created accounting account.

```json
{
  "id": 1,
  "description": "SAMPLE ACCOUNT",
  "account": "123123132-x",
  "program_id": 12,
  "created_at": "2021-10-10T10:10:00.000Z"
  }
```

## Search for an accounting account

There are two ways you can search for an accounting account on the Pismo platform. You can either search for an [account by its ID](https://developers.pismo.io/pismo-docs/reference/getaccountingaccountbyid) or search for [all accounts](https://developers.pismo.io/pismo-docs/reference/searchaccountingaccounts). To search by ID, copy the `id` number from a created accounting account and paste it into the **accountingAccountId** field.

## Example

This response shows when you search a list of accounting accounts:

```json
{
	"has_next": false,
	"items": [
		{
			"id": 1,
			"description": "ACCOUNTING ACCOUNT CREATION TEST",
			"account": "123123132-x",
			"program_id": 1,
			"created_at": "2021-07-22T00:37:20Z"
		},
		{
			"id": 2,
			"description": "ACCOUNTING ACCOUNT CREATION TEST",
			"account": "123123132-x",
			"program_id": 1,
			"created_at": "2021-07-22T00:37:20Z"
		}
	]
}
```

> 📘
>
> The `has_next` parameter means there are more pages to view.

You can still search for [deactivated accounting accounts](https://developers.pismo.io/pismo-docs/docs/create-an-accounting-account#deactivate-an-accounting-account). This response shows a deactivated accounting account. The `deactivated_at` field only returns when the account is deactivated.

```json
{
	"has_next": false,
	"items": [
		{
			"id": 1,
			"description": "ACCOUNTING ACCOUNT CREATION TEST",
			"account": "123123132-x",
			"program_id": 1,
			"created_at": "2021-07-22T00:37:20Z",
			"deactivated_at": "2021-07-23T00:37:20Z"
		}
	]
}
```

## Update an accounting account description

If you find an accounting account description that’s incorrect, you can update it. To update a description of an accounting account:

1. Use the account ID from either `credit_accounting` or `debit_accounting` fields in the response of the [accounting script](https://developers.pismo.io/pismo-docs/reference/getaccountingscriptbyid).
2. Paste this number into the **accountingAccountId** field of the [Update an accounting account description by ID](https://developers.pismo.io/pismo-docs/reference/updateaccountingaccount) endpoint.
3. Write the new description for the accounting account in the `description` body parameter.
4. Run the endpoint.

## Example

This response shows the accounting account description before an update.

```json
{
"id": 2,
"description": "THIS IS THE OLD DESCRIPTION",
"account": "123123132-x",
"program_id": 1,
"created_at": "2021-07-22T00:37:20Z"
}
```

This response shows the accounting account description after an update.

```json
{
"id": 2,
"description": "THIS IS THE NEW DESCRIPTION",
"account": "123123132-x",
"program_id": 1,
"created_at": "2021-07-22T00:37:20Z"
}
```

## Deactivate an accounting account

To deactivate an accounting account, paste the ID into the **accountingAccountId** field of the [Deactivated an accounting account by ID](https://developers.pismo.io/pismo-docs/reference/deleteaccountingaccount) endpoint. To paste this ID, copy the number from the `id` field in an [accounting account](https://developers.pismo.io/pismo-docs/reference/getaccountingaccountbyid). The response shows when you deactivated the accounting account in the `deactivated_at` field.

## Example

This response shows a deactivated accounting account.

```json
{
	"id": 10,
	"description": "ACCOUNTINGACCOUNT",
	"account": "123123132-T1",
	"program_id": 1,
	"created_at": "2022-06-27T18:01:42Z",
	"deactivated_at": "2022-06-28T14:30:58.350214-03:00"
}
```
<!-- source:end -->

### Source 2: `docs/core-platform/create-accounting-entries.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/create-accounting-entries · updatedAt: 2026-05-27T17:03:41.000Z

<!-- source:begin path=docs/core-platform/create-accounting-entries.md part=0-end -->

# Create accounting entries

You can manually [create accounting entries using the Pismo platform](https://developers.pismo.io/pismo-docs/reference/createaccountingentry). You might need to create accounting entries to:

* Correct the balance of an accounting account.
* Move the balance from one accounting account to another.
* Account for a product that’s not on the Pismo platform.

When you create these entries, they affect your company’s accounting records. Accounting entries are the final product of the accounting events processing on the platform.

> 📘
>
> Besides the manual accounting entries creation, the Pismo platform also creates them for you based on the accounting scripts. Pismo is giving you the power to create your own accounting entry. To know more about accounting scripts, check the [Accounting overview](https://developers.pismo.io/pismo-docs/docs/accounting-overview).

## Create an accounting entry

To create an accounting entry on the Pismo platform, use these fields in [Create accounting entry](https://developers.pismo.io/pismo-docs/reference/createaccountingentry).

| Parameter                                   | Description                                                                                               |
| :------------------------------------------ | :-------------------------------------------------------------------------------------------------------- |
| **account\_id**                             | The ID number of an account.                                                                              |
| **credit\_accounting\_account**             | The credit accounting account number.                                                                     |
| **debit\_accounting\_account**              | The debit accounting account account number.                                                              |
| [**entry\_type\_id**](https://developers.pismo.io/pismo-docs/reference/getentrytypebyid) | The ID of the entry type. This entry type comes from the [accounting script](https://developers.pismo.io/pismo-docs/reference/createaccountingscript). |
| **event\_date**                             | The date the event occured.                                                                               |
| **program\_id**                             | The ID number of the program.                                                                             |
| **tracking\_id**                            | The tracking ID of the authorization.                                                                     |
| **transaction\_id**                         | The ID number of the transaction.                                                                         |

## Search for accounting entry types

Accounting entry types are created to classify accounting entries. They can identify the kind of accounting entry and why it was made, depending on their description attribute. For example, the entry type id 102 can be used for International Purchases, or the entry type id 301 that can be used for credit adjustments.

There are two ways you can search for accounting entry types on the Pismo platform. You can either search for an entry by its ID or by searching for all types.

To search for an entry by its ID:

1. Copy the `entry_type_id` number from the response in the [Accounting script](https://developers.pismo.io/pismo-docs/reference/getaccountingscriptbyid).
2. Paste this number into the **entryTypeId** field of the [Search entry type by ID](https://developers.pismo.io/pismo-docs/reference/getentrytypebyid) endpoint.
3. Run the endpoint.

The entry ID number appears in the `id` field of the response.

To see all accounting entry types:

1. Set the amount of entries that appear per page in the **pageSize** field.
2. Set the page offset of accounting entries in the **pageOffset** field.

The amount of entries you want will appear in the response.

> 📘
>
> The accounting entries are delivered both in a [JSON format](https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery) through an [S3 bucket](https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery) and as a message in a [SNS topic](https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/accounting-accounts` | `CreateAccountingAccount` | Create accounting account | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-accounts |
| `POST /v1/accounting-scripts` | `CreateAccountingScript` | Create accounting script V1 | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-scripts-v1 |
| `GET /v1/accounting-accounts/{accountingAccountId}` | `GetAccountingAccountById` | Get accounting account | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-accounts |
| `GET /v1/accounting-accounts` | `SearchAccountingAccounts` | List accounting accounts | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-accounts |
| `GET /v1/accounting-scripts/{accountingScriptId}` | `GetAccountingScriptById` | Get accounting script V1 | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-scripts-v1 |
| `PATCH /v1/accounting-accounts/{accountingAccountId}` | `UpdateAccountingAccount` | Update accounting account | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-accounts |
| `DELETE /v1/accounting-accounts/{accountingAccountId}` | `DeleteAccountingAccount` | Delete accounting account | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-accounts |
| `POST /v1/accounting-entries` | `CreateAccountingEntry` | Create accounting entry | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-entry |
| `GET /v1/entry-types/{entryTypeId}` | `GetEntryTypeById` | Get accounting entry type (outdated) | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-entry-types |

### Operation essentials

- **`POST /v1/accounting-accounts`** (`CreateAccountingAccount`): security `BearerAuth`; required parameters none declared; required body fields `description`, `account`, `program_id`; response statuses 201, 400, 409; error codes in examples none; events none listed.
- **`POST /v1/accounting-scripts`** (`CreateAccountingScript`): security `BearerAuth`; required parameters none declared; required body fields `entry_type_id`, `event_type_id`, `credit_accounting_account_id`, `debit_accounting_account_id`, `program_id`; response statuses 201, 400, 409; error codes in examples none; events none listed.
- **`GET /v1/accounting-accounts/{accountingAccountId}`** (`GetAccountingAccountById`): security `BearerAuth`; required parameters `accountingAccountId` (path); required body fields none declared; response statuses 200, 404; error codes in examples none; events none listed.
- **`GET /v1/accounting-accounts`** (`SearchAccountingAccounts`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400; error codes in examples none; events none listed.
- **`GET /v1/accounting-scripts/{accountingScriptId}`** (`GetAccountingScriptById`): security `BearerAuth`; required parameters `accountingScriptId` (path); required body fields none declared; response statuses 200, 404; error codes in examples none; events none listed.
- **`PATCH /v1/accounting-accounts/{accountingAccountId}`** (`UpdateAccountingAccount`): security `BearerAuth`; required parameters `accountingAccountId` (path); required body fields `description`; response statuses 200, 400, 404; error codes in examples none; events none listed.
- **`DELETE /v1/accounting-accounts/{accountingAccountId}`** (`DeleteAccountingAccount`): security `BearerAuth`; required parameters `accountingAccountId` (path); required body fields none declared; response statuses 200, 404, 409; error codes in examples none; events none listed.
- **`POST /v1/accounting-entries`** (`CreateAccountingEntry`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `entry_type_id`, `event_date`, `program_id`; response statuses 202, 400, 409; error codes in examples none; events `accounting-entry-creation-1`.
- **`GET /v1/entry-types/{entryTypeId}`** (`GetEntryTypeById`): security `BearerAuth`; required parameters `entryTypeId` (path); required body fields none declared; response statuses 200, 404; error codes in examples none; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `CreateAccountingEntry` | `accounting-entry-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/create-an-accounting-account.md`: updatedAt 2026-05-27T17:04:15.000Z.
- `docs/core-platform/create-accounting-entries.md`: updatedAt 2026-05-27T17:03:41.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/create-an-accounting-account.md` | whole document | https://developers.pismo.io/pismo-docs/docs/create-an-accounting-account | `8ca125323455bfa7…` | 2026-05-27T17:04:15.000Z |
| `docs/core-platform/create-accounting-entries.md` | whole document | https://developers.pismo.io/pismo-docs/docs/create-accounting-entries | `82b8674fa0611ef8…` | 2026-05-27T17:03:41.000Z |

## Related knowledge units

- `KU-API-core-platform-accounting--accounting-accounts` — API reference: Core platform - Accounting — Accounting accounts
- `KU-API-core-platform-accounting--accounting-entry` — API reference: Core platform - Accounting — Accounting entry
- `KU-API-core-platform-accounting--accounting-entry-types` — API reference: Core platform - Accounting — Accounting entry types
- `KU-API-core-platform-accounting--accounting-scripts-v1` — API reference: Core platform - Accounting — Accounting scripts V1
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-real-time-event-delivery` — Real-time event delivery: setup, additional subscribers and event filtering
- `KU-EVT-setting-up-event-file-delivery` — Setting up event batch file delivery
- `KU-GS-setup-overview` — Core objects
