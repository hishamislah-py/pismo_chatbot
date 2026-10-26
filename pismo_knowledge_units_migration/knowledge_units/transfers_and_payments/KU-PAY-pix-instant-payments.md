---
ku_id: KU-PAY-pix-instant-payments
title: Pix instant payments (Brazil)
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/pix-instant-payments.md
  sha256: 18079ccebc8330809de4dd864f6e5378fec548e9e72107f000c195ddbc4ec030
  url: https://developers.pismo.io/pismo-docs/docs/pix-instant-payments
  role: primary_guide
  updated_at: '2026-07-20T19:05:54.000Z'
operations:
- post-cancel-dict-refund
- post-close-dict-refund
- post-complete-dict-claim
- post-create-cob
- post-pix-out-transfer
- post-pix-reversal
- post-register-dict-refund
- post-schedule-pix-payment
- post-v2-pix-infraction-cancel
- post-v2-pix-infraction-close
- post-v2-pix-infraction-create
- post-v2-pix-keys-create
related_kus:
- KU-API-instant-payments-pix-management--claims
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-instant-payments-pix-management--keys-part-01
- KU-API-instant-payments-pix-management--refunds
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--scheduled-transfers-v2
- KU-API-instant-payments-qr-code--qr-code
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-pix
- KU-EVT-client-webhooks-part-01
- KU-EVT-client-webhooks-part-02
- KU-EVT-client-webhooks-part-03
- KU-EVT-client-webhooks-part-04
- KU-EVT-client-webhooks-part-05
- KU-EVT-client-webhooks-part-06
- KU-EVT-client-webhooks-part-07
- KU-EVT-client-webhooks-part-08
- KU-EVT-client-webhooks-part-09
- KU-EVT-client-webhooks-part-10
- KU-EVT-client-webhooks-part-11
- KU-EVT-client-webhooks-part-12
- KU-EVT-client-webhooks-part-13
- KU-EVT-client-webhooks-part-14
- KU-EVT-pix-payments-data-events
- KU-PAY-pix-and-qr-codes
- KU-PAY-pix-funds-recovery
grouping_rationale: single source page
---

# Pix instant payments (Brazil)

**KU ID:** `KU-PAY-pix-instant-payments` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/pix-instant-payments.md`:

> **[Pix](https://www.bcb.gov.br/en/financialstability/pix_en)** (short for "Pagamentos Instantaneos" in Portuguese, or "Instant Payments" in English) is a popular Brazilian instant payment system introduced in November 2020. Pix allows individuals and businesses to make electronic money transfers 24/7, with funds immediately available to the recipient. Pix transactions are executed in real time from a linked bank account. To send an instant payment or transfer, a Pix user needs only the recipient's Pix key or a QR (Quick Response) Code.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/pix-instant-payments.md`: Pix instant payments (Brazil); Pix participants; Pix keys; Pix key transfer (key claim); Pix transactions; Generating dynamic QR Codes and BR Codes for Pix transactions; Scheduled transactions; Infraction reports; Infraction report process; Refund requests; Refund request process; Pix funds recovery; Pix events

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 12 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/pix-instant-payments.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pix-instant-payments · updatedAt: 2026-07-20T19:05:54.000Z

<!-- source:begin path=docs/core-banking/pix-instant-payments.md part=0-end -->

# Pix instant payments (Brazil)

