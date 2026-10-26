---
ku_id: KU-CRED-recurring-charges
title: Recurring charges
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/recurring-charges.md
  sha256: 7a047e09b188efc447fab051dbe791621f0304744bc78dd50914a0a87a2f90aa
  url: https://developers.pismo.io/pismo-docs/docs/recurring-charges
  role: primary_guide
  updated_at: '2026-09-18T16:33:45.000Z'
operations:
- create-recurring-charge-link
- create-recurring-charge-plan
- delete-recurring-charge-link
- disable-recurring-charge-plan
- get-scheduled-charge
- list-scheduled-charges
- update-scheduled-charge
related_kus:
- KU-API-revolving-credit-recurring-charges--recurring-charge-links
- KU-API-revolving-credit-recurring-charges--recurring-charge-plans
- KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges
- KU-EVT-catalogue-balance
- KU-GS-setup-overview
grouping_rationale: single source page
---

# Recurring charges

**KU ID:** `KU-CRED-recurring-charges` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/recurring-charges.md`:

> The Pismo platform's Recurring charges API enables you to set up recurring charge plans for accounts. For example, you could use it to set up an annual fee.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/recurring-charges.md`: Recurring charges; Recurring charge plans; Create a plan; Disable a plan; Recurring charge links; Create a link; Delete a link; Recurring scheduled charges; View scheduled charges; Update a scheduled charge; Annual recurring charge; Examples for recurring charge plans; Recurring charge plan example 1; Recurring charge plan example 2; Recurring charge plan example 3; Examples for scheduled charges; Scheduled charges example 1; Scheduled charges example 2; Scheduled charges example 3

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/recurring-charges.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/recurring-charges · updatedAt: 2026-09-18T16:33:45.000Z

<!-- source:begin path=docs/card-issuing/recurring-charges.md part=0-end -->

# Recurring charges

The Pismo platform's Recurring charges API enables you to set up recurring charge plans for accounts. For example, you could use it to set up an annual fee.

To set up a plan for an account, you first create the plan, then create a link between the plan and the account. Once the two are linked, the plan is automatically activated, and the account can begin incurring charges based on the plan settings. One plan can be linked to multiple accounts, and one account can be linked to multiple plans.

<Callout icon="📘" theme="info">
  An account can even be linked to the same plan multiple times, as long as each link has a different `tracking_id`.
</Callout>

You can deactivate a plan for a specific account by deleting the link between them, or you can disable the plan altogether.

These processes are explained in more detail in the following sections.

# Recurring charge plans

## Create a plan

