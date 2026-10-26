---
ku_id: KU-SUP-incidents
title: 'Incidents: describing an issue and the incident lifecycle'
category: rate_limits_and_support
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/resources/describing-an-issue.md
  sha256: 1dc23f559bdb0c1e1d359e30d548201cce830a469831941223da25b2d951c6cb
  url: https://developers.pismo.io/pismo-docs/docs/describing-an-issue
  role: primary_guide
  updated_at: '2026-06-16T14:49:13.000Z'
- path: docs/resources/incident-lifecycle.md
  sha256: 0d0da98bf66db940a393b0ae1e8713bd3a8d0b1d28b4d236a50fbf98d1f5df33
  url: https://developers.pismo.io/pismo-docs/docs/incident-lifecycle
  role: primary_guide
  updated_at: '2026-04-03T17:50:18.000Z'
operations: []
related_kus:
- KU-SUP-operations-status-and-sub-processors
- KU-SUP-service-desk-requests
grouping_rationale: Incident reporting and handling.
---

# Incidents: describing an issue and the incident lifecycle

**KU ID:** `KU-SUP-incidents` · **Category:** Rate limits and support · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Incident reporting and handling.

Scope as stated in `docs/resources/describing-an-issue.md`:

> The description of an issue is the most important piece of information in a service request. In general, the more accurate, specific, and detailed the description is, the simpler it is to resolve. Explain as clearly as you can what is happening and what you expected to happen.

Scope as stated in `docs/resources/incident-lifecycle.md`:

> This page describes the incident lifecycle and Pismo's role in managing and resolving incidents. It also highlights the importance of providing a specific and detailed description of your issue so Pismo can understand and resolve your issue as soon as possible.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/resources/describing-an-issue.md`: Describe the issue; Request types; [Incident](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/171); [Occurence/Event](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/166); <Anchor label="Non-production environment" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/165">Non-production environment</Anchor>; [Question](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/167); [Projects](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/168); [Performance Test](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/454); [Settings](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/1733); Date/Time; Recommended examples; Examples to Avoid; Product; Recommended example; Not recommended example; Correlation identifier (x-cid); Other helpful information
- `docs/resources/incident-lifecycle.md`: Incident lifecycle; Incident resolution process; Incident request status; Incidents identified internally

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/resources/describing-an-issue.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/describing-an-issue · updatedAt: 2026-06-16T14:49:13.000Z

<!-- source:begin path=docs/resources/describing-an-issue.md part=0-end -->

# Describe the issue

The description of an issue is the most important piece of information in a service request. In general, the more accurate, specific, and detailed the description is, the simpler it is to resolve. Explain as clearly as you can what is happening and what you expected to happen.

# Request types

