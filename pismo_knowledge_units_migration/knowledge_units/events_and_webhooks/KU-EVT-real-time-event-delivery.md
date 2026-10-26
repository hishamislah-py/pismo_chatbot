---
ku_id: KU-EVT-real-time-event-delivery
title: 'Real-time event delivery: setup, additional subscribers and event filtering'
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/setting-up-real-time-event-delivery.md
  sha256: f8ce1cee0eba5094f57bb1eb3ad8bffcb649f64295bf3caff2bba045c1bb378d
  url: https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery
  role: primary_guide
  updated_at: '2026-07-29T21:06:24.000Z'
- path: docs/data-and-reporting/setting-up-an-additional-subscriber.md
  sha256: 8565fb28a94b5facdc24a5825f94b43a1f36851ed05ad7fd6718d2f4afab00d5
  url: https://developers.pismo.io/pismo-docs/docs/setting-up-an-additional-subscriber
  role: primary_guide
  updated_at: '2026-07-29T20:26:07.000Z'
- path: docs/data-and-reporting/event-filtering.md
  sha256: cbdc5a2986cc59f08fe704f91dcc7ca705be8645ece03c6cce98c60660cfffb7
  url: https://developers.pismo.io/pismo-docs/docs/event-filtering
  role: primary_guide
  updated_at: '2026-07-28T21:12:36.000Z'
operations: []
related_kus:
- KU-EVT-aws-event-tutorial
- KU-EVT-aws-eventbridge-event-configuration-tutorial
- KU-EVT-azure-event-configuration-tutorial
- KU-EVT-confluent-event-config-tutorial
- KU-EVT-gcp-event-configuration-tutorial
- KU-EVT-pismo-data-platform-http-integration-guide-beta
- KU-EVT-setting-up-event-file-delivery
grouping_rationale: Sequential setup tasks for real-time delivery.
---

# Real-time event delivery: setup, additional subscribers and event filtering

**KU ID:** `KU-EVT-real-time-event-delivery` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Sequential setup tasks for real-time delivery.

Scope as stated in `docs/data-and-reporting/setting-up-real-time-event-delivery.md`:

> In addition to [event file notifications](https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery), you can stream event notifications and data in real time through an integration channel. This guide explains what Pismo configures and what you need to configure for each delivery method.

Scope as stated in `docs/data-and-reporting/setting-up-an-additional-subscriber.md`:

> An additional subscriber lets one organization (the direct subscriber) share event data with another organization (the additional subscriber). Both organizations must be tenants of the same Pismo client.

Scope as stated in `docs/data-and-reporting/event-filtering.md`:

