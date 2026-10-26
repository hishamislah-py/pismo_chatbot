---
ku_id: KU-CRED-accrual-rate-types-and-limits
title: Accrual rate types, accrual-free transaction types and accrual-day limits
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/accrual-type-rate-structures.md
  sha256: 28881e778a4117f07a338636730b77f8e968086108c107f8e3bee537c4e31916
  url: https://developers.pismo.io/pismo-docs/docs/accrual-type-rate-structures
  role: primary_guide
  updated_at: '2026-05-11T19:40:52.000Z'
- path: docs/card-issuing/configuring-transaction-types-to-not-accrue-charges.md
  sha256: e73bd765bcf648fb172f260a119b8414744081ad6b93024f17ae20a206378700
  url: https://developers.pismo.io/pismo-docs/docs/configuring-transaction-types-to-not-accrue-charges
  role: primary_guide
  updated_at: '2026-03-18T15:22:23.000Z'
- path: docs/card-issuing/limiting-the-number-of-days-accruals-can-be-charged.md
  sha256: 668df6b8ef8184954b764e9485feb7125165c0089b28d14f4fa7a7ed742a2aeb
  url: https://developers.pismo.io/pismo-docs/docs/limiting-the-number-of-days-accruals-can-be-charged
  role: primary_guide
  updated_at: '2026-03-18T15:22:24.000Z'
operations:
- deleteAccountAccrualTypesRate
- deleteProgramParamenter
- getAccountsTransactionsInterest
- getProgramParameter
- listAccountAccrualTypeRates
- postAccountAccrualTypesRates
- postAccrualTypesRates
- postInterestAccruals
- updateProgramParamenter
related_kus:
- KU-API-revolving-credit-configurations--account-accrual-rates
- KU-API-revolving-credit-configurations--program-accrual-rates
- KU-API-revolving-credit-interest-accruals--post-interest-accruals
- KU-API-revolving-credit-statements--accruals
- KU-API-revolving-credit-statements--multivalue-program-parameters
- KU-CC-get-started-control-center
- KU-CRED-calculating-interest-accruals
- KU-CRED-configuring-accrual-rates
- KU-EVT-catalogue-transaction
- KU-GS-setup-overview
grouping_rationale: Short accrual-configuration pages.
---

# Accrual rate types, accrual-free transaction types and accrual-day limits

**KU ID:** `KU-CRED-accrual-rate-types-and-limits` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Short accrual-configuration pages.

Scope as stated in `docs/card-issuing/accrual-type-rate-structures.md`:

> Use can you Accrual type rates to configure additional accrual rates that aren't available with transaction categories. Configure the following accrual types using the accrual type rate structure.

Scope as stated in `docs/card-issuing/configuring-transaction-types-to-not-accrue-charges.md`:

> You can specify that certain transaction types block accruals if they are the only transaction types on the cardholder’s statement. This helps to reduce delinquency, since if these types of transactions are the only transactions at the end of the cycle, no value for the account's [open\_due\_date](https://developers.pismo.io/pismo-docs/docs/setup-overview#account)  field is set, and the account as a whole does not accrue charges.

Scope as stated in `docs/card-issuing/limiting-the-number-of-days-accruals-can-be-charged.md`:

> Some countries have rules that limit how many days you can charge accruals on a credit card account after it becomes overdue. To set up such a limit, use the [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) to set the  **Stop accrual # of days** program parameter. For more information, refer to [Additional program parameters for interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals#additional-program-parameters-for-interest-accruals).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/accrual-type-rate-structures.md`: Accrual type rates; Configuring accrual types at the program level; Configuring and managing accrual types at the account level
- `docs/card-issuing/configuring-transaction-types-to-not-accrue-charges.md`: Setting transaction types to block accrual charges
- `docs/card-issuing/limiting-the-number-of-days-accruals-can-be-charged.md`: Limiting the number of days accruals can be charged; Related topics

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 9 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/accrual-type-rate-structures.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accrual-type-rate-structures · updatedAt: 2026-05-11T19:40:52.000Z

