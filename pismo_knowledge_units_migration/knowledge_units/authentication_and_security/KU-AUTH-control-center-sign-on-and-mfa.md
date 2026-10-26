---
ku_id: KU-AUTH-control-center-sign-on-and-mfa
title: Control Center sign-on, passwords and multi-factor authentication
category: authentication_and_security
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/get-access-and-sign-on.md
  sha256: 64439da75845f5812e417dc8c6f1cf1a02eeb120eff274d01f1154b979fe6624
  url: https://developers.pismo.io/pismo-docs/docs/get-access-and-sign-on
  role: primary_guide
  updated_at: '2026-07-31T14:01:29.000Z'
- path: docs/control-center/password-self-reset-control-center.md
  sha256: 32e73c8cdfb4ea62af4374d5c1ce1dfa779d6bc44ad0ee4856cfc01e0f071265
  url: https://developers.pismo.io/pismo-docs/docs/password-self-reset-control-center
  role: primary_guide
  updated_at: '2026-03-18T15:09:17.000Z'
- path: docs/control-center/cc-pw-best-practices.md
  sha256: d78f1c02fc2596354ea7c3ddbd114aeaefb3df7d1fff22eadef9eb6f2062d8c5
  url: https://developers.pismo.io/pismo-docs/docs/cc-pw-best-practices
  role: primary_guide
  updated_at: '2026-03-18T15:09:16.000Z'
- path: docs/control-center/add-methods-for-mfa.md
  sha256: d8d13b663ea82fc0d56953b15c9c334366a165573af6159097f067a145cfa161
  url: https://developers.pismo.io/pismo-docs/docs/add-methods-for-mfa
  role: primary_guide
  updated_at: '2026-06-10T20:31:21.000Z'
operations: []
related_kus:
- KU-SUP-service-desk-requests
grouping_rationale: User sign-on lifecycle.
---

# Control Center sign-on, passwords and multi-factor authentication

**KU ID:** `KU-AUTH-control-center-sign-on-and-mfa` · **Category:** Authentication and security · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 4 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: User sign-on lifecycle.

Scope as stated in `docs/control-center/get-access-and-sign-on.md`:

> To get access to Control Center, contact your Control Center administrator. They'll create your account.

Scope as stated in `docs/control-center/password-self-reset-control-center.md`:

> You can reset your Control Center password on the sign-on screen.

Scope as stated in `docs/control-center/cc-pw-best-practices.md`:

> Passwords are a critical aspect of cybersecurity and can serve as the first line of defense in preventing unauthorized access to your account. They help to protect access to sensitive and proprietary information. This prevention ensures that data and private or sensitive information is used only by the appropriate users.

Scope as stated in `docs/control-center/add-methods-for-mfa.md`:

> As a user in Control Center, you are automatically set up with email verification as your multi-factor authentication (MFA). You can add additional methods for MFA from the **Manage authentication** option in your Profile menu. You can add an authenticator app, a passkey, or both. You can also remove methods (at least one is required) and rename the MFA options.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/get-access-and-sign-on.md`: Sign on to Control Center; Sign on; What if I don't get the sign-on instruction emails?; What if my company uses single sign-on (SSO)?; Get more help
- `docs/control-center/password-self-reset-control-center.md`: Reset your password
- `docs/control-center/cc-pw-best-practices.md`: Best practices for Control Center passwords; Password requirements; Additional password guidelines; Password policy rules; Account lockout rules; Tips for creating a unique password
- `docs/control-center/add-methods-for-mfa.md`: Add additional methods for multi-factor authentication (MFA); Add an MFA method; Add an Authenticator app; Add a passkey; Rename an authentication method; Remove an authentication method

## Prerequisites and dependencies

- Prerequisites are described in `docs/control-center/cc-pw-best-practices.md` section "Password requirements".

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/get-access-and-sign-on.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-access-and-sign-on · updatedAt: 2026-07-31T14:01:29.000Z

<!-- source:begin path=docs/control-center/get-access-and-sign-on.md part=0-end -->

# Sign on to Control Center

To get access to Control Center, contact your Control Center administrator. They'll create your account.

# Sign on

Once your account is created, you'll get two email messages from Pismo Control Center with instructions for signing on.

* One email contains a welcome message with a link to sign on, your username, and a temporary password.
* The other email contains a verification code.

**Note:** Use Control Center with an up-to-date browser based on Chrome technology, such as Google Chrome, Microsoft Edge, or Opera. Pismo supports browser versions that are at least as new as the Long-Term Support (LTS) or Extendable Stable baseline, as well as any versions released after that baseline.

To sign on the first time, do the following:

1. In the welcome email, select the link labeled **Sign on to Control Center**.
2. On the sign-on screen, enter your username from the welcome email.
3. On the next sign-on screen, enter the temporary password from the welcome email.
4. Next, enter the temporary password (in the **Current Password** field) and create a new password. For information about creating a secure password, refer to [Best practices for Control Center passwords](https://developers.pismo.io/pismo-docs/docs/cc-pw-best-practices).
5. Next, enter the verification code from the other email to complete the registration process and start using Control Center.
6. When you first sign on, you're automatically set up with email verification as your multi-factor authentication (MFA) method. MFA adds an extra layer of security by confirming your identity with more than one type of proof, such as a code on your phone or a fingerprint. Pismo recommends adding a passkey, an authenticator, or both. To do this, refer to [Add additional methods for multi-factor authentication (MFA)](https://developers.pismo.io/pismo-docs/docs/add-methods-for-mfa).

Going forward, if you ever forget your password or need to reset it, select **Forgot Password** and [go through the password reset steps](https://developers.pismo.io/pismo-docs/docs/password-self-reset-control-center).

## What if I don't get the sign-on instruction emails?

If you don't get the sign-on instruction emails, use the following process:

1. From the sign-on screen, select **Forgot Password**.
2. You'll receive an email with a recovery code.
3. On the sign-on screen, enter the recovery code, create a new password, and save your changes.
4. You'll be prompted on the sign-on screen to enter a verification code. Select **Didn't receive an email? Resend**.
5. You'll receive the verification code in an email. On the sign-on screen, enter this verification code.
6. For added security, you'll receive a one-time passcode (OTP) via email. On the sign-on screen, enter this passcode to complete authentication and sign on.

If this process doesn't work, contact your Control Center administrator to resend the instruction emails.

In the rare case neither process works, [open a service request](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket) with the Pismo Service Desk.

## What if my company uses single sign-on (SSO)?

<Callout icon="📘" theme="info">
  SSO is only available to customers who have purchased it. Contact your Pismo representative for more information.
</Callout>

If your company uses SSO for Control Center, use the Control Center URL to sign on. Your email is your Control Center username.

After signing on, if your screen displays a message indicating that you don't have a role assigned, contact your Control Center administrator for assistance. After they assign your role, the next time you sign on you'll have the correct permissions and access.

# Get more help

Control Center is intended to be intuitive and contains helpful tips to guide you. But if you need more help, contact your Control Center administrator. To get help with an issue that your administrator can't resolve, [open a service request](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket) with the Pismo Service Desk.
<!-- source:end -->

### Source 2: `docs/control-center/password-self-reset-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/password-self-reset-control-center · updatedAt: 2026-03-18T15:09:17.000Z

<!-- source:begin path=docs/control-center/password-self-reset-control-center.md part=0-end -->

# Reset your password

You can reset your Control Center password on the sign-on screen.

