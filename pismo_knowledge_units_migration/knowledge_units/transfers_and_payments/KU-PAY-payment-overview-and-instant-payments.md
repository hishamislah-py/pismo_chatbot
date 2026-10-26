---
ku_id: KU-PAY-payment-overview-and-instant-payments
title: Banking payment overview, instant payments and integrated payments
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/payment-overview.md
  sha256: 0de7e34d1d200dcfd92b7d2cad8743a60eb4346696bd9acccd1ecd8b4286a918
  url: https://developers.pismo.io/pismo-docs/docs/payment-overview
  role: primary_guide
  updated_at: '2026-08-06T15:12:31.000Z'
- path: docs/core-banking/instant-payments-overview.md
  sha256: 533d1baa91fba867aeed21ab40a3aeea19c1d64ecb89533bd726f9a05b7cfd8d
  url: https://developers.pismo.io/pismo-docs/docs/instant-payments-overview
  role: primary_guide
  updated_at: '2026-04-24T22:19:55.000Z'
- path: docs/core-banking/integrated-payments.md
  sha256: 32839946f94f5be8d2630ed5f4bd16af0514ae94b25ef1850a7c6960dfff6439
  url: https://developers.pismo.io/pismo-docs/docs/integrated-payments
  role: primary_guide
  updated_at: '2026-05-11T15:02:35.000Z'
operations:
- corporate-v2-post-payments
- get-accounts-v1-accounts-status-reasons
- post-corporate-v2-earmarks
related_kus:
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-BANK-managing-account-statuses
- KU-CORE-flex-controls
- KU-CORE-processing-codes-and-transaction-types
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-PAY-faster-payment-system
- KU-PAY-payments
- KU-PAY-pix-instant-payments
- KU-PAY-united-payments-interface
grouping_rationale: Overview pages for banking payments.
---

# Banking payment overview, instant payments and integrated payments

**KU ID:** `KU-PAY-payment-overview-and-instant-payments` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Overview pages for banking payments.

Scope as stated in `docs/core-banking/payment-overview.md`:

> The transaction banking payment feature of the Pismo platform provides functionalities that help you perform different payment transactions such as posting credit or debit payments, force transfer payments, and multi-leg payments. Key functions include:

Scope as stated in `docs/core-banking/instant-payments-overview.md`:

> **Instant payments** refers to digital systems that process payments and enable fund transfers in real time, 24 hours a day, 365 days a year, where the recipient can use the available funds immediately. Instant payment types include:

Scope as stated in `docs/core-banking/integrated-payments.md`:

> Integrated payments is a core banking API that processes transactions affecting customer balances. It supports use cases such as bill payments, tax payments, and wire transfers (for example, TED). Integrated payments is not a standalone product. It acts as an orchestration layer for financial products that move money into or out of customer accounts.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/payment-overview.md`: Payment overview; Post payment; Post credit payments; Post debit payments; Execute fund transfer; Execute force transfers
- `docs/core-banking/instant-payments-overview.md`: Instant payments
- `docs/core-banking/integrated-payments.md`: Integrated payments

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/payment-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/payment-overview · updatedAt: 2026-08-06T15:12:31.000Z

<!-- source:begin path=docs/core-banking/payment-overview.md part=0-end -->

# Payment overview

The transaction banking payment feature of the Pismo platform provides functionalities that help you perform different payment transactions such as posting credit or debit payments, force transfer payments, and multi-leg payments. Key functions include:

* **Post payment**: Use this feature to post both credit and debit transactions to an account. Additionally, you can initiate force transfer payments.
* **Post multi-leg payment**: Execute multiple payment transactions simultaneously. Rather than submitting individual payment requests, you can consolidate different payment types (credit, debit, or a combination of both) into a single request for enhanced efficiency and convenience.

# Post payment

The Pismo platform features a [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) API that enables transaction banking account holders to transfer funds, and conduct cash-in and cash-out transactions. This API leverages many features of the Core payments API, but is particularly tailored for transaction banking clients..

[Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) enables the posting of debits and credits to an account and facilitating fund transfers between them. Follow the guidelines below to use the API for posting credits, debits, earmark payments, or conducting fund transfers. For details about how the Payments API works in general, refer to [Payments and transfers](https://developers.pismo.io/pismo-docs/docs/payments).

## Post credit payments

When initiating credit payments, ensure that you include a `credit` object containing a valid `processing_code` and an `external_account_id`. These attributes identify the target account and the financial transaction type. The following table describes these fields:

| Field name            | Description                                                                                                                                                                                            |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `external_account_id` | Identifies the external ID of the account to which the credit payment is posted. This ID is different from the one provided to you by Pismo.                                                           |
| `processing_code`     | Defines a financial operation type and how the platform handles it. For details about processing codes, refer to [processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types). |

## Post debit payments

Likewise, for debit payments, you must provide values for `processing_code` and `external_account_id` within the `debit` object. Note that if the debit object includes an `earmark_id` value, the debit amount is deducted directly from the earmark balance. The `earmark_id` indicates the ID the earmarked balance from which the amount is withdrawn, the Earmark ID is generated by the [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint.

## Execute fund transfer

To execute fund transfers, include both credit and debit objects. If you specify an `earmark_id` value within the `debit` object, the transferred amount is deducted directly from the earmark balance.

### Execute force transfers

To execute force transfers, include both a `credit` and a `debit` object, and set the `force_post` field to `true`. Note that force transfers from an earmark balance are not supported.

If an account has a status that prevents force operations, the transfer will fail. For more information, refer to [Manage account statuses](https://developers.pismo.io/pismo-docs/docs/managing-account-statuses).

Reasons that restrict force credit or debit operations are:

| Reason ID type                           | Behavior                                                                  |
| :--------------------------------------- | :------------------------------------------------------------------------ |
| **ANY**                                  | Any transaction will be posted without restrictions.                      |
| **MANUAL**                               | Only force transactions are allowed.                                      |
| **CREDIT ONLY**                          | Only credits and force transactions are allowed.                          |
| **DEBIT ONLY**                           | Only debits and force transactions are allowed.                           |
| **CREDIT ONLY - NO FORCE DEBIT ALLOWED** | No force debit transactions allowed.                                      |
| **DEBIT ONLY - NO FORCE CREDIT ALLOWED** | No force credit transactions allowed.                                     |
| **ANY - NO FORCE ALLOWED**               | All transactions allowed, except force transactions.                      |
| **MANUAL - NO FORCE ALLOWED**            | Manual add or update transactions are allowed, except force transactions. |

To get a list of available reasons for a specific account status, use the [List account status reasons](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts-status-reasons) endpoint.

For sample payloads for each of the aforementioned payment types, refer to the examples provided in [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint.
<!-- source:end -->

### Source 2: `docs/core-banking/instant-payments-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/instant-payments-overview · updatedAt: 2026-04-24T22:19:55.000Z

