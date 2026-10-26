---
ku_id: KU-BANK-divisions-and-hierarchies
title: Divisions and hierarchies
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/divisions.md
  sha256: e5ec5f76908812e52c4623c21c284310a2e51935142e3ef3ee35f6ba0fb8e8c9
  url: https://developers.pismo.io/pismo-docs/docs/divisions
  role: primary_guide
  updated_at: '2026-09-09T16:44:46.000Z'
- path: docs/core-banking/hierarchies-2.md
  sha256: 140d5195f88ff8a20361b8cdfea9fa6aa553ef49576637f8897ed03d8e7ce98b
  url: https://developers.pismo.io/pismo-docs/docs/hierarchies-2
  role: primary_guide
  updated_at: '2026-09-17T14:08:03.000Z'
operations:
- get-division-by-code-v2
- getHierarchy
- list-division-v2
- patch-division-v2
- post-account
- post-create-holiday-calendar
- post-division-v2
- post-hierarchies
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--hierarchies
- KU-API-platform-setup-holidays--holiday-calendar
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-GS-program-types
- KU-GS-setup-overview
grouping_rationale: Organisational structure for transaction banking.
---

# Divisions and hierarchies

**KU ID:** `KU-BANK-divisions-and-hierarchies` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Organisational structure for transaction banking.

Scope as stated in `docs/core-banking/divisions.md`:

> Divisions model an organization’s operational structure, mapping regions, countries, branches, and business units into a single hierarchy so clients can scope configuration, control product availability, and inherit operational settings.

Scope as stated in `docs/core-banking/hierarchies-2.md`:

> Every large company has its own way of structuring its business. A global bank, for example, has a corporate headquarters with global regions, which break down into countries that have states, that have cities where you find branches.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/divisions.md`: Divisions; When to use divisions; Core concepts; API; Modeling patterns and best practices; Best practices; Operational rules and governance; Program binding; State and change management; Monitoring and alerts; Example division tree; Example API snippets; Create a division; Update division timezone and administrative division; Get division; Quick checklist before rollout
- `docs/core-banking/hierarchies-2.md`: Hierarchies; Create hierarchies, levels, and divisions; Bind a program to a division; Other hierarchy endpoints

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 8 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/divisions.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/divisions · updatedAt: 2026-09-09T16:44:46.000Z

<!-- source:begin path=docs/core-banking/divisions.md part=0-end -->

# Divisions

Divisions model an organization’s operational structure, mapping regions, countries, branches, and business units into a single hierarchy so clients can scope configuration, control product availability, and inherit operational settings.

Divisions are assigned to accounts and serve as the primary reference for account‑level behavior, especially time‑related settings. So assigning accounts to divisions ensures posting, settlement, and business‑date calculations follow the correct local time on global, 24/7 platforms.

Beyond timezones, divisions govern operational rules such as cycle closing and posting windows, allowing different parts of the organization to run distinct schedules that reflect local market practices or regulatory requirements. By binding program sets to divisions, you can also restrict which products can be created in each region or business unit, enforcing product availability and operational boundaries.

<Callout icon="📘" theme="info">
  **Note**

  Cycle‑closing rules are not configured at the account level, but can be configured at program, organization, or division level.
</Callout>

# When to use divisions

You use divisions to:

* Represent geographic regions, business units, or hybrid models
* Enforce product availability per region or business line
* Define local operational schedules such as cycle closing and posting windows
* Link to [Holiday calendar](https://developers.pismo.io/pismo-docs/reference/post-create-holiday-calendar) for holiday‑aware processing

# Core concepts

Refer to these core concepts when creating divisions.

| **Concept**          | **Description**                                                                                                                                                                                                                                                                               |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hierarchy**        | Divisions form a parent → child tree.                                                                                                                                                                                                                                                         |
| **Inheritance**      | Children inherit parent settings unless explicitly overridden.                                                                                                                                                                                                                                |
| **Scope**            | Divisions scope timezones, cycle rules, calendars, and program bindings.                                                                                                                                                                                                                      |
| **Program binding**  | A division is bound to a single program set. Updating the binding replaces the previous set. Programs refer to financial product offerings, such as credit and debit. For details about programs, refer to [Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview#program) and [Program types](https://developers.pismo.io/pismo-docs/docs/program-types). |
| **Holiday calendar** | Holiday calendars are separate entities for calendars and holidays. Divisions can link to them to inherit holiday and working-day rules. Refer to [Create holiday calendar](https://developers.pismo.io/pismo-docs/reference/post-create-holiday-calendar) for details.                                                                    |

<Callout icon="📘" theme="info">
  **Note**

  * The Pismo platform traverses up the division tree to resolve missing values such as timezone.
  * If no value is found anywhere in the hierarchy, the Pismo platform defaults to UTC.
</Callout>

# API

Use these endpoints to manage divisions.

| Endpoint                                    | Description                                                                                                                 |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2)     | Defines a division’s geographic scope and sets its code, hierarchy ID, level ID, or links it to an administrative division. |
| [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2)    | Modifies an existing division’s configuration, for example its administrative division, timezone, or program.               |
| [Get division](https://developers.pismo.io/pismo-docs/reference/get-division-by-code-v2) | Gets the configuration for a specific division.                                                                             |
| [List division](https://developers.pismo.io/pismo-docs/reference/list-division-v2)       | Returns all divisions and their configurations.                                                                             |

# Modeling patterns and best practices

Divisions define an organization’s operational structure, while [Holiday calendar](https://developers.pismo.io/pismo-docs/reference/post-create-holiday-calendar) captures calendar behavior like holidays and working days, linking a division to an administrative division lets it inherit those calendar rules. In practice, organizations model divisions to suit their needs, many banks mirror geography (Global → Region → Country → Branch) to manage local regulations, holidays, and time zones, while others use business‑line segmentation (Retail, Corporate, Treasury) to separate product sets and operational rules.

A common and recommended approach is a hybrid model that combines geography and business lines. For example, create country-level divisions and then separate retail and corporate subdivisions within each country. This lets you apply regulatory controls and business policies with greater precision.

Less commonly, divisions are organized around processing windows or time zones when timing is the primary concern.

Here is a sample division model for your reference.

| **Model**                      | **Structure / Notes**                                                 |
| ------------------------------ | --------------------------------------------------------------------- |
| **Geographic**                 | Global → Region → Country → Branch                                    |
| **Business unit**              | Organization → Business Unit (Retail, Corporate) → Team/Branch        |
| **Hybrid (recommended)**       | Global → Region → Country → (Retail / Corporate) → Branch             |
| **Time‑based (special cases)** | Use only when processing windows or timezones are the primary concern |

## Best practices

* Keep hierarchy as shallow as practical.
* Define global defaults at high levels and override only when necessary.
* Document each division’s purpose and program bindings.
* Test posting, settlement, cycle closing, and holiday handling across divisions and linked calendars.

# Operational rules and governance

## Program binding

Use the [Create](https://developers.pismo.io/pismo-docs/reference/post-division-v2) or the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint to bind a program set. Any subsequent calls to this endpoint replaces the division’s previous program set, use bindings to restrict product creation and enforce product availability.

## State and change management

Treat division updates as configuration changes and maintain audit logs. Plan safe rollouts and test changes in staging before production.

## Monitoring and alerts

Track changes to division program sets and calendar links. Alert on unexpected program updates or calendar mismatches.

## Example division tree

<Image align="center" alt="Example division tree" caption="Figure 1: Example division tree" src="https://files.readme.io/f114c999c703730052cb9c39e5c2c6e760d3773b0b62e8fbb9407459eb89883a-timezone-hierarchy-diagram_v3.png" />

# Example API snippets

## Create a division

Use [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) to create and define a division and its hierarchy.

```json
{
  "division_id": "<your_division_id>",
  "division_code": "my-division",
  "level_id": "<your_level_id>",
  "parent_code": "my-parent-division",
  "name": "NORAM",
  "description": "North American regional division"
}
```

## Update division timezone and administrative division

[Update an existing division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) by specifying a division code in the URL path. This is a sample request for updating time zone and administrative division.

```json
{
  "timezone": "America/New_York",
  "administrative_division_id": "admin-na-01"
}
```

## Get division

Use [Get division](https://developers.pismo.io/pismo-docs/reference/get-division-by-code-v2) to return a list of division configurations.

```json
{
  "hierarchy_id": "9bb95e15-c0e6-4c84-b644-350c76a83358",
  "level_id": "7d574f66-ebd0-4b83-85a1-98ce7569e5c3",
  "name": "NORAM",
  "division_id": "6f8a456a-8b1a-4022-a2f8-7612595330b5",
  "administrative_division_id": 13,
  "parent_code": "my-parent-division",
  "description": "North American regional division",
  "program_ids": [
    111,
    222,
    333
  ],
  "timezone": "Pacific Standard Time",
  "schema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "title": "Product",
    "description": "A product from Acme's catalog",
    "type": "object",
    "properties": {
      "product_id": {
        "description": "Product ID",
        "type": "integer",
        "format": "int64",
        "example": 1234,
        "x-readme-ref-name": "ProductID"
      }
    },
    "required": [
      "product_id"
    ]
  }
}
```

# Quick checklist before rollout

* Define division purpose and intended model: geographic, business, or hybrid.
* Map parent/child relationships and keep depth minimal.
* Set top‑level defaults such as timezone and cycle rules.
* Bind program sets and document them.
* Link administrative calendars where applicable.
* Test posting, settlement, cycle closing, and holiday handling.
* Maintain audit logs and monitoring for division changes.
<!-- source:end -->

### Source 2: `docs/core-banking/hierarchies-2.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/hierarchies-2 · updatedAt: 2026-09-17T14:08:03.000Z

