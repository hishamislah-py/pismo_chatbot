---
ku_id: KU-BANK-how-overdraft-works
title: How overdraft works
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/how-overdraft-works.md
  sha256: cc5783fbd172ec9f4d9ed21537a30110afdf6ecd6ff51cce2d36754e7fe5dfe2
  url: https://developers.pismo.io/pismo-docs/docs/how-overdraft-works
  role: primary_guide
  updated_at: '2026-04-25T03:11:02.000Z'
operations:
- get-overdraft-account-attachment
- get-overdraft-product
- interest-bearing-v1-list-products
- patch-v1-account-limit
- post-attach-product-to-account
- post-attach-product-to-program
- post-detach-product-from-account
- post-overdraft-product
- post-v1-interest-plan
related_kus:
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-engine--interest-engine
- KU-API-banking-overdraft--account
- KU-API-banking-overdraft--product
- KU-API-banking-overdraft--program
- KU-API-core-platform-ledger--account-limits
- KU-EVT-catalogue-interest
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-overdraft
grouping_rationale: single source page
---

# How overdraft works

**KU ID:** `KU-BANK-how-overdraft-works` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/how-overdraft-works.md`:

> Overdraft is a financial service that allows you to continue making transactions even if there are insufficient funds in your account. This feature provides a safety net for individuals and businesses, ensuring that essential payments and purchases can still be made despite temporary shortfalls in available funds. By permitting your transactions to proceed when funds are insufficient, overdraft helps mitigate the potential disruptions and financial stress that might otherwise occur.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/how-overdraft-works.md`: How overdraft works; How to set up overdraft; Step 1: Set overdraft limit; Step 2: Create interest plan; Step 3: Create overdraft product; Step 4: Attach overdraft product to account; Detach overdraft product from account; Attach overdraft product to program; Check detach status; Additional endpoints

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 9 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/how-overdraft-works.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/how-overdraft-works · updatedAt: 2026-04-25T03:11:02.000Z

<!-- source:begin path=docs/core-banking/how-overdraft-works.md part=0-end -->

# How overdraft works

<br />

Overdraft is a financial service that allows you to continue making transactions even if there are insufficient funds in your account. This feature provides a safety net for individuals and businesses, ensuring that essential payments and purchases can still be made despite temporary shortfalls in available funds. By permitting your transactions to proceed when funds are insufficient, overdraft helps mitigate the potential disruptions and financial stress that might otherwise occur.

Pismo's overdraft service enables your account to access a predetermined amount (the account overdraft limit) authorized by the financial institution to cover for insufficient funds. Interest is typically calculated on the negative balance, and fees can be applied based on how long the account remains overdrawn.

# How to set up overdraft

Setting up overdraft involves these steps.

