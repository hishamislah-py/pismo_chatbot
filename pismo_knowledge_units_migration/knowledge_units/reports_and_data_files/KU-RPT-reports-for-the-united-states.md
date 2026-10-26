---
ku_id: KU-RPT-reports-for-the-united-states
title: Reports for the United States
category: reports_and_data_files
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/reports-for-the-united-states.md
  sha256: 4a813d80d8191074411c27ce8906ad5b93b7872f159c1a2f7e8dba01f1a47c98
  url: https://developers.pismo.io/pismo-docs/docs/reports-for-the-united-states
  role: primary_guide
  updated_at: '2026-04-23T15:21:07.000Z'
operations: []
related_kus:
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Reports for the United States

**KU ID:** `KU-RPT-reports-for-the-united-states` · **Category:** Reports and data files · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/reports-for-the-united-states.md`:

> These regulatory scheduled reports are for Pismo customers that operate in the United States. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/reports-for-the-united-states.md`: Reports for the United States

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/reports-for-the-united-states.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/reports-for-the-united-states · updatedAt: 2026-04-23T15:21:07.000Z

<!-- source:begin path=docs/data-and-reporting/reports-for-the-united-states.md part=0-end -->

# Reports for the United States

These regulatory scheduled reports are for Pismo customers that operate in the United States. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

**Notes:**

* **Product:** On the Pismo platform, there are various products, such as checking accounts, cards, and investments. A report can relate to one or more products.
* **Granularity of information:** The granularity of a report is its level of detail. For example, there are reports that provide information per account or per document or per transaction. If the granularity of a report is at the document level, this means it can encompass data from multiple accounts.

