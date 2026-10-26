---
ku_id: KU-CRED-holidays-in-credit-card-accounts
title: Holidays in credit card accounts
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/holidays-in-credit-card-accounts.md
  sha256: f829de9fd034db2f5adf4e732eaf627708a07ae48ca9d54de31c3e3db47a76de
  url: https://developers.pismo.io/pismo-docs/docs/holidays-in-credit-card-accounts
  role: primary_guide
  updated_at: '2026-03-18T15:22:04.000Z'
operations:
- patch-accounts-v1-accounts
- post-acquisitions-v3-s2s-applications
- post-holiday
- post-v1-admin-division
related_kus:
- KU-API-core-platform-accounts--accounts
- KU-API-platform-setup-divisions--administrative-divisions-deprecated
- KU-API-platform-setup-holidays--holidays-deprecated
- KU-EVT-catalogue-account
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Holidays in credit card accounts

**KU ID:** `KU-CRED-holidays-in-credit-card-accounts` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/holidays-in-credit-card-accounts.md`:

> The Pismo platform supports uninterrupted credit card transactions by default. However, financial institutions usually need to limit transactions on certain days, such as national or regional holidays. Errors setting up holidays can prevent customers from accessing funds or executing payments, so careful planning of holidays is essential.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/holidays-in-credit-card-accounts.md`: Holidays in credit card accounts; Administrative divisions and holidays; Creating administrative divisions; Division hierarchy; Setting up holidays within administrative divisions; Linking administrative divisions

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/holidays-in-credit-card-accounts.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/holidays-in-credit-card-accounts · updatedAt: 2026-03-18T15:22:04.000Z

<!-- source:begin path=docs/card-issuing/holidays-in-credit-card-accounts.md part=0-end -->

# Holidays in credit card accounts

The Pismo platform supports uninterrupted credit card transactions by default. However, financial institutions usually need to limit transactions on certain days, such as national or regional holidays. Errors setting up holidays can prevent customers from accessing funds or executing payments, so careful planning of holidays is essential.

# Administrative divisions and holidays

Since holidays vary from institution to institution and region to region, Pismo enables you to manage holidays using generic structures called **administrative divisions**. Holidays are assigned to divisions, and divisions are assigned to accounts, which inherit the holidays from those divisions.

Administrative divisions can also be nested. That is, a division can be a subdivision (or child) of another division (the parent). In this case, the subdivision inherits all the holidays defined in the parent division. When the subdivision is assigned to an account, the account inherits the holidays defined in the subdivision, as well as those defined in the parent division.

The following diagram illustrates these relationships. Suppose that Division C is assigned to Account 001. Account 001 then inherits the holiday that’s defined in Division C and also the holiday defined in Division A. It does not, however, inherit any holidays defined in Divisions B or D.

<Image alt="Relationships between divisions and holiday inheritence" align="center" src="https://files.readme.io/bf81862cf05adeed6c93ce1e025477d705e3dfdd3ba1a87802972b5c1f1733f2-Diagram_illustrating_Administrative_division_hierarchy_with_holidays.png" />

# Creating administrative divisions

Set up administrative divisions using the [Create administrative division](https://developers.pismo.io/pismo-docs/reference/post-v1-admin-division) endpoint. Then, create a hierarchical relationship between your divisions using the  `parent_id` field. Alternatively, you can use the `external_id` field if you want to use IDs from an external system such as an Enterprise Resource Planning (ERP) application.

Divisions are designed to be used generically. For example, you can define them to represent a **location** (Region > Country > State > City > Branch) or a **business function** (Operations > Information Technology).

## Division hierarchy

Suppose your organization is focused on serving Europe. In this case, you can make a top-level division named **Europe** (ID 1)with subdivisions for the various countries—**France** (ID 2), **Germany** (ID 3), and so on. In this case:

* Europe (region)\
  `id` = 1\
  parent\_id = null (this is the top-level division)
* France (country)\
  `id` = 2\
  `parent_id`= 1
* Germany (country)\
  `id`= 3\
  `parent_id`= 1

Similarly, you can subdivide each contry into smaller regions.

> 📘
>
> For this example, all of the `external_id` fields should be left blank, since it's using the `parent_id` field.

# Setting up holidays within administrative divisions

Use the [Create holiday](https://developers.pismo.io/pismo-docs/reference/post-holiday) endpoint to establish holidays within an administrative division.

> 🚧
>
> The Pismo platform uses the value in the `working_date` field to calculate a statement's real due date. So, this value must be a business date.

# Linking administrative divisions

After establishing administrative divisions and holidays, you can connect the divisions to credit card accounts. To set up and manage these connections, use the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) and [Update account information](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v1-accounts) endpoints. In both endpoints, you must provide the administrative division ID in the `administrative_division_id` field.

> 🚧
>
> To use a division holiday for a credit card account, you must associate the account with the division. Otherwise, the Pismo platform does not consider holidays when generating the real due date for a statement—not even national holidays.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /divisions-core/v1/administrative-division` | `post-v1-admin-division` | Create administrative division (deprecated) | `api-specs/Platform_setup_-_Divisions.yaml` | **yes** | KU-API-platform-setup-divisions--administrative-divisions-deprecated |
| `POST /holidays-core/v1/holiday` | `post-holiday` | Create holiday (deprecated) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-deprecated |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `PATCH /accounts/v1/accounts/{accountId}` | `patch-accounts-v1-accounts` | Update account | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |

### Operation essentials

- **`POST /divisions-core/v1/administrative-division`** (`post-v1-admin-division`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`; response statuses 201, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /holidays-core/v1/holiday`** (`post-holiday`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `holiday_date`, `working_date`; response statuses 201, 400, 401, 404, 500; error codes in examples `EHLD0016`, `EHLD0001`; events none listed.
- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`PATCH /accounts/v1/accounts/{accountId}`** (`patch-accounts-v1-accounts`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 401, 404, 500; error codes in examples none; events `account-account-change-2`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-accounts-v1-accounts` | `account-account-change-2` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/holidays-in-credit-card-accounts.md`: updatedAt 2026-03-18T15:22:04.000Z.
- Links to `post-v1-admin-division`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Divisions.yaml`.
- Links to `post-holiday`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Holidays.yaml`.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/holidays-in-credit-card-accounts.md` | whole document | https://developers.pismo.io/pismo-docs/docs/holidays-in-credit-card-accounts | `f829de9fd034db2f…` | 2026-03-18T15:22:04.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-platform-setup-divisions--administrative-divisions-deprecated` — API reference: Platform setup - Divisions — Administrative divisions (deprecated)
- `KU-API-platform-setup-holidays--holidays-deprecated` — API reference: Platform setup - Holidays — Holidays (deprecated)
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
