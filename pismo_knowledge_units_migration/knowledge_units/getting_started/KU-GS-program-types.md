---
ku_id: KU-GS-program-types
title: Program types
category: getting_started
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/program-types.md
  sha256: 753148587f1d05b939b6edc063ea77b8d01f2b4b54b6141ee9e9a0b094450750
  url: https://developers.pismo.io/pismo-docs/docs/program-types
  role: primary_guide
  updated_at: '2026-06-16T15:10:46.000Z'
operations:
- CreateProgramBasedOnTemplate
- PostTransactionFlow
- customerV2Post
- post-acquisitions-v3-s2s-applications
- programParameter
related_kus:
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--customers
- KU-API-core-platform-transactions--transaction-flows
- KU-API-platform-setup-programs--parameters
- KU-API-platform-setup-programs--programs-part-01
- KU-BANK-transaction-banking-accounts
- KU-CARD-card-network-integration
- KU-CARD-get-started-card-issuing
- KU-CARD-zero-balance-integration
- KU-CC-get-started-control-center
- KU-CORE-processing-codes-and-transaction-types
- KU-CORE-program-parameters-reference-table
- KU-CORE-transactiontypes
- KU-CRED-full-balance-credit-program
- KU-CRED-managing-the-charge-order-for-debit-transactions
- KU-EVT-catalogue-account
- KU-EVT-catalogue-other-domains
- KU-GS-setup-overview
- KU-SELL-seller-management-overview-and-onboarding
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Program types

**KU ID:** `KU-GS-program-types` · **Category:** Getting started · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/get-started/program-types.md`:

> Programs are one of the Pismo platform's [core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview#program). Once you've set up your organization, the next step is to implement programs for it. Pismo has the following program types.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/program-types.md`: Program types; Card-issuing; Merchant; Transaction banking; Creating and managing programs; Getting started; Step 1—Determine the processing codes and transaction types your program will use in its operations; Step 2—Set the values for your program parameters; Step 3—Create your program's accounts and customers; Sample credit program

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/program-types.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/program-types · updatedAt: 2026-06-16T15:10:46.000Z

<!-- source:begin path=docs/get-started/program-types.md part=0-end -->

# Program types

Programs are one of the Pismo platform's [core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview#program). Once you've set up your organization, the next step is to implement programs for it. Pismo has the following program types.

# Card-issuing

Pismo has programs for issuing credit, debit, and prepaid cards.

