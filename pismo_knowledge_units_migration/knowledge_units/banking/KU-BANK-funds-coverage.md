---
ku_id: KU-BANK-funds-coverage
title: Funds coverage
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/funds-coverage.md
  sha256: 4fbb4f9f2a26ca14dc3fb2fafa1784886e7050ff15af428c7d31ec1dd9da517a
  url: https://developers.pismo.io/pismo-docs/docs/funds-coverage
  role: primary_guide
  updated_at: '2026-06-16T22:23:39.000Z'
operations:
- get-protection-source
- post-protection-source
- post-v1-balances-config
- update-protection-source
related_kus:
- KU-API-banking-funds-coverage--protection-sources
- KU-API-core-platform-balance-config-beta--balance-configurations
- KU-CORE-balance-configuration-use-cases
grouping_rationale: single source page
---

# Funds coverage

**KU ID:** `KU-BANK-funds-coverage` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/funds-coverage.md`:

> Funds coverage lets you configure one financial product—such as a savings account, loan, or credit card—to act as a fallback funding source for another product when there is insufficient balance or a payment failure. A common use case is overdraft protection, where funds are automatically pulled from a designated source to prevent transaction declines.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/funds-coverage.md`: Funds coverage; How funds coverage works; Configuring coverage sources; Endpoints; Example configuration; Business rules; Operational flow; Processing code setup; Use the same account as overdraft protection source; Use different accounts as overdraft protection source; Coverage execution during an event; Notes; Common error responses

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/funds-coverage.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/funds-coverage · updatedAt: 2026-06-16T22:23:39.000Z

<!-- source:begin path=docs/core-banking/funds-coverage.md part=0-end -->

# Funds coverage

Funds coverage lets you configure one financial product—such as a savings account, loan, or credit card—to act as a fallback funding source for another product when there is insufficient balance or a payment failure. A common use case is overdraft protection, where funds are automatically pulled from a designated source to prevent transaction declines.

You can define multiple coverage sources, control their priority, and enable or disable them as needed. The service is designed to support additional product types over time without changing how coverage is executed.

<Callout icon="📘" theme="info">
  **Note**

  Funds coverage is available only for overdraft protection and uses the savings balance as the funding source to cover the overdraft.
</Callout>

## How funds coverage works

When a covered account does not have enough available balance to complete a transaction, coverage is applied automatically using your configured sources.

With fund coverage, you can:

* Register which products are allowed to act as fallback sources
* Assign a priority order to each coverage source
* Enable or disable individual sources
* Allow fallback attempts across multiple sources until the shortfall is covered or no options remain

When a shortfall occurs, you select the highest‑priority active source and a funds movement is executed to credit the covered account so the transaction can proceed.

## Configuring coverage sources

You can configure coverage relationships using the funds coverage API.

### Endpoints

Manage coverage configurations using the following endpoints. Refer to each endpoint for detailed field descriptions.

