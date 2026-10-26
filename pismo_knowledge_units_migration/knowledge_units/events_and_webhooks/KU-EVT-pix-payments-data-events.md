---
ku_id: KU-EVT-pix-payments-data-events
title: Instant payments - Pix
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/pix-payments-data-events.md
  sha256: 026066e143e8e9ac75bcf13538a7c28f88fc50f513abedc1f2da72379fb898ad
  url: https://developers.pismo.io/pismo-docs/docs/pix-payments-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:15:16.000Z'
operations:
- patch-v2-pix-keys
- post-cancel-dict-claim
- post-cancel-dict-refund
- post-close-dict-refund
- post-complete-dict-claim
- post-dict-key-claim
- post-pix-out-transfer
- post-pix-reversal
- post-register-dict-refund
- post-schedule
- post-v2-pix-infraction-cancel
- post-v2-pix-infraction-close
- post-v2-pix-infraction-create
- post-v2-pix-keys-create
related_kus:
- KU-API-instant-payments-pix-management--claims
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-instant-payments-pix-management--keys-part-01
- KU-API-instant-payments-pix-management--refunds
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--scheduled-transfers
- KU-EVT-catalogue-pix
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Instant payments - Pix

**KU ID:** `KU-EVT-pix-payments-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/pix-payments-data-events.md`:

> This table lists the Pix endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/pix-payments-data-events.md`: Instant payments - Pix

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 14 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/pix-payments-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pix-payments-data-events · updatedAt: 2026-03-18T15:15:16.000Z

<!-- source:begin path=docs/data-and-reporting/pix-payments-data-events.md part=0-end -->

# Instant payments - Pix

This table lists the Pix endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Pix payments endpoints
      </th>

      <th style={{ textAlign: "left" }}>
        Event
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        [Pix-out transfer](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-pix-out-1">Pix-out notification received</a>\ <a href="https://developers.pismo.io/events/docs/pix-pix-in-1">Pix-in notification received</a> (When funds are deposited in payee's account)\ <a href="https://developers.pismo.io/events/docs/pix-financial-reconciliation-1">Pix reconciliation notification received</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Pix reversal](https://developers.pismo.io/pismo-docs/reference/post-pix-reversal)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-pix-out-reversal-1">Pix-out reversed</a>\ <a href="https://developers.pismo.io/events/docs/pix-pix-in-reversal-1">Pix-in reversed</a> (When funds are transferred from payee's account)\ <a href="https://developers.pismo.io/events/docs/pix-financial-reconciliation-1">Pix transaction reconciliation</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Schedule transfer](https://developers.pismo.io/pismo-docs/reference/post-schedule)
      </td>

      <td style={{ textAlign: "left" }}>
        When scheduled transfer takes place:\ <a href="https://developers.pismo.io/events/docs/pix-pix-out-reversal-1">Pix-out notification received</a>\ <a href="https://developers.pismo.io/events/docs/pix-pix-in-1">Pix-in notification received</a> (When funds are deposited in payee's account)\ <a href="https://developers.pismo.io/events/docs/pix-financial-reconciliation-1">Pix transaction reconciliation</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **Pix management endpoints**
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create key entry](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-keys-create)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-key-status-change-1">Key status change</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update key entry](https://developers.pismo.io/pismo-docs/reference/patch-v2-pix-keys)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-key-status-change-1">Key status change</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create key claim](https://developers.pismo.io/pismo-docs/reference/post-dict-key-claim)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1">Claim status change</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create key claim](https://developers.pismo.io/pismo-docs/reference/post-dict-key-claim)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1">Claim status change</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Complete key claim](https://developers.pismo.io/pismo-docs/reference/post-complete-dict-claim)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1">Claim status change</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Cancel key claim](https://developers.pismo.io/pismo-docs/reference/post-cancel-dict-claim)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1">Claim status change </a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create infraction report](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-infraction-create)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1">Infraction status change </a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Close infraction report](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-infraction-close)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1">Infraction status change</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Cancel infraction report](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-infraction-cancel)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1">Infraction status change</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create refund request](https://developers.pismo.io/pismo-docs/reference/post-register-dict-refund)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1">Pix reversal (refund) status changed</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Cancel refund ](https://developers.pismo.io/pismo-docs/reference/post-cancel-dict-refund)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1">Pix reversal (refund) status changed</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Close refund](https://developers.pismo.io/pismo-docs/reference/post-close-dict-refund)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1">Pix reversal (refund) status changed</a>\ <a href="https://developers.pismo.io/events/docs/pix-financial-reconciliation-1">Pix transaction reconciliation</a>
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | Pix-out transfer | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /pix/v1/pix/in/reversal` | `post-pix-reversal` | Pix reversal | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /pix/v1/pix/out/schedule` | `post-schedule` | Schedule transfer [deprecated] | `api-specs/Instant_payments_-_Pix_payments.yaml` | **yes** | KU-API-instant-payments-pix-payments--scheduled-transfers |
| `POST /v2/pix/keys` | `post-v2-pix-keys-create` | Create key entry | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--keys-part-01 |
| `PATCH /v2/pix/keys` | `patch-v2-pix-keys` | Update key entry | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--keys-part-01 |
| `POST /v2/pix/claims` | `post-dict-key-claim` | Create key claim | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--claims |
| `POST /v2/pix/claims/complete` | `post-complete-dict-claim` | Complete key claim | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--claims |
| `POST /v2/pix/claims/cancel` | `post-cancel-dict-claim` | Cancel key claim | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--claims |
| `POST /v2/pix/infraction-reports` | `post-v2-pix-infraction-create` | Create infraction report (outdated) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01 |
| `POST /v2/pix/infraction-reports/{id}/close` | `post-v2-pix-infraction-close` | Close infraction report | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01 |
| `POST /v2/pix/infraction-reports/{id}/cancel` | `post-v2-pix-infraction-cancel` | Cancel infraction report | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01 |
| `POST /v2/pix/refunds` | `post-register-dict-refund` | Create refund request | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--refunds |
| `POST /v2/pix/refunds/{refundId}/cancel` | `post-cancel-dict-refund` | Cancel refund | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--refunds |
| `POST /v2/pix/refunds/{refundId}/close` | `post-close-dict-refund` | Close refund | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--refunds |

### Operation essentials

- **`POST /pix/v1/pix/out/transfer`** (`post-pix-out-transfer`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `transaction_type`; response statuses 202, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0020`, `EPIX0032`, `EPIX0139`, `EPIX0132`, `EPIX0067`, `EPIX0126`, `EPIX0115`, `EPIX0226`, `EPIX0227`, `EPIX0228`, `EPIX0136`, `EPIX0022`, `EPIX0137`, `EPIX0138`, `EPIX0113`, `EPIX0123`, `EPIX0120`, `EPIX0124`, `EPIX0122`, `EPIX0141`, `EPIX0019`, `EPIX0008`, `EPIX0053`, `EPIX0003`, `EPIX0114`, `EPIX0061`, `EPIX0068`, `EPIX0130`, `EPIX0045`, `EPIX0110`, `EPIX0146`, `EPIX0160`, `EPIX0049`, `EPIX0009`, `EPIX0069`, `EPIX0010`, `EPIX0111`, `EPIX0112`, `EPIX0051`, `EPIX0041`, `EPIX0071`, `EPIX0142`, `EPIX0144`, `EPIX0085`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0042`, `EPIX0017`, `EPIX0108`, `EPIX0109`, `EPIX0014`, `EPIX0043`, `EPIX0089`, `EPIX0046`, `EPIX0070`, `EPIX0018`, `EPIX0051`, `EPIX0060`, `EPIX0030`, `EPIX0050`, `EPIX0058`; events `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`POST /pix/v1/pix/in/reversal`** (`post-pix-reversal`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `end_to_end_id`, `reason`; response statuses 202, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0005`, `EPIX0020`, `PCE001`, `EPIX0045`, `EPIX0049`, `EPIX0084`, `EPIX0009`, `EPIX0010`, `EPIX0069`, `EPIX0132`, `EPIX0003`, `EPIX0041`, `EPIX0008`, `EPIX0071`, `EPIX0083`, `EPIX0085`, `EPIX0086`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0014`, `EPIX0043`, `EPIX0018`, `EPIX0030`; events `pix-financial-reconciliation-1`, `pix-pix-in-reversal-1`, `pix-pix-out-reversal-1`.
- **`POST /pix/v1/pix/out/schedule`** (`post-schedule`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `schedule_datetime`; response statuses 201, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0003`, `EPIX0019`, `EPIX0020`, `EPIX0032`, `EPIX0049`, `EPIX0091`, `EPIX0092`, `EPIX0099`, `EPIX0125`, `EPIX0126`, `EPIX0009`, `EPIX0010`, `EPIX0069`, `EPIX0132`, `EPIX0041`, `EPIX0008`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0017`, `EPIX0042`, `EPIX0095`, `EPIX0096`, `EPIX0097`, `EPIX0098`, `EPIX0018`, `EPIX0030`; events `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`POST /v2/pix/keys`** (`post-v2-pix-keys-create`): security `BearerAuth`; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `key`, `key_type`, `reason`, `bank_account`; response statuses 201, 202, 400, 401, 403, 404, 409, 429, 500, 502, 503, 504; error codes in examples `EPDA0169`, `EPDA0002`, `EPDA0003`, `EPDA0038`, `EPDA0039`, `EPDA0040`, `EPDA0041`, `EPDA0042`, `EPDA0043`, `EPDG0001`, `EPDG0011`, `PBE353`, `EPDG0018`, `EPDG0019`, `EPDG0035`, `EPDG0036`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDA0023`, `EPDA0024`, `EPDG0014`, `PBE353`, `EPDA0025`, `EPDA0028`, `EPDA0029`, `EPDG0005`, `EPDG0006`, `EPDG0007`, `EPDG0010`, `EPDG0016`, `PBE315`, `EPDG0020`, `EPDG0017`, `EPDG0021`, `EPDA0000`, `EPDG0000`; events `pix-dict-key-status-change-1`.
- **`PATCH /v2/pix/keys`** (`patch-v2-pix-keys`): security `BearerAuth`; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `key`, `key_type`, `reason`, `bank_account`; response statuses 200, 202, 400, 401, 403, 404, 409, 429, 500, 502, 503, 504; error codes in examples `EPDA0169`, `EPDA0002`, `EPDA0003`, `EPDG0001`, `EPDG0011`, `PBE353`, `EPDG0018`, `EPDG0019`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDG0014`, `PBE353`, `EPDA0024`, `EPDA0026`, `EPDA0028`, `EPDA0029`, `EPDG0005`, `EPDG0006`, `EPDG0007`, `EPDG0010`, `EPDG0016`, `PBE315`, `EPDG0020`, `EPDG0017`, `EPDG0021`, `EPDA0000`, `EPDG0000`; events `pix-dict-key-status-change-1`.
- **`POST /v2/pix/claims`** (`post-dict-key-claim`): security `BearerAuth`; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `claimer_account`, `key`, `key_type`, `type`; response statuses 200, 202, 400, 401, 403, 404, 500, 502, 504; error codes in examples `EPDA0180`, `EPDA0162`, `EPDA0160`, `EPDA0161`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDG0020`, `EPDA0000`; events `pix-dict-claim-status-change-1`.
- **`POST /v2/pix/claims/complete`** (`post-complete-dict-claim`): security `BearerAuth`; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `claim_id`; response statuses 200, 202, 400, 403, 404, 500, 502, 504; error codes in examples `EPDA0180`, `EPDA0162`, `EPDA0160`, `EPDA0161`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDG0020`, `EPDA0000`; events `pix-dict-claim-status-change-1`.
- **`POST /v2/pix/claims/cancel`** (`post-cancel-dict-claim`): security `BearerAuth`; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `claim_id`, `reason`; response statuses 200, 202, 400, 403, 404, 500, 502, 504; error codes in examples `EPDA0180`, `EPDA0162`, `EPDA0160`, `EPDA0161`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDG0020`, `EPDA0000`; events `pix-dict-claim-status-change-1`.
- **`POST /v2/pix/infraction-reports`** (`post-v2-pix-infraction-create`): security `BearerAuth`; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `transaction_id`, `situation_type`, `reason`; response statuses 201, 202, 400, 401, 403, 429, 500, 502, 503, 504; error codes in examples `EPDA0148`, `EPDA0149`, `EPDA0002`, `EPDA0003`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDA0029`, `EPDG0005`, `EPDG0006`, `EPDG0007`, `EPDG0010`, `EPDG0016`, `PBE315`, `EPDG0020`, `EPDG0017`, `EPDG0021`, `EPDA0000`, `EPDG0000`; events `pix-dict-infraction-status-change-1`.
- **`POST /v2/pix/infraction-reports/{id}/close`** (`post-v2-pix-infraction-close`): security `BearerAuth`; required parameters `Authorization` (header), `id` (path); required body fields `analysis_result`; response statuses 200, 202, 400, 401, 403, 404, 429, 500, 502, 503, 504; error codes in examples `EPDA0148`, `EPDA0149`, `EPDA0001`, `EPDA0070`, `EPDA0002`, `ECM0005`, `EPDA0003`, `ECM0002`, `ECM0003`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDA0049`, `EPDA0029`, `EPDG0005`, `EPDG0006`, `EPDG0007`, `EPDG0010`, `EPDG0016`, `PBE315`, `EPDG0020`, `EPDG0017`, `EPDG0021`, `EPDA0000`, `EPDG0000`; events `pix-dict-infraction-status-change-1`.
- **`POST /v2/pix/infraction-reports/{id}/cancel`** (`post-v2-pix-infraction-cancel`): security `BearerAuth`; required parameters `Authorization` (header), `id` (path); required body fields none declared; response statuses 200, 202, 400, 401, 403, 404, 429, 500, 502, 503, 504; error codes in examples `EPDA0148`, `EPDA0149`, `EPDA0001`, `EPDA0070`, `EPDA0073`, `EPDG0013`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDA0049`, `EPDA0029`, `EPDG0005`, `EPDG0006`, `EPDG0007`, `EPDG0010`, `EPDG0016`, `PBE315`, `EPDG0020`, `EPDG0017`, `EPDG0021`, `EPDA0000`, `EPDG0000`; events `pix-dict-infraction-status-change-1`.
- **`POST /v2/pix/refunds`** (`post-register-dict-refund`): security `BearerAuth`; required parameters `x-tenant` (header), `Idempotency-Key` (header); required body fields `refund_amount`, `refund_reason`, `transaction_id`; response statuses 200, 202, 400, 403, 404, 500, 502, 504; error codes in examples `EPDA0174`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDG0020`, `EPDA0000`, `EPDG0000`; events `pix-dict-refund-status-change-1`.
- **`POST /v2/pix/refunds/{refundId}/cancel`** (`post-cancel-dict-refund`): security `BearerAuth`; required parameters `x-tenant` (header), `Idempotency-Key` (header), `refundId` (path); required body fields none declared; response statuses 200, 400, 403, 404, 500, 502, 504; error codes in examples `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDG0020`, `EPDA0000`, `EPDG0000`; events `pix-dict-refund-status-change-1`.
- **`POST /v2/pix/refunds/{refundId}/close`** (`post-close-dict-refund`): security `BearerAuth`; required parameters `x-tenant` (header), `Idempotency-Key` (header), `refundId` (path); required body fields `refund_analysis_result`; response statuses 200, 202, 400, 403, 404, 500, 502, 504; error codes in examples `EPDA0174`, `EPDA0009`, `EPDA0010`, `EPDA0152`, `EPDG0020`, `EPDA0000`, `EPDG0000`; events `pix-dict-refund-status-change-1`, `pix-financial-reconciliation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-cancel-dict-claim` | `pix-dict-claim-status-change-1` |
| `post-complete-dict-claim` | `pix-dict-claim-status-change-1` |
| `post-dict-key-claim` | `pix-dict-claim-status-change-1` |
| `post-v2-pix-infraction-cancel` | `pix-dict-infraction-status-change-1` |
| `post-v2-pix-infraction-close` | `pix-dict-infraction-status-change-1` |
| `post-v2-pix-infraction-create` | `pix-dict-infraction-status-change-1` |
| `patch-v2-pix-keys` | `pix-dict-key-status-change-1` |
| `post-v2-pix-keys-create` | `pix-dict-key-status-change-1` |
| `post-cancel-dict-refund` | `pix-dict-refund-status-change-1` |
| `post-close-dict-refund` | `pix-dict-refund-status-change-1` |
| `post-register-dict-refund` | `pix-dict-refund-status-change-1` |
| `post-close-dict-refund` | `pix-financial-reconciliation-1` |
| `post-pix-out-transfer` | `pix-financial-reconciliation-1` |
| `post-pix-reversal` | `pix-financial-reconciliation-1` |
| `post-schedule` | `pix-financial-reconciliation-1` |
| `post-pix-out-transfer` | `pix-pix-in-1` |
| `post-schedule` | `pix-pix-in-1` |
| `post-pix-reversal` | `pix-pix-in-reversal-1` |
| `post-pix-out-transfer` | `pix-pix-out-1` |
| `post-schedule` | `pix-pix-out-1` |
| `post-pix-reversal` | `pix-pix-out-reversal-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `pix-dict-claim-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1 | 4 | KU-EVT-catalogue-pix |
| `pix-dict-infraction-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1 | 4 | KU-EVT-catalogue-pix |
| `pix-dict-key-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-key-status-change-1 | 3 | KU-EVT-catalogue-pix |
| `pix-dict-refund-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1 | 3 | KU-EVT-catalogue-pix |
| `pix-financial-reconciliation-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-financial-reconciliation-1 | 5 | KU-EVT-catalogue-pix |
| `pix-pix-in-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-in-1 | 3 | KU-EVT-catalogue-pix |
| `pix-pix-in-reversal-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-in-reversal-1 | 1 | KU-EVT-catalogue-pix |
| `pix-pix-out-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-out-1 | 3 | KU-EVT-catalogue-pix |
| `pix-pix-out-reversal-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-out-reversal-1 | 1 | KU-EVT-catalogue-pix |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/pix-payments-data-events.md`: updatedAt 2026-03-18T15:15:16.000Z.
- Links to `post-schedule`, which is marked `deprecated: true` in `api-specs/Instant_payments_-_Pix_payments.yaml`.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 9 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/pix-payments-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pix-payments-data-events | `026066e143e8e9ac…` | 2026-03-18T15:15:16.000Z |

## Related knowledge units

- `KU-API-instant-payments-pix-management--claims` — API reference: Instant payments - Pix management — Claims
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-instant-payments-pix-management--keys-part-01` — API reference: Instant payments - Pix management — Keys (part 1 of 2)
- `KU-API-instant-payments-pix-management--refunds` — API reference: Instant payments - Pix management — Refunds
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--scheduled-transfers` — API reference: Instant payments - Pix payments — Scheduled transfers
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
