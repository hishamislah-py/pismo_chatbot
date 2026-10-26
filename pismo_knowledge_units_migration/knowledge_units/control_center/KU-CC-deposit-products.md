---
ku_id: KU-CC-deposit-products
title: Control Center deposit products and interest plans
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/deposit-products-in-control-center.md
  sha256: 00a6213a0031a0704eb1270789e1f89b6740ec6a58ce141b249ce57b3f1231dd
  url: https://developers.pismo.io/pismo-docs/docs/deposit-products-in-control-center
  role: primary_guide
  updated_at: '2026-03-18T15:10:14.000Z'
- path: docs/control-center/add-a-savings-account-product.md
  sha256: 62e428673dc657f5ff68084435a22e2f6e07ba0efdd977e3bf329edcfd434201
  url: https://developers.pismo.io/pismo-docs/docs/add-a-savings-account-product
  role: primary_guide
  updated_at: '2026-03-18T16:57:16.000Z'
- path: docs/control-center/add-a-time-deposit-product.md
  sha256: 2d7f74ad3805d68e084a860f389eebd9a29e69f888924871db6c57b20a88422e
  url: https://developers.pismo.io/pismo-docs/docs/add-a-time-deposit-product
  role: primary_guide
  updated_at: '2026-03-18T16:56:11.000Z'
- path: docs/control-center/attach-an-account-to-a-deposit-product.md
  sha256: 7db8b0afe3db4b2bd8e8e2e7a7afcd1d47e8c4923010a31c9c186ced040106da
  url: https://developers.pismo.io/pismo-docs/docs/attach-an-account-to-a-deposit-product
  role: primary_guide
  updated_at: '2026-03-18T15:10:35.000Z'
- path: docs/control-center/interest-plans-in-control-center.md
  sha256: abfad94371020ebd8afb6a096418b951d9c27091c1b0634a7a51acee8c16041d
  url: https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center
  role: primary_guide
  updated_at: '2026-07-07T11:23:12.000Z'
operations:
- interest-bearing-v1-deposit-attach-account
related_kus:
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-BANK-interest-bearing-accounts
- KU-CC-fee-models
- KU-CORE-processing-codes-and-transaction-types
- KU-EVT-catalogue-deposit
grouping_rationale: Deposit-product screens.
---

# Control Center deposit products and interest plans

**KU ID:** `KU-CC-deposit-products` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 5 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Deposit-product screens.

Scope as stated in `docs/control-center/deposit-products-in-control-center.md`:

> From Pismo Control Center, you can create a product for time deposit accounts or savings accounts. A deposit product is an interest-bearing account to which you can apply interest, fees, taxes, and so on. In Control Center, you can only attach debit accounts to deposit products. To attach a different account type, you must use the [Interest-bearing accounts API](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account).

Scope as stated in `docs/control-center/add-a-savings-account-product.md`:

> You can add a savings account product from Pismo Control Center. A savings account is an interest-bearing account that earns interest on deposited funds. With savings account products such as variable-rate savings accounts or money market accounts, your customer has the flexibility to withdraw money at any time without penalty. Savings accounts generally have lower interest rates than time deposit accounts.

Scope as stated in `docs/control-center/add-a-time-deposit-product.md`:

> You can add time deposit products from Pismo Control Center. A time deposit account is an interest-bearing account that has a preset date of maturity. Your customer must leave their money in the account for an agreed-upon length of time, or term. If they want to access their money, they must wait until the end of the term or risk having a penalty for early withdrawal. Time deposit accounts, such as certificates of deposit (CDs) generally pay a higher interest rate than regular savings accounts, however your customer can’t access their money until the end of the term.

Scope as stated in `docs/control-center/attach-an-account-to-a-deposit-product.md`:

> In Control Center, you can only attach debit accounts to a deposit product. To attach a different account type, you must use the [Interest-bearing accounts API](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account).

Scope as stated in `docs/control-center/interest-plans-in-control-center.md`:

> Create interest plans to define how interest is calculated and applied to products. You can create the following interest plan types:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/deposit-products-in-control-center.md`: Deposit products
- `docs/control-center/add-a-savings-account-product.md`: Add a savings account product
- `docs/control-center/add-a-time-deposit-product.md`: Add a time deposit product
- `docs/control-center/attach-an-account-to-a-deposit-product.md`: Attach an account to a deposit product
- `docs/control-center/interest-plans-in-control-center.md`: Interest plans; View interest plans; Create an interest plan

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/deposit-products-in-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/deposit-products-in-control-center · updatedAt: 2026-03-18T15:10:14.000Z

<!-- source:begin path=docs/control-center/deposit-products-in-control-center.md part=0-end -->

# Deposit products

From Pismo Control Center, you can create a product for time deposit accounts or savings accounts. A deposit product is an interest-bearing account to which you can apply interest, fees, taxes, and so on. In Control Center, you can only attach debit accounts to deposit products. To attach a different account type, you must use the [Interest-bearing accounts API](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account).

> 📘
>
> You must contact your Pismo representative for assistance with setting up interest-bearing accounts.

There are two types of deposit product on the Pismo platform:

* **Time deposit**—Also known as term deposit or certificate of deposit (CD), this is a deposit account that sets aside an amount of money for a fixed period of time. These accounts typically offer higher interest rates compared to a savings account, but the money cannot be withdrawn until the end of the term without a penalty.
* **Savings account**—A type of deposit account that provides a safe place to store money while earning interest. The interest rates, schedules, fees, and tax implications are determined according to the [interest plans](https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center) that you associate with the account. These accounts typically pay low interest rates and have lenient withdrawal restrictions.

To view a list of deposit products, go to the main menu and select **Configurations** > **Deposit products**. Select any of the products in the list to view its details.

For information about deposit products on the Pismo platform, refer to [Interest-bearing accounts](https://developers.pismo.io/pismo-docs/docs/interest-bearing-accounts).
<!-- source:end -->

### Source 2: `docs/control-center/add-a-savings-account-product.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/add-a-savings-account-product · updatedAt: 2026-03-18T16:57:16.000Z

<!-- source:begin path=docs/control-center/add-a-savings-account-product.md part=0-end -->

# Add a savings account product

You can add a savings account product from Pismo Control Center. A savings account is an interest-bearing account that earns interest on deposited funds. With savings account products such as variable-rate savings accounts or money market accounts, your customer has the flexibility to withdraw money at any time without penalty. Savings accounts generally have lower interest rates than time deposit accounts.

When you add a savings account product, the interest plan that you want to use must already exist on the Pismo platform. For more information, refer to [Interest plans](https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center).

> 📘
>
> You must contact your Pismo representative for assistance with setting up interest-bearing accounts.

To add a savings account product:

1. From the main menu, select **Configurations** > **Deposit products**.
2. On the **Deposit products** screen, select **Create**.
3. On the **Select Deposit product type** screen, select **Savings account** and select **Next**.
4. On the **Create your savings account product** screen, enter a descriptive name for the product in the **Name** field.
5. In the **Interest plan** menu, select the interest plan that you want to use and select **Next**.
6. On the **Attach processing codes** screen, enter the processing codes (by name or by ID) to be used in the following cases:
   1. **Interest processing code**—used for crediting accrued interest to this product.
   2. (Optional) **Withholding tax processing code**—used for calculating tax withholding for this product.
7. Select **Next**.
8. On the **Review** screen, verify that the information you provided is correct, then select **Finish**.

> 📘 Activate the deposit product
>
> A deposit product is created with the initial status **Created**, but can't be used until it is activated. To activate a deposit product:
>
> 1. On the **Deposit products** screen, select the deposit product.
> 2. On the details screen, select the **Created** button and choose **Active**. (This button could also be labeled **Inactive**.)
> 3. In the **Update status** dialog, enter a reason for the change and then select **Yes**.
<!-- source:end -->

### Source 3: `docs/control-center/add-a-time-deposit-product.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/add-a-time-deposit-product · updatedAt: 2026-03-18T16:56:11.000Z

