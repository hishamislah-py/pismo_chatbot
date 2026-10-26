---
ku_id: KU-CC-processing-codes
title: Control Center processing codes, transaction types and general ledger accounts
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/cc-manage-processing-codes-and-transaction-types.md
  sha256: 7368171dec32f6a31132d0720167e229478e73889df03ac7e69ad09877a03a7f
  url: https://developers.pismo.io/pismo-docs/docs/cc-manage-processing-codes-and-transaction-types
  role: primary_guide
  updated_at: '2026-03-18T15:09:42.000Z'
- path: docs/control-center/create-processing-codes-and-transaction-types.md
  sha256: 3e26f24653e0aa72191808567917960a1ffc4f36df82e28cfec4b2cd4d276a3f
  url: https://developers.pismo.io/pismo-docs/docs/create-processing-codes-and-transaction-types
  role: primary_guide
  updated_at: '2026-03-18T15:09:44.000Z'
- path: docs/control-center/add-a-transaction-type-to-an-existing-processing-code.md
  sha256: 37fa537b3ac30277734e283b93e4ddd06f8847851ae77462b58d4bee3c9e60a9
  url: https://developers.pismo.io/pismo-docs/docs/add-a-transaction-type-to-an-existing-processing-code
  role: primary_guide
  updated_at: '2026-03-18T15:09:46.000Z'
- path: docs/control-center/cc-general-ledger-accounts.md
  sha256: 2cdff4a04da535b8cf894f2b1558c14d42afb77cb2492f1d0608b2e66e499a3b
  url: https://developers.pismo.io/pismo-docs/docs/cc-general-ledger-accounts
  role: primary_guide
  updated_at: '2026-03-18T15:09:40.000Z'
operations:
- CreateProcessingCode
- createProgramTransactionType
related_kus:
- KU-API-platform-setup-orgs-operation--processing-codes
- KU-API-revolving-credit-configurations--program-transaction-types
- KU-CORE-accounting-overview
- KU-CORE-processing-codes-and-transaction-types
- KU-CORE-transactiontypes
- KU-EVT-catalogue-other-domains
- KU-PAY-payments-configurations
grouping_rationale: Processing-code screens.
---

# Control Center processing codes, transaction types and general ledger accounts

**KU ID:** `KU-CC-processing-codes` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 4 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Processing-code screens.

Scope as stated in `docs/control-center/cc-manage-processing-codes-and-transaction-types.md`:

> Use Pismo Control Center to view and create processing codes and transaction types. Every organization has a collection of standard processing codes, and you can define custom codes that suit your organization's business requirements. Processing codes identify financial operations on the Pismo platform. For example, `00` is a purchase, `01` is a withdrawal, and so on. These are defined at the organization level so they can be applied to all programs and the accounts they contain.

Scope as stated in `docs/control-center/create-processing-codes-and-transaction-types.md`:

> With Control Center, you can initially map a transaction type only with one processing code, but you can add more later. When you create a new transaction type, Control Center automatically creates a corresponding reversal processing code and transaction type for you.

Scope as stated in `docs/control-center/add-a-transaction-type-to-an-existing-processing-code.md`:

> When you need to add another transaction type to an existing processing code, you can either create a new transaction type and add it or you can add an existing transaction type. In addition, when adding a transaction type, you can also add reversals at the same time.

Scope as stated in `docs/control-center/cc-general-ledger-accounts.md`:

