---
ku_id: KU-CORE-transactiontypes
title: Transaction types
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/transactiontypes.md
  sha256: 02240170ea95672d12fad909ee96ccb4836a5c4b6b3a71034d1cf2f16e5cc598
  url: https://developers.pismo.io/pismo-docs/docs/transactiontypes
  role: primary_guide
  updated_at: '2026-04-08T11:53:16.000Z'
operations:
- CreateProcessingCode
- PostSetupTransactionType
- SearchTransactionTypes
- post-payments-v1-payments
related_kus:
- KU-API-core-platform-payment-methods--payments
- KU-API-core-platform-transactions--transaction-types
- KU-API-platform-setup-orgs-operation--processing-codes
- KU-CC-processing-codes
- KU-CORE-accounting-overview
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-GS-program-types
- KU-PAY-payments-configurations
grouping_rationale: single source page
---

# Transaction types

**KU ID:** `KU-CORE-transactiontypes` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/transactiontypes.md`:

> A transaction type identifies a transaction, such as a purchase, as either a credit or a debit operation and determines whether the transaction has a financial impact on the customer account. Call [List transaction types](https://developers.pismo.io/pismo-docs/reference/searchtransactiontypes) to get the transaction types configured for your organization.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/transactiontypes.md`: Transaction types; Transaction flows; Step 1—Client application makes a request; Step 2—Pismo evaluates the request; Step 3—Pismo generates a transaction; Step 4—Pismo updates the bank statement; Custom processing codes and transaction flow; Payments configurations; Standard processing code to transaction type mapping

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/transactiontypes.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/transactiontypes · updatedAt: 2026-04-08T11:53:16.000Z

<!-- source:begin path=docs/core-platform/transactiontypes.md part=0-end -->

# Transaction types