> Event filtering lets you control which events a subscribed event source receives. By default, subscribers receive all generated events. Use event filtering to enable or disable specific event types using pattern-based rules.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/setting-up-real-time-event-delivery.md`: Setting up real-time event delivery; AWS: Real-time with Amazon Simple Notification Service (SNS); AWS: Real-time delivery with Amazon EventBridge; Google Cloud: Real-time delivery with Pub/Sub; Azure: Real-time delivery with Service Bus; Confluent cloud: Real-time delivery with Kafka; HTTP webhook (beta): Real-time delivery with HTTPS POST; Validate the integration
- `docs/data-and-reporting/setting-up-an-additional-subscriber.md`: Setting up an additional event subscriber; How it works; Prerequisites; Open a service desk ticket; Review example event data; Validate the configuration; Troubleshooting table
- `docs/data-and-reporting/event-filtering.md`: Setting up event filtering; Why use event filtering; Supported filtering patterns; Open a service desk ticket; Troubleshoot event filtering

## Prerequisites and dependencies

- Prerequisites are described in `docs/data-and-reporting/setting-up-an-additional-subscriber.md` section "Prerequisites".

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/setting-up-real-time-event-delivery.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery · updatedAt: 2026-07-29T21:06:24.000Z

<!-- source:begin path=docs/data-and-reporting/setting-up-real-time-event-delivery.md part=0-end -->

# Setting up real-time event delivery

In addition to [event file notifications](https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery), you can stream event notifications and data in real time through an integration channel. This guide explains what Pismo configures and what you need to configure for each delivery method.

Choose your cloud provider below and follow the corresponding tutorial.

## AWS: Real-time with Amazon Simple Notification Service (SNS)

The following architecture delivers event notifications to your AWS account.

![Image shows the data flow for real-time event notification to an AWS account.](https://files.readme.io/1eb3727-AWSrtFlow.JPG "AWSrtFlow.JPG")

**Pismo configuration:** Pismo creates an [Identity Access Management Role (IAM) Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that publishes events to your Amazon SNS topic.

**What you need to do:** Follow the [AWS SNS event configuration tutorial](https://developers.pismo.io/pismo-docs/docs/aws-event-tutorial) to set up Amazon SNS for real-time event delivery.

<Callout icon="📘" theme="info">
  All primary event fields except the data field are sent as SNS message attributes. This allows you to create filtered subscriptions based on event domains and event types.
</Callout>

## AWS: Real-time delivery with Amazon EventBridge

**Pismo configuration:** Pismo creates an AWS IAM role that publishes events to your Amazon EventBridge event bus.

**What you need to do:** Follow the <Anchor label="AWS EventBridge Event Configuration Tutorial" target="_blank" href="https://developers.pismo.io/pismo-docs/docs/aws-eventbridge-event-configuration-tutorial">AWS EventBridge Event Configuration Tutorial</Anchor> to set up EventBridge for real-time event delivery..

## Google Cloud: Real-time delivery with Pub/Sub

The following architecture delivers event notifications to your Google Cloud account.

![Image shows the data flow for real-time event notification to a GCP account.](https://files.readme.io/5ee0048-GCPrtFlow.JPG "GCPrtFlow.JPG")

**Pismo configuration:** Pismo creates an IAM [service account](https://cloud.google.com/iam/docs/service-accounts) that publishes events to your Pub/Sub topic.

**What you need to do:** Follow the [GCP event configuration tutorial](https://developers.pismo.io/pismo-docs/docs/gcp-event-configuration-tutorial) to set up Pub/Sub for real-time event delivery..

## Azure: Real-time delivery with Service Bus

The following architecture delivers event notifications to your Microsoft Azure account.

![Image shows the data flow for real-time event notification to a Microsoft Azure account.](https://files.readme.io/c1b1dbd-AzureRTflow.JPG "AzureRTflow.JPG")

**Pismo configuration:** Pismo creates a [service principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals) accesses your Azure Service Bus namespace and publishes events.

**What you need to do:** Follow the [Azure event configuration tutorial](https://developers.pismo.io/pismo-docs/docs/azure-event-configuration-tutorial) to set up Azure Service Bus for real-time event delivery..

## Confluent cloud: Real-time delivery with Kafka

**Pismo configuration:** Pismo produces events directly to your Confluent Cloud Kafka topic.

**What you need to do:** Follow the <Anchor label="Confluent event configuration tutorial" target="_blank" href="https://developers.pismo.io/pismo-docs/docs/confluent-event-config-tutorial">Confluent event configuration tutorial</Anchor> to set up real-time event delivery..

## HTTP webhook (beta): Real-time delivery with HTTPS POST

**Pismo configuration:** Pismo sends encrypted events via HTTPS POST to your endpoint using Visa-compliant JWE/JWS standards.

**Your configuration:** Follow the <Anchor label="Pismo data platform – HTTP integration guide (beta)" target="_blank" href="https://developers.pismo.io/pismo-docs/docs/pismo-data-platform-http-integration-guide-beta">Pismo data platform – HTTP integration guide (beta)</Anchor> to configure your endpoint for real-time event delivery.

## Validate the integration

Each provider-specific tutorial includes tools and procedures to help you verify your integration, including:

* Manual validation commands
* Diagnostic scripts that check authentication, permissions, resources, and connectivity

For validation instructions, see the guide for your selected provider.

<Callout icon="⚠️" theme="warn">
  **Retry and retention policy:** To ensure ecosystem stability, the Pismo platform applies retry limits. Events that exceed the retry threshold are moved to controlled retention and can be redelivered upon request, as long as they are within the **24-hour retention window**.
</Callout>

<Callout icon="📘" theme="info">
  **Need Pismo-specific details?** Information such as Pismo's AWS Account ID, single-tenant SFTP endpoints, consumer role ARNs, or external IDs can be obtained from your **Technical Account Manager (TAM)** or the **Implementation Engineer** assigned to your project.
</Callout>
<!-- source:end -->

### Source 2: `docs/data-and-reporting/setting-up-an-additional-subscriber.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/setting-up-an-additional-subscriber · updatedAt: 2026-07-29T20:26:07.000Z

