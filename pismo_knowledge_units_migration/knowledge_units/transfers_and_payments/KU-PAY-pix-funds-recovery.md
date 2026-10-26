---
ku_id: KU-PAY-pix-funds-recovery
title: Pix funds recovery [beta]
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/pix-funds-recovery.md
  sha256: f2a8f599746856f113fe797ad291412d0de85ff7958938a9b42f388d39b8208b
  url: https://developers.pismo.io/pismo-docs/docs/pix-funds-recovery
  role: primary_guide
  updated_at: '2026-04-24T22:22:58.000Z'
operations:
- get-v2-pix-infraction
- post-create-funds-recovery
- post-get-funds-recovery
- post-refund-recovery
related_kus:
- KU-API-instant-payments-pix-management--funds-recovery
- KU-API-instant-payments-pix-management--infraction-reports-part-02
- KU-EVT-catalogue-pix
grouping_rationale: single source page
---

# Pix funds recovery [beta]

**KU ID:** `KU-PAY-pix-funds-recovery` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/pix-funds-recovery.md`:

> This guide details the process for recovering funds in Pix. There is one flow you can use.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/pix-funds-recovery.md`: Pix funds recovery [beta]; Flow example; Scenario; Timeline; `AUTOMATIC` flow summary; Flow aspects; State flow; Endpoints called; Events generated

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/pix-funds-recovery.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pix-funds-recovery · updatedAt: 2026-04-24T22:22:58.000Z

<!-- source:begin path=docs/core-banking/pix-funds-recovery.md part=0-end -->

# Pix funds recovery [beta]

This guide details the process for recovering funds in Pix. There is one flow you can use.

* **`AUTOMATIC`**—The Diretório de Identificadores de Contas Transacionais (DICT)—a national Pix key registry and database—automatically manages tracking and blocking using a standard algorithm.

