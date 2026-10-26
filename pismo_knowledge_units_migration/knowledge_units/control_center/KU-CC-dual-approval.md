---
ku_id: KU-CC-dual-approval
title: Dual approval
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/dual-approval.md
  sha256: 6e916e5a9e32d8a0975a09bcb722e6e7ec0eaa9187455065b76181a5c5895e31
  url: https://developers.pismo.io/pismo-docs/docs/dual-approval
  role: primary_guide
  updated_at: '2026-09-02T08:40:03.000Z'
operations: []
related_kus:
- KU-AUTH-authentication-methods
- KU-AUTH-control-center-sso-and-openid
- KU-CC-accounts
- KU-CC-cards
- KU-CC-control-center-navigation
- KU-CC-lending
- KU-CC-programs
- KU-CORE-working-with-limits-objects
grouping_rationale: single source page
---

# Dual approval

**KU ID:** `KU-CC-dual-approval` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/control-center/dual-approval.md`:

> Use dual approval to add a layer of oversight to critical processes. Dual approval is a security and governance feature that requires two separate individuals to review and approve a critical action or data change before it's finalized. One person initiates the request and a second person reviews and approves it. This process helps to prevent errors and unauthorized changes and reduces fraud.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/dual-approval.md`: Dual approval; Permissions; Notifications; Status; View requests; Send requests for approval; Cancel requests; Approve or reject requests; Frequently asked questions

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/dual-approval.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/dual-approval · updatedAt: 2026-09-02T08:40:03.000Z

<!-- source:begin path=docs/control-center/dual-approval.md part=0-end -->

# Dual approval

Use dual approval to add a layer of oversight to critical processes. Dual approval is a security and governance feature that requires two separate individuals to review and approve a critical action or data change before it's finalized. One person initiates the request and a second person reviews and approves it. This process helps to prevent errors and unauthorized changes and reduces fraud.

Dual approval is also known as the maker/checker model, where the maker (requester) initiates the change request, and the checker (approver) reviews and authorizes it.

Your company must opt-in to use dual approval by requesting dual approval for each process where it’s required.

<Accordion title="Dual approval is available for the following Control Center processes:">
  <ul>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters">Edit a program parameter</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/account-actions">Make a single adjustment to an account</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/account-actions">Change account status</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/card-information">Unblock card (due to too many PIN tries)</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/access-keys-for-basic-authentication">Create or deactivate an access key</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/openid-configurations">Create, edit, or deactivate an OpenID authentication configuration</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/account-actions">Hold, release, or transfer funds</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects">Edit account limits</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/manage-loans-in-control-center">Disburse or adjust a loan</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/card-information#view-and-edit-card-information">Edit card information</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/card-information#reissue-a-card">Reissue a card</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/accounts-overview-cc#account-views">Issue refund</a></li>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/account-configurations-in-control-center#addresses">Edit address</a></li>
  </ul>
</Accordion>

This guide introduces the principles of dual approval and shows you what actions to take.

