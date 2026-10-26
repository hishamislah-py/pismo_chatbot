---
ku_id: KU-CARD-card-network-mandates
title: Card network mandates
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/card-network-mandates.md
  sha256: 60122ee682af10a111fc052fed4fb1754f5bc0343a6d842bc3469eb373bdbc42
  url: https://developers.pismo.io/pismo-docs/docs/card-network-mandates
  role: primary_guide
  updated_at: '2026-03-18T15:20:02.000Z'
operations: []
related_kus:
- KU-CARD-digital-wallets
- KU-PAY-pix-instant-payments
grouping_rationale: single source page
---

# Card network mandates

**KU ID:** `KU-CARD-card-network-mandates` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/card-network-mandates.md`:

> Payment card networks like Visa, Mastercard, Elo, and RuPay have ***mandates*** — rules, requirements, and deadlines that govern how banks, merchants, processors, and service providers must operate in their payment ecosystems.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/card-network-mandates.md`: Card network mandates; Card network mandate categories; Security and  fraud prevention; Authentication; Transaction routing and processing; Dispute and chargeback handling; Technology modernization; Geographic or regional mandates; Why mandates matter; Pismo and mandates FAQ; What are Pismo’s responsibilities for Zero/Full balance mandate compliance?; How does Pismo stay updated on card network mandates?; How does Pismo evaluate and prioritize new mandates? Does Pismo implement only mandatory ones, or also the optional ones?; Does Pismo have a dedicated team or process for tracking and implementing mandates?; Real mandate examples; Key active mandates

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/card-network-mandates.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/card-network-mandates · updatedAt: 2026-03-18T15:20:02.000Z

<!-- source:begin path=docs/card-issuing/card-network-mandates.md part=0-end -->

# Card network mandates

Payment card networks like Visa, Mastercard, Elo, and RuPay have ***mandates*** — rules, requirements, and deadlines that govern how banks, merchants, processors, and service providers must operate in their payment ecosystems.

These mandates cover security, technology upgrades, compliance, data handling, and fraud prevention — and are usually required if you want to remain in good standing with the network.

**Card network mandates apply to:**

* Issuers (banks that issue cards)
* Acquirers (merchant banks)
* Merchants (retailers, e-commerce platforms)
* Payment processors and gateways
* Third-party service providers
* ATM operators and fintechs (Pismo)

# Card network mandate categories

Here are the most common mandate categories.

## Security and  fraud prevention

* **EMV chip adoption**—Mandates the move from magstripe to <a href="https://en.wikipedia.org/wiki/EMV" target="_blank">Europay, Mastercard and Visa </a> (EMV) chip cards to reduce counterfeit fraud.
* **<a href="https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard" target="_blank">Payment Card Industry Data Security Standard</a> (PCI DSS) compliance**—Mandates secure storage and handling of cardholder data.
* **Tokenization**—Requirements for replacing Primary Account Numbers (PAN)s with tokens in mobile wallets (like Apple Pay, Google Pay).
* **3D Secure (3DS 2.x)**—Mandates support for advanced cardholder authentication.
* **Real-time fraud monitoring**— Requirements to have systems that can detect and stop fraud instantly.

## Authentication

* **Strong customer authentication (SCA)** (in Europe)—<a href="https://www.ecb.europa.eu/press/intro/mip-online/2018/html/1803_revisedpsd.en.html" target="_blank">Payment Services Directive</a> (PSD2) mandated, but enforced via Visa/Mastercard mandates.
* **3DS 2.2+ mandate deadlines**—Card networks have set deadlines for issuers/acquirers to support 3DS 2.2 and 2.3 for frictionless and biometric flows.

## Transaction routing and processing

* **Contactless routing rules**—Require support for dual-network contactless cards (e.g., Visa and local network).
* **Debit routing mandates** (e.g., in US)—Require merchants to support routing debit transactions over multiple networks to increase competition and reduce fees.
* **Real-time clearing**—Mandates for faster or same-day settlement in certain markets.

## Dispute and chargeback handling

* **Compelling evidence rules (Visa CE 3.0)**—New requirements for merchants to provide specific data in fraud-related disputes.
* **Shorter response timelines**—Mandated shorter windows to respond to chargebacks or disputes.

## Technology modernization

