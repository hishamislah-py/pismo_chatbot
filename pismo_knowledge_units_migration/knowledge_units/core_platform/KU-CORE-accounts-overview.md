---
ku_id: KU-CORE-accounts-overview
title: Accounts
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/accounts-overview.md
  sha256: b540de821fdcc1a31f69c4bdbee0295d47ae262da3024c33cccdd8ae8fae584a
  url: https://developers.pismo.io/pismo-docs/docs/accounts-overview
  role: primary_guide
  updated_at: '2026-09-14T22:10:12.000Z'
operations:
- PostMigrationProgram
- UpdateProgramInfo
- UpdateStatementsDueDate
- customerV2Post
- get-v1-account-balance
- get-v1-accounts-limits-related-accounts
- patch-accounts-v1-accounts
- patch-accounts-v2-accounts-accountId-status
- patch-acquisitions-v2-s2s-applications
- patch-v2-accounts-accountId-status-rollback
- post-acquisitions-v3-s2s-applications
- v4-get-account-reason
- v4-get-account-status
- v4-post-account-reason
- v4-post-account-status
related_kus:
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--customers
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-API-core-platform-accounts--transfer-account
- KU-API-core-platform-balances-and-limits--account-balances
- KU-API-core-platform-balances-and-limits--related-accounts
- KU-API-platform-setup-programs--programs-part-02
- KU-API-revolving-credit-statements--due-date
- KU-BANK-managing-account-statuses
- KU-CC-accounts
- KU-CORE-working-with-limits-objects
- KU-CRED-account-collection-status
- KU-EVT-catalogue-account
- KU-EVT-catalogue-other-domains
- KU-GS-program-types
grouping_rationale: single source page
---

# Accounts

**KU ID:** `KU-CORE-accounts-overview` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/accounts-overview.md`:

> Once you've set up your Organization and have implemented a [program](https://developers.pismo.io/pismo-docs/docs/program-types),  you can begin creating accounts and customers.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/accounts-overview.md`: Accounts; Create an account; Linking Pismo accounts to an external system; Related accounts; Link and unlink related accounts; Get related account information; Account customers; Account status; Create and update account statuses; Account status reasons; Other account statuses; Get daily account balance limits; Migrate account to different program; Change due date for credit programs

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 15 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/accounts-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accounts-overview · updatedAt: 2026-09-14T22:10:12.000Z

<!-- source:begin path=docs/core-platform/accounts-overview.md part=0-end -->

# Accounts

Once you've set up your Organization and have implemented a [program](https://developers.pismo.io/pismo-docs/docs/program-types),  you can begin creating accounts and customers.

# Create an account