A transaction type identifies a transaction, such as a purchase, as either a credit or a debit operation and determines whether the transaction has a financial impact on the customer account. Call [List transaction types](https://developers.pismo.io/pismo-docs/reference/searchtransactiontypes) to get the transaction types configured for your organization.

The Pismo platform maps transaction types to [processing codes](https://developers.pismo.io/pismo-docs/docs/processingcodes)  to create ***transaction flows***.  Call the [List transaction flows](https://developers.pismo.io/pismo-docs/reference/searchtransactiontypes)  endpoint to get your organization's transaction flow configurations. For more information, refer to [standard processing code to transaction type mapping](https://developers.pismo.io/pismo-docs/docs/transactiontypes#standard-processing-code-to-transaction-type-mapping).

A processing code can have one or more transaction types configured, one for each transaction it generates. depending on whether one or more transactions can be created using the processing code. Use the [create custom transaction types](https://developers.pismo.io/pismo-docs/reference/postsetuptransactiontype) endpoint to create transaction types that represent different kinds of financial operations applicable to your organization.

> 📘 Pismo Control Center
>
> You can also use Pismo Control Center to view and create processing codes and transaction types, including reversals. For details, refer to [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/cc-manage-processing-codes-and-transaction-types).

<Image align="center" alt="Transaction types" src="https://files.readme.io/e4c9622b3ffdc2771437ae825fbde195e35f89e1d35d33a14e054773ffa364ed-transactionTypes.png" />

Processing codes and transaction types enable you to configure a single operation to generate multiple transactions. Each processing code request creates an authorization that, in turn, generates one or more transactions of different transaction types, as illustrated above.

Transaction types are objects with the following **key** fields (not a complete list):

| Field                 | Type    | Description                                         |
| :-------------------- | :------ | :-------------------------------------------------- |
| `transaction_type_id` | integer | Transaction type ID. For example, `101` = purchase. |
| `credit`              | boolean | Is this a credit or debit operation?                |
| `posted_transaction`  | boolean | Should this transaction be posted on statements?    |

# Transaction flows

The following diagram illustrates the basic transaction flows on the Pismo platform and how the platform uses the processing codes and their mappings to transaction types. The steps that follow the diagram explain the flows in more detail.

<Image align="center" alt="Basic transaction flows diagram" src="https://files.readme.io/88fda1319c19862bec0dc6aa6c0a42bb3ce85f659d5554c566a8d751a962fd3a-Processing_codes_and_transaction_typesDesign.png" />

### Step 1—Client application makes a request

This request  includes the processing codes.

#### Transfer processing codes

Use two different processing codes in a single request when it’s a [transfer](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) operation.

* One processing code that defines an operation to debit an internal account in the `from` array.
* Another processing code that defines an operation to credit an external account in the `to` array.

### Step 2—Pismo evaluates the request

The platform evaluates the request, creates an authorization, and generates the [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) event.

### Step 3—Pismo generates a transaction

The platform uses the predefined mapping between the processing code and corresponding transaction types to create at least one transaction. Each transaction generates a [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1) event.

**Note:** One authorization can generate multiple transactions: for example, one transaction for a principal amount and another transaction for an additional fee. These transactions can be of different types, debit or credit.

### Step 4—Pismo updates the bank statement

Pismo updates the bank statement with the created transactions.

Processing codes and their relationships with transaction types have accounting implications. For example, if you have a debit operation, then the platform generates an accounting event for this operation. For more information, refer to [Accounting overview](https://developers.pismo.io/pismo-docs/docs/accounting-overview).

# Custom processing codes and transaction flow

When you [create a custom processing code](https://developers.pismo.io/pismo-docs/reference/createprocessingcode), it initially has  a `PENDING` status. You can't use it in authorizations while it's in this status. Once you configure its transaction flow, its status changes to `SUCCESS`, and it's ready for use. All standard processing codes have a `SUCCESS` status.

# Payments configurations

You can configure processing codes, transaction types, their mappings, and other settings that manage how the platform processes operations in the payments and transactions flow. For more information, refer to [Payments configurations](https://developers.pismo.io/pismo-docs/docs/payments-configurations), which explains how to create your own transaction flows.

# Standard processing code to transaction type mapping

The platform has templates to associate standard processing codes with Pismo [program types](https://developers.pismo.io/pismo-docs/docs/program-types). The following templates are examples that can help you map the processing codes to the Pismo programs. Templates might include codes not applicable to your region.

<details>
  <summary style={{ fontSize: "18px" }}>
    <b>Transaction banking</b>
  </summary>

  Accounts belonging to the transaction banking program types (current, internal, and correspondent).

  | Processing code | Processing code description        | Balance impact          | Transaction type | Transaction type description       |
  | :-------------- | :--------------------------------- | :---------------------- | ---------------- | ---------------------------------- |
  | 219248          | HOLD FUNDS                         | **-1** (debit, cashout) | 7128             | HOLD FUNDS                         |
  | 219249          | HOLD FUNDS CANCEL                  | **1** (credit, cashin)  | 92000046         | HOLD FUNDS CANCEL                  |
  | 219251          | RELEASE FUNDS                      | **1** (credit, cashin)  | 7129             | RELEASE FUNDS                      |
  | 219252          | RELEASE FUNDS CANCEL               | **-1** (debit, cashout) | 92000047         | RELEASE FUNDS CANCEL               |
  | 219258          | HELD FUNDS CASHOUT TRANSFER        | **-1** (debit, cashout) | 92000048         | HELD FUNDS CASHOUT TRANSFER        |
  | 219259          | UNDO HELD FUNDS CASHOUT TRANSFER   | **1** (credit, cashin)  | 92000049         | UNDO HELD FUNDS CASHOUT TRANSFER   |
  | 220035          | CASHIN TRANSFER                    | **1** (credit, cashin)  | 92000040         | CASHIN TRANSFER                    |
  | 220036          | UNDO CASHIN TRANSFER               | **-1** (debit, cashout) | 92000041         | UNDO CASHIN TRANSFER               |
  | 220037          | CASHOUT TRANSFER                   | **-1** (debit, cashout) | 92000042         | CASHOUT TRANSFER                   |
  | 220038          | UNDO CASHOUT TRANSFER              | **1** (credit, cashin)  | 92000043         | UNDO CASHOUT TRANSFER              |
  | 220039          | CREDIT ADJUSTMENT                  | **1** (credit, cashin)  | 92000044         | CREDIT ADJUSTMENT                  |
  | 220040          | DEBIT ADJUSTMENT                   | **-1** (debit, cashout) | 92000045         | DEBIT ADJUSTMENT                   |
  | 220041          | FUTURE DATED CASHIN TRANSFER       | **1** (credit, cashin)  | 92000050         | FUTURE DATED CASHIN TRANSFER       |
  | 220042          | UNDO FUTURE DATED CASHIN TRANSFER  | **-1** (debit, cashout) | 92000051         | UNDO FUTURE DATED CASHIN TRANSFER  |
  | 220043          | FUTURE DATED CASHOUT TRANSFER      | **-1** (debit, cashout  | 92000052         | FUTURE DATED CASHOUT TRANSFER      |
  | 220044          | UNDO FUTURE DATED CASHOUT TRANSFER | **1** (credit, cashin)  | 92000053         | UNDO FUTURE DATED CASHOUT TRANSFER |
</details>

<details>
  <summary style={{ fontSize: "18px" }}>
    <b>Full balance debit</b>
  </summary>

  Accounts for core banking with balance controls within the Pismo platform.

  | Processing code | Processing code description       | Balance impact                    | Transaction type | Transaction type description      |
  | :-------------- | :-------------------------------- | :-------------------------------- | ---------------- | --------------------------------- |
  | 00              | PURCHASE                          | **-1** (debit, cashout)           | 101              | PURCHASE                          |
  | 0001            | REFUND PURCHASE                   | **1** (credit, cashin)            | 503              | PURCHASE REVERSAL                 |
  | 003100          | INTERNATIONAL PURCHASE            | **-1** (debit, cashout)           | 102              | INTERNATIONAL PURCHASE            |
  | 003101          | INTERNATIONAL PURCHASE REVERSAL   | **1** (credit, cashin)            | 508              | INTERNATIONAL PURCHASE REV        |
  | 007000          | DEBIT TRANSFER                    | **-1** (debit, cashout)           | 304              | DEBIT TRANSFER                    |
  | 007001          | DEBIT REVERSAL                    | **1** (credit, cashin)            | 392              | DEBIT REVERSAL                    |
  | 007200          | CREDIT TRANSFER                   | **1** (credit, cashin)            | 320              | MONEY ORDER                       |
  | 007201          | CREDIT REVERSAL                   | **-1** (debit, cashout)           | 391              | CREDIT REVERSAL                   |
  | 007503          | DEPOSIT BY BILL                   | **1** (credit, cashin)            | 341              | DEPOSIT BY BILL                   |
  | 007700          | ZERO DEBIT TRANSFER               | **0** (no impact, zero balance)\* | 330              | ZERO DEBIT TRANSFER               |
  | 007701          | TRANSFER REVERSION ZERO DEBIT     | **0** (no impact, zero balance)\* | 331              | TRANSFER REVERSION ZERO DEBIT     |
  | 01              | NATIONAL WITHDRAWAL               | **-1** (debit, cashout)           | 123              | WITHDRAWAL                        |
  | 01              | NATIONAL WITHDRAWAL               | **-1** (debit, cashout)           | 604              | WITHDRAWAL FEE                    |
  | 0101            | REVERSE NATIONAL WITHDRAWAL       | **1** (credit, cashin)            | 512              | REVERSAL WITHDRAWAL               |
  | 0101            | REVERSE NATIONAL WITHDRAWAL       | **1** (credit, cashin)            | 9467             | REVERSAL FEE WITHDRAWAL           |
  | 013100          | INTERNATIONAL WITHDRAWAL          | **-1** (debit, cashout)           | 124              | INTERNATIONAL WITHDRAWAL          |
  | 013100          | INTERNATIONAL WITHDRAWAL          | **-1** (debit, cashout)           | 604              | WITHDRAWAL FEE                    |
  | 013101          | REVERSAL INTERNATIONAL WITHDRAWAL | **1** (credit, cashin)            | 510              | REVERSAL INTERNATIONAL WITHDRAWAL |
  | 20              | NATIONAL CREDIT VOUCHER           | **1** (credit, cashin)            | 203              | CREDIT VOUCHER                    |
  | 203100          | INTERNATIONAL CREDIT VOUCHER      | **1** (credit, cashin)            | 253              | CREDIT VOUCHER INTER              |
  | 903002          | UTILITIES PAYMENT                 | **1** (credit, cashin)            | 917              | UTILITIES PAYMENT                 |
  | 904002          | UTILITIES PAYMENT REVERSAL        | **-1** (debit, cashout)           | 541              | UTILITIES PAYMENT STATE           |
</details>

<details>
  <summary style={{ fontSize: "18px" }}>
    <b>Full balance credit</b>
  </summary>

  Accounts for credit cards with balance controls within the Pismo platform.

  | Processing code | Processing code description            | Balance impact          | Transaction type | Transaction type description         |
  | :-------------- | :------------------------------------- | :---------------------- | ---------------- | ------------------------------------ |
  | 219734          | INTEREST ON REVOLVING CREDIT           | **-1** (debit, cashout) | 401              | INTEREST ON REVOLVING CREDIT         |
  | 219735          | CAN INTEREST ON REVOLVING CREDIT       | **1** (credit, cashin)  | 451              | CAN INTEREST ON REVOLVING CREDIT     |
  | 219736          | UNDO CANC INTEREST ON REVOLVING CREDIT | **-1** (debit, cashout) | 4519             | INT ON REVOLV CREDIT REV CANC        |
  | 219737          | LATE PAYMENT INTEREST                  | **-1** (debit, cashout) | 402              | LATE PAYMENT INTEREST                |
  | 219738          | CAN LATE PAYMENT INTEREST              | **1** (credit, cashin)  | 452              | CAN LATE PAYMENT INTEREST            |
  | 219739          | UNDO CANC LATE PAYMENT INTEREST        | **-1** (debit, cashout) | 4529             | LATE PAYMENT INT REV CANC            |
  | 219740          | LATE FEE                               | **-1** (debit, cashout) | 403              | LATE FEE                             |
  | 219741          | CAN LATE FEE                           | **1** (credit, cashin)  | 453              | CAN LATE FEE                         |
  | 219742          | UNDO CANC LATE FEE                     | **-1** (debit, cashout) | 4539             | LATE FEE REV CANC                    |
  | 219743          | TAXES                                  | **-1** (debit, cashout) | 405              | TAXES                                |
  | 219744          | CAN TAXES                              | **1** (credit, cashin)  | 455              | CAN TAXES                            |
  | 219745          | UNDO CANC TAXES                        | **-1** (debit, cashout) | 4559             | TAXES REV CANC                       |
  | 219746          | OVERLIMIT FEE                          | **-1** (debit, cashout) | 676              | OVERLIMIT FEE                        |
  | 219747          | CAN OVERLIMIT FEE                      | **1** (credit, cashin)  | 6769             | OVERLIMIT FEE REVERSAL               |
  | 219748          | UNDO CANC OVERLIMIT FEE                | **-1** (debit, cashout) | 67699            | OVERLIMIT FEE REV CANC               |
  | 219749          | DEBIT EXCHANGE DIFFERENCE\*            | **-1** (debit, cashout) | 408              | DEBIT EXCHANGE DIFFERENCE            |
  | 219750          | CAN DEBIT EXCHANGE DIFFERENCE          | **1** (credit, cashin)  | 4089             | CAN DEBIT EXCHANGE DIFFERENCE        |
  | 219751          | UNDO CANC DEBIT EXCHANGE DIFFERENCE    | **-1** (debit, cashout) | 40899            | DEBIT EXC DIFFE REV CANC             |
  | 219752          | CREDIT EXCHANGE DIFFERENCE             | **1** (credit, cashin)  | 409              | CREDIT EXCHANGE DIFFERENCE           |
  | 219753          | CAN CREDIT EXCHANGE DIFFERENCE         | **-1** (debit, cashout) | 4099             | CREDIT EXCHANGE DIFFE REV            |
  | 219754          | UNDO CANC CREDIT EXCHANGE DIFFERENCE   | **1** (credit, cashin)  | 40999            | UNDO CANC CREDIT EXCHANGE DIFFERENCE |
  | 219755          | ANNUITY\*                              | **-1** (debit, cashout) | 602              | ANNUITY                              |
  | 219756          | CAN ANNUITY                            | **1** (credit, cashin)  | 606              | CAN ANNUITY                          |
  | 219757          | UNDO CAN ANNUITY                       | **-1** (debit, cashout) | 99602            | UNDO CAN ANNUITY                     |
  | 00              | PURCHASE                               | **-1** (debit, cashout) | 101              | PURCHASE                             |
  | 0001            | REFUND PURCHASE                        | **1** (credit, cashin)  | 503              | PURCHASE REVERSAL                    |
  | 003100          | INTERNATIONAL PURCHASE                 | **-1** (debit, cashout) | 102              | INTERNATIONAL PURCHASE               |
  | 003101          | INTERNATIONAL PURCHASE REV             | **1** (credit, cashin)  | 508              | INTERNATIONAL PURCHASE REV           |
  | 003800          | INSTALLMENT WITHOUT INTEREST           | **-1** (debit, cashout) | 111              | INSTALLMENT WITHOUT INTEREST         |
  | 003800          | INSTALLMENT WITHOUT INTEREST           | **-1** (debit, cashout) | 112              | INSTALLMENT WITHOUT INTEREST         |
  | 003801          | INSTALLMENT WITHOUT INTEREST REV       | **1** (credit, cashin)  | 504              | INSTALLMENT WITHOUT INTEREST REV     |
  | 003801          | INSTALLMENT WITHOUT INTEREST REV       | **1** (credit, cashin)  | 505              | INSTALLMENT WITHOUT INTEREST REV     |
  | 004000          | PAYMENT                                | **1** (credit, cashin)  | 201              | PAYMENT                              |
  | 004990          | CREDIT BY INSTALLMENTS                 | **1** (credit, cashin)  | 701              | CREDIT BY INSTALLMENTS               |
  | 004991          | REFINANCING AGREEMENT                  | **1** (credit, cashin)  | 711              | REFINANCING AGREEMENT                |
  | 004992          | COMPULSORY INSTALLMENT CREDIT          | **1** (credit, cashin)  | 721              | COMPULSORY INSTALLMENT CREDIT        |
  | 004995          | CAN CREDIT BY INSTALLMENTS             | **-1** (debit, cashout) | 705              | CAN CREDIT BY INSTALLMENTS           |
  | 004996          | CAN REFINANCING AGREEMENT              | **-1** (debit, cashout) | 715              | CAN REFINANCING AGREEMENT            |
  | 004997          | CANC CREDIT COMPULSORY INSTALLMENT     | **-1** (debit, cashout) | 725              | CANCEL COMPULSORY INST CREDIT        |
  | 009100          | CREDIT ADJUSTMENT                      | **1** (credit, cashin)  | 301              | CREDIT ADJUSTMENT                    |
  | 009200          | DEBIT ADJUSTMENT                       | **-1** (debit, cashout) | 302              | DEBIT ADJUSTMENT                     |
  | 01              | NATIONAL WITHDRAWAL                    | **-1** (debit, cashout) | 123              | WITHDRAWAL                           |
  | 01              | NATIONAL WITHDRAWAL                    | **-1** (debit, cashout) | 407              | WITHDRAWAL CHARGES                   |
  | 01              | NATIONAL WITHDRAWAL                    | **-1** (debit, cashout) | 604              | WITHDRAWAL FEE                       |
  | 0101            | NATIONAL WITHDRAWAL REV                | **1** (credit, cashin)  | 512              | WITHDRAWAL REV                       |
  | 0101            | NATIONAL WITHDRAWAL REV                | **1** (credit, cashin)  | 513              | WITHDRAWAL CHARGES REV               |
  | 0101            | NATIONAL WITHDRAWAL REV                | **1** (credit, cashin)  | 9467             | WITHDRAWAL FEE REV                   |
  | 013100          | INTERNATIONAL WITHDRAWAL               | **-1** (debit, cashout) | 124              | INTERNATIONAL WITHDRAWAL             |
  | 013100          | INTERNATIONAL WITHDRAWAL               | **-1** (debit, cashout) | 604              | WITHDRAWAL FEE                       |
  | 013101          | INTERNATIONAL WITHDRAWAL REV           | **1** (credit, cashin)  | 512              | WITHDRAWAL REV                       |
  | 013101          | INTERNATIONAL WITHDRAWAL REV           | **1** (credit, cashin)  | 617              | INTER WITHDRAWAL FEE REV             |
  | 20              | NATIONAL CREDIT VOUCHER                | **1** (credit, cashin)  | 203              | CREDIT VOUCHER                       |
  | 203100          | INTERNATIONAL CREDIT VOUCHER           | **1** (credit, cashin)  | 253              | CREDIT VOUCHER INTER                 |

  * DEBIT EXCHANGE DIFFERENCE: This is DEPRECATED and had been used for charging exchange differences in international purchases.
  * ANNUITY: This is DEPRECATED and had been used for charging credit card annuity.
</details>

<details>
  <summary style={{ fontSize: "18px" }}><b>Full balance prepaid</b></summary>

  Accounts for prepaid credit cards with balance controls within the Pismo platform.

  | Processing code | Processing code description       | Balance impact          | Transaction type | Transaction type description |
  | :-------------- | :-------------------------------- | :---------------------- | ---------------- | ---------------------------- |
  | 00              | PURCHASE                          | **-1** (debit, cashout) | 101              | PURCHASE                     |
  | 0001            | REFUND PURCHASE                   | **1** (credit, cashin)  | 503              | PURCHASE CANCELLATION        |
  | 003100          | INTERNATIONAL PURCHASE            | **-1** (debit, cashout) | 102              | INTERNATIONAL PURCHASE       |
  | 003101          | INTERNATIONAL PURCHASE REVERSAL   | **1** (credit, cashin)  | 508              | CANC INTERNATIONAL PURCHASE  |
  | 007000          | DEBIT TRANSFER                    | **-1** (debit, cashout) | 304              | DEBIT TRANSFER               |
  | 007001          | DEBIT REVERSAL                    | **1** (credit, cashin)  | 392              | DEBIT REVERSAL               |
  | 007200          | CREDIT TRANSFER                   | **1** (credit, cashin)  | 320              | CREDIT TRANSFER              |
  | 007201          | CREDIT REVERSAL                   | **-1** (debit, cashout) | 391              | CREDIT REVERSAL              |
  | 01              | NATIONAL WITHDRAWAL               | **-1** (debit, cashout) | 123              | WITHDRAWAL                   |
  | 01              | NATIONAL WITHDRAWAL               | **-1** (debit, cashout) | 407              | WITHDRAWAL CHARGES           |
  | 01              | NATIONAL WITHDRAWAL               | **-1** (debit, cashout) | 604              | WITHDRAWAL FEE               |
  | 0101            | REVERSE NATIONAL WITHDRAWAL       | **1** (credit, cashin)  | 512              | REVERSAL WITHDRAWAL          |
  | 0101            | REVERSE NATIONAL WITHDRAWAL       | **1** (credit, cashin)  | 513              | REVERSAL WITHDRAWAL CHARGES  |
  | 0101            | REVERSE NATIONAL WITHDRAWAL       | **1** (credit, cashin)  | 9467             | REVERSAL FEE WITHDRAWAL      |
  | 013100          | INTERNATIONAL WITHDRAWAL          | **-1** (debit, cashout) | 124              | INTERNATIONAL WITHDRAWAL     |
  | 013101          | REVERSAL INTERNATIONAL WITHDRAWAL | **1** (credit, cashin)  | 512              | REVERSAL  WITHDRAWAL         |
  | 20              | NATIONAL CREDIT VOUCHER           | **1** (credit, cashin)  | 203              | CREDIT VOUCHER               |
  | 203100          | INTERNATIONAL CREDIT VOUCHER      | **1** (credit, cashin)  | 253              | CREDIT VOUCHER INTER         |
</details>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /v1/transaction-types` | `SearchTransactionTypes` | List transaction types | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `POST /v1/transaction-types` | `PostSetupTransactionType` | Create transaction type | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `POST /payments/v1/payments` | `post-payments-v1-payments` | Transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /orgs-operation/v1/processing-codes` | `CreateProcessingCode` | Create processing code | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |

### Operation essentials

- **`GET /v1/transaction-types`** (`SearchTransactionTypes`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `WTRC00001`, `ETRC05001`, `ETRC00001`; events none listed.
- **`POST /v1/transaction-types`** (`PostSetupTransactionType`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `description`, `credit`, `posted_transaction`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00005`, `WTRC05001`, `WTRC08001`, `ETRC00001`; events `transaction-types-creation-1`.
- **`POST /payments/v1/payments`** (`post-payments-v1-payments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `from`, `to`; response statuses 201, 202, 400, 409, 422, 500, 502; error codes in examples `WP2P0000`, `WP2P0019`, `EP2P9999`, `WP2P0005`, `WP2P0006`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WP2P0020`, `WP2P0013`, `WLDG0006`, `WP2P0010`, `WP2P0000`, `WP2P0000`, `ELDG500`, `EPCG501`, `EP2P9999`, `EP2P0001`, `EP2P0002`; events `authorization-authorization-event-1`.
- **`POST /orgs-operation/v1/processing-codes`** (`CreateProcessingCode`): security `S2SAuthentication`; required parameters none declared; required body fields `processing_code`, `balance_impact`, `description`, `reversal_processing_code`; response statuses 201, 400; error codes in examples none; events `orgs-operation-create-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v1-payments` | `authorization-authorization-event-1` |
| `CreateProcessingCode` | `orgs-operation-create-1` |
| `PostSetupTransactionType` | `transaction-types-creation-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `authorization-authorization-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-event-1 | 9 | KU-EVT-catalogue-other-domains |
| `transaction-creation-1` | transaction | 1 | https://developers.pismo.io/events/docs/transaction-creation-1 | 7 | KU-EVT-catalogue-transaction |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/transactiontypes.md`: updatedAt 2026-04-08T11:53:16.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/transactiontypes.md` | whole document | https://developers.pismo.io/pismo-docs/docs/transactiontypes | `02240170ea95672d…` | 2026-04-08T11:53:16.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-platform-setup-orgs-operation--processing-codes` — API reference: Platform setup - Orgs operation — Processing codes
- `KU-CC-processing-codes` — Control Center processing codes, transaction types and general ledger accounts
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-GS-program-types` — Program types
- `KU-PAY-payments-configurations` — Payments configurations