First, choose the appropriate request type. For more information, refer to [Request types](https://developers.pismo.io/pismo-docs/docs/request-types). Request types include the following:

## [Incident](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/171)

Use this form to report an incident. An incident includes any and all failure events or abnormal behavior of the service or system (application) in a production environment.

Provide the following details for your request:

| Field            | Description                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Summary**      | A short description of the incident you are reporting.                                                                                                                                                                                                                                                                                                                                                                          |
| **Share With**   | Select which company you are opening the ticket for.                                                                                                                                                                                                                                                                                                                                                                            |
| **Category**     | Select a category.                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Sub-category** | Select a sub-category.                                                                                                                                                                                                                                                                                                                                                                                                          |
| **API**          | Select a related API.                                                                                                                                                                                                                                                                                                                                                                                                           |
| **x-CID**        | Enter the x-CID. The x-CID field is a correlation ID used to link a series of related API requests and events. For example, if a user makes an authorization request with 10 installments, the Pismo platform generates an authorization event and 10 transaction events, all with the same x-cid. This can help the support team track everything related to an API call. You can find the x-cid field in the response header. |
| **Impacted**     | Enter the amount of impacted clients.                                                                                                                                                                                                                                                                                                                                                                                           |
| **Description**  | Enter a detailed description of the issue. The more accurate, specific, and detailed the description is, the simpler it is to resolve. Explain as clearly as you can what is happening and what you expected to happen.                                                                                                                                                                                                         |
| **Impact**       | Select an impact option.                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Severity**     | Select a Severity option.                                                                                                                                                                                                                                                                                                                                                                                                       |

## [Occurence/Event](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/166)

Use this form whenever a request presents problems without causing broad or general failure of a service.

| Field            | Description                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Summary**      | A short description of the incident you are reporting.                                                                                                                                                                                                                                                                                                                                                                          |
| **Share With**   | Select which company you are opening the ticket for.                                                                                                                                                                                                                                                                                                                                                                            |
| **Category**     | Select a category.                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Sub-category** | Select a sub-category.                                                                                                                                                                                                                                                                                                                                                                                                          |
| **x-CID**        | Enter the x-CID. The x-CID field is a correlation ID used to link a series of related API requests and events. For example, if a user makes an authorization request with 10 installments, the Pismo platform generates an authorization event and 10 transaction events, all with the same x-cid. This can help the support team track everything related to an API call. You can find the x-cid field in the response header. |
| **APIs**         | Select any related APIs.                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Description**  | Enter a detailed description of the issue. The more accurate, specific, and detailed the description is, the simpler it is to resolve. Explain as clearly as you can what is happening and what you expected to happen.                                                                                                                                                                                                         |

## <Anchor label="Non-production environment" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/165">Non-production environment</Anchor>

Use this form when you need help with error results that you encounter outside of the production environment.

| Field            | Description                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Summary**      | A short description of the incident you are reporting.                                                                                                                                                                                                                                                                                                                                                                          |
| **Category**     | Select a category.                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Sub-category** | Select a sub-category.                                                                                                                                                                                                                                                                                                                                                                                                          |
| **API**          | Select any related APIs.                                                                                                                                                                                                                                                                                                                                                                                                        |
| **x-CID**        | Enter the x-CID. The x-CID field is a correlation ID used to link a series of related API requests and events. For example, if a user makes an authorization request with 10 installments, the Pismo platform generates an authorization event and 10 transaction events, all with the same x-cid. This can help the support team track everything related to an API call. You can find the x-cid field in the response header. |
| **Description**  | Enter a detailed description of the issue. The more accurate, specific, and detailed the description is, the simpler it is to resolve. Explain as clearly as you can what is happening and what you expected to happen.                                                                                                                                                                                                         |

## [Question](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/167)

Use this form whenever you are unclear about a particular result you're experiencing, when information is unclear, or when you are experiencing errors or problems.

| Field            | Description                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Summary**      | A short description of the incident you are reporting.                                                                                                                                                                                                                                                                                                                                                                          |
| **Share With**   | Select which company you are opening the ticket for.                                                                                                                                                                                                                                                                                                                                                                            |
| **Category**     | Select a category.                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Sub-category** | Select a sub-category.                                                                                                                                                                                                                                                                                                                                                                                                          |
| **APIs**         | Select any related APIs.                                                                                                                                                                                                                                                                                                                                                                                                        |
| **X-CID**        | Enter the x-CID. The x-CID field is a correlation ID used to link a series of related API requests and events. For example, if a user makes an authorization request with 10 installments, the Pismo platform generates an authorization event and 10 transaction events, all with the same x-cid. This can help the support team track everything related to an API call. You can find the x-cid field in the response header. |
| **Description**  | Enter a detailed description of the issue. The more accurate, specific, and detailed the description is, the simpler it is to resolve. Explain as clearly as you can what is happening and what you expected to happen.                                                                                                                                                                                                         |

## [Projects](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/168)

Use this form to request an improvement, a new service, or new features.

| Field                            | Description                                                                                                                                                         |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Summary**                      | A short description of the incident you are reporting.                                                                                                              |
| **Description**                  | Enter a detailed description of the request. The more accurate, specific, and detailed the request is, the simpler it is to resolve.                                |
| **Share With**                   | Select which company you are opening the ticket for.                                                                                                                |
| **Scope**                        | Describe the details of what should this new development is capable of doing.                                                                                       |
| **Use Case**                     | Describe the use case(s) of this new development.                                                                                                                   |
| **Goal**                         | Describe the main reason for this new development to be executed.                                                                                                   |
| **Business Benefits**            | Describe the goals of your company that this new development would impact. Would this project impact your growth? How? How much?                                    |
| **Business Impact**              | Describe the business impact. Would this development mitigate any risks of your business?                                                                           |
| **Type**                         | Select a request type.                                                                                                                                              |
| **Business Rules**               | Describe mapped business rules and requirements of this development.                                                                                                |
| **Countries Impacted**           | Select the countries that will be impacted by this development.                                                                                                     |
| **Priority**                     | Select a priority for this development.                                                                                                                             |
| **Regulatory / Mandate / Audit** | Select Yes or No to indicate whether a regulatory/mandate/audit is needed for this development. If Yes, attach the related documentation at the bottom of the page. |
| **Other Relevant Information**   | Enter any other relevant information for this request.                                                                                                              |

## [Performance Test](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/454)

Use this form when you want to test the platform's performance capacity or migration.

| Field                                             | Description                                                                                           |
| :------------------------------------------------ | :---------------------------------------------------------------------------------------------------- |
| **Summary**                                       | A short description of the incident you are reporting.                                                |
| **Share With**                                    | Select which company you are opening the ticket for.                                                  |
| **Test Type**                                     | Select a test type.                                                                                   |
| **Test Description**                              | Enter a detailed description of the test.                                                             |
| **Average TPS target to be achieved in the test** | Enter the average TPS target to be achieved in the test.                                              |
| **Instância a ser testada**                       | Select an instance to be tested.                                                                      |
| **Date and Hour Desired**                         | Select a date and hour for the performance test. Tests must be scheduled 15 calendar days in advance. |
| **Need for Test Data**                            | Select Yes if you need Pismo to generate a data set to use for the test.                              |
| **Responsible for test data generation**          | Select the entity that is responsible for the test data generation.                                   |
| **Environment**                                   | Select the environment where the tests will be performed.                                             |

## [Settings](https://pismolabs.atlassian.net/servicedesk/customer/portal/10/group/45/create/1733)

Use this form for requests pertaining to existing production programs, such as those affecting business rules, changing rates, spending controls, accounting, ICA, embossing, and so on.

| Field            | Description                                                                                                                 |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| **Summary**      | A short description of the incident you are reporting.                                                                      |
| **Share With**   | Select which company you are opening the ticket for.                                                                        |
| **Category**     | Select a category.                                                                                                          |
| **Sub-category** | Select a sub-category.                                                                                                      |
| **Description**  | Describe the desired configuration in detail. If necessary, provide the Program ID, Org ID, and Environment.                |
| **Report Log**   | When a Control Center request fails, the application automatically displays a popup message. You can add this message here. |
| **Priority**     | Select a priority level.                                                                                                    |
| **Environment**  | Select an environment.                                                                                                      |

# Date/Time

Provide the date and time the issue began, along with the duration of the problem, if it eventually resolved. Use [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date/time format if possible.

## Recommended examples

* Started at 2017-09-08T15:13:06+00:00 and it lasted 5 minutes, causing …

* The issue was noticed intermittently 2 to 5 times, starting at 2017-09-10 and …

* The problem has been going on since 2017-09-08T15:13:06+00:00 …

* Between 2017-09-08T15:13:06+00:00 and 2017-09-08T15:18:16+00:00 it was noticed …

## Examples to Avoid

* It happened yesterday at some point…

* We noticed an abnormal behavior back on 9/8 …

# Product

When you create a new ticket, you must provide the product name. It is also recommended you include all other products or services with problems, the APIs or URLs involved, and the request method – API REST or CRM.

## Recommended example

The API-auth API REST has returned the following errors…

## Not recommended example

Users cannot access the APIs.

# Correlation identifier (x-cid)

The **x-cid** field is a correlation ID used to link a series of related API requests and events. For example, if a user makes an authorization request with 10 installments, the Pismo platform generates an authorization event and 10 transaction events, all with the same x-cid. This can help the support team track everything related to an API call. You can find the x-cid field in the response header.

> 📘 Third-party IDs
>
> If you use a third-party tool that has generated an ID that could be helpful to the support team, consider adding it to the description as well. For example, if something is reported from [Cloudflare](https://www.cloudflare.com/), you may provide the **CF-Ray**. (CF-Ray is a unique ID that Cloudflare assigns to every request that passes through its network. It is typically used to debug and troubleshoot individual requests.)

# Other helpful information

The following can also be useful in resolving your issue:

* Screenshots

* [HTTP Archive](https://support.laserfiche.com/kb/1014120/generating-an-http-archive-har-format-file) (HAR) files for web-based interfaces. [HAR Analyzer](https://toolbox.googleapps.com/apps/har_analyzer/) contains instructions for the most used browsers.

* `tcpdump` outputs

* Code snippets and stack traces
<!-- source:end -->

### Source 2: `docs/resources/incident-lifecycle.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/incident-lifecycle · updatedAt: 2026-04-03T17:50:18.000Z

<!-- source:begin path=docs/resources/incident-lifecycle.md part=0-end -->

# Incident lifecycle

This page describes the incident lifecycle and Pismo's role in managing and resolving incidents. It also highlights the importance of providing a specific and detailed description of your issue so Pismo can understand and resolve your issue as soon as possible.

When resolving an incident, Pismo will focus on two key tasks:

* Mitigation: Take immediate steps to restore normal platform operations.
* Resolution: Address any negative effects caused by the incident—such as correcting inaccurate balances or data—and implement changes to prevent the issue from happening again.

Pismo automatically escalates every incident request, no matter what the severity is. It is Pismo's responsibility to evaluate the incident and determine its priority based on the impact that it has. To help ensure that your issue is evaluated properly, it is important to provide a specific and detailed description of your issue (for more information, refer to [Describing an issue](https://developers.pismo.io/pismo-docs/docs/describing-an-issue)). To report an incident, refer to [Open a service request](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket).

The following image provides an overview of the incident lifecycle workflow.

<Image align="center" alt="Image showing the incident lifecycle workflow." border={true} src="https://files.readme.io/df63eaa32f1633b8175f10056079d36442b99a02f40549b2e88785237c698572-image.png" className="border" />

# Incident resolution process

After your request is submitted and acknowledged, the resolution process proceeds as follows:

* A new service request receives the status **In Progress**. You can add comments during this stage, to provide evidence or additional information.
* When the support team has mitigated the issue, they update the status of the request to **Restored**.
* The support team may decline an incident request if:
  * They are unable to reproduce the reported issue.
  * The issue is outside the agreed-upon parameters.
  * The issue is caused by a third party or is otherwise beyond Pismo's control.  (However, the support team will clearly communicate the reason for declining an incident request.)
  * The status of a declined incident is **Resolved** with the resolution **Won’t Do**.
* When the support team has resolved the issue and corrected any negative effects, they update the status of the request to **Resolved**.
* If you are not satisfied with a resolution, be sure to reopen your request instead of submitting a new one.
* For resolved P1 and P2 incidents, **Post Mortem** status indicates that Pismo is investigating how and why it occurred.
* Root Cause Analysis (RCA) refers to the process that the Pismo engineering team follows after an incident is resolved. This process determines why the incident occurred and develops the necessary steps to ensure that it doesn't happen again. Details about the root cause that contain sensitive or internal information may be omitted.
* Incidents with **Pending** status indicate that the support team needs more information or approval to proceed with the planned actions. Pending requests move automatically to Resolved status after 5 days without activity.
* **Closed** status represents that the incident is fully concluded and cannot be reopened.

The following table describes the available priority levels for an incident.

| Incident priority | Description                                                                                                                                |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| P1 - Critical     | Severe impact:<ul><li>Affects many services or critical processes.</li><li>Prevents normal operations or causes critical damage.</li></ul> |
| P2 - High         | Significant impact:<ul><li>Affects some services or processes.</li><li>Interferes with normal operations.</li></ul>                        |
| P3 - Medium       | Partial degradation of services or financial processes.                                                                                    |
| P4 - Low          | Minor impacts to platform performance.                                                                                                     |

Pismo aims to restore normal service operation as quickly as possible. In general, the on-call support team acknowledges all incident requests within 15 minutes. Mitigation can take up to four hours for critical incidents, and up to three days for lower-priority incidents.

# Incident request status

The following table describes the request status values.

| Status      | Description                                                                                                                                                                                                                           |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| New         | Request is awaiting service.  This is the status when a request is first created.                                                                                                                                                     |
| In progress | Resolution is in progress.                                                                                                                                                                                                            |
| Pending     | Waiting for more information from you. After answering the questions,  you must click **To Do** to submit your answers. If no action is taken within 240 hours, the request moves automatically to Resolved status.                   |
| Reopened    | Proposed resolution to a request (in status **Restored**, **Validating**, or **Resolved**) was not satisfactory, and the issue is reopened.                                                                                           |
| Restored    | An incident has been addressed, restoring normal operation.                                                                                                                                                                           |
| Resolved    | Incident has been resolved. At this point, you can either close the request or select **Reopened**, to reopen it if you are not satisfied. If no action is taken within 120 hours,  the request moves automatically to Closed status. |
| Post Mortem | A workaround has resolved an incident and Pismo is developing a more permanent solution.                                                                                                                                              |
| Closed      | Issue has been resolved to your satisfaction.                                                                                                                                                                                         |

# Incidents identified internally

Incidents that are discovered internally are reported on the [Pismo operations status](https://developers.pismo.io/pismo-docs/docs/pismo-operations-status) page, along with updates about its resolution. You are welcome to open an incident even if there's already an incident posted on the status page, in case you encounter any other impacts.

> 📘 Scheduled maintenance activity
>
> Pismo posts notification messages in advance of all scheduled maintenance on the on the [operations status](https://developers.pismo.io/pismo-docs/docs/pismo-operations-status) page. In case of an incident related to a pre-communicated maintenance activity, Pismo reserves the right to decline the request but will provide an explanation for the decision.
<!-- source:end -->

## Lifecycle status

- `docs/resources/describing-an-issue.md`: updatedAt 2026-06-16T14:49:13.000Z.
- `docs/resources/incident-lifecycle.md`: updatedAt 2026-04-03T17:50:18.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/resources/describing-an-issue.md` | whole document | https://developers.pismo.io/pismo-docs/docs/describing-an-issue | `1dc23f559bdb0c1e…` | 2026-06-16T14:49:13.000Z |
| `docs/resources/incident-lifecycle.md` | whole document | https://developers.pismo.io/pismo-docs/docs/incident-lifecycle | `0d0da98bf66db940…` | 2026-04-03T17:50:18.000Z |

## Related knowledge units

- `KU-SUP-operations-status-and-sub-processors` — Pismo operations status and platform sub-processors
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
