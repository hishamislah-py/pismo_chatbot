---
ku_id: KU-CARD-multivalue-program-parameters
title: Multivalue program parameters
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/multivalue-program-parameters.md
  sha256: 36e346b00f7fa5ec97920d7e13db2c1c87aa00edade3cb57361e3a8a06aa178d
  url: https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters
  role: primary_guide
  updated_at: '2026-08-28T14:34:23.000Z'
operations:
- updateProgramParamenter
- v4-post-account-reason
related_kus:
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-API-revolving-credit-statements--multivalue-program-parameters
- KU-CRED-account-collection-status
- KU-EVT-catalogue-account
grouping_rationale: single source page
---

# Multivalue program parameters

**KU ID:** `KU-CARD-multivalue-program-parameters` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/multivalue-program-parameters.md`:

> A multivalue program parameter is a program parameter that takes an array as a value. For example, a parameter could take an array of integer values such as \[2, 4, 6]. Note that, in some cases, only the first value in the array is actually used. In those cases, any additional values are ignored. Use the [Update multivalue program parameter values](https://developers.pismo.io/pismo-docs/reference/updateprogramparamenter) endpoint to set or update multivalue program parameters.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/multivalue-program-parameters.md`: Multivalue program parameters

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/multivalue-program-parameters.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters · updatedAt: 2026-08-28T14:34:23.000Z

<!-- source:begin path=docs/card-issuing/multivalue-program-parameters.md part=0-end -->

# Multivalue program parameters