**[Pix](https://www.bcb.gov.br/en/financialstability/pix_en)** (short for "Pagamentos Instantaneos" in Portuguese, or "Instant Payments" in English) is a popular Brazilian instant payment system introduced in November 2020. Pix allows individuals and businesses to make electronic money transfers 24/7, with funds immediately available to the recipient. Pix transactions are executed in real time from a linked bank account. To send an instant payment or transfer, a Pix user needs only the recipient's Pix key or a QR (Quick Response) Code.

<details>
  <summary><b>Example Pix payment scenario</b></summary>

  Maria wants to pay her friend Pedro for a dinner they had together. They both have bank accounts in Brazil, and both have registered for Pix with their respective banks.

  1. **Payment initiation**:
     * Maria opens her banking app on her smartphone.
     * She selects the option to make a Pix payment.
     * She chooses Pedro as the recipient by entering his Pix key (let's say it's his mobile phone number) or by scanning his QR Code, which contains his Pix information.  Note that this could also be Pedro's bank account information.
     * She enters the payment amount, an optional description (for example: "Dinner payment"), and confirms the payment.

  2. **Transaction notification**:
     * Pedro's banking app receives a notification of the incoming Pix payment from Maria.
     * Pedro's banking app reviews the details, including the payment amounts, and accepts the Pix notification.

  3. **Transaction confirmation**:
     * Maria's banking app sends the payment, and the funds are immediately transferred from Maria's bank account to Pedro's bank account.
     * Pedro receives a notification of the incoming Pix payment from Maria in his banking app.

  4. **Immediate availability**:
     * Pedro can see the funds in his bank account immediately, even if it's outside of regular banking hours. He can use the money right away for any other transactions or withdrawals.
</details>

## Pix participants

Pismo is a technological solution that integrates indirect participants with direct participants, and direct participants with PSTIs (Information Technology Service Providers that the Central Bank of Brazil has licensed.

If your company is interested in becoming a Pix participant, consult the process detailed below. Your Pismo representative can help guide you through this.

<details>
  <summary><b>Process to become a direct Pix participant</b></summary>

  General steps a company might take to become a direct participant in the Pix system:

  **Eligibility check** —Ensure your company meets the eligibility criteria set by the Central Bank of Brazil. These criteria may include financial stability, operational capacity, compliance with relevant regulations, and more.

  **Financial institutions**—Generally, only financial institutions are allowed to become direct participants in the PIX system. This includes banks, credit unions, and other authorized payment institutions.

  **Contact Central Bank or operator**—Reach out to the Central Bank of Brazil or the operator responsible for PIX to express your interest in becoming a direct participant. This could involve sending inquiries, attending workshops, or accessing application guidelines from official sources.

  **Application process**—Submit an application to the Central Bank or the relevant authority. This application will likely include detailed information about your company, its financial stability, operational capabilities, risk management practices, compliance with anti-money laundering (AML) and Know Your Customer (KYC) regulations, and more.

  **Technical integration**—If your application is approved, you'll need to integrate your systems with the Pix infrastructure. This might involve technical processes to ensure seamless connectivity and interoperability with the Pix system.

  **Security and compliance**—As a direct participant, your company will need to adhere to strict security protocols and comply with regulations to ensure the safety and integrity of the PIX system and its transactions.

  **Testing and certification**—Before going live, you'll likely need to undergo testing and certification processes to ensure that your systems and processes function correctly within the Pix ecosystem.

  **Go live**—Once your technical integration, security measures, and compliance checks are in place, you'll be allowed to go live and start processing transactions through the Pix system.

  It's important to note that the process and requirements can vary and are subject to change. To get the most accurate and up-to-date information on becoming a direct participant in Brazil's Pix system, Pismo recommends visiting the official website of the Central Bank of Brazil or contacting them directly.
</details>

## Pix keys

A Pix key is a unique identifier linked to a bank account that allows a user to receive payments without the need to share bank account details, such as their account number and branch code, which are traditionally required for transfers. You can [generate an encrypted Pix key](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-keys-create) with one of the following:

* **Taxpayer ID number**
  * CPF—Cadastro de Pessoas Fisicas (Brazil - Individual Taxpayer Registry) number. Similar to a Social Security number in the US.
  * CNPJ—Cadastro Nacional de Pessoa Juridica (Brazil - National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil.
* **Email address**
* **Mobile phone number**
* **EVP**—Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.

All Pix keys are registered with the BCB, which maintains the **Diretório de Identificadores de Contas Transacionais (DICT)** —a national Pix key registry and database. Individual users can have up to five keys for each account they own. Institutional users can have up to 20 keys. Each key must be associated with only one bank account.

Pismo provides a [Pix key API](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-keys-create) with endpoints for creating and managing keys both locally and with the DICT database.

### Pix key transfer (key claim)

You can use the Pix API to transfer key ownership using a ***key claim*** . You can do this if you try creating a key and it already exists at another financial institution with the same owner or a different owner.

Pismo defines two key claim types with the following enums:

* `OWNERSHIP`—Transfer key ownership between users in the same or another bank. Use this for transfer if creating a  key claim returns `400 Bad Request - EPDG0035 - Entry owned by different person`
* `PORTABILITY`—Transfer key ownership for the same user to another bank. Use this for transfer if creating a  key claim returns `400 Bad Requrest - EPDG0036 - Entry owned by same person, but with different participant.`

**Notes:**

* Only CPF/CNPJ type keys can be transferred.
* You cannot claim an EVP key - virtual payment address - since an EVP key value has no semantic meaning. Instead of starting a Claim process, you simply need to generate a new EVP key.

<details>
  <summary><b>Transfer key process</b></summary>

  1. Call [Create key claim](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-keys-create) to notify the original bank that you want to transfer a key.

  2. Original bank sends an acknowledgement which Pismo processes and uses to generate a <a href="https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1">Pix key claim status changed</a> event. To proceed to the next step, the `status` should be `WAITING_RESOLUTION`.

  3. You have seven days to call [Confirm key claim](https://developers.pismo.io/pismo-docs/reference/post-complete-dict-claim) and confirm the claim. If no confirmation is received after 7 days the following happens, depending on key claim type:
     1. `OWNERSHIP`—The original bank proceeds with the transfer automatically. Proceed to step 4.
     2. `PORTABILITY`—The original bank automatically cancels the key claim. BCB receives the cancellation and contacts the receiving bank. End of process.

  4. The Central Bank of Brazil (BCB) receives this confirmation and contacts the receiving bank.
     1. `OWNERSHIP`—Receiving bank confirms the claim with the end user \[EMAIL or SMS]
        1. Receiving bank calls [Complete key claim](https://developers.pismo.io/pismo-docs/reference/post-complete-dict-claim) to complete the claim.
     2. `PORTABILITY`—Receiving bank completes the claim automatically, which Pismo processes. Key is created in the database. If no completion is received in 30 days,  the original bank proceeds with the cancel automatically.
</details>

## Pix transactions

There are 4 types of Pix transactions, as indicated with the following enums:

**`PIX_OUT`**

This occurs via the [Pix-out transfer](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer) endpoint. Upon fund transfer completion, the platform generates a <a href="https://developers.pismo.io/events/docs/pix-pix-out-1">Pix-out notification received </a> event - the`status` field indicates whether the transaction failed or succeeded.

**`PIX_IN`**

This also occurs via the [Pix-out notification received](https://developers.pismo.io/events/docs/pix-pix-out-1) endpoint when the funds are deposited in the payee's account. This could be a Pismo account or an external account. Upon completion, the platform generates a <a href="https://developers.pismo.io/events/docs/pix-pix-in-1"> Pix-in notification received</a> event - the`status` field indicates whether the transaction failed or succeeded.

**`PIX_OUT_REVERSAL`**

This occurs via the [Pix reversal](https://developers.pismo.io/pismo-docs/reference/post-pix-reversal) endpoint and reverses a `PIX_OUT` transfer. Upon completion, the platform generates a <a href="https://developers.pismo.io/events/docs/pix-pix-out-reversal-1">Pix-out reversed</a> event with a `status` field indicating success or failure.

**`PIX_IN_REVERSAL`**

This also occurs via the [Pix reversal](https://developers.pismo.io/pismo-docs/reference/post-pix-reversal) endpoint and reverses a `PIX_IN` transfer from a payee's account, which can be a Pismo account or an external account. Upon completion, the platform generates a <a href="https://developers.pismo.io/events/docs/pix-pix-in-reversal-1">Pix-in reversed</a> event with a `status` field indicating success or failure.

> 📘 Anti-fraud webhook for Pix transactions
>
> Clients have the option to implement an [anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#client-anti-fraud-webhook-for-banking-transactions) for Pix transactions to supplement the anti-fraud checking and validation Pismo does.

### Generating dynamic QR Codes and BR Codes for Pix transactions

Pismo has a [QR Code API](https://developers.pismo.io/pismo-docs/reference/post-create-cob) for generating dynamic QR Codes.  A dynamic QR Code is a type of QR Code that can be edited or modified after it has been created. Unlike static QR Codes, dynamic QR Codes allow for flexibility in the types of information they convey. They are particularly useful when there is a need to update QR Code information, such as changing a URL, updating contact details, or modifying product information.

You can generate two kinds of dynamic QR Codes: COB and COBV.  COB is short for *cobranca*, which means *charge* in Portuguese. A COB QR Code has an expiration date, while a COBV QR Code has a due date, fine, interest, and rebates.

Pismo also has a [BR Code API](https://developers.pismo.io/pismo-docs/reference/br-code) for generating Brazilian Barcodes (BR Codes) - a standard barcode format used in Brazil for electronic payments. The BCB regulates BR Codes within the the Brazilian Payment System (SPB). The BR Code contains information about the payee, transaction details, and other data.

For more information, refer to [Pix and QR Codes](https://developers.pismo.io/pismo-docs/docs/pix-and-qr-codes) .

## Scheduled transactions

You can [schedule a Pix transaction](https://developers.pismo.io/pismo-docs/reference/post-schedule-pix-payment) for a future date. Basically, you specify a future date to make the payment, along with the transaction details, such as the payee (branch and account) and transaction amount. Pismo executes the transfer on the scheduled date. You can also schedule recurring transactions that take place, weekly, monthly, and so on.

## Infraction reports

**Infraction reports** are used to tag transactions that a Pix user believes are fraudulent or otherwise invalid. In this situation, they can **tag** an infraction (report it to their bank or PSP), which then shares relevant transaction details with the other party’s bank or PSP. Either a payee or payer can [make an infraction report](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-infraction-create). The Pix API provides endpoints for creating and resolving infraction reports.

There are 2 infraction report types:

* `REFUND_REQUEST`—Initiated only by payer's payment service provider (PSP). Used to mark a key as fraudulent and asks for a refund.
* `REFUND_CANCELLED`—Initiated only by payee's PSP.   To indicate that a refund done by an infraction process was a fraud and needs to be returned,

### Infraction report process

1. Payment service provider (PSP) calls [Create infraction report](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-infraction-create) to open an infraction. This generates an <a href="https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1" target="_blank">Pix infraction status changed</a> event with status `OPEN`.
2. PSP can accept or reject infraction using endpoint [Close infraction report](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-infraction-close). This generates a status event with status `CLOSED`.  The `analysis_results` field can be either `AGREED` or `DISAGREED`

During the above steps, the PSP has the option to call [Cancel infraction report](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-infraction-cancel) to cancel the infraction. This generates a status event with status `CANCELLED`.

## Refund requests

The Pix API provides endpoints for creating and managing transaction refund requests.

### Refund request process

1. Payment service provider (PSP) calls [Create refund request](https://developers.pismo.io/pismo-docs/reference/post-register-dict-refund) to open a refund request . This generates a <a href="https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1">Pix reversal (refund) status changed</a> with status `OPEN`.
2. PSP can accept or reject refund request using endpoint [Close refund](https://developers.pismo.io/pismo-docs/reference/post-close-dict-refund). This generates a status event with status `CLOSED`The `analysis_results`field can be either `TOTALLY_ACCEPTED`, `PARTIALLY_ACCEPTED` or `REJECTED`.

During the above steps, the PSP has the option to call [Cancel refund](https://developers.pismo.io/pismo-docs/reference/post-cancel-dict-refund) to cancel the infraction. This generates a status event with status `CANCELLED`.

## Pix funds recovery

As of November, 2025, there are new endpoints for Pix funds recovery. For more information, refer to [Pix funds recovery](https://developers.pismo.io/pismo-docs/docs/pix-funds-recovery).

## Pix events

See the [Pix data events](https://developers.pismo.io/pismo-docs/docs/pix-payments-data-events) guide.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v2/pix/keys` | `post-v2-pix-keys-create` | Create key entry | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--keys-part-01 |
| `POST /v2/pix/claims/complete` | `post-complete-dict-claim` | Complete key claim | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--claims |
| `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | Pix-out transfer | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /pix/v1/pix/in/reversal` | `post-pix-reversal` | Pix reversal | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /v1/pix/qrcode/cob` | `post-create-cob` | Create dynamic COB QR Code | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--qr-code |
| `POST /pix/v2/pix/out/scheduler` | `post-schedule-pix-payment` | Schedule transfer(s) V2 | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `POST /v2/pix/infraction-reports` | `post-v2-pix-infraction-create` | Create infraction report (outdated) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01 |
| `POST /v2/pix/infraction-reports/{id}/close` | `post-v2-pix-infraction-close` | Close infraction report | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01 |
| `POST /v2/pix/infraction-reports/{id}/cancel` | `post-v2-pix-infraction-cancel` | Cancel infraction report | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01 |
| `POST /v2/pix/refunds` | `post-register-dict-refund` | Create refund request | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--refunds |
| `POST /v2/pix/refunds/{refundId}/close` | `post-close-dict-refund` | Close refund | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--refunds |
| `POST /v2/pix/refunds/{refundId}/cancel` | `post-cancel-dict-refund` | Cancel refund | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--refunds |

### Operation essentials

- **`POST /v2/pix/keys`** (`post-v2-pix-keys-create`): security `BearerAuth`; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `key`, `key_type`, `reason`, `bank_account`; response statuses 201, 202, 400, 401, 403, 404, 409, 429, 500, 502, 503, 504; error codes in examples `EPDA0169`, `EPDA0002`, `EPDA0003`, `EPDA0038`, `EPDA0039`, `EPDA0040`, `EPDA0041`, `EPDA0042`, `EPDA0043`, `EPDG0001`, `EPDG0011`, `PBE353`, `EPDG0018`, `EPDG0019`, `EPDG0035`, `EPDG0036`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDA0023`, `EPDA0024`, `EPDG0014`, `PBE353`, `EPDA0025`, `EPDA0028`, `EPDA0029`, `EPDG0005`, `EPDG0006`, `EPDG0007`, `EPDG0010`, `EPDG0016`, `PBE315`, `EPDG0020`, `EPDG0017`, `EPDG0021`, `EPDA0000`, `EPDG0000`; events `pix-dict-key-status-change-1`.
- **`POST /v2/pix/claims/complete`** (`post-complete-dict-claim`): security `BearerAuth`; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `claim_id`; response statuses 200, 202, 400, 403, 404, 500, 502, 504; error codes in examples `EPDA0180`, `EPDA0162`, `EPDA0160`, `EPDA0161`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDG0020`, `EPDA0000`; events `pix-dict-claim-status-change-1`.
- **`POST /pix/v1/pix/out/transfer`** (`post-pix-out-transfer`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `transaction_type`; response statuses 202, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0020`, `EPIX0032`, `EPIX0139`, `EPIX0132`, `EPIX0067`, `EPIX0126`, `EPIX0115`, `EPIX0226`, `EPIX0227`, `EPIX0228`, `EPIX0136`, `EPIX0022`, `EPIX0137`, `EPIX0138`, `EPIX0113`, `EPIX0123`, `EPIX0120`, `EPIX0124`, `EPIX0122`, `EPIX0141`, `EPIX0019`, `EPIX0008`, `EPIX0053`, `EPIX0003`, `EPIX0114`, `EPIX0061`, `EPIX0068`, `EPIX0130`, `EPIX0045`, `EPIX0110`, `EPIX0146`, `EPIX0160`, `EPIX0049`, `EPIX0009`, `EPIX0069`, `EPIX0010`, `EPIX0111`, `EPIX0112`, `EPIX0051`, `EPIX0041`, `EPIX0071`, `EPIX0142`, `EPIX0144`, `EPIX0085`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0042`, `EPIX0017`, `EPIX0108`, `EPIX0109`, `EPIX0014`, `EPIX0043`, `EPIX0089`, `EPIX0046`, `EPIX0070`, `EPIX0018`, `EPIX0051`, `EPIX0060`, `EPIX0030`, `EPIX0050`, `EPIX0058`; events `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`POST /pix/v1/pix/in/reversal`** (`post-pix-reversal`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `end_to_end_id`, `reason`; response statuses 202, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0005`, `EPIX0020`, `PCE001`, `EPIX0045`, `EPIX0049`, `EPIX0084`, `EPIX0009`, `EPIX0010`, `EPIX0069`, `EPIX0132`, `EPIX0003`, `EPIX0041`, `EPIX0008`, `EPIX0071`, `EPIX0083`, `EPIX0085`, `EPIX0086`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0014`, `EPIX0043`, `EPIX0018`, `EPIX0030`; events `pix-financial-reconciliation-1`, `pix-pix-in-reversal-1`, `pix-pix-out-reversal-1`.
- **`POST /v1/pix/qrcode/cob`** (`post-create-cob`): security not declared; required parameters `Authorization` (header); required body fields `payee`, `payer`, `transaction_identification`, `initial_amount`; response statuses 202, 400, 401, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events none listed.
- **`POST /pix/v2/pix/out/scheduler`** (`post-schedule-pix-payment`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `scheduler_details`; response statuses 201, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events `instantpay-scheduler-scheduler-status-change-1`, `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`POST /v2/pix/infraction-reports`** (`post-v2-pix-infraction-create`): security `BearerAuth`; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `transaction_id`, `situation_type`, `reason`; response statuses 201, 202, 400, 401, 403, 429, 500, 502, 503, 504; error codes in examples `EPDA0148`, `EPDA0149`, `EPDA0002`, `EPDA0003`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDA0029`, `EPDG0005`, `EPDG0006`, `EPDG0007`, `EPDG0010`, `EPDG0016`, `PBE315`, `EPDG0020`, `EPDG0017`, `EPDG0021`, `EPDA0000`, `EPDG0000`; events `pix-dict-infraction-status-change-1`.
- **`POST /v2/pix/infraction-reports/{id}/close`** (`post-v2-pix-infraction-close`): security `BearerAuth`; required parameters `Authorization` (header), `id` (path); required body fields `analysis_result`; response statuses 200, 202, 400, 401, 403, 404, 429, 500, 502, 503, 504; error codes in examples `EPDA0148`, `EPDA0149`, `EPDA0001`, `EPDA0070`, `EPDA0002`, `ECM0005`, `EPDA0003`, `ECM0002`, `ECM0003`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDA0049`, `EPDA0029`, `EPDG0005`, `EPDG0006`, `EPDG0007`, `EPDG0010`, `EPDG0016`, `PBE315`, `EPDG0020`, `EPDG0017`, `EPDG0021`, `EPDA0000`, `EPDG0000`; events `pix-dict-infraction-status-change-1`.
- **`POST /v2/pix/infraction-reports/{id}/cancel`** (`post-v2-pix-infraction-cancel`): security `BearerAuth`; required parameters `Authorization` (header), `id` (path); required body fields none declared; response statuses 200, 202, 400, 401, 403, 404, 429, 500, 502, 503, 504; error codes in examples `EPDA0148`, `EPDA0149`, `EPDA0001`, `EPDA0070`, `EPDA0073`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDA0049`, `EPDA0029`, `EPDG0005`, `EPDG0006`, `EPDG0007`, `EPDG0010`, `EPDG0016`, `PBE315`, `EPDG0020`, `EPDG0017`, `EPDG0021`, `EPDA0000`, `EPDG0000`; events `pix-dict-infraction-status-change-1`.
- **`POST /v2/pix/refunds`** (`post-register-dict-refund`): security `BearerAuth`; required parameters `x-tenant` (header), `Idempotency-Key` (header); required body fields `refund_amount`, `refund_reason`, `transaction_id`; response statuses 200, 202, 400, 403, 404, 500, 502, 504; error codes in examples `EPDA0174`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDG0020`, `EPDA0000`, `EPDG0000`; events `pix-dict-refund-status-change-1`.
- **`POST /v2/pix/refunds/{refundId}/close`** (`post-close-dict-refund`): security `BearerAuth`; required parameters `x-tenant` (header), `Idempotency-Key` (header), `refundId` (path); required body fields `refund_analysis_result`; response statuses 200, 202, 400, 403, 404, 500, 502, 504; error codes in examples `EPDA0174`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDG0020`, `EPDA0000`, `EPDG0000`; events `pix-dict-refund-status-change-1`, `pix-financial-reconciliation-1`.
- **`POST /v2/pix/refunds/{refundId}/cancel`** (`post-cancel-dict-refund`): security `BearerAuth`; required parameters `x-tenant` (header), `Idempotency-Key` (header), `refundId` (path); required body fields none declared; response statuses 200, 400, 403, 404, 500, 502, 504; error codes in examples `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDG0020`, `EPDA0000`, `EPDG0000`; events `pix-dict-refund-status-change-1`.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `br-code` | BR Code API | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-schedule-pix-payment` | `instantpay-scheduler-scheduler-status-change-1` |
| `post-complete-dict-claim` | `pix-dict-claim-status-change-1` |
| `post-v2-pix-infraction-cancel` | `pix-dict-infraction-status-change-1` |
| `post-v2-pix-infraction-close` | `pix-dict-infraction-status-change-1` |
| `post-v2-pix-infraction-create` | `pix-dict-infraction-status-change-1` |
| `post-v2-pix-keys-create` | `pix-dict-key-status-change-1` |
| `post-cancel-dict-refund` | `pix-dict-refund-status-change-1` |
| `post-close-dict-refund` | `pix-dict-refund-status-change-1` |
| `post-register-dict-refund` | `pix-dict-refund-status-change-1` |
| `post-close-dict-refund` | `pix-financial-reconciliation-1` |
| `post-pix-out-transfer` | `pix-financial-reconciliation-1` |
| `post-pix-reversal` | `pix-financial-reconciliation-1` |
| `post-schedule-pix-payment` | `pix-financial-reconciliation-1` |
| `post-pix-out-transfer` | `pix-pix-in-1` |
| `post-schedule-pix-payment` | `pix-pix-in-1` |
| `post-pix-reversal` | `pix-pix-in-reversal-1` |
| `post-pix-out-transfer` | `pix-pix-out-1` |
| `post-schedule-pix-payment` | `pix-pix-out-1` |
| `post-pix-reversal` | `pix-pix-out-reversal-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `pix-dict-claim-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1 | 4 | KU-EVT-catalogue-pix |
| `pix-dict-infraction-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1 | 4 | KU-EVT-catalogue-pix |
| `pix-dict-refund-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1 | 3 | KU-EVT-catalogue-pix |
| `pix-pix-in-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-in-1 | 3 | KU-EVT-catalogue-pix |
| `pix-pix-in-reversal-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-in-reversal-1 | 1 | KU-EVT-catalogue-pix |
| `pix-pix-out-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-out-1 | 3 | KU-EVT-catalogue-pix |
| `pix-pix-out-reversal-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-out-reversal-1 | 1 | KU-EVT-catalogue-pix |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/pix-instant-payments.md`: updatedAt 2026-07-20T19:05:54.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 7 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.
- Operation link `br-code` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/pix-instant-payments.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pix-instant-payments | `18079ccebc833080…` | 2026-07-20T19:05:54.000Z |

## Related knowledge units

- `KU-API-instant-payments-pix-management--claims` — API reference: Instant payments - Pix management — Claims
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-instant-payments-pix-management--keys-part-01` — API reference: Instant payments - Pix management — Keys (part 1 of 2)
- `KU-API-instant-payments-pix-management--refunds` — API reference: Instant payments - Pix management — Refunds
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` — API reference: Instant payments - Pix payments — Scheduled transfers V2
- `KU-API-instant-payments-qr-code--qr-code` — API reference: Instant payments - QR Code — QR Code
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-EVT-client-webhooks-part-02` — Client webhooks (part 2 of 14)
- `KU-EVT-client-webhooks-part-03` — Client webhooks (part 3 of 14)
- `KU-EVT-client-webhooks-part-04` — Client webhooks (part 4 of 14)
- `KU-EVT-client-webhooks-part-05` — Client webhooks (part 5 of 14)
- `KU-EVT-client-webhooks-part-06` — Client webhooks (part 6 of 14)
- `KU-EVT-client-webhooks-part-07` — Client webhooks (part 7 of 14)
- `KU-EVT-client-webhooks-part-08` — Client webhooks (part 8 of 14)
- `KU-EVT-client-webhooks-part-09` — Client webhooks (part 9 of 14)
- `KU-EVT-client-webhooks-part-10` — Client webhooks (part 10 of 14)
- `KU-EVT-client-webhooks-part-11` — Client webhooks (part 11 of 14)
- `KU-EVT-client-webhooks-part-12` — Client webhooks (part 12 of 14)
- `KU-EVT-client-webhooks-part-13` — Client webhooks (part 13 of 14)
- `KU-EVT-client-webhooks-part-14` — Client webhooks (part 14 of 14)
- `KU-EVT-pix-payments-data-events` — Instant payments - Pix
- `KU-PAY-pix-and-qr-codes` — Pix and QR Codes
- `KU-PAY-pix-funds-recovery` — Pix funds recovery [beta]
