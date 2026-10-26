---
ku_id: KU-EVT-data-events-concepts
title: 'Data events: concepts and event-generating APIs'
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/event-data.md
  sha256: d13f66f70ee01281155074e571f976b1450d536252a8d6623a36c09da7cf74b3
  url: https://developers.pismo.io/pismo-docs/docs/event-data
  role: primary_guide
  updated_at: '2026-07-31T16:20:01.000Z'
- path: docs/data-and-reporting/data-events.md
  sha256: 34469fee21c9000338bec44a0f37a51a66c162534c16595aba180e3d630b6a01
  url: https://developers.pismo.io/pismo-docs/docs/data-events
  role: primary_guide
  updated_at: '2026-03-18T17:00:38.000Z'
operations: []
related_kus:
- KU-CARD-authorization-events
- KU-CARD-card-tokenization-flow-and-events
- KU-EVT-accounting-data-events
- KU-EVT-accounts-data-events
- KU-EVT-assets-data-events
- KU-EVT-aws-event-file-configuration-tutorial
- KU-EVT-balance-configurations-data-events
- KU-EVT-bank-slips-data-events
- KU-EVT-cards-data-events
- KU-EVT-corporate-banking-data-events
- KU-EVT-delinquency-account-data-events
- KU-EVT-delinquency-buckets-data-events
- KU-EVT-depositary-data-events
- KU-EVT-disputes-endpoint-generated-events
- KU-EVT-faster-payments-events
- KU-EVT-flex-controls-data-events
- KU-EVT-interest-management-data-events
- KU-EVT-international-bank-accounts-data-events
- KU-EVT-ledger-data-events
- KU-EVT-lending-data-events
- KU-EVT-marketplace-data-events
- KU-EVT-merchant-advancements-data-events
- KU-EVT-merchants-data-events
- KU-EVT-migrations-data-events
- KU-EVT-payments-data-events
- KU-EVT-pix-payments-data-events
- KU-EVT-real-time-event-delivery
- KU-EVT-recurring-charges-data-events
- KU-EVT-setting-up-event-file-delivery
- KU-EVT-statement-data-events
- KU-EVT-timeline-overview
- KU-EVT-transactions-data-events
- KU-LIFE-api-deprecation-strategy
- KU-RPT-scheduled-reports
grouping_rationale: Event concepts and the index of event-generating APIs.
---

# Data events: concepts and event-generating APIs

**KU ID:** `KU-EVT-data-events-concepts` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Event concepts and the index of event-generating APIs.

Scope as stated in `docs/get-started/event-data.md`:

> Pismo platform data events contain information pertaining to different platform processing actions, such as account operations, transactions, payments, auditing, and so on.  For the full list of Pismo-generated events, refer to  **[Events](https://developers.pismo.io/events/docs/event-base-main-event)**.

Scope as stated in `docs/data-and-reporting/data-events.md`:

> This guide lists events generated via platform APIs. For information about common event fields and how events are stored and accessed in the cloud, refer to [Data events](https://developers.pismo.io/pismo-docs/docs/event-data).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/event-data.md`: Data events; Data events configuration; Understanding Pismo event data; New event notifications; Sample new file event payload; JSON schema change notifications; Event schemas; Event validation; JSON schemas in HTML; JSON schemas in S3 bucket; Bucket access; Bucket path structure; Breaking changes to event schemas; Example schema-change event payloads
- `docs/data-and-reporting/data-events.md`: Event-generating APIs; Platform authentication; Platform setup; Core platform; Card issuing; Revolving credit; Banking; Instant payments; Data and reporting; Migrations; Seller management; Digital lending

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/event-data.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/event-data · updatedAt: 2026-07-31T16:20:01.000Z

<!-- source:begin path=docs/get-started/event-data.md part=0-end -->

# Data events

Pismo platform data events contain information pertaining to different platform processing actions, such as account operations, transactions, payments, auditing, and so on.  For the full list of Pismo-generated events, refer to  **[Events](https://developers.pismo.io/events/docs/event-base-main-event)**.

The data from these events is delivered to you in [real-time](https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery) or [via files](https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery) that you can download. Delivery works on an **at-least-once delivery guarantee**. This means that the platform keeps attempting to deliver a message until at least one attempt is successful.

To view the APIs that generate data events, refer to [Event generating APIs](https://developers.pismo.io/pismo-docs/docs/data-events).

> 📘 Timeline events versus data events
>
> [Timeline events](https://developers.pismo.io/pismo-docs/docs/timeline-overview) are meant to deliver messages to your end users, such as a credit-limit notification in a mobile banking app. These are not the same as [data events](https://developers.pismo.io/pismo-docs/docs/event-data).

# Data events configuration

Pismo integrates with the following cloud storage providers:

* Amazon Web Services (AWS) – Simple Notification Service (SNS) and EventBridge Service
* Google Cloud Platform (GCP) – Publish/Subscribe services
* Microsoft Azure Cloud Computing Services – Azure Service Bus
* Confluent Connector

Pismo APIs generate data event notifications to your preferred cloud storage provider. In addition, for files, Pismo provides delivery [via SFTP](https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery#setting-up-event-file-delivery-using-sftp) that does not involve cloud storage. Both delivery methods require some initial configuration and setup. For more information, see:

* [Setting up real-time event delivery](https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery)
* [Setting up event file delivery](https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery)

# Understanding Pismo event data

Pismo provides [JSON schemas](https://developers.pismo.io/events/docs/event-base-main-event) to document and validate events and their possible combinations, payloads, and event types. Event payload data is formatted in JavaScript Object Notation (JSON). For more information, see [Event schemas](#event-schemas) below.

```json event_main_payload_json
{
    "event_id": "252212bf-cde2-43f9-b28f-33ea2b452b32",
    "domain": "account",
    "event_type": "customer-creation-1",
    "schema_version": 1,
    "org_id": "<Your Org ID>",
    "cid": "7c7737f0-53d4-9b49-9833-e4c47483634e",
    "timestamp": "2019-07-20T19:03:00.000Z",
    "data": {<Varies according to domain, event_type, and schema_version>}
}
```

* **`event_id`** - Uniquely identifies each event.

* **`domain`** -  Represents a Pismo application domain. Examples include `account`, `authorization`, `cards`, and so on.  You can see a complete domain list in the navigation tab when you view Pismo's [JSON schemas in HTML](https://developers.pismo.io/events/docs/event-base-main-event).

* **`event_type`** -  Represents a processing action within a domain. For example, for `account`, these could include `customer-creation-1`, `limit-change-1`, and `status-change-1`. The number at the end represents the schema version. You can see a complete event type list in the navigation tab when you view Pismo's JSON schemas in HTML.

* **`schema_version`** - Represents the event's JSON schema version. The schema version number appears at the end of the `event_type` field, for example, `limit-change-1`.

* **`cid`** - The correlation identifier field is used to link related API requests and events. For example, if a user makes an authorization request with 10 installments, this generates 1 authorization event and 10 transaction events all containing the same correlation ID.

* **`timestamp`** - Indicates when the event occurred in ISO-8601 format.

* **`data`** - Contains the event data itself. This content varies  according to `domain`, `event_type` and `schema_version`. See Pismo's JSON schemas in HTML for details on event data.

# New event notifications

Event notifications and data are sent in real-time and via files. For event file delivery, event data is  batched for 5 minutes or until it reaches 10MB in size and then saved as a new AWS S3 bucket object to the `/main_stream/` path. When this occurs, a new bucket object event is generated and sent with data containing the object's  path, size, and name.

As with all events, the `dataplatform/new_bucket_object` event generates a new event as well as a real-time notification. The new event is saved as part of the next bucket object.

## Sample new file event payload

```json dataplatform/new_bucket_object-1
{
  "org_id": "TN-f770039e-aabd-498c-9134-9fde4cac4d51", 
  "cid": "d426f496-9fae-491e-a8b0-257eb6b8db16", 
  "event_id": "e03e7919-486e-4552-a7da-ae0b5a2b9a1e", 
  "domain": "dataplatform", 
  "event_type": "new_bucket_object", 
  "schema_version": 1, 
  "timestamp": "2020-04-11T19:22:37.946Z", 
  "data": {
    "object_size": 538, 
    "object_name": "main_stream/2020/04/11/19/dataplatform-tn-f770039e-aabd-498c-9134-9fde4cac4d51-1-2020-06-19-19-17-42-45baae47-28d6-4ef9-9f31-9cd1891d469b", 
    "bucket_name": "pismo-dataplatform-tn-f770039e-aabd-498c-9134-9fde4cac4d51"
  }
}
```

Although this object doesn't have a `.json` extension, it contains JSON event data and you can download it directly.

AWS CLI command to download bucket object:

```shell
aws s3 cp s3://<your bucket name>/main_stream/YYYY/MM/DD/HH/<object name> <download destination path>
```

## JSON schema change notifications

Whenever a JSON schema is created, modified, or deleted, the Pismo platform generates a [JSON schema change](https://developers.pismo.io/events/docs/dataplatform-json-schema-change-1) event. This event contains details about the change, such as the type of change, name of the affected schema, and the previous and new schema version numbers.

# Event schemas

Every event generated by an API has an associated **contract**. Contracts take the form of JSON schemas, which you can use for validation and to understand event payload data. The fields common to all events comprise the **base contract**. What distinguishes one event from another is its `data` field (payload).

You can view available event schemas in these ways:

* JSON schemas in HTML
* JSON schemas in S3 bucket

## Event validation

Pismo validates event payloads against their corresponding JSON schemas. Validation checks include, but are not limited to:

* Required field presence
* Data type validation
* Field format validation
* Schema-specific constraints

To help ensure the delivery of business data, events that fail JSON schema validation but pass all other platform validation checks are still delivered. As a result, data consumers should not assume that every delivered event fully conforms to the published schema.

We recommend validating incoming events against the published JSON schema and implementing appropriate handling for schema validation failures, such as logging, alerting, quarantining the event, or applying fallback processing.

Schema validation failures do not prevent event delivery and should be treated as data-quality issues rather than delivery failures.

## JSON schemas in HTML

The Pismo [event schema reference guide](https://developers.pismo.io/events/docs/event-base-main-event) provides a user-friendly resource for understanding JSON event schemas.  While this HTML is useful to view and understand events, for integration, you should use the S3 bucket JSON schemas.

## JSON schemas in S3 bucket

If you have an Amazon Web Services (AWS) cloud account, you can retrieve JSON schemas from Pismo's AWS [S3 bucket](https://aws.amazon.com/s3/). You will need to periodically check for updates, as no update notification is sent.

| Environment                           | S3 bucket                                          | Update rule                                                                                       |
| :------------------------------------ | :------------------------------------------------- | :------------------------------------------------------------------------------------------------ |
| Development / User acceptance testing | <nobr>`pismo-data-dev-dataplatform-docs`</nobr>    | Every time new events are created or a new schema version is updated during development or tests. |
| Production                            | `pismo-data-prod-dataplatform-docs`                | When these new schemas or versions are validated and promoted to production use.                  |
| For customers in India                | `pismo-data-india-dataplatform-docs/json_schemas/` | Only for customers located in India.                                                              |

### Bucket access

In order to access the JSON Schemas S3 Bucket, you have to complete the [AWS Files Integration](https://developers.pismo.io/pismo-docs/docs/aws-event-file-configuration-tutorial) for your org. There, the bucket access is described and can be tested using the testing script provided in [Test your AWS Integration](https://developers.pismo.io/pismo-docs/docs/aws-event-file-configuration-tutorial#test-your-aws-integration).

You can also obtain S3 bucket JSON schemas using AWS SDKs. To know what SDKs are available, see [Tools to Build on AWS](https://aws.amazon.com/tools/).

### Bucket path structure

The Pismo documentation S3 bucket has the following path structure:

* **`json_schemas/`** - Parent folder for Pismo JSON schemas.

* **`json_schemas/<domain>/`** - These folders represent Pismo application domains such as `account`, `cards`, `authorization`, and so on, and correspond to an event's `domain` field.

* **`json_schemas/<domain>/<event type>.json`** - Within each domain folder are the schema JSON files, named according to an event's  `event_type` field. For example: `json_schemas/account/customer-creation-1.json`.  Note that the schema version is part of the `event_type` field.

AWS CLI command to list all schemas:

```shell
aws s3 ls --recursive s3://pismo-data-dev-dataplatform-docs/json_schemas
```

AWS CLI command to list all schemas from a specific domain (`account`):

```text
aws s3 ls --recursive s3://pismo-data-dev-dataplatform-docs/json_schemas/account
```

# Breaking changes to event schemas

**Breaking changes** to event schemas are those that require you to update your implementation to avoid disruption. Changes of this type are rare, and Pismo is committed to communicating about such changes frequently and well in advance. Pismo considers changes like the following to be breaking changes:

* Renaming  or removing attributes
* Any change to the format of an attribute
* Changing an attribute's data type to any type other than `string`
* Changing optional attributes to required
* Tighter constraints (such as adding a limit to a value)

Pismo does not consider changes that convert an attribute's data type to `string` to be breaking changes. Nevertheless, it's important to review such changes and verify that your data processing logic continues to behave as expected.

In contrast, non-breaking changes to event schemas typically introduce new features or improve performance, but do not disrupt your current implementation. As with [Pismo APIs](https://developers.pismo.io/pismo-docs/docs/api-deprecation-strategy), these changes shouldn't require you to do anything to keep things working correctly. Non-breaking changes include:

* Adding events
* Adding optional fields to an event
* Changing required field to optional
* Looser constraints (such as expanding the range of allowed values)

# Example schema-change event payloads

```json Schema change: Created
{
    "event_id": "8004c09f-9480-42a3-9211-6fa62e026806",
    "cid": "1acb8e5f-f242-423e-be32-593650d81d9e",
    "org_id": "TN-1c058bed-991d-42e6-a60c-6b3b9b16dbea",
    "domain": "dataplatform",
    "event_type": "json_schema_change",
    "schema_version": "1",
    "timestamp": "2023-06-22T00:09:06Z",
    "data": {
        "change_type": "INSERT",
        "schema_name": "domain/event_type-1",
        "schema_domain": "domain",
        "schema_event_type": "event_type",
        "schema_version": "1",
        "new_schema": "{\"$schema\":\"http://json-schema.org/draft-07/schema#\",\"type\":\"object\",\"title\":\"Example JSON Schema\",\"description\":\"Example new description\",\"required\":[\"some_field\"],\"properties\":{\"some_field\":{\"type\":\"string\",\"title\":\"Some field title\"}}}"
    }
}
```

```json Schema change: Modified
{
    "event_id": "e2b3c97f-6ae1-41ac-817a-f6f92166d7dd",
    "cid": "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c",
    "org_id": "TN-9fc8e510-a27c-4b3b-b9a3-bf65f00256a8",
    "domain": "dataplatform",
    "event_type": "json_schema_change",
    "schema_version": "1",
    "timestamp": "2023-06-22T22:69:36Z",
    "data": {
        "change_type": "MODIFY",
        "schema_name": "domain/event_type-1",
        "schema_domain": "domain",
        "schema_event_type": "event_type",
        "schema_version": "1",
        "old_schema": "{\"$schema\":\"http://json-schema.org/draft-07/schema#\",\"type\":\"object\",\"title\":\"Example JSON Schema\",\"description\":\"Example old description\",\"required\":[\"some_field\"],\"properties\":{\"some_field\":{\"type\":\"string\",\"title\":\"Some field title\"}}}",
        "new_schema": "{\"$schema\":\"http://json-schema.org/draft-07/schema#\",\"type\":\"object\",\"title\":\"Example JSON Schema\",\"description\":\"Example new description\",\"required\":[\"some_field\"],\"properties\":{\"some_field\":{\"type\":\"string\",\"title\":\"Some field title\"}}}"
    }
}
```

```json Schema change: Deleted
{
    "event_id": "9fc8e510-a27c-4b3b-b9a3-bf65f00256a8",
    "cid": "1acb8e5f-f242-423e-be32-593650d81d9e",
    "org_id": "TN-9dg84c90-664e-95z7-b94k-9h3l8g76jdud",
    "domain": "dataplatform",
    "event_type": "json_schema_change",
    "schema_version": "1",
    "timestamp": "2023-06-22T11:39:06Z",
    "data": {
        "change_type": "REMOVE",
        "schema_name": "domain/event_type-1",
        "schema_domain": "domain",
        "schema_event_type": "event_type",
        "schema_version": "1",
        "old_schema": "{\"$schema\":\"http://json-schema.org/draft-07/schema#\",\"type\":\"object\",\"title\":\"Example JSON Schema\",\"description\":\"Example old description\",\"required\":[\"some_field\"],\"properties\":{\"some_field\":{\"type\":\"string\",\"title\":\"Some field title\"}}}"
    }
}
```
<!-- source:end -->

### Source 2: `docs/data-and-reporting/data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/data-events · updatedAt: 2026-03-18T17:00:38.000Z

<!-- source:begin path=docs/data-and-reporting/data-events.md part=0-end -->

# Event-generating APIs

This guide lists events generated via platform APIs. For information about common event fields and how events are stored and accessed in the cloud, refer to [Data events](https://developers.pismo.io/pismo-docs/docs/event-data).

> 📘 Timeline events versus data events
>
> [Timeline events](https://developers.pismo.io/pismo-docs/docs/timeline-overview) are meant to deliver messages to your end users, such as a credit-limit notification in a mobile banking app. These are not the same as [data events](https://developers.pismo.io/pismo-docs/docs/event-data).

For information about configuring data event delivery, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

The following events are generated via endpoints or related processing.

# Platform authentication

* Platform authentication (Passport API) - no events

# Platform setup

* Platform setup - Divisions - no events
* Platform setup - Holidays - no events
* Platform setup - Programs - no events
* Platform setup - Organizations - no events

# Core platform

* [Core platform - Accounting](https://developers.pismo.io/pismo-docs/docs/accounting-data-events)
* [Core platform - Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-data-events)
* Core platform - Accumulator - no events
* [Core platform - Balance configurations](https://developers.pismo.io/pismo-docs/docs/balance-configurations-data-events)
* Core platform - Balances and limits - no events
* Core platform - Configurations - no events
* Core platform - Exchange rates/Fee model - no events
* [Core platform - Flex controls](https://developers.pismo.io/pismo-docs/docs/flex-controls-data-events)
* [Core platform - Ledger](https://developers.pismo.io/pismo-docs/docs/ledger-data-events)
* [Core platform - Payments](https://developers.pismo.io/pismo-docs/docs/payments-data-events)
* [Core platform - Transactions](https://developers.pismo.io/pismo-docs/docs/transactions-data-events)

# Card issuing

* Card issuing - 3DS authentication - no events
* [Card issuing - Authorization](https://developers.pismo.io/pismo-docs/docs/authorization-events)
* [Card issuing - Tokenization](https://developers.pismo.io/pismo-docs/docs/card-tokenization-flow-and-events)
* [Card issuing - Disputes](https://developers.pismo.io/pismo-docs/docs/disputes-endpoint-generated-events)
* [Card issuing - Cards](https://developers.pismo.io/pismo-docs/docs/cards-data-events) (cards, cards on file, & tokenization)
* Card issuing - Protection Bulletin - no events

# Revolving credit

* [Revolving credit - Delinquent account](https://developers.pismo.io/pismo-docs/docs/delinquency-account-data-events)
* [Revolving credit - Delinquency](https://developers.pismo.io/pismo-docs/docs/delinquency-buckets-data-events)
* [Revolving credit - Recurring charges](https://developers.pismo.io/pismo-docs/docs/recurring-charges-data-events)
* [Revolving credit - Statements](https://developers.pismo.io/pismo-docs/docs/statement-data-events)

# Banking

* [Banking - Assets](https://developers.pismo.io/pismo-docs/docs/assets-data-events)
* [Banking - Bank accounts](https://developers.pismo.io/pismo-docs/docs/international-bank-accounts-data-events)
* [Banking - Credit receivables](https://developers.pismo.io/pismo-docs/docs/depositary-data-events)
* [Banking - Interest management](https://developers.pismo.io/pismo-docs/docs/interest-management-data-events)
* [Banking - Integrated payments](https://developers.pismo.io/pismo-docs/docs/bank-slips-data-events)
* Banking - Banking authorization - no events
* Banking - Banking reports - no events
* [Banking - Transaction banking](https://developers.pismo.io/pismo-docs/docs/corporate-banking-data-events)

# Instant payments

* Instant payments - BR Code - no events
* Instant payments - QR Code - no events
* [Instant payments - Faster Payments](https://developers.pismo.io/pismo-docs/docs/faster-payments-events)
* [Instant payments - Pix](https://developers.pismo.io/pismo-docs/docs/pix-payments-data-events) (Pix payments and Pix management)

# Data and reporting

* Data and reporting - Timeline - no events

# Migrations

* [Migrations](https://developers.pismo.io/pismo-docs/docs/migrations-data-events)

# Seller management

* [Seller management - Marketplace](https://developers.pismo.io/pismo-docs/docs/marketplace-data-events)
* [Seller management - Merchant advance](https://developers.pismo.io/pismo-docs/docs/merchant-advancements-data-events)
* [Seller management - Merchants](https://developers.pismo.io/pismo-docs/docs/merchants-data-events)

# Digital lending

* [Digital lending](https://developers.pismo.io/pismo-docs/docs/lending-data-events)
<!-- source:end -->

## Lifecycle status

- `docs/get-started/event-data.md`: updatedAt 2026-07-31T16:20:01.000Z.
- `docs/data-and-reporting/data-events.md`: updatedAt 2026-03-18T17:00:38.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/event-data.md` | whole document | https://developers.pismo.io/pismo-docs/docs/event-data | `d13f66f70ee01281…` | 2026-07-31T16:20:01.000Z |
| `docs/data-and-reporting/data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/data-events | `34469fee21c90003…` | 2026-03-18T17:00:38.000Z |

## Related knowledge units

- `KU-CARD-authorization-events` — Authorization events
- `KU-CARD-card-tokenization-flow-and-events` — Card tokenization flow and events
- `KU-EVT-accounting-data-events` — Core platform - Accounting
- `KU-EVT-accounts-data-events` — Core platform - Accounts
- `KU-EVT-assets-data-events` — Banking - Assets
- `KU-EVT-aws-event-file-configuration-tutorial` — AWS event file configuration tutorial
- `KU-EVT-balance-configurations-data-events` — Core platform - Balance configurations
- `KU-EVT-bank-slips-data-events` — Banking - Integrated payments
- `KU-EVT-cards-data-events` — Card issuing - Cards
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
- `KU-EVT-delinquency-account-data-events` — Revolving credit - Delinquent account
- `KU-EVT-delinquency-buckets-data-events` — Revolving credit - Delinquency
- `KU-EVT-depositary-data-events` — Banking - Credit receivables
- `KU-EVT-disputes-endpoint-generated-events` — Card issuing - Disputes
- `KU-EVT-faster-payments-events` — Instant payments - Faster Payments
- `KU-EVT-flex-controls-data-events` — Core platform - Flex controls
- `KU-EVT-interest-management-data-events` — Banking - Interest management
- `KU-EVT-international-bank-accounts-data-events` — Banking - Bank accounts
- `KU-EVT-ledger-data-events` — Core platform - Ledger
- `KU-EVT-lending-data-events` — Lending events
- `KU-EVT-marketplace-data-events` — Seller management - Marketplace
- `KU-EVT-merchant-advancements-data-events` — Seller management - Merchant advance
- `KU-EVT-merchants-data-events` — Seller management - Merchants
- `KU-EVT-migrations-data-events` — Migrations events
- `KU-EVT-payments-data-events` — Core platform - Payments
- `KU-EVT-pix-payments-data-events` — Instant payments - Pix
- `KU-EVT-real-time-event-delivery` — Real-time event delivery: setup, additional subscribers and event filtering
- `KU-EVT-recurring-charges-data-events` — Revolving credit - Recurring charges
- `KU-EVT-setting-up-event-file-delivery` — Setting up event batch file delivery
- `KU-EVT-statement-data-events` — Revolving credit - Statements
- `KU-EVT-timeline-overview` — Timeline events
- `KU-EVT-transactions-data-events` — Core platform - Transactions
- `KU-LIFE-api-deprecation-strategy` — API lifecycle and deprecation strategy
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
