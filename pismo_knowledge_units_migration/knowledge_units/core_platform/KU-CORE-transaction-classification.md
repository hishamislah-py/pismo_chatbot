---
ku_id: KU-CORE-transaction-classification
title: Transaction classification model
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/transaction-classification.md
  sha256: 76607fd0b7cd20bbcc4d1ba056319854d99527409cc24991e4d62eedcd7e0621
  url: https://developers.pismo.io/pismo-docs/docs/transaction-classification
  role: primary_guide
  updated_at: '2026-10-02T14:40:01.000Z'
operations: []
related_kus:
- KU-CARD-program-transaction-types
- KU-CARD-transaction-categories
- KU-CORE-processing-codes-and-transaction-types
- KU-CORE-transactiontypes
grouping_rationale: single source page
---

# Transaction classification model

**KU ID:** `KU-CORE-transaction-classification` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/transaction-classification.md`:

> When the Pismo platform processes a transaction, it uses several configurable entities to classify the transaction and determine how to handle it going forward. These entities enable the Pismo platform to:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/transaction-classification.md`: Transaction classification model; Entities for classifying transactions; Processing codes; Why processing codes exist; For more information; Transaction types; Why transaction types exist; For more information; Program transaction types; Why program transaction types exist; Common customization scenarios; For more information; Transaction categories; Why transaction categories exist; Example transaction categories; For more information; How the entities work together; Example: Card purchase; Step 1: Processing code identifies the transaction.; Step 2: Transaction type defines transaction behavior that the organization level.; Step 3: Program transaction type adds product-specific behavior.; Step 4: Transaction category groups the transaction.; Choosing the right configuration entity

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/transaction-classification.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/transaction-classification · updatedAt: 2026-10-02T14:40:01.000Z

<!-- source:begin path=docs/core-platform/transaction-classification.md part=0-end -->

# Transaction classification model

When the Pismo platform processes a transaction, it uses several configurable entities to classify the transaction and determine how to handle it going forward. These entities enable the Pismo platform to:

* Identify the nature of a transaction
* Apply program-specific business rules
* Group transactions for reporting and operational purposes
* Configure limits, fees, rewards, and other transaction-related behaviors

Understanding how these entities relate to one another is essential when configuring a new product or troubleshooting transaction behavior.

# Entities for classifying transactions

The Pismo platform uses the following entities to classify transactions.

