---
ku_id: KU-CORE-program-limits
title: Program limits
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/program-limits.md
  sha256: e1876c8779827fff23c66c8623389441f5c19539c1b85258a8ef6ad490368f20
  url: https://developers.pismo.io/pismo-docs/docs/program-limits
  role: primary_guide
  updated_at: '2026-04-15T19:59:26.000Z'
operations:
- get-v1-global-configs
- patch-v1-account-limit
- patch-v1-account-limits
- patch-v1-global-configs-program-programId
- post-acquisitions-v3-s2s-applications
- post-v1-global-configs
related_kus:
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-balances-and-limits--account-limits
- KU-API-core-platform-balances-and-limits--program-limits
- KU-API-core-platform-ledger--account-limits
- KU-CC-programs
- KU-CORE-program-parameters-reference-table
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Program limits

**KU ID:** `KU-CORE-program-limits` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/program-limits.md`:

> The Pismo platform allows you to control the total granted limit distributed across all accounts within a program. This feature ensures that the program-level global limit is enforced during operations that increase or decrease limit values, such as account creation, limit updates, or program transfers.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/program-limits.md`: Program limits; Create program limit configuration; Configure program parameter; Check program limits; Update program limit; Create account; Update account limits; Increase account limit; Decrease account limit; Known restrictions; Common errors

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/program-limits.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/program-limits · updatedAt: 2026-04-15T19:59:26.000Z

<!-- source:begin path=docs/core-platform/program-limits.md part=0-end -->

# Program limits

The Pismo platform allows you to control the total granted limit distributed across all accounts within a program. This feature ensures that the program-level global limit is enforced during operations that increase or decrease limit values, such as account creation, limit updates, or program transfers.

To enable this feature, perform the following steps.

