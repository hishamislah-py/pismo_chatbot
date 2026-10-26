---
ku_id: KU-GS-setup-overview
title: Core objects
category: getting_started
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/setup-overview.md
  sha256: a11698f010b71aefa6743c50af440252975b5eff403c85a07a2a352460d75628
  url: https://developers.pismo.io/pismo-docs/docs/setup-overview
  role: primary_guide
  updated_at: '2026-09-29T16:16:18.000Z'
operations:
- CreateProgramBasedOnTemplate
- customerV2Post
- get-v1-org
- patch-v1-orgs
- post-acquisitions-v3-s2s-applications
- post-v2-card
related_kus:
- KU-API-card-issuing-cards--cards
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--customers
- KU-API-platform-setup-organizations--orgs
- KU-API-platform-setup-programs--programs-part-01
- KU-CARD-cards-overview-1
- KU-CARD-get-started-card-issuing
- KU-CC-programs
- KU-CORE-accounts-overview
- KU-EVT-catalogue-account
- KU-EVT-catalogue-cards
- KU-EVT-catalogue-other-domains
- KU-GS-program-types
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Core objects

**KU ID:** `KU-GS-setup-overview` · **Category:** Getting started · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/get-started/setup-overview.md`:

> This guide describes the core objects that are configured during your onboarding process. Many endpoint calls address and interact with these core objects.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/setup-overview.md`: Core objects; Basic component structure; Organization; Program; Entity; Account; Customer; Other objects; Card

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/setup-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/setup-overview · updatedAt: 2026-09-29T16:16:18.000Z

<!-- source:begin path=docs/get-started/setup-overview.md part=0-end -->

# Core objects

This guide describes the core objects that are configured during your onboarding process. Many endpoint calls address and interact with these core objects.

The following diagram shows a high-level overview of an organization, programs, and the mapping of account customers to entities.

<Image align="center" alt="Graphical diagram displaying how account customers map to entities" border={true} src="https://files.readme.io/c470ae2-7a10590-diagram-core-objects2x.png" className="border" />

# Basic component structure