<!-- source:begin path=docs/core-banking/hierarchies-2.md part=0-end -->

# Hierarchies

Every large company has its own way of structuring its business. A global bank, for example, has a corporate headquarters with global regions, which break down into countries that have states, that have cities where you find branches.

To support a variety of complex organizational structures, Pismo's corporate banking solution extends the Pismo platform by introducing a flexible, generic hierarchy that can accommodate any type of structure you need. A hierarchy is created under a single **organization (Org)** and is divided into levels. **Levels** are categories, such as Region, Country, or City, such as North America, Brazil, or Chile. Each level contains **divisions**. At the City level, for example, you might add the divisions London and Glasgow. Level is the primary element and may contain one or more divisions.

Hierarchies are typically organized by geography or corporate structure. Beneath the top level, you might define levels such as region, country, city, and branch. Another pattern is a corporate hierarchy in which a parent company like ABC Corp has subsidiaries such as ABC Services, ABC Construction, and ABC Technologies, each with its own business units.

| Level      | Description                                                                                                                                                                               |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1: Region  | Divisions in Level 1 could include: North America; South America; Europe, Middle East, Africa (EMEA)                                                                                      |
| 2: Country | Country divisions would be countries, such as Mexico, Brazil, Argentina, France                                                                                                           |
| 3: City    | Divisions in level 3: London, Manchester, Buenos Aires, Bariloche, etc. London and Manchester are child divisions of Brazil. Buenos Aires and Bariloche are child divisions of Argentina. |

Every hierarchy has a unique ID, as does each level and division. These IDs are used when creating account families. Each level has an index (0, 1, 2, ...), with 0 representing the Headquarters level or top level, and a description.

# Create hierarchies, levels, and divisions

