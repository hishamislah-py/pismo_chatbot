---
ku_id: KU-CC-control-center-navigation
title: Navigate Control Center
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/control-center-navigation.md
  sha256: c931116efc3f4ae04de1f0d7949fcaf065491aa094eb8e2babe8b53254afdfbf
  url: https://developers.pismo.io/pismo-docs/docs/control-center-navigation
  role: primary_guide
  updated_at: '2026-08-26T13:05:57.000Z'
operations: []
related_kus:
- KU-AUTH-control-center-permissions-and-roles
- KU-AUTH-control-center-sign-on-and-mfa
- KU-CC-accounts
- KU-CC-configuration-menus
- KU-CC-dual-approval
- KU-CC-lending
- KU-CC-seller-management-in-control-center
- KU-CC-users
- KU-GS-setup-overview
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Navigate Control Center

**KU ID:** `KU-CC-control-center-navigation` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/control-center/control-center-navigation.md`:

> A great place to begin with Control Center is by getting familiar with its layout. This overview guides you through the homepage, menus, and key features, so you’ll know exactly where to find what you need.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/control-center-navigation.md`: Navigate Control Center; Homepage; Main menu; Configurations; Customer operations; Users & permissions; Seller management; Organization menu; View and edit organization details; Switch organizations; Search; Notifications; Language selector; Profile menu; Access detailed report log information

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/control-center-navigation.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/control-center-navigation · updatedAt: 2026-08-26T13:05:57.000Z

<!-- source:begin path=docs/control-center/control-center-navigation.md part=0-end -->

# Navigate Control Center

A great place to begin with Control Center is by getting familiar with its layout. This overview guides you through the homepage, menus, and key features, so you’ll know exactly where to find what you need.

Keep in mind that your permissions determine the information that is available to you and the actions that you can perform. Permissions are a collection of roles assigned to your user account, based on tasks you need to perform. Contact your Control Center administrator if you have questions. For more information, refer to [User permissions and roles](https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles).

Use the following table to explore Control Center’s features, understand what you can do, and find links for more information.