* **BIN expansion**—Transition from 6-digit to 8-digit BINs (Visa and Mastercard mandates).
* **Account updater mandates**—Require issuers to support services that keep stored credentials up to date (for subscriptions, recurring payments).
* **Support for digital wallets and Click to Pay**—Card networks are increasingly requiring or promoting support for [Click to Pay](https://developers.pismo.io/pismo-docs/docs/click-to-pay) and mobile wallets.

## Geographic or regional mandates

Networks issue mandates that apply specifically to:

* Europe (PSD2, SCA)
* India (Tokenization, Reserve Bank of India (RBI) rules)
* Brazil ([Pix](https://developers.pismo.io/pismo-docs/docs/pix-instant-payments) , local acquirer mandates)
* US  (<a href="https://www.investopedia.com/terms/d/durbin-amendment.asp" target="_blank">Durbin Amendment</a> compliance, contactless routing)

# Why mandates matter

* **Compliance**—Required to avoid fees, fines, or being cut off from the network.
* **Security**—Help reduce fraud (e.g., EMV cut down counterfeit fraud dramatically).
* **Authentication**—Mandates (like 3DS) improve liability shift and reduce chargebacks.
* **Processing**— Modernize and unify the payments infrastructure globally.
* **Consumer protection**— Prevent fraud and ensure secure, seamless transactions.
* **Innovation enablement**—Help the ecosystem adopt new tech (e.g., biometrics, tokenization).
* **Fair competition**—Encourage network neutrality and support for domestic schemes in emerging markets.
* **Operational standardization**—Ensures consistency across thousands of issuers, acquirers, and merchants.

# Pismo and mandates FAQ

### What are Pismo’s responsibilities for Zero/Full balance mandate compliance?

Pismo has a commitment to implement all new changes for all regions and platform models. Our implementation covers all card network announced requirements.

**Full balance clients**—Pismo assumes complete responsibility for complying with card network mandates. Pismo handles any network-required changes or updates.

**Zero balance clients**—Pismo only intermediates the authorization process. The client, therefore, is responsible  for monitoring, evaluating, and implementing card-network mandated changes. Zero balance clients must ensure their systems are prepared to comply with any updates that affect the network authorization flow.

### How does Pismo stay updated on card network mandates?

Pismo is notified from a subscribed list about any new card network mandate changes. We also regularly check  all card network portal web pages that list all documentation including the Manual, release changes, maintenance dates, and so on.

### How does Pismo evaluate and prioritize new mandates? Does Pismo implement only mandatory ones, or also the optional ones?

Pismo has three release types:

* Mandatory
* Conditional
* Optional

Pismo implements all mandatory ones and conditionals when the customer has the product.

In case the customer wants to implement a change that we are not covering, they need to contact the **Customer Success** team and open a project requesting that our team analyze and see if we can implement  it according to customer requirements. Once this is implemented for the customer,  Pismo then implements it for the whole platform.

### Does Pismo have a dedicated team or process for tracking and implementing mandates?

Yes, Pismo has a **Network Brands** team responsible for analyzing all new mandates and release announcements and their impact on customer business. Once the team decides what to implement, they communicate to the internal developer teams about what needs to be done.

# Real mandate examples

| Card            | Network                                                | Mandate deadline  |
| :-------------- | :----------------------------------------------------- | :---------------- |
| Visa            | Visa	3DS 2.2 Support for Issuers                       | Oct 2022          |
|                 | Visa	CE 3.0 (Compelling evidence in disputes)          | Apr 2022          |
| Mastercard      | Mastercard	8-digit BIN support                         | Apr 2022          |
|                 | Contactless EMV support for US merchants               | 2023+             |
| Visa/Mastercard | Support for tokenization in stored credentials         | Rolling deadlines |
| RuPay           | Mandatory network choice at issuance                   | Sept/Oct 2024     |
|                 | Rewards parity on UPI vs. card payments                | Sept 1, 2024      |
| Elo             | Fraud control and anti-money laundering (AM) reporting | Ongoing           |
|                 | Tokenization and EVC dynamic CVV rollout               | 2024–2025         |

# Key active mandates

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>Visa</summary>

  Visa key active mandates - effective April–June 2025:

  * **Compelling Evidence 3.0 (CE 3.0)**—Merchants must now provide specific evidence—such as prior genuine transactions—to counter friendly‑fraud disputes like reason code 10.4. This expanded evidence policy becomes mandatory in pre‑dispute and arbitration environments.
  * **Visa Acquirer Monitoring Program (VAMP)**—Acquirer metrics are evaluated monthly without grace periods. Dispute resolutions must occur within the same month to avoid counting against ratios, calculated at the merchant descriptor level.
  * **Visa Token Service Updates (April 11 and 12, 2025)**—Changes include support for Token User Identifiers, expanded device binding via FIDO, Digital Currency/NFT transaction exports, a new Merchant Initiated Account Funding Transaction (AFT) tag, and enhanced third‑party data sharing for card-not-present (CNP) transactions.
  * **ATM Service Requirements (effective October 1, 2025)**—U.S.-based ATM issuers must support functions including mini‑statements, deposits, and PIN management services.
</details>

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>Mastercard</summary>

  Mastercard key active mandates - effective 2025.

  * **Fee on undefined authorizations**—Effective July 1, 2025, a processing integrity fee of 0.25% (or minimum $0.04) will be applied in the U.S. on transactions using legacy “undefined” authorization types.
  * **Credential continuity Program (CCP) fee increase**—As of April 1, 2025, Mastercard acquirers in the U.S. will incur a $0.09 fee per recurring transaction using outdated credentials (up from $0.03).
  * **Biometric EMV card rollout**—Mastercard is now mandating support for biometric-enabled cards that incorporate fingerprint sensors at the card level, rolled out globally—including bank‑issued cards in Bangladesh, South Korea, etc.—supported by standard EMV terminals and no new infrastructure.
</details>

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>RuPay</summary>

  * **Choice of card network (RBI directive)**—Effective from September 6, 2024 (some sources cite October 2024 implementation). Banks and card issuers with over 1 million (10 lakh) active cards must offer consumers a choice of card network at the time of credit card issuance or renewal — Visa, Mastercard, or RuPay (National Herald, NDTV Profit).  Enhances consumer flexibility and supports RuPay’s domestic growth. Smaller issuers (\<1M cards) and those with proprietary networks (e.g., AmEx) are exempt.
  * **Parity of rewards on RuPay UPI vs. card transactions** Effective from September 1, 2024. Mandate (NPCI): Issuers must ensure that rewards, benefits, features, and offers for RuPay credit cards used via UPI are not inferior to those when the card is used via traditional card transactions—unless the issuer earns no interchange fee.
  * **Linking RuPay credit cards to UPI and E‑mandate expansion**— RBI and NPCI directive—RuPay credit cards have been enabled to be linked with UPI as part of the RBI’s mandate to allow credit card payments via UPI, starting with RuPay cards.This extension also facilitates e‑mandates (previously limited to bank account debits)—aimed at broadening digital payment usage.
</details>

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>Elo</summary>

  * **Membership and regulatory compliance requirements**—All participants (financial institutions or payment institutions) must be authorized by Brazil’s Central Bank and follow the Elo Payments Arrangement Regulations.\
    This includes mandatory oversight structures covering risk management, fraud monitoring, antimoney‑laundering (AML), KYC, and escalation protocols in case of suspicious activity .
  * **Operational and reporting obligations**—Participants must transmit detailed transaction data for reconciliation, including purchase payment specifics and inter‑participant data exchanges .\
    They must also promptly report and act upon suspected fraud, money‑laundering, or illicit foreign exchange activities—both to Elo and the appropriate authorities—with investigative follow-through and contractual termination of implicated parties where required .
  * **Fraud prevention and risk control**—Elo has implemented robust fraud monitoring (e.g. using FICO® Falcon® Fraud Manager), reducing fraud rates across the network by \~30% for participating issuers. They also partner with identity verification providers (like Prove Identity) to combat SIM‑swap and synthetic fraud, with mandates to integrate digital identity solutions across issuing banks.
  * **Security technology innovations**— Elo has begun rolling out dynamic verification code (EVC®) cards—battery‑free, EMV‑integrated static‑to‑dynamic codes—for enhanced e‑commerce security. While not yet mandatory, adoption is accelerating under Elo’s fraud reduction strategy.
  * **Digital currency and financial inclusion pilots**—Participation in Brazil’s central bank-backed digital currency pilots with offline payment capabilities is underway. Elo mandates integrations with hardware‑secure digital wallets and offline‑capable devices as part of these programs.
</details>
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/card-network-mandates.md`: updatedAt 2026-03-18T15:20:02.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/card-network-mandates.md` | whole document | https://developers.pismo.io/pismo-docs/docs/card-network-mandates | `60122ee682af10a1…` | 2026-03-18T15:20:02.000Z |

## Related knowledge units

- `KU-CARD-digital-wallets` — Digital wallets, MDES Token Connect and Click to Pay
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
