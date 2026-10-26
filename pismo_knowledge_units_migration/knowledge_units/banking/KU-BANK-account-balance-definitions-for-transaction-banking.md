---
ku_id: KU-BANK-account-balance-definitions-for-transaction-banking
title: Account balance definitions for transaction banking
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/account-balance-definitions-for-transaction-banking.md
  sha256: 76ba81c1a2825ffa3aef016b822db2dcd2f5b028b651499eab017db89e799291
  url: https://developers.pismo.io/pismo-docs/docs/account-balance-definitions-for-transaction-banking
  role: primary_guide
  updated_at: '2026-05-14T17:15:27.000Z'
operations:
- corporate-v2-post-payments
- get-account-balance-history
- get-account-balances
- get-accounts
- get-v1-account-balance
- get-v1-account-limit
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-core-platform-balances-and-limits--account-balances
- KU-API-core-platform-ledger--account-limits
- KU-CORE-working-with-limits-objects
- KU-EVT-catalogue-account
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Account balance definitions for transaction banking

**KU ID:** `KU-BANK-account-balance-definitions-for-transaction-banking` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/account-balance-definitions-for-transaction-banking.md`:

> This article explains how account balances are defined in transaction banking, which differs somewhat from the way they are defined in the core platform. On the Pismo platform, a transaction banking account is a debit account, so credit account balances are not relevant. For information about how the core platform determines account balances and limits, see [Account limits](https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/account-balance-definitions-for-transaction-banking.md`: Account balance definitions for transaction banking

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/account-balance-definitions-for-transaction-banking.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/account-balance-definitions-for-transaction-banking · updatedAt: 2026-05-14T17:15:27.000Z

<!-- source:begin path=docs/core-banking/account-balance-definitions-for-transaction-banking.md part=0-end -->

# Account balance definitions for transaction banking

This article explains how account balances are defined in transaction banking, which differs somewhat from the way they are defined in the core platform. On the Pismo platform, a transaction banking account is a debit account, so credit account balances are not relevant. For information about how the core platform determines account balances and limits, see [Account limits](https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects).

The transaction banking domain leverages the functionality of the core platform's account balance endpoints, acting like a secondary ledger by taking the existing balance data from the core platform and using it in a manner that's more tailored for transaction banking.

On the Pismo platform, the core platform and transaction banking use different endpoints to retrieve account balances.

**Core platform**

