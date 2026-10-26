---
ku_id: KU-RPT-report-files-accounts-and-transactions
title: 'Report files: accounts analytic, account balances, billing, discharge tracking, portfolio and transaction balances'
category: reports_and_data_files
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/accounts-analytic-report-files.md
  sha256: c0add47b6614b7a31b8d9e3c62e72c610c84b245dda129393726c2cae71652fc
  url: https://developers.pismo.io/pismo-docs/docs/accounts-analytic-report-files
  role: primary_guide
  updated_at: '2026-03-18T15:16:09.000Z'
- path: docs/data-and-reporting/accounts-balances-report-files.md
  sha256: bf013a28e052e410ea237ec3f6e694e0af24e4ba5b625dd1884cbd2fffb8edac
  url: https://developers.pismo.io/pismo-docs/docs/accounts-balances-report-files
  role: primary_guide
  updated_at: '2026-03-18T15:16:11.000Z'
- path: docs/data-and-reporting/billing-report-files.md
  sha256: e1bc0852ea3a16b10f910f691913540d5eb123f76f39b38bef4848a0c814ca4c
  url: https://developers.pismo.io/pismo-docs/docs/billing-report-files
  role: primary_guide
  updated_at: '2026-03-18T15:16:14.000Z'
- path: docs/data-and-reporting/discharge-tracking-report-files.md
  sha256: 5257144c5551391209d4d778edaaa2a343dc34c8e8e0e77fc217a055b26121fe
  url: https://developers.pismo.io/pismo-docs/docs/discharge-tracking-report-files
  role: primary_guide
  updated_at: '2026-03-18T15:16:15.000Z'
- path: docs/data-and-reporting/portfolio-balance-report-files.md
  sha256: db9dd4150ebb4474025674db94720d5710f43dfe190662d2e5c6daefe08c3df8
  url: https://developers.pismo.io/pismo-docs/docs/portfolio-balance-report-files
  role: primary_guide
  updated_at: '2026-03-18T15:16:17.000Z'
- path: docs/data-and-reporting/transactions-balance-report-files.md
  sha256: 0df24d318179a7752ce346bc53953c4bf3c47306877d959e747133eaa9058768
  url: https://developers.pismo.io/pismo-docs/docs/transactions-balance-report-files
  role: primary_guide
  updated_at: '2026-03-18T15:16:18.000Z'
operations: []
related_kus:
- KU-RPT-scheduled-reports
grouping_rationale: Short report-file layout pages with the same structure.
---

# Report files: accounts analytic, account balances, billing, discharge tracking, portfolio and transaction balances

**KU ID:** `KU-RPT-report-files-accounts-and-transactions` · **Category:** Reports and data files · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 6 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Short report-file layout pages with the same structure.

Scope as stated in `docs/data-and-reporting/accounts-analytic-report-files.md`:

> The accounts analytic report contains the analytics from the previous day. The files for this job are saved in your designated cloud storage container in the `/reports/accounts_analytic/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

Scope as stated in `docs/data-and-reporting/accounts-balances-report-files.md`:

> The account balances report contains the account balances from the previous day. The files for this job are saved in your designated cloud storage container in the `/reports/accounts_balances/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

Scope as stated in `docs/data-and-reporting/billing-report-files.md`:

> The billing report contains the billing events from the previous day. The files for this job are saved in your designated cloud storage container in the `/reports/billing/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

Scope as stated in `docs/data-and-reporting/discharge-tracking-report-files.md`:

> The Discharge tracking report contains the discharge tracking events from the previous day. The files for this job are saved in your designated cloud storage container in the `reports/discharge_tracking/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

Scope as stated in `docs/data-and-reporting/portfolio-balance-report-files.md`:

> The Portfolio balance report contains the portfolio balance events from the previous day. The files for this job are saved in your designated cloud storage container in the `reports/portfolio_balance/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

Scope as stated in `docs/data-and-reporting/transactions-balance-report-files.md`:

> The Transactions balance report contains the transactions balances from the previous day. The files for this job are saved in your designated cloud storage container in the `reports/transactions_balance/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/accounts-analytic-report-files.md`: Accounts analytic report files
- `docs/data-and-reporting/accounts-balances-report-files.md`: Account balances report files
- `docs/data-and-reporting/billing-report-files.md`: Billing report files
- `docs/data-and-reporting/discharge-tracking-report-files.md`: Discharge tracking report files
- `docs/data-and-reporting/portfolio-balance-report-files.md`: Portfolio balance report files
- `docs/data-and-reporting/transactions-balance-report-files.md`: Transactions balance report files

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/accounts-analytic-report-files.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accounts-analytic-report-files · updatedAt: 2026-03-18T15:16:09.000Z

<!-- source:begin path=docs/data-and-reporting/accounts-analytic-report-files.md part=0-end -->

# Accounts analytic report files

The accounts analytic report contains the analytics from the previous day. The files for this job are saved in your designated cloud storage container in the `/reports/accounts_analytic/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

* Report frequency: Once daily
* Reporting period: Previous day
* Update type: Incremental

The following table lists the accounts analytic report fields.

| Field          | Type   | Description                                                      |
| :------------- | :----- | :--------------------------------------------------------------- |
| Org\_ID        | string | Organization ID                                                  |
| RefDate        | date   | Date that the report file was generated in the YYYY-MM-DD format |
| ProgramName    | string | Name of the program to which the account belongs                 |
| Program\_ID    | int    | Program ID                                                       |
| Account\_ID    | int    | Account ID                                                       |
| DocumentNumber | string | State-issued ID number of the account owner                      |
| Name           | string | Entity name of the account owner                                 |
| CreationDate   | date   | Date of the account creation in the YYYY-MM-DD HH:MM:SS format   |
| Brand          | string | Card network                                                     |
| External\_ID   | string | Customer-defined external ID                                     |
<!-- source:end -->

### Source 2: `docs/data-and-reporting/accounts-balances-report-files.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accounts-balances-report-files · updatedAt: 2026-03-18T15:16:11.000Z

<!-- source:begin path=docs/data-and-reporting/accounts-balances-report-files.md part=0-end -->

# Account balances report files

The account balances report contains the account balances from the previous day. The files for this job are saved in your designated cloud storage container in the `/reports/accounts_balances/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

* Report frequency: Once daily
* Reporting period: Previous day
* Update type: Incremental

The following table lists the account balances report fields.

<HTMLBlock>
  {`
  <table>
      <thead>
          <tr>
              <th>Field</th>
              <th>Data type</th>
              <th>Description</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>Org_ID</td>
              <td>string</td>
              <td>Organization ID</td>
          </tr>
          <tr>
              <td>RefDate</td>
              <td>date</td>
              <td>Date the report file was generated</td>
          </tr>
          <tr>
              <td>Account_ID</td>
              <td>int</td>
              <td>Account ID</td>
          </tr>
          <tr>
              <td>Program_ID</td>
              <td>int</td>
              <td>Program ID</td>
          </tr>
          <tr>
              <td>DueDays</td>
              <td>int</td>
              <td>Number of days the account has been in arrears</td>
          </tr>
          <tr>
              <td>Type</td>
              <td>string</td>
              <td>Balance type:<br>
                <ul>
                  <li><code>RotativoEmDia</code> (RevolvingOnDay): Includes all balances from transactions that are still within the allowed payment period, even if the statement due date has passed. It reflects transactions up to the current date.
                  <li><code>RotativoAtraso</code> (RevolvingDelay): Includes all balances from transactions that are overdue and have not been paid.
                  <li><code>Corrente</code> (Current): These are balances from transactions included in the open statement (current cycle) and also those mapped to future statements (future cycles).
                  <li><code>Futuro</code> (Future): Includes balances from transactions that will be charged in future statements, such as installment purchases.
  					</td>
          </tr>
          <tr>
              <td>AccountStatus</td>
              <td>string</td>
              <td>Account status</td>
          </tr>
          <tr>
              <td>Balance</td>
              <td>double</td>
              <td>Balance summarized according to Type</td>
          </tr>
      </tbody>
  </table>
  `}
</HTMLBlock>
<!-- source:end -->

### Source 3: `docs/data-and-reporting/billing-report-files.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/billing-report-files · updatedAt: 2026-03-18T15:16:14.000Z