You can create an account with the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications)  endpoint. You can create it with this endpoint or create it as a work-in-progress and add more information to it later with the [Update account application](https://developers.pismo.io/pismo-docs/reference/patch-acquisitions-v2-s2s-applications)  endpoint before finally submitting it to create the account and its related structures and data.

**Note:** The create and update endpoint processing is asynchronous, meaning that you should not try to access created or modified account objects until the events these endpoints generate are received.

> 📘 Account limits
>
> For information on this topic, refer to [Account limits](https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects).

# Linking Pismo accounts to an external system

Pismo's  `account` object has an `external_id` field that allows you to seamlessly integrate your systems and accounts with Pismo's.

# Related accounts

You can define a parent and child relationship between accounts. A parent account can have multiple child accounts. A child account can have only one parent, but it can have multiple child accounts of its own (grandchild accounts of the main parent account). All child and grandchild accounts connect to the main parent account.

<br />

<Image align="center" alt="Related accounts relationship diagram" src="https://files.readme.io/e50a2db-Related_accounts_V3.png" />

<br />

## Link and unlink related accounts

To link accounts, use the `account` object's `parent_account_id` field. You can set this when [creating an account](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) or [updating an account](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v1-accounts).

To unlink a parent account, call  [Update account](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v1-accounts) and enter "`null`"  for the `parent_account_id` field.

## Get related account information

You can see balances and limits of all related accounts with a single call to [Get related accounts](https://developers.pismo.io/pismo-docs/reference/get-v1-accounts-limits-related-accounts). Given a parent account ID, this endpoint provides an overview of all related accounts within the same Org, with up to two levels of child accounts. The endpoint returns balances and limits of both the parent account and its active child and grandchild accounts. Active account means that its [account status](https://developers.pismo.io/pismo-docs/docs/accounts-2#account-status) is `NORMAL`.

# Account customers

Each account must have at least one customer, which can be  a person or company. Each account is initially created with either a `person` or `company` object representing the account's initial customer and account owner.

[Additional customers are added](https://developers.pismo.io/pismo-docs/reference/customerv2post)  with a `customer` object. The `person` and `company` objects include many fields **not** included in the `customer` object.

An account can have multiple customers to support functionality such as joint accounts and credit cards that use the same account balance among multiple customers. A customer can have multiple accounts also. For example, a person may have an account associated with a corporate credit card and another account associated with a debit card.

# Account status

Every account is created with a `NORMAL` status.

The following table describes  pre-defined account status enum values.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Status
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `DEBIT_ONLY`
      </td>

      <td>
        Account is active. Allows cash-out but not cash-in.
      </td>
    </tr>

    <tr>
      <td>
        `NORMAL`
      </td>

      <td>
        Account is active. Allows both cash-in and cash-out, based on account limits.

        This is the default account status.
      </td>
    </tr>

    <tr>
      <td>
        `BLOCKED`
      </td>

      <td>
        Account is blocked. Allows cash-in only.

        This is a temporary status. You can change it to `DEBIT_ONLY`, `NORMAL`, or `CANCELLED` when needed.
      </td>
    </tr>

    <tr>
      <td>
        `CANCELLED`
      </td>

      <td>
        Account is cancelled. No cash-in or cash-out allowed.

        This is a final status. If you need to recover a cancelled account, you must use the [Roll back account status](https://developers.pismo.io/pismo-docs/reference/patch-v2-accounts-accountid-status-rollback) endpoint or change the status in [Control Center](https://developers.pismo.io/pismo-docs/docs/account-actions#change-account-status).
      </td>
    </tr>
  </tbody>
</Table>

## Create and update account statuses

* You can create your own account statuses with the [Create account status](https://developers.pismo.io/pismo-docs/reference/v4-post-account-status)  endpoint.
* You can call [List statuses](https://developers.pismo.io/pismo-docs/reference/v4-get-account-status) to get account statuses.
* You can update an account's status with the [Update account status](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v2-accounts-accountid-status) endpoint.

## Account status reasons

You have the option to specify reasons for an account status change. For example, an account could become `BLOCKED` due to a court order or fraud attempt.

* To add reasons to your Organization, use the [Create account status reason](https://developers.pismo.io/pismo-docs/reference/v4-post-account-reason) endpoint. This endpoint returns a reason ID that you can pass when you [update an account's status](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v2-accounts-accountid-status).
* You can call [List status reasons](https://developers.pismo.io/pismo-docs/reference/v4-get-account-reason) to get an account's status reasons and their IDs.

## Other account statuses

* [Account collection statuses](https://developers.pismo.io/pismo-docs/docs/account-collection-status)—Credit collection statuses such as `OVERDUE`.
* [Transaction banking account statuses](https://developers.pismo.io/pismo-docs/docs/managing-account-statuses) —Transaction banking accounts have their own unique statuses.

# Get daily account balance limits

You can use the [Get daily account balance limits](https://developers.pismo.io/pismo-docs/reference/get-v1-account-balance)  endpoint to get a range of the account's balance limits as calculated daily at 11:59PM in your time zone. You can define your own date range for the query or use the default range of 10 days prior to yesterday. You can query the account balance limits as far back as 515 days before the current date for the maximum range of 90 days.

In addition to using this endpoint, you can also schedule the [account limits report file](https://developers.pismo.io/pismo-docs/docs/account-limits-report-files) , which contains all consolidated account balances from the previous day.

# Migrate account to different program

The Pismo platform allows you to [migrate an account from one program to another](https://developers.pismo.io/pismo-docs/reference/postmigrationprogram). For instance, if a cardholder wants to upgrade their credit card program, use this endpoint to do the migration.

# Change due date for credit programs

If there is a conflict in due date between the account and the target program, you can change the due date in the account or in either the source or target programs:

* [Change the due date in the account](https://developers.pismo.io/pismo-docs/reference/updatestatementsduedate)
* [Change the due date in the program](https://developers.pismo.io/pismo-docs/reference/updateprograminfo)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `PATCH /acquisitions/v2/s2s/applications/{applicationId}` | `patch-acquisitions-v2-s2s-applications` | Update account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `PATCH /accounts/v1/accounts/{accountId}` | `patch-accounts-v1-accounts` | Update account | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `GET /v1/accounts/{accountId}/related-accounts-limits` | `get-v1-accounts-limits-related-accounts` | Get related accounts | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--related-accounts |
| `POST /accounts/v2/customers` | `customerV2Post` | Create customer | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |
| `PATCH /accounts/v2/accounts/{accountId}/status/rollback` | `patch-v2-accounts-accountId-status-rollback` | Roll back status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `POST /accounts/v4/statuses` | `v4-post-account-status` | Create status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `GET /accounts/v4/statuses` | `v4-get-account-status` | List statuses | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `PATCH /accounts/v2/accounts/{accountId}/status` | `patch-accounts-v2-accounts-accountId-status` | Update status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `POST /accounts/v4/reasons` | `v4-post-account-reason` | Create status reason | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `GET /accounts/v4/reasons` | `v4-get-account-reason` | List status reasons | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `GET /v1/accounts/{accountId}/daily-balances` | `get-v1-account-balance` | Get daily account balance limits | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--account-balances |
| `POST /accounts/v1/accounts/programs/migration` | `PostMigrationProgram` | Transfer account to different program | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--transfer-account |
| `PUT /statements/v1/accounts/{accountId}/statements/due-date` | `UpdateStatementsDueDate` | Change due date | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `PATCH /programs/v1/programs/{id}` | `UpdateProgramInfo` | Update program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-02 |

### Operation essentials

- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`PATCH /acquisitions/v2/s2s/applications/{applicationId}`** (`patch-acquisitions-v2-s2s-applications`): security `BearerAuth`; required parameters `applicationId` (path); required body fields none declared; response statuses 200, 400, 409, 500; error codes in examples none; events `onboarding-succeeded-1`.
- **`PATCH /accounts/v1/accounts/{accountId}`** (`patch-accounts-v1-accounts`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 401, 404, 500; error codes in examples none; events `account-account-change-2`.
- **`GET /v1/accounts/{accountId}/related-accounts-limits`** (`get-v1-accounts-limits-related-accounts`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `WBLS0001`, `WBLS0004`, `WBLS0006`, `EBLS9999`; events none listed.
- **`POST /accounts/v2/customers`** (`customerV2Post`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `entity`, `customer`; response statuses 201, 400, 409, 500; error codes in examples none; events `account-account-owner-change-1`, `account-customer-creation-1`.
- **`PATCH /accounts/v2/accounts/{accountId}/status/rollback`** (`patch-v2-accounts-accountId-status-rollback`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 204, 404, 500; error codes in examples none; events `account-status-change-2`.
- **`POST /accounts/v4/statuses`** (`v4-post-account-status`): security `BearerAuth`; required parameters none declared; required body fields `name`, `allowed_operations`; response statuses 201, 400, 409, 500; error codes in examples `EACC0004`, `EACC0018`, `EACC0000`, `EACC0003`, `EACC9999`; events `account-status-creation-1`.
- **`GET /accounts/v4/statuses`** (`v4-get-account-status`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `EACC0005`, `EACC0018`, `WACC0011`, `EACC0000`, `EACC9999`; events none listed.
- **`PATCH /accounts/v2/accounts/{accountId}/status`** (`patch-accounts-v2-accounts-accountId-status`): security `BearerAuth`; required parameters `accountId` (path); required body fields `status`; response statuses 204, 400, 404, 500; error codes in examples none; events `account-status-change-2`.
- **`POST /accounts/v4/reasons`** (`v4-post-account-reason`): security `BearerAuth`; required parameters none declared; required body fields `name`; response statuses 201, 400, 409, 500; error codes in examples `EACC0004`, `EACC0018`, `EACC0000`, `EACC0003`, `EACC9999`; events `account-reason-creation-1`.
- **`GET /accounts/v4/reasons`** (`v4-get-account-reason`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `EACC0005`, `EACC0018`, `WACC0011`, `EACC0000`, `EACC9999`; events none listed.
- **`GET /v1/accounts/{accountId}/daily-balances`** (`get-v1-account-balance`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `WBLS0005`, `WLDG0021`, `EBLS9999`; events none listed.
- **`POST /accounts/v1/accounts/programs/migration`** (`PostMigrationProgram`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `program`; response statuses 200, 400, 404, 409, 500; error codes in examples none; events `account-program-migration-1`.
- **`PUT /statements/v1/accounts/{accountId}/statements/due-date`** (`UpdateStatementsDueDate`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `id`; response statuses 200, 400, 404, 409, 500; error codes in examples `GN0001`; events none listed.
- **`PATCH /programs/v1/programs/{id}`** (`UpdateProgramInfo`): security `S2SAuthentication`; required parameters `id` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `EOA0017`, `EOA0080`, `EOA0018`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0082`, `EOA0059`, `EOA0020`, `EOA0064`, `EOA0034`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-update-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-accounts-v1-accounts` | `account-account-change-2` |
| `customerV2Post` | `account-account-owner-change-1` |
| `customerV2Post` | `account-customer-creation-1` |
| `PostMigrationProgram` | `account-program-migration-1` |
| `v4-post-account-reason` | `account-reason-creation-1` |
| `patch-accounts-v2-accounts-accountId-status` | `account-status-change-2` |
| `patch-v2-accounts-accountId-status-rollback` | `account-status-change-2` |
| `v4-post-account-status` | `account-status-creation-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `patch-acquisitions-v2-s2s-applications` | `onboarding-succeeded-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |
| `UpdateProgramInfo` | `programs-update-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/accounts-overview.md`: updatedAt 2026-09-14T22:10:12.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/accounts-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accounts-overview | `b540de821fdcc1a3…` | 2026-09-14T22:10:12.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--customers` — API reference: Core platform - Accounts — Customers
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-API-core-platform-accounts--transfer-account` — API reference: Core platform - Accounts — Transfer account
- `KU-API-core-platform-balances-and-limits--account-balances` — API reference: Core platform - Balances and limits — Account balances
- `KU-API-core-platform-balances-and-limits--related-accounts` — API reference: Core platform - Balances and limits — Related accounts
- `KU-API-platform-setup-programs--programs-part-02` — API reference: Platform setup - Programs — Programs (part 2 of 2)
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-BANK-managing-account-statuses` — Manage account statuses
- `KU-CC-accounts` — Control Center accounts: overview, management, actions and configurations
- `KU-CORE-working-with-limits-objects` — Account limits
- `KU-CRED-account-collection-status` — Account collection status
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-program-types` — Program types