1. Select **Forgot Password**.
2. If you have an active account with a valid email address, you'll receive an email with a recovery code. If you don't have an account or email, contact your Control Center administrator.
3. On the sign-on screen, enter the recovery code, create a new password, and save your changes.
4. For added security, you must verify your identity using your chosen multi-factor authentication (MFA) method (email, passkey, or authenticator app). For more information about MFA, refer to [Add additional methods for multi-factor authentication (MFA)](https://developers.pismo.io/pismo-docs/docs/add-methods-for-mfa).
5. Complete authentication and sign on.
<!-- source:end -->

### Source 3: `docs/control-center/cc-pw-best-practices.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cc-pw-best-practices · updatedAt: 2026-03-18T15:09:16.000Z

<!-- source:begin path=docs/control-center/cc-pw-best-practices.md part=0-end -->

# Best practices for Control Center passwords

Passwords are a critical aspect of cybersecurity and can serve as the first line of defense in preventing unauthorized access to your account. They help to protect access to sensitive and proprietary information. This prevention ensures that data and private or sensitive information is used only by the appropriate users.

To ensure secure passwords, the Control Center has implemented a strong list of requirements. While passwords may seem inconvenient, they are an important protection that should be taken seriously.

# Password requirements

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Requirement
      </th>

      <th>
        Things to consider
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Cannot be the same as your current password
      </td>

      <td>
        Do not reuse any of your previous six passwords.
      </td>
    </tr>

    <tr>
      <td>
        Cannot be an exact match for any attribute values in your user profile
      </td>

      <td>
        Avoid using your first or last name or your user ID.
      </td>
    </tr>

    <tr>
      <td>
        Cannot be too similar to your current password
      </td>

      <td>
        Do not simply add a number or character to your current password; the new password must be unique.
      </td>
    </tr>

    <tr>
      <td>
        Cannot be a commonly-used password
      </td>

      <td>
        Avoid things like "Password" or "Welcome123".
      </td>
    </tr>

    <tr>
      <td>
        Must have a minimum of 12 and a maximum of 255 characters
      </td>

      <td>
        Longer passwords are harder to hack.
      </td>
    </tr>

    <tr>
      <td>
        Must contain at least one of the following special characters: `~!@#$%^&\*()-\_=+\[]{};:.,\<>/?`
      </td>

      <td>
        Only one special character is required, but consider using more than one for a stronger password.
      </td>
    </tr>

    <tr>
      <td>
        Must contain at least one numeral: `0123456789`
      </td>

      <td>
        Avoid four or more sequential numbers such as 1234.
      </td>
    </tr>

    <tr>
      <td>
        Must contain at least one upper case character:\
        `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
      </td>

      <td>
        Avoid four or more sequential letters such as ABCD.
      </td>
    </tr>

    <tr>
      <td>
        Must contain at least one lower case character:\
        `abcdefghijklmnopqrstuvwxyz`
      </td>

      <td>
        Try alternating upper and lower case letters.
      </td>
    </tr>
  </tbody>
</Table>

## Additional password guidelines

In addition to the requirements, also consider the following guidelines when creating your password.

* Do not use the name of a pet, family member, product, sport, or organization.
* Do not use phone numbers, addresses, birthdays, or other identifying numbers.
* Never use simple adjacent keyboard combinations (e.g., asdfjkl;).
* Do not use palindromes (words or phrases that read the same forward and backwards, for example madam, kayak, nurses run, race car).
* Do not use spaces. If a system improperly handles spaces, it might be more vulnerable to certain types of attacks.
* Do not use the same password for more than one account.
* Do not write your password down or store it near your computer or desk. Use an approved password management tool, if available.

# Password policy rules

* 6 prior passwords are maintained in the password history count for a maximum of 365 days
* The password expires every 90 days (every 3 months)

# Account lockout rules

* Account lockout occurs after 6 distinct failed attempts (repeated attempts of the same password are not counted)
* Locked accounts due to failed password attempts are automatically unlocked after 30 minutes

# Tips for creating a unique password

The key to creating a hard-to-hack password is to make it unique and easy to remember but hard to guess.

Here are some tips to create easy-to-remember but hard-to-guess passwords:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Try this...
      </th>

      <th>
        Examples...
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Relate the password to something you can easily remember, for instance a favorite hobby or vacation destination.
      </td>

      <td>
        "I love to be in Italy" could be changed to "1luv2bn1talE!". It is secure and memorable.
      </td>
    </tr>

    <tr>
      <td>
        Use a phrase you know well but incorporate shortcuts or acronyms.
      </td>

      <td>
        "One for all and all for one" (from *The Three Musketeers* written by Dumas) can be changed to\
        "14A\&a41duMas".
      </td>
    </tr>

    <tr>
      <td>
        Use the first letter of a phrase that is meaningful to you but incorporate symbols or acronyms.
      </td>

      <td>
        "I love my children and they are the best part of me." could be changed to "1Lmc\&TRtbpom!"
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

### Source 4: `docs/control-center/add-methods-for-mfa.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/add-methods-for-mfa · updatedAt: 2026-06-10T20:31:21.000Z

<!-- source:begin path=docs/control-center/add-methods-for-mfa.md part=0-end -->

# Add additional methods for multi-factor authentication (MFA)

As a user in Control Center, you are automatically set up with email verification as your multi-factor authentication (MFA). You can add additional methods for MFA from the **Manage authentication** option in your Profile menu. You can add an authenticator app, a passkey, or both. You can also remove methods (at least one is required) and rename the MFA options.

# Add an MFA method

The three types of MFA allowed for Control Center are:

* **Email**—This is the default option for all users.
* **Authenticator App**—Use a Time-based One-Time Password (TOTP) authenticator app of your choice, such as Google Authenticator or Microsoft Authenticator, to access your account with the added security of multi-factor authentication.
* **Passkey**—Use your passkey device to authenticate.

If you define more than one method, you will see the choice of authentication methods when you log in.

<Callout icon="📘" theme="info">
  Pismo recommends that once you add a more secure MFA method, you should remove the email verification method from your authentication list. Refer to [Remove an authentication method](https://developers.pismo.io/pismo-doc:add-methods-for-mfa#remove-an-authentication-method) for details.
</Callout>

## Add an Authenticator app

You can add any TOTP authenticator application, such as Google Authenticator or Microsoft Authenticator, to access your Control Center account. To do this, you need to first download the authenticator application and then register or pair it with your account. Pairing creates a trust between your authenticator application and your account so that you can use it to authenticate when you log in.

To add an authenticator application as a log in authentication option:

1. Download the authenticator application of your choice to your mobile device.
2. Log into Control Center and on your profile menu, select **Manage authentication**. You can view the profile menu from the profile icon (the person) in the top-right corner of the header.
3. On the **Authentication** screen, select **Add Method**.
4. On the **Select Method** pop-up pane, select **Authenticator App**. An **Authenticator App** pairing pane displays with a pairing QR code.
5. Scan the QR code with the authenticator application and enter the code.
6. Select **Finish**. Your authenticator application is now paired with your account and it will display in the authenticator as **Pismo Control Center: username**.
   * You will receive an email to the email address associated with your Control Center user with the subject "New authentication device added". No action is needed as it is just a confirmation that you have added an authenticator application to your account.
   * The next time you log in to Control Center, you will see the authentication option **Authenticator app**. You can change this option name, if you'd like.

## Add a passkey

A passkey is a Fast Identity Online (FIDO2) authentication method that allows you to log in to applications and websites with the same method you use to unlock your device, such as biometrics, PIN, or pattern. Passkeys are strong, password-less secondary authentication using public key cryptography credentials.

Passkeys are considered the most secure of the three authentication methods for Control Center. There are a number of benefits of using FIDO2 passkeys:

* Stronger security—Passkeys are considered significantly resistant to phishing attacks.
* Improved user experience—Passkeys are a more convenient and streamlined option for MFA authentication.
* Standardized and interoperable—FIDO2 is an open standard that allows for interoperability between devices and platforms.

To add a passkey as a log in authentication option:

1. Log into Control Center and on your profile menu, select **Manage authentication**. You can view the profile menu from the profile icon (the person) in the top-right corner of the header.
2. On the **Authentication** screen, select **Add Method**.
3. On the **Select Method** pop-up pane, select **Passkey**.
4. On the Create a passkey prompt pop-up, select **Continue**.
5. You device will display a prompt for you to select the passkey option available on your device (fingerprint, password, etc.). Select one. A confirmation message is briefly displayed to indicate you have added a passkey and it is listed in the authentication methods list.

Your passkey is now associated with your account. This passkey is only saved on the device on which you created it.

* You will receive an email to the email address associated with your Control Center user with the subject "New authentication device added". No action is needed as it is just a confirmation that you have added a FIDO2 passkey to your account.
* The next time you log in to Control Center, you will see the authentication option **Passkey**. You can change this option name, if you'd like.

# Rename an authentication method

You have the option to rename an authentication method. For example, you can change the default "Authenticator app" to the name of the specific application, such as "Google Authenticator".

To rename an existing authentication method from your authentication list:

1. On your profile menu, select **Manage authentication**. You can view the profile menu from the profile icon (the person) in the top-right corner of the header.
2. On the **Authentication** screen, select the **More actions menu** next to the method you want to rename and select **Edit name**.
3. Enter the new name and select the checkmark. A success message briefly displays and the new name is displayed in the authentication methods list.

# Remove an authentication method

You can, at any time, remove an authentication method from your profile. However, at least one method is required. Therefore, if you currently only have one authentication option, you must add another before you can remove the first one.

To remove an existing authentication method from your authentication list:

1. On your profile menu, select **Manage authentication**.
2. On the **Authentication** screen, select the **More actions menu** next to the method you want to delete and select **Remove**.
3. Select **Remove** at the confirmation prompt. A success message briefly displays and the selected method is immediately removed from the authentication methods list.
<!-- source:end -->

## Lifecycle status

- `docs/control-center/get-access-and-sign-on.md`: updatedAt 2026-07-31T14:01:29.000Z.
- `docs/control-center/password-self-reset-control-center.md`: updatedAt 2026-03-18T15:09:17.000Z.
- `docs/control-center/cc-pw-best-practices.md`: updatedAt 2026-03-18T15:09:16.000Z.
- `docs/control-center/add-methods-for-mfa.md`: updatedAt 2026-06-10T20:31:21.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/get-access-and-sign-on.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-access-and-sign-on | `64439da75845f581…` | 2026-07-31T14:01:29.000Z |
| `docs/control-center/password-self-reset-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/password-self-reset-control-center | `32e73c8cdfb4ea62…` | 2026-03-18T15:09:17.000Z |
| `docs/control-center/cc-pw-best-practices.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cc-pw-best-practices | `d78f1c02fc259635…` | 2026-03-18T15:09:16.000Z |
| `docs/control-center/add-methods-for-mfa.md` | whole document | https://developers.pismo.io/pismo-docs/docs/add-methods-for-mfa | `d8d13b663ea82fc0…` | 2026-06-10T20:31:21.000Z |

## Related knowledge units

- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