<HTMLBlock>
  {`
  <table border="0" cellpadding="0" cellspacing="0" width="1496" style="">
    <thead>
      <tr height="39" style="height: 29pt;">
        <th>Report&nbsp;</th>
        <th>Frequency&nbsp;</th>
        <th>Description&nbsp;</th>
        <th>Notes</th>
      </tr>
    </thead>

    <tbody>

  <!-- 1099-Withholding Threshold Tracking -->
      <tr height="225" style="height: 169pt;">
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">1099-Withholding Threshold Tracking&nbsp;</td>
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Daily&nbsp;</td>
        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">The Withholding Threshold Tracking report tracks the amount of interest earned on a customer's account. It also identifies when the interest on an account goes over a specified threshold, such as $10. which determines when the interest must be reported. This report is the source of the data used in the Form 1099-INT report.
  </br></br>For more information, refer to <a href="https://www.irs.gov/forms-pubs/about-form-1099-int" target="_blank">About Form 1099-INT, Interest Income</a> from the U.S. Internal Revenue Service.</td>
        <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  Deposit accounts</br></br>
  <b>Delivery format options:</b></br>
  Parquet (Analytical report that can be used to validate the data included in the official report)</br></br>
  <b>Granularity of information:</b></br>
  Account</br>
  Document number
  </td>
      </tr>

  <!-- 1099-INT -->
      <tr height="225" style="height: 169pt;">
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">1099-INT&nbsp;</td>
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Annual&nbsp;</td>
        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">The Form 1099-INT (Interest Income) report is a tax reporting document required by the Internal Revenue Service (IRS), the United States tax authority. Financial institutions must issue this report to any customers that earned $10 or more in interest during the year. The taxpayer uses this report to complete Form 1040 for their U.S individual income tax return.
  </br></br>The report gets data from the 1099-Withholding Threshold Tracking report.
  </br></br>For more information, refer to <a href="https://www.irs.gov/forms-pubs/about-form-1099-int" target="_blank">About Form 1099-INT, Interest Income</a> from the U.S. Internal Revenue Service.</td>
        <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  Deposit accounts</br></br>
  <b>Delivery format options:</b></br>
  Parquet (Analytical report that can be used to validate the data included in the official report)</br></br>
  <b>Granularity of information:</b></br>
  Account</br>
  Document number
  </td>
      </tr>

  <!-- Call Report -->
      <tr height="225" style="height: 169pt;">
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Call Report&nbsp;</td>
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Quarterly&nbsp;</td>
        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">Call Reports is responsible for reporting information on the financial condition and operating results of U.S. depository institutions. It exists to provide U.S. banking regulators with standardized, periodic data used for prudential supervision, regulatory oversight, and public disclosure.
  </br></br>The report is required by the Federal Financial Institutions Examination Council (FFIEC) and is submitted to its member agencies, including the Federal Reserve, Federal Deposit Insurance Corporation (FDIC), and the Office of the Comptroller of the Currency (OCC). The information reported supports supervisory monitoring of institutional safety and soundness, compliance with regulatory and accounting requirements, and broader policy analysis.</td>
        <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  Corporate (Transaction accounts), Banking (Other deposits), Interest engine (Other deposits)</br></br>
  <b>Delivery format options:</b></br>
  XML (FED - USA)</br>
  Parquet (Analytical report that can be used to validate the data included in the official report)</br></br>
  <b>Granularity of information:</b></br>
  Organization</br>
  Deposit type
  </td>
      </tr>

  <!-- FDIC Part 370 -->
      <tr height="225" style="height: 169pt;">
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">FDIC Part 370&nbsp;</td>
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Annual&nbsp;</td>
        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">FDIC Part 370 (12 CFR Part 370) is a regulation requiring covered institutions (banks with 2 million or more deposit accounts) to maintain complete and accurate records so the FDIC can promptly determine deposit insurance coverage in the event of a bank failure. The rule ensures depositors receive insured funds quickly and minimizes costs to the Deposit Insurance Fund.</td>
        <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  Deposit Accounts (Savings, Time Deposits / CD), Investment</br></br>
  <b>Delivery format options:</b></br>
  CSV</br></br>
  <b>Granularity of information:</b></br>
  Organization</br>
  Account</br>
  Customer (one row per customer per account)
  </td>
      </tr>

  <!-- Form 1042-S -->
      <tr height="225" style="height: 169pt;">
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Form 1042-S&nbsp;</td>
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Annual&nbsp;</td>
        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">The Form 1042-S is responsible for tracking U.S. source income paid to foreign persons (nonresident aliens, foreign entities) from time deposits and CD accounts, along with any tax withholding applied under Chapter 3 (Nonresident Aliens) or Chapter 4 (FATCA).</br></br> Pismo delivers this report in two files. One file is an analytic layer that you can use to validate the numbers. The other file is the final layout containing the information requested by the regulator.</td>
        <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  Time Deposits / CD Account</br></br>
  <b>Delivery format options:</b></br>
  Parquet (analytical and final report, consolidated)</br></br>
  <b>Granularity of information:</b></br>
  Account</br>
  Beneficiary (Nonresident alien)</br>
  Document Number (Foreign TIN)
  </td>
      </tr>

  <!-- FR2900 -->
      <tr height="225" style="height: 169pt;">
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">FR2900&nbsp;</td>
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Weekly or Quarterly&nbsp;</td>
        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">The FR 2900 report contains information about transaction accounts (accounts that allow the account holder to easily withdraw their money), other deposits, and vault cash (the physical money held by financial institutions in their vaults and teller drawers to cover daily customer withdrawals).
  </br></br>For more information, refer to <a href="https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_2900_(Savings_and_Loans)" target="_blank">FR 2900 (Savings and Loans)</a> from the U.S. Federal Reserve.</td>
        <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br> 
  Transaction accounts, bank accounts, deposit accounts</br></br>
  <b>Delivery format options:</b></br>
  XML (FED - USA)</br>
  Parquet (Analytical report that can be used to validate the data included in the official report)</br></br>
  <b>Granularity of information:</b></br>
  Organization</br>
  Deposit type
  </td>
      </tr>

  <!-- Single Account Statement -->
      <tr height="225" style="height: 169pt;">
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Single Account Statement&nbsp;</td>
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly&nbsp;</td>
        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">The Single Account Statement report lists a customer's account statements for the month. It supports only individual statements on a savings account. It does not support consolidated statements (statements that combine multiple accounts).
  </br></br>A regulator does not require this as a report. It's used by the consumer or financial institution."</td>
        <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  Deposit accounts</br></br>
  <b>Delivery format options:</b></br>
  Parquet (Analytical report)</br></br>
  <b>Granularity of information:</b></br>
  Account
  </td>
      </tr>

  <!-- Summary Of Deposit (SOD) -->
      <tr height="225" style="height: 169pt;">
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Summary Of Deposit (SOD)&nbsp;</td>
        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Annual (as of June 30 each year)&nbsp;</td>
        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">The Summary of Deposits (SOD) is an annual survey of branch office deposits as of June 30 for all FDIC-insured institutions, including insured U.S. branches of foreign banks. It is submitted to the Federal Deposit Insurance Corporation (FDIC) and has been conducted since 1934.
  </br></br>The SOD provides branch-level deposit data used for banking market analysis, regulatory supervision, and monitoring regional banking concentration. Total deposits reported must reconcile with the Call Report (Schedule RC, item 13.a for domestic-only banks, or Schedule RC-E for foreign branch banks).</td>
        <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  Corporate (Transaction accounts), Banking (Other deposits), Interest engine (Other deposits)</br></br>
  <b>Delivery format options:</b></br>
  Parquet file</br></br>
  <b>Granularity of information:</b></br>
  Organization
  </td>
      </tr>

    </tbody>
  </table>
  `}
</HTMLBlock>
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/reports-for-the-united-states.md`: updatedAt 2026-04-23T15:21:07.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/reports-for-the-united-states.md` | whole document | https://developers.pismo.io/pismo-docs/docs/reports-for-the-united-states | `4a813d80d8191074…` | 2026-04-23T15:21:07.000Z |

## Related knowledge units

- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
