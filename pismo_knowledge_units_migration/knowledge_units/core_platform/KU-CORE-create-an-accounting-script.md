---
ku_id: KU-CORE-create-an-accounting-script
title: Create accounting scripts
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/create-an-accounting-script.md
  sha256: 43c1592d572fddf6a1faf7cf1259f38cd88c0acc199562ed4c01fff3bb4fe802
  url: https://developers.pismo.io/pismo-docs/docs/create-an-accounting-script
  role: primary_guide
  updated_at: '2026-09-01T18:41:20.000Z'
operations:
- CreateAccountingScript
- CreateAccountingScriptV2
related_kus:
- KU-API-core-platform-accounting--accounting-scripts-v1
- KU-API-core-platform-accounting--accounting-scripts-v2
- KU-CORE-accounting-overview
grouping_rationale: single source page
---

# Create accounting scripts

**KU ID:** `KU-CORE-create-an-accounting-script` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/create-an-accounting-script.md`:

> Accounting scripts specify the details of an accounting entry, and the rules used to generate it. When an event occurs, such as funds being credited to an account or a purchase being confirmed, the Pismo platform uses the accounting script to create the appropriate accounting entry.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/create-an-accounting-script.md`: Create accounting scripts; Accounting script versions; Supported flows; New features in accounting scripts v2; Flexibility across multiple programs; Single‑step setup for accounts and routing; Expressions; Parameters; Create script; Examples; Accounting scripts v1; Accounting script v2

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/create-an-accounting-script.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/create-an-accounting-script · updatedAt: 2026-09-01T18:41:20.000Z

<!-- source:begin path=docs/core-platform/create-an-accounting-script.md part=0-end -->

# Create accounting scripts

Accounting scripts specify the details of an accounting entry, and the rules used to generate it. When an event occurs, such as funds being credited to an account or a purchase being confirmed, the Pismo platform uses the accounting script to create the appropriate accounting entry.

# Accounting script versions

The Pismo platform offers two versions of setting up accounting routing.

