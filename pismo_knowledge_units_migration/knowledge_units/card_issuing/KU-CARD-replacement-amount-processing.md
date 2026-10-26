---
ku_id: KU-CARD-replacement-amount-processing
title: Replacement amount processing
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/replacement-amount-processing.md
  sha256: 727688e490c753f824bb416e8f69978b1bd69b25468cba762c6f0c809b1fa571
  url: https://developers.pismo.io/pismo-docs/docs/replacement-amount-processing
  role: primary_guide
  updated_at: '2026-03-18T15:20:58.000Z'
operations: []
related_kus:
- KU-CARD-authorization-events
- KU-CARD-clearing
grouping_rationale: single source page
---

# Replacement amount processing

**KU ID:** `KU-CARD-replacement-amount-processing` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/replacement-amount-processing.md`:

> The Pismo platform supports replacement amount processing in the authorization/base I flow to reflect a transaction amount change. When processing a cancellation request, the platform may receive the replacement amount field populated with information that indicates an amount to replace the original one.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/replacement-amount-processing.md`: Replacement amount processing; General processing

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/replacement-amount-processing.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/replacement-amount-processing · updatedAt: 2026-03-18T15:20:58.000Z

<!-- source:begin path=docs/card-issuing/replacement-amount-processing.md part=0-end -->

# Replacement amount processing

The Pismo platform supports replacement amount processing in the authorization/base I flow to reflect a transaction amount change. When processing a cancellation request, the platform may receive the replacement amount field populated with information that indicates an amount to replace the original one.

**Note**: This feature is for full balance integration only.

Instead of canceling the entire authorization as it would for regular cancellation requests, this type of replacement operation allows you to:

* Update [pending authorization](https://developers.pismo.io/pismo-docs/docs/replacement-amount-processing#replacement-of-pending-authorization) authorization amounts.
* Reopen a [canceled authorization](https://developers.pismo.io/pismo-docs/docs/replacement-amount-processing#replacement-of-canceled-authorization).

The Pismo platform currently supports replacement amount processing for both major card networks:

* **Mastercard** - Both domestic and international operations are supported.
* **Visa** - Only domestic operations are supported. For international transactions, the platform ignores the replacement requests and settles the correct amounts in the clearing/base II processing.

# General processing

1. The platform receives a cancellation request and finds the original authorization related to this request.
2. The platform verifies whether the replacement amount is present in the message request:

* **Mastercard or Visa** - A  new cancellation request (**mti 0400/0420**) contains the replacement amount information in the **Field 95 - Replacement Amounts**. The platform checks if this field is present, populated, and has an amount greater than **0** to indicate a replacement.
* **Mastercard only** - A single message clearing T464 file contains the replacement information in the EREC message.

3. If the replacement amount is present, the platform initiates the replacement amount processing flow and validates whether the authorization can have its amount replaced.

* The original authorization and the replacement request must be the same operation (they must have the same processing code). If they are not, the platform denies the replacement request.
* The original authorization must be in the pending or canceled status.  If the original authorization is settled by the clearing/base II flow, the platform denies the replacement request.

4. Depending on the authorization status, the platform proceeds as follows.

* #### Replacement of pending authorization
  ❶  When the platform receives a cancellation request with replacement information for a  pending authorization, it calculates the new authorization amount based on the replacement information present in the message.\
  ❷  The platform directly impacts the account limit with the difference between original amounts and the replacement one. The platform does not apply any authorization validation rules at this stage since the authorization has been previously approved.\
  ❸  The platform replaces the original authorization amount.\
  ❹  The platform issues an [authorization event](https://developers.pismo.io/pismo-docs/docs/authorization-events#network-authorization-event) with the category set as REPLACEMENT.

* #### Replacement of canceled authorization
  ❶  When the platform receives a cancellation request with replacement information for a canceled authorization, it validates if the replacement request message has the **DE4 - Transaction** amount set as **0**. This is a safety check that indicates that the request is replacing a canceled authorization of amount 0 with a new amount and reopening that authorization to be charged on the account.\
  ❷  After this validation, if the flow continues, the platform impacts the account limits with the full amount of the replacement request.\
  ❸  The platform reopens the authorization and updates its status to open.\
  ❹  The platform replaces the authorization amount of **0** with the replacement amount.\
  ❺  The platform issues an [authorization event](https://developers.pismo.io/pismo-docs/docs/authorization-events#network-authorization-event) with the category set as REPLACEMENT.

5. After the replacement amount request is processed, the authorization usually receives a clearing message to settle this operation with the replacement amount. All rules for clearing/base II apply to this authorization. It is possible for it to be canceled, partially canceled, or to receive more than one confirmation message. For more information about clearing processing, refer to [this page](https://developers.pismo.io/pismo-docs/docs/clearingbase).
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/replacement-amount-processing.md`: updatedAt 2026-03-18T15:20:58.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/replacement-amount-processing.md` | whole document | https://developers.pismo.io/pismo-docs/docs/replacement-amount-processing | `727688e490c753f8…` | 2026-03-18T15:20:58.000Z |

## Related knowledge units

- `KU-CARD-authorization-events` — Authorization events
- `KU-CARD-clearing` — Clearing: Base II and the clearing rules engine
