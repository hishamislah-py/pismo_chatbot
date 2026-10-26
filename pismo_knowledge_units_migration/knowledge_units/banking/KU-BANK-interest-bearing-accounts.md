---
ku_id: KU-BANK-interest-bearing-accounts
title: Interest-bearing accounts
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/interest-bearing-accounts.md
  sha256: de8147ab1a30f15e8ac98894ff0bbc670084f882651ae0c29d0ed73d071789ac
  url: https://developers.pismo.io/pismo-docs/docs/interest-bearing-accounts
  role: primary_guide
  updated_at: '2026-10-07T15:28:28.000Z'
operations:
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-create-savings-account-product
- interest-bearing-v1-deposit-account-open
- interest-bearing-v1-deposit-attach-account
- interest-bearing-v1-deposit-update-account-attachment
- interest-bearing-v1-deposit-update-payout-account
- interest-bearing-v1-list-products
- interest-bearing-v1-patch-deposit-product
- interest-bearing-v1-savings-account-attach-account
- interest-bearing-v1-savings-account-update-payout-account
- post-v1-interest-plan
related_kus:
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-API-banking-interest-bearing-accounts--deposit-account-open
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-engine--interest-engine
- KU-BANK-penalties-for-cd-accounts
- KU-CC-deposit-products
- KU-CC-fee-models
- KU-CORE-fee-models
- KU-CORE-fee-models-create-and-simulate
- KU-EVT-catalogue-deposit
- KU-EVT-catalogue-interest
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Interest-bearing accounts

**KU ID:** `KU-BANK-interest-bearing-accounts` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/interest-bearing-accounts.md`:

> Banks and financial institutions offer various types of accounts that can earn interest, including savings accounts and deposit accounts. These accounts are typically used for short-term savings, emergency funds, specific goals like travel or major purchases, or as part of a diversified investment strategy. They provide a safer alternative to riskier investment options and offer a convenient solution for saving money while accruing interest. These accounts can often be created as sub-accounts by account holders through their banking apps.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/interest-bearing-accounts.md`: Interest-bearing accounts; Interest-bearing accounts on the Pismo platform; Banking by Pismo; Override account-level configurations; Maturity notices; Funding duration; Pismo integration with other banking systems; Penalties for deposit products; Output events; Interest capitalization ledger entries; Regulatory reports; Examples; Scenario 1; Scenario 2; Common configuration parameters

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 11 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/interest-bearing-accounts.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/interest-bearing-accounts · updatedAt: 2026-10-07T15:28:28.000Z

<!-- source:begin path=docs/core-banking/interest-bearing-accounts.md part=0-end -->

# Interest-bearing accounts

Banks and financial institutions offer various types of accounts that can earn interest, including savings accounts and deposit accounts. These accounts are typically used for short-term savings, emergency funds, specific goals like travel or major purchases, or as part of a diversified investment strategy. They provide a safer alternative to riskier investment options and offer a convenient solution for saving money while accruing interest. These accounts can often be created as sub-accounts by account holders through their banking apps.

The Pismo platform offers an [API](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-list-products) that supports a wide range of interest-bearing accounts, including savings and deposit accounts, all capable of performing daily interest calculations and payouts as well as on a monthly, quarterly, semi-annual, annual basis, or at its maturity.

Pismo offers the following bank account products, each with its own specific rules and benefits:

* **Savings account product**: These accounts can be created as sub-accounts in banking apps, allowing for easy deposit and withdrawal of funds.

* **Deposit product**: Also known as Certificates of Deposit (CDs), these accounts have a preset maturity date. Customers must leave their money in the account for an agreed-upon term. Early withdrawals may incur fees, and these accounts often have a minimum deposit requirement, a maximum balance limit, and a cooling-off period. They offer various rule possibilities, making them versatile for clients looking for different interest calculation options.

The return, interest rate, and other features of these accounts depend on the account terms and conditions and can vary based on the account type and the financial institution. They might require a minimum deposit or balance, have restrictions on withdrawals and transfers, and the terms can change over time.

