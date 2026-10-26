---
ku_id: KU-PAY-installments-payment
title: Installments payment
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/installments-payment.md
  sha256: 922a7c336d0d9a903317c13fcd69655c7c0567f667565562d14ee9acf45b2663
  url: https://developers.pismo.io/pismo-docs/docs/installments-payment
  role: primary_guide
  updated_at: '2026-06-16T23:01:01.000Z'
operations:
- CancelInstallmentsAdvanceV2
- CreateProcessingCode
- InstallmentAdvancedV2
- PostSetupTransactionType
- PostTransactionFlow
- post-payments-v1-force
- post-payments-v1-installments
related_kus:
- KU-API-core-platform-payment-methods--force-operations
- KU-API-core-platform-payment-methods--installments-payments
- KU-API-core-platform-transactions--transaction-flows
- KU-API-core-platform-transactions--transaction-types
- KU-API-platform-setup-orgs-operation--processing-codes
- KU-API-revolving-credit-statements--advancements
- KU-CORE-flex-controls
- KU-CORE-processing-codes-and-transaction-types
- KU-EVT-catalogue-balance
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-PAY-payments-configurations
grouping_rationale: single source page
---

# Installments payment

**KU ID:** `KU-PAY-installments-payment` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/installments-payment.md`:

> The [Installments payment](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-installments) endpoint gives users an easy way to pay in installments. You can set up rules for installments using [flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/installments-payment.md`: Installments payment; Create processing code; Create transaction type; Create transaction flow; Make an installments payment; Financed charge; Skip balance validation; Generated events; Manage installments on the customer statement

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/installments-payment.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/installments-payment · updatedAt: 2026-06-16T23:01:01.000Z

<!-- source:begin path=docs/core-platform/installments-payment.md part=0-end -->

# Installments payment

The [Installments payment](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-installments) endpoint gives users an easy way to pay in installments. You can set up rules for installments using [flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls).

> 📘
>
> Currently, the **Installments payment** endpoint only works with credit accounts. You must calculate all fees and interests ahead of time and include them in the request. Talk to your Pismo representative about defining these for your organization.

Before you call the **Installments payment** endpoint, you need to configure [processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) for the endpoint. The following sections step you through how to do this.

> 🚧
>
> If you try to call the **Installments payment** endpoint without first configuring the processing codes and transaction types, the platform will not be able to create the transactions involving the principal amount and other charges.

# Create processing code