<!-- source:begin path=docs/card-issuing/accrual-type-rate-structures.md part=0-end -->

# Accrual type rates

Use can you Accrual type rates to configure additional accrual rates that aren't available with transaction categories. Configure the following accrual types using the accrual type rate structure.

* Withdrawal interest
* Bill payment interest
* Overdraft interest
* Financial tax

You can configure these accruals so that the Pismo platform applies them either before or after the due date, and you can configure them at either the program or account level.

## Configuring accrual types at the program level

Use the [Configure program accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesrates) endpoint to configure accrual types at the program level. The following code sample shows an example payload for configuring annual rates at the program level.

```curl
curl --request POST  
     --url <https://sandbox.pismolabs.io/credit-cycle-configurations/v1/programs/5689/accrual-type-rates>  
     --header 'accept: application/json'  
     --header 'authorization: Bearer <your_bearer_token>'  
     --header 'content-type: application/json'  
     --data '  
{  
  "accrual_type": "WITHDRAWAL_INTEREST",  
  "period_to_calculate": "UNTIL_DUE_DATE",  
  "validity_to_calculate": "IMMEDIATE",  
  "transaction_category_id": 1237456,  
  "default_rate": 2,  
  "rate_if_overdue": 3  
}
```

## Configuring and managing accrual types at the account level

To configure accrual types at the account level:

1. First configure them at the program level.
2. Use the [Configure account accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccountaccrualtypesrates) endpoint to configure the accrual type at the account level, passing an account ID and program transaction category ID as parameters.

<Callout icon="📘" theme="info">
  You can't create an account accrual type rate without first creating the corresponding program accrual type rate. Even though you don't pass in the ID of the program accrual type rate when you create an account accrual type rate, the Pismo platform is able to use the `transaction_category_id`, `accrual_type` and `period_to_calculate` fields to determine which of the program rates to override with the account-specific rate.
</Callout>

Use the following endpoints to list and delete account accrual type rates.

