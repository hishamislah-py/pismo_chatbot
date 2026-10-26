---
ku_id: KU-CARD-visa-flexible-credentials
title: Visa Flexible Credentials [beta]
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/visa-flexible-credentials.md
  sha256: 348b55c0df0d92ecbb0fc0e813227a7e6335973267b489672caa2450b0923e48
  url: https://developers.pismo.io/pismo-docs/docs/visa-flexible-credentials
  role: primary_guide
  updated_at: '2026-10-07T01:39:37.000Z'
operations:
- create-card-relationship
- create-card-rules
- enroll-card-enrollment
related_kus:
- KU-API-card-issuing-visa-flexible-credentials--enrollment
- KU-API-card-issuing-visa-flexible-credentials--relationships
- KU-API-card-issuing-visa-flexible-credentials--rules
grouping_rationale: single source page
---

# Visa Flexible Credentials [beta]

**KU ID:** `KU-CARD-visa-flexible-credentials` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/visa-flexible-credentials.md`:

> Implementing VFC supports real-time decisioning, and opens the door to hyper-personalized financial experiences. Pismo provides a [VFC API](https://developers.pismo.io/pismo-docs/reference/enroll-card-enrollment)  to implement this feature.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/visa-flexible-credentials.md`: Visa Flexible Credentials [beta]; VFC Managed deployment; VFC card setup; VFC transaction flow; VFC use cases; Use case #1; Use case #2

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/visa-flexible-credentials.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/visa-flexible-credentials · updatedAt: 2026-10-07T01:39:37.000Z

<!-- source:begin path=docs/card-issuing/visa-flexible-credentials.md part=0-end -->

# Visa Flexible Credentials [beta]

<a href="https://developer.visa.com/capabilities/visa-flexible-credential" target="blank">Visa Flexible Credentials</a> (VFC) is a cutting-edge solution that allows issuers to provide consumers with greater control over how they pay. It enables a single card to access multiple funding sources, such as debit, credit, prepaid, and installment plans. The funding sources offered depend on region. These funding sources (including when they are accesed with cards) are known as ***credentials***.

