---
ku_id: KU-CORE-program-parameters-reference-table
title: Program parameters
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/program-parameters-reference-table.md
  sha256: 7a80876e3a5735fd50dbf63694a60b3a191a55efb5dacf9b2cab675d0b172ff3
  url: https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table
  role: primary_guide
  updated_at: '2026-05-27T21:43:48.000Z'
operations:
- createProgramParameter
- createTransactionCategory
- postAccrualTypeMinimumValue
- postInterestAccruals
- programParameter
- setProgramsParameters
related_kus:
- KU-API-platform-setup-programs--parameters
- KU-API-revolving-credit-interest-accruals--accrual-types-minimum-value
- KU-API-revolving-credit-interest-accruals--post-interest-accruals
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-CC-get-started-control-center
- KU-CORE-account-parameters-reference-table
- KU-CRED-minimum-amount-due-calculation
- KU-EVT-catalogue-transaction
- KU-GS-program-types
grouping_rationale: single source page
---

# Program parameters

**KU ID:** `KU-CORE-program-parameters-reference-table` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/program-parameters-reference-table.md`:

> **Program parameters** are configurable properties that manage how a program is set up and how it behaves. The following table provides basic reference information about program parameters and whether they are required—that is, automatically assigned to a program depending on its [program type](https://developers.pismo.io/pismo-docs/docs/program-types).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/program-parameters-reference-table.md`: Program parameters

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/program-parameters-reference-table.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table · updatedAt: 2026-05-27T21:43:48.000Z

<!-- source:begin path=docs/core-platform/program-parameters-reference-table.md part=0-end -->

# Program parameters

