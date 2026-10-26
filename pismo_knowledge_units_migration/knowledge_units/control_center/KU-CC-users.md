---
ku_id: KU-CC-users
title: 'Control Center users: create, edit, export and audit'
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/users.md
  sha256: 8eba3a6cf470ba9b2868c3749cde0857ebdde06d4b5db8423ce264a579ff9abe
  url: https://developers.pismo.io/pismo-docs/docs/users
  role: primary_guide
  updated_at: '2026-08-26T11:59:29.000Z'
- path: docs/control-center/users-and-permissions-in-control-center.md
  sha256: 4b83d2a5318b73cd82f0aff4b6e303e8f71c943cc108c8d509df362a8330314e
  url: https://developers.pismo.io/pismo-docs/docs/users-and-permissions-in-control-center
  role: primary_guide
  updated_at: '2026-03-18T15:10:46.000Z'
- path: docs/control-center/add-a-user.md
  sha256: 2dce4323a34f3cd0a2ab015cb79a8e85c56a872749d82f1f7a2b98d75afa9971
  url: https://developers.pismo.io/pismo-docs/docs/add-a-user
  role: primary_guide
  updated_at: '2026-05-19T18:06:54.000Z'
- path: docs/control-center/export-user-list.md
  sha256: 57296d54eef907018c81bee29b2de3736126dbad4bc1d8c780f907787fba40ad
  url: https://developers.pismo.io/pismo-docs/docs/export-user-list
  role: primary_guide
  updated_at: '2026-03-18T15:10:48.000Z'
- path: docs/control-center/view-user-activity-audit.md
  sha256: 762038e885ad11294aa8d8dca25f986e6da8245c719d9456d75a4e11ecda5f2a
  url: https://developers.pismo.io/pismo-docs/docs/view-user-activity-audit
  role: primary_guide
  updated_at: '2026-08-26T11:55:02.000Z'
operations: []
related_kus:
- KU-AUTH-control-center-permissions-and-roles
- KU-AUTH-control-center-sso-and-openid
- KU-CC-control-center-navigation
- KU-CC-dual-approval
- KU-SUP-service-desk-requests
grouping_rationale: User administration tasks.
---

# Control Center users: create, edit, export and audit

**KU ID:** `KU-CC-users` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 5 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: User administration tasks.

Scope as stated in `docs/control-center/users.md`:

> Manage users, which includes the following:

Scope as stated in `docs/control-center/users-and-permissions-in-control-center.md`:

> You can create and edit users, export an organization's user list, and assign permissions—a set of roles that define what users can do.

Scope as stated in `docs/control-center/add-a-user.md`:

> If you have the Admin or User manager role, you can create and edit users in Control Center. You can only manage users in the organization that you're currently signed on to. To create or edit a user in a different organization, switch to that organization and ensure that you have the correct role.

Scope as stated in `docs/control-center/export-user-list.md`:

> You can export the list of an organization's users as a CSV file. The exported user list contains information useful for auditing and reporting purposes. To complete this task, you must have the Admin or User manager role assigned to your user. To export the user list for a different organization, you must [switch to that organization](https://developers.pismo.io/pismo-docs/docs/control-center-navigation).

Scope as stated in `docs/control-center/view-user-activity-audit.md`:

> View and export an audit log of Control Center user activity. To access the audit log, you must have the Admin, Auditor, or User manager role.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/users.md`: Users
- `docs/control-center/users-and-permissions-in-control-center.md`: User profiles
- `docs/control-center/add-a-user.md`: Create and edit users; Create a user; Edit a user; Resend sign-on instruction emails
- `docs/control-center/export-user-list.md`: Export user list
- `docs/control-center/view-user-activity-audit.md`: Audit; View the audit log; Export the audit log

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/users.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/users · updatedAt: 2026-08-26T11:59:29.000Z

<!-- source:begin path=docs/control-center/users.md part=0-end -->

# Users

Manage users, which includes the following:

* [Audit](https://developers.pismo.io/pismo-docs/docs/view-user-activity-audit)—View and export an audit log of Control Center user activity.
* [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval)—Dual approval is a security and governance feature that requires two separate individuals to review and approve a critical action or data change before it's finalized. One person initiates the request and a second person reviews and approves it. This process adds a layer of oversight, helping to prevent errors, unauthorized changes, and fraud.
* [User profiles](https://developers.pismo.io/pismo-docs/docs/users-and-permissions-in-control-center)—Create and edit Control Center users, and export an organization's user list.

For information about assigning system permissions, refer to [Permissions](https://developers.pismo.io/pismo-docs/docs/platform-authentication-in-control-center).
<!-- source:end -->

### Source 2: `docs/control-center/users-and-permissions-in-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/users-and-permissions-in-control-center · updatedAt: 2026-03-18T15:10:46.000Z

<!-- source:begin path=docs/control-center/users-and-permissions-in-control-center.md part=0-end -->

# User profiles

You can create and edit users, export an organization's user list, and assign permissions—a set of roles that define what users can do.

For more information, refer to the following:

* [Create and edit users](https://developers.pismo.io/pismo-docs/docs/add-a-user)
* [Export user list](https://developers.pismo.io/pismo-docs/docs/export-user-list)
* [User permissions and roles](https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles)
<!-- source:end -->

### Source 3: `docs/control-center/add-a-user.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/add-a-user · updatedAt: 2026-05-19T18:06:54.000Z

<!-- source:begin path=docs/control-center/add-a-user.md part=0-end -->

# Create and edit users

If you have the Admin or User manager role, you can create and edit users in Control Center. You can only manage users in the organization that you're currently signed on to. To create or edit a user in a different organization, switch to that organization and ensure that you have the correct role.

Keep in mind that creating and managing users is something your team handles. Pismo cannot create or manage users on your behalf.

<Callout icon="📘" theme="info">
  These steps apply only to users **not** using single sign-on (SSO).

  SSO allows users to access Control Center using your organization’s Identity Provider, so users only need one set of credentials. It’s an optional feature available to customers who purchase it. To enable SSO, contact your Pismo representative. For details, refer to [Get started with SSO for Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-sso-for-control-center).
</Callout>

# Create a user

To create a user:

1. From the main menu, select **Users & permissions** > **User profiles**.
2. On the **Users** screen, select **Create**.
3. On the **Create a new user** screen, enter the user's name and email.
4. Select the preferred language for the user.
5. In the **Permissions** section, assign roles for the user using the toggles and then **Save** your changes. For more information, refer to [User permissions and roles](https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles).

> 📘 User confirmation by email required
>
> When you create a user account, Pismo sends two sign-on instruction emails to the user.
>
> * One email contains a welcome message with a link to sign on, their username, and a temporary password.
> * The other email contains a verification code.
>
> If your user doesn't get these emails, you can [resend them](https://developers.pismo.io/pismo-docs/docs/add-a-user#resend-sign-on-instruction-emails).

# Edit a user

To edit a user:

1. From the main menu, select **Users & permissions** > **User profiles**.

2. On the **Users** screen, use search to find the user.

3. In the search results, select the **Edit** icon beside the user you want to edit.

4. On the **Users** screen, edit the user's name and email address.

5. (Optional) If the user hasn’t yet verified their email and their own a password, select **Resend emails** to resend the sign-on emails.

6. In the **Permissions** section, assign roles for the user using the toggles and then **Save** your changes.

# Resend sign-on instruction emails

If a user doesn't get the sign-on instruction emails, either the first time they sign on or when they change their password, you can use the following process to resend the emails:

1. From the main menu, select **Users & permissions** > **User profiles**.

2. On the **Users** screen, use search to find the user.

3. In the search results, select the **Edit** icon beside the user you want to edit.

4. On the **Edit user** screen, select **Resend emails** to send both emails again.<br />\
   If the **Resend emails** button is not available, it's because the user has already verified their email and created their own password.

<Callout icon="📘" theme="info">
  To ensure that your company isn't blocking emails from Pismo, check that Pismo is on the email safe sender list.
</Callout>
<!-- source:end -->

### Source 4: `docs/control-center/export-user-list.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/export-user-list · updatedAt: 2026-03-18T15:10:48.000Z

<!-- source:begin path=docs/control-center/export-user-list.md part=0-end -->

# Export user list

You can export the list of an organization's users as a CSV file. The exported user list contains information useful for auditing and reporting purposes. To complete this task, you must have the Admin or User manager role assigned to your user. To export the user list for a different organization, you must [switch to that organization](https://developers.pismo.io/pismo-docs/docs/control-center-navigation).

To export the user list:

1. From the main menu, select **Users & permissions** > **User profiles**.
2. On the **Users** screen, select **Export user list**.\
   The user list is exported and saved as a CSV file on your local machine.\
   If the export failed, an error message is displayed. To troubleshoot the issue, do the following:
   1. In the **Export user list** dialog, select **Try again**.
   2. If the issue persists, open a [service request](https://developers.pismo.io/pismo-docs/docs/service-desk) on the Pismo Service Desk.

Refer to the following table for a description of the included fields.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        User ID
      </td>

      <td>
        The unique ID of the user in the system
      </td>
    </tr>

    <tr>
      <td>
        Name
      </td>

      <td>
        The name of the user
      </td>
    </tr>

    <tr>
      <td>
        Email
      </td>

      <td>
        The email address of the user
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        The verification status of the user's account

        <ul><li><b>VERIFICATION\_REQUIRED</b>: The user did not verify their email address and access their account.</li>
        <li><b>ACCOUNT\_OK</b>: The user verified their email address and accessed their account.</li></ul>
      </td>
    </tr>

    <tr>
      <td>
        Date of Creation
      </td>

      <td>
        The date when the account was created
      </td>
    </tr>

    <tr>
      <td>
        Last Login
      </td>

      <td>
        The date and time when the user last logged in

        If the user's **Status** is set to **VERIFICATION\_REQUIRED**, **Last Login** is left blank.
      </td>
    </tr>

    <tr>
      <td>
        Roles
      </td>

      <td>
        The roles assigned to the user account

        If the user is not assigned a role, **Roles** is left blank.

        For more information, refer to [User permissions and roles](https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles).
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

### Source 5: `docs/control-center/view-user-activity-audit.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/view-user-activity-audit · updatedAt: 2026-08-26T11:55:02.000Z

<!-- source:begin path=docs/control-center/view-user-activity-audit.md part=0-end -->

# Audit

View and export an audit log of Control Center user activity. To access the audit log, you must have the Admin, Auditor, or User manager role.

The audit log provides a detailed record, helping you:

* Track user actions and system changes
* Understand how Control Center is used across your organization
* Investigate issues and incidents
* Monitor activity to support compliance and auditing

From Control Center, you can do the following:

* [View the audit log](#view-the-audit-log)
* [Export the audit log](#export-the-audit-log)

# View the audit log

To view the audit log and inspect an entry in more detail, do the following:

1. From the main menu, select **Users & permissions** > **Audit**.
2. On the **Audit** screen, select an entry. You can find specific entries by filtering the list or using the search field.\
   The **Audit details** screen is displayed.

Refer to the following table for a description of the sections on the **Audit details** screen.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Section
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Action summary
      </td>

      <td>
        Provides a high-level overview of the action, including the affected feature, action status, date and time, and any relevant identifying attribute details (for example, transaction type name and ID).
      </td>
    </tr>

    <tr>
      <td>
        Description
      </td>

      <td>
        Includes a brief explanation of the action, offering additional context.
      </td>
    </tr>

    <tr>
      <td>
        User
      </td>

      <td>
        Shows information about the user who performed the action, including their username, user ID, and assigned Control Center roles.
      </td>
    </tr>

    <tr>
      <td>
        Technical details
      </td>

      <td>
        Contains technical metadata related to the action, such as the IP address, device and browser information, and the correlation ID.

        A correlation ID is a system-level identifier that acts as a tracking reference for the user action, linking all connected backend processes throughout its lifecycle, to support end-to-end tracing and troubleshooting.
      </td>
    </tr>

    <tr>
      <td>
        Activity details
      </td>

      <td>
        Contains the request and response payloads exchanged with the backend API

        The payloads show the exact data sent and returned for the action, so you can understand what was executed and verify the outcome.
      </td>
    </tr>
  </tbody>
</Table>

**Note**: Not all sections are included for every audit log entry. The displayed sections depend on the specific action and affected feature.

# Export the audit log

You can export the audit log as a CSV file to capture user activity from Control Center and analyze it. For example, you can use the information to investigate issues, review historical changes, create reports, or retain records for external auditing and compliance purposes.

The exported file is available to download only for the user who initiated the export, and only the most recent export is available for download. If you export the audit log again, the previous file is replaced.

> 📘 Filtering the audit log
>
> If you apply any filters, the exported file contains only the filtered data.

To export the audit log, do the following:

1. Select **Export** and confirm.\
   When the export is complete, Control Center notifies you that the file is ready to download.
2. Open the **Notifications** menu and select **Your audit export is ready**.\
   The **Audit** screen is displayed.
3. Select **Download**.\
   **Note:** You have 24 hours to download the file. After that, you'll need to export the audit log again.
<!-- source:end -->

## Lifecycle status

- `docs/control-center/users.md`: updatedAt 2026-08-26T11:59:29.000Z.
- `docs/control-center/users-and-permissions-in-control-center.md`: updatedAt 2026-03-18T15:10:46.000Z.
- `docs/control-center/add-a-user.md`: updatedAt 2026-05-19T18:06:54.000Z.
- `docs/control-center/export-user-list.md`: updatedAt 2026-03-18T15:10:48.000Z.
- `docs/control-center/view-user-activity-audit.md`: updatedAt 2026-08-26T11:55:02.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/users.md` | whole document | https://developers.pismo.io/pismo-docs/docs/users | `8eba3a6cf470ba9b…` | 2026-08-26T11:59:29.000Z |
| `docs/control-center/users-and-permissions-in-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/users-and-permissions-in-control-center | `4b83d2a5318b73cd…` | 2026-03-18T15:10:46.000Z |
| `docs/control-center/add-a-user.md` | whole document | https://developers.pismo.io/pismo-docs/docs/add-a-user | `2dce4323a34f3cd0…` | 2026-05-19T18:06:54.000Z |
| `docs/control-center/export-user-list.md` | whole document | https://developers.pismo.io/pismo-docs/docs/export-user-list | `57296d54eef90701…` | 2026-03-18T15:10:48.000Z |
| `docs/control-center/view-user-activity-audit.md` | whole document | https://developers.pismo.io/pismo-docs/docs/view-user-activity-audit | `762038e885ad1129…` | 2026-08-26T11:55:02.000Z |

## Related knowledge units

- `KU-AUTH-control-center-permissions-and-roles` — Control Center permissions, roles and API permission groups
- `KU-AUTH-control-center-sso-and-openid` — Control Center SSO and OpenID Connect configuration
- `KU-CC-control-center-navigation` — Navigate Control Center
- `KU-CC-dual-approval` — Dual approval
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