Implementing VFC supports real-time decisioning, and opens the door to hyper-personalized financial experiences. Pismo provides a [VFC API](https://developers.pismo.io/pismo-docs/reference/enroll-card-enrollment)  to implement this feature.

# VFC Managed deployment

Pismo offers the **VFC Managed** deployment model to clients. With VFC Managed, Visa handles the VFC's infrastructure and management. This contrasts with VFC Self-Serve, where the issuer manages the infrastructure and functionality. VFC Managed allows issuers to easily integrate VFC capabilities into their existing systems and offers features like automated credential issuance and management, as well as integration with Visa's payment infrastructure.

**Why use Pismo's VFC APIs**

* Pismo handles and manages Visa's required cryptography to integrate with Visa's VFC APIs.
* Pismo securely handles PCI  (Payment Card Industry) sensitive data on the issuer's behalf.

# VFC card setup

Setting up a card and credentials in VFC means linking a single physical or digital card to one or more alternate funding and enabling dynamic control over how payments are routed at the time of transaction.

Instead of having one card for each funding type (like a debit card, a credit card, or prepaid card), you enroll a card into the VFC program so that it can access alternative funding sources. Users can designate a primary funding source (default) and one or more secondary credentials as a fallback. Then, depending on the cardholder's preferences, you can create transaction rules to enable which card source to use at checkout.

**VFC set up involves:**

1. [Enrolling](https://developers.pismo.io/pismo-docs/reference/enroll-card-enrollment) two credentials (primary and secondary) in VFC. You need to enroll each credential  individually.
2. [Configuring](https://developers.pismo.io/pismo-docs/reference/create-card-relationship) a primary to secondary relationship between the two credentials.
3. [Setting up VFC rules](https://developers.pismo.io/pismo-docs/reference/create-card-rules) YYou set rules for when to use your primary card and when to swap to use your secondary card. Additionally, you can limit VFC to specific transaction types, merchants, and purchase categories.

Users can designate one of their secondary credentials that VFC uses when the preferred chosen credential is unavailable or unusable for a given transaction. The  credential is typically a traditional card (like a standard debit or credit card) that you've enrolled in the system and authorized to serve as a backup.

# VFC transaction flow

When you attempt a transaction using a VFC card, the system first determines if the card is enrolled in the VFC program. If not, normal processing continues. If it is, then the appropriate VFC rules are applied. These rules determine whether the primary or secondary credential funding source is used. If that source fails—normal processing applies - the transaction is declined to the acquirer and merchant as-is.

# VFC use cases

## Use case #1

**Scenario:**

A  cardholder has access to VFC and enrolls both  a Debit card and a Credit card. The cardholder wants to set a VFC rule so that while their Debit card is their primary credential, a transaction is re-routed to the Credit card if the transaction amount is above AUD 100.

**Implementation**

The client calls  the [Create rules](https://developers.pismo.io/pismo-docs/reference/create-card-rules)  endpoint passing the following parameters and values:

```json

scope.controlType = TCT_GLOBAL // Transaction control type (TCT) global

scope.cardHolderBillAmount.minAmount = 100 // Minimum transaction amount allowed
```

## Use case #2

**Scenario**

The cardholder (with the same two cards/credentials as Use case #1) sets a budget for dining out and doesn't want to spend more than EUR 60.00 on credit on any restaurant in the next week (1st - 7th February 2029). In other words, the first 60 goes on credit and the rest from debit.

**Implementation**

The client calls  the [Create rules](https://developers.pismo.io/pismo-docs/reference/create-card-rules)  endpoint passing the following parameters and values:

```json
source.controlType = MCT_DINING  // Merchant Category Type (MCT) dining

scope.cardHolderBillAmount.maxAmount = 60

scope.timeRange.startTime = 2029-02-01T00:00:01 // February 1

scope.timeRange.endTime = 2029-02-07T23:59:59   // February 7
```

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /flex_credentials/v1/vfc/enrollment/cards/{cardId}` | `enroll-card-enrollment` | Enroll card in VFC | `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` | no | KU-API-card-issuing-visa-flexible-credentials--enrollment |
| `POST /flex_credentials/v1/vfc/relationship/cards/{cardId}` | `create-card-relationship` | Create card relationships | `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` | no | KU-API-card-issuing-visa-flexible-credentials--relationships |
| `POST /flex_credentials/v1/vfc/rules/cards/{cardId}` | `create-card-rules` | Create rules | `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` | no | KU-API-card-issuing-visa-flexible-credentials--rules |

### Operation essentials

- **`POST /flex_credentials/v1/vfc/enrollment/cards/{cardId}`** (`enroll-card-enrollment`): security `BearerAuth`; required parameters `access_token` (header), `cardId` (path); required body fields none declared; response statuses 201, 400, 401, 500; error codes in examples `ERR9993`, `ERR9786`, `ERR5446`; events none listed.
- **`POST /flex_credentials/v1/vfc/relationship/cards/{cardId}`** (`create-card-relationship`): security `BearerAuth`; required parameters `cardId` (path), `access_token` (header); required body fields `cards`; response statuses 201, 400, 401, 500; error codes in examples `ERR9993`, `ERR9786`, `ERR5446`; events none listed.
- **`POST /flex_credentials/v1/vfc/rules/cards/{cardId}`** (`create-card-rules`): security `BearerAuth`; required parameters `access_token` (header), `cardId` (path); required body fields `rules`; response statuses 201, 400, 401, 500; error codes in examples `ERR9993`, `ERR9786`, `ERR5446`; events none listed.

## Lifecycle status

- `docs/card-issuing/visa-flexible-credentials.md`: updatedAt 2026-10-07T01:39:37.000Z.
- The source title marks the feature as beta: "Visa Flexible Credentials [beta]".

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/visa-flexible-credentials.md` | whole document | https://developers.pismo.io/pismo-docs/docs/visa-flexible-credentials | `348b55c0df0d92ec…` | 2026-10-07T01:39:37.000Z |

## Related knowledge units

- `KU-API-card-issuing-visa-flexible-credentials--enrollment` — API reference: Card issuing - Visa Flexible Credentials [beta] — Enrollment
- `KU-API-card-issuing-visa-flexible-credentials--relationships` — API reference: Card issuing - Visa Flexible Credentials [beta] — Relationships
- `KU-API-card-issuing-visa-flexible-credentials--rules` — API reference: Card issuing - Visa Flexible Credentials [beta] — Rules