* [List account accrual type rates](https://developers.pismo.io/pismo-docs/reference/listaccountaccrualtyperates)
* [Delete account accrual type rate](https://developers.pismo.io/pismo-docs/reference/deleteaccountaccrualtypesrate)
<!-- source:end -->

### Source 2: `docs/card-issuing/configuring-transaction-types-to-not-accrue-charges.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/configuring-transaction-types-to-not-accrue-charges · updatedAt: 2026-03-18T15:22:23.000Z

<!-- source:begin path=docs/card-issuing/configuring-transaction-types-to-not-accrue-charges.md part=0-end -->

# Setting transaction types to block accrual charges

You can specify that certain transaction types block accruals if they are the only transaction types on the cardholder’s statement. This helps to reduce delinquency, since if these types of transactions are the only transactions at the end of the cycle, no value for the account's [open\_due\_date](https://developers.pismo.io/pismo-docs/docs/setup-overview#account)  field is set, and the account as a whole does not accrue charges.

> 📘
>
> An account also does not accrue charges if the unpaid balance is less than the minimum amount defined for the program. See [Calculating interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals) for more information.

Use the program parameter `IGNORE_ACCRUALS_IF_ONLY_TTS` to specify which transactions should not accrue charges if they are the only transactions on the statement. This parameter takes an array of their transaction type IDs.You set this with the [Update multivalue program parameter values](https://developers.pismo.io/pismo-docs/reference/updateprogramparamenter) endpoint. Look up the parameter ID for `IGNORE_ACCRUALS_IF_ONLY_TTS` in the [Multivalue program parameters guide,](https://developers.pismo.io/pismo-docs/docs/multivalue-parameters) Set `parameterID` to this value, and use the`values` field to set the transaction type IDs.

For example, suppose the parameter ID of the annuity transaction type is 5, and you set `IGNORE_ACCRUALS_IF_ONLY_TTS` to an array containing only the number 5. Then, if only annuity transactions exist at the end of a cycle, the account is marked to not calculate accruals on the next cycle. However, if any other type of transaction is posted on the statement, then charges do accrue, even on the annuity transactions.

Use the following endpoints to retrieve a list of the configured transaction types or to delete the list, respectively:

* [Get program parameter values](https://developers.pismo.io/pismo-docs/reference/getprogramparameter)
* [Delete program parameter values](https://developers.pismo.io/pismo-docs/reference/deleteprogramparamenter)
<!-- source:end -->

### Source 3: `docs/card-issuing/limiting-the-number-of-days-accruals-can-be-charged.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/limiting-the-number-of-days-accruals-can-be-charged · updatedAt: 2026-03-18T15:22:24.000Z

<!-- source:begin path=docs/card-issuing/limiting-the-number-of-days-accruals-can-be-charged.md part=0-end -->

# Limiting the number of days accruals can be charged

Some countries have rules that limit how many days you can charge accruals on a credit card account after it becomes overdue. To set up such a limit, use the [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) to set the  **Stop accrual # of days** program parameter. For more information, refer to [Additional program parameters for interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals#additional-program-parameters-for-interest-accruals).

Once an account has been overdue for more days than the value defined in **Stop accrual # of days**, the Pismo platform sets the status of any new accruals to `STOP_ACCRUAL`. The platform does not post accruals with this status during the cycle closing process.

Note that the platform still calculates the new accruals, it just doesn't post them. If you later decide that you want to post the accruals, you can do so using the [Post interest accruals](https://developers.pismo.io/pismo-docs/reference/postinterestaccruals) endpoint.

> 📘 Notes
>
> * You can also post an accrual by using the [Update interest accrual statuses](https://developers.pismo.io/pismo-docs/reference/getaccountstransactionsinterest) endpoint to change its status to `PENDING`. However, this only works if the accrual was created in the current cycle. If you change the status of an older accrual to `PENDING`, the Pismo platform does not post it. Instead, the accrual becomes "lost" in the sense that it becomes very difficult to locate using the API. For this reason, Pismo recommends that you use the [Post interest accruals](https://developers.pismo.io/pismo-docs/reference/postinterestaccruals) endpoint whenever you need to manually post an accrual.
> * Reaching the `STOP_ACCRUAL` limit does not automatically advance future installments onto the current statement. You can implement this behavior using the API. Work with your Pismo representative if you have questions.

# Related topics

[Configuring accrual rates](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/programs/{programId}/accrual-type-rates` | `postAccrualTypesRates` | Configure program accrual rates | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-accrual-rates |
| `POST /v1/accounts/{accountId}/accrual-type-rates` | `postAccountAccrualTypesRates` | Configure account accrual rates | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--account-accrual-rates |
| `GET /v1/accounts/{accountId}/accrual-type-rates` | `listAccountAccrualTypeRates` | List account accrual rates | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--account-accrual-rates |
| `DELETE /v1/accounts/{accountId}/accrual-type-rates` | `deleteAccountAccrualTypesRate` | Delete account accrual rates | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--account-accrual-rates |
| `PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}` | `updateProgramParamenter` | Update multivalue program parameter values | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--multivalue-program-parameters |
| `GET /statements-v2/v1/programs/{programId}/parameters/{parameterId}` | `getProgramParameter` | List multivalue program parameter values | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--multivalue-program-parameters |
| `DELETE /statements-v2/v1/programs/{programId}/parameters/{parameterId}` | `deleteProgramParamenter` | Delete multivalue program parameter values | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--multivalue-program-parameters |
| `POST /v1/accounts/{accountId}/interest-accruals` | `postInterestAccruals` | Post interest accruals | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--post-interest-accruals |
| `PATCH /statements-v2/v3/accounts/{accountId}/interest-accruals` | `getAccountsTransactionsInterest` | Update interest accrual statuses | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |

### Operation essentials

- **`POST /v1/programs/{programId}/accrual-type-rates`** (`postAccrualTypesRates`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 200, 400, 409, 500; error codes in examples `EX0001`; events none listed.
- **`POST /v1/accounts/{accountId}/accrual-type-rates`** (`postAccountAccrualTypesRates`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 409, 500; error codes in examples `EX0001`; events none listed.
- **`GET /v1/accounts/{accountId}/accrual-type-rates`** (`listAccountAccrualTypeRates`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `EX0001`; events none listed.
- **`DELETE /v1/accounts/{accountId}/accrual-type-rates`** (`deleteAccountAccrualTypesRate`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `EX0001`, `EX0002`; events none listed.
- **`PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}`** (`updateProgramParamenter`): security `BearerAuth`; required parameters `programId` (path), `parameterId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `CE0001`, `GN0001`; events none listed.
- **`GET /statements-v2/v1/programs/{programId}/parameters/{parameterId}`** (`getProgramParameter`): security `BearerAuth`; required parameters `programId` (path), `parameterId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `CE0001`, `GN0001`; events none listed.
- **`DELETE /statements-v2/v1/programs/{programId}/parameters/{parameterId}`** (`deleteProgramParamenter`): security `BearerAuth`; required parameters `programId` (path), `parameterId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `EX0002`, `CE0001`, `GN0001`; events none listed.
- **`POST /v1/accounts/{accountId}/interest-accruals`** (`postInterestAccruals`): security `BearerAuth`; required parameters `accountId` (path); required body fields `accrual_statuses`; response statuses 201, 400, 403, 404, 422, 500; error codes in examples `EIAC0002`, `WIAC0005`, `WIAC0002`, `WIAC0003`, `GN0001`; events `transaction-creation-1`.
- **`PATCH /statements-v2/v3/accounts/{accountId}/interest-accruals`** (`getAccountsTransactionsInterest`): security `BearerAuth`; required parameters `accountId` (path); required body fields `accruals`; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `postInterestAccruals` | `transaction-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/accrual-type-rate-structures.md`: updatedAt 2026-05-11T19:40:52.000Z.
- `docs/card-issuing/configuring-transaction-types-to-not-accrue-charges.md`: updatedAt 2026-03-18T15:22:23.000Z.
- `docs/card-issuing/limiting-the-number-of-days-accruals-can-be-charged.md`: updatedAt 2026-03-18T15:22:24.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/accrual-type-rate-structures.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accrual-type-rate-structures | `28881e778a4117f0…` | 2026-05-11T19:40:52.000Z |
| `docs/card-issuing/configuring-transaction-types-to-not-accrue-charges.md` | whole document | https://developers.pismo.io/pismo-docs/docs/configuring-transaction-types-to-not-accrue-charges | `e73bd765bcf648fb…` | 2026-03-18T15:22:23.000Z |
| `docs/card-issuing/limiting-the-number-of-days-accruals-can-be-charged.md` | whole document | https://developers.pismo.io/pismo-docs/docs/limiting-the-number-of-days-accruals-can-be-charged | `668df6b8ef818495…` | 2026-03-18T15:22:24.000Z |

## Related knowledge units

- `KU-API-revolving-credit-configurations--account-accrual-rates` — API reference: Revolving credit - Configurations — Account accrual rates
- `KU-API-revolving-credit-configurations--program-accrual-rates` — API reference: Revolving credit - Configurations — Program accrual rates
- `KU-API-revolving-credit-interest-accruals--post-interest-accruals` — API reference: Revolving credit - Interest accruals — Post interest accruals
- `KU-API-revolving-credit-statements--accruals` — API reference: Revolving credit - Statements — Accruals
- `KU-API-revolving-credit-statements--multivalue-program-parameters` — API reference: Revolving credit - Statements — Multivalue program parameters
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CRED-calculating-interest-accruals` — Calculating interest accruals
- `KU-CRED-configuring-accrual-rates` — Configuring accrual rates
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-GS-setup-overview` — Core objects
