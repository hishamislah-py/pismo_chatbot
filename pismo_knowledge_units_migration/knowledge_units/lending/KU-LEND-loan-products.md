---
ku_id: KU-LEND-loan-products
title: 'Loan products: overview and creation'
category: lending
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/lending/loan-product-overview.md
  sha256: b7ae47f77f25c6728a57657facad83af783b71dbfa0370e106b18904140b7041
  url: https://developers.pismo.io/pismo-docs/docs/loan-product-overview
  role: primary_guide
  updated_at: '2026-09-11T12:33:58.000Z'
- path: docs/lending/create-loan-products.md
  sha256: 09427642a4da61de5925e269a33e6a5457154d537ae8cfb0c4c33d53fcc8d246
  url: https://developers.pismo.io/pismo-docs/docs/create-loan-products
  role: primary_guide
  updated_at: '2026-09-22T17:42:19.000Z'
operations:
- CreateProcessingCode
- createLoanProductV2
- createRepaymentHierarchyV2
- post-v1-interest-plan
related_kus:
- KU-API-banking-interest-engine--interest-engine
- KU-API-lending--loan-products
- KU-API-lending--repayment-hierarchy
- KU-API-platform-setup-orgs-operation--processing-codes
- KU-CC-deposit-products
- KU-CC-lending
- KU-CC-processing-codes
- KU-EVT-catalogue-interest
- KU-EVT-catalogue-lending
- KU-EVT-catalogue-other-domains
grouping_rationale: Concept and creation.
---

# Loan products: overview and creation

**KU ID:** `KU-LEND-loan-products` · **Category:** Lending · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Concept and creation.

Scope as stated in `docs/lending/loan-product-overview.md`:

> You can create loan products to match your business requirements and the types of loans you want to offer. A loan product defines the options and rules individual loans inherit, including how often repayments are due, how interest is calculated, what limits apply, and so on. Loan products act as templates for your loans, so configuring them is a required first step before you can create individual loans.

Scope as stated in `docs/lending/create-loan-products.md`:

> Use this guide to create your loan products. Before starting—or at any time in this process—if you need more foundational information about loan products, refer to [Loan product overview](https://developers.pismo.io/pismo-docs/docs/loan-product-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/lending/loan-product-overview.md`: Loan product overview; Loan product types; Personal; BNPL; Loan configuration options
- `docs/lending/create-loan-products.md`: Create loan products; Prerequisites; Create a repayment hierarchy; Create interest plans; Create processing codes; Create a loan product; Scenario—Create a BNPL loan product

## Prerequisites and dependencies

- Prerequisites are described in `docs/lending/create-loan-products.md` section "Prerequisites".
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/lending/loan-product-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/loan-product-overview · updatedAt: 2026-09-11T12:33:58.000Z

<!-- source:begin path=docs/lending/loan-product-overview.md part=0-end -->

# Loan product overview

You can create loan products to match your business requirements and the types of loans you want to offer. A loan product defines the options and rules individual loans inherit, including how often repayments are due, how interest is calculated, what limits apply, and so on. Loan products act as templates for your loans, so configuring them is a required first step before you can create individual loans.

It's possible to create multiple loan products to distinguish and grow your lending portfolio. For example, you might create one Buy Now, Pay Later (BNPL) loan product for a group of similar items in your storefront, or build separate loan products for each individual item you sell. Later, as you add inventory, you can create new loan products.

# Loan product types

You can create personal and BNPL loan products.

## Personal

A personal loan is an unsecured loan issued to an individual and repaid over multiple installments. Its features include:

* Installments calculated using a reducing balance
* Weekly, biweekly, monthly, or quarterly repayment plans
* Auto‑collection from a bank account or card
* Partial repayment options that adjust installment amount or loan terms
* Early full repayment options

**Example:** A customer wants to renovate their kitchen and takes out a personal loan to cover $15,000 in remodeling costs, then repays the loan over a set period with fixed monthly payments.

## BNPL

A BNPL loan is an unsecured loan issued at checkout for a purchase amount. Its features include:

* Interest‑free periods
* Biweekly or monthly repayment frequencies
* Disbursement directly to merchants
* Auto‑repayment from a bank account or card
* Contract cancellation for returns
* Charges for missed payments or post‑promotion interest
* Live data streams for notifications, reporting, and artificial intelligence and machine learning integrations
* In some regions, BNPL loans are not subject to credit checks. Confirm whether this applies in your region.

**Example:** A customer buys a $600 smartphone and chooses **Buy Now, Pay Later** at checkout. The total purchase price is split into four equal payments. They pay the four installments over the next four months.

# Loan configuration options

When creating your loan products, in addition to the loan type, you define various options, including:

* **Disbursement options**—How and when loan funds are released to the borrower. You can disburse in a single lump sum, through multiple payments, or let the lender handle disbursement outside of Pismo in the lender’s own system.
* **Repayment options**—How the Pismo platform calculates repayment schedules, including:
  * **Repayment calculation method**—The repayments are either **flat**, where borrowers pay the same amount each cycle, or **reducing**, where they pay a larger amount in the first cycle and a decreasing amount for each cycle after that.
  * **Frequency**—How often payments must be paid: biweekly, monthly, quarterly, and annually
* **Interest rate options**—Controls interest behavior, including:
  * **Moratorium interest**—Amortizes accrued interest over the remaining loan term
  * **Interest-only installments**—Allows reduced payments for part of the loan while keeping the loan principal amount unchanged
  * **Early final settlement**—Allows a single final repayment before the final scheduled payment date
* **Grace period**—The number of calendar days after an installment due date during which the Pismo platform does not apply late fees or mark the repayment as delinquent, between 0-365 days. <br /><br /> During the grace period, the arrears counter still runs in the background, starting from the original due date. If the customer pays within the grace period, there is no impact to the customer and no late fees or penalties are charged. If the customer pays after the grace period ends, the arrears counter shows the days past due, and late fees or penalties are calculated from the due date.
* **Rules**—Set limits for these loan values:
  * **Loan amount**—Maximum amount that can be borrowed
  * **Number of installments**—Maximum number of installments used to split each repayment
  * **Loan term length**—Maximum time the borrower has to repay the loan
  * **Interest rate** —Maximum interest rate that can be applied to the loan amount
* **Charge plan codes**—Links service charges, fees, or taxes to a product or service

<br />
<!-- source:end -->

### Source 2: `docs/lending/create-loan-products.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/create-loan-products · updatedAt: 2026-09-22T17:42:19.000Z

<!-- source:begin path=docs/lending/create-loan-products.md part=0-end -->

# Create loan products

Use this guide to create your loan products. Before starting—or at any time in this process—if you need more foundational information about loan products, refer to [Loan product overview](https://developers.pismo.io/pismo-docs/docs/loan-product-overview).

# Prerequisites

Before creating your loan product, you must set up the following:

* [Repayment hierarchy](https://developers.pismo.io/pismo-docs/docs/create-loan-products#create-repayment-hierarchy)
* [Interest plan](https://developers.pismo.io/pismo-docs/docs/create-loan-products#create-interest-plan)
* [Processing codes](https://developers.pismo.io/pismo-docs/docs/create-loan-products#create-processing-codes)

## Create a repayment hierarchy

Use the repayment hierarchy to define the order that loan components are paid, such as principal, interest, fees, and so on. You can use Control Center or the API.

| Method         | Description                                                                                                    | For more information                                         |
| :------------- | :------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| Control Center | Create processing codes for repayment and select them during loan creation (repayment processing codes types). | [Loan products](https://developers.pismo.io/pismo-docs/docs/loan-products-cc)                        |
| API            | Use the **Create repayment hierarchy** endpoint.                                                               | [Create repayment hierarchy](https://developers.pismo.io/pismo-docs/reference/createrepaymenthierarchyv2) |

Use the [Create repayment hierarchy](https://developers.pismo.io/pismo-docs/reference/createrepaymenthierarchyv2) endpoint with the following payload to indicate the order that you want for each loan component.

<Accordion title="Request payload">
  ```json
  {
      "hierarchy_code": "HIERARCHY_001",
      "hierarchy": [
        "PRINCIPAL",
        "INTEREST",
        "TAX",
        "FEE",
        "CHARGE",
        "PENALTY",
        "INSURANCE"
      ]
  }
  ```
</Accordion>

How the request is structured:

| Parameter       | Description                                                                                                                                                                                                                                               |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hierarchy\_code | Specifies a unique identifier for the repayment hierarchy. Reference this code when creating a loan product to associate the hierarchy with that product.                                                                                                 |
| hierarchy       | Defines the repayment priority order. This array must include all seven components the order repayments are applied. In the previous example, repayments are applied to principal first, then interest, tax, fee, charge, penalty, and finally insurance. |

## Create interest plans

Create interest plans to define how interest is calculated and applied to loan products. You can use Control Center or the API.

| Method         | Description                                                                                          | For more information                                                                       |
| :------------- | :--------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| Control Center | You must first create interest plans, then you can add them to your loan products in Control Center. | To create interest plans, refer to [Interest plans](https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center). |
| API            | Use the **Create interest plan** endpoint.                                                           | [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan)                                          |

Use the [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan) endpoint to define the interest type, rate, and so on.

<Accordion title="Request payload">
  ```json
  {
      "accrual_basis": "ACTUAL/365",
      "accrual_frequency": "DAILY",
      "capitalisation_frequency": "DAILY",
      "currency_code": "986",
      "description": "INTEREST PLAN FOR BNPL LENDING",
      "interest_type": "SIMPLE",
      "operation_type": "DEBIT",
      "fixed_interest_rate": 0.8,
      "start_date": "2025-09-17",
      "metadata": {
          "sample": "QUARTERLY"
      }
  }
  ```
</Accordion>

This endpoint generates an [Interest plan created](https://developers.pismo.io/events/docs/interest-management-interest-plan-creation-success-1) event.

## Create processing codes

Processing codes identify the financial operations that occur across the loan lifecycle and determine the balance impact of each operation (such as credit, debit, or no impact). Some important points to keep in mind:

* Each loan product requires at least one Booking processing code and one Repayment processing code.
  * **Booking processing codes** define how the loan is booked, such as its accounting impact for disbursement. When creating Booking processing codes, set the balance impact to either **debit** or **no impact** (Zero balance) because booking processing codes increase loan exposure.
  * **Repayment processing codes** define how the loan is repaid, such as updating the payment schedule or adjusting the balance. When creating Repayment processing codes, set the balance impact to **credit** because loan repayments decrease the customer's outstanding loan balance.
* Once you associate a Booking processing code with a loan product, you cannot use the same processing code with any other active loan product. If you later make the loan product inactive, the processing code becomes available and you can associate it with a different loan product.
* If a loan product includes a grace period, you must also configure a **Penalty waiver processing code** to define how penalties are handled during that period, such as allowing a borrower to repay a loan early without incurring an early repayment fee.
* All other processing codes are optional when creating loan products.
* You must tag your processing codes with **Lending** or **BNPL**.

You can use Control Center or the API.

| Method         | Description                                                                                                 | For more information                                                                                                                     |
| :------------- | :---------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| Control Center | You must first create your processing codes, then you can add them to your loan products in Control Center. | To create processing codes, refer to [Create processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/create-processing-codes-and-transaction-types). |
| API            | Use the **Create processing code** endpoint.                                                                | [Create processing code](https://developers.pismo.io/pismo-docs/reference/createprocessingcode)                                                                                       |

Use the [Create processing code](https://developers.pismo.io/pismo-docs/reference/createprocessingcode) endpoint to create a Booking processing code that has a `BNPL` tag:

<Accordion title="Booking processing code request example">
  ```json
  {
    "processing_code": "WC2TH",
    "balance_impact": -1,
    "description": "BNPL BOOKING",
    "reversal_processing_code": "PSM004",
    "partial_reversal_processing_code": "000515",
    "tags": [
      "BNPL"
    ]
  }
  ```
</Accordion>

# Create a loan product

You’re ready to create a loan product. Whether you use Control Center or the API, you’ll find the steps you need in the associated guides and reference material.

| Method         | Description                                                         | For more information                           |
| :------------- | :------------------------------------------------------------------ | :--------------------------------------------- |
| Control Center | Use the Control Center creation wizard to create your loan product. | [Loan products](https://developers.pismo.io/pismo-docs/docs/loan-products-cc)          |
| API            | Use the **Create loan product** endpoint.                           | [Create loan product](https://developers.pismo.io/pismo-docs/reference/createloanproductv2) |

# Scenario—Create a BNPL loan product

In this example, a BNPL loan is created in Brazilian Real (currency code 986). The loan product specifies a single lump-sum disbursement, and the loan becomes active as soon as it is booked.

<Accordion title="Create a BNPL loan product request example">
  ```json
  {
      "product_name": "Complete BNPL with Prepayment info",
      "product_type": "BNPL",
      "processing_codes": {
          "booking": [
              "bookJ3V1H"
          ],
          "repayment": [
              "repayM7QR"
          ],
          "restructuring": [
              "restructure6YCZ"
          ],
          "present_value_discount": [
              "discount155V"
          ],
          "early_final_settlement": {
              "fee": [
                  "efsMRT0"
              ]
          },
          "insurance": {
              "booking": [
                  "insLP28"
              ],
              "repayment": [
                  "insrepayGH39"
              ]
          },
          "disbursement": {
              "internal": [
                  "internalFVVX"
              ],
              "external": [
                  "externalPVTQ"
              ]
          },
          "prepayment": {
              "fee": [
                  "prepaymentDRV0"
              ]
          }
      },
      "loan_activation_method": "ON_BOOKING",
      "currency": "986",
      "collateral": "NONE",
      "disbursement_method": {
          "type": "SINGLE"
      },
      "interest_plan_ids": [
          "712edbb8-5005-4f41-af95-dc2014f4045d"
      ],
      "repayment_hierarchy_code": "HIERARCHY_FEE_FIRST",
      "prepayment": {
          "penalty": {
              "type": "FIXED_AMOUNT", // PERCENTAGE or "FIXED_AMOUNT"
              "value": 20.0
          },
          "lock_in_period": 0, // optional, >= 0
          "reduce_option": [
              "INSTALLMENT",
              "TERM"
          ] // required, at least one
      },
      "early_final_settlement": {
          "penalty": {
              "type": "PERCENTAGE",
              "value": 0.1
          },
          "lock_in_period": 2
      }
  }
  ```
</Accordion>

After you create the loan product, the API response returns the `product_id`. Use this ID to book a loan.

```json
{
    "product_id": "2717a296-124a-47cc-b2a1-91e80dc723eb"
}
```

<br />

<br />

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v2/repayment-hierarchies` | `createRepaymentHierarchyV2` | Create repayment hierarchy | `api-specs/Lending.yaml` | no | KU-API-lending--repayment-hierarchy |
| `POST /v1/interest/plan` | `post-v1-interest-plan` | Create interest plan | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `POST /orgs-operation/v1/processing-codes` | `CreateProcessingCode` | Create processing code | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `POST /v2/loan-products` | `createLoanProductV2` | Create loan product | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |

### Operation essentials

- **`POST /v2/repayment-hierarchies`** (`createRepaymentHierarchyV2`): security `BearerAuth`; required parameters `Idempotency-Key` (header); required body fields `hierarchy`, `hierarchy_code`; response statuses 201, 202, 400, 500; error codes in examples `WLND0001`, `ELND0601`, `ELND0603`, `ELND0605`, `ELND0606`, `ELND0607`, `ELND0608`, `ELND0001`; events none listed.
- **`POST /v1/interest/plan`** (`post-v1-interest-plan`): security `BearerAuth`; required parameters none declared; required body fields `accrual_basis`, `accrual_frequency`, `capitalization_frequency`, `currency_code`, `description`, `interest_type`, `start_date`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `interest-engine-interest-plan-creation-success-1`.
- **`POST /orgs-operation/v1/processing-codes`** (`CreateProcessingCode`): security `S2SAuthentication`; required parameters none declared; required body fields `processing_code`, `balance_impact`, `description`, `reversal_processing_code`; response statuses 201, 400; error codes in examples none; events `orgs-operation-create-1`.
- **`POST /v2/loan-products`** (`createLoanProductV2`): security `BearerAuth`; required parameters none declared; required body fields `collateral`, `currency`, `disbursement_method`, `processing_codes`, `product_name`, `product_type`; response statuses 201, 202, 400, 500; error codes in examples `ELND1501`, `ELND0350`, `ELND0351`, `ELND0352`, `ELND0353`, `ELND0354`, `ELND0355`, `ELND0356`, `ELND0357`, `ELND0358`, `ELND0359`, `ELND0360`, `ELND0361`, `ELND0362`, `ELND0363`, `ELND0380`, `ELND0011`, `ELND0012`, `ELND0379`, `ELND0001`; events `lending-loan-product-creation-3`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-interest-plan` | `interest-engine-interest-plan-creation-success-1` |
| `createLoanProductV2` | `lending-loan-product-creation-3` |
| `CreateProcessingCode` | `orgs-operation-create-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `interest-management-interest-plan-creation-success-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-management-interest-plan-creation-success-1 | 1 | KU-EVT-catalogue-interest |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/lending/loan-product-overview.md`: updatedAt 2026-09-11T12:33:58.000Z.
- `docs/lending/create-loan-products.md`: updatedAt 2026-09-22T17:42:19.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/lending/loan-product-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/loan-product-overview | `b7ae47f77f25c672…` | 2026-09-11T12:33:58.000Z |
| `docs/lending/create-loan-products.md` | whole document | https://developers.pismo.io/pismo-docs/docs/create-loan-products | `09427642a4da61de…` | 2026-09-22T17:42:19.000Z |

## Related knowledge units

- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--repayment-hierarchy` — API reference: Lending — Repayment hierarchy
- `KU-API-platform-setup-orgs-operation--processing-codes` — API reference: Platform setup - Orgs operation — Processing codes
- `KU-CC-deposit-products` — Control Center deposit products and interest plans
- `KU-CC-lending` — Control Center lending: loan products and loan management
- `KU-CC-processing-codes` — Control Center processing codes, transaction types and general ledger accounts
- `KU-EVT-catalogue-interest` — Event catalogue: interest
- `KU-EVT-catalogue-lending` — Event catalogue: lending
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