| Entity                                                                               | Purpose                                                                |
| :----------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| [Processing code](https://developers.pismo.io/pismo-docs/docs/transaction-classification#processing-codes)                   | Identifies the fundamental purpose of the transaction.                 |
| [Transaction type](https://developers.pismo.io/pismo-docs/docs/transaction-classification#transaction-types)                 | Represents an organization-level transaction definition.               |
| [Program transaction type](https://developers.pismo.io/pismo-docs/docs/transaction-classification#program-transaction-types) | Allows a program to customize transaction behavior.                    |
| [Transaction category](https://developers.pismo.io/pismo-docs/docs/transaction-classification#transaction-categories)        | Groups transactions for business, reporting, and operational purposes. |

Each entity acts as a layer of meaning or customization added to the transaction it's assigned to. These layers determine how the Pismo platform applies business rules to the transactions. The following sections describe these entities in more detail.

## Processing codes

A processing code is the earliest classification assigned to a transaction. It identifies the transaction's primary purpose and provides the foundation for all subsequent classification. Processing codes typically originate from information received during transaction processing.

Examples include:

* Purchase
* Withdrawal
* Refund
* Payment Balance inquiry

### Why processing codes exist

Processing codes provide a consistent method for identifying transaction behavior regardless of program configuration. For example, a purchase remains a purchase regardless of whether it belongs to a consumer credit card, commercial card, prepaid card, or debit product.

By establishing a consistent starting point, processing codes create a reusable transaction model that can support multiple products and programs.

### For more information

For more information about processing codes, refer to the [Processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) guide.

## Transaction types

A transaction type defines a specific transaction behavior within the Pismo platform. While processing codes identify the general purpose of a transaction, transaction types provide a more detailed organization-level classification.

Examples:

* A straight forward purchase using a card:\
  Processing code: Purchase > Transaction type: Card purchase
* An international purchase might include a fee:\
  Processing code: International Purchase > Transaction type: International Card purchase > Transaction type: Cross Border Fee

The transaction type is the foundation for transaction processing rules.

<Callout icon="📘" theme="info">
  Transaction types are defined at the organization level, unlike [program transaction types](https://developers.pismo.io/pismo-docs/docs/transaction-classification#program-transaction-types), which are program-specific.
</Callout>

### Why transaction types exist

Transaction types allow the Pismo platform to standardize transaction handling across programs.

Examples of behavior associated with transaction types include:

* Accounting treatment
* Settlement processing
* Interest calculations
* Authorization behavior
* Posting rules

Because you define transaction types at the organization level, you can reuse them across many programs.

Transaction types describe what a transaction is. They do not typically describe how an individual program wants to use that transaction. Program-specific customization occurs at the next layer.

### For more information

For more information about transaction types, refer to the [Transaction types](https://developers.pismo.io/pismo-docs/docs/transactiontypes) guide.

## Program transaction types

A program transaction type represents a program-specific implementation of a transaction type. This layer allows institutions to tailor transaction definitions to the needs of a specific card program or product.

Examples:\
Transaction type: Card purchase > Program transaction type: Consumer purchase\
Transaction type: Card purchase > Program transaction type: Corporate purchase

Both examples can share the same underlying transaction type while behaving differently at the program level.

### Why program transaction types exist

Different products often require different business rules. For example, a consumer credit product might allow certain transaction types that a commercial card program does not. A corporate card product might apply different spending controls, reporting rules, or accounting treatment.

Rather than creating new transaction types for each product, program transaction types provide a configurable layer where you can apply your business requirements.

### Common customization scenarios

Program transaction types are commonly used to configure:

* Product-specific processing behavior
* Spending controls
* Fee behavior
* Rewards eligibility
* Operational workflows
* Reporting requirements

This separation improves maintainability by enabling changes at the program level without affecting the organization-wide transaction definitions.

### For more information

For more information about program transaction types, refer to the [Program transaction types](https://developers.pismo.io/pismo-docs/docs/program-transaction-types) guide.

## Transaction categories

Transaction categories group transactions into business-oriented classifications. While transaction types and program transaction types focus on transaction behavior, transaction categories focus on operational and business organization.

For example:\
Program transaction type: Corporate purchase > Transaction category: Purchases

Multiple program transaction types can belong to the same transaction category.

### Why transaction categories exist

Organizations often need to treat groups of transactions similarly for configuration or reporting purposes. Transaction categories provide a way to organize transactions without changing their underlying processing definitions.

**You set values for interest rates in transaction categories.** A transaction type inherits its interest rates from the transaction category it belongs to, so the interest rates applied to transactions are ultimately determined by the transaction categories.

**Transaction categories also allow programs to:**

* Apply the same limit controls to all purchase-related transactions.
* Group cash-related transactions together for reporting.
* Produce operational reports using business-friendly categories.

### Example transaction categories

The following table shows some examples of commonly-used transaction categories.

| Transaction category | Typical purpose                            |
| :------------------- | :----------------------------------------- |
| Purchases            | Standard purchase transactions             |
| Cash transactions    | Cash withdrawals and cash-related activity |
| Payments             | Payment and repayment activity             |
| Fees                 | Service charges and operational fees       |
| Adjustments          | Account corrections and adjustments        |

### For more information

For more information about transaction categories, refer to the [Transaction categories](https://developers.pismo.io/pismo-docs/docs/transaction-category-structure) guide.

# How the entities work together

The easiest way to understand the transaction classification model is to follow a transaction through the hierarchy.

## Example: Card purchase

Assume a cardholder makes a purchase at a merchant.

### Step 1: Processing code identifies the transaction.

The transaction enters the platform and is identified as a purchase.

Example:\
Processing code: Purchase

### Step 2: Transaction type defines transaction behavior that the organization level.

The transaction is mapped to a transaction type.

Example:\
Transaction type: Card purchase

The Pismo platform now understands how it should process this type of transaction within the organization in general.

### Step 3: Program transaction type adds product-specific behavior.

The transaction is associated with a program-specific definition.

Example:\
Program transaction type: Corporate purchase

At this stage, you can apply product-specific business logic.

### Step 4: Transaction category groups the transaction.

The transaction is assigned to a transaction category.

Example:\
Transaction category: Purchases

The transaction can now participate in reporting, controls, and operational processes associated with that category.

# Choosing the right configuration entity

When configuring transaction behavior, it's important to modify the correct entity. The following table clarifies which entity to use for various outcome goals.

| Goal                                               | Entity to configure      |
| :------------------------------------------------- | :----------------------- |
| Identify the fundamental purpose of a transaction. | Processing code          |
| Define organization transaction behavior.          | Transaction type         |
| Customize behavior for a specific program.         | Program transaction type |
| Group transactions for business use and reporting  | Transaction category     |

As a general rule:

* Use transaction types to define behavior at the organization level.
* Use program transaction types to configure product-specific behavior.
* Use transaction categories to organize transactions for business purposes.
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/transaction-classification.md`: updatedAt 2026-10-02T14:40:01.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/transaction-classification.md` | whole document | https://developers.pismo.io/pismo-docs/docs/transaction-classification | `76607fd0b7cd20bb…` | 2026-10-02T14:40:01.000Z |

## Related knowledge units

- `KU-CARD-program-transaction-types` — Program transaction types
- `KU-CARD-transaction-categories` — Transaction categories
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CORE-transactiontypes` — Transaction types
