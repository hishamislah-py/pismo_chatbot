---
ku_id: KU-GS-pismo-platform-onboarding
title: Onboarding for new customers
category: getting_started
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/pismo-platform-onboarding.md
  sha256: 06445d2f3712f0f78584c87f24955d61fadd4ec7b5608c34403182c81844da63
  url: https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding
  role: primary_guide
  updated_at: '2026-07-16T12:24:04.000Z'
operations: []
related_kus:
- KU-AUTH-pismo-platform-security-guide
- KU-CC-get-started-control-center
- KU-CC-users
- KU-GS-platform-overview-and-solutions
- KU-GS-setup-overview
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Onboarding for new customers

**KU ID:** `KU-GS-pismo-platform-onboarding` · **Category:** Getting started · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/get-started/pismo-platform-onboarding.md`:

> As a new customer, you'll follow an onboarding process to create your organization, access required tools and systems, and configure authentication. The exact steps vary depending on the products you plan to build—banking, card issuing, lending, and so on—but the overall process follows a common pattern.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/pismo-platform-onboarding.md`: Onboarding for new customers; Planning; Organization creation; Pismo Service Desk access; Test and production environment access; Pismo Control Center access; Authentication set up; Next steps

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/pismo-platform-onboarding.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding · updatedAt: 2026-07-16T12:24:04.000Z

<!-- source:begin path=docs/get-started/pismo-platform-onboarding.md part=0-end -->

# Onboarding for new customers

As a new customer, you'll follow an onboarding process to create your organization, access required tools and systems, and configure authentication. The exact steps vary depending on the products you plan to build—banking, card issuing, lending, and so on—but the overall process follows a common pattern.

Throughout the onboarding process, you work closely with your Pismo support team. This guide walks you through the steps you’ll take together.

# Planning

Your Pismo support team will schedule planning sessions with you to shape your onboarding path. These sessions build on earlier conversations about your business goals, current challenges, desired products, and more.

# Organization creation

Your support team creates your organization (known as your org) on the Pismo platform. The organization specifies your company’s details, such as its legal name, address, and time zone.

> 📘 Some technical context
>
> Pismo uses core objects and has a built-in object hierarchy. The organization is the root object on the Pismo platform—a container for all your programs, accounts, and customers.
>
> When your organization is created, you receive an org ID (also referred to as a tenant ID), which looks like TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be.
>
> Most API endpoint calls require this identifier, typically passed in the header.
>
> For a comprehensive overview, refer to [Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview).

To create your organization, the support team will ask for the following information:

* Company's legal name
* Company’s preferred name on the Pismo platform (this can be the same as the legal name)
* Company’s document number, which is the unique company ID (such as a government tax ID or business registration number)
* Address
* Legal representative (person or entity)
* Email of the person at your company who can be contacted if necessary. This person is also assigned the Admin role in Control Center, which means they can create and edit Control Center users. You can add the Admin role to other users later, and even remove the role from this initial user. For more information, refer to [Create and edit users](https://developers.pismo.io/pismo-docs/docs/add-a-user).
* Currency
* Time zone

# Pismo Service Desk access

The Pismo Service Desk is where you submit requests, resolve issues, and ask questions. To request access, refer to [Request access to Pismo resources](https://developers.pismo.io/pismo-docs/docs/requests-for-access).

Keep these two points in mind:

* From the **Settings** dropdown, select **Access request**, then select **Service Desk Portal**.
* In the **Description** field, enter the email addresses of all users who need access.

Your support team can help if needed.

# Test and production environment access

Your support team sets up access to two environments:

* **Test environment**—A non‑production environment used to test new and updated features. If you prefer to use your own test environment, let your support team know.
* **Production environment**—A live environment used to process actual customer data.

Additionally, you can use tools like Postman with Pismo's pre-built collections to test API endpoints before going live. For more information, refer to [Test Pismo APIs with Postman](https://developers.pismo.io/pismo-docs/docs/testing-pismo-api-endpoints-with-postman).

# Pismo Control Center access

Control Center is a web-based interface you can use to complete many tasks without using REST APIs. Your support team sets up your access. After that, the people in your company assigned the Admin role create and manage users. For more information, refer to [Get started with Control Center ](https://developers.pismo.io/pismo-docs/docs/get-started-building-control-center).

# Authentication set up

To access Pismo APIs, you generate an access token linked to your org ID, which provides server-to-server (S2S) authentication. Your support team works with you to set up the appropriate authentication method.

| Method                     | Description                                                                                                                                                                                                                                                                                                                         |
| :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Basic (client credentials) | Basic S2S authentication uses a **server\_key** and **server\_secret**, like username/password                                                                                                                                                                                                                                      |
| OpenID Connect (preferred) | OpenID Connect (OIDC) provides greater security, supports multi-tenancy, and supports role-based access including third-party access. With OIDC, you generate public and private RSA key pairs, then generate a JSON Web Token (JWT) for each key pair. You share the public key with Pismo and sign the JWT with your private key. |
| OAuth2                     | OAuth2 follows the RFC 6749 specification, providing secure token-based authentication. With OAuth2, Pismo obtains the access tokens using the Client credentials grant type.                                                                                                                                                       |

Additionally, Mutual Transport Layer Security (mTLS) is mandatory for all API calls to the Pismo platform to ensure compliance with security regulations.

For a comprehensive overview, refer to the [Pismo platform security guide.](https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide)

# Next steps

With ongoing support and guidance from your Pismo team, you’ll set up your programs and accounts. Refer to [Start building](https://developers.pismo.io/pismo-docs/docs/start-building) to get started.

<br />
<!-- source:end -->

## Lifecycle status

- `docs/get-started/pismo-platform-onboarding.md`: updatedAt 2026-07-16T12:24:04.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/pismo-platform-onboarding.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding | `06445d2f3712f0f7…` | 2026-07-16T12:24:04.000Z |

## Related knowledge units

- `KU-AUTH-pismo-platform-security-guide` — Security guide for Pismo platform
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CC-users` — Control Center users: create, edit, export and audit
- `KU-GS-platform-overview-and-solutions` — Pismo platform overview, main solutions and where to start
- `KU-GS-setup-overview` — Core objects
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
