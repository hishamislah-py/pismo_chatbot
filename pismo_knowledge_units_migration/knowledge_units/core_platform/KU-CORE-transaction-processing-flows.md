---
ku_id: KU-CORE-transaction-processing-flows
title: Transaction processing flows
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/transaction-processing-flows.md
  sha256: dd8a2d0d808982f8baf0e89bf03e6b79f4f1cdb233bdaebda3b949272017f063
  url: https://developers.pismo.io/pismo-docs/docs/transaction-processing-flows
  role: primary_guide
  updated_at: '2026-09-28T14:08:47.000Z'
operations:
- post-authorization
- post-payment-confirm
- post-payments
- post-payments-cancel
related_kus:
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-CORE-balance-configurations
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Transaction processing flows

**KU ID:** `KU-CORE-transaction-processing-flows` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/transaction-processing-flows.md`:

> The Pismo platform supports multiple transaction processing flows. Depending on the transaction flow used, transactions might or might not participate in shared-limit processing, account hierarchy resolution, centralized billing, and centralized limit restoration.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/transaction-processing-flows.md`: Transaction processing flows; Payment methods API; Supported operations; Shared-limit behavior; Card network authorization flows; Authorizations; Reversals; Clearing; Matched clearing; Unmatched clearing; Payments API; Choosing the appropriate flow

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/transaction-processing-flows.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/transaction-processing-flows · updatedAt: 2026-09-28T14:08:47.000Z

<!-- source:begin path=docs/core-platform/transaction-processing-flows.md part=0-end -->

# Transaction processing flows

The Pismo platform supports multiple transaction processing flows. Depending on the transaction flow used, transactions might or might not participate in shared-limit processing, account hierarchy resolution, centralized billing, and centralized limit restoration.

Understanding the behavior of each flow is essential because it determines:

* Whether parent and child accounts are evaluated
* Whether transactions are consolidated into the centralizing account
* Whether shared limits are consumed across the hierarchy
* How reversals, cancellations, and limit restoration are processed

# Payment methods API