<!-- source:begin path=docs/data-and-reporting/billing-report-files.md part=0-end -->

# Billing report files

The billing report contains the billing events from the previous day. The files for this job are saved in your designated cloud storage container in the `/reports/billing/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

* Report frequency: Once daily
* Reporting period: Previous day
* Update type: Incremental

The following table lists the billing report fields.

> 📘
>
> Decimal values are rounded to the hundredths.

<HTMLBlock>
  {`
  <table>
      <thead>
          <tr>
              <th>Field</th>
              <th>Data type</th>
              <th>Description</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>Org_ID</td>
              <td>string</td>
              <td>Organization ID</td>
          </tr>
          <tr>
              <td>RefDate</td>
              <td>date</td>
              <td>Date the report file was generated</td>
          </tr>
          <tr>
              <td>Program_ID</td>
              <td>int</td>
              <td>Program ID</td>
          </tr>
          <tr>
              <td>ProgramName</td>
              <td>string</td>
              <td>Program name</td>
          </tr>
          <tr>
              <td>Account_ID</td>
              <td>int</td>
              <td>Account ID</td>
          </tr>
          <tr>
              <td>DueDate</td>
              <td>date</td>
              <td>Due date</td>
          </tr>
          <tr>
              <td>TransactionType_ID</td>
              <td>int</td>
              <td>Transaction type ID</td>
          </tr>
          <tr>
              <td>Description</td>
              <td>string</td>
              <td>Transaction description</td>
          </tr>
          <tr>
              <td>Qtd</td>
              <td>string</td>
              <td>Number of transactions</td>
          </tr>
          <tr>
              <td>Valor</td>
              <td>double</td>
              <td>Total amount</td>
          </tr>
      </tbody>
  </table>
  `}
</HTMLBlock>
<!-- source:end -->

### Source 4: `docs/data-and-reporting/discharge-tracking-report-files.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/discharge-tracking-report-files · updatedAt: 2026-03-18T15:16:15.000Z

<!-- source:begin path=docs/data-and-reporting/discharge-tracking-report-files.md part=0-end -->

# Discharge tracking report files

The Discharge tracking report contains the discharge tracking events from the previous day. The files for this job are saved in your designated cloud storage container in the `reports/discharge_tracking/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

* Report frequency: Once daily
* Reporting period: Previous day
* Update type: Incremental

The following table lists the Discharge tracking report fields.

> 📘
>
> Decimal values are rounded to the hundredths.

<HTMLBlock>
  {`
  <table>
      <thead>
          <tr>
              <th>Field</th>
              <th>Data type</th>
              <th>Description</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>Org_ID</td>
              <td>string</td>
              <td>Organization ID</td>
          </tr>
          <tr>
              <td>RefDate</td>
              <td>timestamp</td>
              <td>Date the report file was generated</td>
          </tr>
          <tr>
              <td>Account_ID</td>
              <td>int</td>
              <td>Account ID</td>
          </tr>
          <tr>
              <td>CreditTransaction_ID</td>
              <td>bigint</td>
              <td>Credit transaction ID</td>
          </tr>
          <tr>
              <td>DebitTransaction_ID</td>
              <td>bigint</td>
              <td>Debit transaction ID</td>
          </tr>
          <tr>
              <td>Amount</td>
              <td>double</td>
              <td>Discharge amount</td>
          </tr>
          <tr>
              <td>DischargeDateTime</td>
              <td>timestamp</td>
              <td>Date and time of discharge</td>
          </tr>
          <tr>
              <td>day</td>
              <td>int</td>
              <td>Day</td>
          </tr>
          <tr>
              <td>CreditAuthorizationTrackingId</td>
              <td>int</td>
              <td>Credit authorization tracking ID</td>
          </tr>
          <tr>
              <td>DebitAuthorizationTrackingId</td>
              <td>int</td>
              <td>Debit authorization tracking ID</td>
          </tr>      
      </tbody>
  </table>
  `}
</HTMLBlock>
<!-- source:end -->

### Source 5: `docs/data-and-reporting/portfolio-balance-report-files.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/portfolio-balance-report-files · updatedAt: 2026-03-18T15:16:17.000Z

