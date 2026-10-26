---
ku_id: KU-CRED-full-balance-credit-program
title: 'Full balance credit programs: concepts and configuration'
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/full-balance-credit-program.md
  sha256: d536479bb86b38cb54d6a5209709f8be49463dd5e13d2efa2f2113858fad1cd0
  url: https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program
  role: primary_guide
  updated_at: '2026-07-24T12:30:42.000Z'
- path: docs/card-issuing/creating-and-configuring-a-full-balance-credit-program.md
  sha256: 82d65ee96746b26ca8b5850c044d1b31e2e95554ea8fd20ca8b6d58f77d955a3
  url: https://developers.pismo.io/pismo-docs/docs/creating-and-configuring-a-full-balance-credit-program
  role: primary_guide
  updated_at: '2026-03-18T15:23:45.000Z'
operations:
- PatchProgramTransactionType
- PostSetupTransactionType
- createProgramTransactionType
- createTransactionCategory
- getFeaturesByAccountStatus
- patch-accounts-v2-accounts-accountId-status
- patch-v2-accounts-accountId-status-rollback
- patchFeaturesByAccountStatus
- postFeaturesByAccountStatus
- v4-post-account-status
related_kus:
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-API-core-platform-transactions--transaction-types
- KU-API-revolving-credit-configurations--features-by-account-status
- KU-API-revolving-credit-configurations--program-transaction-types
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-BANK-managing-account-statuses
- KU-CARD-program-transaction-types
- KU-CARD-transaction-categories
- KU-CC-programs
- KU-CORE-processing-codes-and-transaction-types
- KU-CRED-credit-liquidation
- KU-CRED-discharging-transactions
- KU-CRED-understanding-statements
- KU-EVT-catalogue-account
- KU-EVT-catalogue-transaction
- KU-PAY-force-operation
- KU-SUP-service-desk-requests
grouping_rationale: Concept and configuration steps.
---

# Full balance credit programs: concepts and configuration

**KU ID:** `KU-CRED-full-balance-credit-program` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Concept and configuration steps.

Scope as stated in `docs/card-issuing/full-balance-credit-program.md`:

> In a Full balance credit program, the Pismo platform provides card management and authorization integration with your card network. It also manages your customers’ balances and credit limits.

Scope as stated in `docs/card-issuing/creating-and-configuring-a-full-balance-credit-program.md`:

> Now that you understand how a Full balance credit program works, you’re ready to create and configure your own.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/full-balance-credit-program.md`: Full balance credit program; Managing credit accounts; Handling credit voucher authorization; Using configurable entities; Transaction types; Program transaction categories; Program transaction types; Handling overdue transactions; Discharging transactions; Closing an account; Definitive cancellation: Permanently stopping credit cycles; Option 1: Disable credit cycle features for the account; Option 2: Create and apply a `DEFINITIVE_CANCELLATION` account status
- `docs/card-issuing/creating-and-configuring-a-full-balance-credit-program.md`: Creating and configuring a Full balance credit program; Creating the program; Configuring the program in Control Center; Adding configurable entities; Configuring features based on account status

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 10 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/full-balance-credit-program.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program · updatedAt: 2026-07-24T12:30:42.000Z

<!-- source:begin path=docs/card-issuing/full-balance-credit-program.md part=0-end -->

# Full balance credit program

In a Full balance credit program, the Pismo platform provides card management and authorization integration with your card network. It also manages your customers’ balances and credit limits.

In a credit program, accounts are post-paid. This means that a cardholder can charge as much to their card as they like as long as the card balance remains below their credit limit. For each account, a statement is issued periodically showing relevant information about the account, such as the account balance. The statement specifies a minimum amount that the cardholder must pay by a certain date to avoid additional charges.

By the end of this guide, you should understand how a Full balance credit program manages credit accounts, including:

* How the program uses configurable entities (transaction types, program transaction categories, and program transaction types)
* How the program handles overdue transactions
* How the program discharges transactions

You should also understand how to create and configure a Full balance credit program.

# Managing credit accounts

Every transaction in a credit program is either a **debit transaction** or a **credit transaction**.

A debit transaction can be:

* A purchase with network authorization
* A debit adjustment made by a [force operation](https://developers.pismo.io/pismo-docs/docs/force-operation)
* A purchase through on-us authorization

A credit transaction can be:

* A cardholder’s  payment to their account
* A network credit voucher authorization. For more information, refer to [Handling credit voucher authorization](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#handling-credit-voucher-authorization) .
* A credit adjustment

Every credit program has a [credit card cycle](https://developers.pismo.io/pismo-docs/docs/understanding-statements#credit-card-cycles-billing-periods). This is the period of time that is covered by a single customer statement. It’s also called the **billing cycle**.

The **total amount due** or **debt** is the amount that the cardholder owes on their card. The total amount due equals the total debits minus the total credits. This is normally the only amount the cardholder needs to worry about. However, to support regulatory and tax requirements, the Pismo platform tracks balances of all individual transactions.

When the cardholder makes a payment (credit transaction), the Pismo platform uses it to reduce the balance of one or more debit transactions.

If a debit transaction becomes overdue, charges are normally applied that increase the account balance.

For each credit cycle, an account has a cycle closing date and a due date. On the morning of the **cycle closing date**, the Pismo platform  uses the credits and debits for the cycle to calculate the total amount due, minimum amount due, and any interests, taxes, or fines and posts them to the cycle statement. It then closes the cycle.

<Callout icon="🚧" theme="warn">
  Any new transactions that take place on the cycle closing date are usually posted in the next cycle, since the previous cycle is closed right at the beginning of the day. However, if a transaction happens on the cycle closing date, but before the cycle is closed, it’s posted in that cycle.
</Callout>

The **due date** is nominally the last day that the cardholder can pay the minimum amount due (MAD) before incurring charges for late payments. However, the cardholder might be granted more time to pay the MAD under the following conditions.

* You can use the **Defines the number of additional grace days granted to the program** program parameter to give the cardholder one or more additional days to pay the MAD before charges start to accrue. This value is added to the due date to get the **real due date**, which appears as a field on the statement.
* If the due date (or the real due date, if **Defines the number of additional grace days granted to the program** is set), is not a business day, the Pismo platform finds the next business day and uses that date for the real due date.

To sum up:\
real due date = due date + additional grace days + adjustment for non-business days

<Callout icon="🚧" theme="warn">
  The Pismo platform calculates charges for late payments starting from the due date, not the real due date. If the cardholder pays the MAD by the real due date, then those charges are never applied.
</Callout>

## Handling credit voucher authorization

A credit voucher is a document submitted by a merchant to an acquirer (usually a bank) as evidence of a partial or total refund of a charge. The voucher is submitted to the card network for processing, after which, it’s submitted to the Pismo platform as a network credit voucher.

By default, when a network credit voucher is received, the Pismo platform waits for clearing or Base II processing to be completed before updating the account limit or balance. If you wish to decline this recommended behavior, open a ticket with the [Pismo Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk) stating that you wish to decline it and that you would like the account limit or balance impact to occur at the time of authorization. Be aware, however, that you do this at your own discretion, based on your unique objectives, internal policies, and any legislation to which you might be subject.

## Using configurable entities

Full balance credit programs use the following configurable entities to determine how to apply charges to overdue transactions and how to discharge transaction balances:

* Transaction types
* Program transaction categories
* Program transaction types

<Image alt="An overview of how the Pismo platform uses configurable entities" align="center" className="border" border={true} src="https://files.readme.io/13ddb0a-How_the_program_uses_configurable_entities_V20.png" />

### Transaction types

A transaction type identifies a transaction as either a credit or a debit. It also determines whether the transaction should be listed on the monthly statement.

Transaction types are defined at the organization level. For more information, refer to [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) .

### Program transaction categories

Use program transaction categories to set properties such as charge order and accrual rates at the program level for a group of related transaction types. For more information, refer to [Program transaction categories](https://developers.pismo.io/pismo-docs/docs/transaction-category-structure#program-transaction-categories).

### Program transaction types

Use program transaction types to associate program transaction categories with transaction types. For more information, refer to [Program transaction types](https://developers.pismo.io/pismo-docs/docs/program-transaction-types).

## Handling overdue transactions

A transaction is overdue if it meets the following criteria.

* It has an unpaid balance.
* It appears on a statement whose due date has passed.

The real due date applies to all the debit transactions posted during that credit cycle. So, although each debit transaction posted on that statement happens at a different point in time, all of them become overdue on the same day (the day when the account becomes overdue).

The Pismo platform can apply different charges for overdue transactions. These include:

* **Refinancing interest**—Interest charged on the unpaid amount when the cardholder doesn't pay the total amount due by the real due date. Different refinancing interest charges can be configured in the program transaction category, depending on whether the cardholder pays the minimum amount due before the real due date or not. (A higher rate is normally charged if the account is overdue.)
* **Taxes**—Supports only IOF (Brazilian market).
* **Interest on cash withdrawals / bill payments**—Charged beginning on the day after the transaction date until paid off.
* **Fines**—Various fees that can be charged on overdue transactions.
* **Overdue interest**—Interest charged on an unpaid balance after the real due date when the MAD has not been paid.

<Callout icon="🚧" theme="warn">
  As explained in [Credit liquidation](https://developers.pismo.io/pismo-docs/docs/credit-liquidation), an account's collection status changes to `OVERDUE` if the MAD is not paid by the due date + **Number of days to block the account for unpaid statement** . This causes the account to be blocked.

  On the other hand, a transaction with an unpaid balance becomes overdue after the  real due date of the statement, if the MAD has not been paid. Accruals are calculated starting from the due date (which could be before the real due date). This usually happens before the account's status changes to `OVERDUE`.

  It's important not to confuse these two things. Although overdue transactions can lead to an account being blocked, they don't have to, and an account normally starts accruing overdue interest before it's actually blocked.
</Callout>

## Discharging transactions

The **discharge process** defines how a cardholder's payments are applied to transactions to reduce their debt. When a credit transaction occurs, its value is deducted from the balances of one or more debit transactions. For more information about the discharge process, refer to the [Discharging transactions](https://developers.pismo.io/pismo-docs/docs/discharging-transactions) guide.

## Closing an account

To close an account, set its account status (`status`) to a final status, such as `CANCELLED`. Once an account is closed, you can't change its status using the [Update status](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v2-accounts-accountid-status) endpoint. If you need to reopen a closed account, you must use the [Rollback status](https://developers.pismo.io/pismo-docs/reference/patch-v2-accounts-accountid-status-rollback) endpoint.

By default, closing an account does not automatically stop the Pismo platform from opening and closing credit cycles for that account. This can have a performance impact on the credit cycle, so it's a good idea to configure the platform to permanently stop the credit cycles when an account is closed. For instructions on how to do this, refer to the next section.

## Definitive cancellation: Permanently stopping credit cycles

In some business scenarios (for example, charge‑off, legal cancellation, or irreversible account termination), issuers must ensure that no new credit cycles are opened or closed for an account. There are two options for doing this.

> 🚧 Important (applies to both options)
>
> Once an account is definitively canceled, the Pismo platform permanently stops closing credit cycles for that account. This behavior is irreversible, even if the account status is later changed. This is not specific to any of the following options, but to the fact that the account reached a definitive‑cancellation state as evaluated by the platform.

### Option 1: Disable credit cycle features for the account

This is the preferred and most reliable approach. Use the [Configure features by account status](https://developers.pismo.io/pismo-docs/reference/postfeaturesbyaccountstatus) endpoint to configure the credit cycle to disable specific lifecycle features when an account reaches a given status (for example, `CANCELLED`). To fully stop credit cycles, set the following fields to `false` in the `features` object.

* `close-statements`
* `create-accruals`
* `late-payment-fee`
* `overlimit`

With these features disabled, the Pismo platform does not execute cycle logic for accounts in that status **regardless of future status changes**.

### Option 2: Create and apply a `DEFINITIVE_CANCELLATION` account status

This is the legacy approach. Option 1 is recommended. Use the [Create status](https://developers.pismo.io/pismo-docs/reference/v4-post-account-status) endpoint to define a custom account status called `DEFINITIVE_CANCELLATION` and apply it to the account. When the Pismo platform detects this status, it permanently stops cycle closing and opening.
<!-- source:end -->

### Source 2: `docs/card-issuing/creating-and-configuring-a-full-balance-credit-program.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/creating-and-configuring-a-full-balance-credit-program · updatedAt: 2026-03-18T15:23:45.000Z

