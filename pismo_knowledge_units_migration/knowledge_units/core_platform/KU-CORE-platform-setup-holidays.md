---
ku_id: KU-CORE-platform-setup-holidays
title: Platform setup - Holidays and administrative divisions
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/platform-setup-holidays.md
  sha256: 13477a8b2dda2a32015c6d846a56033876636dbbadf2ed1777cf9b0c7a04fc36
  url: https://developers.pismo.io/pismo-docs/docs/platform-setup-holidays
  role: primary_guide
  updated_at: '2026-03-18T15:13:59.000Z'
operations:
- get-v1-admin-division
- get-v1-holidays
- post-holiday
- post-payments-v1-payments
- post-v1-admin-division
- post-v2-admin-division
- post-v2-holiday
related_kus:
- KU-API-core-platform-payment-methods--payments
- KU-API-platform-setup-divisions--administrative-divisions-deprecated
- KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated
- KU-API-platform-setup-holidays--holidays-deprecated
- KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat
- KU-BANK-calendars-and-holidays
- KU-CRED-calculating-interest-accruals
- KU-EVT-catalogue-other-domains
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Platform setup - Holidays and administrative divisions

**KU ID:** `KU-CORE-platform-setup-holidays` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/platform-setup-holidays.md`:

> By default, the Pismo platform operates 24 x 7 x 365 and allows platform activities  to occur at any time. However, in practice there are legal, security, and regulatory factors that restrict financial activities on certain days. These factors also can vary by location and type of business.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/platform-setup-holidays.md`: Platform setup - Holidays and administrative divisions; Endpoints for transaction banking; Define non-working days (weekends and holidays); Define administrative divisions

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/platform-setup-holidays.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/platform-setup-holidays · updatedAt: 2026-03-18T15:13:59.000Z

<!-- source:begin path=docs/core-platform/platform-setup-holidays.md part=0-end -->

# Platform setup - Holidays and administrative divisions

By default, the Pismo platform operates 24 x 7 x 365 and allows platform activities  to occur at any time. However, in practice there are legal, security, and regulatory factors that restrict financial activities on certain days. These factors also can vary by location and type of business.

