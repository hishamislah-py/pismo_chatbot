---
ku_id: KU-CRED-account-collection-status
title: Account collection status
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/account-collection-status.md
  sha256: fc29ba1e74134e109a7cf8196600772693c1f3363214d1f769d0f3c24cd3df47
  url: https://developers.pismo.io/pismo-docs/docs/account-collection-status
  role: primary_guide
  updated_at: '2026-04-29T15:16:42.000Z'
operations:
- v4-post-account-status
related_kus:
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-CORE-accounts-overview
- KU-CRED-minimum-amount-due-calculation
- KU-EVT-catalogue-account
grouping_rationale: single source page
---

# Account collection status

**KU ID:** `KU-CRED-account-collection-status` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/account-collection-status.md`:

> Credit card accounts have a collection status whose value can be either `NORMAL` or `OVERDUE`.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/account-collection-status.md`: Account collection status; Changing the account collection status

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/account-collection-status.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/account-collection-status · updatedAt: 2026-04-29T15:16:42.000Z

<!-- source:begin path=docs/card-issuing/account-collection-status.md part=0-end -->

# Account collection status

Credit card accounts have a collection status whose value can be either `NORMAL` or `OVERDUE`.

If a customer fails to pay at least the [minimum amount due (MAD)](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation) by a **specified number of days** after the due date, the account's collection status changes to `OVERDUE` and the account is blocked, so the customer cannot do a cash-out (purchase, cash withdrawal, and so on). You set the specified number of days in the program parameter **Number of days to block the account for unpaid statement**. If you don't set this parameter, it defaults to 10, and the account's status changes to `OVERDUE` on the day after the due date plus 10 days.

Note that changing the account collection status does not affect the [account status](https://developers.pismo.io/pismo-docs/docs/accounts-overview#account-status), which can block cash-outs even if the collection status is `NORMAL`. Customers can create their own account statuses using the [Create status](https://developers.pismo.io/pismo-docs/reference/v4-post-account-status) endpoint, so whether a particular account status blocks cash-outs depends on how the customer defines it.

The following table summarizes the relationships between account collection status and account status.

| Collection status | Account status blocks cash-outs | Can the customer do a cash-out? |
| :---------------- | :------------------------------ | :------------------------------ |
| NORMAL            | N                               | Y                               |
| NORMAL            | Y                               | N                               |
| OVERDUE           | N                               | N                               |
| OVERDUE           | Y                               | N                               |

# Changing the account collection status

As explained in the previous section, the **Number of days to block the account for unpaid statement** parameter determines when the collection status changes from `NORMAL` to `OVERDUE`—specifically, it is the number of days after the due date before the account is blocked. If the account holder pays the MAD within that period, the collection status never changes to `OVERDUE`. Once the collection status is `OVERDUE`, it reverts to `NORMAL` automatically if the account holder makes a payment that exceeds the MAD.

<Callout icon="📘" theme="info">
  You can use the <Anchor label="Update account collection status" target="_blank" href="ref:changeaccountcollectionstatus">Update account collection status</Anchor> endpoint to change the account’s collection status based on your own rules, enabling or blocking the account from performing cash‑out operations according to the defined collection status.
</Callout>

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /accounts/v4/statuses` | `v4-post-account-status` | Create status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |

### Operation essentials

- **`POST /accounts/v4/statuses`** (`v4-post-account-status`): security `BearerAuth`; required parameters none declared; required body fields `name`, `allowed_operations`; response statuses 201, 400, 409, 500; error codes in examples `EACC0004`, `EACC0018`, `EACC0000`, `EACC0003`, `EACC9999`; events `account-status-creation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `v4-post-account-status` | `account-status-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/account-collection-status.md`: updatedAt 2026-04-29T15:16:42.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/account-collection-status.md` | whole document | https://developers.pismo.io/pismo-docs/docs/account-collection-status | `fc29ba1e74134e10…` | 2026-04-29T15:16:42.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-CORE-accounts-overview` — Accounts
- `KU-CRED-minimum-amount-due-calculation` — Minimum amount due calculation
- `KU-EVT-catalogue-account` — Event catalogue: account
