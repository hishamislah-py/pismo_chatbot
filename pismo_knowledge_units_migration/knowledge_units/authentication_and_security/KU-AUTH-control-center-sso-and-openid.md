---
ku_id: KU-AUTH-control-center-sso-and-openid
title: Control Center SSO and OpenID Connect configuration
category: authentication_and_security
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/get-started-with-sso-for-control-center.md
  sha256: 07bf69b25639fe5ac81e47c47385561a094aa2f37b3e6b52bb656413d8226716
  url: https://developers.pismo.io/pismo-docs/docs/get-started-with-sso-for-control-center
  role: primary_guide
  updated_at: '2026-07-23T18:14:43.000Z'
- path: docs/control-center/openid-configurations.md
  sha256: d3db7b0aa5239ba21309b9ad2fe8c9948d56683dd24c8b7bfbc0ca85b6b9c323
  url: https://developers.pismo.io/pismo-docs/docs/openid-configurations
  role: primary_guide
  updated_at: '2026-08-05T11:16:14.000Z'
operations: []
related_kus:
- KU-AUTH-authentication-methods
- KU-AUTH-control-center-permissions-and-roles
- KU-CC-dual-approval
grouping_rationale: SSO setup and the OpenID configuration screen.
---

# Control Center SSO and OpenID Connect configuration

**KU ID:** `KU-AUTH-control-center-sso-and-openid` · **Category:** Authentication and security · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: SSO setup and the OpenID configuration screen.

Scope as stated in `docs/control-center/get-started-with-sso-for-control-center.md`:

> An optional package allows clients to add Single Sign-On (SSO) authentication to Control Center for a fee. This gives you the ability to have your organization’s users sign in to Pismo Control Center through an Identity Provider (IdP) using a single set of credentials. Pismo supports SSO with the Security Assertion Markup Language (SAML) 2.0 protocol. Any identity provider that supports SAML 2.0 works with Pismo. The advantage of this is that your IdP acts as a trusted service that manages user accounts and their authentication.

Scope as stated in `docs/control-center/openid-configurations.md`:

> Create and manage OpenID Connect (OIDC) authentication configurations for your organization. OIDC provides greater security guarantees in service communications than basic authentication using client credentials and is the preferred way to authenticate with the Pismo platform.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/get-started-with-sso-for-control-center.md`: Get started with SSO for Control Center; How SSO with SAML work with Control Center; Configure SSO for SAML; Step 1: Set up your identity provider (IdP); Step 2: Send IdP configuration information to Pismo; Step 3: Assign Roles in Control Center; Integration flow with role mapping; Configure a user role in Entra ID; Step 4: Finalize the configuration in the IdP; Considerations for creating users with SSO integration; User deletion and revoking access to Control Center; Terms to know
- `docs/control-center/openid-configurations.md`: OpenID Connect; View OIDC authentication configurations; Create an OIDC authentication configuration; Manage OIDC authentication configurations; Edit an OIDC authentication configuration; Deactivate an OIDC authentication configuration

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/get-started-with-sso-for-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-with-sso-for-control-center · updatedAt: 2026-07-23T18:14:43.000Z

<!-- source:begin path=docs/control-center/get-started-with-sso-for-control-center.md part=0-end -->

# Get started with SSO for Control Center

An optional package allows clients to add Single Sign-On (SSO) authentication to Control Center for a fee. This gives you the ability to have your organization’s users sign in to Pismo Control Center through an Identity Provider (IdP) using a single set of credentials. Pismo supports SSO with the Security Assertion Markup Language (SAML) 2.0 protocol. Any identity provider that supports SAML 2.0 works with Pismo. The advantage of this is that your IdP acts as a trusted service that manages user accounts and their authentication.

<Callout icon="📘" theme="info">
  Single sign-on (SSO) is only available to customers who have purchased it. Contact your Pismo representative for more information.
</Callout>

# How SSO with SAML work with Control Center

This is the basic log in and authentication flow when a user accesses the Pismo Control Center with SAML SSO configured:

1. User navigates to Control Center to login using SSO.
2. User enters their email address and Control Center determines if this email domain uses an SSO profile to authenticate. If the email domain has a rule to use SSO, the SAML request for login is sent to the identity provider (IdP).
3. User logs in to the IdP.
4. The IdP prepares a SAML response and sends it to the user's browser.
5. The IdP posts the SAML response to Control Center, and the user is directed to their unique Control Center homepage.

# Configure SSO for SAML

<Callout icon="🚧" theme="warn">
  Before you start your configuration, you must ensure your IdP supports SAML 2.0.

  If you are unfamiliar with SSO or SAML, refer to the [Terms to know](https://developers.pismo.io/pismo-docs/docs/get-started-with-sso-for-control-center#terms-to-know) section before proceeding with the configuration steps.
</Callout>

## Step 1: Set up your identity provider (IdP)

1. **Log in to your IdP admin console**—access your IdP (e.g., Okta, OneLogin, Entra ID, Google Workspace, etc.).
2. **Create a new SAML application**—create an application in your IdP that represents the relationship between Control Center and your IdP.
   1. Navigate to the console section where you can add a new application.
   2. Select SAML-based authentication.
3. **Configure basic application settings**.

   1. Provide a name and description for the SAML application.
   2. Optionally, upload a logo for easier identification.
   3. **Configure SAML Settings**—you will see a screen like this (actual layout is dependent on your chosen IdP):

      <Image align="center" src="https://files.readme.io/e0c598d3e3ccb2959d38115655f224caa5bdf4cdd3466f16a2de483b321ecefc-AttributesAndClaims2.png" />
   4. Enter the Identifier`Identifier (Entity ID)` provided by Pismo. This is a unique identifier for the service provider (the application a user wants to access—in this case, Pismo Control Center), often a URL or a URN.\
      Note: this URL or URN is unique to each environment (one for production, one for test, and so on).
   5. Enter the URL provided by Pismo where Control Center will receive SAML assertions from the IdP into the  `Reply URL (Assertion Consumer Service URL)` field.\
      Note: this URL is unique to each environment (one for production, one for test, and so on).
4. **Map Attributes**—(e.g., email, first name, last name) from the IdP to the SP. The following attributes are required:
   * **Username**—email address (string)
   * **Name**—In Control Center, there is a single field for name and you can send anything you want for this field (first name + last name, first name only, display name and so on). (string)
   * **Email address**—user email address (string)
5. Select **Unique User Identifier**—this is a default claim that is added when an app is created.
   * **Namespace**— [http://schemas.xmlsoap.org/ws/2005/05/identity/claims](http://schemas.xmlsoap.org/ws/2005/05/identity/claims)
   * **Source**—Attribute
   * **Source attribute**—user.email
6. **Download IdP metadata SAML certificate**—Download then save the IdP metadata XML file. This is required for Control Center configuration.

## Step 2: Send IdP configuration information to Pismo

You must send the IdP metadata XML file you downloaded in the previous step to Pismo. Do this through a secure Enhanced File Transfer (EFT).

1. Pismo will send you an email invite to register to the EFT. Note: If you are already registered, connect to the online [EFT Portal](https://filexchange.visa.com/Web/Account/Login.htm).
2. Log in to your account using the email account and password you created when you registered to the EFT.
3. Select the **Shared with Me** folder and then select the folder that was shared with you by Pismo.
4. Upload the metadata XML file.

## Step 3: Assign Roles in Control Center

With the optional package that allows you to set up Single Sign-On (SSO) authentication to Control Center, you  can also set up role mapping in Control Center. Role-based access control (RBAC) enforces the principle of least privilege. With RBAC, users are granted only the minimum access necessary for their roles. Control Center users can be assigned to multiple roles, each with different permissions. If you have multiple organizations, your users can be assigned to different roles for each organization. For example, a user can be an Admin in organization 1 but an Accounts viewer in organization 2.

### Integration flow with role mapping

Once you have configured the role mapping for your users, this is the authorization flow for users when logging in to Control Center:

1. User logs in via the IdP.
2. IdP sends an authentication token with attributes.
3. Control Center reads the attributes:
   1. Identifies the user via email
   2. Determines access levels via the custom attribute
4. Permissions are applied based on the received values.

To create the role mapping for your users, you need to provide SAML assertions. The assertions must be provided in a very specific format: `OrgID/rolename` (for example: TN-123456789/controlc-admin).

* OrgID is mandatory—This is because you may have more than one organization in Control Center and users can be assigned separate roles for each organization.
* Rolename must be the exact name of the role—Only those roles in the table above are allowed, you cannot add new roles or modify the pre-defined role names.
* You can send multiple roles in the SAML assertion—either as a semicolon-separated list in a single SAML attribute or as a multi-value SAML attribute.

### Configure a user role in Entra ID

To enable Control Center to interpret access levels, you must configure a user role in Entra ID, which is a 4-step process:

* Create groups
* Add roles
* Assign roles to the groups
* Edit attributes and claims

#### Create groups

Create custom groups for Pismo roles and assign your team members (users) to these groups. You can assign a Pismo role to each group and you can add users to multiple groups.

1. Log in to the [Entra ID Dashboard](https://entra.microsoft.com/).
2. From the left navigation panel, select **Groups**.
3. Select **Add new group**:
   1. **Group type**—select Security
   2. **Group name**—enter the name of the group (for example, Setup viewer)
   3. Select **No members added** and add users to the group

#### Add roles

Custom roles are not supported within Control Center. Role management is restricted to a list of pre-defined roles. Refer to the Control Center [User permissions and roles](https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles) guide for the list of roles ad permission details.

To create the role mapping for your users, you need to provide SAML assertions. The assertions must be provided in a very specific format: `OrgID/rolename` (for example: TN-123456789/controlc-admin).

* `OrgID` is mandatory—This is because you may have more than one organization in Control Center and users can be assigned separate roles for each organization.
* `Rolename` must be the exact name of the role—Only those roles in the table above are allowed, you cannot add new roles or modify the pre-defined role names.
* You can send multiple roles in the SAML assertion—either as a semicolon-separated list in a single SAML attribute or as a multi-value SAML attribute.

Take the following steps to add roles:

1. Go to **Entra ID** > **App registrations**.
2. Select the application you created for the Pismo Control Center.

   1. Go to **Manage** > **App roles**.
   2. Select **Create app role**.

      <Image align="center" alt="App roles screen in Control Center with the Create app role option highlighted" src="https://files.readme.io/291c6f3aa692471847689fbb96238b968183a789cd2e15ece084cb8142fb57f8-CreateAppRole.png" />
   3. In the **Create app role** pane:

      * Add a **Display name**
      * Add **Allowed member types**
      * Add a **Value**—this value must follow the orgId/Role name pattern
      * Enter a **Description**
      * Select **Apply**.

        <Image align="center" alt="Create app role screen in Control Center" width="500px" src="https://files.readme.io/3f109150fba64135036f86068533fd8a966f135240c819019f955c433236932c-CreateAppRoleScreen.png" />

#### Assign roles to Entra ID groups

1. Go to **Enterprise applications** and open the App created for Pismo Control Center.
2. Go to **Manage** > **Users and groups**.
3. Select **Add user and groups**.
4. Under  **Add users and groups** select **None Selected** to add a group. A list of users and security groups displays.
5. You can search for a group you created in the previous step and select the groups that display in the list. Choose **Select** to proceed.
6. Under **Select a role** select **None Selected**. All the roles that you defined for the application are displayed.
7. Select a role and choose **Select** .
8. Select **Assign** to finish the assignment of users and groups to the app.

#### Edit attributes and claims

1. Go to **Manage** > **Single-sign on**.
2. In the **Attributes & Claims** section, select **Edit**.
3. Add a new claim for the role:
   * **Name**—ControlCenterRole
   * **Namespace**—(if required) [http://schemas.xmlsoap.org/ws/2005/05/identity/claims](http://schemas.xmlsoap.org/ws/2005/05/identity/claims)
   * **Source**—Attribute
   * **Source attribute**—user.assignedroles
4. **Save** the configuration and ensure the claim is included in the token sent to Control Center.

## Step 4: Finalize the configuration in the IdP

Once Pismo receives the metadata file, we will complete your configuration and notify you when the system is ready to test. Once you are notified that configuration is complete, do the following:

1. **Test the configuration.**
   1. Ensure that user attributes are correctly mapped.
   2. Perform a test login to verify that SSO is working as expected.
2. **Enable SSO for users.**
   1. Once testing is successful, notify Pismo and we will enable SSO for your users in your email domain.
   2. Add users into your IdP (refer to the next section for special considerations when creating users with SSO).
   3. Provide necessary documentation or training to your end-users on how to use SSO.

# Considerations for creating users with SSO integration

There are some specific considerations for Control Center administrators when creating users with SSO integration. The main thing to keep in mind is that while you must initially create all your users in your IdP, you must manage Control Center users and user roles from the Control Center.

If you have a user in your IdP but you haven’t created a user for that person in the Control Center, this is what happens when they log into the Control Center for the first time using SSO:

1. When a person without a defined user account in Control Center logs into Control Center for the first time, a user account is automatically created using Just-in-Time (JIT) provisioning from SAML.
2. Since the newly assigned user does not yet have a role assigned, they will not have permissions to see anything in Control Center upon initial log in. They will be directed to a page telling them to reach out to their company Control Center admin to have roles assigned.
3. As the company Control Center admin, you must log in to Control Center to assign the appropriate roles to the user.
4. The next time the user logs into Control Center, they will have the correct access.

## User deletion and revoking access to Control Center

Control Center users are not synced with users in your IdP. Therefore, Pismo does not get notified if user access is revoked in IdP. So, user deletion for Control Center is a two-step process.

First, you must revoke user access in your IdP. If users try to log in to Control Center again through SSO after their current session expires, Pismo revokes their access but does not delete the user.

Next, you need to delete the user in Control Center to remove the user, so that user does not count towards your user account limit. Note that users that were created in Control Center before the integration was turned on will still be shown as users in Control Center even If you never granted them access in your IdP.

# Terms to know

| Term                                      | Meaning                                                                                                                                                                                                                                                   |
| :---------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identity Provider (IdP)                   | An Identity Provider is a trusted service that stores and authenticates a user’s identity.                                                                                                                                                                |
| Service Provider                          | The application a user wants to access, such as Pismo Control Center.                                                                                                                                                                                     |
| Security Assertion Markup Language (SAML) | SAML is an open standard authentication protocol that you can use to implement SSO in your Control Center org. SAML allows identity providers and service providers to securely exchange user information, enabling user authentication between services. |
| SAML Assertion                            | A SAML assertion, which is part of a SAML response, describes a user by asserting facts, like username or email address. During authentication, the identity provider signs the SAML assertion, and the service provider validates the signature.         |
| SAML Request                              | When a user attempts to access the service provider, the service provider sends a SAML request asking the identity provider to authenticate the user.                                                                                                     |
| SAML Response                             | To authenticate the user, the identity provider sends a SAML response to the service provider. The response contains a signed SAML assertion with facts about the user.                                                                                   |
<!-- source:end -->

### Source 2: `docs/control-center/openid-configurations.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/openid-configurations · updatedAt: 2026-08-05T11:16:14.000Z

