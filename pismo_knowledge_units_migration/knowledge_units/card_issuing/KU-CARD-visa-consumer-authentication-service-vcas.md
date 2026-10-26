---
ku_id: KU-CARD-visa-consumer-authentication-service-vcas
title: Visa Consumer Authentication Service (VCAS)
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/visa-consumer-authentication-service-vcas.md
  sha256: 39eb4e90362c0d2f787779fd9f9efd3fb4992dc8cc484f36ec4bf113d888a882
  url: https://developers.pismo.io/pismo-docs/docs/visa-consumer-authentication-service-vcas
  role: primary_guide
  updated_at: '2026-06-22T20:44:58.000Z'
operations: []
related_kus:
- KU-EVT-vcas-client-webhooks
grouping_rationale: single source page
---

# Visa Consumer Authentication Service (VCAS)

**KU ID:** `KU-CARD-visa-consumer-authentication-service-vcas` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/visa-consumer-authentication-service-vcas.md`:

> Visa Consumer Authentication Service (VCAS) is  a service that verifies cardholder identity during online transactions—especially important for card-not-present purchases like those made on e-commerce websites.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/visa-consumer-authentication-service-vcas.md`: Visa Consumer Authentication Service (VCAS); Issuer webhooks; VCAS use cases; Use case #1; Use case #2; Use case #3

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/visa-consumer-authentication-service-vcas.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/visa-consumer-authentication-service-vcas · updatedAt: 2026-06-22T20:44:58.000Z

<!-- source:begin path=docs/card-issuing/visa-consumer-authentication-service-vcas.md part=0-end -->

# Visa Consumer Authentication Service (VCAS)

Visa Consumer Authentication Service (VCAS) is  a service that verifies cardholder identity during online transactions—especially important for card-not-present purchases like those made on e-commerce websites.

VCAS is Visa’s EMV® 3-D Secure protocol (also known as 3DS 2.x) implementation. (Note: EMV® is a registered trademark of EMVCo, LLC, representing the global specifications used for secure payment technologies, including EMV® 3‑D Secure).

Its primary goals are to:

* Reduce fraud
* Ensure regulatory compliance
* Improve the user's authentication experience

Pismo supports Real Time Data Exchange (RDX) APIs to integrate into VCAS to help with transaction authentication decisions and provides a 3DS authentication service to clients based on a referral model. RDX allows the issuer to decide how much they would like to be involved in the transaction process by sharing data between VCAS and the issuer or issuer’s processor. This solution initially includes EMV 3DS and Visa network transactions.

Frictionless transactions require no user verification while friction transactions do require this. In this solution, PISMO in VCAS will provide three specific working flows with StepUp OTP for friction transactions and out-of-band (OOB) authentication, enabling VCAS configuration to support two use cases for the OTP challenge flow (e-mail and SMS), and additionally, having an in-app authentication (OOB) for Pismo’s customer banks.

# Issuer webhooks