<!-- source:begin path=docs/data-and-reporting/setting-up-an-additional-subscriber.md part=0-end -->

# Setting up an additional event subscriber

An additional subscriber lets one organization (the direct subscriber) share event data with another organization (the additional subscriber). Both organizations must be tenants of the same Pismo client.

Use an additional subscriber when multiple organizations need access to the same event stream for reporting, analytics, integrations, or operational workflows. Events can be delivered through real-time streaming, batch file delivery, or both.

The following event delivery architecture image shows how a direct subscriber shares events with an additional subscriber through real-time streams and batch files.

<Image align="center" alt="Image illustrating how event filtering works. " border={true} src="https://files.readme.io/d281159-DATA__Diagram_for_Additional_subscriber_V4.png" className="border" />

## How it works

* The direct subscriber forwards events to the additional subscriber.

* Delivery can be via real-time streaming, batch file, or both.

* The additional subscriber can receive events from multiple organizations and distinguish them by using `org_id`.

* Event delivery supports AWS, GCP, and Azure environments.

* You can use event filtering to control which events are shared.

<Callout icon="📘" theme="info">
  Organizations can use different cloud providers as long as both organizations are tenants of the same Pismo client.
</Callout>

## Prerequisites

Before you submit a request, confirm the following:

* [ ] The direct subscriber (source org) is configured on the Pismo data platform
* [ ] The additional subscriber (destination org) is a tenant of the same client
* [ ] The additional subscriber has data integration configured (can receive events)

## Open a service desk ticket

