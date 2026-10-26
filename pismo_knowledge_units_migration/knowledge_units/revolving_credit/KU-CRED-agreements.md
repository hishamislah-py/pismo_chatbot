---
ku_id: KU-CRED-agreements
title: 'Agreements: compulsory, statement, installment and payment agreements'
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/compulsory-agreements.md
  sha256: b4942cc8c729b27bed9e54db677c9eb1d0e0296e2634f67e17fbc524328c10d2
  url: https://developers.pismo.io/pismo-docs/docs/compulsory-agreements
  role: primary_guide
  updated_at: '2026-03-18T15:22:43.000Z'
- path: docs/card-issuing/statement-agreements.md
  sha256: 34cf67cdc9371dd374f06bea40aa16e8bcb1785c6ff77d61613876f0f500ebda
  url: https://developers.pismo.io/pismo-docs/docs/statement-agreements
  role: primary_guide
  updated_at: '2026-03-18T15:22:41.000Z'
- path: docs/card-issuing/installment-agreements.md
  sha256: 65ab8ea09caa27059cc23d6aa022f1aa443a98c2b1d1a486344dcd533c30aed0
  url: https://developers.pismo.io/pismo-docs/docs/installment-agreements
  role: primary_guide
  updated_at: '2026-03-18T15:22:37.000Z'
- path: docs/card-issuing/creating-payment-agreements-with-custom-transactions.md
  sha256: a219617f5f9d57cc93a0a278e344e2baaa38ec08a6c76feba8106a9694e61398
  url: https://developers.pismo.io/pismo-docs/docs/creating-payment-agreements-with-custom-transactions
  role: primary_guide
  updated_at: '2026-08-06T20:43:32.000Z'
operations:
- DeleteInstallmentPaymentByPaymentAgreementId
- GetInstallmentPayments
- InstallmentAdvancedV2
- InstallmentPaymentsv4
- PostTransactionFlow
- get-accounts-v1-accounts
- getByStatementId
- getTotalDue
related_kus:
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-transactions--transaction-flows
- KU-API-revolving-credit-statements--advancements
- KU-API-revolving-credit-statements--refinancing
- KU-API-revolving-credit-statements--statement
- KU-CORE-transactiontypes
- KU-EVT-catalogue-balance
grouping_rationale: Agreement types.
---

# Agreements: compulsory, statement, installment and payment agreements

**KU ID:** `KU-CRED-agreements` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 4 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Agreement types.

Scope as stated in `docs/card-issuing/compulsory-agreements.md`:

