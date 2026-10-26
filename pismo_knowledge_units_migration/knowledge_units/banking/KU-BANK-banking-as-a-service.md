---
ku_id: KU-BANK-banking-as-a-service
title: Banking as a Service
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/banking-as-a-service.md
  sha256: a09ab2d58b9ce6840ba559b7d0ff977059e5cbe32f3530769d566e0e00ba325f
  url: https://developers.pismo.io/pismo-docs/docs/banking-as-a-service
  role: primary_guide
  updated_at: '2026-06-16T22:33:10.000Z'
operations:
- customerV2Post
- post-acquisitions-v3-s2s-applications
- post-create-cob
- post-credentials
- post-integrated-payments-api-v1-bankslips-cashout
- post-integrated-payments-api-v1-bankslips-pay
- post-payments-v1-payments
- post-pix-out-transfer
- post-qrcode-cobv
- post-v2-pix-keys-create
related_kus:
- KU-API-banking-authentication--provider-credentials
- KU-API-banking-integrated-payments--bank-slip
- KU-API-banking-integrated-payments--transfer
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--customers
- KU-API-core-platform-payment-methods--payments
- KU-API-instant-payments-pix-management--keys-part-01
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-qr-code--qr-code
- KU-CC-get-started-control-center
- KU-EVT-catalogue-account
- KU-EVT-catalogue-integrated
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-pix
- KU-GS-setup-overview
- KU-PAY-bank-slips
- KU-PAY-pix-instant-payments
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Banking as a Service

**KU ID:** `KU-BANK-banking-as-a-service` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/banking-as-a-service.md`:

> Banking as a Service (BaaS) is a business model where a bank or other financial institution provides banking services and infrastructure to non-financial client organizations (such as retailers and utility companies). BaaS enables you to embed financial products into your services without having to deal with the laws and regulations that would otherwise entail.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/banking-as-a-service.md`: Banking as a Service; Getting started; Step 1: Set up your org, programs, accounts, and customers; Step 2: Partner with a provider; Step 3: Register your provider relationship with Pismo; Step 4: Set up event notifications; Step 5: Use the Pismo API to complete your configuration; About KYC

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 10 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/banking-as-a-service.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/banking-as-a-service · updatedAt: 2026-06-16T22:33:10.000Z

<!-- source:begin path=docs/core-banking/banking-as-a-service.md part=0-end -->

# Banking as a Service

Banking as a Service (BaaS) is a business model where a bank or other financial institution provides banking services and infrastructure to non-financial client organizations (such as retailers and utility companies). BaaS enables you to embed financial products into your services without having to deal with the laws and regulations that would otherwise entail.

<Callout icon="🚧" theme="warn">
  Note that Pismo is not a licensed bank and does not directly implement a BaaS. Instead, it provides a cloud-based technology platform that enables its customers, in collaboration with Pismo’s BaaS partners, such as Celcoin, to offer banking services.
</Callout>

**With Pismo technology and a partnering BaaS provider, you can:**

