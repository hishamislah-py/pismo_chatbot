---
ku_id: KU-BANK-managing-account-statuses
title: Manage account statuses
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/managing-account-statuses.md
  sha256: 46a04a8a9adbb73a77eb4c052e692a838ec5eff2caecc49912bb3dbe4c4ce6fe
  url: https://developers.pismo.io/pismo-docs/docs/managing-account-statuses
  role: primary_guide
  updated_at: '2026-04-28T18:52:12.000Z'
operations:
- get-accounts-v1-accounts-status-reasons
- patch-accounts-accountId-status-rollback-v2
- patch-accounts-v2-accounts-accountId-status
- patch-dormancy-config-v2
- post-accounts-accountId-close
- post-dormancy-config-v2
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--dormancy
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-CORE-accounts-overview
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
grouping_rationale: single source page
---

# Manage account statuses

**KU ID:** `KU-BANK-managing-account-statuses` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/managing-account-statuses.md`:

> Managing account statuses within the Pismo platform involves configuring and mapping account status change reasons to your organization. Key statuses include `INACTIVE`, `DORMANT`, and `UNCLAIMED`, which require specific change reasons to function correctly. Dormancy types are defined based on the period of inactivity and are set at the division level.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/managing-account-statuses.md`: Manage account statuses; Account statuses common to all accounts; Manage inactive/dormant transaction banking accounts; Account statuses specific to transaction banking accounts; Configure dormancy statuses and change reasons; Account status change reasons must be mapped to the organization (Org) during its setup. For the `INACTIVE`, `DORMANT`, and `UNCLAIMED` statuses to function correctly, they must be assigned specific account status change reasons. Note that there is no standard behavior predefined for these statuses at the Org level.; Update account status and reasons; Rollback account; Close account

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/managing-account-statuses.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/managing-account-statuses · updatedAt: 2026-04-28T18:52:12.000Z

<!-- source:begin path=docs/core-banking/managing-account-statuses.md part=0-end -->

# Manage account statuses

Managing account statuses within the Pismo platform involves configuring and mapping account status change reasons to your organization. Key statuses include `INACTIVE`, `DORMANT`, and `UNCLAIMED`, which require specific change reasons to function correctly. Dormancy types are defined based on the period of inactivity and are set at the division level.

Account status changes impact operational permissions, such as allowing or restricting debit and credit postings, as well as forced credits and debits. To ensure accurate processing, it's crucial to validate and configure mappings during the organization's setup. This includes setting up fee configurations and deductions. Proper management of account statuses helps maintain efficient and accurate tracking of account activities within Pismo platform.

# Account statuses common to all accounts

The `status` field for any account can contain one of the following values:

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
        `NORMAL`
      </td>

      <td>
        Account is active. Allows both cash-in and cash-out, based on the limits of thes account.
      </td>
    </tr>

    <tr>
      <td>
        `BLOCKED`
      </td>

      <td>
        Account is blocked. Allows cash-in only.\
        This is a temporary status, so it is possible to change it to `NORMAL` or `CANCELLED` when needed (details below).
      </td>
    </tr>

    <tr>
      <td>
        `CANCELLED`
      </td>

      <td>
        Account is cancelled. No cash-in or cash-out allowed.\
        This is a final status, so you must use a different endpoint to roll back this status (details below).
      </td>
    </tr>
  </tbody>
</Table>