> A compulsory agreement is the same as an [installment agreement](https://developers.pismo.io/pismo-docs/docs/installment-agreements), except that the `compulsory` field is set to `true`, indicating that it's the result of a renegotiation that was made independently of the customer.

Scope as stated in `docs/card-issuing/statement-agreements.md`:

> If a cardholder wishes to renegotiate all debt—past, present, and future—use a statement agreement contract.

Scope as stated in `docs/card-issuing/installment-agreements.md`:

> If a cardholder wishes to renegotiate only overdue debt, use an **installment agreement** contract.

Scope as stated in `docs/card-issuing/creating-payment-agreements-with-custom-transactions.md`:

> When you create a payment agreement, you can associate it with a transaction flow using custom transactions. The following table lists the processing codes you should use for this feature. They are default codes for the platform.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/compulsory-agreements.md`: Compulsory agreements; Manage compulsory agreements
- `docs/card-issuing/statement-agreements.md`: Statement agreements; Creating a statement agreement; Manage existing statement agreements
- `docs/card-issuing/installment-agreements.md`: Installment agreements; Creating an installment agreement; Manage installment agreements
- `docs/card-issuing/creating-payment-agreements-with-custom-transactions.md`: Creating payment agreements with custom transactions; Step 1: Create a transaction flow using a custom key; Example: Create a transaction flow for the agreement installment using processing code 005092; Step 2: Associate the custom key when creating the payment agreement; Example: Create payment agreement with custom transactions

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 8 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/compulsory-agreements.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/compulsory-agreements · updatedAt: 2026-03-18T15:22:43.000Z

<!-- source:begin path=docs/card-issuing/compulsory-agreements.md part=0-end -->

# Compulsory agreements

A compulsory agreement is the same as an [installment agreement](https://developers.pismo.io/pismo-docs/docs/installment-agreements), except that the `compulsory` field is set to `true`, indicating that it's the result of a renegotiation that was made independently of the customer.

## Manage compulsory agreements

Use the endpoints in the [Refinancing API](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) to create, manage, and search for your compulsory agreements (as well as other types of payment agreements).
<!-- source:end -->

### Source 2: `docs/card-issuing/statement-agreements.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/statement-agreements · updatedAt: 2026-03-18T15:22:41.000Z

<!-- source:begin path=docs/card-issuing/statement-agreements.md part=0-end -->

# Statement agreements

If a cardholder wishes to renegotiate all debt—past, present, and future—use a statement agreement contract.

> 📘
>
> If you don’t advance all future debt to the current statement before implementing the statement agreement, the compensation between the statement agreement credit and the future debt will only happen in the future closing dates.

The platform then:

* Adds a credit to the total balance for current statements after advancing all future debt.
* Creates installments for current and future statements

Refer to the figure below.

<Image title="Credit card refinancing overview - 4.png" alt="Advancing future debt to the current cycle and creating installments" align="center" src="https://files.readme.io/c5db614-Credit_card_refinancing_overview_-_4.png">
  Advancing future debt to the current cycle and creating installments (shown in gray and orange)
</Image>

After implementing the statement agreement in Cycle 2, the total balance is 290 for 12 installments. To avoid becoming overdue again, the cardholder has to make a payment of 35 for the next 12 due dates.

> 📘 A note for Brazilian developers
>
> According to a Brazilian Central Bank resolution, any debt renegotiation occurring after 1 January, 2024 may not have a sum of interest and fines higher than the original debt amount. This includes revolving interest charges and payment agreement interest.

## Creating a statement agreement

Before you create a new statement agreement, make sure the customer is eligible for refinancing. So, check with your organization’s refinancing terms, procedures, and conditions (for example, debt-to-income or credit history).

If the customer is eligible for refinancing:

1. Get the balance information for the account using the [Get total amount due](https://developers.pismo.io/pismo-docs/reference/gettotaldue) endpoint.
2. Get the refinanced amount from the  `balance.open` field in the response.
3. Use your own calculation method based on the refinanced amount to generate a new payment plan.

> 📘
>
> Since the Pismo platform supports a collection of installments, you can use any desired amortization system to calculate a payment agreement.

4. Use the [Create installment advance without interest](https://developers.pismo.io/pismo-docs/reference/installmentadvancedv2) endpoint to advance all installments on the account to the current statement.
5. After you have the plan, use the [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) endpoint to create a new statement agreement, setting the values of the body parameters as indicated in Steps 6 through 8.
6. Set the values of the following parameters as indicated.
   * `statement_agreement` = `true`
   * `compulsory` = `false`
   * `settle_accrual` = `false`
7. Use the `installment` body parameter to create an array of installments for the payment agreement.
8. Populate the remaining fields. Note that IOF fields only apply to Brazil. If you’re not in Brazil, enter 0 in the IOF fields.
9. Execute the endpoint.

Once you’ve created a new statements agreement, the Pismo platform posts the new agreement on the currently open and future statements. If the customer needs to cancel the agreement, use [Cancel payment agreement](https://developers.pismo.io/pismo-docs/reference/deleteinstallmentpaymentbypaymentagreementid).

## Manage existing statement agreements

Use the other endpoints in the [Refinancing API](https://developers.pismo.io/pismo-docs/reference/getinstallmentpayments) to search for and manage your statement agreements (as well as other types of payment agreements).
<!-- source:end -->

### Source 3: `docs/card-issuing/installment-agreements.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/installment-agreements · updatedAt: 2026-03-18T15:22:37.000Z

<!-- source:begin path=docs/card-issuing/installment-agreements.md part=0-end -->

# Installment agreements

If a cardholder wishes to renegotiate only overdue debt, use an **installment agreement** contract.

After implementing an installment agreement, the debt due on an account redistributes across the next statements. The platform then adds a credit equal to the refinanced balance and overdue balance from other past statements. It creates installments for current and future statements. Refer to the figure below.

<Image title="Credit card refinancing overview - 3.png" alt="Redistributing the debt across the billing cycles" align="center" src="https://files.readme.io/ae18778-Credit_card_refinancing_overview_-_3.png">
  Redistributing the debt across the billing cycles (shown in orange)
</Image>

After implementing the installment agreement of the 100 that was overdue in Cycle 1, the cardholder needs to make a payment of 160 in Cycle 2 to avoid becoming overdue in DD2. The cardholder also has to make a payment of 60 in DD3 in Cycle 3.  To avoid becoming overdue again, the cardholder has to pay 10 in the 10 subsequent due dates.

## Creating an installment agreement

Before you create a new payment agreement, make sure the customer is eligible for refinancing. So, check with your organization’s refinancing terms, procedures, and conditions (for example, debt-to-income or credit history).

If the customer is eligible for refinancing:

1. Get their account details using the [Get account](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts) endpoint.
2. Copy the number from the `current_cycle` field in the response.
3. Execute the [List statements v3](https://developers.pismo.io/pismo-docs/reference/getbystatementid) endpoint, entering the number from Step 2 into the `startCycle` field.
4. Get the refinanced amount from the `previous_balance` field in the response.
5. Use your own calculation method based on the refinanced amount to generate a new payment plan.

> 📘
>
> Since the Pismo platform supports a collection of installments, you can use any desired amortization system to calculate a payment agreement.

7. After you have the plan, use [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) to create a new installment agreement.
8. In this endpoint, set the following fields to `false`.

   * `statement_agreement`
   * `compulsory`
   * `settle_accural`
9. Use the `installment` body parameter to create installments for the payment agreement.
10. Populate the remaining fields. Note that IOF fields only apply to Brazil. If you’re not in Brazil, enter 0 in the IOF fields.
11. Execute the endpoint.

Once you’ve created a new installment agreement, the Pismo platform posts the new installments on the currently open and future statements. If the customer needs to cancel the agreement, use [Cancel payment agreement](https://developers.pismo.io/pismo-docs/reference/deleteinstallmentpaymentbypaymentagreementid).

## Manage installment agreements

Use the other endpoints in the [Refinancing API](https://developers.pismo.io/pismo-docs/reference/getinstallmentpayments) to search for and manage your installment agreements (as well as other types of payment agreements).
<!-- source:end -->

### Source 4: `docs/card-issuing/creating-payment-agreements-with-custom-transactions.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/creating-payment-agreements-with-custom-transactions · updatedAt: 2026-08-06T20:43:32.000Z

<!-- source:begin path=docs/card-issuing/creating-payment-agreements-with-custom-transactions.md part=0-end -->

# Creating payment agreements with custom transactions

When you create a payment agreement, you can associate it with a transaction flow using custom transactions. The following table lists the processing codes you should use for this feature. They are default codes for the platform.

| Processing code | Description             | **Undo processing code** | **Description**                |
| :-------------- | :---------------------- | :----------------------- | :----------------------------- |
| 005091          | REFINANCING INSTALLMENT | 005095                   | CANCEL REFINANCING INSTALLMENT |
| 005092          | AGREEMENT INSTALLMENT   | 005096                   | CANCEL AGREEMENT INSTALLMENT   |
| 005093          | COMPULSORY INSTALLMENT  | 005097                   | CANCEL COMPULSORY INSTALLMENT  |

When additional transactions need to be created as part of a payment agreement, such as insurance, fees, or other auxiliary charges, the integration must follow a two‑step configuration process. This ensures that the Pismo platform properly generates the additional transactions and links them to the agreement lifecycle.

# Step 1: Create a transaction flow using a custom key

First, define a transaction flow for the additional transaction type using the [Create transaction flow ](https://developers.pismo.io/pismo-docs/reference/posttransactionflow) endpoint. The `custom_key` serves as a unique identifier for this custom transaction flow. You reference it when you create the payment agreement in Step 2.

<Callout icon="📘" theme="info">
  In Step 1, the value for `custom_key` must have an "Amount" suffix. For example: `Insurance01Amount`. In Step 2, you must remove the suffix from this value before passing it in the `custom_key`field of the`custom_transactions` objects: `Insurance01`.
</Callout>

## Example: Create a transaction flow for the agreement installment using processing code 005092

In this example:

* The `custom_key` (`Insurance01Amount`) identifies the transaction flow. It must end in "Amount".
* This flow defines how the custom transaction is created and processed.

```curl
curl --request POST \ 
     --url https://sandbox.pismolabs.io/transactions-core/v1/transaction-flow \ 
     --header 'Accept: application/json' \ 
     --header 'Authorization: Bearer <your_bearer_token>' \ 
     --header 'Content-type: application/json' \ 
     --data ' 
{ 
  "key": "OTHER", 
  "transaction_type_id": 10000, 
  "processing_code": "005092", 
  "custom_key": "Insurance01Amount" 
}'
```

# Step 2: Associate the custom key when creating the payment agreement

Use the [Create payment agreement ](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) endpoint to create the payment agreement. Remove the "Amount" suffix from the value that you used for `custom_key`in Step one, and use the resulting value for the `custom_key` fields in the `custom_transactions` objects of the request. You should use a different value for the `custom_key` fields  in the `custom_contract_transaction` object.

## Example: Create payment agreement with custom transactions

In this example:

* `Insurance01` is used in the `custom_key` field of each `custom_transactions`object (instead of `Insurance01Amount`).
* A new value, `Insurance02`, is used in the `custom_key` field of the `custom_contract_transaction` object.
* The transaction created from the `custom_contract_transaction` field can represent any value you choose as long **as it does not exceed the total contract amount**. It appears on the current statement, but does not impact the balance or limit.
* The `custom_transactions` array lists transactions associated with installments, which appear on the statements. (`posted_transaction` = `true` in the [transaction types](https://developers.pismo.io/pismo-docs/docs/transactiontypes).)
* As a result, the Pismo platform automatically creates and manages the insurance transactions associated with `Insurance01` as part of the payment agreement.

```curl
curl --request POST \ 
     --url https://sandbox.pismolabs.io/statements/v4/accounts/accountId/installment-payments \ 
     --header 'accept: application/json' \ 
     --header 'authorization: Bearer <your_bearer_token>' \ 
     --header 'content-type: application/json' \ 
     --data '
{
  "statement_agreement": true,
  "compulsory": false,
  "settle_accrual": false,
  "split_iof": false,
  "use_original_rate": false,
  "custom_contract_transaction": {
    "custom_key": "Insurance02",
    "amount": 100
  },
  "installments": [
        {
            "installment_number": 1,
            "description": "first installment",
            "total_amount": 604.55,
            "principal_amount": 541.00,
            "interest_rate": 18.00,
            "interest_amount": 50.00,
            "iof_amount": 10.00,
            "daily_iof_amount": 0.00,
            "custom_transactions": [
                {
                    "amount": 3.55,
                    "custom_key": "Insurance01"
                }
            ]
        },
        {
            "installment_number": 2,
            "description": "second installment",
            "total_amount": 604.55,
            "principal_amount": 541.00,
            "interest_rate": 18.00,
            "interest_amount": 50.00,
            "iof_amount": 10.00,
            "daily_iof_amount": 0.00,
            "custom_transactions": [
                {
                    "amount": 3.55,
                    "custom_key": "Insurance01"
                }
            ]
        }
  ]
}
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /statements/v4/accounts/{accountId}/installment-payments` | `InstallmentPaymentsv4` | Create payment agreement | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `GET /statements-v2/v2/accounts/{accountId}/total-due` | `getTotalDue` | Get account total due | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `POST /statements/v2/accounts/{accountId}/installment-advance` | `InstallmentAdvancedV2` | Create installment advancement (no cancellation event) (deprecated) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |
| `DELETE /statements/v4/accounts/{accountId}/installment-payments/{id}` | `DeleteInstallmentPaymentByPaymentAgreementId` | Cancel payment agreement | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `GET /statements/v4/accounts/{accountId}/installment-payments` | `GetInstallmentPayments` | List payment agreements | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `GET /accounts/v1/accounts/{accountId}` | `get-accounts-v1-accounts` | Get account | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `GET /statements-v2/v3/accounts/{accountId}/statements` | `getByStatementId` | List statements | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `POST /v1/transaction-flow` | `PostTransactionFlow` | Create transaction flow | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |

### Operation essentials

- **`POST /statements/v4/accounts/{accountId}/installment-payments`** (`InstallmentPaymentsv4`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `statement_agreement`, `installments`; response statuses 201, 400, 404, 423, 500; error codes in examples `GN0001`; events `balance-installment-payment-processed-1`.
- **`GET /statements-v2/v2/accounts/{accountId}/total-due`** (`getTotalDue`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.
- **`POST /statements/v2/accounts/{accountId}/installment-advance`** (`InstallmentAdvancedV2`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields none declared; response statuses 200, 400, 423, 500; error codes in examples `GN0001`; events `balance-installment-advancement-1`.
- **`DELETE /statements/v4/accounts/{accountId}/installment-payments/{id}`** (`DeleteInstallmentPaymentByPaymentAgreementId`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path), `id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `GN0001`; events none listed.
- **`GET /statements/v4/accounts/{accountId}/installment-payments`** (`GetInstallmentPayments`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields none declared; response statuses 200, 500; error codes in examples `GN0001`; events none listed.
- **`GET /accounts/v1/accounts/{accountId}`** (`get-accounts-v1-accounts`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 404, 500; error codes in examples none; events none listed.
- **`GET /statements-v2/v3/accounts/{accountId}/statements`** (`getByStatementId`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.
- **`POST /v1/transaction-flow`** (`PostTransactionFlow`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `processing_code`, `key`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00003`, `WTRC00005`, `WTRC04003`, `WTRC04004`, `WTRC04005`, `WTRC04006`, `WTRC05003`, `WTRC07001`, `WTRC04001`, `ETRC04003`, `ETRC04004`, `ETRC04005`, `ETRC04006`, `WTRC08001`, `ETRC00001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `InstallmentAdvancedV2` | `balance-installment-advancement-1` |
| `InstallmentPaymentsv4` | `balance-installment-payment-processed-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/compulsory-agreements.md`: updatedAt 2026-03-18T15:22:43.000Z.
- `docs/card-issuing/statement-agreements.md`: updatedAt 2026-03-18T15:22:41.000Z.
- `docs/card-issuing/installment-agreements.md`: updatedAt 2026-03-18T15:22:37.000Z.
- `docs/card-issuing/creating-payment-agreements-with-custom-transactions.md`: updatedAt 2026-08-06T20:43:32.000Z.
- Links to `InstallmentAdvancedV2`, which is marked `deprecated: true` in `api-specs/Revolving_credit_-_Statements.yaml`.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/compulsory-agreements.md` | whole document | https://developers.pismo.io/pismo-docs/docs/compulsory-agreements | `b4942cc8c729b27b…` | 2026-03-18T15:22:43.000Z |
| `docs/card-issuing/statement-agreements.md` | whole document | https://developers.pismo.io/pismo-docs/docs/statement-agreements | `34cf67cdc9371dd3…` | 2026-03-18T15:22:41.000Z |
| `docs/card-issuing/installment-agreements.md` | whole document | https://developers.pismo.io/pismo-docs/docs/installment-agreements | `65ab8ea09caa2705…` | 2026-03-18T15:22:37.000Z |
| `docs/card-issuing/creating-payment-agreements-with-custom-transactions.md` | whole document | https://developers.pismo.io/pismo-docs/docs/creating-payment-agreements-with-custom-transactions | `a219617f5f9d57cc…` | 2026-08-06T20:43:32.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-revolving-credit-statements--advancements` — API reference: Revolving credit - Statements — Advancements
- `KU-API-revolving-credit-statements--refinancing` — API reference: Revolving credit - Statements — Refinancing
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-CORE-transactiontypes` — Transaction types
- `KU-EVT-catalogue-balance` — Event catalogue: balance