<!-- source:begin path=docs/control-center/add-a-time-deposit-product.md part=0-end -->

# Add a time deposit product

You can add time deposit products from Pismo Control Center. A time deposit account is an interest-bearing account that has a preset date of maturity. Your customer must leave their money in the account for an agreed-upon length of time, or term. If they want to access their money, they must wait until the end of the term or risk having a penalty for early withdrawal. Time deposit accounts, such as certificates of deposit (CDs) generally pay a higher interest rate than regular savings accounts, however your customer can’t access their money until the end of the term.

For a time deposit product, you must provide a maturity date. This date must respect the maximum and minimum term, if the deposit product has set them.

> 📘
>
> You must contact your Pismo representative for assistance with setting up interest-bearing accounts.

The interest plan that you want to use must already exist on the platform. For more information, refer to [Interest plans](https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center).

To add a time deposit product:

1. From the main menu, select **Configurations** > **Deposit products**.
2. On the **Deposit products** screen, select **Create**.
3. On the **Select your deposit product type** screen, choose **Time deposit** and select **Next**.
4. On the **Create your time deposit product** screen, enter a descriptive name for the product in the **Name** field.
5. In the **Interest plan** menu, select the interest plan that you want to use.
6. Select a term type:
   * **Flexible**
   * **Fixed**
7. Select the maturity instructions:
   * For the principal amount: **Pay** or **Rollover**.
   * For the earned interest amount: **Pay** or **Rollover**.
