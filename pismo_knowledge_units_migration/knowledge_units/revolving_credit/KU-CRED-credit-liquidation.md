---
ku_id: KU-CRED-credit-liquidation
title: Credit liquidation
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/credit-liquidation.md
  sha256: 5247e42f0cbe9e9d1026342cd6abfe7ddcbaeb7efdc487461d5d453fbc1226a6
  url: https://developers.pismo.io/pismo-docs/docs/credit-liquidation
  role: primary_guide
  updated_at: '2026-07-30T15:57:06.000Z'
operations:
- delinquent-account-closure-get
- postFeaturesByAccountStatus
- updateProgramParamenter
related_kus:
- KU-API-revolving-credit-configurations--features-by-account-status
- KU-API-revolving-credit-delinquent-account--delinquent-account-closure
- KU-API-revolving-credit-statements--multivalue-program-parameters
- KU-CARD-multivalue-program-parameters
- KU-CRED-account-collection-status
- KU-CRED-minimum-amount-due-calculation
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Credit liquidation

**KU ID:** `KU-CRED-credit-liquidation` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/credit-liquidation.md`:

> When a customer fails to pay at least the [minimum amount due (MAD)](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation) by a specified number of days after the due date (determined by the program parameter **Number of days to block the account for unpaid statement**), the account's collection status changes to `OVERDUE`, and the account is blocked from doing cash-outs (purchases, cash withdrawals, and so on). For more information about collection statuses, refer to [Account collection status](https://developers.pismo.io/pismo-docs/docs/account-collection-status).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/credit-liquidation.md`: Credit liquidation; Closing delinquent accounts; How to manually close a delinquent account; How to automate closing delinquent accounts; Get delinquent account closure information; Late transactions; Statement cycles after a delinquent account closure; How to stop statement cycles for a canceled account

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/credit-liquidation.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/credit-liquidation · updatedAt: 2026-07-30T15:57:06.000Z

<!-- source:begin path=docs/card-issuing/credit-liquidation.md part=0-end -->

# Credit liquidation

When a customer fails to pay at least the [minimum amount due (MAD)](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation) by a specified number of days after the due date (determined by the program parameter **Number of days to block the account for unpaid statement**), the account's collection status changes to `OVERDUE`, and the account is blocked from doing cash-outs (purchases, cash withdrawals, and so on). For more information about collection statuses, refer to [Account collection status](https://developers.pismo.io/pismo-docs/docs/account-collection-status).

