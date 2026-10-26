---
ku_id: KU-CORE-accounting-scripts-examples
title: Accounting scripts examples
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/accounting-scripts-examples.md
  sha256: 80e8d59127d2b08b942ca58026405134f9fa07fc017b3144c82e9c7f865cfcd5
  url: https://developers.pismo.io/pismo-docs/docs/accounting-scripts-examples
  role: primary_guide
  updated_at: '2026-03-18T22:57:09.000Z'
operations:
- InstallmentPaymentsv4
related_kus:
- KU-API-revolving-credit-statements--refinancing
- KU-CRED-agreements
- KU-EVT-catalogue-balance
grouping_rationale: single source page
---

# Accounting scripts examples

**KU ID:** `KU-CORE-accounting-scripts-examples` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/accounting-scripts-examples.md`:

> This guide currently provides one detailed example how the Pismo platform handles accounting in the case of refinancing. The guide will be enhanced to include other use case examples.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/accounting-scripts-examples.md`: Accounting scripts examples; Refinancing example; Transactions and accounting events; Refinancing credit and refinancing contract; First installment; Subsequent installments; Due date of each installment; Daily interest accounting events; Transactions and accounting events details; Transactions details; Accounting events details

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/accounting-scripts-examples.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accounting-scripts-examples · updatedAt: 2026-03-18T22:57:09.000Z

<!-- source:begin path=docs/core-platform/accounting-scripts-examples.md part=0-end -->

# Accounting scripts examples

This guide currently provides one detailed example how the Pismo platform handles accounting in the case of refinancing. The guide will be enhanced to include other use case examples.

# Refinancing example