You set up levels using the [Create hierarchy](https://developers.pismo.io/pismo-docs/reference/post-hierarchies) endpoint. After creating levels, use their IDs to add divisions using the [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) endpoint. A division is also used in scenarios related to [account creation](https://developers.pismo.io/pismo-docs/reference/post-account), defining [business holidays](https://developers.pismo.io/pismo-docs/reference/post-create-holiday-calendar), program binding, and so on.

A division element (for example, Country = United Kingdom) can have a parent/child relationship with a division at a different level. For example, London is not only a division element for the city level, it could also have United Kingdom as its parent division at the country level.

<Image align="center" alt="diagram showing hierarchies, levels, and divisions" caption="Parent/child relationships between divisions are represented by the red arrows." src="https://files.readme.io/b7074ff-hierarchy_concepts.png" />

# Bind a program to a division

You bind one program set to a division, and accounts inherit that set through the division hierarchy when you update the division using the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint. A program set defines the programs available to a division, and each division is associated with exactly one set. A subsequent call to this endpoint replaces the current program set with a new one, whether you are adding programs, removing programs, or switching to a different set entirely. Note that an account in the program set can belong to only one division. Refer to [Divisions](https://developers.pismo.io/pismo-docs/docs/divisions) for more details.

<Callout icon="📘" theme="info">
  **About program set**

  A program set is the group of `program_ids` associated with a division. When you [create](https://developers.pismo.io/pismo-docs/reference/post-division-v2) or [update](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) a division, you define which programs are allowed for that division.

  For details about programs, refer to [Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview#program).
</Callout>

# Other hierarchy endpoints

* [Get hierarchy](https://developers.pismo.io/pismo-docs/reference/gethierarchy): Enables you to view hierarchies by ID.
* [Get division](https://developers.pismo.io/pismo-docs/reference/get-division-by-code-v2): Gets information about a specific division.
* Further, you can optionally [update a division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) with certain configurations and behaviors. You can define a division's holidays, for example, and forbid transactions on those days. If your division has no defined holidays, every day is treated as a working day.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/holiday-calendar` | `post-create-holiday-calendar` | Create holiday calendar | `api-specs/Platform_setup_-_Holidays.yaml` | no | KU-API-platform-setup-holidays--holiday-calendar |
| `POST /corporate/v2/divisions` | `post-division-v2` | Create division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `PATCH /corporate/v2/divisions/{divisionCode}` | `patch-division-v2` | Update division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `GET /corporate/v2/divisions/{divisionCode}` | `get-division-by-code-v2` | Get division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `GET /corporate/v2/divisions` | `list-division-v2` | List division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `POST /corporate/v1/hierarchies` | `post-hierarchies` | Create hierarchy | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--hierarchies |
| `POST /corporate/v1/corporate-accounts` | `post-account` | Create transaction banking account | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `GET /corporate/v1/hierarchies/{hierarchyId}` | `getHierarchy` | Get hierarchy | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--hierarchies |

### Operation essentials

- **`POST /v1/holiday-calendar`** (`post-create-holiday-calendar`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`; response statuses 201, 400, 404, 409, 500; error codes in examples `EHLD0016`, `EHLD0050`, `EHLD0028`, `EHLD0030`, `EHLD0049`, `EHLD0052`, `EHLD0027`, `EHLD0001`; events none listed.
- **`POST /corporate/v2/divisions`** (`post-division-v2`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `hierarchy_id`, `level_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WDIV0015`, `WDIV0011`, `WDIV0005`, `WDIV0007`, `WDIV0006`, `WDIV0012`, `WDIV0018`, `WDIV0019`, `WDIV0017`, `WDIV0016`, `ECMN9999`; events `corporate-division-creation-2`.
- **`PATCH /corporate/v2/divisions/{divisionCode}`** (`patch-division-v2`): security `BearerAuth`; required parameters `divisionCode` (path); required body fields none declared; response statuses 204, 400, 401, 403, 404, 500; error codes in examples `WDIV0015`, `WDIV0011`, `WDIV0005`, `WDIV0007`, `WDIV0006`, `WDIV0008`, `WDIV0009`, `WDIV0010`, `WDIV0012`, `WDIV0018`, `WDIV0019`, `WDIV0002`, `WDIV0017`, `ECMN9999`; events `corporate-division-change-2`.
- **`GET /corporate/v2/divisions/{divisionCode}`** (`get-division-by-code-v2`): security `BearerAuth`; required parameters `divisionCode` (path); required body fields none declared; response statuses 200, 401, 403, 404, 500; error codes in examples `WDIV0002`, `WDIV0017`, `ECMN9999`; events none listed.
- **`GET /corporate/v2/divisions`** (`list-division-v2`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400; error codes in examples `WDIV0001`, `WDIV0011`, `WCMN0004`, `WCMN0006`; events none listed.
- **`POST /corporate/v1/hierarchies`** (`post-hierarchies`): security `BearerAuth`; required parameters none declared; required body fields `name`, `levels`; response statuses 201, 400, 401, 403, 500; error codes in examples `WHIE0001`, `WHIE0002`, `WHIE0003`, `WHIE0004`, `WHIE0005`, `WHIE0007`, `ECMN9999`; events `corporate-hierarchy-creation-1`.
- **`POST /corporate/v1/corporate-accounts`** (`post-account`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `program_id`, `applicant`, `external_account_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WCAC0013`, `WCAC0005`, `WCAC0006`, `WCAC0004`, `WCAC0016`, `WCAC0009`, `WDIV0002`, `WCAC0011`, `WCAC0014`, `ECMN9999`; events `corporate-corporate-account-creation-1`, `onboarding-succeeded-1`.
- **`GET /corporate/v1/hierarchies/{hierarchyId}`** (`getHierarchy`): security `BearerAuth`; required parameters `hierarchyId` (path); required body fields none declared; response statuses 200, 500; error codes in examples `ECMN9999`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-account` | `corporate-corporate-account-creation-1` |
| `patch-division-v2` | `corporate-division-change-2` |
| `post-division-v2` | `corporate-division-creation-2` |
| `post-hierarchies` | `corporate-hierarchy-creation-1` |
| `post-account` | `onboarding-succeeded-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/divisions.md`: updatedAt 2026-09-09T16:44:46.000Z.
- `docs/core-banking/hierarchies-2.md`: updatedAt 2026-09-17T14:08:03.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/divisions.md` | whole document | https://developers.pismo.io/pismo-docs/docs/divisions | `e5ec5f76908812e5…` | 2026-09-09T16:44:46.000Z |
| `docs/core-banking/hierarchies-2.md` | whole document | https://developers.pismo.io/pismo-docs/docs/hierarchies-2 | `140d5195f88ff8a2…` | 2026-09-17T14:08:03.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--hierarchies` — API reference: Banking - Transaction banking — Hierarchies
- `KU-API-platform-setup-holidays--holiday-calendar` — API reference: Platform setup - Holidays — Holiday calendar
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-program-types` — Program types
- `KU-GS-setup-overview` — Core objects
