---
ku_id: KU-SUP-service-desk-requests
title: 'Pismo Service Desk: opening, tracking and modifying requests'
category: rate_limits_and_support
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/resources/service-desk.md
  sha256: 5fd05a0e5f74608f7d39eecab4b1c7d501470c8dc35f82b2c3191e9e93a73121
  url: https://developers.pismo.io/pismo-docs/docs/service-desk
  role: primary_guide
  updated_at: '2026-06-30T14:11:30.000Z'
- path: docs/resources/support.md
  sha256: 9d2eed33cb172f65208b6047f078f8b052293caff62aa750c3b619d8ec4d113a
  url: https://developers.pismo.io/pismo-docs/docs/support
  role: primary_guide
  updated_at: '2026-04-03T17:50:18.000Z'
- path: docs/resources/opening-a-service-desk-ticket.md
  sha256: bbec95cf212974582bcf0dd81ffc083a5cc8a27cb24c63b2e4137bab0d0422cb
  url: https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket
  role: primary_guide
  updated_at: '2026-06-16T14:49:13.000Z'
- path: docs/resources/modify-a-service-request.md
  sha256: a803c608ebddd4471b973a46184a3a734750e1a9452ef9410174be1083d4ac63
  url: https://developers.pismo.io/pismo-docs/docs/modify-a-service-request
  role: primary_guide
  updated_at: '2026-04-03T17:50:18.000Z'
- path: docs/resources/track-a-service-request.md
  sha256: 88a4852249beeac6666c4d54046721c7c77fe2df8dbff454b6730d11254059a3
  url: https://developers.pismo.io/pismo-docs/docs/track-a-service-request
  role: primary_guide
  updated_at: '2026-04-03T17:50:18.000Z'
- path: docs/resources/request-types.md
  sha256: 98ca3ddc90dd481ebc8ebbcdd35f63d4631f7f9f1855d8c7044790a243755b75
  url: https://developers.pismo.io/pismo-docs/docs/request-types
  role: primary_guide
  updated_at: '2026-06-16T14:49:13.000Z'
- path: docs/resources/requests-for-access.md
  sha256: eda00d54cf5ed50ea5cd13fd6e2d1c7ee1e19a4a9959ef336007f8b48ec8fcd9
  url: https://developers.pismo.io/pismo-docs/docs/requests-for-access
  role: primary_guide
  updated_at: '2026-06-16T14:49:13.000Z'
- path: docs/resources/non-incident-lifecycle.md
  sha256: 0f62437bb06b5c33409c2af84d6d49057d1c2d6bd9891137c210b43878c8519a
  url: https://developers.pismo.io/pismo-docs/docs/non-incident-lifecycle
  role: primary_guide
  updated_at: '2026-06-16T14:49:13.000Z'
- path: docs/resources/requesting-a-performance-test.md
  sha256: 6df67c4594f74f383fe0be4608fb2f967bbcb54be2d573dcaa9725a172cd0771
  url: https://developers.pismo.io/pismo-docs/docs/requesting-a-performance-test
  role: primary_guide
  updated_at: '2026-07-27T19:41:13.000Z'
operations: []
related_kus:
- KU-AUTH-control-center-permissions-and-roles
- KU-CC-get-started-control-center
- KU-GS-environments
- KU-SUP-incidents
- KU-SUP-operations-status-and-sub-processors
grouping_rationale: One request workflow split across short pages.
---

# Pismo Service Desk: opening, tracking and modifying requests

**KU ID:** `KU-SUP-service-desk-requests` · **Category:** Rate limits and support · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 9 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: One request workflow split across short pages.

Scope as stated in `docs/resources/service-desk.md`:

> The Pismo Service Desk enables you to <Anchor label="open" target="_blank" href="doc:opening-a-service-desk-ticket">open</Anchor> and <Anchor label="track" target="_blank" href="doc:track-a-service-request">track</Anchor> service requests. For information about the types of requests you can submit, refer to [Request types](https://developers.pismo.io/pismo-docs/docs/request-types).

Scope as stated in `docs/resources/support.md`:

> Pismo is committed to maintaining maximum platform availability and resolving technical issues as swiftly and completely as possible. To ensure this, Pismo provides the following resources and support tools:

Scope as stated in `docs/resources/opening-a-service-desk-ticket.md`:

> Follow the steps in this guide to open a service request.

Scope as stated in `docs/resources/modify-a-service-request.md`:

> You can update your service request at any time by escalating, canceling, or reopening it—depending on your needs and the status of the ticket.

Scope as stated in `docs/resources/track-a-service-request.md`:

> Pismo aims to restore normal service operation as quickly as possible. In general, the on-call support team acknowledges all incident requests within 15 minutes. Mitigation can take up to four hours for critical incidents, and up to three days for lower-priority incidents.

Scope as stated in `docs/resources/request-types.md`:

> This guide provides information about the types of service requests you can open using the Pismo Service Desk.

Scope as stated in `docs/resources/requests-for-access.md`:

> This guide provides information on requesting Pismo resources pertaining to existing production programs, such as those affecting business rules, changing rates, spending controls, accounting, ICA, embossing, and so on.

Scope as stated in `docs/resources/non-incident-lifecycle.md`:

> This workflow is standard and applies to the following requests:

Scope as stated in `docs/resources/requesting-a-performance-test.md`:

> You can request a performance test to assess how efficiently your implementation operates on the Pismo platform. The test results return performance-related information, such as Transactions Per Second (TPS) measurements (min, average, and max) and number of pods in use. This also allows you to enable the production environment in advance, in case of uncertainties or concerns about system behavior.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/resources/service-desk.md`: Pismo Service Desk
- `docs/resources/support.md`: Support
- `docs/resources/opening-a-service-desk-ticket.md`: Open a service request
- `docs/resources/modify-a-service-request.md`: Modify a service request; Escalate a request; Modify a request
- `docs/resources/track-a-service-request.md`: Track a service request
- `docs/resources/request-types.md`: Request types and common fields; Request types; Common fields
- `docs/resources/requests-for-access.md`: Request access to Pismo resources
- `docs/resources/non-incident-lifecycle.md`: Non-incident lifecycle; Non-incident request status
- `docs/resources/requesting-a-performance-test.md`: Request a performance test; Prerequisites

## Prerequisites and dependencies

- Prerequisites are described in `docs/resources/requesting-a-performance-test.md` section "Prerequisites".

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/resources/service-desk.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/service-desk · updatedAt: 2026-06-30T14:11:30.000Z

<!-- source:begin path=docs/resources/service-desk.md part=0-end -->

# Pismo Service Desk

The Pismo Service Desk enables you to <Anchor label="open" target="_blank" href="doc:opening-a-service-desk-ticket">open</Anchor> and <Anchor label="track" target="_blank" href="doc:track-a-service-request">track</Anchor> service requests. For information about the types of requests you can submit, refer to [Request types](https://developers.pismo.io/pismo-docs/docs/request-types).

> 📘
>
> For information about getting a Service Desk user account, refer to [Request access to Pismo resources](https://developers.pismo.io/pismo-docs/docs/requests-for-access).

When you open the Pismo Service Desk page, you see a number of request links. A detailed description of each of the links is described below.

<Image align="center" alt="Screenshot of Pismo Service Desk" border={true} src="https://files.readme.io/60931d0f153a2f24ca1295ac0cda31d69714db3c6212ddb9a1e961d0342d10c6-image.png" className="border" />

You can request help with the following items on the Pismo Service Desk page:

**<Anchor label="Incident" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/171">Incident</Anchor>**\
Use this form to report an incident. An incident includes any and all failure events or abnormal behavior of the service or system (application) in a production environment that meets at least one of the following conditions:

* Unavailability in the execution of operational activities of the business areas;
* Presence of a vital impact on the continuity of operations under the responsibility of the business areas.

Any problem outside the conditions mentioned above must be opened as a ticket in the <Anchor label="Occurrence/Event" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/166">Occurrence/Event</Anchor> form.

If you have problems/errors obtained outside the production environment (EXT/UAT), open a ticket in the <Anchor label="Sandbox" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/165">Sandbox</Anchor> form.

If you have any questions about the functionality of services or systems, open a ticket in the <Anchor label="Question" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/167">Question</Anchor> form.

**<Anchor label="Occurrence/Event" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/166">Occurrence/Event</Anchor>**

Use this form whenever a request presents problems without causing broad or general failure of a service.

**<Anchor label="Sandbox" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/165">Sandbox</Anchor>**

Use this form when you need help with error results that you encounter outside of the production environment.

**<Anchor label="Question" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/167">Question</Anchor>**

Use this form whenever you are unclear about a particular result you're experiencing, when information is unclear, or when you are experiencing errors or problems.

**<Anchor label="Projects" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/168">Projects</Anchor>**

Use this form to request an improvement, a new service, or new features.

**<Anchor label="Performance Test" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/454">Performance Test</Anchor>**

Use this form when you want to test the platform's performance capacity or migration.

**<Anchor label="Deployment Window" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/1568">Deployment Window</Anchor>**

Use this form for requests that are related to the deployment window.

**<Anchor label="Settings" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/1733">Settings</Anchor>**

Use this form for requests pertaining to existing production programs, such as those affecting business rules, changing rates, spending controls, accounting, ICA, embossing, and so on.
<!-- source:end -->

### Source 2: `docs/resources/support.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/support · updatedAt: 2026-04-03T17:50:18.000Z

<!-- source:begin path=docs/resources/support.md part=0-end -->

# Support

Pismo is committed to maintaining maximum platform availability and resolving technical issues as swiftly and completely as possible. To ensure this, Pismo provides the following resources and support tools:

* [Pismo Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk): Tracking system for submitted technical issues, questions, and suggestions.
* [Pismo operations status](https://developers.pismo.io/pismo-docs/docs/pismo-operations-status): Status page for daily systems availability, scheduled maintenance, and reported incidents.
<!-- source:end -->

### Source 3: `docs/resources/opening-a-service-desk-ticket.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket · updatedAt: 2026-06-16T14:49:13.000Z

<!-- source:begin path=docs/resources/opening-a-service-desk-ticket.md part=0-end -->

# Open a service request

Follow the steps in this guide to open a service request.

**To open a Service Desk request:**

1. Go to [https://pismolabs.atlassian.net/servicedesk](https://pismolabs.atlassian.net/servicedesk/). If you don't have access, refer to [Request access to Pismo resources](https://developers.pismo.io/pismo-docs/docs/requests-for-access).

2. Log in with your email and password.

3. Select **PISMO | Service Desk** (Portuguese) or **PISMO | Service Desk EN** (English).

4. Choose the appropriate request type. For more information, refer to [Request types](https://developers.pismo.io/pismo-docs/docs/request-types). Request types include the following:

   * **[Incident](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/171)** - Use this form to report an incident. An incident includes any and all failure events or abnormal behavior of the service or system (application) in a production environment.
   * **[Occurence/Event](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/166)** - Use this form whenever a request presents problems without causing broad or general failure of a service.
   * **<Anchor label="Non-production environment" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/165">Non-production environment</Anchor>** - Use this form when you need help with error results that you encounter outside of the production environment.
   * **[Question](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/167)** - Use this form whenever you are unclear about a particular result you're experiencing, when information is unclear, or when you are experiencing errors or problems.
   * **[Projects](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/168)** - Use this form to request an improvement, a new service, or new features.
   * **[Performance Test](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/454)** - Use this form when you want to test the platform's performance capacity or migration.
   * **[Deployment Window](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/1568)** - Use this form for requests that are related to the deployment window.
   * **[Settings](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/1733)** - Use this form for requests pertaining to existing production programs, such as those affecting business rules, changing rates, spending controls, accounting, ICA, embossing, and so on.

5. Enter information into all required form fields. Describe the problem with as much detail as possible (for more information, refer to [Describing an issue](https://developers.pismo.io/pismo-docs/docs/describing-an-issue)).

6. Select **Send** to submit your form.
<!-- source:end -->

### Source 4: `docs/resources/modify-a-service-request.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/modify-a-service-request · updatedAt: 2026-04-03T17:50:18.000Z

<!-- source:begin path=docs/resources/modify-a-service-request.md part=0-end -->

# Modify a service request

You can update your service request at any time by escalating, canceling, or reopening it—depending on your needs and the status of the ticket.

# Escalate a request

Pismo automatically escalates every incident request, no matter what the severity is. It is Pismo's responsibility to evaluate the incident and determine its priority based on the impact that it has. To help ensure that your issue is evaluated properly, it is important to provide a specific and detailed description of your issue (for more information, refer to [Describing an issue](https://developers.pismo.io/pismo-docs/docs/describing-an-issue)). To report an incident, refer to [Open a service request](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket).

After 30 minutes, for incident requests that are classified as Priority 1 (P1) or Priority 2 (P2), an **Escalate** button displays on the portal. This option to escalate an incident ticket will help you get more information about what is going on. This will send a call to the team that is working on the ticket saying that the client is asking for an update.

# Modify a request

**To modify Service Desk requests:**

1. Go to [ https://pismolabs.atlassian.net/servicedesk/](https://pismolabs.atlassian.net/servicedesk/).

2. Select the profile icon at the top right of the screen and then select   **Requests**.

<Image alt="Pismo service desk screenshots Requests menu item" align="center" className="border" border={true} src="https://files.readme.io/39d483faaa09a40e5775d0b88f1d44b1231fb8e018884725acc76276efcb9873-version_C.png" />

3. Use the search result filters as needed to find specific results.

<Image title="requests.png" alt="Pismo service desk filtered requests table" align="center" className="border" border={true} src="https://files.readme.io/0595872-requests.png" />

4. You can cancel an unclosed ticket at any time using the **Cancel Ticket** link.

<Image align="center" className="border" border={true} src="https://files.readme.io/26b731a55d9fe687af192773d3ec32196b1a683c72127f9781047699be4c36c3-image.png" />

5. If you are not satisfied with the resolution of your ticket, you should reopen your request instead of submitting a new one. This can be done by opening your ticket and selecting the Reopen link.

<Image align="center" className="border" border={true} src="https://files.readme.io/923ca552d241c5a492900cf1accf23b59acc57be655b5a0f016f4c221bb8b327-image.png" />
<!-- source:end -->

### Source 5: `docs/resources/track-a-service-request.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/track-a-service-request · updatedAt: 2026-04-03T17:50:18.000Z

<!-- source:begin path=docs/resources/track-a-service-request.md part=0-end -->

# Track a service request

Pismo aims to restore normal service operation as quickly as possible. In general, the on-call support team acknowledges all incident requests within 15 minutes. Mitigation can take up to four hours for critical incidents, and up to three days for lower-priority incidents.

After you [open a service request](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket), you are redirected to a page showing request details. You also should receive a confirmation email.

The following options appear on the page's right-hand side:

* **Enable/disable system notifications**: If enabled, you receive emails about status changes, added comments, and other activity. If disabled, you receive emails when requests are closed.
* **Share the ticket with others**: Shares the request with other team or company members.

> 📘 Reopen a request
>
> If you are not satisfied with a resolution, you should reopen your request instead of submitting a new one. For more information, refer to [Modify a service request](https://developers.pismo.io/pismo-docs/docs/modify-a-service-request).

**To track Service Desk requests:**

1. Go to [ https://pismolabs.atlassian.net/servicedesk/](https://pismolabs.atlassian.net/servicedesk/).

2. Select the profile icon at the top right of the screen and then select   **Requests**.

<Image align="center" alt="Pismo service desk screenshots Requests menu item" border={true} src="https://files.readme.io/39d483faaa09a40e5775d0b88f1d44b1231fb8e018884725acc76276efcb9873-version_C.png" className="border" />

3. Use the search result filters as needed to find specific results.

<Image align="center" alt="Pismo service desk filtered requests table" border={true} src="https://files.readme.io/0595872-requests.png" title="requests.png" className="border" />
<!-- source:end -->

### Source 6: `docs/resources/request-types.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/request-types · updatedAt: 2026-06-16T14:49:13.000Z

<!-- source:begin path=docs/resources/request-types.md part=0-end -->

# Request types and common fields

This guide provides information about the types of service requests you can open using the Pismo Service Desk.

# Request types

> 📘 Operational Level Agreements
>
> Each request type has an Operational Level Agreement (OLA) that defines the expected resolution time based on the issue's nature and urgency.

The following table describes the different types of requests and their OLAs.

**Note:** Table entries marked **N/A** indicate **Not Applicable**.

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Request type
      </th>

      <th>
        Description
      </th>

      <th>
        Operational Level Agreement (OLA)
      </th>

      <th>
        Comments
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Incident
      </td>

      <td>
        A service, system, or application has failed or is not functioning correctly.
      </td>

      <td>
        **Acknowledgement**: 15 minutes.

        **Mitigation**: Up to 4 hours for critical incidents; up to 3 business days for lower-priority incidents.
      </td>

      <td>
        **Impacted**: Number of affected users.

        **Severity**: Severity of the incident
      </td>
    </tr>

    <tr>
      <td>
        Occurrence/Event
      </td>

      <td>
        Occurrence is the record of a bug, error, or suspected failure that requires IT support, without causing a broad or generalized service outage.\
        It may involve impact to specific functionalities, access channels, or defined groups of users or clients.
      </td>

      <td>
        3 business days
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Non-production environment
      </td>

      <td>
        An issue is occurring in a non-production environment.
      </td>

      <td>
        7 business days
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Question
      </td>

      <td>
        You have a general question or need clarification.
      </td>

      <td>
        7 business days
      </td>

      <td>
        Describe the issue as best you can. This is the most important form field (refer to [Describing an issue](https://developers.pismo.io/pismo-docs/docs/describing-an-issue)).
      </td>
    </tr>

    <tr>
      <td>
        Projects
      </td>

      <td>
        You are suggesting an improvement, a new service, or new feature.
      </td>

      <td>
        Varies according to prioritization and analysis.
      </td>

      <td>
        **Scope**: Project objectives or functional specifications about the improvement/new feature.

        **Priority**: Priority of this project/new feature.
      </td>
    </tr>

    <tr>
      <td>
        Performance Test
      </td>

      <td>
        Refer to [Request a performance test](https://developers.pismo.io/pismo-docs/docs/requesting-a-performance-test).
      </td>

      <td>
        N/A
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Deployment Window
      </td>

      <td>
        You have a request related to the deployment window.
      </td>

      <td>
        N/A
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Settings/Configuration
      </td>

      <td>
        You have a request pertaining to existing programs in production, such as those affecting business rules, changing rates, spending controls, and so on.
      </td>

      <td>
        10 business days
      </td>

      <td>
        Select your configuration category and subcategory.
      </td>
    </tr>
  </tbody>
</Table>

# Common fields

The following fields are common to most service request types:

* **Summary**: Provide a high-level issue description.
* **Description**: Describe the issue with as much detail as possible. This is the most important form field. For more information, refer to [Describing an issue](https://developers.pismo.io/pismo-docs/docs/describing-an-issue).
* **Category** (and sub-category): Select an issue category, such as Credit, Digital Account, and so on. The adjacent column is then populated with a sub-category drop-down menu for you to choose from.
* **Share with**: Choose the company that this request pertains to.
* **API**: Select an affected API.
* **X-CID**: This is a correlation identifier field used internally by Pismo to link related API requests and events.
<!-- source:end -->

### Source 7: `docs/resources/requests-for-access.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/requests-for-access · updatedAt: 2026-06-16T14:49:13.000Z

<!-- source:begin path=docs/resources/requests-for-access.md part=0-end -->

# Request access to Pismo resources

This guide provides information on requesting Pismo resources pertaining to existing production programs, such as those affecting business rules, changing rates, spending controls, accounting, ICA, embossing, and so on.

> 📘 Pismo Control Center access and roles
>
> For access to [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center), contact your Pismo representative. If you need additional access, contact any user who has the Admin or User manager role. For more information, refer to [User permissions and roles](https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles).

**To make an access request via the Pismo Service Desk:**

1. In a web browser, open [https://pismolabs.atlassian.net/servicedesk/](https://pismolabs.atlassian.net/servicedesk/).
2. Select **PISMO | Service Desk EN**.
3. Go to the next section and select **Settings**.
4. On the request form, enter a short description of your request in the **Summary** field.
5. In the **Settings** menus, select the **Access request** type and for the **subtype** select  one of the following:

   1. **Service Desk Portal**
   2. **Slack Connect**
   3. **Status Page**

<Image align="center" alt="Service desk screenshot" border={true} src="https://files.readme.io/83d8fb2-2024-07-31_13-49-02.png" className="border" />

6. In the **Priority** menu, select a value from **Highest** to **Lowest**.
7. In the **Description** field, make sure to include the following:
   1. Email address of the users to be added.
   2. For Slack access, provide the name of the channel. This usually is in the form `_<company_name>_pismo`. For example `_xyzbank_pismo`.
8. Select **Send**.
<!-- source:end -->

### Source 8: `docs/resources/non-incident-lifecycle.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/non-incident-lifecycle · updatedAt: 2026-06-16T14:49:13.000Z

<!-- source:begin path=docs/resources/non-incident-lifecycle.md part=0-end -->

# Non-incident lifecycle

This workflow is standard and applies to the following requests:

* Occurrence/Event
* Question
* Non-production environment
* Projects
* Performance Tests
* Settings

# Non-incident request status

The following table describes the request status values.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Status
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Open
      </td>

      <td>
        Request is awaiting service.  This is the status when a request is first created or has been re-opened.
      </td>
    </tr>

    <tr>
      <td>
        In progress
      </td>

      <td>
        Resolution or development is in progress.
      </td>
    </tr>

    <tr>
      <td>
        Pending
      </td>

      <td>
        Waiting for more information from you.

        <ul>
          <li>After answering the questions, select **To Do** to submit your answers.</li>
          <li>If no action is taken within **80 business hours**, the request moves automatically to **Closed** status.</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>
        Resolved / Validating
      </td>

      <td>
        Request has been resolved.

        <ul>
          <li>At this point, you can either close the request or select **Reopened**, to reopen it if you are not satisfied.</li>
          <li>If no action is taken within **120 hours**,  the request moves automatically to **Closed** status.</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>
        Closed
      </td>

      <td>
        Request has been resolved to your satisfaction.
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

### Source 9: `docs/resources/requesting-a-performance-test.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/requesting-a-performance-test · updatedAt: 2026-07-27T19:41:13.000Z

<!-- source:begin path=docs/resources/requesting-a-performance-test.md part=0-end -->

# Request a performance test

You can request a performance test to assess how efficiently your implementation operates on the Pismo platform. The test results return performance-related information, such as Transactions Per Second (TPS) measurements (min, average, and max) and number of pods in use. This also allows you to enable the production environment in advance, in case of uncertainties or concerns about system behavior.

# Prerequisites

To run a performance test, you’ll need a data set. You have three options:

* Upload your own data set tailored to your implementation.
* Use an anonymized data set generated by Pismo.
* Select an existing data set already added to your Pismo test environment.

Choose the option that best fits your testing goals and environment setup.

> 🚧 Requirements
>
> * Pismo must analyze and approve any requests for performance testing.
> * You must schedule your tests at least 15 calendar days in advance.

**To open an access request:**

1. In a web browser, open [https://pismolabs.atlassian.net/servicedesk/](https://pismolabs.atlassian.net/servicedesk/).
2. Select **PISMO | Service Desk EN**.
3. Scroll down and select **Performance test**.

<Image align="center" alt="Performance test screenshot" border={true} width="600px" src="https://files.readme.io/bf8feb1d051ddb2d22edd1c72abab68b50a1222fa20787de2f5ba55c7cb3fb5a-image.png" className="border" />

4. On the request form, provide the details for your request using the table below.

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
        **Summary**
      </td>

      <td>
        A short description of the test you want.
      </td>
    </tr>

    <tr>
      <td>
        **Share with**
      </td>

      <td>
        Select which company you are opening the ticket for.
      </td>
    </tr>

    <tr>
      <td>
        **Test type**
      </td>

      <td>
        <ul>
          <li>**Migration:** Validates system capabilities for base migration to the Pismo platform.</li>
          <li>**Platform:**  Measures the performance of your integration after a migration is completed.</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>
        **Test Description**
      </td>

      <td>
        Details of what will be tested, such as:

        * Test Objective.
        * Volume to be tested.
        * List of endpoint/ APIs that will be consumed (for platform test only).
        * Name of the person responsible for the test.
      </td>
    </tr>

    <tr>
      <td>
        **Average TPS target to be achieved in the test**
      </td>

      <td>
        Average Transactions Per Second (TPS) target that you want to achieve in the test.
      </td>
    </tr>

    <tr>
      <td>
        **Instância a ser testada (Instance to be tested)**
      </td>

      <td>
        Select the check box for each entity type to be tested, such as Account.
      </td>
    </tr>

    <tr>
      <td>
        **Date and hour desired**
      </td>

      <td>
        When to run the test (you must specify a date no sooner than 15 calendar days in advance).
      </td>
    </tr>

    <tr>
      <td>
        **Need for test data?**
      </td>

      <td>
        Choose **Yes** if you need Pismo to generate a data set to use for the test. If you select **No**, you will need to upload your own data set tailored to your implementation.
      </td>
    </tr>

    <tr>
      <td>
        **Responsible for test data generation**
      </td>

      <td>
        Select one of the following options:

        <ul>
          <li>**Pismo**</li>
          <li>**Client** (you)</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>
        **Environment**
      </td>

      <td>
        The environment where the tests will be performed. Refer to [Environments](https://developers.pismo.io/pismo-docs/docs/environments) for more information.
      </td>
    </tr>
  </tbody>
</Table>

5. Select **Send** to submit your request.
<!-- source:end -->

## Lifecycle status

- `docs/resources/service-desk.md`: updatedAt 2026-06-30T14:11:30.000Z.
- `docs/resources/support.md`: updatedAt 2026-04-03T17:50:18.000Z.
- `docs/resources/opening-a-service-desk-ticket.md`: updatedAt 2026-06-16T14:49:13.000Z.
- `docs/resources/modify-a-service-request.md`: updatedAt 2026-04-03T17:50:18.000Z.
- `docs/resources/track-a-service-request.md`: updatedAt 2026-04-03T17:50:18.000Z.
- `docs/resources/request-types.md`: updatedAt 2026-06-16T14:49:13.000Z.
- `docs/resources/requests-for-access.md`: updatedAt 2026-06-16T14:49:13.000Z.
- `docs/resources/non-incident-lifecycle.md`: updatedAt 2026-06-16T14:49:13.000Z.
- `docs/resources/requesting-a-performance-test.md`: updatedAt 2026-07-27T19:41:13.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/resources/service-desk.md` | whole document | https://developers.pismo.io/pismo-docs/docs/service-desk | `5fd05a0e5f74608f…` | 2026-06-30T14:11:30.000Z |
| `docs/resources/support.md` | whole document | https://developers.pismo.io/pismo-docs/docs/support | `9d2eed33cb172f65…` | 2026-04-03T17:50:18.000Z |
| `docs/resources/opening-a-service-desk-ticket.md` | whole document | https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket | `bbec95cf21297458…` | 2026-06-16T14:49:13.000Z |
| `docs/resources/modify-a-service-request.md` | whole document | https://developers.pismo.io/pismo-docs/docs/modify-a-service-request | `a803c608ebddd447…` | 2026-04-03T17:50:18.000Z |
| `docs/resources/track-a-service-request.md` | whole document | https://developers.pismo.io/pismo-docs/docs/track-a-service-request | `88a4852249beeac6…` | 2026-04-03T17:50:18.000Z |
| `docs/resources/request-types.md` | whole document | https://developers.pismo.io/pismo-docs/docs/request-types | `98ca3ddc90dd481e…` | 2026-06-16T14:49:13.000Z |
| `docs/resources/requests-for-access.md` | whole document | https://developers.pismo.io/pismo-docs/docs/requests-for-access | `eda00d54cf5ed50e…` | 2026-06-16T14:49:13.000Z |
| `docs/resources/non-incident-lifecycle.md` | whole document | https://developers.pismo.io/pismo-docs/docs/non-incident-lifecycle | `0f62437bb06b5c33…` | 2026-06-16T14:49:13.000Z |
| `docs/resources/requesting-a-performance-test.md` | whole document | https://developers.pismo.io/pismo-docs/docs/requesting-a-performance-test | `6df67c4594f74f38…` | 2026-07-27T19:41:13.000Z |

## Related knowledge units

- `KU-AUTH-control-center-permissions-and-roles` — Control Center permissions, roles and API permission groups
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-GS-environments` — Environments
- `KU-SUP-incidents` — Incidents: describing an issue and the incident lifecycle
- `KU-SUP-operations-status-and-sub-processors` — Pismo operations status and platform sub-processors
