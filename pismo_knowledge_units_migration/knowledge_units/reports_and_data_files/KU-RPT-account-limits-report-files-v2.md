---
ku_id: KU-RPT-account-limits-report-files-v2
title: Account limits report files
category: reports_and_data_files
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/account-limits-report-files-v2.md
  sha256: 64e4f01d818c908a2b988122cee6759a6756d073a601046478ce08b51fe65a0b
  url: https://developers.pismo.io/pismo-docs/docs/account-limits-report-files-v2
  role: primary_guide
  updated_at: '2026-06-30T22:52:42.000Z'
operations: []
related_kus:
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Account limits report files

**KU ID:** `KU-RPT-account-limits-report-files-v2` · **Category:** Reports and data files · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/account-limits-report-files-v2.md`:

> The account limits report contains the consolidated account limits from the previous day, in the timezone configured for the organization. The files for this job are saved in your designated cloud storage container in the `reports/accounts_limits_v2/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/account-limits-report-files-v2.md`: Account limits report files

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/account-limits-report-files-v2.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/account-limits-report-files-v2 · updatedAt: 2026-06-30T22:52:42.000Z

<!-- source:begin path=docs/data-and-reporting/account-limits-report-files-v2.md part=0-end -->

# Account limits report files

The account limits report contains the consolidated account limits from the previous day, in the timezone configured for the organization. The files for this job are saved in your designated cloud storage container in the `reports/accounts_limits_v2/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

* Report frequency: Once daily
* Reporting period: Previous day
* Update type: Full

The following table lists the account limits report fields.

| Field                               | Data type        | Description                                                                                                                                                                                                                                               |
| :---------------------------------- | :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Org\_ID                             | string           | Organization ID                                                                                                                                                                                                                                           |
| RefDate\*                           | date             | Date of the last closed balance of the account, in the timezone configured for the organization                                                                                                                                                           |
| Account\_ID                         | bigint\*         | Account ID                                                                                                                                                                                                                                                |
| ProgramName                         | string           | Name of the program that the account is in                                                                                                                                                                                                                |
| Program\_ID                         | int              | ID of the program that the account is in                                                                                                                                                                                                                  |
| AccountStatus                       | string           | Account status                                                                                                                                                                                                                                            |
| MaxCreditLimit                      | decimal(38,10)\* | Issuer-granted maximum credit limit                                                                                                                                                                                                                       |
| TotalCreditLimit                    | decimal(38,10)\* | Total credit limit as set by the user. This can be any value up to the MaxCreditLimit.                                                                                                                                                                    |
| WithdrawalCreditLimit\*\*           | decimal(38,10)   | Amount limit for withdrawal in credit programs. This value is calculated by multiplying TotalCreditLimit and Withdrawal limit percentage (defined for the program).                                                                                       |
| TotalOverDraftLimit                 | decimal(38,10)\* | Issuer-granted limit for overdraft spending on debit accounts                                                                                                                                                                                             |
| PercentageOverLimit                 | decimal(38,10)\* | Percentage of the maximum credit limit (max\_credit\_limit) made available for purchases over the credit limit on the account. When the credit limit is reached, the value of available\_credit\_limit field is negative in the event.                    |
| TotalInstallmentCreditLimit\*\*     | decimal(38,10)   | Issuer-granted maximum credit limit on the secondary bucket of credit                                                                                                                                                                                     |
| AvailableCreditLimit                | decimal(38,10)\* | Credit available to the customer. The platform calculates this value based on the initial total\_credit\_limit and any relevant debit and credit activity on the account.                                                                                 |
| AvailableSavingsAccountLimit        | decimal(38,10)\* | Current balance applied to an interest-bearing account                                                                                                                                                                                                    |
| AvailableWithdrawalCredit\*\*       | decimal(38,10)   | The amount available for withdrawal in credit programs. The platform calculates this value based on the initial withdrawal\_credit\_limit and any debit and credit activity on the account that impacts the withdrawal credit limit.                      |
| AvailableTotalInstallmentCredit\*\* | decimal(38,10)   | The amount of secondary credit limit currently available for new transactions. The platform calculates this value based on the initial TotalInstallmentCredit and any debit and credit activity on the account that impacts the installment credit limit. |
| HeldFunds                           | decimal(38,10)\* | Amount held in reserve that the account holder can’t access, usually due to a legal action                                                                                                                                                                |
| AdditionalFunds\*\*                 | decimal(38,10)   | Amount that can be used as supplementary when needed                                                                                                                                                                                                      |

*\*Updated functionality from v1*

*\*\*New in v2*
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/account-limits-report-files-v2.md`: updatedAt 2026-06-30T22:52:42.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/account-limits-report-files-v2.md` | whole document | https://developers.pismo.io/pismo-docs/docs/account-limits-report-files-v2 | `64e4f01d818c908a…` | 2026-06-30T22:52:42.000Z |

## Related knowledge units

- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
