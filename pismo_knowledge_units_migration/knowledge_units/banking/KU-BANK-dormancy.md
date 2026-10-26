---
ku_id: KU-BANK-dormancy
title: Dormancy and dormancy reactivation exceptions
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/dormancy-overview.md
  sha256: 6a73c38fc3984897f7c5b01b8d10ad53900ac64eed908f7ab2e93da0711753e2
  url: https://developers.pismo.io/pismo-docs/docs/dormancy-overview
  role: primary_guide
  updated_at: '2026-04-24T21:44:58.000Z'
- path: docs/core-banking/dormancy-reactivation-exception.md
  sha256: cbfb212a2850d9e2db46d5e91fa1af26eb86173219ccb4801f6140ea02480082
  url: https://developers.pismo.io/pismo-docs/docs/dormancy-reactivation-exception
  role: primary_guide
  updated_at: '2026-04-24T21:44:58.000Z'
operations:
- corporate-put-bulk-file
- corporate-v2-post-payments
- corporate-v3-post-multileg-payments
- get-accounts-v1-accounts-status-reasons
- patch-dormancy-config-v2
- post-dormancy-config-v2
related_kus:
- KU-API-banking-transaction-banking--bulk-payment-files
- KU-API-banking-transaction-banking--dormancy
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-BANK-managing-account-statuses
- KU-CORE-processing-codes-and-transaction-types
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-PAY-force-operation
grouping_rationale: One feature.
---

# Dormancy and dormancy reactivation exceptions

**KU ID:** `KU-BANK-dormancy` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: One feature.

Scope as stated in `docs/core-banking/dormancy-overview.md`:

> The Pismo platform allows you to designate an account as dormant if it has remained inactive for an extended period. It features an API that enables you to set dormancy rules, which govern account reactivation conditions and status changes.

Scope as stated in `docs/core-banking/dormancy-reactivation-exception.md`:

> The dormancy process reactivates an account whenever a transaction is posted, unless the transaction uses a processing code included in `dormant_processing_codes`. While this is appropriate for different types of operations, it does not account for variables that only exist outside of the Pismo platform—such as legacy transaction codes or custom identifiers—that should not influence a bank account’s dormancy state. To address this gap, the Pismo platform provides a dormancy reactivation exception feature that allows specific transactions to bypass reactivation based on attributes like metadata or soft descriptors. This capability is designed to support exceptions driven by variables external to the platform but intrinsic to your business rules, while preserving the platform’s standard behavior for all other cases.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/dormancy-overview.md`: Dormancy overview; Configure dormancy; Account status-check schedule; Dormancy metrics; Account status change; Skip processing codes; Account status reason ID; Forced transactions reactivation; Account timezone for dormancy checks; Dormancy inheritance
- `docs/core-banking/dormancy-reactivation-exception.md`: Dormancy reactivation exception; Reactivation exceptions configuration; How reactivation exception works; Examples; Reactivation exception fails; Reactivation exception succeeds

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/dormancy-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/dormancy-overview · updatedAt: 2026-04-24T21:44:58.000Z

<!-- source:begin path=docs/core-banking/dormancy-overview.md part=0-end -->

# Dormancy overview

The Pismo platform allows you to designate an account as dormant if it has remained inactive for an extended period. It features an API that enables you to set dormancy rules, which govern account reactivation conditions and status changes.

Dormancy pertains to bank accounts that show no financial activity over an extended duration. Banks monitor dormant accounts closely due to their susceptibility to internal fraud. Dormant accounts are also vulnerable to fund siphoning due to lack of attention from the account holder. Regulators in many countries stipulate rules for dormancy, and banks can usually establish their own reactivation rules, to mitigate operational and fraud risks. Banks typically transition an account through an inactive phase before moving to dormancy. A customer-initiated transaction, such as a fund transfer, check payment, or ATM cash withdrawal, can prevent an inactive account from entering dormancy.

Following dormancy, an account might enter  `UNCLAIMED` status, prompting its closure and transfer of its funds to a central bank. Transactions on dormant accounts are restricted to bank-initiated activities only (unlike a total account blockage).

If a dormant account can be reactivated, a bank can opt to do this manually or allow a customer-initiated debit or credit transaction to reactivate the account.

# Configure dormancy

The Pismo platform's dormancy feature evaluates various factors to determine whether an account's status must be changed. To begin configuring dormancy, consider the following questions:

* What is the level of the dormancy configuration — is it at the program level or division level? If dormancy configurations exist at both levels, they must adhere to the hierarchy described in [Dormancy inheritance](#dormancy-inheritance). One thing to remember is that setting a dormancy configuration at the account level is not possible.
* What time of day should the platform check the dormancy status of the account? Note that the timezone setting for dormancy check **is inherited from the division or program**. For more information, see [Account status-check schedule](#account-status-check-schedule).
* How many statuses do you need to define for the account? You can define as many statuses as you want (minimum of one) and specify their order.
* How many days can an account remain in each status? Additionally, you must determine the number of days an account can remain without any transactions to trigger a status change. For example:
  * Dormant (3 days); Inactive (5 days)
  * Inactive (3 days); Dormant (5 days); Unclaimed (30 days)
  * Unclaimed (45 days)
* Which processing codes (if any) can reactivate a dormant account?

Once you have these answers, use the [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) endpoint to set up dormancy configurations.

## Account status-check schedule

The Pismo platform verifies the account's correct status only during scheduled checks, which are initiated by one of the following triggers:

* Account created under a program or division that is already configured for dormancy.
* Creation of a dormancy configuration for a division or program with existing accounts.
* When a transaction occurs in an account belonging to a program or division with dormancy configuration, excluding transactions designated to skip based on defined processing codes, the previous schedule is deleted and replaced with a new one.
* Change in account status, either by the dormancy configuration or manually.

The scheduling process always follows the following logic: `inactive since` + # days until the next dormancy state. When a trigger occurs, the Pismo platform evaluates the next account status and determines the number of days until the status changes.

### Dormancy metrics

To understand dormancy metrics, note the following:

* `Inactivity_time` is the number of days the account has remained inactive. It is the difference between the current date/time (UTC) minus the `inactive_since` date/time.

- `Inactive_since` is the date/time of the most recent account activity. If a new dormancy configuration is established, for existing accounts, `inactive_since` equals the date/time of dormancy configuration creation until the occurrence of the subsequent transaction. However, if the account is opened subsequent to the creation of the dormancy configuration, `inactive_since` refers to the account's creation time until the occurrence of the next transaction.

## Account status change

When a transaction occurs that is allowed to reactivate a dormant account, the platform restores the account status to `NORMAL`. When the criteria are met to change an account status to inactive, the platform automatically transitions the account to the next status. When an account moves to another program or division with a different dormancy configuration, it retains its current status.

## Skip processing codes

Some transactions, such interest accruals, charges, and taxes, are not considered customer-initiated transactions. These transactions do not affect the calculation of dormancy based on account inactivity.

To specify which transactions can reactivate a dormant account or reset the inactivity counter, you specify the relevant processing codes when creating or updating the dormancy configuration. Use [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) to retrieve a list of available processing codes. For more information about processing codes, see [Standard processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types#standard-processing-codes) and [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types).

Regardless of account status, when a transaction with a disallowed processing code occurs, the `inactive_since` date remains unchanged. As a result, `inactivity_time` does not reset, and the transaction is not factored into the dormancy calculation.

# Account status reason ID

You can configure [account status reasons](https://developers.pismo.io/pismo-docs/docs/managing-account-statuses#configure-dormancy-statuses-and-change-reasons) to explain why an account status was changed. Reasons are represented by numerical IDs (`reason_id`). They are optionally associated with statuses. They also can be used to override account status restrictions for debits and credits. Each account status can link to only one reason ID, and each account can have only one combination of reason ID and account status. For instance, the status `NORMAL` typically has the reason `ANY`, indicating that any transaction is permitted, including [force operations](https://developers.pismo.io/pismo-docs/docs/force-operation).

To see a list of account status reason IDs, use [List account status reasons](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts-status-reasons).

Reason IDs include the following types:

| Reason ID type                           | Behavior                                                                  |
| :--------------------------------------- | :------------------------------------------------------------------------ |
| **ANY**                                  | Any transaction will change the status back to `NORMAL`.                  |
| **MANUAL**                               | Status resets to `NORMAL` only if manually updated.                       |
| **CREDIT ONLY**                          | Only credits change the status back to `NORMAL`.                          |
| **DEBIT ONLY**                           | Only debits change the status back to `NORMAL`.                           |
| **CREDIT ONLY - NO FORCE DEBIT ALLOWED** | No force debit transactions allowed.                                      |
| **DEBIT ONLY - NO FORCE CREDIT ALLOWED** | No force credit transactions allowed.                                     |
| **ANY - NO FORCE ALLOWED**               | All transactions allowed, except force transactions.                      |
| **MANUAL - NO FORCE ALLOWED**            | Manual add or update transactions are allowed, except force transactions. |

For information about statuses and reason IDs, see [Manage account statuses](https://developers.pismo.io/pismo-docs/docs/managing-account-statuses).

<Callout icon="📘" theme="info">
  **Note**

  Each reason ID is unique per organization and environment, and there is no endpoint to create one. In dormancy scenarios, the reason ID is associated with the `DORMANT` status. It is important to clearly specify which transactions are permitted when an account is in each status.
</Callout>

# Forced transactions reactivation

Forced transactions are typically initiated by the bank rather than the account holder and often follow nonstandard flows. This setting ensures that reactivation only occurs through intentional and expected user activity.

The `deny_forced_transaction_reactivation` field allows you to determine whether forced transactions can reactivate an account in `DORMANT` status.

For example, if you specify `true` in `deny_forced_transaction_reactivation`, forced transactions do not trigger reactivation of a dormant account. If `false`, forced transactions can reactivate the account as part of their processing flow.

# Account timezone for dormancy checks

This setting ensures that dormancy evaluations are aligned with the correct business context, this is especially important for organizations operating across multiple time zones. It prevents premature or delayed status changes due to time zone mismatches.

The `check_timezone_origin` field allows you to define which time zone is used when evaluating dormancy conditions for an account. You can select either `PROGRAM` or `DIVISION` to apply your time zone setting.

<Callout icon="📘" theme="info">
  **Note**

  When neither `PROGRAM` nor `DIVISION` is specified, the Pismo platform defaults to using the time zone associated with the dormancy `target_id`.
</Callout>

# Dormancy inheritance

Dormancy configurations are established at either the division or program level. If an account is under a program that has a dormancy configuration, it adheres to the rules defined by that program's configuration. However, if an account also is under a division inside that program and the division has its own dormancy configuration, hierarchy rules apply.\
For divisions, the hierarchy always follows this order: **division > program**. Since you cannot set dormancy configuration at the account level, accounts can only inherit it from either the division or program. If a dormancy configuration exists for both the division and program, the division’s configuration applies.

<Callout icon="📘" theme="info">
  **Note**

  In other scenarios on the Pismo platform, hierarchy always follows the order account → division → program. However, in dormancy configurations, it is not possible to define settings for accounts. It is important to take this rule into account when dealing with multiple divisions and programs. See the following example for further clarification.
</Callout>

Here is an illustration of how dormancy inheritance works:

<Image align="center" alt="Dormancy inheritance" caption="Figure 1: Dormancy inheritance" src="https://files.readme.io/4860014-Dormancy_overview_guide_V7.png" />
<!-- source:end -->

### Source 2: `docs/core-banking/dormancy-reactivation-exception.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/dormancy-reactivation-exception · updatedAt: 2026-04-24T21:44:58.000Z

