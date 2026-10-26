---
ku_id: KU-PAY-hold-funds
title: Hold funds
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/hold-funds.md
  sha256: fdf6966656a2d0500d8f3ceb3b6160a4e401523bc4c5f170d983360f1dc454a7
  url: https://developers.pismo.io/pismo-docs/docs/hold-funds
  role: primary_guide
  updated_at: '2026-07-24T14:39:55.000Z'
operations:
- get-v1-account-balance
- get-v1-account-limit
- post-payments-v1-hold-funds-block
- post-payments-v1-hold-funds-transfer
- post-payments-v1-hold-funds-transfer-cancel
- post-payments-v1-hold-funds-unblock
related_kus:
- KU-API-core-platform-balances-and-limits--account-balances
- KU-API-core-platform-ledger--account-limits
- KU-API-core-platform-payment-methods--hold-funds
- KU-CORE-accounts-overview
- KU-CORE-processing-codes-and-transaction-types
- KU-CORE-working-with-limits-objects
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-PAY-payments-configurations
grouping_rationale: single source page
---

# Hold funds

**KU ID:** `KU-PAY-hold-funds` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/hold-funds.md`:

> Hold funds feature allows you to prevent or limit financial movement of a specified amount of money out of the account. Usually, but not always, this occurs due to a legal action. While the funds are held, you can call the [List account limits](https://developers.pismo.io/pismo-docs/reference/get-v1-account-limit) endpoint to view the held funds amount. Held funds can't be withdrawn or moved until they are released back into the account or transferred to another account.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/hold-funds.md`: Hold funds; Workflow; Processing codes and transaction types; Events; Authorization created; Account balance changed; Transaction created; Example of hold funds actions; Hold funds; Release funds; Transfer held funds; Cancel transfer of held funds; Get account balances; Check current account balance; Check end-of-day balance

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/hold-funds.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/hold-funds · updatedAt: 2026-07-24T14:39:55.000Z

<!-- source:begin path=docs/core-platform/hold-funds.md part=0-end -->

# Hold funds