<!-- source:begin path=docs/data-and-reporting/portfolio-balance-report-files.md part=0-end -->

# Portfolio balance report files

The Portfolio balance report contains the portfolio balance events from the previous day. The files for this job are saved in your designated cloud storage container in the `reports/portfolio_balance/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

* Report frequency: Once daily
* Reporting period: Previous day
* Update type: Full

The following table lists the Portfolio balance report fields.

> 📘
>
> Decimal values are rounded to the hundredths.

<HTMLBlock>
  {`
  <table>
      <thead>
          <tr>
              <th>Field</th>
              <th>Data type</th>
              <th>Description</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>Org_ID</td>
              <td>string</td>
              <td>Organization ID.</td>
          </tr>
          <tr>
              <td>RefDate</td>
              <td>date</td>
              <td>Date that the Portfolio balance report file was generated</td>
          </tr>
          <tr>
              <td>Account_ID</td>
              <td>int</td>
              <td>Account ID</td>
          </tr>
          <tr>
              <td>Program_ID</td>
              <td>int</td>
              <td>Program ID</td>
          </tr>
          <tr>
              <td>DueDays</td>
              <td>int</td>
              <td>Number of days account has been in arrears</td>
          </tr>
          <tr>
              <td>AccountStatus</td>
              <td>string</td>
              <td>Account status</td>
          </tr>
          <tr>
              <td>BalanceType</td>
              <td>string</td>
              <td>Balance type: - OverdueRefinancing– Sum of overdue debts <br> - Refinancing: Sum of debts in refinancing/revolving <br> - AccruedRefinancing: Sum of accumulated revolving interest charges and IOF <br> - AccruedOverdue: Sum of accumulated late payment charges and fines <br> - InterestRefinancing: Sum of accumulated revolving interest charges on current cycle debts <br> - FixedIOFRefinancing: Sum of the accumulated fixed IOF charges of the current cycle <br> - IofRefinancing: Sum of accumulated IOF charges for the current cycle <br> - DefaultOverdue: Sum of accumulated deadweight charges of the current cycle <br> - FineOverdue: Sum of accumulated fines for the current cycle <br> - StatementRefinancing: Sum of invoice installments <br> - RefinancingPurchase: Sum of installment purchases <br> - OtherDebts: Sum of other debt</td>
          </tr>
          <tr>
              <td>Balance</td>
              <td>double</td>
              <td>Total balance</td>
          </tr>
      </tbody>
  </table>
  `}
</HTMLBlock>
<!-- source:end -->

### Source 6: `docs/data-and-reporting/transactions-balance-report-files.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/transactions-balance-report-files · updatedAt: 2026-03-18T15:16:18.000Z

<!-- source:begin path=docs/data-and-reporting/transactions-balance-report-files.md part=0-end -->

# Transactions balance report files

