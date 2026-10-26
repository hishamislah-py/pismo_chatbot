---
ku_id: KU-CARD-full-balance-versus-zero-balance
title: Full balance versus Zero balance integration
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/full-balance-versus-zero-balance.md
  sha256: d5a234d5c5e4953302c9d88f33c03d1493db7bbbd6b97e89948f819ef967b3ab
  url: https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance
  role: primary_guide
  updated_at: '2026-04-03T20:55:04.000Z'
operations:
- post-payments-v1-force
related_kus:
- KU-API-core-platform-payment-methods--force-operations
- KU-CARD-anti-fraud-integration
- KU-CARD-authorization-validation-rules-for-card-network-operations
- KU-CARD-card-lifecycle-and-statuses
- KU-CARD-cards-overview-1
- KU-CARD-clearing
- KU-CARD-digital-wallets
- KU-CARD-disputes-overview
- KU-CARD-get-started-card-issuing
- KU-CARD-incremental-authorization
- KU-CARD-physical-card-embossing
- KU-CARD-replacement-amount-processing
- KU-CARD-zero-balance-integration
- KU-CORE-accounting-overview
- KU-CORE-accounts-overview
- KU-CORE-flex-controls
- KU-CORE-processing-codes-and-transaction-types
- KU-CORE-transactions-overview
- KU-CRED-negotiating-credit-card-debt
- KU-CRED-understanding-statements
- KU-ERR-validation-codes-for-authorization-events-part-01
- KU-ERR-validation-codes-for-authorization-events-part-02
- KU-EVT-catalogue-other-domains
- KU-EVT-timeline-overview
- KU-GS-setup-overview
- KU-PAY-force-operation
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Full balance versus Zero balance integration

**KU ID:** `KU-CARD-full-balance-versus-zero-balance` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/full-balance-versus-zero-balance.md`:

> The following table summarizes the differences between Full balance and Zero balance integration.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/full-balance-versus-zero-balance.md`: Full balance versus Zero balance integration; Card creation and management; Card validations; Customized card validations; Clearing Base II authorization; Anti-fraud check; Statement management; General ledger management; Accounting management; Adjustment handling; Transaction management; Flex transaction controls; Refinancing options

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/full-balance-versus-zero-balance.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance · updatedAt: 2026-04-03T20:55:04.000Z

<!-- source:begin path=docs/card-issuing/full-balance-versus-zero-balance.md part=0-end -->

# Full balance versus Zero balance integration

The following table summarizes the differences between Full balance and Zero balance integration.

With Full balance integration, Pismo handles most of the process. With Zero balance integration, you are responsible for managing your customers’ balances and credit limits. For both, Pismo provides card management and authorization integration with Visa, Mastercard, and other card networks.