The [Payment methods API](https://developers.pismo.io/pismo-docs/reference/post-authorization) is the recommended integration path for new implementations and fully supports Commercial cards shared-limit functionality.

The API is hierarchy-aware when:

* The account hierarchy has been configured
* Shared limits have been enabled through the `impact_parent_accounts `balance configuration

When these requirements are met, debit and credit operations affect all applicable accounts in the hierarchy rather than only the originating account.

## Supported operations

The following Payment methods API operations support Commercial cards.

* [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization)
* [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments)
* [Confirm pre-authorized cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payment-confirm)
* [Cancel cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments-cancel)

## Shared-limit behavior

When a supported transaction reaches the Payment methods API:

* The platform resolves the applicable account hierarchy.
* Shared-limit validations are performed.
* Impacted accounts are identified.
* Ledger impacts are applied across the configured hierarchy.

Both debit and credit transactions can participate in this process.

<Callout icon="📘" theme="info">
  Transfers processed through the Payment methods API do not participate in shared-limit behavior. The following configurations do not apply to transfers.

  * `impact_parent_accounts`
  * `update_balance_after_discharge`
</Callout>

# Card network authorization flows

Commercial cards supports transactions originating from card networks. Unlike the Payment methods API, network transactions participate in shared-limit processing only under specific conditions.

To enter the hierarchy-aware flow:

* You must configure the account hierarchy
* You must enable `impact_parent_accounts` in the account's [balance configuration.](https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview)
* The network message type must be supported.

Both debit and credit transactions can participate when these conditions are met. Network-originated refunds and credit vouchers follow the same routing rules as purchases.

## Authorizations

Dual-message authorizations support Commercial cards shared-limit processing if you `impact_parent_accounts`. The same behavior applies to authorization advice messages that communicate the card network's decision after the transaction has been processed.

<Callout icon="📘" theme="info">
  Single-message authorizations do not participate in Commercial cards shared-limit processing, regardless of configuration.
</Callout>

## Reversals

When an authorization originally participated in shared-limit processing, subsequent reversal and reversal advice messages follow the same hierarchy-aware path. The Pismo platform uses the configuration recorded on the original authorization to determine how to process the reversal. As a result, limit restoration and account impacts follow the same hierarchy used during the original authorization.

## Clearing

Commercial cards also supports shared-limit processing during clearing events.

The following clearing operations are supported:

* Clearing confirmation
* Full cancellation
* Partial cancellation

### Matched clearing

When a prior authorization exists, the platform uses the configuration stored with the original authorization to determine whether shared-limit processing applies.

### Unmatched clearing

When a clearing message arrives without a matching authorization, the platform evaluates the account's current balance configuration to determine whether the transaction should follow the hierarchy-aware flow.

# Payments API

The Payments API is Pismo's original payments product.

Although still supported, it differs significantly from the Payment methods API because it is not hierarchy-aware.

The Payments API:

* Does not resolve account hierarchies.
* Does not identify parent accounts.
* Does not identify child accounts.
* Does not automatically consolidate activity into a centralizing account.

Instead, all operations affect only the account specified in the request. For most Commercial cards implementations, the Payment methods API is the preferred option.

# Choosing the appropriate flow

The following table summarizes the differences between the available transaction flows.

| Transaction flow            | Hierarchy-aware debits | Hierarchy-aware credits | Recommended for Commercial cards                                          |
| :-------------------------- | :--------------------- | :---------------------- | :------------------------------------------------------------------------ |
| Payment methods API         | Yes                    | Yes                     | Yes                                                                       |
| Card network authorizations | Yes, when configured   | Yes, when configured    | Yes                                                                       |
| Payments API                | No                     | Limited                 | **No.** Pismo recommends that you use one of the other transaction flows. |

The Payment methods API provides the most complete Commercial cards experience because it supports hierarchy resolution, shared-limit processing, centralized account behavior, and coordinated limit restoration.

Card network authorization flows also support Commercial cards when the appropriate configuration is enabled and supported message types are used.

The Payments API remains available but should be used with an understanding of its hierarchy limitations and operational constraints.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /payment-methods/v1/authorization` | `post-authorization` | Request authorization | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `POST /payment-methods/v2/payments` | `post-payments` | Create cash-in or cash-out | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `POST /payment-methods/v2/payments/confirm` | `post-payment-confirm` | Confirm pre-authorized cash-in or cash-out | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-02 |
| `POST /payment-methods/v2/payments/cancel` | `post-payments-cancel` | Cancel cash-in or cash-out | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |

### Operation essentials

- **`POST /payment-methods/v1/authorization`** (`post-authorization`): security `BearerAuth`; required parameters none declared; required body fields `currency_code`, `mti`, `network`; response statuses 200, 201, 400, 401, 403, 422, 500; error codes in examples `WONA0001`, `WONA0004`, `WONA0005`, `WONA0006`, `WONA0011`, `WONA0012`, `WONA0013`, `WONA0015`, `WONA0016`, `WONA0018`, `WONA0019`, `WONA0020`, `WONA0032`, `WONA0033`, `WONA0036`, `WONA039`, `WONA040`, `WONA041`, `WONA042`, `WONA043`, `EINS0004`, `EINS0005`, `EINS0006`, `EINS0010`, `EINS0011`, `EINS0012`, `EINS0015`, `EINS0016`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `payment-methods-authorization-1`, `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/payments`** (`post-payments`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `amount`, `processing_code`, `tracking_id`; response statuses 200, 201, 400, 401, 409, 422, 500; error codes in examples `WONP0001`, `WONB0001`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/payments/confirm`** (`post-payment-confirm`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `original_tracking_id`; response statuses 200, 202, 400, 404, 409, 422, 500; error codes in examples `WONP0010`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/payments/cancel`** (`post-payments-cancel`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `original_tracking_id`; response statuses 200, 201, 400, 404, 409, 422, 500; error codes in examples `WONP0001`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-authorization` | `payment-methods-authorization-1` |
| `post-authorization` | `platform-authorization-platform-authorization-1` |
| `post-payment-confirm` | `platform-authorization-platform-authorization-1` |
| `post-payments` | `platform-authorization-platform-authorization-1` |
| `post-payments-cancel` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/transaction-processing-flows.md`: updatedAt 2026-09-28T14:08:47.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/transaction-processing-flows.md` | whole document | https://developers.pismo.io/pismo-docs/docs/transaction-processing-flows | `dd8a2d0d808982f8…` | 2026-09-28T14:08:47.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-CORE-balance-configurations` — Balance configurations and filter templates
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