| Feature                                                              | What you can do                                                                                                                          |
| :------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| [Homepage](https://developers.pismo.io/pismo-docs/docs/control-center-navigation#homepage)                   | View key information, including programs, announcements, and your favorites                                                              |
| [Main menu](https://developers.pismo.io/pismo-docs/docs/control-center-navigation#main-menu)                 | Access essential Control Center features                                                                                                 |
| [Organization menu](https://developers.pismo.io/pismo-docs/docs/control-center-navigation#organization-menu) | Switch between organizations and view and edit organization details                                                                      |
| [Search](https://developers.pismo.io/pismo-docs/docs/control-center-navigation#search)                       | Search for anything in Control Center                                                                                                    |
| [Notifications](https://developers.pismo.io/pismo-docs/docs/control-center-navigation#notifications)         | Get alerts, updates, and important messages                                                                                              |
| [Language selector](https://developers.pismo.io/pismo-docs/docs/control-center-navigation#language-selector) | Switch between English and Portuguese                                                                                                    |
| [Profile menu](https://developers.pismo.io/pismo-docs/docs/control-center-navigation#profile-menu)           | View information about your user ID, session, and version. You can also manage authentication methods, create a report log, and sign out |

# Homepage

The Control Center homepage displays as your landing page when you sign on and anytime you select **Home** from the main menu. The homepage highlights:

* Your programs
* Announcements about what's new, including upcoming features, important changes, and any pending actions, such as requests and approvals
* Your favorites. To add a favorite feature to your homepage, go to the main menu and select the star next to any item.
* A link to the Pismo Developers Portal for deeper technical resources

<Image align="center" alt="Control Center dashboard" border={true} src="https://files.readme.io/49167555dfe450b830c186096d4d104c90bc12eb3bb619daac26effb9ba71e4b-Screenshot_2025-12-15_at_3.02.01PM.png" className="border" />

# Main menu

The main menu connects you to the features and tools needed to build and manage your payment, banking, and lending programs. Access the main menu in the top left corner. Your permissions determine which features display on your menu. For for more information, refer to [User permissions and roles](https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles).

<Image align="center" alt="Control Center main menu" border={true} width="40% " src="https://files.readme.io/7ae1cd28acff4f02cbd2a1b941760359262258fde6d19798e8f0ca5523297156-Screenshot_2025-10-20_at_4.25.35_PM.png" className="border" />

## Configurations

Set up and manage your platform-wide, card, banking, and lending features.

<Image align="center" alt="Configurations menu " border={true} width="80% " src="https://files.readme.io/c5b0ff456e2b8aa315ca89a788083261194465455d3d5d94641c595bfd14579c-Screenshot_2026-08-26_at_9.04.43_AM.png" className="border" />

For more information about using each feature, refer to:

* [Platform configurations](https://developers.pismo.io/pismo-docs/docs/platform-configurations)
* [Card configurations](https://developers.pismo.io/pismo-docs/docs/cards-configurations)
* [Banking configurations ](https://developers.pismo.io/pismo-docs/docs/banking-configurations)
* [Lending configurations](https://developers.pismo.io/pismo-docs/docs/digital-lending)

## Customer operations

Manage customer accounts and transaction disputes.

<Image align="center" alt="Control center customer operations menu" border={true} width="50% " src="https://files.readme.io/569fa0f128f202c1b34a4a1c502dd415cdee682cc510fd981e22d62bca043620-customer-operations-control-center.png" className="border" />

For more information, refer to [Customer operations](https://developers.pismo.io/pismo-docs/docs/customer-operations).

## Users & permissions

Manage all aspects of user access, such as creating users and viewing their Control Center activity. Additionally, oversee system permissions, including access keys and API permissions groups.

<Image align="center" alt="Control center users and permissions menu" width="80% " src="https://files.readme.io/b8676148f058896d23b2563d735ce80208de038cfdb939719d1eba1aadb4c509-8_-_menu_users_and_perms_2.png" />

For more information about using each feature, refer to:

* [Users](https://developers.pismo.io/pismo-docs/docs/users)
* [Permissions](https://developers.pismo.io/pismo-docs/docs/platform-authentication-in-control-center)

## Seller management

Manage merchants that sell products through digital channels and at physical points of sale. To use Seller management in Control Center, your company must have purchased it and your permissions must include the **Seller management admin** role. For details about purchasing Seller management, contact your Pismo representative. To get access, contact your Control Center administrator.

<Image align="center" alt="Seller management menu" border={true} width="50% " src="https://files.readme.io/7cdf13d99e7ab814a4c44b7d7bad74320bb4e5ad84877d98b454c148b950bde6-Screenshot_2025-10-20_at_3.36.49_PM.png" className="border" />

For more information, refer to [Seller management](https://developers.pismo.io/pismo-docs/docs/seller-management-in-control-center).

# Organization menu

View and edit details about your organization, as well as switch between organizations if you're part of more than one. To open the organization menu, go to the Control Center header on the left.

<Image align="center" alt="Organization menu" border={true} width="40% " src="https://files.readme.io/35537c2ad91a76e0eb4d12bae837017fc9e4712020700f3dea6d25ad68255eac-org_image.png" className="border" />

The organization menu displays your company’s details, such as its legal name, address, and time zone. Pismo creates your organization when you onboard. For more information, refer to [Organization](https://developers.pismo.io/pismo-docs/docs/setup-overview#organization).

## View and edit organization details

To view and edit details about your organization:

1. Select **View organization details**.

2. If you want to edit these details, select **Edit**, then save your changes.

## Switch organizations

If you're part of more than one organization, you can switch between them without having to log out. Keep in mind that switching organizations might also change which features you can see and use. Your Control Center administrator assigns you specific permissions for each of your organizations.

To switch organizations, find the new organization using the search bar or from the list in **Your other organizations** and select the desired organization.

# Search

Find anything in Control Center by using the search bar in the top-right corner of the header.

<Image align="center" alt="Control Center search bar" border={true} width="40% " src="https://files.readme.io/42ce35c8ba8564e4f36a4d66fdbc3297dda29d9fce2cdf495bb2914471cc4fea-Search.png" className="border" />

# Notifications

Notifications announce upcoming features and key activities and alert you when you need to take action. View notifications from the notification icon (the bell) in the top-right corner of the header. When there's a new notification, you'll see a red badge on the icon. The number indicates how many notifications are unread.

<Image align="center" alt="Control Center notification icon" border={true} width="42% " src="https://files.readme.io/92fa6d5986367124362e9e8503aae08d5925e4685f94f9b4566b33790e6398a8-Notifications.png" className="border" />

Select the icon to open recent notifications. You can take these actions:

* Use the **Unread only** toggle to display only messages you haven't read yet.
* Select **Mark all as read** to mark all currently displayed messages as read.
* Select **View all notifications** to open the full, detailed notification page.

You’ll receive these types of notifications.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Notification type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Setup
      </td>

      <td>
        Notifies you about key activities, such as:

        <ul>
          <li>File download and upload requests</li>
          <li>New program creation requests</li>
          <li>Transaction details</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>
        Announcements
      </td>

      <td>
        Alerts you to application updates, new features, and scheduled maintenance
      </td>
    </tr>

    <tr>
      <td>
        Approval
      </td>

      <td>
        Notifies you about actions you need to take. For example, if you're using dual approval, you'll get notifications about requests and approvals. For more information, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).
      </td>
    </tr>
  </tbody>
</Table>

# Language selector

Select your language (English or Portuguese) from the language selector icon (the flag) in the top-right corner of the header.

<Image align="center" alt="Control Center language selector" border={true} width="40% " src="https://files.readme.io/623b41d19a61bf88a203b16b1d9c7ce6c984f566655c513d69fffd74ee8e1e25-Language_selector.png" className="border" />

# Profile menu

View the profile menu from the profile icon (the person) in the top-right corner of the header.

<Image align="center" alt="Control Center profile icon" border={true} width="40% " src="https://files.readme.io/5bff6ef887af21fd0e95490426a701e26fbdfad9123cd9cf0687040ce30e3e7d-Profile_icon.png" className="border" />

Use the profile menu to manage the following settings.

| Settings              | What you can do                                                                                                                                                                                          |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User name             | View your Control Center user ID                                                                                                                                                                         |
| Report log            | Copy detailed information to include in a Service Desk request. For more help, refer to [Access detailed report log information](https://developers.pismo.io/pismo-docs/docs/control-center-navigation#access-detailed-report-log-information).  |
| Manage authentication | Select the multi-factor authentication to use when signing on to Control Center. For more information, refer to [Add additional methods for multi-factor authentication (MFA)](https://developers.pismo.io/pismo-docs/docs/add-methods-for-mfa). |
| Sign out              | Sign out of Control Center                                                                                                                                                                               |
| Session ID            | View the unique ID for your current Control Center login session                                                                                                                                         |
| Version number        | View the Control Center version.                                                                                                                                                                         |

## Access detailed report log information

When a Control Center request fails, a report log notification displays with details about your current session. You can also access this notification anytime in the profile menu.

<Image align="center" alt="Report log notification" border={true} width="300px" src="https://files.readme.io/12000c32e6262ee78da7997ff63a64977bd4d34b16b31d68a346dccb0ca463ec-2025-03-26_13-14-55.png" className="border" />

This information is useful if you're opening a Service Desk request to report an issue. To copy the information:

1. Select **Copy report log**. The information is saved in your clipboard.
2. Paste the information from your clipboard into the description when you create your Service Desk request. For more information, refer to [Open a service request](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket).

The report log has these details.

| Detail               | Description                                                                                                                                                    | Example                              |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| Correlation ID       | The Correlation ID groups a series of related API requests and events.                                                                                         | fecc8fa6-3564-4dcc-bd28-a9f237ba63bc |
| Endpoint path name   | The endpoint that was called                                                                                                                                   | /crm-core-bff/query                  |
| statusCode           | The HTTP response status code. Errors are identified when the statusCode is one of the following: 400, 403, 405, 409, 500, 502, 503, 504 (but not 401 or 404). | 500 (Internal server error)          |
| operationNameGraphql | The operation performed by the endpoint                                                                                                                        | getTotalTransactionsPerformed        |
| Date-time stamp      | The date and time the operation occurred                                                                                                                       | 2025-03-26T21:09:24.742Z             |
<!-- source:end -->

## Lifecycle status

- `docs/control-center/control-center-navigation.md`: updatedAt 2026-08-26T13:05:57.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/control-center-navigation.md` | whole document | https://developers.pismo.io/pismo-docs/docs/control-center-navigation | `c931116efc3f4ae0…` | 2026-08-26T13:05:57.000Z |

## Related knowledge units

- `KU-AUTH-control-center-permissions-and-roles` — Control Center permissions, roles and API permission groups
- `KU-AUTH-control-center-sign-on-and-mfa` — Control Center sign-on, passwords and multi-factor authentication
- `KU-CC-accounts` — Control Center accounts: overview, management, actions and configurations
- `KU-CC-configuration-menus` — Control Center configuration menus: platform, banking and card configurations
- `KU-CC-dual-approval` — Dual approval
- `KU-CC-lending` — Control Center lending: loan products and loan management
- `KU-CC-seller-management-in-control-center` — Seller management
- `KU-CC-users` — Control Center users: create, edit, export and audit
- `KU-GS-setup-overview` — Core objects
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
