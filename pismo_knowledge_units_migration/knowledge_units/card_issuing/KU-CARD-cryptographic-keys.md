---
ku_id: KU-CARD-cryptographic-keys
title: Cryptographic process with Pismo and the card network
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/cryptographic-keys.md
  sha256: 6730c3f5a5ae43d44d652801e1d7e0f7047faffc60c4e40f776a9069d914cf91
  url: https://developers.pismo.io/pismo-docs/docs/cryptographic-keys
  role: primary_guide
  updated_at: '2026-05-18T16:20:24.000Z'
operations: []
related_kus:
- KU-CARD-card-network-integration
grouping_rationale: single source page
---

# Cryptographic process with Pismo and the card network

**KU ID:** `KU-CARD-cryptographic-keys` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/cryptographic-keys.md`:

> Before you begin issuing cards or processing card transactions, you need to go through a ceremony with the card network and Pismo to generate a master key for encrypting lower-level keys used for encryption in operations that need to be done securely.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/cryptographic-keys.md`: Cryptographic process with Pismo and the card network; Client cryptographic key ceremony; Embosser cryptographic key ceremony; Hardware security module (HSM); Transporting sub-keys

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/cryptographic-keys.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cryptographic-keys · updatedAt: 2026-05-18T16:20:24.000Z

<!-- source:begin path=docs/card-issuing/cryptographic-keys.md part=0-end -->

# Cryptographic process with Pismo and the card network

Before you begin issuing cards or processing card transactions, you need to go through a ceremony with the card network and Pismo to generate a master key for encrypting lower-level keys used for encryption in operations that need to be done securely.

