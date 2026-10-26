---
ku_id: KU-CARD-digital-wallets
title: Digital wallets, MDES Token Connect and Click to Pay
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/wallet-overview.md
  sha256: 7f446c0f9c55941420e51ded4c9c71b086cec775fd9d2a160739417e68376d8b
  url: https://developers.pismo.io/pismo-docs/docs/wallet-overview
  role: primary_guide
  updated_at: '2026-03-18T15:23:07.000Z'
- path: docs/card-issuing/mdes-token-connect.md
  sha256: a528d61f13f30c6ce7fd66848ccd22399530170e9626714b2ff9f17c073cd755
  url: https://developers.pismo.io/pismo-docs/docs/mdes-token-connect
  role: primary_guide
  updated_at: '2026-03-18T15:23:41.000Z'
- path: docs/card-issuing/click-to-pay.md
  sha256: cc0a528a36d6f1c8e702453e0b6296ced1844c4dbd43f044b2d85f8885f19111
  url: https://developers.pismo.io/pismo-docs/docs/click-to-pay
  role: primary_guide
  updated_at: '2026-05-11T19:40:52.000Z'
operations:
- post-v1-clicktopay-enroll_card
- post-v1-clicktopay-enroll_customer
related_kus:
- KU-API-card-issuing-tokenization--visa-click-to-pay
- KU-CARD-card-on-file-and-automatic-updater
- KU-CARD-card-tokenization-process-and-onboarding
- KU-EVT-catalogue-cards
grouping_rationale: Wallet overview stub and its features.
---

# Digital wallets, MDES Token Connect and Click to Pay

**KU ID:** `KU-CARD-digital-wallets` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Wallet overview stub and its features.

Scope as stated in `docs/card-issuing/wallet-overview.md`:

> A digital wallet, also known as an *e-wallet*, lets you replace card sensitive information with an encrypted digital token that can be used for payments and other card operations without exposing card data, such as the Card Verification Value (CVV) or Primary Account Number (PAN), which might happen with a physical card or digital transmission.

Scope as stated in `docs/card-issuing/mdes-token-connect.md`:

> MDES stands for <a href="https://developer.mastercard.com/product/mdes" target="_blank">Mastercard Digital Enablement Service</a>. Mastercard's Token Connect product is a framework within MDES that allows Issuers (card-issuing banks) to directly push a "tokenized" version of a customer's card (for example, their debit or credit card) to digital wallets, merchant platforms, or other ***token requestors*** . This method is often referred to as "issuer-initiated tokenization" or "push provisioning."

Scope as stated in `docs/card-issuing/click-to-pay.md`:

> Click to Pay is a secure, streamlined online checkout solution that makes e‑commerce as easy as tapping a card at point-of-sale devices. It is an implementation of the <a href="https://www.emvco.com/emv-technologies/secure-remote-commerce/" target="_blank">EMV Secure Remote Commerce (SRC)</a> standard—a universal “Click to Pay” button that supports Visa, Mastercard, AmEx, and Discover across participating websites .

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/wallet-overview.md`: Digital wallets
- `docs/card-issuing/mdes-token-connect.md`: MDES Token Connect [Beta]; How Token Connect works (high-level flow); Pismo's role; Key benefits
- `docs/card-issuing/click-to-pay.md`: Click to Pay; Click to Pay services Pismo supports; How it works for consumers; Benefits for consumers and merchants; Security and convenience; Using Pismo's Click to Pay API; Get authorized for Click to Pay; Key API endpoints and sample payloads; Enroll customer and card in Visa Click to Pay; Enroll card in Visa Click To Pay; Click to Pay event

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/wallet-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/wallet-overview · updatedAt: 2026-03-18T15:23:07.000Z

<!-- source:begin path=docs/card-issuing/wallet-overview.md part=0-end -->

# Digital wallets

A digital wallet, also known as an *e-wallet*, lets you replace card sensitive information with an encrypted digital token that can be used for payments and other card operations without exposing card data, such as the Card Verification Value (CVV) or Primary Account Number (PAN), which might happen with a physical card or digital transmission.

Pismo offers two tokenization solutions:

* [Third-party wallets](https://developers.pismo.io/pismo-docs/docs/card-tokenization-process-and-onboarding)—Card tokenization process and onboarding
* [Pismo card-on-file](https://developers.pismo.io/pismo-docs/docs/pismo-card-on-file)
<!-- source:end -->

### Source 2: `docs/card-issuing/mdes-token-connect.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/mdes-token-connect · updatedAt: 2026-03-18T15:23:41.000Z

<!-- source:begin path=docs/card-issuing/mdes-token-connect.md part=0-end -->

# MDES Token Connect [Beta]