<!-- source:begin path=docs/core-banking/instant-payments-overview.md part=0-end -->

# Instant payments

**Instant payments** refers to digital systems that process payments and enable fund transfers in real time, 24 hours a day, 365 days a year, where the recipient can use the available funds immediately. Instant payment types include:

* **Instant bank transfers**—Between payment service providers (PSPs), using account numbers.
* **Instant payment transfers**—From one bank account to another using an **alias** (such as a mobile phone number, email address, or similarly unique identifier).

The Pismo platform currently integrates with [Pix](https://developers.pismo.io/pismo-docs/docs/pix-instant-payments) (Brazil), [Faster Payments](https://developers.pismo.io/pismo-docs/docs/faster-payment-system) (UK), and [United Payments Interface](https://developers.pismo.io/pismo-docs/docs/united-payments-interface)  (India) for instant payments.

Pismo is working towards integrating with payment rails globally, including regions such as Europe, Asia, Latin America, and North America. Reach out to your Pismo representative for more information.

<Callout icon="📘" theme="info">
  You can apply [flex controls](https://developers.pismo.io/pismo-docs/docs/flex-controls) to transactions and configure the amount and time. In Brazil, avoid high-value transactions at night from 8 PM to 6 AM.
</Callout>
<!-- source:end -->

### Source 3: `docs/core-banking/integrated-payments.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/integrated-payments · updatedAt: 2026-05-11T15:02:35.000Z

<!-- source:begin path=docs/core-banking/integrated-payments.md part=0-end -->

# Integrated payments

Integrated payments is a core banking API that processes transactions affecting customer balances. It supports use cases such as bill payments, tax payments, and wire transfers (for example, TED). Integrated payments is not a standalone product. It acts as an orchestration layer for financial products that move money into or out of customer accounts.

Refer to the following guides for more information.

* [Instant payments](https://developers.pismo.io/pismo-docs/docs/instant-payments-overview)
* <Anchor label="PIX instant payments (Brazil)" target="_blank" href="doc:pix-instant-payments">PIX instant payments (Brazil)</Anchor>
* <Anchor label="Faster Payments (UK)" target="_blank" href="doc:faster-payment-system">Faster Payments (UK)</Anchor>
* <Anchor label="RuPay and UPI instant payments (India)" target="_blank" href="doc:united-payments-interface">RuPay and UPI instant payments (India)</Anchor>
* <Anchor label="Bank slips" target="_blank" href="doc:bank-slips">Bank slips</Anchor>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /corporate/v2/payments` | `corporate-v2-post-payments` | Post payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `POST /corporate/v2/earmarks` | `post-corporate-v2-earmarks` | Create earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `GET /accounts/v1/accounts-status/reasons` | `get-accounts-v1-accounts-status-reasons` | List status reasons V1 (deprecated) | `api-specs/Core_platform_-_Accounts.yaml` | **yes** | KU-API-core-platform-accounts--statuses-and-reasons |

### Operation essentials

- **`POST /corporate/v2/payments`** (`corporate-v2-post-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`; response statuses 201, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WPMT0017`, `WPMT0011`, `WPMT0053`, `WPMT0018`, `WPMT0029`, `WPMT0030`, `WPMT0031`, `WPMT0062`, `WPMT0063`, `WCAC0010`, `WPMT0001`, `WPMT0061`, `WPMT0015`, `WPMT0016`, `WPMT0003`, `WPMT0004`, `WPMT0005`, `WPMT0006`, `WPMT0009`, `WPMT0010`, `WPMT0021`, `WEAM0008`, `WEAM0006`, `WPMT0050`, `WEAM0017`, `WEAM0019`, `WPMT0022`, `WPMT0023`, `WPMT0024`, `WPMT0025`, `WPMT0026`, `WCMN0002`, `WPMT0028`, `WPMT0045`, `WPMT0049`, `WPMT0036`, `WPMT0044`, `WPMT0051`, `WPMT0035`, `WPMT0046`, `WPMT0054`, `WPMT0055`, `WPMT0056`, `WPMT0058`, `WPMT0008`, `WPMT0014`, `WPMT0019`, `WCAC0002`, `WCAC0012`, `WPMT0002`, `WCAC0001`, `WEAM0007`, `WPMT0007`, `WPMT0052`, `WEAM0049`, `WPMT0047`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`POST /corporate/v2/earmarks`** (`post-corporate-v2-earmarks`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `internal_operation`; response statuses 201, 400, 401, 403, 409, 423, 500; error codes in examples `WOBK0007`, `WEAM0014`, `WEAM0015`, `WEAM0005`, `WEAM0006`, `WEAM0017`, `WEAM0019`, `WEAM0026`, `WEAM0036`, `WEAM0037`, `WEAM0039`, `WEAM0040`, `WEAM0047`, `WEAM0042`, `WEAM0043`, `WEAM0044`, `WEAM0045`, `WEAM0046`, `WEAM0016`, `WEAM0018`, `WEAM0009`, `WEAM0020`, `WEAM0023`, `WEAM0024`, `WEAM0001`, `WEAM0025`, `WEAM0034`, `WEAM0033`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-earmark-1`, `platform-authorization-platform-authorization-1`, `transaction-creation-1`.
- **`GET /accounts/v1/accounts-status/reasons`** (`get-accounts-v1-accounts-status-reasons`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 404, 500; error codes in examples none; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-v2-post-payments` | `account-balances-balance-change-1` |
| `post-corporate-v2-earmarks` | `account-balances-balance-change-1` |
| `corporate-v2-post-payments` | `accounting-entry-creation-1` |
| `corporate-v2-post-payments` | `availables-change-available-1` |
| `post-corporate-v2-earmarks` | `availables-change-available-1` |
| `post-corporate-v2-earmarks` | `corporate-earmark-1` |
| `corporate-v2-post-payments` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v2-earmarks` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-payments` | `rules-evaluation-requested-1` |
| `post-corporate-v2-earmarks` | `transaction-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/payment-overview.md`: updatedAt 2026-08-06T15:12:31.000Z.
- `docs/core-banking/instant-payments-overview.md`: updatedAt 2026-04-24T22:19:55.000Z.
- `docs/core-banking/integrated-payments.md`: updatedAt 2026-05-11T15:02:35.000Z.
- Links to `get-accounts-v1-accounts-status-reasons`, which is marked `deprecated: true` in `api-specs/Core_platform_-_Accounts.yaml`.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/payment-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/payment-overview | `0de7e34d1d200dcf…` | 2026-08-06T15:12:31.000Z |
| `docs/core-banking/instant-payments-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/instant-payments-overview | `533d1baa91fba867…` | 2026-04-24T22:19:55.000Z |
| `docs/core-banking/integrated-payments.md` | whole document | https://developers.pismo.io/pismo-docs/docs/integrated-payments | `32839946f94f5be8…` | 2026-05-11T15:02:35.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-BANK-managing-account-statuses` — Manage account statuses
- `KU-CORE-flex-controls` — Flexible transaction controls: concepts, examples and simulation
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-PAY-faster-payment-system` — Faster Payments (UK)
- `KU-PAY-payments` — Payments and transfers
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
- `KU-PAY-united-payments-interface` — RuPay and UPI instant payments (India)