A multivalue program parameter is a program parameter that takes an array as a value. For example, a parameter could take an array of integer values such as \[2, 4, 6]. Note that, in some cases, only the first value in the array is actually used. In those cases, any additional values are ignored. Use the [Update multivalue program parameter values](https://developers.pismo.io/pismo-docs/reference/updateprogramparamenter) endpoint to set or update multivalue program parameters.

The following table lists the multivalue program parameters that are available on the Pismo platform.

Notes about data types:

* Boolean: Accepts only 'TRUE' or 'FALSE'. (Case is ignored.)
* Integer: Accepts values from -2^63 to (2^63)-1
* String: Maximum 100 characters
* Decimal: Maximum 100 character

<SortedTable
  data={[
  {
    'Parameter ID': '1',
    'Name': 'IGNORE_ACCRUALS_IF_ONLY_TTS',
    'Applies to': 'Setting transaction types to block accrual charges',
    'Type': 'Integer array',
    'Description': 'Transaction type IDs for transactions that should not accrue interest and that should not cause the account to be promoted to delinquent if they are the only types of transactions that are overdue.<br><br>**Example:** [701, 711, 722]',
  },
  {
    'Parameter ID': '2',
    'Name': 'PAYMENTS_TTS',
    'Applies to': 'Payment transactions',
    'Type': 'Integer array',
    'Description': 'Transaction type IDs for transactions that should be considered as payments. These types are used to calculate the total amount paid on the invoice and the amount paid by the due date.<br><br>By default, the platform considers the following transaction types as payments: 201, 244, 255, 276, 282, 320, 342, 701, 711, 721, 2224. If you configure this parameter, you need to list all the transaction types that you want to consider as payments, because this parameter overrides the default platform configuration.<br><br>**Example:** [201, 244, 255, 276]',
  },
  {
    'Parameter ID': '3',
    'Name': 'DISCHARGE_PRIORITIZED_TTS_MIGRATION',
    'Applies to': 'Discharge process at migration',
    'Type': 'Integer array',
    'Description': 'Parameter used during migration to define which credit transaction types should prioritize the discharge of debits based on authorization info. If not configured, the platform applies the default hierarchy.<br><br>**Example:** [201, 244]',
  },
  {
    'Parameter ID': '500',
    'Name': 'DELINQUENT_ACCOUNT_CLOSURE_REASON',
    'Applies to': 'Credit liquidation',
    'Type': 'String array of integer values',
    'Description': 'The external ID of the reason for the account closure.<br><br>**Notes:**<br>Only the first value in the array is used.<br>For parameter 500 to work, you must create the reason using the [Create status reason](https://developers.pismo.io/pismo-docs/reference/v4-post-account-reason) endpoint.<br>Although the external_id is not required in the creation of the status reason, it is required to be used in the Creli process.<br><br>**Example:** ["12345"]',
  },
  {
    'Parameter ID': '501',
    'Name': 'DELINQUENT_ACCOUNT_CLOSURE_PROCESSING_CODE',
    'Applies to': 'Credit liquidation',
    'Type': 'String array',
    'Description': 'Processing code for the credit transaction that the delinquent account closure process uses to settle the total due.<br><br>**Note:** Only the first value in the array is used.<br><br>**Example:** ["004000"]',
  },
  {
    'Parameter ID': '502',
    'Name': 'DELINQUENT_ACCOUNT_CLOSURE_DAYS',
    'Applies to': 'Credit liquidation',
    'Type': 'String array of integer values',
    'Description': 'The number of days an [account\'s collection status](https://developers.pismo.io/pismo-docs/docs/account-collection-status) must be `OVERDUE` before the account can be closed.<br><br>**Note:** Only the first value in the array is used.<br><br>**Example:** ["60"]',
  },
  {
    'Parameter ID': '503',
    'Name': 'DAYS_BEFORE_TO_WARNING_DELINQUENT_CLOSURE',
    'Applies to': 'Credit liquidation',
    'Type': 'Integer array',
    'Description': 'The number of days a warning event is generated before a delinquent account is closed. For example, if a delinquent account is due to be closed on the 20th day of the month, and DAYS_BEFORE_TO_WARNING_DELINQUENT_CLOSURE is set to 5, then a warning event is generated starting on day 15 of the month. Another warning event is generated on each subsequent day until the 19th (or until the the account is no longer in delinquency).<br><br>**Note:** Only the first value in the array is used.<br><br>**Example:** [5,15,20]',
  },
  {
    'Parameter ID': '504',
    'Name': 'RECURRING_CHARGE_FINAL_ACCOUNT_STATUS',
    'Applies to': 'Create recurring charge plan',
    'Type': 'String array',
    'Description': 'Final account status indicating that both the recurring charge links and the scheduled charges have been canceled. **Note:** Only the first value in the array is used.<br><br>**Example:** ["CANCELLED"]',
  },
  {
    'Parameter ID': '505',
    'Name': 'DELINQUENT_ACCOUNT_CLOSURE_LATE_TRX_DEBIT_PROCESSING_CODE',
    'Applies to': 'Credit liquidation',
    'Type': 'String array',
    'Description': 'After an account is closed for delinquency, it can still receive late transactions. The Pismo platform creates offsetting transactions to settle these. If a late credit transaction is received, the platform creates a debit transaction to settle it. The first value in the DELINQUENT_ACCOUNT_CLOSURE_LATE_TRX_DEBIT_PROCESSING_CODE array is the processing code for these debit transactions.<br><br>**Note:** Only the first value in the array is used.<br><br>**Example:** ["004000"]',
  },
  {
    'Parameter ID': '506',
    'Name': 'DELINQUENT_ACCOUNT_CLOSURE_LATE_TRX_CREDIT_PROCESSING_CODE',
    'Applies to': 'Credit liquidation',
    'Type': 'String array',
    'Description': 'After an account is closed for delinquency, it can still receive late transactions. The Pismo platform creates offsetting transactions to settle these. If a late debit transaction is received, the platform creates a credit transaction to settle it. The first value in the DELINQUENT_ACCOUNT_CLOSURE_LATE_TRX_CREDIT_PROCESSING_CODE array is the processing code for these credit transactions.<br><br>**Note:** Only the first value in the array is used.<br><br>**Example:** ["004000"]',
  },
  {
    'Parameter ID': '507',
    'Name': 'DELINQUENCY_BUCKETS_PAYMENTS_TRANSACTIONS_TYPES',
    'Applies to': 'Get delinquency bucket',
    'Type': 'Integer array',
    'Description': 'Acceptable transaction types for discharging a delinquency bucket balance.<br><br>**Example:** [201, 200]',
  },
  {
    'Parameter ID': '508',
    'Name': 'DELINQUENT_ACCOUNT_EXCLUDED_STEPS',
    'Applies to': 'Credit liquidation',
    'Type': 'String array',
    'Description': 'Steps to exclude from the delinquent account flow.<br><br>**Example:** ["POST_INTEREST_ACCRUAL", "POST_INSTALLMENT_ADVANCE","POST_CREDIT_TRANSACTION","SET_CARD_AS_BLOCKED"]',
  },
  {
    'Parameter ID': '509',
    'Name': 'DELINQUENT_ACCOUNT_FINAL_ACCOUNT_STATUS',
    'Applies to': 'Credit liquidation',
    'Type': 'String array',
    'Description': 'Final account status for a delinquent account flow. **Note:** Only the first value in the array is used.<br><br>**Example:** ["CANCELLED"]',
  },
  {
    'Parameter ID': '510',
    'Name': 'DELINQUENT_ACCOUNT_IGNORE_ACCOUNT_STATUS',
    'Applies to': 'Credit liquidation',
    'Type': 'String array',
    'Description': 'Account statuses that the delinquent account flow should ignore.<br><br>**Example:** ["STAND-BY", "BLOCKED"]',
  },
  {
    'Parameter ID': '511',
    'Name': 'DELINQUENT_ACCOUNT_TRANSACTION_TYPES_SEPARATE_CANCELLATION',
    'Applies to': 'Credit liquidation',
    'Type': 'Integer array',
    'Description': 'Transaction types that should be canceled before account closure.<br><br>**Example:** [502, 504]',
  },
  {
    'Parameter ID': '512',
    'Name': 'PAYMENT_AGREEMENT_SIMULATION_INTEREST_CAP_ENABLED — **[BETA]**',
    'Applies to': 'Payment agreements',
    'Type': 'Boolean (true/false)',
    'Description': 'Enables or disables the automatic filtering of simulations by the interest cap. Only simulations with interest amounts below the cap are considered.<br><br>**Note:** This parameter is still in beta and is only available in certain test environments. Contact your Pismo representative if you have questions.<br><br>**Example:** TRUE',
  },
  {
    'Parameter ID': '513',
    'Name': 'PAYMENT_AGREEMENT_SIMULATION_FIRST_INSTALLMENT_AS_DOWNPAYMENT — **[BETA]**',
    'Applies to': 'Payment agreements',
    'Type': 'Boolean (true/false)',
    'Description': 'Enables or disables using the first installment amount as a down payment. The amount is also considered in the formula for calculating the interest cap.<br><br>**Note:** This parameter is still in beta and is only available in certain test environments. Contact your Pismo representative if you have questions.<br><br>**Example:** TRUE',
  },
  {
    'Parameter ID': '514',
    'Name': 'PAYMENT_AGREEMENT_SIMULATION_ENABLED — **[BETA]**',
    'Applies to': 'Payment agreements',
    'Type': 'Boolean (true/false)',
    'Description': 'Enables or disables the automatic simulation of invoice installment plans at the end of the program cycle.<br><br>**Note:** This parameter is still in beta and is only available in certain test environments. Contact your Pismo representative if you have questions.<br><br>**Example:** TRUE',
  },
  {
    'Parameter ID': '1000',
    'Name': 'CHARGE_IOF_INDEPENDENTLY',
    'Applies to': 'Accrual generation and reversal',
    'Type': 'Boolean (true | false)',
    'Description': 'Enables or disables the generation of IOF accruals regardless of the REFINANCING configuration. That is, when enabled, it generates the IOF accrual even if the REFINANCING rate is zero. Otherwise, it follows the current behavior, where the IOF accrual is only generated if the calculated REFINANCING value is greater than zero.<br><br>**Note:** Although this is actually a single value parameter, it\'s used in conjunction with a multivalue parameter (EXCLUDE_TXN_CATEGORY_CHARGE_IOF_INDEPENDENTLY), so it\'s included in this list for convenience.<br><br>**Example:** TRUE',
  },
  {
    'Parameter ID': '1001',
    'Name': 'CHARGE_FINE_INDEPENDENTLY',
    'Applies to': 'Accrual generation and reversal',
    'Type': 'Boolean (true | false)',
    'Description': 'Enables or disables the generation of FINE accruals regardless of the OVERDUE configuration. That is, when enabled, it generates the FINE accrual even if the OVERDUE rate is zero. Otherwise, it follows the current behavior, where the FINE accrual is only generated if the calculated OVERDUE value is greater than zero.<br><br>**Note:** Although this is actually a single value parameter, it\'s used in conjunction with a multivalue parameter (EXCLUDE_TXN_CATEGORY_CHARGE_FINE_INDEPENDENTLY), so it\'s included in this list for convenience.<br><br>**Example:** TRUE',
  },
  {
    'Parameter ID': '1002',
    'Name': 'EXCLUDE_TXN_CATEGORY_CHARGE_IOF_INDEPENDENTLY',
    'Applies to': 'Accrual generation and reversal',
    'Type': 'Integer array',
    'Description': 'Normally, when CHARGE_IOF_INDEPENDENTLY is set to `true`, IOF charges are generated regardless of the refinancing total (the amount calculated for accruals of the REFINANCING type). You can exclude transaction categories from this behavior using the EXCLUDE_TXN_CATEGORY_CHARGE_IOF_INDEPENDENTLY program parameter.<br><br>If the ID of a transaction category is included in the EXCLUDE_TXN_CATEGORY_CHARGE_IOF_INDEPENDENTLY array, then the IOF charge for a transaction in that category is generated only if the refinancing amount for that transaction is greater than zero.<br><br>**Example:** [811, 812]',
  },
  {
    'Parameter ID': '1003',
    'Name': 'EXCLUDE_TXN_CATEGORY_CHARGE_FINE_INDEPENDENTLY',
    'Applies to': 'Accrual generation and reversal',
    'Type': 'Integer array',
    'Description': 'Normally, when CHARGE_FINE_INDEPENDENTLY is set to `true`, fines are generated regardless of the overdue total (the amount calculated for accruals of the OVERDUE type). You can exclude transaction categories from this. behavior using the EXCLUDE_TXN_CATEGORY_CHARGE_FINE_INDEPENDENTLY program parameter.<br><br>If the ID of a transaction category is included in the EXCLUDE_TXN_CATEGORY_CHARGE_FINE_INDEPENDENTLY array, then the fine for a transaction in that category is generated only if the overdue amount for that transaction is greater than zero.<br><br>**Example:** [723, 750]',
  }
]}
/>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}` | `updateProgramParamenter` | Update multivalue program parameter values | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--multivalue-program-parameters |
| `POST /accounts/v4/reasons` | `v4-post-account-reason` | Create status reason | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |

### Operation essentials

- **`PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}`** (`updateProgramParamenter`): security `BearerAuth`; required parameters `programId` (path), `parameterId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `CE0001`, `GN0001`; events none listed.
- **`POST /accounts/v4/reasons`** (`v4-post-account-reason`): security `BearerAuth`; required parameters none declared; required body fields `name`; response statuses 201, 400, 409, 500; error codes in examples `EACC0004`, `EACC0018`, `EACC0000`, `EACC0003`, `EACC9999`; events `account-reason-creation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `v4-post-account-reason` | `account-reason-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/multivalue-program-parameters.md`: updatedAt 2026-08-28T14:34:23.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/multivalue-program-parameters.md` | whole document | https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters | `36e346b00f7fa5ec…` | 2026-08-28T14:34:23.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-API-revolving-credit-statements--multivalue-program-parameters` — API reference: Revolving credit - Statements — Multivalue program parameters
- `KU-CRED-account-collection-status` — Account collection status
- `KU-EVT-catalogue-account` — Event catalogue: account