* [List account limits](https://developers.pismo.io/pismo-docs/reference/get-v1-account-limit)
* [Get daily account balance limits](https://developers.pismo.io/pismo-docs/reference/get-v1-account-balance)

**Transaction banking**

* [Get transaction banking account information](https://developers.pismo.io/pismo-docs/reference/get-accounts)
* [Get account balance](https://developers.pismo.io/pismo-docs/reference/get-account-balances)
* [Get account balance history](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history)

Here is a list of account balance definitions for transaction banking.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Term
      </th>

      <th>
        Definition
      </th>

      <th>
        Equivalent in core platform?
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Accrued remunerative interest
      </td>

      <td>
        `remunerative_interest_accrued` is the total interest amount that has accrued but has not yet been capitalized. It increases as interest accumulates and decreases when the accrued interest is added to the principal balance.
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        Available balance
      </td>

      <td>
        The available balance refers to the balance used for validating transactions.\
        The available account balance comprises the sum of the account balance and the credit limit that a customer is eligible to use.

        Available balance can be understood through this formula: `book_balance` -  `earmarked_balance` +  `overdraft_limit`.
      </td>

      <td>
        No. However it can be computed by adding  `available_credit_limit` and `total_overdraft_limit`.
      </td>
    </tr>

    <tr>
      <td>
        Book balance
      </td>

      <td>
        The book balance, also known as the consolidated balance, is the total amount of all cleared funds. This balance includes earmarked funds, but does not include uncleared funds. It consists solely of funds that the customer owns or those that  are provided by the bank. Bank-owned funds, specifically those set aside for [losses](https://www.investopedia.com/terms/n/netloss.asp), are not part of the book balance, as they are not subject to interest accrual.

        Book balance is calculated as follows: `credit_balance` -  `debit_balance`.
      </td>

      <td>
        No. However, it can be computed using core balances with the formula: `available_credit_limit` + `held_funds` + `additional_funds`.
      </td>
    </tr>

    <tr>
      <td>
        Credit balance
      </td>

      <td>
        The aggregate of the remaining balance from all the credit transactions that have been posted to the account.
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        Debit balance
      </td>

      <td>
        The total balance of debit transactions recorded for the account. Any value greater than zero indicates the use of a credit limit.
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        Earmarked balance
      </td>

      <td>
        An amount that has been set aside for future use, but has not yet been debited from the account. Earmarking reduces the available balance and increments the earmarked balance correspondingly. Despite being subtracted from the available balance, it continues to form part of the book balance.

        Only the actual execution of an earmark results in a debit. When the earmark is executed, the earmarked balance decreases, but the available balance is not affected, although the book balance does see a reduction equivalent to the executed earmark. The earmark balance is computed as follows: `SUM(earmark_balance[1],earmark_balance[2],…,earmark_balance[N])` , where `N` is the number of earmarks applied to the account.
      </td>

      <td>
        Yes. `held_funds`.
      </td>
    </tr>

    <tr>
      <td>
        Future-dated credits balance
      </td>

      <td>
        The `future_dated_credits_balance` represents the balance that are scheduled to settle on a future date after the posting date. The account’s `book_balance` is credited once the settlement occurs. This value increases when future-dated credits are posted through the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint, and decreases when those payments are either settled or canceled. The `future_dated_credits_balance` is always maintained as a positive value.
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        Future-dated debits balance
      </td>

      <td>
        The`future_dated_debits_balance` is the balance that is scheduled to settle on a future date after the initial posting date. The account’s `book_balance` is debited when settlement occurs. This balance increases when future-dated debits are posted through the[ Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint, and decreases as those payments are settled or canceled. The `future_dated_debits_balance` is always a positive value.
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        Held funds
      </td>

      <td>
        `held_funds` are funds that are temporarily restricted due to regulatory or operational requirements. These funds are unavailable for transactions and represent the total amount of earmarked or otherwise restricted balances.
      </td>

      <td>
        Yes . This is equivalent to `held_funds`.  `corporate.held_funds` = `earmarked_balance` + `held_checks_balance` + `restricted_funds`
      </td>
    </tr>

    <tr>
      <td>
        Held check balance
      </td>

      <td>
        The balance from checks that the bank considers available but temporarily holds in order to earn interest. It increases when check holds are applied and decreases when those holds are released or canceled.
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        Ledger balance
      </td>

      <td>
        The net result of all fund movements, both cleared and uncleared. It can be viewed as the cumulative effect of all postings in a given account, irrespective of their clearance status.

        The ledger balance is calculated as: `book_balance` +  `uncleared_funds`.
      </td>

      <td>
        No. Since uncleared funds are absent on the core platform, the balance for future scenarios is not applicable.
      </td>
    </tr>

    <tr>
      <td>
        Overdraft limit
      </td>

      <td>
        Assigned to the account following an initial risk analysis. As it only serves as a record of the granted limit, it isn't impacted if a transaction exceeds the available account balance. In an ideal scenario, when the account balance is insufficient, the overdraft limit is used and the available balance decreases correspondingly.
      </td>

      <td>
        Yes. This is equivalent to `total_overdraft_limit`. See  [account limits](https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects).
      </td>
    </tr>

    <tr>
      <td>
        Restricted funds
      </td>

      <td>
        The portion of an account balance blocked by regulatory or operational restrictions, such as judicial orders or FDIC receivership, and unavailable for transactions.
      </td>

      <td>
        Yes. `held_funds`.
      </td>
    </tr>

    <tr>
      <td>
        Uncleared funds
      </td>

      <td>
        The balance under consideration for future clearing. Uncleared funds are not included in either the book balance or available balance. These funds remain outside these balances until they are cleared.

        Uncleared funds have a [settlement date](https://www.investopedia.com/terms/s/settlementdateaccounting.asp), which is the date the funds are expected to be confirmed. If they are successfully cleared on the settlement date, the funds transition from the uncleared balance to the available and book balances. This balance often sees changes due to use cases such as checks.

        It's important to note that the account statement is affected by the clearance of funds on the settlement date. The relevant change is the movement of funds from the uncleared balance to the available and book balances.

        Note that `uncleared_funds` is calculated as `future_dated_credits_balance` - `future_dated_debits_balance`
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        Uncleared checks balance
      </td>

      <td>
        The total value of checks that have been posted to the account but have not yet cleared. These funds are unavailable until the checks settle on a future date after posting. Upon settlement, the amount is credited to the account’s book balance. This balance increases when checks are posted as uncleared and decreases when those checks are settled or canceled.
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        Value dated balance
      </td>

      <td>
        This balance is the basis for calculating interest accumulation. By default, it starts as the book balance value. If there are no backdated transactions, it remains equal to the book balance. However, if a backdated transaction occurs, the value dated balance is revised, and new balances for credit and debit interest are calculated.
      </td>

      <td>
        No
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /v1/accounts/{accountId}/limits` | `get-v1-account-limit` | List account limits | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |
| `GET /v1/accounts/{accountId}/daily-balances` | `get-v1-account-balance` | Get daily account balance limits | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--account-balances |
| `GET /corporate/v1/corporate-accounts/{externalAccountId}` | `get-accounts` | Get transaction banking account information | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `GET /bank-statements/v1/account-balances/{externalAccountId}` | `get-account-balances` | Get transaction banking account balance | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `GET /bank-statements/v1/account-balances/{externalAccountId}/history` | `get-account-balance-history` | Get transaction banking account balance history | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `POST /corporate/v2/payments` | `corporate-v2-post-payments` | Post payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |

### Operation essentials

- **`GET /v1/accounts/{accountId}/limits`** (`get-v1-account-limit`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `WLDG0020`, `WLDG0022`, `ELDG9999`; events none listed.
- **`GET /v1/accounts/{accountId}/daily-balances`** (`get-v1-account-balance`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `WBLS0005`, `WLDG0021`, `EBLS9999`; events none listed.
- **`GET /corporate/v1/corporate-accounts/{externalAccountId}`** (`get-accounts`): security `BearerAuth`; required parameters `externalAccountId` (path); required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples `WCAC0012`, `WDIV0002`, `WCAC0023`, `ECMN9999`; events none listed.
- **`GET /bank-statements/v1/account-balances/{externalAccountId}`** (`get-account-balances`): security `BearerAuth`; required parameters `externalAccountId` (path); required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples `CMN0002`, `WABL0003`, `WABL0002`, `WABL0001`, `CMN9999`, `EABL0001`; events none listed.
- **`GET /bank-statements/v1/account-balances/{externalAccountId}/history`** (`get-account-balance-history`): security `BearerAuth`; required parameters `externalAccountId` (path); required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples `CMN0002`, `WHIS0002`, `WHIS0003`, `WHIS0004`, `WHIS0006`, `WHIS0007`, `WHIS0008`, `WHIS0001`, `WHIS0005`, `CMN9999`, `EABL0001`; events none listed.
- **`POST /corporate/v2/payments`** (`corporate-v2-post-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`; response statuses 201, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WPMT0017`, `WPMT0011`, `WPMT0053`, `WPMT0018`, `WPMT0029`, `WPMT0030`, `WPMT0031`, `WPMT0062`, `WPMT0063`, `WCAC0010`, `WPMT0001`, `WPMT0061`, `WPMT0015`, `WPMT0016`, `WPMT0003`, `WPMT0004`, `WPMT0005`, `WPMT0006`, `WPMT0009`, `WPMT0010`, `WPMT0021`, `WEAM0008`, `WEAM0006`, `WPMT0050`, `WEAM0017`, `WEAM0019`, `WPMT0022`, `WPMT0023`, `WPMT0024`, `WPMT0025`, `WPMT0026`, `WCMN0002`, `WPMT0028`, `WPMT0045`, `WPMT0049`, `WPMT0036`, `WPMT0044`, `WPMT0051`, `WPMT0035`, `WPMT0046`, `WPMT0054`, `WPMT0055`, `WPMT0056`, `WPMT0058`, `WPMT0008`, `WPMT0014`, `WPMT0019`, `WCAC0002`, `WCAC0012`, `WPMT0002`, `WCAC0001`, `WEAM0007`, `WPMT0007`, `WPMT0052`, `WEAM0049`, `WPMT0047`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-v2-post-payments` | `account-balances-balance-change-1` |
| `corporate-v2-post-payments` | `accounting-entry-creation-1` |
| `corporate-v2-post-payments` | `availables-change-available-1` |
| `corporate-v2-post-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-payments` | `rules-evaluation-requested-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/account-balance-definitions-for-transaction-banking.md`: updatedAt 2026-05-14T17:15:27.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/account-balance-definitions-for-transaction-banking.md` | whole document | https://developers.pismo.io/pismo-docs/docs/account-balance-definitions-for-transaction-banking | `76ba81c1a2825ffa…` | 2026-05-14T17:15:27.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-core-platform-balances-and-limits--account-balances` — API reference: Core platform - Balances and limits — Account balances
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-CORE-working-with-limits-objects` — Account limits
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
