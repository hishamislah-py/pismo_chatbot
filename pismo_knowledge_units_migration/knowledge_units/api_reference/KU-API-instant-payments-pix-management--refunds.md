---
ku_id: KU-API-instant-payments-pix-management--refunds
title: 'API reference: Instant payments - Pix management — Refunds'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Instant_payments_-_Pix_management.yaml
  sha256: 7d7fee078ccf55696a5fdd1a00ea559d88a6148a11b28529395dab8f2405a750
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: openapi_specification
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/operations_catalog.csv
  sha256: b218bf75940b0c374ca9e3a48fe92fb615b559e3192f263aff99b738b50a71cf
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/request_response_examples.csv
  sha256: ac921f2e8d0d154511b4550462e609cf6bebe3e6ce05dada157e0ed645a80856
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- get-list-dict-refunds
- post-register-dict-refund
- get-dict-refund
- post-cancel-dict-refund
- post-close-dict-refund
related_kus:
- KU-ERR-codes-epda
- KU-ERR-codes-epdg
- KU-EVT-catalogue-pix
- KU-EVT-pix-payments-data-events
- KU-PAY-pix-instant-payments
specification_version: 0.0.1
---

# API reference: Instant payments - Pix management — Refunds

**KU ID:** `KU-API-instant-payments-pix-management--refunds` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Refunds` in `api-specs/Instant_payments_-_Pix_management.yaml` (“Instant payments - Pix management”, version `0.0.1`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage DICT refunds endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/pix/refunds` | `get-list-dict-refunds` | List refunds | no |
| `POST /v2/pix/refunds` | `post-register-dict-refund` | Create refund request | no |
| `GET /v2/pix/refunds/{refundId}` | `get-dict-refund` | Get refund | no |
| `POST /v2/pix/refunds/{refundId}/cancel` | `post-cancel-dict-refund` | Cancel refund | no |
| `POST /v2/pix/refunds/{refundId}/close` | `post-close-dict-refund` | Close refund | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v2/pix/refunds operationId=get-list-dict-refunds -->
### `GET /v2/pix/refunds` — List refunds

- **operationId:** `get-list-dict-refunds`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Refunds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List DICT refunds for an organization.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization/tenant ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `participant_role` | query | yes | string | Participant role filter | enum: ["CONTESTED", "REQUESTED"]; example: "CONTESTED" |
| `funds_recovery_id` | query | no | string | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `x-cid` | header | no | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> | example: "B20220921145635222303062944CA66F" |
| `include_details` | query | no | boolean | Include details in response? Default is `false`. | default: false; example: false |
| `limit` | query | no | integer | Maximum results to return. Default is `20`. Maximum is `200`. | default: 20; maximum: 200; example: 20 |
| `modified_after` | query | no | string | Return DICT refunds modified after this date.  A RFC 3339 date-time value. For example - `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `modified_before` | query | no | string | Return DICT refunds modified before this date.  A RFC 3339 date-time value. For example - `2023-04-12T23:20:50.52Z`. | example: "2023-04-12T23:20:50.52Z" |
| `status` | query | no | string | Refund status filter | enum: ["OPEN", "CLOSED", "CANCELLED"]; example: "OPEN" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | List refunds | `application/json`: object (schema `RefundListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 500 | Internal server errpr | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_more_elements` | boolean (schema `HasMoreElements`) | yes | Are there more items? | example: true |
| `items` | array of object (schema `Refund`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EPDA0009` (Missing required header 'x-tenant'):

```json
{
  "code": "EPDA0009",
  "message": "Missing required header 'x-tenant'"
}
```

403 Example `EPDA0010` (Missing required header 'x-account-id'):

```json
{
  "code": "EPDA0010",
  "message": "Missing required header 'x-account-id'"
}
```

403 Example `EPDA0152` (Missing required param 'id'):

```json
{
  "code": "EPDA0152",
  "message": "Missing required param 'id'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Service timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout while executing the request"
}
```

504 Example `Provider timeout`:

```json
{
  "code": "EPDG0000",
  "message": "Timeout while executing the request"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 504 | `EPDA0000` | Timeout while executing the request |
| 504 | `EPDG0000` | Timeout while executing the request |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500;502;504`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/refunds operationId=post-register-dict-refund -->
### `POST /v2/pix/refunds` — Create refund request

