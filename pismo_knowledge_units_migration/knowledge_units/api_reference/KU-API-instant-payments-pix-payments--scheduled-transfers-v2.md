---
ku_id: KU-API-instant-payments-pix-payments--scheduled-transfers-v2
title: 'API reference: Instant payments - Pix payments — Scheduled transfers V2'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Instant_payments_-_Pix_payments.yaml
  sha256: 034f2ce79f002354b67746b854ac39de6bcc9063b279eec88e9a7207202ad8f7
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
- list-scheduled-transfers
- post-schedule-pix-payment
- advance-pix-out-execution
- get-scheduled-pix-payment
- delete-cancel-pix-out
- get-scheduler-executions
- cancel-pix-out-execution
related_kus:
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-pix
- KU-PAY-pix-and-qr-codes
- KU-PAY-pix-automatic
- KU-PAY-pix-instant-payments
specification_version: '1.0'
---

# API reference: Instant payments - Pix payments — Scheduled transfers V2

**KU ID:** `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 7 operation(s) tagged `Scheduled transfers V2` in `api-specs/Instant_payments_-_Pix_payments.yaml` (“Instant payments - Pix payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /pix/v2/pix/out/scheduler` | `list-scheduled-transfers` | List scheduled Pix transfers | no |
| `POST /pix/v2/pix/out/scheduler` | `post-schedule-pix-payment` | Schedule transfer(s) V2 | no |
| `POST /pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id}/advance` | `advance-pix-out-execution` | Execute scheduled Pix-out transfer in advance | no |
| `GET /pix/v2/pix/out/scheduler/{scheduler_id}` | `get-scheduled-pix-payment` | Get scheduled transfer | no |
| `DELETE /pix/v2/pix/out/scheduler/{scheduler_id}` | `delete-cancel-pix-out` | Cancel scheduled transfer V2 | no |
| `GET /pix/v2/pix/out/scheduler/:scheduler_id/executions` | `get-scheduler-executions` | List Pix scheduler executions | no |
| `DELETE /pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id}` | `cancel-pix-out-execution` | Cancel Pix-out scheduled execution | no |

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=GET path=/pix/v2/pix/out/scheduler operationId=list-scheduled-transfers -->
### `GET /pix/v2/pix/out/scheduler` — List scheduled Pix transfers