To create a recurring charge plan, use the [Create recurring charge plan](https://developers.pismo.io/pismo-docs/reference/create-recurring-charge-plan) endpoint. If successful, this endpoint returns an ID for the recurring charge plan, which can be used with the other endpoints in the API.

A recurring charge plan is defined on the [organization (Org)](https://developers.pismo.io/pismo-docs/docs/setup-overview#organization) level.

## Disable a plan

To disable a recurring charge plan, use the [Disable recurring charge plan](https://developers.pismo.io/pismo-docs/reference/disable-recurring-charge-plan) endpoint. Once a plan is disabled, it can no longer be linked to accounts. If you set `disable_all_accounts` to true, the endpoint also deletes any existing links associated with the plan, and the accounts associated with the deleted links no longer incur the charges specified in the plan.

If `disable_all_accounts` is false (the default), then accounts that were linked to the plan before it was disabled remain linked to it, and the accounts continue to incur charges based on the plan.

# Recurring charge links

## Create a link

To link a recurring charge plan to an account, use the [Create link](https://developers.pismo.io/pismo-docs/reference/create-recurring-charge-link) endpoint. If successful, this endpoint returns an ID for the link.

## Delete a link

To deactivate a plan that's linked to an account, use the [Delete recurring charge link](https://developers.pismo.io/pismo-docs/reference/delete-recurring-charge-link) endpoint. If successful, the link between the plan and the account is deleted, and the account no longer incurs the charges specified in the plan. This does not delete the plan itself, and any links the plan has with other accounts are unaffected.

# Recurring scheduled charges

Recurring scheduled charges are recurring charges with status `PENDING`. In other words, they are charges that are scheduled, but have not yet been incurred by the account.

## View scheduled charges

Use the [List scheduled charges](https://developers.pismo.io/pismo-docs/reference/list-scheduled-charges) endpoint to retrieve a list of scheduled charges filtered by query parameters. The returned list includes the ID for each charge in the list. Use the [Get scheduled charge](https://developers.pismo.io/pismo-docs/reference/get-scheduled-charge) endpoint with this ID to retrieve the information for a specific charge.

## Update a scheduled charge

Use the [Update scheduled charge](https://developers.pismo.io/pismo-docs/reference/update-scheduled-charge) endpoint to modify a scheduled charge.

<Callout icon="🚧" theme="warn">
  To update a scheduled charge for a cycle, you must execute [Update scheduled charge](https://developers.pismo.io/pismo-docs/reference/update-scheduled-charge) before the cycle closing date of that cycle. In other words, you can update a scheduled charge for a future cycle or the current cycle, but not for a cycle that is already closed.
</Callout>

<Callout icon="📘" theme="info">
  [Update scheduled charge](https://developers.pismo.io/pismo-docs/reference/update-scheduled-charge) does not change the recurring charge plan, which might be linked to multiple accounts. It updates one charge for one cycle/statement of one account.
</Callout>

## Annual recurring charge

A common special case is setting up an annual recurring charge. You can set up this type of charge in one of two ways.

* As a monthly charge where each month 1/12th of the annual amount is charged
* As a once per year fee. To set up this type of fee, follow these steps.
  1. Set up a monthly fee equal to the full annual amount.
  2. Apply a 100% discount to the first 11 cycles. This makes months 1 through 11 have zero net charges, and those charges appear on the statement as `SETTLED`. Only cycle 12 charges the full amount.
  3. Set `renew_method`=`WITH_DISCOUNT`. This tells the Pismo platform to reapply the 11 discounts on each renewal.

For examples of both approaches, refer to [Recurring charge plan example 3](https://developers.pismo.io/pismo-docs/docs/recurring-charges#recurring-charge-plan-example-3).

# Examples for recurring charge plans

## Recurring charge plan example 1

Suppose you define a recurring charge plan with the following settings:

* `number_of_cycles` = 6
* `installment_amount` = 20
* `first_cycles_to_discount` = 2
* `discount_percentage` = 10
* `split_transaction` = true

Since `split_transaction` is true, two transactions are posted to the account for each discounted installment — a debit transaction for the installment amount and a credit transaction for the discount. If an installment is not discounted, only one transaction is posted.

<Callout icon="📘" theme="info">
  You specify the type of transaction used for the installment using `processing_code`. If `split_transaction` is true, you specify the type of transaction used for the discount using `secondary_processing_code`. So, normally, you would use `processing_code` to specify a debit transaction and `secondary_processing_code` to specify a credit transaction. However, you aren’t forced to do this. You could make both transactions debits, for example. It’s unlikely that you’ll encounter a scenario where you would need to do something like this, so it's not recommended.
</Callout>

`installment_amount` is the charge per cycle before any discount is applied. Since the discount percentage is 10%, the actual discount is $2 (the installment amount $20 multiplied by 0.1).  `first_cycles_to_discount` is 2, so the charge is $18 ($20 - $2) for the first two cycles and $20 for the next four cycles.

What happens after cycle 6 depends on what you specify for `renew_method`. There are three possible settings:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        `renew_method`
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `NO_RENEW`
      </td>

      <td>
        The link does not renew after `number_of_cycles` have passed. In the example, no more charges are incurred after cycle 6 as a result of the plan.
      </td>
    </tr>

    <tr>
      <td>
        `WITH_DISCOUNT`
      </td>

      <td>
        The link is renewed after the specified number of cycles have passed, and the discount is applied again.

        In the example, the discount is applied to cycles 1 and 2, but no discount is applied to cycles 3 through 6. After the 6th cycle, the link between the plan and the account is deleted, a new link (with a new link ID) is created, and the sequence repeats, with the same discounts applied to cycles 1 and 2. This sequence of events continues to repeat indefinitely.
      </td>
    </tr>

    <tr>
      <td>
        `WITHOUT_DISCOUNT`
      </td>

      <td>
        The link is renewed after `number_of_cycles` have passed, but the discount is not applied.

        In the example, after the 6th cycle, the link between the plan and the account is deleted and a new link is created. In this case, however, the full charge of $20 is incurred for all 6 cycles (assuming the account balance does not drop below `minimum_spend_to_charge`). The link continues to be recreated every 6 cycles with the full charge incurred for each cycle.
      </td>
    </tr>
  </tbody>
</Table>

Suppose you set `renew_method` to `WITH_DISCOUNT`. You create the plan using a request similar to this:

```curl
curl --request POST \
     --url https://sandbox.pismolabs.io/recurring-charge/v1/recurring-charge-plans \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'x-cid: 5bb05174-4e80-11ea-b77f-2e728ce88125' \
     --data '
{
  "split_transaction": true,
  "description": "Annuity {counter}",
  "secondary_description": "Discount {counter}",
  "number_of_cycles": 6,
  "first_cycles_to_discount": 2,
  "discount_percentage": 10,
  "minimum_spend_to_charge": 100,
  "renew_method": "WITH_DISCOUNT",
  "tracking_id": "3ea22692-a209-11eb-89a2-f73e179dcbc2",
  "processing_code": "99066",
  "secondary_processing_code": "99067",
  "installment_amount": 20
}
```

Notice that `minimum_spend_to_charge` is set to $100. This is the minimum amount of debt (total debits) that the account must have for charges to be incurred. Assume the account balance does not drop below this amount. With these settings, the client incurs the following charges on their statements:

| Cycle number | Installment amount | Discount | Charge |
| :----------- | :----------------- | :------- | :----- |
| 1            | $20                | $2       | $18    |
| 2            | $20                | $2       | $18    |
| 3            | $20                | $2       | $20    |
| 4            | $20                | $2       | $20    |
| 5            | $20                | $2       | $20    |
| 6            | $20                | $2       | $20    |

Since `split_transaction` is true, two transactions — a debit transaction for the base amount of the installment (the amount before the discount is applied) and a credit transaction for the discount amount — are posted to the account for cycles 1 and 2. So, for example, on the statement for cycle 1, there would be a debit transaction in the amount of $20 and a credit transaction for $2. Both transactions would appear on the statement.

Since `renew_method` is set to WITH\_DISCOUNT, the same charges repeat in the next 6 cycles and the next 6, and so on.

## Recurring charge plan example 2

Suppose you define a recurring charge plan with the same settings as in the previous example, but with `split_transaction` set to false:

* `number_of_cycles` = 6
* `installment_amount` = 20
* `first_cycles_to_discount` = 2
* `discount_percentage` = 10
* `split_transaction` = false
* `renew_method` = WITH\_DISCOUNT

You create the plan using a request similar to the following.

```curl
curl --request POST \
     --url https://sandbox.pismolabs.io/recurring-charge/v1/recurring-charge-plans \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'x-cid: 5bb05174-4e80-11ea-b77f-2e728ce88125' \
     --data '
{
  "split_transaction": false,
  "description": "Annuity {counter}",
  "number_of_cycles": 6,
  "first_cycles_to_discount": 2,
  "discount_percentage": 10,
  "minimum_spend_to_charge": 100,
  "renew_method": "WITH_DISCOUNT",
  "tracking_id": "3ea22692-a209-11eb-89a2-f73e179dcbc2",
  "processing_code": "99066",
  "installment_amount": 20
}
```

The charges incurred are the same as in the previous example, however, only one transaction is created for each installment. For cycle 1, for example, there would be one debit transaction for $18 posted to the account. The installment would also appear as one transaction on the statement.

## Recurring charge plan example 3

This example shows how to set up an annual scheduled charge. Suppose you want to charge an annual fee of $120. As explained in the [Annual recurring charge ](https://developers.pismo.io/pismo-docs/docs/recurring-charges#annual-recurring-charge)section, there are two ways to do this.

One way is to split the charge across the cycles. `number_of_cycles` = 12\
`installment_amount` = 10\
Here, you've set `installment_amount` to 1/12 of the total annual charge. That is, 120 / 12 = 10.

Another way is to set `installment_amount` to 120 and discount the first 11 cycles by 100%. This would result in no charges for the first 11 cycles and a charge of $120 in cycle 12. The JSON code for this would be as follows.

```json
{  
    "number_of_cycles": 12,  
    "installment_amount": 120,  
    "first_cycles_to_discount": 11,  
    "discount_percentage": 100,  
    "renew_method": "WITH_DISCOUNT",  
    "split_transaction": false
} 
```

<Callout icon="🚧" theme="warn">
  Be sure to set `split_transaction` = `false`.  If you set it to `true`, each discounted cycle posts two transactions (a debit amount and an offsetting credit amount). This clutters the statement for the 11 free months.
</Callout>

# Examples for scheduled charges

## Scheduled charges example 1

When you use [List scheduled charges](https://developers.pismo.io/pismo-docs/reference/list-scheduled-charges) or [Get scheduled charge](https://developers.pismo.io/pismo-docs/reference/get-scheduled-charge) to view scheduled charges, you must take into account the value of `split_transaction`. If `split_transaction` is `true`, then the `installment_amount` field returned by these endpoints has the same value that you entered when you created the plan, and the `secondary_installment_amount` field represents the value of the discount (if any) that's applied to `installment_amount`. Refer to [Recurring charge plan example 1](https://developers.pismo.io/pismo-docs/docs/recurring-charges#recurring-charge-plan-example-1).

If `split_transaction` is false, then the discount (if any) is deducted from `installment_amount` and saved back into the same field. In other words, `installment_amount` is set equal to `installment_amount` minus the discount. So, the new installment amount can be different depending on whether the charge is discounted.

The following code shows the kind of results you might get from running [List scheduled charges](https://developers.pismo.io/pismo-docs/reference/list-scheduled-charges). In this case, only one charge is listed because `per_page` is set to 1. There is a value for `secondary_installment_amount`, so the plan probably has `split_transaction` set to true, although this could have been overridden using [Update scheduled charge](https://developers.pismo.io/pismo-docs/reference/update-scheduled-charge). (Refer to the next example.)

```json
{
  "current_page": 1,
  "per_page": 1,
  "pages": 10,
  "total_items": 10,
  "is_last_page": true,
  "items": [
    {
      "recurring_scheduled_charge_id": 880077,
      "org_id": "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d",
      "account_id": 6912345,
      "created_at": "2023-03-30T12:26:41",
      "updated_at": "2022-02-01",
      "statement_id": 9497889,
      "recurring_charge_link_id": 98660282,
      "status": "PENDING",
      "creation_cid": "f7ad1742-cae5-4d59-be97-7d6127b363ea",
      "cancellation_cid": "10a30b55-53a0-4cf9-9e20-25a6ccec12dd",
      "processing_code": "99066",
      "installment_amount": 10.9,
      "description": "Annuity 1/12",
      "authorization_id": 1099901,
      "authorization_tracking_id": "fd0e5a8a-bc33-436a-8fba-0e82c7d7c12e",
      "secondary_processing_code": "99067",
      "secondary_installment_amount": 5.45,
      "secondary_description": "Discount",
      "secondary_authorization_id": 1099901,
      "secondary_authorization_tracking_id": "7ec3b2b2-8e70-4b0a-ac4d-86c6275310c2"
    }
  ]
}
```

<Callout icon="📘" theme="info">
  If you supply a value in the `description` field when you create a link, this value is used in the `description` field of all the charges, as in the previous example. If you don't provide a value for `description` in the link, the `description` field of the plan is used.

  The `secondary_description` field in the charge always gets its value from the plan.
</Callout>

## Scheduled charges example 2

When you use [Update scheduled charge](https://developers.pismo.io/pismo-docs/reference/update-scheduled-charge), it's possible to split the charge between `installment_amount` and `secondary_installment_amount`, even if `split_transaction` is false. However, to do this, you need to enter a value for `secondary_processing_code`. Otherwise, you get an error.

Suppose you have a recurring charge plan with the following settings:

* `number_of_cycles` = 6
* `installment_amount` = 20
* `first_cycles_to_discount` = 2
* `discount_percentage` = 50
* `processing_code` = "99066"
* `split_transaction` = false

The plan is applied to an account with ID 3512347. When you run [List scheduled charges](https://developers.pismo.io/pismo-docs/reference/list-scheduled-charges) on this account, the result includes the following information for one of the scheduled charges.

```json
  "items": [
    ...
    {
      "recurring_scheduled_charge_id": 450066,
      "org_id": "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d",
      "account_id": 3512347,
      "created_at": "2023-02-12T11:19:11",
      "updated_at": "2023-02-20",
      "statement_id": 9497889,
      "recurring_charge_link_id": 12560211,
      "status": "PENDING",
      "creation_cid": "22bccfdc-e282-4b33-afa4-56e9dd30783b",
      "cancellation_cid": "e55ca816-9b9a-424a-a251-9ff76b042030",
      "processing_code": "99066",
      "installment_amount": 10,
      "description": "Annuity 3/6",
      "authorization_id": 2059211,
      "authorization_tracking_id": "294f167e-dd0f-4e75-b430-8361d8ba8ebe",
    },
    ...
  ]
```

Notice that `installment_amount` is $10, which is 50% less than the value of `installment_amount` that was used to create the plan. This is because `split_transaction` is set to false. The value of `installment_amount` returned by [List scheduled charges](https://developers.pismo.io/pismo-docs/reference/list-scheduled-charges) is the discounted amount.

Now, suppose you execute the following request.

```curl
curl --request PATCH \
     --url https://sandbox.pismolabs.io/recurring-charge/v1/accounts/3512347/scheduled-charges/450066 \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <your_bearer_token>' \
     --header 'content-type: application/json' \
     --data '
{
  "installment_amount": 20,
  "processing_code": "99066",
  "description": "Annuity 3/6",
  "secondary_processing_code": "99067",
  "secondary_installment_amount": 10,
  "secondary_description": "Discount"
}
```

This request updates the scheduled charge shown in the previous code block. It changes `installment_amount` to 20 and sets `secondary_installment_amount` to 10. Since `split_transaction` is set to  false in the plan, you had to include a value for `secondary_processing_code`. Assume that "990066" and "990067" are processing codes for a debit transaction and a credit transaction, respectively. Then, the amount of the charge is 20 - 10 = $10 — the same as it was before you executed the request. You've just split the transaction for this one charge.

## Scheduled charges example 3

[Update scheduled charge](https://developers.pismo.io/pismo-docs/reference/update-scheduled-charge) can be used to settle a charge. Suppose a client asks the bank to fully discount a customer's installment for a particular cycle. To skip the installment, you execute the endpoint with `installment_amount` set to 0 and use the statement ID to specify the cycle you want to skip.

Say you have the same recurring charge plan that was used in the previous example:

* `number_of_cycles` = 6
* `installment_amount` = 20
* `first_cycles_to_discount` = 2
* `discount_percentage` = 50
* `processing_code` = "99066"
* `split_transaction` = false

The plan is applied to an account with ID 3512347. You run [List scheduled charges](https://developers.pismo.io/pismo-docs/reference/list-scheduled-charges) to find the ID for the statement that you want to skip, which turns out to be the one shown below (the same one as in the last example).

```json
  "items": [
    ...
    {
      "recurring_scheduled_charge_id": 450066,
      "org_id": "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d",
      "account_id": 3512347,
      "created_at": "2023-02-12T11:19:11",
      "updated_at": "2023-02-20",
      "statement_id": 9497889,
      "recurring_charge_link_id": 12560211,
      "status": "PENDING",
      "creation_cid": "22bccfdc-e282-4b33-afa4-56e9dd30783b",
      "cancellation_cid": "e55ca816-9b9a-424a-a251-9ff76b042030",
      "processing_code": "99066",
      "installment_amount": 10,
      "description": "Link between an account and a recurring charge plan",
      "authorization_id": 2059211,
      "authorization_tracking_id": "294f167e-dd0f-4e75-b430-8361d8ba8ebe",
    },
    ...
  ]
```

To skip the charge for this statement's cycle, you execute the following request.

```curl
curl --request PATCH \
     --url https://sandbox.pismolabs.io/recurring-charge/v1/accounts/3512347/scheduled-charges/450066 \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <your_bearer_token>' \
     --header 'content-type: application/json' \
     --data '
{
  "installment_amount": 0,
  "processing_code": "99066",
  "description": "Installment settled",
}
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/recurring-charge-plans` | `create-recurring-charge-plan` | Create recurring charge plan | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-charge-plans |
| `DELETE /v1/recurring-charge-plans/{recurring_charge_plan_id}` | `disable-recurring-charge-plan` | Disable recurring charge plan | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-charge-plans |
| `POST /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id}` | `create-recurring-charge-link` | Create link | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-charge-links |
| `DELETE /v1/recurring-charge-links/{recurring_charge_link_id}` | `delete-recurring-charge-link` | Delete recurring charge link | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-charge-links |
| `GET /v1/accounts/{account_id}/scheduled-charges` | `list-scheduled-charges` | List scheduled charges | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges |
| `GET /v1/accounts/{account_id}/scheduled-charges/{recurring_scheduled_charge_id}` | `get-scheduled-charge` | Get scheduled charge | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges |
| `PATCH /v1/accounts/{account_id}/scheduled-charges/{recurring_scheduled_charge_id}` | `update-scheduled-charge` | Update scheduled charge | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges |

### Operation essentials

- **`POST /v1/recurring-charge-plans`** (`create-recurring-charge-plan`): security `BearerAuth`; required parameters none declared; required body fields `processing_code`, `installment_amount`, `number_of_cycles`, `tracking_id`; response statuses 200, 400, 409, 500; error codes in examples none; events `balance-recurring-charge-plan-created-1`.
- **`DELETE /v1/recurring-charge-plans/{recurring_charge_plan_id}`** (`disable-recurring-charge-plan`): security `BearerAuth`; required parameters `recurring_charge_plan_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events `balance-recurring-charge-plan-disabled-1`.
- **`POST /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id}`** (`create-recurring-charge-link`): security `BearerAuth`; required parameters `recurring_charge_plan_id` (path), `account_id` (path); required body fields `tracking_id`; response statuses 200, 400, 404, 500; error codes in examples none; events `balance-recurring-charge-plan-linked-to-account-1`.
- **`DELETE /v1/recurring-charge-links/{recurring_charge_link_id}`** (`delete-recurring-charge-link`): security `BearerAuth`; required parameters `recurring_charge_link_id` (path); required body fields none declared; response statuses 200, 400, 409, 500; error codes in examples none; events `balance-recurring-charge-plan-unlinked-from-account-1`.
- **`GET /v1/accounts/{account_id}/scheduled-charges`** (`list-scheduled-charges`): security `BearerAuth`; required parameters `account_id` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples none; events none listed.
- **`GET /v1/accounts/{account_id}/scheduled-charges/{recurring_scheduled_charge_id}`** (`get-scheduled-charge`): security `BearerAuth`; required parameters `account_id` (path), `recurring_scheduled_charge_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events none listed.
- **`PATCH /v1/accounts/{account_id}/scheduled-charges/{recurring_scheduled_charge_id}`** (`update-scheduled-charge`): security `BearerAuth`; required parameters `account_id` (path), `recurring_scheduled_charge_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events `balance-recurring-scheduled-charge-updated-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `create-recurring-charge-plan` | `balance-recurring-charge-plan-created-1` |
| `disable-recurring-charge-plan` | `balance-recurring-charge-plan-disabled-1` |
| `create-recurring-charge-link` | `balance-recurring-charge-plan-linked-to-account-1` |
| `delete-recurring-charge-link` | `balance-recurring-charge-plan-unlinked-from-account-1` |
| `update-scheduled-charge` | `balance-recurring-scheduled-charge-updated-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/recurring-charges.md`: updatedAt 2026-09-18T16:33:45.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/recurring-charges.md` | whole document | https://developers.pismo.io/pismo-docs/docs/recurring-charges | `7a047e09b188efc4…` | 2026-09-18T16:33:45.000Z |

## Related knowledge units

- `KU-API-revolving-credit-recurring-charges--recurring-charge-links` — API reference: Revolving credit - Recurring charges — Recurring charge links
- `KU-API-revolving-credit-recurring-charges--recurring-charge-plans` — API reference: Revolving credit - Recurring charges — Recurring charge plans
- `KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges` — API reference: Revolving credit - Recurring charges — Recurring scheduled charges
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-GS-setup-overview` — Core objects
