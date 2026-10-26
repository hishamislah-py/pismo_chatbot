---
ku_id: KU-PAY-multi-leg-payments
title: Multi-leg payments
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/multi-leg-payments.md
  sha256: f3c29a390a9cefea268e263c26c929599259b11406f97fe68d62929970e316db
  url: https://developers.pismo.io/pismo-docs/docs/multi-leg-payments
  role: primary_guide
  updated_at: '2026-06-16T17:13:21.000Z'
operations:
- corporate-v2-post-payments
- corporate-v3-get-multileg-payment
- get-accounts
- v4-get-account-reason
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-BANK-managing-account-statuses
- KU-EVT-catalogue-account
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Multi-leg payments

**KU ID:** `KU-PAY-multi-leg-payments` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/multi-leg-payments.md`:

> The [Multi-leg payments feature](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments-1) enables you to process payment transactions by grouping multiple legs into a single request. This approach simplifies payment processing and removes the need to send multiple separate single-leg payment requests. With this feature, you can define each individual transaction—either credit or debit—within each leg of the multi-leg payment.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/multi-leg-payments.md`: Multi-leg payments; Supported features; Multi-leg and tracking ID; About tracking ID; Force payment restrictions; Error handling mechanism; Error response structure; Error identification; How to use Post multi-leg payment

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/multi-leg-payments.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/multi-leg-payments · updatedAt: 2026-06-16T17:13:21.000Z

<!-- source:begin path=docs/core-banking/multi-leg-payments.md part=0-end -->

# Multi-leg payments

The [Multi-leg payments feature](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments-1) enables you to process payment transactions by grouping multiple legs into a single request. This approach simplifies payment processing and removes the need to send multiple separate single-leg payment requests. With this feature, you can define each individual transaction—either credit or debit—within each leg of the multi-leg payment.

The Pismo platform ensures data integrity by enforcing strict validation, idempotency, and error-handling mechanisms throughout the payment lifecycle. Each transaction is uniquely identified by a multi-leg ID, which cannot be reused across different services. In the event of errors—such as a failed debit or credit leg—the platform employs a robust rollback process to reverse all successfully executed legs, maintaining transactional consistency and supporting accurate reconciliation.

<Callout icon="📘" theme="info">
  **Notes**

  * Each multi-leg payment request must contain a minimum of two legs (either credit or debit) and can include up to a maximum of 20 legs.
  * You cannot use [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments-1) to transfer credit and debit leg payments to different accounts for identical amounts. For such situations, use [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) instead.
</Callout>

# Supported features

In addition to simplifying complex transactions, multi-leg payments offer several capabilities that enhance flexibility, control, and reconciliation.

* **Instant clearing**: Use the `instant_clearing` field to request immediate clearing for specific debit or credit legs. Refer to [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments-1) for details.
* **Earmark support**: Debit legs can reference an `earmark_id` to use earmarked funds.
* **Granular validation rules**: Per-leg validation options allow override or force behavior for account status and ledger checks, reducing the likelihood of rollbacks.
* **Metadata support**: You can pass metadata and soft descriptor in each leg. Custom metadata provided in the request is returned in responses and included in events, aiding reconciliation and reporting.

# Multi-leg and tracking ID

A `multileg_id` uniquely identifies the entire multi-leg payment request. A tracking ID on the other hand, is used to identify and track an individual payment leg within a multi-leg transaction, whether debit or credit. When using  [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments-1), you must pass a tracking ID in each leg to ensure the transaction is unique.

### About tracking ID

Each tracking ID is single-use and cannot be reused across different services. For example, if a tracking ID has already been used for a [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments), it cannot be used again for a leg in [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments-1).

# Force payment restrictions

