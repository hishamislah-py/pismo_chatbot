---
ku_id: KU-CORE-legal-blocks
title: Legal blocks (outdated)
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/legal-blocks.md
  sha256: d8a753841cf3673cd84aef8d6a4e39903b93a3280df4760e9c64473e1bc1e999
  url: https://developers.pismo.io/pismo-docs/docs/legal-blocks
  role: primary_guide
  updated_at: '2026-03-18T15:13:17.000Z'
operations:
- get-accounts-v1-accounts
- patch-accounts-v2-accounts-accountId-status
related_kus:
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-EVT-catalogue-account
- KU-PAY-hold-funds
grouping_rationale: single source page
---

# Legal blocks (outdated)

**KU ID:** `KU-CORE-legal-blocks` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/legal-blocks.md`:

> A legal or judicial block is a block that is placed on an account for legal reasons. A legal block prevents or limits financial movement within the account. The Pismo platform offers both total and partial legal blocks.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/legal-blocks.md`: Legal blocks (outdated); Total legal blocks; Get the current status; Sample response; Place a total legal block; Add a reason for a total legal block; Remove a total legal block

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/legal-blocks.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/legal-blocks · updatedAt: 2026-03-18T15:13:17.000Z

<!-- source:begin path=docs/core-platform/legal-blocks.md part=0-end -->

# Legal blocks (outdated)

> 🚧 Deprecation notice
>
> This functionality is scheduled to be deprecated. This is a continuous improvement action for the platform. For any new deployments, use [Hold funds](https://developers.pismo.io/pismo-docs/docs/hold-funds) instead.

A legal or judicial block is a block that is placed on an account for legal reasons. A legal block prevents or limits financial movement within the account. The Pismo platform offers both total and partial legal blocks.

# Total legal blocks

If a total legal block is placed on an account, the Pismo platform blocks all financial movement into or out of the account. A total legal block is also called a **levy**.

## Get the current status

To find out if an account is totally blocked, you need to get its current status. You do this using the [Get account details](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts) endpoint. The account is totally blocked if the `status` field of the response is set to "BLOCKED". The following sample response shows that the account in question is blocked.

### Sample response

```json
{
  "available_limit": 11.0,
  "program_type": "DEBIT",
  "current_cicle": null,
  "org": "TN-f60b5e18-9f53-46ce-953b-b81ddf123456",
  "document_number": "97835021234",
  "program_name": "Pismo-Prog-Debit",
  "entity_type": "PHYSICAL",
  "current_balance": null,
  "name": "Test Name",
  "acquisition_id": 16468012,
  "email": "test@email.com",
  "status": "BLOCKED"
}
```

## Place a total legal block

> 📘
>
> The Pismo platform does not distinguish between total legal blocks and other types of total blocks. In both cases, the account status is simply changed to "BLOCKED". If you need to clarify that an account is blocked for legal reasons, you can do so by [adding a reason for the block](https://developers.pismo.io/pismo-docs/docs/legal-blocks#add-a-reason-for-a-total-legal-block).

You place a total legal block on an account by changing its `status` to "BLOCKED". You do this by calling the [Update account status](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v2-accounts-accountid-status) endpoint and passing the following payload in the body of the request:

```json
{
  "status": "BLOCKED"
}
```

## Add a reason for a total legal block

There is currently no endpoint for adding reasons, but you can contact Pismo to implement status change reasons for you. See [Account status change reasons](accounts-overview#account-status-reasons) for more info.

## Remove a total legal block

The act of removing a total legal block on an account is called a **full legal unlock**. You perform a full legal unlock by calling the [Update account status](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v2-accounts-accountid-status) endpoint and passing the following payload in the body of the request:

```json
{  
  "status": "NORMAL"  
}
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /accounts/v1/accounts/{accountId}` | `get-accounts-v1-accounts` | Get account | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `PATCH /accounts/v2/accounts/{accountId}/status` | `patch-accounts-v2-accounts-accountId-status` | Update status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |

### Operation essentials

- **`GET /accounts/v1/accounts/{accountId}`** (`get-accounts-v1-accounts`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 404, 500; error codes in examples none; events none listed.
- **`PATCH /accounts/v2/accounts/{accountId}/status`** (`patch-accounts-v2-accounts-accountId-status`): security `BearerAuth`; required parameters `accountId` (path); required body fields `status`; response statuses 204, 400, 404, 500; error codes in examples none; events `account-status-change-2`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-accounts-v2-accounts-accountId-status` | `account-status-change-2` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/legal-blocks.md`: updatedAt 2026-03-18T15:13:17.000Z.
- The source title marks the page as outdated: "Legal blocks (outdated)".

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/legal-blocks.md` | whole document | https://developers.pismo.io/pismo-docs/docs/legal-blocks | `d8a753841cf3673c…` | 2026-03-18T15:13:17.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-PAY-hold-funds` — Hold funds
