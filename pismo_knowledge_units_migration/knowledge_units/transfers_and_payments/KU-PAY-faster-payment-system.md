---
ku_id: KU-PAY-faster-payment-system
title: Faster Payments (UK)
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/faster-payment-system.md
  sha256: 4905cb805c0f8fb3eafdacdd243272cc47012e3d15fc9dc69562088972bc8c22
  url: https://developers.pismo.io/pismo-docs/docs/faster-payment-system
  role: primary_guide
  updated_at: '2026-05-13T19:08:34.000Z'
operations:
- delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name
- patch-accounts-v2-accounts-accountId-status
- post-acquisitions-v3-s2s-applications
- post-cancel-fps
- post-cop-verification
- post-create-fps
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan
- post-release-fps
related_kus:
- KU-API-banking-bank-accounts--bank-accounts-part-01
- KU-API-banking-bank-accounts--bank-accounts-part-02
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-CORE-accounts-overview
- KU-EVT-catalogue-account
- KU-EVT-catalogue-fps
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Faster Payments (UK)

**KU ID:** `KU-PAY-faster-payment-system` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/faster-payment-system.md`:

> The United Kingdom’s <a href="https://www.wearepay.uk/what-we-do/payment-systems/faster-payment-system/" target="_blank">Faster Payment System</a> (FPS) has revolutionized the way real-time payments are processed, enabling individuals and businesses to transfer funds within seconds, 24/7. Pismo's flexible endpoints empower clients to seamlessly connect with FPS providers who participate in the processing and settlement of domestic UK transactions.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/faster-payment-system.md`: Faster Payments (UK); FPS in the UK; Pismo and FPS Integration; Provider connectivity; Account creation; Account status; Account deletion; FPS outbound transactions; FPS inbound transactions; FPS returns; FPS reversals; Return reversals; Suspense transaction flow; High level flow; Step 1 - FPS-in received from provider (credit to beneficiary).; Step 2 - Anti-fraud provider responds; Step 3 - Client calls FPS release or cancel transaction endpoints; Confirmation of Payee; High-level architecture; Key components; End-to-end flow; Opting out; Opt-out indicator; FPS events; Conclusion

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 8 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/faster-payment-system.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/faster-payment-system · updatedAt: 2026-05-13T19:08:34.000Z

<!-- source:begin path=docs/core-banking/faster-payment-system.md part=0-end -->

# Faster Payments (UK)

The United Kingdom’s <a href="https://www.wearepay.uk/what-we-do/payment-systems/faster-payment-system/" target="_blank">Faster Payment System</a> (FPS) has revolutionized the way real-time payments are processed, enabling individuals and businesses to transfer funds within seconds, 24/7. Pismo's flexible endpoints empower clients to seamlessly connect with FPS providers who participate in the processing and settlement of domestic UK transactions.

This guide  documents Pismo services for FPS integration in the UK, their architectural approach, its major transaction flows, and the end-to-end process for connecting to FPS using Pismo’s next-generation platform.

# FPS in the UK

FPS is a UK banking initiative, introduced in 2008, designed to reduce payment times between different banks' customer accounts from three working days to a few seconds. <a href="https://www.wearepay.uk/" target="_blank">Pay.UK</a> owns and operates FPS and makes it accessible to banks and authorized payment providers known as **Direct** and **Indirect** participants.   Direct participants connect straight to the central infrastructure, handling their own settlement with the Bank of England, while Indirect participants lack direct links, instead using a sponsoring Direct participant (a bank or large PSP) to send/receive payments and settle funds, making it a cost-effective way to access the network without full infrastructure investment.

The FPS service supports various payment types, including single immediate payments, forward-dated payments, and standing orders.

**Key features:**

* Near-instant settlement and clearing of payments
* 24/7/365 availability
* Robust security and anti-fraud measures
* Supports both retail and business payments

# Pismo and FPS Integration

Pismo provides powerful, reliable endpoints that simplify FPS connectivity.