You, as the issuer, need to code the webhooks to implement Pismo's VCAS solution. These webhooks are detailed in Pismo's [Client webhooks for VCAS](https://developers.pismo.io/pismo-docs/docs/vcas-client-webhooks) guide:

* **StepUp**—Get authentication method/delivery channel and display text. For more information, refer to [Stepup call](https://vcasdocs.cardinalcommerce.com/rdx/docs/getting-started-with-rdx#stepup-call)  in the Getting Started with RDX guide.
* **Initiate Action**—Request One-Time Passcode (OTP) action. For more information, refer to [Initiate Action call](https://vcasdocs.cardinalcommerce.com/rdx/docs/getting-started-with-rdx#initiate-action-call)  in the Getting Started with RDX guide.
* **Validate**—Validate entered OTP verification code. For more information, refer to [Validate call](https://vcasdocs.cardinalcommerce.com/rdx/docs/getting-started-with-rdx#validate-call)  in the Getting Started with RDX guide.

<Callout icon="📘" theme="info">
  - PISMO will use RDX integration to communicate the StepUp method.
  - Pismo does not share Payment Card Industry Data Security Standard (PCI-DSS) data.
  - Pismo provides the encrypt/decrypt keys for the hashed PAN.
</Callout>

# VCAS use cases

There are three main use cases for handling calls to VCAS with a StepUp request via OTP.

1. VCAS generates, delivers, and validates the StepUp.
2. Issuer generates, delivers, and validates the StepUp.
3. VCAS generates, issuer delivers, and VCAS validates the StepUp.

## Use case #1

<Image align="center" alt="A graphic showing the use case where VCAS generates, delivers, and validates the OTP" src="https://files.readme.io/caf253c63beeab57a2dad4336eca997677e7c2545a72cc6a17ffba29b4ddf778-Use_Case_1__OTP_Flow-Final.png" />

\*You can use the Pismo static decision module

In this case, VCAS generates, delivers, and validates the StepUp In the sample steps below, the issuer does not implement the **Initiate Action** webhook.

1. E-commerce site calls VCAS with OTP request.
2. VCAS calls Pismo with OTP request and PAN
3. Pismo calls issuer's **StepUp webhook** .
4. Issuer responds with OTP delivery channel (SMS or email) and informational texts.
5. Pismo sends issuer's response to VCAS.
6. VCAS generates OTP verification code.
7. VCAS notifies ecommerce site of  delivery channel.
8. E-commerce site prompts cardholder for OTP verification code.
9. VCAS sends verification code to cardholder via delivery channel.
10. Cardholder enters OTP verification code at e-commerce site.
11. E-commerce site sends entered OTP verification code to VCAS for validation.
12. VCAS validates OTP verification code and sends result to e-commerce site.

## Use case #2

<Image align="center" alt="A graphic showing the use case where the issuer generates, delivers, and validates the OTP." src="https://files.readme.io/c5e70989ff9059cfb8137a8c83406203517c103494311d856aeab6da4d80954d-Use_Case_2__OTP_Flow-Final.png" />

\*You can use the Pismo static decision module

In this case, the issuer generates, delivers, and validates the OTP. In the example steps below, the issuer implements **Initiate Action** and **Validate** webhooks.

1. E-commerce site calls VCAS with OTP request.
2. VCAS calls Pismo with OTP request.
3. Pismo calls issuer's **StepUp webhook**.
4. Issuer responds with delivery channel (SMS or email) and informational texts.
5. Pismo sends issuer's response to VCAS.
6. VCAS notifies e-commerce site of delivery channel.
7. E-commerce site prompts cardholder for verification code.
8. VCAS calls Pismo to initiate action.
9. Pismo calls issuer's **Initiate Action webhook**.
10. Issuer generates verification code.
11. Issuer sends verification code to cardholder via delivery channel.
12. Cardholder inputs verification code at e-commerce site.
13. E-commerce site calls VCAS to validate entered verification code.
14. VCAS calls Pismo to validate entered verification code.
15. Pismo calls issuer's **Validate webhook**.
16. Issuer responds with validation result.
17. Pismo sends validation result to VCAS.
18. VCAS sends validation result to e-commerce site.

## Use case #3

<Image align="center" alt="A graphic showing the use case where VCAS generates, issuer delivers, and VCAS validates the OTP." src="https://files.readme.io/40590bea1a39b13389064eabd2812a6e40a8b63b4823a165e9c33c65c9005d59-Use_Case_3__OOB_Flow-Final.png" />

\*You can use the Pismo static decision module

In this case, VCAS generates, issuer delivers, and VCAS validates the OTP. In the example steps below, the issuer  implements the **Initiate Action** webhook.

Here, Pismo receives the request from VCAS and engages with the issuer to initiate the\
OOB process. This use case requires integration between Pismo and the issuer bank, outside of\
VCAS solution scope.

1. E-commerce site calls VCAS with OTP request.
2. VCAS calls Pismo with OTP request.
3. Pismo calls issuer's **StepUp webhook**.
4. Issuer responds with delivery channel (SMS or email)  and informational texts.
5. Pismo sends issuer's response to VCAS.
6. VCAS generates OTP verification code.
7. VCAS calls e-commerce site to notify user of delivery channel.
8. E-commerce site prompts user for verification code.
9. VCAS calls Pismo to initiate action.
10. Pismo calls Issuer's **Initiate Action webhook**.
11. Issuer sends verification code to cardholder via delivery channel
12. Cardholder enters verification code.
13. E-commerce site sends entered verification code to VCAS for validation.
14. VCAS validates entered verification code and sends result to e-commerce site.
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/visa-consumer-authentication-service-vcas.md`: updatedAt 2026-06-22T20:44:58.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/visa-consumer-authentication-service-vcas.md` | whole document | https://developers.pismo.io/pismo-docs/docs/visa-consumer-authentication-service-vcas | `39eb4e90362c0d2f…` | 2026-06-22T20:44:58.000Z |

## Related knowledge units

- `KU-EVT-vcas-client-webhooks` — Client webhooks for VCAS