Refinancing is the process of creating a new credit contract agreement for an existing credit card debt. The new agreement has new terms, such as the interest rate and applicable taxes. Refinancing on the Pismo platform utilizes the [installment agreement](https://developers.pismo.io/pismo-docs/docs/installment-agreements) functionality.

In this example, assume the card holder has R$3526.64 in debt and receives a credit from the issuer to settle the debt under a refinancing agreement. The card holder has agreed to repay the debt in three installments on specified dates in July, August, and September.

The total amount of the refinancing contract (principal + interest + tax) is R$4591.68 and is to be paid over three installments. The total IOF (financial tax in Brazil) is R$32.31, also split over three installments.

|                     | Amount (R$) | Principal (R$) | Interest (R$) | IOF (R$)  |
| :------------------ | :---------- | :------------- | :------------ | :-------- |
| Installment 1       | 1530.56     | 1025.87        | 497.55        | 7.14      |
| Installment 2       | 1530.56     | 1166.93        | 353.13        | 10.50     |
| Installment 3       | 1530.56     | 1333.84        | 182.05        | 14.67     |
| **Contract totals** | **4591.68** | **3526.64**    | **1032.73**   | **32.31** |

## Transactions and accounting events

In this refinancing example, the platform generates transactions and the corresponding transaction events and accounting events on the following dates.

| Date         | Platform action                                 |
| :----------- | :---------------------------------------------- |
| 1 July       | Platform creates refinancing contract           |
| 20 July      | Cycle close for the 1st refinancing installment |
| 30 July      | Due date of the 1st refinancing installment     |
| 20 August    | Cycle close of the 2nd refinancing installment  |
| 30 August    | Due date of the 2nd refinancing installment     |
| 20 September | Cycle close for the 3rd refinancing installment |
| 30 September | Due date of the 3rd refinancing installment     |

The Pismo platform creates transactions and accounting events as follows (details provided in the sections below).

* [Refinancing credit and refinancing contract](https://developers.pismo.io/pismo-docs/docs/accounting-scripts-examples#refinancing-credit-and-refinancing-contract) and [first installment](https://developers.pismo.io/pismo-docs/docs/accounting-scripts-examples#first-installment) transactions and events on the same day
* Transactions and events for [subsequent installments](https://developers.pismo.io/pismo-docs/docs/accounting-scripts-examples#subsequent-installments) at later dates
* Additional accounting events on the [due date of each installment](https://developers.pismo.io/pismo-docs/docs/accounting-scripts-examples#due-date-of-each-installment)
* Additional [daily interest accounting events](https://developers.pismo.io/pismo-docs/docs/accounting-scripts-examples#daily-interest-accounting-events)

### Refinancing credit and refinancing contract

At the time of the new refinancing contract, the Pismo platform creates two transactions: refinancing credit transaction (701) and refinancing contract transaction (703).

| Transaction type | Transaction type description | Transaction description                                                                                                                                                                                                                                                                                                                                                                                        |
| :--------------- | :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 701              | Refinancing credit           | Refinancing credit transaction represents the credit that the cardholder receives to cover their past debt and to pay it to the issuer bank in installments. This transaction amount includes the principal amount only, as specified in the [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) endpoint.                                                                                                   |
| 703              | Refinancing contract         | Refinancing contract transaction is not available on the cardholder's statement as it is created for accounting purposes only. This transaction amount includes the principal amount (the same amount as in the refinancing credit 701 transaction) + interest + any taxes (in Brazil, this is usually the total IOF). The platform places total interest in the **Interest amount** field on the transaction. |

At the same time, if the accounting scripts are configured, the Pismo platform creates corresponding accounting events for the refinancing credit and for the refinancing contract.

| Accounting event type | Entry type | Accounting event type description              |
| :-------------------- | :--------- | :--------------------------------------------- |
| 701                   | 701        | Refinancing credit                             |
| 703                   | 2121       | Refinancing contract                           |
| 703                   | 2122       | Refinancing contract interest                  |
| 703                   | 2123       | Refinancing contract IOF (if the IOF is not 0) |

### First installment

When the platform creates transactions and accounting events for the refinancing credit and the refinancing contract, it also creates the following transactions for the first installment.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Transaction type
      </th>

      <th>
        Transaction type description
      </th>

      <th>
        Transaction description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        702
      </td>

      <td>
        Refinancing installment
      </td>

      <td>
        This transaction amount is \[(principal + interest + total IOF) / number of installments]. The platform places interest for this installment in the **Interest amount** field on the transaction.
      </td>
    </tr>

    <tr>
      <td>
        417
      </td>

      <td>
        Installment IOF
      </td>

      <td>
        If `split_iof` is `false` (which is the default), this transaction amount is the total IOF.\
        If `split_iof` is `true`, this transaction amount is (total IOF / number of installments)
      </td>
    </tr>
  </tbody>
</Table>

At the same time, the platform generates the following accounting events for the first installment.

| Accounting event type | Entry type | Accounting event type description |
| :-------------------- | :--------- | :-------------------------------- |
| 702                   | 702        | Refinancing installment           |
| 702                   | 2125       | Refinancing installment interest  |

### Subsequent installments

For each subsequent installment, the platform creates refinancing installment transactions (702 and 417), places them in the appropriate statements, and generates corresponding accounting events (702).

The platform creates as many refinancing installment transactions (702) as the number of installments specified in the [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) endpoint. It also generates separate transactions for each installment IOF transaction (417).

* If `split_iof` is `false`, the platform creates one installment IOF transaction (417) with the full IOF tax amount.
* If  `split_iof` is `true`, the platform splits the IOF tax into installments and creates as many installment IOF transactions (417) as the number of installments.

For the second and remaining installments, the platform generates installments accounting events (702 and 2125) at the closing of the previous cycle.

* For the second installment, the platform generates events at the closing of the first installment's cycle.
* For the third installment, the platform generates events at the closing of the second installment's cycle.

### Due date of each installment

On the due date of each installment's statement, the platform creates the following accounting events (2126 and 2127).

| Accounting event type | Entry type | Accounting event type description         |
| :-------------------- | :--------- | :---------------------------------------- |
| 702                   | 2126       | Refinancing installment due date          |
| 702                   | 2127       | Refinancing installment interest due date |

### Daily interest accounting events

The platform creates daily interest accounting events (2080) based on the platform amortization price model, starting on the following day of the refinancing contract creation and until the last installment's due date.

| Accounting event type | Entry type | Accounting event type description |
| :-------------------- | :--------- | :-------------------------------- |
| 702                   | 2080       | Refinancing daily interest        |

The total amount of the refinancing interest in this example is $R1032.73. The platform calculates the daily refinancing interest and starts sending daily events the next day after creating the contract (in this case, on 2 July). The refinancing daily interest events end on the due date of the last installment (in this case, on 30 September).

## Transactions and accounting events details

The following table provides an overview of the transactions and related accounting events that the platform creates over the term of this example refinancing agreement, with the corresponding dates.

<br />

The following table provides an overview of the transactions and related accounting events that the platform creates over the term of this example refinancing agreement, with the corresponding dates.

<ContentModal label="Transactions and accounting events details" title="Results" modalId="resultsTable" useNextTable openOnHash={false} targetSelector=".rdmd-table-inner > table" />

| Date         | Transaction type | Event type | Entry type | Description                               | Cycle stage     | When it happens                            | What is accounted                                    |
| ------------ | ---------------- | ---------- | ---------- | ----------------------------------------- | --------------- | ------------------------------------------ | ---------------------------------------------------- |
| 1 July       | 701              | 701        | 701        | Refinancing credit                        | Contract        | Refinancing credit: transaction creation   | Principal amount                                     |
| 1 July       | 703              | 703        | 2121       | Refinancing contract                      | Contract        | Refinancing contract: transaction creation | Principal amount + fixed IOF                         |
| 1 July       | 703              | 703        | 2122       | Refinancing contract interest             | Contract        | Refinancing contract: transaction creation | Total interest                                       |
| 1 July       | 703              | 703        | 2123       | Total IOF refinancing                     | Contract        | Refinancing contract: transaction creation | Total IOF                                            |
| 1 July       | 702              | 702        | 702        | Installment refinancing                   | 1st installment | 1st installment: transactions creation     | Installment principal amount + total installment IOF |
| 1 July       | 702              | 702        | 2125       | Installment refinancing interest          | 1st installment | 1st installment: transactions creation     | Installment interest                                 |
| 30 July      | 702              | 702        | 2126       | Installment refinancing due date          | 1st installment | 1st installment: statement due date        | Installment principal amount + total installment IOF |
| 30 July      | 702              | 702        | 2127       | Installment refinancing interest due date | 1st installment | 1st installment: statement due date        | Installment interest                                 |
| 20 July      | 702              | 702        | 702        | Installment refinancing                   | 2nd installment | 1st installment: cycle close               | Installment principal amount + total installment IOF |
| 20 July      | 702              | 702        | 2125       | Installment refinancing interest          | 2nd installment | 1st installment: cycle close               | Installment interest                                 |
| 30 August    | 702              | 702        | 2126       | Installment refinancing due date          | 2nd installment | 2nd installment: statement due date        | Installment principal amount + total installment IOF |
| 30 August    | 702              | 702        | 2127       | Installment refinancing interest due date | 2nd installment | 2nd installment: statement due date        | Installment interest                                 |
| 20 August    | 702              | 702        | 702        | Installment refinancing                   | 3rd installment | 2nd installment: cycle close               | Installment principal amount + total installment IOF |
| 20 August    | 702              | 702        | 2125       | Installment refinancing interest          | 3rd installment | 2nd installment: cycle close               | Installment interest                                 |
| 30 September | 702              | 702        | 2126       | Installment refinancing due date          | 3rd installment | 3rd installment: statement due date        | Installment principal amount + total installment IOF |
| 30 September | 702              | 702        | 2127       | Installment refinancing interest due date | 3rd installment | 3rd installment: statement due date        | Installment interest                                 |

### Transactions details

The following table details the transactions that the platform creates over the course of the three installments specified in this refinancing example.

<ContentModal label="Transactions details" title="Results" modalId="resultsTable" useNextTable openOnHash={false} targetSelector=".rdmd-table-inner > table" />

| Created At | Transaction ID | Authorization ID | Transaction type ID | Description             | Installment | Account ID | Statement ID | Amount (R$) | Interest amount (R$) | Interest rate | IOF amount (R$) |
| ---------- | -------------- | ---------------- | ------------------- | ----------------------- | ----------- | ---------- | ------------ | ----------- | -------------------- | ------------- | --------------- |
| 1 July     | 7949           | 44443972         | 701                 | REFINANCING CREDIT      | 1           | 10267      | 33331091     | 3526.64     | 0                    | 0             | 0               |
| 1 July     | 7971           | 44443972         | 703                 | REFINANCING CONTRACT    |             | 10267      | 33331091     | 4591.68     | 1032.73              | 0.08          | 32.31           |
| 1 July     | 7961           | 44443972         | 417                 | IOF REFINANCING         | 1           | 10267      | 33331091     | 7.14        | 0                    |               | 0               |
| 1 July     | 7962           | 44443972         | 702                 | REFINANCING INSTALLMENT | 1           | 10267      | 33331091     | 1530.56     | 497.55               | 0.08          | 0               |
| 1 July     | 7963           | 44443972         | 417                 | IOF REFINANCING         | 2           | 10267      | 33331099     | 10.50       | 0                    |               | 0               |
| 1 July     | 7964           | 44443972         | 702                 | REFINANCING INSTALLMENT | 2           | 10267      | 33331099     | 1530.56     | 363.63               | 0.08          | 0               |
| 1 July     | 7965           | 44443972         | 417                 | IOF REFINANCING         | 3           | 10267      | 33331092     | 14.67       | 0                    |               | 0               |
| 1 July     | 7966           | 44443972         | 702                 | REFINANCING INSTALLMENT | 3           | 10267      | 33331092     | 1530.56     | 196.73               | 0.08          | 0               |

### Accounting events details

The following table details the accounting events that the platform creates for the refinancing contract.

<ContentModal label="Accounting events details" title="Results" modalId="resultsTable" useNextTable openOnHash={false} targetSelector=".rdmd-table-inner > table" />

| CreatedAt | Transaction\_ID | EventType\_ID | EntryType\_ID | Description                   | Amount (R$) | Amount breakdown             |
| --------- | --------------- | ------------- | ------------- | ----------------------------- | ----------- | ---------------------------- |
| 1 July    | 7949            | 701           | 701           | REFINANCING CREDIT            | 3526.64     | Principal refinancing amount |
| 1 July    | 7971            | 703           | 2121          | REFINANCING CONTRACT          | 3558.95     | Principal + total IOF        |
| 1 July    | 7971            | 703           | 2122          | REFINANCING CONTRACT INTEREST | 1032.73     | Refinancing interest amount  |
| 1 July    | 7971            | 703           | 2123          | REFINANCING CONTRACT IOF      | 32.31       | Total IOF                    |

For installment 1, the platform creates the following accounting events.

<ContentModal label="Installment 1 details" title="Results" modalId="resultsTable" useNextTable openOnHash={false} targetSelector=".rdmd-table-inner > table" />

| CreatedAt | Transaction\_ID | EventType\_ID | EntryType\_ID | Description                                 | Amount (R$) | Amount breakdown                                      |
| --------- | --------------- | ------------- | ------------- | ------------------------------------------- | ----------- | ----------------------------------------------------- |
| 1 July    | 7962            | 702           | 702           | INSTALLMENT REFINANCING                     | 1033.01     | Installment principal amount + installment IOF amount |
| 1 July    | 7962            | 702           | 2125          | INSTALLMENT REFINANCING INTEREST            | 124.06      | Installment interest                                  |
| 30 July   | 7962            | 702           | 2126          | INSTALLMENT REFINANCING - DUE DATE          | 344.16      | Same amount as 702 entry type                         |
| 30 July   | 7962            | 702           | 2127          | INSTALLMENT REFINANCING INTEREST - DUE DATE | 124.06      | Same amount as 2125 entry type                        |

For installment 2, the platform creates the following accounting events.

<ContentModal label="Installment 2 details" title="Results" modalId="resultsTable" useNextTable openOnHash={false} targetSelector=".rdmd-table-inner > table" />

| CreatedAt | Transaction\_ID | EventType\_ID | EntryType\_ID | Description                                 | Amount (R$) | Amount breakdown                                      |
| --------- | --------------- | ------------- | ------------- | ------------------------------------------- | ----------- | ----------------------------------------------------- |
| 20 July   | 7962            | 702           | 702           | INSTALLMENT REFINANCING                     | 1177.43     | Installment principal amount + installment IOF amount |
| 20 July   | 7962            | 702           | 2125          | INSTALLMENT REFINANCING INTEREST            | 497.55      | Installment Interest                                  |
| 30 August | 7962            | 702           | 2126          | INSTALLMENT REFINANCING - DUE DATE          | 1177.43     | Same amount as 702 entry type                         |
| 30 August | 7962            | 702           | 2127          | INSTALLMENT REFINANCING INTEREST - DUE DATE | 497.55      | Same amount as 2125 entry type                        |

For installment 3, the platform creates the following accounting events.

<ContentModal label="Installment 3 details" title="Results" modalId="resultsTable" useNextTable openOnHash={false} targetSelector=".rdmd-table-inner > table" />

| CreatedAt    | Transaction\_ID | EventType\_ID | EntryType\_ID | Description                                 | Amount (R$) | Amount breakdown                                      |
| ------------ | --------------- | ------------- | ------------- | ------------------------------------------- | ----------- | ----------------------------------------------------- |
| 20 August    | 7962            | 702           | 702           | INSTALLMENT REFINANCING                     | 1348.51     | Installment principal amount + installment IOF amount |
| 20 August    | 7962            | 702           | 2125          | INSTALLMENT REFINANCING INTEREST            | 353.13      | Installment Interest                                  |
| 30 September | 7962            | 702           | 2126          | INSTALLMENT REFINANCING - DUE DATE          | 1348.51     | Same amount as 702 entry type                         |
| 30 September | 7962            | 702           | 2127          | INSTALLMENT REFINANCING INTEREST - DUE DATE | 353.13      | Same amount as 2125 entry type                        |

The following table is the sample of the accounting events that the platform creates for daily refinancing interest.

<ContentModal label="Accounting events for daily refinancing interest" title="Results" modalId="resultsTable" useNextTable openOnHash={false} targetSelector=".rdmd-table-inner > table" />

| CreatedAt | Event\_ID  | EventType\_ID | EntryType\_ID | Description                | Amount (R$) |
| --------- | ---------- | ------------- | ------------- | -------------------------- | ----------- |
| 2 July    | 6960654736 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.050      |
| 3 July    | 6973498106 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.110      |
| 4 July    | 6988041360 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.180      |
| 5 July    | 7001826140 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.240      |
| 6 July    | 7014912482 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.310      |
| 7 July    | 7023912622 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.370      |
| 8 July    | 7036899568 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.440      |
| 9 July    | 7051194857 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.500      |
| 10 July   | 7063575288 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.570      |
| 11 July   | 7075446886 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.630      |
| 12 July   | 7087370490 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.700      |
| 13 July   | 7100243600 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.760      |
| 14 July   | 7109476026 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.830      |
| 15 July   | 7119521432 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.900      |
| 16 July   | 7133044455 | 702           | 2080          | REFINANCING DAILY INTEREST | 15.970      |
| 17 July   | 7144262608 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.030      |
| 18 July   | 7157261934 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.100      |
| 19 July   | 7169670284 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.170      |
| 20 July   | 7181258647 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.240      |
| 21 July   | 7189337287 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.310      |
| 22 July   | 7198540318 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.380      |
| 23 July   | 7210635631 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.440      |
| 24 July   | 7222625337 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.510      |
| 25 July   | 7235530965 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.580      |
| 26 July   | 7248063719 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.650      |
| 27 July   | 7260088697 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.720      |
| 28 July   | 7267987577 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.800      |
| 29 July   | 7277731612 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.870      |
| 30 July   | 7290373987 | 702           | 2080          | REFINANCING DAILY INTEREST | 16.940      |
| 31 July   | 7303522893 | 702           | 2080          | REFINANCING DAILY INTEREST | 17.150      |
| 1 August  | 7315782226 | 702           | 2080          | REFINANCING DAILY INTEREST | 10.610      |
| 2 August  | 7328693458 | 702           | 2080          | REFINANCING DAILY INTEREST | 10.650      |
| 3 August  | 7341701157 | 702           | 2080          | REFINANCING DAILY INTEREST | 10.700      |
| 4 August  | 7350324547 | 702           | 2080          | REFINANCING DAILY INTEREST | 10.740      |
| 5 August  | 7359730063 | 702           | 2080          | REFINANCING DAILY INTEREST | 10.790      |
| 6 August  | 7368534100 | 702           | 2080          | REFINANCING DAILY INTEREST | 10.830      |
| 7 August  | 7371923474 | 702           | 2080          | REFINANCING DAILY INTEREST | 10.880      |
| 8 August  | 7399445055 | 702           | 2080          | REFINANCING DAILY INTEREST | 10.930      |
| 9 August  | 7411771691 | 702           | 2080          | REFINANCING DAILY INTEREST | 10.970      |
| 10 August | 7425779657 | 702           | 2080          | REFINANCING DAILY INTEREST | 11.020      |
| 11 August | 7432880800 | 702           | 2080          | REFINANCING DAILY INTEREST | 11.070      |
| 12 August | 7442560223 | 702           | 2080          | REFINANCING DAILY INTEREST | 11.110      |
| 13 August | 7454960328 | 702           | 2080          | REFINANCING DAILY INTEREST | 11.160      |
| 14 August | 7467669086 | 702           | 2080          | REFINANCING DAILY INTEREST | 11.210      |
| 15 August | 7479235301 | 702           | 2080          | REFINANCING DAILY INTEREST | 11.250      |
| 16 August | 7492456886 | 702           | 2080          | REFINANCING DAILY INTEREST | 11.300      |
| 17 August | 7503994165 | 702           | 2080          | REFINANCING DAILY INTEREST | 11.350      |
| 18 August | 7514331135 | 702           | 2080          | REFINANCING DAILY INTEREST | 11.400      |
| 19 August | 7524741904 | 702           | 2080          | REFINANCING DAILY INTEREST | 11.450      |
| ...       | ...        | ...           | ...           | ...                        | ...         |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /statements/v4/accounts/{accountId}/installment-payments` | `InstallmentPaymentsv4` | Create payment agreement | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |

### Operation essentials

- **`POST /statements/v4/accounts/{accountId}/installment-payments`** (`InstallmentPaymentsv4`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `statement_agreement`, `installments`; response statuses 201, 400, 404, 423, 500; error codes in examples `GN0001`; events `balance-installment-payment-processed-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `InstallmentPaymentsv4` | `balance-installment-payment-processed-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/accounting-scripts-examples.md`: updatedAt 2026-03-18T22:57:09.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/accounting-scripts-examples.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accounting-scripts-examples | `80e8d59127d2b08b…` | 2026-03-18T22:57:09.000Z |

## Related knowledge units

- `KU-API-revolving-credit-statements--refinancing` — API reference: Revolving credit - Statements — Refinancing
- `KU-CRED-agreements` — Agreements: compulsory, statement, installment and payment agreements
- `KU-EVT-catalogue-balance` — Event catalogue: balance