Deposit accounts are particularly popular on the Pismo platform due to their ability to support multiple rule possibilities, while savings accounts remain more basic. The interest-bearing accounts solution from Pismo is notable for its robust capability to process large volumes of daily operations, fully customizable fee and interest calculations, and the generation of legal reports.

This guide provides information on the available options to set up interest-bearing accounts on the Pismo platform, including common parameters, outputs, and examples.

# Interest-bearing accounts on the Pismo platform

## Banking by Pismo

If you maintain accounts on the Pismo platform as part of its core banking solution, you have seamless access to the products and solutions offered by Pismo and are uniquely set up to take advantage of their flexible configurations and high-capacity processing.

In this case, work with the Pismo representative to set up interest-bearing accounts. **Note that you can also set up the following steps in Pismo Control Center**:

<Image align="center" alt="Pismo banking workflow" caption="Figure 1: Pismo banking workflow" src="https://files.readme.io/68067c512e23ef748f6e51e6b14de2d6922ffa5605c2d4d5b019d0742ddfea34-interest-bearing-accounts-core-banking-by-pismo.png" />

> 📘 Note
>
> Use [Open deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-account-open) if you want to streamline three operations in one: specify a transaction banking account (`external_account_id`), attach product to it (using `product_id`), and set renewal instructions (using `renewal_term`). This ensures atomic account creation and configuration.