| Feature                                                                                               | Full balance | Zero balance |
| :---------------------------------------------------------------------------------------------------- | :----------- | :----------- |
| Product setup: organization, programs, authorization                                                  | X            | X            |
| [Account](https://developers.pismo.io/pismo-docs/docs/accounts-overview#account-customers), customer creation                                 | X            | X            |
| [Card creation and management](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#card-creation-and-management)     | X            | X            |
| [Card validations](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#card-validations)                             | X            | X - some     |
| [Customized card validations](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#customized-card-validations)       | X            | X            |
| [Dispute management](https://developers.pismo.io/pismo-docs/docs/disputes-overview)                                                           | X            | X            |
| Authorization through Base I                                                                          | X            | X            |
| Streamed [data events](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview)                                                   | X            | X            |
| Streamed [timeline events](https://developers.pismo.io/pismo-docs/docs/timeline-overview)                                                     | X            |              |
| [Clearing Base II authorization](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#clearing-base-ii-authorization) | X            |              |
| [Anti-fraud check](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#anti-fraud-check)                             | X            |              |
| [Transaction management](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#transaction-management)                 | X            |              |
| Account balance and limit checks                                                                      | X            |              |
| Credit and debit settlement                                                                           | X            |              |
| [Statement management](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#statement-management)                     | X            |              |
| [General ledger management](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#general-ledger-management)           | X            |              |
| [Accounting management](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#accounting-management)                   | X            |              |
| [Adjustment handling](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#adjustment-handling)                       | X            |              |
| [Replacement amount processing](https://developers.pismo.io/pismo-docs/docs/replacement-amount-processing)                                    | X            |              |
| [Incremental authorization](https://developers.pismo.io/pismo-docs/docs/incremental-authorization)                                            | X            |              |
| [Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#flex-transaction-controls)       | X            | X            |
| [Refinancing options](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#refinancing-options)                       | X            |              |

### Card creation and management

Card creation and management includes the following:

* [Card lifecycle (create, update, cancel)](https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses)
* [Card embossing integration](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing)
* [Virtual cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#card-types)
* [Digital wallets](https://developers.pismo.io/pismo-docs/docs/wallet-overview)
* [PIN updates](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#card-data)
* Network integration
* Base I authorization processing

Refer to [Get started with card issuing](https://developers.pismo.io/pismo-docs/docs/get-started-with-card-issuing) for more information.

### Card validations

During transaction processing, there are two types of [card validations](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events) that take place:

* Stateless validations (Personal Identification Number (PIN), Card Verification Value (CVV), entry mode, and so on).
* Stateful validations (account/card status, limits, Application Transaction Counter (ATC), and so on).

For the validations done for Full balance versus Zero balance, refer to [List of validation rules](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations#list-of-rules).

### Customized card validations

An issuer can customize some validations, including:

* Allow local currency to be used in international purchases
* Allow transaction using card magnetic stripe
* Check terminal capabilities (entry mode vs. terminal capability)
* Must verify cryptogram for contactless or chip transactions
* Allow no-CVV and PIN validation for the card not present transactions
* Disable Card Verification Method (CVM)
* Validate chip signature
* PIN max error attempts
* Application Transaction Counter (ATC) range validation

Contact your Pismo representative to implement customized card validations.

### Clearing Base II authorization

Card networks send two types of authorization messages, created by two types of messaging systems: a single-message system (SMS) and a dual-message system (DMS). The clearing/base II reconciliation process handles these messages.

With Zero balance integration, you are responsible for handling [Clearing Base II](https://developers.pismo.io/pismo-docs/docs/clearingbase) authorization.

### Anti-fraud check

With Full balance integration, the Pismo platform provides [anti-fraud integration](https://developers.pismo.io/pismo-docs/docs/anti-fraud-integration) via a partner.

With Zero balance integration, you are responsible for your own anti-fraud checks as well as account and balance checks. refer to [Zero balance anti-fraud and validations integration](https://developers.pismo.io/pismo-docs/docs/zero-balance-anti-fraud-integration-1).

### Statement management

Credit card balances and interest accruals are managed in cycles (billing periods). A statement corresponds to a single cycle. The first cycle begins the moment the card is activated. After that, the first full day of each cycle follows the closing date of the previous cycle. On the last day of a cycle, the cycle is closed, and a grace period begins. This grace period belongs to the next cycle. When the grace period ends, if the card balance has not been paid off, charges begin to accrue. For more information, refer to [Understanding statements](https://developers.pismo.io/pismo-docs/docs/understanding-statements).

With Zero balance integration, you are responsible for managing the statement lifecycle.

### General ledger management

The Pismo platform uses [accounts](https://developers.pismo.io/pismo-docs/docs/setup-overview#account) to keep track of money flowing into and out of a company's general ledger.

With Zero balance integration, you are responsible for maintaining a general ledger.

### Accounting management

When you use the Pismo platform with Full balance integration, Pismo generates the accounting recordkeeping to the issuer's accounting systems after processing a transaction. Refer to the [Accounting overview](https://developers.pismo.io/pismo-docs/docs/accounting-overview) guide for more details.

With Zero balance integration, the issuer is responsible for handling accounting events via an [accounting script](https://developers.pismo.io/pismo-docs/docs/accounting-overview#accounting-script).

### Adjustment handling

It's sometimes necessary to add or remove money from a customer's account to reconcile balance inconsistencies (to credit an account when a transaction fails to be delivered or to return money to the customer). For more information, refer to the [Force operation](https://developers.pismo.io/pismo-docs/docs/force-operation).

With Zero balance integration, you are responsible for making adjustments. You can do this using the [Force operation](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-force) endpoint.

### Transaction management

A transaction is a record of a purchase, transfer, payment, or manual adjustment. In most cases, a cleared authorization triggers creating a transaction. For more information, refer to the [Transactions overview](https://developers.pismo.io/pismo-docs/docs/transactions-overview).

Transaction management includes the following:

* Create transactions
* Set up [transaction types and processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types)
* Payments API access

With Zero balance integration, you are responsible for creating a transaction after clearing an authorization. However, you cannot set up transaction types and processing codes.

### Flex transaction controls

The Pismo platform provides [flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls) that enable you to restrict a customer's financial operations. For example, you can set a maximum amount allowed for a certain transaction type.

With Full balance integration, you use the Pismo API to restrict customers' financial operations. With Zero balance integration, you are responsible for implementing such restrictions.

### Refinancing options

You must have processes in place that allow cardholders to refinance their credit card debt. To that end, your program must make the following options available:

* **Installment advances**—Used to settle future debt on the current cycle, rather than on a future cycle.
* **Installment agreement**—Used to refinance an existing credit card debt.
* **Statement agreement**—A contract that renegotiates all debt – past, present, and future.

With Zero balance integration, you are responsible for providing refinancing options to your customers.

For more information, refer to [Credit card refinancing overview](https://developers.pismo.io/pismo-docs/docs/negotiating-credit-card-debt).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /payments/v1/payments/force` | `post-payments-v1-force` | Force operation | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--force-operations |

### Operation essentials

- **`POST /payments/v1/payments/force`** (`post-payments-v1-force`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields none declared; response statuses 201, 202, 400, 409, 500; error codes in examples `WP2P0000`, `WP2P1005`, `WRAT00001`, `WP2P0022`, `WP2P0023`, `WP2P0000`, `ERAT00001`, `ERAT00002`, `ERAT00003`, `EP2P0012`; events `authorization-authorization-event-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v1-force` | `authorization-authorization-event-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/full-balance-versus-zero-balance.md`: updatedAt 2026-04-03T20:55:04.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/full-balance-versus-zero-balance.md` | whole document | https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance | `d5a234d5c5e49533…` | 2026-04-03T20:55:04.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--force-operations` — API reference: Core platform - Payment methods — Force operations
- `KU-CARD-anti-fraud-integration` — Anti-fraud integration
- `KU-CARD-authorization-validation-rules-for-card-network-operations` — Authorization validation rules for card network operations
- `KU-CARD-card-lifecycle-and-statuses` — Card lifecycle and statuses
- `KU-CARD-cards-overview-1` — Cards management
- `KU-CARD-clearing` — Clearing: Base II and the clearing rules engine
- `KU-CARD-digital-wallets` — Digital wallets, MDES Token Connect and Click to Pay
- `KU-CARD-disputes-overview` — Disputes overview
- `KU-CARD-get-started-card-issuing` — Get started with card issuing
- `KU-CARD-incremental-authorization` — Incremental authorization
- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-CARD-replacement-amount-processing` — Replacement amount processing
- `KU-CARD-zero-balance-integration` — Zero balance integration and anti-fraud validations
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
- `KU-CORE-accounts-overview` — Accounts
- `KU-CORE-flex-controls` — Flexible transaction controls: concepts, examples and simulation
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CORE-transactions-overview` — Transactions overview
- `KU-CRED-negotiating-credit-card-debt` — Credit card refinancing
- `KU-CRED-understanding-statements` — Understanding statements
- `KU-ERR-validation-codes-for-authorization-events-part-01` — Validation codes for authorization events (part 1 of 2)
- `KU-ERR-validation-codes-for-authorization-events-part-02` — Validation codes for authorization events (part 2 of 2)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-timeline-overview` — Timeline events
- `KU-GS-setup-overview` — Core objects
- `KU-PAY-force-operation` — Force operation
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