8. (Optional) In the **Fee model** field, enter the name of the Fee model that you want to use to define the method used to calculate fees, such as a fixed value or a percentage. For more information, refer to [Fee models](https://developers.pismo.io/pismo-docs/docs/fee-models-in-control-center).
9. (Optional) For a flexible term, enter the minimum and maximum number of days that deposited funds will remain in the account.
10. (Optional) In the **Cool off period** field, enter the number of days after the initial investment amount can be withdrawn without penalty. The value must be greater than or equal to the funding duration (which you set in the next step).
11. (Optional) In the **Funding duration** field, enter the number of days during which funds can be credited to the account before the account is blocked. If no value is set, credit operations are always allowed.
12. Select **Next**.
13. On the **Attach processing codes** screen, enter the processing codes (by name or by ID) to be used in the following cases:
    * **Interest processing code**—used for calculating interest accrual
    * **Maturity processing code**—applied when the product has reached its maturity date (for redemption).
    * **Detach processing code**—applied when a detach happens without reaching the maturity date (for early redemption).
    * (Optional) **Withholding tax processing code**—defines how the Pismo platform treats withholding tax for this product.
14. Select **Next**.
15. On the **Review** screen, verify that the information you provided is correct, then select **Finish**.

> 📘 Activate the deposit product
>
> A deposit product is created with the initial status **Created**, but can't be used until it is activated. To activate a deposit product:
>
> 1. On the **Deposit products** screen, select the deposit product.
> 2. On the details screen, select the **Created** button and choose **Active**. (This button could also be labeled **Inactive**.)
> 3. In the **Update status** dialog, enter a reason for the change and then select **Yes**.
<!-- source:end -->

### Source 4: `docs/control-center/attach-an-account-to-a-deposit-product.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/attach-an-account-to-a-deposit-product · updatedAt: 2026-03-18T15:10:35.000Z

<!-- source:begin path=docs/control-center/attach-an-account-to-a-deposit-product.md part=0-end -->

# Attach an account to a deposit product

In Control Center, you can only attach debit accounts to a deposit product. To attach a different account type, you must use the [Interest-bearing accounts API](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account).

> 📘 Prerequisites
>
> * The deposit product must be in **Active** status.
> * The organization must already have an [interest plan](https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center).

To attach an account to a deposit product:

1. From the main menu, select **Customer operations** > **Accounts**.
2. On the **Accounts management** screen, select the type of data you want to search: **Document**, **Account**, **Email**, or **Name**.
3. In the result list, select the account you want to manage. The account must be of the type **Debit**.
4. On the account overview screen, open the **Deposit products** tab.
5. Select the deposit product that you want to attach or detach. The deposit product must be in **Active** status.
6. To attach the account, select **Attach**.

> 📘
>
> Select **Detach** to detach an account that is currently attached to a deposit product.
<!-- source:end -->

### Source 5: `docs/control-center/interest-plans-in-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center · updatedAt: 2026-07-07T11:23:12.000Z

<!-- source:begin path=docs/control-center/interest-plans-in-control-center.md part=0-end -->

# Interest plans

Create interest plans to define how interest is calculated and applied to products. You can create the following interest plan types:

* **Fixed**—The interest rate remains the same for the entire investment term or for a defined portion of it.
* **Floating**—The interest rate changes with market conditions and is tied to a benchmark rate. Floating interest plans are sometimes called variable interest plans.

<Callout icon="📘" theme="info">
  Interest plans are defined at the organization level only.
</Callout>

For more information, refer to [Interest-bearing accounts](https://developers.pismo.io/pismo-docs/docs/interest-bearing-accounts).

From Control Center, you can do the following:

* [View interest plans](#view-interest-plans)
* [Create an interest plan](#create-an-interest-plan)

# View interest plans

To view the list of interest plans, do the following:

* From the main menu, select **Configurations** > **Interest plans**.\
  The **Interest plans** screen displays.

Refer to the following table for a description of the columns.

| Column             | Description                                                                     |
| :----------------- | :------------------------------------------------------------------------------ |
| **NAME**           | The name of the interest plan                                                   |
| **RATE TYPE**      | The type of rate applied to the interest plan, either **Fixed** or **Floating** |
| **ACCRUAL BASIS**  | How interest is calculated over time                                            |
| **ACCRUAL**        | How often the interest is calculated and added to to the balance                |
| **CAPITALIZATION** | How often the interest is paid out                                              |
| **INTEREST TYPE**  | How interest is calculated, either **Simple** or **Compound**                   |
| **START DATE**     | The date when the interest plan becomes active                                  |
| **STATUS**         | The status of the interest plan                                                 |

To view a specific interest plan, do the following:

1. From the main menu, select **Configurations** > **Interest plans**.
2. On the **Interest plans** screen, select an interest plan.\
   The **Interest plan details** screen displays, divided into the following tabs:

* **Plan overview**—View key information about the interest plan.
* **Interest rate & tiers**—View the plan’s interest rate and type and configuration details for interest by tiers. If you didn’t configure interest by tiers, no interest by tiers information is shown.
* **Interest thresholds**—View configuration details for interest thresholds. If you didn’t configure interest thresholds, no interest threshold information is shown.

# Create an interest plan

To create an interest plan, do the following:

1. From the main menu, select **Configurations** > **Interest plans**.
2. On the **Interest plans** screen, select **Create interest plan**.\
   **Note**: Tooltips are included next to some steps. If you need help, hover over them for additional information.
3. On the **Plan details** screen, do the following:
   1. In **Name**, enter a unique name for the interest plan.\
      The name can have a maximum of 200 characters.
   2. In **Start date**, select the date when the interest plan becomes active.
   3. In **Accrual basis**, select how interest is calculated over time.
   4. In **Accrual frequency**, select how often interest accrues.
   5. In **Capitalization frequency**, select how often interest is applied to the balance.
   6. From **Currency**, select the interest plan's currency.
   7. In **Interest type**, select the accrual calculation method.
   8. Select **Next**.
4. (Optional) On the **Processing code** screen, select a fee model processing code, and select **Next**.

   **Note**: You can only apply one fee model processing code to an interest plan.\
   For more information on fee models and processing codes, refer to the following guides:

   * [Fee models](https://developers.pismo.io/pismo-docs/docs/fee-model)
   * [Processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types)
5. On the **Rate type** screen, do one of the following:
   * To create a fixed rate interest plan, select **Fixed**. In **Fixed interest rate**, enter the annual interest rate for the plan.
   * To create a floating rate interest plan, select **Floating**, and do the following:
     1. In **Benchmark**, select a benchmark market index rate.\
        **Note**: The **DI** benchmark is available only if you selected **BD/252** as the accrual basis on the **Plan details** screen.
     2. In **Margin rate**, enter the plan's margin rate.
     3. (Optional) In **Margin**, enter the plan's margin.  If you don't want to add a margin, leave the field blank.
6. Select **Next**.
7. (Optional) On the **Interest by tiers** screen, do the following:
   1. In **Tier type**, select the format you want to base your tiers on.
   2. In **Tier calculation**, select how interest is applied when a balance moves into a new tier.\
      The **Tiers** section displays.
   3. In the **Tiers** section, create your interest by tiers configuration.\
      **Note**: You can add a maximum of two tiers, and you can delete a tier by selecting the trash icon.\
      Fixed rate plans use the fixed interest rate, and floating plans use the margin rate.
   4. Select **Next**.
8. (Optional) On the **Interest thresholds** screen, do the following:
   1. In **Cap threshold**, enter the maximum rate allowed before the cap effective rate is triggered.
   2. In **Cap effective rate**, enter the rate to apply when the cap threshold is reached.
   3. In **Floor threshold**, enter the minimum rate allowed before the floor effective rate is triggered.
   4. In **Floor effective rate**, enter the rate to apply when the floor threshold is reached.
   5. Select **Next**.
9. Review your interest plan details.\
   If you want to make changes, select **Back** until you reach the required page.
10. Select **Create**.\
    Your interest plan is created and added to the list of interest plans.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/deposits/accounts/{accountId}/attach` | `interest-bearing-v1-deposit-attach-account` | Attach deposit to account | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |

### Operation essentials

- **`POST /v1/deposits/accounts/{accountId}/attach`** (`interest-bearing-v1-deposit-attach-account`): security `BearerAuth`; required parameters `accountId` (path); required body fields `product_id`; response statuses 201, 400, 404, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0308`, `EIBACC0309`, `EIBACC0310`, `EIBACC0311`, `EIBACC0312`, `EIBACC0379`, `EIBACC0064`, `EIBACC0114`, `EIBACC0007`, `EIBACC0304`; events `deposit-product-account-attach-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `interest-bearing-v1-deposit-attach-account` | `deposit-product-account-attach-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/control-center/deposit-products-in-control-center.md`: updatedAt 2026-03-18T15:10:14.000Z.
- `docs/control-center/add-a-savings-account-product.md`: updatedAt 2026-03-18T16:57:16.000Z.
- `docs/control-center/add-a-time-deposit-product.md`: updatedAt 2026-03-18T16:56:11.000Z.
- `docs/control-center/attach-an-account-to-a-deposit-product.md`: updatedAt 2026-03-18T15:10:35.000Z.
- `docs/control-center/interest-plans-in-control-center.md`: updatedAt 2026-07-07T11:23:12.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/deposit-products-in-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/deposit-products-in-control-center | `00a6213a0031a070…` | 2026-03-18T15:10:14.000Z |
| `docs/control-center/add-a-savings-account-product.md` | whole document | https://developers.pismo.io/pismo-docs/docs/add-a-savings-account-product | `62e428673dc657f5…` | 2026-03-18T16:57:16.000Z |
| `docs/control-center/add-a-time-deposit-product.md` | whole document | https://developers.pismo.io/pismo-docs/docs/add-a-time-deposit-product | `2d7f74ad3805d68e…` | 2026-03-18T16:56:11.000Z |
| `docs/control-center/attach-an-account-to-a-deposit-product.md` | whole document | https://developers.pismo.io/pismo-docs/docs/attach-an-account-to-a-deposit-product | `7db8b0afe3db4b2b…` | 2026-03-18T15:10:35.000Z |
| `docs/control-center/interest-plans-in-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center | `abfad94371020ebd…` | 2026-07-07T11:23:12.000Z |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-BANK-interest-bearing-accounts` — Interest-bearing accounts
- `KU-CC-fee-models` — Control Center fee models: manage and link fee models
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-EVT-catalogue-deposit` — Event catalogue: deposit
