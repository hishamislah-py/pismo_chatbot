---
ku_id: KU-CC-lending
title: 'Control Center lending: loan products and loan management'
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/digital-lending.md
  sha256: a98447a1ef4c5bdcf425b24f289ea95997d039e6a0356aa5b64089f007a50ebd
  url: https://developers.pismo.io/pismo-docs/docs/digital-lending
  role: primary_guide
  updated_at: '2026-08-31T15:01:15.000Z'
- path: docs/control-center/loan-products-cc.md
  sha256: 309e953331f1fe442641117fa5d06395a0c726eb5b79db0d1502d5b059e03090
  url: https://developers.pismo.io/pismo-docs/docs/loan-products-cc
  role: primary_guide
  updated_at: '2026-08-31T15:25:07.000Z'
- path: docs/control-center/manage-loans-in-control-center.md
  sha256: 4bcae297d95adfcef0245da3fae6202d34b27e6b121bc26ea8775fbed09ce497
  url: https://developers.pismo.io/pismo-docs/docs/manage-loans-in-control-center
  role: primary_guide
  updated_at: '2026-08-05T11:19:15.000Z'
operations:
- bookLoanV2
- post-v1-simulation
related_kus:
- KU-API-core-platform-payment-methods-admin--simulation
- KU-API-lending--loans
- KU-BANK-interest-bearing-accounts
- KU-CC-deposit-products
- KU-CC-dual-approval
- KU-CC-processing-codes
- KU-CORE-processing-codes-and-transaction-types
- KU-EVT-catalogue-lending
- KU-EVT-catalogue-other-domains
- KU-LEND-lending-overview
- KU-LEND-loan-management
- KU-LEND-loan-products
grouping_rationale: Lending screens.
---

# Control Center lending: loan products and loan management

**KU ID:** `KU-CC-lending` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Lending screens.

Scope as stated in `docs/control-center/digital-lending.md`:

> Use Pismo's lending configurations to create loan products for your customers. Lending configurations include:

Scope as stated in `docs/control-center/loan-products-cc.md`:

> Create, view, and manage loan products for your organization. A loan product defines the options and rules individual loans inherit, including how often repayments are due, how interest is calculated, what limits apply, and so on. With the loan products feature, you can:

Scope as stated in `docs/control-center/manage-loans-in-control-center.md`:

> View and manage your customers' loans in Control Center. With the loans feature, you can:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/digital-lending.md`: Lending configurations
- `docs/control-center/loan-products-cc.md`: Loan products; View loan products; Create a loan product; Manage loan products; Edit a loan product; Deactivate a loan product
- `docs/control-center/manage-loans-in-control-center.md`: Manage loans in Control Center; View loans; Repayment schedule tab; Disbursement tab; Manage loans; Disburse a loan; Adjust a loan

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/digital-lending.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/digital-lending · updatedAt: 2026-08-31T15:01:15.000Z

<!-- source:begin path=docs/control-center/digital-lending.md part=0-end -->

# Lending configurations

Use Pismo's lending configurations to create loan products for your customers. Lending configurations include:

* [Loan products](https://developers.pismo.io/pismo-docs/reference/loan-products-cc)—Create and manage loan products that define the behavior of a group of loans, including repayment schedules, interest calculation methods, and other loan settings.
<!-- source:end -->

### Source 2: `docs/control-center/loan-products-cc.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/loan-products-cc · updatedAt: 2026-08-31T15:25:07.000Z

<!-- source:begin path=docs/control-center/loan-products-cc.md part=0-end -->

# Loan products

Create, view, and manage loan products for your organization. A loan product defines the options and rules individual loans inherit, including how often repayments are due, how interest is calculated, what limits apply, and so on. With the loan products feature, you can:

* Create loan products to launch new lending offers tailored to your business and customer needs
* Define a loan configuration once, then apply it consistently across loans, removing the need to manually configure loan terms and behavior for individual loans

For more information, refer to [Loan product overview](https://developers.pismo.io/pismo-docs/docs/loan-product-overview).

From Control Center, you can do the following:

* [View loan products](#view-loan-products)
* [Create a loan product](#create-a-loan-product)
* [Manage loan products](#manage-loan-products)

# View loan products

To view the list of loan products and explore a loan product in more detail, do the following:

1. From the main menu, select **Configurations** > **Loan products**.\
   The **Loan products** screen is displayed.

<Image align="center" alt="Loan products screen" border={true} src="https://files.readme.io/eca634730e2073311229014206b53f0e7170cd9856be4346cd665694bf6d344f-Screenshot_2026-08-26_at_1.48.49_PM.png" className="border" />

The **Loan products** screen lists the loan products for your organization and includes key details.

A loan product can have one of the following statuses:

* **Active**—The loan product is in use.
* **Inactive**—The loan product was deactivated and is no longer available.

2. On the **Loan products** screen, select a loan product.\
   The **Loan products details** screen is displayed.

<Image align="center" alt="Loan product details screen" border={true} src="https://files.readme.io/a9aa8bf4b061b7a0135a8bc97ea11bf34c82b102f1e5dc5386cf6e7808c7fc44-Screenshot_2026-08-26_at_1.49.02_PM.png" className="border" />

The **Loan product details** screen provides a detailed view of a loan product's configuration and associated settings. For more information about each tab, refer to the following table.

| Tab                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Product details**        | Provides an overview of the loan product. Wherever the edit icon appears (pencil), you can make changes.                                                                                                                                                                                                                                                                                                                            |
| **Processing codes**       | Lists the processing codes applied to the loan product. You can add additional processing codes from this screen. For general information about processing codes, refer to [Processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types). For information about creating processing codes in Control Center, refer to [Create processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/create-processing-codes-and-transaction-types).          |
| **Interest plans**         | Lists the interest plans applied to the loan product. When you first create a loan product, this screen is blank. You can add interest plans from this screen. For general information about interest on the Pismo platform, refer to [Interest-bearing accounts](https://developers.pismo.io/pismo-docs/docs/interest-bearing-accounts). For information about creating interest plans in Control Center, refer to [Interest plans](https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center). |
| **Early final settlement** | Displays the early final settlement (EFS) details configured during loan product creation. EFS occurs when a borrower repays the full amount of the loan, plus any applicable charges, before the final scheduled payment date. EFS details are shown only if EFS is configured.                                                                                                                                                    |
| **Prepayment**             | Displays the prepayment details configured during loan product creation. Prepayment details are shown only if prepayment is configured.                                                                                                                                                                                                                                                                                             |

# Create a loan product

Create a loan product to define the terms, pricing, and rules that apply to the loans you offer. Because loan products act as templates, configuring at least one loan product is a required first step before you can book any individual loan. You can create multiple loan products to diversify and grow your lending portfolio, adding new products over time as your offerings expand.

> 📘 Before you begin
>
> * Before creating a loan product, you must create the processing codes you plan to use and tag them with **Lending** or **BNPL**. Each loan product requires at least one Booking processing code and one Repayment processing code. For more information about creating processing codes, refer to [Create processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/create-processing-codes-and-transaction-types).
> * You must create your loan product in one session; you can't save and return later.

To create a loan product, do the following:

1. On the **Loan products** screen, select **Create loan product**.\
   **Note:** The creation wizard includes tooltips that provide additional guidance. Hover over the tooltip icon to learn more about a screen or understand how specific settings affect loan behavior.

2. On the **Product details** screen, configure your loan product details, and select **Next**.\
   **Note:** Loan products are created at the organization level and are not tied to a specific program. Ensure the currency you select matches the currency of the programs whose accounts will have loans booked against the loan product. If your organization operates programs in more than one currency, create a separate loan product for each currency.

3. On the **Processing code types** screen, select the processing code types to use with the loan product, and select **Next**.\
   Processing codes identify the financial operations that occur across the loan lifecycle and determine the balance impact of each operation. For more information, refer to [Processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types).

   In this creation wizard, processing codes are grouped by types. In this step, select the processing code types you want to use. In the next step, you'll select the specific processing codes within each type.

   **Notes:**

   * For all loan products, Booking and Repayment processing codes types are required.
   * If you configured a grace period on the **Product details** screen, the Penalty Waiver processing code type is also required.

4. On the **PC selection** screen, select the processing codes to apply to the loan product, and select **Next**.\
   **Note:** Once you associate a Booking processing code with a loan product, you cannot use the same processing code with any other loan product.

5. (Optional) On the **Early final settlement** screen, configure the early final settlement behavior for the loan product, and select **Next**.

6. (Optional) On the **Prepayment** screen, configure the prepayment behavior for the loan product, and select **Next**.

7. On the **Review and create loan product** screen, review your loan product details, and select **Create**.

# Manage loan products

From Control Center, you can do the following:

* [Edit a loan product](#edit-a-loan-product)
* [Deactivate a loan product](#deactivate-a-loan-product)

## Edit a loan product

Edit a loan product to keep it aligned with your organization's evolving lending requirements. You can update product details as well as manage the processing codes and interest plans associated with the product.

**Note:** Editing a loan product does not affect existing loans. Existing loans retain their current configuration, while loans created afterward use the updated loan product details.

To edit the loan product details, do the following:

1. On the **Loan products** screen, select an active loan product.
2. On the **Product details** tab, select the edit icon for the attribute you want to edit.\
   **Note:** Not all loan product details are editable. You can edit any loan product detail that displays the edit icon (pencil).
3. Update the value and select **Save**.

To add a processing code, do the following:

1. On the **Loan products** screen, select an active loan product, and select the **Processing codes** tab.
2. Select **Add processing code**, configure your processing codes, and select **Add**.\
   **Note:** You cannot remove processing codes.

To add an interest plan, do the following:

1. On the **Loan products** screen, select an active loan product, and select the **Interest plans** tab.
2. Select **Add interest plan**, configure your interest plans, and select **Add**.\
   **Note:** You can remove interest plans by selecting the trash icon.

## Deactivate a loan product

Deactivate a loan product to permanently remove it from use, such as when consolidating overlapping products, replacing a product with a newer version, or retiring a lending offer. Deactivated loan products remain in the list to preserve their history.

> 🚧 Deactivating loan products
>
> You cannot delete loan products; you can only deactivate them.
>
> When you deactivate a loan product, you can't reactive it. If you need to use it again, you must create a new loan product.
>
> After you deactivate a loan product, existing loans previously created using the loan product are not affected.

To deactivate a loan product, on the **Loan products** screen, slide the **Active** status toggle for the loan you want to deactivate, and confirm. You can also deactivate a loan product in the same way from the **Loan product details** screen.

<br />
<!-- source:end -->

### Source 3: `docs/control-center/manage-loans-in-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/manage-loans-in-control-center · updatedAt: 2026-08-05T11:19:15.000Z

<!-- source:begin path=docs/control-center/manage-loans-in-control-center.md part=0-end -->

# Manage loans in Control Center

View and manage your customers' loans in Control Center. With the loans feature, you can:

* View the list of created loans for an account
* Monitor loan repayment progress
* Pay out and track disbursements
* Make adjustments to individual loan repayment installments

> 📘 Supported actions and role requirements
>
> In Control Center, you can only view, disburse, and adjust loans. You can't simulate or book a loan. To simulate or book a loan, you must use the [Create simulation](https://developers.pismo.io/pismo-docs/reference/post-v1-simulation) and [Book loan](https://developers.pismo.io/pismo-docs/reference/bookloanv2) endpoints.
>
> The actions available to you in Control Center depend on your role:
>
> * Users with the Backoffice operator or Accounts operator role can view, disburse, and adjust loans.
> * Users with the Backoffice viewer, Accounts viewer, or Collection analyst role can view loans only.

For more information about lending on the Pismo platform, refer to [Lending overview](https://developers.pismo.io/pismo-docs/docs/lending-overview).

From Control Center, you can do the following:

* [View loans](#view-loans)
* [Manage loans](#manage-loans)

# View loans

To view the loans for an account and inspect a loan in more detail, do the following:

1. From the main menu, select **Customer operations** > **Accounts**, and search for the account.
2. On the account screen, select the **Loans** tab.\
   The **Loan details** screen is displayed. You can find specific loans by filtering the list.\
   **Note:** You can also access the **Loan details** screen through the **Loans** preview card on the **Overview** tab.
3. Select a loan.\
   The **Loan information** screen is displayed, divided into the following tabs:
   * **Details**—Provides an overview of the loan, including key financial amounts, interest rate information, and [loan product](https://developers.pismo.io/pismo-docs/docs/loan-product-overview) details.
   * **Repayment schedule**—Displays the repayment installment schedule for the loan. For more information, refer to [Repayment schedule tab](#repayment-schedule-tab).
   * **Disbursement**—Lists all disbursements associated with the loan. For more information, refer to [Disbursement tab](#disbursement-tab).

The **Loan details** screen displays the list of created loans for an account and includes an overview of key loan and financial details.

<Image align="center" alt="Screenshot showing an excerpt of the Loan details screen" border={true} src="https://files.readme.io/dff944cd1167b3e18fdfc4da23bf05ea11e3769014e3e1c233c03798a9f31e4b-loan-details-screen.png" className="border" />

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Column
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **ID**
      </td>

      <td>
        The ID of the loan

        The ID is generated automatically and assigned when the loan is booked
      </td>
    </tr>

    <tr>
      <td>
        **PRINCIPAL**
      </td>

      <td>
        The original amount of the loan before interest or repayments are applied
      </td>
    </tr>

    <tr>
      <td>
        **BALANCE**
      </td>

      <td>
        The remaining amount of the loan to be repaid
      </td>
    </tr>

    <tr>
      <td>
        **INTEREST RATE**
      </td>

      <td>
        The percentage applied to the loan to calculate how much interest is charged over time
      </td>
    </tr>

    <tr>
      <td>
        **PAID**
      </td>

      <td>
        The total loan amount already repaid
      </td>
    </tr>

    <tr>
      <td>
        **START DATE**
      </td>

      <td>
        The date when the loan becomes active
      </td>
    </tr>

    <tr>
      <td>
        **NEXT PAYMENT**
      </td>

      <td>
        The date when the next scheduled repayment is due
      </td>
    </tr>

    <tr>
      <td>
        **STATUS**
      </td>

      <td>
        The status of the loan

        For more information, refer to [Manage loans](https://developers.pismo.io/pismo-docs/docs/manage-loans).
      </td>
    </tr>
  </tbody>
</Table>

The following sections describe the **Repayment schedule** and **Disbursement** tabs in more detail.

## Repayment schedule tab

The **Repayment schedule** tab displays the repayment installment plan for the loan. You can view payment progress and track the status of each individual repayment.

<Image align="center" alt="Screenshot showing an excerpt of the repayment schedule tab" border={true} src="https://files.readme.io/4118b6f6d4b41c45799c29b2ed6189d8907402c077a285c639cabbf387e004ae-repayment-schedule-tab.png" className="border" />

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Column
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **PERIOD**
      </td>

      <td>
        The installment number in the repayment schedule
      </td>
    </tr>

    <tr>
      <td>
        **REAL DUE DATE**
      </td>

      <td>
        The date when the repayment for the installment is due
      </td>
    </tr>

    <tr>
      <td>
        **DUE**
      </td>

      <td>
        The remaining amount of the installment to be repaid
      </td>
    </tr>

    <tr>
      <td>
        **PAID**
      </td>

      <td>
        The amount already repaid for the installment
      </td>
    </tr>

    <tr>
      <td>
        **INITIAL AMOUNT**
      </td>

      <td>
        The original amount calculated for the installment
      </td>
    </tr>

    <tr>
      <td>
        **STATUS**
      </td>

      <td>
        The status of the installment

        For more information, refer to [Manage loans](https://developers.pismo.io/pismo-docs/docs/manage-loans).
      </td>
    </tr>

    <tr>
      <td>
        **ADJUST**
      </td>

      <td>
        The option to adjust the repayment details for the installment

        For more information, refer to [Adjust a loan](#adjust-a-loan).
      </td>
    </tr>
  </tbody>
</Table>

To view more information about a specific installment, you can expand it. The expanded view shows a detailed breakdown of how the repayment is calculated.

## Disbursement tab

The **Disbursement** tab lists all disbursements made for the loan.  Each entry represents an individual disbursement and contains key information about the disbursement and its status.

<Image align="center" alt="Screenshot showing an excerpt of the disbursement tab" border={true} src="https://files.readme.io/09c9f601fdacb5bb6a476ba467784f2eee644ef720c741b739b8e5979ea90073-disbursement-tab.png" className="border" />

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Column
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **DISBURSEMENT ID**
      </td>

      <td>
        The ID of the disbursement

        The disbursement ID is generated automatically and assigned when the disbursement is made
      </td>
    </tr>

    <tr>
      <td>
        **DATE**
      </td>

      <td>
        The date when the disbursement was made
      </td>
    </tr>

    <tr>
      <td>
        **AMOUNT**
      </td>

      <td>
        The amount disbursed
      </td>
    </tr>

    <tr>
      <td>
        **ACC. TYPE**
      </td>

      <td>
        The type of account receiving the funds, **Internal** or **External**.

        * Internal accounts are accounts registered to your organization on the Pismo platform
        * External accounts are accounts outside of the Pismo platform
      </td>
    </tr>

    <tr>
      <td>
        **ACC. ID**
      </td>

      <td>
        The ID of the account receiving the disbursement

        **Note:** The account ID applies to internal accounts only.
      </td>
    </tr>

    <tr>
      <td>
        **STATUS**
      </td>

      <td>
        The status of the disbursement

        For more information, refer to [Manage loans](https://developers.pismo.io/pismo-docs/docs/manage-loans).
      </td>
    </tr>
  </tbody>
</Table>

# Manage loans

From Control Center, you can do the following:

* [Disburse a loan](#disburse-a-loan)
* [Adjust a loan](#adjust-a-loan)

> 📘 Dual approval
>
> If your company is using the dual approval feature, these changes require approval. With dual approval, you initiate the change and submit a request for approval. A second person must review and approve it. The change doesn't take effect until it's been approved.
>
> For more information about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).

## Disburse a loan

Make disbursements to release funds to your customers' accounts.

> 📘 Disbursement criteria
>
> You can only make a disbursement if you meet at least one of the following criteria:
>
> * The loan status is **Booked** and the disbursement amount is less than the loan principal amount.
> * The loan is configured for multiple disbursements and the loan status is **Active**. When making a disbursement, the cumulative value of all disbursements must not exceed the loan principal amount.\
>   **Example:** For a loan with a principal amount of $10,000, if you've already disbursed $7,000, your remaining disbursements must not exceed $3,000.

> 📘 External accounts
>
> You can't make a disbursement to an external account from Control Center. This option is intended only to keep a log of external disbursements, without any movement of funds.

To make a disbursement, do the following:

1. Select a loan.

2. Select **Manage loan** > **Disburse loan**.

   <Image align="left" alt="screenshot showing the Disburse loan button" border={true} src="https://files.readme.io/9474bb996d4e9e9dd3bed5f04a916eaa73ae680b066de02ee6b31b69ed66c77f-disburse-loan-button.png" className="border" />

3. In the **Disburse loan** dialog, configure the disbursement details.\
   **Note:** You can't select blocked or canceled accounts.

4. Select **Next**.
   * If you selected **External**, the disbursement details are logged and an entry is added to the **Disbursement** tab.
   * If you selected **Internal**, the funds are paid out to your selected internal account and an entry is added to the **Disbursement** tab.

## Adjust a loan

Make adjustments to your customers' loan repayment details.

You can make adjustments to:

* Correct repayment calculation errors
* Respond to borrower requests, such as changing payment terms
* Restructure payments to reflect updated loan conditions

When you make an adjustment, your changes update the repayment schedule and affect the overall loan balance.

> 📘 Adjustment criteria
>
> To make an adjustment, the loan status must be **Active** and the repayment installment status must not be **Paid** or **Canceled**.

To make an adjustment, do the following:

1. Select a loan.
2. Select **Manage loan** > **Adjust loan**.

   <Image alt="Screenshot showing the Adjust loan button" border={true} src="https://files.readme.io/6d79e1ce1473d36883cb5aafb6d145b214bcb60f0ade25f31546574ac822e60b-adjust-loan-button.png" className="border" />

   Alternatively, on the **Repayment schedule** tab, select the adjust icon for the installment you want to adjust.
3. In the **Adjust loan** dialog, configure the loan adjustment.
4. Select **Next**.\
   The installment and overall loan repayment details are adjusted.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/simulations` | `post-v1-simulation` | Create simulation | `api-specs/Core_platform_-_Payment_methods_admin.yaml` | no | KU-API-core-platform-payment-methods-admin--simulation |
| `POST /v2/loans` | `bookLoanV2` | Book loan | `api-specs/Lending.yaml` | no | KU-API-lending--loans |

### Operation essentials

- **`POST /v1/simulations`** (`post-v1-simulation`): security not declared; required parameters none declared; required body fields `amount`, `authorization_mode`; response statuses 200, 400, 422, 500; error codes in examples `DO0002`, `SI001`, `SI003`; events none listed.
- **`POST /v2/loans`** (`bookLoanV2`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `installment_plan_id`, `loan_product_id`, `number_of_installments`; response statuses 202, 400, 500; error codes in examples `ELND0004`, `ELND0001`; events `lending-loan-booked-1`, `platform-authorization-platform-authorization-1`.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `loan-products-cc` | Loan products | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `bookLoanV2` | `lending-loan-booked-1` |
| `bookLoanV2` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/control-center/digital-lending.md`: updatedAt 2026-08-31T15:01:15.000Z.
- `docs/control-center/loan-products-cc.md`: updatedAt 2026-08-31T15:25:07.000Z.
- `docs/control-center/manage-loans-in-control-center.md`: updatedAt 2026-08-05T11:19:15.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- Operation link `loan-products-cc` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/digital-lending.md` | whole document | https://developers.pismo.io/pismo-docs/docs/digital-lending | `a98447a1ef4c5bdc…` | 2026-08-31T15:01:15.000Z |
| `docs/control-center/loan-products-cc.md` | whole document | https://developers.pismo.io/pismo-docs/docs/loan-products-cc | `309e953331f1fe44…` | 2026-08-31T15:25:07.000Z |
| `docs/control-center/manage-loans-in-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/manage-loans-in-control-center | `4bcae297d95adfce…` | 2026-08-05T11:19:15.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods-admin--simulation` — API reference: Core platform - Payment methods admin — Simulation
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-BANK-interest-bearing-accounts` — Interest-bearing accounts
- `KU-CC-deposit-products` — Control Center deposit products and interest plans
- `KU-CC-dual-approval` — Dual approval
- `KU-CC-processing-codes` — Control Center processing codes, transaction types and general ledger accounts
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-EVT-catalogue-lending` — Event catalogue: lending
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-LEND-lending-overview` — Lending overview and participants
- `KU-LEND-loan-management` — Loan management overview
- `KU-LEND-loan-products` — Loan products: overview and creation