- **operationId:** `post-register-dict-refund`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Refunds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a DICT refund request.
>
> On PSP timeout, a `202 Accepted` response is returned and the process continues asynchronously, eventually emitting an event if it succeeds. 
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1">Pix reversal (refund) status changed</a> event. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization/tenant ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |
| `x-cid` | header | no | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> | example: "B20220921145635222303062944CA66F" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `RefundRegisterRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `refund_amount` | string (schema `RefundAmount`) | yes | Refund amount | example: "20.10" |
| `refund_reason` | string (schema `RefundReason`) | yes | Refund reason. <br><br>`PIX_AUTOMATICO` means a refund was requested due to failed Automatic Pix operation.<br> | enum: ["FRAUD", "OPERATIONAL_FLAW", "PIX_AUTOMATICO", "REFUND_CANCELLED"]; example: "OPERATIONAL_FLAW" |
| `transaction_id` | string (schema `RefundTransactionID`) | yes | Refund transaction ID | example: "E9999901012341234123412345678900" |
| `refund_details` | string (schema `RefundDetails`) | no | Details about refund | maxLength: 2000; example: "Details about the refund request" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Refund registered | `application/json`: object (schema `Refund`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 500 | Internal server errpr | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `contested_participant` | string (schema `ContestedParticipant`) | yes | Challenged participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `creation_date_time` | string | yes | Creation date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `last_modified` | string | yes | Last modified date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `refund_amount` | string (schema `RefundAmount`) | yes | Refund amount | example: "20.10" |
| `refund_id` | string | yes | Refund ID | example: "12345645-9ff7-439f-a318-2e6f974707a5" |
| `refund_reason` | string (schema `RefundReason`) | yes | Refund reason. <br><br>`PIX_AUTOMATICO` means a refund was requested due to failed Automatic Pix operation.<br> | enum: ["FRAUD", "OPERATIONAL_FLAW", "PIX_AUTOMATICO", "REFUND_CANCELLED"]; example: "OPERATIONAL_FLAW" |
| `requesting_participant` | string (schema `RequestingParticipant`) | yes | Requesting participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `status` | string (schema `RefundStatus`) | yes | Refund status | enum: ["OPEN", "CLOSED", "CANCELLED"]; example: "CLOSED" |
| `transaction_id` | string (schema `RefundTransactionID`) | yes | Refund transaction ID | example: "E9999901012341234123412345678900" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `infraction_report_id` | string (schema `InfractionReportID`) | no | Infraction report ID (UUID) | format: "uuid"; maxLength: 36; example: "cfdff46e-5d58-45b8-b7aa-591a65f74444" |
| `refund_analysis_details` | string (schema `RefundAnalysisDetails`) | no | Refund analysis details | example: "Details about the refund analysis." |
| `refund_analysis_result` | string (schema `RefundAnalysis`) | no | Respondent's refund request analysis result. | enum: ["TOTALLY_ACCEPTED", "PARTIALLY_ACCEPTED", "REJECTED"]; example: "PARTIALLY_ACCEPTED" |
| `refund_details` | string (schema `RefundDetails`) | no | Details about refund | maxLength: 2000; example: "Details about the refund request" |
| `refund_rejection_reason` | string (schema `RefundRejectionReason`) | no | Refund rejecton reason. <br><br>**REQUIRED** when `refund_analysis_result` is `REJECTED`.<br> | enum: ["NO_BALANCE", "ACCOUNT_CLOSURE", "INVALID_REQUEST", "OTHER"]; example: "NO_BALANCE" |
| `refund_account` | object (schema `RefundAccount`) | no |  |  |
| `refund_transaction_id` | string (schema `RefundTransactionID`) | no | Refund transaction ID | example: "E9999901012341234123412345678900" |
| `funds_recovery_id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `monitor_account` | boolean (schema `MonitorAccount`) | no | Should the account be monitored for suspicious activity? | example: false |
| `effective_refunded_amount` | number (schema `EffectiveRefundedAmount`) | no | Actual amount refunded to the user. | example: 20.1 |

##### Response 202

- Response header `x-cid`: Request tracking identifier. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

202 Example `Request accepted and will processed async`:

```json
{
  "code": "EPDA0174",
  "message": "Refund flow will continue asynchronously"
}
```

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EPDA0009` (Missing required header 'x-tenant'):

```json
{
  "code": "EPDA0009",
  "message": "Missing required header 'x-tenant'"
}
```

403 Example `EPDA0010` (Missing required header 'x-account-id'):

```json
{
  "code": "EPDA0010",
  "message": "Missing required header 'x-account-id'"
}
```

403 Example `EPDA0152` (Missing required param 'id'):

```json
{
  "code": "EPDA0152",
  "message": "Missing required param 'id'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Service timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout while executing the request"
}
```

504 Example `Provider timeout`:

```json
{
  "code": "EPDG0000",
  "message": "Timeout while executing the request"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `EPDA0174` | Refund flow will continue asynchronously |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 504 | `EPDA0000` | Timeout while executing the request |
| 504 | `EPDG0000` | Timeout while executing the request |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-refund-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;403;404;500;502;504`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v2/pix/refunds/{refundId} operationId=get-dict-refund -->
### `GET /v2/pix/refunds/{refundId}` — Get refund

- **operationId:** `get-dict-refund`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Refunds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get DICT refund

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization/tenant ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `x-account-id` | header | no | string | Pismo account ID. **REQUIRED** if this is an intra-PSP transaction, meaing a transaction within the same organization or participant. | example: "8675309" |
| `refundId` | path | yes | string | Refund ID | example: "4749993777899937" |
| `x-cid` | header | no | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> | example: "B20220921145635222303062944CA66F" |
| `useProvider` | query | no | string | Search refund in provider? Default is `false`. | example: "true" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Search refund | `application/json`: object (schema `Refund`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 500 | Internal server errpr | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `contested_participant` | string (schema `ContestedParticipant`) | yes | Challenged participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `creation_date_time` | string | yes | Creation date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `last_modified` | string | yes | Last modified date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `refund_amount` | string (schema `RefundAmount`) | yes | Refund amount | example: "20.10" |
| `refund_id` | string | yes | Refund ID | example: "12345645-9ff7-439f-a318-2e6f974707a5" |
| `refund_reason` | string (schema `RefundReason`) | yes | Refund reason. <br><br>`PIX_AUTOMATICO` means a refund was requested due to failed Automatic Pix operation.<br> | enum: ["FRAUD", "OPERATIONAL_FLAW", "PIX_AUTOMATICO", "REFUND_CANCELLED"]; example: "OPERATIONAL_FLAW" |
| `requesting_participant` | string (schema `RequestingParticipant`) | yes | Requesting participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `status` | string (schema `RefundStatus`) | yes | Refund status | enum: ["OPEN", "CLOSED", "CANCELLED"]; example: "CLOSED" |
| `transaction_id` | string (schema `RefundTransactionID`) | yes | Refund transaction ID | example: "E9999901012341234123412345678900" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `infraction_report_id` | string (schema `InfractionReportID`) | no | Infraction report ID (UUID) | format: "uuid"; maxLength: 36; example: "cfdff46e-5d58-45b8-b7aa-591a65f74444" |
| `refund_analysis_details` | string (schema `RefundAnalysisDetails`) | no | Refund analysis details | example: "Details about the refund analysis." |
| `refund_analysis_result` | string (schema `RefundAnalysis`) | no | Respondent's refund request analysis result. | enum: ["TOTALLY_ACCEPTED", "PARTIALLY_ACCEPTED", "REJECTED"]; example: "PARTIALLY_ACCEPTED" |
| `refund_details` | string (schema `RefundDetails`) | no | Details about refund | maxLength: 2000; example: "Details about the refund request" |
| `refund_rejection_reason` | string (schema `RefundRejectionReason`) | no | Refund rejecton reason. <br><br>**REQUIRED** when `refund_analysis_result` is `REJECTED`.<br> | enum: ["NO_BALANCE", "ACCOUNT_CLOSURE", "INVALID_REQUEST", "OTHER"]; example: "NO_BALANCE" |
| `refund_account` | object (schema `RefundAccount`) | no |  |  |
| `refund_transaction_id` | string (schema `RefundTransactionID`) | no | Refund transaction ID | example: "E9999901012341234123412345678900" |
| `funds_recovery_id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `monitor_account` | boolean (schema `MonitorAccount`) | no | Should the account be monitored for suspicious activity? | example: false |
| `effective_refunded_amount` | number (schema `EffectiveRefundedAmount`) | no | Actual amount refunded to the user. | example: 20.1 |

##### Response 202

- Response header `x-cid`: Request tracking identifier. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

202 Example `Request accepted and will processed async`:

```json
{
  "code": "EPDA0174",
  "message": "Refund flow will continue asynchronously"
}
```

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EPDA0009` (Missing required header 'x-tenant'):

```json
{
  "code": "EPDA0009",
  "message": "Missing required header 'x-tenant'"
}
```

403 Example `EPDA0010` (Missing required header 'x-account-id'):

```json
{
  "code": "EPDA0010",
  "message": "Missing required header 'x-account-id'"
}
```

403 Example `EPDA0152` (Missing required param 'id'):

```json
{
  "code": "EPDA0152",
  "message": "Missing required param 'id'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Service timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout while executing the request"
}
```

504 Example `Provider timeout`:

```json
{
  "code": "EPDG0000",
  "message": "Timeout while executing the request"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `EPDA0174` | Refund flow will continue asynchronously |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 504 | `EPDA0000` | Timeout while executing the request |
| 504 | `EPDG0000` | Timeout while executing the request |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;403;404;500;502;504`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/refunds/{refundId}/cancel operationId=post-cancel-dict-refund -->
### `POST /v2/pix/refunds/{refundId}/cancel` — Cancel refund

- **operationId:** `post-cancel-dict-refund`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Refunds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel a DICT refund request. 
>
> On PSP timeout, a `202 Accepted` response is returned and the process continues asynchronously, eventually emitting an event if it succeeds. 
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1">Pix reversal (refund) status changed</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization/tenant ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `x-cid` | header | no | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> | example: "B20220921145635222303062944CA66F" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |
| `refundId` | path | yes | string | Refund ID | example: "4749993777899937" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Refund cancelled | `application/json`: object (schema `Refund`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 500 | Internal server errpr | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `contested_participant` | string (schema `ContestedParticipant`) | yes | Challenged participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `creation_date_time` | string | yes | Creation date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `last_modified` | string | yes | Last modified date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `refund_amount` | string (schema `RefundAmount`) | yes | Refund amount | example: "20.10" |
| `refund_id` | string | yes | Refund ID | example: "12345645-9ff7-439f-a318-2e6f974707a5" |
| `refund_reason` | string (schema `RefundReason`) | yes | Refund reason. <br><br>`PIX_AUTOMATICO` means a refund was requested due to failed Automatic Pix operation.<br> | enum: ["FRAUD", "OPERATIONAL_FLAW", "PIX_AUTOMATICO", "REFUND_CANCELLED"]; example: "OPERATIONAL_FLAW" |
| `requesting_participant` | string (schema `RequestingParticipant`) | yes | Requesting participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `status` | string (schema `RefundStatus`) | yes | Refund status | enum: ["OPEN", "CLOSED", "CANCELLED"]; example: "CLOSED" |
| `transaction_id` | string (schema `RefundTransactionID`) | yes | Refund transaction ID | example: "E9999901012341234123412345678900" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `infraction_report_id` | string (schema `InfractionReportID`) | no | Infraction report ID (UUID) | format: "uuid"; maxLength: 36; example: "cfdff46e-5d58-45b8-b7aa-591a65f74444" |
| `refund_analysis_details` | string (schema `RefundAnalysisDetails`) | no | Refund analysis details | example: "Details about the refund analysis." |
| `refund_analysis_result` | string (schema `RefundAnalysis`) | no | Respondent's refund request analysis result. | enum: ["TOTALLY_ACCEPTED", "PARTIALLY_ACCEPTED", "REJECTED"]; example: "PARTIALLY_ACCEPTED" |
| `refund_details` | string (schema `RefundDetails`) | no | Details about refund | maxLength: 2000; example: "Details about the refund request" |
| `refund_rejection_reason` | string (schema `RefundRejectionReason`) | no | Refund rejecton reason. <br><br>**REQUIRED** when `refund_analysis_result` is `REJECTED`.<br> | enum: ["NO_BALANCE", "ACCOUNT_CLOSURE", "INVALID_REQUEST", "OTHER"]; example: "NO_BALANCE" |
| `refund_account` | object (schema `RefundAccount`) | no |  |  |
| `refund_transaction_id` | string (schema `RefundTransactionID`) | no | Refund transaction ID | example: "E9999901012341234123412345678900" |
| `funds_recovery_id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `monitor_account` | boolean (schema `MonitorAccount`) | no | Should the account be monitored for suspicious activity? | example: false |
| `effective_refunded_amount` | number (schema `EffectiveRefundedAmount`) | no | Actual amount refunded to the user. | example: 20.1 |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EPDA0009` (Missing required header 'x-tenant'):

```json
{
  "code": "EPDA0009",
  "message": "Missing required header 'x-tenant'"
}
```

403 Example `EPDA0010` (Missing required header 'x-account-id'):

```json
{
  "code": "EPDA0010",
  "message": "Missing required header 'x-account-id'"
}
```

403 Example `EPDA0152` (Missing required param 'id'):

```json
{
  "code": "EPDA0152",
  "message": "Missing required param 'id'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Service timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout while executing the request"
}
```

504 Example `Provider timeout`:

```json
{
  "code": "EPDG0000",
  "message": "Timeout while executing the request"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 504 | `EPDA0000` | Timeout while executing the request |
| 504 | `EPDG0000` | Timeout while executing the request |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-refund-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500;502;504`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/refunds/{refundId}/close operationId=post-close-dict-refund -->
### `POST /v2/pix/refunds/{refundId}/close` — Close refund

- **operationId:** `post-close-dict-refund`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Refunds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Close a DICT refund request. 
>
> On PSP timeout, a `202 Accepted` response is returned and the process continues asynchronously, eventually emitting an event if it succeeds.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1">Pix reversal (refund) status changed</a> event and a <a href="https://developers.pismo.io/events/docs/pix-financial-reconciliation-1">Pix transaction reconciliation </a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization/tenant ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `x-cid` | header | no | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> | example: "B20220921145635222303062944CA66F" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |
| `refundId` | path | yes | string | Refund ID | example: "4749993777899937" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `RefundCloseRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `refund_analysis_details` | string (schema `RefundAnalysisDetails`) | no | Refund analysis details | example: "Details about the refund analysis." |
| `refund_analysis_result` | string (schema `RefundAnalysis`) | yes | Respondent's refund request analysis result. | enum: ["TOTALLY_ACCEPTED", "PARTIALLY_ACCEPTED", "REJECTED"]; example: "PARTIALLY_ACCEPTED" |
| `refund_rejection_reason` | string (schema `RefundRejectionReason`) | no | Refund rejecton reason. <br><br>**REQUIRED** when `refund_analysis_result` is `REJECTED`.<br> | enum: ["NO_BALANCE", "ACCOUNT_CLOSURE", "INVALID_REQUEST", "OTHER"]; example: "NO_BALANCE" |
| `refund_transaction_id` | string (schema `RefundTransactionID`) | no | Refund transaction ID | example: "E9999901012341234123412345678900" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Refund closed | `application/json`: object (schema `Refund`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 500 | Internal server errpr | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `contested_participant` | string (schema `ContestedParticipant`) | yes | Challenged participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `creation_date_time` | string | yes | Creation date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `last_modified` | string | yes | Last modified date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `refund_amount` | string (schema `RefundAmount`) | yes | Refund amount | example: "20.10" |
| `refund_id` | string | yes | Refund ID | example: "12345645-9ff7-439f-a318-2e6f974707a5" |
| `refund_reason` | string (schema `RefundReason`) | yes | Refund reason. <br><br>`PIX_AUTOMATICO` means a refund was requested due to failed Automatic Pix operation.<br> | enum: ["FRAUD", "OPERATIONAL_FLAW", "PIX_AUTOMATICO", "REFUND_CANCELLED"]; example: "OPERATIONAL_FLAW" |
| `requesting_participant` | string (schema `RequestingParticipant`) | yes | Requesting participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `status` | string (schema `RefundStatus`) | yes | Refund status | enum: ["OPEN", "CLOSED", "CANCELLED"]; example: "CLOSED" |
| `transaction_id` | string (schema `RefundTransactionID`) | yes | Refund transaction ID | example: "E9999901012341234123412345678900" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `infraction_report_id` | string (schema `InfractionReportID`) | no | Infraction report ID (UUID) | format: "uuid"; maxLength: 36; example: "cfdff46e-5d58-45b8-b7aa-591a65f74444" |
| `refund_analysis_details` | string (schema `RefundAnalysisDetails`) | no | Refund analysis details | example: "Details about the refund analysis." |
| `refund_analysis_result` | string (schema `RefundAnalysis`) | no | Respondent's refund request analysis result. | enum: ["TOTALLY_ACCEPTED", "PARTIALLY_ACCEPTED", "REJECTED"]; example: "PARTIALLY_ACCEPTED" |
| `refund_details` | string (schema `RefundDetails`) | no | Details about refund | maxLength: 2000; example: "Details about the refund request" |
| `refund_rejection_reason` | string (schema `RefundRejectionReason`) | no | Refund rejecton reason. <br><br>**REQUIRED** when `refund_analysis_result` is `REJECTED`.<br> | enum: ["NO_BALANCE", "ACCOUNT_CLOSURE", "INVALID_REQUEST", "OTHER"]; example: "NO_BALANCE" |
| `refund_account` | object (schema `RefundAccount`) | no |  |  |
| `refund_transaction_id` | string (schema `RefundTransactionID`) | no | Refund transaction ID | example: "E9999901012341234123412345678900" |
| `funds_recovery_id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `monitor_account` | boolean (schema `MonitorAccount`) | no | Should the account be monitored for suspicious activity? | example: false |
| `effective_refunded_amount` | number (schema `EffectiveRefundedAmount`) | no | Actual amount refunded to the user. | example: 20.1 |

##### Response 202

- Response header `x-cid`: Request tracking identifier. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

202 Example `Request accepted and will processed async`:

```json
{
  "code": "EPDA0174",
  "message": "Refund flow will continue asynchronously"
}
```

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EPDA0009` (Missing required header 'x-tenant'):

```json
{
  "code": "EPDA0009",
  "message": "Missing required header 'x-tenant'"
}
```

403 Example `EPDA0010` (Missing required header 'x-account-id'):

```json
{
  "code": "EPDA0010",
  "message": "Missing required header 'x-account-id'"
}
```

403 Example `EPDA0152` (Missing required param 'id'):

```json
{
  "code": "EPDA0152",
  "message": "Missing required param 'id'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Service timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout while executing the request"
}
```

504 Example `Provider timeout`:

```json
{
  "code": "EPDG0000",
  "message": "Timeout while executing the request"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `EPDA0174` | Refund flow will continue asynchronously |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 504 | `EPDA0000` | Timeout while executing the request |
| 504 | `EPDG0000` | Timeout while executing the request |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-refund-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1 |
| `pix-financial-reconciliation-1` | https://developers.pismo.io/events/docs/pix-financial-reconciliation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;403;404;500;502;504`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Refund -->
### Schema `Refund`

Pointer: `#/components/schemas/Refund`. Type: object (schema `Refund`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `contested_participant` | string (schema `ContestedParticipant`) | yes | Challenged participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `creation_date_time` | string | yes | Creation date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `last_modified` | string | yes | Last modified date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `refund_amount` | string (schema `RefundAmount`) | yes | Refund amount | example: "20.10" |
| `refund_id` | string | yes | Refund ID | example: "12345645-9ff7-439f-a318-2e6f974707a5" |
| `refund_reason` | string (schema `RefundReason`) | yes | Refund reason. <br><br>`PIX_AUTOMATICO` means a refund was requested due to failed Automatic Pix operation.<br> | enum: ["FRAUD", "OPERATIONAL_FLAW", "PIX_AUTOMATICO", "REFUND_CANCELLED"]; example: "OPERATIONAL_FLAW" |
| `requesting_participant` | string (schema `RequestingParticipant`) | yes | Requesting participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `status` | string (schema `RefundStatus`) | yes | Refund status | enum: ["OPEN", "CLOSED", "CANCELLED"]; example: "CLOSED" |
| `transaction_id` | string (schema `RefundTransactionID`) | yes | Refund transaction ID | example: "E9999901012341234123412345678900" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `infraction_report_id` | string (schema `InfractionReportID`) | no | Infraction report ID (UUID) | format: "uuid"; maxLength: 36; example: "cfdff46e-5d58-45b8-b7aa-591a65f74444" |
| `refund_analysis_details` | string (schema `RefundAnalysisDetails`) | no | Refund analysis details | example: "Details about the refund analysis." |
| `refund_analysis_result` | string (schema `RefundAnalysis`) | no | Respondent's refund request analysis result. | enum: ["TOTALLY_ACCEPTED", "PARTIALLY_ACCEPTED", "REJECTED"]; example: "PARTIALLY_ACCEPTED" |
| `refund_details` | string (schema `RefundDetails`) | no | Details about refund | maxLength: 2000; example: "Details about the refund request" |
| `refund_rejection_reason` | string (schema `RefundRejectionReason`) | no | Refund rejecton reason. <br><br>**REQUIRED** when `refund_analysis_result` is `REJECTED`.<br> | enum: ["NO_BALANCE", "ACCOUNT_CLOSURE", "INVALID_REQUEST", "OTHER"]; example: "NO_BALANCE" |
| `refund_account` | object (schema `RefundAccount`) | no |  |  |
| `refund_transaction_id` | string (schema `RefundTransactionID`) | no | Refund transaction ID | example: "E9999901012341234123412345678900" |
| `funds_recovery_id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `monitor_account` | boolean (schema `MonitorAccount`) | no | Should the account be monitored for suspicious activity? | example: false |
| `effective_refunded_amount` | number (schema `EffectiveRefundedAmount`) | no | Actual amount refunded to the user. | example: 20.1 |

<!-- schema: #/components/schemas/message.Message -->
### Schema `message.Message`

Pointer: `#/components/schemas/message.Message`. Type: object (schema `message.Message`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

<!-- schema: #/components/schemas/RefundAccount -->
### Schema `RefundAccount`

Pointer: `#/components/schemas/RefundAccount`. Type: object (schema `RefundAccount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_id_number` | string (schema `TaxIdNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits. | minLength: 11; maxLength: 14; example: "123412341234" |
| `participant` | string (schema `Participant`) | no | Participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "00115678" |
| `branch` | string (schema `Branch`) | no | Bank-assigned branch ID or ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | example: "011" |
| `account_number` | string (schema `AccountNumber`) | no | Account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | no | Account type:  <br>  `CACC` - Checking account<br>  `SVGS` - Savings account<br>  `TRAN` - Transactional account (Brazil only). Also known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking. <br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |

<!-- schema: #/components/schemas/message.DetailMessage -->
### Schema `message.DetailMessage`

Pointer: `#/components/schemas/message.DetailMessage`. Type: object (schema `message.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `message.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `message.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `message.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/message.ExternalMessage -->
### Schema `message.ExternalMessage`

Pointer: `#/components/schemas/message.ExternalMessage`. Type: object (schema `message.ExternalMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Error code | example: "PBE315" |
| `message` | string | yes | Error message | example: "Generic error" |

<!-- schema: #/components/schemas/message.ParameterMessage -->
### Schema `message.ParameterMessage`

Pointer: `#/components/schemas/message.ParameterMessage`. Type: object (schema `message.ParameterMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Parameter in error | example: "query parameter" |
| `message` | string | yes | Error message | example: "Generic error" |

<!-- schema: #/components/schemas/message.PayloadMessage -->
### Schema `message.PayloadMessage`

Pointer: `#/components/schemas/message.PayloadMessage`. Type: object (schema `message.PayloadMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Field in error | example: "Entity.field" |
| `message` | string | yes | Error messsage | example: "Generic error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_Pix_management.yaml` | tag `Refunds`: GET /v2/pix/refunds, POST /v2/pix/refunds, GET /v2/pix/refunds/{refundId}, POST /v2/pix/refunds/{refundId}/cancel, POST /v2/pix/refunds/{refundId}/close | https://github.com/PismoDevEx/pismo-api-specs | `7d7fee078ccf5569…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-epda` — Error codes: EPDA
- `KU-ERR-codes-epdg` — Error codes: EPDG
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-EVT-pix-payments-data-events` — Instant payments - Pix
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