1. If applicable, set up the [fee model](https://developers.pismo.io/pismo-docs/docs/fee-models) in the Pismo platform to withhold any taxes or operational fees. Refer to  [Fee models](https://developers.pismo.io/pismo-docs/docs/fee-models-in-control-center) for how to set this up in Control Center.
2. Configure a [flexible plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan) to accrue interest according to your needs. To set this up in Control Center, refer to [Interest plans](https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center).
3. Create a product ([Savings](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-savings-account-product) or [Deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)) in the Pismo platform. Refer to [Deposit products](https://developers.pismo.io/pismo-docs/docs/deposit-products-in-control-center) if you want to configure it using Control Center.
4. Attach the product you created to specific accounts or all accounts in a program. Note that you cannot attach more than one product to the same program or account.

> 📘 Note
>
> You can optionally attach a [deposit](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account) or [savings](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-attach-account) account to a product using a past effective date, with all product lifecycle events and calculations based on that historical start date.

5. Define a renewal term using [Attach deposit to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account), to be applied at maturity to the next deposit cycle. To update a renewal term, use [Update deposit account attachment overrides](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-account-attachment).
6. Once complete, events are generated to notify you of the interest to be posted. For more information, refer to [Output events](#output-events).

> 📘 Minimum amount for interest calculation
>
> * You have the option to specify a minimum amount used for interest calculation, either at the program level or for a specific account ID. Specify a value in the `min_amount` field of [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product) or [Create savings account product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-savings-account-product). If you choose not to set a minimum, interest is calculated on any amount.

### Override account-level configurations

You can override account-level configurations inherited from the product, this includes:

* Maturity instructions
* Renewal term
* Penalties
* Payout account

Refer to [Update deposit account attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-account-attachment) for rule overrides (`overrides`, only for deposit accounts) and [Update payout account for deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-payout-account) (`payout_account`) for [savings](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-update-payout-account) and [deposit](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-payout-account) account overrides.

### Maturity notices

Supports configuring up to three maturity notices for a deposit product. When a configured notice date is reached, Pismo platform sends an event indicating that the account is approaching maturity. For example, notices can be set for 30, 14, and 7 days before maturity. The configuration is optional and can be [created](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product) or [updated](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-patch-deposit-product) after product creation. Refer to `notices` in [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product).

### Funding duration

When you [create a deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product) without specifying a value in `funding_duration`, a newly created deposit account begins in a `BLOCKED` status, and it always accepts cash in while cash out remains restricted until the funding conditions are met. To prevent both cash in and cash out, you must provide a funding duration; once that period is reached, the status moves from `BLOCKED` to `NO OPERATIONS`.

## Pismo integration with other banking systems

If you maintain accounts in a different core banking system outside of Pismo, you can still utilize the Pismo platform to offer interest-bearing accounts to your clients and to process accrual calculations. In addition to the flexibility and high capacity of Pismo platform processing, this solution offers legal reports.

In this case, work with the Pismo representative to set up interest-bearing accounts.

<Image align="center" alt="Pismo integration with other banking systems" caption="Figure 2: Pismo integration with other banking systems" src="https://files.readme.io/3a328ab6ece142b6d1d49b9b83ef01b2bea06bd247b110769033a95224d1f91d-integration-with-other-banking-systems.png" />

1. If applicable, set up the [fee model](https://developers.pismo.io/pismo-docs/docs/fee-models) in the Pismo platform to withhold any taxes or operational fees.
2. Configure a flexible plan to accrue interest according to your needs.
3. Configure integration with your core banking system.
4. Once complete, events are generated to notify you of the interest to be posted. For more information, refer to [Output events](#output-events).

## Penalties for deposit products

You can set different types for deposit accounts. For details, refer to [Penalties for CD accounts](https://developers.pismo.io/pismo-docs/docs/penalties-for-cd-accounts).

## Output events

The Pismo platform generates events such as [Interest accrual succeeded](https://developers.pismo.io/events/docs/interest-engine-interest-accrual-account-success-1) and [Interest capitalization succeeded](https://developers.pismo.io/events/docs/interest-engine-interest-capitalization-account-success-1).

## Interest capitalization ledger entries

During interest capitalization, the Pismo platform records a credit entry in the deposit account and, when an interest payout account is configured, creates a corresponding debit entry to transfer the amount. This ensures a complete accounting trail and improves financial tracking.

## Regulatory reports

Contact your Pismo representative for the regulatory reports available in your region.

## Examples

### Scenario 1

For example, your principal amount is 10,000, the floating interest rate is DI (10.65% for the entire period), the index rate is 103%, the accrual rate is daily, and the payout frequency is daily. The Pismo platform uses your account balance to calculate the daily yield after the cut‑off window and credits the amount to your account on the next business day (D+1), according to your configured settings.

If you make no deposits or withdrawals, your account accrues the following amounts:

• On day 2, the credited amount is 4.13.\
• On day 3, the credited amount is 4.13.\
• On day 4, the credited amount is 4.14, and so on.

### Scenario 2

In this example, your principal amount is 10,000, the fixed interest rate is 6.17%, the accrual rate is monthly, and the payout frequency is monthly. The platform calculates your yield based on your account balance and credits it to your account each month.

If you make no deposits or withdrawals, your account accrues the following amounts:

• For month 2, the credited amount is 50.02.\
• For month 3, the credited amount is 50.27.\
• For month 4, the credited amount is 50.51, and so on.

## Common configuration parameters

The following parameters are common for setting up interest-bearing accounts. Refer to [Create interest plan ](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan) for detailed field descriptions.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Possible values
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Accrual basis** dictates the total days in a year to be considered when calculating the daily rate.
      </td>

      <td>
        * **BD/252** -  calculates daily interest using a 252-day year and the actual number of business days in each time period.
        * **Actual/360** - calculates daily interest using a 360-day year and the actual number of days in each time period.
        * **Actual/365**  - calculates daily interest using a 365-day year and the actual number of days in each time period.
        * **Actual/actual** - calculates daily interest using the actual number of days in the year (which in the leap year is 366) and the actual number of days in each time period.
      </td>
    </tr>

    <tr>
      <td>
        **Accrual frequency** defines when the accrual process happens.
      </td>

      <td>
        * **Daily**
        * **Monthly**
        * **Quarterly**
        * **Semi-annually**
        * **Yearly**
        * **Maturity**
      </td>
    </tr>

    <tr>
      <td>
        **Capitalization frequency** defines when the interest payment happens.
      </td>

      <td>
        * **Daily**
        * **Monthly**
        * **Quarterly**
        * **Semi-annually**
        * **Yearly**
        * **Maturity**
      </td>
    </tr>

    <tr>
      <td>
        **Capitalization mode** allows capitalized interest to be directed either back into the deposit as reinvestment or to a designated external account as a cash‑out.
      </td>

      <td>
        Two options are available:

        * `REINVEST`
        * `PAYOUT`

        Refer to [Attach deposit to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account) and [Update deposit account attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-account-attachment) for details.
      </td>
    </tr>

    <tr>
      <td>
        **Interest calculation** supports using the end‑of‑day account balance as the basis for computing interest. You can specify which balance is used for interest calculation.
      </td>

      <td>
        The Pismo platform calculates interest using a deposit‑based method that evaluates daily deposits and withdrawals and computes interest from the change in the account’s balance each day.

        Refer to `accrual_model` in [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product) for more information.
      </td>
    </tr>

    <tr>
      <td>
        **Interest type** indicates if the accrual is based on simple or compound interest calculation.
      </td>

      <td>
        * **Simple** - calculated only on the initial principal deposit amount.
        * **Compound** - calculated on both the initial principal and all of the previously accumulated interest, thereby multiplying savings at an accelerated rate.
      </td>
    </tr>

    <tr>
      <td>
        **Operation type** indicates the type of operations for your interest plan.
      </td>

      <td>
        There are two operation types:

        * **DEBIT**

        * **CREDIT**
      </td>
    </tr>

    <tr>
      <td>
        **Tax withholding** specifies the point in time when tax withholding takes effect. If omitted, no tax is withheld.
      </td>

      <td>
        When your `withholding_moment` is `ACCRUAL`, you must provide the fee processing code configured in the fee model. Refer to [Creating and applying fee models](https://developers.pismo.io/pismo-docs/docs/create-fee-model) for more information.

        There are two withholding moments:

        * **ACCRUAL**

        * **CAPITALIZATION**
      </td>
    </tr>

    <tr>
      <td>
        **Interest rates** determine how much interest the account holder earns on their deposits.
      </td>

      <td>
        * **Fixed**- remains constant for a specific period.
        * **Benchmark rate** can fluctuate over time in response to market conditions. For instance, reference rates like those in the US, or benchmark rates such as DI in Brazil, BOE in the UK, RBI in India, or RBA in Australia.
        * **Margin rate** is a percentage applied on the benchmark rate. For example, if the DI rate is 10.65%, the financial institution can provide an interest-bearing account that pays 100% of this rate for a year (the same 10.65%) or 103% of this rate (10.96%).
        * **Margin / Spread** is a percentage added to the benchmark rate. For example, if the BOE rate today is 2.5% and spread is 2.25%, so the interest rate used to calculate is 4.75.
      </td>
    </tr>

    <tr>
      <td>
        **Interest by tiers** applies different interest rates to specific balance ranges within the same interest plan.
      </td>

      <td>
        * **Type** allows you to specify either `TERM` (based on the period of time since the deposit was made.) or `AMOUNT` (interest rate amount according to the current balance)

        * **Tier calculation** is the tier calculation method.
      </td>
    </tr>

    <tr>
      <td>
        **Interest threshold** establishes optional cap (upper limit) and floor (lower limit) boundaries for the applied interest rate. Each boundary includes a threshold representing the maximum or minimum allowable rate and an effective rate applied when the corresponding limit is reached.
      </td>

      <td>
        * **Cap threshold**

        * **Cap effective rate**

        * **Floor threshold**

        * **Floor effective rate**
      </td>
    </tr>

    <tr>
      <td>
        **Interest base model** determines how interest is calculated. The default is `CLOSING-BALANCE`.
      </td>

      <td>
        * **CLOSING-BALANCE** calculates interest using a single end-of-day balance.

        * **BALANCE-CHANGE** calculates interest after each intraday balance movement, such as a credit or debit. With `BALANCE-CHANGE`, interest accrues on the balance held during each interval between consecutive movements rather than on a single end-of-day balance.
      </td>
    </tr>

    <tr>
      <td>
        **Fee** is any fee or tax that you want to apply.
      </td>

      <td>
        You can configure and attach any [fee model](https://developers.pismo.io/pismo-docs/docs/fee-models). For example, you can configure and apply national taxes or custom operational fees.
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /v1/products` | `interest-bearing-v1-list-products` | List products | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/deposits/accounts/open` | `interest-bearing-v1-deposit-account-open` | Open deposit account | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--deposit-account-open |
| `POST /v1/interest/plan` | `post-v1-interest-plan` | Create interest plan | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `POST /v1/savings-accounts` | `interest-bearing-v1-create-savings-account-product` | Create savings account product | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/deposits` | `interest-bearing-v1-create-deposit-product` | Create deposit product | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/deposits/accounts/{accountId}/attach` | `interest-bearing-v1-deposit-attach-account` | Attach deposit to account | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/savings-accounts/accounts/{accountId}/attach` | `interest-bearing-v1-savings-account-attach-account` | Attach savings account to account | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `PATCH /v1/deposits/accounts/{accountId}/attachment` | `interest-bearing-v1-deposit-update-account-attachment` | Update deposit account attachment overrides | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `PATCH /v1/deposits/accounts/{accountId}` | `interest-bearing-v1-deposit-update-payout-account` | Update payout account for deposit account | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `PATCH /v1/savings-accounts/accounts/{accountId}` | `interest-bearing-v1-savings-account-update-payout-account` | Update payout account for savings account | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `PATCH /v1/deposits/{productId}` | `interest-bearing-v1-patch-deposit-product` | Update deposit product | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |

### Operation essentials

- **`GET /v1/products`** (`interest-bearing-v1-list-products`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `EIBACC0008`, `EIBACC0007`; events none listed.
- **`POST /v1/deposits/accounts/open`** (`interest-bearing-v1-deposit-account-open`): security `BearerAuth`; required parameters none declared; required body fields `account`, `deposit_attachment`; response statuses 201, 400, 403, 404, 409, 422, 500, 502, 504; error codes in examples `EIBACC0008`, `EIBACC0325`, `EIBACC0380`, `EIBACC0331`, `EIBACC0108`, `EIBACC0330`, `EIBACC0018`, `EIBACC0065`, `EIBACC0103`, `EIBACC0107`, `EIBACC0109`, `EIBACC0110`, `EIBACC0236`, `EIBACC0284`, `EIBACC0379`, `EIBACC0298`, `EIBACC0299`, `EIBACC0303`, `EIBACC0305`, `EIBACC0306`, `EIBACC0307`, `EIBACC0308`, `EIBACC0319`, `EIBACC0320`, `EIBACC0321`, `EIBACC0005`, `EIBACC0104`, `EIBACC0064`, `EIBACC0106`, `EIBACC0396`, `EIBACC0297`, `EIBACC0007`, `EIBACC0066`, `EIBACC0328`, `EIBACC0324`, `EIBACC0322`, `EIBACC0329`; events `deposit-product-account-attach-1`, `deposit-product-deposit-account-opened-1`.
- **`POST /v1/interest/plan`** (`post-v1-interest-plan`): security `BearerAuth`; required parameters none declared; required body fields `accrual_basis`, `accrual_frequency`, `capitalization_frequency`, `currency_code`, `description`, `interest_type`, `start_date`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `interest-engine-interest-plan-creation-success-1`.
- **`POST /v1/savings-accounts`** (`interest-bearing-v1-create-savings-account-product`): security `BearerAuth`; required parameters none declared; required body fields `interest_plan_id`, `name`, `processing_codes`; response statuses 201, 400, 500; error codes in examples `EIBACC0008`, `EIBACC0007`; events `savings-account-product-creation-1`.
- **`POST /v1/deposits`** (`interest-bearing-v1-create-deposit-product`): security `BearerAuth`; required parameters none declared; required body fields `name`, `interest_plan_id`, `term_type`; response statuses 201, 400, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0393`, `EIBACC0007`; events `deposit-product-creation-1`.
- **`POST /v1/deposits/accounts/{accountId}/attach`** (`interest-bearing-v1-deposit-attach-account`): security `BearerAuth`; required parameters `accountId` (path); required body fields `product_id`; response statuses 201, 400, 404, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0308`, `EIBACC0309`, `EIBACC0310`, `EIBACC0311`, `EIBACC0312`, `EIBACC0379`, `EIBACC0064`, `EIBACC0114`, `EIBACC0007`, `EIBACC0304`; events `deposit-product-account-attach-1`.
- **`POST /v1/savings-accounts/accounts/{accountId}/attach`** (`interest-bearing-v1-savings-account-attach-account`): security `BearerAuth`; required parameters `accountId` (path); required body fields `product_id`; response statuses 204, 400, 404, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0114`, `EIBACC0007`; events `deposit-product-account-attach-1`.
- **`PATCH /v1/deposits/accounts/{accountId}/attachment`** (`interest-bearing-v1-deposit-update-account-attachment`): security `BearerAuth`; required parameters `accountId` (path); required body fields `deposit_configs`; response statuses 200, 400, 404, 409, 500; error codes in examples `EIBACC0315`, `EIBACC0308`, `EIBACC0310`, `EIBACC0307`, `EIBACC0306`, `EIBACC0305`, `EIBACC0299`, `EIBACC0298`, `EIBACC0109`, `EIBACC0110`, `EIBACC0113`, `EIBACC0301`, `EIBACC0314`, `EIBACC0007`, `EIBACC0316`; events `deposit-product-account-attachment-updated-1`.
- **`PATCH /v1/deposits/accounts/{accountId}`** (`interest-bearing-v1-deposit-update-payout-account`): security `BearerAuth`; required parameters `accountId` (path); required body fields `payout_account`; response statuses 200, 400, 403, 404, 409, 422, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0114`, `EIBACC0302`, `EIBACC0007`; events none listed.
- **`PATCH /v1/savings-accounts/accounts/{accountId}`** (`interest-bearing-v1-savings-account-update-payout-account`): security `BearerAuth`; required parameters `accountId` (path); required body fields `payout_account`; response statuses 200, 400, 403, 404, 409, 422, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0114`, `EIBACC0302`, `EIBACC0007`; events none listed.
- **`PATCH /v1/deposits/{productId}`** (`interest-bearing-v1-patch-deposit-product`): security `BearerAuth`; required parameters `productId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0007`; events `deposit-product-update-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `interest-bearing-v1-deposit-account-open` | `deposit-product-account-attach-1` |
| `interest-bearing-v1-deposit-attach-account` | `deposit-product-account-attach-1` |
| `interest-bearing-v1-savings-account-attach-account` | `deposit-product-account-attach-1` |
| `interest-bearing-v1-deposit-update-account-attachment` | `deposit-product-account-attachment-updated-1` |
| `interest-bearing-v1-create-deposit-product` | `deposit-product-creation-1` |
| `interest-bearing-v1-deposit-account-open` | `deposit-product-deposit-account-opened-1` |
| `interest-bearing-v1-patch-deposit-product` | `deposit-product-update-1` |
| `post-v1-interest-plan` | `interest-engine-interest-plan-creation-success-1` |
| `interest-bearing-v1-create-savings-account-product` | `savings-account-product-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/interest-bearing-accounts.md`: updatedAt 2026-10-07T15:28:28.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/interest-bearing-accounts.md` | whole document | https://developers.pismo.io/pismo-docs/docs/interest-bearing-accounts | `de8147ab1a30f15e…` | 2026-10-07T15:28:28.000Z |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-API-banking-interest-bearing-accounts--deposit-account-open` — API reference: Banking - Interest-bearing accounts — Deposit account open
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-BANK-penalties-for-cd-accounts` — Penalties and taxes for CD accounts
- `KU-CC-deposit-products` — Control Center deposit products and interest plans
- `KU-CC-fee-models` — Control Center fee models: manage and link fee models
- `KU-CORE-fee-models` — Fee management and fee models
- `KU-CORE-fee-models-create-and-simulate` — Creating, applying and simulating fee models
- `KU-EVT-catalogue-deposit` — Event catalogue: deposit
- `KU-EVT-catalogue-interest` — Event catalogue: interest
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
