---
ku_id: KU-RPT-accounting-events-report-files
title: Accounting events report files
category: reports_and_data_files
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/accounting-events-report-files.md
  sha256: 0d2bf541e58171847575c4542b08db0235eaa13dc2dfea8a8c648bea088cd084
  url: https://developers.pismo.io/pismo-docs/docs/accounting-events-report-files
  role: primary_guide
  updated_at: '2026-04-09T14:21:39.000Z'
operations: []
related_kus:
- KU-CORE-processing-codes-and-transaction-types
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Accounting events report files

**KU ID:** `KU-RPT-accounting-events-report-files` · **Category:** Reports and data files · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/accounting-events-report-files.md`:

> The accounting events report contains the accounting events from the previous day. The files for this job are saved in your designated cloud storage container in the `/reports/accounting_events/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/accounting-events-report-files.md`: Accounting events report files; Sample accounting events files; CSV format; JSON format; HTML format

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/accounting-events-report-files.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accounting-events-report-files · updatedAt: 2026-04-09T14:21:39.000Z

<!-- source:begin path=docs/data-and-reporting/accounting-events-report-files.md part=0-end -->

# Accounting events report files

The accounting events report contains the accounting events from the previous day. The files for this job are saved in your designated cloud storage container in the `/reports/accounting_events/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

* Report frequency: Once daily
* Reporting period: Previous day
* Update type: Incremental

The following table lists the accounting events report fields.

<Callout icon="📘" theme="info">
  Decimal values are rounded to the hundredths.