<!-- source:begin path=docs/core-banking/dormancy-reactivation-exception.md part=0-end -->

# Dormancy reactivation exception

The dormancy process reactivates an account whenever a transaction is posted, unless the transaction uses a processing code included in `dormant_processing_codes`. While this is appropriate for different types of operations, it does not account for variables that only exist outside of the Pismo platform—such as legacy transaction codes or custom identifiers—that should not influence a bank account’s dormancy state. To address this gap, the Pismo platform provides a dormancy reactivation exception feature that allows specific transactions to bypass reactivation based on attributes like metadata or soft descriptors. This capability is designed to support exceptions driven by variables external to the platform but intrinsic to your business rules, while preserving the platform’s standard behavior for all other cases.

# Reactivation exceptions configuration

Use the `reactivation_exceptions_config` object in the [Create](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) or [Update dormancy configuration](https://developers.pismo.io/pismo-docs/reference/patch-dormancy-config-v2) endpoints to define attribute‑based rules that let specific transactions bypass dormancy reactivation. This object includes two fields.

| Field name | Description                                                                                                                                                                                                                                                                                                      |
| :--------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `field`    | Indicates which transaction attribute the Pismo platform should evaluate to determine whether a transaction is exempt from reactivating a dormant account. The field value can be either `soft_descriptor` or `metadata`, and you supply corresponding values for the selected option.                           |
| `values`   | Specifies the values that, when found in the selected field, prevent the transaction from reactivating the account. You can provide any values in this field. The list contains the exact values you expect to receive in either the `soft_descriptor` or `metadata` field, depending on which one you selected. |

## How reactivation exception works

This is how you create and apply dormancy reactivation exception.

1. In the [Create](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) or [Update dormancy configuration](https://developers.pismo.io/pismo-docs/reference/patch-dormancy-config-v2) endpoint, set a value in the field property of the `reactivation_exceptions_config` object. This value can be either `soft_descriptor`—which tells the Pismo platform to check the `soft_descriptor` field in the `credit` or `debit` object, or at the root level—or `metadata`.

The request body follows this format.

```json
{
   "reactivation_exceptions_config":{
      "field":"<attribute_field_name>",
      "values":[
         "<value1>",
         "<value2>",
         "..."
      ]
   }
}
```

2. Specify a value or values in the selected field (either `soft_descriptor` or `metadata`) in the `credit` or `debit` object or at the root level of the following endpoints.

* [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)
* [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments)
* [Upload bulk file](https://developers.pismo.io/pismo-docs/reference/corporate-put-bulk-file) (include `soft_descriptor` and `values` fields with specified values in the bulk file)

<Callout icon="📘">
  **Notes**

  * You can configure up to 30 values in the values list.
  * The `metadata` and `soft_descriptor` fields appear both within the `credit` and `debit` objects and at the root level of the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) request body. You can use either location to trigger dormancy exceptions defined in the dormancy configuration.
  * When you set a value for `soft_descriptor`—whether in `credit`, `debit`, or at the root—or when you set a value in `metadata`, that value becomes the one used by `reactivation_exceptions_config`.  For example, if `reactivation_exceptions_config.field` is set to `soft_descriptor`, the Pismo platform pulls the `soft_descriptor` value either from `credit`/ `debit` or the root.
</Callout>

## Examples

### Reactivation exception fails

Consider an example where values are specified in these fields.

| Endpoint                                                     | Field                                   | Value             |
| ------------------------------------------------------------ | --------------------------------------- | ----------------- |
| [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) | `reactivation_exceptions_config.field`  | `soft_descriptor` |
| [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) | `reactivation_exceptions_config.values` | `001`             |
| [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)               | `credit.soft_descriptor`                | `005`             |

**Result**:  The value `005` in `credit.soft_descriptor` does not override the dormancy‑reactivation rule because the code configured in `reactivation_exceptions_config.values` is `001`. Since the value provided in [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) is `005`—which does not match the configured exception—the Pismo platform does not treat it as an allowed exception, and the dormant account is reactivated.

### Reactivation exception succeeds

| Endpoint                                                     | Field                                   | Value               |
| ------------------------------------------------------------ | --------------------------------------- | ------------------- |
| [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) | `reactivation_exceptions_config.field`  | `metadata.t_code`   |
| [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) | `reactivation_exceptions_config.values` | `001`, `005`, `006` |
| [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)               | `metadata`                              | `001`               |

**Result**: Since `001` is one of the custom values defined in `reactivation_exceptions_config.values` that blocks dormant accounts from being reactivated, it is applied, and the account remains inactive.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /corporate/v2/dormancy-config` | `post-dormancy-config-v2` | Create dormancy configuration | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `GET /accounts/v1/accounts-status/reasons` | `get-accounts-v1-accounts-status-reasons` | List status reasons V1 (deprecated) | `api-specs/Core_platform_-_Accounts.yaml` | **yes** | KU-API-core-platform-accounts--statuses-and-reasons |
| `PATCH /corporate/v2/dormancy-config/{dormancyConfigId}` | `patch-dormancy-config-v2` | Update dormancy configuration | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `POST /corporate/v2/payments` | `corporate-v2-post-payments` | Post payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `POST /corporate/v3/payments/multileg` | `corporate-v3-post-multileg-payments` | Post multi-leg payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `PUT /corporate/v1/bulk-payments/{bulkId}` | `corporate-put-bulk-file` | Upload bulk file | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-payment-files |

### Operation essentials

- **`POST /corporate/v2/dormancy-config`** (`post-dormancy-config-v2`): security `BearerAuth`; required parameters none declared; required body fields `check_time`, `target_type`, `target_id`, `statuses`; response statuses 201, 400, 401, 403, 404, 500; error codes in examples `WDOR0001`, `WDOR0002`, `WDOR0010`, `WDOR0011`, `WDOR0005`, `WDOR0006`, `WDOR0008`, `WDOR0009`, `WDOR0004`, `WDOR0003`, `ECMN9999`; events `corporate-dormancy-config-creation-1`.
- **`GET /accounts/v1/accounts-status/reasons`** (`get-accounts-v1-accounts-status-reasons`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 404, 500; error codes in examples none; events none listed.
- **`PATCH /corporate/v2/dormancy-config/{dormancyConfigId}`** (`patch-dormancy-config-v2`): security `BearerAuth`; required parameters `dormancyConfigId` (path); required body fields none declared; response statuses 204, 400, 401, 403, 404, 500; error codes in examples `WDOR0001`, `WDOR0002`, `WDOR0010`, `WDOR0011`, `WDOR0005`, `WDOR0006`, `WDOR0009`, `WDOR0007`, `ECMN9999`; events `corporate-dormancy-config-change-1`.
- **`POST /corporate/v2/payments`** (`corporate-v2-post-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`; response statuses 201, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WPMT0017`, `WPMT0011`, `WPMT0053`, `WPMT0018`, `WPMT0029`, `WPMT0030`, `WPMT0031`, `WPMT0062`, `WPMT0063`, `WCAC0010`, `WPMT0001`, `WPMT0061`, `WPMT0015`, `WPMT0016`, `WPMT0003`, `WPMT0004`, `WPMT0005`, `WPMT0006`, `WPMT0009`, `WPMT0010`, `WPMT0021`, `WEAM0008`, `WEAM0006`, `WPMT0050`, `WEAM0017`, `WEAM0019`, `WPMT0022`, `WPMT0023`, `WPMT0024`, `WPMT0025`, `WPMT0026`, `WCMN0002`, `WPMT0028`, `WPMT0045`, `WPMT0049`, `WPMT0036`, `WPMT0044`, `WPMT0051`, `WPMT0035`, `WPMT0046`, `WPMT0054`, `WPMT0055`, `WPMT0056`, `WPMT0058`, `WPMT0008`, `WPMT0014`, `WPMT0019`, `WCAC0002`, `WCAC0012`, `WPMT0002`, `WCAC0001`, `WEAM0007`, `WPMT0007`, `WPMT0052`, `WEAM0049`, `WPMT0047`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`POST /corporate/v3/payments/multileg`** (`corporate-v3-post-multileg-payments`): security `BearerAuth`; required parameters none declared; required body fields `multileg_id`; response statuses 202, 400, 403, 409, 500; error codes in examples `WMLP0001`, `WMLP0002`, `WMLP0003`, `WMLP0004`, `WMLP0008`, `WMLP1044`, `WMLP0005`, `WMLP1026`, `WMLP1028`, `WMLP1027`, `WMLP1049`, `WMLP1002`, `WMLP1003`, `WMLP1004`, `WMLP1005`, `WMLP1039`, `WMLP1006`, `WMLP1022`, `WMLP1007`, `WMLP1008`, `WMLP1009`, `WMLP1010`, `WMLP1011`, `WMLP1013`, `WMLP1014`, `WMLP1015`, `WMLP1016`, `WMLP1017`, `WMLP1019`, `WMLP1048`, `WMLP1023`, `WMLP1036`, `WMLP1034`, `WMLP1035`, `WMLP1024`, `WMLP1037`, `WMLP1038`, `WMLP1030`, `WMLP1040`, `WMLP1041`, `WMLP1042`, `WMLP1043`, `WMLP1046`, `WMLP0009`, `ECMN9999`; events `corporate-multi-leg-creation-2`, `corporate-multi-leg-status-change-2`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`PUT /corporate/v1/bulk-payments/{bulkId}`** (`corporate-put-bulk-file`): security `BearerAuth`; required parameters `bulkId` (path), `signature` (header); required body fields none declared; response statuses 200, 400, 401, 403, 409, 500; error codes in examples `WBUP0001`, `WBUP0004`, `WBUP0005`, `WBUP0006`, `WBUP0007`, `WBUP0008`, `WBUP0009`, `WBUP0010`, `WBUP0003`, `ECMN9999`; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `get-processing-code-by-tenant` | List processing codes | not found in the current OpenAPI specifications. Name-based inference: link text "List processing codes" equals the endpoint name "List processing codes" in the removed-endpoints list (row Payment configurations / Core platform, date removed `5/6/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`ProcessingCodeList` (GET /orgs-operation/v1/processing-codes)); no source states that it replaces the removed endpoint. |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-v2-post-payments` | `account-balances-balance-change-1` |
| `corporate-v2-post-payments` | `accounting-entry-creation-1` |
| `corporate-v2-post-payments` | `availables-change-available-1` |
| `patch-dormancy-config-v2` | `corporate-dormancy-config-change-1` |
| `post-dormancy-config-v2` | `corporate-dormancy-config-creation-1` |
| `corporate-v3-post-multileg-payments` | `corporate-multi-leg-creation-2` |
| `corporate-v3-post-multileg-payments` | `corporate-multi-leg-status-change-2` |
| `corporate-v2-post-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v3-post-multileg-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-payments` | `rules-evaluation-requested-1` |
| `corporate-v3-post-multileg-payments` | `rules-evaluation-requested-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/dormancy-overview.md`: updatedAt 2026-04-24T21:44:58.000Z.
- `docs/core-banking/dormancy-reactivation-exception.md`: updatedAt 2026-04-24T21:44:58.000Z.
- Links to `get-accounts-v1-accounts-status-reasons`, which is marked `deprecated: true` in `api-specs/Core_platform_-_Accounts.yaml`.
- Links to `get-processing-code-by-tenant`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "List processing codes" equals the endpoint name "List processing codes" in the removed-endpoints list (row Payment configurations / Core platform, date removed `5/6/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`ProcessingCodeList` (GET /orgs-operation/v1/processing-codes)); no source states that it replaces the removed endpoint.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/dormancy-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/dormancy-overview | `6a73c38fc3984897…` | 2026-04-24T21:44:58.000Z |
| `docs/core-banking/dormancy-reactivation-exception.md` | whole document | https://developers.pismo.io/pismo-docs/docs/dormancy-reactivation-exception | `cbfb212a2850d9e2…` | 2026-04-24T21:44:58.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--bulk-payment-files` — API reference: Banking - Transaction banking — Bulk payment files
- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-BANK-managing-account-statuses` — Manage account statuses
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-force-operation` — Force operation