* Ensure you have the correct [permissions](https://developers.pismo.io/pismo-docs/docs/dual-approval#permissions)
* Understand [notifications](https://developers.pismo.io/pismo-docs/docs/dual-approval#notifications)
* Become familiar with the [status](https://developers.pismo.io/pismo-docs/docs/dual-approval#status) of requests
* Learn what you can do with requests:
  * [View requests](https://developers.pismo.io/pismo-docs/docs/dual-approval#view-requests)
  * [Send requests for approval](https://developers.pismo.io/pismo-docs/docs/dual-approval#send-requests-for-approval)
  * [Cancel requests](https://developers.pismo.io/pismo-docs/docs/dual-approval#cancel-requests)
  * [Approve or reject requests](https://developers.pismo.io/pismo-docs/docs/dual-approval#approve-or-reject-requests)
* Refer to [frequently asked questions](https://developers.pismo.io/pismo-docs/docs/dual-approval#frequently-asked-questions) for answers to the most common questions

# Permissions

Your permissions determine the information that's available to you and the actions that you can perform for dual approval. Permissions are a collection of roles assigned to your user account, based on tasks you need to perform. If you have questions or need your permissions updated, contact your Control Center administrator.

* **Send approval requests and view requests**—The same permissions you use to make or view changes also apply to dual approval. For example, if you can change a program parameter, you can also request dual approval for that parameter. Similarly, if you can view account changes, you can view dual approval requests for those changes.
* **Approve or reject requests**—To approve or reject a request, you must have the specific approver role for that request type. Refer to the following table for details.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Request type
      </th>

      <th>
        Approver role
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        * Edit a program parameter
      </td>

      <td>
        Setup approver
      </td>
    </tr>

    <tr>
      <td>
        * Make a single adjustment to an account
        * Change an account status
        * Unblock card (due to too many PIN tries)
        * Hold, release, or transfer funds
        * Edit account limits
        * Disburse or adjust a loan
        * Edit card information
        * Reissue a card
        * Issue refund
        * Edit address
      </td>

      <td>
        Backoffice approver
      </td>
    </tr>

    <tr>
      <td>
        * Create or deactivate an access key
        * Create, edit, or deactivate an OpenID authentication configuration
      </td>

      <td>
        API keys approver
      </td>
    </tr>
  </tbody>
</Table>

# Notifications

Control Center sends notifications as requests move through the approval process. For example, if you're an approver, you receive notifications when requests require your approval. If you're a requester, you receive notifications when your requests have been approved or rejected.

You can find all your notifications from the notification icon (the bell) in the top-right corner of the header. Select the link in the notification to open a dual approval request, where you'll find more details and actions you can take. For more information about notifications, refer to [Notifications](https://developers.pismo.io/pismo-docs/docs/control-center-navigation#notifications).

# Status

Control Center displays the current status of each request and keeps a history of status changes. You can view statuses on both the **Dual approval** screen and on the individual request details screens.

The request statuses are:

* **Pending**—Request was submitted and is awaiting approval
* **Canceled**—Requester withdrew the request
* **Approved**—Approver approved the request
* **Rejected**—Approver rejected the request
* **Error**—Request failed due to an error

# View requests

There are several ways to view requests.

* **For requests received through notifications**—If your permissions allow, you’ll get a notification when a request’s status changes. Select the link in the notification to open the the request for more details.
* **For all requests**—To view all requests, from the main menu select **Users & permissions** > **Dual approval** > select the pending request.
* **For account change requests**—To view account change requests (such as single adjustments), from the main menu select **Customer operations** > **Accounts** > select the account  > **Requests & approvals** tab > select pending request.
* **For program parameter requests**—To view program parameter requests, from the main menu select **Configurations** > **Programs** > select the program >  **Parameters** tab > select pending parameter > select **configuration request** link on the modal.

# Send requests for approval

When you make a change that requires dual approval, Control Center displays a message prompting you to send the request for approval. The change doesn't take effect until it's approved. Throughout the approval process, Control Center sends status notifications to keep everyone informed.

Following is an example of the message for a single-adjustment request. Other types of requests display similar messages, though not exactly like this example.

<Image align="center" alt="Message prompting you to send a request for approval" border={true} width="60% " src="https://files.readme.io/421d304ab3a0240f4d45e2dd15708a1bcc8bdc74d6ddabb3e78b16d65545e2de-Screenshot_2025-08-25_at_11.12.32_AM.png" className="border" />

> 📘 Program parameter updates temporarily blocked
>
> To avoid conflicting changes, Pismo blocks updates to a program parameter while an approval request is under review. Once the request is approved or rejected, you can make other program parameter changes.

# Cancel requests

You can cancel your own requests that are in **Pending** status. When you cancel a request, all potential approvers are notified and the request history is updated. To cancel requests:

1. On the **Dual approval** screen, select the pending request you want to cancel.
2. On the **Request details** screen, select **Cancel request** and confirm.

# Approve or reject requests

To approve or reject requests:

1. On the **Dual approval** screen, select the pending request.
2. In the dialog, select **Approve** or **Reject**. If you reject a request, you'll be prompted to give a short reason.

<Image align="center" alt="Dialog box for approving and rejecting requests" border={true} width="160% " src="https://files.readme.io/18e57ee73546c416454e320be32670a1e076c983ac232df0d3947ac26c43d3f9-Screenshot_2025-08-25_at_11.06.16_AM.png" className="border" />

# Frequently asked questions

**Question:** What happens if the approver is not available to review the request?

**Answer:** The approver is an assigned role and not a specific person. You should assign multiple people to the approver role so that anyone with the role can review the request.

***

**Question:** Is there a report that tells me if there are old requests?

**Answer:** No, but you can filter the **Dual approval** page by status and date to view pending requests older than 7 or 30 days.

***

**Question:** What happens if there’s an API failure after I’ve sent a request for approval?

**Answer:** If an API failure occurs, your request is processed immediately without dual approval to keep workflows running. For example, your request for an account status change will take effect right away, without dual approval.

***

**Question:** What if my approval request reached the approver, but then the API fails?

**Answer:** In this case, the approval or rejection won’t go through. Both you and the approver will see an error notification and a report log. Once the API is restored, you'll need to resubmit your request.
<!-- source:end -->

## Lifecycle status

- `docs/control-center/dual-approval.md`: updatedAt 2026-09-02T08:40:03.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/dual-approval.md` | whole document | https://developers.pismo.io/pismo-docs/docs/dual-approval | `6e916e5a9e32d8a0…` | 2026-09-02T08:40:03.000Z |

## Related knowledge units

- `KU-AUTH-authentication-methods` — API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys
- `KU-AUTH-control-center-sso-and-openid` — Control Center SSO and OpenID Connect configuration
- `KU-CC-accounts` — Control Center accounts: overview, management, actions and configurations
- `KU-CC-cards` — Control Center cards: card information and card network tokenization
- `KU-CC-control-center-navigation` — Navigate Control Center
- `KU-CC-lending` — Control Center lending: loan products and loan management
- `KU-CC-programs` — Control Center programs: create, edit, clone, export and import
- `KU-CORE-working-with-limits-objects` — Account limits
