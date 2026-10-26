---
ku_id: KU-AUTH-control-center-security
title: Control Center security guide
category: authentication_and_security
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/security-guide-for-control-center.md
  sha256: c547d3b92871c4eb9a24cc7b1b1aab9e0d9d60bddfc14d594c4c827f5578be7e
  url: https://developers.pismo.io/pismo-docs/docs/security-guide-for-control-center
  role: primary_guide
  updated_at: '2026-08-05T13:28:32.000Z'
- path: docs/control-center/security-for-control-center.md
  sha256: 73fb9df522081fdd9eda7657c1a875ef0b6dad34f38f8a61484bef7a1014a195
  url: https://developers.pismo.io/pismo-docs/docs/security-for-control-center
  role: primary_guide
  updated_at: '2026-06-05T16:24:36.000Z'
operations: []
related_kus:
- KU-AUTH-control-center-sign-on-and-mfa
- KU-AUTH-control-center-sso-and-openid
- KU-CC-dual-approval
- KU-SUP-operations-status-and-sub-processors
grouping_rationale: Same topic from two areas.
---

# Control Center security guide

**KU ID:** `KU-AUTH-control-center-security` · **Category:** Authentication and security · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Same topic from two areas.

Scope as stated in `docs/get-started/security-guide-for-control-center.md`:

> Pismo is committed to providing you with a trusted set of financial services. We have used our cloud industry experience building enterprise software and running some of the world’s largest online services to create and implement a robust set of security technologies and practices. These practices help reduce the cost, complexity, and risk associated with security in the financial services cloud. Our mission is to deliver the highest levels of security, privacy, compliance, and availability to the financial sector and help you protect your business assets. Pismo invests annually in cybersecurity and employs dedicated cybersecurity professionals. We take a defense-in-depth approach to security on the Pismo platform, helping you strengthen your security posture, streamline your compliance efforts, and enable digital transformation.

Scope as stated in `docs/control-center/security-for-control-center.md`:

> Control Center has systems and policies in place to ensure and enforce security. These include requirements and processes related to the creation, authentication, and authorization of users and account and organization access. They also include defined practices for data retention and handling of Personally Identifiable Information (PII). Because passwords are a critical aspect of cybersecurity, the Control Center has implemented a strong list of requirements.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/security-guide-for-control-center.md`: Security guide for Control Center; Security and access for Control Center; Idle timeout; Authentication; User authentication and access; Multi-factor Authentication (MFA) in Control Center; Enterprise authentication; Authorization; Dual approval; Audit log; Data retention policy; Personal Identifiable Information (PII)
- `docs/control-center/security-for-control-center.md`: Control Center security

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/security-guide-for-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/security-guide-for-control-center · updatedAt: 2026-08-05T13:28:32.000Z

<!-- source:begin path=docs/get-started/security-guide-for-control-center.md part=0-end -->

# Security guide for Control Center

Pismo is committed to providing you with a trusted set of financial services. We have used our cloud industry experience building enterprise software and running some of the world’s largest online services to create and implement a robust set of security technologies and practices. These practices help reduce the cost, complexity, and risk associated with security in the financial services cloud. Our mission is to deliver the highest levels of security, privacy, compliance, and availability to the financial sector and help you protect your business assets. Pismo invests annually in cybersecurity and employs dedicated cybersecurity professionals. We take a defense-in-depth approach to security on the Pismo platform, helping you strengthen your security posture, streamline your compliance efforts, and enable digital transformation.

The Pismo platform follows an API-driven architecture. This design allows for seamless integration with various systems and services that you may have. Many of our clients chose to build their own UI on top of the Pismo platform. This method allows you to control all access and authentication to the Pismo platform, including single sign-on (SSO) and multi-factor authentication (MFA) policies. You can also access the Pismo platform through  Pismo Control Center.

# Security and access for Control Center

Pismo Control Center is a Web application that enables business users to perform various tasks on the Pismo platform. It is designed to enable business users to use the platform without having to understand the platform's REST APIs. You can use it to perform a variety of tasks, from managing financial transactions to overseeing customer accounts, all through an intuitive and accessible interface.

The Control Center UI currently supports English and Portuguese.

### Idle timeout

As a security measure, the Control Center enforces an idle timeout period of 60 minutes.

# Authentication

## User authentication and access

Authentication validates the identity of a user. It is typically handled by checking credentials, such as usernames and passwords. Pismo enforces strong password policies in Control Center. Refer to [Best practices for passwords in Control Center](https://developers.pismo.io/pismo-docs/docs/cc-pw-best-practices) for  requirements and tips to create a secure password. It also includes multi-factor authentication (MFA) through email.

When a client creates an organization (Org) in Control Center, they will be given an Admin user for that Org. That Admin user will receive two separate emails that will allow them to create their password. Once established as an Admin user, that Admin can then go into Control Center to create all users and give those users the correct roles. If there are multiple organizations, the Control Center Admin can assign users different roles for different organizations.

All new users created by the Admin will be sent the two emails to set their own password and access Control Center.  If the user has been assigned to more than one Org, they can see that in a drop-down list when they log in.

If a user has access to more than one organization in Control Center, they can switch to the one they want to view from Control Center header. When a user switches organizations, their permissions for the current Org are applied and they will only be able to access features in Control Center based on their roles for that current organization.

## Multi-factor Authentication (MFA) in Control Center

MFA is mandatory base setting for Control Center for the whole environment. MFA can also be managed directly by the client if they are using [Enterprise authentication](https://developers.pismo.io/pismo-docs/docs/security-guide-for-control-center#enterprise-authentication).

With MFA, upon initial login, all users are subject to email authentication. After the user enters their username and password, the platform sends a code to the email address linked to the user account. They must enter this code to complete the user registration process and log in. Emailing the registration code requires that everyone logging in to use the application has their valid email address registered with Pismo. If the registered email address is inactive or invalid, the user is unable to access the authentication code and therefore will be unable to log into the platform.

After initial registration, each user has the option to add other authentication methods, including an authenticator app and passkey, that they can select as subsequent login authentication.

## Enterprise authentication

An optional feature allows clients to add Single Sign-On (SSO) authentication to Control Center for a fee. This gives you the ability to have your organization’s users sign in to Pismo Control Center through an Identity Provider (IdP) using a single set of credentials. Pismo supports SSO with the Security Assertion Markup Language (SAML) 2.0 protocol. Any identity provider that supports SAML 2.0 works with Pismo. The advantage of this is that your IdP acts as a trusted service that manages user accounts and their authentication.

<Callout icon="📘" theme="info">
  Single sign-on (SSO) is only available to customers who have purchased it. Contact your Pismo representative for more information.
</Callout>

Note: If your company wants to maintain IP restrictions for Control Center, you can manage that using SSO.

For full details of SSO for Control Center, refer to the [Get started with SSO for Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-sso-for-control-center).

# Authorization

Once a user is authenticated, authorization defines the access rights for that user and limits access to only the resources permitted for that specific user. Authorization follows the concept of least privilege, where users receive the minimum access rights that are necessary for their jobs. Pismo uses role-based access control (RBAC) to enforce least privilege.

Within the Control Center, Admins and User managers can assign and manage user roles. Role management is limited to the defined roles within Control Center as custom roles are not supported. For a list of available roles, go to **Users & Permissions** in Control Center.

# Dual approval

Dual approval is an optional feature that requires agreement from two individuals to finalize certain changes to platform data. It provides an additional layer of oversight, which reduces the potential for errors and fraud.

Dual approval is applied at the organization level. Rather than making a change directly, Control Center saves the operation as a pending approval request and starts an approval workflow. When dual approval is active, rather than making a change directly, Control Center displays a popup message asking the user if they want to submit an approval request. Anyone with permission to make changes can request dual approval, but users must have specific roles to be an approver in this workflow.

For details about the dual approval feature, workflow, and approver roles, refer to the [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval) guide for Control Center.

# Audit log

The Pismo platform maintains a history of all operations that users perform in Control Center. Use the Audit feature within the Control Center to access this data. There is an export option for reporting purposes.

In addition, you can monitor system status through the **Status Page** in Control Center. To subscribe to status page updates refer to the [Pismo operations status](https://developers.pismo.io/pismo-docs/docs/pismo-operations-status) guide.

# Data retention policy

At Pismo, we follow defined policies regarding retention of records and information. This is summarized as follows:

* Records and information are retained and disposed of in accordance with a retention schedule.
* Records remain readable, immutable, retrievable, and accessible throughout their required retention period.
* Records are protected in safe and secure conditions.
* Once a record has been finalized, drafts and working copies become non-record information and are not retained as records unless instructed by the Legal Department that destruction has been suspended, such as for active or anticipated litigation, audit, or government investigation (“Legal Hold”).
* Records and information are kept for no longer than necessary for their identified business purpose unless subject to additional legal or regulatory requirements.
* Personal information that has been de-personalized or otherwise rendered unusable and unidentifiable pursuant to applicable privacy regulations is presumed to be compliant with the policy.
* All records and information created pursuant to our business activities are proprietary information and do not belong to an individual. All employees are required to return records and information upon request or when leaving the company. Staff also ensures that third parties return all records and information upon request or termination of contract.

## Personal Identifiable Information (PII)

Pismo is continuously monitoring data privacy legislation and will continue to comply with relevant data privacy legislation. At Pismo, we adhere to regional data protection restrictions for the physical location of where the data is stored.

Toward that end, we match the following global privacy rules for data stored in the associated regions:

| Regulation                                  | Compliance notes                                                                                                                                  |
| :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| General Data Protection Regulation (GDPR)   | The Pismo platform supports data retention policies and is designed to ensure GDPR compliance to address regulatory requirements.                 |
| General Personal Data Protection Law (LGPD) | Personal data protection law for Brazil, equivalent to GDPR.                                                                                      |
| Digital Personal Data Protection (DPDP)     | Data protection policy for India.                                                                                                                 |
| Personal Data Protection Act (PDPA)         | Data protection policy for Singapore and the Philippines.                                                                                         |
| Information Security Manual (ISM)           | Australian government’s primary Cloud compliance and security regulation. It is enforced through the Infosec Registered Assessors Program (IRAP). |
| Consumer Privacy Act (CCPA)                 | Data privacy act for the state of California, United States.                                                                                      |
<!-- source:end -->

### Source 2: `docs/control-center/security-for-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/security-for-control-center · updatedAt: 2026-06-05T16:24:36.000Z

