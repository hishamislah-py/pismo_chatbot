---
ku_id: KU-CORE-processing-codes-and-transaction-types
title: Processing codes
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/processing-codes-and-transaction-types.md
  sha256: c6400539ad9c0f1a2fcb085efa6ffdfc86b9e0ef80d053e4f2c53bfab28fee77
  url: https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types
  role: primary_guide
  updated_at: '2026-06-24T18:30:58.000Z'
operations:
- CreateProcessingCode
- PostTransactionFlow
- ProcessingCodeList
- post-org-rule-model
related_kus:
- KU-API-core-platform-rule-models--model
- KU-API-core-platform-transactions--transaction-flows
- KU-API-platform-setup-orgs-operation--processing-codes
- KU-CC-processing-codes
- KU-CORE-accounts-overview
- KU-CORE-balance-configurations
- KU-CORE-flex-controls
- KU-CORE-transactiontypes
- KU-EVT-catalogue-other-domains
- KU-GS-program-types
- KU-PAY-payments-configurations
grouping_rationale: single source page
---

# Processing codes

**KU ID:** `KU-CORE-processing-codes-and-transaction-types` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/processing-codes-and-transaction-types.md`:

> Processing codes identify financial operations on the Pismo platform. For example, `00` is a purchase, `01` is a withdrawal, and so on. Processing codes are defined at the organization level, and can be used for all organization [programs](https://developers.pismo.io/pismo-docs/docs/program-types) and [accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview). An organization is created with a number of [standard processing codes](https://developers.pismo.io/pismo-docs/docs/processingcodes#standard-processing-codes) automatically available to it.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/processing-codes-and-transaction-types.md`: Processing codes; Standard processing codes; Custom processing codes; Default reversal processing codes; Default partial reversal processing codes; Default reversal processing codes; Changing processing codes during authorization with rule models

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/processing-codes-and-transaction-types.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types · updatedAt: 2026-06-24T18:30:58.000Z

<!-- source:begin path=docs/core-platform/processing-codes-and-transaction-types.md part=0-end -->

# Processing codes