> General ledger accounts on the Pismo platform maintain a comprehensive record of all financial transactions that occur within an organization. This supports the double-entry accounting method, which is a common accounting strategy that ensures comprehensive and accurate financial reporting.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/cc-manage-processing-codes-and-transaction-types.md`: Processing codes and transaction types; View processing codes and transaction types
- `docs/control-center/create-processing-codes-and-transaction-types.md`: Create processing codes and transaction types; Create a processing code; Processing codes details; Edit processing code name
- `docs/control-center/add-a-transaction-type-to-an-existing-processing-code.md`: Add a transaction type to an existing processing code
- `docs/control-center/cc-general-ledger-accounts.md`: General ledger accounts; View general ledger accounts; Create a new general ledger account; Deactivate a general ledger account

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/cc-manage-processing-codes-and-transaction-types.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cc-manage-processing-codes-and-transaction-types · updatedAt: 2026-03-18T15:09:42.000Z

<!-- source:begin path=docs/control-center/cc-manage-processing-codes-and-transaction-types.md part=0-end -->

# Processing codes and transaction types

Use Pismo Control Center to view and create processing codes and transaction types. Every organization has a collection of standard processing codes, and you can define custom codes that suit your organization's business requirements. Processing codes identify financial operations on the Pismo platform. For example, `00` is a purchase, `01` is a withdrawal, and so on. These are defined at the organization level so they can be applied to all programs and the accounts they contain.

For transactions, processing codes are mapped to transaction types to create transaction flows. For domains such as balance configurations, flex controls, fees and rules, and rule models, processing codes are used to indicate to which operations to apply controls or fees.

> 📘 Using Control Center vs. using API endpoints to create transaction types
>
> * When using Control Center, you can initially add a transaction type with only one mapped processing code. You can then add additional transaction types later.\
>   To immediately link a processing code to multiple transaction types, you must use the [Payments configurations API](https://developers.pismo.io/pismo-docs/docs/payments-configurations).
> * When you add a transaction type in Control Center, Control Center automatically creates a corresponding reversal processing code and transaction type for you. This code is applied when undoing the operation. However, when you add a transaction with the API endpoints, the platform does not add a reversal code unless you specify one.

For more information about processing codes and transaction types on the Pismo platform, refer to:

* [Standard processing code to transaction type mapping](https://developers.pismo.io/pismo-docs/docs/transactiontypes#standard-processing-code-to-transaction-type-mapping)
* [Processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types)
* [Transaction types](https://developers.pismo.io/pismo-docs/docs/transactiontypes)

# View processing codes and transaction types

You can view the processing codes and transaction types that are configured for your organization directly from Control Center:

1. From the main menu, select **Configurations** > **Processing codes & transaction types**.\
   The **Processing codes and transaction types** screen displays with the **Processing codes** tab open by default.
2. On the **Processing codes and transaction types** screen, do one of the following:
   * On the **Processing codes** tab, select a code from the list to view its details.
   * Select the **Transaction types** tab, then select a transaction type to view its details.
<!-- source:end -->

### Source 2: `docs/control-center/create-processing-codes-and-transaction-types.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/create-processing-codes-and-transaction-types · updatedAt: 2026-03-18T15:09:44.000Z

<!-- source:begin path=docs/control-center/create-processing-codes-and-transaction-types.md part=0-end -->

# Create processing codes and transaction types

With Control Center, you can initially map a transaction type only with one processing code, but you can add more later. When you create a new transaction type, Control Center automatically creates a corresponding reversal processing code and transaction type for you.

# Create a processing code

To create a processing code:

1. From the main menu, select **Configurations** > **Processing codes & transaction types**.\
   The **Processing codes & transaction types** screen displays with the **Processing codes** tab open by default.
2. On the **Processing codes & transaction types** screen, select **Create**.
3. On the **Processing code** tab, enter a unique Processing code name and an ID using 1–6 letters and numbers.
4. Select the type of balance impact for the transaction. Balance impact indicates how a transaction affects an account: it can credit funds, debit funds, or have no impact, known as Zero balance.
5. Optionally, select the appropriate tags to identify related processing codes.
6. Select **Next**.
7. On the **Reversal processing code** tab, select either **Create new** or **Select existing**.
   1. If you chose **Create new**:
      1. Enter a unique Reversal processing code name or leave the default.
      2. Define a Reversal processing code ID using 1–6 letters and numbers.
   2. If you chose **Select existing**, choose the **Select** button next to the existing Reversal processing code you want to add.
8. In the **Partial reversal processing code** section, you will select or create a partial reversal processing code. This code is used to cancel or reverse part of a previously authorized transaction. It releases a portion of the funds. For example, it adjusts the payment amount when a customer returns part of an order.\
   Select **Use default**, **Create new**, or **Select existing**.
   1. If you chose **Create new**:
      1. Enter a unique Partial reversal processing code name or leave the default.
      2. Define a Partial reversal processing code ID using 1–6 letters and numbers.
      3. Select **Next**.
   2. If you chose **Select existing**:
      1. Choose the **Select** button next to the existing Partial reversal processing code you want to add.
      2. Select **Next**.
   3. If you chose **Use default**, select **Next.**
9. On the **Review** tab, verify that the information you provided is correct and select **Finish**.\
   The Processing codes details screen for the processing code you just created is displayed.
10. Since no transaction types have been created yet for this processing code, its status on the **Authorization PC** tab will be **Missing TT**. To add a transaction type, select the **Add transaction type** button at the bottom of the screen.

