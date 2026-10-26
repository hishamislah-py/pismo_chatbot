---
ku_id: KU-RPT-transactions-denied
title: Transactions denied report files
category: reports_and_data_files
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/transactions-denied.md
  sha256: b5b7376b72600d9033791e638021035d7afd060bbda8cb2bc2eddb50785a92ba
  url: https://developers.pismo.io/pismo-docs/docs/transactions-denied
  role: primary_guide
  updated_at: '2026-03-18T15:16:19.000Z'
operations: []
related_kus:
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Transactions denied report files

**KU ID:** `KU-RPT-transactions-denied` · **Category:** Reports and data files · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/transactions-denied.md`:

> The Transactions denied report contains the denied transactions from the previous day. The files for this job are saved in your designated cloud storage container in the `reports/transactions_denied/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/transactions-denied.md`: Transactions denied report files

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/transactions-denied.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/transactions-denied · updatedAt: 2026-03-18T15:16:19.000Z

<!-- source:begin path=docs/data-and-reporting/transactions-denied.md part=0-end -->

# Transactions denied report files

The Transactions denied report contains the denied transactions from the previous day. The files for this job are saved in your designated cloud storage container in the `reports/transactions_denied/` subfolder. For more information, refer to [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports).

* Report frequency: Once daily
* Reporting period: Previous day
* Update type: Incremental

The following table lists the Transactions balance report fields.

> 📘
>
> The report's decimal values are rounded to the hundredths.

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
              <td>Pismo organization/tenant ID</td>
          </tr>
          <tr>
              <td>RefDate</td>
              <td>date</td>
              <td>File generation date</td>
          </tr>
          <tr>
              <td>EventDateHour</td>
              <td>timestamp</td>
              <td>Date and time Network/Acquirer message received. This field represents the value contained in fields 12 (Time) and 13 (Date) of the Card Network Specification. If these values are present, they are used without validations and since the network only sends the day and month, the current year is assumed. If they are not present, the current time of the authorization is used (UTC-3).</td>
          </tr>
          <tr>
              <td>Account_ID</td>
              <td>integer</td>
              <td>Pismo account ID. This information is fetched using the Card used in the authorization. If no card is found, this information will not be present in the DECLINED event.</td>
          </tr>
          <tr>
              <td>Card_ID</td>
              <td>bigint</td>
              <td>Pismo card ID. If no card is found, based on the PAN received, this information will not be present in the DECLINED event.</td>
          </tr>
          <tr>
              <td>EntryMode</td>
              <td>integer</td>
              <td>How the payment was entered.</td>
          </tr>
          <tr>
              <td>MerchantName</td>
              <td>string</td>
              <td>Merchant&#39;s &#39;doing business as&#39; name. This field represents the value received in field 43, subfield 1, of the Card Network Specification.</td>
          </tr>
          <tr>
              <td>OperationName</td>
              <td>string</td>
              <td>The name of the operation during the authorization stage: Processing code name.</td>
          </tr>
          <tr>
              <td>NumberOfInstallments</td>
              <td>integer</td>
              <td>In purchases with installments, this field represents the number of installments for which the authorization was requested. For any operation other than purchase with installments, this value should be 1.</td>
          </tr>
          <tr>
              <td>LocalCurrencyCode</td>
              <td>string</td>
              <td>Currency code of the place where the authorization was requested. The value received in field 49 of the Card Network Specification.</td>
          </tr>
          <tr>
              <td>LocalCurrencyTransactionAmount</td>
              <td>double</td>
              <td>Amount in local currency where the authorization was requested. The value received in field 4 of the Card Network Specification.</td>
          </tr>
          <tr>
              <td>SettlementCurrencyCode</td>
              <td>string</td>
              <td>Currency code of the settlement amount received in the authorization message - the value received in field 50 of the Card Network Specification.</td>
          </tr>
          <tr>
              <td>PrincipalAmount</td>
              <td>double</td>
              <td>Calculated amount of the authorization without taxes or fees in the cardholder&#39;s currency. For Declined transactions this field may be null, since no calculation was performed.</td>
          </tr>
          <tr>
              <td>MerchantCategory_ID</td>
              <td>bigint</td>
              <td>Merchant category code based on the merchant&#39;s type of business or service. This field represents the value received in field 18 of the Card. Network Specification.</td>
          </tr>
          <tr>
              <td>AuthorizationResponseCode</td>
              <td>string</td>
              <td>Response code that the authorization platform assigns to the authorization request. Indicates whether it was declined or not.</td>
          </tr>
      </tbody>
  </table>
  `}
</HTMLBlock>
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/transactions-denied.md`: updatedAt 2026-03-18T15:16:19.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/transactions-denied.md` | whole document | https://developers.pismo.io/pismo-docs/docs/transactions-denied | `b5b7376b72600d90…` | 2026-03-18T15:16:19.000Z |

## Related knowledge units

- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