<!-- source:begin path=docs/control-center/openid-configurations.md part=0-end -->

# OpenID Connect

Create and manage OpenID Connect (OIDC) authentication configurations for your organization. OIDC provides greater security guarantees in service communications than basic authentication using client credentials and is the preferred way to authenticate with the Pismo platform.

Together with OIDC authentication, the Pismo platform uses API permission groups to control access to the Pismo APIs. All OIDC authentication configurations must have at least one permission group applied. For more information, refer to [Permission groups](https://developers.pismo.io/pismo-docs/docs/cc-api-permission-groups).

> 📘 Role requirements
>
> Only users with the Admin role can create and manage OIDC authentication configurations.

> 🚧 Updating existing configurations
>
> Existing OIDC authentication configurations that do not have any applied permission groups operate without restrictions. However, once you apply permission groups to an unrestricted configuration, you can only generate a JSON Web Token (JWT) for the applied groups.
>
> Updating an unrestricted configuration to use only specific permission groups can affect live integrations. If you attempt to generate a JWT that specifies a permission group that is not applied to the configuration, you will receive a 403 Forbidden error response.
>
> To avoid an interruption in service, before you update the permission groups for an unrestricted configuration, identify all permission groups currently used by the integration and make sure they're applied to the configuration.

> 📘 Dual approval
>
> If your company is using the dual approval feature, creating, editing, or deactivating an OpenID authentication configuration requires approval. With dual approval, you initiate the change and submit a request for approval. A second person must review and approve it. The change doesn't take effect until the request is approved.
>
> For more information about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).

