---
ku_id: KU-CORE-account-parameters-reference-table
title: Account parameters
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/account-parameters-reference-table.md
  sha256: a4cf17bdb60f5050e72c50422cfcb5382b3b56de8ac3d2b4c4a1cfa276638cb0
  url: https://developers.pismo.io/pismo-docs/docs/account-parameters-reference-table
  role: primary_guide
  updated_at: '2026-05-28T21:27:21.000Z'
operations:
- account-parameters-find
- account-parameters-update
related_kus:
- KU-API-core-platform-accounts--account-parameters
- KU-CORE-program-parameters-reference-table
- KU-GS-program-types
grouping_rationale: single source page
---

# Account parameters

**KU ID:** `KU-CORE-account-parameters-reference-table` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/account-parameters-reference-table.md`:

> **Account parameters** are configurable properties that manage how an account is set up and how it behaves. **All account parameters have corresponding [program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table).** Account parameters give you the option of configuring the same properties differently for specific accounts. The following table provides basic reference information about account parameters, including their value type and whether they are required—that is, automatically assigned to an account depending on its [program type](https://developers.pismo.io/pismo-docs/docs/program-types).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/account-parameters-reference-table.md`: Account parameters

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/account-parameters-reference-table.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/account-parameters-reference-table · updatedAt: 2026-05-28T21:27:21.000Z

<!-- source:begin path=docs/core-platform/account-parameters-reference-table.md part=0-end -->

# Account parameters

