---
ku_id: KU-CRED-configuring-accrual-rates
title: Configuring accrual rates
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/configuring-accrual-rates.md
  sha256: dd388b656f5dc5376f64011e575fe058baabddbe605e44997095d4f6e9d3619d
  url: https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates
  role: primary_guide
  updated_at: '2026-08-31T16:10:45.000Z'
operations:
- createProgramParameter
- createProgramTransactionType
- postAccountAccrualTypesRates
- postAccrualTypesRates
- saveAccountTransactionInterest
- updateProgramParameter
related_kus:
- KU-API-platform-setup-programs--parameters
- KU-API-revolving-credit-configurations--account-accrual-rates
- KU-API-revolving-credit-configurations--program-accrual-rates
- KU-API-revolving-credit-configurations--program-transaction-types
- KU-API-revolving-credit-statements--account-transaction-categories
- KU-BANK-how-overdraft-works
- KU-CARD-transaction-categories
- KU-CC-get-started-control-center
- KU-CORE-program-parameters-reference-table
- KU-CRED-accrual-rate-types-and-limits
- KU-CRED-minimum-amount-due-calculation
- KU-CRED-understanding-statements
grouping_rationale: single source page
---

# Configuring accrual rates

**KU ID:** `KU-CRED-configuring-accrual-rates` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/configuring-accrual-rates.md`:

> An account can accrue various charges over the course of a [credit cycle](https://developers.pismo.io/pismo-docs/docs/understanding-statements#credit-card-cycles-billing-periods). For example, if an account has an unpaid balance at the end of the cycle, the Pismo platform might apply a refinancing charge to the account for every day the balance remains unpaid. The account might accrue other charges during the cycle, such as interest on a withdrawal.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/configuring-accrual-rates.md`: Configuring accrual rates; Refinancing accrual type rates; Overdue accrual type rates; Late payment fees; How to configure accrual types; Validation for configuring accruals; Changing the interest rate period; Examples; Example 1: Configuring refinancing and overdue accrual types at the program level; Example 2: Configuring refinancing and overdue accrual types at the account level; Example 3: Configuring a withdrawal interest accrual type at the account level

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/configuring-accrual-rates.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates · updatedAt: 2026-08-31T16:10:45.000Z

<!-- source:begin path=docs/card-issuing/configuring-accrual-rates.md part=0-end -->

# Configuring accrual rates