<!-- source:begin path=docs/card-issuing/creating-and-configuring-a-full-balance-credit-program.md part=0-end -->

# Creating and configuring a Full balance credit program

Now that you understand how a Full balance credit program works, you’re ready to create and configure your own.

## Creating the program

Use Pismo Control Center to create your Full balance credit program. Pismo provides a program template as a starting point for a new Credit Full Balance program. Alternatively, if you already have an existing full balance credit program, you can copy it. For more information, refer to [Add programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-programs).

> 🚧
>
> You can't change the program type of an existing program, so make sure you choose credit and Full balance during the creation process (or copy a program of the correct type).

## Configuring the program in Control Center

After creating the program, use Control Center to configure it. For example, the **Transaction categories** tab enables you to specify rates for various charges. For more information, refer to [Edit program details and parameters](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters).

## Adding configurable entities

Transaction types are independent of any specific program, so you can optionally create them before creating your first program. A program transaction category, however, must be linked to a program at creation, so you have to create categories after creating their associated programs. Since program transaction types are linked to program transaction categories at creation, these entities must be created last.

* **Transaction types:** Use the [Create transaction type](https://developers.pismo.io/pismo-docs/reference/postsetuptransactiontype) endpoint. In the request, you must specify whether the transaction type is a credit or debit. You also must specify whether the associated  transactions should appear on the customer’s statement.
* **Program transaction categories:** Use the [Create program transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory) endpoint. You must set values for the various rates in the request. You also have the option of specifying a charge order.
* **Program transaction types:** Use the [Create program transaction type](https://developers.pismo.io/pismo-docs/reference/createprogramtransactiontype) endpoint, passing the program ID as a query parameter and the IDs of the regular transaction type and the program transaction category (`transaction_category_id`) as body parameters. You also have the option of specifying a charge order as a body parameter. This charge order, if present, takes precedence over a charge order defined in the program transaction category. Once a program transaction type is created, you can modify its settings using the [Update program transaction type](https://developers.pismo.io/pismo-docs/reference/patchprogramtransactiontype) endpoint.

## Configuring features based on account status

You can prevent the Pismo platform from performing certain actions on an account if the account has a specified [account status](https://developers.pismo.io/pismo-docs/docs/managing-account-statuses). These actions include:

* Closing the billing cycle
* Charging late payment fees
* Charging overlimit fees

For example, you could instruct the platform not to close an account if its status is `BLOCKED`.

Use the following endpoints to set up and manage this behavior.

* [Configure features by account status](https://developers.pismo.io/pismo-docs/reference/postfeaturesbyaccountstatus)
* [List features by account status](https://developers.pismo.io/pismo-docs/reference/getfeaturesbyaccountstatus)
* [Update features by account status](https://developers.pismo.io/pismo-docs/reference/patchfeaturesbyaccountstatus)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PATCH /accounts/v2/accounts/{accountId}/status` | `patch-accounts-v2-accounts-accountId-status` | Update status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `PATCH /accounts/v2/accounts/{accountId}/status/rollback` | `patch-v2-accounts-accountId-status-rollback` | Roll back status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `POST /v1/features-by-account-status` | `postFeaturesByAccountStatus` | Configure features by account status | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--features-by-account-status |
| `POST /accounts/v4/statuses` | `v4-post-account-status` | Create status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `POST /v1/transaction-types` | `PostSetupTransactionType` | Create transaction type | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `POST /statements-v2/v1/transactions-categories` | `createTransactionCategory` | Create program transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `POST /v1/programs/{programId}/program-transaction-types` | `createProgramTransactionType` | Create program transaction type | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-transaction-types |
| `PATCH /v1/programs/{programId}/transaction-types/{transactionTypeId}` | `PatchProgramTransactionType` | Update program transaction type description | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `GET /v1/features-by-account-status` | `getFeaturesByAccountStatus` | List features by account status | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--features-by-account-status |
| `PATCH /v1/features-by-account-status` | `patchFeaturesByAccountStatus` | Update features by account status | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--features-by-account-status |

### Operation essentials

- **`PATCH /accounts/v2/accounts/{accountId}/status`** (`patch-accounts-v2-accounts-accountId-status`): security `BearerAuth`; required parameters `accountId` (path); required body fields `status`; response statuses 204, 400, 404, 500; error codes in examples none; events `account-status-change-2`.
- **`PATCH /accounts/v2/accounts/{accountId}/status/rollback`** (`patch-v2-accounts-accountId-status-rollback`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 204, 404, 500; error codes in examples none; events `account-status-change-2`.
- **`POST /v1/features-by-account-status`** (`postFeaturesByAccountStatus`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 500; error codes in examples `EX0001`, `WCCC011`, `GN0001`; events none listed.
- **`POST /accounts/v4/statuses`** (`v4-post-account-status`): security `BearerAuth`; required parameters none declared; required body fields `name`, `allowed_operations`; response statuses 201, 400, 409, 500; error codes in examples `EACC0004`, `EACC0018`, `EACC0000`, `EACC0003`, `EACC9999`; events `account-status-creation-1`.
- **`POST /v1/transaction-types`** (`PostSetupTransactionType`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `description`, `credit`, `posted_transaction`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00005`, `WTRC05001`, `WTRC08001`, `ETRC00001`; events `transaction-types-creation-1`.
- **`POST /statements-v2/v1/transactions-categories`** (`createTransactionCategory`): security `BearerAuth`; required parameters `Authorization` (header), `program-id` (header); required body fields `default_rate`, `fine_rate`, `minimum_value`, `overdue_rate_after_due_date`, `refinancing_rate_after_due_date`; response statuses 201, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`POST /v1/programs/{programId}/program-transaction-types`** (`createProgramTransactionType`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 201, 400, 404, 500; error codes in examples `EX0001`, `EX0002`; events none listed.
- **`PATCH /v1/programs/{programId}/transaction-types/{transactionTypeId}`** (`PatchProgramTransactionType`): security `BearerAuth`; required parameters `programId` (path), `transactionTypeId` (path); required body fields `description`; response statuses 200, 400, 404, 500; error codes in examples `WTRC00003`, `WTRC00005`, `WTRC03001`, `ETRC03002`; events none listed.
- **`GET /v1/features-by-account-status`** (`getFeaturesByAccountStatus`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EX0001`, `EX0004`, `GN0001`; events none listed.
- **`PATCH /v1/features-by-account-status`** (`patchFeaturesByAccountStatus`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EX0001`, `WCCC011`, `GN0001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-accounts-v2-accounts-accountId-status` | `account-status-change-2` |
| `patch-v2-accounts-accountId-status-rollback` | `account-status-change-2` |
| `v4-post-account-status` | `account-status-creation-1` |
| `PostSetupTransactionType` | `transaction-types-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/full-balance-credit-program.md`: updatedAt 2026-07-24T12:30:42.000Z.
- `docs/card-issuing/creating-and-configuring-a-full-balance-credit-program.md`: updatedAt 2026-03-18T15:23:45.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/full-balance-credit-program.md` | whole document | https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program | `d536479bb86b38cb…` | 2026-07-24T12:30:42.000Z |
| `docs/card-issuing/creating-and-configuring-a-full-balance-credit-program.md` | whole document | https://developers.pismo.io/pismo-docs/docs/creating-and-configuring-a-full-balance-credit-program | `82d65ee96746b26c…` | 2026-03-18T15:23:45.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-revolving-credit-configurations--features-by-account-status` — API reference: Revolving credit - Configurations — Features by account status
- `KU-API-revolving-credit-configurations--program-transaction-types` — API reference: Revolving credit - Configurations — Program transaction types
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-BANK-managing-account-statuses` — Manage account statuses
- `KU-CARD-program-transaction-types` — Program transaction types
- `KU-CARD-transaction-categories` — Transaction categories
- `KU-CC-programs` — Control Center programs: create, edit, clone, export and import
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CRED-credit-liquidation` — Credit liquidation
- `KU-CRED-discharging-transactions` — Discharging transactions and the default discharge process
- `KU-CRED-understanding-statements` — Understanding statements
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-PAY-force-operation` — Force operation
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