Some countries/regions, require you to close accounts if they remain overdue for a certain number of days. You can [close delinquent accounts manually](https://developers.pismo.io/pismo-docs/docs/credit-liquidation#how-to-manually-close-a-delinquent-account), or you can configure the Pismo platform to [close delinquent accounts automatically](https://developers.pismo.io/pismo-docs/docs/credit-liquidation#how-to-automate-closing-delinquent-accounts).

An account that is overdue, meaning the MAD has not been paid by the due date, is called a **delinquent** account.

<Callout icon="🚧" theme="warn">
  If a delinquent account is closed, it's permanently canceled and cannot be reopened.
</Callout>

# Closing delinquent accounts

When the Pismo platform closes a delinquent account, it follows these steps.

1. **Post accrued interest.** The delinquent account should have accrued some interest that is in a pending state. This interest is posted to the statement before the account is closed.
2. **Advance future installments.** If the account has installments in future statements, these are moved to the current statement. This allows the Pismo platform to sum all the debts in the current statement.
3. **Zero out the balance.** Now that all the debts are in the current statement, a credit transaction is posted that is equal to the current balance, so that the resulting balance is zero.
4. **Change account status to the final account status defined by the `DELINQUENT_ACCOUNT_CLOSURE_ACCOUNT_STATUS` multivalue program parameter.**
5. **Block account cards.** Any credit cards issued for the account must be blocked, so the customer can't keep using them.
6. **Generate a [Delinquent account closed](https://developers.pismo.io/events/docs/delinquent-account-delinquent-account-1)  event.**

<Callout icon="📘" theme="info">
  It's possible for a transaction to be authorized before a delinquent account is closed, but not posted until after it's closed. For information about how the Pismo platform handles this situation, refer to [Late transactions](https://developers.pismo.io/pismo-docs/docs/credit-liquidation#late-transactions).
</Callout>

## How to manually close a delinquent account

To manually close an account for nonpayment, use the [Close delinquent account](https://developers.pismo.io/pismo-docs/reference/delinquent-ccount-closure-post) endpoint. This endpoint starts the delinquent account closure process for one account.

The Pismo platform needs to make the following validations in order for the request be successful.

* The account must be a credit account.
* If `processing_code` is not in the body of the request, the endpoint uses the value of the [multivalue program parameter](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters) `DELINQUENT_ACCOUNT_CLOSURE_LATE_TRX_DEBIT_PROCESSING_CODE`. If `DELINQUENT_ACCOUNT_CLOSURE_LATE_TRX_DEBIT_PROCESSING_CODE` is also not set, the endpoint throws an error.
* If `reason` is not in the body of the request, the endpoint uses the value configured in the [multivalue program parameter](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters) `DELINQUENT_ACCOUNT_CLOSURE_REASON`. If this parameter is also not set, the endpoint throws an error.

If [Close delinquent account](https://developers.pismo.io/pismo-docs/reference/delinquent-ccount-closure-post) executes successfully, the account status is set to the final account status defined by the `DELINQUENT_ACCOUNT_CLOSURE_ACCOUNT_STATUS` [multivalue program parameter](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters).

## How to automate closing delinquent accounts

The Pismo platform runs a job once a day to automatically close delinquent accounts. To activate this job for your program, use the [Update multivalue program parameter values](https://developers.pismo.io/pismo-docs/reference/updateprogramparamenter) endpoint to configure the parameters with the following parameter IDs: 500 - 503, 505, 506, 508 - 511. For more details about these parameters, refer to the table in the [Multivalue program parameter](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters) guide. Note that the "Applies to" column of the table also indicates which parameters apply to credit liquidation.

If you provide a non-empty array of integers for the `DAYS_BEFORE_TO_WARNING_DELINQUENT_CLOSURE` parameter, the job generates a [Delinquent account warning](https://developers.pismo.io/events/docs/delinquent-account-delinquent-account-warning-1) event for each integer in the array. For example, if the first integer in the array is 5, the job generates a warning event 5 days before the account is due to be closed.

## Get delinquent account closure information

If an account is going through the delinquent closure process, use the [Get delinquent account closure process information](https://developers.pismo.io/pismo-docs/reference/delinquent-account-closure-get) endpoint to get the account closure information.

# Late transactions

A late transaction is a transaction that was authorized for an account before the account was closed for delinquency, but wasn't posted until after the account was closed.

When an account is closed for delinquency, the Pismo platform monitors the account for the next 365 days. If a late transaction is posted to the account during this period, the platform posts a credit or debit adjustment to bring the account balance back to zero. The platform then issues a [late\_transaction-1](https://developers.pismo.io/events/docs/delinquent-account-late-transaction-1) event.

<Callout icon="📘" theme="info">
  The count for the 365 day period begins the day after the account is closed. If a late transaction occurs on the day of closure, the Pismo platform processes it the following day.
</Callout>

# Statement cycles after a delinquent account closure

When the Pismo platform closes a delinquent account, it does not automatically stop closing statement cycles for the account. Statements continue to close on their regular schedule, even after the status changes to the final account status defined by the `DELINQUENT_ACCOUNT_CLOSURE_ACCOUNT_STATUS` multivalue program parameter.

This behavior exists because the platform monitors the account for late transactions for 365 days after closure. Statements must include late transactions as well as the corresponding reversal transactions (credits or debits that bring the balance back to zero). There is always one statement per cycle per account—multiple open statements do not accumulate.

After the 365-day monitoring period ends, the platform stops processing new transactions for the account. However, statement cycles continue to close unless you explicitly stop them.

## How to stop statement cycles for a canceled account

To stop statement cycles from closing for a canceled account, use the [Configure features by account status](https://developers.pismo.io/pismo-docs/reference/postfeaturesbyaccountstatus) endpoint. Map the account's final status in the credit liquidation process to disable the statement-closing feature.

When statement closing is disabled for an account status, the platform stops the following operations for accounts in that status:

* Statement closing events
* Statement update events
* Other balance operations tied to the statement cycle

<Callout icon="📘" theme="info">
  If the Pismo platform cannot close statement cycles for a canceled account, this means that it also can't create new statements for the account. So, the account is left with one open statment.
</Callout>

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}` | `updateProgramParamenter` | Update multivalue program parameter values | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--multivalue-program-parameters |
| `GET /v1/accounts/{account_id}` | `delinquent-account-closure-get` | Get delinquent account closure process information | `api-specs/Revolving_credit_-_Delinquent_account.yaml` | no | KU-API-revolving-credit-delinquent-account--delinquent-account-closure |
| `POST /v1/features-by-account-status` | `postFeaturesByAccountStatus` | Configure features by account status | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--features-by-account-status |

### Operation essentials

- **`PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}`** (`updateProgramParamenter`): security `BearerAuth`; required parameters `programId` (path), `parameterId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `CE0001`, `GN0001`; events none listed.
- **`GET /v1/accounts/{account_id}`** (`delinquent-account-closure-get`): security `BearerAuth`; required parameters `account_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events none listed.
- **`POST /v1/features-by-account-status`** (`postFeaturesByAccountStatus`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 500; error codes in examples `EX0001`, `WCCC011`, `GN0001`; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `delinquent-ccount-closure-post` | Close delinquent account | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `delinquent-account-delinquent-account-1` | delinquent | 1 | https://developers.pismo.io/events/docs/delinquent-account-delinquent-account-1 | 1 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/credit-liquidation.md`: updatedAt 2026-07-30T15:57:06.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 3 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.
- Operation link `delinquent-ccount-closure-post` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/credit-liquidation.md` | whole document | https://developers.pismo.io/pismo-docs/docs/credit-liquidation | `5247e42f0cbe9e9d…` | 2026-07-30T15:57:06.000Z |

## Related knowledge units

- `KU-API-revolving-credit-configurations--features-by-account-status` — API reference: Revolving credit - Configurations — Features by account status
- `KU-API-revolving-credit-delinquent-account--delinquent-account-closure` — API reference: Revolving credit - Delinquent account — Delinquent account closure
- `KU-API-revolving-credit-statements--multivalue-program-parameters` — API reference: Revolving credit - Statements — Multivalue program parameters
- `KU-CARD-multivalue-program-parameters` — Multivalue program parameters
- `KU-CRED-account-collection-status` — Account collection status
- `KU-CRED-minimum-amount-due-calculation` — Minimum amount due calculation
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
