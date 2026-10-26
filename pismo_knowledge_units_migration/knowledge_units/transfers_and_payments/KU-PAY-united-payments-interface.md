---
ku_id: KU-PAY-united-payments-interface
title: RuPay and UPI instant payments (India)
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/united-payments-interface.md
  sha256: 9642ee6db4eb8643a588339feff7bc907a46b7dfc439b976d4431c2b473b91e4
  url: https://developers.pismo.io/pismo-docs/docs/united-payments-interface
  role: primary_guide
  updated_at: '2026-04-28T18:30:05.000Z'
operations:
- post-card-bill
- post-funds-transfer
related_kus:
- KU-API-instant-payments-rupay-on-upi--upi
- KU-AUTH-authentication-methods
- KU-AUTH-identity-connectivity-with-mtls
- KU-EVT-catalogue-other-domains
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
grouping_rationale: single source page
---

# RuPay and UPI instant payments (India)

**KU ID:** `KU-PAY-united-payments-interface` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/united-payments-interface.md`:

> Customers with RuPay cards that are UPI-enabled (linked to a UPI app), can make payments and transfers directly from their card to merchants and have their credit card accounts debited in real-time.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/united-payments-interface.md`: RuPay and UPI instant payments (India); Connecting with the Pismo platform; Configure signed certificate for mTLS; Testing and production domains; UPI processing codes; Anti-fraud webhook for UPI transactions; Sample RuPay UPI Transfer funds endpoint request

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/united-payments-interface.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/united-payments-interface · updatedAt: 2026-04-28T18:30:05.000Z

<!-- source:begin path=docs/core-banking/united-payments-interface.md part=0-end -->

# RuPay and UPI instant payments (India)

<a href="https://www.rupay.co.in/rupay-credit-card-on-upi" target="_blank">RuPay</a> (derived from the words "rupee" and "payment") is a  National Payments Corporation of India (NPCI)-created Indian domestic card network.  NPCI also developed the  <a href="https://www.npci.org.in/what-we-do/upi/product-overview" target="_blank">United Payments Interface (UPI)</a>, a real-time payment system for processing inter-bank transactions. RuPay credit card on UPI was launched at the Global Fintech Fest on 20th September 2022.

Customers with RuPay cards that are UPI-enabled (linked to a UPI app), can make payments and transfers directly from their card to merchants and have their credit card accounts debited in real-time.

The Pismo platform supports RuPay-UPI integration. Clients can use Pismo endpoints for transactional flows ([Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-funds-transfer)), plus the onboarding and account lifecycle processes for establishing and managing UPI user accounts.

With the acceptance of credit cards using QR codes, customers have additional opportunity and ease in using their credit cards and merchants benefit from the increased consumption.

To further enrich offerings to customers and merchants, new features are being introduced as part of RuPay credit card on UPI Phase 2. For example:  credit card bill payment, Equated Monthly Installment, and BIN management.

