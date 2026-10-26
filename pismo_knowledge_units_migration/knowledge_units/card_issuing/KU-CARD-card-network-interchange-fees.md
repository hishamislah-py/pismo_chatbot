---
ku_id: KU-CARD-card-network-interchange-fees
title: Card network interchange fees
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/card-network-interchange-fees.md
  sha256: b026fdaab6948b51f1d5704548e9dd267fa204c4397d3e29204a7e4da651f5d3
  url: https://developers.pismo.io/pismo-docs/docs/card-network-interchange-fees
  role: primary_guide
  updated_at: '2026-03-18T15:20:26.000Z'
operations: []
related_kus:
- KU-CARD-authorization-events
- KU-CARD-full-and-zero-balance-workflows
grouping_rationale: single source page
---

# Card network interchange fees

**KU ID:** `KU-CARD-card-network-interchange-fees` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/card-network-interchange-fees.md`:

> Card network interchange fees, often referred to simply as interchange fees or swipe fees, are fees that payment card networks, such as Visa or MasterCard, charge to facilitate credit and debit card transaction processing. These fees are an integral part of the payment card ecosystem and play a significant role in the revenue model for both card issuers (banks or financial institutions) and the card networks themselves.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/card-network-interchange-fees.md`: Card network interchange fees; Key points about card network interchange fees

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/card-network-interchange-fees.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/card-network-interchange-fees · updatedAt: 2026-03-18T15:20:26.000Z

<!-- source:begin path=docs/card-issuing/card-network-interchange-fees.md part=0-end -->

# Card network interchange fees

Card network interchange fees, often referred to simply as interchange fees or swipe fees, are fees that payment card networks, such as Visa or MasterCard, charge to facilitate credit and debit card transaction processing. These fees are an integral part of the payment card ecosystem and play a significant role in the revenue model for both card issuers (banks or financial institutions) and the card networks themselves.

You can find the interchange fee for a transaction in the <a href="https://developers.pismo.io/events/docs/networktransactions-clearing-1" target="_blank">network authorizations clearing event message</a>:

**"Data" > "raw\_message" > "interchangeFeeIndicator":"C"** - "C" = type of transaction where "C" is credit

**"Data" > "raw\_message" > "interchangeFee": "0000000014"**