To create a processing code, use the [Create processing code](https://developers.pismo.io/pismo-docs/reference/createprocessingcode) endpoint, and provide the required body parameters in the request.

| Field             | Description                                                                                                                        |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `processing_code` | Unique alphanumeric identifier.                                                                                                    |
| `description`     | Description for this operation.                                                                                                    |
| `balance_impact`  | Use **1** for credit/cash-in operations, **-1** for debit/cash-out operations, and **0** for operations that don't impact balance. |

To create two related processing codes (where one is used to reverse the other), use the [Create processing code](https://developers.pismo.io/pismo-docs/reference/createprocessingcode) endpoint and, in addition to the required fields for the first processing code,  provide values in the optional `undo_processing_code` and `undo_description` fields.

For additional options, see [Create or update processing code](https://developers.pismo.io/pismo-docs/docs/payments-configurations#create-or-update-processing-code).

# Create transaction type

To create a transaction type, use the [Create transaction type](https://developers.pismo.io/pismo-docs/reference/postsetuptransactiontype) endpoint. You need to create a transaction type for the contract and another one for the installments. If the operation includes taxes that appear on the customer’s statement, you need to create transaction types for them, too.

Example for creating a new transaction type for the contract:

```json
{  
     "transaction_type_id": 7500,  
     "description": "Contract for credit offering",  
     "credit": true,  
     "posted_transaction": false  
}
```

In this case, the contract does not appear on the customer’s statement  (`posted_transaction` is false).

Example for creating a new transaction type for the installments transactions:

```json
{  
     "transaction_type_id": 7501,  
     "description": "Installment credit offering",  
     "credit": true,  
     "posted_transaction": true  
}
```

In this case, the transaction installments will be on the final customer’s statement  (`posted_transaction` is true).

# Create transaction flow

The final step before calling the **Installments payments** endpoint is to setup the transaction flow. A transaction flow links a processing code with transaction types for installment non-network operations. Using the [Create transaction flow](https://developers.pismo.io/pismo-docs/reference/posttransactionflow) endpoint, you can define transaction flows for both the contract and the installments.

Example for a contract transaction:

```json
{  
     "key": "CONTRACT",  
     "transaction_type_id": 7500,  
     "processing_code": "5566"  
}
```

Example for an installment transaction:

```json
{  
     "key": "INSTALLMENT",  
     "transaction_type_id": 7501,  
     "processing_code": "5566"  
}
```

> 📘
>
> Note that the same processing code is linked to the contract transaction type and to the installment transaction type.

# Make an installments payment

You make an installments payment using the [Installments payment](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-installments) endpoint. The payload for the request should include an array of installment objects. Optionally, you can also include the `first_installment_date`. For example, you could use the following sample code to create two installments that would start on June 1, 2023:

```json
{
    "charging_amount": 22.30,
    "processing_code": "005000",
    "descriptor": "Test descriptor",
    "tracking_id": "2a1ea2f6-97fb-4738-97f4-d25ac88713a1",
    "account_id": 1,
  	"first_installment_date": 2023-06-01,
    "installments": [
        {
            "installment_number": 1,
            "total_amount": 11.15,
            "principal_amount": 10.00,
            "interest_amount": 1.00,
            "interest_rate": 0.10,
            "tax_amount": 0.15
        },
        {
            "installment_number": 2,
            "total_amount": 11.15,
            "principal_amount": 10.00,
            "interest_amount": 1.00,
            "interest_rate": 0.10,
            "tax_amount": 0.15
        }
    ]
}
```

If successful, this request returns the following response:

```json
{
	"authorization_id": 36174570,
	"tracking_id": "2a1ea2f6-97fb-4738-97f4-d25ac88713a1",
	"event_date": "2022-06-28T16:01:11.674"
}
```

## Financed charge

The `financed_charge` object in the [Installments payment](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-installments) endpoint request allows you to specify financed charges such as fees or taxes that are embedded in each installment's `principal_amount` field.

When you provide a value or multiples values in this object, the platform generates a separate accounting transaction for the specified financed charges. All fields within the `financed_charge` object must have the suffix “ \_amount”. For example, “io&#x66;**\_amount**”, "iva\*\*\_amount\*\*", “your\_ta&#x78;**\_amount**”. Work with your Pismo representative to define new financed charge type fields. When the representative creates and maps the new field, you can then use it and get the expected result.

> 🚧 Don't use tax\_amount field
>
> If you use the `financed_charge` object, you can't use the `tax_amount` field for the installments in the same request.
>
> The `financed_charge` object is reserved for cases when the fee or tax is embedded in the `principal_amount` and must not be described in the `tax_amount` field.

```json
{  
	"charging_amount": 22,  
	"processing_code": "215000",  
	"descriptor": "Installments payment",  
	"account_id": 123,  
	"tracking_id": "754d7b6b-a7c1-494c-8f7b-06d36a28c0bf",  
	"financed_charge": {  
          "iof_amount": 1,
          "fee_amount": 0.5
	},  
	"installments": [  
		{  
			"installment_number": 1,  
			"total_amount": 11,  
			"principal_amount": 10,  
			"interest_amount": 1,
			"interest_rate": 0.1
		},  
		{  
			"installment_number": 2,  
			"total_amount": 11,  
			"principal_amount": 10,  
			"interest_amount": 1,  
			"interest_rate": 0.1
    }
   ]
}
```

## Skip balance validation

By default, the Pismo platform performs account balance validation for installment operations. To skip account balance validation for installments, you can set the `skip_balance_validation` field to `true`, which forces the impact on the account's balance without checking the account limits.

In the following example, the account's global limit is 3,000.00 and the installments contract specifies 3 installments of 1,100.00. Since `skip_balance_validation` is `true` and the balance impact is forced, 3,300.00 in principal amount and 150.45 in fees and taxes is used for this installments operation for the total of 3,450.45. Global limit on the account remains 3,000.00. In this case, the call to check available limit on the account will return -450.45.

```json
{  
	"charging_amount": 3450.45,  
	"processing_code": "00",  
	"descriptor": "Installments payment",  
	"account_id": 345,  
	"tracking_id": "123d4b5b-a7c1-494c-8f7b-06d36a28c0bf",  
	"skip_balance_validation": true,  
	"installments": [  
		{  
          "installment_number": 1,  
          "total_amount": 1150.15,  
          "principal_amount": 1100.00,
          "interest_amount": 50,
          "interest_rate": 0.1,
          "tax_amount": 0.15
		},  
		{  
          "installment_number": 2,  
          "total_amount": 1150.15,  
          "principal_amount": 1100.00,
          "interest_amount": 50,
          "interest_rate": 0.1,
          "tax_amount": 0.15
		}, 
    {  
          "installment_number": 3,  
          "total_amount": 1150.15,  
          "principal_amount": 1100.00,
          "interest_amount": 50,
          "interest_rate": 0.1,
          "tax_amount": 0.15
		}  
	]
```

## Generated events

The **Installments payment** endpoint generates an [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) event. The `details` field of the event contains the same array of installment objects that you send in the **Installments payment** request. For example:

```json
{
    "cid": "test-installments-80605872",
    "timestamp": "2022-08-29T17:32:48Z",
    "org_id": "08102A0B-D4F8-42A2-8B0E-2052D05577D7",
    "domain": "authorization",
    "schema_version": "1",
    "event_type": "authorization-event",
    "data": {
        "amount": 22.3,
        "event_date": "2022-08-29T17:32:48.515",
        "authorization": {
            "id": 39787630,
            "code": "815958",
            "descriptor": "Test descriptor",
            "processing_code": "005000",
            "operation_description": "TRANSFER",
            "type": "INSTALLMENTS_PAYMENT",
            "account": {
                "id": 2
            },
            "card": {},
            "custom": {},
            "merchant": {},
            "available_change": {
                "id": "7154e307-b068-4af9-842e-116935091438",
                "update_datetime": "2022-08-29T17:32:48Z"
            }
        },
        "currency": "USD",
        "tracking_id": "b2163e26-ca87-4ec9-b6e9-76f2150359b7",
        "correlation_id": "test-installments-80605872",
        "location": {},
        "installments": {
            "number_of_installments": 2,
            "details": [
                {
                    "installment_number": 1,
                    "total_amount": 11.15,
                    "principal_amount": 10,
                    "interest_amount": 1,
                    "interest_rate": 0.1,
                    "tax_amount": 0.15
                },
                {
                    "installment_number": 2,
                    "total_amount": 11.15,
                    "principal_amount": 10,
                    "interest_amount": 1,
                    "interest_rate": 0.1,
                    "tax_amount": 0.05
                }
            ]
        }
    }
}
```

# Manage installments on the customer statement

An installment advance is a transfer of one or more installments from future cycles/statements to the present cycle/statement, always in descending order (that is, transferring the last installments first).

Use the [Create installment advance](https://developers.pismo.io/pismo-docs/reference/installmentadvancedv2) endpoint to advance installments. If you want to cancel the contract by advancing all installments, set `mode` to "all". If you want to advance a set number of installments (without canceling the contract), set `mode` to "single", and enter the number of installments that you want to advance in the `installments_to_advance`field. When you execute the request, the operation transfers the installments to the current statement.  You can then make a [force operation](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-force) to settle the installments debt .

> 📘
>
> If `mode` is set to "all", the `installments_to_advance` field is ignored. If `mode` is set to “single” and `installments_to_advance` is not filled, all transactions are advanced.

When an installment is advanced, the interest, if any, is released. The interest amount is returned as a credit (available limit) to the customer's account.

> 📘
>
> The `remove_interest_from_current` field indicates whether the interest for the current statement should be released. The default value is "false". This field only applies when `mode` is set to "all". If `mode` is set to "single", the interest for the current statement cannot be released. Interest on future installments is always released when those installments are advanced.

Use the [Cancel installments advance](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentsadvancev2) endpoint to cancel an advance. When an installment advance is canceled, the interest on the installment, if any, is reinserted, and the installment reverts to the original (future) cycle/statement.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /payments/v1/payments/installments` | `post-payments-v1-installments` | Create installments payment | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--installments-payments |
| `POST /orgs-operation/v1/processing-codes` | `CreateProcessingCode` | Create processing code | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `POST /v1/transaction-types` | `PostSetupTransactionType` | Create transaction type | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `POST /v1/transaction-flow` | `PostTransactionFlow` | Create transaction flow | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |
| `POST /statements/v2/accounts/{accountId}/installment-advance` | `InstallmentAdvancedV2` | Create installment advancement (no cancellation event) (deprecated) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |
| `POST /payments/v1/payments/force` | `post-payments-v1-force` | Force operation | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--force-operations |
| `DELETE /statements/v2/accounts/{accountId}/installment-advance/{id}` | `CancelInstallmentsAdvanceV2` | Cancel installments advancement (no cancellation event) (deprecated) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |

### Operation essentials

- **`POST /payments/v1/payments/installments`** (`post-payments-v1-installments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `account_id`, `charging_amount`, `processing_code`, `installments`; response statuses 201, 202, 400, 404, 409, 422, 500; error codes in examples `WP2P0000`, `WP2P0024`, `WP2P0025`, `WP2P0026`, `WP2P0027`, `WP2P0028`, `WP2P0029`, `WP2P0030`, `WP2P0005`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WLDG0006`, `WP2P0023`, `WP2P0022`, `WP2P0010`, `RULVAL0409`, `WP2P0000`, `WP2P0000`; events `authorization-authorization-event-1`.
- **`POST /orgs-operation/v1/processing-codes`** (`CreateProcessingCode`): security `S2SAuthentication`; required parameters none declared; required body fields `processing_code`, `balance_impact`, `description`, `reversal_processing_code`; response statuses 201, 400; error codes in examples none; events `orgs-operation-create-1`.
- **`POST /v1/transaction-types`** (`PostSetupTransactionType`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `description`, `credit`, `posted_transaction`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00005`, `WTRC05001`, `WTRC08001`, `ETRC00001`; events `transaction-types-creation-1`.
- **`POST /v1/transaction-flow`** (`PostTransactionFlow`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `processing_code`, `key`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00003`, `WTRC00005`, `WTRC04003`, `WTRC04004`, `WTRC04005`, `WTRC04006`, `WTRC05003`, `WTRC07001`, `WTRC04001`, `ETRC04003`, `ETRC04004`, `ETRC04005`, `ETRC04006`, `WTRC08001`, `ETRC00001`; events none listed.
- **`POST /statements/v2/accounts/{accountId}/installment-advance`** (`InstallmentAdvancedV2`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields none declared; response statuses 200, 400, 423, 500; error codes in examples `GN0001`; events `balance-installment-advancement-1`.
- **`POST /payments/v1/payments/force`** (`post-payments-v1-force`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields none declared; response statuses 201, 202, 400, 409, 500; error codes in examples `WP2P0000`, `WP2P1005`, `WRAT00001`, `WP2P0022`, `WP2P0023`, `WP2P0000`, `ERAT00001`, `ERAT00002`, `ERAT00003`, `EP2P0012`; events `authorization-authorization-event-1`.
- **`DELETE /statements/v2/accounts/{accountId}/installment-advance/{id}`** (`CancelInstallmentsAdvanceV2`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path), `id` (path); required body fields none declared; response statuses 200, 400, 404, 423, 500; error codes in examples `GN0001`; events `balance-installment-advancement-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v1-force` | `authorization-authorization-event-1` |
| `post-payments-v1-installments` | `authorization-authorization-event-1` |
| `CancelInstallmentsAdvanceV2` | `balance-installment-advancement-1` |
| `InstallmentAdvancedV2` | `balance-installment-advancement-1` |
| `CreateProcessingCode` | `orgs-operation-create-1` |
| `PostSetupTransactionType` | `transaction-types-creation-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `authorization-authorization-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-event-1 | 9 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/installments-payment.md`: updatedAt 2026-06-16T23:01:01.000Z.
- Links to `InstallmentAdvancedV2`, which is marked `deprecated: true` in `api-specs/Revolving_credit_-_Statements.yaml`.
- Links to `CancelInstallmentsAdvanceV2`, which is marked `deprecated: true` in `api-specs/Revolving_credit_-_Statements.yaml`.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/installments-payment.md` | whole document | https://developers.pismo.io/pismo-docs/docs/installments-payment | `922a7c336d0d9a90…` | 2026-06-16T23:01:01.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--force-operations` — API reference: Core platform - Payment methods — Force operations
- `KU-API-core-platform-payment-methods--installments-payments` — API reference: Core platform - Payment methods — Installments payments
- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-platform-setup-orgs-operation--processing-codes` — API reference: Platform setup - Orgs operation — Processing codes
- `KU-API-revolving-credit-statements--advancements` — API reference: Revolving credit - Statements — Advancements
- `KU-CORE-flex-controls` — Flexible transaction controls: concepts, examples and simulation
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-PAY-payments-configurations` — Payments configurations
