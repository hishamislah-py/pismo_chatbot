---
ku_id: KU-CARD-incremental-authorization
title: Incremental authorization
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/incremental-authorization.md
  sha256: 4e4fac4b298596a0c25876cc09e0663685cb9c207a1f8db22c971519518bd10c
  url: https://developers.pismo.io/pismo-docs/docs/incremental-authorization
  role: primary_guide
  updated_at: '2026-03-18T15:21:00.000Z'
operations: []
related_kus:
- KU-CARD-authorization-events
- KU-CARD-clearing
grouping_rationale: single source page
---

# Incremental authorization

**KU ID:** `KU-CARD-incremental-authorization` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/incremental-authorization.md`:

> Merchants and acquirers can use incremental authorization to add some amount to a  previously created authorization to reflect a transaction's real amount.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/incremental-authorization.md`: Incremental authorization; General processing; Identifying incremental authorization; Visa; Mastercard

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/incremental-authorization.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/incremental-authorization · updatedAt: 2026-03-18T15:21:00.000Z

<!-- source:begin path=docs/card-issuing/incremental-authorization.md part=0-end -->

# Incremental authorization

Merchants and acquirers can use incremental authorization to add some amount to a  previously created authorization to reflect a transaction's real amount.

Incremental authorization:

* Only occurs in the authorization/base I flow.
* Is based on a new authorization request that identifies the original authorization.
* If approved, increments the authorization amounts.

The Pismo platform identifies an incremental authorization differently between the Visa and Mastercard card networks, but the processing is the same.

**Note**: This feature is for full balance integration only.

# General processing

When the Pismo platform [identifies an incremental authorization](https://developers.pismo.io/pismo-docs/docs/incremental-authorization#identifying-incremental-authorization), the flow is as follows:

**Step 1**

The platform retrieves the original authorization based on the identifier received in the ISO message.

If the platform doesn't find the original authorization based on the identifier received in the ISO message, it handles this request as a new authorization with a new authorization code. Then, the request follows a regular authorization flow. Depending on the validation results, the platform approves or declines this request.

**Step 2**

When the platform finds the original authorization, it validates whether this authorization can be incremented or not. To qualify:

* Both the original and the incremental authorization must be the same operation (they must have the same processing code).
* The original authorization must be pending and not be settled by the clearing/base II process.

If the original authorization doesn’t meet these requirements (for example, if it is declined, canceled, or settled), the platform creates a new authorization request that follows regular authorization flow.

**Step 3**

Once the platform determines that the authorization can be incremented, it marks the request as incremental and proceeds with the usual authorization flow to validate whether to approve or deny the authorization.

**Step 4**

If the incremental authorization is approved, the platform:

* Adds the incremental amount to the transaction.
* Impacts the account limits with the amount of the incremental operation.
* Issues an [authorization event](https://developers.pismo.io/pismo-docs/docs/authorization-events#network-authorization-event) with the category set as INCREMENTAL.

**Step 5**

If the incremental authorization is declined for any reason, the platform issues an [authorization event](https://developers.pismo.io/pismo-docs/docs/authorization-events#network-authorization-event) with the category set as DECLINED.In both approved and denied scenarios, the issued events have the amounts and information of  the incremental operation, but the identifiers of that authorization, such as `authorization_id`, `authorization_code`, and `cid` are the same as the original one, allowing the events to be linked to each other.

**Step 6**

After being incremented, the authorization usually receives a clearing message to settle this operation with the summed amount of both the original and incremental authorization. All rules for clearing/base II apply to this authorization. It is possible for it to be canceled, partially canceled, or to receive more than one confirmation message. For more information about clearing processing, refer to [this page](https://developers.pismo.io/pismo-docs/docs/clearingbase).

# Identifying incremental authorization

Visa and Mastercard have different ways to indicate that an authorization request is incremental.

## Visa

The platform uses the following fields in the Visa request message for incremental authorization processing:

|                                         |                                                                                                                                                                                                                                                                                                  |
| :-------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Field 63.3 – Message Reason Code**    | When this field contains the value **3900**, the platform identifies the authorization request as incremental.                                                                                                                                                                                   |
| **Field 62.2 – Transaction Identifier** | After identifying the request as incremental, the platform uses the transaction identifier in this field to link the request with the original authorization that is being incremented and follows incremental processing as described [here](https://developers.pismo.io/pismo-docs/docs/incremental-authorization#general-processing). |

## Mastercard

In the Mastercard messages, there is no specific code that identifies an authorization request as incremental. The platform uses the following fields in the Mastercard request message for incremental authorization processing:

|                                     |                                                                                                                                                                                                                                                                                                                                                                 |
| :---------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DE 48, subelement 63 (Trace ID)** | If this field is populated, it indicates some relationship of this request with an original authorization. The platform uses this value to find and compare it to the value of **DE 63 (Network Data)** of the related original authorization.                                                                                                                  |
| **DE 63 (Network Data)**            | If this value in the related original authorization matches the value in **DE 48, subelement 63 (Trace ID)** in the request message and the request is in a pre-authorization state, the platform identifies the authorization request as incremental and follows incremental processing as described [here](https://developers.pismo.io/pismo-docs/docs/incremental-authorization#general-processing). |

> 📘
>
> The platform ignores the trace ID when the value received for the Banknet Reference Number is **999999**, since this value can be used only to populate the field without indicating any relationship.
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/incremental-authorization.md`: updatedAt 2026-03-18T15:21:00.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/incremental-authorization.md` | whole document | https://developers.pismo.io/pismo-docs/docs/incremental-authorization | `4e4fac4b298596a0…` | 2026-03-18T15:21:00.000Z |

## Related knowledge units

- `KU-CARD-authorization-events` — Authorization events
- `KU-CARD-clearing` — Clearing: Base II and the clearing rules engine
