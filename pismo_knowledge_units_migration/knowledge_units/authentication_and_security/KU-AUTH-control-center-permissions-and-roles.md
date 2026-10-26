---
ku_id: KU-AUTH-control-center-permissions-and-roles
title: Control Center permissions, roles and API permission groups
category: authentication_and_security
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/platform-authentication-in-control-center.md
  sha256: 43ff3613d0b0f67b9b6b4ef61f36766ae8a031ceaa1b0107c11f4c70483b6621
  url: https://developers.pismo.io/pismo-docs/docs/platform-authentication-in-control-center
  role: primary_guide
  updated_at: '2026-03-18T15:10:51.000Z'
- path: docs/control-center/cc-api-permission-groups.md
  sha256: 1c8969be92abdc928c1315e689306f461aa2369e585c8a26ebad6abacefea682
  url: https://developers.pismo.io/pismo-docs/docs/cc-api-permission-groups
  role: primary_guide
  updated_at: '2026-07-13T10:47:20.000Z'
- path: docs/control-center/control-center-access-profiles-and-roles.md
  sha256: 951b3febc0906330ecb513d225d30bb4db1a8e817c0f39a3b724e0084a1fce11
  url: https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles
  role: primary_guide
  updated_at: '2026-06-04T13:29:10.000Z'
operations: []
related_kus:
- KU-AUTH-authentication-methods
- KU-AUTH-control-center-sso-and-openid
- KU-CC-users
grouping_rationale: Authorization model for Control Center and API permission groups.
---

# Control Center permissions, roles and API permission groups

**KU ID:** `KU-AUTH-control-center-permissions-and-roles` · **Category:** Authentication and security · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Authorization model for Control Center and API permission groups.

Scope as stated in `docs/control-center/platform-authentication-in-control-center.md`:

> Manage system permissions, which include the following:

Scope as stated in `docs/control-center/cc-api-permission-groups.md`:

> API permission groups control access to Pismo API endpoints. When creating an OpenID Connect (OIDC) authentication configuration, you must apply at least one permission group to it. Applied permission groups define the API endpoints you can access using OpenID access tokens generated from the configuration.

Scope as stated in `docs/control-center/control-center-access-profiles-and-roles.md`:

> Your permissions determine the information that's available to you and the actions that you can perform. Permissions are a collection of roles assigned to your user account, based on tasks you need to perform. If you can't access certain menu items or screens, you might not have the correct role.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/platform-authentication-in-control-center.md`: Permissions; Authentication types
- `docs/control-center/cc-api-permission-groups.md`: Permission groups
- `docs/control-center/control-center-access-profiles-and-roles.md`: User permissions and roles; Roles

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/platform-authentication-in-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/platform-authentication-in-control-center · updatedAt: 2026-03-18T15:10:51.000Z

<!-- source:begin path=docs/control-center/platform-authentication-in-control-center.md part=0-end -->

# Permissions

Manage system permissions, which include the following:

* [Access keys](https://developers.pismo.io/pismo-docs/docs/access-keys-for-basic-authentication)—With basic authentication, Pismo provides you with an encryption key pair (a server key and a secret key). These are the credentials your client applications will use to connect to the Pismo platform. You can view all access keys related to your organization and generate new keys.
* [OpenID ](https://developers.pismo.io/pismo-docs/docs/openid-configurations)—Add and manage OpenID authentication configurations for an organization.
* [Permission groups](https://developers.pismo.io/pismo-docs/docs/api-permission-groups)— View API permission groups, which control access to each of the platform APIs. This is only applicable if you use OpenID Connect for authentication.

For more information about managing users, refer to [Users](https://developers.pismo.io/pismo-docs/docs/users).

## Authentication types

The Pismo platform supports two types of authentication:

* **Basic authentication with client credentials** (also known as S2S)—This method is the most common among clients. For more information about basic authentication on the Pismo platform, refer to [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials).
* **OpenID Connect for Servers**—In this method, the clients will use a JSON Web Token (JWT) to perform the authentication. For more information about with OpenID Connect authentication on the Pismo platform, refer to [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid).
<!-- source:end -->

### Source 2: `docs/control-center/cc-api-permission-groups.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cc-api-permission-groups · updatedAt: 2026-07-13T10:47:20.000Z

<!-- source:begin path=docs/control-center/cc-api-permission-groups.md part=0-end -->

# Permission groups

API permission groups control access to Pismo API endpoints. When creating an OpenID Connect (OIDC) authentication configuration, you must apply at least one permission group to it. Applied permission groups define the API endpoints you can access using OpenID access tokens generated from the configuration.

