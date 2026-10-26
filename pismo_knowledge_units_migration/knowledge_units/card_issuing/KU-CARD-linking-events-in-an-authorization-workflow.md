---
ku_id: KU-CARD-linking-events-in-an-authorization-workflow
title: Linking authorization events
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/linking-events-in-an-authorization-workflow.md
  sha256: 7c42210ae0ed7709e03689bf18efb51663b243e1e8a723ee52ddd97c1ba61cc6
  url: https://developers.pismo.io/pismo-docs/docs/linking-events-in-an-authorization-workflow
  role: primary_guide
  updated_at: '2026-06-26T15:44:17.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# Linking authorization events

**KU ID:** `KU-CARD-linking-events-in-an-authorization-workflow` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/linking-events-in-an-authorization-workflow.md`:

> Using events to map the life cycle of an authorization.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/linking-events-in-an-authorization-workflow.md`: Linking authorization events; Single action event mapping; Authorization online flow events; Reconciliation flow events; Mapping events of different actions taken over an authorization; Linking authorization with cancellation in online flow; Linking authorization with confirmation events; Mapping events external to the network-authorization events; Linking transaction creation events; Linking account limits impact events

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/linking-events-in-an-authorization-workflow.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/linking-events-in-an-authorization-workflow · updatedAt: 2026-06-26T15:44:17.000Z

<!-- source:begin path=docs/card-issuing/linking-events-in-an-authorization-workflow.md part=0-end -->

# Linking authorization events

Using events to map the life cycle of an authorization.

The authorization platform emits multiple events for each operation action. You can use these events to verify operation life cycle and monitor how events impact other parts of the flow, outside of the authorization itself.

Each event represents one step in the authorization process life cycle and provides all the relevant information for that step. For example, an authorization request that is approved and then confirmed in the clearing/base II flow issues the following events.

**Authorization request (online flow):**

* **iso8583-message** – Raw message in the authorization request.
* **network-authorization** – Request approval. `AUTHORIZATION` category
* **timeline/authorization\_authorize** – Request approval
* **network-message** – Approval response

**Clearing/base II (reconciliation flow):**

* **raw\_credit\_visa** – Raw message received in the clearing/base II flow. Event type depends on the operation type and network used.
* **network-authorization** – `CONFIRMATION` category. Request confirmation.
* **timeline/confirmation\_authorize** – Request confirmation.

To map an authorization's entire life cycle, you need to identify every related issued event. Each authorization action generates events that need to be linked to other events the authorization generates. The following sections show how to link the events of a single action and how to link events of different actions.

## Single action event mapping

A single action is any message received from the network that Pismo processes such as:

* **Authorization request**
* **Cancellation request**
* **Reconciliation flow message**

### Authorization online flow events

Online flow steps:

1. Pismo receives a message from the network indicating that an authorization request has been made. This message has its own kind of encoding and also contains sensitive data, so, after first validating it,  Pismo removes any sensitive data.
2. Pismo issues an [iso8583](https://en.wikipedia.org/wiki/ISO_8583) event containing the information. The event payload contains a [base contract](https://developers.pismo.io/events/docs/event-base-main-event) with a `cid` (correlation identifier) field. This field is used to link this event with later Pismo-issued events.
3. Pismo processes the request and issues a **network-authorization** event and a **timeline** event. The network-authorization event has the same `cid` value as the `iso8583-message` event. It also contains a `data.authorization_id` field. This field contains the internal `authorization_id` generated for the authorization. This ID is used to link the events of other actions over this authorization.
4. At the end of the flow, right before responding to the network, the platform issues a network-message event with the same `cid` value.

As should be evident, the easiest way to link events is via the `cid` field.

The flow is depicted below.

![Illustration of the authorization flow.](https://files.readme.io/f6fef47-diagram-online-authorization-request-flow_2x.png "diagram-online-authorization-request-flow_2x.png")

> 📘 Zero balance and the `cid` field
>
> For Zero balance workflows, you must use the field id present in the payload that is sent in the authorization flow to find the respective `network-message` event. The value in this field is the same as the value in the `cid` field.

### Reconciliation flow events

Reconciliation flow events:

1. Pismo receives a message from the network indicating that an authorization is confirmed or cancelled. Pismo parses the message and removes any sensitive data.
2. Pismo issues an event with this raw information (raw\_*\_*). The event payload contains a base contract with a `cid` field that you can use to link this event with later events.
3. Pismo processes the request and issues a **network-authorization** event and a **timeline** event. The network-authorization event has a `cid` field with the same value as in the raw\_*\_* event. It also has a `data.authorization_id` field. This is the internal ID generated for the authorization. This ID is the same as the one in the online flow. It links the events of all actions taken by this authorization.

As usual, the easiest way to link events is via the `cid` field.

Reconciliation flow:

![Illustration of the reconciliation flow.](https://files.readme.io/812c3d3-diagram-conciliation_2x.png "diagram-conciliation_2x.png")

> 🚧 Reconciliation message notes
>
> A reconciliation message may not be related to an authorization. When a new authorization is created, the events issued are the same as those described here, but the network-authorization event category will be “AUTHORIZATION”. The `authorization_id` will contain a new id and will not be related to previous network-authorization events.

> 📘 Zero balance notes
>
> For Zero balance workflows, you receive the raw reconciliation event and must use this event to perform the reconciliation flow on your side.

## Mapping events of different actions taken over an authorization

After linking a single action's events, you need to link the events from actions for the same authorization. You can use the network-authorization event to do this.

Here are two examples.

### Linking authorization with cancellation in online flow

If an operation is approved and then cancelled, the platform issues events for both actions (approval and cancellation). You can use the network-authorization event to link these events.

For example, suppose an operation is approved that has an `authorization_id` of 12345, a `cid` equal to `uuid-abc-777`, and an `authorization_code` of `ABC123`. The network-authorization event for the approval will have the following payload.

```json
{
    "event_id": "unique-event-id",
    "domain": "networktransactions",
    "event_type": "network-authorization",
    "schema_version": "1",
    "org_id": "org-id",
    "cid": "uuid-abc-777",
    "timestamp": "2021-01-01T00:00:00.000Z",
    "data": {
        "mti": "0100",
        "authorization_category": "AUTHORIZATION",
        "authorization_type": "NETWORK",
        "authorization_id": 12345,
        "authorization_code": "ABC123",
        "authorization_status":1,
        "ledger_update_id": "uuid-ledger-id",
        ...
        other fields omitted
        ...
    }
}
```

When the Pismo platform processes the cancellation, it issues an event with a new `cid`, which is used to link all the events of the cancellation flow. But the information for the operation, such as the `authorization_id` and the `authorization_code`, must be the same. The cancellation event will have the following payload.

```json
{
    "event_id": "unique-event-id",
    "domain": "networktransactions",
    "event_type": "network-authorization",
    "schema_version": "1",
    "org_id": "org-id",
    "cid": "uuid-333-zzz",
    "timestamp": "2021-01-02T00:00:00.000Z",
    "data": {
        "mti": "0400",
        "authorization_category": "CANCELLATION",
        "authorization_type": "NETWORK",
        "authorization_id": 12345,
        "authorization_code": "ABC123",
        "authorization_status":4,
        "ledger_update_id": "uuid-ledger-id-cancel",
        ...
        other fields omitted
        ...
    }
}
```

In this case, you can link both events using the `authorization_id` field, since it's a unique identifier for that authorization. It's possible to use fields like `tid` and `retrieval_reference_number` to link authorization messages, but those fields are not guaranteed to be the same for all messages, since they are generated by the acquirer and the network, so Pismo recommends that you use the `authorization_id` for this linking.

### Linking authorization with confirmation events

You can use the network-authorization event to link an authorization with a confirmation received from the reconciliation flow.

Here's the network-authorization event for the previous example.

```json
{
    "event_id": "unique-event-id",
    "domain": "networktransactions",
    "event_type": "network-authorization",
    "schema_version": "1",
    "org_id": "org-id",
    "cid": "uuid-abc-777",
    "timestamp": "2021-01-01T00:00:00.000Z",
    "data": {
        "mti": "0100",
        "authorization_category": "AUTHORIZATION",
        "authorization_type": "NETWORK",
        "authorization_id": 12345,
        "authorization_code": "ABC123",
        "authorization_status":1,
        "ledger_update_id": "uuid-ledger-id",
        ...
        other fields omitted
        ...
    }
}
```

When the Pismo platform processes the confirmation for this authorization, it issues a new event. The event contains the following payload.

```json
{
    "event_id": "unique-event-id",
    "domain": "networktransactions",
    "event_type": "network-authorization",
    "schema_version": "1",
    "org_id": "org-id",
    "cid": "uuid-abc-777",
    "timestamp": "2021-01-01T00:00:00.000Z",
    "data": {
        "mti": "0100",
        "authorization_category": "CONFIRMATION",
        "authorization_type": "NETWORK",
        "authorization_id": 12345,
        "authorization_code": "ABC123",
        "authorization_status":2,
        ...
        other fields omitted
        ...
    }
}
```

You can link both events using the `authorization_id` field, since it's a unique identifier for that authorization. It's possible to use fields like `tid` and `retrieval_reference_number` to link authorization messages, but those fields are not guaranteed to be the same for all messages, since they are generated by the acquirer and the network. So Pismo recommends that you use the `authorization_id` for this linking.

<Callout icon="📘" theme="info">
  In the reconciliation flow, there could be different amounts in the confirmation payload. This indicates that the authorization was confirmed with a different value, and this difference impacted the account limits. Also, there could be many partial cancellation events for the same authorization, all of them with amounts less than the total amount of the authorization.
</Callout>

Using these two types of linking --  events of a single action and events of different actions -- you can map the entire life cycle of an operation. You can tell if it was approved or declined; if it was approved, confirmed, and then cancelled; or if it was partially cancelled. The purpose of the events issued by the platform is to provide you with the information you need to monitor and control your tenant accounts and the operations realized through the network authorization flow.

#### How to correctly read airport tax amounts across two categories

For Visa transactions with airport tax, two clearing records are produced and paired internally:

* The AIRPORT\_TAX event is a lifecycle marker only and the `airport_tax` field is null.
* The CONFIRMATION event carries the actual tax amount in the `airport_tax` field, and the `contract_amount` reflects the total (installment + tax). The `contract_amount` is the gross total while `principal_amount`/`local_amount` are net of the tax. A record that triggers the AIRPORT\_TAX category does not carry a tax amount, so `airport_tax` is null on that event.

To get the airport tax value: filter for authorization\_category = CONFIRMATION with the same `authorization_id `and read the `airport_tax` field. The two clearing messages may arrive in any order, but the platform pairs them before emitting the confirmation event.

## Mapping events external to the network-authorization events

Using the network-authorization event, it's possible to link external events created by other APIs or other groups. Those events are **transaction creation** and **account limits impacts**.

### Linking transaction creation events

When the Pismo platform approves and confirms an authorization, it creates a transaction and posts it to the cardholder. This generates a transaction creation event (domain: transaction, type: creation). The `data.authorization.id` field for this event should contain the same authorization id as the `data.authorization.id` field of the network-authorization event. This confirms that the platform created a transaction for the authorization.

### Linking account limits impact events

If an action should have an impact on the limit of an account, the authorization platform calls the Ledger API to perform this impact. The Ledger API registers a unique id for the impact. You can use this id to link the impact with the action that caused it. The Ledger API emits an event to indicate the impact (domain: availables, type: change\_available)

The network-authorization event has a `ledger_update_id` field that contains the id for the impact event. You can use this to link the network-authorization event to the impact event. This confirms that Pismo applied the impact to the account limits.

<Callout icon="📘" theme="info">
  A network-authorization event can have a null value in the `ledger_update_id` field. This indicates that the operation had no impact on the account limits. For example, when there is a confirmation in the reconciliation flow with the same amount that was approved, there is no impact on the account limits.
</Callout>
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/linking-events-in-an-authorization-workflow.md`: updatedAt 2026-06-26T15:44:17.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/linking-events-in-an-authorization-workflow.md` | whole document | https://developers.pismo.io/pismo-docs/docs/linking-events-in-an-authorization-workflow | `7c42210ae0ed7709…` | 2026-06-26T15:44:17.000Z |

## Related knowledge units

- None.
