---
ku_id: KU-EVT-interest-management-data-events
title: Banking - Interest management
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/interest-management-data-events.md
  sha256: 4893dc673bced3a07075e0faefdff1c93e5a35999f0f81952a4cf31c0992ff31
  url: https://developers.pismo.io/pismo-docs/docs/interest-management-data-events
  role: primary_guide
  updated_at: '2026-08-06T23:10:24.000Z'
operations:
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-create-savings-account-product
- interest-bearing-v1-deposit-attach-account
- interest-bearing-v1-deposit-attach-program
- interest-bearing-v1-deposit-detach-account
- interest-bearing-v1-patch-deposit-product
- interest-bearing-v1-patch-savings-account-product
- interest-bearing-v1-savings-account-attach-account
- interest-bearing-v1-savings-account-attach-program
- interest-bearing-v1-savings-account-detach-account
- post-v1-interest-deposit
- post-v1-interest-plan
related_kus:
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-bearing-accounts--program-attachment
- KU-API-banking-interest-engine--interest-engine
- KU-API-banking-interest-operations--interest-engine
- KU-EVT-catalogue-deposit
- KU-EVT-catalogue-interest
- KU-EVT-catalogue-other-domains
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Banking - Interest management

**KU ID:** `KU-EVT-interest-management-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/interest-management-data-events.md`:

> This table lists the interest management endpoints and the events they generate. For information on setting up event notifications, refer to [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/interest-management-data-events.md`: Banking - Interest management

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 12 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/interest-management-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/interest-management-data-events · updatedAt: 2026-08-06T23:10:24.000Z

<!-- source:begin path=docs/data-and-reporting/interest-management-data-events.md part=0-end -->

# Banking - Interest management

This table lists the interest management endpoints and the events they generate. For information on setting up event notifications, refer to [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint                                                                                      | Event                                                                                                                            |
| :-------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| **Interest management API**                                                                   |                                                                                                                                  |
| [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan)                                             | [Interest Plan Creation Succeeded](https://developers.pismo.io/events/docs/interest-management-interest-plan-creation-success-1) |
| **Interest operations API**                                                                   |                                                                                                                                  |
| [Deposit money](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-deposit)                                                 | [Interest deposit succeeded](https://developers.pismo.io/events/docs/interest-management-interest-deposit-success-1)             |
| [Deposit money](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-deposit)                                                 | [Interest deposit failed](https://developers.pismo.io/events/docs/interest-management-interest-deposit-failure-1)                |
| [Deposit money](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-deposit)                                                 | [Interest registration succeeded](https://developers.pismo.io/events/docs/interest-management-interest-registration-success-1)   |
| [Deposit money](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-deposit)                                                 | [Interest registration failed](https://developers.pismo.io/events/docs/interest-management-interest-registration-failure-1)      |
| **Interest-bearing accounts API**                                                             |                                                                                                                                  |
| [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)                      | [Deposit product created](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)           |
| [Update deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-patch-deposit-product)                       | [Deposit product updated](https://developers.pismo.io/events/docs/deposit-product-update-1)                                      |
| [Create savings account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-savings-account-product)              | [Savings account product created](https://developers.pismo.io/events/docs/savings-account-product-creation-1)                    |
| [Update savings account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-patch-savings-account-product)               | [Savings account product updated](https://developers.pismo.io/events/docs/savings-account-product-update-1)                      |
| [Attach deposit to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account)                   | [Account attached](https://developers.pismo.io/events/docs/deposit-product-account-attach-1)                                     |
| [Detach deposit from account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-detach-account)                 | [Account detached](https://developers.pismo.io/events/docs/deposit-product-account-detach-1)                                     |
| [Attach savings account to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-attach-account)   | [Account attached](https://developers.pismo.io/events/docs/deposit-product-account-attach-1)                                     |
| [Detach savings account from account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-detach-account) | [Account detached](https://developers.pismo.io/events/docs/deposit-product-account-detach-1)                                     |
| [Attach deposit product to program](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-program)           | [Program attached](https://developers.pismo.io/events/docs/deposit-product-program-attach-1)                                     |
| [Attach savings accounts to program](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-attach-program)  | [Program attached](https://developers.pismo.io/events/docs/deposit-product-program-attach-1)                                     |

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/interest/plan` | `post-v1-interest-plan` | Create interest plan | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `POST /v1/interest/deposit` | `post-v1-interest-deposit` | Deposit money | `api-specs/Banking_-_Interest_operations.yaml` | no | KU-API-banking-interest-operations--interest-engine |
| `POST /v1/deposits` | `interest-bearing-v1-create-deposit-product` | Create deposit product | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `PATCH /v1/deposits/{productId}` | `interest-bearing-v1-patch-deposit-product` | Update deposit product | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/savings-accounts` | `interest-bearing-v1-create-savings-account-product` | Create savings account product | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `PATCH /v1/savings-accounts/{productId}` | `interest-bearing-v1-patch-savings-account-product` | Update savings account product | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/deposits/accounts/{accountId}/attach` | `interest-bearing-v1-deposit-attach-account` | Attach deposit to account | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/deposits/accounts/{accountId}/detach` | `interest-bearing-v1-deposit-detach-account` | Detach deposit from account | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/savings-accounts/accounts/{accountId}/attach` | `interest-bearing-v1-savings-account-attach-account` | Attach savings account to account | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/savings-accounts/accounts/{accountId}/detach` | `interest-bearing-v1-savings-account-detach-account` | Detach savings account from account | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/deposits/programs/{programId}/attach` | `interest-bearing-v1-deposit-attach-program` | Attach deposit product to program | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `POST /v1/savings-accounts/programs/{programId}/attach` | `interest-bearing-v1-savings-account-attach-program` | Attach savings accounts to program | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |

### Operation essentials

- **`POST /v1/interest/plan`** (`post-v1-interest-plan`): security `BearerAuth`; required parameters none declared; required body fields `accrual_basis`, `accrual_frequency`, `capitalization_frequency`, `currency_code`, `description`, `interest_type`, `start_date`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `interest-engine-interest-plan-creation-success-1`.
- **`POST /v1/interest/deposit`** (`post-v1-interest-deposit`): security `BearerAuth`; required parameters `content-type` (header), `authorization` (header); required body fields `tracking_id`, `account_id`, `interest_plan_id`, `amount`, `value_date`, `maturity_date`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `interest-engine-interest-deposit-failure-1`, `interest-engine-interest-deposit-success-1`, `interest-engine-interest-registration-failure-1`, `interest-engine-interest-registration-success-1`.
- **`POST /v1/deposits`** (`interest-bearing-v1-create-deposit-product`): security `BearerAuth`; required parameters none declared; required body fields `name`, `interest_plan_id`, `term_type`; response statuses 201, 400, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0393`, `EIBACC0007`; events `deposit-product-creation-1`.
- **`PATCH /v1/deposits/{productId}`** (`interest-bearing-v1-patch-deposit-product`): security `BearerAuth`; required parameters `productId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0007`; events `deposit-product-update-1`.
- **`POST /v1/savings-accounts`** (`interest-bearing-v1-create-savings-account-product`): security `BearerAuth`; required parameters none declared; required body fields `interest_plan_id`, `name`, `processing_codes`; response statuses 201, 400, 500; error codes in examples `EIBACC0008`, `EIBACC0007`; events `savings-account-product-creation-1`.
- **`PATCH /v1/savings-accounts/{productId}`** (`interest-bearing-v1-patch-savings-account-product`): security `BearerAuth`; required parameters `productId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0007`; events `savings-account-product-update-1`.
- **`POST /v1/deposits/accounts/{accountId}/attach`** (`interest-bearing-v1-deposit-attach-account`): security `BearerAuth`; required parameters `accountId` (path); required body fields `product_id`; response statuses 201, 400, 404, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0308`, `EIBACC0309`, `EIBACC0310`, `EIBACC0311`, `EIBACC0312`, `EIBACC0379`, `EIBACC0064`, `EIBACC0114`, `EIBACC0007`, `EIBACC0304`; events `deposit-product-account-attach-1`.
- **`POST /v1/deposits/accounts/{accountId}/detach`** (`interest-bearing-v1-deposit-detach-account`): security `BearerAuth`; required parameters `accountId` (path); required body fields `product_id`; response statuses 204, 400, 404, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0114`, `EIBACC0007`; events `deposit-product-account-detach-1`.
- **`POST /v1/savings-accounts/accounts/{accountId}/attach`** (`interest-bearing-v1-savings-account-attach-account`): security `BearerAuth`; required parameters `accountId` (path); required body fields `product_id`; response statuses 204, 400, 404, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0114`, `EIBACC0007`; events `deposit-product-account-attach-1`.
- **`POST /v1/savings-accounts/accounts/{accountId}/detach`** (`interest-bearing-v1-savings-account-detach-account`): security `BearerAuth`; required parameters `accountId` (path); required body fields `product_id`; response statuses 204, 400, 404, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0114`, `EIBACC0007`; events `deposit-product-account-detach-1`.
- **`POST /v1/deposits/programs/{programId}/attach`** (`interest-bearing-v1-deposit-attach-program`): security `BearerAuth`; required parameters `programId` (path); required body fields `product_id`; response statuses 201, 400, 404, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0317`, `EIBACC0318`, `EIBACC0308`, `EIBACC0309`, `EIBACC0310`, `EIBACC0311`, `EIBACC0312`, `EIBACC0379`, `EIBACC0064`, `EIBACC0106`, `EIBACC0007`, `EIBACC0304`; events `deposit-product-program-attach-1`.
- **`POST /v1/savings-accounts/programs/{programId}/attach`** (`interest-bearing-v1-savings-account-attach-program`): security `BearerAuth`; required parameters `programId` (path); required body fields `product_id`; response statuses 204, 400, 404, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0114`, `EIBACC0007`; events `deposit-product-program-attach-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `interest-bearing-v1-deposit-attach-account` | `deposit-product-account-attach-1` |
| `interest-bearing-v1-savings-account-attach-account` | `deposit-product-account-attach-1` |
| `interest-bearing-v1-deposit-detach-account` | `deposit-product-account-detach-1` |
| `interest-bearing-v1-savings-account-detach-account` | `deposit-product-account-detach-1` |
| `interest-bearing-v1-create-deposit-product` | `deposit-product-creation-1` |
| `interest-bearing-v1-deposit-attach-program` | `deposit-product-program-attach-1` |
| `interest-bearing-v1-savings-account-attach-program` | `deposit-product-program-attach-1` |
| `interest-bearing-v1-patch-deposit-product` | `deposit-product-update-1` |
| `post-v1-interest-deposit` | `interest-engine-interest-deposit-failure-1` |
| `post-v1-interest-deposit` | `interest-engine-interest-deposit-success-1` |
| `post-v1-interest-plan` | `interest-engine-interest-plan-creation-success-1` |
| `post-v1-interest-deposit` | `interest-engine-interest-registration-failure-1` |
| `post-v1-interest-deposit` | `interest-engine-interest-registration-success-1` |
| `interest-bearing-v1-create-savings-account-product` | `savings-account-product-creation-1` |
| `interest-bearing-v1-patch-savings-account-product` | `savings-account-product-update-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `deposit-product-account-attach-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-account-attach-1 | 3 | KU-EVT-catalogue-deposit |
| `deposit-product-account-detach-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-account-detach-1 | 2 | KU-EVT-catalogue-deposit |
| `deposit-product-program-attach-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-program-attach-1 | 2 | KU-EVT-catalogue-deposit |
| `deposit-product-update-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-update-1 | 1 | KU-EVT-catalogue-deposit |
| `interest-management-interest-plan-creation-success-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-management-interest-plan-creation-success-1 | 1 | KU-EVT-catalogue-interest |
| `savings-account-product-creation-1` | savings | 1 | https://developers.pismo.io/events/docs/savings-account-product-creation-1 | 1 | KU-EVT-catalogue-other-domains |
| `savings-account-product-update-1` | savings | 1 | https://developers.pismo.io/events/docs/savings-account-product-update-1 | 1 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/interest-management-data-events.md`: updatedAt 2026-08-06T23:10:24.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 11 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/interest-management-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/interest-management-data-events | `4893dc673bced3a0…` | 2026-08-06T23:10:24.000Z |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-bearing-accounts--program-attachment` — API reference: Banking - Interest-bearing accounts — Program attachment
- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-banking-interest-operations--interest-engine` — API reference: Banking - Interest operations — Interest engine
- `KU-EVT-catalogue-deposit` — Event catalogue: deposit
- `KU-EVT-catalogue-interest` — Event catalogue: interest
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
