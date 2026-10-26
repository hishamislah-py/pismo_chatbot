---
ku_id: KU-BANK-penalties-for-cd-accounts
title: Penalties and taxes for CD accounts
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/penalties-for-cd-accounts.md
  sha256: ffc0a43b3fbc3425a7f8180e8a08c63e2fe990fd474a900868940e92553b5605
  url: https://developers.pismo.io/pismo-docs/docs/penalties-for-cd-accounts
  role: primary_guide
  updated_at: '2026-10-06T18:47:10.000Z'
operations:
- PostSetupTransactionType
- PostTransactionFlow
- get-account-balances
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-simulate-penalty
- post-v1-interest-plan
- postModel
related_kus:
- KU-API-banking-interest-bearing-accounts--penalty
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-engine--interest-engine
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-core-platform-transactions--transaction-flows
- KU-API-core-platform-transactions--transaction-types
- KU-API-platform-setup-rates-and-fees--fee-models
- KU-CORE-fee-models
- KU-EVT-catalogue-deposit
- KU-EVT-catalogue-interest
- KU-EVT-catalogue-transaction
grouping_rationale: single source page
---

# Penalties and taxes for CD accounts

**KU ID:** `KU-BANK-penalties-for-cd-accounts` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/penalties-for-cd-accounts.md`:

> You can apply penalties and tax withholding to certificate of deposit (CD) accounts when specific withdrawal conditions occur, such as shortly after account opening, during the term, or after multiple withdrawals within a short period.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/penalties-for-cd-accounts.md`: Penalties and taxes for CD accounts; Penalties; Supported penalty models; Penalty types; Early withdrawal after opening; Tiered interest forfeiture; Subsequent withdrawal; Grace period; Withdrawal fee; Required accounting configuration; The four building blocks; What you provide; How the components work together; Penalty configuration; Penalty types; Penalty calculation; Percentage-based penalties; Fixed-amount penalties; Simulate penalties; Request parameters; Simulate a full withdrawal; Simulation rules and errors; Key rules and considerations; Example penalties object; Taxes

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/penalties-for-cd-accounts.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/penalties-for-cd-accounts · updatedAt: 2026-10-06T18:47:10.000Z

<!-- source:begin path=docs/core-banking/penalties-for-cd-accounts.md part=0-end -->

# Penalties and taxes for CD accounts

You can apply penalties and tax withholding to certificate of deposit (CD) accounts when specific withdrawal conditions occur, such as shortly after account opening, during the term, or after multiple withdrawals within a short period.

CD penalty configuration lets you model different withdrawal behaviors across the product lifecycle. You can apply these penalty types individually or combine them to enforce product rules more precisely. Penalties are configured at the deposit product level during its creation, and the Pismo platform evaluates them at withdrawal time.