1. Go to: [https://pismolabs.atlassian.net/servicedesk/customer/portal/10](https://pismolabs.atlassian.net/servicedesk/customer/portal/10)
2. Select **Settings**.
3. Enter a short description of the request in the **Summary** field.
4. For **Category**, select **Data**.
5. For **Sub-Category**, select **Additional Subscriber**.
6. Copy the request template into the **Description** field and enter your values:

```
CONFIGURATION REQUEST — Additional Event Subscriber
====================================================

Requester Name:        Your Name
Contact Email:         you@company.com
Environment:           Production / Sandbox

Source Org ID:         TN-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  (the organization that generates the events)

Destination Org ID:    TN-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  (the organization that will receive the shared events)

Delivery Type:         Real-Time Streaming / Batch File Delivery / Both
Cloud Provider (Dest): AWS / GCP / Azure

Event Filtering:       Yes / No
  (If Yes, please also open an Event Filtering request
   or list the filtering patterns below)
Filtering Patterns:    domain.* / *.event_type / domain.event_type
```

7. When a Control Center request fails, the application automatically displays a popup message. You can add this message in the **Report Log** field.
8. Select a value for **Priority**.
9. Select the appropriate **Environment**.
10. Select **Send** to submit the request.

<Callout icon="📘" theme="info">
  Use lowercase values for all Org IDs.
</Callout>

<Callout icon="⏱️" theme="default">
  **Important**: After Pismo completes the initial configuration, you have **24 hours** to adjust permissions/access on your side. If Pismo cannot deliver events within this window, the integration is paused and you will need to open a new ticket to resume.
</Callout>

<Callout icon="📘" theme="info">
  **Need Pismo-specific details?** Information such as Pismo's AWS Account ID, single-tenant SFTP endpoints, consumer role ARNs, or external IDs can be obtained from your **Technical Account Manager (TAM)** or the **implementation engineer** assigned to your project.
</Callout>

## Review example event data

Events from a direct subscriber include the `org_id` field, allowing the additional subscriber to identify the source:

```
{
    "event_id": "252212bf-cde2-43f9-b28f-33ea2b452b32",
    "domain": "onboarding",
    "event_type": "succeeded",
    "schema_version": 1,
    "org_id": "TN-a1db4e4e-315f-4a67-9036-ecacd370b561",
    "cid": "8a3f650b-c80c-451f-993d-7368dba4c715",
    "timestamp": "2019-07-20T19:03:00.000Z",
    "data": {}
}
```

If the additional subscriber receives events from multiple organizations, use `org_id` to identify and filter the source organization.

## Validate the configuration

After Pismo confirms the configuration, use the [Prerequisites](#prerequisites) checklist and the troubleshooting table to verify that event delivery works as expected.

### Troubleshooting table

| Symptom                   | Likely Cause                             | Fix                                        |
| ------------------------- | ---------------------------------------- | ------------------------------------------ |
| No events at destination  | Source org not delivering                | Verify source org's integration is active  |
| No events at destination  | Additional subscriber not configured yet | Wait for Pismo confirmation                |
| Wrong events arriving     | No filtering applied                     | Open an Event Filtering ticket             |
| Duplicate events in files | Multiple source orgs                     | Filter by `org_id` in your processing code |
| Missing org\_id in events | Legacy event format                      | Contact Pismo support                      |
| Events delayed            | Batch window not elapsed                 | Wait up to 5 minutes for file batching     |
<!-- source:end -->

### Source 3: `docs/data-and-reporting/event-filtering.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/event-filtering · updatedAt: 2026-07-28T21:12:36.000Z

<!-- source:begin path=docs/data-and-reporting/event-filtering.md part=0-end -->

# Setting up event filtering

Event filtering lets you control which events a subscribed event source receives. By default, subscribers receive all generated events. Use event filtering to enable or disable specific event types using pattern-based rules.

Event filtering can help you:

* Reduce unnecessary event traffic.
* Simplify downstream processing.
* Limit exposure of sensitive information when sharing events with partner organizations.

This guide explains supported filtering patterns, how to request a configuration change, and how to verify the implementation.

<Image align="center" alt="Image illustrating event filtering." border={true} width="900px" src="https://files.readme.io/633499a-Events_filtering_and_Additional_subscriber_New_V4.png" className="border" />

## Why use event filtering

* **Reduce noise** — Receive only the events relevant to your business.
* **Protect sensitive data** — Prevent sensitive event data from being shared with partner organizations.

## Supported filtering patterns

Use the following patterns to specify which events to enable or disable:

| Pattern                 | Meaning                                      | Example                |
| ----------------------- | -------------------------------------------- | ---------------------- |
| `*.<event_type>`        | A specific event type from any domain        | `*.succeeded`          |
| `<domain>.*`            | All event types from a specific domain       | `onboarding.*`         |
| `<domain>.<event_type>` | A specific event type from a specific domain | `transactions.created` |

## Open a service desk ticket

1. Go to: [https://pismolabs.atlassian.net/servicedesk/customer/portal/10](https://pismolabs.atlassian.net/servicedesk/customer/portal/10)
2. Select **Settings**.
3. Enter a short description of the request in the **Summary** field.
4. In **Category**, select **Data**.
5. In **Sub-Category**, select **Event Filtering**.
6. Copy the template below into the **Description** field and replace the sample values with your information.:

```
CONFIGURATION REQUEST — Event Filtering
========================================

Org ID:            TN-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Environment:       Production / Sandbox
Requester Name:    Your Name
Contact Email:     you@company.com

Action:            Disable / Enable
  Disable = STOP sending these events
  Enable  = START sending these events (that were previously blocked)

Filtering Patterns (one per line):
  onboarding.*
  *.failed
  transactions.created

Apply to Partner Org?  No / Yes
Partner Org ID:        TN-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  (only if applying filter to a partner/additional subscriber org)

```

7. When a Control Center request fails, the application automatically displays a popup message. You can add this message in the **Report Log** field.
8. In **Priority**, select the appropriate priority level.
9. In **Environment**, select the environment for the configuration.
10. Select **Send** to submit the request.

<Callout icon="📘" theme="info">
  Event filtering takes effect immediately after Pismo implements the request.
</Callout>

<Callout icon="📘" theme="info">
  **Need Pismo-specific details?** Information such as Pismo's AWS Account ID, single-tenant SFTP endpoints, consumer role ARNs, or external IDs can be obtained from your **Technical Account Manager (TAM)** or the **Implementation Engineer** assigned to your project.
</Callout>

## Troubleshoot event filtering

After Pismo confirms filters are applied, use the troubleshooting table below to identify and resolve common issues.

| Symptom                                    | Likely cause                                     | Fix                                                            |
| ------------------------------------------ | ------------------------------------------------ | -------------------------------------------------------------- |
| Still receiving disabled events            | The filter has not  been applied yet             | Confirm with Pismo that the ticket is resolved                 |
| No events received                         | The filter is too broad                          | Check if `*.*` was used — this disables everything             |
| Unexpected events are filtered             | The filtering pattern contains an error          | Verify `domain`/`event_type` names in Pismo documentation      |
| Partner organization still receives events | The filter was applied to the wrong organization | Update the request with the correct organization ID            |
| Events are intermittent                    | An unrelated infrastructure issue exists         | Run the appropriate troubleshooting script for the integration |
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/setting-up-real-time-event-delivery.md`: updatedAt 2026-07-29T21:06:24.000Z.
- `docs/data-and-reporting/setting-up-an-additional-subscriber.md`: updatedAt 2026-07-29T20:26:07.000Z.
- `docs/data-and-reporting/event-filtering.md`: updatedAt 2026-07-28T21:12:36.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/setting-up-real-time-event-delivery.md` | whole document | https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery | `f8ce1cee0eba5094…` | 2026-07-29T21:06:24.000Z |
| `docs/data-and-reporting/setting-up-an-additional-subscriber.md` | whole document | https://developers.pismo.io/pismo-docs/docs/setting-up-an-additional-subscriber | `8565fb28a94b5fac…` | 2026-07-29T20:26:07.000Z |
| `docs/data-and-reporting/event-filtering.md` | whole document | https://developers.pismo.io/pismo-docs/docs/event-filtering | `cbdc5a2986cc59f0…` | 2026-07-28T21:12:36.000Z |

## Related knowledge units

- `KU-EVT-aws-event-tutorial` — AWS SNS event configuration tutorial
- `KU-EVT-aws-eventbridge-event-configuration-tutorial` — AWS EventBridge event configuration tutorial
- `KU-EVT-azure-event-configuration-tutorial` — Azure event configuration tutorial
- `KU-EVT-confluent-event-config-tutorial` — Confluent event configuration tutorial
- `KU-EVT-gcp-event-configuration-tutorial` — GCP event configuration tutorial
- `KU-EVT-pismo-data-platform-http-integration-guide-beta` — Pismo data platform – HTTP integration guide (beta)
- `KU-EVT-setting-up-event-file-delivery` — Setting up event batch file delivery
