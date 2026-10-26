---
ku_id: KU-PAY-pix-and-qr-codes
title: Pix and QR Codes
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/pix-and-qr-codes.md
  sha256: baa3fa80fceebfbe165369002b139d6e6ea236261266a0b5106a7d31766d07f6
  url: https://developers.pismo.io/pismo-docs/docs/pix-and-qr-codes
  role: primary_guide
  updated_at: '2026-05-11T21:53:41.000Z'
operations:
- post-create-cob
- post-create-recurrence
- post-create-recurrence-cob
- post-create-recurrence-cobv
- post-create-static
- post-pix-out-transfer
- post-qr-code
- post-qrcode-cobv
- post-schedule-pix-payment
related_kus:
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--scheduled-transfers-v2
- KU-API-instant-payments-qr-code--qr-code
- KU-API-instant-payments-qr-code--recurring-payment
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-pix
- KU-PAY-pix-automatic
grouping_rationale: single source page
---

# Pix and QR Codes

**KU ID:** `KU-PAY-pix-and-qr-codes` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/pix-and-qr-codes.md`:

> Pix uses QR Codes—specifically the BR Code format adhering to Europay Mastercard Visa (EMV) standards—to embed payment details such as recipient account, Pix key, and in the case of dynamic codes, transaction amount and metadata.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/pix-and-qr-codes.md`: Pix and QR Codes; Static QR Codes; Dynamic QR Codes; Consumer and merchant flow; Use cases; Security and architecture; Why QR Codes are essential to Pix; Dynamic QR Code types; COB—immediate payment request; COBV—due date payment request; COBR—recurring payment request; Withdrawal—cash withdrawal; Change; Using QR Codes; API endpoints and sample payloads; Create dynamic COB QR Code; Create dynamic COBV QR Code; Create recurrent compound QR Code (journey 2); Create recurrent COB QR Code (journey 3); Create recurrent COBV QR Code (journey 4); Create recurrent static QR Code (journey 4); Summary

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 9 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/pix-and-qr-codes.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pix-and-qr-codes · updatedAt: 2026-05-11T21:53:41.000Z

<!-- source:begin path=docs/core-banking/pix-and-qr-codes.md part=0-end -->

# Pix and QR Codes

Pix uses QR Codes—specifically the BR Code format adhering to Europay Mastercard Visa (EMV) standards—to embed payment details such as recipient account, Pix key, and in the case of dynamic codes, transaction amount and metadata.

## Static QR Codes

* Contain only recipient’s account or Pix key.
* Suitable for recurring or fixed‑amount payments—like at small shops or service stations.
* Payer must enter the amount manually.

## Dynamic QR Codes

* Unique per transaction.
* Includes recipient, amount, due date, fines/discounts, and transaction ID.
* Automatically expires after a set time.
* Built to facilitate seamless automation and reconciliation for merchants.

# Consumer and merchant flow

1. Merchant generates a QR Code (static or dynamic) and displays it on-screen, printed receipt, or mobile app.
2. Customer opens their banking or wallet app, chooses Pix, scans the QR Code.
3. The app extracts payment data (amount if dynamic), shows the details, the user confirms, and taps “pay.”
4. Funds are transferred in seconds, any time of day.

## Use cases

* **Person-to-Merchant (P2M)**—QR codes are widely adopted in Brazil for merchant payments—over 30% of Pix volume is P2M.
* **E-commerce and online checkout**—Users scan QR or copy-paste a Pix code to pay instantly.
* **Small businesses and service vendors**—Use static QR Codes on stickers, receipts, or booths for simple payments.
* **Large merchants**—Use dynamic QR Codes tied to back-end billing systems so that each transaction is uniquely identifiable and settled quickly.

# Security and architecture

Pix keys (CPF/CNPJ, email, phone number, or random UUID) provide identity linkage via the Central Bank’s DICT database .

BR Codes conform to EMV QR‑code standards and may embed a link to fetch dynamic charge data via a secure endpoint, often encoded as a JWT payload including amount; banks validate the digital signature before proceeding.

## Why QR Codes are essential to Pix

