---
ku_id: KU-CORE-commercial-cards
title: Commercial cards programs
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/corporate-card-programs.md
  sha256: 790e62ec21775183f7d7f45e617bb8fc6e1cfb03fcd9a91d92ce7ba9fa2b87ac
  url: https://developers.pismo.io/pismo-docs/docs/corporate-card-programs
  role: primary_guide
  updated_at: '2026-09-21T17:47:49.000Z'
- path: docs/core-platform/how-to-implement-a-commercial-cards-program.md
  sha256: dcbf6b9cd06614fccdafe6b632a7fd72866bc54c64228f4715f19dbf8c4ddc8b
  url: https://developers.pismo.io/pismo-docs/docs/how-to-implement-a-commercial-cards-program
  role: primary_guide
  updated_at: '2026-09-21T17:50:18.000Z'
operations:
- patch-accounts-v1-accounts
- patch-config-by-tenant
- post-acceptance-by-tenant
- post-acquisitions-v3-s2s-applications
- post-config-by-tenant
- post-v1-balances-config
- put-v1-balances-config
related_kus:
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-balance-config-beta--balance-configurations
- KU-API-core-platform-balance-watcher--limit-acceptance-configurations
- KU-API-core-platform-balance-watcher--limit-configurations
- KU-API-core-platform-payment-configurations--payment-method-acceptances
- KU-API-core-platform-payment-configurations--payment-method-configurations
- KU-CORE-accounts-overview
- KU-CORE-balance-configurations
- KU-CORE-transaction-processing-flows
- KU-EVT-catalogue-account
- KU-EVT-catalogue-other-domains
- KU-PAY-payment-configurations
grouping_rationale: Concept and implementation steps.
---

# Commercial cards programs

**KU ID:** `KU-CORE-commercial-cards` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Concept and implementation steps.

Scope as stated in `docs/core-platform/corporate-card-programs.md`:

> A **Commercial cards** program enables you to manage spending across multiple accounts using a shared credit structure. Instead of assigning independent limits to individual cardholders, you create hierarchical account structures that share and distribute available credit across departments, teams, or employees. This provides centralized spending controls, consolidated billing, and shared limit management across an organization's account hierarchy.

Scope as stated in `docs/core-platform/how-to-implement-a-commercial-cards-program.md`:

> To implement a Commercial cards program, follow these steps.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/corporate-card-programs.md`: Commercial cards overview; Account hierarchy; Centralizing account; Authorization; Transactions and statements; Payments; Common use cases for Commercial cards
- `docs/core-platform/how-to-implement-a-commercial-cards-program.md`: How to implement a Commercial cards program; 1. Create the account hierarchy; 2. Configure the centralizing account; 3. Enable shared-limit processing; 4. Enable limit restoration

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 9 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/corporate-card-programs.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/corporate-card-programs · updatedAt: 2026-09-21T17:47:49.000Z

<!-- source:begin path=docs/core-platform/corporate-card-programs.md part=0-end -->

# Commercial cards overview

A **Commercial cards** program enables you to manage spending across multiple accounts using a shared credit structure. Instead of assigning independent limits to individual cardholders, you create hierarchical account structures that share and distribute available credit across departments, teams, or employees. This provides centralized spending controls, consolidated billing, and shared limit management across an organization's account hierarchy.

Commercial cards is a cross-product capability that you can use across multiple transaction processing flows. Depending on the flow, the Pismo platform applies the same shared-limit hierarchy and authorization principles while adapting processing to the specific channel and transaction type. For more information about transaction processing flows, refer to the [Transaction processing flows](https://developers.pismo.io/pismo-docs/docs/transaction-processing-flows) guide.

# Account hierarchy

The Pismo platform lets you to organize a program's accounts in a parent-child hierarchy. This is a general platform feature—that is, it's not specific to Commercial cards. For more information about account hierarchies, refer to the [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview) guide.

In a Commercial cards program, each account in the hierarchy can participate in a **shared limit** structure, enabling you to control spending activity at multiple levels. Shared limits allow multiple accounts to consume credit from the same limit structure.

## Centralizing account

In the account hierarchy for a Commercial cards program, you designate one account as the **centralizer** or **centralizing account**.

The centralizing account is responsible for:

* Consolidating transactions
* Receiving payments
* Generating statements
* Supporting accounting processes

This lets you manage spending and billing from a single account.

<Callout icon="🚧" theme="warn">
  You should not designate more than one account in a hierarchy as a centralizer. The Pismo platform does not prevent you from doing so, but this can lead to unpredictable behavior.
</Callout>

# Authorization

The Pismo platform validates available credit across the account hierarchy during a transaction authorization. It approves a transaction only if all required accounts meet the necessary validation and limit requirements.

Authorization events might include information about the accounts impacted by the transaction, providing visibility into how shared limits are consumed.

# Transactions and statements

The Pismo platform records transactions in the centralizing account, enabling consolidated billing and reporting. Transaction records also identify the original account that initiated the purchase.

Your organization benefits from:

* Centralized statements
* Consolidated invoice management
* Simplified reconciliation
* Visibility across departments and users

# Payments

The Pismo platform processes payments through the centralizing account. When it receives a payment, limit restoration should follow the configured payment and discharge process, helping maintain consistency across the shared limit hierarchy.

You must enable this behavior by setting `authorization.update_balance_after_discharge`=`true` in the acceptance configuration associated with the invoice-payment processing code. For example, you could do this at the organization level using the [Create org configuration](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) or [Update org configuration ](https://developers.pismo.io/pismo-docs/reference/patch-config-by-tenant) endpoints. For more information about payment configuration, refer to the [Payment methods configurations overview](https://developers.pismo.io/pismo-docs/docs/payment-configurations) guide.

# Common use cases for Commercial cards

The following are some of the most common use cases for Commercial cards.

* **Corporate card programs:** Provide employees with access to a shared company credit facility while maintaining centralized control over spending.
* **Fleet card programs:** Manage spending across vehicles, drivers, and operational units using a shared limit structure.
* **Department-based budgeting:** Allocate spending capacity to departments while enforcing organization-wide credit controls.
<!-- source:end -->

### Source 2: `docs/core-platform/how-to-implement-a-commercial-cards-program.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/how-to-implement-a-commercial-cards-program · updatedAt: 2026-09-21T17:50:18.000Z

<!-- source:begin path=docs/core-platform/how-to-implement-a-commercial-cards-program.md part=0-end -->

# How to implement a Commercial cards program

To implement a Commercial cards program, follow these steps.

# 1. Create the account hierarchy

Parent-child relationships define how limits are shared. A hierarchy can contain multiple levels. To organize the accounts in a program, specify the ID of the parent account for each account in the hierarchy, except for the top-level account, which has no parent. You can specify the parent ID when creating an account using the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoint. To specify the parent ID for an existing account, use  the [Update account](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v1-accounts) endpoint. For more information, refer to the [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview) guide.

# 2. Configure the centralizing account

The hierarchy must identify the centralizing account. This is normally the top-level account in the hierarchy. Do this by running either [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) or [Update account](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v1-accounts) and setting the `centralizer` field to `true` in the body parameters.

<Callout icon="📘" theme="info">
  Make sure all accounts that are not centralizers have the `centralizer` field set to `false`. This is the default.
</Callout>

# 3. Enable shared-limit processing

To control which organizations and programs can use shared limits, you must use [balance configuration](https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview).

If you haven't already created a balance configuration, create one using the [Create balance configuration ](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config) endpoint. To enable shared limit processing, include a `global_configs` object with `impact_parent_accounts` set to `true`.

If a balance configuration already exists and doesn't have a `global_configs` object with `impact_parent_accounts` set to `true`, use the [Replace balance configuration](https://developers.pismo.io/pismo-docs/reference/put-v1-balances-config) endpoint to replace it with one that does.

Once enabled, authorizations evaluate credit availability across all impacted accounts in the hierarchy.

