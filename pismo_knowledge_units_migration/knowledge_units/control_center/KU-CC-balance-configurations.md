---
ku_id: KU-CC-balance-configurations
title: Control Center balance configurations
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/balance-configurations-in-control-center.md
  sha256: 9c3ba0118ef1f8897ce2eb08c8fffdaa674bd616bafcda768e2281b4deb499ae
  url: https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center
  role: primary_guide
  updated_at: '2026-06-12T17:23:35.000Z'
- path: docs/control-center/edit-an-existing-balance-configuration.md
  sha256: a227ff846b3f21554887366b13694df044c247d43a10935adf4900b6a8256aab
  url: https://developers.pismo.io/pismo-docs/docs/edit-an-existing-balance-configuration
  role: primary_guide
  updated_at: '2026-03-18T15:09:26.000Z'
operations: []
related_kus:
- KU-CORE-balance-configurations
grouping_rationale: Create and edit.
---

# Control Center balance configurations

**KU ID:** `KU-CC-balance-configurations` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Create and edit.

Scope as stated in `docs/control-center/balance-configurations-in-control-center.md`:

> Use Control Center to create balance configurations, which are a flexible set of rules that define how account balances and limits are impacted based on transaction activity. You can create them to manage account balances for your card and banking transactions.

Scope as stated in `docs/control-center/edit-an-existing-balance-configuration.md`:

> Change your balance configurations as needed by updating scenarios.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/balance-configurations-in-control-center.md`: Balance configurations in Control Center; View balance configurations; Create a balance configuration; Activate or deactivate a balance configuration
- `docs/control-center/edit-an-existing-balance-configuration.md`: Edit an existing balance configuration; Add a scenario; Edit a scenario; Edit the scenario name; Change the status; Edit conditions; Reorder conditions; Add or edit a condition; Delete a condition; Edit filters; Processing codes; MCCs; Installments; Currency codes

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/balance-configurations-in-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center · updatedAt: 2026-06-12T17:23:35.000Z

<!-- source:begin path=docs/control-center/balance-configurations-in-control-center.md part=0-end -->

# Balance configurations in Control Center

Use Control Center to create balance configurations, which are a flexible set of rules that define how account balances and limits are impacted based on transaction activity. You can create them to manage account balances for your card and banking transactions.

For example, if you’re a bank, you can give a customer two separate credit limits for the same account:

* A primary limit for everyday purchases
* A secondary limit specifically for purchases made in multiple installments

For more information and examples, refer to [Balance configurations overview](https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview).

<Callout icon="📘" theme="info">
  You can create and view balance configurations at the program level only, which apply to all accounts in the program. To create and view balance configurations at the organization, program, or specific account level, use the appropriate endpoint in the [Balance configuration API](https://developers.pismo.io/pismo-docs/docs/post-v1-balances-config-1).
</Callout>

From Control Center, you can do the following:

* [View the list of balance configurations ](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center#view-the-list-of-balance-configurations) at the program level
* [Create a balance configuration ](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center#create-a-balance-configuration) at the program level
* [Activate or deactivate a balance configuration](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center#activate-or-deactivate-a-balance-configuration)
* [Edit an existing balance configuration](https://developers.pismo.io/pismo-docs/docs/edit-an-existing-balance-configuration) at the program level

# View balance configurations

To view the list of balance configurations at the program level:

1. From the main menu, select **Configurations** > **Balance configurations**.
2. On the **Balance configurations** screen, select a balance configuration to review its details. You can find a specific balance configuration by using the **Filter** field. Filter on the program name or balance configuration ID.

# Create a balance configuration

To create a balance configuration at the program level:

1. From the main menu, select **Configurations** > **Balance configurations**.
2. On the **Balance configurations** screen, select **Create configuration**.
3. On the **Program** screen, select the program to associate with this balance configuration. You can select only one program. Select **Next**.
4. On the **Scenario** screen, do the following:
   1. Enter a name for the scenario.
   2. Set whether to create the balance configuration as **active** (activated when created) or **inactive** (created but not activated).
   3. Select **Next**.
5. Create filters, which are the rules used in scenarios. Refer to the following table for descriptions of each filter. You can also find this information in Control Center.

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Filter
      </th>

      <th>
        Description
      </th>

      <th>
        Examples
      </th>

      <th>
        Required
      </th>

      <th>
        Special instructions
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Processing codes
      </td>

      <td>
        Specify transaction types
      </td>

      <td>
        Purchases\
        Withdrawals
      </td>

      <td>
        Yes, you must select at least one processing code.
      </td>

      <td>
        You can add multiple process codes and even select all.
      </td>
    </tr>

    <tr>
      <td>
        Merchant Category Codes (MCCs)
      </td>

      <td>
        Categorize businesses by their goods and services
      </td>

      <td>
        MCC 5411 is the code for grocery stores.

        MCC 5812 is the code for restaurants.
      </td>

      <td>
        No
      </td>

      <td>
        You can add multiple MCCs.
      </td>
    </tr>

    <tr>
      <td>
        Installments
      </td>

      <td>
        Indicate that a total purchase is split into smaller, manageable payments
      </td>

      <td>
        A credit card payment is split into three installments.
      </td>

      <td>
        No
      </td>

      <td>
        Set both minimum and maximum installments or leave both blank. The maximum number of installments allowed is 99.
      </td>
    </tr>

    <tr>
      <td>
        Currency codes
      </td>

      <td>
        Specify the three-letter identifier for currencies
      </td>

      <td>
        BRL is the code for the Brazilian real.

        USD is the code for the U.S. dollar.
      </td>

      <td>
        No
      </td>

      <td>
        You can add just one currency code.
      </td>
    </tr>
  </tbody>
</Table>

6. Review the filters you created in the **Filters created** field, then select **Next**.
7. On the **Conditions** screen, define the criteria for evaluating scenarios.<br />\
   Note that when you create a balance configuration, you define just one condition initially, which is known as the **default**. This is important because the Pismo platform checks conditions in the priority order you set. If the first condition matches, the search stops there, and the platform uses this condition. If not, the search continues until there is a match. If no conditions match, the platform denies the transaction.<br />\
   If you create other conditions, known as **custom** conditions, they are higher in priority than the default condition. The default condition is always the lowest in the priority order, meaning that it’s always checked last.<br />\
   You can reorder, edit, and delete custom conditions, but you can’t reorder, edit, or delete the default.<br />\
   To create more conditions, first create this balance configuration and then you can edit it. For more information, refer to [Edit an existing balance configuration](https://developers.pismo.io/pismo-docs/docs/edit-an-existing-balance-configuration).<br />\
   Your options vary depending on whether you selected a debit or credit program earlier. Refer to the following table for descriptions of each condition. You can also find this information in the tooltips in Control Center.

**Credit programs**

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Condition
      </th>

      <th>
        Description
      </th>

      <th>
        Options
      </th>

      <th>
        Special instructions
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Amount consider
      </td>

      <td>
        Checks if the account has enough limit or balance
      </td>

      <td>
        * *Contract amount*\* is the total amount, including the principal amount, interest, and fees.
        * *Principal amount*\* is the original amount, excluding interest and fees.
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Consider
      </td>

      <td>
        Specifies which limits and balances should be checked before approving a transaction
      </td>

      <td>
        * *Available credit limit*\* is the portion of a card holder's total credit limit that is available for use.
        * *Available withdrawal credit*\* is the amount a cardholder can withdraw from their credit account, after accounting for previous withdrawals and related transactions.
        * *Available total installment credit*\* is the amount of credit still available for purchases made in installments within a credit account.
      </td>

      <td>
        When selecting multiple options, keep in mind that they interact differently based on your choices.

        * *(available credit limit + over-limit)*\* = the transaction is checked against the sum of these two options
        * *(available credit limit + over-limit) & available withdrawal credit*\* = the transaction is checked against the sum of available credit limit + over-limit, and it’s also separately checked against the amount of available withdrawal credit
        * *(available credit limit & available withdrawal credit)*\* = the transaction is checked against both amounts separately
      </td>
    </tr>

    <tr>
      <td>
        Impact
      </td>

      <td>
        Specifies the limits or balances to credit or debit using the contract amount
      </td>

      <td>
        * *Available credit limit*\* is the portion of a cardholder's total credit limit that is available for use. It’s based on the initial total credit limit and any debit and credit activity on the account.
        * *Available withdrawal credit*\* is the amount a cardholder can withdraw from their credit account, after accounting for previous withdrawals and related transactions.
        * *Available total installment credit*\* is the amount of credit still available for purchases made in installments within a credit account.

        This value is based on the total installment credit limit set for the account and is reduced as installment-based transactions are made. It helps determine whether a customer can make additional purchases using installment plans.
      </td>

      <td />
    </tr>
  </tbody>
</Table>

**Debit programs**

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Condition
      </th>

      <th>
        Description
      </th>

      <th>
        Options
      </th>

      <th>
        Special instructions
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Amount consider
      </td>

      <td>
        Checks if the account has enough limit or balance
      </td>

      <td>
        * *Contract amount*\* is the total amount, including the principal amount, interest, and fees.
        * *Principal amount*\* is the original amount, excluding interest and fees.
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Consider
      </td>

      <td>
        Specifies which limits and balances should be checked before approving a transaction
      </td>

      <td>
        * *Available credit limit*\* is the available balance in a cardholder’s checking account.
        * *Available savings account limit*\* is the money in a savings account that is currently accessible.
        * *Held funds* \*are amounts in an account that are temporarily blocked from use.
        * *Additional funds*\* are extra money added to an account to increase the total available balance, such as a promotional credit or bonus.
      </td>

      <td>
        When you select **Available credit limit**, the transaction is automatically checked against the sum of available credit limit + available savings account limit + overdraft limit.
      </td>
    </tr>

    <tr>
      <td>
        Impact
      </td>

      <td>
        Specifies the limits or balances to credit or debit using the contract amount
      </td>

      <td>
        * *Available credit limit*\* is the available balance in a cardholder’s checking account.
        * *Available savings account limit* \*is the money in a savings account that is currently accessible.
        * *Held funds*\* are amounts in an account that are temporarily blocked from use.
        * *Additional funds*\* are extra money added to an account to increase the total available balance, such as a promotional credit or bonus.
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Opposite impact
      </td>

      <td>
        Specifies the limits or balances where funds should be transferred to offset the option chosen for Impact
      </td>

      <td>
        Same as **Impact**
      </td>

      <td />
    </tr>
  </tbody>
</Table>

8. Review the conditions you created in the **Conditions created** field, then select **Next**.
9. On the **Review and create balance configuration** screen, ensure the information is correct. If you want to change anything, select **Back**. When you’re satisfied with all the information, select **Create**.

# Activate or deactivate a balance configuration

You can create a balance configuration as **active** (immediately activated) or as **inactive** (saved but not activated) and activate it later.

To activate an inactive balance configuration:

1. From the main menu, select **Configurations** > **Balance configurations**.
2. Select the inactive balance configuration you want to activate.
3. On the **Balance configuration details** screen, select your configuration.
4. On the **Scenario details** screen, set the **Inactive** toggle switch to **Active**.

To deactivate a balance configuration at any time, use the previous steps and set the **Active** toggle switch to **Inactive**.
<!-- source:end -->

### Source 2: `docs/control-center/edit-an-existing-balance-configuration.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/edit-an-existing-balance-configuration · updatedAt: 2026-03-18T15:09:26.000Z