</Callout>

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
              <td>ID of the org to which the event belongs</td>
          </tr>
          <tr>
              <td>CreatedAt</td>
              <td>timestamp</td>
              <td>Date the report file was generated <br/>(YYYY-MM-DD HH:MM:SS.sssssssss)</td>
          </tr>
          <tr>
              <td>EventDate</td>
              <td>date</td>
              <td>Event date in ISO 8601 (YYYY-MM-DD)</td>
          </tr>
          <tr>
              <td>DebitAccount</td>
              <td>string</td>
              <td>ID of the account debited by accounting entry</td>
          </tr>
          <tr>
              <td>CreditAccount</td>
              <td>string</td>
              <td>ID of the account credited by accounting entry</td>
          </tr>
          <tr>
              <td>EntryType_ID</td>
              <td>bigint</td>
              <td>ID of the accounting entry type</td>
          </tr>
          <tr>
              <td>Description</td>
              <td>string</td>
              <td>Event description</td>
          </tr>
          <tr>
              <td>Account_ID</td>
              <td>int</td>
              <td>Account ID</td>
          </tr>
          <tr>
              <td>Amount</td>
              <td>double</td>
              <td>Transaction amount and currency code</td>
          </tr>
          <tr>
              <td>Program_ID</td>
              <td>int</td>
              <td>ID of the program to which the transaction belongs</td>
          </tr>
          <tr>
              <td>ProgramName</td>
              <td>string</td>
              <td>Name of the program to which the transaction belongs</td>
          </tr>
          <tr>
              <td>BrandName</td>
              <td>string</td>
              <td>Card brand</td>
          </tr>
          <tr>
              <td>Transaction_ID</td>
              <td>bigint</td>
              <td>Transaction ID</td>
          </tr>
          <tr>
              <td>Authorization_ID</td>
              <td>bigint</td>
              <td>Authorization ID</td>
          </tr>
          <tr>
              <td>RefDate</td>
              <td>timestamp</td>
              <td>Date the accounting_events file was created in the bucket <br/>(YYYY-MM-DD HH:MM:SS.sssssssss)</td>
          </tr>
          <tr>
              <td>ProcessingCode</td>
              <td>string</td>
              <td>Defines the operation type, which is used either in the network or in the non-network operations</td>
          </tr>
          <tr>
              <td>ProcessingCodeDescription</td>
              <td>string</td>
              <td>Description of the processing code</td>
          </tr>
          <tr>
              <td>Event_ID</td>
              <td>int</td>
              <td>ID that identifies the business event</td>
          </tr>
          <tr>
              <td>AccountEntry_ID</td>
              <td>int</td>
              <td>ID that identifies the accounting entry</td>
          </tr>
          <tr>
              <td>DebitCostCenter</td>
              <td>string</td>
              <td>Debit cost center</td>
          </tr>
          <tr>
              <td>CreditCostCenter</td>
              <td>string</td>
              <td>Credit cost center</td>
          </tr>
          <tr>
              <td>AuthorizationDate</td>
              <td>date</td>
              <td>Authorization date in ISO 8601 (YYYY-MM-DD)</td>
          </tr>
          <tr>
              <td>InstallmentNumber</td>
              <td>int</td>
              <td>Sequential number that represents the order of the installment</td>
          </tr>
      </tbody>
  </table>
  `}
</HTMLBlock>

# Sample accounting events files

The report file is delivered to the storage container in the PARQUET file format. (For more information, refer to [Apache Parquet](https://parquet.apache.org/). The examples in this section are in the CSV, JSON, and HTML formats for readability.

The file contents are the same for any type of program related to the records. The credit, debit, or prepaid program records differ only in their descriptions and codes. For more information on standard processing codes associated with Pismo program types, refer to [Processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types).

## CSV format

The following example illustrates the file layout and provides sample contents of the accounting events file. The file layout corresponds to the layout of the file in PARQUET format.

```Text CSV
Org_ID,CreatedAt,EventDate,DebitAccount,CreditAccount,EntryType_ID,Description,Account_ID,Amount,Program_ID,ProgramName,BrandName,Transaction_ID,Authorization_ID,RefDate,ProcessingCode,ProcessingCodeDescription,Event_ID,AccountEntry_ID,DebitCostCenter,CreditCostCenter,AuthorizationDate,InstallmentNumber
TN-0000-0000-0000-0000-0000-0000-0000,57676000000000,2023-01-18T00:00:00.000Z,0,0,101,PURCHASE,12345678,85.18,999,CREDIT PROGRAM,MASTERCARD,720160876,2371961,19250276000000,0,PURCHASE,98090944,100181032,0,0,2023-01-18,1
TN-0000-0000-0000-0000-0000-0000-0000,49605000000000,2023-01-18T00:00:00.000Z,0,0,123,WITHDRAWAL,102414567,10.03,2895,CREDIT - Gold,MASTERCARD,720158888,2371962,19250276000000,1,LOCAL WITHDRAWAL,98088888,100179999,0,0,2023-01-18,5
TN-0000-0000-0000-0000-0000-0000-0000,83334000000000,2023-01-18T00:00:00.000Z,0,0,320,CREDIT TRANSFER,12345678,1000,888,PREPAID PROGRAM,MASTERCARD,720164231,2371963,19250276000000,7200,CREDIT TRANSFER,98092269,100182549,0,0,2023-01-18,12
TN-0000-0000-0000-0000-0000-0000-0000,83604000000000,2023-01-18T00:00:00.000Z,0,0,304,DEBIT TRANSFER,12345678,20000,444,PREPAID PROGRAM,MASTERCARD,720164235,2371964,19250276000000,7000,DEBIT TRANSFER,98092273,100182553,0,0,2023-01-18,2
TN-0000-0000-0000-0000-0000-0000-0000,32759000000000,2023-01-18T00:00:00.000Z,0,0,243,PIX CANCELATION,12345678,20.1,777,PREPAID PROGRAM,MASTERCARD,720106712,2371965,19250276000000,11001,PIX CANCELATION,98088094,100178174,0,0,2023-01-18,1
```

<Callout icon="📘" theme="info">
  You can [**download a sample\_accounting\_events** CSV file](https://pismoassets.pismo.io/pismo-docs/sample_accounting_events.csv) using this link.
</Callout>

## JSON format

The following example illustrates sample contents of the accounting events file in JSON format for readability.

<details>
  <summary>JSON - Sample accounting events file</summary>

  ```json
  {
      "Org_ID": "TN-0000-0000-0000-0000-0000-0000-0000",
      "CreatedAt": 57676000000000,
      "EventDate": "2023-01-18T00:00:00.000Z",
      "DebitAccount": "0",
      "CreditAccount": "0",
      "EntryType_ID": 101,
      "Description": "PURCHASE",
      "Account_ID": 12345678,
      "Amount": 85.18,
      "Program_ID": 999,
      "ProgramName": "CREDIT PROGRAM",
      "BrandName": "MASTERCARD",
      "Transaction_ID": 720160876,
      "Authorization_ID": 2371961,
      "RefDate": 19250276000000,
      "ProcessingCode": "00",
      "ProcessingCodeDescription": "PURCHASE",
      "Event_ID": 98090944,
      "AccountEntry_ID": 100181032,
      "DebitCostCenter": "0",
      "CreditCostCenter": "0",
      "AuthorizationDate": "2023-01-18",
      "InstallmentNumber": 1
  }
  {
      "Org_ID": "TN-0000-0000-0000-0000-0000-0000-0000",
      "CreatedAt": 49605000000000,
      "EventDate": "2023-01-18T00:00:00.000Z",
      "DebitAccount": "0",
      "CreditAccount": "0",
      "EntryType_ID": 123,
      "Description": "WITHDRAWAL",
      "Account_ID": 102414567,
      "Amount": 10.03,
      "Program_ID": 2895,
      "ProgramName": "CREDIT - Gold",
      "BrandName": "MASTERCARD",
      "Transaction_ID": 720158888,
      "Authorization_ID": 2371962,
      "RefDate": 19250276000000,
      "ProcessingCode": "01",
      "ProcessingCodeDescription": "LOCAL WITHDRAWAL",
      "Event_ID": 98088888,
      "AccountEntry_ID": 100179999,
      "DebitCostCenter": "0",
      "CreditCostCenter": "0",
      "AuthorizationDate": "2023-01-18",
      "InstallmentNumber": 5
  }
  {
      "Org_ID": "TN-0000-0000-0000-0000-0000-0000-0000",
      "CreatedAt": 83334000000000,
      "EventDate": "2023-01-18T00:00:00.000Z",
      "DebitAccount": "0",
      "CreditAccount": "0",
      "EntryType_ID": 320,
      "Description": "CREDIT TRANSFER",
      "Account_ID": 12345678,
      "Amount": 1000,
      "Program_ID": 888,
      "ProgramName": "PREPAID PROGRAM",
      "BrandName": "MASTERCARD",
      "Transaction_ID": 720164231,
      "Authorization_ID": 2371963,
      "RefDate": 19250276000000,
      "ProcessingCode": "007200",
      "ProcessingCodeDescription": "CREDIT TRANSFER",
      "Event_ID": 98092269,
      "AccountEntry_ID": 100182549,
      "DebitCostCenter": "0",
      "CreditCostCenter": "0",
      "AuthorizationDate": "2023-01-18",
      "InstallmentNumber": 12
  }
  {
      "Org_ID": "TN-0000-0000-0000-0000-0000-0000-0000",
      "CreatedAt": 83604000000000,
      "EventDate": "2023-01-18T00:00:00.000Z",
      "DebitAccount": "0",
      "CreditAccount": "0",
      "EntryType_ID": 304,
      "Description": "DEBIT TRANSFER",
      "Account_ID": 12345678,
      "Amount": 20000,
      "Program_ID": 444,
      "ProgramName": "PREPAID PROGRAM",
      "BrandName": "MASTERCARD",
      "Transaction_ID": 720164235,
      "Authorization_ID": 2371964,
      "RefDate": 19250276000000,
      "ProcessingCode": "007000",
      "ProcessingCodeDescription": "DEBIT TRANSFER",
      "Event_ID": 98092273,
      "AccountEntry_ID": 100182553,
      "DebitCostCenter": "0",
      "CreditCostCenter": "0",
      "AuthorizationDate": "2023-01-18",
      "InstallmentNumber": 2
  }
  {
      "Org_ID": "TN-0000-0000-0000-0000-0000-0000-0000",
      "CreatedAt": 32759000000000,
      "EventDate": "2023-01-18T00:00:00.000Z",
      "DebitAccount": "0",
      "CreditAccount": "0",
      "EntryType_ID": 243,
      "Description": "PIX CANCELATION",
      "Account_ID": 12345678,
      "Amount": 20.1,
      "Program_ID": 777,
      "ProgramName": "PREPAID PROGRAM",
      "BrandName": "MASTERCARD",
      "Transaction_ID": 720106712,
      "Authorization_ID": 2371965,
      "RefDate": 19250276000000,
      "ProcessingCode": "011001",
      "ProcessingCodeDescription": "PIX CANCELATION",
      "Event_ID": 98088094,
      "AccountEntry_ID": 100178174,
      "DebitCostCenter": "0",
      "CreditCostCenter": "0",
      "AuthorizationDate": "2023-01-18",
      "InstallmentNumber": 1
  }
  ```
</details>

## HTML format

The following example illustrates the file layout and provides sample contents of the accounting events. The file layout here corresponds to the layout of the file in PARQUET format.

<HTMLBlock>
  {`
  <button class="modal-button" href="#htmlTable2">Sample<i class="icon-maximize2"onclick="event.target.parentElement.click()"></i></button>

  <dialog class="modal" id="htmlTable2">
  <form class="form" method="dialog">
  <div class="modal-header">  
  <h2>Sample accounting events file</h2>
  <span class="close">&times;</span>
  </div>
  <div class="table-wrapper">

  <table>

  <thead><tr><th>Org_ID</th>
  <th>CreatedAt</th>
  <th>EventDate</th>
  <th>DebitAccount</th>
  <th>CreditAccount</th>
  <th>EntryType_ID</th>
  <th>Description</th>
  <th>Account_ID</th>
  <th>Amount</th>
  <th>Program_ID</th>
  <th>ProgramName</th>
  <th>BrandName</th>
  <th>Transaction_ID</th>
  <th>Authorization_ID</th>  
  <th>RefDate</th>
  <th>ProcessingCode</th>
  <th>ProcessingCodeDescription</th>
  <th>Event_ID</th>
  <th>AccountEntry_ID</th>
  <th>DebitCostCenter</th>
  <th>CreditCostCenter</th>
  <th>AuthorizationDate</th>  
  <th>InstallmentNumber</th>  
  </tr></thead>
  <tbody><tr>
  <td>TN-0000-0000-0000-0000-0000-0000-0000</td>
  <td align="right">57676000000000</td>
  <td>2023-01-18T00:00:00.000Z</td>
  <td>0</td>
  <td>0</td>
  <td align="right">101</td>
  <td>PURCHASE</td>
  <td align="right">12345678</td>
  <td align="right">85.18</td>
  <td align="right">999</td>
  <td>CREDIT PROGRAM</td>
  <td>MASTERCARD</td>
  <td align="right">720160876</td>
  <td align="right">2371961</td>  
  <td align="right">19250276000000</td>
  <td align="right">00</td>
  <td>PURCHASE</td>
  <td align="right">98090944</td>
  <td align="right">100181032</td>
  <td>0</td>
  <td>0</td>
  <td>2023-01-18</td>
  <td>1</td>    
  </tr>
  <tr>
  <td>TN-0000-0000-0000-0000-0000-0000-0000</td>
  <td align="right">49605000000000</td>
  <td>2023-01-18T00:00:00.000Z</td>
  <td>0</td>
  <td>0</td>
  <td align="right">123</td>
  <td>WITHDRAWAL</td>
  <td align="right">102414567</td>
  <td align="right">10.03</td>
  <td align="right">2895</td>
  <td>CREDIT - Gold</td>
  <td>MASTERCARD</td>
  <td align="right">720158888</td>
  <td align="right">2371962</td>    
  <td align="right">19250276000000</td>
  <td align="right">01</td>
  <td>LOCAL WITHDRAWAL</td>
  <td align="right">98088888</td>
  <td align="right">100179999</td>
  <td>0</td>
  <td>0</td>
  <td>2023-01-18</td>  
  <td>5</td>    
  </tr>
  <tr>
  <td>TN-0000-0000-0000-0000-0000-0000-0000</td>
  <td align="right">83334000000000</td>
  <td>2023-01-18T00:00:00.000Z</td>
  <td>0</td>
  <td>0</td>
  <td align="right">320</td>
  <td>CREDIT TRANSFER</td>
  <td align="right">12345678</td>
  <td align="right">1000</td>
  <td align="right">888</td>
  <td>PREPAID PROGRAM</td>
  <td>MASTERCARD</td>
  <td align="right">720164231</td>
  <td align="right">2371963</td>    
  <td align="right">19250276000000</td>
  <td align="right">7200</td>
  <td>CREDIT TRANSFER</td>
  <td align="right">98092269</td>
  <td align="right">100182549</td>
  <td>0</td>
  <td>0</td>
  <td>2023-01-18</td>
  <td>12</td>    
  </tr>
  <tr>
  <td>TN-0000-0000-0000-0000-0000-0000-0000</td>
  <td align="right">83604000000000</td>
  <td>2023-01-18T00:00:00.000Z</td>
  <td>0</td>
  <td>0</td>
  <td align="right">304</td>
  <td>DEBIT TRANSFER</td>
  <td align="right">12345678</td>
  <td align="right">2371964</td>    
  <td align="right">20000</td>
  <td align="right">444</td>
  <td>PREPAID PROGRAM</td>
  <td>MASTERCARD</td>
  <td align="right">720164235</td>
  <td align="right">19250276000000</td>
  <td align="right">7000</td>
  <td>DEBIT TRANSFER</td>
  <td align="right">98092273</td>
  <td align="right">100182553</td>
  <td>0</td>
  <td>0</td>
  <td>2023-01-18</td>  
  <td>2</td>    
  </tr>
  <tr>
  <td>TN-0000-0000-0000-0000-0000-0000-0000</td>
  <td align="right">32759000000000</td>
  <td>2023-01-18T00:00:00.000Z</td>
  <td>0</td>
  <td>0</td>
  <td align="right">243</td>
  <td>PIX CANCELATION</td>
  <td align="right">12345678</td>
  <td align="right">20.1</td>
  <td align="right">777</td>
  <td>PREPAID PROGRAM</td>
  <td>MASTERCARD</td>
  <td align="right">720106712</td>
  <td align="right">2371965</td>    
  <td align="right">19250276000000</td>
  <td align="right">11001</td>
  <td>PIX CANCELATION</td>
  <td align="right">98088094</td>
  <td align="right">100178174</td>
  <td>0</td>
  <td>0</td>
  <td>2023-01-18</td>  
  <td>1</td>    
  </tr>
  </tbody></table>

   </div>  
    </form>
  </dialog>
  `}
</HTMLBlock>
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/accounting-events-report-files.md`: updatedAt 2026-04-09T14:21:39.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/accounting-events-report-files.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accounting-events-report-files | `0d2bf541e5817184…` | 2026-04-09T14:21:39.000Z |

## Related knowledge units

- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
