---
ku_id: KU-CRED-configuring-a-sellos-tax
title: Configuring a sellos tax
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/configuring-a-sellos-tax.md
  sha256: cce7a7b50defb9feaf5d237285f16beca66e8a5a11b0c16926cda6b4ef9ffbfe
  url: https://developers.pismo.io/pismo-docs/docs/configuring-a-sellos-tax
  role: primary_guide
  updated_at: '2026-03-18T15:22:27.000Z'
operations:
- createTransactionCategory
- getTransactionTypes_1
- postAccountAccrualTypesRates
- postAccrualTypeMinimumValue
- postAccrualTypesRates
related_kus:
- KU-API-revolving-credit-configurations--account-accrual-rates
- KU-API-revolving-credit-configurations--program-accrual-rates
- KU-API-revolving-credit-interest-accruals--accrual-types-minimum-value
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-API-revolving-credit-statements--transaction-types
- KU-CC-get-started-control-center
- KU-CRED-configuring-accrual-rates
grouping_rationale: single source page
---

# Configuring a sellos tax

**KU ID:** `KU-CRED-configuring-a-sellos-tax` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/configuring-a-sellos-tax.md`:

> A sellos tax is a type of local government tax that's charged on an unpaid balance after the due date.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/configuring-a-sellos-tax.md`: Configuring a sellos tax; Setting the  minimum amount for a sellos tax

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/configuring-a-sellos-tax.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/configuring-a-sellos-tax · updatedAt: 2026-03-18T15:22:27.000Z

<!-- source:begin path=docs/card-issuing/configuring-a-sellos-tax.md part=0-end -->

# Configuring a sellos tax

A sellos tax is a type of local government tax that's charged on an unpaid balance after the due date.

There are two options for creating a sellos tax.

* The first option is to create a new accrual type for the tax. To do this, open a service request for the Pismo team to configure the new accrual type for your program. The service request just needs to include the name for the accrual type (`SELLOS_TAX` for example).
* The second option is to use the existing `FINANCIAL_TAX`  accrual type for the sellos tax.

Whichever option you choose, once you have the accrual type that you’re going to use, you need to configure an **accrual type rate** for it. To do this, associate the accrual type with a transaction category to configure the rate at the program level. If you need to create a new transaction category for this, use the [Create transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory) endpoint. The ID of the new category is returned in the `id` field of the response. If you want to use an existing transaction category, use the [List program transaction types](https://developers.pismo.io/pismo-docs/reference/gettransactiontypes_1) endpoint to find its ID. Once you have the ID for the transaction category, apply the accrual type rate using the [Configure program interest rates](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesrates) endpoint.

Optionally, you can also configure the rate at the account level by associating it with an account transaction category. To do this, first configure the rate at the program level, using the above steps, then use the [Configure account interest rates](https://developers.pismo.io/pismo-docs/reference/postaccountaccrualtypesrates) endpoint to configure it at the account level.

For more information, refer to [Configuring accrual rates](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates).

# Setting the  minimum amount for a sellos tax

Depending on the rules in your jurisdiction, you might also need to set a minimum amount for the sellos tax. Then, when the Pismo platform calculates the tax for an overdue balance, it compares the result to this minimum value and uses whichever amount is greater.

To set a minimum amount for a sellos tax, use the [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) to set the **Enables minimum value rule for posting accruals at the closing cycle moment** program parameter to `true`. Then use the [Configure minimum value by accrual type](https://developers.pismo.io/pismo-docs/reference/postaccrualtypeminimumvalue) endpoint to configure the minimum value.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /statements-v2/v1/transactions-categories` | `createTransactionCategory` | Create program transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `GET /statements-v2/v1/programs-transactions-types` | `getTransactionTypes_1` | List program transaction types | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--transaction-types |
| `POST /v1/programs/{programId}/accrual-type-rates` | `postAccrualTypesRates` | Configure program accrual rates | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-accrual-rates |
| `POST /v1/accounts/{accountId}/accrual-type-rates` | `postAccountAccrualTypesRates` | Configure account accrual rates | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--account-accrual-rates |
| `POST /v1/accrual-type-minimum-value` | `postAccrualTypeMinimumValue` | Configure minimum value by accrual type | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--accrual-types-minimum-value |

### Operation essentials

- **`POST /statements-v2/v1/transactions-categories`** (`createTransactionCategory`): security `BearerAuth`; required parameters `Authorization` (header), `program-id` (header); required body fields `default_rate`, `fine_rate`, `minimum_value`, `overdue_rate_after_due_date`, `refinancing_rate_after_due_date`; response statuses 201, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`GET /statements-v2/v1/programs-transactions-types`** (`getTransactionTypes_1`): security `BearerAuth`; required parameters `program-id` (header); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`POST /v1/programs/{programId}/accrual-type-rates`** (`postAccrualTypesRates`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 200, 400, 409, 500; error codes in examples `EX0001`; events none listed.
- **`POST /v1/accounts/{accountId}/accrual-type-rates`** (`postAccountAccrualTypesRates`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 409, 500; error codes in examples `EX0001`; events none listed.
- **`POST /v1/accrual-type-minimum-value`** (`postAccrualTypeMinimumValue`): security `BearerAuth`; required parameters none declared; required body fields `accrual_type`, `hierarchy_name`, `hierarchy_value`, `minimum_amount_to_post`; response statuses 201, 400, 500; error codes in examples `EX0001`, `GN0001`; events none listed.

## Lifecycle status

- `docs/card-issuing/configuring-a-sellos-tax.md`: updatedAt 2026-03-18T15:22:27.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/configuring-a-sellos-tax.md` | whole document | https://developers.pismo.io/pismo-docs/docs/configuring-a-sellos-tax | `cce7a7b50defb9fe…` | 2026-03-18T15:22:27.000Z |

## Related knowledge units

- `KU-API-revolving-credit-configurations--account-accrual-rates` — API reference: Revolving credit - Configurations — Account accrual rates
- `KU-API-revolving-credit-configurations--program-accrual-rates` — API reference: Revolving credit - Configurations — Program accrual rates
- `KU-API-revolving-credit-interest-accruals--accrual-types-minimum-value` — API reference: Revolving credit - Interest accruals — Accrual types minimum value
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-API-revolving-credit-statements--transaction-types` — API reference: Revolving credit - Statements — Transaction types
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CRED-configuring-accrual-rates` — Configuring accrual rates