Pismo's integration supports both direct and indirect access models, enabling clients to connect with a variety of FPS providers depending on their regulatory status and business requirements.

**Major transaction flows:**

* Provider connectivity
* Account creation
* FPS outbound transactions
* FPS inbound transactions
* FPS returns
* FPS reversals
* FPS return reversals
* FPS events

The following sections walk through each of these flows, highlighting the technical and operational considerations involved.

## Provider connectivity

The initial key step is to establish a secure and resilient connection with FPS providers.

**Pismo's role**::

* Enables clients to authenticate with their chosen provider using industry-standard protocols (such as <a href="https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/" target="_blank">mTLS</a> (mutual TLS).
* Ensures that all due diligence, compliance checks, and contractual arrangements are in place before establishing connectivity.
* Supports providers' multiple API versions.
* Manages provider configuration and credentials.
* Provides end-to-end data encryption.

## Account creation

Before participating in FPS transactions, you need to create Pismo accounts and register them with your provider.

1. [Create account](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications)  with Pismo.  This generates an [Account created](https://developers.pismo.io/events/docs/onboarding-succeeded-1)  event
2. Call Pismo’s [Register UK bank account](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan)  using UK account number and sort code to update relevant account details. This validates bank account details and ensures FPS scheme eligibility.

Pismo registers the account with the provider and receives activation confirmation. A [Bank account registered](https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1)  event is generated after Pismo receives the provider's webhook notification.

**Note:** If there is any error on the provider's end while creating the account, a [Provider notification generated](https://developers.pismo.io/events/docs/banking-prospect-provider-notification-1) event notifies the customer that  while Pismo successfully created the bank account but it failed at the provider's end.

### Account status

To update the status for an FPS account, call [Update status](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v2-accounts-accountid-status). For more information on account statuses, refer to [Account status](https://developers.pismo.io/pismo-docs/docs/accounts-overview#account-status) .

### Account deletion

To delete an FPS account, call [Delete bank account](https://developers.pismo.io/pismo-docs/reference/delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name).

## FPS outbound transactions

Outbound transactions involve sending funds from a client’s account to a FPS network recipient.

**Pismo's role**:

* Enables clients to initiatie new FPS payments with all mandatory fields (amount, currency, beneficiary details, reference, etc.) via Pismo's [FPS out-transfer](https://developers.pismo.io/pismo-docs/reference/post-create-fps)  endpoint
* Submits payment instructions to the chosen provider, with synchronous or asynchronous confirmation.
* Retrieves transaction status updates, including payment tracking.
* Receives provider webhook notifications and notifies clients of transaction status via the [FPS out payment transaction event generated](https://developers.pismo.io/events/docs/fps-fps-out-status-change-1) event

**Key points:**

* **Payment limits**—Limit maintenance must be configured at the client’s end based on scheme-defined limits.
* **Idempotency**—Preventing duplicate submissions through robust idempotency tokens

<details>
  <summary style={{ fontWeight: "bold", fontSize: "20px" }}>Sample FPS out-transfer payload</summary>

  ```json
  {  
    "creditor_account": {  
      "identification": "AA00AAA000000000000000",  
      "name": "Pam Demic",  
      "scheme_name": "iban"  
    },  
    "end_to_end_id": "1374f841568e4ff4b3a63b023c1870ec",  
    "instructed_amount": {  
      "amount": 10.5,  
      "currency": "GBP"  
    },  
    "remittance_information": {  
      "reference": "Reference information"  
    },  
    "originated_overseas": {  
      "ultimate_debtor": {  
        "address": "501 Congress Avenue, Suite 150 Austin, TX 78701",  
        "name": "Luke Wharm"  
      },  
      "ultimate_debtor_account": {  
        "account_number": "123456",  
        "identification": "BOFAUS3N",  
        "scheme_name": "BIC"  
      }  
    }  
  ```
</details>

## FPS inbound transactions

Inbound transactions occur when a client receives funds from another FPS participant.

**Pismo’s role:**

* **Account mapping**—Ensures correct allocation of inbound funds to the appropriate client account
* **Real-time notifications**—Instant notifications and notify [events](https://developers.pismo.io/events/docs/fps-fps-in-status-change-1) keeping clients up-to-date.
* **Suspense transactions**—For handling Suspense transactions, Pismo provide clients with an endpoint, allowing them to make decisions on held transactions based on their anti-fraud provider’s recommendations or analysis.

**Key points:**

* Any Incoming transaction from the provider to Pismo is always settled at the payment scheme.
* If approved, Pismo clears the transaction  and the beneficiary can access funds. Otherwise, Pismo creates a return transaction that references the original transaction for traceability.

## FPS returns

A payment return is used when a credited party returns a previus payment's funds back to the debited party.

**Pismo's role**:

* Supports  outbound and inbound transaction return requests
* Tracks the return lifecycle, from initiation to resolution
* Handles provider-specific return codes and required documentation seamlessly
* Generates [FPS outbound payment return processed](https://developers.pismo.io/events/docs/fps-fps-out-return-status-change-1) event
* Generates [FPS inbound payment return processed](https://developers.pismo.io/events/docs/fps-fps-in-return-status-change-1)  event.\
  This happens when  Pismo receives a FPS -in transfer and fails to credit the amount due to any reason. In this case,  Pismo submits the return to the Provider and generates this event. 
* Ensures return requests are raised within FPS-mandated timeframes
* Provides clear, auditable trails for all return actions

## FPS reversals

A payment reversal occurs when a payment has been cancelled.

**Pismo’s role**:

* Supports client or provider-initiated reversal requests.
* Automates the workflow for capturing reversal justifications and required evidence.
* Integrates with external case management systems for dispute resolution.
* Generates the [FPS inbound payment reversal processed](https://developers.pismo.io/events/docs/fps-fps-in-reversal-status-change-1) event.

### Return reversals

This use case is not in scope for Direct participants. When an incoming FPS payment reaches Pismo, and due to an account-level issue (such as blocked, closed, or invalid beneficiary account), Pismo is unable to credit the funds to the intended recipient. In this case, Pismo initiates a return referencing the original transaction.\
However, if this return fails—for example, due to a technical issue at the provider’s end —it may trigger a return reversal.

**To ensure resolution:**

* Pismo automatically retries the return transaction multiple times until it is successfully accepted by Form3.
* These retries are tracked internally and are part of Pismo’s FPS operational resilience strategy. This mechanism ensures that failed returns are not left unresolved and that funds are either returned or properly reversed in accordance with FPS protocols.

# Suspense transaction flow

Pismo clients can use the suspense transaction flow to manage incoming FPS transactions that have been temporarily placed on hold due to suspected fraud pending a decision from the client’s anti-fraud (AF) provider.

This flow supports scenarios where:

* An FPS incoming (cash-in) transaction is received.
* Client’s AF provider returns "hold" instead of approve or reject.
* Pismo places the transaction amount into Additional Funds (unavailable balance) so the beneficiary cannot use the funds until a final decision is made.
* The client later calls Pismo’s [release](https://developers.pismo.io/pismo-docs/reference/post-release-fps)  or [cancel](https://developers.pismo.io/pismo-docs/reference/post-cancel-fps)  endpoints to finalize the transaction.

This mechanism ensures compliance with fraud/risk requirements while maintaining realtime processing expectations for FPS instant payments.

## High level flow

### Step 1 - FPS-in received from provider (credit to beneficiary).

If anti-fraud is enabled, Pismo triggers anti-fraud workflow with client’s anti-fraud provider.

### Step 2 - Anti-fraud provider responds

* **Approved**—Transaction completes normally.
* **Rejected**—Pismo creates an FPS return.
* **On Hold** —Transaction becomes a **suspense transaction**.

For suspended transactions, Pismo moves the credited amount into Additional Funds (not available to the beneficiary).

### Step 3 - Client calls FPS release or cancel transaction endpoints

Client evaluates the anti-fraud context and uses Pismo’s suspense fransaction endpoints to either [release](https://developers.pismo.io/pismo-docs/reference/post-release-fps)  or [cancel](https://developers.pismo.io/pismo-docs/reference/post-cancel-fps)  the transaction (reverses funds to sender).

# Confirmation of Payee

The <a href="https://www.wearepay.uk/what-we-do/overlay-services/confirmation-of-payee/" target="_blank">Confirmation of Payee (CoP)</a> is a banking name-checking service.  The  <a href="https://www.wearepay.uk/" target="_blank">Pay.UK</a> mandates CoP for Faster Payments in the UK.

CoP allows a payer to verify whether the payee name matches the account details before a payment is executed. This helps reduce misdirected payments and Authorised Push Payment (APP) fraud. APP fraud occurs when criminals deceive victims into willingly transferring money from their bank account to a fraudulent account, often via instant bank transfers. Because victims authorize the payment, these scams are hard to reverse. Common tactics include social engineering, such as impersonating banks, police, or businesses.

## High-level architecture

The Pismo CoP service is designed to integrate seamlessly with client channels and internal systems while ensuring compliance with FPS and Pay.UK requirements.

The service operates as an orchestration layer between client-facing channels, and external Confirmation of Payee providers within the FPS ecosystem.

### Key components

* Client or third-party channels (mobile banking, internet banking)
* Pismo instant payments platform
* External CoP provider (FPS ecosystem)

## End-to-end flow

1. Customer enters payee details including name, sort code, account number, and account type.
2. Client calls Pismo's  [CoP endpoint](https://developers.pismo.io/pismo-docs/reference/post-cop-verification).
3. Pismo validates the request and routes it to the external CoP Provider. A [CoP name verification requested](https://developers.pismo.io/events/docs/fps-cop-name-verification-submissions-1)  event is generated and sent to the client.
4. The external CoP provider validates the name and returns result to Pismo. Names are either `confirmed` or `rejected`.
5. Pismo forwards the response back to the client via a [CoP name verification result received](https://developers.pismo.io/events/docs/fps-cop-name-verification-admissions-1)  event.
6. Client displays result to the customer.

## Opting out

Pay.UK allows customers, under defined conditions, to opt out of Confirmation of Payee checks. To support this, Pismo has introduced an opt-out indicator as part of the account registration process.

### Opt-out indicator

Clients can opt out when [registering a UK bank account](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan). You can do this with the `name_matching_status` field within the `metadata` object:

```json
{
  "metadata": {
    "name_matching_status": "opted_out"
  }
}
```

The default for `name_matching_status` is `supported`.

# FPS events

Pismo creates the FPS [events](https://developers.pismo.io/events/docs/fps-fps-in-reversal-status-change-1) and events for account creation and subsequent transaction confirmation for reconciliation purposes and sends them to the client.

# Conclusion

Integrating with FPS offers significant business advantages, but it demands technical expertise, regulatory awareness, and operational excellence. By leveraging Pismo’s robust endpoints and support, clients can confidently connect with FPS providers and offer secure, high-performance payment experiences to their customers. For more information, or to begin your FPS integration journey, please contact your Pismo representative or consult our developer documentation.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /v2/accounts/{accountId}/bank-accounts/uk-scan` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan` | Register UK bank account | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `PATCH /accounts/v2/accounts/{accountId}/status` | `patch-accounts-v2-accounts-accountId-status` | Update status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName}` | `delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name` | Delete bank account | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-02 |
| `POST /v1/payments/fps/out` | `post-create-fps` | Send Faster Payment [beta] | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/payments/fps/release/{endToEndId}` | `post-release-fps` | Release FPS inbound transaction [beta] | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/payments/fps/cancel/{endToEndId}` | `post-cancel-fps` | Cancel FPS inbound transaction [beta] | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/payments/fps/cop` | `post-cop-verification` | Confirmation of payee [beta] | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |

### Operation essentials

- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /v2/accounts/{accountId}/bank-accounts/uk-scan`** (`post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `scheme`; response statuses 201, 400, 403, 404, 409, 500; error codes in examples `EIBA0009`, `EIBA0012`, `EIBA0006`, `EIBA0007`, `EIBA0023`, `EIBA0010`, `EIBA0028`, `EIBA0005`, `EIBA0011`, `EIBA0013`, `EIBA0015`; events `intl-bankaccounts-intl-bankaccount-register-1`.
- **`PATCH /accounts/v2/accounts/{accountId}/status`** (`patch-accounts-v2-accounts-accountId-status`): security `BearerAuth`; required parameters `accountId` (path); required body fields `status`; response statuses 204, 400, 404, 500; error codes in examples none; events `account-status-change-2`.
- **`DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName}`** (`delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path), `schemeName` (path); required body fields none declared; response statuses 204, 400, 403, 404, 500; error codes in examples `EIBA0012`, `EIBA0016`, `EIBA0006`, `EIBA0007`, `EIBA0023`, `EIBA0010`, `EIBA0005`, `EIBA0011`, `EIBA0013`, `EIBA0015`; events `intl-bankaccounts-intl-bankaccount-update-1`.
- **`POST /v1/payments/fps/out`** (`post-create-fps`): security not declared; required parameters `Authorization` (header), `Idempotency-key` (header); required body fields `end_to_end_id`, `creditor_account`, `scheme_payment_type`, `currency`; response statuses 201, 400, 403, 404, 409, 429, 500, 502; error codes in examples `EFPS0004`, `EFPS0016`, `EFPS0019`, `EFPS0025`, `EFPS0029`, `EFPS0037`, `EFPS0038`, `EFPS0039`, `EFPS0046`, `EFPS0047`, `EFPS0073`, `EFPS0002`, `EFPS0021`, `EFPS0033`, `EFPS0034`, `EFPS0035`, `EFPS0040`, `EFPS0041`, `EFPS0010`, `EFPS0018`, `EFPS0028`, `EFPS0031`, `EFPS0022`, `EFPS0036`, `EFPS0015`, `EFPS0006`, `EFPS0009`, `EFPS0011`, `EFPS0012`, `EFPS0017`, `EFPS0020`, `EFPS0023`, `EFPS0024`, `EFPS0026`, `EFPS0027`, `EFPS0030`, `EFPS0032`, `EFPS0014`; events `fps-fps-out-return-status-change-1`, `fps-fps-out-status-change-1`.
- **`POST /v1/payments/fps/release/{endToEndId}`** (`post-release-fps`): security not declared; required parameters `Authorization` (header), `x-tenant` (header), `endToEndId` (path); required body fields none declared; response statuses 200, 400, 403, 404, 409, 429, 500, 502; error codes in examples `EFPS0004`, `EFPS0016`, `EFPS0019`, `EFPS0025`, `EFPS0029`, `EFPS0037`, `EFPS0038`, `EFPS0039`, `EFPS0046`, `EFPS0047`, `EFPS0002`, `EFPS0021`, `EFPS0033`, `EFPS0034`, `EFPS0035`, `EFPS0040`, `EFPS0041`, `EFPS0010`, `EFPS0018`, `EFPS0028`, `EFPS0031`, `EFPS0022`, `EFPS0036`, `EFPS0094`, `EFPS0015`, `EFPS0006`, `EFPS0009`, `EFPS0011`, `EFPS0012`, `EFPS0017`, `EFPS0020`, `EFPS0023`, `EFPS0024`, `EFPS0026`, `EFPS0027`, `EFPS0030`, `EFPS0032`, `EFPS0014`; events `fps-fps-in-status-change-1`.
- **`POST /v1/payments/fps/cancel/{endToEndId}`** (`post-cancel-fps`): security not declared; required parameters `Authorization` (header), `x-tenant` (header), `endToEndId` (path); required body fields none declared; response statuses 200, 400, 403, 404, 409, 429, 500, 502; error codes in examples `EFPS0004`, `EFPS0016`, `EFPS0019`, `EFPS0025`, `EFPS0029`, `EFPS0037`, `EFPS0038`, `EFPS0039`, `EFPS0046`, `EFPS0047`, `EFPS0002`, `EFPS0021`, `EFPS0033`, `EFPS0034`, `EFPS0035`, `EFPS0040`, `EFPS0041`, `EFPS0010`, `EFPS0018`, `EFPS0028`, `EFPS0031`, `EFPS0022`, `EFPS0036`, `EFPS0095`, `EFPS0015`, `EFPS0006`, `EFPS0009`, `EFPS0011`, `EFPS0012`, `EFPS0017`, `EFPS0020`, `EFPS0023`, `EFPS0024`, `EFPS0026`, `EFPS0027`, `EFPS0030`, `EFPS0032`, `EFPS0014`; events `fps-fps-in-status-change-1`.
- **`POST /v1/payments/fps/cop`** (`post-cop-verification`): security not declared; required parameters `Authorization` (header), `x-tenant` (header), `Idempotency-key` (header); required body fields `id`, `account_classification`, `account_number`, `account_number_code`, `bank_id`, `bank_id_code`, `name`; response statuses 200, 400, 403, 409, 429, 500, 502, 504; error codes in examples `EFPS0004`, `EFPS0016`, `EFPS0002`, `EFPS0086`, `EFPS0058`, `EFPS0015`, `EFPS0006`, `EFPS0023`, `EFPS0014`, `EFPS0012`; events `fps-cop-name-verification-admissions-1`, `fps-cop-name-verification-submissions-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-accounts-v2-accounts-accountId-status` | `account-status-change-2` |
| `post-cop-verification` | `fps-cop-name-verification-admissions-1` |
| `post-cop-verification` | `fps-cop-name-verification-submissions-1` |
| `post-cancel-fps` | `fps-fps-in-status-change-1` |
| `post-release-fps` | `fps-fps-in-status-change-1` |
| `post-create-fps` | `fps-fps-out-return-status-change-1` |
| `post-create-fps` | `fps-fps-out-status-change-1` |
| `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan` | `intl-bankaccounts-intl-bankaccount-register-1` |
| `delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name` | `intl-bankaccounts-intl-bankaccount-update-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `fps-cop-name-verification-admissions-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-cop-name-verification-admissions-1 | 1 | KU-EVT-catalogue-fps |
| `fps-cop-name-verification-submissions-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-cop-name-verification-submissions-1 | 1 | KU-EVT-catalogue-fps |
| `fps-fps-in-return-status-change-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-fps-in-return-status-change-1 | 1 | KU-EVT-catalogue-fps |
| `fps-fps-in-status-change-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-fps-in-status-change-1 | 2 | KU-EVT-catalogue-fps |
| `fps-fps-out-return-status-change-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-fps-out-return-status-change-1 | 1 | KU-EVT-catalogue-fps |
| `fps-fps-out-status-change-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-fps-out-status-change-1 | 1 | KU-EVT-catalogue-fps |
| `intl-bankaccounts-intl-bankaccount-register-1` | intl | 1 | https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1 | 7 | KU-EVT-catalogue-other-domains |
| `onboarding-succeeded-1` | onboarding | 1 | https://developers.pismo.io/events/docs/onboarding-succeeded-1 | 4 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/faster-payment-system.md`: updatedAt 2026-05-13T19:08:34.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 10 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/faster-payment-system.md` | whole document | https://developers.pismo.io/pismo-docs/docs/faster-payment-system | `4905cb805c0f8fb3…` | 2026-05-13T19:08:34.000Z |

## Related knowledge units

- `KU-API-banking-bank-accounts--bank-accounts-part-01` — API reference: Banking - Bank accounts — Bank accounts (part 1 of 2)
- `KU-API-banking-bank-accounts--bank-accounts-part-02` — API reference: Banking - Bank accounts — Bank accounts (part 2 of 2)
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-CORE-accounts-overview` — Accounts
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-fps` — Event catalogue: fps
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