Banks and other financial institutions operate on a schedule of **business days** (when normal business activity occurs) and **non-business days** (when offices are closed, limiting commerce and delaying access to funds). To help manage these situations, the platform provides the [Holidays API](https://developers.pismo.io/pismo-docs/reference/get-v1-holidays) and [Divisions API](https://developers.pismo.io/pismo-docs/reference/get-v1-admin-division), to automatically manage platform activities (for example, financial transactions) based on when and where the activities take place:

* **Holidays API**—Define the working and non-working days for your organization on the Pismo platform. This enables you to associate business rules that restrict certain platform activities based on the date or day of the week. Every holiday must be associated with at least one division.
* **Administrative divisions API**—Most businesses that use the Pismo platform operate in multiple states and countries around the world, which use different regulations and calendars. Divisions separate your organization into logical groups (usually by geography), enabling you to restrict operations according to different schedules. An `administrative_divisions_id` is required when configuring a non-working day.

# Endpoints for transaction banking

To support transaction banking accounts, the **v2** version of the [Administrative Divisions API](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) uses the following objects to define business dates and rules for permitting or blocking certain transaction activities on non-business dates:

* `working_days`: Defines business days (working days) when transactions can be processed.
* `metadata`: Uses [parameters](https://developers.pismo.io/pismo-docs/docs/posting-transactions-on-holidays#parameters) to specify business rules for holidays. For details, see [Posting Transactions on Holidays](https://developers.pismo.io/pismo-docs/docs/posting-transactions-on-holidays).

In transaction banking, an administrative division functions as a calendar, refer to [Calendars and holidays in transaction banking](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-transaction-banking) for more information.

> 📘 Notes
>
> * The **v1** version of the Holidays API was designed to support only national holidays. These endpoints are being maintained for **legacy implementations only.**
> * The **v2** version of the [Holidays](https://developers.pismo.io/pismo-docs/reference/post-v2-holiday) and [Administrative divisions](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) APIs offers greater flexibility in defining non-business days, including weekends and state, municipal, and local holidays, as well as accommodating specific business requirements.

# Define non-working days (weekends and holidays)

When configuring days, the Pismo platform uses numerical values. For example: 0 = Sunday and 6 = Saturday.

After you create divisions and holidays, you can apply different [interest accrual configurations](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals) to use for the accounts that you link to each division. For example, your configuration may allow fund transfers only on days 1 through 5. So, if a [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) request occurs on day 0 or 6, the platform blocks the transaction.

> 📘 Implementing divisions and a schedule of non-working days
>
> Configuring holidays and administrative divisions requires careful planning, because errors can lead to serious consequences. For instance, if a bank holiday is set incorrectly, it could lead to unexpected loss of access to funds or inability to process payments.
>
> Considerations include laws and regulations, days of the week and holidays, as well as other factors that may be specific to a particular state or region. Therefore, the APIs provide only the basic objects and data structures that you must configure, based on your own unique circumstances.
>
> For assistance and answers to any questions, contact the [Pismo Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk).

# Define administrative divisions

Many holidays are specific to a particular state or region, while others are celebrated more widely throughout the country. For instance, if your company does business in the UK, you can [define an administrative division](https://developers.pismo.io/pismo-docs/reference/post-v1-admin-division) for each member country and then [define the holidays](https://developers.pismo.io/pismo-docs/reference/post-holiday) for each division. For example:

* **New Year’s Day** and **New Year’s Day** are bank holidays throughout the UK.
* **2nd January** is a bank holiday in Scotland only.
* **St. Patrick’s Day** is a bank holiday in Northern Ireland only.

<Image alt="Diagram showing relationships between divisions, holidays, and dates" align="center" className="border" border={true} src="https://files.readme.io/d7212f3-Diagram_for_Holidays_and_Divisions_core_V6.png" />

<br />

Divisions are designed to have parent-child relationships. For example, a geographic division **1021** for **Maranhão** (state) can be a child of the division **1001** for **Brazil** (country) and a parent of division **1031** for **Bacabeira** (city).

> 📘
>
> Administrative division ID is a **required attribute** for configuring a holiday. You must provide an `administrative_division_id` value **unless** you provide an `external_id`, which lets you keep using an existing ID from another system.

<Table align={[null,"left",null]}>
  <thead>
    <tr>
      <th>
        Division A attributes
      </th>

      <th>
        Division B attributes
      </th>

      <th>
        Division C attributes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        AdministrativeDivision\_ID: 1001
        Name: Brazil
        Parent\_ID: NULL (top level)
      </td>

      <td>
        AdministrativeDivision\_ID: 1021\
        Name: Maranhão\
        Parent\_ID: 1001
      </td>

      <td>
        AdministrativeDivision\_ID:1031\
        Name: Bacabeira\
        Parent\_ID: 102
      </td>
    </tr>
  </tbody>
</Table>

```
[
    {
        "AdministrativeDivision_ID": 1001,
        "Parent_ID": null,
        "Org_ID": "TenantTest",
        "Name": "Brasil",
        "Type": "Country",
        "External_ID": "BR",
        "WorkingDays": "1,2,3,4,5",
        "Metadata": {"post_interest": false}
    },
    {
        "AdministrativeDivision_ID": 1021,
        "Parent_ID": 1001,
        "Org_ID": "TenantTest",
        "Name": "Maranhão",
        "Type": "State",
        "External_ID": "MA",
        "WorkingDays": "1,2,3,4,5",
        "Metadata": {"post_interest": false}
    },
    {
        "AdministrativeDivision_ID": 1031,
        "Parent_ID": 1021,
        "Org_ID": "TenantTest",
        "Name": "Bacabeira",
        "Type": "City",
        "External_ID": "MA_Bacabeira",
        "WorkingDays": "1,2,3,4,5",
        "Metadata": {"post_interest": false}
    }
]
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /holidays-core/v1/holiday` | `get-v1-holidays` | List holidays (deprecated) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-deprecated |
| `GET /divisions-core/v1/administrative-division/{id}` | `get-v1-admin-division` | Get admin division info (deprecated) | `api-specs/Platform_setup_-_Divisions.yaml` | **yes** | KU-API-platform-setup-divisions--administrative-divisions-deprecated |
| `POST /divisions-core/v2/administrative-division` | `post-v2-admin-division` | Create administrative division (deprecated) | `api-specs/Platform_setup_-_Divisions.yaml` | **yes** | KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated |
| `POST /holidays-core/v2/holiday` | `post-v2-holiday` | Create holiday (deprecated) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat |
| `POST /payments/v1/payments` | `post-payments-v1-payments` | Transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /divisions-core/v1/administrative-division` | `post-v1-admin-division` | Create administrative division (deprecated) | `api-specs/Platform_setup_-_Divisions.yaml` | **yes** | KU-API-platform-setup-divisions--administrative-divisions-deprecated |
| `POST /holidays-core/v1/holiday` | `post-holiday` | Create holiday (deprecated) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-deprecated |

### Operation essentials

- **`GET /holidays-core/v1/holiday`** (`get-v1-holidays`): security `S2SAuthentication`; required parameters `administrativeDivisionId` (query); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples `EHLD0016`, `EHLD0041`, `EHLD0039`, `EHLD0046`, `EHLD0048`, `EHLD0047`, `EHLD0001`; events none listed.
- **`GET /divisions-core/v1/administrative-division/{id}`** (`get-v1-admin-division`): security `S2SAuthentication`; required parameters `id` (path); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /divisions-core/v2/administrative-division`** (`post-v2-admin-division`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`; response statuses 201, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /holidays-core/v2/holiday`** (`post-v2-holiday`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `holiday_date`; response statuses 201, 400, 401, 404, 500; error codes in examples `EHLD0016`, `EHLD0028`, `EHLD0030`, `EHLD0031`, `EHLD0027`, `EHLD0001`; events none listed.
- **`POST /payments/v1/payments`** (`post-payments-v1-payments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `from`, `to`; response statuses 201, 202, 400, 409, 422, 500, 502; error codes in examples `WP2P0000`, `WP2P0019`, `EP2P9999`, `WP2P0005`, `WP2P0006`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WP2P0020`, `WP2P0013`, `WLDG0006`, `WP2P0010`, `WP2P0000`, `WP2P0000`, `ELDG500`, `EPCG501`, `EP2P9999`, `EP2P0001`, `EP2P0002`; events `authorization-authorization-event-1`.
- **`POST /divisions-core/v1/administrative-division`** (`post-v1-admin-division`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`; response statuses 201, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /holidays-core/v1/holiday`** (`post-holiday`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `holiday_date`, `working_date`; response statuses 201, 400, 401, 404, 500; error codes in examples `EHLD0016`, `EHLD0001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v1-payments` | `authorization-authorization-event-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/platform-setup-holidays.md`: updatedAt 2026-03-18T15:13:59.000Z.
- Links to `get-v1-holidays`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Holidays.yaml`.
- Links to `get-v1-admin-division`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Divisions.yaml`.
- Links to `post-v2-admin-division`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Divisions.yaml`.
- Links to `post-v2-holiday`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Holidays.yaml`.
- Links to `post-v1-admin-division`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Divisions.yaml`.
- Links to `post-holiday`, which is marked `deprecated: true` in `api-specs/Platform_setup_-_Holidays.yaml`.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/platform-setup-holidays.md` | whole document | https://developers.pismo.io/pismo-docs/docs/platform-setup-holidays | `13477a8b2dda2a32…` | 2026-03-18T15:13:59.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-API-platform-setup-divisions--administrative-divisions-deprecated` — API reference: Platform setup - Divisions — Administrative divisions (deprecated)
- `KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated` — API reference: Platform setup - Divisions — Administrative divisions V2 (deprecated)
- `KU-API-platform-setup-holidays--holidays-deprecated` — API reference: Platform setup - Holidays — Holidays (deprecated)
- `KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat` — API reference: Platform setup - Holidays — Holidays v2 - Transaction banking (deprecated)
- `KU-BANK-calendars-and-holidays` — Calendars, holidays and posting transactions on holidays in transaction banking
- `KU-CRED-calculating-interest-accruals` — Calculating interest accruals
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