# Flow example

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>AUTOMATIC flow example</summary>

  ## Scenario

  **Case**: Wrong PIX scam (high volume, standard case)

  * **Victim**: Maria Santos (CPF: 987.654.321-00)
  * **Amount**: R$ 800.00
  * **Fraud date**: 11/10/2025 at 9:15 AM
  * **Situation**: Scammer convinced victim to send PIX "by mistake"
  * **Objective**: PSP wants to process quickly using DICT's standard algorithm

  ## Timeline

  #### **Day 1 - 11/10/2025**

  ##### 9:15 AM - Fraudulent transaction occurs

  ```
  Victim (PSP A) → Scammer (PSP B)
  EndToEndId: E98765432109876543210987654321001
  Amount: R$ 800.00
  ```

  ##### 9:30 AM - Victim reports to PSP

  Maria calls PSP A reporting that she was a victim of a scam.

  ##### 9:45 AM - **STEP 1: Funds recovery creation (`AUTOMATIC`)**

  **PSP A Request**:

  [Create funds recovery](https://developers.pismo.io/pismo-docs/reference/post-create-funds-recovery)

  ```bash
  POST /v1/pix/funds-recoveries

  {
    "flow_type": "AUTOMATED",
    "root_transaction_id": "E98765432109876543210987654321001",
    "situation_type": "SCAM",
    "contact_information": {
      "email": "fraud@pspa.com.br",
      "phone": "+5511987654321"
    },
    "report_details": "Client reports wrong PIX scam. Scammer claimed to have sent PIX by mistake and requested refund.",
    "tracking_graph_parameters": {
      "min_transaction_amount": 50.00,
      "max_transactions": 100,
      "hop_window": "PT1H",
      "max_hops": 4
    }
  }
  ```

  **Response (202 Accepted)**:

  ```json
  {
    "code": "EPDA0000",
    "message": "Funds recovery flow will continue asynchronously"
  }
  ```

  ##### 9:46 AM - Automatic processing initiated

  **Note**: DICT processes automatically:

  * Creates funds recovery
  * Sends root transaction infraction notification (PSP B blocks funds)
  * Builds tracking graph (8 transactions, 3 hops)
  * Calculates automatic prioritization
  * Sends infraction notifications to 5 PSPs

  ##### 9:50 AM - Event: CREATED

  **Event published**:

  [Pix funds recovery status changed](https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1)

  ```json
  {
    "domain": "pix-dict",
    "event_type": "funds_recoveries_status_changed",
    "data": {
      "funds_recovery_id": "650e8400-e29b-41d4-a716-446655440001",
      "status": "CREATED",
      "flow_type": "AUTOMATED",
      "changed_at": "2025-11-10T09:50:00Z"
    }
  }
  ```

  ##### 9:55 AM - Event: `AWAITING_ANALYSIS`

  After complete automatic processing, status changes directly to AWAITING\_ANALYSIS:

  ```json
  {
    "domain": "pix-dict",
    "event_type": "funds_recoveries_status_changed",
    "data": {
      "funds_recovery_id": "650e8400-e29b-41d4-a716-446655440001",
      "status": "AWAITING_ANALYSIS",
      "flow_type": "AUTOMATED",
      "changed_at": "2025-11-10T09:55:00Z"
    }
  }
  ```

  **Important note**: In `AUTOMATIC` flow, the status **never** goes through `TRACKED`, as the graph is created internally by DICT without exposure to the PSP.

  ##### 10:00 AM - PSP A Receives Confirmation

  PSP A queries the recovery:

  [Get funds recovery](https://developers.pismo.io/pismo-docs/reference/post-get-funds-recovery)

  ```bash
  GET /v1/pix/funds-recoveries/650e8400-e29b-41d4-a716-446655440001
  ```

  **Response**:

  ```json
  {
    "id": "650e8400-e29b-41d4-a716-446655440001",
    "status": "AWAITING_ANALYSIS",
    "flow_type": "AUTOMATED",
    "root_transaction_id": "E98765432109876543210987654321001",
    "situation_type": "SCAM",
    "reporter_participant": "12345678",
    "created_at": "2025-11-10T09:45:00Z",
    "updated_at": "2025-11-10T09:55:00Z"
  }
  ```

  #### **Days 2-8 - 11/11/2025 to 11/17/2025**

  ##### **STEP 2: Analysis by receiving PSPs (7 days)**

  **11/11 - PSP B analyzes (root transaction)**:

  ```
  - Blocked balance: R$ 300 (of R$ 800)
  - Client has complaint history
  - Account with atypical movement
  - Decision: ACCEPT
  ```

  **11/11 - PSP C analyzes**:

  ```
  - Mule account (opened 1 day ago)
  - Blocked balance: R$ 200
  - Decision: ACCEPT
  ```

  **11/12 - PSP D analyzes**:

  ```
  - Old account with clean history
  - Client claims legitimate product sale
  - Decision: REJECT
  ```

  **11/13 - PSP E analyzes**:

  ```
  - Mule account (opened 3 days ago)
  - Multiple suspicious transfers
  - Decision: ACCEPT
  ```

  **11/14 - PSP F analyzes**:

  ```
  - Account with fast dispersion pattern
  - Blocked balance: R$ 80
  - Decision: ACCEPT
  ```

  ##### 11/17 9:55 AM - Status Changes to `ANALYSED`

  After 7 days or all responses, status automatically changes:

  **Event published**:

  [Pix funds recovery status changed](https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1)

  ```json
  {
    "domain": "pix-dict",
    "event_type": "funds_recoveries_status_changed",
    "data": {
      "funds_recovery_id": "650e8400-e29b-41d4-a716-446655440001",
      "status": "ANALYSED",
      "changed_at": "2025-11-17T09:55:00Z"
    }
  }
  ```

  #### **Day 9 - 11/18/2025**

  ##### 8:00 AM - PSP A queries results

  [Get infraction report](https://developers.pismo.io/pismo-docs/reference/get-v2-pix-infraction)

  ```bash
  GET /v2/pix/infraction-reports?fundsRecoveryId=650e8400-e29b-41d4-a716-446655440001
  ```

  **Analysis summary**:

  * ✅ Accepted: 4 transactions (R$ 680 potential)
  * ❌ Rejected: 1 transaction (R$ 150 lost)

  ##### 8:30 AM - **STEP 3: Refund Request**

  **Request**:

  [Initiate refund funds recovery](https://developers.pismo.io/pismo-docs/reference/post-refund-recovery)

  ```bash
  POST /v1/pix/funds-recoveries/650e8400-e29b-41d4-a716-446655440001/refund
  ```

  **Response (202 Accepted)**:

  ```json
  {
    "code": "EPDA0000",
    "message": "Refund funds recovery flow will continue asynchronously"
  }
  ```

  ##### 8:35 AM - Status Changes to REFUNDING

  **Event published**:

  [Pix funds recovery status changed](https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1)

  ```json
  {
    "domain": "pix-dict",
    "event_type": "funds_recoveries_status_changed",
    "data": {
      "funds_recovery_id": "650e8400-e29b-41d4-a716-446655440001",
      "status": "REFUNDING",
      "changed_at": "2025-11-18T08:35:00Z"
    }
  }
  ```

  ##### 8:40 AM - Sequential refunds

  DICT builds refund graph (accepted transactions only) and processes refunds sequentially:

  ```
  Refund order:
  1. E9...001 (PSP B) → R$ 300
  2. E9...002 (PSP C) → R$ 200
  3. E9...005 (PSP E) → R$ 100
  4. E9...007 (PSP F) → R$ 80

  Result: All refunds processed successfully
  ```

  ##### 9:00 AM - Status changes to `COMPLETED`

  **Event published**:

  [Pix funds recovery status changed](https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1)

  ```json
  {
    "domain": "pix-dict",
    "event_type": "funds_recoveries_status_changed",
    "data": {
      "funds_recovery_id": "650e8400-e29b-41d4-a716-446655440001",
      "status": "COMPLETED",
      "changed_at": "2025-11-18T09:00:00Z"
    }
  }
  ```

  ##### 9:15 AM - PSP A Notifies Client

  ```
  SMS to Maria Santos:

  Hello Maria,

  Your funds recovery has been completed!

  Fraud amount: R$ 800.00
  Recovered amount: R$ 680.00
  Recovery rate: 85%

  The funds are already in your account.

  PSP A - Anti-Fraud Team
  ```

  ## `AUTOMATIC` flow summary

  ```
  Timeline:
  - Day 1 (9:45 AM): Creation + Automatic processing
  - Day 1 (9:55 AM): Blocks sent (AWAITING_ANALYSIS)
  - Day 9 (9:55 AM): Analysis completed (ANALYSED)
  - Day 10 (8:35 AM): Refund initiated (REFUNDING)
  - Day 10 (9:00 AM): Process completed (COMPLETED)

  Result:
  ✅ R$ 680 recovered (85%)
  ❌ R$ 120 not recovered (15%)

  AUTOMATIC flow advantages:
  - Fast and automatic processing
  - No need for human intervention
  - Optimized DICT algorithm
  - Ideal for high volume cases
  - Shorter total processing time
  ```

  ***
</details>

# Flow aspects

| Aspect                 | AUTOMATIC             |
| ---------------------- | --------------------- |
| **PSP control**        | Limited               |
| **Setup time**         | \~10 min (automatic)  |
| **`TRACKED`status**    | ❌ No (skips directly) |
| **Multiple graphs**    | ❌ Only 1 (internal)   |
| **Prioritization**     | Algorithm only        |
| **Graph visibility**   | ❌ Not exposed         |
| **Experimentation**    | ❌ No                  |
| **Total time**         | 9-10 days             |
| **Complexity**         | Low                   |
| **Ideal for**          | Standard cases        |
| **Recommended volume** | High                  |

## State flow

**`AUTOMATIC`**:

```
CREATED → AWAITING_ANALYSIS → ANALYSED → REFUNDING → COMPLETED
   ↓
CANCELLED
```

# Endpoints called

**`AUTOMATIC`**:

| Name                                                       | URL                                              |
| ---------------------------------------------------------- | ------------------------------------------------ |
| [Create funds recovery](https://developers.pismo.io/pismo-docs/reference/post-create-funds-recovery)    | `POST /funds-recoveries` (with graph parameters) |
| [Initiate refund funds recovery](https://developers.pismo.io/pismo-docs/reference/post-refund-recovery) | `POST /funds-recoveries/{id}/refund`             |

# Events generated

[Pix funds recovery status changed](https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/pix/funds-recoveries` | `post-create-funds-recovery` | Create funds recovery [beta] | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |
| `GET /v1/pix/funds-recoveries/{funds_recovery_id}` | `post-get-funds-recovery` | Get funds recovery [beta] | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |
| `GET /v2/pix/infraction-reports/{id}` | `get-v2-pix-infraction` | Get infraction report | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-02 |
| `POST /v1/pix/funds-recoveries/{funds_recovery_id}/refund` | `post-refund-recovery` | Initiate refund funds recovery [beta] | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |

### Operation essentials

- **`POST /v1/pix/funds-recoveries`** (`post-create-funds-recovery`): security `BearerAuth`; required parameters none declared; required body fields `root_transaction_id`, `situation_type`, `contact_information`; response statuses 201, 202, 400, 404, 409, 422, 504; error codes in examples `EPDA0169`, `EPDA0001`, `EPDA0192`, `EPDA0079`, `EPDA0190`, `EPDA0191`, `EPDA0192`, `EPDA0000`; events `pix-dict-funds-recoveries-status-change-1`.
- **`GET /v1/pix/funds-recoveries/{funds_recovery_id}`** (`post-get-funds-recovery`): security `BearerAuth`; required parameters `funds_recovery_id` (path); required body fields none declared; response statuses 200, 400, 403, 404, 504; error codes in examples `EPDA0000`, `EPDA0000`, `EPDA0000`, `EPDA0000`; events none listed.
- **`GET /v2/pix/infraction-reports/{id}`** (`get-v2-pix-infraction`): security `BearerAuth`; required parameters `Authorization` (header), `id` (path); required body fields none declared; response statuses 200, 400, 401, 403, 429, 500, 502, 503, 504; error codes in examples `EPDA0001`, `EPDA0070`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDA0029`, `EPDG0005`, `EPDG0006`, `EPDG0007`, `EPDG0010`, `EPDG0016`, `PBE315`, `EPDG0020`, `EPDG0017`, `EPDG0021`, `EPDA0000`, `EPDG0000`; events none listed.
- **`POST /v1/pix/funds-recoveries/{funds_recovery_id}/refund`** (`post-refund-recovery`): security `BearerAuth`; required parameters `funds_recovery_id` (path); required body fields none declared; response statuses 200, 202, 400, 404; error codes in examples `EPDA0000`, `EPDA0000`, `EPDA0000`; events `pix-dict-funds-recoveries-status-change-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-create-funds-recovery` | `pix-dict-funds-recoveries-status-change-1` |
| `post-refund-recovery` | `pix-dict-funds-recoveries-status-change-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `pix-dict-funds-recoveries-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1 | 3 | KU-EVT-catalogue-pix |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/pix-funds-recovery.md`: updatedAt 2026-04-24T22:22:58.000Z.
- The source title marks the feature as beta: "Pix funds recovery [beta]".

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/pix-funds-recovery.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pix-funds-recovery | `f2a8f599746856f1…` | 2026-04-24T22:22:58.000Z |

## Related knowledge units

- `KU-API-instant-payments-pix-management--funds-recovery` — API reference: Instant payments - Pix management — Funds recovery
- `KU-API-instant-payments-pix-management--infraction-reports-part-02` — API reference: Instant payments - Pix management — Infraction reports (part 2 of 2)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