For more information about using OIDC with the Pismo platform, refer to [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid).

# View OIDC authentication configurations

To view the list of OIDC authentication configurations and explore a configuration in more detail, do the following:

1. From the main menu, select **Users & permissions** > **OpenID Connect**.
2. On the **OpenID Connect** screen, select a configuration.\
   The **OpenID Connect details** screen is displayed, divided into the following tabs:
   * **OpenID Connect configuration**—Provides an overview of the configuration, including key identity and verification details, metadata, status, and editing capabilities.
   * **Permission groups**—Displays a list of the permission groups applied to the configuration and gives you the option to edit them.

<Image align="center" alt="Screenshot showing an excerpt of the OpenID Connect screen" border={true} src="https://files.readme.io/e033da0220db42cf72f6d868eb875ffa019951f72dff734fbec36e086d42f366-Openid-connect.png" className="border" />

The **OpenID Connect** screen displays the list of OIDC authentication configurations for your organization. Each configuration is assigned a tenant ID, a unique identifier generated by the Pismo platform when the configuration is created.

A configuration can have one of the following statuses:

* **Active**—The configuration is in use.
* **Deactivated**—The configuration was deactivated and is no longer available.
* **Pending approval** (dual approval only)—A change was made to the configuration and is pending approval.

# Create an OIDC authentication configuration