| Endpoint                                                 | Description                                                                                                                                                                |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Create protection source](https://developers.pismo.io/pismo-docs/reference/post-protection-source)   | Creates a new protection source configuration, defining which financial products can act as coverage sources for a specified covered product and how they are prioritized. |
| [Update protection source](https://developers.pismo.io/pismo-docs/reference/update-protection-source) | Updates an existing protection source configuration, allowing you to modify coverage sources, hierarchy, activation status, or processing codes.                           |
| [Get protection source](https://developers.pismo.io/pismo-docs/reference/get-protection-source)       | Retrieves the current protection source configuration for a covered product and account, including configured sources and their priority order.                            |

### Example configuration

```json
{
  "protectionSources": [
    {
      "covered": "overdraft",
      "sources": [
        {
          "type": "savings_account",
          "id": "123456",
          "processing_code": 7000,
          "hierarchy": 1,
          "active": true
        },
        {
          "type": "loan",
          "id": "LN789",
          "processing_code": 789100,
          "hierarchy": 2,
          "active": true
        }
      ]
    }
  ]
}
```

In this example, you configure two coverage sources for an overdraft: a savings account and a loan, with the savings account set as the primary source. If the savings account does not have sufficient funds to cover the overdraft, coverage automatically falls back to the loan.

## Business rules

When you configure coverage sources, the following rules are enforced.

* Coverage sources must exist, belong to the customer, and meet eligibility criteria.
* Each source must have a unique hierarchy value; gaps are allowed if intentional.
* A product cannot act as a coverage source for itself.
* You can control availability using the `active` flag.
* You must include all required fields in your request.
* Errors are returned for invalid IDs, unauthorized relationships, duplicate hierarchy values, or circular references.

## Operational flow

### Processing code setup

Before coverage can be executed, you must configure a processing code that defines how funds move between products. Use the [Create balance configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config) endpoint to create a processing code.

Depending on your setup:

* If the coverage source and covered account belong to the same account holder, the processing code typically debits the savings account balance and credits the available balance. For example, using a savings account as coverage source for overdraft protection.
* If the accounts belong to different customers within the same organization, you must specify both the impacted account and the counterpart account.

Note that you are responsible for creating processing codes and balance configurations. Refer to these examples.

### Use the same account as overdraft protection source

```json
{
  "id": "d567a7ef-447c-467a-90ee-79584f055436",
  "account_id": 13409,
  "configs": [
    {
      "scenarios": [
        {
          "condition": {
            "type": "default",
            "amount_to_check_balance": "amount",
            "order": 1
          },
          "result": {
            "impact": [
              "AvailableCreditLimit"
            ],
            "consider": [
              "AvailableSavingsAccountLimit"
            ],
            "amount": "contract_amount",
            "amount_consider": "principal_amount",
            "reset_limit": "never"
          }
        }
      ],
      "filters": {
        "currency_code": "",
        "account_type": "",
        "mcc": null,
        "processing_codes": [
          "{processing_code_value}"
        ],
        "min_installments": 0,
        "max_installments": 0
      },
      "is_active": true
    }
  ]
}
```

In this example, account ID `13409` is both the impacted account and the overdraft protection source. If a shortfall or overdraft occurs on account `13409`, the Pismo platform uses the available savings balance in that same account to cover it. For more information about impacted and counterpart accounts, refer to [Create balance configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config) and [Balance configuration use cases](https://developers.pismo.io/pismo-docs/docs/balance-configuration-use-cases).

### Use different accounts as overdraft protection source

```json
{
  "id": "d567a7ef-447c-467a-90ee-79584f055436",
  "account_id": 13409,
  "configs": [
    {
      "scenarios": [
        {
          "condition": {
            "type": "default",
            "amount_to_check_balance": "amount",
            "order": 1
          },
          "result": {
            "impact": [
              "AvailableCreditLimit"
            ],
            "consider": [
              "AvailableSavingsAccountLimit"
            ],
            "amount": "contract_amount",
            "amount_consider": "principal_amount",
            "reset_limit": "never",
            "impact_account": {
              "account_id": 123456
            },
            "counterpart_account": {
              "account_id": 789456,
              "processing_code": "000000000"
            }
          }
        }
      ],
      "filters": {
        "currency_code": "",
        "account_type": "",
        "mcc": null,
        "processing_codes": [
          "000000000"
        ],
        "min_installments": 0,
        "max_installments": 0
      },
      "is_active": true
    }
  ]
}
```

When the impacted and counterpart accounts belong to different account holders, you must specify both account IDs in the API call. In this example, account `123456` is the impacted account, and account `789456` is the counterpart account. If an overdraft occurs, the Pismo platform uses the counterpart account as the protection source to cover the impacted account.

### Coverage execution during an event

During an overdraft or balance shortfall, the Pismo platform performs the following actions.

* Verifies that coverage is enabled for the account
* Queries the ledger to calculate the exact shortfall amount
* Uses funds coverage to retrieve eligible sources in priority order
* Triggers a funds movement using the configured processing code
* Credits the covered account’s available balance so the transaction can complete

<Callout icon="💡" theme="default">
  ### Notes

  * If the first source does not fully cover the shortfall, the next active source in the hierarchy is automatically attempted.
  * All fund movements follow standard posting rules, ensuring ledger consistency and audibility.
</Callout>

## Common error responses

These are the common errors and why they occur.

| Error type       | HTTP status | Error message                                          |
| ---------------- | ----------- | ------------------------------------------------------ |
| Bad Request      | `400`       | Account ID not found                                   |
| Not Found        | `404`       | Overdraft product is inactive for the selected account |
| Validation error | `400`       | Source cannot be the same as covered target.           |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/protection-sources` | `post-protection-source` | Create protection source | `api-specs/Banking_-_Funds_coverage.yaml` | no | KU-API-banking-funds-coverage--protection-sources |
| `PATCH /v1/protection-sources` | `update-protection-source` | Update protection source | `api-specs/Banking_-_Funds_coverage.yaml` | no | KU-API-banking-funds-coverage--protection-sources |
| `GET /v1/protection-sources/accounts/{accountId}` | `get-protection-source` | Get protection source | `api-specs/Banking_-_Funds_coverage.yaml` | no | KU-API-banking-funds-coverage--protection-sources |
| `POST /v1/balances-config` | `post-v1-balances-config` | Create balance configuration | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--balance-configurations |

### Operation essentials

- **`POST /v1/protection-sources`** (`post-protection-source`): security `BearerAuth`; required parameters `AuthorizationToken` (header); required body fields `covered`, `sources`; response statuses 201, 400, 404, 409, 500; error codes in examples `EFCA0001`, `EFCA0002`, `EFCA0015`, `EFCA0016`, `EFCA0010`, `EFCA0006`, `EFCA0007`, `EFCA0011`, `EFCA0012`, `EFCA0013`, `EFCA0014`; events none listed.
- **`PATCH /v1/protection-sources`** (`update-protection-source`): security `BearerAuth`; required parameters `AuthorizationToken` (header); required body fields `covered`, `sources`; response statuses 201, 400, 404, 500; error codes in examples `EFCA0001`, `EFCA0002`, `EFCA0015`, `EFCA0016`, `EFCA0006`, `EFCA0007`, `EFCA0011`, `EFCA0012`, `EFCA0013`, `EFCA0014`; events none listed.
- **`GET /v1/protection-sources/accounts/{accountId}`** (`get-protection-source`): security `BearerAuth`; required parameters `accountId` (path), `AuthorizationToken` (header); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EFCA0001`, `EFCA0009`, `EFCA0006`; events none listed.
- **`POST /v1/balances-config`** (`post-v1-balances-config`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields none declared; response statuses 201, 400, 404, 500; error codes in examples `EBCF0321`, `EBCF0320`, `EBCF0317`, `EBLC9999`; events none listed.

## Lifecycle status

- `docs/core-banking/funds-coverage.md`: updatedAt 2026-06-16T22:23:39.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/funds-coverage.md` | whole document | https://developers.pismo.io/pismo-docs/docs/funds-coverage | `4fbb4f9f2a26ca14…` | 2026-06-16T22:23:39.000Z |

## Related knowledge units

- `KU-API-banking-funds-coverage--protection-sources` — API reference: Banking - Funds coverage — Protection sources
- `KU-API-core-platform-balance-config-beta--balance-configurations` — API reference: Core platform - Balance configurations — Balance configurations
- `KU-CORE-balance-configuration-use-cases` — Balance configuration use cases
