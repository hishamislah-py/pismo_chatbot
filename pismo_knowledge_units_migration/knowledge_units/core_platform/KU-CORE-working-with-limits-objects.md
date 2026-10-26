---
ku_id: KU-CORE-working-with-limits-objects
title: Account limits
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/working-with-limits-objects.md
  sha256: 879a03d4f58455a46836813edac537655fdbcb53b3fbf84d78aa61f4f53dce17
  url: https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects
  role: primary_guide
  updated_at: '2026-06-24T13:20:53.000Z'
operations:
- get-v1-account-limit
- patch-v1-account-limit
- patch-v1-account-limits
- post-acquisitions-v3-s2s-applications
- post-payments-v1-hold-funds-block
related_kus:
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-balances-and-limits--account-limits
- KU-API-core-platform-ledger--account-limits
- KU-API-core-platform-payment-methods--hold-funds
- KU-CC-accounts
- KU-CORE-program-parameters-reference-table
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Account limits

**KU ID:** `KU-CORE-working-with-limits-objects` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/working-with-limits-objects.md`:

> Every account on the Pismo platform has defined limits for different financial operations.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/working-with-limits-objects.md`: Account limits; Credit account limits; Debit account limits

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/working-with-limits-objects.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects · updatedAt: 2026-06-24T13:20:53.000Z

<!-- source:begin path=docs/core-platform/working-with-limits-objects.md part=0-end -->

# Account limits

Every account on the Pismo platform has defined limits for different financial operations.

You can [list](https://developers.pismo.io/pismo-docs/reference/get-v1-account-limit) all available limits on the account and [update](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits) some of them. You can also update certain account limits from the **Limits** tab in [Control Center](https://developers.pismo.io/pismo-docs/docs/accounts-overview-cc).

The following tables list all account limit fields available on the Pismo platform as they apply to credit and debit accounts.

<Callout icon="📘" theme="info">
  The [Update account limits (outdated)](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit) endpoint does not validate the account limit against the program’s global limit. To validate the account limit against the program’s global limit, use the [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits) endpoint.
</Callout>

# Credit account limits

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `available_credit_limit`
      </td>

      <td>
        Credit available to the customer. The platform calculates this value based on the initial `total_credit_limit` and any relevant debit and credit activity on the account.
      </td>
    </tr>

    <tr>
      <td>
        `available_monthly_credit`
      </td>

      <td>
        Deprecated
      </td>
    </tr>

    <tr>
      <td>
        `available_total_installment_credit`
      </td>

      <td>
        Amount available for installments
      </td>
    </tr>

    <tr>
      <td>
        `available_withdrawal_credit`
      </td>

      <td>
        Amount available for withdrawal. The platform calculates this value based on the initial\
        `withdrawal_credit_limit` and any debit and credit activity on the account that impacts the withdrawal credit limit.
      </td>
    </tr>

    <tr>
      <td>
        `max_credit_limit`
      </td>

      <td>
        Maximum credit limit approved for this account. Usually based on a credit analysis.

        You can [update](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits) this value as needed.

        * **Note:** This is the same thing as `granted_limit` in the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoint.
      </td>
    </tr>

    <tr>
      <td>
        `monthly_credit_limit`
      </td>

      <td>
        Deprecated
      </td>
    </tr>

    <tr>
      <td>
        `percentage_over_limit`
      </td>

      <td>
        Maximum credit limit (`max_credit_limit`) percentage made available for purchases over the account credit limit.

        You can [update](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits) this value as needed.

        * **Note:** When the credit limit is reached, the value of `available_credit_limit` field is negative in the event.
      </td>
    </tr>

    <tr>
      <td>
        `total_credit_limit`
      </td>

      <td>
        User-set total credit limit. This can be any value up to the `max_credit_limit`.

        You can [update](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits) this value as needed.

        * **Note:** This is the same thing as `limit` in the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications)  endpoint.
      </td>
    </tr>

    <tr>
      <td>
        `total_installment_credit_limit`
      </td>

      <td>
        Amount limit for installments.

        You can [update](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits) this value as needed.
      </td>
    </tr>

    <tr>
      <td>
        `withdrawal_credit_limit`
      </td>

      <td>
        Amount limit for withdrawal in credit programs. This value is calculated by multiplying `total_credit_limit`  and **Withdrawal limit percentage** (defined for the [program](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table)).
      </td>
    </tr>
  </tbody>
</Table>

# Debit account limits

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `available_credit_limit`
      </td>

      <td>
        Balance available to the customer. When there is an activity on the account, the platform determines whether to impact this limit and calculates it accordingly.
      </td>
    </tr>

    <tr>
      <td>
        `available_monthly_credit`
      </td>

      <td>
        Deprecated
      </td>
    </tr>

    <tr>
      <td>
        `available_savings_account_limit`
      </td>

      <td>
        Savings account available limit. This value is initially set at 0. When there is an activity on the account, the platform determines whether to impact this limit and calculates it accordingly.
      </td>
    </tr>

    <tr>
      <td>
        `held_funds`
      </td>

      <td>
        Funds held on the account. Usually, but not always, this occurs due to a legal action.

        This value is initially defined as `amount`  when [blocking amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-block).
      </td>
    </tr>

    <tr>
      <td>
        `monthly_credit_limit`
      </td>

      <td>
        Deprecated
      </td>
    </tr>

    <tr>
      <td>
        `total_overdraft_limit`
      </td>

      <td>
        Maximum limit for overdraft spending.

        You can [update](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits) this value as needed.
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
| `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limits` | Update account limits | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--account-limits |
| `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limit` | Update account limits (outdated) | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /payments/v1/payments/hold-funds/block` | `post-payments-v1-hold-funds-block` | Block amount | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--hold-funds |

### Operation essentials

- **`GET /v1/accounts/{accountId}/limits`** (`get-v1-account-limit`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `WLDG0020`, `WLDG0022`, `ELDG9999`; events none listed.
- **`PATCH /v1/accounts/{accountId}/limits`** (`patch-v1-account-limits`): security `BearerAuth`; required parameters `accountId` (path), `x-tenant` (header); required body fields none declared; response statuses 204, 400, 500; error codes in examples none; events `ledger-limit-changed-1`.
- **`PATCH /v1/accounts/{accountId}/limits`** (`patch-v1-account-limit`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `WLDG0021`, `WLDG0010`, `WLDG0025`, `WLDG0022`, `ELDG9999`; events `ledger-limit-changed-1`.
- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /payments/v1/payments/hold-funds/block`** (`post-payments-v1-hold-funds-block`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `account_id`, `amount`, `processing_code`; response statuses 201, 202, 400, 404, 500; error codes in examples `WP2P0000`; events `authorization-authorization-event-1`, `availables-change-available-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v1-hold-funds-block` | `authorization-authorization-event-1` |
| `post-payments-v1-hold-funds-block` | `availables-change-available-1` |
| `patch-v1-account-limit` | `ledger-limit-changed-1` |
| `patch-v1-account-limits` | `ledger-limit-changed-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/working-with-limits-objects.md`: updatedAt 2026-06-24T13:20:53.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/working-with-limits-objects.md` | whole document | https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects | `879a03d4f58455a4…` | 2026-06-24T13:20:53.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-balances-and-limits--account-limits` — API reference: Core platform - Balances and limits — Account limits
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-API-core-platform-payment-methods--hold-funds` — API reference: Core platform - Payment methods — Hold funds
- `KU-CC-accounts` — Control Center accounts: overview, management, actions and configurations
- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