**Account parameters** are configurable properties that manage how an account is set up and how it behaves. **All account parameters have corresponding [program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table).** Account parameters give you the option of configuring the same properties differently for specific accounts. The following table provides basic reference information about account parameters, including their value type and whether they are required—that is, automatically assigned to an account depending on its [program type](https://developers.pismo.io/pismo-docs/docs/program-types).

In the **Constraints** column, every account parameter is either required, optional, or not allowed for each program type.

Use the [Update account parameter ](https://developers.pismo.io/pismo-docs/reference/account-parameters-update) endpoint to set or update the value of an account parameter for an account. This endpoint requires the ID for the account parameter (`parameter_id`), which you can get using the [List account parameters](https://developers.pismo.io/pismo-docs/reference/account-parameters-find) endpoint.

> 📘 Notes:
>
> * The ID for an account parameter is the same as the ID of the corresponding program parameter. IDs are not included in the table because they can change depending on the environment. Use the [List account parameters](https://developers.pismo.io/pismo-docs/reference/account-parameters-find) endpoint to get a list of the parameters for your account that includes their IDs.
> * The **Display name** column shows the name of the account parameter as it appears in the results of the [List account parameters](https://developers.pismo.io/pismo-docs/reference/account-parameters-find) endpoint.
> * In the **Constraints** column, '0' is short for 'zero'. For example, 'PREPAID 0 BALANCE' means 'PREPAID ZERO BALANCE'.
> * Parameters that are flagged as **restricted** in their description are only applicable to certain customers.
> * If a parameter is flagged as **outdated**, another, preferred, method is now available to perform the same task. The parameter can still be used, however.

<SortedTable
  columnsConfig={{
   'Description': {minWidth: '225px'},
    'Account parameter?': { wrapHeader: true },
    'Constraints': {minWidth: '225px'},
    'Value type': { wrapHeader: true },
    'Default value': { wrapHeader: true, align: "center" }	
  }}
  data={[
    {
      'Display name': 'Account financial classification',
      'Applies to': '',
      'Description': 'This is used in audit in accounting register to compare the generated accruals.',
      'Constraints': 'credit: REQUIRED\ndebit: not allowed\nprepaid: not allowed\ncredit 0 balance: not allowed\ndebit 0 balance: not allowed\nprepaid 0 balance: not allowed\nmerchant: not allowed\ncurrent accounts: not allowed\ninternal accounts: not allowed\ncorrespondent accounts: not allowed\ntransport: not allowed',
      'Value type': 'integer',
      'Default value': '0',
      'Category': ''
    },
    {
      'Display name': 'Allow overriding the minimum amount due for the current statement',
      'Applies to': 'MAD calculation',
      'Description': 'Enables overriding the minimum amount due for the current statement.',
      'Constraints': 'credit: optional\ndebit: not allowed\nprepaid: not allowed\ncredit 0 balance: not allowed\ndebit 0 balance: not allowed\nprepaid 0 balance: not allowed',
      'Value type': 'boolean',
      'Default value': '0 (false)',
      'Category': ''
    },
    {
      'Display name': 'Allow transfr/cash-in',
      'Applies to': '',
      'Description': '[Restricted] Allow accounts to receive funds transfer/cashin.',
      'Constraints': 'credit: optional\ndebit: optional\nprepaid: optional\ncredit 0 balance: optional\ndebit 0 balance: optional\nprepaid 0 balance: optional',
      'Value type': 'boolean',
      'Default value': '0 (false)',
      'Category': 'Parameter'
    },
    {
      'Display name': 'Card expiration (# of months)',
      'Applies to': '',
      'Description': 'Number of months to add to the current date to set card expirations.',
      'Constraints': 'credit: REQUIRED\ndebit: REQUIRED\nprepaid: REQUIRED\ncredit 0 balance: REQUIRED\ndebit 0 balance: REQUIRED\nprepaid 0 balance: REQUIRED',
      'Value type': 'integer',
      'Default value': '72',
      'Category': 'Parameter'
    },
    {
      'Display name': 'Defines the accrual reversal strategy in case of purchase cancellation.',
      'Applies to': 'Accrual generation and reversal',
      'Description': 'Parameter responsible for configuring the accrual reversal strategy in the event of a purchase cancellation.',
      'Constraints': 'credit: REQUIRED\ndebit: not allowed\nprepaid: not allowed\ncredit 0 balance: not allowed\ndebit 0 balance: not allowed\nprepaid 0 balance: not allowed\ncurrent accounts: not allowed\ninternal accounts: not allowed\ncorrespondent accounts: not allowed',
      'Value type': 'integer',
      'Default value': '0',
      'Category': 'Parameter'
    },
    {
      'Display name': 'Delinquency bucket calculation',
      'Applies to': 'Delinquency bucket',
      'Description': "Defines if the delinquency buckets should be calculated for tracking an account's debt.\n\nValues:\n0 - Do not calculate.\n1 - Calculate and amortize buckets from oldest to newest.",
      'Constraints': 'credit: REQUIRED\ndebit: not allowed\nprepaid: not allowed\ncredit 0 balance: not allowed\ndebit 0 balance: not allowed\nprepaid 0 balance: not allowed',
      'Value type': 'integer',
      'Default value': '0',
      'Category': 'Parameter'
    },
    {
      'Display name': 'Emboss an additional card',
      'Applies to': 'Embossing',
      'Description': '(Private label cards only) Specifies that the addional card will be sent to embossing.',
      'Constraints': 'credit: not allowed\ndebit: not allowed\nprepaid: not allowed\ncredit 0 balance: not allowed\ndebit 0 balance: not allowed\nprepaid 0 balance: not allowed',
      'Value type': 'boolean',
      'Default value': '0 (false)',
      'Category': 'Files'
    },
    {
      'Display name': 'Emboss card with no address',
      'Applies to': 'Embossing',
      'Description': 'Allow cards without an address to be sent for embossing.',
      'Constraints': 'credit: optional\ndebit: optional\nprepaid: optional\ncredit 0 balance: optional\ndebit 0 balance: optional\nprepaid 0 balance: optional',
      'Value type': 'boolean',
      'Default value': '0 (false)',
      'Category': 'Files'
    },
    {
      'Display name': 'Interest projection reversal',
      'Applies to': 'Accrual generation and reversal',
      'Description': 'Defines whether the projected interest between the cut (closing) and the due date of the invoice should be reversed if any payment occurs before the due date.\n\nValues:\n0 - Do not reverse (default)\n1 - Reverse',
      'Constraints': 'credit: REQUIRED\ndebit: not allowed\nprepaid: not allowed\ncredit 0 balance: not allowed\ndebit 0 balance: not allowed\nprepaid 0 balance: not allowed',
      'Value type': 'integer',
      'Default value': '0',
      'Category': 'Parameter'
    },
    {
      'Display name': 'Internal authorizations',
      'Applies to': '',
      'Description': "If TRUE, ignore the issuer's denial. This allows adaptation to different compliance rules or to create an extra layer of security.",
      'Constraints': 'credit: optional\ndebit: optional\nprepaid: optional\ncredit 0 balance: optional\ndebit 0 balance: optional\nprepaid 0 balance: optional',
      'Value type': 'boolean',
      'Default value': '1 (true)',
      'Category': 'Parameter'
    },
    {
      'Display name': 'IOF daily rate',
      'Applies to': 'Accrual generation and reversal',
      'Description': '[Outdated - restricted] IOF daily tax rate on a credit operation (revolving, installment billing and invoice settlement).',
      'Constraints': 'credit: REQUIRED\ndebit: not allowed\nprepaid: not allowed\ncredit 0 balance: not allowed\ndebit 0 balance: not allowed\nprepaid 0 balance: not allowed',
      'Value type': 'decimal',
      'Default value': '0,0082',
      'Category': 'Invoice'
    },
    {
      'Display name': 'IOF International fee',
      'Applies to': 'Accrual generation and reversal',
      'Description': '[Outdated] IOF fee for international purchases.',
      'Constraints': 'credit: REQUIRED\ndebit: REQUIRED\nprepaid: REQUIRED\ncredit 0 balance: REQUIRED\ndebit 0 balance: REQUIRED\nprepaid 0 balance: REQUIRED',
      'Value type': 'decimal',
      'Default value': '6.38',
      'Category': 'Tax'
    },
    {
      'Display name': 'IOF monthly fee',
      'Applies to': 'Accrual generation and reversal',
      'Description': '[Outdated] IOF monthly fee on a credit operation (revolving, invoice installment and invoice agreement).',
      'Constraints': 'credit: REQUIRED\ndebit: not allowed\nprepaid: not allowed\ncredit 0 balance: not allowed\ndebit 0 balance: not allowed',
      'Value type': 'decimal',
      'Default value': '0.38',
      'Category': 'Parameter'
    }
	]}
/>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PUT /accounts/v1/accounts/{accountId}/parameters/{parameterId}` | `account-parameters-update` | Update parameter | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--account-parameters |
| `GET /accounts/v1/accounts/{accountId}/parameters` | `account-parameters-find` | List parameters | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--account-parameters |

### Operation essentials

- **`PUT /accounts/v1/accounts/{accountId}/parameters/{parameterId}`** (`account-parameters-update`): security `BearerAuth`; required parameters `accountId` (path), `parameterId` (path); required body fields none declared; response statuses 200, 500; error codes in examples none; events none listed.
- **`GET /accounts/v1/accounts/{accountId}/parameters`** (`account-parameters-find`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/core-platform/account-parameters-reference-table.md`: updatedAt 2026-05-28T21:27:21.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/account-parameters-reference-table.md` | whole document | https://developers.pismo.io/pismo-docs/docs/account-parameters-reference-table | `a4cf17bdb60f5050…` | 2026-05-28T21:27:21.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--account-parameters` — API reference: Core platform - Accounts — Account parameters
- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-GS-program-types` — Program types