* **Interoperability**—Any Pix‑enabled app across any bank or fintech can scan the same code format.
* **No new hardware needed**—Merchants don’t need card terminals—just display the code. Consumers just need a smartphone.
* **Speed and automation**—Dynamic codes support automatic reconciliation and fast settlements; static codes simplify frequent small-value payments.
* **Low costs**—Especially beneficial for merchants and micro‑businesses, who otherwise face card‑processing fees.

# Dynamic QR Code types

## COB—immediate payment request

COB is short for ***cobranca***, which means "charge" in Portuguese.

**Purpose**: Generates a request for a one-time, immediate payment.\
**Key points**:

* Includes a fixed amount and expiration date.
* Can contain fields like `payer_solicitation`(payee text sent to payer)  and `allows_value_change`(payer can change payment values).
* Ideal for one-off transactions such as e-commerce or in-person payments.
* When combined with a COBR in a composite QR Code, it triggers [Pix Automatic Journey 3](https://developers.pismo.io/pismo-docs/docs/pix-automatic#pix-automatic-use-cases-journeys) (`AUT3`).

## COBV—due date payment request

**Purpose**: Payment request with a due date, supporting interest, fines, and discounts.\
**Key points**:

* Supports fields like `due_date`(payment due date) and `charges`(charge information).
* Enables automatic reconciliation and delinquency control.
* Commonly used as a replacement for traditional <a href="https://en.wikipedia.org/wiki/Boleto" target="_blank">boletos</a>.
* When combined with a COBR in a composite QR Code, it triggers [Pix Automatic journey 4](https://developers.pismo.io/pismo-docs/docs/pix-automatic#pix-automatic-use-cases-journeys)  (`AUT4`).

## COBR—recurring payment request

**Purpose**: Used to configure recurring payment authorizations in Pix Automatic.\
**Key points**:

* Identified with `recurrence_id`field.
* Can be used:
  * Standalone ([journey 2](https://developers.pismo.io/pismo-docs/docs/pix-automatic#pix-automatic-use-cases-journeys)).
  * With COB ([journey 3](https://developers.pismo.io/pismo-docs/docs/pix-automatic#pix-automatic-use-cases-journeys)).
  * With static QR or COBV ([journey 4](https://developers.pismo.io/pismo-docs/docs/pix-automatic#pix-automatic-use-cases-journeys)).
  * Always part of a composite QR Code structure.

## Withdrawal—cash withdrawal

**Purpose**: Enables cash withdrawal via Pix at authorized commercial establishments.\
**Key points**:

* The customer makes a Pix payment and receives the equivalent amount in cash.
* Can be used with dynamic or static QR Codes.
* Requires accreditation as a Cash Withdrawal Service Facilitator (FSS) with the Central Bank of Brazil (BCB)—a Pix-participating financial or payment institution authorized to enable cash withdrawals and cash back during purchases.
* Content structure in the QR Code payload:
  ```json
  "withdraw": {
      "agent_modality": "AGTEC",
      "ispb_service_provider": "85478745",
      "amount": 10.0,
      "allows_value_change": true
  }
  ```

## Change

**Purpose**: Enables cashback transactions via Pix.\
**Key points**:

* The customer pays more than the purchase amount and receives the difference in cash.
* Used in commercial environments accredited for this service.
* Requires accreditation as a Cash Withdrawal Service Facilitator (FSS)
* Content structure in the QR Code payload:
  ```json
  "change": {
      "agent_modality": "AGTEC",
      "ispb_service_provider": "85478745",
       "amount": 10.0,
  }
   
  ```

# Using QR Codes

* Call [Validate QR Code](https://developers.pismo.io/pismo-docs/reference/post-qr-code)  to validate a QR Code for a [Pix-out transfer](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer).
* Pay immediately a COB, COBV, Charge and Withdrawal QR Code for a  [Pix-out transfer](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer)  payment.
* Schedule payment for a COB and COBV QR Code using [Schedule transfer(s) V2 \[beta\]](ref:post-schedule-pix-payment).

**Note:** Pismo automatically identifies the `transaction_id `when a Pix -in is received and changes a QR Code  status to `COMPLETED`.

# API endpoints and sample payloads

## Create dynamic COB QR Code

[Create dynamic COB QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-cob) —Generate a new dynamic COB QR Code and EMV (Europay Mastercard Visa) string.

COB is short for ***cobranca***, which means "charge" in Portuguese. A COB QR Code has an expiration date while a COBV QR Code has a due date, fine, interest, and rebates.

<details>
  <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample payload</summary>

  ```json
  curl -X POST "https://sandbox.pismolabs.io/qrcode/v1/pix/qrcode/cob" \
  -H "Authorization: Bearer <your_bearer_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "payee": {
      "address": "10 Downing Street, London SW1A 2AB, UK",
      "city": "Brasilia",
      "key": "chuck@steaks.com",
      "state": "DF",
      "zip_code": "8675309"
    },
    "payer": {
      "name": "Eva Destrukion",
      "address": "10 Downing Street, London SW1A 2AB, UK",
      "city": "Brasilia",
      "document_number": "42761202686",
      "state": "DF",
      "trade_name": "Acme Widgets",
      "type": "NATURAL_PERSON",
      "zip_code": "8675309"
    },
    "transaction_identification": "trans-id-7578994740",
    "initial_amount": 86753.09,
    "payer_solicitation": "For dinner last night",
    "qrcode_expiration_time": 7200,
    "allows_value_change": true,
    "reusable": true,
    "location": {
      "url_jwk": "example.com/jwk",
      "url_payload": "example.com/pix/8b3da2f3-941-40d1-a91a-bd93113bd441"
    },
    "additional_information": [
      {
        "name": "Purity of essence",
        "value": "5.00"
      }
    ],
    "access_token": "153ed19a-e738-4417-9e98-a515c276a731"
  }'
  ```
</details>

## Create dynamic COBV QR Code

[Create dynamic COBV QR Code](https://developers.pismo.io/pismo-docs/reference/post-qrcode-cobv) —Generate a new COBV QR Code image and EMV (Europay Mastercard Visa) string.

<details>
  <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample payload</summary>

  ```json
  curl -X POST "https://sandbox.pismolabs.io/qrcode/v1/pix/qrcode/cobv" \
  -H "Authorization: Bearer <your_bearer_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "charge": {
      "due_date": "2024-01-12",
      "discount_type": "FIXED_VALUE_UNTIL_THE_DATES_INFORMED",
      "discount_value": 99,
      "fine_type": "FIXED_VALUE",
      "fine_value": 45.67,
      "interest_type": "VALUE_WORKING_DAYS",
      "interest_value": 34.09
    },
    "payee": {
      "address": "10 Downing Street, London SW1A 2AB, UK",
      "city": "Brasilia",
      "key": "chuck@steaks.com",
      "state": "DF",
      "zip_code": "8675309"
    },
    "payer": {
      "name": "Eva Destrukion",
      "address": "10 Downing Street, London SW1A 2AB, UK",
      "city": "Brasilia",
      "document_number": "42761202686",
      "state": "DF",
      "zip_code": "8675309"
    },
    "initial_amount": 86753.09,
    "transaction_identification": "trans-id-7578994740",
    "payer_solicitation": "For dinner last night",
    "qrcode_expiration_time": 7200,
    "reusable": true,
    "allows_value_change": true
  }'
  ```
</details>

## Create recurrent compound QR Code (journey 2)

[Create recurrent compound QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-recurrence) —Create a compound QR Code containing only recurring payment authorization configuration data.

<details>
  <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample payload</summary>

  ```json
  curl -X POST "https://sandbox.pismolabs.io/qrcode/v1/pix/qrcode/recurrence" \
  -H "Authorization: Bearer <your_bearer_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "payee": {
      "city": "Brasilia",
      "state": "DF",
      "zip_code": "8675309"
    },
    "transaction_identification": "trans-id-7578994740",
    "recurrence_id": "RN219952X6X02505XXCONTRACTXXX",
    "recurrence": {
      "frequency_type": "MONTH",
      "first_payment_date": "2025-04-25",
      "last_payment_date": "2026-06-10",
      "amount": 1050.44,
      "debtor": {
        "document_number": "42761202686",
        "document_type": "NATURAL_PERSON",
        "name": "Eva Destrukion"
      },
      "contract_id": "5509-uroo-78944-9987",
      "description": "Gym membership",
      "retry": true
    },
    "access_token": "153ed19a-e738-4417-9e98-a515c276a731"
  }'
  ```
</details>

## Create recurrent COB QR Code (journey 3)

[Create recurrent COB QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-recurrence-cob)—Create a COB QR Code for a recurring payment as a EMV (Europay Mastercard Visa) string. Recurring  payments are used for such things as subscriptions, school fees, rent, gym memberships and more.

<details>
  <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample payload</summary>

  ```json
  curl -X POST "https://sandbox.pismolabs.io/qrcode/v1/pix/qrcode/cob/recurrence" \
  -H "Authorization: Bearer <your_bearer_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "payee": {
      "address": "10 Downing Street, London SW1A 2AB, UK",
      "city": "Brasilia",
      "key": "chuck@steaks.com",
      "state": "DF",
      "zip_code": "8675309"
    },
    "payer": {
      "name": "Eva Destrukion",
      "document_number": "42761202686",
      "type": "NATURAL_PERSON"
    },
    "initial_amount": 86753.09,
    "transaction_identification": "trans-id-7578994740",
    "recurrence": {
      "frequency_type": "MONTH",
      "first_payment_date": "2025-04-25",
      "debtor": {
        "document_number": "42761202686",
        "document_type": "NATURAL_PERSON",
        "name": "Eva Destrukion"
      },
      "contract_id": "5509-uroo-78944-9987"
    }
  }'
  ```
</details>

## Create recurrent COBV QR Code (journey 4)

[Create recurrent COBV QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-recurrence-cobv) —Create a COBV QR Code for a recurring payment as a EMV (Europay Mastercard Visa) string

<details>
  <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample payload</summary>

  ```json
  curl -X POST "https://sandbox.pismolabs.io/qrcode/v1/pix/qrcode/cobv/recurrence" \
  -H "Authorization: Bearer <your_bearer_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "charge": {
      "due_date": "2024-01-12",
      "discount_type": "FIXED_VALUE_UNTIL_THE_DATES_INFORMED",
      "discount_value": 99,
      "fine_type": "FIXED_VALUE",
      "fine_value": 45.67,
      "interest_type": "VALUE_WORKING_DAYS",
      "interest_value": 34.09
    },
    "payee": {
      "address": "10 Downing Street, London SW1A 2AB, UK",
      "city": "Brasilia",
      "key": "chuck@steaks.com",
      "state": "DF",
      "zip_code": "8675309"
    },
    "payer": {
      "name": "Eva Destrukion",
      "document_number": "42761202686",
      "type": "NATURAL_PERSON"
    },
    "initial_amount": 86753.09,
    "transaction_identification": "trans-id-7578994740",
    "recurrence": {
      "frequency_type": "MONTH",
      "first_payment_date": "2025-04-25",
      "debtor": {
        "document_number": "42761202686",
        "document_type": "NATURAL_PERSON",
        "name": "Eva Destrukion"
      },
      "contract_id": "5509-uroo-78944-9987"
    }
  }'
  ```
</details>

## Create recurrent static QR Code (journey 4)

[Create recurrent static QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-static) —Create a recurrent static QR Code and EMV (Europay Mastercard Visa) string.

<details>
  <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample payload</summary>

  ```json
  curl -X POST "https://sandbox.pismolabs.io/qrcode/v1/pix/qrcode/static/recurrence" \
  -H "Authorization: Bearer <your_bearer_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "payee": {
      "address": "10 Downing Street, London SW1A 2AB, UK",
      "city": "Brasilia",
      "key": "chuck@steaks.com",
      "state": "DF",
      "zip_code": "8675309"
    },
    "amount": 86753.09,
    "transaction_identification": "trans-id-7578994740",
    "additional_information": "Additional info about this qrcode",
    "location": {
      "url_jwk": "example.com/jwk",
      "url_payload_rec": "example.com/rec/8b3da2f3-941-40d1-a91a-bd93113bd441"
    },
    "recurrence_id": "RN219952X6X02505XXCONTRACTXXX",
    "recurrence": {
      "frequency_type": "MONTH",
      "first_payment_date": "2025-04-25",
      "last_payment_date": "2026-06-10",
      "amount": 1050.44,
      "min_payment_amount": 10.09,
      "debtor": {
        "document_number": "42761202686",
        "document_type": "NATURAL_PERSON",
        "name": "Eva Destrukion"
      },
      "contract_id": "5509-uroo-78944-9987",
      "description": "Gym membership",
      "retry": true
    },
    "access_token": "153ed19a-e738-4417-9e98-a515c276a731"
  }'
  ```
</details>

# Summary

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        QR Code Type
      </th>

      <th>
        Embedded Data
      </th>

      <th>
        Use Case/Advantages
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Static
      </td>

      <td>
        Pix key or account (no amount)
      </td>

      <td>
        * Regular small payments
        * Reusable, simple, ideal for small vendors
        * Natural and legal person can create
        * Normal transfer and buy purpose
      </td>
    </tr>

    <tr>
      <td>
        Dynamic
      </td>

      <td>
        Pix key + amount + txID + expiry
      </td>

      <td>
        * Automated merchant billing
        * Precise, traceable, suited to e‑commerce and  larger businesses
        * Legal person can create
        * Always have buy/charge purpose
      </td>
    </tr>
  </tbody>
</Table>

QR Codes are integral to how Pix enables seamless, real-time payments in Brazil. Whether you pay at a café, at a checkout terminal, or through an e‑commerce platform, you simply scan—or tap on—a code, confirm the amount, and the transfer happens in seconds. The system’s design emphasizes speed, low cost, and broad compatibility.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /pix/v1/pix/qrcode/validate` | `post-qr-code` | Validate QR Code | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | Pix-out transfer | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /pix/v2/pix/out/scheduler` | `post-schedule-pix-payment` | Schedule transfer(s) V2 | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `POST /v1/pix/qrcode/cob` | `post-create-cob` | Create dynamic COB QR Code | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--qr-code |
| `POST /v1/pix/qrcode/cobv` | `post-qrcode-cobv` | Create dynamic COBV QR Code | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--qr-code |
| `POST /v1/pix/qrcode/recurrence` | `post-create-recurrence` | Create recurrent compound QR Code | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--recurring-payment |
| `POST /v1/pix/qrcode/cob/recurrence` | `post-create-recurrence-cob` | Create recurrent COB QR Code | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--recurring-payment |
| `POST /v1/pix/qrcode/cobv/recurrence` | `post-create-recurrence-cobv` | Create recurrent COBV QR Code | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--recurring-payment |
| `POST /v1/pix/qrcode/static/recurrence` | `post-create-static` | Create recurrent static QR Code | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--recurring-payment |

### Operation essentials

- **`POST /pix/v1/pix/qrcode/validate`** (`post-qr-code`): security not declared; required parameters `Authorization` (header); required body fields `emv`; response statuses 200, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0003`, `EPIX0015`, `EPIX0019`, `EPIX0020`, `PCE001`, `EPIX0032`, `EPIX0061`, `EPIX0070`, `EPIX0074`, `EPIX0076`, `EPIX0127`, `EPIX0128`, `EPIX0129`, `EPIX0131`, `EPIX0134`, `EPIX0143`, `EPIX0009`, `EPIX0010`, `EPIX0041`, `EPIX0059`, `EPIX0008`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0017`, `EPIX0042`, `EPIX0018`, `EPIX0060`, `EPIX0075`, `EPIX0073`, `EPIX0030`, `EPIX0058`; events none listed.
- **`POST /pix/v1/pix/out/transfer`** (`post-pix-out-transfer`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `transaction_type`; response statuses 202, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0020`, `EPIX0032`, `EPIX0139`, `EPIX0132`, `EPIX0067`, `EPIX0126`, `EPIX0115`, `EPIX0226`, `EPIX0227`, `EPIX0228`, `EPIX0136`, `EPIX0022`, `EPIX0137`, `EPIX0138`, `EPIX0113`, `EPIX0123`, `EPIX0120`, `EPIX0124`, `EPIX0122`, `EPIX0141`, `EPIX0019`, `EPIX0008`, `EPIX0053`, `EPIX0003`, `EPIX0114`, `EPIX0061`, `EPIX0068`, `EPIX0130`, `EPIX0045`, `EPIX0110`, `EPIX0146`, `EPIX0160`, `EPIX0049`, `EPIX0009`, `EPIX0069`, `EPIX0010`, `EPIX0111`, `EPIX0112`, `EPIX0051`, `EPIX0041`, `EPIX0071`, `EPIX0142`, `EPIX0144`, `EPIX0085`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0042`, `EPIX0017`, `EPIX0108`, `EPIX0109`, `EPIX0014`, `EPIX0043`, `EPIX0089`, `EPIX0046`, `EPIX0070`, `EPIX0018`, `EPIX0051`, `EPIX0060`, `EPIX0030`, `EPIX0050`, `EPIX0058`; events `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`POST /pix/v2/pix/out/scheduler`** (`post-schedule-pix-payment`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `scheduler_details`; response statuses 201, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events `instantpay-scheduler-scheduler-status-change-1`, `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`POST /v1/pix/qrcode/cob`** (`post-create-cob`): security not declared; required parameters `Authorization` (header); required body fields `payee`, `payer`, `transaction_identification`, `initial_amount`; response statuses 202, 400, 401, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events none listed.
- **`POST /v1/pix/qrcode/cobv`** (`post-qrcode-cobv`): security not declared; required parameters `Authorization` (header); required body fields `charge`, `payee`, `payer`, `initial_amount`, `transaction_identification`; response statuses 202, 400, 401, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events none listed.
- **`POST /v1/pix/qrcode/recurrence`** (`post-create-recurrence`): security not declared; required parameters `Authorization` (header); required body fields `payee`, `transaction_identification`; response statuses 202, 400, 401, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events none listed.
- **`POST /v1/pix/qrcode/cob/recurrence`** (`post-create-recurrence-cob`): security not declared; required parameters `Authorization` (header); required body fields `payee`, `payer`, `initial_amount`, `transaction_identification`; response statuses 202, 400, 401, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events none listed.
- **`POST /v1/pix/qrcode/cobv/recurrence`** (`post-create-recurrence-cobv`): security not declared; required parameters `Authorization` (header); required body fields `charge`, `payee`, `payer`, `initial_amount`, `transaction_identification`; response statuses 202, 400, 401, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events none listed.
- **`POST /v1/pix/qrcode/static/recurrence`** (`post-create-static`): security not declared; required parameters `Authorization` (header); required body fields `payee`, `amount`, `transaction_identification`; response statuses 202, 400, 401, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-schedule-pix-payment` | `instantpay-scheduler-scheduler-status-change-1` |
| `post-pix-out-transfer` | `pix-financial-reconciliation-1` |
| `post-schedule-pix-payment` | `pix-financial-reconciliation-1` |
| `post-pix-out-transfer` | `pix-pix-in-1` |
| `post-schedule-pix-payment` | `pix-pix-in-1` |
| `post-pix-out-transfer` | `pix-pix-out-1` |
| `post-schedule-pix-payment` | `pix-pix-out-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/pix-and-qr-codes.md`: updatedAt 2026-05-11T21:53:41.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/pix-and-qr-codes.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pix-and-qr-codes | `baa3fa80fceebfbe…` | 2026-05-11T21:53:41.000Z |

## Related knowledge units

- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` — API reference: Instant payments - Pix payments — Scheduled transfers V2
- `KU-API-instant-payments-qr-code--qr-code` — API reference: Instant payments - QR Code — QR Code
- `KU-API-instant-payments-qr-code--recurring-payment` — API reference: Instant payments - QR Code — Recurring payment
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-PAY-pix-automatic` — Pix Automatic