1. [Configure program limit](https://developers.pismo.io/pismo-docs/docs/program-limits#create-program-limit-configuration) to set the maximum granted limit allowed for a program via Control Center or API.
2. [Configure program parameter](https://developers.pismo.io/pismo-docs/docs/program-limits#configure-program-parameter) **Program\_limit\_validation** via Control Center or API.

Once these configurations are enabled, the platform activates validation for specific workflows, including account creation and account transfer between programs. Any time the configured global program limit of a program may be impacted by these operations, the Pismo platform performs limit validation and stores the limit in the program accumulator.

Workflows that may increase the accumulated value of a program—such as account creation, account transfer to another program, and account limit increase—require validation to ensure the program’s global limit is not exceeded.

Workflows that decrease the account limit do not require validation against the program limit. However, it must be considered for updating the program accumulator, as it reduces the total limit value.

<Callout icon="🚧" theme="warn">
  The Pismo platform does not support retroactive limit validation for account operations that occurred before the global program limits were configured. Only accounts that are created, transferred to another program, or updated with new limits after these configurations are enabled are included in the program accumulator.  Refer to [Known restrictions](https://developers.pismo.io/pismo-docs/docs/program-limits#known-restrictions)  for details.
</Callout>

# Create program limit configuration

To define a global granted limit at the program level via API, call the [Configure program limit](https://developers.pismo.io/pismo-docs/reference/post-v1-global-configs) endpoint. Consider the following request example.

```json
{
  "level": "PROGRAM",  
  "program_id": 123,
  "limits": {
    "max_credit_limit": {
      "value": 100000,
      "is_active": true
    }
  }
}
```

The maximum credit limit  `value` represents the sum of all account limits within the program, regardless of each account’s status. If you want to exclude accounts with specific account status from being counted toward the program limit, you must set those accounts' limit to zero. This ensures that only accounts with active granted limits contribute to the program’s total.

You can also use Control Center to define the global limit. For more information, refer to [Edit programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters).

# Configure program parameter

To enable validation of account limits against the program-level global limit, you must enable a specific parameter at the program level. Only accounts associated with a program where the parameter **Program\_limit\_validation** is enabled will be subject to limit validation. If the parameter is not enabled, account creation and transfers will not trigger checks against the program-level limit.

To configure this program parameter via API, use the [Update program parameters](https://developers.pismo.io/pismo-docs/reference/post-v1-global-configs)  endpoint.

In Control Center, if you define and enable a global limit, the **Program\_limit\_validation** parameter is automatically set to **true**. For more information, refer to [Edit programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters).

Once this parameter is enabled, the platform will validate account creation and program transfers against the program’s configured global limit.

For more details on program parameters, refer to the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide.

# Check program limits

To check the configured global limit granted for a program along with its current accumulated limit value via API, call the [Get program limits](https://developers.pismo.io/pismo-docs/reference/get-v1-global-configs)  endpoint. Consider the following response example.

```json
[
    {
        "level": "PROGRAM",
        "program_id": 28134,
        "limits": {
            "max_credit_limit": {
                "value": 100000,
                "is_active": true,
                "accumulated": 5000
            }
        }
    }
] 
```

In this example, the program with ID 28134 has a maximum credit limit of $100000, is currently active, and has an accumulated limit value of $5000.

You can also use Control Center to check the global limit. For more information, refer to [Edit programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters).

# Update program limit

To update the global granted limit for a program or to activate/deactivate the limit via API, call the [Update program limit](https://developers.pismo.io/pismo-docs/reference/patch-v1-global-configs-program-programid)  endpoint. Consider the following request example.

```json
{
  "limits": {
    "max_credit_limit": {
      "value": 100500,
      "is_active": true
    }
  }
}
```

This request updates the maximum credit limit to $100500 for the specified program and ensures the limit is active. To deactivate the limit, set `is_active` to `false`.

You can also use Control Center to update the global limit. For more information, refer to [Edit programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters).

# Create account

When you create a new account in a program that has a global limit configured and the **Program\_limit\_validation** parameter set, the platform validates whether the requested account limit complies with the program’s available limit. If the program has sufficient available limit, the platform successfully creates the account and increases the program accumulator by the granted limit of the new account.

If the program limit is insufficient, the platform rejects the request, doesn't create the account, and doesn't change the program accumulator value.

To create a new account, call the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoint. Consider the following request example.

```json
{
    "application": {
        "submit": true,
        "due_date": 99999,
        "program_id": 12345,
        "applicant": {
            "account": {
                "limit": "10",
                "granted_limit":10
            },
            "customer": {
                "nickname": "Test",
                "printedName": "Test name 1"
            },
            "personal": {
                "name": "Test name 1",
                "printedNamelength": 30
            },
            "birthDate": "25/07/1996",
            "document_number": "999999999915"
        }
    }
} 
```

The value provided in the `granted_limit` field is used both for validation and for accumulation at the program level.

<Callout icon="📘" theme="info">
  If the `granted_limit` value falls outside the range defined by the program’s **Minimum credit limit** and **Maximum credit limit** parameters, the platform automatically adjusts this value to the nearest valid value (either the minimum or maximum).
</Callout>

For more details, refer to [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) for full documentation on account creation.

# Update account limits

Use the [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits) endpoint to increase or decrease limits for a specific account. This endpoint triggers validation against the global program limit configured in the [Configure program limit](https://developers.pismo.io/pismo-docs/reference/post-v1-global-configs) endpoint.

You can also use Control Center to update account limits. For more information, refer to [Edit programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters).

<Callout icon="📘" theme="info">
  Updating limits through the outdated [Update account limits (outdated)](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit) endpoint does not trigger validation against the program limit. However, if the program limit is configured, the accumulator will still be updated accordingly.
</Callout>

## Increase account limit

When there is an increase to the credit limit of an account that belongs to a program with an active global limit, the platform validates whether sufficient limit is available at the program level. If the request is approved, the difference between the old and new account limits is added to the program accumulator.

To perform this operation with validation against the program limit, call the [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits) endpoint.

```json
{
	"max_credit_limit": 1500
} 
```

## Decrease account limit

When there is a decrease in the credit limit of an account that belongs to a program with a configured global limit, the platform reduces the program accumulator by the difference between the previous and the new account limit.

To perform this operation with validation against the program limit, call the [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits) endpoint.

```json
{
	"max_credit_limit": 1000
} 
```

# Known restrictions

The program-level accumulator does not retroactively include accounts that were created, transferred, or updated before the global limit configuration was applied. As a result, only accounts created, transferred to another program, or updated with new limits after these configurations are applied will be considered in the program accumulator. This limitation may lead to incomplete accumulator coverage, potentially impacting enforcement accuracy.

The following example illustrates the expected behavior when accounts are created or updated before the program limits are configured.

| Day | Action                                                                                                    | Outcome                                                                                   | Program accumulator |
| :-- | :-------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- | :------------------ |
| 1   | Create account #1 with the granted limit of $ 1000                                                        | The account limit is not validated against the program limit                              | 0                   |
| 2   | Increase the granted limit of account #1 from $1000 to $1500                                              | The account limit is not validated against the program limit                              | 0                   |
| 3   | Set the global program limit to $100000 and activate the **Program\_limit\_validation** program parameter | All accounts created and account limits updated from this point forward are considered    | 0                   |
| 4   | Create account #2 with a granted limit of $200                                                            | The account limit is validated against the program limit and the accumulator is increased | 200                 |
| 5   | Decrease the granted limit of account #1 from $1500 to $1000                                              | The accumulator is decreased by the difference                                            | 300                 |

# Common errors

Refer to the following list of common errors when working with the program limits.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Error
      </th>

      <th>
        Cause
      </th>

      <th>
        How to solve
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        The account is being created with a value different than set in the

        `granted_value`

        field.
      </td>

      <td>
        The value assigned during account creation does not fall within the

        **Minimum credit limit**

        and

        **Maximum credit limit**

        defined in the program parameters.
      </td>

      <td>
        Adjust the

        **Minimum credit limit**

        or

        **Maximum credit limit**

        program parameters or the

        `granted_limit`

        value on the account so that the value falls within the allowed range.
      </td>
    </tr>

    <tr>
      <td>
        The system does not allow an account in the program even though the

        `granted_limit`

        is lower than the program’s available limit.
      </td>

      <td>
        The

        `granted_limit`

        on the account is below the

        **Minimum credit limit**

        defined in the program parameters. The platform adjusts the value to the nearest acceptable limit, which may cause rejection.
      </td>

      <td>
        Update the

        **Minimum credit limit**

        to accommodate the desired

        `granted_limit`

        value.
      </td>
    </tr>

    <tr>
      <td>
        The program accumulator is greater than the defined limit value.
      </td>

      <td>
        The program limit was decreased to a value less than the accumulated value.
      </td>

      <td>
        Increase the program limit to the value equal to or greater than the accumulated value.
      </td>
    </tr>

    <tr>
      <td>
        The limit of a cancelled account is being considered in the accumulator of the program limit.
      </td>

      <td>
        The cancelled account still has a limit greater than zero, which causes it to be included in the accumulator calculation.
      </td>

      <td>
        Update the account’s limit to zero before or during the cancellation process to ensure it is excluded from the accumulator.
      </td>
    </tr>

    <tr>
      <td>
        The system is not validating the account limit against the program limit when creating a new account.
      </td>

      <td>
        <li>The program limit is not activated using the [Create program limits configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-global-configs) endpoint.</li><li>The account creation workflow is not set to validate limits against the program.</li>
      </td>

      <td>
        <li>Activate the program limit using the [Create program limits configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-global-configs) endpoint.</li><li>Enable account limit validation in the program parameters.</li>
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/global-configs` | `post-v1-global-configs` | Configure program limit | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--program-limits |
| `GET /v1/global-configs` | `get-v1-global-configs` | Get program limits | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--program-limits |
| `PATCH /v1/global-configs/program/{programId}` | `patch-v1-global-configs-program-programId` | Update program limit | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--program-limits |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limits` | Update account limits | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--account-limits |
| `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limit` | Update account limits (outdated) | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |

### Operation essentials

- **`POST /v1/global-configs`** (`post-v1-global-configs`): security `BearerAuth`; required parameters none declared; required body fields `level`, `program_id`, `limits`; response statuses 201, 400, 409, 500; error codes in examples `WBLS0001`, `WBLS0002`, `WBLS0003`, `EBLS9999`; events none listed.
- **`GET /v1/global-configs`** (`get-v1-global-configs`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `WBLS0005`, `WBLS0001`, `EBLS9999`; events none listed.
- **`PATCH /v1/global-configs/program/{programId}`** (`patch-v1-global-configs-program-programId`): security `BearerAuth`; required parameters `programId` (path); required body fields `limits`; response statuses 204, 400, 404, 500; error codes in examples `WBLS0001`, `WBLS0002`, `WBLS0003`, `WBLS0007`, `EBLS9999`; events none listed.
- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`PATCH /v1/accounts/{accountId}/limits`** (`patch-v1-account-limits`): security `BearerAuth`; required parameters `accountId` (path), `x-tenant` (header); required body fields none declared; response statuses 204, 400, 500; error codes in examples none; events `ledger-limit-changed-1`.
- **`PATCH /v1/accounts/{accountId}/limits`** (`patch-v1-account-limit`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `WLDG0021`, `WLDG0010`, `WLDG0025`, `WLDG0022`, `ELDG9999`; events `ledger-limit-changed-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-v1-account-limit` | `ledger-limit-changed-1` |
| `patch-v1-account-limits` | `ledger-limit-changed-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/program-limits.md`: updatedAt 2026-04-15T19:59:26.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/program-limits.md` | whole document | https://developers.pismo.io/pismo-docs/docs/program-limits | `e1876c8779827fff…` | 2026-04-15T19:59:26.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-balances-and-limits--account-limits` — API reference: Core platform - Balances and limits — Account limits
- `KU-API-core-platform-balances-and-limits--program-limits` — API reference: Core platform - Balances and limits — Program limits
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-CC-programs` — Control Center programs: create, edit, clone, export and import
- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