Processing codes identify financial operations on the Pismo platform. For example, `00` is a purchase, `01` is a withdrawal, and so on. Processing codes are defined at the organization level, and can be used for all organization [programs](https://developers.pismo.io/pismo-docs/docs/program-types) and [accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview). An organization is created with a number of [standard processing codes](https://developers.pismo.io/pismo-docs/docs/processingcodes#standard-processing-codes) automatically available to it.

<Image align="center" alt="Pismo configurations with manual and automatic behaviors for processing codes" src="https://files.readme.io/a490d99ab2764904b2e229be8f8379f8689f7bbbba2cc4be895e8abf5bcfe02d-Processing_codes_1.png" />

For transactions, processing codes are mapped to [transaction types](https://developers.pismo.io/pismo-docs/docs/transactiontypes)  to create ***transaction flows*** . For more information, refer to  [standard processing code to transaction type mapping](https://developers.pismo.io/pismo-docs/docs/transactiontypes#standard-processing-code-to-transaction-type-mapping).

<Callout icon="📘" theme="info">
  You can also use Pismo Control Center to view and create processing codes and transaction types, including reversals. For details, refer to [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/cc-manage-processing-codes-and-transaction-types).
</Callout>

For other domains, like [balance configurations](https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview), [flex controls](https://developers.pismo.io/pismo-docs/docs/flex-controls), [fees and rules](https://developers.pismo.io/pismo-docs/docs/fee-model), and [rule models](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types#changing-processing-codes-during-authorization-with-rule-models), processing codes are used to indicate what operations to apply controls or fees to.

To find processing codes assigned to your organization, call the [List processing codes](https://developers.pismo.io/pismo-docs/reference/processingcodelist)  endpoint.

Processing codes are objects with the following **key** fields (not a complete list):

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `processing_code`
      </td>

      <td>
        string (2-6 chars)
      </td>

      <td>
        Processing code.
      </td>
    </tr>

    <tr>
      <td>
        `type`
      </td>

      <td>
        enum
      </td>

      <td>
        `AUTHORIZATION` —Transaction authorization\
        `REVERSAL`—Transaction reversal
      </td>
    </tr>

    <tr>
      <td>
        `balance_impact`
      </td>

      <td>
        enum
      </td>

      <td>
        `1` = credits (account credited).\
        `0`= no impact (no accounts impacted) Zero balance has no impact\
        `-1`= debits (account debited).
      </td>
    </tr>

    <tr>
      <td>
        `reversal_processing_code`
      </td>

      <td>
        string (2-6 chars)
      </td>

      <td>
        Processing code for cancellation. Used in  transactions and accounting flow to post the correct entries related to cancellation.
      </td>
    </tr>

    <tr>
      <td>
        `partial_reversal_processing_code`
      </td>

      <td>
        string (2-6 chars)
      </td>

      <td>
        Processing code for partial reversal cancellation. Used in transactions and accounting flow to  post the correct entries related to partial cancellation.
      </td>
    </tr>

    <tr>
      <td>
        `status`
      </td>

      <td>
        enum
      </td>

      <td>
        `PENDING` - missing required configurations\
        `SUCCESS` - required configurations done
      </td>
    </tr>
  </tbody>
</Table>

As shown. each processing code has either an `AUTHORIZATION` or `REVERSAL` type.

Full and partial reversals of an authorization processing code can be either equal or different ones as per the business requirements. Only authorization processing codes should be passed to Pismo authorization systems (Payment methods, Network authorization, P2P).

During cancellation, the authorization system uses the original processing code to perform the cancellation, the opposite financial impact is then applied (reversing the operation at authorization level) and the reversal processing codes associated with the operation are used to define the transactions that should be posted along with any accounting entries that need to be done.

# Standard processing codes

Processing codes can be either **standard** or **custom**. Standard processing codes are related to platform default operations like instant payments processing (Pix, UPI), credit cycle flow (interest accruals posting, taxes and fees), transaction banking (hold funds, release funds) and so on.  Standard processing codes are available to all customers at organization creation time. Since all  organizations use these processing codes, customizations are not allowed.

Network processing codes, used for processing Visa, Mastercard, RuPay, ELO, and other card networks, are also considered standard processing codes.

<details>
  <summary style={{ fontSize: "18px" }}><b>Standard authorization processing codes</b></summary>

  **KEY:**

  * **PC** - Processing code
  * **BI** - Balance impact (1=credt, 0=no impact, -1=debit)

  **TAGS:**

  Tags apply only to `AUTHORIZATION` processing codes. You cannot add a tag to a reverse processing code, as it could be associated with more than one authorization processing code.

  * **GLOBAL**—Common to all customers and all locations.
  * **BRAZIL**—Brazilian market.
  * **ARGENTINA** —Argentinian market.
  * **INDIA**—Indian market.
  * **NETWORK**—Network (Visa, Mastercard, ELO, Rupay, and so on).
  * **MASTERCARD**—Mastercard network.
  * **VISA**—Visa network.
  * **ELO**—ELO network (Brazil).
  * **RUPAY**—RuPay network (India).
  * **FPS**—Faster Payments System (FPS)—Great Britain.
  * **TECBAN**— Tecnologia Bancária S.A (TECBAN)—Brazil.
  * **UPI**—Unified Payments Interface (UPI)— India.
  * **PIX**—Pagamentos Instantaneos (PIX) instant payments (Brazil).
  * **TRANSACTION\_BANKING**—Transaction banking.
  * **BNPL**—Buy Now, Pay Later (BNPL) banking.
  * **LENDING**—Lending.
  * **DEPRECATED** —Do not use or consider anymore.

  <br />

  <Table>
    <thead>
      <tr>
        <th>
          PC
        </th>

        <th>
          Description
        </th>

        <th>
          BI
        </th>

        <th>
          Tags
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          00
        </td>

        <td>
          PURCHASE
        </td>

        <td>
          -1
        </td>

        <td>
          ELO
          GLOBAL
          MASTERCARD
          RUPAY
          VISA
        </td>
      </tr>

      <tr>
        <td>
          01
        </td>

        <td>
          NATIONAL WITHDRAWAL
        </td>

        <td>
          -1
        </td>

        <td>
          ELO
          GLOBAL
          MASTERCARD
          RUPAY
          VISA
        </td>
      </tr>

      <tr>
        <td>
          02
        </td>

        <td>
          DEBIT ADJUSTMENT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          MASTERCARD
        </td>
      </tr>

      <tr>
        <td>
          04
        </td>

        <td>
          INQUIRY AND SIMULATION
        </td>

        <td>
          0
        </td>

        <td>
          ELO
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          09
        </td>

        <td>
          PURCHASE WITH CASH BACK
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          MASTERCARD
        </td>
      </tr>

      <tr>
        <td>
          10
        </td>

        <td>
          NATIONAL ACCOUNT FUNDING TRANSACTION
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          VISA
        </td>
      </tr>

      <tr>
        <td>
          11
        </td>

        <td>
          PURCHASE QUASI-CASH
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          VISA
        </td>
      </tr>

      <tr>
        <td>
          14
        </td>

        <td>
          RECURRING PAYMENT
        </td>

        <td>
          -1
        </td>

        <td>
          ELO
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          15
        </td>

        <td>
          INSTALLMENTS FOR GOODS AND SERVICES
        </td>

        <td>
          -1
        </td>

        <td>
          ELO
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          17
        </td>

        <td>
          CASH DISBURSEMENT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          MASTERCARD
        </td>
      </tr>

      <tr>
        <td>
          18
        </td>

        <td>
          UNIQUE TRANSACTION/SCRIP ISSUE
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          MASTERCARD
        </td>
      </tr>

      <tr>
        <td>
          20
        </td>

        <td>
          CREDIT VOUCHER
        </td>

        <td>
          1
        </td>

        <td>
          ELO
          GLOBAL
          MASTERCARD
          RUPAY
          VISA
        </td>
      </tr>

      <tr>
        <td>
          21
        </td>

        <td>
          DEPOSIT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
          MASTERCARD
          RUPAY
        </td>
      </tr>

      <tr>
        <td>
          22
        </td>

        <td>
          CREDIT ADJUSTMENT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
          MASTERCARD
          RUPAY
        </td>
      </tr>

      <tr>
        <td>
          23
        </td>

        <td>
          CHECK DEPOSIT GUARANTEE
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
          MASTERCARD
        </td>
      </tr>

      <tr>
        <td>
          24
        </td>

        <td>
          CHECK DEPOSIT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
          MASTERCARD
        </td>
      </tr>

      <tr>
        <td>
          26
        </td>

        <td>
          NATIONAL ORIGINAL CREDIT TRANSACTION
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
          MASTERCARD
        </td>
      </tr>

      <tr>
        <td>
          28
        </td>

        <td>
          PAYMENT TRANSACTION/MONEY LOAD
        </td>

        <td>
          1
        </td>

        <td>
          INDIA RUPAY
        </td>
      </tr>

      <tr>
        <td>
          29
        </td>

        <td>
          MONEY LOAD BY ACCOUNT OR CARD
        </td>

        <td>
          1
        </td>

        <td>
          INDIA
          RUPAY
        </td>
      </tr>

      <tr>
        <td>
          30
        </td>

        <td>
          BALANCE INQUIRY
        </td>

        <td>
          0
        </td>

        <td>
          ELO
          GLOBAL
          MASTERCARD
          VISA
        </td>
      </tr>

      <tr>
        <td>
          31
        </td>

        <td>
          BALANCE INQUIRY
        </td>

        <td>
          0
        </td>

        <td>
          ELO
          GLOBAL
          RUPAY
        </td>
      </tr>

      <tr>
        <td>
          39
        </td>

        <td>
          ELIGIBILITY INQUIRY
        </td>

        <td>
          0
        </td>

        <td>
          GLOBAL
          VISA
        </td>
      </tr>

      <tr>
        <td>
          40
        </td>

        <td>
          ACCOUNT TRANSFER
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          MASTERCARD
          RUPAY
          VISA
        </td>
      </tr>

      <tr>
        <td>
          50
        </td>

        <td>
          BILL PAYMENT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          VISA
        </td>
      </tr>

      <tr>
        <td>
          53
        </td>

        <td>
          RECEIPT OF FUNDS
        </td>

        <td>
          1
        </td>

        <td>
          ELO
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          70
        </td>

        <td>
          PIN CHANGE
        </td>

        <td>
          0
        </td>

        <td>
          GLOBAL
          VISA
        </td>
      </tr>

      <tr>
        <td>
          72
        </td>

        <td>
          PIN UNBLOCK
        </td>

        <td>
          0
        </td>

        <td>
          GLOBAL
          VISA
        </td>
      </tr>

      <tr>
        <td>
          91
        </td>

        <td>
          PIN UNBLOCK
        </td>

        <td>
          0
        </td>

        <td>
          GLOBAL
          MASTERCARD
        </td>
      </tr>

      <tr>
        <td>
          92
        </td>

        <td>
          PIN CHANGE
        </td>

        <td>
          0
        </td>

        <td>
          ELO
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          98
        </td>

        <td>
          PIN CHANGE
        </td>

        <td>
          0
        </td>

        <td>
          ELO
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          99
        </td>

        <td>
          PIN UNBLOCK
        </td>

        <td>
          0
        </td>

        <td>
          ELO
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          01WZB
        </td>

        <td>
          WITHDRAWAL ZERO BALANCE
        </td>

        <td>
          0
        </td>

        <td>
          INDIA
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          003100
        </td>

        <td>
          INTERNATIONAL PURCHASE
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          003200
        </td>

        <td>
          INSTALLMENT PLAN
        </td>

        <td>
          -1
        </td>

        <td>
          ARGENTINA
          BRAZIL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          003300
        </td>

        <td>
          CASH OUT WPAY
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          003400
        </td>

        <td>
          PLAN GOBIERNO/PLAN AHORA 12
        </td>

        <td>
          -1
        </td>

        <td>
          ARGENTINA
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          003410
        </td>

        <td>
          CC - MERCHANT INSTALLMENTS - CUOTA A CUOTA
        </td>

        <td>
          -1
        </td>

        <td>
          ARGENTINA
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          003420
        </td>

        <td>
          ACCELERATED PLANS (AC/AN)
        </td>

        <td>
          -1
        </td>

        <td>
          ARGENTINA
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          003500
        </td>

        <td>
          SERVICIOS DIGITALES INTERNACIONALES
        </td>

        <td>
          -1
        </td>

        <td>
          ARGENTINA
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          003600
        </td>

        <td>
          SERVICIOS DIGITALES NACIONALES
        </td>

        <td>
          -1
        </td>

        <td>
          ARGENTINA
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          003800
        </td>

        <td>
          INSTALLMENT WITHOUT INTEREST
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          003810
        </td>

        <td>
          INSTALLMENTS WITH INTEREST
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          004000
        </td>

        <td>
          PAYMENT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          004990
        </td>

        <td>
          CREDIT BY INSTALLMENTS
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          004991
        </td>

        <td>
          REFINANCING AGREEMENT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          004992
        </td>

        <td>
          COMPULSORY INSTALLMENT CREDIT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          005091
        </td>

        <td>
          REFINANCING INSTALLMENT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          005092
        </td>

        <td>
          AGREEMENT INSTALLMENT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          005093
        </td>

        <td>
          COMPULSORY INSTALLMENT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          005100
        </td>

        <td>
          PAGAMENTO CONTA CONSUMO
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
        </td>
      </tr>

      <tr>
        <td>
          006100
        </td>

        <td>
          PAGAMENTO DE BOLETO BANCARIO
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
        </td>
      </tr>

      <tr>
        <td>
          007000
        </td>

        <td>
          DEBIT TRANSFER
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          007200
        </td>

        <td>
          CREDIT TRANSFER
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          007400
        </td>

        <td>
          TED CASH IN
        </td>

        <td>
          1
        </td>

        <td>
          BRAZIL
        </td>
      </tr>

      <tr>
        <td>
          007503
        </td>

        <td>
          DEPOSIT BY BILL
        </td>

        <td>
          1
        </td>

        <td>
          BRAZIL
        </td>
      </tr>

      <tr>
        <td>
          007700
        </td>

        <td>
          DEBIT TRANSFER
        </td>

        <td>
          0
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          008800
        </td>

        <td>
          PIX ON-US
        </td>

        <td>
          1
        </td>

        <td>
          BRAZIL
          NETWORK
          DEPRECATED
        </td>
      </tr>

      <tr>
        <td>
          008900
        </td>

        <td>
          PIX INSTALLMENTS ON-US
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          NETWORK
          DEPRECATED
        </td>
      </tr>

      <tr>
        <td>
          009000
        </td>

        <td>
          PURCHASE ON-US
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          NETWORK
          DEPRECATED
        </td>
      </tr>

      <tr>
        <td>
          009100
        </td>

        <td>
          CREDIT ADJUSTMENT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          009200
        </td>

        <td>
          DEBIT ADJUSTMENT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          009595
        </td>

        <td>
          Saving To Available Credit (Maturity)
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          009696
        </td>

        <td>
          Saving To Available Credit (Detach)
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          009797
        </td>

        <td>
          INTEREST RATE CREDIT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          009900
        </td>

        <td>
          INSTALLMENTS WITHOUT INTEREST ON-US
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          NETWORK
          DEPRECATED
        </td>
      </tr>

      <tr>
        <td>
          010000
        </td>

        <td>
          TRANSFERENCIA SPB DEBITO
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
        </td>
      </tr>

      <tr>
        <td>
          010200
        </td>

        <td>
          TRANSFERENCIA SPB CREDITO
        </td>

        <td>
          1
        </td>

        <td>
          BRAZIL
        </td>
      </tr>

      <tr>
        <td>
          013100
        </td>

        <td>
          INTERNATIONAL WITHDRAWAL
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          013200
        </td>

        <td>
          WITHDRAWAL TECBAN
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          NETWORK
          TECBAN
        </td>
      </tr>

      <tr>
        <td>
          022000
        </td>

        <td>
          DEBIT VOUCHER
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          110300
        </td>

        <td>
          DEBIT CHECKING ACCOUNT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          110303
        </td>

        <td>
          CREDIT CHECKING ACCOUNT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          110400
        </td>

        <td>
          CREDIT SAVING ACCOUNT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          110403
        </td>

        <td>
          DEBIT SAVING ACCOUNT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          203100
        </td>

        <td>
          PURCHASE RETURN INTER / CREDIT VOUCHER
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          203300
        </td>

        <td>
          REFUND WPAY
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          218819
        </td>

        <td>
          PAGAMENTO PIX
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          218822
        </td>

        <td>
          RECEBIMENTO PIX
        </td>

        <td>
          1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          218825
        </td>

        <td>
          PAGAMENTO PIX PJ
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          219248
        </td>

        <td>
          HOLD FUNDS
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219251
        </td>

        <td>
          RELEASE FUNDS
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219258
        </td>

        <td>
          HELD FUNDS CASHOUT TRANSFER
        </td>

        <td>
          -1
        </td>

        <td>
          TRANSACTION\_BANKING
        </td>
      </tr>

      <tr>
        <td>
          219686
        </td>

        <td>
          DISBURSEMENT CASH OUT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219689
        </td>

        <td>
          REPAYMENT CASH OUT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219692
        </td>

        <td>
          DISBURSEMENT CASH IN
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219698
        </td>

        <td>
          REPAYMENT CASH IN
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219734
        </td>

        <td>
          INTEREST ON REVOLVING CREDIT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219737
        </td>

        <td>
          LATE PAYMENT INTEREST
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219740
        </td>

        <td>
          LATE FEE
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219743
        </td>

        <td>
          TAXES
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219746
        </td>

        <td>
          OVERLIMIT FEE
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219749
        </td>

        <td>
          DEBIT EXCHANGE DIFFERENCE
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219752
        </td>

        <td>
          CREDIT EXCHANGE DIFFERENCE
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219755
        </td>

        <td>
          ANNUITY
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          219794
        </td>

        <td>
          PIX SAQUE
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          219797
        </td>

        <td>
          RECEBIMENTO PIX SAQUE
        </td>

        <td>
          1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          219800
        </td>

        <td>
          PIX TROCO
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          219803
        </td>

        <td>
          RECEBIMENTO PIX TROCO
        </td>

        <td>
          1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          220035
        </td>

        <td>
          CASHIN TRANSFER
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          220037
        </td>

        <td>
          CASHOUT TRANSFER
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          220039
        </td>

        <td>
          CREDIT ADJUSTMENT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          220040
        </td>

        <td>
          DEBIT ADJUSTMENT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          220054
        </td>

        <td>
          CHECK CASHIN TRANSFER
        </td>

        <td>
          1
        </td>

        <td>
          TRANSACTION\_BANKING
        </td>
      </tr>

      <tr>
        <td>
          220056
        </td>

        <td>
          CHECK HOLD FUNDS
        </td>

        <td>
          1
        </td>

        <td>
          TRANSACTION\_BANKING
        </td>
      </tr>

      <tr>
        <td>
          220058
        </td>

        <td>
          CHECK RELEASE FUNDS
        </td>

        <td>
          1
        </td>

        <td>
          TRANSACTION\_BANKING
        </td>
      </tr>

      <tr>
        <td>
          220060
        </td>

        <td>
          CHECK CASHIN FUTURE FUNDS
        </td>

        <td>
          1
        </td>

        <td>
          TRANSACTION\_BANKING
        </td>
      </tr>

      <tr>
        <td>
          220062
        </td>

        <td>
          CHECK RELEASE FUTURE FUNDS
        </td>

        <td>
          1
        </td>

        <td>
          TRANSACTION\_BANKING
        </td>
      </tr>

      <tr>
        <td>
          283300
        </td>

        <td>
          CASH IN WPAY
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          320200
        </td>

        <td>
          DEBIT UPI RUPAY
        </td>

        <td>
          -1
        </td>

        <td>
          INDIA
          UPI
        </td>
      </tr>

      <tr>
        <td>
          320203
        </td>

        <td>
          CREDIT UPI RUPAY
        </td>

        <td>
          1
        </td>

        <td>
          INDIA
          UPI
        </td>
      </tr>

      <tr>
        <td>
          903002
        </td>

        <td>
          UTILITIES PAYMENT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          997350
        </td>

        <td>
          REFINANCING INTEREST REFUND
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          997351
        </td>

        <td>
          OVERDUE INTEREST REFUND
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          997352
        </td>

        <td>
          IOF REFUND
        </td>

        <td>
          1
        </td>

        <td>
          BRAZIL
        </td>
      </tr>

      <tr>
        <td>
          PSM005
        </td>

        <td>
          INTERNATIONAL AFT
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          PSM007
        </td>

        <td>
          INTERNATIONAL OCT
        </td>

        <td>
          1
        </td>

        <td>
          GLOBAL
          NETWORK
        </td>
      </tr>

      <tr>
        <td>
          PSM012
        </td>

        <td>
          EMI UPI RUPAY
        </td>

        <td>
          -1
        </td>

        <td>
          INDIA
          UPI
        </td>
      </tr>

      <tr>
        <td>
          PSM014
        </td>

        <td>
          FORECLOSE EMI UPI RUPAY
        </td>

        <td>
          1
        </td>

        <td>
          INDIA
          UPI
        </td>
      </tr>

      <tr>
        <td>
          PSM016
        </td>

        <td>
          AMOUNT BLOCKED
        </td>

        <td>
          -1
        </td>

        <td>
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          PSM018
        </td>

        <td>
          INSTALLMENT WITHDRAWAL TECBAN
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          NETWORK
          TECBAN
        </td>
      </tr>

      <tr>
        <td>
          PSM021
        </td>

        <td>
          Pix Automatic Refund
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          PSM024
        </td>

        <td>
          Payment Pix by Approximation
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          PSM027
        </td>

        <td>
          Receipt Pix by Approximation
        </td>

        <td>
          1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          PSM030
        </td>

        <td>
          SCHEDULED PIX PAYMENT
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          PSM033
        </td>

        <td>
          AUTOMATIC PIX PAYMENT
        </td>

        <td>
          -1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          PSM036
        </td>

        <td>
          AUTOMATIC PIX RECEIPT
        </td>

        <td>
          1
        </td>

        <td>
          BRAZIL
          PIX
        </td>
      </tr>

      <tr>
        <td>
          PSM039
        </td>

        <td>
          CASHBACK
        </td>

        <td>
          1
        </td>

        <td>
          ELO
          GLOBAL
        </td>
      </tr>

      <tr>
        <td>
          PSM041
        </td>

        <td>
          FUTURE DATED CASHIN TRANSFER
        </td>

        <td>
          1
        </td>

        <td>
          TRANSACTION\_BANKING
        </td>
      </tr>

      <tr>
        <td>
          PSM043
        </td>

        <td>
          FUTURE DATED CASHOUT TRANSFER
        </td>

        <td>
          -1
        </td>

        <td>
          TRANSACTION\_BANKING
        </td>
      </tr>

      <tr>
        <td>
          PSM045
        </td>

        <td>
          RESTRICT FUNDS
        </td>

        <td>
          -1
        </td>

        <td>
          TRANSACTION\_BANKING
        </td>
      </tr>

      <tr>
        <td>
          PSM047
        </td>

        <td>
          RELEASE RESTRICTION
        </td>

        <td>
          1
        </td>

        <td>
          TRANSACTION\_BANKING
        </td>
      </tr>

      <tr>
        <td>
          PSM049
        </td>

        <td>
          RESTRICTED FUNDS CASHOUT TRANSFER
        </td>

        <td>
          -1
        </td>

        <td>
          TRANSACTION\_BANKING
        </td>
      </tr>

      <tr>
        <td>
          PSM051
        </td>

        <td>
          FPS Payment
        </td>

        <td>
          -1
        </td>

        <td>
          FPS
        </td>
      </tr>

      <tr>
        <td>
          PSM054
        </td>

        <td>
          FPS Receipt
        </td>

        <td>
          1
        </td>

        <td>
          FPS
        </td>
      </tr>

      <tr>
        <td>
          PSM057
        </td>

        <td>
          FPS Transfer In
        </td>

        <td>
          1
        </td>

        <td>
          FPS
        </td>
      </tr>

      <tr>
        <td>
          PSM060
        </td>

        <td>
          FPS Transfer Out
        </td>

        <td>
          -1
        </td>

        <td>
          FPS
        </td>
      </tr>
    </tbody>
  </Table>
</details>

<details>
  <summary style={{ fontSize: "18px" }}><b>Standard reversal authorization processing codes</b></summary>

  **KEY:**

  **PC** - Processing code

  **BI** - Balance impact  (1=credt, 0=no impact, -1=debit)

  **RAPC**—Related authorization PCs

  <br />

  | PC     | Description                                              | BI | RAPC                                                                                                                          |
  | ------ | -------------------------------------------------------- | -- | ----------------------------------------------------------------------------------------------------------------------------- |
  | 0001   | REFUND PURCHASE                                          | 1  | 00                                                                                                                            |
  | 000515 | PARTIAL CANCELLATION                                     | 1  | Default Partial Reversal Processing Code is associated to a list of Processing Code when they don't have a specific Reversal. |
  | 003101 | INTERNATIONAL PURCHASE REVERSAL                          | 1  | 003100                                                                                                                        |
  | 003201 | REVERSAL INSTALLMENT PLAN                                | 1  | 003200                                                                                                                        |
  | 003301 | REVERSAL CASH OUT WPAY                                   | 1  | 003300                                                                                                                        |
  | 003401 | REVERSAL PLAN GOBIERNO/PLAN AHORA 12                     | 1  | 003300                                                                                                                        |
  | 003411 | REVERSAL CC-MERCHANT INSTALLMENTS - CUOTA A CUOTA        | 1  | 003410                                                                                                                        |
  | 003421 | REVERSAL ACCELERATED PLANS (AC/AN)                       | 1  | 003420                                                                                                                        |
  | 003501 | REVERSAL SERVICIOS DIGITALES INTERNACIONALES             | 1  | 003500                                                                                                                        |
  | 003601 | REVERSAL SERVICIOS DIGITALES NACIONALES                  | 1  | 003600                                                                                                                        |
  | 003801 | INSTALLMENT WITHOUT INTEREST REVERSAL                    | 1  | 003800                                                                                                                        |
  | 003811 | REVERSAL INSTALLMENTS WITH INTEREST                      | 1  | 003810                                                                                                                        |
  | 004995 | CAN CREDIT BY INSTALLMENTS                               | -1 | 004990                                                                                                                        |
  | 004996 | CAN REFINANCING AGREEMENT                                | -1 | 004991                                                                                                                        |
  | 004997 | CANC CREDIT COMPULSORY INSTALLMENT                       | -1 | 004992                                                                                                                        |
  | 005095 | CANC REFINANCING INSTALLMENT                             | 1  | 005091                                                                                                                        |
  | 005096 | CANC AGREEMENT INSTALLMENT                               | 1  | 005092                                                                                                                        |
  | 005097 | CANC COMPULSORY INSTALLMENT                              | 1  | 005093                                                                                                                        |
  | 005200 | ESTORNO DO PAGAMENTO DE CONTA CONSUMO                    | 1  | 005100                                                                                                                        |
  | 005300 | CANC DO ESTORNO DO PAGAMENTO DE CONTA CONSUMO            | -1 | 005200                                                                                                                        |
  | 006200 | ESTORNO DO PAGAMENTO DE BOLETO BANCARIO                  | 1  | 006100                                                                                                                        |
  | 006300 | CANC DO ESTORNO DO PAGAMENTO DE BOLETO BANCARIO          | -1 | 006200                                                                                                                        |
  | 007001 | DEBIT REVERSAL                                           | 1  | 007000                                                                                                                        |
  | 007201 | CREDIT REVERSAL                                          | -1 | 007200                                                                                                                        |
  | 007401 | REVERSAL TED CASH IN                                     | -1 | 007400                                                                                                                        |
  | 007701 | TRANSFER REVERSION ZERO DEBIT                            | 0  | 007700                                                                                                                        |
  | 008801 | REVERSAL PIX ON-US                                       | -1 | 008800                                                                                                                        |
  | 008901 | REVERSAL PIX INSTALLMENTS ON-US                          | 1  | 008900                                                                                                                        |
  | 009001 | REVERSAL PURCHASE ON-US                                  | 1  | 009000                                                                                                                        |
  | 009898 | REVERSAL INTEREST RATE CREDIT                            | -1 | 009797                                                                                                                        |
  | 009901 | REVERSAL INSTALLMENTS WITHOUT INTEREST ON-US             | 1  | 009900                                                                                                                        |
  | 009999 | CANCELLATION REV INTEREST RATE CREDIT                    | 1  | 009898                                                                                                                        |
  | 010001 | REVERSAO DE SPB DEBITO                                   | 1  | 010000                                                                                                                        |
  | 0101   | REVERSE NATIONAL WITHDRAWAL                              | 1  | 01                                                                                                                            |
  | 010201 | REVERSAO DE SPB CREDITO                                  | -1 | 010200                                                                                                                        |
  | 013101 | REVERSAL INTERNATIONAL WITHDRAWAL                        | 1  | 013100                                                                                                                        |
  | 013201 | REVERSAL WITHDRAWAL TECBAN                               | 1  | 013200                                                                                                                        |
  | 0201   | REVERSE DEBIT ADJUSTMENT                                 | 1  | 02                                                                                                                            |
  | 022001 | REVERSAL DEBIT VOUCHER                                   | 1  | 022000                                                                                                                        |
  | 0401   | REVERSAL INQUIRY AND SIMULATION                          | 0  | 04                                                                                                                            |
  | 0901   | REVERSAL PURCHASE WITH CASH BACK                         | 1  | 09                                                                                                                            |
  | 1101   | REVERSAL PURCHASE QUASI-CASH                             | 1  | 11                                                                                                                            |
  | 110301 | CANCEL DEBIT CHECKING ACCOUNT                            | 1  | 110300                                                                                                                        |
  | 110304 | CANCEL CREDIT CHECKING ACCOUNT                           | -1 | 110303                                                                                                                        |
  | 110401 | CANCEL CREDIT SAVING ACCOUNT                             | -1 | 110400                                                                                                                        |
  | 110404 | CANCEL DEBIT SAVING ACCOUNT                              | 1  | 110403                                                                                                                        |
  | 1401   | REVERSAL RECURRING PAYMENT                               | 1  | 14                                                                                                                            |
  | 1501   | REVERSAL INSTALLMENTS FOR GOODS AND SERVICES             | 1  | 15                                                                                                                            |
  | 1701   | REVERSAL CASH DISBURSEMENT                               | 1  | 17                                                                                                                            |
  | 1801   | REVERSAL UNIQUE TRANSACTION/SCRIP ISSUE                  | 1  | 18                                                                                                                            |
  | 203101 | REVERSAL PURCHASE RETURN INTER / CREDIT VOUCHER          | -1 | 203100                                                                                                                        |
  | 203301 | REVERSAL REFUND WPAY                                     | -1 | 203300                                                                                                                        |
  | 2101   | REVERSAL DEPOSIT                                         | -1 | 21                                                                                                                            |
  | 218820 | ESTORNO - PAGAMENTO PIX                                  | 1  | 218819                                                                                                                        |
  | 218821 | CANC - ESTORNO PAGAMENTO PIX                             | -1 | 218820                                                                                                                        |
  | 218823 | ESTORNO - RECEBIMENTO PIX                                | -1 | 218822                                                                                                                        |
  | 218824 | CANC - ESTORNO RECEBIMENTO PIX                           | 1  | 218823                                                                                                                        |
  | 218826 | ESTORNO PAGAMENTO PIX PJ                                 | 1  | 218825                                                                                                                        |
  | 218827 | CANC ESTORNO PAGAMENTO PIX PJ                            | -1 | 218826                                                                                                                        |
  | 219249 | HOLD FUNDS CANCEL                                        | 1  | 219248                                                                                                                        |
  | 219252 | RELEASE FUNDS CANCEL                                     | -1 | 219251                                                                                                                        |
  | 219259 | UNDO HELD FUNDS CASHOUT TRANSFER                         | 1  | 219258                                                                                                                        |
  | 219687 | CAN DISBURSEMENT CASH OUT                                | 1  | 219686                                                                                                                        |
  | 219688 | EST CAN DISBURSEMENT CASH OUT                            | -1 | 219687                                                                                                                        |
  | 219690 | CAN REPAYMENT CASH OUT                                   | 1  | 219689                                                                                                                        |
  | 219691 | EST CAN REPAYMENT CASH OUT                               | -1 | 219690                                                                                                                        |
  | 219693 | CAN DISBURSEMENT CASH IN                                 | -1 | 219692                                                                                                                        |
  | 219694 | EST CAN DISBURSEMENT CASH IN                             | 1  | 219693                                                                                                                        |
  | 219699 | CAN REPAYMENT CASH IN                                    | -1 | 219698                                                                                                                        |
  | 219700 | EST CAN REPAYMENT CASH IN                                | 1  | 219699                                                                                                                        |
  | 219735 | CAN INTEREST ON REVOLVING CREDIT                         | 1  | 219734                                                                                                                        |
  | 219736 | UNDO CANC INTEREST ON REVOLVING CREDIT                   | -1 | 219735                                                                                                                        |
  | 219738 | CAN LATE PAYMENT INTEREST                                | 1  | 219737                                                                                                                        |
  | 219739 | UNDO CANC LATE PAYMENT INTEREST                          | -1 | 219738                                                                                                                        |
  | 219741 | CAN LATE FEE                                             | 1  | 219740                                                                                                                        |
  | 219742 | UNDO CANC LATE FEE                                       | -1 | 219741                                                                                                                        |
  | 219744 | CAN TAXES                                                | 1  | 219743                                                                                                                        |
  | 219745 | UNDO CANC TAXES                                          | -1 | 219744                                                                                                                        |
  | 219747 | CAN OVERLIMIT FEE                                        | 1  | 219746                                                                                                                        |
  | 219748 | UNDO CANC OVERLIMIT FEE                                  | -1 | 219747                                                                                                                        |
  | 219750 | CAN DEBIT EXCHANGE DIFFERENCE                            | 1  | 219749                                                                                                                        |
  | 219751 | UNDO CANC DEBIT EXCHANGE DIFFERENCE                      | -1 | 219750                                                                                                                        |
  | 219753 | CAN CREDIT EXCHANGE DIFFERENCE                           | -1 | 219752                                                                                                                        |
  | 219754 | UNDO CANC CREDIT EXCHANGE DIFFERENCE                     | 1  | 219753                                                                                                                        |
  | 219756 | CAN ANNUITY                                              | 1  | 219755                                                                                                                        |
  | 219757 | UNDO CAN ANNUITY                                         | -1 | 219756                                                                                                                        |
  | 219795 | ESTORNO - PIX SAQUE                                      | 1  | 219794                                                                                                                        |
  | 219796 | CANC - ESTORNO PIX SAQUE                                 | -1 | 219795                                                                                                                        |
  | 219798 | ESTORNO RECEBIMENTO PIX SAQUE                            | -1 | 219797                                                                                                                        |
  | 219799 | CANC ESTORNO RECEB PIX SAQUE                             | 1  | 219798                                                                                                                        |
  | 219801 | ESTORNO - PIX TROCO                                      | 1  | 219800                                                                                                                        |
  | 219802 | CANC - ESTORNO PIX TROCO                                 | -1 | 219801                                                                                                                        |
  | 219804 | ESTORNO RECEBIMENTO PIX TROCO                            | -1 | 219803                                                                                                                        |
  | 219805 | CANC ESTORNO RECEB PIX TROCO                             | 1  | 219804                                                                                                                        |
  | 220036 | UNDO CASHIN TRANSFER                                     | -1 | 220035                                                                                                                        |
  | 220038 | UNDO CASHOUT TRANSFER                                    | 1  | 220037                                                                                                                        |
  | 220055 | UNDO CHECK CASHIN TRANSFER                               | -1 | 220054                                                                                                                        |
  | 220057 | UNDO CHECK HOLD FUNDS                                    | -1 | 220056                                                                                                                        |
  | 220059 | UNDO CHECK RELEASE FUNDS                                 | -1 | 220058                                                                                                                        |
  | 220061 | UNDO CHECK CASHIN FUTURE FUNDS                           | -1 | 220060                                                                                                                        |
  | 220063 | UNDO CHECK RELEASE FUTURE FUNDS                          | -1 | 220062                                                                                                                        |
  | 2201   | REVERSAL CREDIT ADJUSTMENT                               | -1 | 22                                                                                                                            |
  | 2301   | REVERSAL CHECK DEPOSIT GUARANTEE                         | -1 | 23                                                                                                                            |
  | 2401   | REVERSAL CHECK DEPOSIT                                   | -1 | 24                                                                                                                            |
  | 2801   | REVERSAL PAYMENT TRANSACTION/MONEY LOAD                  | -1 | 28                                                                                                                            |
  | 283301 | REVERSAL CASH IN WPAY                                    | -1 | 283300                                                                                                                        |
  | 2901   | REVERSAL MONEY LOAD BY ACCOUNT OR CARD                   | -1 | 29                                                                                                                            |
  | 3001   | REVERSAL BALANCE INQUIRY                                 | 0  | 30                                                                                                                            |
  | 3101   | REVERSAL BALANCE INQUIRY                                 | 0  | 31                                                                                                                            |
  | 320201 | REVERSAL - DEBIT UPI RUPAY                               | 1  | 320200                                                                                                                        |
  | 320202 | CANC - REVERSAL DEBIT UPI RUPAY                          | -1 | 320201                                                                                                                        |
  | 320204 | REVERSAL - CREDIT UPI RUPAY                              | -1 | 320203                                                                                                                        |
  | 320205 | CANC - REVERSAL CREDIT UPI RUPAY                         | 1  | 320204                                                                                                                        |
  | 3901   | REVERSAL ELIGIBILITY INQUIRY                             | -1 | 39                                                                                                                            |
  | 4001   | REVERSAL ACCOUNT TRANSFER                                | 1  | 40                                                                                                                            |
  | 5001   | REVERSAL BILL PAYMENT                                    | 1  | 50                                                                                                                            |
  | 5301   | REVERSAL RECEIPT OF FUNDS                                | -1 | 53                                                                                                                            |
  | 7001   | REVERSAL PIN CHANGE                                      | 0  | 70                                                                                                                            |
  | 7201   | REVERSAL PIN UNBLOCK                                     | 0  | 72                                                                                                                            |
  | 904002 | UTILITIES PAYMENT REVERSAL                               | 1  | 903002                                                                                                                        |
  | 9101   | REVERSAL PIN UNBLOCK                                     | 0  | 91                                                                                                                            |
  | 9201   | REVERSAL PIN CHANGE                                      | 0  | 92                                                                                                                            |
  | 9801   | REVERSAL PIN CHANGE                                      | 0  | 98                                                                                                                            |
  | 9901   | REVERSAL PIN UNBLOCK                                     | 0  | 99                                                                                                                            |
  | PSM000 | CREDIT PARTIAL CANCELLATION                              | -1 | Default Partial Reversal Processing Code is associated to a list of Processing Code when they don't have a specific Reversal. |
  | PSM001 | NO IMPACT PARTIAL CANCELLATION                           | 0  | Default Partial Reversal Processing Code is associated to a list of Processing Code when they don't have a specific Reversal. |
  | PSM002 | CREDIT CANCELLATION                                      | -1 | Default Reversal Processing Code is associated to a list of Processing Code when they don't have a specific Reversal.         |
  | PSM003 | NO IMPACT CANCELLATION                                   | 0  | Default Reversal Processing Code is associated to a list of Processing Code when they don't have a specific Reversal.         |
  | PSM004 | DEBIT CANCELLATION                                       | 1  | Default Reversal Processing Code is associated to a list of Processing Code when they don't have a specific Reversal.         |
  | PSM006 | REVERSAL INTERNATIONAL AFT                               | 1  | PSM005                                                                                                                        |
  | PSM008 | REVERSAL INTERNATIONAL OCT                               | -1 | PSM007                                                                                                                        |
  | PSM009 | REVERSAL NATIONAL AFT                                    | 1  | 10                                                                                                                            |
  | PSM010 | PARTIAL REVERSAL NATIONAL AFT                            | 1  | 10                                                                                                                            |
  | PSM011 | REVERSAL NATIONAL OCT                                    | -1 | 26                                                                                                                            |
  | PSM013 | REVERSAL EMI UPI RUPAY                                   | 1  | PSM012                                                                                                                        |
  | PSM015 | REVERSAL FORECLOSE EMI UPI RUPAY                         | -1 | PSM014                                                                                                                        |
  | PSM017 | AMOUNT UNBLOCKED                                         | 1  | PSM016                                                                                                                        |
  | PSM019 | REV INSTALLMENT WITHDRAWAL TECBAN                        | 1  | PSM018                                                                                                                        |
  | PSM020 | PARTIAL REV INSTALLMENT WITHDRAWAL TECBAN                | 1  | PSM018                                                                                                                        |
  | PSM022 | Cancellation of Pix Automatic Refund                     | 1  | PSM021                                                                                                                        |
  | PSM023 | Reversal of Pix Automatic Refund Cancellation            | -1 | PSM022                                                                                                                        |
  | PSM025 | Cancellation of Payment by Pix by Approximation          | 1  | PSM024                                                                                                                        |
  | PSM026 | Reversal of Payment by Pix by Approximation Cancellation | -1 | PSM025                                                                                                                        |
  | PSM028 | Cancellation of Receipt Pix by Approximation             | -1 | PSM027                                                                                                                        |
  | PSM029 | Reversal of Receipt by Pix by Approximation Cancellation | 1  | PSM028                                                                                                                        |
  | PSM031 | CANC SCHEDULED PIX PAYMENT                               | 1  | PSM030                                                                                                                        |
  | PSM032 | REVERSAL OF SCHED PIX PAYMENT CANCEL                     | -1 | PSM031                                                                                                                        |
  | PSM034 | CANC AUTO PIX PAYMENT                                    | 1  | PSM033                                                                                                                        |
  | PSM035 | REVERSAL OF AUTO PIX PAYMENT CANCEL                      | -1 | PSM034                                                                                                                        |
  | PSM037 | CANCEL AUTO PIX RECEIPT                                  | -1 | PSM036                                                                                                                        |
  | PSM038 | REVERSAL OF AUTO PIX RECEIPT CANCEL                      | 1  | PSM037                                                                                                                        |
  | PSM040 | CASHBACK REVERSAL                                        | -1 | PSM039                                                                                                                        |
  | PSM042 | UNDO FUTURE DATED CASHIN TRANSFER                        | -1 | PSM041                                                                                                                        |
  | PSM044 | UNDO FUTURE DATED CASHOUT TRANSFER                       | 1  | PSM043                                                                                                                        |
  | PSM046 | RESTRICT FUNDS CANCEL                                    | 1  | PSM045                                                                                                                        |
  | PSM048 | RELEASE RESTRICTION CANCEL                               | -1 | PSM047                                                                                                                        |
  | PSM050 | RESTRICTED FUNDS CASHOUT TRANSFER CANCEL                 | 1  | PSM049                                                                                                                        |
  | PSM052 | FPS Payment Rev                                          | 1  | PSM051                                                                                                                        |
  | PSM053 | FPS Payment Rev Canc                                     | -1 | PSM052                                                                                                                        |
  | PSM055 | FPS Receipt Rev                                          | -1 | PSM054                                                                                                                        |
  | PSM056 | FPS Receipt Rev Canc                                     | 1  | PSM055                                                                                                                        |
  | PSM058 | FPS Transfer In Rev                                      | -1 | PSM057                                                                                                                        |
  | PSM059 | FPS Transfer In Rev Canc                                 | 1  | PSM058                                                                                                                        |
  | PSM061 | FPS Transfer Out Rev                                     | 1  | PSM060                                                                                                                        |
  | PSM062 | FPS Transfer Out Rev Canc                                | -1 | PSM061                                                                                                                        |
</details>

## Custom processing codes

You can configure your own custom processing code with the [Create processing code](https://developers.pismo.io/pismo-docs/reference/createprocessingcode)  endpoint. For a custom processing code, you must configure its reversal and partial reversal processing codes, and all required configurations.

For transactions, once a custom processing code is created, it needs to be [mapped](https://developers.pismo.io/pismo-docs/reference/posttransactionflow)  to a [transaction type](https://developers.pismo.io/pismo-docs/reference/transactiontypes)  to create a transaction flow. Refer to [Payments configurations](https://developers.pismo.io/pismo-docs/docs/payments-configurations) for more information. This guide has a tutorial on creating your own transaction flows.

A custom processing code is created with a `PENDING`status . Initially, its use is not allowed in authorizations. Once the transaction flow for a custom processing code is completely configured, its status changes to `SUCCESS`and it is ready for use. All standard processing codes have a `SUCCESS` status.

> 📘 New authorization system
>
> Life cycle (`status`) will take effect on the platform after the platform's authorization system is migrated to use the new processing code domain. All current processing codes created before the migration of the processing code database on January 2, 2025 remains ready for usage. New processing codes created after this date should follow the flow to have its status updated to `SUCCESS`. Denial of requests with processing codes with status `PENDING` will take effect later and will be announced by the authorization teams.

# Default reversal processing codes

Every `AUTHORIZATION` processing code is **required** to have a reversal and a partial reversal processing code. When [creating a new processing code](https://developers.pismo.io/pismo-docs/reference/createprocessingcode) , customers must specify the reversal processing code. Partial reversal code is optional but, if not present, a default value is assigned based on the balance Impact.

There is currently no established standard for implementing a “cancel a cancellation”—this approach introduces unnecessary complexity and risk to transaction integrity. For this reason, we strongly advise against configuring or relying on such functionality. Instead, the recommended best practice is to treat the initial cancellation as final. If a reversal is required, the client should initiate a new authorization rather than attempting to cancel the cancellation. This ensures consistency, reduces operational overhead, and aligns with expected platform behavior.

### Default partial reversal processing codes

<HTMLBlock>
  {`
  <table>
    <thead>
      <th>Processing code</th><th>Description</th><th>Balance impact</th><th>Link</th>
    </thead>
    <tr><td>000515</td><td>PARTIAL CANCELLATION</td><td>1</td><td>Linked to PC  with balance impact =  -1.</td></tr>
    <tr><td>PSM000</td><td>CREDIT PARTIAL CANCELLATION</td><td>-1</td><td>Linked to PC  with balance impact = 0.</td></tr>
    <tr><td>PSM001</td><td>NO IMPACT PARTIAL CANCELLATION</td><td>0</td><td>Linked to PC  with  balance impact = 1.</td></tr>
  </table>
  `}
</HTMLBlock>

Pismo also defines generic reversal processing codes available to customers to use as standard processing codes. Those ones can be linked to a processing code when the customer doesn’t want to create or use a specific reversal processing code for the one being created. Since the endpoint requires the reversal one, the request must contain one of them so that the correct link is made. Below we show the list of standard processing codes for reversals:

### Default reversal processing codes

<HTMLBlock>
  {`
  <table>
    <thead>
      <th>Processing code</th><th>Description</th><th>Balance impact</th><th>Link</th>
    </thead>
    <tr><td>PSM002</td><td>CREDIT CANCELLATION</td><td>-1</td><td>Linked to PC  with balance impact =  1</td></tr>
    <tr><td>PSM003</td><td>NO IMPACT CANCELLATION</td><td>0</td><td>Linked to PC  with balance impact = 0</td></tr>
    <tr><td>PSM004</td><td>DEBIT CANCELLATION</td><td>1</td><td>Linked to PC  with  balance impact = -1</td></tr>
  </table>
  `}
</HTMLBlock>

# Changing processing codes during authorization with rule models

You can use *rule models* to change a card network processing code during authorization. For example, you may want to use a custom processing code if the merchant is Apple. Rule models are created for an organization and can be applied to an organization, program, or account. The Pismo platform has a [Rule model API](https://developers.pismo.io/pismo-docs/reference/post-org-rule-model)  you can use to implement this feature.

**Sample payload to create rule model:**

This rule model assigns the custom processing code `MYPC03` to the authorization if the merchant is Apple and it's a domestic transaction. If it's an international transaction, then `003100` is assigned as the processing code.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /orgs-operation/v1/processing-codes` | `ProcessingCodeList` | List processing codes | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `POST /orgs-operation/v1/processing-codes` | `CreateProcessingCode` | Create processing code | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `POST /v1/transaction-flow` | `PostTransactionFlow` | Create transaction flow | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |
| `POST /v1/models` | `post-org-rule-model` | Create org rule model | `api-specs/Core_platform_-_Rule_models.yaml` | no | KU-API-core-platform-rule-models--model |

### Operation essentials

- **`GET /orgs-operation/v1/processing-codes`** (`ProcessingCodeList`): security `S2SAuthentication`; required parameters none declared; required body fields none declared; response statuses 200, 400; error codes in examples none; events none listed.
- **`POST /orgs-operation/v1/processing-codes`** (`CreateProcessingCode`): security `S2SAuthentication`; required parameters none declared; required body fields `processing_code`, `balance_impact`, `description`, `reversal_processing_code`; response statuses 201, 400; error codes in examples none; events `orgs-operation-create-1`.
- **`POST /v1/transaction-flow`** (`PostTransactionFlow`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `processing_code`, `key`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00003`, `WTRC00005`, `WTRC04003`, `WTRC04004`, `WTRC04005`, `WTRC04006`, `WTRC05003`, `WTRC07001`, `WTRC04001`, `ETRC04003`, `ETRC04004`, `ETRC04005`, `ETRC04006`, `WTRC08001`, `ETRC00001`; events none listed.
- **`POST /v1/models`** (`post-org-rule-model`): security not declared; required parameters none declared; required body fields `rules`; response statuses 201, 400, 500; error codes in examples none; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `transactiontypes` | Transaction types; transaction type | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `CreateProcessingCode` | `orgs-operation-create-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/processing-codes-and-transaction-types.md`: updatedAt 2026-06-24T18:30:58.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- Operation link `transactiontypes` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/processing-codes-and-transaction-types.md` | whole document | https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types | `c6400539ad9c0f1a…` | 2026-06-24T18:30:58.000Z |

## Related knowledge units

- `KU-API-core-platform-rule-models--model` — API reference: Core platform - Rule models — Model
- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-platform-setup-orgs-operation--processing-codes` — API reference: Platform setup - Orgs operation — Processing codes
- `KU-CC-processing-codes` — Control Center processing codes, transaction types and general ledger accounts
- `KU-CORE-accounts-overview` — Accounts
- `KU-CORE-balance-configurations` — Balance configurations and filter templates
- `KU-CORE-flex-controls` — Flexible transaction controls: concepts, examples and simulation
- `KU-CORE-transactiontypes` — Transaction types
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-program-types` — Program types
- `KU-PAY-payments-configurations` — Payments configurations