MDES stands for <a href="https://developer.mastercard.com/product/mdes" target="_blank">Mastercard Digital Enablement Service</a>. Mastercard's Token Connect product is a framework within MDES that allows Issuers (card-issuing banks) to directly push a "tokenized" version of a customer's card (for example, their debit or credit card) to digital wallets, merchant platforms, or other ***token requestors*** . This method is often referred to as "issuer-initiated tokenization" or "push provisioning."

In short, instead of waiting for a merchant or wallet to request card information and tokenize it, the bank itself can—via MDES Token Connect—initiate the tokenization when the customer wants to add their card to a wallet or online store.

# How Token Connect works (high-level flow)

1. The cardholder logs into their bank’s app or online banking.
2. The bank shows a list of supported wallets or merchants.
3. The cardholder selects where to push their card and which account to tokenize.
4. The wallet or merchant authenticates the user and links the token.
5. Once approved, the tokenized card is ready for payments (tap-to-pay, online checkout, recurring billing, etc.).

Because the bank triggers the token creation, cardholders don’t need to manually type full card details into every site or app — the “token” acts as a stand-in.

# Pismo's role

Pismo acts as a **pass-though proxy** for MDES Token Connect. To make integration easier, Pismo's <a href="https://developers.pismo.io/pismo-docs/reference/token_connet_push_multiple_accounts">MDES Token Connect API</a> and endpoints mirror the MDES Token Connect API  and endpoints. For full technical details, refer to <a href="https://developer.mastercard.com/mdes-token-connect/documentation/#overview" target="_blank">Mastercard's Token Connect site</a> and documentation.

# Key benefits

* No need for customers to manually enter card details.
* Faster and more secure onboarding to wallets and merchants.
* Improved user experience and reduced friction.
<!-- source:end -->

### Source 3: `docs/card-issuing/click-to-pay.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/click-to-pay · updatedAt: 2026-05-11T19:40:52.000Z

<!-- source:begin path=docs/card-issuing/click-to-pay.md part=0-end -->

# Click to Pay

Click to Pay is a secure, streamlined online checkout solution that makes e‑commerce as easy as tapping a card at point-of-sale devices. It is an implementation of the <a href="https://www.emvco.com/emv-technologies/secure-remote-commerce/" target="_blank">EMV Secure Remote Commerce (SRC)</a> standard—a universal “Click to Pay” button that supports Visa, Mastercard, AmEx, and Discover across participating websites .

Click to Pay brings the contactless in-store experience online: faster, safer, password-free, and more secure. It's part of a broader industry shift toward a unified, tokenized, and frictionless approach to digital commerce across brands and devices.

The card networks support Click to Pay across major regions: North America, Europe, Asia-Pacific, Latin America, and Central and Eastern Europe, Middle East, and Africa (CEMEA).

## Click to Pay services Pismo supports

* Visa
* Mastercard (in development)
* Other card networks' Click to Pay services to be added in the future

# How it works for consumers

* Look for the Click to Pay icon (double right‑arrow) during checkout.
* Identify yourself using your email or phone number; a one‑time passcode (OTP) is sent for authentication.
* Select which of your enrolled cards to use and complete the purchase—no re‑typing necessary.

## Benefits for consumers and merchants

**For consumers**

* One-time enrollment, reusable tokens
* No need to re-enter 16-digit numbers
* Enhanced security via OTPs and tokens

**For merchants**

* Reduced cart abandonment and higher conversions
* Simpler integration thanks to EMV‑standard SDKs
* Lower fraud, fewer false declines, streamlined UX

## Security and convenience

* Uses tokenization, so merchants never see a consumer's actual card details .
* Fraud rates are significantly lower since real card numbers aren't shared.
* Checkout is faster (saves \~20 seconds) and authorization rates are often 4–10% higher.

# Using Pismo's Click to Pay API

