---
ku_id: KU-BANK-restrictions
title: 'Restrictions: restrict funds, restriction management and operation blocks'
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/restrict-funds.md
  sha256: c7ee7645dd65f2cfda27fb1f46775a979200cee59deb83895011e0af90ea8ee6
  url: https://developers.pismo.io/pismo-docs/docs/restrict-funds
  role: primary_guide
  updated_at: '2026-04-24T22:11:15.000Z'
- path: docs/core-banking/restriction-management.md
  sha256: 3b95ec92bce61c676ba69e7ddfcd8e8a0f37e86233a49c622b29822d51dd5081
  url: https://developers.pismo.io/pismo-docs/docs/restriction-management
  role: primary_guide
  updated_at: '2026-04-24T21:44:58.000Z'
- path: docs/core-banking/operation-block.md
  sha256: 5ed765bdb2cecc9036fe9637b509e93479fa540b29373869aca550c8c3b5f8e5
  url: https://developers.pismo.io/pismo-docs/docs/operation-block
  role: primary_guide
  updated_at: '2026-04-24T22:11:31.000Z'
operations:
- corporate-delete-v2-operation-block-id
- corporate-get-v2-operation-blocks
- corporate-patch-v2-operation-block-id
- corporate-post-v2-operation-blocks
- corporate-v2-list-operation-blocks
- get-corporate-v1-restricted-funds
- list-corporate-v1-restricted-funds
- patch-corporate-v1-restricted-funds
- post-corporate-v1-restricted-funds
- post-dormancy-config-v2
related_kus:
- KU-API-banking-transaction-banking--dormancy
- KU-API-banking-transaction-banking--operations-blocks
- KU-API-banking-transaction-banking--restricted-funds
- KU-BANK-file-based-processing
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
grouping_rationale: Related account-restriction mechanisms.
---

# Restrictions: restrict funds, restriction management and operation blocks

**KU ID:** `KU-BANK-restrictions` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Related account-restriction mechanisms.

Scope as stated in `docs/core-banking/restrict-funds.md`:

> Restricting funds is a feature that enables financial institutions to block full or partial amounts in their clients’ accounts. This capability is essential in situations where specific funds must be excluded from the general asset pool available to unsecured creditors, ensuring they receive priority handling or special protection.

Scope as stated in `docs/core-banking/restriction-management.md`:

> The [Dormancy](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) feature includes enhanced restriction management capabilities, giving you greater flexibility and control over how account restrictions are applied when accounts transition into and out of dormant status.

Scope as stated in `docs/core-banking/operation-block.md`:

> Operation block is a core feature of the transaction banking platform that lets financial institutions temporarily restrict account activity at the program, division, or organization level.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/restrict-funds.md`: Restrict funds; Feature highlights; File-based processing; Processing codes; Example; Before restriction; After restriction
- `docs/core-banking/restriction-management.md`: Restriction management; Restrictions; Example; Default behavior; Conditional override; Impact of `reason_external_id`; Reactivation with last restriction; Example
- `docs/core-banking/operation-block.md`: Operation block; Feature highlights; Endpoints; Allowed operations

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 10 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/restrict-funds.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/restrict-funds · updatedAt: 2026-04-24T22:11:15.000Z

<!-- source:begin path=docs/core-banking/restrict-funds.md part=0-end -->

# Restrict funds

Restricting funds is a feature that enables financial institutions to block full or partial amounts in their clients’ accounts. This capability is essential in situations where specific funds must be excluded from the general asset pool available to unsecured creditors, ensuring they receive priority handling or special protection.

The solution supports multiple approaches, allowing institutions to temporarily restrict access to account balances—either in whole or in part—during judicial or regulatory events such as liquidation or receivership.

Because financial institutions need to act instantly, restricted funds empowers banks to freeze funds at a moment’s notice and later lift the restriction, restoring account access whenever required.

# Feature highlights

With restricted funds, you can transfer funds between the available balance and restricted funds in either direction. You can perform these operations through API requests or file uploads. Restricted funds can function on its own or alongside the [operation block](https://developers.pismo.io/pismo-docs/docs/operation-block) feature. In some scenarios—such as FDIC receivership—an institution might first need to block all operations across accounts within a division, program, or organization before applying specific fund restrictions.

These endpoints let you restrict and release funds.

| Endpoint                                                          | Description                                                                                  |
| :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| [Create fund restriction](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds) | Specifies the amount to be restricted from an account.                                       |
| [Get fund restriction](https://developers.pismo.io/pismo-docs/reference/get-corporate-v1-restricted-funds)     | Returns detailed information about a single restricted funds request by restricted funds ID. |
| [List fund restrictions](https://developers.pismo.io/pismo-docs/reference/list-corporate-v1-restricted-funds)  | List all restricted funds.                                                                   |
| [Release restrictions](https://developers.pismo.io/pismo-docs/reference/corporate-v2-list-operation-blocks)    | Releases fund restrictions using a restricted funds ID.                                      |

## File-based processing

Restrict funds supports file uploads, enabling you to submit a single UTF-8 NDJSON file containing multiple [restrict funds](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds) and [release restriction](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v1-restricted-funds) actions, rather than making separate API calls. For more information, refer to [ File-based processing](https://developers.pismo.io/pismo-docs/docs/file-based-processing).

# Processing codes

Each processing code represents a specific operation that impacts the balance by transferring funds between `available_balance` and `restricted_funds`. The default processing codes listed in this table define how each operation is handled internally and the type of transaction that is generated.

| Processing Code | Description                  | Balance impact | Link                                     |
| --------------- | ---------------------------- | -------------- | ---------------------------------------- |
| `PSM045`        | `RESTRICT FUNDS`             | `-1`           | Linked to PC with balance impact = `-1`. |
| `PSM046`        | `RESTRICT FUNDS CANCEL`      | `-1`           | Linked to PC with balance impact = `1`.  |
| `PSM047`        | `RELEASE RESTRICTION`        | `-1`           | Linked to PC with balance impact = `-1`. |
| `PSM048`        | `RELEASE RESTRICTION CANCEL` | `-1`           | Linked to PC with balance impact = `-1`. |

<Callout icon="📘">
  **Note**

  The values `-1` and `1` indicate the type of operation, where\
  `1` = credits (account credited).\
  `-1` = debits (account debited).
</Callout>

# Example

This example shows when a restriction is placed on your available balance, the amount is deducted from `available_balance` and transferred to `restricted_funds`.

### Before restriction

```json
{
  "account_id": "ACCOUNT-A",
  "division_code": "my-division-code",
  "program_id": 1111,
  "status": "NORMAL",
  "external_account_id": "12345679",
  "currency_numeric_code": "840",
  "currency_alphabetic_code": "USD",
  "document_number": "9999999",
  "account_creation_datetime": "2025-09-04T00:00:00.000Z",
  "available_balance": 100,
  "earmarked_balance": 0,
  "overdraft_limit": 0,
  "ledger_balance": 100,
  "book_balance": 100,
  "value_dated_balance": 100,
  "future_dated_credits_balance": 0,
  "future_dated_debits_balance": 0,
  "uncleared_funds": 0,
  "uncleared_checks_balance": 0,
  "restricted_funds": 0
}
```

### After restriction

```json
{
  "account_id": "ACCOUNT-A",
  "division_code": "my-division-code",
  "program_id": 1111,
  "status": "NORMAL",
  "external_account_id": "12345679",
  "currency_numeric_code": "840",
  "currency_alphabetic_code": "USD",
  "document_number": "9999999",
  "account_creation_datetime": "2025-09-04T00:00:00.000Z",
  "available_balance": 0,
  "earmarked_balance": 0,
  "overdraft_limit": 0,
  "ledger_balance": 100,
  "book_balance": 100,
  "value_dated_balance": 100,
  "future_dated_credits_balance": 0,
  "future_dated_debits_balance": 0,
  "uncleared_funds": 0,
  "uncleared_checks_balance": 0,
  "restricted_funds": 100
}
```

However, when the restriction is lifted, the process is reversed: funds are moved from `restricted_funds` back to `available_balance`, making them available again for transactions. This mechanism provides precise control over fund availability, supporting operational rules and client-specific configurations.
<!-- source:end -->

### Source 2: `docs/core-banking/restriction-management.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/restriction-management · updatedAt: 2026-04-24T21:44:58.000Z