For more information about creating OIDC authentication configurations, refer to [OpenID Connect](https://developers.pismo.io/pismo-docs/docs/openid-configurations).

For more information about OIDC authentication on the Pismo platform, refer to [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid).

To view the list of available permission groups for your organization, from the main menu, select **Users & permissions** > **Permission groups**. Use the search fields and filter options to refine and sort the list.

From Control Center, you can:

* View the permission groups available for your organization
* Identify the permission group required to access a specific endpoint
* Determine which endpoints are included in a permission group
* Verify whether an account ID is required to access an endpoint

<Image align="center" alt="screenshot showing an excerpt of the API permission groups screen" border={true} src="https://files.readme.io/2ff3f3a28892b35cdf730738718de470648722f1e0434880b8b568b8b4a1e7cc-permission-groups-without-callouts.png" className="border" />
<!-- source:end -->

### Source 3: `docs/control-center/control-center-access-profiles-and-roles.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles · updatedAt: 2026-06-04T13:29:10.000Z

<!-- source:begin path=docs/control-center/control-center-access-profiles-and-roles.md part=0-end -->

# User permissions and roles

Your permissions determine the information that's available to you and the actions that you can perform. Permissions are a collection of roles assigned to your user account, based on tasks you need to perform. If you can't access certain menu items or screens, you might not have the correct role.

For help with your permissions, contact your Control Center administrator or a user who has the Admin or User manager role.

# Roles

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Role
      </th>

      <th style={{ textAlign: "left" }}>
        Role name
      </th>

      <th style={{ textAlign: "left" }}>
        Write access (view/edit/add)
      </th>

      <th style={{ textAlign: "left" }}>
        Read access (view only)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Accounts operator
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-accounts-operator
      </td>

      <td style={{ textAlign: "left" }}>
        Edit cards and accounts information, including all information in accounts management
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Accounts viewer
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-accounts-viewer
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        View cards and accounts information
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Admin
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-admin
      </td>

      <td style={{ textAlign: "left" }}>
        Edit access to all screens and functions, except accounts and disputes management

        Edit the access keys for an organization
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        API keys approver
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-api-approver
      </td>

      <td style={{ textAlign: "left" }}>
        Approve dual approval requests for creating or deactivating access keys and for creating, editing, or deactivating OpenID authentication configurations
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Auditor
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-auditor
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        View user profiles and user activity logs. View some program information
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Backoffice approver
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-backoffice-approver
      </td>

      <td style={{ textAlign: "left" }}>
        Approve dual approval requests for account changes
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Backoffice operator
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-backoffice-operator
      </td>

      <td style={{ textAlign: "left" }}>
        Edit all information related to accounts and disputes management
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Backoffice viewer
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-backoffice-viewer
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        View disputes, cards, and accounts information
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Collections analyst
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-collection-analyst
      </td>

      <td style={{ textAlign: "left" }}>
        Edit account and card statuses
      </td>

      <td style={{ textAlign: "left" }}>
        View all account information
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Seller management admin
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-seller-mgmt-admin
      </td>

      <td style={{ textAlign: "left" }}>
        Manage marketplaces, merchants, and creditor operations including MDR and settlement\
        Note: To use Seller management in Control Center, you must have purchased it. Contact your Pismo representative for details.
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Setup advanced
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-setup-advanced
      </td>

      <td style={{ textAlign: "left" }}>
        Edit flex controls
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Setup advanced viewer
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-setup-advanced-viewer
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        View flex controls
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Setup approver
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-setup-approver
      </td>

      <td style={{ textAlign: "left" }}>
        Approve dual approval requests for program information and selected financial information (including program parameters)
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Setup operator
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-setup-operator
      </td>

      <td style={{ textAlign: "left" }}>
        Edit program information and selected financial information (including processing codes, transaction types, transaction categories, fee models, and interest plans)
      </td>

      <td style={{ textAlign: "left" }}>
        View flex controls
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Setup viewer
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-setup-viewer
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        View program information and selected financial information (including processing codes and transaction types, transaction categories, fee models, and interest plans).\
        View flex controls
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        User manager
      </td>

      <td style={{ textAlign: "left" }}>
        controlc-user-manager
      </td>

      <td style={{ textAlign: "left" }}>
        Create and edit user profiles, and export an organization's user list
      </td>

      <td style={{ textAlign: "left" }}>
        View user activity logs
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## Lifecycle status

- `docs/control-center/platform-authentication-in-control-center.md`: updatedAt 2026-03-18T15:10:51.000Z.
- `docs/control-center/cc-api-permission-groups.md`: updatedAt 2026-07-13T10:47:20.000Z.
- `docs/control-center/control-center-access-profiles-and-roles.md`: updatedAt 2026-06-04T13:29:10.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/platform-authentication-in-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/platform-authentication-in-control-center | `43ff3613d0b0f67b…` | 2026-03-18T15:10:51.000Z |
| `docs/control-center/cc-api-permission-groups.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cc-api-permission-groups | `1c8969be92abdc92…` | 2026-07-13T10:47:20.000Z |
| `docs/control-center/control-center-access-profiles-and-roles.md` | whole document | https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles | `951b3febc0906330…` | 2026-06-04T13:29:10.000Z |

## Related knowledge units

- `KU-AUTH-authentication-methods` — API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys
- `KU-AUTH-control-center-sso-and-openid` — Control Center SSO and OpenID Connect configuration
- `KU-CC-users` — Control Center users: create, edit, export and audit