An account can accrue various charges over the course of a [credit cycle](https://developers.pismo.io/pismo-docs/docs/understanding-statements#credit-card-cycles-billing-periods). For example, if an account has an unpaid balance at the end of the cycle, the Pismo platform might apply a refinancing charge to the account for every day the balance remains unpaid. The account might accrue other charges during the cycle, such as interest on a withdrawal.

An **accrual rate**, which is usually a percentage, determines the charge amount. The Pismo platform uses entities called **accrual types** to configure accrual rates. Accrual types include:

* [Refinancing](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates#refinancing-accrual-type-rates)—A daily charge applied to an unpaid balance if the account holder has not paid the total amount due
* [Overdue](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates#overdue-accrual-type-rates)—A daily charge applied to an unpaid balance if the account holder has not paid the [minimum amount due (MAD)](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation)
* **Withdrawal interest**—Interest charged on a withdrawal
* **Bill payment interest**—Interest charged on a bill payment
* **Overdraft interest**—Interest charged on an [overdraft](https://developers.pismo.io/pismo-docs/docs/how-overdraft-works)
* **Financial tax**—A tax required by a particular country or region
* **Fine**—A one-time charge that the Pismo platform applies on the day an account becomes overdue
* [Late payment fee](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates#late-payment-fees)—A fixed amount that the Pismo platform charges once per cycle whenever there are any overdue transactions. You configure this at the program level.

By default, accrual rates that are defined as percentages are monthly percentages. For example, if you set the refinancing accrual rate to 2, this means the account accrues 2% of the unpaid balance per month. You can change the interest rate period using a program parameter. For more information, refer to [Changing the interest rate period](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates#changing-the-interest-rate-period).

<Callout icon="📘" theme="info">
  **IOF rates** (Brazil only)—You can use program parameters to set various rates for IOF taxes at the program level. For more information, refer to [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table).
</Callout>

# Refinancing accrual type rates

Refinancing accrual type rates only apply if the cardholder doesn’t pay the total amount due. Transaction categories and account transaction categories both contain the following fields for specifying refinancing accrual type rates.

* `refinancing_rate_after_due_date`—Revolving rate as a percentage if the account is *not* overdue (that is, the cardholder has paid the MAD). The Pismo platform charges this accrual daily until the balance is zero (that is, until the TAD is paid). Example: 14.99 = 14.99%.
* `overdue_rate_after_due_date`—Revolving rate as a percentage if the cardholder *is* overdue (that is, the cardholder has *not* paid the MAD). The Pismo platform charges this accrual daily until you pay the MAD. If there is still an unpaid balance (that is, the TAD has not been met) after you've paid the MAD, the platform begins to use `refinancing_rate_after_due_date`. Example: 15.99 = 15.99%.

# Overdue accrual type rates

Overdue accrual type rates only apply if the cardholder doesn't pay the minimum amount due. Program transaction categories and account transaction categories both contain the following fields for specifying an overdue accrual type rate.

* `default_rate`—Overdue rate as a percentage. The Pismo platform charges this daily until you pay the MAD. Example: 1 = 1%.
* `fine_rate`—The rate for a fine that the Pismo platform charges on the day a transaction becomes overdue. The platform changes this only on the first overdue day for each transaction. The rate is a percentage. Example: 2 = 2%.

# Late payment fees

Some markets might require you to charge the cardholder a fixed amount for an overdue account, regardless of how many transactions are overdue or their balances. For example, the charge could be $20 at the end of a credit cycle if any transactions are overdue.

To set a late payment fee, use [Create program parameter](https://developers.pismo.io/pismo-docs/reference/createprogramparameter) or [Update program parameter](https://developers.pismo.io/pismo-docs/reference/updateprogramparameter) to set the `LATE_PAYMENT_FEE` program parameter. Once you set this parameter, if an account has overdue transactions at the end of a credit cycle, the Pismo platform creates a debit transaction on the account for the amount of the fixed fee.

The late payment fee is not linked to any particular transaction category. Any overdue balance for the program triggers it.

<Callout icon="🚧" theme="warn">
  Note that if you configure both the fine rate for a transaction category and a late payment fee, the account could accrue two late fees for the same overdue transaction.
</Callout>

# How to configure accrual types

Configure most accrual types using the following structures.

* [Transaction categories](https://developers.pismo.io/pismo-docs/docs/transaction-category-structure)—Configure rates for the following accrual types. The Pismo platform applies the rates starting on the day after the statement due date. Use this structure to configure accrual types at the program or account level.
  * Refinancing
  * Overdue
* [Accrual type rates](https://developers.pismo.io/pismo-docs/docs/accrual-type-rate-structures)—Extends transaction categories with rate structures that provide more flexibility. Use this structure to configure the following accrual types at either the program or account level.
  * Withdrawal interest
  * Bill payment interest
  * Overdraft interest
  * Financial tax

# Validation for configuring accruals

By default, when you update an accrual rate, the Pismo platform starts applying the new rate immediately. In some cases, you might want the platform to wait until the next cycle due date to start applying the new rate. To do this, use [Configure program accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesrates) or [Configure account accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccountaccrualtypesrates) to set the `validity-to-calculate` field to `DUE_DATE` (at the program or account level, respectively).

For example, suppose you use [Configure program accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesrates) to set `default_rate` to 2% for accruals of type `REFINANCING` for some program transaction category, and you set `validity_to_calculate` to `IMMEDIATE`. This creates a new [accrual type rate](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates). Later, you use the same endpoint to set `default_rate` to 3% for `REFINANCING` accruals for the same transaction category, but this time, you set `validity_to_calculate` to `DUE_DATE`. This creates another new accrual type rate.

Now, suppose the platform generates a transaction in this category for a `REFINANCING` accrual. If it generates the transaction before the due date, it uses the 2% rate from the first accrual type rate that you created. If it generates it after the due date, it uses the 3% rate from the second accrual type rate.

<Callout icon="📘" theme="info">
  Note that this example only works if you set the rate at the program level using [Configure program accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesrates). To set a rate at the account level, you need to use [Configure account accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccountaccrualtypesrates). This endpoint only has options for configuring `WITHDRAWAL_INTEREST`, `BILLPAYMENT_INTEREST`, and `OVERDRAFT_INTEREST`. It's possible to set `REFINANCING`, `OVERDUE` and `FINE` using the accrual type rate structure (which would enable you to set  `validity-to-calculate` to `DUE_DATE` for them). To do this, open a service request.
</Callout>

# Changing the interest rate period

By default, accrual rates are monthly rates. For example, if you set the refinancing rate to 10, you’re setting the rate  to 10% per month, where 'month' refers to a business month, which is 30 days. On the other hand, if you want to use annual rates, you should set the interest rate period to 365 days (a calendar year). To do this, use the [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) to set the program parameter **Interest rate period** to 365.

No matter how you set the period, the Pismo platform converts the rates into daily rates to apply them. The platform divides each configured rate by **Interest rate period** to get the corresponding daily rate.

<Callout icon="🚧" theme="warn">
  IMPORTANT: When you change **Interest rate period**, it changes the accrual calculations for ALL interest rates in the program (except `fine_rate`, which is not affected by **Interest rate period**). If you already have existing rates operating, **you must change them within the same day to avoid financial issues**. To find the new value for an existing rate when changing **Interest rate period**, use the following formula.

  New value for existing rate = New **Interest rate period** / old **Interest rate period** x old value of existing rate

  Here's an example of changing an existing monthly rate (**Interest rate period** = 30) to an annual rate.\
  New **Interest rate period**: 365\
  Existing rate (monthly): 15%\
  New value for existing rate (annual) = New **Interest rate period** / old **Interest rate period** x old value of existing rate = 365/30 x 15% = 182.5%
</Callout>

For example, to use annual rates based on a calendar year, you would configure the rates in the usual way, providing the nominal interest rates for one year. Then, you would set **Interest rate period** to 365. The following code sample shows a sample payload for configuring annual rates by program.

```curl
curl --request POST \
--url https://api-sandbox.pismolabs.io/statements-v2/v1/transactions-categories \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--header 'x-program-id: 1122' \
--data '
{
"default_rate": 178,
"fine_rate": 2,
"overdue_rate_after_due_date": 178,
"refinancing_rate_after_due_date": 178,
"description": "purchase",
"charge_order": 2,
"secondary_charge_order": 7
}
```

In the sample, the value for `default_rate` is 178, meaning a 178% annual accrual rate. The platform divides 178 by 365 to get a corresponding daily rate of 0.48767123%. (The Pismo platform rounds the result to 8 decimal places.) The platform performs the same calculation to get the daily rates for `overdue_rate_after_due_date` and `refinancing_rate_after_due_date`.

<Callout icon="🚧" theme="warn">
  Note that the value for `fine_rate` in the sample code is only 2%. Because the platform applies `fine_rate` only once on the first day the account becomes overdue, it ignores **Interest rate period** and treats `fine_rate` as a monthly rate.
</Callout>

<Callout icon="📘" theme="info">
  Changing **Interest rate period** affects all accrual rates at both program and account level (except for `fine_rate`, as noted above.)
</Callout>

# Examples

## Example 1: Configuring refinancing and overdue accrual types at the program level

The following steps demonstrate how to configure rates for refinancing and overdue accrual types at the program level.

**Step 1:** Create a debit transaction type:

```curl
curl --request POST \
     --url https://api-sandbox.pismolabs.io/transactions-core/v1/transaction-types \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <your_bearer_token>' \
     --header 'content-type: application/json' \
     --data '
{
  "credit": false,
  "posted_transaction": true,
  "transaction_type_id": 101,
  "description": "Purchase"
}
'
```

**Step 2:** Create a program transaction category. Note that the program ID is passed as a header. This must be the program that the account is in.

```curl
curl --request POST \
     --url https://api-sandbox.pismolabs.io/statements-v2/v1/transactions-categories \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <your_bearer_token>' \
     --header 'content-type: application/json' \
     --header 'x-program-id: 5689' \
     --data '
{
  "description": "Rate settings",
  "refinancing_rate_after_due_date": 15.99,
  "default_rate": 1.99,
  "fine_rate": 2.95,
  "overdue_rate_after_due_date": 17.99,
  "minimum_value": 1,
  "charge_order": 2
}
'
```

If successful, the request returns a program transaction category ID. Assume the ID is 1237456.

**Step 3:** Use the [Create program transaction type](https://developers.pismo.io/pismo-docs/reference/createprogramtransactiontype) endpoint to create a program transaction type linking the category to the transaction type. This time, the program ID is passed as a path parameter. Creating this link results in the rates defined in the program transaction category being applied to any transactions that have the specified transaction type.

```curl
curl --request POST \
     --url https://sandbox.pismolabs.io/credit-cycle-configurations/v1/programs/5689/program-transaction-types \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <your_bearer_token>' \
     --header 'content-type: application/json' \
     --data '
{
  "transaction_type_id": 101,
  "transaction_category_id": 1237456,
  "charge_order": 2
}
'
```

## Example 2: Configuring refinancing and overdue accrual types at the account level

The following steps demonstrate how to configure rates for refinancing and overdue accrual types at the account level.

**Steps 1 and 2:** The same as steps 1 and 2 in Example 1.

**Step 3:** Use the [Create or update account transaction category](https://developers.pismo.io/pismo-docs/reference/saveaccounttransactioninterest)  endpoint to create an account transaction category for the account. You set the rates for the new category in the same request.

```curl
curl --request POST \
     --url https://api-sandbox.pismolabs.io/statements-v2/v1/accounts/129006785/accounts-transactions-categories \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <your_bearer_token>' \
     --header 'content-type: application/json'
     --data '
{
  "description": "purchase",
  "refinancing_rate_after_due_date": 15.99,
  "default_rate": 1,
  "fine_rate": 2,
  "overdue_rate_after_due_date": 17.99,
  "refinancing_rate_after_due_date_multiplier_percent": 1.5,
  "default_rate_multiplier_percent": 1.7,
  "fine_rate_multiplier_percent": 2,
  "overdue_rate_after_due_date_multiplier_percent": 0.7,
  "start_cycle": 4,
  "start_date": "2021-08-20"
}
'
```

These rates override the rates in the program transaction category.

## Example 3: Configuring a withdrawal interest accrual type at the account level

The following steps demonstrate how to configure a withdrawal interest accrual type at the account level.

**Step 1:** Create a debit transaction type for a withdrawal:

```curl
curl --request POST \
     --url https://api-sandbox.pismolabs.io/transactions-core/v1/transaction-types \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <your_bearer_token>' \
     --header 'content-type: application/json' \
     --data '
{
  "credit": false,
  "posted_transaction": true,
  "transaction_type_id": 102,
  "description": "Withdrawal"
}
'
```

**Step 2:** Create a program transaction category. Note that you pass the program ID as a header. This must be the program that the account is in.

```curl
curl --request POST \
     --url https://api-sandbox.pismolabs.io/statements-v2/v1/transactions-categories \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <your_bearer_token>' \
     --header 'content-type: application/json' \
     --header 'x-program-id: 5689' \
     --data '
{
  "description": "Rate settings",
  "refinancing_rate_after_due_date": 15.99,
  "default_rate": 1.99,
  "fine_rate": 2.95,
  "overdue_rate_after_due_date": 17.99,
  "minimum_value": 1,
  "charge_order": 2
}
'
```

If successful, the request returns a program transaction category ID. Assume the ID is 1237456.

**Step 3:** Open a service request to create an accrual type rate. In the service request, provide the program ID and the program transaction category ID from step 2.

**Step 4:** Use the [Configure account accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccountaccrualtypesrates) endpoint to create an account accrual type rate. This entity must link to the program transaction category created in Step 2, so you should pass the ID for that category in `transaction_category_id`.

```curl
curl --request POST \
--url https://api-sandbox.pismolabs.io/statements-v2/v1/accounts/129006785/accrual-types-rates \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <your_bearer_token>' \
     --header 'content-type: application/json' \
     --header 'x-program-id: 1122' \
     --data '
{
  "transaction_category_id": 1237456,
  "accrual_type": "WITHDRAWAL_INTEREST",
  "period_to_calculate": "UNTIL_DUE_DATE",
  "default_rate": 2.99,
  "rate_if_overdue": 18.5,
  "validity_to_calculate": "IMMEDIATE"
}
'
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /programs/v1/programs/{program_id}/parameters` | `createProgramParameter` | Link optional parameter to program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `PUT /programs/v1/programs/{program_id}/parameters/{program_parameter_id}` | `updateProgramParameter` | Update program parameter | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `POST /v1/programs/{programId}/accrual-type-rates` | `postAccrualTypesRates` | Configure program accrual rates | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-accrual-rates |
| `POST /v1/accounts/{accountId}/accrual-type-rates` | `postAccountAccrualTypesRates` | Configure account accrual rates | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--account-accrual-rates |
| `POST /v1/programs/{programId}/program-transaction-types` | `createProgramTransactionType` | Create program transaction type | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-transaction-types |
| `POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` | `saveAccountTransactionInterest` | Create or update account transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |

### Operation essentials

- **`POST /programs/v1/programs/{program_id}/parameters`** (`createProgramParameter`): security `S2SAuthentication`; required parameters `program_id` (path); required body fields `parameter_name`; response statuses 201, 400; error codes in examples none; events none listed.
- **`PUT /programs/v1/programs/{program_id}/parameters/{program_parameter_id}`** (`updateProgramParameter`): security `S2SAuthentication`; required parameters `program_id` (path), `program_parameter_id` (path); required body fields `value`; response statuses 200, 400; error codes in examples none; events none listed.
- **`POST /v1/programs/{programId}/accrual-type-rates`** (`postAccrualTypesRates`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 200, 400, 409, 500; error codes in examples `EX0001`; events none listed.
- **`POST /v1/accounts/{accountId}/accrual-type-rates`** (`postAccountAccrualTypesRates`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 409, 500; error codes in examples `EX0001`; events none listed.
- **`POST /v1/programs/{programId}/program-transaction-types`** (`createProgramTransactionType`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 201, 400, 404, 500; error codes in examples `EX0001`, `EX0002`; events none listed.
- **`POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories`** (`saveAccountTransactionInterest`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `transaction_category_id`; response statuses 201, 400, 423, 500; error codes in examples `EX0002`, `GN0001`; events none listed.

## Lifecycle status

- `docs/card-issuing/configuring-accrual-rates.md`: updatedAt 2026-08-31T16:10:45.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/configuring-accrual-rates.md` | whole document | https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates | `dd388b656f5dc537…` | 2026-08-31T16:10:45.000Z |

## Related knowledge units

- `KU-API-platform-setup-programs--parameters` — API reference: Platform setup - Programs — Parameters
- `KU-API-revolving-credit-configurations--account-accrual-rates` — API reference: Revolving credit - Configurations — Account accrual rates
- `KU-API-revolving-credit-configurations--program-accrual-rates` — API reference: Revolving credit - Configurations — Program accrual rates
- `KU-API-revolving-credit-configurations--program-transaction-types` — API reference: Revolving credit - Configurations — Program transaction types
- `KU-API-revolving-credit-statements--account-transaction-categories` — API reference: Revolving credit - Statements — Account transaction categories
- `KU-BANK-how-overdraft-works` — How overdraft works
- `KU-CARD-transaction-categories` — Transaction categories
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-CRED-accrual-rate-types-and-limits` — Accrual rate types, accrual-free transaction types and accrual-day limits
- `KU-CRED-minimum-amount-due-calculation` — Minimum amount due calculation
- `KU-CRED-understanding-statements` — Understanding statements