<!-- source:begin path=docs/core-banking/restriction-management.md part=0-end -->

# Restriction management

The [Dormancy](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) feature includes enhanced restriction management capabilities, giving you greater flexibility and control over how account restrictions are applied when accounts transition into and out of dormant status.

These improvements enable you to define rules that adapt restrictions based on an account’s existing state, control how restrictions behave during reactivation, and ensure that transactions and dormancy checks follow your operational and compliance requirements.

Advanced restriction management includes the following features.

| Feature                                                                   | Description                                                                                       |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [Restrictions](#restrictions)                                             | Apply conditional restrictions when an account becomes dormant, based on its current restriction. |
| [Reactivation with last restriction](#reactivation-with-last-restriction) | Decide whether an account should retain its last restriction upon reactivation.                   |

These improvements make restriction handling more context‑aware and customizable, reducing the need for manual intervention and helping ensure compliance with business rules across different regions and operational scenarios. For details, refer to [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2).

These subsections describe each capability in detail, explain how it works, and provide examples for implementation.

# Restrictions

The `statuses` field in the [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) endpoint is an array of status objects that you use to define the statuses related to dormancy. Each status object contains a restrictions array field that allows you to define conditional logic that is applied when the account status changes to `DORMANT`.

The Pismo platform checks the account’s current restriction using the field `current_reason_external_id`.\
If a matching condition is found in the `restrictions` array, the account is assigned the corresponding `new_reason_external_id` when it becomes dormant. If no condition matches, the account receives the default restriction defined by `reason_external_id`.

## Example

### Default behavior

After 30 days of inactivity, an account transitions to `DORMANT` with the restriction `reason_external_id` = `CREDIT_ONLY`.

### Conditional override

If an account is `NORMAL` and restricted as `DEBIT_ONLY`, you can configure the system so that when it becomes `DORMANT`, it receives `NONE` instead of the default `CREDIT_ONLY`.

<Callout icon="📘">
  **Note**

  You can add as many restrictions as necessary to meet your business needs.
</Callout>

### Impact of `reason_external_id`

This table summarizes how `reason_external_id` impacts different financial transactions.

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

# Reactivation with last restriction

The `reactivation_with_last_restriction` field allows you to control whether an account, once reactivated from a dormant status, must retain the restriction it had before becoming dormant.

If you set `reactivation_with_last_restriction` to `true`, the account returns to `NORMAL` status with the same restriction it had before dormancy; otherwise, the account is reactivated without any previous restrictions, unless another rule applies.

## Example

If an account was `NORMAL` with a restriction of `DEBIT_ONLY` before becoming `DORMANT`, setting `reactivation_with_last_restriction` =` true` ensures it returns to `NORMAL` with `DEBIT_ONLY` after reactivation.
<!-- source:end -->

### Source 3: `docs/core-banking/operation-block.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/operation-block · updatedAt: 2026-04-24T22:11:31.000Z

<!-- source:begin path=docs/core-banking/operation-block.md part=0-end -->

# Operation block

Operation block is a core feature of the transaction banking platform that lets financial institutions temporarily restrict account activity at the program, division, or organization level.

Unlike the [restrict funds](https://developers.pismo.io/pismo-docs/docs/restrict-funds) feature, which targets specific amounts, operation block applies to all operations for entire account groups, while still permitting certain authorized activities—such as earmarks or check processing. This ensures that essential internal processes can continue even when most activities are frozen.

The feature is designed for rapid response, enabling institutions to halt all operations with a single request. It can be applied in targeted situations—such as suspending activity in specific regions—or in broader cases, such as locking down operations during a cyberattack.

# Feature highlights

Operation block includes the following features.

* Block transactions based on division, program, or organization-level definitions.
* Allow specific operations by using the allow operation field.
* Provide a comprehensive suite of APIs to create, update, list, and revoke blocks.
* Integrate seamlessly with other features, such as [restrict funds](https://developers.pismo.io/pismo-docs/docs/restrict-funds).

# Endpoints

The operation block endpoints allow clients to create, view, modify, and remove operation blocks.

| Endpoint                                                             | Description                                                        |
| -------------------------------------------------------------------- | ------------------------------------------------------------------ |
| [Create operation block](https://developers.pismo.io/pismo-docs/reference/corporate-post-v2-operation-blocks)     | Establishes an operation block for a specific division or program. |
| [List operation block](https://developers.pismo.io/pismo-docs/reference/corporate-v2-list-operation-blocks)       | Lists every operation block associated with the organization.      |
| [Get operation block details](https://developers.pismo.io/pismo-docs/reference/corporate-get-v2-operation-blocks) | Returns detailed information about a single operation block.       |
| [Update operation block](https://developers.pismo.io/pismo-docs/reference/corporate-patch-v2-operation-block-id)  | Modifies the properties of an existing operation block.            |
| [Revoke operation block](https://developers.pismo.io/pismo-docs/reference/corporate-delete-v2-operation-block-id) | Removes an operation block that was previously configured.         |

## Allowed operations

You can configure operations to be exempt from the blocking rule by specifying them in the `allowed_operations` field of [Create operation block](https://developers.pismo.io/pismo-docs/reference/corporate-post-v2-operation-blocks). When explicitly enabled, these operations bypass block enforcement, allowing for more granular control over transaction behavior during the blocking period.

The available operations are listed in the description of the `allowed_operations` field of the [Create operation block](https://developers.pismo.io/pismo-docs/reference/corporate-post-v2-operation-blocks) endpoint. For example, If you set `allowed_operations` to `EARMARK_CANCEL`, `EARMARK_RELEASE`, or `EARMARK_UPDATE`, then all earmark operations are allowed, while all other operations are blocked.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /corporate/v1/restricted-funds` | `post-corporate-v1-restricted-funds` | Create fund restriction | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `GET /corporate/v1/restricted-funds/{restrictedFundsId}` | `get-corporate-v1-restricted-funds` | Get fund restriction | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `GET /corporate/v1/restricted-funds` | `list-corporate-v1-restricted-funds` | List fund restrictions | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `GET /corporate/v2/operations-blocks` | `corporate-v2-list-operation-blocks` | List operation blocks | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--operations-blocks |
| `PATCH /corporate/v1/restricted-funds/{restrictedFundsId}` | `patch-corporate-v1-restricted-funds` | Release restriction | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `POST /corporate/v2/dormancy-config` | `post-dormancy-config-v2` | Create dormancy configuration | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `POST /corporate/v2/operations-blocks` | `corporate-post-v2-operation-blocks` | Create operation block | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--operations-blocks |
| `GET /corporate/v2/operations-blocks/{operationsBlockId}` | `corporate-get-v2-operation-blocks` | Get operation block details | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--operations-blocks |
| `PATCH /corporate/v2/operations-blocks/{operationsBlockId}` | `corporate-patch-v2-operation-block-id` | Update operation block | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--operations-blocks |
| `DELETE /corporate/v2/operations-blocks/{operationsBlockId}` | `corporate-delete-v2-operation-block-id` | Revoke operation block | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--operations-blocks |

### Operation essentials

- **`POST /corporate/v1/restricted-funds`** (`post-corporate-v1-restricted-funds`): security `BearerAuth`; required parameters none declared; required body fields `hold_method`, `amount`, `operation`; response statuses 201, 400, 401, 409, 429, 500; error codes in examples `WRFO0001`, `WRFO0006`, `WRFO0009`, `WOBK0007`, `WRFO0011`, `WRFO0012`, `WRFO0013`, `WRFO0014`, `WRFO0015`, `WRFO0016`, `WRFO0010`, `WRFO0004`, `WRFO0005`, `WRFO0003`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-restricted-funds-1`, `platform-authorization-platform-authorization-1`.
- **`GET /corporate/v1/restricted-funds/{restrictedFundsId}`** (`get-corporate-v1-restricted-funds`): security `BearerAuth`; required parameters `restrictedFundsId` (path); required body fields none declared; response statuses 200, 404, 500; error codes in examples `WRFO0007`, `ECMN9999`; events none listed.
- **`GET /corporate/v1/restricted-funds`** (`list-corporate-v1-restricted-funds`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 500; error codes in examples `ECMN9999`; events none listed.
- **`GET /corporate/v2/operations-blocks`** (`corporate-v2-list-operation-blocks`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 403, 500; error codes in examples `WCMN0004`, `ECMN9999`; events none listed.
- **`PATCH /corporate/v1/restricted-funds/{restrictedFundsId}`** (`patch-corporate-v1-restricted-funds`): security `BearerAuth`; required parameters `restrictedFundsId` (path); required body fields `amount`, `operation`; response statuses 200, 400, 409, 429, 500; error codes in examples `WRFO0001`, `WRFO0008`, `WRFO0009`, `WOBK0007`, `WRFO0011`, `WRFO0005`, `WRFO0019`, `WRFO0003`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-restricted-funds-1`, `platform-authorization-platform-authorization-1`.
- **`POST /corporate/v2/dormancy-config`** (`post-dormancy-config-v2`): security `BearerAuth`; required parameters none declared; required body fields `check_time`, `target_type`, `target_id`, `statuses`; response statuses 201, 400, 401, 403, 404, 500; error codes in examples `WDOR0001`, `WDOR0002`, `WDOR0010`, `WDOR0011`, `WDOR0005`, `WDOR0006`, `WDOR0008`, `WDOR0009`, `WDOR0004`, `WDOR0003`, `ECMN9999`; events `corporate-dormancy-config-creation-1`.
- **`POST /corporate/v2/operations-blocks`** (`corporate-post-v2-operation-blocks`): security `BearerAuth`; required parameters none declared; required body fields `description`; response statuses 201, 400, 401, 403, 409, 500; error codes in examples `WOBK0001`, `WDOR0002`, `WOBK0003`, `WOBK0004`, `WOBK0008`, `ECMN9999`; events none listed.
- **`GET /corporate/v2/operations-blocks/{operationsBlockId}`** (`corporate-get-v2-operation-blocks`): security `BearerAuth`; required parameters `operationsBlockId` (path); required body fields none declared; response statuses 200, 401, 403, 404, 500; error codes in examples `WOBK0006`, `ECMN9999`; events none listed.
- **`PATCH /corporate/v2/operations-blocks/{operationsBlockId}`** (`corporate-patch-v2-operation-block-id`): security `BearerAuth`; required parameters `operationsBlockId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `WOBK0002`, `WOBK0005`, `WOBK0009`, `WOBK0006`, `ECMN9999`; events none listed.
- **`DELETE /corporate/v2/operations-blocks/{operationsBlockId}`** (`corporate-delete-v2-operation-block-id`): security `BearerAuth`; required parameters `operationsBlockId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `WOBK0009`, `WOBK0005`, `WOBK0006`, `ECMN9999`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-corporate-v1-restricted-funds` | `account-balances-balance-change-1` |
| `post-corporate-v1-restricted-funds` | `account-balances-balance-change-1` |
| `patch-corporate-v1-restricted-funds` | `availables-change-available-1` |
| `post-corporate-v1-restricted-funds` | `availables-change-available-1` |
| `post-dormancy-config-v2` | `corporate-dormancy-config-creation-1` |
| `patch-corporate-v1-restricted-funds` | `corporate-restricted-funds-1` |
| `post-corporate-v1-restricted-funds` | `corporate-restricted-funds-1` |
| `patch-corporate-v1-restricted-funds` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v1-restricted-funds` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/restrict-funds.md`: updatedAt 2026-04-24T22:11:15.000Z.
- `docs/core-banking/restriction-management.md`: updatedAt 2026-04-24T21:44:58.000Z.
- `docs/core-banking/operation-block.md`: updatedAt 2026-04-24T22:11:31.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/restrict-funds.md` | whole document | https://developers.pismo.io/pismo-docs/docs/restrict-funds | `c7ee7645dd65f2cf…` | 2026-04-24T22:11:15.000Z |
| `docs/core-banking/restriction-management.md` | whole document | https://developers.pismo.io/pismo-docs/docs/restriction-management | `3b95ec92bce61c67…` | 2026-04-24T21:44:58.000Z |
| `docs/core-banking/operation-block.md` | whole document | https://developers.pismo.io/pismo-docs/docs/operation-block | `5ed765bdb2cecc90…` | 2026-04-24T22:11:31.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-banking-transaction-banking--operations-blocks` — API reference: Banking - Transaction banking — Operations blocks
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-BANK-file-based-processing` — File-based processing, file signature and encryption
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