For details on adding a transaction type to your new processing code, follow the instructions in the [Add a transaction type to an existing processing code](https://developers.pismo.io/pismo-docs/docs/add-a-transaction-type-to-an-existing-processing-code) guide.

To create a processing code using the APIs, use the [Create processing code](https://developers.pismo.io/pismo-docs/reference/createprocessingcode) endpoint.

# Processing codes details

When you select a processing code from the list on the **Processing codes** tab, its details are displayed on the **Processing codes details** screen. This screen has three tabs and open by default to the **Authorization PC** tab.

* **Authorization PC** tab—Displays a list of all authorization processing codes associated with the selected code.
* **Reversal PC** tab—Displays a list of only reversal processing codes associated with the selected code.
* **Partial reversal PC** tab—Displays a list of only partial reversal processing codes associated with the selected code.

# Edit processing code name

To edit a processing code name, select the Edit icon to the right of the name on its details screen then make the desired change and select **Save**.
<!-- source:end -->

### Source 3: `docs/control-center/add-a-transaction-type-to-an-existing-processing-code.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/add-a-transaction-type-to-an-existing-processing-code · updatedAt: 2026-03-18T15:09:46.000Z

<!-- source:begin path=docs/control-center/add-a-transaction-type-to-an-existing-processing-code.md part=0-end -->

# Add a transaction type to an existing processing code

When you need to add another transaction type to an existing processing code, you can either create a new transaction type and add it or you can add an existing transaction type. In addition, when adding a transaction type, you can also add reversals at the same time.

To add another transaction type to an existing processing code:

1. From the main menu, select **Configurations** > **Processing codes & transaction types**.\
   The **Processing codes & transaction types** screen displays with the **Processing codes** tab open by default.
2. Select the processing code to which you want to add a transaction type.
3. On the **Processing code details** screen, select **Add transaction type**.
4. On the **Select processing codes types** screen, select one or more processing code types to associate with the transaction type.
   * **Authorization processing code**—This code is used to authorize a transaction. It specifies the type of request, such as a purchase, cash advance, or balance inquiry, and directs the transaction to the correct network for approval.
   * **Reversal processing code**—This code is used to cancel or reverse a previously authorized transaction. It releases the funds and prevents the transaction from being completed.
   * **Partial reversal processing code**—This code is used to cancel or reverse only part of a previously authorized transaction. It releases a portion of the funds.
5. Select **Next**. The **Transaction type** tab displays. This is the first tab in the process. The other tabs displayed depend on which processing code or codes you selected. Possible tabs are **Reversal transaction type**, **Partial reversal transaction type**, **Transaction flow**, and **Review**.
6. On the **Transaction type** tab, select either **Create new** or **Select existing**.
   1. If you chose **Create new**:
      1. Enter a unique transaction type name and transaction type ID using 4–9 numbers, greater than 7000.
      2. In the **Select the financial type and impact** section:
         1. Select if the transaction type debits or credits funds.
         2. Select if transactions appear on statements.
         3. Select **Next**.
   2. If you chose **Select existing**:
      1. Choose the **Select** button next to the existing transaction type you want to add.
      2. Select **Next**.
7. On the **Reversal transaction type** tab (displayed only if you chose this type of processing code type), select either **Create new** or **Select existing**.
   1. If you chose **Create new**:
      1. Enter a unique Reversal transaction type name and define Reversal transaction type ID using 1–6 letters and numbers.
      2. Select **Next**.
   2. If you chose **Select existing**:
      1. Choose the **Select** button next to the existing Reversal transaction type you want to add.
      2. Select **Next**.
8. On the **Partial reversal transaction type** tab (displayed only if you chose this type of processing code type), select either **Create new** or **Select existing**.
   1. If you chose **Create new**:
      1. Enter a unique Partial reversal transaction type name and define Partial reversal transaction type ID using 1–6 letters and numbers.
      2. Select **Next**.
   2. If you chose **Select existing**:
      1. Choose the **Select** button next to the existing Partial reversal transaction type you want to add.
      2. Select **Next**.
9. On the Transaction flow tab, select a key to define how processing code and transaction type are linked.\
   Note: A transaction flow defines how a processing code maps to transaction types and creates debit and credit entries after authorization.
   1. Select a key. Key options are:
      * **Principal**—Principal is the original amount, excluding interest and fees.
      * **Installment**—An installment splits a purchase or outstanding balance into multiple scheduled payments over time, with fees and interest calculated upfront.
      * **Contract**—Contract is the total amount, including the principal amount, interest, and fees.
      * **Custom key**—A custom key is any value you define, like fees or taxes.
   2. Select **Next**.
10. On the **Review** tab, verify that everything is correct and select **Finish**.

> 📘
>
> If no transaction category is associated with the processing code, its status on the **Transaction type** tab will be **Missing PC**.

You can also create transactions types with the [Create program transaction type](https://developers.pismo.io/pismo-docs/reference/createprogramtransactiontype) endpoint.
<!-- source:end -->

### Source 4: `docs/control-center/cc-general-ledger-accounts.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cc-general-ledger-accounts · updatedAt: 2026-03-18T15:09:40.000Z

<!-- source:begin path=docs/control-center/cc-general-ledger-accounts.md part=0-end -->

# General ledger accounts

General ledger accounts on the Pismo platform maintain a comprehensive record of all financial transactions that occur within an organization. This supports the double-entry accounting method, which is a common accounting strategy that ensures comprehensive and accurate financial reporting.

General ledger accounts keep a record of the funds in your general ledger. Each accounting script has two accounting accounts. One records your organization's assets, and the other records its liabilities.

For information about general ledger accounts on the Pismo platform, refer to [Accounting overview](https://developers.pismo.io/pismo-docs/docs/accounting-overview).

From the Control Center, you can:

* [View general ledger accounts](https://developers.pismo.io/pismo-docs/docs/cc-general-ledger-accounts#view-general-ledger-accounts)
* [Create a new general ledger account](https://developers.pismo.io/pismo-docs/docs/cc-general-ledger-accounts#create-a-new-general-ledger-account)
* [Deactivate a general ledger account](https://developers.pismo.io/pismo-docs/docs/cc-general-ledger-accounts#deactivate-a-general-ledger-account)

Note that you cannot edit or delete general ledger accounts, you can only deactivate them.

# View general ledger accounts

To view a list of all general ledger accounts, including deactivated accounts:

1. From the main menu, select **Configurations** > **General ledger accounts**.
2. On the **General ledger accounts** screen, select an account to view its details.
3. (Optional) Once you display the details of an account, you can rename it. To rename the account, select the **Edit** icon next to the account name, make your change, and **Save** the changes.

# Create a new general ledger account

To create a general ledger account:

1. From the main menu, select **Configurations** > **General ledger accounts**.
2. On the **General ledger accounts** screen, select **Create**.
3. On the **Create a general ledger account** screen, do the following:
   * Enter a name for the account.
   * Enter an account number (up to 50 characters).
   * Choose the programs that you want to use this account, using Search and Browse.
4. Select **Next** then select **Finish**.

# Deactivate a general ledger account

Control Center does not allow you to update or delete general ledger accounts—you can only deactivating them.

Once an account is deactivated, it cannot be reactivated. Inactive general ledger accounts still appear in search results.

To deactivate a general ledger account:

1. From the main menu, select **Configurations** > **General ledger accounts**.
2. On the **General ledger accounts** screen, select **Deactivate account**.
3. Select **Deactivate account** again to confirm.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /orgs-operation/v1/processing-codes` | `CreateProcessingCode` | Create processing code | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `POST /v1/programs/{programId}/program-transaction-types` | `createProgramTransactionType` | Create program transaction type | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-transaction-types |

### Operation essentials

- **`POST /orgs-operation/v1/processing-codes`** (`CreateProcessingCode`): security `S2SAuthentication`; required parameters none declared; required body fields `processing_code`, `balance_impact`, `description`, `reversal_processing_code`; response statuses 201, 400; error codes in examples none; events `orgs-operation-create-1`.
- **`POST /v1/programs/{programId}/program-transaction-types`** (`createProgramTransactionType`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 201, 400, 404, 500; error codes in examples `EX0001`, `EX0002`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `CreateProcessingCode` | `orgs-operation-create-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/control-center/cc-manage-processing-codes-and-transaction-types.md`: updatedAt 2026-03-18T15:09:42.000Z.
- `docs/control-center/create-processing-codes-and-transaction-types.md`: updatedAt 2026-03-18T15:09:44.000Z.
- `docs/control-center/add-a-transaction-type-to-an-existing-processing-code.md`: updatedAt 2026-03-18T15:09:46.000Z.
- `docs/control-center/cc-general-ledger-accounts.md`: updatedAt 2026-03-18T15:09:40.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/cc-manage-processing-codes-and-transaction-types.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cc-manage-processing-codes-and-transaction-types | `7368171dec32f6a3…` | 2026-03-18T15:09:42.000Z |
| `docs/control-center/create-processing-codes-and-transaction-types.md` | whole document | https://developers.pismo.io/pismo-docs/docs/create-processing-codes-and-transaction-types | `3e26f24653e0aa72…` | 2026-03-18T15:09:44.000Z |
| `docs/control-center/add-a-transaction-type-to-an-existing-processing-code.md` | whole document | https://developers.pismo.io/pismo-docs/docs/add-a-transaction-type-to-an-existing-processing-code | `37fa537b3ac30277…` | 2026-03-18T15:09:46.000Z |
| `docs/control-center/cc-general-ledger-accounts.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cc-general-ledger-accounts | `2cdff4a04da535b8…` | 2026-03-18T15:09:40.000Z |

## Related knowledge units

- `KU-API-platform-setup-orgs-operation--processing-codes` — API reference: Platform setup - Orgs operation — Processing codes
- `KU-API-revolving-credit-configurations--program-transaction-types` — API reference: Revolving credit - Configurations — Program transaction types
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CORE-transactiontypes` — Transaction types
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-payments-configurations` — Payments configurations
