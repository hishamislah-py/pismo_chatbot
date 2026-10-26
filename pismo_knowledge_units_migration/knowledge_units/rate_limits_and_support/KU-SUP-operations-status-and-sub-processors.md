---
ku_id: KU-SUP-operations-status-and-sub-processors
title: Pismo operations status and platform sub-processors
category: rate_limits_and_support
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/resources/pismo-operations-status.md
  sha256: e9e7779279a1264b5d487a4a8c84331b01361fb5f14e9f8f53825a2c694dd968
  url: https://developers.pismo.io/pismo-docs/docs/pismo-operations-status
  role: primary_guide
  updated_at: '2026-06-16T14:49:13.000Z'
- path: docs/resources/pismo-platform-sub-processors.md
  sha256: 9a37fc61d4d81d1326f1486936a62a77fd433f21c08b44a59aba2271c1b2ea58
  url: https://developers.pismo.io/pismo-docs/docs/pismo-platform-sub-processors
  role: primary_guide
  updated_at: '2026-04-03T17:50:18.000Z'
operations: []
related_kus:
- KU-SUP-service-desk-requests
grouping_rationale: Operational transparency pages; the sub-processor page is a stub.
---

# Pismo operations status and platform sub-processors

**KU ID:** `KU-SUP-operations-status-and-sub-processors` · **Category:** Rate limits and support · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Operational transparency pages; the sub-processor page is a stub.

Scope as stated in `docs/resources/pismo-operations-status.md`:

> The operations status page helps keep you informed about systems availability, scheduled maintenance, and incident reports. You can also use this resource to subscribe to push notifications. Please note that for incident reports, each request type has an Operational Level Agreement (OLA) that defines the expected resolution time based on the issue's nature and urgency. Refer to [Request types and common fields](https://developers.pismo.io/pismo-docs/reference/request-types) for more information. For status messages, scheduled maintenance alerts are sent out to clients 7 days before the maintenance is scheduled to occur. For emergency maintenance, status messages are sent out 1-2 hours before the maintenance is scheduled to occur.

Scope as stated in `docs/resources/pismo-platform-sub-processors.md`:

> This page lists sub-processors that provide processing activities on customer data on behalf of Pismo clients.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/resources/pismo-operations-status.md`: Pismo operations status; Subscribe to notifications; View status messages; View uptime and historical data; View reported incidents
- `docs/resources/pismo-platform-sub-processors.md`: Pismo platform sub-processors

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/resources/pismo-operations-status.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pismo-operations-status · updatedAt: 2026-06-16T14:49:13.000Z

<!-- source:begin path=docs/resources/pismo-operations-status.md part=0-end -->

# Pismo operations status

The operations status page helps keep you informed about systems availability, scheduled maintenance, and incident reports. You can also use this resource to subscribe to push notifications. Please note that for incident reports, each request type has an Operational Level Agreement (OLA) that defines the expected resolution time based on the issue's nature and urgency. Refer to [Request types and common fields](https://developers.pismo.io/pismo-docs/reference/request-types) for more information. For status messages, scheduled maintenance alerts are sent out to clients 7 days before the maintenance is scheduled to occur. For emergency maintenance, status messages are sent out 1-2 hours before the maintenance is scheduled to occur.

> 📘 Access is limited
>
> To get access to the operations status page, contact your Pismo representative.

# Subscribe to notifications

To receive messages about status changes in the Production environment, maintenance activity, or incidents, click **Subscribe to updates**.

<Image align="center" alt="Screen capture of the Subscribe to updates button. " border={true} width="425px" src="https://files.readme.io/6830462-2024-01-31_14-52-33.png" className="border" />

Click **Manage My Subscription** to select which system components you want to receive updates about (the default is All). You can register to receive status update via:

* Email
* Text message
* Webhook

<Callout icon="📘" theme="info">
  You can also [Open a service request](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket) directly from this dialog.
</Callout>

# View status messages

At the top of the Pismo status page is a high-level status message. Typically, this message reads All systems operational), but you also may see a message about a current ongoing operation, similar to the following.

<Image align="center" alt="Screen capture of status page." border={true} src="https://files.readme.io/7971608-2024-01-31_14-57-38.png" className="border" />

> 📘 Scheduled maintenance activity
>
> Pismo posts notification messages in advance of all scheduled maintenance on the on the operations status page. In case of an incident related to a pre-communicated maintenance activity, Pismo reserves the right to decline the request but will provide an explanation for the decision.

Below the status messages are 90-day daily performance graphs for each system, such as Gateways, Account Management, and PCI Networks. To see details about a specific system, click the plus (**+**) sign next to its name. To see operational status for a specific day, hover over a bar.

<Image align="center" alt="Screen capture of the 90-day performance graph." border={true} src="https://files.readme.io/eee62dd-2024-01-31_14-59-04.png" className="border" />

Below the daily performance graphs, the status page has the following sections:

* **Scheduled Maintenance**: Logged scheduled maintenance. Click an entry's link for more information. May not appear if no maintenance is scheduled.
* **Past Incidents**: Past logged incidents. Click on an entry's link for more information.

# View uptime and historical data

Pismo also provides historical data about system operations. To see this information, click **View historical uptime**.

<Image align="center" alt="Screen capture of the View historical uptime link." border={true} src="https://files.readme.io/0c72ee9-2024-01-31_15-02-01.png" className="border" />

Current data, in calendar graph form, appears for the first system.

<Image align="center" alt="Screen capture of the calendar graph." border={true} src="https://files.readme.io/087956e-2024-01-31_15-03-19.png" className="border" />

On this screen, you can:

* Use the drop-down menu to switch between systems.
* Use the arrow buttons to switch among 90-day time spans.
* Hover over a green square for data about a specific day.

# View reported incidents

To see logged incident reports, click the **Incidents** tab.

<Image align="center" alt="Screen capture of Incidents report tab." border={true} src="https://files.readme.io/f336ab5-2024-01-31_15-05-17.png" className="border" />

On this screen you can:

* Click an incident link to access more information.
* Use the **Filter Components** menu for a list of logged incidents for a specific system component.
* Use the arrow buttons to switch among 90-day time spans.
<!-- source:end -->

### Source 2: `docs/resources/pismo-platform-sub-processors.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pismo-platform-sub-processors · updatedAt: 2026-04-03T17:50:18.000Z

<!-- source:begin path=docs/resources/pismo-platform-sub-processors.md part=0-end -->

# Pismo platform sub-processors

This page lists sub-processors that provide processing activities on customer data on behalf of Pismo clients.

* AWS Australia
* AWS Brazil
* AWS Europe
* AWS India
* AWS USA
* Cloudflare
* FutureX
* PingID

If you have further questions about the list of sub-processors, contact your Pismo representative.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.


### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `request-types` | Request types and common fields | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Lifecycle status

- `docs/resources/pismo-operations-status.md`: updatedAt 2026-06-16T14:49:13.000Z.
- `docs/resources/pismo-platform-sub-processors.md`: updatedAt 2026-04-03T17:50:18.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Operation link `request-types` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/resources/pismo-operations-status.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pismo-operations-status | `e9e7779279a1264b…` | 2026-06-16T14:49:13.000Z |
| `docs/resources/pismo-platform-sub-processors.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pismo-platform-sub-processors | `9a37fc61d4d81d13…` | 2026-04-03T17:50:18.000Z |

## Related knowledge units

- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