1. [Set overdraft limit](#step-1-set-overdraft-limit)
2. [Create interest plan](#step-2-create-interest-plan)
3. [Create overdraft product](#step-3-create-overdraft-product)
4. [Attach overdraft product to account](#step-4-attach-overdraft-product-to-account)

## Step 1: Set overdraft limit

Set your account overdraft limit by executing the [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit) endpoint with the `total_overdraft_limit` field set to the value of the limit.

This ensures that the account has a predefined limit that can be used for overdraft transactions.

## Step 2: Create interest plan

Use the [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan) endpoint to define how interest is calculated on an overdraft amount.

## Step 3: Create overdraft product

Use the [Create overdraft product](https://developers.pismo.io/pismo-docs/reference/post-overdraft-product) endpoint to create an overdraft product. If the product is successfully created, the endpoint returns a `201` response, and an event is generated which contains the parameters of the new product.

## Step 4: Attach overdraft product to account

Link the created overdraft product to an account using the [Attach product to account](https://developers.pismo.io/pismo-docs/reference/post-attach-product-to-account) endpoint.

When the linking is successful, a `2xx` response is returned. If an error occurs, a `4xx` error is returned with the reason for the error.

## Detach overdraft product from account

To unlink an overdraft product from an account, use the [Detach product from account](https://developers.pismo.io/pismo-docs/reference/post-detach-product-from-account) endpoint.

## Attach overdraft product to program

You can attach your overdraft product to a program using the  [Attach product to program](https://developers.pismo.io/pismo-docs/reference/post-attach-product-to-program) endpoint. Make sure to include the relevant program and product IDs in your request.

## Check detach status

Pismo detaches the overdraft product from your account upon receiving your request, you can check the detach status by calling [Get limit config by account](https://developers.pismo.io/pismo-docs/reference/get-config-by-account-1), and make sure that the response returns `over_limit = enable: false`.

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Sample response</summary>

  ```json
  {
    "over_limit": {
      "enable": false
    }
  }
  ```
</details>

# Additional endpoints

These endpoints are also available for managing overdraft.

| Description                                                    | Endpoint                                            |
| -------------------------------------------------------------- | --------------------------------------------------- |
| [Get account attachment](https://developers.pismo.io/pismo-docs/reference/get-overdraft-account-attachment) | Get the overdraft product linked to the account ID  |
| [List product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-list-products)          | List all overdraft products created by organization |
| [Get overdraft product](https://developers.pismo.io/pismo-docs/reference/get-overdraft-product)             | Get specific product by product ID                  |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limit` | Update account limits (outdated) | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |
| `POST /v1/interest/plan` | `post-v1-interest-plan` | Create interest plan | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `POST /v1/overdraft` | `post-overdraft-product` | Create overdraft product | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--product |
| `POST /v1/overdraft/accounts/{accountId}/attach` | `post-attach-product-to-account` | Attach overdraft product to account | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--account |
| `POST /v1/overdraft/accounts/{accountId}/detach` | `post-detach-product-from-account` | Detach overdraft product from account | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--account |
| `POST /v1/overdraft/programs/{programId}/attach` | `post-attach-product-to-program` | Attach overdraft product to program | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--program |
| `GET /v1/overdraft/attachments/accounts/{accountId}` | `get-overdraft-account-attachment` | Get overdraft product details for an account | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--account |
| `GET /v1/products` | `interest-bearing-v1-list-products` | List products | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /v1/overdraft/{productId}` | `get-overdraft-product` | Get overdraft product | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--product |

### Operation essentials

- **`PATCH /v1/accounts/{accountId}/limits`** (`patch-v1-account-limit`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `WLDG0021`, `WLDG0010`, `WLDG0025`, `WLDG0022`, `ELDG9999`; events `ledger-limit-changed-1`.
- **`POST /v1/interest/plan`** (`post-v1-interest-plan`): security `BearerAuth`; required parameters none declared; required body fields `accrual_basis`, `accrual_frequency`, `capitalization_frequency`, `currency_code`, `description`, `interest_type`, `start_date`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `interest-engine-interest-plan-creation-success-1`.
- **`POST /v1/overdraft`** (`post-overdraft-product`): security `BearerAuth`; required parameters none declared; required body fields `name`, `interest_plan_id`, `processing_code`; response statuses 201, 400, 404, 422, 500; error codes in examples `EOVD0008`, `EOVD0012`, `EOVD0020`, `EOVD0076`, `EOVD0021`, `EOVD0027`, `EOVD0007`, `EOVD0015`, `EOVD0016`, `EOVD0017`, `EOVD0018`, `EOVD0019`, `EOVD0022`, `EOVD0023`, `EOVD0024`, `EOVD0025`, `EOVD0026`, `EOVD0028`, `EOVD0029`; events `overdraft-product-creation-1`.
- **`POST /v1/overdraft/accounts/{accountId}/attach`** (`post-attach-product-to-account`): security `BearerAuth`; required parameters `accountId` (path), `AuthorizationToken` (header); required body fields `product_id`; response statuses 204, 400, 403, 404, 409, 500; error codes in examples `EOVD0008`, `EOVD0012`, `EOVD0034`, `EOVD0040`, `EOVD0043`, `EOVD0050`, `EOVD0069`, `EOVD0051`, `EOVD0035`, `EOVD0041`, `EOVD0047`, `EOVD0070`, `EOVD0045`, `EOVD0007`, `EOVD0029`, `EOVD0030`, `EOVD0031`, `EOVD0032`, `EOVD0033`, `EOVD0036`, `EOVD0038`, `EOVD0039`, `EOVD0042`, `EOVD0044`, `EOVD0048`, `EOVD0052`, `EOVD0064`, `EOVD0065`, `EOVD0066`, `EOVD0067`, `EOVD0068`; events `overdraft-product-account-attach-1`.
- **`POST /v1/overdraft/accounts/{accountId}/detach`** (`post-detach-product-from-account`): security `BearerAuth`; required parameters `accountId` (path), `AuthorizationToken` (header); required body fields `product_id`; response statuses 204, 400, 404, 409, 500; error codes in examples `EOVD0008`, `EOVD0012`, `EOVD0040`, `EOVD0043`, `EOVD0069`, `EOVD0076`, `EOVD0041`, `EOVD0047`, `EOVD0070`, `EOVD0072`, `EOVD0038`, `EOVD0039`, `EOVD0042`, `EOVD0044`, `EOVD0048`, `EOVD0063`, `EOVD0064`, `EOVD0065`, `EOVD0066`, `EOVD0067`, `EOVD0068`; events `overdraft-product-account-detach-1`.
- **`POST /v1/overdraft/programs/{programId}/attach`** (`post-attach-product-to-program`): security `BearerAuth`; required parameters `programId` (path); required body fields `product_id`; response statuses 204, 400, 403, 404, 409, 500; error codes in examples `EOVD0008`, `EOVD0012`, `EOVD0034`, `EOVD0040`, `EOVD0043`, `EOVD0050`, `EOVD0069`, `EOVD0051`, `EOVD0035`, `EOVD0041`, `EOVD0047`, `EOVD0070`, `EOVD0045`, `EOVD0007`, `EOVD0029`, `EOVD0030`, `EOVD0031`, `EOVD0032`, `EOVD0033`, `EOVD0036`, `EOVD0038`, `EOVD0039`, `EOVD0042`, `EOVD0044`, `EOVD0048`, `EOVD0052`, `EOVD0064`, `EOVD0065`, `EOVD0066`, `EOVD0067`, `EOVD0068`; events `overdraft-product-program-attach-1`.
- **`GET /v1/overdraft/attachments/accounts/{accountId}`** (`get-overdraft-account-attachment`): security `BearerAuth`; required parameters `accountId` (path), `AuthorizationToken` (header), `x-account-id` (header); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EOVD0043`, `EOVD0069`, `EOVD0070`, `EOVD0044`, `EOVD0064`, `EOVD0065`, `EOVD0066`, `EOVD0067`, `EOVD0068`; events none listed.
- **`GET /v1/products`** (`interest-bearing-v1-list-products`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `EIBACC0008`, `EIBACC0007`; events none listed.
- **`GET /v1/overdraft/{productId}`** (`get-overdraft-product`): security `BearerAuth`; required parameters `productId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EOVD0073`, `EOVD0074`, `EOVD0075`, `EOVD0076`, `EOVD0047`, `EOVD0048`; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `get-config-by-account-1` | Get configuration by account; Get limit config by account | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-interest-plan` | `interest-engine-interest-plan-creation-success-1` |
| `patch-v1-account-limit` | `ledger-limit-changed-1` |
| `post-attach-product-to-account` | `overdraft-product-account-attach-1` |
| `post-detach-product-from-account` | `overdraft-product-account-detach-1` |
| `post-overdraft-product` | `overdraft-product-creation-1` |
| `post-attach-product-to-program` | `overdraft-product-program-attach-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/how-overdraft-works.md`: updatedAt 2026-04-25T03:11:02.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- Operation link `get-config-by-account-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/how-overdraft-works.md` | whole document | https://developers.pismo.io/pismo-docs/docs/how-overdraft-works | `cc5783fbd172ec9f…` | 2026-04-25T03:11:02.000Z |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-banking-overdraft--account` — API reference: Banking - Overdraft — Account
- `KU-API-banking-overdraft--product` — API reference: Banking - Overdraft — Product
- `KU-API-banking-overdraft--program` — API reference: Banking - Overdraft — Program
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-EVT-catalogue-interest` — Event catalogue: interest
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-overdraft` — Event catalogue: overdraft