Hold funds feature allows you to prevent or limit financial movement of a specified amount of money out of the account. Usually, but not always, this occurs due to a legal action. While the funds are held, you can call the [List account limits](https://developers.pismo.io/pismo-docs/reference/get-v1-account-limit) endpoint to view the held funds amount. Held funds can't be withdrawn or moved until they are released back into the account or transferred to another account.

There are four different actions available in the hold funds feature:

* **Hold funds** ([Block amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-block) endpoint) transfers a specified amount of money out of the available account balance and holds it in reserve, so that the account holder no longer has access to it. The amount to be moved to held funds must be available in the client account (that means the sum of `available_credit_limit` and `available_savings_account_limit`), otherwise the operation is denied.  The account must be active with the [account status](https://developers.pismo.io/pismo-docs/docs/accounts-overview#account-status) NORMAL or BLOCKED and the program type can be any type except CREDIT.
* **Release held funds** ([Unblock held amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-unblock) endpoint) releases the total or partial amount blocked from held funds balance to available balance. The amount released is fully moved to the `available_credit_limit` balance. The amount to be released must be less than or equal to the held funds, otherwise the operation is denied.
* **Transfer held funds** ([Transfer held amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-transfer) endpoint) transfers the total or partial retained balance from held funds out of the Pismo platform to an external third-party account. The amount to be transferred must be less than or equal to the held funds, otherwise the operation is denied. Once the held funds are transferred to a third-party account, you can cancel the transfer to place the held funds back into the client account.
* **Cancel transfer of held funds** ([Cancel transfer of held amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-transfer-cancel) endpoint) cancels transfer of a previously held amount from a Pismo account to an external third-party account.

# Workflow

The following diagram represents the hold funds transaction flow:

<Image align="center" alt="Image showing the hold funds transaction flow." src="https://files.readme.io/f2839ed-789971e-pismo-diagram-hold-funds.png" />

Note that you need to move the amount from the available balance to held funds and only then it is possible to transfer the amount to a third-party account. If you block an amount, the way to reverse it is using the unblock endpoint.

If you transfer the blocked amount to a third-party account, the way to reverse it is to make a cash-in for the account and then block the amount once again.

# Processing codes and transaction types

Processing codes are used in each endpoint of this service: hold funds, release funds, transfer to a third-party account, and cancel transfer of held funds. These processing codes must be associated with specific operation types and transaction types that will generate the transactions after the authorization. When [creating a processing code](https://developers.pismo.io/pismo-docs/reference/post-processing-code-by-tenant) for each hold funds service, ensure that the `operation_type` is set to `HOLD_FUNDS`.

For more information, see [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) and [Payments configurations](https://developers.pismo.io/pismo-docs/docs/payments-configurations).

| Processing code | Balance impact           | Processing code description   | Transaction type | Transaction type description  | Operation type |
| :-------------- | :----------------------- | :---------------------------- | :--------------- | :---------------------------- | :------------- |
| 999999          | **-1** (debit, cash-out) | Hold funds                    | 9999             | Hold funds                    | HOLD\_FUNDS    |
| 999999          | **1** (credit, cash-in)  | Release funds                 | 9999             | Release funds                 | HOLD\_FUNDS    |
| 999999          | **-1** (debit, cash-out) | Transfer court account        | 9999             | Transfer court account        | HOLD\_FUNDS    |
| 999999          | **1** (credit, cash-in)  | Cancel transfer court account | 9999             | Cancel transfer court account | HOLD\_FUNDS    |

# Events

The platform generates the following two events whenever an authorization is successfully completed.

## Authorization created

The following endpoints generate the [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) event.

| Endpoint                                                                         | Authorization type  |
| :------------------------------------------------------------------------------- | :------------------ |
| [Block amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-block)                            | BLOCK               |
| [Unblock amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-unblock)                        | UNBLOCK             |
| [Transfer held amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-transfer)                 | TRANSFER            |
| [Cancel transfer of held funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-transfer-cancel) | HELD\_FUNDS\_CREDIT |

## Account balance changed

The following endpoints generate the [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1) event.

| Endpoint                                                                         | Operation type | Impact                                                      |
| :------------------------------------------------------------------------------- | :------------- | :---------------------------------------------------------- |
| [Block amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-block)                            | DEBIT          | Debit available credit limit and/or available savings limit |
| [Unblock amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-unblock)                        | CREDIT         | Credit available credit limit                               |
| [Transfer held amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-transfer)                 | DEBIT          | Debit held funds                                            |
| [Cancel transfer of held funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-transfer-cancel) | CREDIT         | Credit available credit limit                               |

## Transaction created

The [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1) event occurs asynchronously when the platform creates a transaction after the successful authorization.

# Example of hold funds actions

## Hold funds

You can block a specific amount using the [Block amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-block) endpoint.  Once blocked, the corresponding amount is moved from the `available_credit_limit` to the `held_funds` limit.

By default, the Pismo platform performs account balance validation to ensure the account has sufficient funds to block an amount. You also have the option to force this operation without performing account balance validation. When you set `skip_balance_validation` to `true`, the platform skips account balance validation and blocks the amount regardless whether the account has a sufficient available balance. In this case, if the account doesn’t have a sufficient balance, its available balance will be in a negative state and any future usual debit operations will not be possible until the account receives enough credit.

Below is a sample of a request to hold funds.

`POST v1/payments/hold-funds/block`

```json
{  
    "account_id": 111507785,  
    "tracking_id":"b970c8a9-5ec9-4e46-8c0d-f411e0bd6ce7",  
    "amount":500.45,  
    "processing_code":283503,  
    "description":"Legal block",  
    "skip_balance_validation": false,
  	"metadata":{  
        "message": "Block requested"  
    }  
}
```

## Release funds

You can release a specific amount using the [Unblock amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-unblock) endpoint. Once unblocked, the amount is moved back to the `available_credit_limit` limit.

Below is a sample of a request to release funds.

`POST v1/payments/hold-funds/unblock`

```json
{  
    "account_id": 111507785,  
    "tracking_id":"c852a2b1-9ad0-5a57-9d1e-a512f1ae7df8",  
    "amount":30.22,  
    "processing_code":283506,  
    "description":"Legal unblock",  
    "metadata":{  
        "message":"Unblock requested"  
    }  
}
```

## Transfer held funds

To perform a transfer of held funds to an external account, use the [Transfer held funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-transfer) endpoint. Once transferred, the amount is removed from the `held_funds` limit.

<Callout icon="📘" theme="info">
  You can only transfer an amount that was previously blocked.
</Callout>

Below is a sample of a request to transfer held funds.

`POST v1/payments/hold-funds/transfer`

```json
{  
    "account_id": 111507785,  
    "tracking_id":"d853b3c2-1ba2-6b58-0e2a-b513a2bf8ea9",  
    "amount":100.63,  
    "processing_code":283506,  
    "description":"Transfer to judicial court",  
    "metadata":{  
        "message":"Transfer requested",  
        "transfer_to":"International Bank"  
    }  
}
```

## Cancel transfer of held funds

To perform a transfer of held funds to an external account, use the [Cancel transfer of held funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-transfer-cancel) endpoint.

Below is a sample of a request to cancel transfer of held funds.

`POST v1/payments/hold-funds/transfer/cancel`

```json
{
  "tracking_id": "be68db6e-8da0-4761-8632-6a51857bd123",
  "account_id": 101,
  "amount": 12.13,
  "processing_code": "004000",
  "description": "Blocked value",
  "metadata": {
    "my-custom-key": "my-custom-value"
  }
}
```

# Get account balances

## Check current account balance

To find out the amount of held funds, you need to get its account limits. You can do this by checking the field `held_funds` in the response of the  [List account limits](https://developers.pismo.io/pismo-docs/reference/get-v1-account-limit) endpoint.

Below is a sample of response with the current account balances.

`GET v1/accounts/{accountId}/limits`

```json
{
    "available_savings_account_limit": 9596.85,
    "available_credit_limit": 7845.98,
    "held_funds": 2285.72
}

```

For more information, see the [Account limits](https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects) guide.

## Check end-of-day balance

To find out the held funds at the end of a specific day, you need to check the field `held_funds` in the response of the [Get daily account balance limits](https://developers.pismo.io/pismo-docs/reference/get-v1-account-balance) endpoint.

Below is a sample of response with the current account balances.

`GET ledger/v1/accounts/{accountId}/daily-balances`

```json
{
            "account_id": "2412",
            "org_id": "08102A0B-D4F8-42A2-8B0E-2052D05577D7",
            "ref_date": "2023-02-01",
            "available_credit_limit": 2997.41,
            "available_withdrawal_credit": 411.05,
            "available_total_installment_credit": 455.45,
            "available_savings_account_limit": 311.08,
            "held_funds": 311.08
        },
```

For more information, see the [Daily account balances](https://developers.pismo.io/pismo-docs/docs/accounts-overview#get-daily-account-balance-limits) guide.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /v1/accounts/{accountId}/limits` | `get-v1-account-limit` | List account limits | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |
| `POST /payments/v1/payments/hold-funds/block` | `post-payments-v1-hold-funds-block` | Block amount | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--hold-funds |
| `POST /payments/v1/payments/hold-funds/unblock` | `post-payments-v1-hold-funds-unblock` | Unblock held amount | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--hold-funds |
| `POST /payments/v1/payments/hold-funds/transfer` | `post-payments-v1-hold-funds-transfer` | Transfer held amount | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--hold-funds |
| `POST /payments/v1/payments/hold-funds/transfer/cancel` | `post-payments-v1-hold-funds-transfer-cancel` | Cancel transfer of held amount | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--hold-funds |
| `GET /v1/accounts/{accountId}/daily-balances` | `get-v1-account-balance` | Get daily account balance limits | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--account-balances |

### Operation essentials

- **`GET /v1/accounts/{accountId}/limits`** (`get-v1-account-limit`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `WLDG0020`, `WLDG0022`, `ELDG9999`; events none listed.
- **`POST /payments/v1/payments/hold-funds/block`** (`post-payments-v1-hold-funds-block`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `account_id`, `amount`, `processing_code`; response statuses 201, 202, 400, 404, 500; error codes in examples `WP2P0000`; events `authorization-authorization-event-1`, `availables-change-available-1`.
- **`POST /payments/v1/payments/hold-funds/unblock`** (`post-payments-v1-hold-funds-unblock`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `account_id`, `amount`, `processing_code`; response statuses 201, 202, 400, 404, 500; error codes in examples `WP2P0000`; events `authorization-authorization-event-1`, `availables-change-available-1`.
- **`POST /payments/v1/payments/hold-funds/transfer`** (`post-payments-v1-hold-funds-transfer`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `account_id`, `amount`, `processing_code`; response statuses 201, 202, 400, 404, 500; error codes in examples `WP2P0000`; events `authorization-authorization-event-1`, `availables-change-available-1`.
- **`POST /payments/v1/payments/hold-funds/transfer/cancel`** (`post-payments-v1-hold-funds-transfer-cancel`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `original_tracking_id`, `account_id`, `amount`, `processing_code`; response statuses 201, 202, 400, 404, 500; error codes in examples `WP2P0000`; events `authorization-authorization-event-1`, `availables-change-available-1`.
- **`GET /v1/accounts/{accountId}/daily-balances`** (`get-v1-account-balance`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `WBLS0005`, `WLDG0021`, `EBLS9999`; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `post-processing-code-by-tenant` | Payments configurations; creating a processing code | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v1-hold-funds-block` | `authorization-authorization-event-1` |
| `post-payments-v1-hold-funds-transfer` | `authorization-authorization-event-1` |
| `post-payments-v1-hold-funds-transfer-cancel` | `authorization-authorization-event-1` |
| `post-payments-v1-hold-funds-unblock` | `authorization-authorization-event-1` |
| `post-payments-v1-hold-funds-block` | `availables-change-available-1` |
| `post-payments-v1-hold-funds-transfer` | `availables-change-available-1` |
| `post-payments-v1-hold-funds-transfer-cancel` | `availables-change-available-1` |
| `post-payments-v1-hold-funds-unblock` | `availables-change-available-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `authorization-authorization-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-event-1 | 9 | KU-EVT-catalogue-other-domains |
| `availables-change-available-1` | availables | 1 | https://developers.pismo.io/events/docs/availables-change-available-1 | 22 | KU-EVT-catalogue-other-domains |
| `transaction-creation-1` | transaction | 1 | https://developers.pismo.io/events/docs/transaction-creation-1 | 7 | KU-EVT-catalogue-transaction |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/hold-funds.md`: updatedAt 2026-07-24T14:39:55.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 3 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.
- Operation link `post-processing-code-by-tenant` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/hold-funds.md` | whole document | https://developers.pismo.io/pismo-docs/docs/hold-funds | `fdf6966656a2d050…` | 2026-07-24T14:39:55.000Z |

## Related knowledge units

- `KU-API-core-platform-balances-and-limits--account-balances` — API reference: Core platform - Balances and limits — Account balances
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-API-core-platform-payment-methods--hold-funds` — API reference: Core platform - Payment methods — Hold funds
- `KU-CORE-accounts-overview` — Accounts
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CORE-working-with-limits-objects` — Account limits
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-PAY-payments-configurations` — Payments configurations