The Pismo platform provides a full-featured [Click to Pay API](https://developers.pismo.io/pismo-docs/reference/post-v1-clicktopay-enroll_customer) .

## Get authorized for Click to Pay

Before using Pismo's API, an issuer needs to contact their card network and fulfill all necessary requirements to enroll customers in the Click to Pay service. Once authorized, you can use Pismo's API to start enrolling and managing your card customers.

## Key API endpoints and sample payloads

Shown here are Click to Pay enrollment endpoints and sample payloads. There are also get, update, and delete Click to Pay endpoints.

### Enroll customer and card in Visa Click to Pay

[Enroll customer and card in Visa CTP](https://developers.pismo.io/pismo-docs/reference/post-v1-clicktopay-enroll_customer) —Enroll a customer and card in Visa's Click to Pay service.

<details>
  <summary style={{ fontSize: "18px" }}><b>Sample payload</b></summary>

  ```json
  curl -X POST "https://gw-pci.pismolabs.io/cards-tokenization/v1/clicktopay/visa/enroll/customer" \
  -H "Authorization: Bearer <your_bearer_token>" \
  -H "Content-Type: application/json" \
  -H "x-tenant: YOUR_TENANT_ID" \
  -H "x-customer-id: YOUR_CUSTOMER_ID" \
  -H "x-cid: YOUR_CORRELATION_ID" \
  -d '{
    "owner_bid": "1000052",
    "card_information": {
      "card_id": 6743052,
      "billing_address": {
        "city": "San Francisco",
        "state": "CA",
        "postal_code": "94105",
        "country_code": "USA",
        "address_line1": "1000 Market Street",
        "address_line2": "Building 56",
        "address_line3": "Suite 101"
      }
    },
    "customer_information": {
      "first_name": "Alex",
      "last_name": "Miller",
      "emails": ["anita_drink@provider.com"],
      "phones": ["+55 (45) 99999-9999"],
      "locale": "en-US",
      "national_identifiers": [{
        "type": "NATIONAL_IDENTITY",
        "value": "A123456"
      }],
      "consent": {
        "time_of_consent": "2020-05-05T12:12:12.000Z",
        "version": "1.0",
        "presenter": "Acme Bank"
      }
    }
  }'
  ```
</details>

### Enroll card in Visa Click To Pay

[Enroll card in Visa CTP](https://developers.pismo.io/pismo-docs/reference/post-v1-clicktopay-enroll_card) —Enroll a customer card in Visa's Click to Pay service.

<details>
  <summary style={{ fontSize: "18px" }}><b>Sample payload</b></summary>

  ```json
  curl -X POST https://gw-pci.pismolabs.io/cards-tokenization/v1/clicktopay/visa/enroll/card \
  -H "Authorization: Bearer <your_bearer_token>" \
  -H "Content-Type: application/json" \
  -H "x-tenant: YOUR_TENANT_ID" \
  -H "x-customer-id: YOUR_CUSTOMER_ID" \
  -H "x-cid: YOUR_CORRELATION_ID" \
  -d '{
    "card_id": 6743052,
    "owner_bid": "1000052",
    "billing_address": {
      "city": "San Francisco",
      "state": "CA",
      "postal_code": "94105",
      "country_code": "USA",
      "address_line1": "1000 Market Street",
      "address_line2": "Building 56",
      "address_line3": "Suite 101"
    }
  }'
  ```

  <br />
</details>

## Click to Pay event

All non-GET Click to Pay endpoints generate a [Click to Pay event generated](https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1)  event.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/clicktopay/visa/enroll/customer` | `post-v1-clicktopay-enroll_customer` | Enroll customer and card in Visa CTP | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--visa-click-to-pay |
| `POST /v1/clicktopay/visa/enroll/card` | `post-v1-clicktopay-enroll_card` | Enroll card in Visa CTP | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--visa-click-to-pay |

### Operation essentials

- **`POST /v1/clicktopay/visa/enroll/customer`** (`post-v1-clicktopay-enroll_customer`): security `BearerAuth`; required parameters `x-tenant` (header), `x-customer-id` (header); required body fields `owner_bid`, `card_information`, `customer_information`; response statuses 202, 400, 429, 500; error codes in examples none; events `cards-tokenization-click-to-pay-1`.
- **`POST /v1/clicktopay/visa/enroll/card`** (`post-v1-clicktopay-enroll_card`): security `BearerAuth`; required parameters `x-tenant` (header), `x-customer-id` (header); required body fields `owner_bid`, `card_id`; response statuses 202, 400, 429, 500; error codes in examples none; events `cards-tokenization-click-to-pay-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-clicktopay-enroll_card` | `cards-tokenization-click-to-pay-1` |
| `post-v1-clicktopay-enroll_customer` | `cards-tokenization-click-to-pay-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `cards-tokenization-click-to-pay-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1 | 6 | KU-EVT-catalogue-cards |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/wallet-overview.md`: updatedAt 2026-03-18T15:23:07.000Z.
- `docs/card-issuing/mdes-token-connect.md`: updatedAt 2026-03-18T15:23:41.000Z.
- `docs/card-issuing/click-to-pay.md`: updatedAt 2026-05-11T19:40:52.000Z.
- The source title marks the feature as beta: "MDES Token Connect [Beta]".

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/wallet-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/wallet-overview | `7f446c0f9c559414…` | 2026-03-18T15:23:07.000Z |
| `docs/card-issuing/mdes-token-connect.md` | whole document | https://developers.pismo.io/pismo-docs/docs/mdes-token-connect | `a528d61f13f30c6c…` | 2026-03-18T15:23:41.000Z |
| `docs/card-issuing/click-to-pay.md` | whole document | https://developers.pismo.io/pismo-docs/docs/click-to-pay | `cc0a528a36d6f1c8…` | 2026-05-11T19:40:52.000Z |

## Related knowledge units

- `KU-API-card-issuing-tokenization--visa-click-to-pay` — API reference: Card issuing - Tokenization — Visa Click to Pay
- `KU-CARD-card-on-file-and-automatic-updater` — Card-on-file and automatic updater
- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-EVT-catalogue-cards` — Event catalogue: cards