<!-- source:begin path=docs/control-center/edit-an-existing-balance-configuration.md part=0-end -->

# Edit an existing balance configuration

Change your balance configurations as needed by updating scenarios.

# Add a scenario

To add a scenario:

1. From the main menu, select **Configurations** > **Balance configurations**.
2. On the **Balance configurations** screen, select a balance configuration to review its details. You can find a specific balance configuration by using the **Filter** field. Filter on the program name or balance configuration ID.
3. On the **Balance configuration details** screen, select **Add scenario**.
4. Use steps 4-9 of [Create a balance configuration](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center#create-a-balance-configuration) to complete the process.

# Edit a scenario

To edit a scenario:

1. From the main menu, select **Configurations** > **Balance configurations**.
2. On the **Balance configurations** screen, select a balance configuration to review its details. You can find a specific balance configuration by using the **Filter** field. Filter on the program name or balance configuration ID.
3. On the **Balance configuration details** screen, select a scenario. From here, you can edit the scenario name, change its status, edit conditions, and edit filters.

## Edit the scenario name

To change the scenario name, select the edit icon (pencil), enter a new name, and select **Save**.

## Change the status

If you created a balance configuration and initially set it as inactive, you can set it to active anytime. Similarly, you can deactivate an active configuration anytime as well. To change the status, refer to [Activate or deactivate a balance configuration](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center#activate-or-deactivate-a-balance-configuration).

## Edit conditions

Use conditions to define the criteria for evaluating scenarios. Note that when you create a balance configuration, you define just one condition initially, which is known as the **default**. This is important because the Pismo platform checks conditions in the priority order you set. If the first condition matches, the search stops there, and the platform uses this condition. If not, the search continues until there is a match. If no conditions match, the platform denies the transaction.<br />\
If you create other conditions, known as **custom** conditions, they are higher in priority than the default condition. The default condition is always the lowest in the priority order, meaning that it’s always checked last.<br />\
You can reorder, edit, and delete custom conditions, but you can’t reorder, edit, or delete the default.

### Reorder conditions

To reorder conditions, drag and drop them to the order you prefer. The default condition must always be last.

### Add or edit a condition

1. On the **Scenario details** screen, do one of the following:
   * To add a condition, select **Add condition**.
   * To edit a condition, select the edit icon (pencil) for the condition you want to edit.
2. Use steps 7-9 of [Create a balance configuration](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center#create-a-balance-configuration) to complete the process.

### Delete a condition

To delete an existing condition, on the **Scenario details** screen, select the delete icon (trash can) for the condition you want to delete and confirm.

## Edit filters

Use filters, which are the rules used in scenarios. You can filter transactions by processing codes, Merchant Category Codes (MCCs), installments, and currency codes. For more information on filter types, refer to step 5 of [Create a balance configuration](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center#create-a-balance-configuration). The changes you can make depend on the filter type.

### Processing codes

You can add and delete processing codes. On the **Scenario details** screen, select **Processing codes** and do one of the following:

* To add a new processing code, select **Add processing codes**. On the **Filters** screen, add the codes you want and select **Create**.
* To delete a processing code, select the delete icon (trash can) for the code you want to delete and confirm.

### MCCs

You can add and delete MCCs. On the **Scenario details** screen, select **MCCs** and do one of the following:

* To add a new MCC, select **Add MCC**. On the **Filters** screen, add the codes you want and select **Create**.
* To delete a MCC, select the delete icon (trash can) for the code you want to delete and confirm.

### Installments

You can edit an existing installment.

1. On the **Scenario details** screen, select **Installments**.
2. Select the edit icon (pencil), enter the new installment amounts in the **Minimum** and **Maximum** fields, and select **Save.**

### Currency codes

You can edit and delete a currency code. You can have only one currency code. On the **Scenario details** screen, select **Currency codes** and do one of the following:

* To edit a currency code, select the edit icon (pencil), search for the currency code, and select **Save**.
* To delete a currency code, select the delete icon (trash can) for the code you want to delete and confirm.
<!-- source:end -->

## Lifecycle status

- `docs/control-center/balance-configurations-in-control-center.md`: updatedAt 2026-06-12T17:23:35.000Z.
- `docs/control-center/edit-an-existing-balance-configuration.md`: updatedAt 2026-03-18T15:09:26.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/balance-configurations-in-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center | `9c3ba0118ef1f889…` | 2026-06-12T17:23:35.000Z |
| `docs/control-center/edit-an-existing-balance-configuration.md` | whole document | https://developers.pismo.io/pismo-docs/docs/edit-an-existing-balance-configuration | `a227ff846b3f2155…` | 2026-03-18T15:09:26.000Z |

## Related knowledge units

- `KU-CORE-balance-configurations` — Balance configurations and filter templates