- **operationId:** `list-scheduled-transfers`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Scheduled transfers V2`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> List scheduled Pix transfers with filtering options.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `x-cid` | header | no | string | The Correlation ID UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |
| `beginDate` | query | yes | string | Begin date filter. RFC 3339 format. For example: `2023-04-12T23:20:50.52Z`. <br><br>Maximum days allowed between `beginDate` and `endDate` is 30.<br> | example: "2023-04-12T23:20:50.52Z" |
| `endDate` | query | yes | string | End date filter. RFC 3339 format. For example: `2023-04-12T23:20:50.52Z`. <br><br>Maximum days allowed between `beginDate` and `endDate` is 30.<br> | example: "2023-04-12T23:20:50.52Z" |
| `status` | query | no | string | Scheduler status filter | enum: ["ACTIVE", "INACTIVE", "CANCELLED", "COMPLETED"]; example: "ACTIVE" |
| `perPage` | query | yes | string | Per page amount (min=1, max=100). Default is `20`. |  |
| `afterId` | query | no | string | Last returned item ID from response. Use this field to return more results. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `scheduler.SchedulerSearchQueryResponse2`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking ID. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `next_page` | boolean (schema `NextPage`) | no | Are tbere more results? | example: false |
| `last_id` | integer (schema `LastID`) | no | Last returned item ID. Use this ID to get more results.<br> | example: 1602619 |
| `page_size` | number (schema `PageSize`) | no | Maximum elements returned per query. |  |
| `number_elements` | number (schema `NumberElements`) | no | Total items returned in query |  |
| `filters` | array of object (schema `scheduler.ItemQueryFilterResponse`) | no |  |  |
| `sorts` | array of object (schema `scheduler.ItemQuerySortResponse`) | no |  |  |
| `items` | array of object (schema `scheduler.ItemQueryResponse`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=POST path=/pix/v2/pix/out/scheduler operationId=post-schedule-pix-payment -->
### `POST /pix/v2/pix/out/scheduler` — Schedule transfer(s) V2

- **operationId:** `post-schedule-pix-payment`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Scheduled transfers V2`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Schedule a Pix-out transfer or Pix-out recurring transfers. 
>
> This endpoint gives you more scheduling options than the version 1 [Schedule transfer](https://developers.pismo.io/pismo-docs/reference/post-schedule) endpoint. These include additional options (`scheduler_details` object) for recurring transfers.
>
> As with the [Pix-out transfer](ref:post-pix-out-transfer) endpoint, if you are using a key or QR Code, you need to call  <a href="https://developers.pismo.io/pismo-docs/reference/post-v2-pix-keys-validate">Validate DICT key</a> or <a href="https://developers.pismo.io/pismo-docs/reference/post-qr-code">Get and validate QR Code</a> before calling this endpoint. You need to enter the `end_to_end_id` returned from those calls here. If you are not using a key or QR Code, this endpoint generates and returns an `end_to_end_id` value you can use in other endpoints.
>
> The `end_to_end_id` field is a Brazil Central Bank (BCB) requirement to track Pix transactions.  Basically, there are two steps to a Pix transaction: 1. Initialize a transaction and 2. Confirm a transaction. The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information.
>
> This endpoint directly generates an [Instant pay scheduler status changed](https://developers.pismo.io/events/docs/instantpay-scheduler-scheduler-status-change-1) event.
>
> To create a recurring payment, set `type` = `RECURRING` and pass a value for `cycle`. This property has 2 attributes and should be set as shown in the sample table below: 
>
> `cycle.type` | `cycle.count` | New transaction created every:
> ---------- | ----------- | ------------ 
> `DAILY`      | 5           | 5 days
> `WEEKLY`     | 2           | 2 weeks
> `MONTHLY`    | 1           | 1 month
> `MONTHLY`    | 2           | 2 months
> `YEARLY`     | 1           | 1 year
>
> **Notes**
>
> * `WEEKLY` sets the `start_date` weekday. For a scheduler with `start_date` = Thursday, the next transaction is always on a Thursday.
>
> * `MONTHLY / YEARLY` sets the `start_date` day. For a scheduler with `start_date` = `2024-10-12`, the next transaction is always created on day 12 of each cycle count. Now, for days `29`, `30` and `31`, the scheduler uses the previous month's last day when that day doesn't exist in the current month. For example, considering a scheduler starting at `2024-01-30`, the next transaction is created on `2024-02-29`.
>
> **Preset schedules (Beta)**
>
> > ⚠️ The `PRESET` scheduler type is currently in **beta** and may change. Reach out to Pismo before using it in production.
>
> To create a preset payment: set `type` = `PRESET` and provide the full list of executions in `scheduler_details.executions`. 
> Each item has a `due_date` (`YYYY-MM-DD`) and a pre-established `end_to_end_id`. From 1 to 60 executions are supported and are all created upfront in a single operation, so `start_scheduler_date`, `end_scheduler_date` and `cycle` must **NOT** be passed for this type — the schedule window is derived from the executions' `due_date`.
>
> Once created, the executions can be listed through the [List Pix scheduler executions](ref:get-scheduler-executions) endpoint. Because they already exist, the [Get scheduled transfer](ref:get-scheduled-pix-payment) endpoint does not return `executions_preview` for `PRESET` schedulers.
>
> The optional `processing_code` (up to 6 alphanumeric characters) is propagated to the resulting Pix-out transfer.
>
> **Events**
>
> * When the transfer takes place, <a href="https://developers.pismo.io/events/docs/pix-pix-out-1">Pix-out notification received</a> and <a href="https://developers.pismo.io/events/docs/pix-financial-reconciliation-1">Pix reconciliation notification received </a> events are generated.
>
> * Also, when the transfer takes place, a <a href="https://developers.pismo.io/events/docs/pix-pix-in-1">Pix-in notification received</a> event is generated when the funds are deposited in the payee's account, which can be a Pismo account or an external account.
>
> * For all events, the `status` or `result` field indicates operation success or failure.
>
> For more information, refer to the [Pix instant payments](doc:pix-instant-payments) guide.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo accound ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique ID to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |
| `x-cid` | header | no | string | The Correlation ID UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `scheduler.SchedulerRegisterRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | yes | Amount to be transferred. | example: 1050.44 |
| `bank_account` | object (schema `scheduler.BankAccount`) | yes |  |  |
| `initiation_type` | string (schema `InitiationType2`) | yes | Initiation type:  <br><br>  `MANUAL` - Manually initiated. Key is not used - bank account, bank code, document number, and branch are used for identification.<br><br>  `DICT` - Diretorio de Identificadores de Contas de Transação (Transaction accounts ID directory). Pix/DICT key is used for identification.<br><br>  `DYNAMIC_QRCODE` - The amount and other details for a dynamic code are included automatically. <br>  <br> | enum: ["MANUAL", "DICT", "STATIC_QRCODE", "DYNAMIC_QRCODE"]; maxLength: 20; example: "DICT" |
| `ispb` | string (schema `ISPB`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |
| `is_device_registered` | boolean (schema `IsDeviceRegistered`) | no | Is device registered to do a Pix-out transfer? Default is `true`. | example: true |
| `payee` | object (schema `scheduler.Payee`) | yes |  |  |
| `qr_code_additional_information` | array of object (schema `QRcodeAddInfo`) | no | Additional QR Code information. |  |
| `qr_code_additional_information[].name` | string | no | QR Code name | example: "Discount" |
| `qr_code_additional_information[].value` | string | no | QR Code value | example: "Paying until the 5th, there will be a 10% discount" |
| `scheduler_details` | object (schema `scheduler.SchedulerDetailsRequest`) | yes | Scheduler details accepted when creating a scheduler. |  |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `remittance_information` | string (schema `RemittanceInformation`) | no | Remittance information. Information from payee when transaction is a static QR Code.<br> | maxLength: 140 |
| `transaction_identification` | string | no | Transaction ID. <br><br>**Notes:**<br>  * **REQUIRED** if `initiation_type` = `DYNAMIC_QR_CODE`. <br><br>  * Do **NOT** pass if `initiation_type` = `MANUAL` or `DICT`. <br><br>  * If `STATIC_QR_CODE` contains `transaction_identification`, it is **REQUIRED** to pass it.<br> | example: "1a84daf6-a61b-4aba-919a-a9943db7102e" |
| `flex_controls` | object (schema `FlexControls`) | no | [Flex control ID](https://developers.pismo.io/pismo-docs/docs/flex-controls#pix-and-accounts) and schedule limit checking before creating a new scheduler.<br> |  |
| `taxes` | object (schema `Taxes`) | no | Only available in the test environment for direct participants. Tax information related to the transaction.<br> |  |
| `processing_code` | string | no | Optional processing code propagated to the resulting Pix-out transfer. Up to 6 alphanumeric characters.<br><br>For more information, refer to the [Processing codes](doc:processing-codes-and-transaction-types) guide.<br> | maxLength: 6; example: "500001" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `scheduler.SchedulerRegisterResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too many requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway timeout | `application/json`: object (schema `customer.Error`) |

##### Response 201

- Response header `x-cid`: Request tracking ID. (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `scheduler_id` | string (schema `SchedulerID`) | no | Scheduled PIX transaction ID | example: "7b29a055-00e1-41e5-b880-aebe517b3bf6" |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 409

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)
##### Response 502

- Response header `x-cid`: Request tracking ID. (string)
##### Response 504

- Response header `x-cid`: Request tracking ID. (string)

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `instantpay-scheduler-scheduler-status-change-1` | https://developers.pismo.io/events/docs/instantpay-scheduler-scheduler-status-change-1 |
| `pix-financial-reconciliation-1` | https://developers.pismo.io/events/docs/pix-financial-reconciliation-1 |
| `pix-pix-in-1` | https://developers.pismo.io/events/docs/pix-pix-in-1 |
| `pix-pix-out-1` | https://developers.pismo.io/events/docs/pix-pix-out-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;404;409;429;500;502;504`, has examples `False`, emits events `4`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-and-qr-codes`, `KU-PAY-pix-automatic`, `KU-PAY-pix-instant-payments`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=POST path=/pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id}/advance operationId=advance-pix-out-execution -->
### `POST /pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id}/advance` — Execute scheduled Pix-out transfer in advance

- **operationId:** `advance-pix-out-execution`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Scheduled transfers V2`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Perform a scheduled Pix-out transfer execution in advance. A scheduled transfer can have many executions if, for example, it is recurring. 
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/instantpay-scheduler-execution-status-change-1">Instant pay execution status changed</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `scheduler_id` | path | yes | string | Schedule ID | maxLength: 36; example: "8675309" |
| `execution_id` | path | yes | string | Sequential number incremented for each scheduled transfer execution. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Success | `application/json`: string |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 202

- Response header `x-cid`: Request tracking identifier. (string)
**202 `application/json` body fields:**

_No fields declared in the schema._

##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `instantpay-scheduler-execution-status-change-1` | https://developers.pismo.io/events/docs/instantpay-scheduler-execution-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=GET path=/pix/v2/pix/out/scheduler/{scheduler_id} operationId=get-scheduled-pix-payment -->
### `GET /pix/v2/pix/out/scheduler/{scheduler_id}` — Get scheduled transfer

- **operationId:** `get-scheduled-pix-payment`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Scheduled transfers V2`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get a scheduled Pix payment.
>
> For `ONCE` and `RECURRING` schedulers, set `showPreview=true` to include `executions_preview` (a preview of upcoming executions that will be created in the future). For `PRESET` schedulers, `executions_preview` is never returned because all executions are created upfront — retrieve them through the [List Pix scheduler executions](ref:get-scheduler-executions) endpoint instead.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo accound ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `scheduler_id` | path | yes | string | Schedule ID | maxLength: 36; example: "8675309" |
| `x-cid` | header | no | string | The Correlation ID UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |
| `showPreview` | query | no | boolean | Should a preview of upcoming executions be presented? Default is `false` (no execution previews returned). Has no effect for `PRESET` schedulers, whose executions are all created upfront and available through the [List Pix scheduler executions](ref:get-scheduler-executions) endpoint.<br> | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `scheduler.SchedulerSearchResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking ID. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `scheduler_id` | string (schema `SchedulerID`) | yes | Scheduled PIX transaction ID | example: "7b29a055-00e1-41e5-b880-aebe517b3bf6" |
| `scheduler_creation_datetime` | string | no | Datetime when scheduled transfer created. RFC 3339 format. | example: "2021-10-11T00:00:00.000Z" |
| `scheduler_lastupdate_datetime` | string | no | Datetime when scheduled transfer last updated. RFC 3339 format. | example: "2021-10-11T00:00:00.000Z" |
| `scheduler_details` | object (schema `scheduler.SchedulerDetails`) | no |  |  |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `status` | string (schema `SchedulerStatus`) | no | Scheduler status | enum: ["DELIVERED", "PROCESSING", "CANCELLED", "SUCCESS", "FAIL", "PENDING"]; example: "DELIVERED" |
| `is_device_registered` | boolean (schema `IsDeviceRegistered`) | no | Is device registered to do a Pix-out transfer? Default is `true`. | example: true |
| `payee` | object (schema `scheduler.PayeeResponse`) | no |  |  |
| `payer` | object (schema `scheduler.PayerResponse`) | no |  |  |
| `next_execution` | object (schema `scheduler.Execution`) | no |  |  |
| `executions_preview` | object (schema `scheduler.ExecutionsPreview`) | no | Preview of upcoming executions that will be created in the future. Present only when `showPreview=true` and the scheduler `type` is `ONCE` or `RECURRING`. Not returned for `PRESET` schedulers, whose executions are all created upfront and available through the [List Pix scheduler executions](ref:get-scheduler-executions) endpoint.<br> |  |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=DELETE path=/pix/v2/pix/out/scheduler/{scheduler_id} operationId=delete-cancel-pix-out -->
### `DELETE /pix/v2/pix/out/scheduler/{scheduler_id}` — Cancel scheduled transfer V2

- **operationId:** `delete-cancel-pix-out`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Scheduled transfers V2`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Cancel scheduled Pix transfer.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/instantpay-scheduler-scheduler-status-change-1">Instant pay scheduler status change</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `scheduler_id` | path | yes | string | Schedule ID | maxLength: 36; example: "8675309" |
| `x-cid` | header | no | string | The Correlation ID UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 |  |  |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 204

- Response header `x-cid`: Request tracking ID. (string)
##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `instantpay-scheduler-scheduler-status-change-1` | https://developers.pismo.io/events/docs/instantpay-scheduler-scheduler-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=GET path=/pix/v2/pix/out/scheduler/:scheduler_id/executions operationId=get-scheduler-executions -->
### `GET /pix/v2/pix/out/scheduler/:scheduler_id/executions` — List Pix scheduler executions

- **operationId:** `get-scheduler-executions`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Scheduled transfers V2`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> List Pix payment scheduler executions - scheduled Pix transfers that have run to completion. A scheduled transfer can have many executions if, for example, it is recurring.
>
> For `PRESET` schedulers, all executions are created upfront when the scheduler is registered, so this endpoint returns the complete set of executions provided in `scheduler_details.executions`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `x-cid` | header | no | string | The Correlation ID UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |
| `beginDate` | query | no | string | Begin creation date for scheduler executions filter. Format = YYYY-MM-DD.<br> | example: "2023-04-12" |
| `endDate` | query | no | string | End creation date for scheduler executions filter. Format = YYYY-MM-DD.<br> | example: "2023-04-12" |
| `status` | query | no | string | Execution status filter | enum: ["PENDING", "SUCCESS", "FAIL", "CANCELLED", "PROCESSING", "DELIVERED"]; example: "PENDING" |
| `perPage` | query | yes | string | Per page amount (min=1, max=100). Default is `20`. |  |
| `afterId` | query | no | string | Last returned item ID from response. Use this field to return more results. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `scheduler.ExecutionsListResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking ID. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `last_id` | integer (schema `LastID`) | no | Last returned item ID. Use this ID to get more results.<br> | example: 1602619 |
| `next_page` | boolean (schema `NextPage`) | no | Are tbere more results? | example: false |
| `number_elements` | number (schema `NumberElements`) | no | Total items returned in query |  |
| `page_size` | number (schema `PageSize`) | no | Maximum elements returned per query. |  |
| `items` | array of object (schema `scheduler.Executiona`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=DELETE path=/pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id} operationId=cancel-pix-out-execution -->
### `DELETE /pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id}` — Cancel Pix-out scheduled execution

- **operationId:** `cancel-pix-out-execution`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Scheduled transfers V2`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Perform a Pix-out execution cancel. A scheduled transfer can have many executions if, for example, it is recurring. 
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/instantpay-scheduler-execution-status-change-1">Instant pay execution status changed</a> event.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo accound ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `scheduler_id` | path | yes | string | Schedule ID | maxLength: 36; example: "8675309" |
| `execution_id` | path | yes | string | Sequential number incremented for each scheduled transfer execution. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Success | `application/json`: string |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 204

- Response header `x-cid`: Request tracking identifier. (string)
**204 `application/json` body fields:**

_No fields declared in the schema._

##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `instantpay-scheduler-execution-status-change-1` | https://developers.pismo.io/events/docs/instantpay-scheduler-execution-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/scheduler.ItemQueryFilterResponse -->
### Schema `scheduler.ItemQueryFilterResponse`

Pointer: `#/components/schemas/scheduler.ItemQueryFilterResponse`. Type: object (schema `scheduler.ItemQueryFilterResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `label` | string | no | Field name | example: "status" |
| `value` | string | no | Field's value | example: "ACTIVE" |
| `operator` | string | no | Operator type | example: "EQUAL" |

<!-- schema: #/components/schemas/scheduler.ItemQuerySortResponse -->
### Schema `scheduler.ItemQuerySortResponse`

Pointer: `#/components/schemas/scheduler.ItemQuerySortResponse`. Type: object (schema `scheduler.ItemQuerySortResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | no | Field name | example: "status" |
| `order` | string | no | Order | enum: ["ASC", "DESC"]; example: "ASC" |

<!-- schema: #/components/schemas/scheduler.ItemQueryResponse -->
### Schema `scheduler.ItemQueryResponse`

Pointer: `#/components/schemas/scheduler.ItemQueryResponse`. Type: object (schema `scheduler.ItemQueryResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `day_type` | string | yes | Day type | enum: ["BUSINESS", "CALENDAR"]; example: "CALENDAR" |
| `cycle` | object (schema `SchedulerCycle`) | no | Cycle property present for scheduler `type` = `RECURRING`. Defaults to `MONTHLY`.<br> |  |
| `is_device_registered` | boolean (schema `IsDeviceRegistered`) | no | Is device registered to do a Pix-out transfer? Default is `true`. | example: true |
| `end_date` | string | yes | End date, format = YYYY-MM-DD | example: "2025-11-14" |
| `start_date` | string | yes | Start date, format = YYYY-MM-DD | example: "2024-11-14" |
| `scheduler_id` | string (schema `SchedulerID`) | yes | Scheduled PIX transaction ID | example: "7b29a055-00e1-41e5-b880-aebe517b3bf6" |
| `status` | string (schema `SchedulerStatus2`) | yes | Scheduler status | enum: ["ACTIVE", "INACTIVE", "CANCELLED", "COMPLETED"]; example: "COMPLETED" |
| `type` | string (schema `ProcessingType`) | yes | Scheduler processing type:<br><br>* `ONCE` - A single scheduled transfer executed on `start_scheduler_date`.<br><br>* `RECURRING` - Transfers created over time according to `cycle`, from `start_scheduler_date` until `end_scheduler_date`.<br><br>* `PRESET` - **(Beta)** The caller pre-establishes all executions in the `scheduler_details.executions` list. `start_scheduler_date`/`end_scheduler_date` and `cycle` are **NOT** used - the schedule window is derived from the executions' `due_date`.<br> | enum: ["ONCE", "RECURRING", "PRESET"]; example: "RECURRING" |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `description` | string | no | Item description | example: "Weekly payment" |
| `continue_even_failed` | boolean | no | Continue on failure? | default: false; example: true |
| `execution_hour` | string | no | Scheduled execution hour, format = HH:MM:SS | example: "17:56:00" |
| `retry_hour` | string | no | Scheduled retry hour, format = HH:MM:SS | example: "20:00:00" |
| `check_interval` | string | no | Check scheduler interval in minutes. | example: "10" |
| `created_at` | string (schema `scheduler.CreatedAt`) | no | Scheduled item creation time, RFC 3339 format | example: "2024-11-14T17:54:40Z" |
| `updated_at` | string (schema `UpdatedAt`) | no | Scheduled item last updated time, RFC 3339 format | example: "2024-11-14T17:54:40Z" |

<!-- schema: #/components/schemas/customer.Error -->
### Schema `customer.Error`

Pointer: `#/components/schemas/customer.Error`. Type: object (schema `customer.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error's code. | example: "EPT0001" |
| `details` | object (schema `customer.DetailMessage`) | no |  |  |
| `message` | string | no | Error's message. | example: "User not found" |

<!-- schema: #/components/schemas/scheduler.BankAccount -->
### Schema `scheduler.BankAccount`

Pointer: `#/components/schemas/scheduler.BankAccount`. Type: object (schema `scheduler.BankAccount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_type` | string (schema `AccountType`) | yes | Account type:  <br /><br>  `CACC` - Checking/current account.  Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |

<!-- schema: #/components/schemas/scheduler.Payee -->
### Schema `scheduler.Payee`

Pointer: `#/components/schemas/scheduler.Payee`. Type: object (schema `scheduler.Payee`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | yes | Account type:  <br /><br>  `CACC` - Checking/current account.  Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `bank` | string (schema `Bank`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID for the receiving bank, an 8-digit value. | maxLength: 8; example: "237" |
| `branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `beneficiary_id` | string (schema `BeneficiaryID`) | no | Beneficiary ID. This ID created when the [Register beneficiary](ref:post-intl-bank-accounts-v1-bank-accounts-beneficiaries) endpoint is called.<br> | maxLength: 36; example: "97c96d96-9b87-404b-88e5-287f2b0e6e0a" |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |
| `key` | string (schema `Key`) | no | Pix key value. | maxLength: 77; example: "email@email.com" |
| `type` | string (schema `PersonType`) | no | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights.<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |

<!-- schema: #/components/schemas/scheduler.SchedulerDetailsRequest -->
### Schema `scheduler.SchedulerDetailsRequest`

Pointer: `#/components/schemas/scheduler.SchedulerDetailsRequest`. Type: object (schema `scheduler.SchedulerDetailsRequest`).

> Scheduler details accepted when creating a scheduler.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `ProcessingType`) | yes | Scheduler processing type:<br><br>* `ONCE` - A single scheduled transfer executed on `start_scheduler_date`.<br><br>* `RECURRING` - Transfers created over time according to `cycle`, from `start_scheduler_date` until `end_scheduler_date`.<br><br>* `PRESET` - **(Beta)** The caller pre-establishes all executions in the `scheduler_details.executions` list. `start_scheduler_date`/`end_scheduler_date` and `cycle` are **NOT** used - the schedule window is derived from the executions' `due_date`.<br> | enum: ["ONCE", "RECURRING", "PRESET"]; example: "RECURRING" |
| `description` | string | no | Schedule description | maxLength: 200; example: "Pay at end of month" |
| `start_scheduler_date` | string (schema `SchedulerDateStart`) | no | Date to start the scheduled payment. <br><br>Format = YYYY-MM-DD <br><br>Transfers are made at midnight on this date and, if recurring, every month until `end_scheduler_date`.<br><br>**REQUIRED** for `type` = `ONCE` or `RECURRING`. <br><br>Must **NOT** be passed for `type` = `PRESET`. The schedule start is derived from the earliest execution `due_date`.<br> | example: "2024-06-10" |
| `end_scheduler_date` | string (schema `SchedulerDateEnd`) | no | Date to stop the scheduled payment (maximum = 1 year). <br><br>Format = YYYY-MM-DD. <br><br>**REQUIRED** for `type` = `ONCE` or `RECURRING`. <br><br>Must **NOT** be passed for `type` = `PRESET`. The schedule end is derived from the latest execution `due_date`.<br> | example: "2024-06-10" |
| `cycle` | object (schema `SchedulerCycle`) | no | Cycle property present for scheduler `type` = `RECURRING`. Defaults to `MONTHLY`.<br> |  |
| `executions` | array of object (schema `scheduler.PresetExecution`) | no | List of pre-established executions. <br><br>**REQUIRED** if `type` = `PRESET` (1 to 60 items).<br><br>Must **NOT** be passed for `type` = `ONCE` or `RECURRING`. <br><br>Each execution is created up front and can be retrieved through the [List Pix scheduler executions](ref:get-scheduler-executions) endpoint.<br><br> This field is input-only: it is passed when creating a scheduler. The [Get scheduled transfer](ref:get-scheduled-pix-payment) endpoint does not return this field.<br> | minItems: 1; maxItems: 60 |

<!-- schema: #/components/schemas/FlexControls -->
### Schema `FlexControls`

Pointer: `#/components/schemas/FlexControls`. Type: object (schema `FlexControls`).

> [Flex control ID](https://developers.pismo.io/pismo-docs/docs/flex-controls#pix-and-accounts) and schedule limit checking before creating a new scheduler.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pix_limit_id` | string | yes | Rule ID for scheduled Pix limit | example: "279207b0-d553-424e-a454-8d704cca3702" |

<!-- schema: #/components/schemas/Taxes -->
### Schema `Taxes`

Pointer: `#/components/schemas/Taxes`. Type: object (schema `Taxes`).

> Only available in the test environment for direct participants. Tax information related to the transaction.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_identifier` | string (schema `TaxIdentifier`) | no | Tax identifier, referring to the NFe, NFSe or aggregating tax document. <br><br>In Brazil, NF-e and NFS-e are the two primary types of mandatory electronic invoices (Notas Fiscais) used for tax compliance.<br><br> * NF-e (Nota Fiscal Eletrônica): Used for the sale and movement of physical goods or products. It is regulated at the state level by SEFAZ (SEFAZ (Secretaria da Fazenda) is the State Department of Finance in Brazil.) and travels with the goods.<br><br> * NFS-e (Nota Fiscal de Serviços Eletrônica): Used for the provision of services (e.g., consulting, repairs, digital subscriptions). It is regulated by individual city governments.<br><br>The value entered must correspond to the tax document used for calculating the IBS and CBS taxes associated with the transaction.<br> | maxLength: 50; example: "IS0435879820240605bcdb1fhn43a" |
| `records` | array of object (schema `Records`) | no | Tax record types information. You must pass, at a minimum, 2 objects - at least one with `CBS` tax type and at least one with `IBS` tax type.<br> |  |

<!-- schema: #/components/schemas/scheduler.SchedulerDetails -->
### Schema `scheduler.SchedulerDetails`

Pointer: `#/components/schemas/scheduler.SchedulerDetails`. Type: object (schema `scheduler.SchedulerDetails`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `ProcessingType`) | yes | Scheduler processing type:<br><br>* `ONCE` - A single scheduled transfer executed on `start_scheduler_date`.<br><br>* `RECURRING` - Transfers created over time according to `cycle`, from `start_scheduler_date` until `end_scheduler_date`.<br><br>* `PRESET` - **(Beta)** The caller pre-establishes all executions in the `scheduler_details.executions` list. `start_scheduler_date`/`end_scheduler_date` and `cycle` are **NOT** used - the schedule window is derived from the executions' `due_date`.<br> | enum: ["ONCE", "RECURRING", "PRESET"]; example: "RECURRING" |
| `description` | string | no | Schedule description | maxLength: 200; example: "Pay at end of month" |
| `start_scheduler_date` | string (schema `SchedulerDateStart`) | no | Date to start the scheduled payment. <br><br>Format = YYYY-MM-DD <br><br>Transfers are made at midnight on this date and, if recurring, every month until `end_scheduler_date`.<br><br>**REQUIRED** for `type` = `ONCE` or `RECURRING`. <br><br>Must **NOT** be passed for `type` = `PRESET`. The schedule start is derived from the earliest execution `due_date`.<br> | example: "2024-06-10" |
| `end_scheduler_date` | string (schema `SchedulerDateEnd`) | no | Date to stop the scheduled payment (maximum = 1 year). <br><br>Format = YYYY-MM-DD. <br><br>**REQUIRED** for `type` = `ONCE` or `RECURRING`. <br><br>Must **NOT** be passed for `type` = `PRESET`. The schedule end is derived from the latest execution `due_date`.<br> | example: "2024-06-10" |
| `cycle` | object (schema `SchedulerCycle`) | no | Cycle property present for scheduler `type` = `RECURRING`. Defaults to `MONTHLY`.<br> |  |

<!-- schema: #/components/schemas/scheduler.PayeeResponse -->
### Schema `scheduler.PayeeResponse`

Pointer: `#/components/schemas/scheduler.PayeeResponse`. Type: object (schema `scheduler.PayeeResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `Name`) | no | Name | maxLength: 200; example: "Walter Melon" |
| `document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `ispb` | string (schema `ISPB`) | no | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |

<!-- schema: #/components/schemas/scheduler.PayerResponse -->
### Schema `scheduler.PayerResponse`

Pointer: `#/components/schemas/scheduler.PayerResponse`. Type: object (schema `scheduler.PayerResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `Name`) | no | Name | maxLength: 200; example: "Walter Melon" |
| `document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `ispb` | string (schema `ISPB`) | no | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |

<!-- schema: #/components/schemas/scheduler.Execution -->
### Schema `scheduler.Execution`

Pointer: `#/components/schemas/scheduler.Execution`. Type: object (schema `scheduler.Execution`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `check_date_time` | string | no | Datetime check_interval processed. RFC 3339 format. | example: "2021-10-11T00:00:00.000Z" |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `executed_at` | string (schema `scheduler.ExecutedAt`) | no | Scheduled item execution time, RFC 3339 format | example: "2024-11-14T17:54:40Z" |
| `execution_date_time` | string | no | When the scheduler task was scheduled to run. RFC 3339 format. | example: "2021-10-11T00:00:00.000Z" |
| `execution_id` | integer (schema `ExecutionID`) | no | Sequential number incremented for each scheduled transfer execution. | example: 2 |
| `retry_date_time` | string | no | Datetime to retry transfer after error. RFC 3339 format. | example: "2021-10-11T00:00:00.000Z" |
| `status` | string (schema `SchedulerStatus`) | no | Scheduler status | enum: ["DELIVERED", "PROCESSING", "CANCELLED", "SUCCESS", "FAIL", "PENDING"]; example: "DELIVERED" |

<!-- schema: #/components/schemas/scheduler.ExecutionsPreview -->
### Schema `scheduler.ExecutionsPreview`

Pointer: `#/components/schemas/scheduler.ExecutionsPreview`. Type: object (schema `scheduler.ExecutionsPreview`).

> Preview of upcoming executions that will be created in the future. Present only when `showPreview=true` and the scheduler `type` is `ONCE` or `RECURRING`. Not returned for `PRESET` schedulers, whose executions are all created upfront and available through the [List Pix scheduler executions](ref:get-scheduler-executions) endpoint.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_more` | boolean | no | Are there more than 50 upcoming executions? | example: false |
| `items` | array of object (schema `scheduler.PreviewExecution`) | no | List of upcoming executions preview, limited to 50 items. | maxItems: 50 |

<!-- schema: #/components/schemas/scheduler.Executiona -->
### Schema `scheduler.Executiona`

Pointer: `#/components/schemas/scheduler.Executiona`. Type: object (schema `scheduler.Executiona`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `execution_id` | integer (schema `ExecutionID`) | yes | Sequential number incremented for each scheduled transfer execution. | example: 2 |
| `execution_datetime` | string | yes | When the scheduler task was scheduled to run. RFC 3339 format. | example: "2021-10-11T00:00:00.000Z" |
| `status` | string (schema `ExecutionStatus`) | yes | Execution status | enum: ["PENDING", "SUCCESS", "FAIL", "CANCELLED", "PROCESSING", "DELIVERED"]; example: "PENDING" |
| `check_datetime` | string | no | Datetime check_interval processed. RFC 3339 format. | example: "2021-10-11T00:00:00.000Z" |
| `created_at` | string (schema `scheduler.CreatedAt`) | no | Scheduled item creation time, RFC 3339 format | example: "2024-11-14T17:54:40Z" |
| `executed_at` | string (schema `scheduler.ExecutedAt`) | no | Scheduled item execution time, RFC 3339 format | example: "2024-11-14T17:54:40Z" |
| `retry_datetime` | string | no | Retry datetime, RFC3339 format | example: "2021-10-11T00:00:00.000Z" |
| `updated_at` | string (schema `UpdatedAt`) | no | Scheduled item last updated time, RFC 3339 format | example: "2024-11-14T17:54:40Z" |
| `error` | object (schema `scheduler.ExecutionError`) | no |  |  |

<!-- schema: #/components/schemas/SchedulerCycle -->
### Schema `SchedulerCycle`

Pointer: `#/components/schemas/SchedulerCycle`. Type: object (schema `SchedulerCycle`).

> Cycle property present for scheduler `type` = `RECURRING`. Defaults to `MONTHLY`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | no | Recurring cycle type | enum: ["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]; example: "MONTHLY" |
| `count` | integer | no | Cycle count for generating new transactions. Each daily, weekly, monthly, or yearly occurrence is counted as one cycle. | example: 1 |

<!-- schema: #/components/schemas/customer.DetailMessage -->
### Schema `customer.DetailMessage`

Pointer: `#/components/schemas/customer.DetailMessage`. Type: object (schema `customer.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `customer.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `customer.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `customer.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/scheduler.PresetExecution -->
### Schema `scheduler.PresetExecution`

Pointer: `#/components/schemas/scheduler.PresetExecution`. Type: object (schema `scheduler.PresetExecution`).

> A single pre-established execution for a `PRESET` scheduler.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `due_date` | string | yes | Date on which the execution runs. Format = YYYY-MM-DD. | example: "2026-10-15" |
| `end_to_end_id` | string (schema `EndToEndID`) | yes | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |

<!-- schema: #/components/schemas/Records -->
### Schema `Records`

Pointer: `#/components/schemas/Records`. Type: object (schema `Records`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_type` | string (schema `TaxType`) | no | Tax type:<br><br> `IBS` = Goods and services tax. A state and municipal tax that unifies and replaces the main subnational consumption taxes (state ICMS and municipal ISS).<br><br>`CBS` = Contribution on goods and services. A federal tax that consolidates and replaces previous federal social contributions and taxes (PIS, Cofins, and IPI).<br> | enum: ["CBS", "IBS"]; example: "IBS" |
| `amount` | number (schema `TaxAmount`) | no | Tax amount. Must be greater than zero. | example: 1050.44 |

<!-- schema: #/components/schemas/scheduler.PreviewExecution -->
### Schema `scheduler.PreviewExecution`

Pointer: `#/components/schemas/scheduler.PreviewExecution`. Type: object (schema `scheduler.PreviewExecution`).

> A single upcoming execution in the preview.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `execution_id` | integer (schema `ExecutionID`) | no | Sequential number incremented for each scheduled transfer execution. | example: 2 |
| `date` | string | no | Scheduled date for the upcoming execution. RFC 3339 format. | example: "2025-01-15T00:00:00.000Z" |

<!-- schema: #/components/schemas/scheduler.ExecutionError -->
### Schema `scheduler.ExecutionError`

Pointer: `#/components/schemas/scheduler.ExecutionError`. Type: object (schema `scheduler.ExecutionError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code |  |
| `message` | string | no | Error message |  |

<!-- schema: #/components/schemas/customer.ExternalMessage -->
### Schema `customer.ExternalMessage`

Pointer: `#/components/schemas/customer.ExternalMessage`. Type: object (schema `customer.ExternalMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Error code. | example: "PBE315" |
| `message` | string | yes | Error message. | example: "Generic error" |

<!-- schema: #/components/schemas/customer.ParameterMessage -->
### Schema `customer.ParameterMessage`

Pointer: `#/components/schemas/customer.ParameterMessage`. Type: object (schema `customer.ParameterMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Parameter field | example: "Query parameter" |
| `message` | string | yes | Message about parameter | example: "Generic error" |

<!-- schema: #/components/schemas/customer.PayloadMessage -->
### Schema `customer.PayloadMessage`

Pointer: `#/components/schemas/customer.PayloadMessage`. Type: object (schema `customer.PayloadMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Payload parameter | example: "Entity.field" |
| `message` | string | yes | Message about error | example: "Generic error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_Pix_payments.yaml` | tag `Scheduled transfers V2`: GET /pix/v2/pix/out/scheduler, POST /pix/v2/pix/out/scheduler, POST /pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id}/advance, GET /pix/v2/pix/out/scheduler/{scheduler_id}, DELETE /pix/v2/pix/out/scheduler/{scheduler_id}, GET /pix/v2/pix/out/scheduler/:scheduler_id/executions, DELETE /pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id} | https://github.com/PismoDevEx/pismo-api-specs | `034f2ce79f002354…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-PAY-pix-and-qr-codes` — Pix and QR Codes
- `KU-PAY-pix-automatic` — Pix Automatic
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