The Pismo platform has a built-in object hierarchy. The following table describes the platform's built-in object hierarchy and their basic relationships.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Object
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organization
      </td>

      <td>
        Defines your company or enterprise. Contains one or more programs.
      </td>
    </tr>

    <tr>
      <td>
        Program
      </td>

      <td>
        Defines a set of parameters for a group of accounts. A program has a [type](https://developers.pismo.io/pismo-docs/docs/program-types), such as credit, debit, or prepaid.
      </td>
    </tr>

    <tr>
      <td>
        Entity
      </td>

      <td>
        A **legal entity** (person, company, or organization). As an attribute, an entity object contains a government document number, such as a driver's license, as well as other legal information that identifies a person, company, or organization.

        Every customer is associated with an entity object. If you do not provide an entity object when calling the [Create customer](https://developers.pismo.io/pismo-docs/reference/customerv2post)  endpoint, Pismo automatically creates one. Within an organization, multiple customer records with different customer IDs can be linked to the same entity object, indicating that they represent the same person or company. This relationship can help identify and track a person’s or company’s activities across customer records within an organization and, potentially, across multiple organizations. To search organization data by entity ID, contact the  [Pismo Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk) and request access to this capability.
      </td>
    </tr>

    <tr>
      <td>
        Account
      </td>

      <td>
        Each account belongs to a single program. An attribute not defined for an account is inherited from its program.
      </td>
    </tr>

    <tr>
      <td>
        Customer
      </td>

      <td>
        Each account contains at least one customer, either an individual or company. Accounts can have multiple *customers* (typically to accommodate additional cardholders) but only one designated *owner*. A customer can only belong to one account.
      </td>
    </tr>
  </tbody>
</Table>

The first thing you need to do is work with Pismo to onboard your organization and add the first program to the Pismo platform. When those are in place, you can start creating accounts and customers, issuing cards, and calling Pismo API endpoints.

> 📘 Field details
>
> Specific field names, lengths, and ranges are not detailed in this guide. You can find this information in the API endpoint reference documentation.

# Organization

The Pismo implementation team works with you to set up your organization. The organization is the root object on the Pismo platform, which is the container for all your [programs](https://developers.pismo.io/pismo-docs/docs/setup-overview#program).

| Description                                                                                                 | Org element           | Example                 |
| :---------------------------------------------------------------------------------------------------------- | :-------------------- | :---------------------- |
| Your organization or company's legal name                                                                   | Official name         | Change the World LLC    |
| Your organization's preferred name on the Pismo platform                                                    | Organization name     | Change the World        |
| Your organization's document number                                                                         | Document number       | 08350504000143          |
| Street address name                                                                                         | Address               | Maple Lane              |
| Street address number                                                                                       | Number                | 900                     |
| Any additional address information, such as unit, floor, suite, and so on                                   | Complementary address | Suite 200               |
| Neighborhood, as some countries use assigned neighborhoods in addresses                                     | Neighborhood          | Shady Oaks              |
| Country postal code                                                                                         | Zipcode               | 12230660                |
| City                                                                                                        | City                  | London                  |
| State/Province/Region                                                                                       | State                 | SP                      |
| Country                                                                                                     | Country               | England                 |
| Your organization's legal representative                                                                    | Legal proxy name      | Pismo Organization LTDA |
| Email                                                                                                       | Email                 | `info@myorg.com`        |
| [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency numeric code; for example, 986 (Brazilian real) | Currency numeric code | 986                     |
| [Timezone name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)                               | Timezone              | America/Sao\_Paulo      |

When created, your organization is assigned an identifier that is referred to as either an **organization ID**, **org ID** or **tenant ID** and looks similar to this: `TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be`.

("`TN`" is short for *tenant*, the legacy term for organization.)

Refer to the following endpoints for specific details about organization fields.

* [Get organization](https://developers.pismo.io/pismo-docs/reference/get-v1-org)
* [Update organization](https://developers.pismo.io/pismo-docs/reference/patch-v1-orgs)

# Program

After you have set up your organization, you can use [Control Center](https://developers.pismo.io/pismo-docs/docs/cc-manage-programs) or [Programs API](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) to create your organization's first program. Program attributes depend on the [program type](https://developers.pismo.io/pismo-docs/docs/program-types).

> 📘 Control Center limitations
>
> You can perform most program configurations using Control Center. However, some configuration steps may still require you to work through the Pismo implementation team.

# Entity

An entity object contains legal information that identifies a person or a company. The [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoint creates a default entity object for the account owner based on document ID. You can also define an entity object with the [Create customer](https://developers.pismo.io/pismo-docs/reference/customerv2post) endpoint.

# Account

You can create an account with the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoint. For more information, refer to the [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview) guide.

# Customer

An account customer can be either a person or a company. When you create an account, the first customer—the account owner—is also created.  Accounts can have multiple customers, typically to accommodate primary and additional cardholders, but only one owner. A customer can only belong to one account.

Call the [Create customer](https://developers.pismo.io/pismo-docs/reference/customerv2post) endpoint to define either a person or company customer object and add this customer to an account. For more information, refer to the [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview) guide.

# Other objects

## Card

To get started issuing cards, refer to [Get started with card issuing](https://developers.pismo.io/pismo-docs/docs/get-started-with-card-issuing). You can issue a card with the [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card) endpoint.

Cards also come with associated *mode* objects for combination cards—cards that can be used for both credit and debit transactions. For more information, refer to [Create a combination card with modes](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#create-a-combination-card-with-card-modes).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /accounts/v2/customers` | `customerV2Post` | Create customer | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |
| `GET /orgs-core/v1/orgs/{id}` | `get-v1-org` | Get organization | `api-specs/Platform_setup_-_Organizations.yaml` | no | KU-API-platform-setup-organizations--orgs |
| `PATCH /orgs-core/v1/orgs` | `patch-v1-orgs` | Update organization | `api-specs/Platform_setup_-_Organizations.yaml` | no | KU-API-platform-setup-organizations--orgs |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /wallet/v2/cards` | `post-v2-card` | Create card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |

### Operation essentials

- **`POST /accounts/v2/customers`** (`customerV2Post`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `entity`, `customer`; response statuses 201, 400, 409, 500; error codes in examples none; events `account-account-owner-change-1`, `account-customer-creation-1`.
- **`GET /orgs-core/v1/orgs/{id}`** (`get-v1-org`): security `S2SAuthentication`; required parameters `id` (path), `x-tenant` (header); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples `EOA0030`, `EOA0035`, `EOA0100`, `EOA0001`; events none listed.
- **`PATCH /orgs-core/v1/orgs`** (`patch-v1-orgs`): security `S2SAuthentication`; required parameters `x-tenant` (header); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples `EOA0030`, `EOA0100`, `EOA0001`; events none listed.
- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /wallet/v2/cards`** (`post-v2-card`): security `BearerAuth`; required parameters `x-customer-id` (header); required body fields `name`, `type`; response statuses 200, 201, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `customerV2Post` | `account-account-owner-change-1` |
| `customerV2Post` | `account-customer-creation-1` |
| `post-v2-card` | `cards-create-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/get-started/setup-overview.md`: updatedAt 2026-09-29T16:16:18.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/setup-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/setup-overview | `a11698f010b71aef…` | 2026-09-29T16:16:18.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--customers` — API reference: Core platform - Accounts — Customers
- `KU-API-platform-setup-organizations--orgs` — API reference: Platform setup - Organizations — Orgs
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-CARD-cards-overview-1` — Cards management
- `KU-CARD-get-started-card-issuing` — Get started with card issuing
- `KU-CC-programs` — Control Center programs: create, edit, clone, export and import
- `KU-CORE-accounts-overview` — Accounts
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-program-types` — Program types
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