The above operations interchange fee value (`interchangeFee`) represents 0.14 in the settlement currency. The fields here are from a Mastercard T464 single message clearing event. Other networks may call these fields something slightly different. See the [sample clearing event messages](https://developers.pismo.io/pismo-docs/docs/authorization-events#clearingbase-ii-events) in the Authorization events guide  for more information.

See [Full and zero balance workflows ](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows)to see where the clearing message fits within the overall transaction processing workflow.

The rest of this guide details general information about interchange fees.

## Key points about card network interchange fees

* **Purpose**—Interchange fees are intended to cover the costs associated with processing card transactions, including authorization, clearing, settlement, fraud prevention, and other operational expenses. They also help fund the rewards and benefits that card issuers offer to cardholders.

* **Structure**—Interchange fees are not set at a fixed rate and can vary depending on various factors, including the card type (credit or debit), the merchant category (i.e., retail, e-commerce, or restaurant), the transaction location (domestic or international), and the specific card network. Different card networks have their own interchange fee schedules, which may change periodically.

* **Calculation**—Interchange fees are typically calculated as a percentage of the transaction amount plus a fixed per-transaction fee. For example, an interchange fee might be set at 1.5% of the transaction amount plus $0.10 per transaction. This means that for a $100 transaction, the interchange fee would be $1.60 ($1.50 as a percentage + $0.10 as a fixed fee).

* **Revenue distribution**—The revenue generated from interchange fees is usually shared among the various parties involved in a card transaction. This includes the card-issuing bank (issuer), the cardholder's bank, the payment card network (i.e., Visa or MasterCard), and the merchant's acquiring bank. The exact distribution can vary by region and card network.

* **Impact**—Interchange fees can have a significant impact on merchants, especially smaller businesses, as they are one of the costs associated with accepting card payments. Merchants may negotiate with acquiring banks to secure lower interchange rates, and some countries have implemented regulations to limit interchange fees to promote fair competition.

* **Regulation**—Many countries have regulatory bodies that oversee interchange fees and may impose caps or restrictions to ensure fair competition and protect consumers and merchants. These regulations vary widely by region and can have a substantial impact on the payment card industry.

* **Rewards programs**—Interchange fees are one of the key sources of funding for credit card rewards programs. Issuers use a portion of the interchange revenue to offer incentives such as cashback rewards, travel points, or other perks to cardholders.

In summary, card network interchange fees are a crucial part of the payment card ecosystem, serving to cover transaction processing costs, fund rewards programs, and generate revenue for the various stakeholders involved in card transactions. The specific fee structure and regulations governing interchange fees can vary widely by region and payment network.

<details>
  <summary style={{ fontSize: "18px" }}><b>How interchange fees are calculated</b></summary>

  Interchange fees are calculated based on a complex formula set by the payment card networks. While the specific formula and rates can vary between card networks and regions, here are some of the common factors that are typically considered in the calculation of interchange fees:

  * **Transaction amount** - The total dollar amount of the transaction is a fundamental factor in determining the interchange fee. Typically, the higher the transaction amount, the higher the interchange fee, as it represents a larger potential risk and cost to the card network and issuing bank.

  * **Card type** - Interchange fees vary depending on the card type used. Credit cards and debit cards may have different fee structures. Within these categories, there may be further distinctions based on the card's features or rewards program (i.e., basic, rewards, premium).

  * **Merchant category** - The type of business where the transaction takes place can influence interchange fees. Transactions at different types of merchants (i.e., grocery stores, restaurants, online retailers) may incur different interchange rates. Some categories might have higher fees due to perceived risks or costs associated with processing those types of transactions.

  * **Card-present vs. card-not-present** - Transactions conducted in person (card-present) often have lower interchange rates than those conducted online or over the phone (card-not-present). This is because card-not-present transactions typically carry a higher risk of fraud.

  * **Region and currency** - Interchange fees can also vary by geographic region and currency. Different countries or regions may have their own interchange fee structures based on local market conditions and regulations.

  * **Issuer and acquirer relationships** - The specific agreements between card issuers (banks that issue credit/debit cards to consumers) and acquirers (banks that handle merchant accounts) can affect interchange fees. In some cases, merchants can negotiate lower interchange rates with their acquirers.

  * **Card network rules** - Payment card networks periodically update their interchange fee schedules, and these rules can change over time. They may introduce new fee categories, adjust rates, or modify their criteria.

  * **Transaction authorization and clearing costs** -  Interchange fees are designed to cover the cost of authorizing a transaction (verifying that the cardholder has sufficient funds or credit) and clearing it (processing and settling the transaction between the parties involved).

  * **Fraud prevention and risk management** - Interchange fees can also include a component to cover the cost of fraud prevention and risk management measures the card network and the issuer implement.

  It's important to note that interchange fees can be quite complex, with various combinations of these factors contributing to the final fee for a given transaction. Additionally, payment card networks periodically update their interchange fee schedules, so these fees can change over time.

  Merchants often have little control over the interchange fees they pay, as these fees are determined by the card networks and issuers. However, they can sometimes negotiate with acquiring banks for more favorable rates, especially if they are high-volume merchants or part of a larger organization.
</details>

<details>
  <summary style={{ fontSize: "18px" }}>
    <b>How much are interchange fees</b>
  </summary>

  Interchange fees can vary widely depending on several factors, including the card type (credit or debit), the specific card network, the country or region where the transaction takes place, the merchant category, the transaction amount, and the type of card used (i.e., basic, rewards, premium). Interchange fees are typically set by the card networks and may be subject to regulation by government authorities.

  Here are some general examples of interchange fee ranges in the United States, which is one of the countries with a well-documented interchange fee structure. Please note that these figures are provided as examples and may not reflect the current rates:

  * **Debit card interchange fees** - Debit card interchange fees in the U.S. can range from around 0.05% to 1.0% of the transaction amount, plus a fixed per-transaction fee, which could be in the range of $0.05 to $0.25 or more per transaction. The exact fee depends on factors such as the type of debit card (basic or rewards), the merchant category, and the specific card network.

  * **Credit card interchange fees** - Credit card interchange fees in the U.S. often range from about 1.0% to 3.0% or more of the transaction amount, depending on factors like the card type, merchant category, and card network. Premium or rewards credit cards typically have higher interchange fees due to the associated rewards programs.

  * **Specific examples** - For example, a standard credit card transaction might have an interchange fee of 1.65% of the transaction amount plus $0.10 per transaction. In contrast, a premium rewards credit card transaction might have a higher interchange fee of 2.30% of the transaction amount plus $0.15 per transaction.

  It's important to emphasize that these figures are illustrative and can change over time due to various factors, including regulatory changes, card network policies, and market dynamics. Additionally, interchange fee structures can vary significantly between countries and regions.

  To obtain the most accurate and up-to-date information on interchange fees, you should consult the official websites of relevant card networks (i.e., Visa, MasterCard), government regulatory authorities, or industry associations in your specific jurisdiction. Additionally, if you are a merchant, your acquiring bank or payment processor can provide you with information on the interchange fees that apply to your transactions.
</details>

<details>
  <summary style={{ fontSize: "18px" }}><b>How interchange fees are regulated</b></summary>

  Card network interchange fees are subject to regulation in many countries to promote competition, protect consumers, and ensure fair and transparent practices within the payment card industry. Regulation of interchange fees can vary significantly from one jurisdiction to another, and the regulation level can depend on the local payment card market's maturity and development.

  **Key aspects about interchange fee regulation:**

  * **Regulatory bodies** - Many countries have regulatory authorities responsible for overseeing and regulating payment card systems. These authorities often have the power to set caps or limits on interchange fees. In the United States, for example, the Dodd-Frank Wall Street Reform and Consumer Protection Act led to the creation of the Consumer Financial Protection Bureau (CFPB), which has authority over interchange fees.

  * **Interchange fee caps** -  Regulatory bodies can impose maximum interchange fee limits that card networks and issuers are allowed to charge for specific types of transactions. These caps are often designed to prevent anticompetitive behavior and to ensure that interchange fees are reasonable and proportional to the cost of processing transactions.

  * **Transparency requirements** - Regulations can require card networks and issuers to provide more transparency regarding interchange fees. This includes disclosing interchange rates to merchants and consumers, which helps stakeholders understand the cost structure of card transactions.

  * **Anti-steering rules** - In some cases, regulations may restrict card networks from imposing rules that prevent merchants from encouraging the use of lower-cost payment methods or from steering customers toward particular card brands or networks.

  * **Competitive market forces** - In regions with well-established card markets and significant competition, market forces may play a role in regulating interchange fees. Card networks and issuers may voluntarily adjust their interchange fee structures to remain competitive.

  * **Merchant negotiation** - Merchants, especially larger ones or those with substantial bargaining power, may negotiate directly with acquiring banks for more favorable interchange fee rates. Negotiations can lead to customized fee structures based on the merchant's transaction volume and other factors.

  * **International regulation** - In some cases, international organizations may set guidelines or standards for interchange fees. For example, the European Union has implemented regulations that affect interchange fees within its member states, such as the Interchange Fee Regulation (IFR).

  It's important to note that the specifics of interchange fee regulation can vary widely from one jurisdiction to another. Some regions may have more stringent regulations in place, while others rely more on market competition and negotiation. Additionally, regulations in this area can evolve over time in response to changes in the payment card industry and emerging technologies.

  Merchants, card networks, and issuers typically need to stay informed about local regulations and compliance requirements to ensure they operate within the legal framework of their respective markets.
</details>

<details>
  <summary style={{ fontSize: "18px" }}>
    <b>How interchange fees are regulated in Brazil</b>
  </summary>

  The <a href="https://www.bcb.gov.br/en" target="_blank">Central Bank of Brazil</a> and the <a href="https://www.gov.br/cade/en/access-to-information/about-us" target="_blank">Administrative Council for Economic Defense (CADE)</a> regulate interchange fees in Brazil. The primary regulatory framework governing interchange fees in Brazil includes the <a href="https://www.bcb.gov.br/pre/normativos/circ/2013/pdf/circ_3682_v2_L.pdf" target="_blank">Circular No. 3,682/2013</a> issued by the Central Bank, which establishes rules and guidelines for payment card operations.

  **Key aspects about Brazilian interchange fee regulation:**

  * **Caps on interchange fee** -  The Central Bank of Brazil implements a cap on interchange fees for debit and credit card transactions. These caps are designed to limit the maximum fees that card networks and issuers can charge to merchants for processing card transactions.

  * **Differentiated rates** - Interchange fees in Brazil often vary based on factors such as the card type (debit or credit), merchant category, and transaction amount. The aim is to establish more favorable rates for smaller businesses and merchants.

  * **Merchant negotiation** -  Merchants in Brazil have the ability to negotiate interchange fee rates with acquiring banks. This allows for some flexibility in fee arrangements, particularly for larger merchants.

  * **Regulation of anti-competitive practices** - The Brazilian antitrust authority - CADE - monitors and regulates practices related to payment card networks to ensure that they do not engage in anti-competitive behavior that could harm competition in the payment card market.

  * **Regulation of network rules** - Payment card networks operating in Brazil are subject to regulation regarding their rules, including rules related to interchange fees and other aspects of the card payment ecosystem. CADE plays a role in overseeing these rules to ensure they comply with Brazilian competition laws.

  Please note that it's important to consult the most current sources and the official websites of regulatory authorities like the Central Bank of Brazil and CADE for the latest information on Brazilian interchange fee regulation. In addition, it's advisable to consult with local legal or financial experts who are familiar with the current regulatory landscape in Brazil for the most up-to-date information.
</details>

<details>
  <summary style={{ fontSize: "18px" }}><b>How interchange fees are regulated in the United Kingdom</b></summary>

  Interchange fees in the United Kingdom (UK) are regulated primarily under European Union regulations, as well as through the actions of domestic regulatory bodies. It is recommended you check with relevant authorities for any recent changes.

  **Key aspects about UK interchange fee regulation:**

  * **EU Regulation (Interchange Fee Regulation - IFR)** - The European Union (EU) has implemented the Interchange Fee Regulation (IFR) as of June 2015, which applied to interchange fees for card-based payment transactions within the EU, including the UK at that time. The IFR introduced caps on interchange fees for both consumer debit and credit card transactions. Debit card interchange fees are capped at 0.2% of the transaction value, while credit card interchange fees are capped at 0.3%.

  * **<a href="https://www.gov.uk/government/organisations/competition-and-markets-authority" target="_blank">Competition and Markets Authority (CMA)</a>** - In the UK, the CMA plays a role in promoting competition within the payment card industry. It conducts investigations and issues recommendations to ensure that practices such as anti-competitive agreements between card networks and issuers do not stifle competition.

  * **<a href="https://www.psr.org.uk/" target="_blank">Payment Systems Regulator (PSR)</a>** - The PSR, a subsidiary of the <a href="https://www.fca.org.uk/" target="_blank">Financial Conduct Authority (FCA)</a>, has regulatory oversight over payment systems in the UK, including payment card systems. The PSR aims to ensure that payment systems are competitive and that they work in the best interests of consumers and businesses.

  * **Card network rules** - Payment card networks like Visa and MasterCard have rules and agreements that govern their operations, including interchange fee structures. These rules are subject to regulatory scrutiny to ensure they comply with EU and UK competition laws.

  * **Domestic regulation post-Brexit** - Since the UK's exit from the EU (Brexit), the country may have developed its own regulations governing payment card interchange fees. It's essential to check with UK regulatory authorities, such as the FCA, for the most up-to-date information on how interchange fees are regulated in the post-Brexit era.

  * **Merchant acquirer agreements** - Merchants in the UK typically have agreements with acquiring banks or payment service providers that outline the terms and conditions, including interchange fee rates, for processing card transactions. These agreements are subject to regulatory oversight to ensure fairness and transparency.

  Given the dynamic nature of financial regulations and the potential for changes in the regulatory landscape, it's crucial you consult official sources such as the FCA, the UK government, or relevant industry associations for the most current information on interchange fee regulation in the United Kingdom. Additionally, legal or financial experts with expertise in the UK payment card industry can provide insights into the latest developments in this area.
</details>

<details>
  <summary style={{ fontSize: "18px" }}>
    <b>How interchange fees are regulated in the United States</b>
  </summary>

  In the United States, the regulation of interchange fees primarily falls under the purview of the financial industry and is influenced by various laws and regulations.

  **Key aspects about United States interchange fee regulation:**

  * **Dodd-Frank Wall Street Reform and Consumer Protection Act** - The Dodd-Frank Act, passed in 2010, established the <a href="https://www.investopedia.com/terms/d/durbin-amendment.asp" target="_blank">Durbin Amendment</a>, which specifically addressed debit card interchange fees. The Durbin Amendment limits the fees that card-issuing banks can charge merchants for processing debit card transactions. It capped these fees at a maximum level, typically expressed as a percentage of the transaction value.

  * **Payment card networks** - Major payment card networks like Visa, Mastercard, American Express, and Discover have their own rules and regulations governing interchange fees. These networks set interchange rates and periodically update them. They negotiate these rates with card-issuing banks and may be subject to antitrust regulations.

  * **Antitrust laws** - Interchange fees have been the subject of antitrust scrutiny in the past. Merchants have raised concerns about anti-competitive behavior by card networks and banks, leading to legal actions and settlements.

  * **Regulatory agencies** - Various regulatory agencies in the United States oversee aspects of the payment card industry and can influence interchange fee regulation:

    * **Consumer Financial Protection Bureau (CFPB)** - The CFPB has authority over consumer protection in financial transactions and has taken an interest in issues related to interchange fees.

    * **Federal Reserve** - The Federal Reserve has played a role in implementing and enforcing certain aspects of the Durbin Amendment related to debit card interchange fees.

  * **Merchant agreements and contracts** - Merchants often negotiate interchange fee rates as part of their agreements with payment processors or acquiring banks. These contracts can influence the fees that merchants pay for card transactions.

  * **State laws** - Some states have enacted their own laws or regulations related to interchange fees. These can vary from state to state and may provide additional protections for merchants.

  * **Litigation** - Interchange fee regulation has been the subject of ongoing litigation and legal challenges. Court decisions can impact the regulatory landscape.

  It's important to note that interchange fee regulation in the United States primarily applies to debit cards, as credit card interchange fees are generally not subject to the same level of regulation. The fees for credit card transactions are typically determined through negotiations between merchants and card networks.
</details>

<details>
  <summary style={{ fontSize: "18px" }}>
    <b>How interchange fees are regulated in India</b>
  </summary>

  Interchange fees in India are regulated primarily by the <a href="https://www.rbi.org.in/" target="_blank">Reserve Bank of India (RBI)</a>, the country's central bank, and the <a href="https://www.npci.org.in/" target="_blank">National Payments Corporation of India (NPCI)</a>, which plays a significant role in the operation of retail payment systems in the country. Please note that regulations can change, and it's essential to verify the most up-to-date information from official sources and regulatory authorities.

  **Key aspects about Indian interchange fee regulation:**

  * **Reserve Bank of India (RBI) regulation** - The RBI issues guidelines and regulations related to interchange fees for various electronic payment methods, including debit cards and prepaid payment instruments. These guidelines aim to ensure fairness, transparency, and competitiveness in the payment card industry.

  * **National Payments Corporation of India (NPCI)** - The NPCI is a key organization that operates various retail payment systems in India, including the <a href="https://www.npci.org.in/what-we-do/upi/product-overview" target="_blank">Unified Payments Interface (UPI)</a> and <a href="https://www.rupay.co.in/" target="_blank">RuPay</a>, a domestic card payment network. NPCI plays a central role in the setting and regulation of interchange fees for card transactions processed through RuPay.

  * **Interchange fee structure** - The interchange fee structure in India typically includes fees for different types of card transactions, such as debit card transactions, prepaid card transactions, and credit card transactions. The fee structure can vary based on factors like the transaction amount and card type.

  * **Caps on interchange fees** - The RBI can impose caps or limitations on interchange fees for specific transaction types, such as card-present and card-not-present transactions. These caps are often intended to ensure that interchange fees are reasonable and do not hinder the growth of electronic payments.

  * **Merchant Discount Rate (MDR)** - In addition to interchange fees, the RBI regulates the MDR, which is the fee mercants pay to acquiring banks for accepting card payments. MDR guidelines aim to strike a balance between providing incentives for merchants to accept electronic payments and ensuring affordability for small businesses.

  * **Network rules** - Payment card networks like Visa and MasterCard also operate in India and have their own rules and regulations regarding interchange fees and payment card processing. These rules are subject to RBI and NPCI regulatory oversight.

  * **Regular updates and amendments** - Regulatory authorities in India periodically review and update interchange fee regulations to align with changing market dynamics and promote digital payments.

  Keep in mind that regulatory frameworks can evolve so it's crucial to consult official sources, such as the RBI and NPCI for the most current information and regulatory guidelines regarding Indian interchange fees. Additionally, seeking guidance from legal or financial experts with Indian payment card industry knowledge is advisable for the latest insights.
</details>
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/card-network-interchange-fees.md`: updatedAt 2026-03-18T15:20:26.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/card-network-interchange-fees.md` | whole document | https://developers.pismo.io/pismo-docs/docs/card-network-interchange-fees | `b026fdaab6948b51…` | 2026-03-18T15:20:26.000Z |

## Related knowledge units

- `KU-CARD-authorization-events` — Authorization events
- `KU-CARD-full-and-zero-balance-workflows` — Full and Zero balance transaction workflows