Create an OIDC authentication configuration to enable secure, token-based access to the Pismo APIs when you need to:

* Integrate a backend service or external application with the Pismo platform
* Configure permissions for internal users
* Define access rules for a new environment or organization

To create an OIDC authentication configuration, do the following:

1. On the **OpenID Connect** screen, select **Create OpenID**.
2. On the **Name & public key encoding** screen, enter a name and provide your public key.\
   For more information on how to generate a public/private key pair, refer to [Server authentication](https://developers.pismo.io/pismo-docs/reference/authentication-with-openid#server-authentication).
3. Select **Next**.
4. On the **Permission groups** screen, select the permission groups you want to apply to the configuration, and select **Next**.\
   **Note:** You must select at least one permission group to continue.
5. Review the configuration details and select **Finish**.

# Manage OIDC authentication configurations

From Control Center, you can do the following:

* [Edit an OIDC authentication configuration](#edit-an-oidc-authentication-configuration)
* [Deactivate an OIDC authentication configuration](#deactivate-an-oidc-authentication-configuration)

## Edit an OIDC authentication configuration

Edit your OIDC authentication configuration details to keep them aligned with your organization's evolving security and access requirements. You can edit the name, public key, and applied permission groups.

You may need to edit a configuration when:

* Updating the configuration name to reflect a change in scope
* Updating an incorrect public key
* Aligning API access with updated integration or security requirements

> 🚧 Updating permission groups
>
> You can generate a JWT only for permission groups that are applied to the configuration. When you edit the permission groups applied to a configuration and attempt to generate a JWT that specifies permission groups that aren't applied to the configuration, you will receive a 403 Forbidden error response.

To edit the name or public key, do the following:

1. On the **OpenID Connect** screen, select an active configuration.
2. On the **OpenID Connect configuration** tab, select the edit icon for the attribute you want to edit.
3. Update the value and select **Save**.

To edit the applied permission groups, do the following:

1. On the **OpenID Connect** screen, select an active configuration, and select the **Permission groups** tab.
2. Select **Edit groups**, configure your permission groups, and select **Save**.

## Deactivate an OIDC authentication configuration

Deactivate an OIDC authentication configuration to permanently remove it from use. This is typically done when a configuration is no longer needed, for example, when it's being replaced by a newer version or must be disabled for security or access control reasons. Deactivated configurations remain in the list, to aid in traceability and auditing.

> 🚧 Deactivating a configuration
>
> A configuration cannot be deleted, only deactivated.
>
> When you deactivate a configuration, you won't be able to reactive it. If you need access again, you must create a new configuration.

To deactivate an OIDC authentication configuration, do the following:

1. On the **OpenID Connect** screen, select an active configuration.
2. On the **OpenID Connect configuration** tab, select the **Active** status toggle, and confirm your choice.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.


### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `authentication-with-openid` | Server authentication | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Lifecycle status

- `docs/control-center/get-started-with-sso-for-control-center.md`: updatedAt 2026-07-23T18:14:43.000Z.
- `docs/control-center/openid-configurations.md`: updatedAt 2026-08-05T11:16:14.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Operation link `authentication-with-openid` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/get-started-with-sso-for-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-with-sso-for-control-center | `07bf69b25639fe5a…` | 2026-07-23T18:14:43.000Z |
| `docs/control-center/openid-configurations.md` | whole document | https://developers.pismo.io/pismo-docs/docs/openid-configurations | `d3db7b0aa5239ba2…` | 2026-08-05T11:16:14.000Z |

## Related knowledge units

- `KU-AUTH-authentication-methods` — API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys
- `KU-AUTH-control-center-permissions-and-roles` — Control Center permissions, roles and API permission groups
- `KU-CC-dual-approval` — Dual approval
