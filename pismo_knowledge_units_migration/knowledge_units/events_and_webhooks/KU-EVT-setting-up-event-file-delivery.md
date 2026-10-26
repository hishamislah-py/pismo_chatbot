---
ku_id: KU-EVT-setting-up-event-file-delivery
title: Setting up event batch file delivery
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/setting-up-event-file-delivery.md
  sha256: aac65a5595c499cbb43b34fc142c54c2062b7c2b6f9c529bd27f049f5c15ea7a
  url: https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery
  role: primary_guide
  updated_at: '2026-07-13T14:00:14.000Z'
operations: []
related_kus:
- KU-EVT-gcp-event-file-configuration-tutorial
- KU-EVT-real-time-event-delivery
- KU-EVT-sftp-event-file-configuration-tutorial
grouping_rationale: single source page
---

# Setting up event batch file delivery

**KU ID:** `KU-EVT-setting-up-event-file-delivery` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/setting-up-event-file-delivery.md`:

> In addition to [real-time notifications](https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery), event data can be delivered as files via a configured integration channel to cloud storage — Amazon Web Services (AWS), Google Cloud Platform (GCP) — or downloaded using Secure File Transfer Protocol (SFTP).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/setting-up-event-file-delivery.md`: Setting up event batch file delivery; How it works; AWS S3; GCP cloud storage; SFTP; Validate integration

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/setting-up-event-file-delivery.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery · updatedAt: 2026-07-13T14:00:14.000Z

<!-- source:begin path=docs/data-and-reporting/setting-up-event-file-delivery.md part=0-end -->

# Setting up event batch file delivery

In addition to [real-time notifications](https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery), event data can be delivered as files via a configured integration channel to cloud storage — Amazon Web Services (AWS), Google Cloud Platform (GCP) — or downloaded using Secure File Transfer Protocol (SFTP).

## How it works

Event data is batched for **5 minutes** or until it reaches **10 MB** in size, then saved as a new object containing event JSON data in the `/main_stream/` path.

For information security, no S3 bucket is ever exposed publicly. A [Key Management Service (KMS)](https://aws.amazon.com/kms/) key is created for each bucket so that stored objects are encrypted and only decrypted when you download them.

Choose your delivery method below and follow the corresponding tutorial.

<Callout icon="⚠️" theme="warn">
  **File retention and download responsibility** Pismo retains files while your organization is active. However, we strongly recommend downloading files to your own infrastructure as soon as they are produced — either in real time (triggered by event notifications) or within 24 hours if you use a batch/polling strategy. These files belong to your organization, and keeping a local copy ensures you always have access. Please note that Pismo may charge additional fees for recovery requests of files older than 30 days.
</Callout>

# AWS S3

The following image shows the data flow for event file delivery to an AWS account

![Image shows the data flow for event file delivery to an AWS account.](https://files.readme.io/d3c4ba5-AWSedFlow.JPG "AWSedFlow.JPG")

#### How it works

1. Event files are generated and saved in a dedicated S3 bucket exclusive to your Org.

2. A listener detects the new file and generates a <Anchor label="new bucket object event" target="_blank" href="doc:event-data#new-event-file-notification">new bucket object event</Anchor>.

3. If you have real-time event delivery configured, the event is sent as a notification to your [SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html). Otherwise, you can poll the bucket periodically.

4. Your AWS account receives the event identifying the bucket, object path, and size.

5. Your routine invokes ([`sts:AssumeRole`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)) on Pismo's <Anchor label="IAM Role" target="_blank" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM Role</Anchor>, and then downloads the file via ( [`s3:GetObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)).

#### Pismo creates for you:

* **S3 bucket**— Exclusive to your Org. Example: `arn:aws:s3:::pismo-dataplatform-tn-376a4170-3c93-4676-b294-ec0b4241c7ab`
* **IAM Role** — For file downloading (`s3:GetObject`). Example: `arn:aws:iam::{pismo_aws_account_id}:role/dataplatform-consumer-tn-376a4170-...`

**Your configuration:** Follow the <Anchor label="AWS event file configuration tutorial" target="_blank" href="doc:aws-event-file-configuration-tutorial">AWS event file configuration tutorial</Anchor>.

# GCP cloud storage

The following image shows the data flow for event file delivery to a GCP account:

![Image shows the data flow for event file delivery to a GCP account.](https://files.readme.io/4129cfc-GCPedFlow.JPG "GCPedFlow.JPG")

**How it works:**

1. Event files are generated and saved in a dedicated S3 bucket.

2. A listener detects the new file and generates a notification.

3. The notification is delivered to your  [Pub/Sub](https://cloud.google.com/pubsub) topic.

4. Pismo's event consumer copies the file to your GCP Cloud Storage bucket.

**Your configuration:** Follow the [GCP event file configuration tutorial](https://developers.pismo.io/pismo-docs/docs/gcp-event-file-configuration-tutorial).

## SFTP

If you can't use cloud-native integrations (AWS/GCP), or prefer a simpler approach, SFTP is available. Pismo's SFTP service abstracts the S3 bucket behind an SFTP layer — when you connect, you access the same files.

<Callout icon="📘" theme="info">
  You can associate up to **8 SSH** keys per organization. Sandbox and production credentials are separate.
</Callout>

**Access endpoints:**

| Environment           | Endpoint                    | Port |
| --------------------- | --------------------------- | ---- |
| Sandbox / Development | sftp-main.data.pismolabs.io | 22   |
| Production            | sftp-main.data.pismo.io     | 22   |

**Knowing when files are available**: Set up real-time event notifications. Otherwise, periodically connect and check for new files.

**Your configuration:** Follow the <Anchor label="SFTP event file configuration tutorial" target="_blank" href="https://developers.pismo.io/pismo-docs/docs/sftp-event-file-configuration-tutorial">SFTP event file configuration tutorial</Anchor>.

## Validate integration

Each provider-specific tutorial includes a **Validate Integration** section with:

* Step-by-step manual validation commands
* Automated diagnostic scripts that check authentication, resources, permissions, and connectivity

Follow the tutorial for your chosen delivery method to access these tools.

<Callout icon="📘" theme="info">
  **Need Pismo-specific details?** Information such as Pismo's AWS Account ID, single-tenant SFTP endpoints, consumer role ARNs, or external IDs can be obtained from your **Technical Account Manager (TAM)** or the **Implementation Engineer** assigned to your project.
</Callout>

<br />
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/setting-up-event-file-delivery.md`: updatedAt 2026-07-13T14:00:14.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/setting-up-event-file-delivery.md` | whole document | https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery | `aac65a5595c499cb…` | 2026-07-13T14:00:14.000Z |

## Related knowledge units

- `KU-EVT-gcp-event-file-configuration-tutorial` — GCP event file configuration tutorial
- `KU-EVT-real-time-event-delivery` — Real-time event delivery: setup, additional subscribers and event filtering
- `KU-EVT-sftp-event-file-configuration-tutorial` — SFTP event file configuration tutorial