* [Accounting scripts v1](https://developers.pismo.io/pismo-docs/reference/createaccountingscript)
* [Accounting scripts v2](https://developers.pismo.io/pismo-docs/reference/createaccountingscriptv2)

Below are the key functional differences between the two accounting script versions.

## Supported flows

The following table lists available flows supported by each accounting scripts version.

| Flows                                                           | v1 | v2 |
| :-------------------------------------------------------------- | :- | :- |
| Clearing                                                        | x  |    |
| Installment contract creation                                   | x  |    |
| Installment contract cancellation                               | x  |    |
| Debit transaction                                               | x  | x  |
| Credit transaction                                              | x  |    |
| Installment cycle opening and closing                           | x  | x  |
| Accrual                                                         | x  | x  |
| Accrual that supports the 4966 resolution for the Brazil region |    | x  |
| Daily interest appropriation                                    | x  |    |
| Seller management                                               | x  |    |
| Discharge                                                       |    | x  |

## New features in accounting scripts v2

Accounting scripts v2 introduce the following features that are not supported in accounting scripts v1.

* [Flexibility across multiple programs](https://developers.pismo.io/pismo-docs/docs/create-an-accounting-script#flexibility-across-multiple-programs)
* [Single‑step setup for accounts and routing](https://developers.pismo.io/pismo-docs/docs/create-an-accounting-script#singlestep-setup-for-accounts-and-routing)
* [Expressions](https://developers.pismo.io/pismo-docs/docs/create-an-accounting-script#expressions)
* [Parameters](https://developers.pismo.io/pismo-docs/docs/create-an-accounting-script#parameters)

### Flexibility across multiple programs

With accounting scripts v2, you have the following options to configure routing based on programs.

* Perform batch routing across multiple program IDs simultaneously
* Configure routing based on program type

This improves efficiency, especially when multiple programs share similar accounting behavior.

### Single‑step setup for accounts and routing

Unlike accounting scripts v1, where you must create accounting accounts before configuring routing, accounting scripts v2 let you submit the entire accounting script configuration in a single request using the [Create accounting script v2](https://developers.pismo.io/pismo-docs/reference/createaccountingscriptv2) endpoint. This eliminates intermediate steps and reduces the risk of configuration mismatches between accounts and scripts.

### Expressions

Accounting scripts v2 provide additional tools that enhance accuracy and configurability and allow you to define how the accounting amount should be calculated in the `expression` field. This removes the need for you to perform external calculations before routing.

In this context, expressions are mathematical equations that generate accounting values dynamically rather than relying on fixed values. All values that make up a transaction can be provided directly in the accounting entry input. Alternatively, you can define an expression to calculate a specific value based on other transaction attributes.

#### Expression examples

If you want to receive the transaction amount net of a fee or interest charge, you can configure expressions such as: `amount-interest` or `amount-fee`. This allows accounting amounts to be calculated automatically rather than being passed explicitly in the transaction input.

You can pass the following expressions in the `expressions` field with the description of how the accounting entry will calculate this value.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th width="180px">
        Expression value
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `amount`
      </td>

      <td>
        Full principal amount of the transaction on the event date. It usually represents the gross value of the operation associated with the corresponding entry type.
      </td>
    </tr>

    <tr>
      <td>
        `fee`
      </td>

      <td>
        Total fee amount
      </td>
    </tr>

    <tr>
      <td>
        `amount-fee`
      </td>

      <td>
        Net amount excluding fee
      </td>
    </tr>

    <tr>
      <td>
        `interest`
      </td>

      <td>
        Total interest amount. Amount of interest calculated/incurred on the transaction, whether it is a contract transaction or an installment.

        **Important:** This should only be used if the interest is included together with the transaction’s total amount, so that the “interest” is explicitly identified as such. If the interest is already in a separate transaction, “amount” should be used instead.
      </td>
    </tr>

    <tr>
      <td>
        `amount-interest`
      </td>

      <td>
        Net amount excluding interest. Interest for transactions composed of multiple monetary components, the value to be posted may be defined using calculation of expressions (e.g., amount – interest).
      </td>
    </tr>

    <tr>
      <td>
        `fine`
      </td>

      <td>
        Fine amount included in a payment (amount that is “discharged”). This type should only be used when linked to transaction 201 (payment). When used, it provides details of how much of that payment corresponds to the fine.
      </td>
    </tr>
  </tbody>
</Table>

For example, consider a transaction composed of the following components:

* Principal amount: `100`
* Interest: `20`

If you want to create an accounting entry based on the transaction amount excluding the interest portion,  use the expression: `amount-interest` in the `expression` field.

This results in the calculation `100 - 20 = 80` and accounting entry 101 generated with a value of `80`, representing the transaction amount minus the interest amount.

### Parameters

Parameters support custom implementation of product‑specific and regulatory‑specific accounting logic. Parameters are set in the `parameters` object. They allow you to specify when accounting entries are generated (the exact point in the lifecycle of an account or a transaction) and to define other specific accounting behaviors and accrual-related rules.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Name
      </th>

      <th>
        Valid values
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `pismo:timing`
      </td>

      <td>
        `REGULAR`\
        `DUE_DATE`\
        `CYCLE_OPENING`\
        `CYCLE_CLOSING`\
        `DAILY_INTEREST`
      </td>

      <td>
        Posting occurs...

        * `REGULAR` when the transaction is created
        * `DUE_DATE` on the transaction’s due date
        * `CYCLE_OPENING` on the statement opening
        * `CYCLE_CLOSING` on the statement closing
        * `DAILY_INTEREST` when the daily interest is posted
      </td>
    </tr>

    <tr>
      <td>
        `pismo:overdue`
      </td>

      <td>
        `TRUE` or `FALSE`
      </td>

      <td>
        Indicates whether the account is overdue. You are responsible for providing logic that evaluates and returns the appropriate value.
      </td>
    </tr>

    <tr>
      <td>
        `pismo:rounding`
      </td>

      <td>
        `TRUE` or `FALSE`
      </td>

      <td>
        Indicates whether rounding should be applied to the accounting calculation or accrual amount.
      </td>
    </tr>

    <tr>
      <td>
        `pismo:accrual_type`
      </td>

      <td>
        `REFINANCING`
      </td>

      <td>
        Identifies the type of accrual being processed.
      </td>
    </tr>

    <tr>
      <td>
        `bacen:classification`
      </td>

      <td>
        `1`, `2`, or `3`
      </td>

      <td>
        (Brazil-specific) For institutions that comply with BACEN Resolution 4,966, this parameter can be used to apply different accounting treatments according to the customer's risk classification. This parameter allows accounting rules to be configured according to the customer classification requirements defined by BACEN regulations.

        Values `1` and `2` are used for customers in stage 1 or stage 2 who are not classified as problematic assets.

        Value `3` is used for customers classified as problematic assets.
      </td>
    </tr>
  </tbody>
</Table>

# Create script

To create an accounting script, use the following endpoints.

* V1: [Create accounting script v1](https://developers.pismo.io/pismo-docs/reference/createaccountingscript)
* V2:[Create accounting script v2](https://developers.pismo.io/pismo-docs/reference/createaccountingscriptv2)

<Callout icon="📘" theme="info">
  You can include cost centers in the accounting script to improve its management. This is helpful when you need to create an accounting script for revenue and another for expense.

  Only create cost centers if your organization requires it.  If you need to create a cost center, enter required values in the `cost_center` object with details about the [cost center](https://developers.pismo.io/pismo-docs/docs/accounting-overview#cost-centers) in your organization. If you don’t need to create a cost center, then enter `0` in the required fields.
</Callout>

## Examples

### Accounting scripts v1

The following payload request example for [Create accounting script v1](https://developers.pismo.io/pismo-docs/reference/createaccountingscript) is creating an accounting script for entry type ID 404 (IOF of international transactions) and doesn't include any cost centers.

```json
{
  "program_id": {{program_id}},
  "event_type_id": 404,
  "entry_type_id": 404,
  "entry_name": "amount",
  "debit_accounting_account_id": 8195465874,
  "credit_accounting_account_id": 8195410017,
  "cost_center": {
    "debit_org": "0",
    "credit_org": "0",
    "debit_cost": "0",
    "credit_cost": "0"
  }
}
```

The following payload request example for [Create accounting script v1](https://developers.pismo.io/pismo-docs/reference/createaccountingscript) is creating an accounting script for entry type ID 101 (purchase) and defines the organization's cost centers.

```json
{
  "id": 812046,
  "program_id": 1,
  "event_type_id": 101,
  "entry_type_id": 101,
  "entry_name": "interest",
  "debit_accounting": 
		{
      "id": 1,
      "description": "ACCOUNTING ACCOUNT CREATION TEST",
      "cosif": "161200000006",
			"account": "123123132-x",
      "program_id": 0,
      "created_at": "2021-07-22T00:37:20Z",
      "deactivated_at": null
    },	
  "credit_accounting": 
  {
    "id": 1,
    "description": "ACCOUNTING ACCOUNT CREATION TEST",
    "cosif": "161200000006",
		"account": "123123132-x",
    "program_id": 0,
    "created_at": "2021-07-22T00:37:20Z",
    "deactivated_at": null
  },
  "cost_center": {
    "debit_org": "TN-ORG1",
    "credit_org": "TN-ORG2",
    "debit_cost": "C1",
    "credit_cost": "C2",
    "deactivated_at": null
  },
  "processing_code": "00",
  "deactivated_at": null
 }

```

### Accounting script v2

The following payload request example for [Create accounting script v2](https://developers.pismo.io/pismo-docs/reference/createaccountingscriptv2) defines an accounting script for entry type ID 121 (installment transactions) that uses the full principal amount expression and regular timing, causing the Pismo platform to generate the accounting entry when the transaction is created.

```json
{
 "program_id": 1122,
 "event_type_id": 121, //transaction type ID
 "entry_type_id": {
  "id": 1,
  "description": "INSTALLMENT",
  "type": "CREATION",
  "reason": "NEW",
  "responsible": "service-desk"
 },
 "debit_accounting": {
  "description": "Collection and disbursement on behalf",
  "account": "51920001"
 },
  "credit_accounting": {
  "description": "Outstanding balance indue",
  "account": "27510001"
 },
 "expression": "AMOUNT",
 "parameters": [
  {
   "name": "pismo:timing",
   "value": "REGULAR"
  }
 ]
}

```

You can also combine  parameters to create an accounting script, as illustrated in the following payload request example for [Create accounting script v2](https://developers.pismo.io/pismo-docs/reference/createaccountingscriptv2) that uses total interest amount expression and defines several different additional parameters.

```json
{
   "program_types": ["CREDIT"],
   "entry_type_id": {
     "id": 2010,
     "description": "MORA DIARIA",
     "type": "CREATION",
     "reason": "NEW",
     "responsible": "service-desk"
  },
   "debit_accounting": {
     "description": "CARTAO DE CRED-PARC.CORRENTE PARC.EMISSOR-PISMO",
     "account": "1612000007"
  },
   "credit_accounting": {
     "description": "(-)R.A CARTAO DE CREDITO-ROTATIVO-PISMO",
     "account": "1612000002"
  },
   "processing_code": "",
   "expression": "interest",
   "parameters": [
    {
       "name": "bacen:classification",
       "value": "3"
    },
    {
       "name": "pismo:accrual_type",
       "value": "OVERDUE"
    },
    {
       "name": "pismo:overdue",
       "value": "TRUE"
    },
    {
       "name": "pismo:rounding",
       "value": "FALSE"
    }
    
  ]
}

```

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/accounting-scripts` | `CreateAccountingScript` | Create accounting script V1 | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-scripts-v1 |
| `POST /v2/accounting-scripts` | `CreateAccountingScriptV2` | Create accounting script V2 | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-scripts-v2 |

### Operation essentials

- **`POST /v1/accounting-scripts`** (`CreateAccountingScript`): security `BearerAuth`; required parameters none declared; required body fields `entry_type_id`, `event_type_id`, `credit_accounting_account_id`, `debit_accounting_account_id`, `program_id`; response statuses 201, 400, 409; error codes in examples none; events none listed.
- **`POST /v2/accounting-scripts`** (`CreateAccountingScriptV2`): security `BearerAuth`; required parameters none declared; required body fields `credit_accounting`, `debit_accounting`, `entry_type_id`, `expression`; response statuses 201, 400, 409; error codes in examples none; events none listed.

## Lifecycle status

- `docs/core-platform/create-an-accounting-script.md`: updatedAt 2026-09-01T18:41:20.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/create-an-accounting-script.md` | whole document | https://developers.pismo.io/pismo-docs/docs/create-an-accounting-script | `43c1592d572fddf6…` | 2026-09-01T18:41:20.000Z |

## Related knowledge units

- `KU-API-core-platform-accounting--accounting-scripts-v1` — API reference: Core platform - Accounting — Accounting scripts V1
- `KU-API-core-platform-accounting--accounting-scripts-v2` — API reference: Core platform - Accounting — Accounting scripts V2
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