You can also preview the penalties that would apply to a planned withdrawal, including a full withdrawal of the account balance before executing it. Refer to [Simulate penalties](#simulate-penalties).

When designing a penalty strategy, pay close attention to:

* the customer event that triggers the penalty
* whether the penalty should be percentage-based or fixed
* the dependency on the interest plan
* whether multiple penalties may apply together

A CD product can include one or more of these penalty types, refer to the [Penalty types](#penalty-types) section for more details. Depending on the product configuration, you can apply more than one penalty to the same withdrawal.

# Penalties

## Supported penalty models

CD account penalties use two main calculation models.

<Table>
  <thead>
    <tr>
      <th>
        Penalty model
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Percentage-based
      </td>

      <td>
        Calculates the penalty by applying the equivalent of a configured number of interest days to the withdrawn amount. In a percentage‑based penalty, the Pismo platform calculates the value of X interest days on the withdrawn amount. Percentage‑based penalties require the following interest‑plan values from the product:

        * `fixed_interest_rate` or `benchmark_rate`
        * `accrual_basis`
      </td>
    </tr>

    <tr>
      <td>
        Fixed amount
      </td>

      <td>
        Calculates a penalty as the monetary value of forfeited interest days, typically based on the account balance or CD principal. Fixed-amount penalties calculate the monetary value of X forfeited interest days for the account balance.
      </td>
    </tr>
  </tbody>
</Table>

## Penalty types

Here is a summary table of all penalty types. For the relevant fee IDs and transaction flows, refer to [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product).

| Penalty type                                                      | Model                            | Basis                                      | Main configuration                                                   |
| ----------------------------------------------------------------- | -------------------------------- | ------------------------------------------ | -------------------------------------------------------------------- |
| [Early withdrawal after opening](#early-withdwawal-after-opening) | Percentage-based                 | Withdrawn amount                           | `applicable_within_days`, `penalty_interest_days`                    |
| [Tiered interest forfeiture](#tiered-interest-forfeiture)         | Fixed amount                     | Days held tier                             | `min_days_held`, `max_days_held`, `forfeited_interest_days`          |
| [Subsequent withdrawal](#subsequent-withdrawal)                   | Percentage-based                 | Withdrawn amount                           | `window_behavior`, `applicable_within_days`, `penalty_interest_days` |
| [Grace period](#grace-period)                                     | Percentage-based                 | Withdrawn amount                           | `duration_days`, `penalty_interest_days`                             |
| [Withdrawal fee](#withdrawal-fee)                                 | Percentage-based or fixed amount | Withdrawn amount or fixed configured value | `type`, `value`                                                      |

### Early withdrawal after opening

This penalty applies to any withdrawal made within a configured number of days after account opening.

#### How it works

This is how early withdrawal after opening is calculated.

| Calculation factor | Description                                    |
| ------------------ | ---------------------------------------------- |
| Type               | Percentage-based                               |
| Basis              | Withdrawn amount                               |
| Equivalent to      | `penalty_interest_days` days of interest       |
| Applies within     | `applicable_within_days` after account opening |

#### Example

```json
"penalties": {
  "early_withdrawal_after_opening": {
    "applicable_within_days": 10,
    "penalty_interest_days": 7
  }
}
```

In this example, the Pismo platform applies a penalty equivalent to **seven days of simple interest** on the withdrawn amount for any withdrawal made within the first **ten days** after the deposit account opens.

### Tiered interest forfeiture

This penalty applies a fixed penalty amount based on how long the funds remained in the account before withdrawal.

#### How it works

| Calculation factor | Description                                                                  |
| ------------------ | ---------------------------------------------------------------------------- |
| Type               | Fixed amount                                                                 |
| Basis              | A holding‑period tier defined by `min_days_held` and `max_days_held`         |
| Equivalent to      | `forfeited_interest_days` days of interest, converted into a monetary amount |

#### Rules

* You can define multiple tiers.
* Tiers must not overlap.
* The last tier’s `max_days_held` must **not exceed** the product’s `max_term`.

#### Example

```json
"tiered_interest_forfeiture": [
  {
    "min_days_held": 1,
    "max_days_held": 90,
    "forfeited_interest_days": 30
  },
  {
    "min_days_held": 91,
    "max_days_held": 180,
    "forfeited_interest_days": 90
  }
]
```

In this example:

* A withdrawal made between day 1 and day 90 forfeits 30 days of interest.
* A withdrawal made between day 91 and day 180 forfeits 90 days of interest.

The Pismo platform converts the forfeited interest days into a fixed monetary penalty amount. The penalty amount remains fixed and does not vary based on the amount withdrawn.

### Subsequent withdrawal

This penalty applies when a customer makes subsequent withdrawals within a configured time window.

#### How it works

| Calculation factor | Description                              |
| ------------------ | ---------------------------------------- |
| Type               | Percentage-based                         |
| Basis              | Withdrawn amount                         |
| Equivalent to      | `penalty_interest_days` days of interest |
| Window             | `applicable_within_days`                 |

#### Window strategies

Window strategies define how the time window is tracked when evaluating whether a penalty applies. The window sets the period in which withdrawals are reviewed, and the strategy determines how that period behaves after each withdrawal.

This penalty supports two window strategies:

* `ROLLING`: the window resets after each withdrawal
* `FIXED`: the window starts with the first withdrawal and does not reset

#### Example

```json
"subsequent_withdrawals": {
  "window_behavior": "ROLLING",
  "applicable_within_days": 6,
  "penalty_interest_days": 7
}
```

In this example, the Pismo platform applies a penalty equivalent to seven days of simple interest to any subsequent withdrawal made within a six-day rolling window. Each qualifying withdrawal resets the window and starts a new six-day period.

### Grace period

This penalty applies to withdrawals made during the grace period.

During the grace period, customers can make multiple cash‑out transactions without penalty as long as the total amount withdrawn does not exceed the matured CD balance.

When cumulative withdrawals go beyond the matured CD balance, only the excess amount is classified as an early withdrawal and is subject to the grace‑period penalty defined at the deposit product level.

If a withdrawal reduces the remaining balance below the previous principal amount, the Pismo platform applies the grace‑period penalty.

This behavior is deterministic and evaluated per transaction:

* The penalty applies only to the withdrawal that causes the cumulative amount to exceed the matured balance.
* The penalty is calculated solely on the excess amount and is never applied retroactively.

#### How it works

| Calculation factor | Description                              |
| ------------------ | ---------------------------------------- |
| Type               | Percentage-based                         |
| Basis              | Withdrawn amount                         |
| Equivalent to      | `penalty_interest_days` days of interest |
| Duration           | `duration_days`                          |

#### Example

```json
"grace_period": {
  "duration_days": 10,
  "penalty_interest_days": 30
}
```

In this example, a withdrawal made during the ten-day grace period triggers a penalty only if it causes the remaining balance to fall below the previous CD principal. If that happens, the Pismo platform applies a penalty equivalent to 30 days of interest.

> 📘 Note
>
> There is an option for you to accrue interest during grace period. Refer to `accrue_during_grace_period` in [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product) for more details.

### Withdrawal fee

This penalty is a generic withdrawal fee that you can configure as either a percentage-based fee or a fixed amount.

#### How it works

| Calculation factor | Description                                                                     |
| ------------------ | ------------------------------------------------------------------------------- |
| Type               | Percentage-based or fixed amount                                                |
| Values             | The product defines these directly in the `withdrawal_fee` configuration object |

#### Example

```json
"withdrawal_fee": {
  "type": "PERCENTAGE",
  "value": 1.5
}
```

In this example, a 1.5% fee is applied to the withdrawn amount because the penalty is configured using the `PERCENTAGE` type.

## Required accounting configuration

Penalty‑enabled CD accounts rely on accounting components that you must provide before penalty transactions can post. Each penalty type needs a transaction type and a transaction flow, and these objects define how the penalty appears in the ledger and in financial accounting, and how the fee connects to the withdrawal operation.

### The four building blocks

These objects work together to support penalty operations. Each one answers a different part of the penalty configuration.

| Object           | What it answers              | Role                                                                                                                                                                                                               |
| ---------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Fee model        | What to charge and how much  | Holds a `fees[]` array. Each fee has an ID and a calculation method (`calculation`) such as `FIXED`, `PERCENTAGE`, `GREATER`, or `DYNAMIC_BY_AMOUNT`. Refer to [Create fee model ](https://developers.pismo.io/pismo-docs/reference/postmodel)for more details. |
| Processing code  | When to charge               | Identifies the financial operation. The fee is ignored if the operation does not match the processing code linked to the fee.                                                                                      |
| Transaction type | How it appears in the ledger | Defines credit and posted transactions. Custom IDs start at `7000` because lower values are reserved for Pismo internals.                                                                                          |
| Transaction flow | The wiring                   | Maps one processing code to one transaction type using a key such as `PRINCIPAL`, `INSTALLMENT`, `CONTRACT`, or `OTHER`.                                                                                           |

### What you provide

| Item             | Description                                                                                                                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Transaction type | Defines credit, posted\_transaction, and how the entry appears in the ledger and financial accounting. Custom IDs start at `7000` because lower values are reserved for Pismo internals. |
| Transaction flow | Maps one processing code to one transaction type. The mapping uses a key such as `PRINCIPAL`, `INSTALLMENT`, `CONTRACT`, or `OTHER`.                                                     |
| Processing code  | Identifies when the penalty is charged. Penalties use Pismo’s standard processing codes: `PSM175` for the penalty charge and `PSM176` for the reversal.                                  |

### How the components work together

A fee model only calculates the penalty amount. It does not create a transaction. To convert a calculated penalty into accounting entries, the fee must land in a transaction type through a transaction flow. Penalty operations need two transaction types mapped to the same processing code. The `PRINCIPAL` mapping covers the withdrawal operation. The `OTHER` mapping covers the penalty amount.

When the key is `OTHER`, the transaction flow must include a `custom_key`. This value ties the flow to a specific fee inside the fee model. `custom_key` is the fee ID plus the suffix `Amount`. For example, if the fee ID is `earlyWithdrawalAfterOpeningID`, the `custom_key` is `earlyWithdrawalAfterOpeningAmount`. Incorrect suffixes or fee IDs prevent the penalty from posting.

### Penalty configuration

#### Example (`PRINCIPAL`)

This example shows how to configure a penalty that subtracts a principal amount as the deduction method.

```shell
curl --request POST \
--url https://sandbox.pismolabs.io/transactions-core/v1/transaction-flow \
--header 'Content-type: application/json' \
--data '{
"key": "PRINCIPAL",
"transaction_type_id": 10000,
"processing_code": "PSM175",
}'
```

Using the example, you

1. set the processing code for the penalty. In the example, use `PSM175` for debit.
2. define the transaction type by assigning a transaction type ID supplied by the client.
3. map the withdrawal operation to its transaction type using key `PRINCIPAL`, which shows that the amount comes from the principal.

Refer to [Create transaction type](https://developers.pismo.io/pismo-docs/reference/postsetuptransactiontype) for details.

#### Example (`OTHER`)

Besides using principal to cover a penalty, you can set the key `OTHER` and pass a `custom_key` value to show that the penalty is paid through an alternative method. In this example, you use `PSM175` as the processing code.

```shell
curl --request POST \
--url https://sandbox.pismolabs.io/transactions-core/v1/transaction-flow \
--header 'Content-type: application/json' \
--data '{
"key": "OTHER",
"transaction_type_id": 10001,
"processing_code": "PSM175",
"custom_key": "earlyWithdrawalAfterOpeningAmount"
}'
```

1. Set the processing code `PSM175` for the penalty.
2. Map the penalty amount to its transaction type using key `OTHER` and a `custom_key` value, where `custom_key` is the fee ID with the suffix `ID` replaced by `Amount` (for example, `earlyWithdrawalAfterOpeningPenaltyID` becomes `earlyWithdrawalAfterOpeningPenaltyAmount`).
3. Upon completion, the Pismo platform attaches the fee model to your organization, program, or account.

For details, refer to [Create transaction flow](https://developers.pismo.io/pismo-docs/reference/posttransactionflow).

### Penalty types

| Penalty type                                                      | Fee ID                                 | Transaction flow                           |
| ----------------------------------------------------------------- | -------------------------------------- | ------------------------------------------ |
| [Early withdrawal after opening](#early-withdrawal-after-opening) | `earlyWithdrawalAfterOpeningPenaltyID` | `earlyWithdrawalAfterOpeningPenaltyAmount` |
| [Tiered interest forfeiture](#tiered-interest-forfeiture)         | `tieredInterestForfeiturePenaltyID`    | `tieredInterestForfeiturePenaltyAmount`    |
| [Grace period](#grace-period)                                     | `gracePeriodPenaltyID`                 | `gracePeriodPenaltyAmount`                 |
| [Withdrawal fee](#withdrawal-fee)                                 | `withdrawalFeePenaltyID`               | `withdrawalFeePenaltyAmount`               |
| [Subsequent withdrawal](#subsequent-withdrawal)                   | `subsequentWithdrawalPenaltyID`        | `subsequentWithdrawalPenaltyAmount`        |

For each penalty type, you provide one transaction type for the penalty and one transaction flow that maps the withdrawal processing code to that transaction type. Your `custom_key` must point to the penalty’s fee ID.

After you configure a transaction type and transaction flow for each penalty associated with your deposit product, the Pismo platform creates a fee model containing the configured penalties and attaches it to the account or program.

## Penalty calculation

Penalty calculation depends on the penalty type.

### Percentage-based penalties

This model applies to:

* Early withdrawal after opening
* Subsequent withdrawal
* Grace period
* Withdrawal fee when configured as a percentage

The Pismo platform derives the effective penalty percentage from the product’s interest settings.

#### Example parameters

The following formula is used to calculate a percentage-based penalty.

| Calculation factor      | Value       |
| ----------------------- | ----------- |
| `fixed_interest_rate`   | 3% annually |
| `accrual_basis`         | 365         |
| `penalty_interest_days` | 7           |
| `withdrawal_amount`     | 10,000      |

#### Step 1: Compute the daily rate

```text
daily_rate = fixed_interest_rate / accrual_basis
daily_rate = 0.03 / 365 ≈ 0.0000822
```

#### Step 2: Compute the penalty factor for X interest days

```text
penalty_factor = daily_rate * penalty_interest_days
penalty_factor = 0.0000822 * 7 ≈ 0.0005754
```

#### Step 3: Convert the factor into a percentage

```text
penalty_percent = penalty_factor * 100
penalty_percent ≈ 0.05754 (%)
```

#### Step 4: Apply the percentage to the withdrawal amount

```text
penalty_amount = withdrawal_amount * (penalty_percent / 100)
penalty_amount = 10,000 * 0.0005754 ≈ 5.75
```

#### Result

The penalty amount is 5.75.

### Fixed-amount penalties

This model applies to:

* Tiered interest forfeiture
* Withdrawal fee when configured as a fixed amount

The Pismo platform computes a monetary penalty based on forfeited interest days.

#### Example parameters

| Calculation factor        | Value       |
| ------------------------- | ----------- |
| `interest_rate`           | 3% annually |
| `accrual_basis`           | 365         |
| `forfeited_interest_days` | 30          |
| CD principal amount       | 500         |

#### Formula

```text
penalty = (((1 + (interest_rate * n / accrual_basis)) * CD_amount) - CD_amount)
```

#### Applied example

Note that the subtraction of 500 removes the original principal amount, ensuring the formula returns only the interest portion, which represents the penalty.

```text
penalty = (((1 + (0.03 * 30 / 365)) * 500) - 500)
penalty ≈ 1.23
```

#### Result

The fixed penalty amount is 1.23. The Pismo platform then uses this monetary value as the fixed amount for the fee model.

## Simulate penalties

Before performing an actual withdrawal, you can preview the penalties that would apply by using the [Simulate penalty](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-simulate-penalty) endpoint:

The simulation is read-only and does not modify any data. It evaluates all penalty rules configured for the account's product, including:

* Early withdrawal after opening
* Grace period
* Tiered interest forfeiture
* Withdrawal fee
* Subsequent withdrawal

For details about penalty types, refer to the `penalties` object in [Create deposit product]().

### Request parameters

| Field               | Required | Description                                                                                                                                                          |
| ------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `withdrawal_date`   | Yes      | Simulated withdrawal date, in ISO 8601 format. For example, `2026-12-15T00:00:00Z`.                                                                                  |
| `withdrawal_amount` | No       | The amount the customer intends to withdraw. When passed, it must not exceed the current book balance. When omitted, the Pismo platform simulates a full withdrawal. |

### Simulate a full withdrawal

If you omit `withdrawal_amount`, the Pismo platform fetches the account's current book balance using [Get transaction banking account balance](https://developers.pismo.io/pismo-docs/reference/get-account-balances) and calculates the penalty on that value. This lets you simulate a full withdrawal without having to look up the balance first.

The `withdrawal_amount` returned in the response shows the value used in the simulation, which equals the book balance when the field was omitted in the request.

**Request example for a full-withdrawal simulation:**

```shell
curl --request POST \

   --url https://sandbox.pismolabs.io/savings-products/v1/deposits/accounts/accountId/penalty-simulation \

   --header 'accept: application/json' \

   --header 'content-type: application/json' \

   --data '

{

 "withdrawal_date": "2026-12-15T00:00:00Z" 

}
```

**Response example:**

```json
{
  "withdrawal_amount": 40667.17,
  "withdrawal_date": "2026-12-15T00:00:00Z",
  "penalty_rule_applied": [
    {
      "type": "fixed",
      "value": 50.00,
      "description": "Withdrawal fee"
    },
    {
      "type": "percentage",
      "value": 181.75,
      "description": "Early withdrawal after opening penalty"
    }
  ],
  "penalty_amount": 231.75,
  "penalty_breakdown": {
    "fixed_amount": 50.00,
    "percentage_amount": 181.75
  },
  "currency": "BRL",
  "gross_amount": 41329.34,
  "interest_earned_amount": 667.17,
  "net_amount": 41097.59,
  "simulation_timestamp": "2026-06-19T19:22:55Z"
}
```

In this example, you can see the results of a withdrawal simulation, including any applicable penalty rules, penalty amounts, and calculated withdrawal values.

**Response fields**

| Field                    | Description                                                                                                                                                 |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `withdrawal_amount`      | The withdrawal amount used in the simulation. Equals the book balance when omitted in the request.                                                          |
| `withdrawal_date`        | The withdrawal date used in the simulation, in ISO 8601 format.                                                                                             |
| `penalty_rule_applied`   | List of penalty rules that apply to the withdrawal. Each item includes type (percentage or fixed), value, and description. Omitted when no penalties apply. |
| `penalty_amount`         | Total penalty amount, combining all relevant penalty rules.                                                                                                 |
| `penalty_breakdown`      | Total penalty split by calculation type, in `fixed_amount` and `percentage_amount`. Omitted when no penalty applies.                                        |
| `currency`               | Currency in ISO 4217 alphabetic format. Omitted when no penalty applies.                                                                                    |
| `gross_amount`           | Gross amount of the deposit account: total balance without interest plus total interest earned. Always present; `0` when no total record exists.            |
| `interest_earned_amount` | Total interest earned (paid or capitalized) on the account. Always present; `0` when no total record exists.                                                |
| `net_amount`             | Net amount after deducting penalties: `gross_amount - penalty_amount`.                                                                                      |
| `simulation_timestamp`   | Date and time of the simulation, in ISO 8601 format.                                                                                                        |

### Simulation rules and errors

* A `withdrawal_date` inside the cool-off period results in no penalties.
* `withdrawal_date` must not be in the past.
* A withdrawal\_amount of zero or a negative value is rejected.
* A `withdrawal_amount` greater than the current book balance is rejected, and the error details return the available balance.
* Simulation is available only for deposit accounts.

## Key rules and considerations

* Penalties are evaluated at withdrawal time.
* A single withdrawal can trigger multiple penalties if the product configuration allows it.
* Percentage-based penalties depend on the product’s interest plan to derive the effective rate.
* To preview penalties for a planned withdrawal, including a full withdrawal, use the [Simulate penalty](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-simulate-penalty) endpoint. Refer to [Simulate penalties](#simulate-penalties) for more information.
* Tiered interest forfeiture tiers must be:
  * non-overlapping
  * logically ordered
  * bounded by the product’s maximum term

## Example penalties object

This example shows how a CD product can define multiple penalties.

```json
"penalties": {
  "early_withdrawal_after_opening": {
    "applicable_within_days": 10,
    "penalty_interest_days": 7
  },
  "tiered_interest_forfeiture": [
    {
      "min_days_held": 1,
      "max_days_held": 90,
      "forfeited_interest_days": 30
    },
    {
      "min_days_held": 91,
      "max_days_held": 180,
      "forfeited_interest_days": 90
    }
  ],
  "subsequent_withdrawals": {
    "window_behavior": "ROLLING",
    "applicable_within_days": 6,
    "penalty_interest_days": 7
  },
  "grace_period": {
    "duration_days": 10,
    "penalty_interest_days": 30
  },
  "withdrawal_fee": {
    "type": "PERCENTAGE",
    "value": 1.5
  }
```

# Taxes

You can also configure tax withholding when creating an [interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan). Using the `withholding_moment` field in `tax_withholding` to specify when taxes are withheld, you can choose either `ACCRUAL` or `CAPITALIZATION`. If you omit `tax_withholding`, no tax withholding applies.

For details, refer to [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan).

> 📘 Note
>
> The processing code used in the fee model must match the one used in the interest plan. This serves as a prerequisite for the configuration requirements. Refer to [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan) and [Fee models](https://developers.pismo.io/pismo-docs/docs/fee-models) for more details.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/deposits` | `interest-bearing-v1-create-deposit-product` | Create deposit product | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/fee/models` | `postModel` | Create fee model | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--fee-models |
| `POST /v1/transaction-types` | `PostSetupTransactionType` | Create transaction type | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `POST /v1/transaction-flow` | `PostTransactionFlow` | Create transaction flow | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |
| `POST /v1/deposits/accounts/{accountId}/penalty-simulation` | `interest-bearing-v1-simulate-penalty` | Simulate penalty | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--penalty |
| `GET /bank-statements/v1/account-balances/{externalAccountId}` | `get-account-balances` | Get transaction banking account balance | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `POST /v1/interest/plan` | `post-v1-interest-plan` | Create interest plan | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |

### Operation essentials

- **`POST /v1/deposits`** (`interest-bearing-v1-create-deposit-product`): security `BearerAuth`; required parameters none declared; required body fields `name`, `interest_plan_id`, `term_type`; response statuses 201, 400, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0393`, `EIBACC0007`; events `deposit-product-creation-1`.
- **`POST /v1/fee/models`** (`postModel`): security `bearerAuth`; required parameters `Authorization` (header); required body fields `model_description`, `fees`; response statuses 201, 400, 401, 500; error codes in examples none; events none listed.
- **`POST /v1/transaction-types`** (`PostSetupTransactionType`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `description`, `credit`, `posted_transaction`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00005`, `WTRC05001`, `WTRC08001`, `ETRC00001`; events `transaction-types-creation-1`.
- **`POST /v1/transaction-flow`** (`PostTransactionFlow`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `processing_code`, `key`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00003`, `WTRC00005`, `WTRC04003`, `WTRC04004`, `WTRC04005`, `WTRC04006`, `WTRC05003`, `WTRC07001`, `WTRC04001`, `ETRC04003`, `ETRC04004`, `ETRC04005`, `ETRC04006`, `WTRC08001`, `ETRC00001`; events none listed.
- **`POST /v1/deposits/accounts/{accountId}/penalty-simulation`** (`interest-bearing-v1-simulate-penalty`): security `BearerAuth`; required parameters `accountId` (path); required body fields `withdrawal_date`; response statuses 200, 400, 403, 404, 422, 500; error codes in examples `EIBACC0015`, `EIBACC0008`, `EIBACC0338`, `EIBACC0005`, `EIBACC0226`, `EIBACC0064`, `EIBACC0294`, `EIBACC0295`, `EIBACC0296`, `EIBACC0007`, `EIBACC0204`; events none listed.
- **`GET /bank-statements/v1/account-balances/{externalAccountId}`** (`get-account-balances`): security `BearerAuth`; required parameters `externalAccountId` (path); required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples `CMN0002`, `WABL0003`, `WABL0002`, `WABL0001`, `CMN9999`, `EABL0001`; events none listed.
- **`POST /v1/interest/plan`** (`post-v1-interest-plan`): security `BearerAuth`; required parameters none declared; required body fields `accrual_basis`, `accrual_frequency`, `capitalization_frequency`, `currency_code`, `description`, `interest_type`, `start_date`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `interest-engine-interest-plan-creation-success-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `interest-bearing-v1-create-deposit-product` | `deposit-product-creation-1` |
| `post-v1-interest-plan` | `interest-engine-interest-plan-creation-success-1` |
| `PostSetupTransactionType` | `transaction-types-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/penalties-for-cd-accounts.md`: updatedAt 2026-10-06T18:47:10.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- `docs/core-banking/penalties-for-cd-accounts.md` line 444: `[Create deposit product]()` (empty link target, kept as published)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/penalties-for-cd-accounts.md` | whole document | https://developers.pismo.io/pismo-docs/docs/penalties-for-cd-accounts | `ffc0a43b3fbc3425…` | 2026-10-06T18:47:10.000Z |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--penalty` — API reference: Banking - Interest-bearing accounts — Penalty
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-platform-setup-rates-and-fees--fee-models` — API reference: Platform setup - Rates and fees — Fee models
- `KU-CORE-fee-models` — Fee management and fee models
- `KU-EVT-catalogue-deposit` — Event catalogue: deposit
- `KU-EVT-catalogue-interest` — Event catalogue: interest
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
