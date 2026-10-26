---
ku_id: KU-PAY-bacs
title: 'BACS: clearing, Direct Debit mandates and indemnity claims'
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/banking-automated-clearing-system.md
  sha256: 2c49b96df07d758ac52c48eeed595a89f09650d737801a01398af52c7bcd8de6
  url: https://developers.pismo.io/pismo-docs/docs/banking-automated-clearing-system
  role: primary_guide
  updated_at: '2026-08-28T20:22:51.000Z'
- path: docs/core-banking/bacs-direct-debit-and-mandate-processing.md
  sha256: faceeca614093ebc9df86cb9c49507ac9281b1a8152b8babd0ce9f86479d5845
  url: https://developers.pismo.io/pismo-docs/docs/bacs-direct-debit-and-mandate-processing
  role: primary_guide
  updated_at: '2026-10-08T14:05:37.000Z'
- path: docs/core-banking/bacs-direct-debit-indemity-claims.md
  sha256: 69cd3f67261389631092c830a399a9e2c4aff1d729b109124b2c2f67f7ce7b88
  url: https://developers.pismo.io/pismo-docs/docs/bacs-direct-debit-indemity-claims
  role: primary_guide
  updated_at: '2026-10-09T12:34:49.000Z'
operations:
- get-bacs-claim-list
- patch-accounts-v1-accounts
- post-acquisitions-v3-s2s-applications
- post-cancel-bacs
- post-create-bacs
- post-create-claim
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan
- post-raise-claim-reversal
- post-release-bacs
related_kus:
- KU-API-banking-bank-accounts--bank-accounts-part-01
- KU-API-core-platform-accounts--accounts
- KU-API-payment-rails-bacs-payments--bacs-direct-credit
- KU-API-payment-rails-bacs-payments--bacs-direct-debit
- KU-EVT-catalogue-account
- KU-EVT-catalogue-bacs
- KU-EVT-catalogue-other-domains
- KU-PAY-faster-payment-system
grouping_rationale: One payment rail.
---

# BACS: clearing, Direct Debit mandates and indemnity claims

**KU ID:** `KU-PAY-bacs` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: One payment rail.

Scope as stated in `docs/core-banking/banking-automated-clearing-system.md`:

> The <a href="https://www.moderntreasury.com/learn/what-is-bacs" target="_blank">Bankers' Automated Clearing System</a> (BACS) is a long-standing electronic payment system in the United Kingdom used to transfer money directly between bank accounts. BACS is cheap and reliable, making it ideal for bulk payments like employee payrolls and is widely integrated into business and government systems.

Scope as stated in `docs/core-banking/bacs-direct-debit-and-mandate-processing.md`:

> Pismo is integrating the UK BACS payment scheme through a provider, such as [Form3](https://www.form3.tech/), for clients. The provider allows BACS scheme connectivity, messaging, and notifications. Pismo's integration includes mandate management and inbound Direct Debit processing. A mandate in BACS is a formal authorization—officially called a Direct Debit Instruction (DDI)—that a customer gives to a business to collect money directly from their bank account.

Scope as stated in `docs/core-banking/bacs-direct-debit-indemity-claims.md`:

> A BACS <a href="https://www.bacs.co.uk/operating/indemnity-claims/" target="_blank">Direct Debit Indemnity Claim</a> (DDIC) is a mechanism under the <a href="https://www.directdebit.co.uk/direct-debit-guarantee/" target="_blank">UK Direct Debit Guarantee</a> that allows a customer's bank to immediately refund them for an erroneous, unauthorized, or non-compliant Direct Debit payment, and then automatically recover that money from the collecting business (the Service User).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/banking-automated-clearing-system.md`: Bankers' Automated Clearing System (BACS); Key aspects; Bank-to-bank transfers; Payment processing; Getting started—create and register Pismo accounts; BACS API endpoints; BACS events; Suspense transaction flow
- `docs/core-banking/bacs-direct-debit-and-mandate-processing.md`: BACS Direct Debit and mandate processing; Enabling Pismo account for mandates; Mandate management; Inbound Direct Debit processing; Detailed processing; Direct Debit returns; Detailed return processing
- `docs/core-banking/bacs-direct-debit-indemity-claims.md`: BACS Direct Debit indemity claims; Key protections and features; End-to-end claim lifecycle; Claim initiation requirements; Client responsibility; Endpoints; Events

## Prerequisites and dependencies

- Prerequisites are described in `docs/core-banking/bacs-direct-debit-indemity-claims.md` section "Claim initiation requirements".
- Depends on 9 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/banking-automated-clearing-system.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/banking-automated-clearing-system · updatedAt: 2026-08-28T20:22:51.000Z

<!-- source:begin path=docs/core-banking/banking-automated-clearing-system.md part=0-end -->

# Bankers' Automated Clearing System (BACS)

The <a href="https://www.moderntreasury.com/learn/what-is-bacs" target="_blank">Bankers' Automated Clearing System</a> (BACS) is a long-standing electronic payment system in the United Kingdom used to transfer money directly between bank accounts. BACS is cheap and reliable, making it ideal for bulk payments like employee payrolls and is widely integrated into business and government systems.

This guide provides an overview of the BACS payment rail integration on the Pismo platform for UK clients. BACS is supported as an additional UK payment rail alongside [Faster Payment Systems](https://developers.pismo.io/pismo-docs/docs/faster-payment-system) (FPS).

# Key aspects

* **Usage**—Used primarily for regular, predictable, and high-volume payments rather than urgent, one-off, or high-value payments.
* **Cost-effective**—It is often cheaper than other methods, such as cheques or <a href="https://www.starlingbank.com/resources/banking/what-is-chaps-guide-to-chaps-payments/" target="_blank">CHAPS</a>.
* **Availability**—Accessible via most UK banks and building societies.

# Bank-to-bank transfers

BACS bank-to-bank transfers:

* **Direct credit deposits**—Funds are sent from an originator’s bank account to a beneficiary’s bank account. Direct credits are typically used for payroll, pensions, refunds, supplier payments, and benefits disbursement.
  * **Outbound direct credit**—A bank or platform initiates a direct credit on a client's behalf, instructing BACS to push funds to beneficiary accounts. Commonly used for bulk payments such as salaries.
  * **Inbound direct credit**—The bank or platform, acting on the beneficiary's behalf, receives a direct credit.  In this flow, the system processes incoming BACS files/messages and credits the beneficiary account after scheme validation and settlement.
* **Direct debits** —An organization (originator) collects funds from a payer’s bank account. Widely used for recurring payments such as utilities, subscriptions, insurance premiums, and loan repayments.
  * **Outbound direct debit**—An originating bank or platform submits a  direct debit collection request on a user's behalf, instructing BACS to collect funds from payer accounts.
  * **Inbound direct debit**—A originating bank or platform submits a direct debit collection request on a user's behalf, instructing BACS to collect funds from payer accounts.

# Payment processing

Payments are processed in batches, not instantly, and typically follow a 3 working-day cycle:

* **Day 1**—Payment is submitted
* **Day 2**—Banks process transaction
* **Day 3**—Funds are deposited in recipient's account

# Getting started—create and register Pismo accounts

Before participating in BACS transactions, clients need to create Pismo accounts and register them as UK accounts:

1. [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications)
2. [Register UK bank account](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan)— Validates bank account details and ensures BACS scheme eligibility. Pismo registers the account with the provider and receives activation confirmation.

**Note**: If there is any error on the provider's end while creating the account, a Provider notification generated event notifies the customer that while Pismo successfully created the bank account it failed at the provider's end.

# BACS API endpoints

The main BACS API endpoint is  [Send BACS direct credit outbound payment](https://developers.pismo.io/pismo-docs/reference/post-create-bacs)

<details>
  <summary style={{ fontSize: "18px", fontWeight: "bold" }}>Send BACS direct credit outbound payment sample payload</summary>

  ```json
  curl --request POST \
       --url https://sandbox.pismolabs.io/bacs/v1/payments/bacs/directcredit/out \
       --header 'accept: application/json' \
       --header 'content-type: application/json' \
       --data '
  {
    "reference": "Weekly money for Mom",
    "creditor_account": {
      "name": "Len Lease",
      "scheme_name": "iban",
      "identification": "AA00AAA000000000000000"
    },
    "currency": {
      "amount": 600,
      "code": "GBP"
    }
  }
  ```
</details>

Two other BACS endpoints—[Cancel BACS inbound transaction](https://developers.pismo.io/pismo-docs/reference/post-cancel-bacs) and [Release BACS inbound transaction](https://developers.pismo.io/pismo-docs/reference/post-release-bacs) are discussed in the [Suspense transaction flow  ](https://developers.pismo.io/pismo-docs/docs/banking-automated-clearing-system#suspense-transaction-flow)section below.

# BACS events

BACS payment processing generates the following events:

* [BACS direct credit outbound payment processed](https://developers.pismo.io/events/docs/bacs-direct-credit-out-status-change-1)—The [Send BACS direct credit outbound payment](https://developers.pismo.io/pismo-docs/reference/post-create-bacs) endpoint generates this event.

<br />

* [BACS direct credit inbound payment processed](https://developers.pismo.io/events/docs/bacs-direct-credit-in-status-change-1)—The [Release BACS inbound transaction ](https://developers.pismo.io/pismo-docs/reference/post-release-bacs)and [Cancel BACS inbound transaction ](https://developers.pismo.io/pismo-docs/reference/post-cancel-bacs)endpoints generate this event.

<br />

* [BACS direct credit outbound return payment processed](https://developers.pismo.io/events/docs/bacs-direct-credit-out-return-status-change-1)—The [Send BACS direct credit outbound payment](https://developers.pismo.io/pismo-docs/reference/post-create-bacs) endpoint generates this event.

<br />

* [BACS direct credit reversal processed](https://developers.pismo.io/events/docs/bacs-direct-credit-reversal-status-change-1)—The BACS scheme ran into an internal issue and requested the reversal of a previously processed transaction.

<br />

* [BACS direct credit inbound return payment processed](https://developers.pismo.io/events/docs/bacs-direct-credit-in-return-status-change-1)—Return payment bas been processed.

# Suspense transaction flow

Pismo clients can use the suspense transaction flow to manage incoming BACS transactions that have been temporarily placed on hold due to suspected fraud pending a decision from the client’s anti-fraud (AF) provider.

**Flow details:**

1. BACS-in received from provider (credit to beneficiary). If anti-fraud is enabled, Pismo triggers anti-fraud workflow with client’s anti- fraud provider.
2. Anti-fraud provider responds:

* **Approved**—Transaction completes normally.
* **Rejected**—Pismo creates a BACS return.
* **On hold** —Transaction becomes a suspense transaction. For suspended transactions, Pismo moves the credited amount into Additional Funds (not available to the beneficiary).

3. Client calls BACS [release](https://developers.pismo.io/pismo-docs/reference/post-release-bacs) or [cancel](https://developers.pismo.io/pismo-docs/reference/post-cancel-bacs) transaction endpoints Client evaluates the anti-fraud context and uses Pismo’s suspense transaction endpoints to either release or cancel the transaction (reverses funds to sender).

<br />
<!-- source:end -->

### Source 2: `docs/core-banking/bacs-direct-debit-and-mandate-processing.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/bacs-direct-debit-and-mandate-processing · updatedAt: 2026-10-08T14:05:37.000Z

<!-- source:begin path=docs/core-banking/bacs-direct-debit-and-mandate-processing.md part=0-end -->

# BACS Direct Debit and mandate processing 

Pismo is integrating the UK BACS payment scheme through a provider, such as [Form3](https://www.form3.tech/), for clients. The provider allows BACS scheme connectivity, messaging, and notifications. Pismo's integration includes mandate management and inbound Direct Debit processing. A mandate in BACS is a formal authorization—officially called a Direct Debit Instruction (DDI)—that a customer gives to a business to collect money directly from their bank account.

**Key details about BACS mandates**

* **Permission** - A business cannot take any money until the customer agrees to and signs this mandate.
* **Flexibility** - It allows the business to collect varying amounts on regular dates, making it ideal for subscriptions or utility bills.
* **Information needed** - The mandate includes the customer's name, bank name, account number, and branch sort code. It also lists the business's unique Service User Number (SUN).
* **Simplified integration** - Simplified integration to BACS through Pismo

# Enabling Pismo account for mandates

During [account creation](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) , or [updating](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v1-accounts) , pass the text - `bacsMandataEnabled=true` in the`metadata` parameter (creation) or the`custom_fields` parameter (updating). Otherwise, the default is `false`

For more information, refer to [Getting started - create and register Pismo accounts](https://developers.pismo.io/pismo-docs/docs/banking-automated-clearing-system#getting-startedcreate-and-register-pismo-accounts)

# Mandate management

Pismo provides the following API endpoints for mandate management. The events they generate, if any, are noted.

**Mandate flow**—Mandate received/created > validation > active > amend or suspension > cancel/expired

<HTMLBlock>
  {`
  <table>
    <thead><tr><td>Endpoint</td><td>Event</td></tr></thead>
  <tr>
     <td>
        <a
           href="https://developers.pismo.io/pismo-docs/reference/post-create-mandate"
           >Create BACS mandate</a
        ><br />POST /v1/payments/bacs/directdebit/paper-mandates
     </td>
     <td>
        <a
           href="https://developers.pismo.io/events/docs/bacs-mandate-status-change-1"
           >BACS mandate status change</a
        >
     </td>
     <td></td>
    </tr>
  <tr>
     <td>
        <a
           href="https://developers.pismo.io/pismo-docs/reference/get-bacs-mandate-list"
           >List BACS direct debit mandates</a
        ><br />GET /v1/payments/bacs/directdebit/mandates
     </td>
     <td>
        None
     </td>
     <td></td>
    </tr>
  <tr>
     <td>
        <a
           href="https://developers.pismo.io/pismo-docs/reference/get-bacs-directdebit-list"
           >List BACS direct debit transactions</a
        ><br />GET /v1/payments/bacs/directdebit
     </td>
     <td>
        None
     </td>
     <td></td>
    </tr>
  <tr>
     <td>
        <a
           href="https://developers.pismo.io/pismo-docs/reference/patch-amend-mandate"
           >Amend BACS mandate</a
        ><br />PATCH /v1/payments/bacs/directdebit/mandates/{id}
     </td>
     <td>
        <a
           href="https://developers.pismo.io/events/docs/bacs-mandate-status-change-1"
           >BACS mandate status change</a
        >
     </td>
     <td></td>
    </tr>
  <tr>
     <td>
        <a
           href="https://developers.pismo.io/pismo-docs/reference/post-cancel-mandate"
           >Cancel BACS mandate</a
        ><br />POST /v1/payments/bacs/directdebit/mandates/{id}/cancel
     </td>
     <td>
        <a
           href="https://developers.pismo.io/events/docs/bacs-mandate-status-change-1"
           >BACS mandate status change</a
        >
     </td>
     <td></td>
    </tr>



  </table>
  `}
</HTMLBlock>

# Inbound Direct Debit processing

In this paying-bank flow, the provider, such as Form3, sends an inbound Direct Debit message to Pismo. Pismo maps the message, identifies the account and mandate, performs validations, posts the debit where valid, records lifecycle information and notifies client.

**End-to-end flow**— Service user > BACS > Provider > Pismo validation and posting > Client consumption

### Detailed processing

1. **Direct Debit submitted**—An external service user, such as a utility company or a insurance provider submits a Direct Debit collection through the BACS scheme
2. **BACS processing**—The BACS scheme validates and processes the collection instruction according to scheme rules
3. **Pismo notified**—Provider receives the scheme message and forwards it to Pismo
4. **Validation and transaction creation**—Pismo validates the mandate status, account status, and product eligibility and creates an internal transaction record for processing
5. **Ledger posting**—The customer's account is debited and ledger balances are updated
6. **Status update and client notification**—The payment status at Pismo is updated and client is notified of final transaction outcome

The customer account is successfully debited and the transaction is available for reconciliation, reporting, customer viewing and audit review.

# Direct Debit returns

Pismo supports return processing when a Direct Debit collection cannot be completed or requires reversal after submission.

Returns can happen under the following conditions:

* Account closed
* Account transferred
* Insufficient funds
* Invalid account information
* Mandate issues

**Inbound flow** —BACS scheme > Provider > Pismo > Client

**Outbound flow**—Pismo > Provide > BACS scheme > Events to Client

### Detailed return processing

1. **Return initiated**—Pismo generates the return and notifies Provider
2. **Original transaction matching**—Pismo identifies the original Direct Debt, transaction reference, settlement references and customer account
3. **Return validation**—Validations include duplicate return checks, reference validation, and account mapping verification.
4. **Return reversal**—Where applicable, the original debit is reversed, balances adjusted, and ledger entries updated.
5. **Status updates**—Transaction status updated.
6. **Client notification**—Pismo generates [an event](https://developers.pismo.io/events/docs/bacs-direct-debit-out-status-change-1)  indicating the return processed, reason code, original payment reference, and updated status.

The Provider can inform customers, update reporting, perform reconciliation and manage operational exceptions.

<br />

<br />

<br />

<br />

<br />
<!-- source:end -->

### Source 3: `docs/core-banking/bacs-direct-debit-indemity-claims.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/bacs-direct-debit-indemity-claims · updatedAt: 2026-10-09T12:34:49.000Z

<!-- source:begin path=docs/core-banking/bacs-direct-debit-indemity-claims.md part=0-end -->

# BACS Direct Debit indemity claims

A BACS <a href="https://www.bacs.co.uk/operating/indemnity-claims/" target="_blank">Direct Debit Indemnity Claim</a> (DDIC) is a mechanism under the <a href="https://www.directdebit.co.uk/direct-debit-guarantee/" target="_blank">UK Direct Debit Guarantee</a> that allows a customer's bank to immediately refund them for an erroneous, unauthorized, or non-compliant Direct Debit payment, and then automatically recover that money from the collecting business (the Service User).

**Note:** This feature is in **beta**, talk to your Pismo representative before using this in production.

# Key protections and features

* **The Direct Debit Guarantee**—Backed by UK banks and building societies, this rule gives customers the right to an immediate, full refund from their bank if an error or unauthorized payment occurs.
* **Common Uses**—Utility bills, mortgages, gym memberships, software subscriptions, insurance premiums, and charitable donations.
* **Comparison**—Unlike faster UK payment rails (like Faster Payments) which settle near-real-time, BACS Direct Debit is a "pull" payment designed for predictable, automated, bulk-processed collections.

# End-to-end claim lifecycle

The process is asynchronous. Clients should treat the initial submission response as confirmation that the instruction has been received or submitted, not as confirmation that funds have been recovered.

1. **Identify the claim**—The client identifies an issue after settlement, associates it with the original Direct Debit and determines the claim amount and BACS reason code.

2. **Submit the instruction to Pismo**—The client sends the claim instruction. Pismo validates the request at platform level, links it to the original payment and [creates a claim record](https://developers.pismo.io/pismo-docs/reference/post-create-claim) .

3. **Initiate lifecycle tracking**—Pismo assigns internal identifiers and initializes an asynchronous state machine so that submission, acknowledgement, outcome and ledger activity remain traceable.

4. **Submit provider claim through Form3**—Pismo transforms the claim into the provider integration format and submits it to <a href="https://www.form3.tech/" target="_blank">Form3</a>. Form3 performs technical validation and forwards the claim to BACS.

5. **Route for external review**—BACS routes the claim to the receiving bank. The receiving bank reviews the claim under the applicable scheme process.

6. **Receive the outcome** —The response returns through Receiving Bank → BACS → Form3 → Pismo. The result is accepted or rejected and may include scheme or rejection references.

7. **Resolve the claim** —Pismo [updates the claim state](https://developers.pismo.io/events/docs/bacs-direct-debit-claim-status-change-1) . If acceptance and fund flow-back are confirmed, the corresponding ledger impact is applied. Pismo then makes the final outcome available to the client.

8. **Complete client operations**—The client reconciles the result, communicates with the customer, and closes or escalates its operational case.

# Claim initiation requirements

A claim request should contain enough information to identify the client, the original settled transaction, the intended recovery and the reason for the claim. Exact field names will be defined in the API reference.

| Data group           | Expected information                                                                                     |
| :------------------- | :------------------------------------------------------------------------------------------------------- |
| Original transaction | Pismo payment or transaction identifier; original BACS reference; settlement reference where available   |
| Claim details        | Claim amount; currency; full or partial claim indicator; BACS reason code                                |
| Client references    | Client claim or case identifier; idempotency reference; customer or account reference where permitted    |
| Operational context  | Request timestamp; initiating system; optional notes or evidence reference                               |
| Traceability         | Correlation identifier and audit metadata required to connect API requests, provider messages and events |

## Client responsibility

The client remains responsible for deciding whether to raise the claim and for selecting the appropriate reason and amount. Pismo and Form3 provide technical processing rather than customer-claim adjudication. Form3 is an example of a provider.

# Endpoints

Pismo provides the following endpoints for BACS DDIC claims:

1. [Raise a Direct Debit indemnity claim](https://developers.pismo.io/pismo-docs/reference/post-create-claim) — Create a BACS Direct Debit Indemnity Claim (DDIC). Generates a [BACS Direct Debit indemnity claim status changed](https://developers.pismo.io/events/docs/bacs-direct-debit-claim-status-change-1) event.
2. [List BACS Direct Debit indemnity claims](https://developers.pismo.io/pismo-docs/reference/get-bacs-claim-list) —List DDIC claims for an account
3. [Reverse BACS Direct Debit indemnity claim](https://developers.pismo.io/pismo-docs/reference/post-raise-claim-reversal) —Reverse a previously raised BACS Direct Debit indemnity claim. Generates a [BACS Direct Debit indemnity claim reversal status changed](https://developers.pismo.io/events/docs/bacs-direct-debit-claim-reversal-status-change-1) event.

# Events

Processing for BACS DDIC claims generates the following events:

1. [BACS Direct Debit indemnity claim status changed](https://developers.pismo.io/events/docs/bacs-direct-debit-claim-status-change-1)  — DDIC claim status has changed. Transitionting to one of the following statuses generates this - `CREATED`, `PROCESSING`, `CONFIRMED`and `FAILED`.
2. [BACS Direct Debit indemnity claim reversal status changed](https://developers.pismo.io/events/docs/bacs-direct-debit-claim-reversal-status-change-1) — DDIC claim reversal status has changed. Transitionting to one of the following statuses generates this - `CREATED`, `PROCESSING`, `CONFIRMED`and `FAILED`.

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /v2/accounts/{accountId}/bank-accounts/uk-scan` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan` | Register UK bank account | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `POST /v1/payments/bacs/directcredit/out` | `post-create-bacs` | Send BACS direct credit outbound payment [beta] | `api-specs/Payment_rails_-_BACS_payments.yaml` | no | KU-API-payment-rails-bacs-payments--bacs-direct-credit |
| `POST /v1/payments/bacs/directcredit/cancel/{id}` | `post-cancel-bacs` | Cancel BACS inbound transaction [beta] | `api-specs/Payment_rails_-_BACS_payments.yaml` | no | KU-API-payment-rails-bacs-payments--bacs-direct-credit |
| `POST /v1/payments/bacs/directcredit/release/{id}` | `post-release-bacs` | Release BACS inbound transaction [beta] | `api-specs/Payment_rails_-_BACS_payments.yaml` | no | KU-API-payment-rails-bacs-payments--bacs-direct-credit |
| `PATCH /accounts/v1/accounts/{accountId}` | `patch-accounts-v1-accounts` | Update account | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /v1/payments/bacs/directdebit/claims` | `post-create-claim` | Raise BACS Direct Debit indemnity claim [beta] | `api-specs/Payment_rails_-_BACS_payments.yaml` | no | KU-API-payment-rails-bacs-payments--bacs-direct-debit |
| `GET /v1/payments/bacs/directdebit/claims` | `get-bacs-claim-list` | List BACS Direct Debit indemnity claims [beta] | `api-specs/Payment_rails_-_BACS_payments.yaml` | no | KU-API-payment-rails-bacs-payments--bacs-direct-debit |
| `POST /v1/payments/bacs/directdebit/claims/reversal/{id}` | `post-raise-claim-reversal` | Reverse BACS Direct Debit indemnity claim [beta] | `api-specs/Payment_rails_-_BACS_payments.yaml` | no | KU-API-payment-rails-bacs-payments--bacs-direct-debit |

### Operation essentials

- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /v2/accounts/{accountId}/bank-accounts/uk-scan`** (`post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `scheme`; response statuses 201, 400, 403, 404, 409, 500; error codes in examples `EIBA0009`, `EIBA0012`, `EIBA0006`, `EIBA0007`, `EIBA0023`, `EIBA0010`, `EIBA0028`, `EIBA0005`, `EIBA0011`, `EIBA0013`, `EIBA0015`; events `intl-bankaccounts-intl-bankaccount-register-1`.
- **`POST /v1/payments/bacs/directcredit/out`** (`post-create-bacs`): security not declared; required parameters `Authorization` (header), `Idempotency-key` (header); required body fields `reference`, `creditor_account`, `currency`; response statuses 201, 400, 403, 404, 409, 429, 500, 502; error codes in examples `EBACS0004`, `EBACS0016`, `EBACS0019`, `EBACS0025`, `EBACS0029`, `EBACS0037`, `EBACS0038`, `EBACS0039`, `EBACS0046`, `EBACS0047`, `EBACS0073`, `EBACS0002`, `EBACS0021`, `EBACS0033`, `EBACS0034`, `EBACS0035`, `EBACS0040`, `EBACS0041`, `EBACS0010`, `EBACS0018`, `EBACS0028`, `EBACS0031`, `EBACS0022`, `EBACS0036`, `EBACS0015`, `EBACS0006`, `EBACS0009`, `EBACS0011`, `EBACS0012`, `EBACS0017`, `EBACS0020`, `EBACS0023`, `EBACS0024`, `EBACS0026`, `EBACS0027`, `EBACS0030`, `EBACS0032`, `EBACS0014`; events `bacs-direct-credit-out-return-status-change-1`, `bacs-direct-credit-out-status-change-1`.
- **`POST /v1/payments/bacs/directcredit/cancel/{id}`** (`post-cancel-bacs`): security not declared; required parameters `Authorization` (header), `id` (path); required body fields none declared; response statuses 200, 400, 403, 404, 409, 429, 500, 502; error codes in examples `EBACS0004`, `EBACS0016`, `EBACS0019`, `EBACS0025`, `EBACS0029`, `EBACS0037`, `EBACS0038`, `EBACS0039`, `EBACS0046`, `EBACS0047`, `EBACS0002`, `EBACS0021`, `EBACS0033`, `EBACS0034`, `EBACS0035`, `EBACS0040`, `EBACS0041`, `EBACS0010`, `EBACS0018`, `EBACS0028`, `EBACS0031`, `EBACS0022`, `EBACS0036`, `EBACS0096`, `EBACS0015`, `EBACS0006`, `EBACS0009`, `EBACS0011`, `EBACS0012`, `EBACS0017`, `EBACS0020`, `EBACS0023`, `EBACS0024`, `EBACS0026`, `EBACS0027`, `EBACS0030`, `EBACS0032`, `EBACS0014`; events `bacs-direct-credit-in-status-change-1`.
- **`POST /v1/payments/bacs/directcredit/release/{id}`** (`post-release-bacs`): security not declared; required parameters `Authorization` (header), `id` (path); required body fields none declared; response statuses 200, 400, 403, 404, 409, 429, 500, 502; error codes in examples `EBACS0004`, `EBACS0016`, `EBACS0019`, `EBACS0025`, `EBACS0029`, `EBACS0037`, `EBACS0038`, `EBACS0039`, `EBACS0046`, `EBACS0047`, `EBACS0002`, `EBACS0021`, `EBACS0033`, `EBACS0034`, `EBACS0035`, `EBACS0040`, `EBACS0041`, `EBACS0010`, `EBACS0018`, `EBACS0028`, `EBACS0031`, `EBACS0022`, `EBACS0036`, `EBACS0097`, `EBACS0015`, `EBACS0006`, `EBACS0009`, `EBACS0011`, `EBACS0012`, `EBACS0017`, `EBACS0020`, `EBACS0023`, `EBACS0024`, `EBACS0026`, `EBACS0027`, `EBACS0030`, `EBACS0032`, `EBACS0014`; events `bacs-direct-credit-in-status-change-1`.
- **`PATCH /accounts/v1/accounts/{accountId}`** (`patch-accounts-v1-accounts`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 401, 404, 500; error codes in examples none; events `account-account-change-2`.
- **`POST /v1/payments/bacs/directdebit/claims`** (`post-create-claim`): security not declared; required parameters `Authorization` (header), `Idempotency-key` (header); required body fields `clearing_id`, `reference`, `reason_code`, `original_instruction`, `disputed_transactions`; response statuses 201, 400, 403, 409, 500; error codes in examples `EBACS0004`, `EBACS0002`, `EBACS0085`, `EBACS0086`, `EBACS0021`, `EBACS0058`, `EBACS0003`; events `bacs-direct-debit-claim-status-change-1`.
- **`GET /v1/payments/bacs/directdebit/claims`** (`get-bacs-claim-list`): security not declared; required parameters `Authorization` (header); required body fields none declared; response statuses 200, 400, 403, 500; error codes in examples `EBACS0004`, `EBACS0002`, `EBACS0085`, `EBACS0003`; events none listed.
- **`POST /v1/payments/bacs/directdebit/claims/reversal/{id}`** (`post-raise-claim-reversal`): security not declared; required parameters `Authorization` (header), `Idempotency-key` (header), `id` (path); required body fields `original_instruction_id`; response statuses 201, 400, 403, 404, 409, 500; error codes in examples `EBACS0004`, `EBACS0002`, `EBACS0085`, `EBACS0086`, `EBACS0107`, `EBACS0108`, `EBACS0003`; events `bacs-direct-debit-claim-reversal-status-change-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-accounts-v1-accounts` | `account-account-change-2` |
| `post-cancel-bacs` | `bacs-direct-credit-in-status-change-1` |
| `post-release-bacs` | `bacs-direct-credit-in-status-change-1` |
| `post-create-bacs` | `bacs-direct-credit-out-return-status-change-1` |
| `post-create-bacs` | `bacs-direct-credit-out-status-change-1` |
| `post-raise-claim-reversal` | `bacs-direct-debit-claim-reversal-status-change-1` |
| `post-create-claim` | `bacs-direct-debit-claim-status-change-1` |
| `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan` | `intl-bankaccounts-intl-bankaccount-register-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `bacs-direct-credit-in-return-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-credit-in-return-status-change-1 | 1 | KU-EVT-catalogue-bacs |
| `bacs-direct-credit-in-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-credit-in-status-change-1 | 2 | KU-EVT-catalogue-bacs |
| `bacs-direct-credit-out-return-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-credit-out-return-status-change-1 | 1 | KU-EVT-catalogue-bacs |
| `bacs-direct-credit-out-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-credit-out-status-change-1 | 1 | KU-EVT-catalogue-bacs |
| `bacs-direct-debit-claim-reversal-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-debit-claim-reversal-status-change-1 | 1 | KU-EVT-catalogue-bacs |
| `bacs-direct-debit-claim-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-debit-claim-status-change-1 | 1 | KU-EVT-catalogue-bacs |
| `bacs-mandate-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-mandate-status-change-1 | 3 | KU-EVT-catalogue-bacs |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/banking-automated-clearing-system.md`: updatedAt 2026-08-28T20:22:51.000Z.
- `docs/core-banking/bacs-direct-debit-and-mandate-processing.md`: updatedAt 2026-10-08T14:05:37.000Z.
- `docs/core-banking/bacs-direct-debit-indemity-claims.md`: updatedAt 2026-10-09T12:34:49.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 9 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/banking-automated-clearing-system.md` | whole document | https://developers.pismo.io/pismo-docs/docs/banking-automated-clearing-system | `2c49b96df07d758a…` | 2026-08-28T20:22:51.000Z |
| `docs/core-banking/bacs-direct-debit-and-mandate-processing.md` | whole document | https://developers.pismo.io/pismo-docs/docs/bacs-direct-debit-and-mandate-processing | `faceeca614093ebc…` | 2026-10-08T14:05:37.000Z |
| `docs/core-banking/bacs-direct-debit-indemity-claims.md` | whole document | https://developers.pismo.io/pismo-docs/docs/bacs-direct-debit-indemity-claims | `69cd3f6726138963…` | 2026-10-09T12:34:49.000Z |

## Related knowledge units

- `KU-API-banking-bank-accounts--bank-accounts-part-01` — API reference: Banking - Bank accounts — Bank accounts (part 1 of 2)
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-payment-rails-bacs-payments--bacs-direct-credit` — API reference: Payment rails - BACS payments — BACS direct credit
- `KU-API-payment-rails-bacs-payments--bacs-direct-debit` — API reference: Payment rails - BACS payments — BACS direct debit
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-bacs` — Event catalogue: bacs
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-faster-payment-system` — Faster Payments (UK)