You can use the [Update status](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v2-accounts-accountid-status) endpoint to change the account status to one of the values described previously. See [Account status](https://developers.pismo.io/pismo-docs/docs/accounts-overview#account-status) for more information.

# Manage inactive/dormant transaction banking accounts

Transaction banking accounts come with extra statuses to help you manage inactive or dormant accounts. An account becomes inactive or dormant when no transactions occur for a specific period.

The Pismo platform allows you to define three types of dormancy based on how long the account has been inactive. These dormancy types are set at the division level, which is explained in the following sections.

## Account statuses specific to transaction banking accounts

The additional account statuses for transaction banking are as follows:

* `INACTIVE`
* `DORMANT`
* `UNCLAIMED`

For transaction banking accounts in any inactive status, a customer-initiated transaction reactivates the account and restores its status to `NORMAL`. Account status reasons help control the types of transactions accepted into the account, thereby activating it.

An automated process within the Pismo platform checks for accounts that have been idle for a specified length of time. When such an account is found, its status is changed to one of the predefined values. Typically, an idle account first becomes `INACTIVE`. If it remains `INACTIVE` for a prolonged period, it changes to `DORMANT`. If it stays `DORMANT` even longer, its status changes to `UNCLAIMED`. The duration an account must remain idle before each status change depends on your custom settings. You can configure the inactivity period, the resulting status, and the reason for the status change after the specified length of time.

## Configure dormancy statuses and change reasons

The available **account status change reasons** for this feature are as follows:

| Account status reason                | Description                                                                              |
| ------------------------------------ | ---------------------------------------------------------------------------------------- |
| `DEBIT_ONLY`                         | Only debits are allowed.                                                                 |
| `CREDIT_ONLY`                        | Only credits are allowed.                                                                |
| `ALL`                                | Any transaction is allowed.                                                              |
| `NONE`                               | No transactions are allowed, with the exception of forced operations, which are allowed. |
| `ALL_NO_FORCE_ALLOWED`               | Any transaction is allowed, except the forced transactions (credit or debit).            |
| `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED` | Only credits and force credits are allowed.                                              |
| `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED` | Only debits and force debits are allowed.                                                |
| `FORCE_CREDIT_ONLY`                  | Debits, credits, and force debits are not allowed.                                       |
| `FORCE_DEBIT_ONLY`                   | Debits, credits, and force credits are not allowed.                                      |
| `NONE_NO_FORCE_ALLOWED`              | Debits, credits, force debits, and force credits are not allowed                         |

These parameters must be applied by division using the [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) endpoint. Instead of providing the reason, you must pass an `reason_external_id`. To obtain a list of these IDs, use [List account status reasons](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts-status-reasons). The following code snippet demonstrates the type of response you should receive when you call [List account status reasons](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts-status-reasons).

<details>
  <summary style={{ fontSize: "18px", fontWeight: "bold" }}>Sample response</summary>

  ```json
  {
      "code": "ALL",
      "reason_id": 1619,
      "show_user": false,
      "description": "Any",
      "account_status_id": 2421
  },
  {
      "code": "ALL_NO_FORCE_ALLOWED",
      "reason_id": 1440,
      "show_user": false,
      "description": "Any - No Force Allowed",
      "account_status_id": 2421
  },
  {
      "code": "CREDIT_ONLY",
      "reason_id": 1618,
      "show_user": false,
      "description": "Credit Only",
      "account_status_id": 2421
  },
  {
      "code": "CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED",
      "reason_id": 1438,
      "show_user": false,
      "description": "Credit Only - No Force Debit Allowed",
      "account_status_id": 2421
  },
  {
      "code": "DEBIT_ONLY",
      "reason_id": 1421,
      "show_user": false,
      "description": "Debit Only",
      "account_status_id": 1316
  },
  {
      "code": "DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED",
      "reason_id": 1439,
      "show_user": false,
      "description": "Debit Only - No Force Credit Allowed",
      "account_status_id": 2421
  },
  {
      "code": "FORCE_CREDIT_ONLY",
      "reason_id": 2774,
      "show_user": false,
      "description": "Force Credit Only - No Force Debit Allowed",
      "account_status_id": 1316
  },
  {
      "code": "FORCE_DEBIT_ONLY",
      "reason_id": 2775,
      "show_user": false,
      "description": "Force Debit Only - No Force Credit Allowed",
      "account_status_id": 1316
  },
  {
      "code": "NONE",
      "reason_id": 1620,
      "show_user": false,
      "description": "Manual",
      "account_status_id": 2421
  },
  {
      "code": "NONE_NO_FORCE_ALLOWED",
      "reason_id": 1441,
      "show_user": false,
      "description": "Manual - No Force Allowed",
      "account_status_id": 2421
  }
  ```
</details>

<Callout icon="📘" theme="info">
  **Notes**

  * If a transaction is posted and the account status is either `INACTIVE`, `DORMANT`, or `UNCLAIMED`, the account's status reverts to `NORMAL` unless the processing code for the account is listed in `dormant_processing_code` in [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2).
  * When you use the [Update dormancy configuration](https://developers.pismo.io/pismo-docs/reference/patch-dormancy-config-v2) endpoint, an account enters the dormant state (`INACTIVE`, `DORMANT`, or `UNCLAIMED`) only after the specified number of days has elapsed without any transactions. The following code demonstrates how you pass the values for these parameters in the body of the [Update dormancy configuration](https://developers.pismo.io/pismo-docs/reference/patch-dormancy-config-v2) request:
</Callout>

<details>
  <summary style={{ fontSize: "18px", fontWeight: "bold" }}>Sample request</summary>

  ```json
  {
      "check_time": "09:00:00",
      "target_type": "DIVISION",
      "target_id": "{{division.city.code}}",
      "statuses": [
          {
              "status": "DORMANT",
              "reason_external_id": "CREDIT_ONLY",
              "days": 1,
              "reactivation_with_last_restriction": true,
              "restrictions": [
                  {
                      "current_reason_external_id": "DEBIT_ONLY",
                      "new_reason_external_id": "CREDIT_ONLY"
                  }
              ]
          }
      ],
      "dormant_processing_codes": [
          "220040"
      ],
      "deny_forced_transaction_reactivation": true
  }
  ```
</details>

The following table outlines the relationship between various account status change reasons and the corresponding permissions for operations on those accounts. It specifies whether debit and credit postings are allowed, as well as whether forced credits and debits are permitted under each account status type. This detailed breakdown helps in understanding the operational capabilities associated with different account statuses.

| `reason_external_id`                 | Debit posting allowed | Credit posting allowed | Forced credit allowed | Forced debit allowed |
| :----------------------------------- | :-------------------- | :--------------------- | :-------------------- | :------------------- |
| `DEBIT_ONLY`                         | ✔                     |                        | ✔                     | ✔                    |
| `CREDIT_ONLY`                        |                       | ✔                      | ✔                     | ✔                    |
| `ALL`                                | ✔                     | ✔                      | ✔                     | ✔                    |
| `NONE`                               |                       |                        | ✔                     | ✔                    |
| `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED` |                       | ✔                      | ✔                     |                      |
| `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED` | ✔                     |                        |                       | ✔                    |
| `ALL_NO_FORCE_ALLOWED`               | ✔                     | ✔                      |                       |                      |
| `NONE_NO_FORCE_ALLOWED`              |                       |                        |                       |                      |
| `FORCE_CREDIT_ONLY`                  |                       |                        | ✔                     |                      |
| `FORCE_DEBIT_ONLY`                   |                       |                        |                       | ✔                    |

### Account status change reasons must be mapped to the organization (Org) during its setup. For the `INACTIVE`, `DORMANT`, and `UNCLAIMED` statuses to function correctly, they must be assigned specific account status change reasons. Note that there is no standard behavior predefined for these statuses at the Org level.

Here is the standard account status behavior, note that the account status reasons always override the standard behavior of account status.

| Status      | Debit posting allowed | Credit posting allowed | Forced credit allowed | Forced debit allowed |
| :---------- | :-------------------- | :--------------------- | :-------------------- | :------------------- |
| `NORMAL`    | ✔                     | ✔                      | ✔                     | ✔                    |
| `BLOCKED`   |                       | ✔                      | ✔                     | ✔                    |
| `CANCELED`  |                       |                        |                       |                      |
| `DORMANT`   |                       | ✔                      | ✔                     | ✔                    |
| `INACTIVE`  | ✔                     | ✔                      | ✔                     | ✔                    |
| `UNCLAIMED` |                       |                        |                       |                      |

# Update account status and reasons

To update the account status or reason, please note the following:

* **Final Status Restrictions**: Changes cannot be made if the account is currently in a final status, such as `UNCLAIMED` or `CANCELED`. To modify an account in a final status, you must use the [Roll back transaction banking account status](https://developers.pismo.io/pismo-docs/reference/patch-accounts-accountid-status-rollback-v2) endpoint.
* **Change to Final Status**: It is not possible to change an account status to a final status or to one that is specified in the dormancy configuration the account adheres to. If you intend to transition an account to a final status, use the [Close transaction banking account](https://developers.pismo.io/pismo-docs/reference/post-accounts-accountid-close) endpoint.

# Rollback account

To rollback an account, it is important to consider a few key points. First, the account's current status must be a final status. Second, while you are allowed to choose a new status and reason for the account during the rollback, this new status cannot be a final status or a dormant status.

# Close account

To close an account, several validation criteria must be met. The account must not have any scheduled payments, and there should be no balances in the account, whether earmarked or book balance.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PATCH /accounts/v2/accounts/{accountId}/status` | `patch-accounts-v2-accounts-accountId-status` | Update status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `POST /corporate/v2/dormancy-config` | `post-dormancy-config-v2` | Create dormancy configuration | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `GET /accounts/v1/accounts-status/reasons` | `get-accounts-v1-accounts-status-reasons` | List status reasons V1 (deprecated) | `api-specs/Core_platform_-_Accounts.yaml` | **yes** | KU-API-core-platform-accounts--statuses-and-reasons |
| `PATCH /corporate/v2/dormancy-config/{dormancyConfigId}` | `patch-dormancy-config-v2` | Update dormancy configuration | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback` | `patch-accounts-accountId-status-rollback-v2` | Roll back transaction banking account status | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /corporate/v1/corporate-accounts/{externalAccountId}/close` | `post-accounts-accountId-close` | Close transaction banking account | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |

### Operation essentials

- **`PATCH /accounts/v2/accounts/{accountId}/status`** (`patch-accounts-v2-accounts-accountId-status`): security `BearerAuth`; required parameters `accountId` (path); required body fields `status`; response statuses 204, 400, 404, 500; error codes in examples none; events `account-status-change-2`.
- **`POST /corporate/v2/dormancy-config`** (`post-dormancy-config-v2`): security `BearerAuth`; required parameters none declared; required body fields `check_time`, `target_type`, `target_id`, `statuses`; response statuses 201, 400, 401, 403, 404, 500; error codes in examples `WDOR0001`, `WDOR0002`, `WDOR0010`, `WDOR0011`, `WDOR0005`, `WDOR0006`, `WDOR0008`, `WDOR0009`, `WDOR0004`, `WDOR0003`, `ECMN9999`; events `corporate-dormancy-config-creation-1`.
- **`GET /accounts/v1/accounts-status/reasons`** (`get-accounts-v1-accounts-status-reasons`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 404, 500; error codes in examples none; events none listed.
- **`PATCH /corporate/v2/dormancy-config/{dormancyConfigId}`** (`patch-dormancy-config-v2`): security `BearerAuth`; required parameters `dormancyConfigId` (path); required body fields none declared; response statuses 204, 400, 401, 403, 404, 500; error codes in examples `WDOR0001`, `WDOR0002`, `WDOR0010`, `WDOR0011`, `WDOR0005`, `WDOR0006`, `WDOR0009`, `WDOR0007`, `ECMN9999`; events `corporate-dormancy-config-change-1`.
- **`PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback`** (`patch-accounts-accountId-status-rollback-v2`): security `BearerAuth`; required parameters `externalAccountId` (path); required body fields none declared; response statuses 204, 400, 404, 422, 500; error codes in examples `WCAC0012`, `WCAC0013`, `WCAC0005`, `WCAC0034`, `WCAC0037`, `WCAC0036`, `WCAC0020`, `WCAC0020`, `WCAC0021`, `WCAC0038`, `ECMN9999`; events `account-status-change-2`.
- **`POST /corporate/v1/corporate-accounts/{externalAccountId}/close`** (`post-accounts-accountId-close`): security `BearerAuth`; required parameters `externalAccountId` (path); required body fields none declared; response statuses 204, 400, 401, 403, 422, 500; error codes in examples `WCAC0012`, `WCAC0018`, `WCAC0019`, `WCAC0028`, `WCAC0029`, `WCAC0035`, `WCAC0040`, `WCAC0045`, `ECMN9999`; events `account-status-change-2`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-accounts-accountId-status-rollback-v2` | `account-status-change-2` |
| `patch-accounts-v2-accounts-accountId-status` | `account-status-change-2` |
| `post-accounts-accountId-close` | `account-status-change-2` |
| `patch-dormancy-config-v2` | `corporate-dormancy-config-change-1` |
| `post-dormancy-config-v2` | `corporate-dormancy-config-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/managing-account-statuses.md`: updatedAt 2026-04-28T18:52:12.000Z.
- Links to `get-accounts-v1-accounts-status-reasons`, which is marked `deprecated: true` in `api-specs/Core_platform_-_Accounts.yaml`.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/managing-account-statuses.md` | whole document | https://developers.pismo.io/pismo-docs/docs/managing-account-statuses | `46a04a8a9adbb73a…` | 2026-04-28T18:52:12.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-CORE-accounts-overview` — Accounts
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