# 4. Enable limit restoration

After the Pismo platform discharges a payment, it should restore the limits on the centralizer and all its child accounts. Enable this behavior by setting `authorization.update_balance_after_discharge`=`true` in the acceptance configuration associated with the invoice-payment processing code. You can use the [platform configuration](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) or [acceptance configuration](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant) endpoints to do this. For more information, refer to the [Payment methods configurations overview](https://developers.pismo.io/pismo-docs/docs/payment-configurations) guide.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/config` | `post-config-by-tenant` | Create limit config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-configurations |
| `POST /payment-methods-configs/v1/configs` | `post-config-by-tenant` | Create org configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `PATCH /payment-methods-configs/v1/configs` | `patch-config-by-tenant` | Update org configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `PATCH /accounts/v1/accounts/{accountId}` | `patch-accounts-v1-accounts` | Update account | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /v1/balances-config` | `post-v1-balances-config` | Create balance configuration | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--balance-configurations |
| `PUT /v1/balances-config/{configId}` | `put-v1-balances-config` | Replace balance configuration | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--balance-configurations |
| `POST /v1/acceptance/processing-code/{processingCode}` | `post-acceptance-by-tenant` | Create limit acceptance config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-acceptance-configurations |
| `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `post-acceptance-by-tenant` | Create org acceptance configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-acceptances |

### Operation essentials

- **`POST /v1/config`** (`post-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-config-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/configs`** (`post-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-config-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`PATCH /payment-methods-configs/v1/configs`** (`patch-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples none; events none listed.
- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`PATCH /accounts/v1/accounts/{accountId}`** (`patch-accounts-v1-accounts`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 401, 404, 500; error codes in examples none; events `account-account-change-2`.
- **`POST /v1/balances-config`** (`post-v1-balances-config`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields none declared; response statuses 201, 400, 404, 500; error codes in examples `EBCF0321`, `EBCF0320`, `EBCF0317`, `EBLC9999`; events none listed.
- **`PUT /v1/balances-config/{configId}`** (`put-v1-balances-config`): security `BearerAuth`; required parameters `configId` (path), `x-tenant` (header); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `WBLC0022`, `EBLC9999`; events none listed.
- **`POST /v1/acceptance/processing-code/{processingCode}`** (`post-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}`** (`post-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-accounts-v1-accounts` | `account-account-change-2` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/corporate-card-programs.md`: updatedAt 2026-09-21T17:47:49.000Z.
- `docs/core-platform/how-to-implement-a-commercial-cards-program.md`: updatedAt 2026-09-21T17:50:18.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/corporate-card-programs.md` | whole document | https://developers.pismo.io/pismo-docs/docs/corporate-card-programs | `790e62ec21775183…` | 2026-09-21T17:47:49.000Z |
| `docs/core-platform/how-to-implement-a-commercial-cards-program.md` | whole document | https://developers.pismo.io/pismo-docs/docs/how-to-implement-a-commercial-cards-program | `dcbf6b9cd06614fc…` | 2026-09-21T17:50:18.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-balance-config-beta--balance-configurations` — API reference: Core platform - Balance configurations — Balance configurations
- `KU-API-core-platform-balance-watcher--limit-acceptance-configurations` — API reference: Core platform - Balance watcher — Limit acceptance configurations
- `KU-API-core-platform-balance-watcher--limit-configurations` — API reference: Core platform - Balance watcher — Limit configurations
- `KU-API-core-platform-payment-configurations--payment-method-acceptances` — API reference: Core platform - Payment configurations — Payment method acceptances
- `KU-API-core-platform-payment-configurations--payment-method-configurations` — API reference: Core platform - Payment configurations — Payment method configurations
- `KU-CORE-accounts-overview` — Accounts
- `KU-CORE-balance-configurations` — Balance configurations and filter templates
- `KU-CORE-transaction-processing-flows` — Transaction processing flows
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-payment-configurations` — Payment methods configurations overview