<!-- source:begin path=docs/control-center/security-for-control-center.md part=0-end -->

# Control Center security

Control Center has systems and policies in place to ensure and enforce security. These include requirements and processes related to the creation, authentication, and authorization of users and account and organization access. They also include defined practices for data retention and handling of Personally Identifiable Information (PII). Because passwords are a critical aspect of cybersecurity, the Control Center has implemented a strong list of requirements.

For details on these items and more, refer to these resources:

* [Security guide for Control Center](https://developers.pismo.io/pismo-docs/docs/security-guide-for-control-center)—General high-level security information
* [Best practices for Control Center passwords](https://developers.pismo.io/pismo-docs/docs/cc-pw-best-practices)—Password requirements and tips for creating secure passwords
* [Reset your password](https://developers.pismo.io/pismo-docs/docs/password-self-reset-control-center)—Instructions for resetting your password
* [Get started with SSO for Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-sso-for-control-center)—Single sign-on (SSO) is only available to customers who have purchased it. Contact your Pismo representative for more information.
* [Add additional methods for multi-factor authentication (MFA)](https://developers.pismo.io/pismo-docs/docs/add-methods-for-mfa)—When you first sign on to Control Center, you’re already set up with email verification as your MFA method. For stronger protection, Pismo recommends adding a passkey, an authenticator app, or both. Use this guide for step-by-step instructions.

<br />
<!-- source:end -->

## Lifecycle status

- `docs/get-started/security-guide-for-control-center.md`: updatedAt 2026-08-05T13:28:32.000Z.
- `docs/control-center/security-for-control-center.md`: updatedAt 2026-06-05T16:24:36.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/security-guide-for-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/security-guide-for-control-center | `c547d3b92871c4eb…` | 2026-08-05T13:28:32.000Z |
| `docs/control-center/security-for-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/security-for-control-center | `73fb9df522081fdd…` | 2026-06-05T16:24:36.000Z |

## Related knowledge units

- `KU-AUTH-control-center-sign-on-and-mfa` — Control Center sign-on, passwords and multi-factor authentication
- `KU-AUTH-control-center-sso-and-openid` — Control Center SSO and OpenID Connect configuration
- `KU-CC-dual-approval` — Dual approval
- `KU-SUP-operations-status-and-sub-processors` — Pismo operations status and platform sub-processors