<Callout icon="📘" theme="info">
  Note that this process is part of  [Card network certification](https://developers.pismo.io/pismo-docs/docs/network-certification).
</Callout>

In cryptography, a ***key ceremony*** is a ceremony held to generate or use a cryptographic key. A **Zone Master Key** (ZMK), also known as an Interchange key (IK), is a key-encrypting key which is distributed manually between two (or more) communicating sites, within a shared network, in order that further keys can be exchanged automatically without the need for manual intervention. The ZMK is used to encrypt keys of a lower level (e.g. ZPK) for transmission. The Zone Master Key (ZMK) transport key is also known as  "BKEM" or "ZCMK", or some other term depending on the card network's nomenclature.

<Callout icon="📘" theme="info">
  Along with card network certification, you should begin the encryption process **as soon as possible**.
</Callout>

The actual ceremony takes about one hour, but it needs to be in person. In order to meet Payment Card Industry (PCI) requirements, the transport key ZMK **must** be composed of at least 3 hexadecimal components. AES-256 encryption is the standard,  however, on client request, Pismo still uses 3DES for legacy client implementation.

The ZMK key components must be transported physically (not via digital means) and separately. They can come in through via different courier companies in an identified, serialized, numbered envelope. Cryptographic components cannot (under any circumstances) be sent using the same method, that is, if one is sent by regular postal mail, the others must follow another method. Often 3 different courier companies are used to transport components individually and entirely separately to reduce the risk of compromise. Regular postal mail can take a month or longer depending on the customs processes of the country of origin or destination.

If any problem arises, and one or more components are lost, it is understood that the resulting ZMK key is compromised, and new components must be generated in order to preserve the integrity and confidentiality of sensitive information. In this scenario, the process will need to be restarted.

Pismo's ceremonial key processes are intended to form a ZMK key of transport that enables customers/partners to exchange cryptographic key files  with Pismo, where they need to be generated and/or registered in [hardware security modules](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM).

The in-person ceremony generates the Zone Master Key transport key. Lower level keys do not necessarily need to be generated in-person, although you can use this ceremony to do so. If this is the case, the ceremony can take longer depending on how many keys are involved.

## Client cryptographic key ceremony

Clients typically ask the card networks - Mastercard, Visa, and so on - to issue components to form a ZMK transport key. Guidelines and regulations require that these transport keys have at least 3 components  requiring 3 custodians responsible for a component's custody, transport, and handling. No one other than a custodian can view the respective component.

Payment Card Industry (PCI) regulations require that specialized companies/carriers separately carry out transporting components.  If any of them are lost, the others are safe. If a component is lost, it is no longer possible to form the resulting ZMK transport key, so a new component generation ceremony must be performed. Components are never transported digitally, only physically.

**Key ceremony with payment processor and card network:**

* KCV =  [Key checksum value](https://en.wikipedia.org/wiki/Key_checksum_value)

<Image align="center" alt="Key ceremony between Pismo and client" src="https://files.readme.io/e045eb9-cryptoCeremony.png" />

The key ceremony takes place at Pismo offices in a secure room with key custodian members (one for each component), and at least one ceremonial conductor and witness. At that time, the transport key component custodians can be partner company members (clients) visiting the Pismo office or they can be Pismo employees with delegated custody for the respective components the client has made available.

The network ships the  three encryption key components to Pismo custodians in sealed and secured envelopes that must not be tampered with during transit. Components should be transported through 3 different courier companies to guarantee separate deliveries.

The same courier company cannot be used to transport all 3 components. Ideally, 3 companies should be used. However, if only two can be used, then one of them should transport the third component on a different date then the other component they transported.

During the ceremony, a cryptographic key import operation is performed. At the ceremony, there will be one representative from the Pismo information security team. Other Pismo employees may sign as witnesses, but only the information security representative can be in the room when the components are entered into the HSM.

At Pismo, all keys relevant to the project scope are generated, and are encrypted with the network-issued transport key. The network-generated transport keys must be composed of at least 3 hexadecimal components. All the working keys—CVK1, CVK2, POS5, POS7, PEK, CAK, and so on—are default encrypted with the network transport key

A Pismo-generated transport key encrypts the keys that need to be shared with ACS and embossing partners, which are delivered to the partner-appointed custodians.

After completing the key ceremony generation process, all relevant project keys can be sent to client custodians so that they can proceed with their upload to the Mastercard application.

Key custodian members and witnesses sign a confidentiality agreement regarding the ceremony's information, attendance, and minutes. They cannot access the safe room with electronic audio and video devices  such as cell phones, smartphones, recorders, computers, and so on.

## Embosser cryptographic key ceremony

Pismo has several partners/clients who  issue their cards through embossers or embossing factories. The embosser or Pismo, given its HSM,  can generate the ZMK transport key components.

**Key ceremony with embosser:**

<Image align="center" alt="Key ceremony between Pimso and embosser" src="https://files.readme.io/0c9c3c6-Cryptographic_process_with_Pismo_and_the_card_network_2_V7.png" />

The ceremony is performed in a secure room with key custodian members (one for each component), and at least one ceremonial conductor and witness. If the components for forming the transport key (ZMK) were generated via Pismo's HSM, the import ceremony takes place at the embosser; if they were generated at the embosser, the ceremony takes place at Pismo.

Key custodian members and witnesses sign a confidentiality agreement regarding the ceremony's information, attendance, and minutes. They cannot access the safe room with electronic audio and video devices such as cell phones, smartphones, recorders, computers, and so on.

## Hardware security module (HSM)

Pismo uses <Anchor label="FutureX HSM" target="_blank" href="https://www.futurex.com/products/hardware-security-modules">FutureX HSM</Anchor> and connects to it with the <a href="https://www.futurex.com/products/crypto-management/excrypt-touch/" target="_blank">ExcryptTouch</a> portable device .  This device incorporates a FIPS 140-2 Level 3 compliant HSM, which allows security officers to conduct remote device management procedures and key loading processes without being confined to a rack. It also makes it possible to manage and configure network-connected Futurex devices in order to reduce travel time. Data center access is kept to a minimum.

ExcryptTouch is digitally signed with an organization's unique root certificate, ensuring all connections are encrypted and authenticated. It provides authenticated activity/access logs as well as detailed audit records.

**Industry compliance standards**

• FIPS 140-2 Level 3 Compliant\
• ANSI X9.24 Part 1 and Part 2—TR-39\
• FCC Part 15 - Class B\
• PCI HSM\
• RoHS

**Logical security settings**

• Dual-factor authentication for increased security\
• Dual logins required to access the configuration application\
• Key component entry occurs in separate steps, each with its own check digit display

**Connectivity methods**

• Ethernet (wired)\
• Wi-Fi

## Transporting sub-keys

Once the ZMK transport key has been generated between Pismo and a client or Pismo and an embossing partner, it is possible to transport *sub-keys* between different HSMs (different encryption boundaries).

The following are considered **sub-keys**:

* ZPK (aka, PEK, -IWK, embossing key, etc): 001 (Zone PIN Key or PIN Encryption Key)
* CVK (aka CVV, or CSCK, CAVV, CAK, etc): 402 (Card Verification Key)
* KEK(aka ZMK, ZCMK, BKEM, etc):: 107 | 000 (Key Encryption Key)
* MK-AC (aka as MDK, masterkey, IMK, IMKac, etc): 109 (Master Key for Application Cryptograms)
* MK-SMI: 209 (Master Key for Secure Messaging - Integrity)
* MK-SMC: 309 (Master Key for Secure Messaging - Confidentiality)
* ZEK: 00A (Zone Encryption Key for PAN)

Keys that Pismo exchanges with embossing partners:  ZPK, MK-AC, MK-SMI, MK-SMC.

Keys that Pismo exchanges with the card network:  KEK (Only for dynamic PIN keys), ZPK (Only for static PIN keys), CVKs (depending on the advice configuration), MK-AC (depending on the advice configuration).

To transport these keys, they must be *enveloped /wrapped* via the transport key (ZMK) through HSM commands. In this way, the keys are translated into a readable format for the Pismo HSM and also for the partner.

The HSM never provides a clear key, only in a format encrypted by the LMK (Local Master Key) or the ZMK (Zone Master Key) transport key. The subkey cryptograms can be transported via digital means (secure email, digital communicator) in a password-protected encrypted file with the password sent separately through other means.
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/cryptographic-keys.md`: updatedAt 2026-05-18T16:20:24.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/cryptographic-keys.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cryptographic-keys | `6730c3f5a5ae43d4…` | 2026-05-18T16:20:24.000Z |

## Related knowledge units

- `KU-CARD-card-network-integration` — Card network integration and certification