**Program parameters** are configurable properties that manage how a program is set up and how it behaves. The following table provides basic reference information about program parameters and whether they are required—that is, automatically assigned to a program depending on its [program type](https://developers.pismo.io/pismo-docs/docs/program-types).

Program parameters come with default values. To change the value of a program parameter, use [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center). Alternatively, you can use the [API endpoints](https://developers.pismo.io/pismo-docs/reference/setprogramsparameters).

In the **Constraints** column, every program parameter is labeled as required, optional, or not allowed for each program type.

* If it's not allowed, you can't assign the parameter to that program type.
* If it's optional, you can use the [Link optional parameter to program](https://developers.pismo.io/pismo-docs/reference/createprogramparameter) endpoint to assign it to the program, then use Control Center or the API to update its value.

> 📘 Notes:
>
> * The **Display name** column shows the name of the program parameter as it appears in Control Center.
> * The **Account parameter?** column indicates whether there is a corresponding account parameter. For more information, refer to the [Account parameters](https://developers.pismo.io/pismo-docs/docs/account-parameters-reference-table) guide.
> * In the **Constraints** column, '0' is short for 'zero'. For example, 'PREPAID 0 BALANCE' means 'PREPAID ZERO BALANCE'.
> * Entries marked **N/A** indicate **Not Applicable**.
> * The program parameter ID is not included in the table because it can change depending on the environment. Use the [List program parameters](https://developers.pismo.io/pismo-docs/reference/programparameter) endpoint to get a list of the parameters for your program that includes their IDs.
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
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'integer',
    'Default value': '0',
    'Category': '',
  },
  {
    'Display name': 'Accounting MDR',
    'Applies to': '',
    'Description': '[Outdated - restricted] MDR (merchant discount rate) – Pre-payment discount percentage for merchants.',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'percent',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Accounting RAV',
    'Applies to': '',
    'Description': '[Outdated - restricted] RAV (pre-payment of receivables) – Pre-payment discount percentage for pre-payment of credit card settlements.',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'percent',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Accrual calculation strategy',
    'Applies to': 'Accrual generation and reversal',
    'Description': "Defines the start date for daily accruals.\n0 - Normal (Due date +1)\n1 - Calculation goes back to debit date. (First installment: transaction date + 1. Other installments: corresponding cycle start date + 1).\n\n The Pismo platform uses the date defined in this parameter to calculate interest charges for each transaction category. If the parameter is set to start interest from the due date, but you want cash withdrawals to accrue interest from the transaction date instead, use the [Create transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory) endpoint.",
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Accrual minimum amount to be posted',
    'Applies to': 'Accrual generation and reversal',
    'Description': 'Enables minimum value rule for accruals at the time of posting. When enabled, the platform checks whether the sum of charges generated is lower than the configured minimum value. If so, the value defined in the configuration is posted. Otherwise, the sum of the charges is posted.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>parameter transport: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Accrual projection calculation method',
    'Applies to': 'Accrual projection from cycle closing to due date',
    'Description': '0 - Disabled, 1 - LINEAR PROJECTION (accruals projected from cycle closing to the due date).',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Allow account creation',
    'Applies to': '',
    'Description': '[Outdated - restricted] Automatically generate bank accounts upon account creation.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance:optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Allow document_number reuse',
    'Applies to': '',
    'Description': 'Allow more than one account to be created for the same document_number in the same program.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Allow multiple physical cards',
    'Applies to': 'Embossing',
    'Description': 'Allow more than one physical card to consume the same balance.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: REQUIRED<br>prepaid: REQUIRED<br>credit 0 balance: REQUIRED<br>debit 0 balance: REQUIRED<br>prepaid 0 balance: REQUIRED',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Card',
  },
  {
    'Display name': 'Allow overriding the minimum amount due for the current statement',
    'Applies to': 'MAD calculation',
    'Description': 'Enables overriding the minimum amount due for the current statement.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: optional<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': '',
  },
  {
    'Display name': 'Allow program migration between different brands',
    'Applies to': '',
    'Description': 'If TRUE, the program can receive accounts from programs with a different brand than the current one.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional<br>merchant: optional<br>current accounts: optional<br>internal accounts: optional<br>correspondent accounts: optional<br>parameter transport: optional',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Allow sending card passwords via SMS',
    'Applies to': '',
    'Description': 'If TRUE, allow sending card passwords via SMS password to card.',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Card',
  },
  {
    'Display name': 'Allow tokenized transactions with new card on file',
    'Applies to': '',
    'Description': 'Allow approval of tokenized transactions with cards in CREATED status (but not yet activated).',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: REQUIRED<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Allow transfr/cash-in',
    'Applies to': '',
    'Description': '[Restricted] Allow accounts to receive funds transfer/cashin.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Allows the program to receive an account previously in a different brand program.',
    'Applies to': '',
    'Description': 'Allows the program to receive an account previously in a different brand program.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional<br>merchant: optional<br>current accounts: optional<br>internal accounts: optional<br>correspondent accounts: optional<br>transport: optional',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': '',
  },
  {
    'Display name': 'Approve rules authorization',
    'Applies to': '',
    'Description': 'If TRUE (and if spending controls are configured), authorizations are approved by default when the response from the rules-api includes an error.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: REQUIRED<br>prepaid: optional<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Approve rules cancellation',
    'Applies to': '',
    'Description': 'If TRUE, deny authorizations by default if Rules API is unavailable.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'ATC maximum offset',
    'Applies to': '',
    'Description': 'When comparing the current ATC value received with the values registered in our database. The difference must be less than this value.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: REQUIRED<br>prepaid: REQUIRED<br>credit 0 balance: REQUIRED<br>debit 0 balance: REQUIRED<br>prepaid 0 balance: REQUIRED',
    'Value type': 'integer',
    'Default value': '15',
    'Category': 'Card',
  },
  {
    'Display name': 'ATC minimum offset',
    'Applies to': '',
    'Description': 'When comparing the current ATC value received with the values registered in our database. The difference must be greater than this value.',
    'Account parameter?': 'No',
    'Constraints': 'debit: REQUIRED<br>credit: REQUIRED<br>prepaid: REQUIRED<br>credit 0 balance: REQUIRED<br>debit 0 balance: REQUIRED<br>prepaid 0 balance: REQUIRED',
    'Value type': 'integer',
    'Default value': '5',
    'Category': 'Card',
  },
  {
    'Display name': 'Calculate accruals for not due transactions',
    'Applies to': 'Accrual generation and reversal',
    'Description': 'If TRUE, generate accruals for not due transactions of accounts in refinancing.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>parameter transport: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Card expiration (# of months)',
    'Applies to': '',
    'Description': 'Number of months to add to the current date to set card expirations.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: REQUIRED<br>prepaid: REQUIRED<br>credit 0 balance: REQUIRED<br>debit 0 balance: REQUIRED<br>prepaid 0 balance: REQUIRED',
    'Value type': 'integer',
    'Default value': '72',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Contract bind allowed',
    'Applies to': '',
    'Description': '[Restricted] If TRUE, a contract can be bound to an account from a specific program.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Create physical card when creating accounts',
    'Applies to': 'Embossing',
    'Description': 'When creating an account, also create a physical card (for account owner).',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Card',
  },
  {
    'Display name': 'Creditor advancement fee',
    'Applies to': '',
    'Description': 'Defines a fixed fee to be applied to the transaction, with the same due day as the transaction.',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: optional',
    'Value type': 'decimal',
    'Default value': '10',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Creditor discount rate',
    'Applies to': '',
    'Description': 'A new transaction is created with the current date and a new counterpart transaction.',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: optional',
    'Value type': 'decimal',
    'Default value': '0.025',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Creditor maximum advancement percentage',
    'Applies to': '',
    'Description': 'Max percentage that can be anticipated from the merchant schedule.',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: optional',
    'Value type': 'decimal',
    'Default value': '1',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Defines the accrual reversal strategy in case of purchase cancellation.',
    'Applies to': 'Accrual generation and reversal',
    'Description': 'Parameter responsible for configuring the accrual reversal strategy in the event of a purchase cancellation.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed',
    'Value type': 'integer',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Defines the number of additional grace days granted to the program.',
    'Applies to': 'Grace days',
    'Description': 'Programs with this setting will receive the number of additional grace days configured in addition to the original grace period. Allowed value: from 0 to 10.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Delayed payment period for boleto (bank slip) (days)',
    'Applies to': '',
    'Description': '[Outdated] Delayed payment # of days for boleto. Calculated either by Due Date or by Real Due Date (if due date falls on a holiday or weekend)',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '5',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Delinquency bucket calculation',
    'Applies to': 'Delinquency bucket',
    'Description': 'Defines if the delinquency buckets should be calculated for tracking an account\'s debt.<br><br>Values:<br>0 - Do not calculate.<br>1 - Calculate and amortize buckets from oldest to newest.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'DIFOP',
    'Applies to': '',
    'Description': '[Outdated - restricted] Refers to the revenue from overdue charges up to 59 days.',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '0',
    'Category': 'Tax',
  },
  {
    'Display name': 'Due date exchange control',
    'Applies to': '',
    'Description': 'Flag for validating the change of expiration dates. If TRUE, you cannot change the due date more than once per cycle.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'boolean',
    'Default value': '1 (true)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Emboss an additional card',
    'Applies to': 'Embossing',
    'Description': '(Private label cards only) Specifies that the addional card will be sent to embossing.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Files',
  },
  {
    'Display name': 'Emboss card with no address',
    'Applies to': 'Embossing',
    'Description': 'Allow cards without an address to be sent for embossing.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Files',
  },
  {
    'Display name': 'Enable accrual reversal to new accrual types',
    'Applies to': 'Accrual generation and reversal',
    'Description': 'Enable reversal of accruals for new AccrualTypes.<br><br>Values:<br>[TRUE, FALSE]',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchants: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Enable the accounts creation',
    'Applies to': '',
    'Description': 'Enable the accounts creation',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: REQUIRED<br>prepaid: REQUIRED<br>credit 0 balance: REQUIRED<br>debit 0 balance: REQUIRED<br>prepaid 0 balance: REQUIRED<br>merchants: REQUIRED<br>current accounts: REQUIRED<br>internal accounts: REQUIRED<br>correspondent accounts: REQUIRED',
    'Value type': 'boolean',
    'Default value': '1 (true)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Enables minimum value rule for posting accruals at the closing cycle moment.<br>H',
    'Applies to': 'Accrual generation and reversal',
    'Description': 'Enables minimum value rule for posting accruals at the closing cycle moment. After setting this parameter to TRUE, use the [Configure minimum value by accrual type](https://developers.pismo.io/pismo-docs/reference/postaccrualtypeminimumvalue) endpoint to configure the minimum value.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': '',
  },
  {
    'Display name': 'Enables the recharge flow.',
    'Applies to': 'Recharge',
    'Description': 'Enables the recharge flow.<br><br>Values:<br>0 - Enabled<br>1 - Disabled',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'integer',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Fine amount for late payment',
    'Applies to': 'Late payment',
    'Description': 'Program parameter to configure a fine amount and to use it to calculate and post a transaction at each cycle closing if the rules are satisfied.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Fixed fee applied to the advancement transaction',
    'Applies to': '',
    'Description': 'Fixed fee applied to the advancement transaction',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: optional',
    'Value type': 'decimal',
    'Default value': '10',
    'Category': '',
  },
  {
    'Display name': 'Generate random password on card creation',
    'Applies to': '',
    'Description': 'If TRUE, generate random passwords for new cards (user can only change afterward).',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Card',
  },
  {
    'Display name': 'Ignore grace days on pending accruals reversal for revolving accounts',
    'Applies to': 'Accrual reversal',
    'Description': 'Ignore the grace period when reversing pending accruals for revolving accounts. If an account has been revolving for more than one cycle and receives a payment within the grace period, the platform reverses the pending accruals from the date of payment instead of from the due date.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'integer',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Interest projection reversal',
    'Applies to': 'Accrual generation and reversal',
    'Description': 'Defines whether the projected interest between the cut (closing) and the due date of the invoice should be reversed if any payment occurs before the due date.<br><br>Values:<br>0 - Do not reverse (default)<br>1 - Reverse',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Interest rate period',
    'Applies to': 'Accrual generation and reversal',
    'Description': 'The number of days used to calculate the daily interest. By default, this value is 30—the number of days in the banking month—but some institutions use other values, such as 360 (bank year) or 365/366 (calendar year).',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>parameter transport: not allowed',
    'Value type': 'integer',
    'Default value': '30',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Internal authorizations',
    'Applies to': '',
    'Description': 'If TRUE, ignore the issuer\'s denial. This allows adaptation to different compliance rules or to create an extra layer of security.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'boolean',
    'Default value': '1 (true)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'IOF daily rate',
    'Applies to': 'Accrual generation and reversal',
    'Description': '[Outdated - restricted] IOF daily tax rate on a credit operation (revolving, installment billing and invoice settlement).',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '0,0082',
    'Category': 'Invoice',
  },
  {
    'Display name': 'IOF first day',
    'Applies to': 'Accrual generation and reversal',
    'Description': '[Brazil only] If TRUE, revolving IOF charge on unpaid debit balance always occurs on the first day of the month.<br><br>Values: [TRUE, FALSE]',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'IOF International fee',
    'Applies to': 'Accrual generation and reversal',
    'Description': '[Outdated] IOF fee for international purchases.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: REQUIRED<br>prepaid: REQUIRED<br>credit 0 balance: REQUIRED<br>debit 0 balance: REQUIRED<br>prepaid 0 balance: REQUIRED',
    'Value type': 'decimal',
    'Default value': '6.38',
    'Category': 'Tax',
  },
  {
    'Display name': 'IOF monthly fee',
    'Applies to': 'Accrual generation and reversal',
    'Description': '[Outdated] IOF monthly fee on a credit operation (revolving, invoice installment and invoice agreement).',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: **not allowed**<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '0.38',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Limit transactions for temporary cards',
    'Applies to': '',
    'Description': '[Restricted] Transaction limit amount of a temporary type card. The amount on the card is renewed every time the Issuer renews the card. Counts only authorized transactions.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional<br>current accounts: optional',
    'Value type': 'integer',
    'Default value': '14',
    'Category': 'Card',
  },
  {
    'Display name': 'MAD equals TAD',
    'Applies to': 'Statement - Cycle closing',
    'Description': 'If TRUE, the minimum amount due (MAD) is always equal to the total amount due (TAD).<br><br>Values:<br>[TRUE, FALSE]',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: optional<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>parameter transport: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Max name length on physical card',
    'Applies to': 'Embossing',
    'Description': 'Maximum number of characters for the cardholder\'s name on a physical card.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: REQUIRED<br>prepaid: REQUIRED<br>credit 0 balance: REQUIRED<br>debit 0 balance: REQUIRED<br>prepaid 0 balance: REQUIRED',
    'Value type': 'integer',
    'Default value': '25',
    'Category': 'Credit',
  },
  {
    'Display name': 'Max percentage that can be anticipated',
    'Applies to': '',
    'Description': 'Max percentage that can be anticipated',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: optional',
    'Value type': 'decimal',
    'Default value': '1',
    'Category': '',
  },
  {
    'Display name': 'Maximum amount entered according to the invoice',
    'Applies to': '',
    'Description': '[Restricted] Maximum amount for first payment in the execution of a statement agreement (v2 and v3 agreement endpoints only).',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '30000000',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Maximum credit limit',
    'Applies to': '',
    'Description': '(Credit programs only) Overall maximum credit limit for credit accounts in the program.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '1000',
    'Category': 'Credit',
  },
  {
    'Display name': 'Maximum number of card holders',
    'Applies to': '',
    'Description': 'Limits the maximum number of additional card holders for an account.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'integer',
    'Default value': '',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Maximum percentage of first payment',
    'Applies to': '',
    'Description': '[Restricted] Maximum percentage of first payment to effect a statement agreement (v2 and v3 endpoints only).',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '10',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Maximum recharge value',
    'Applies to': '',
    'Description': 'Maximum recharge amount',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: optional<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: optional',
    'Value type': 'decimal',
    'Default value': '2500',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Merchant discount rate',
    'Applies to': '',
    'Description': '[Restricted] Merchant Discount Rate (prepayment discount percentage for merchants).',
    'Account parameter?': 'No',
    'Constraints': 'n/a',
    'Value type': 'integer',
    'Default value': '',
    'Category': 'Rate',
  },
  {
    'Display name': 'Minimo boleto',
    'Applies to': 'Statement - Cycle closing',
    'Description': 'When the statement amount is less than this value, the outstanding balance does not accrue interest.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Minimum credit limit',
    'Applies to': '',
    'Description': '(Credit programs only) Overall minimum credit limit for credit accounts in the program.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '0',
    'Category': 'Credit',
  },
  {
    'Display name': 'Minimum deposit amount',
    'Applies to': '',
    'Description': 'For an interest-bearing account, accrual adjustments depend on interest-rate and period rules. By establishing a minimum amount to be applied, a minimum amount is required for each deposit.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: not allowed<br>debit: REQUIRED<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '100',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Minimum down payment',
    'Applies to': 'Payment agreement',
    'Description': '[Restricted] Minimum down payment amount for effecting a payment agreement (v2 and v3 endpoints only).',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '15',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Minimum installment payment',
    'Applies to': 'Payment agreement',
    'Description': '[Restricted] Minimum amount of each installment of a statement agreement (v2 and v3 endpoints only).',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '15',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Minimum payment calculation method',
    'Applies to': 'Statement - Cycle closing',
    'Description': 'Method for calculating minimum amount due (MAD).<br><br>For more information, refer to [Minimum amount due calculation](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation#mad-calculation-strategy).',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Minimum percentage of first payment',
    'Applies to': 'Minimum percentage of first payment to effect a statement agreement (v2 and v3 endpoints only).',
    'Description': 'Method for calculating minimum amount due (MAD).<br><br>For more information, refer to [Minimum amount due calculation](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation#mad-calculation-strategy).',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '10',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Minimum recharge value',
    'Applies to': '',
    'Description': 'Minimum recharge value',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: optional<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: optional',
    'Value type': 'decimal',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Non-business days',
    'Applies to': 'Statement - Due date',
    'Description': 'Days of the week to be considered non-business days<br><br>Values can be a combination of the following digits representing the days of the week.<br>1 - Monday<br>2 - Tuesday<br>3 - Wednesday<br>4 - Thursday<br>5 - Friday<br>6 - Saturday<br>7 - Sunday.<br><br>For example, a value of 67 indicates that Saturday and Sunday are non-business days.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '67',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Number of days before due date to set the closing date of the statement',
    'Applies to': 'Statement - Due date',
    'Description': 'Number of days before due date to set the closing date of the statement.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '10',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Number of days to block the account for unpaid statement',
    'Applies to': 'Account - Unpaid statement',
    'Description': 'Number of days after due date to block the account for nonpayment.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '10',
    'Category': 'Charge',
  },
  {
    'Display name': 'Opt-in savings account',
    'Applies to': '',
    'Description': 'Flag indicating whether the account is an interest-bearing account.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: not allowed<br>debit: REQUIRED<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Overdue fee calculation method',
    'Applies to': 'Overdue fee calculation',
    'Description': 'Defines how late fees are applied to overdue transactions.<br><br>Values:<br>0 - Late Fee applied on 100% of the remaining balance of overdue transactions.<br>1 - Late Fee applied only to the minimum payment of the balance of overdue transactions.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Overdue strategy start',
    'Applies to': 'Overdue tolerance calculation',
    'Description': 'Defines the strategy for starting overdue on credit card statements.<br><br>Values:<br>0 - Overdue should always start on DueDate + 1. (default)<br>1 - If DueDate occurs on a non-business day, then overdue should start on RealDueDate + 1. Otherwise, it should follow the default behavior.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'integer',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Overdue tolerance amount',
    'Applies to': 'Overdue tolerance calculation',
    'Description': 'Fixed amount that is used by the **Overdue tolerance method** to determine if the account should be considered overdue.<br><br>Example: 70.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'decimal',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Overdue tolerance method',
    'Applies to': 'Overdue tolerance calculation',
    'Description': 'Configure which tolerance method should be used for delaying overdue status.<br><br>Values:<br>0 — Do not use.<br>1 — Maximum value. Between the Overdue tolerance amount and (MAD x Overdue tolerance percentage), use whichever value is greater. If the difference between the payment and the overdue amount is less than or equal to this value, the account is not considered overdue.<br>2 — Minimum value. Between the Overdue tolerance amount and (MAD x Overdue tolerance percentage), use whichever value is lower. If the difference between the payment and the overdue amount is less than or equal to this value, the account is not considered overdue.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'integer',
    'Default value': '1',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Overdue tolerance percentage',
    'Applies to': 'Overdue tolerance calculation',
    'Description': 'Percentage of the overdue amount that is used by the **Overdue tolerance method** to determine if the account should be considered overdue. Must be greater than 0 and less than or equal to 100.<br><br>Values: 0% to 100%',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'percent',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Overlimit fee amount',
    'Applies to': 'Overlimit fee charge',
    'Description': 'Fee applied if the customer exceeds the card limit (if allowed for the account). This fee is charged at the end of the invoice cycle.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '0',
    'Category': 'Tax',
  },
  {
    'Display name': 'Payment tolerance amount',
    'Applies to': 'Payment tolerance calculation',
    'Description': 'Fixed amount that is used by the **Payment tolerance method** to determine if the account should accrue interest.<br><br>Example: [$70.]',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'decimal',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Payment tolerance method',
    'Applies to': 'Payment tolerance calculation',
    'Description': 'Configure which tolerance method should be used for payment.<br><br>Values:<br>0 — Do not use.<br>1 — Maximum value. Between the Payment tolerance amount and (Payment tolerance percentage x TAD), use whichever value is higher. If the difference between the payment and the total amount due is less than or equal to this value, no interest is accrued.<br>2 — Minimum value. Between the Payment tolerance amount and (Payment tolerance percentage x TAD), use whichever value is lower. If the difference between the payment and the total amount due is less than or equal to this value, no interest is accrued.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'integer',
    'Default value': '1',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Payment tolerance percentage',
    'Applies to': 'Payment tolerance calculation',
    'Description': '"Percentage of the total amount due (TAD) that is used by the **Payment tolerance method** to determine if the account should accrue interest. Must be greater than 0 and less than or equal to 100.<br><br>Values: 0% to 100%',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'decimal',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Percentage for calculating the minimum payment amount.',
    'Applies to': 'Statement - Cycle closing',
    'Description': 'Percentage for calculating the minimum payment amount when the amount is calculated on the invoice and not on the balance of each transaction. This parameter is only be used when the **Minimum payment calculation method** parameter is equal to 2.<br><br>Values: 0% to 100%',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '15',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Percentage rate over the anticipated gross amount<br>',
    'Applies to': '',
    'Description': 'Percentage rate over the anticipated gross amount',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: optional',
    'Value type': 'decimal',
    'Default value': '0.025',
    'Category': '',
  },
  {
    'Display name': 'Post pre-scheduled transactions',
    'Applies to': '',
    'Description': 'Enables the program to check if there are transactions to be posted when the cycle closes. If there are, the transactions will be posted.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>parameter transport: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Post the pre-scheduled transactions when the cycle closes.',
    'Applies to': '',
    'Description': 'Post the pre-scheduled transactions when the cycle closes.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': '',
  },
  {
    'Display name': 'Revolving Minimum Amount Due (MAD) percentage',
    'Applies to': 'MAD calculation',
    'Description': 'This defines the percentage applied to the total balance when the compulsory MAD calculation strategy is enabled.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: optional<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not_allowe',
    'Value type': 'percent',
    'Default value': '0',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Revolving statement summary at cycle closing',
    'Applies to': '',
    'Description': 'If TRUE, enables the sending of events with revolving statement summary at cycle closing.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Secondary charge order',
    'Applies to': 'Discharge of debit transactions',
    'Description': 'Consider an alternative form of discharge order at the account level.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>parameter transport: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Send cycle opening event when first cycle is created',
    'Applies to': 'Statement - Cycle closing',
    'Description': 'Indicates whether the [Statement cycle opened event](https://developers.pismo.io/events/docs/statements-cycle-opening-1) should be sent when the first cycle is opened. This event is only sent for the first cycle. If the parameter is `false`, it\'s never sent.<br><br>Values: [TRUE, FALSE]',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchants: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accouts: not allowed<br>transport: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Send email notification upon payment',
    'Applies to': '',
    'Description': 'If TRUE, send email notifications upon processing any bank/gateway/authorizer payment.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Send password via SMS',
    'Applies to': '',
    'Description': 'If TRUE, enables sending password via SMS when creating an account.',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Send rules authorization',
    'Applies to': 'Card network authorization workflow',
    'Description': 'If Flex Controls are configured, set this parameter to 2 to trigger evaluation through the Flex Controls API during authorization.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: not allowed<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'integer',
    'Default value': '2',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Send SMS notification upon payment',
    'Applies to': '',
    'Description': 'If TRUE, send SMS notifications upon processing any bank/gateway/authorizer payment.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Set EventDate in accounting entries to work days',
    'Applies to': '',
    'Description': 'If this parameter is set to true, the EventDate field in accounting entries will contain dates for only work days. For example, if an accounting entry is created on a non-work day such as Saturday, the EventDate for this accounting entry will be the date of the next work day such as Monday. If this parameter is set to false, the EventDate field in accounting entries will contain dates for both work and non-work days. In this case, if an accounting entry is created on a Saturday, the EventDate will be that Saturday’s date.',
    'Account parameter?': '',
    'Constraints': 'credit: REQUIRED<br>debit: REQUIRED<br>prepaid: REQUIRED<br>credit 0 balance: REQUIRED<br>debit 0 balance: REQUIRED<br>prepaid 0 balance: REQUIRED',
    'Value type': 'Boolean',
    'Default value': '1 (true)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Set external id as main key for accounts',
    'Applies to': '',
    'Description': 'Use external_id as main key instead of document_number.',
    'Account parameter?': 'No',
    'Constraints': 'credit: optional<br>debit: optional<br>prepaid: optional<br>credit 0 balance: optional<br>debit 0 balance: optional<br>prepaid 0 balance: optional',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Skip auto-renewal of temporary cards',
    'Applies to': '',
    'Description': 'By default, a temporary card is renewed when the PCI data is consulted. When this parameter is defined as TRUE, the renewal is skipped.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: REQUIRED<br>prepaid: REQUIRED<br>credit 0 balance: REQUIRED<br>debit 0 balance: REQUIRED<br>prepaid 0 balance: REQUIRED',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Card',
  },
  {
    'Display name': 'Standard calendar selection',
    'Applies to': '',
    'Description': 'Standard calendar selection',
    'Account parameter?': 'No',
    'Constraints': 'n/a',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': '',
  },
  {
    'Display name': 'Stop accrual # of days',
    'Applies to': 'Accrual generation and reversal',
    'Description': 'Maximum number of days in overdue for which fees, interest, and fines are calculated and posted. The platform won’t post any accrued amount that was calculated after the **Stop accrual # of days** number of days. You can still post these accruals manually using the [Post interest accruals](https://developers.pismo.io/pismo-docs/reference/postinterestaccruals) endpoint.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '63',
    'Category': 'Charge',
  },
  {
    'Display name': 'Stores the number of days to reach the daily accrual calculation.',
    'Applies to': 'Accrual generation and reversal',
    'Description': 'The number of days in the interest rate period. This parameter can be used to configure different periods for interest rates, such an annual or monthly period. Refer to Changing the interest rate period for more information.',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchants: not allowed',
    'Value type': 'integer',
    'Default value': '30 (monthly)',
    'Category': '',
  },
  {
    'Display name': 'Strategy for calculating the statement minimum amount for compulsory',
    'Applies to': 'MAD calculation',
    'Description': 'Defines the strategy for calculating the compulsory Minimum Amount Due (MAD).',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: optional<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed<br>merchants: not allowed',
    'Value type': 'boolean',
    'Default value': '0 (false)',
    'Category': 'Parameter',
  },
  {
    'Display name': 'Timeline Category display name',
    'Applies to': '',
    'Description': '[Restricted] Display name for the Category field of a timeline.',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '',
    'Category': 'Transaction type',
  },
  {
    'Display name': 'Timeline Type display name',
    'Applies to': '',
    'Description': '[Restricted] Display name for the Type field of a timeline.',
    'Account parameter?': 'No',
    'Constraints': 'credit: not allowed<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'integer',
    'Default value': '',
    'Category': 'Transaction type',
  },
  {
    'Display name': 'Validity period of temporary cards',
    'Applies to': '',
    'Description': 'Validity period of temporary cards',
    'Account parameter?': 'No',
    'Constraints': 'credit: REQUIRED<br>debit: REQUIRED<br>prepaid: REQUIRED<br>credit 0 balance: REQUIRED<br>debit 0 balance: REQUIRED<br>prepaid 0 balance: REQUIRED<br>merchant: not allowed<br>current accounts: not allowed<br>internal accounts: not allowed<br>correspondent accounts: not allowed<br>transport: not allowed',
    'Value type': 'integer',
    'Default value': '24',
    'Category': 'Card',
  },
  {
    'Display name': 'Withdrawal limit percentage',
    'Applies to': '',
    'Description': 'Maximum allowed percentage for withdrawals and payments. This value is a percentage of the maximum credit limit granted by the institution to users of this program. This value is set in decimal places. For example, to set a withdrawal limit of 10%, use 0.1.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: not allowed<br>prepaid: not allowed<br>credit 0 balance: not allowed<br>debit 0 balance: not allowed<br>prepaid 0 balance: not allowed',
    'Value type': 'decimal',
    'Default value': '1',
    'Category': 'Credit',
  },
  {
    'Display name': 'Wrong password attempts',
    'Applies to': '',
    'Description': 'Number of wrong password attempts allowed before blocking the card.',
    'Account parameter?': 'Yes',
    'Constraints': 'credit: REQUIRED<br>debit: REQUIRED<br>prepaid: REQUIRED<br>credit 0 balance: REQUIRED<br>debit 0 balance: REQUIRED<br>prepaid 0 balance: REQUIRED',
    'Value type': 'integer',
    'Default value': '3',
    'Category': 'Tariff',
  },
]}
/>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /programs/v1/programs/parameters/batch` | `setProgramsParameters` | Update program(s) parameters | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `POST /programs/v1/programs/{program_id}/parameters` | `createProgramParameter` | Link optional parameter to program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `GET /programs/v1/programs/{program_id}/parameters` | `programParameter` | List program parameters | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `POST /statements-v2/v1/transactions-categories` | `createTransactionCategory` | Create program transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `POST /v1/accrual-type-minimum-value` | `postAccrualTypeMinimumValue` | Configure minimum value by accrual type | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--accrual-types-minimum-value |
| `POST /v1/accounts/{accountId}/interest-accruals` | `postInterestAccruals` | Post interest accruals | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--post-interest-accruals |

### Operation essentials

- **`POST /programs/v1/programs/parameters/batch`** (`setProgramsParameters`): security `S2SAuthentication`; required parameters none declared; required body fields none declared; response statuses 204, 400; error codes in examples none; events none listed.
- **`POST /programs/v1/programs/{program_id}/parameters`** (`createProgramParameter`): security `S2SAuthentication`; required parameters `program_id` (path); required body fields `parameter_name`; response statuses 201, 400; error codes in examples none; events none listed.
- **`GET /programs/v1/programs/{program_id}/parameters`** (`programParameter`): security `S2SAuthentication`; required parameters `program_id` (path); required body fields none declared; response statuses 200, 400; error codes in examples none; events none listed.
- **`POST /statements-v2/v1/transactions-categories`** (`createTransactionCategory`): security `BearerAuth`; required parameters `Authorization` (header), `program-id` (header); required body fields `default_rate`, `fine_rate`, `minimum_value`, `overdue_rate_after_due_date`, `refinancing_rate_after_due_date`; response statuses 201, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`POST /v1/accrual-type-minimum-value`** (`postAccrualTypeMinimumValue`): security `BearerAuth`; required parameters none declared; required body fields `accrual_type`, `hierarchy_name`, `hierarchy_value`, `minimum_amount_to_post`; response statuses 201, 400, 500; error codes in examples `EX0001`, `GN0001`; events none listed.
- **`POST /v1/accounts/{accountId}/interest-accruals`** (`postInterestAccruals`): security `BearerAuth`; required parameters `accountId` (path); required body fields `accrual_statuses`; response statuses 201, 400, 403, 404, 422, 500; error codes in examples `EIAC0002`, `WIAC0005`, `WIAC0002`, `WIAC0003`, `GN0001`; events `transaction-creation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `postInterestAccruals` | `transaction-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/program-parameters-reference-table.md`: updatedAt 2026-05-27T21:43:48.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/program-parameters-reference-table.md` | whole document | https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table | `7a80876e3a5735fd…` | 2026-05-27T21:43:48.000Z |

## Related knowledge units

- `KU-API-platform-setup-programs--parameters` — API reference: Platform setup - Programs — Parameters
- `KU-API-revolving-credit-interest-accruals--accrual-types-minimum-value` — API reference: Revolving credit - Interest accruals — Accrual types minimum value
- `KU-API-revolving-credit-interest-accruals--post-interest-accruals` — API reference: Revolving credit - Interest accruals — Post interest accruals
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CORE-account-parameters-reference-table` — Account parameters
- `KU-CRED-minimum-amount-due-calculation` — Minimum amount due calculation
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-GS-program-types` — Program types