The Transactions balance report contains the transactions balances from the previous day. The files for this job are saved in your designated cloud storage container in the `reports/transactions_balance/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

* Report frequency: Once daily
* Reporting period: Previous day
* Update type: Incremental

The following table lists the Transactions balance report fields.

> 📘
>
> Decimal values are rounded to the hundredths.

<HTMLBlock>
  {`
  <table>
      <thead>
          <tr>
              <th>Field</th>
              <th>Data type</th>
              <th>Description</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>Org_ID</td>
              <td>string</td>
              <td>Organization ID</td>
          </tr>
          <tr>
              <td>RefDate</td>
              <td>timestampdate</td>
              <td>File creation date</td>
          </tr>
          <tr>
              <td>Account_ID</td>
              <td>int</td>
              <td>Account ID</td>
          </tr>
          <tr>
              <td>Statement_ID</td>
              <td>int</td>
              <td>Statement ID</td>
          </tr>
          <tr>
              <td>Balance</td>
              <td>double</td>
              <td>Invoice balance</td>
          </tr>
          <tr>
              <td>CicleClosingDate</td>
              <td>date</td>
              <td>Cycle closing date</td>
          </tr>
          <tr>
              <td>DueDate</td>
              <td>date</td>
              <td>Due date</td>
          </tr>
          <tr>
              <td>DueDays</td>
              <td>int</td>
              <td>Number of days the account has been in arrears</td>
          </tr>
          <tr>
              <td>Type</td>
              <td>string</td>
            <td>Balance record type: <br>- <code>ROTATIVO</code> (Revolving) <br>- <code>CREDOR</code> (Creditor)<br>- <code>CORRENTE</code> (Current)<br>- <code>CORTADA</code> (Cut)<br>- <code>FUTURA</code> (Future)</td>
          </tr>
          <tr>
              <td>Program_ID</td>
              <td>int</td>
              <td>Program ID</td>
          </tr>
          <tr>
              <td>ProgramName</td>
              <td>string</td>
              <td>Program name</td>
          </tr>
      </tbody>
  </table>
  `}
</HTMLBlock>
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/accounts-analytic-report-files.md`: updatedAt 2026-03-18T15:16:09.000Z.
- `docs/data-and-reporting/accounts-balances-report-files.md`: updatedAt 2026-03-18T15:16:11.000Z.
- `docs/data-and-reporting/billing-report-files.md`: updatedAt 2026-03-18T15:16:14.000Z.
- `docs/data-and-reporting/discharge-tracking-report-files.md`: updatedAt 2026-03-18T15:16:15.000Z.
- `docs/data-and-reporting/portfolio-balance-report-files.md`: updatedAt 2026-03-18T15:16:17.000Z.
- `docs/data-and-reporting/transactions-balance-report-files.md`: updatedAt 2026-03-18T15:16:18.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/accounts-analytic-report-files.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accounts-analytic-report-files | `c0add47b6614b7a3…` | 2026-03-18T15:16:09.000Z |
| `docs/data-and-reporting/accounts-balances-report-files.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accounts-balances-report-files | `bf013a28e052e410…` | 2026-03-18T15:16:11.000Z |
| `docs/data-and-reporting/billing-report-files.md` | whole document | https://developers.pismo.io/pismo-docs/docs/billing-report-files | `e1bc0852ea3a16b1…` | 2026-03-18T15:16:14.000Z |
| `docs/data-and-reporting/discharge-tracking-report-files.md` | whole document | https://developers.pismo.io/pismo-docs/docs/discharge-tracking-report-files | `5257144c55513912…` | 2026-03-18T15:16:15.000Z |
| `docs/data-and-reporting/portfolio-balance-report-files.md` | whole document | https://developers.pismo.io/pismo-docs/docs/portfolio-balance-report-files | `db9dd4150ebb4474…` | 2026-03-18T15:16:17.000Z |
| `docs/data-and-reporting/transactions-balance-report-files.md` | whole document | https://developers.pismo.io/pismo-docs/docs/transactions-balance-report-files | `0df24d318179a775…` | 2026-03-18T15:16:18.000Z |

## Related knowledge units

- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