* Set up your organization, programs, and customer accounts with Pismo.
* Implement [Pix instant payments](https://developers.pismo.io/pismo-docs/docs/pix-instant-payments) (Brazil only).
* Pay [bank slips](https://developers.pismo.io/pismo-docs/docs/bank-slips) (Brazil only). Bank slips are also known as *boletos* in Brazil.
* Execute [P2P](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) (Pismo account to Pismo account transactions).
* Perform [Cash-out transfers](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-cashout) to external accounts.
* Use other services depending on what your provider allows and supports.

**Pismo technology benefits include:**

* Easy regulatory compliance

* Account management, monitoring, and reporting

* Transaction validations, including anti-fraud checks and Know Your Customer (KYC).  For more information, refer to [About KYC](https://developers.pismo.io/pismo-docs/docs/banking-as-a-service#about-kyc).

# Getting started

To use a BaaS, follow these steps.

### Step 1: Set up your org, programs, accounts, and customers

Work with your Pismo representative to set up your organization. Once you do that, you can use the API to [Create accounts](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) and [Create customers](https://developers.pismo.io/pismo-docs/reference/customerv2post).

For more information, refer to [Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview). Also, check out [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) which enables you to do a lot of your setup through a convenient UI.

### Step 2: Partner with a provider

Set up a relationship with one of the payment service providers (PSP) that Pismo works with and that are licensed in their respective countries or regions to provide BaaS services. This includes Celcoin.

Your Pismo representative can help you get set up with a PSP.

### Step 3: Register your provider relationship with Pismo

Use the [Create provider credential](https://developers.pismo.io/pismo-docs/reference/post-credentials) endpoint to register your provider relationship with Pismo.

### Step 4: Set up event notifications

Set up [data and reporting](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview) to receive notifications (events) about Pismo account/customer setup and transaction success/failure.

### Step 5: Use the Pismo API to complete your configuration

Use the following endpoints with BaaS.

* [Banking authorization](https://developers.pismo.io/pismo-docs/reference/post-credentials): Register provider relationship with Pismo.
* [Pix payments](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer): Brazilian instant payment system
* [Pix management](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-keys-create): Manage Pix keys, claims, and infraction reports.
* [QR Code (dynamic)](https://developers.pismo.io/pismo-docs/reference/post-create-cob): Generate QR Codes for Pix.
* [BR Code](https://developers.pismo.io/pismo-docs/reference/post-qrcode-cobv): Generate BR Codes for Pix.
* [Integrated payments](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-pay): Bank slips (boletos)
* [Payments](https://developers.pismo.io/pismo-docs/reference/payments-1): P2P transactions

# About KYC

Know Your Customer (KYC) is a process that financial institutions and other businesses use to verify the identity of their customers. In the context of transactions, KYC is crucial for preventing fraud, money laundering, and other illicit activities.

The following is a brief overview of how KYC works in transactions.

1. **Documentation**: Customers are required to provide certain documents to establish their identity. This might include a government-issued photo identification (such as a driver's license or passport), proof of address (like a utility bill or bank statement), and, in some cases, additional information depending on the jurisdiction and the financial institution's requirements.

2. **Verification**: The financial institution verifies the submitted documents to ensure that they are legitimate and belong to the individual seeking the credit card.

3. **Customer information**: Financial institutions collect and maintain detailed information about their customers. This includes personal information, contact details, and transaction history. Keeping accurate and up-to-date records helps in monitoring and managing risks associated with credit card transactions.

4. **Risk assessment**: KYC is an essential component of risk management for financial institutions. By understanding their customers, institutions can assess the level of risk associated with each customer and transaction. Unusual or suspicious activity can be flagged for further investigation.

5. **Compliance with regulations**: KYC is often mandated by regulatory authorities to ensure that financial institutions are taking appropriate measures to combat fraud and money laundering. Institutions must adhere to specific guidelines and regulations set by the relevant authorities.

In credit card transactions, KYC helps protect both the customer and the financial institution. It minimizes the chances of identity theft, unauthorized transactions, and other fraudulent activities. It also plays a crucial role in regulatory compliance, promoting a more secure and transparent financial system.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /payments/v1/payments` | `post-payments-v1-payments` | Transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /v1/transfers/cashout` | `post-integrated-payments-api-v1-bankslips-cashout` | Perform cash-out | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--transfer |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /accounts/v2/customers` | `customerV2Post` | Create customer | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |
| `POST /banking-auth/v1/credentials` | `post-credentials` | Create provider credential | `api-specs/Banking_-_Authentication.yaml` | no | KU-API-banking-authentication--provider-credentials |
| `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | Pix-out transfer | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /v2/pix/keys` | `post-v2-pix-keys-create` | Create key entry | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--keys-part-01 |
| `POST /v1/pix/qrcode/cob` | `post-create-cob` | Create dynamic COB QR Code | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--qr-code |
| `POST /v1/pix/qrcode/cobv` | `post-qrcode-cobv` | Create dynamic COBV QR Code | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--qr-code |
| `POST /v1/bankslips/pay` | `post-integrated-payments-api-v1-bankslips-pay` | Pay bank slip | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip |

### Operation essentials

- **`POST /payments/v1/payments`** (`post-payments-v1-payments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `from`, `to`; response statuses 201, 202, 400, 409, 422, 500, 502; error codes in examples `WP2P0000`, `WP2P0019`, `EP2P9999`, `WP2P0005`, `WP2P0006`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WP2P0020`, `WP2P0013`, `WLDG0006`, `WP2P0010`, `WP2P0000`, `WP2P0000`, `ELDG500`, `EPCG501`, `EP2P9999`, `EP2P0001`, `EP2P0002`; events `authorization-authorization-event-1`.
- **`POST /v1/transfers/cashout`** (`post-integrated-payments-api-v1-bankslips-cashout`): security `BearerAuth`; required parameters `Authorization` (header), `x-idempotency-key` (header); required body fields `account_id`, `amount`, `processing_code`; response statuses 202, 400, 403, 409, 500, 502, 504; error codes in examples `EIP0003`, `EIP0008`, `EIP0010`, `EIP0012`, `EIP0013`, `EIP0016`, `EIP0017`, `EIP0020`, `EIP0005`, `EIP0006`, `EIP0009`, `EIP0029`, `EIP0030`, `EIP0031`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0011`, `EIP0015`, `EIP0019`, `EIP0022`, `EIP0028`, `EIP0053`, `EIP0069`, `EIP0070`, `EIP0018`, `EIP0021`, `EIP0024`, `EIP0002`; events `integrated-payments-financial-reconciliation-1`, `integrated-payments-transaction-status-change-1`, `integrated-payments-transfer-out-created-1`.
- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /accounts/v2/customers`** (`customerV2Post`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `entity`, `customer`; response statuses 201, 400, 409, 500; error codes in examples none; events `account-account-owner-change-1`, `account-customer-creation-1`.
- **`POST /banking-auth/v1/credentials`** (`post-credentials`): security `bearerAuth`; required parameters `account_token` (header); required body fields `key`, `provider`, `type`; response statuses 201, 400, 500, 502, 504; error codes in examples `EBAA0004`, `BA00005`, `EBAA0007`, `EPIX0005`, `EBAA0009`, `EBAA0010`, `EBAA0011`, `EBAA0012`, `EBAA0014`, `EBAA0002`, `EBAA0003`; events none listed.
- **`POST /pix/v1/pix/out/transfer`** (`post-pix-out-transfer`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `transaction_type`; response statuses 202, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0020`, `EPIX0032`, `EPIX0139`, `EPIX0132`, `EPIX0067`, `EPIX0126`, `EPIX0115`, `EPIX0226`, `EPIX0227`, `EPIX0228`, `EPIX0136`, `EPIX0022`, `EPIX0137`, `EPIX0138`, `EPIX0113`, `EPIX0123`, `EPIX0120`, `EPIX0124`, `EPIX0122`, `EPIX0141`, `EPIX0019`, `EPIX0008`, `EPIX0053`, `EPIX0003`, `EPIX0114`, `EPIX0061`, `EPIX0068`, `EPIX0130`, `EPIX0045`, `EPIX0110`, `EPIX0146`, `EPIX0160`, `EPIX0049`, `EPIX0009`, `EPIX0069`, `EPIX0010`, `EPIX0111`, `EPIX0112`, `EPIX0051`, `EPIX0041`, `EPIX0071`, `EPIX0142`, `EPIX0144`, `EPIX0085`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0042`, `EPIX0017`, `EPIX0108`, `EPIX0109`, `EPIX0014`, `EPIX0043`, `EPIX0089`, `EPIX0046`, `EPIX0070`, `EPIX0018`, `EPIX0051`, `EPIX0060`, `EPIX0030`, `EPIX0050`, `EPIX0058`; events `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`POST /v2/pix/keys`** (`post-v2-pix-keys-create`): security `BearerAuth`; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `key`, `key_type`, `reason`, `bank_account`; response statuses 201, 202, 400, 401, 403, 404, 409, 429, 500, 502, 503, 504; error codes in examples `EPDA0169`, `EPDA0002`, `EPDA0003`, `EPDA0038`, `EPDA0039`, `EPDA0040`, `EPDA0041`, `EPDA0042`, `EPDA0043`, `EPDG0001`, `EPDG0011`, `PBE353`, `EPDG0018`, `EPDG0019`, `EPDG0035`, `EPDG0036`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDA0023`, `EPDA0024`, `EPDG0014`, `PBE353`, `EPDA0025`, `EPDA0028`, `EPDA0029`, `EPDG0005`, `EPDG0006`, `EPDG0007`, `EPDG0010`, `EPDG0016`, `PBE315`, `EPDG0020`, `EPDG0017`, `EPDG0021`, `EPDA0000`, `EPDG0000`; events `pix-dict-key-status-change-1`.
- **`POST /v1/pix/qrcode/cob`** (`post-create-cob`): security not declared; required parameters `Authorization` (header); required body fields `payee`, `payer`, `transaction_identification`, `initial_amount`; response statuses 202, 400, 401, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events none listed.
- **`POST /v1/pix/qrcode/cobv`** (`post-qrcode-cobv`): security not declared; required parameters `Authorization` (header); required body fields `charge`, `payee`, `payer`, `initial_amount`, `transaction_identification`; response statuses 202, 400, 401, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events none listed.
- **`POST /v1/bankslips/pay`** (`post-integrated-payments-api-v1-bankslips-pay`): security `BearerAuth`; required parameters `Authorization` (header), `x-idempotency-key` (header); required body fields `account_id`, `amount`; response statuses 202, 400, 403, 404, 409, 500, 502, 504; error codes in examples `EIP0005`, `EIP0006`, `EIP0008`, `EIP0010`, `EIP0012`, `EIP0013`, `EIP0017`, `EIP0023`, `EIP0020`, `EIP0061`, `EIP0005`, `EIP0006`, `EIP0009`, `EIP0030`, `EIP0049`, `EIP0063`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0011`, `EIP0015`, `EIP0019`, `EIP0022`, `EIP0028`, `EIP0041`, `EIP0051`, `EIP0053`, `EIP0069`, `EIP0070`, `EIP0018`, `EIP0021`, `EIP0024`, `EIP0002`; events `authorization-authorization-event-1`, `integrated-payments-bankslip-status-change-1`, `integrated-payments-financial-reconciliation-1`.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `payments-1` | Payments | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `customerV2Post` | `account-account-owner-change-1` |
| `customerV2Post` | `account-customer-creation-1` |
| `post-integrated-payments-api-v1-bankslips-pay` | `authorization-authorization-event-1` |
| `post-payments-v1-payments` | `authorization-authorization-event-1` |
| `post-integrated-payments-api-v1-bankslips-pay` | `integrated-payments-bankslip-status-change-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-financial-reconciliation-1` |
| `post-integrated-payments-api-v1-bankslips-pay` | `integrated-payments-financial-reconciliation-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-transaction-status-change-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-transfer-out-created-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |
| `post-v2-pix-keys-create` | `pix-dict-key-status-change-1` |
| `post-pix-out-transfer` | `pix-financial-reconciliation-1` |
| `post-pix-out-transfer` | `pix-pix-in-1` |
| `post-pix-out-transfer` | `pix-pix-out-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/banking-as-a-service.md`: updatedAt 2026-06-16T22:33:10.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Operation link `payments-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/banking-as-a-service.md` | whole document | https://developers.pismo.io/pismo-docs/docs/banking-as-a-service | `a09ab2d58b9ce684…` | 2026-06-16T22:33:10.000Z |

## Related knowledge units

- `KU-API-banking-authentication--provider-credentials` — API reference: Banking - Authentication — Provider credentials
- `KU-API-banking-integrated-payments--bank-slip` — API reference: Banking - Integrated payments — Bank slip
- `KU-API-banking-integrated-payments--transfer` — API reference: Banking - Integrated payments — Transfer
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--customers` — API reference: Core platform - Accounts — Customers
- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-API-instant-payments-pix-management--keys-part-01` — API reference: Instant payments - Pix management — Keys (part 1 of 2)
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-qr-code--qr-code` — API reference: Instant payments - QR Code — QR Code
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-integrated` — Event catalogue: integrated
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-GS-setup-overview` — Core objects
- `KU-PAY-bank-slips` — Bank slips
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