In scenarios where `force_post` is set to `true`, any reason-based force payment restrictions on the account result in a failed force payment operation. These restrictions apply to both credit and debit operations. Use the  [List status reasons](https://developers.pismo.io/pismo-docs/reference/v4-get-account-reason) endpoint to view the corresponding reason IDs. Forced transfers from an earmark balance are not supported.

If an account has a status that prevents force operations, the payment will fail. For more information, refer to [Manage account statuses](https://developers.pismo.io/pismo-docs/docs/managing-account-statuses).

# Error handling mechanism

During the processing of a multi-leg payment request, the Pismo platform enforces a robust error-handling mechanism known as rollback to safeguard data integrity. If any leg—credit or debit—fails, all previously successful legs are rolled back. If a rollback attempt itself fails, those legs are marked as `ROLLBACK_FAILED`. The rollback process is resource-intensive and generates compensating transactions to reverse any legs that were already executed.\
To minimize the need for rollbacks, the Pismo platform performs thorough validations when each payment request is received and proactively returns errors for invalid inputs before processing begins.

## Error response structure

When validation errors occur in a request, the API returns a structured error response with these components.

* **Standard error message**: For example, error code `WMLP0005` warns about invalid inputs without providing leg-specific details. This typically occurs when reusing a `tracking_id`.
* **Duplicate tracking ID**: If you reuse a tracking ID from a previous payment, the system returns error code `WPMT0007` and rejects the request.
* **List of leg-specific errors**: For certain failures, the response includes detailed errors for individual legs within the error object of each leg. In some cases, errors apply to the entire request, such as when the maximum number of legs is exceeded, and only a standard code and message are returned.

## Error identification

When a leg fails, you can retrieve the payment’s status using [Get multi-leg payment status](https://developers.pismo.io/pismo-docs/reference/corporate-v3-get-multileg-payment) and check the `event_datetime` field in the affected leg to see when the error occurred. This information is available only if the multi-leg payment was being created and the failure occurred while generating platform authorization. Note that not all legs display the `event_datetime` field.

<Callout icon="📘" theme="info">
  **Note**

  If either a credit or debit leg fails in a multi-leg payment, the Pismo platform automatically initiates a rollback of all previously executed legs, unless the rollback itself fails. In cases where a rollback cannot be completed, the affected legs are marked as `ROLLBACK_FAILED`.

  This rollback mechanism helps maintain transactional consistency. You can monitor the status of a multi-leg payment by using the [Get multi-leg payment status](https://developers.pismo.io/pismo-docs/reference/corporate-v3-get-multileg-payment) endpoint with a `multileg_id`. The `event_datetime` field might be displayed for a failed leg only when the multi-leg payment is created and the failure occurs while generating platform authorization. If a rollback fails under these conditions, the same endpoint reflects that status, enabling you to verify the outcome.
</Callout>

# How to use Post multi-leg payment

Consider a scenario in which your account has a balance of $1000, and you wish to initiate a payment request with three legs: two debit legs (one for $100, another for $200) and one credit leg for $600. Here are the API request details.

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Sample request</summary>

  ```curl cURL
  curl --request POST \
       --url https://sandbox.pismolabs.io/corporate/v3/payments/multileg \
       --header 'accept: application/json' \
       --header 'content-type: application/json' \
       --data '
  {
    "multileg_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e245",
    "debits": [
      {
        "tracking_id": "cf7f77ae-466c-428d-8e9f-7834341dd81e",
        "amount": 100.00,
        "currency": "USD",
        "external_account_id": "account-a",
        "processing_code": "219258",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "force_post": false,
        "validation_rules": {
          "ACCOUNT_STATUS": {
            "override": false
          },
          "LEDGER": {
            "force": false
          }
        },
        "skip_account_date_validation": false,
        "earmark_id": "8a3be3c1-5a2c-4d98-9901-8-account-a",
        "instant_clearing": false
      },
      {
        "tracking_id": "4cd1caeb-d454-4c92-971f-aeb6c14a4445",
        "amount": 200.00,
        "currency": "USD",
        "external_account_id": "account-a",
        "processing_code": "220037",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "instant_clearing": false
      }
    ],
    "credits": [
      {
        "tracking_id": "8c0d14ff-5c1d-4046-8e55-6833161f218e",
        "amount": 600.00,
        "currency": "USD",
        "external_account_id": "account-a",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "instant_clearing": false,
        "force_post": true
      }
    ],
    "metadata": {
      "custom_info": "abc"
    }
  }
  ```
</details>

Upon successful execution, the API returns the following response payload to confirm the successful processing of your request.

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Sample response</summary>

  ```json JSON
  202 Accepted
  {
    "debits": [
      {
        "tracking_id": "cf7f77ae-466c-428d-8e9f-7834341dd81e",
        "external_account_id": "account-a",
        "processing_code": "219258",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 100,
        "currency": "USD",
        "earmark_id": "8a3be3c1-5a2c-4d98-9901-account-a",
        "force_post": false,
        "validation_rules": {
          "ACCOUNT_STATUS": {
            "force": false,
            "override": false
          },
          "LEDGER": {
            "force": false,
            "override": false
          }
        },
        "instant_clearing": false,
        "skip_account_date_validation": false
      },
      {
        "tracking_id": "4cd1caeb-d454-4c92-971f-aeb6c14a4445",
        "external_account_id": "account-a",
        "processing_code": "220037",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 200,
        "currency": "USD",
        "force_post": false,
        "instant_clearing": false,
        "skip_account_date_validation": false
      }
    ],
    "credits": [
      {
        "tracking_id": "8c0d14ff-5c1d-4046-8e55-6833161f218e",
        "external_account_id": "account-a",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 600,
        "currency": "USD",
        "force_post": true,
        "instant_clearing": false,
        "skip_account_date_validation": false
      }
    ],
    "multileg_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e245",
    "metadata": {
      "custom_info": "abc"
    }
  }
  ```
</details>

You can optionally use [Get transaction banking account information](https://developers.pismo.io/pismo-docs/reference/get-accounts) to retrieve and display the complete result of this transaction. As shown in the response, the payment request comprising two debit legs totaling $300 and one credit leg of $600 results in an updated account balance of $1300.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /corporate/v2/payments` | `corporate-v2-post-payments` | Post payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `GET /accounts/v4/reasons` | `v4-get-account-reason` | List status reasons | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `GET /corporate/v3/payments/multileg/{multilegId}` | `corporate-v3-get-multileg-payment` | Get multi-leg payment status | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-02 |
| `GET /corporate/v1/corporate-accounts/{externalAccountId}` | `get-accounts` | Get transaction banking account information | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |

### Operation essentials

- **`POST /corporate/v2/payments`** (`corporate-v2-post-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`; response statuses 201, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WPMT0017`, `WPMT0011`, `WPMT0053`, `WPMT0018`, `WPMT0029`, `WPMT0030`, `WPMT0031`, `WPMT0062`, `WPMT0063`, `WCAC0010`, `WPMT0001`, `WPMT0061`, `WPMT0015`, `WPMT0016`, `WPMT0003`, `WPMT0004`, `WPMT0005`, `WPMT0006`, `WPMT0009`, `WPMT0010`, `WPMT0021`, `WEAM0008`, `WEAM0006`, `WPMT0050`, `WEAM0017`, `WEAM0019`, `WPMT0022`, `WPMT0023`, `WPMT0024`, `WPMT0025`, `WPMT0026`, `WCMN0002`, `WPMT0028`, `WPMT0045`, `WPMT0049`, `WPMT0036`, `WPMT0044`, `WPMT0051`, `WPMT0035`, `WPMT0046`, `WPMT0054`, `WPMT0055`, `WPMT0056`, `WPMT0058`, `WPMT0008`, `WPMT0014`, `WPMT0019`, `WCAC0002`, `WCAC0012`, `WPMT0002`, `WCAC0001`, `WEAM0007`, `WPMT0007`, `WPMT0052`, `WEAM0049`, `WPMT0047`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`GET /accounts/v4/reasons`** (`v4-get-account-reason`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `EACC0005`, `EACC0018`, `WACC0011`, `EACC0000`, `EACC9999`; events none listed.
- **`GET /corporate/v3/payments/multileg/{multilegId}`** (`corporate-v3-get-multileg-payment`): security `BearerAuth`; required parameters `multilegId` (path); required body fields none declared; response statuses 200, 404; error codes in examples `WPMT0010`, `WOBK0007`, `WMLP0007`; events none listed.
- **`GET /corporate/v1/corporate-accounts/{externalAccountId}`** (`get-accounts`): security `BearerAuth`; required parameters `externalAccountId` (path); required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples `WCAC0012`, `WDIV0002`, `WCAC0023`, `ECMN9999`; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `corporate-v3-post-multileg-payments-1` | Multi-leg payments feature; Post multi-leg payment | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-v2-post-payments` | `account-balances-balance-change-1` |
| `corporate-v2-post-payments` | `accounting-entry-creation-1` |
| `corporate-v2-post-payments` | `availables-change-available-1` |
| `corporate-v2-post-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-payments` | `rules-evaluation-requested-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/multi-leg-payments.md`: updatedAt 2026-06-16T17:13:21.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- Operation link `corporate-v3-post-multileg-payments-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/multi-leg-payments.md` | whole document | https://developers.pismo.io/pismo-docs/docs/multi-leg-payments | `f3c29a390a9cefea…` | 2026-06-16T17:13:21.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-BANK-managing-account-statuses` — Manage account statuses
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