> 📘 Newest API endpoint - Get card bill
>
> Pismo recently added a new API endpoint - [Get card bill](https://developers.pismo.io/pismo-docs/reference/post-card-bill)  - that lets you get a credit card statement based on account reference number and mobile phone.

# Connecting with the Pismo platform

You need to use mTLS to connect with the Pismo plaform. For more information, refer to [Identity connectivity with mTLS](https://developers.pismo.io/pismo-docs/docs/identity-connectivity-with-mtls)

mTLS is **mandatory** for all API calls to the Pismo platform. This protocol keeps the platform in compliance with legal requirements. To configure mTLS, contact your Pismo representative.

## Configure signed certificate for mTLS

There are three ways to configure the signed certificate:

* Pismo generates and signs a private and public key and sends the public key to you through a secure channel.
* You generate a private and public key and send the public key to Pismo through a Certificate Signing Request (CSR). Pismo sends back a signed public certificate.
* You generate your own public certificate and sign it with your own CA. You provide the signed certificate to Pismo for upload to Cloudflare.

## Testing and production domains

mTLS domains to access Pismo UPI API:

* UAT - `https://api-sandbox-cdn.pismolabs.io`
* Production - `https://prod-cdn.ind.pismo.io`

The Sandbox domain to access the API via Postman is `https://api-sandbox.pismolabs.io`

**Notes:**

* For every API endpoint call, a valid auth token has to be passed in a header. You **must** use Pismo's [OpenID Authentication](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid) .
* You need to generate private and public keys, share the public key with Pismo and, in turn, Pismo shares the organization details you can use to generate the JWT signed with the private key. Using the JWT, the auth token can be generated from Pismo using the [Passport API endpoint](https://developers.pismo.io/pismo-docs/reference/post-passport-v1-oauth2-token-1)

# UPI processing codes

| Operation name   | Payment PC | Refund PC | Refund cancellation PC |
| :--------------- | :--------- | :-------- | :--------------------- |
| DEBIT UPI RUPAY  | 320200     | 320201    | 320202                 |
| CREDIT UPI RUPAY | 320203     | 320204    | 320205                 |

# Anti-fraud webhook for UPI transactions

You have the option to implement an [anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#full-balance-anti-fraud--webhook)  for UPI transactions to supplement the anti-fraud checking and validation Pismo does.

# Sample RuPay UPI Transfer funds endpoint request

```json
curl --request POST \
     --url https://sandbox.pismolabs.io/upi-gateway/v1/cards/transfer \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "amount": 500,
  "currency": "INR",
  "account_reference_number": "12345600000000001140340134",
  "external_transaction_datetime": "2020-09-15T19:39:54.013Z",
  "external_transaction_id": "MGS584A1244F6BC4D50A3FABE6D93DF913C",
  "mcc": "6012",
  "merchant_name": "Cafe Coffee Day",
  "phone_number": "919846049491",
  "transaction_reference": "Lunch",
  "transaction_type": "C",
  "upi_reference_number": "123412341234",
  "credit_account_number": "98765004371"
}
'
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/cards/transfer` | `post-funds-transfer` | Transfer UPI funds | `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` | no | KU-API-instant-payments-rupay-on-upi--upi |
| `POST /v1/cards/credit-card-bill` | `post-card-bill` | Get card bill | `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` | no | KU-API-instant-payments-rupay-on-upi--upi |

### Operation essentials

- **`POST /v1/cards/transfer`** (`post-funds-transfer`): security `BearerAuth`; required parameters `Authorization` (header), `user-agent` (header); required body fields `amount`, `currency`, `account_reference_number`, `external_transaction_datetime`, `external_transaction_id`, `mcc`, `merchant_name`, `phone`, `transaction_type`, `upi_reference_number`; response statuses 201, 202, 400, 401, 403, 404, 408, 409, 500, 502; error codes in examples `EUPI0002`, `EUPI0003`, `EUPI0104`, `EUPI0101`, `EUPI0108`, `EUPI0120`, `EUPI0004`, `EUPI0110`, `EUPI0020`, `EUPI0100`, `EUPI0112`, `EUPI0113`, `EUPI0114`, `EUPI0121`, `EUPI0001`, `EUPI0105`, `EUPI0106`, `EUPI0109`; events `payment-methods-authorization-1`, `platform-authorization-platform-authorization-1`.
- **`POST /v1/cards/credit-card-bill`** (`post-card-bill`): security `BearerAuth`; required parameters `Authorization` (header), `user-agent` (header); required body fields `card_info`, `phone`; response statuses 200, 400, 403, 404, 422, 500; error codes in examples `EUPI0003`, `EUPI0023`, `EUPI0002`, `EUPI0004`, `EUPI0028`, `EUPI0032`, `EUPI0007`, `EUPI0042`, `EUPI0001`; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `post-passport-v1-oauth2-token-1` | Get OpenID access token; Passport API endpoint | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-funds-transfer` | `payment-methods-authorization-1` |
| `post-funds-transfer` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/united-payments-interface.md`: updatedAt 2026-04-28T18:30:05.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Operation link `post-passport-v1-oauth2-token-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/united-payments-interface.md` | whole document | https://developers.pismo.io/pismo-docs/docs/united-payments-interface | `9642ee6db4eb8643…` | 2026-04-28T18:30:05.000Z |

## Related knowledge units

- `KU-API-instant-payments-rupay-on-upi--upi` — API reference: Instant payments - RuPay on UPI — UPI
- `KU-AUTH-authentication-methods` — API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys
- `KU-AUTH-identity-connectivity-with-mtls` — Identity connectivity with mTLS
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
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