**Note**: **Full balance** and **Zero balance** are Pismo platform card network integration models.  For more information, refer to [Full balance versus Zero balance integration](https://developers.pismo.io/pismo-docs/docs/card-network-integration#full-versus-zero-balance-integration).

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Program type
      </th>

      <th>
        Description
      </th>

      <th>
        Code enum
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Full balance credit
      </td>

      <td>
        Full balance credit accounts.\
        Credit product that enables a cardholder to borrow funds to pay for goods and services. These borrowed amounts must be paid back with interest and any additional agreed-upon charges. Credit cards provide the cardholder with a revolving line of credit, meaning they can borrow up to a certain limit and repay the amount over time.\
        For more information, refer to [Get started with card issuing](https://developers.pismo.io/pismo-docs/docs/get-started-with-card-issuing) and [Full balance credit program](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program)
      </td>

      <td>
        `CREDITO`
      </td>
    </tr>

    <tr>
      <td>
        Zero balance credit
      </td>

      <td>
        Zero balance credit accounts\
        Credit product that enables a cardholder to borrow funds to pay for goods and services. These borrowed amounts must be paid back with interest and any additional agreed-upon charges. Credit cards provide the cardholder with a revolving line of credit, meaning they can borrow up to a certain limit and repay the amount over time.\
        For more information, refer to [ Full balance versus Zero balance integration](https://developers.pismo.io/pismo-docs/docs/card-network-integration#full-versus-zero-balance-integration) and .[Zero balance integration - issuer's guide](https://developers.pismo.io/pismo-docs/docs/zero-balance-integration)
      </td>

      <td>
        `CREDITO ZERO-BALANCE`
      </td>
    </tr>

    <tr>
      <td>
        Full balance debit
      </td>

      <td>
        Full balance debit accounts\
        Operation values are automatically deducted from the cardholder's account.\
        For more information, refer to [Get started with card issuing](https://developers.pismo.io/pismo-docs/docs/get-started-with-card-issuing)  and [Managing the charge order for debit transactions](https://developers.pismo.io/pismo-docs/docs/managing-the-charge-order-for-debit-transactions) .
      </td>

      <td>
        `DEBITO`
      </td>
    </tr>

    <tr>
      <td>
        Zero balance debit
      </td>

      <td>
        Zero balance debit accounts\
        Operation values are automatically deducted from the cardholder's account.\
        For more information, refer to  [Full versus Zero balance integration](https://developers.pismo.io/pismo-docs/docs/card-network-integration#full-versus-zero-balance-integration) and [Zero balance integration - issuer's guide](https://developers.pismo.io/pismo-docs/docs/zero-balance-integration)
      </td>

      <td>
        `DEBITO ZERO-BALANCE`
      </td>
    </tr>

    <tr>
      <td>
        Full balance prepaid
      </td>

      <td>
        Full balance prepaid accounts\
        Similar to a debit card. Requires previously deposited funds, specifically a prior recharge intended for executing payment transactions.\
        For more information, refer to [Get started with card issuing](https://developers.pismo.io/pismo-docs/docs/get-started-with-card-issuing).
      </td>

      <td>
        `PRE-PAGO`
      </td>
    </tr>

    <tr>
      <td>
        Zero balance prepaid
      </td>

      <td>
        Zero balance prepaid accounts\
        Similar to a debit card. Requires previously deposited funds, specifically a prior recharge intended for executing payment transactions.\
        For more refer to  [Full versus Zero balance integration](https://developers.pismo.io/pismo-docs/docs/card-network-integration#full-versus-zero-balance-integration)  and [Zero balance integration - issuer's guide](https://developers.pismo.io/pismo-docs/docs/zero-balance-integration)
      </td>

      <td>
        `PRE-PAGO ZERO-BALANCE`
      </td>
    </tr>

    <tr>
      <td>
        Voucher prepaid
      </td>

      <td>
        Voucher meal/food card.
      </td>

      <td>
        `VOUCHER`
      </td>
    </tr>
  </tbody>
</Table>

# Merchant

| Program type | Description                                                                                                                                                                                                                                            | Code enum  |
| :----------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- |
| Merchant     | Merchant programs manage a seller's commercial accounts. Merchants can register and parameterize their products, rates and fees, home bank, and so on. For more information, refer to the [Seller management overview](https://developers.pismo.io/pismo-docs/docs/seller-management-overview) | `MERCHANT` |

# Transaction banking

Transaction banking focuses on transactions between a bank and a large organization, such as a multinational corporation, lending for short-term expenses and long-term investments. For more information, refer to the [Transaction banking overview](https://developers.pismo.io/pismo-docs/docs/corporate-banking-overview)

| Program type                 | Description                                                                                                                                                                                                                                                                                            | Code enum                |
| :--------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------- |
| Correspondent accounts debit | Accounts financial institutions hold with each other to facilitate international transactions and provide services to their customers in different geographic locations.                                                                                                                               | `CORRESPONDENT ACCOUNTS` |
| Current accounts debit       | Also known as checking accounts, these are a type of deposit account that businesses use to manage their everyday financial transactions. This bank account allows customers to manage their daily finances, serving as a central place to receive income, pay bills, and handle various transactions. | `CURRENT ACCOUNTS`       |
| Internal accounts debit      | Account used within an organization for internal purposes rather than for transactions with external parties. These accounts help manage and track internal financial activities, such as bookkeeping, accounting, and internal fund transfers.                                                        | `INTERNAL ACCOUNTS`      |

# Creating and managing programs

A program's basic structure is detailed in the [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) endpoint. Refer to the [Sample credit program](https://developers.pismo.io/pismo-docs/docs/program-types-copy#sample-credit-program)  below to find out what a typical internal credit program configuration might look like.

You can  [create and manage programs](https://developers.pismo.io/pismo-docs/docs/programs-in-control-center)  using Pismo Control Center.  You can also do the same using the [Programs API](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate).

> 📘 Program implementation
>
> When a program is first created, its status is `PENDING`. To configure PCI cards and accounting, please open a [Jira ticket](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket) . After Pismo's Payment Card Industry (PCI) and accounting teams have done their behind-the-scenes work and configurations, the program's status becomes `ACTIVE` and is available for use.

# Getting started

Once you've picked a program, you need to start doing the following:

## Step 1—Determine the processing codes and transaction types your program will use in its operations

[Processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types), in combination with [transaction types](https://developers.pismo.io/pismo-docs/docs/transactiontypes), define how financial operations are implemented on the Pismo platform. For each organization, Pismo provides a [standard set of processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types#standard-processing-codes).

Pismo  also provides a [standard set of processing codes to transaction types mapping](https://developers.pismo.io/pismo-docs/docs/transactiontypes#standard-processing-code-to-transaction-type-mapping). These mappings are known as **transaction flows**. This is a reference you can use to define the transaction flows for your program. This can be done in [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types-cc) or with the [Create transaction flow](https://developers.pismo.io/pismo-docs/reference/posttransactionflow)  endpoint.

## Step 2—Set the values for your program parameters

Program parameters define limits and what your program allows or doesn't allow. The [Program parameters reference table](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table)  indicates what parameters are automatically assigned to a program depending on its type.  You can set  values for your assigned parameters either in the [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center)  or with the [Programs API](https://developers.pismo.io/pismo-docs/reference/programparameter).

## Step 3—Create your program's accounts and customers

Begin creating your program's [accounts](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) and [customers](https://developers.pismo.io/pismo-docs/reference/customerv2post).

# Sample credit program

Internally, the Pismo platform keeps a JSON file for each program. Below is an example of what a typical credit program might look like, with the processing codes, transaction types, program transaction categories, network acceptances, and program parameters given to a credit program upon creation. Other fields that you need to configure, such as `brand`, `currency_numeric_code`, `bin`, `due_dates`, and other fields are also shown.

<Accordion title="Credit program JSON">
  ```json
  {
    "name": "Cred",
    "program_type": "CREDITO",
    "brand": "VISA",
    "currency_numeric_code": "971",
    "timezone": "Africa/Addis_Ababa",
    "country_code": "AFG",
    "bin": {
      "value": "123121",
      "start_range": "123121",
      "end_range": "567565"
    },
    "due_dates": [
      {
        "day": 1,
        "active": true
      },
      {
        "day": 4,
        "active": true
      },
      {
        "day": 3,
        "active": true
      },
      {
        "day": 5,
        "active": true
      }
    ],
    "programs_parameters": [
      {
        "parameter_name": "VALOR ANUIDADE",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "PARCELAS ANUIDADE",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "PERCENTUAL LIMITE SAQUE",
        "value": 1,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "NUMERO MESES EXPIRACAO CARTAO",
        "value": 60,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "IOF DIARIO",
        "value": 0.0082,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "IOF FIXO",
        "value": 0.38,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "TAMANHO MAX NOME EMBOSSADO",
        "value": 25,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "ACCRUAL_PROJECTION_STRATEGY",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "DIAS ANTECEDENCIA CORTE",
        "value": 10,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "TENTATIVAS SENHA ERRADA",
        "value": 3,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "DIAS ATRASO BLOQUEIO CONTA",
        "value": 10,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "STOP ACCRUAL",
        "value": 63,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "IOF INTERNACIONAL",
        "value": 6.38,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "ATC MIN OFFSET",
        "value": 5,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "ATC MAX OFFSET",
        "value": 15,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "ACCRUAL RATE DISCOUNT",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "IOF_FIRST_DAY",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "CONTROLE DE TROCA DE VENCIMENTOS",
        "value": 1,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "LIMITE GLOBAL MAXIMO",
        "value": 1000,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "LIMITE GLOBAL MINIMO",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "SKIP_RENEW_TEMPORARY_CARD",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "NON_BUSINESS_DAYS",
        "value": 67,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "OVERLIMIT_FEE_AMOUNT",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "ACCEPT_MULTIPLE_PLASTIC_CARDS",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "ACCRUAL_PROJECTION_REVERSAL",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "ACCRUAL_CALC_STRATEGY",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "MIN_PAYMENT_CALC_STRATEGY",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "MINIMO BOLETO",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "OVERDUE_ACCRUAL_CALC_STRATEGY",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "DELINQUENCY_BUCKET_CALC_STRATEGY",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "ALLOW_ACCOUNTS_CREATION",
        "value": 1,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "GRACE_PERIOD_ADDITIONAL_NR_OF_DAYS",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "ACCRUALS_REVERSAL_STRATEGY",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "LATE_PAYMENT_FEE",
        "value": 0,
        "status": "ACTIVE"
      },
      {
        "parameter_name": "OVERLIMIT_PERCENTAGE",
        "valid_from": "2023-05-24T14:32:20Z",
        "value": 0,
        "account_parameter": true,
        "status": "ACTIVE"
      }
    ],
    "transactions_categories": [
      {
        "transaction_category_id": 114121,
        "transaction_category_description": "Trans Nao Financiaveis",
        "refinancing_rate_before_due_date": 0,
        "refinancing_rate_after_due_date": 0,
        "default_rate": 0,
        "fine_rate": 0,
        "overdue_rate_after_due_date": 0,
        "minimum_value": 0,
        "charge_order": 0
      },
      {
        "transaction_category_id": 114122,
        "transaction_category_description": "Trans Financiaveis",
        "refinancing_rate_before_due_date": 0,
        "refinancing_rate_after_due_date": 0,
        "default_rate": 0,
        "fine_rate": 0,
        "overdue_rate_after_due_date": 0,
        "minimum_value": 0,
        "charge_order": 0
      },
      {
        "transaction_category_id": 114123,
        "transaction_category_description": "Internas",
        "refinancing_rate_before_due_date": 0,
        "refinancing_rate_after_due_date": 0,
        "default_rate": 0,
        "fine_rate": 0,
        "overdue_rate_after_due_date": 0,
        "minimum_value": 0,
        "charge_order": 0
      }
    ],
    "programs_transactions_types": [
      {
        "transaction_type_id": 101,
        "transaction_category": "Trans Financiaveis",
        "description": "COMPRA A VISTA"
      },
      {
        "transaction_type_id": 102,
        "transaction_category": "Trans Financiaveis",
        "description": "COMPRA INTERNACIONAL"
      },
      {
        "transaction_type_id": 111,
        "transaction_category": "Trans Financiaveis",
        "description": "PARCELADO SEM JUROS"
      },
      {
        "transaction_type_id": 112,
        "transaction_category": "Trans Financiaveis",
        "description": "PARCELA SEM JUROS"
      },
      {
        "transaction_type_id": 123,
        "transaction_category": "Trans Financiaveis",
        "description": "SAQUE"
      },
      {
        "transaction_type_id": 124,
        "transaction_category": "Trans Financiaveis",
        "description": "SAQUE INTERNACIONAL"
      },
      {
        "transaction_type_id": 201,
        "transaction_category": "Internas",
        "description": "PAGAMENTO"
      },
      {
        "transaction_type_id": 203,
        "transaction_category": "Internas",
        "description": "VOUCHER DE CREDITO"
      },
      {
        "transaction_type_id": 301,
        "transaction_category": "Internas",
        "description": "AJUSTE A CREDITO"
      },
      {
        "transaction_type_id": 302,
        "transaction_category": "Trans Financiaveis",
        "description": "AJUSTE A DEBITO"
      },
      {
        "transaction_type_id": 401,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "ENCARGOS REFINANCIAMENTO"
      },
      {
        "transaction_type_id": 402,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "JUROS DE MORA"
      },
      {
        "transaction_type_id": 403,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "MULTA"
      },
      {
        "transaction_type_id": 404,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "IOF INTERNACIONAL"
      },
      {
        "transaction_type_id": 405,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "IOF"
      },
      {
        "transaction_type_id": 406,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "IOF SAQUE"
      },
      {
        "transaction_type_id": 407,
        "transaction_category": "Trans Financiaveis",
        "description": "ENCARGOS SAQUE"
      },
      {
        "transaction_type_id": 408,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "DEBITO DIF CAMBIAL"
      },
      {
        "transaction_type_id": 409,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "CREDITO DIF CAMBIAL"
      },
      {
        "transaction_type_id": 417,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "IOF PARCELAMENTO"
      },
      {
        "transaction_type_id": 451,
        "transaction_category": "Internas",
        "description": "ESTORNO ENCARGOS REFINANC"
      },
      {
        "transaction_type_id": 452,
        "transaction_category": "Internas",
        "description": "ESTORNO JUROS DE MORA"
      },
      {
        "transaction_type_id": 453,
        "transaction_category": "Internas",
        "description": "ESTORNO MULTA"
      },
      {
        "transaction_type_id": 455,
        "transaction_category": "Internas",
        "description": "ESTORNO IOF"
      },
      {
        "transaction_type_id": 503,
        "transaction_category": "Internas",
        "description": "CANC DE COMPRA"
      },
      {
        "transaction_type_id": 504,
        "transaction_category": "Internas",
        "description": "CANC PARCELADO SEM JUROS"
      },
      {
        "transaction_type_id": 505,
        "transaction_category": "Internas",
        "description": "CANC PARCELA SEM JUROS"
      },
      {
        "transaction_type_id": 508,
        "transaction_category": "Internas",
        "description": "CANC COMPRA INTERNACIONAL"
      },
      {
        "transaction_type_id": 509,
        "transaction_category": "Internas",
        "description": "CANC IOF INTERNACIONAL"
      },
      {
        "transaction_type_id": 512,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "ESTORNO SAQUE"
      },
      {
        "transaction_type_id": 513,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "ESTORNO ENCARGOS SAQUE"
      },
      {
        "transaction_type_id": 602,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "ANUIDADE"
      },
      {
        "transaction_type_id": 604,
        "transaction_category": "Trans Financiaveis",
        "description": "TARIFA SAQUE"
      },
      {
        "transaction_type_id": 606,
        "transaction_category": "Internas",
        "description": "ESTORNO DE ANUIDADE"
      },
      {
        "transaction_type_id": 617,
        "transaction_category": "Internas",
        "description": "ESTORNO TARIFA SAQUE INTER"
      },
      {
        "transaction_type_id": 676,
        "transaction_category": "Trans Financiaveis",
        "description": "OVERLIMIT FEE"
      },
      {
        "transaction_type_id": 701,
        "transaction_category": "Internas",
        "description": "CREDITO POR PARCELAMENTO"
      },
      {
        "transaction_type_id": 702,
        "transaction_category": "Trans Financiaveis",
        "description": "PARCELA DE REFINANCIAMENTO"
      },
      {
        "transaction_type_id": 703,
        "transaction_category": "Internas",
        "description": "CONTRATO REFINANCIAMENTO"
      },
      {
        "transaction_type_id": 704,
        "transaction_category": "Internas",
        "description": "CANC PARCELA REFINANC"
      },
      {
        "transaction_type_id": 705,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "CANC CREDITO PARCELAMENTO"
      },
      {
        "transaction_type_id": 706,
        "transaction_category": "Internas",
        "description": "CANC CONTRATO REFINANC"
      },
      {
        "transaction_type_id": 711,
        "transaction_category": "Internas",
        "description": "CREDITO POR ACORDO"
      },
      {
        "transaction_type_id": 712,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "PARCELA DE ACORDO"
      },
      {
        "transaction_type_id": 713,
        "transaction_category": "Internas",
        "description": "CONTRATO DE ACORDO"
      },
      {
        "transaction_type_id": 714,
        "transaction_category": "Internas",
        "description": "CANC PARCELA ACORDO"
      },
      {
        "transaction_type_id": 715,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "CANC CREDITO ACORDO"
      },
      {
        "transaction_type_id": 716,
        "transaction_category": "Internas",
        "description": "CANCELAMENTO CONTRATO ACORDO"
      },
      {
        "transaction_type_id": 721,
        "transaction_category": "Internas",
        "description": "CREDITO POR PARCELAMENTO CP"
      },
      {
        "transaction_type_id": 722,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "PARCELA DE REFINANCIAMENTO CP"
      },
      {
        "transaction_type_id": 723,
        "transaction_category": "Internas",
        "description": "CONTRATO REFINANCIAMENTO CP"
      },
      {
        "transaction_type_id": 724,
        "transaction_category": "Internas",
        "description": "CANC PARC DE REF CP"
      },
      {
        "transaction_type_id": 725,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "CANC CREDITO PARCELAMENTO CP"
      },
      {
        "transaction_type_id": 726,
        "transaction_category": "Internas",
        "description": "CANC CONTRATO REF CP"
      },
      {
        "transaction_type_id": 4089,
        "transaction_category": "Internas",
        "description": "ESTORNO DEBITO DIF CAMBIAL"
      },
      {
        "transaction_type_id": 4099,
        "transaction_category": "Trans Financiaveis",
        "description": "ESTORNO CREDITO DIF CAMBIAL"
      },
      {
        "transaction_type_id": 4519,
        "transaction_category": "Trans Financiaveis",
        "description": "CANC ESTORNO ENCARGOS REFINANC"
      },
      {
        "transaction_type_id": 4529,
        "transaction_category": "Trans Financiaveis",
        "description": "CANC ESTORNO JUROS DE MORA"
      },
      {
        "transaction_type_id": 4539,
        "transaction_category": "Trans Financiaveis",
        "description": "CANC ESTORNO MULTA"
      },
      {
        "transaction_type_id": 4559,
        "transaction_category": "Trans Financiaveis",
        "description": "CANC ESTORNO IOF"
      },
      {
        "transaction_type_id": 6769,
        "transaction_category": "Internas",
        "description": "OVERLIMIT FEE REVERSAL"
      },
      {
        "transaction_type_id": 9467,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "ESTORNO TARIFA SAQUE"
      },
      {
        "transaction_type_id": 9469,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "ESTORNO IOF SAQUE"
      },
      {
        "transaction_type_id": 40899,
        "transaction_category": "Trans Financiaveis",
        "description": "CANC EST DEBITO DIF CAMBIAL"
      },
      {
        "transaction_type_id": 40999,
        "transaction_category": "Internas",
        "description": "CANC EST CREDITO DIF CAMBIAL"
      },
      {
        "transaction_type_id": 45359,
        "description": "dfdsff"
      },
      {
        "transaction_type_id": 45565,
        "description": "tt teste 455"
      },
      {
        "transaction_type_id": 45566,
        "description": "Canc tt teste 455"
      },
      {
        "transaction_type_id": 67699,
        "transaction_category": "Internas",
        "description": "OVERLIMIT FEE REV CANC"
      },
      {
        "transaction_type_id": 99602,
        "transaction_category": "Trans Nao Financiaveis",
        "description": "CANC ESTORNO ANUIDADE"
      }
    ],
    "network_acceptances": [
      {
        "processing_code": "00",
        "credit_limit_impact_id": 1,
        "credit_limit_impact_description": "COMPRA GLOBAL",
        "impact_only_conciliation": 0
      },
      {
        "processing_code": "0001",
        "credit_limit_impact_id": 4,
        "credit_limit_impact_description": "PAGAMENTO",
        "impact_only_conciliation": 0
      },
      {
        "processing_code": "0101",
        "credit_limit_impact_id": 4,
        "credit_limit_impact_description": "PAGAMENTO",
        "impact_only_conciliation": 0
      },
      {
        "processing_code": "01",
        "credit_limit_impact_id": 2,
        "credit_limit_impact_description": "SAQUE CREDITO",
        "impact_only_conciliation": 0
      },
      {
        "processing_code": "20",
        "credit_limit_impact_id": 4,
        "credit_limit_impact_description": "PAGAMENTO",
        "impact_only_conciliation": 1
      },
      {
        "processing_code": "203100",
        "credit_limit_impact_id": 4,
        "credit_limit_impact_description": "PAGAMENTO",
        "impact_only_conciliation": 1
      },
      {
        "processing_code": "003101",
        "credit_limit_impact_id": 4,
        "credit_limit_impact_description": "PAGAMENTO",
        "impact_only_conciliation": 0
      },
      {
        "processing_code": "003100",
        "credit_limit_impact_id": 1,
        "credit_limit_impact_description": "COMPRA GLOBAL",
        "impact_only_conciliation": 0
      },
      {
        "processing_code": "003801",
        "credit_limit_impact_id": 4,
        "credit_limit_impact_description": "PAGAMENTO",
        "impact_only_conciliation": 0
      },
      {
        "processing_code": "003800",
        "credit_limit_impact_id": 1,
        "credit_limit_impact_description": "COMPRA GLOBAL",
        "impact_only_conciliation": 0
      },
      {
        "processing_code": "004000",
        "credit_limit_impact_id": 4,
        "credit_limit_impact_description": "PAGAMENTO",
        "impact_only_conciliation": 0
      },
      {
        "processing_code": "013101",
        "credit_limit_impact_id": 4,
        "credit_limit_impact_description": "PAGAMENTO",
        "impact_only_conciliation": 0
      },
      {
        "processing_code": "013100",
        "credit_limit_impact_id": 1,
        "credit_limit_impact_description": "COMPRA GLOBAL",
        "impact_only_conciliation": 0
      }
    ]
  }
  ```

  <br />
</Accordion>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /v1/transaction-flow` | `PostTransactionFlow` | Create transaction flow | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |
| `GET /programs/v1/programs/{program_id}/parameters` | `programParameter` | List program parameters | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /accounts/v2/customers` | `customerV2Post` | Create customer | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |

### Operation essentials

- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /v1/transaction-flow`** (`PostTransactionFlow`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `processing_code`, `key`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00003`, `WTRC00005`, `WTRC04003`, `WTRC04004`, `WTRC04005`, `WTRC04006`, `WTRC05003`, `WTRC07001`, `WTRC04001`, `ETRC04003`, `ETRC04004`, `ETRC04005`, `ETRC04006`, `WTRC08001`, `ETRC00001`; events none listed.
- **`GET /programs/v1/programs/{program_id}/parameters`** (`programParameter`): security `S2SAuthentication`; required parameters `program_id` (path); required body fields none declared; response statuses 200, 400; error codes in examples none; events none listed.
- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /accounts/v2/customers`** (`customerV2Post`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `entity`, `customer`; response statuses 201, 400, 409, 500; error codes in examples none; events `account-account-owner-change-1`, `account-customer-creation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `customerV2Post` | `account-account-owner-change-1` |
| `customerV2Post` | `account-customer-creation-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/get-started/program-types.md`: updatedAt 2026-06-16T15:10:46.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/program-types.md` | whole document | https://developers.pismo.io/pismo-docs/docs/program-types | `753148587f1d05b9…` | 2026-06-16T15:10:46.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--customers` — API reference: Core platform - Accounts — Customers
- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-platform-setup-programs--parameters` — API reference: Platform setup - Programs — Parameters
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-BANK-transaction-banking-accounts` — Transaction banking and transaction banking accounts
- `KU-CARD-card-network-integration` — Card network integration and certification
- `KU-CARD-get-started-card-issuing` — Get started with card issuing
- `KU-CARD-zero-balance-integration` — Zero balance integration and anti-fraud validations
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-CORE-transactiontypes` — Transaction types
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
- `KU-CRED-managing-the-charge-order-for-debit-transactions` — Managing the charge order for debit transactions
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-setup-overview` — Core objects
- `KU-SELL-seller-management-overview-and-onboarding` — Seller management overview and onboarding
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
