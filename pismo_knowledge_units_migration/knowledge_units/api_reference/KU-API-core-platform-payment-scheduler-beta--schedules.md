---
ku_id: KU-API-core-platform-payment-scheduler-beta--schedules
title: 'API reference: Core platform - Payment scheduler — Schedules'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Payment_scheduler_beta.yaml
  sha256: dbe6a1a7f7485280f004fa281d79f8fe07a63968944e323007c55bbf7f8373f0
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
- post-v1-create-single-schedule
- post-v1-create-bulk-single-schedules
- post-v1-create-transfer-schedules
- post-v1-create-bulk-transfer-schedules
- post-pre-schedules
- post-bulk-pre-schedules
- post-execute-pre-schedule
- get-all-schedules
- get-schedule-executions
- get-schedule
- delete-schedule
- patch-schedule
related_kus:
- KU-EVT-catalogue-scheduler
- KU-EVT-payments-data-events
- KU-PAY-payment-scheduler
specification_version: 1.0.0
---

# API reference: Core platform - Payment scheduler — Schedules

**KU ID:** `KU-API-core-platform-payment-scheduler-beta--schedules` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 12 operation(s) tagged `Schedules` in `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (“Core platform - Payment scheduler”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to enable scheduler creation and processing

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/schedules` | `post-v1-create-single-schedule` | Create single schedule | no |
| `POST /v1/schedules/bulk` | `post-v1-create-bulk-single-schedules` | Create bulk single schedules | no |
| `POST /v1/transfers` | `post-v1-create-transfer-schedules` | Create transfer schedule | no |
| `POST /v1/transfers/bulk` | `post-v1-create-bulk-transfer-schedules` | Create bulk transfer schedules | no |
| `POST /v1/pre-schedules` | `post-pre-schedules` | Create pre-schedule | no |
| `POST /v1/pre-schedules/bulk` | `post-bulk-pre-schedules` | Create bulk pre-schedules | no |
| `POST /v1/accounts/{accountId}/pre-schedules/{scheduleId}/execute` | `post-execute-pre-schedule` | Execute pre-schedule | no |
| `GET /v1/accounts/{accountId}/schedules` | `get-all-schedules` | List account schedules | no |
| `GET /v1/accounts/{accountId}/schedules/{scheduleId}/executions` | `get-schedule-executions` | List schedule executions | no |
| `GET /v1/accounts/{accountId}/schedules/{scheduleId}` | `get-schedule` | Get schedule | no |
| `DELETE /v1/accounts/{accountId}/schedules/{scheduleId}` | `delete-schedule` | Cancel schedule | no |
| `PATCH /v1/accounts/{accountId}/schedules/{scheduleId}` | `patch-schedule` | Update schedule | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=POST path=/v1/schedules operationId=post-v1-create-single-schedule -->
### `POST /v1/schedules` — Create single schedule

- **operationId:** `post-v1-create-single-schedule`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a single schedule, which executes a simple payment operation on a single account. Configure the schedule's execution frequency and other details in the `schedule_details` field.
>
> In some cases, due to errors and retries, execution of the scheduled transaction might occur on the following day instead of the originally scheduled date. To address this, the `allow_execution_after_day_change` flag in `schedule_details` enables you to pre-authorize execution of the scheduled transaction on the next day. This flag must be set to `true` for schedules that are set to be executed at the end of the day (after 11:30pm UTC). If the schedule is not executed on the expected day for any reason, and this field isn't set to `true`, the schedule is not executed and is marked as `EXECUTED_WITH_ERROR_NEXT_DAY_NOT_ALLOWED`.
>
> This endpoint generates the [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event with the `status` field set to `CREATED`.
>
> Each execution of the schedule also generates the [Scheduled payment executed](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1) event.
>
> Refer to the [Payment scheduler](doc:payment-scheduler) guide for more information.

#### Request body

Required: yes

> Request processing body

**Content type `application/json`** — schema: object (schema `SingleScheduleRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | yes | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |
| `schedule_details` | object (schema `SingleScheduleDetails`) | yes | Single schedule details |  |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 8675309 |
| `amount` | number (schema `Amount`) | yes | Credit or debit amount | format: "float"; example: 100.23 |
| `currency_code` | string (schema `CurrencyCode`) | yes | Three-letter currency code of the operation in ISO 4217. | example: "BRL" |
| `processing_code` | string (schema `ProcessingCode`) | yes | Processing code that identifies the credit or debit operation | example: "219803" |
| `description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `restrictions` | object (schema `Restrictions`) | no | Restrictions applied to the schedule |  |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Request was processed successfully, existing schedule with the corresponding `schedule_id` returned. | `application/json`: object (schema `SingleScheduleResponse`) |
| 201 | Request was processed successfully, new schedule created. | `application/json`: object (schema `SingleScheduleResponse`) |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | no | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | no | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `scheduler-payments-scheduled-payments-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1 |
| `scheduler-payments-scheduled-payments-execution-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;201;400;403;500`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-payments-data-events`, `KU-PAY-payment-scheduler`.

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=POST path=/v1/schedules/bulk operationId=post-v1-create-bulk-single-schedules -->
### `POST /v1/schedules/bulk` — Create bulk single schedules

- **operationId:** `post-v1-create-bulk-single-schedules`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create multiple single schedules in a single request. This request triggers an asynchronous process to create the schedules. Once processing is complete, the [Bulk single schedules created](https://developers.pismo.io/events/docs/scheduler-payments-bulk-scheduled-payments-1) event is sent with the result of the operation.
>
> This endpoint accepts a `defaults` object that can be used to set common values for all schedules in the request. Individual schedules can override any default value by specifying the field in their own definition.
>
> In some cases, due to errors and retries, execution of the scheduled transaction might occur on the following day instead of the originally scheduled date. To address this, the `allow_execution_after_day_change` flag in `schedule_details` enables you to pre-authorize execution of the scheduled transaction on the next day. This flag must be set to `true` for schedules that are set to be executed at the end of the day (after 11:30pm UTC). If the schedule is not executed on the expected day for any reason, and this field isn't set to `true`, the schedule is not executed and is marked as `EXECUTED_WITH_ERROR_NEXT_DAY_NOT_ALLOWED`.
>
> This endpoint generates the [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event with the `status` field set to `CREATED`.
>
> Each execution of the schedule also generates the [Scheduled payment executed](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1) event.
>
> Refer to the [Payment scheduler](doc:payment-scheduler) guide for more information.

#### Request body

Required: yes

> Request processing body

**Content type `application/json`** — schema: object (schema `BulkSingleScheduleRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `defaults` | object (schema `BulkSingleScheduleDefaults`) | no | Default values applied to all schedules in the request. Individual schedules can override these values. |  |
| `schedules` | array of object (schema `BulkSingleScheduleItem`) | yes | List of schedules to create. Each schedule can override any default value. | minItems: 1; maxItems: 100 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Request was accepted and schedules will be processed asynchronously. |  |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `scheduler-payments-bulk-scheduled-payments-1` | https://developers.pismo.io/events/docs/scheduler-payments-bulk-scheduled-payments-1 |
| `scheduler-payments-scheduled-payments-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1 |
| `scheduler-payments-scheduled-payments-execution-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;500`, has examples `False`, emits events `3`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=POST path=/v1/transfers operationId=post-v1-create-transfer-schedules -->
### `POST /v1/transfers` — Create transfer schedule

- **operationId:** `post-v1-create-transfer-schedules`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a transfer schedule, which represents a transfer operation from a parent (main) account to one or more associated child accounts. Configure the schedule's execution frequency and other details in the `schedule_details` field.
>
> Transfer amounts can be set as follows.
> - If you fill out the `strategy` field, the platform uses the strategy logic to determine transfer amounts.
> - If you don't fill out the `strategy` field, you must specify the `amount` field for each transfer in the `transfers` array.
>
> In some cases, due to errors and retries, execution of the scheduled transaction might occur on the following day instead of the originally scheduled date. To address this, the `allow_execution_after_day_change` flag in `schedule_details` enables you to pre-authorize execution of the scheduled transaction on the next day. This flag must be set to `true` for schedules that are set to be executed at the end of the day (after 11:30pm UTC). If the schedule is not executed on the expected day for any reason, and this field isn't set to `true`, the schedule is not executed and is marked as `EXECUTED_WITH_ERROR_NEXT_DAY_NOT_ALLOWED`.
>
> This endpoint generates the [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event with the `status` field set to `CREATED`.
>
> Each execution of the schedule also generates the [Scheduled payment executed](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1) event.
>
> Refer to the [Payment scheduler](doc:payment-scheduler) guide for more information.

#### Request body

Required: yes

> Request processing body

**Content type `application/json`** — schema: object (schema `TransferScheduleRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | yes | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |
| `schedule_details` | object (schema `TransferScheduleDetails`) | yes | Transfer schedule details |  |
| `description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `strategy` | string (schema `Strategy`) | no | If the `strategy` field is not specified, you must provide the `amount` field for each transfer in the `transfers` array. The following strategy types determine the transfer amounts when a strategy is specified.<br><br>- `SWEEP`: Transfers the entire balance from the child account to the parent account. The terms "parent" and "child" refer to account roles, but no relationship validation is performed.<br><br>   Child → Parent<br><br>- `OVERDRAFT_SWEEEP`: Follows the same logic as `SWEEP`, except when a child account is negative, in which case the main account sends enough money to zero out the child account.<br><br>   Parent → Child<br> | enum: ["OVERDRAFT_SWEEP", "SWEEP"]; example: "SWEEP" |
| `transfers` | array of object (schema `Transfers`) | yes | List of transfers, including their origin and destination accounts.<br>The `amount` field must be provided if the `strategy` is not specified.<br> |  |
| `transfers[].description` | string | no | Transfer description | example: "Transfer to savings account" |
| `transfers[].amount` | number (schema `Amount`) | no | Credit or debit amount | format: "float"; example: 100.23 |
| `transfers[].metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `transfers[].to` | object | no | Information about the destination account for the transfer |  |
| `transfers[].to.account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `transfers[].to.processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |
| `transfers[].from` | object | no | Information about the source account for the transfer |  |
| `transfers[].from.account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `transfers[].from.processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Request was processed successfully, existing schedule with the corresponding `schedule_id` returned. | `application/json`: object (schema `TransferScheduleResponse`) |
| 201 | Request was processed successfully and new transfer schedule was created | `application/json`: object (schema `TransferScheduleResponse`) |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | no | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | no | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `scheduler-payments-scheduled-payments-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1 |
| `scheduler-payments-scheduled-payments-execution-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;201;400;403;500`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-payments-data-events`, `KU-PAY-payment-scheduler`.

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=POST path=/v1/transfers/bulk operationId=post-v1-create-bulk-transfer-schedules -->
### `POST /v1/transfers/bulk` — Create bulk transfer schedules

- **operationId:** `post-v1-create-bulk-transfer-schedules`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create multiple transfer schedules in a single request. This request triggers an asynchronous process to create the schedules. Once processing is complete, the [Bulk transfer schedules created](https://developers.pismo.io/events/docs/scheduler-payments-bulk-transfer-scheduled-payments-1) event is sent with the result of the operation.
>
> This endpoint accepts a `defaults` object that can be used to set common values for all schedules in the request. Individual schedules can override any default value by specifying the field in their own definition.
>
> Transfer amounts can be set as follows.
> - If you fill out the `strategy` field, the platform uses the strategy logic to determine transfer amounts.
> - If you don't fill out the `strategy` field, you must specify the `amount` field for each transfer in the `transfers` array, or provide a default amount in `transfer_defaults`.
>
> In some cases, due to errors and retries, execution of the scheduled transaction might occur on the following day instead of the originally scheduled date. To address this, the `allow_execution_after_day_change` flag in `schedule_details` enables you to pre-authorize execution of the scheduled transaction on the next day. This flag must be set to `true` for schedules that are set to be executed at the end of the day (after 11:30pm UTC). If the schedule is not executed on the expected day for any reason, and this field isn't set to `true`, the schedule is not executed and is marked as `EXECUTED_WITH_ERROR_NEXT_DAY_NOT_ALLOWED`.
>
> This endpoint generates the [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event with the `status` field set to `CREATED`.
>
> Each execution of the schedule also generates the [Scheduled payment executed](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1) event.
>
> Refer to the [Payment scheduler](doc:payment-scheduler) guide for more information.

#### Request body

Required: yes

> Request processing body

**Content type `application/json`** — schema: object (schema `BulkTransferScheduleRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `defaults` | object (schema `BulkTransferScheduleDefaults`) | no | Default values applied to all transfer schedules in the request. Individual schedules can override these values. |  |
| `schedules` | array of object (schema `BulkTransferScheduleItem`) | yes | List of transfer schedules to create. Each schedule can override any default value. | minItems: 1; maxItems: 100 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Request was accepted and schedules will be processed asynchronously. |  |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `scheduler-payments-bulk-transfer-scheduled-payments-1` | https://developers.pismo.io/events/docs/scheduler-payments-bulk-transfer-scheduled-payments-1 |
| `scheduler-payments-scheduled-payments-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1 |
| `scheduler-payments-scheduled-payments-execution-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;500`, has examples `False`, emits events `3`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=POST path=/v1/pre-schedules operationId=post-pre-schedules -->
### `POST /v1/pre-schedules` — Create pre-schedule

- **operationId:** `post-pre-schedules`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a pre-schedule, which is executed by a direct call from the Pismo platform at the end of the closing cycle. To configure execution of a pre-schedule, contact your Pismo representative or call the [Execute pre-schedule](ref:post-execute-pre-schedule) endpoint.
>
> This endpoint generates the [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event with the `status` field set to `CREATED`.
>
> Once the pre-schedule is created, its execution generates the following events.
>
> - First execution of the pre-schedule on the start date generates the [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event with the `status` field set to `IN_PROGRESS`.
> - Last execution of the pre-schedule on the end date generates the [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event with the `status` field set to `COMPLETED`.
> - Each execution of the pre-schedule also generates the [Scheduled payment executed](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1) event with the corresponding execution status.
>
> Refer to the [Payment scheduler](doc:payment-scheduler) guide for more information.

#### Request body

Required: yes

> Request processing body

**Content type `application/json`** — schema: object (schema `PreScheduleRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | yes | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |
| `schedule_details` | object (schema `PreScheduleDetails`) | yes | Pre-schedule details |  |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 8675309 |
| `amount` | number (schema `Amount`) | yes | Credit or debit amount | format: "float"; example: 100.23 |
| `currency_code` | string (schema `CurrencyCode`) | yes | Three-letter currency code of the operation in ISO 4217. | example: "BRL" |
| `processing_code` | string (schema `ProcessingCode`) | yes | Processing code that identifies the credit or debit operation | example: "219803" |
| `description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Request was processed successfully, existing schedule with the corresponding `schedule_id` returned. | `application/json`: object (schema `PreScheduleResponse`) |
| 201 | Request was processed successfully, new pre-schedule created. | `application/json`: object (schema `PreScheduleResponse`) |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | no | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | no | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `scheduler-payments-scheduled-payments-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1 |
| `scheduler-payments-scheduled-payments-execution-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;201;400;403;500`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-payments-data-events`, `KU-PAY-payment-scheduler`.

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=POST path=/v1/pre-schedules/bulk operationId=post-bulk-pre-schedules -->
### `POST /v1/pre-schedules/bulk` — Create bulk pre-schedules

- **operationId:** `post-bulk-pre-schedules`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create multiple pre-schedules in a single request. This request triggers an asynchronous process to create the pre-schedules. Once processing is complete, the [Bulk pre-schedules created](https://developers.pismo.io/events/docs/scheduler-payments-bulk-pre-scheduled-payments-1) event is sent with the result of the operation.
>
> Pre-schedule is a type of schedule that is executed by a direct call from the Pismo platform at the end of the closing cycle. To configure a pre-schedule execution, contact your Pismo representative or call the [Execute pre-schedule](ref:post-execute-pre-schedule) endpoint.
>
> This endpoint generates the [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event with the `status` field set to `CREATED`.
>
> Once the pre-schedule is created, its execution generates the following events.
>
> - First execution of the pre-schedule on the start date generates the [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event with the `status` field set to `IN_PROGRESS`.
> - Last execution of the pre-schedule on the end date generates the [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event with the `status` field set to `COMPLETED`.
> - Each execution of the pre-schedule also generates the [Scheduled payment executed](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1) event with the corresponding execution status.
>
> Refer to the [Payment scheduler](doc:payment-scheduler) guide for more information.

#### Request body

Required: yes

> Request processing body

**Content type `application/json`** — schema: array of object (schema `PreScheduleRequest`) (schema `BulkPreScheduleRequest`)

_No fields declared in the schema._

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Request was processed successfully, new multiple pre-schedules accepted. |  |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `scheduler-payments-bulk-pre-scheduled-payments-1` | https://developers.pismo.io/events/docs/scheduler-payments-bulk-pre-scheduled-payments-1 |
| `scheduler-payments-scheduled-payments-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1 |
| `scheduler-payments-scheduled-payments-execution-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;500`, has examples `False`, emits events `3`, deprecated `False`.

Guides that link to this operation: `KU-EVT-payments-data-events`.

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=POST path=/v1/accounts/{accountId}/pre-schedules/{scheduleId}/execute operationId=post-execute-pre-schedule -->
### `POST /v1/accounts/{accountId}/pre-schedules/{scheduleId}/execute` — Execute pre-schedule

- **operationId:** `post-execute-pre-schedule`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Execute the pre-schedule.
>
> This endpoint generates the [Scheduled payment executed](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Pismo account ID | format: "int64" |
| `scheduleId` | path | yes | string | Schedule ID |  |

#### Request body

Required: yes

> Request processing body

**Content type `application/json`** — schema: object (schema `ExecuteRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pismo_metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `scheduler-payments-scheduled-payments-execution-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=GET path=/v1/accounts/{accountId}/schedules operationId=get-all-schedules -->
### `GET /v1/accounts/{accountId}/schedules` — List account schedules

- **operationId:** `get-all-schedules`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account schedules with paging and filter options.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Pismo account ID | format: "int64" |
| `statementId` | query | no | integer | Statement ID |  |
| `cursor` | query | no | string | Pagination cursor |  |
| `limit` | query | no | integer | Pagination limit | default: 10; minimum: 0 |
| `order` | query | no | string | Returned results order. Items are sorted on the `created_at` field. By default, the order is descending (`DESC`), with the newest schedules returned first. | enum: ["ASC", "DESC"]; default: "DESC" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Request was processed successfully. | `application/json`: object (schema `GetAllScheduleResponse`) |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean (schema `HasNext`) | no | Is there a next page? | example: true |
| `next_cursor` | string (schema `NextCursor`) | no | Cursor value to apply in a subsequent query to continue pagination | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |
| `count` | integer (schema `Count`) | no | Number of items | example: 1 |
| `items` | array of object (schema `Schedule`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=GET path=/v1/accounts/{accountId}/schedules/{scheduleId}/executions operationId=get-schedule-executions -->
### `GET /v1/accounts/{accountId}/schedules/{scheduleId}/executions` — List schedule executions

- **operationId:** `get-schedule-executions`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account schedule executions.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Pismo account ID | format: "int64" |
| `scheduleId` | path | yes | string | Schedule ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Request was processed successfully, existing executions with the corresponding schedule ID returned. | `application/json`: object (schema `GetScheduleExecutionsResponse`) |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean (schema `HasNext`) | no | Is there a next page? | example: true |
| `next_cursor` | string (schema `NextCursor`) | no | Cursor value to apply in a subsequent query to continue pagination | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |
| `count` | integer (schema `Count`) | no | Number of items | example: 1 |
| `items` | array of object (schema `Execution`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=GET path=/v1/accounts/{accountId}/schedules/{scheduleId} operationId=get-schedule -->
### `GET /v1/accounts/{accountId}/schedules/{scheduleId}` — Get schedule

- **operationId:** `get-schedule`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get account schedule by schedule ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Pismo account ID | format: "int64" |
| `scheduleId` | path | yes | string | Schedule ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Request was processed successfully, existing schedule with the corresponding ID returned. | `application/json`: object (schema `Schedule`) |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | no | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |
| `schedule_kind` | string (schema `ScheduleKind`) | no | Schedule type | enum: ["SINGLE", "MULTIPLE", "PRE"]; example: "SINGLE" |
| `description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `schedule_details` | object (schema `ScheduleDetails`) | no | Schedule details |  |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `status` | string (schema `Status`) | no | Schedule status | enum: ["CREATED", "IN_PROGRESS", "CANCELED", "COMPLETED"]; example: "COMPLETED" |
| `created_at` | string (schema `CreatedAt`) | no | Date of schedule creation in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:35:05.125Z" |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `pismo_metadata` | object (schema `PismoMetadata`) | no | Any key-value object with custom information that must be passed forward in the Pismo authorization flow. Used for internal purposes only. | example: {"any-key": "any-value"} |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |
| `processing_codes` | object (schema `ProcessingCodes`) | no | Object with the processing codes for credit and debit operations |  |
| `amount` | number (schema `Amount`) | no | Credit or debit amount | format: "float"; example: 100.23 |
| `currency_code` | string (schema `CurrencyCode`) | no | Three-letter currency code of the operation in ISO 4217. | example: "BRL" |
| `restrictions` | object (schema `Restrictions`) | no | Restrictions applied to the schedule |  |
| `strategy` | string (schema `Strategy`) | no | If the `strategy` field is not specified, you must provide the `amount` field for each transfer in the `transfers` array. The following strategy types determine the transfer amounts when a strategy is specified.<br><br>- `SWEEP`: Transfers the entire balance from the child account to the parent account. The terms "parent" and "child" refer to account roles, but no relationship validation is performed.<br><br>   Child → Parent<br><br>- `OVERDRAFT_SWEEEP`: Follows the same logic as `SWEEP`, except when a child account is negative, in which case the main account sends enough money to zero out the child account.<br><br>   Parent → Child<br> | enum: ["OVERDRAFT_SWEEP", "SWEEP"]; example: "SWEEP" |
| `transfers` | array of object (schema `Transfers`) | no | List of transfers, including their origin and destination accounts.<br>The `amount` field must be provided if the `strategy` is not specified.<br> |  |
| `transfers[].description` | string | no | Transfer description | example: "Transfer to savings account" |
| `transfers[].amount` | number (schema `Amount`) | no | Credit or debit amount | format: "float"; example: 100.23 |
| `transfers[].metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `transfers[].to` | object | no | Information about the destination account for the transfer |  |
| `transfers[].to.account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `transfers[].to.processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |
| `transfers[].from` | object | no | Information about the source account for the transfer |  |
| `transfers[].from.account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `transfers[].from.processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=DELETE path=/v1/accounts/{accountId}/schedules/{scheduleId} operationId=delete-schedule -->
### `DELETE /v1/accounts/{accountId}/schedules/{scheduleId}` — Cancel schedule

- **operationId:** `delete-schedule`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel account schedule by schedule ID.
>
> This endpoint generates the [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) event with the `status` field set to `CANCELED`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Pismo account ID | format: "int64" |
| `scheduleId` | path | yes | string | Schedule ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Request was processed successfully. |  |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `scheduler-payments-scheduled-payments-1` | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_scheduler_beta.yaml method=PATCH path=/v1/accounts/{accountId}/schedules/{scheduleId} operationId=patch-schedule -->
### `PATCH /v1/accounts/{accountId}/schedules/{scheduleId}` — Update schedule

- **operationId:** `patch-schedule`
- **Specification:** `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` (Core platform - Payment scheduler)
- **Server base URL(s):** `https://sandbox.pismolabs.io/scheduler-payments`
- **Tags:** `Schedules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update account schedule by schedule ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Pismo account ID | format: "int64" |
| `scheduleId` | path | yes | string | Schedule ID |  |

#### Request body

Required: yes

> Request processing body

**Content type `application/json`** — schema: object (schema `UpdateSchedulerRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `single` | object | no | Single schedule object |  |
| `single.description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `single.metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `single.restrictions` | object (schema `Restrictions`) | no | Restrictions applied to the schedule |  |
| `single.schedule_details` | object | no | Schedule details |  |
| `single.schedule_details.end_date` | string (schema `EndDate`) | no | End date of schedule executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `single.schedule_details.retries` | object (schema `Retries`) | no | Configuration to define retry policy for failed executions. |  |
| `pre` | object | no | Pre-schedule object |  |
| `pre.schedule_details` | object (schema `PreScheduleDetails`) | no | Pre-schedule details |  |
| `pre.processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |
| `pre.amount` | number (schema `Amount`) | no | Credit or debit amount | format: "float"; example: 100.23 |
| `pre.currency_code` | string (schema `CurrencyCode`) | no | Three-letter currency code of the operation in ISO 4217. | example: "BRL" |
| `pre.description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `pre.metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `transfer` | object | no | Transfer schedule object |  |
| `transfer.description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `transfer.metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `transfer.schedule_details` | object | no | Schedule details |  |
| `transfer.schedule_details.end_date` | string (schema `EndDate`) | no | End date of schedule executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No content |  |
| 400 | Bad request |  |
| 403 | Operation forbidden |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/SingleScheduleDetails -->
### Schema `SingleScheduleDetails`

Pointer: `#/components/schemas/SingleScheduleDetails`. Type: object (schema `SingleScheduleDetails`).

> Single schedule details

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `Type`) | no | Should a schedule be executed once or in a recurring fashion?<br>- `ONCE`: Executed only once on the date specified in `start_date`.<br>- `RECURRING`: Executed repeatedly according to the interval defined in `interval`, within the period between `start_date` and `end_date`. A recurring schedule can run daily, weekly, monthly, or yearly, which is set in the `interval` field.<br> | enum: ["ONCE", "RECURRING"]; example: "RECURRING" |
| `interval` | string (schema `Interval`) | no | Schedule execution frequency | enum: ["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]; example: "DAILY" |
| `day_type` | string (schema `DayType`) | no | `BUSINESS_DAY` type ignores weekends and holidays, `CALENDAR_DAY` includes all calendar days. | enum: ["BUSINESS_DAY", "CALENDAR_DAY"]; example: "CALENDAR_DAY" |
| `start_date` | string (schema `StartDateTime`) | no | Start date of executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `end_date` | string (schema `EndDate`) | no | End date of schedule executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `retries` | object (schema `Retries`) | no | Configuration to define retry policy for failed executions. |  |
| `allow_execution_after_day_change` | boolean (schema `AllowExecutionAfterDayChange`) | no | Can the schedule be executed after the day changes? For single and transfer schedules that are scheduled for after 11:30pm UTC, this field is required to be `true`. | default: false; example: false |

<!-- schema: #/components/schemas/Restrictions -->
### Schema `Restrictions`

Pointer: `#/components/schemas/Restrictions`. Type: object (schema `Restrictions`).

> Restrictions applied to the schedule

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `minimum_daily_available` | number | no | Establishes a minimum limit value to always be maintained in the customer's balance. If the value of the customer's balance is lower than the minimum limit value, the schedule is executed, otherwise its execution is stopped and saved as "Executed with restrictions".<br> | format: "float"; example: 100.23 |
| `minimum_monthly_average_available` | number | no | Follows the same logic as `minimum_daily_available`, except it considers an average limit value from the first day of the month until the day before the scheduled execution to compare with the customer’s balance value.<br> | format: "float"; example: 100.23 |
| `minimum_days_account_inactivity` | integer | no | If the days of account inactivity are greater than this field value, the schedule execution is stopped and saved as "Executed with restrictions".<br> | example: 5 |

<!-- schema: #/components/schemas/BulkSingleScheduleDefaults -->
### Schema `BulkSingleScheduleDefaults`

Pointer: `#/components/schemas/BulkSingleScheduleDefaults`. Type: object (schema `BulkSingleScheduleDefaults`).

> Default values applied to all schedules in the request. Individual schedules can override these values.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |
| `currency_code` | string (schema `CurrencyCode`) | no | Three-letter currency code of the operation in ISO 4217. | example: "BRL" |
| `description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `amount` | number (schema `Amount`) | no | Credit or debit amount | format: "float"; example: 100.23 |
| `schedule_details` | object (schema `BulkSingleScheduleDetailsDefault`) | no | Default schedule details that can be applied to all schedules |  |
| `restrictions` | object (schema `Restrictions`) | no | Restrictions applied to the schedule |  |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

<!-- schema: #/components/schemas/BulkSingleScheduleItem -->
### Schema `BulkSingleScheduleItem`

Pointer: `#/components/schemas/BulkSingleScheduleItem`. Type: object (schema `BulkSingleScheduleItem`).

> Individual schedule in the bulk request. Only `schedule_id` is required; other fields use defaults or override them.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | yes | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |
| `currency_code` | string (schema `CurrencyCode`) | no | Three-letter currency code of the operation in ISO 4217. | example: "BRL" |
| `description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `amount` | number (schema `Amount`) | no | Credit or debit amount | format: "float"; example: 100.23 |
| `schedule_details` | object (schema `BulkSingleScheduleDetailsOverride`) | no | Schedule details that override the defaults for this specific schedule |  |
| `restrictions` | object (schema `Restrictions`) | no | Restrictions applied to the schedule |  |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

<!-- schema: #/components/schemas/TransferScheduleDetails -->
### Schema `TransferScheduleDetails`

Pointer: `#/components/schemas/TransferScheduleDetails`. Type: object (schema `TransferScheduleDetails`).

> Transfer schedule details

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `Type`) | no | Should a schedule be executed once or in a recurring fashion?<br>- `ONCE`: Executed only once on the date specified in `start_date`.<br>- `RECURRING`: Executed repeatedly according to the interval defined in `interval`, within the period between `start_date` and `end_date`. A recurring schedule can run daily, weekly, monthly, or yearly, which is set in the `interval` field.<br> | enum: ["ONCE", "RECURRING"]; example: "RECURRING" |
| `interval` | string (schema `Interval`) | no | Schedule execution frequency | enum: ["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]; example: "DAILY" |
| `day_type` | string (schema `DayType`) | no | `BUSINESS_DAY` type ignores weekends and holidays, `CALENDAR_DAY` includes all calendar days. | enum: ["BUSINESS_DAY", "CALENDAR_DAY"]; example: "CALENDAR_DAY" |
| `end_date` | string (schema `EndDate`) | no | End date of schedule executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `start_date` | string (schema `StartDateTime`) | no | Start date of executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `allow_execution_after_day_change` | boolean (schema `AllowExecutionAfterDayChange`) | no | Can the schedule be executed after the day changes? For single and transfer schedules that are scheduled for after 11:30pm UTC, this field is required to be `true`. | default: false; example: false |

<!-- schema: #/components/schemas/BulkTransferScheduleDefaults -->
### Schema `BulkTransferScheduleDefaults`

Pointer: `#/components/schemas/BulkTransferScheduleDefaults`. Type: object (schema `BulkTransferScheduleDefaults`).

> Default values applied to all transfer schedules in the request. Individual schedules can override these values.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `schedule_details` | object (schema `BulkTransferScheduleDetailsDefault`) | no | Default schedule details that can be applied to all transfer schedules |  |
| `strategy` | string (schema `Strategy`) | no | If the `strategy` field is not specified, you must provide the `amount` field for each transfer in the `transfers` array. The following strategy types determine the transfer amounts when a strategy is specified.<br><br>- `SWEEP`: Transfers the entire balance from the child account to the parent account. The terms "parent" and "child" refer to account roles, but no relationship validation is performed.<br><br>   Child → Parent<br><br>- `OVERDRAFT_SWEEEP`: Follows the same logic as `SWEEP`, except when a child account is negative, in which case the main account sends enough money to zero out the child account.<br><br>   Parent → Child<br> | enum: ["OVERDRAFT_SWEEP", "SWEEP"]; example: "SWEEP" |
| `transfer_defaults` | object (schema `BulkTransferDefaults`) | no | Default values for individual transfers within schedules |  |

<!-- schema: #/components/schemas/BulkTransferScheduleItem -->
### Schema `BulkTransferScheduleItem`

Pointer: `#/components/schemas/BulkTransferScheduleItem`. Type: object (schema `BulkTransferScheduleItem`).

> Individual transfer schedule in the bulk request. Only `schedule_id` and `transfers` are required; other fields use defaults or override them.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | yes | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |
| `description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `schedule_details` | object (schema `BulkTransferScheduleDetailsOverride`) | no | Schedule details that override the defaults for this specific transfer schedule |  |
| `strategy` | string (schema `Strategy`) | no | If the `strategy` field is not specified, you must provide the `amount` field for each transfer in the `transfers` array. The following strategy types determine the transfer amounts when a strategy is specified.<br><br>- `SWEEP`: Transfers the entire balance from the child account to the parent account. The terms "parent" and "child" refer to account roles, but no relationship validation is performed.<br><br>   Child → Parent<br><br>- `OVERDRAFT_SWEEEP`: Follows the same logic as `SWEEP`, except when a child account is negative, in which case the main account sends enough money to zero out the child account.<br><br>   Parent → Child<br> | enum: ["OVERDRAFT_SWEEP", "SWEEP"]; example: "SWEEP" |
| `transfers` | array of object (schema `BulkTransferItemRequest`) | yes | List of transfers for this schedule. At least one transfer is required. | minItems: 1 |

<!-- schema: #/components/schemas/PreScheduleDetails -->
### Schema `PreScheduleDetails`

Pointer: `#/components/schemas/PreScheduleDetails`. Type: object (schema `PreScheduleDetails`).

> Pre-schedule details

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `statement` | object (schema `Statement`) | no |  |  |

<!-- schema: #/components/schemas/Schedule -->
### Schema `Schedule`

Pointer: `#/components/schemas/Schedule`. Type: object (schema `Schedule`).

> Schedule object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `schedule_id` | string (schema `ScheduleID`) | no | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |
| `schedule_kind` | string (schema `ScheduleKind`) | no | Schedule type | enum: ["SINGLE", "MULTIPLE", "PRE"]; example: "SINGLE" |
| `description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `schedule_details` | object (schema `ScheduleDetails`) | no | Schedule details |  |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `status` | string (schema `Status`) | no | Schedule status | enum: ["CREATED", "IN_PROGRESS", "CANCELED", "COMPLETED"]; example: "COMPLETED" |
| `created_at` | string (schema `CreatedAt`) | no | Date of schedule creation in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:35:05.125Z" |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `pismo_metadata` | object (schema `PismoMetadata`) | no | Any key-value object with custom information that must be passed forward in the Pismo authorization flow. Used for internal purposes only. | example: {"any-key": "any-value"} |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |
| `processing_codes` | object (schema `ProcessingCodes`) | no | Object with the processing codes for credit and debit operations |  |
| `amount` | number (schema `Amount`) | no | Credit or debit amount | format: "float"; example: 100.23 |
| `currency_code` | string (schema `CurrencyCode`) | no | Three-letter currency code of the operation in ISO 4217. | example: "BRL" |
| `restrictions` | object (schema `Restrictions`) | no | Restrictions applied to the schedule |  |
| `strategy` | string (schema `Strategy`) | no | If the `strategy` field is not specified, you must provide the `amount` field for each transfer in the `transfers` array. The following strategy types determine the transfer amounts when a strategy is specified.<br><br>- `SWEEP`: Transfers the entire balance from the child account to the parent account. The terms "parent" and "child" refer to account roles, but no relationship validation is performed.<br><br>   Child → Parent<br><br>- `OVERDRAFT_SWEEEP`: Follows the same logic as `SWEEP`, except when a child account is negative, in which case the main account sends enough money to zero out the child account.<br><br>   Parent → Child<br> | enum: ["OVERDRAFT_SWEEP", "SWEEP"]; example: "SWEEP" |
| `transfers` | array of object (schema `Transfers`) | no | List of transfers, including their origin and destination accounts.<br>The `amount` field must be provided if the `strategy` is not specified.<br> |  |
| `transfers[].description` | string | no | Transfer description | example: "Transfer to savings account" |
| `transfers[].amount` | number (schema `Amount`) | no | Credit or debit amount | format: "float"; example: 100.23 |
| `transfers[].metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `transfers[].to` | object | no | Information about the destination account for the transfer |  |
| `transfers[].to.account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `transfers[].to.processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |
| `transfers[].from` | object | no | Information about the source account for the transfer |  |
| `transfers[].from.account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `transfers[].from.processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |

<!-- schema: #/components/schemas/Execution -->
### Schema `Execution`

Pointer: `#/components/schemas/Execution`. Type: object (schema `Execution`).

> Execution object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `execution_id` | string (schema `ExecutionID`) | no | Execution ID | example: "eec3df75-629d-43dc-8eb7-e3b186188341" |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `schedule_id` | string (schema `ScheduleID`) | no | Schedule ID (idempotency field for this operation) | minLength: 36; maxLength: 50; example: "eec3df75-629d-43dc-8eb7-e3b186188341" |
| `execution_status` | string (schema `ExecutionStatus`) | no | Status of execution. | enum: ["EXECUTED", "EXECUTED_WITH_RESTRICTIONS", "EXECUTED_WITH_ERROR_NEXT_DAY_NOT_ALLOWED", "EXECUTED_WITHOUT_SCRAPING", "EXECUTED_WITH_ERROR_BANK_SLIP"]; example: "EXECUTED_WITH_RESTRICTIONS" |
| `authorizations` | array of object (schema `Authorization`) | no |  |  |

<!-- schema: #/components/schemas/ScheduleDetails -->
### Schema `ScheduleDetails`

Pointer: `#/components/schemas/ScheduleDetails`. Type: object (schema `ScheduleDetails`).

> Schedule details

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `Type`) | no | Should a schedule be executed once or in a recurring fashion?<br>- `ONCE`: Executed only once on the date specified in `start_date`.<br>- `RECURRING`: Executed repeatedly according to the interval defined in `interval`, within the period between `start_date` and `end_date`. A recurring schedule can run daily, weekly, monthly, or yearly, which is set in the `interval` field.<br> | enum: ["ONCE", "RECURRING"]; example: "RECURRING" |
| `interval` | string (schema `Interval`) | no | Schedule execution frequency | enum: ["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]; example: "DAILY" |
| `day_type` | string (schema `DayType`) | no | `BUSINESS_DAY` type ignores weekends and holidays, `CALENDAR_DAY` includes all calendar days. | enum: ["BUSINESS_DAY", "CALENDAR_DAY"]; example: "CALENDAR_DAY" |
| `start_date` | string (schema `StartDateTime`) | no | Start date of executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `end_date` | string (schema `EndDate`) | no | End date of schedule executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `retries` | object (schema `Retries`) | no | Configuration to define retry policy for failed executions. |  |
| `allow_execution_after_day_change` | boolean (schema `AllowExecutionAfterDayChange`) | no | Can the schedule be executed after the day changes? For single and transfer schedules that are scheduled for after 11:30pm UTC, this field is required to be `true`. | default: false; example: false |
| `statement` | object (schema `Statement`) | no |  |  |

<!-- schema: #/components/schemas/ProcessingCodes -->
### Schema `ProcessingCodes`

Pointer: `#/components/schemas/ProcessingCodes`. Type: object (schema `ProcessingCodes`).

> Object with the processing codes for credit and debit operations

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `credit` | string (schema `ProcessingCodeCredit`) | no | Processing code that identifies the credit operation | example: "219803" |
| `debit` | string (schema `ProcessingCodeDebit`) | no | Processing code that identifies the debit operation | example: "219803" |

<!-- schema: #/components/schemas/Retries -->
### Schema `Retries`

Pointer: `#/components/schemas/Retries`. Type: object (schema `Retries`).

> Configuration to define retry policy for failed executions.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `interval_recurrence` | integer (schema `IntervalRecurrence`) | no | Interval for retries, in minutes | minimum: 1; maximum: 60; example: 5 |
| `number_of_attempts` | integer (schema `NumberOfAttempts`) | no | Maximum number of execution retries | minimum: 1; maximum: 10; example: 5 |

<!-- schema: #/components/schemas/BulkSingleScheduleDetailsDefault -->
### Schema `BulkSingleScheduleDetailsDefault`

Pointer: `#/components/schemas/BulkSingleScheduleDetailsDefault`. Type: object (schema `BulkSingleScheduleDetailsDefault`).

> Default schedule details that can be applied to all schedules

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `Type`) | no | Should a schedule be executed once or in a recurring fashion?<br>- `ONCE`: Executed only once on the date specified in `start_date`.<br>- `RECURRING`: Executed repeatedly according to the interval defined in `interval`, within the period between `start_date` and `end_date`. A recurring schedule can run daily, weekly, monthly, or yearly, which is set in the `interval` field.<br> | enum: ["ONCE", "RECURRING"]; example: "RECURRING" |
| `interval` | string (schema `Interval`) | no | Schedule execution frequency | enum: ["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]; example: "DAILY" |
| `day_type` | string (schema `DayType`) | no | `BUSINESS_DAY` type ignores weekends and holidays, `CALENDAR_DAY` includes all calendar days. | enum: ["BUSINESS_DAY", "CALENDAR_DAY"]; example: "CALENDAR_DAY" |
| `start_date` | string (schema `StartDateTime`) | no | Start date of executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `end_date` | string (schema `EndDate`) | no | End date of schedule executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `retries` | object (schema `Retries`) | no | Configuration to define retry policy for failed executions. |  |
| `allow_execution_after_day_change` | boolean (schema `AllowExecutionAfterDayChange`) | no | Can the schedule be executed after the day changes? For single and transfer schedules that are scheduled for after 11:30pm UTC, this field is required to be `true`. | default: false; example: false |

<!-- schema: #/components/schemas/BulkSingleScheduleDetailsOverride -->
### Schema `BulkSingleScheduleDetailsOverride`

Pointer: `#/components/schemas/BulkSingleScheduleDetailsOverride`. Type: object (schema `BulkSingleScheduleDetailsOverride`).

> Schedule details that override the defaults for this specific schedule

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `Type`) | no | Should a schedule be executed once or in a recurring fashion?<br>- `ONCE`: Executed only once on the date specified in `start_date`.<br>- `RECURRING`: Executed repeatedly according to the interval defined in `interval`, within the period between `start_date` and `end_date`. A recurring schedule can run daily, weekly, monthly, or yearly, which is set in the `interval` field.<br> | enum: ["ONCE", "RECURRING"]; example: "RECURRING" |
| `interval` | string (schema `Interval`) | no | Schedule execution frequency | enum: ["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]; example: "DAILY" |
| `day_type` | string (schema `DayType`) | no | `BUSINESS_DAY` type ignores weekends and holidays, `CALENDAR_DAY` includes all calendar days. | enum: ["BUSINESS_DAY", "CALENDAR_DAY"]; example: "CALENDAR_DAY" |
| `start_date` | string (schema `StartDateTime`) | no | Start date of executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `end_date` | string (schema `EndDate`) | no | End date of schedule executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `retries` | object (schema `Retries`) | no | Configuration to define retry policy for failed executions. |  |
| `allow_execution_after_day_change` | boolean (schema `AllowExecutionAfterDayChange`) | no | Can the schedule be executed after the day changes? For single and transfer schedules that are scheduled for after 11:30pm UTC, this field is required to be `true`. | default: false; example: false |

<!-- schema: #/components/schemas/BulkTransferScheduleDetailsDefault -->
### Schema `BulkTransferScheduleDetailsDefault`

Pointer: `#/components/schemas/BulkTransferScheduleDetailsDefault`. Type: object (schema `BulkTransferScheduleDetailsDefault`).

> Default schedule details that can be applied to all transfer schedules

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `Type`) | no | Should a schedule be executed once or in a recurring fashion?<br>- `ONCE`: Executed only once on the date specified in `start_date`.<br>- `RECURRING`: Executed repeatedly according to the interval defined in `interval`, within the period between `start_date` and `end_date`. A recurring schedule can run daily, weekly, monthly, or yearly, which is set in the `interval` field.<br> | enum: ["ONCE", "RECURRING"]; example: "RECURRING" |
| `interval` | string (schema `Interval`) | no | Schedule execution frequency | enum: ["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]; example: "DAILY" |
| `day_type` | string (schema `DayType`) | no | `BUSINESS_DAY` type ignores weekends and holidays, `CALENDAR_DAY` includes all calendar days. | enum: ["BUSINESS_DAY", "CALENDAR_DAY"]; example: "CALENDAR_DAY" |
| `start_date` | string (schema `StartDateTime`) | no | Start date of executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `end_date` | string (schema `EndDate`) | no | End date of schedule executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `allow_execution_after_day_change` | boolean (schema `AllowExecutionAfterDayChange`) | no | Can the schedule be executed after the day changes? For single and transfer schedules that are scheduled for after 11:30pm UTC, this field is required to be `true`. | default: false; example: false |

<!-- schema: #/components/schemas/BulkTransferDefaults -->
### Schema `BulkTransferDefaults`

Pointer: `#/components/schemas/BulkTransferDefaults`. Type: object (schema `BulkTransferDefaults`).

> Default values for individual transfers within schedules

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | no | Credit or debit amount | format: "float"; example: 100.23 |
| `description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `from_processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |
| `to_processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

<!-- schema: #/components/schemas/BulkTransferScheduleDetailsOverride -->
### Schema `BulkTransferScheduleDetailsOverride`

Pointer: `#/components/schemas/BulkTransferScheduleDetailsOverride`. Type: object (schema `BulkTransferScheduleDetailsOverride`).

> Schedule details that override the defaults for this specific transfer schedule

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `Type`) | no | Should a schedule be executed once or in a recurring fashion?<br>- `ONCE`: Executed only once on the date specified in `start_date`.<br>- `RECURRING`: Executed repeatedly according to the interval defined in `interval`, within the period between `start_date` and `end_date`. A recurring schedule can run daily, weekly, monthly, or yearly, which is set in the `interval` field.<br> | enum: ["ONCE", "RECURRING"]; example: "RECURRING" |
| `interval` | string (schema `Interval`) | no | Schedule execution frequency | enum: ["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]; example: "DAILY" |
| `day_type` | string (schema `DayType`) | no | `BUSINESS_DAY` type ignores weekends and holidays, `CALENDAR_DAY` includes all calendar days. | enum: ["BUSINESS_DAY", "CALENDAR_DAY"]; example: "CALENDAR_DAY" |
| `start_date` | string (schema `StartDateTime`) | no | Start date of executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `end_date` | string (schema `EndDate`) | no | End date of schedule executions in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br> | format: "date-time"; example: "2023-01-02T07:00:00.000Z" |
| `allow_execution_after_day_change` | boolean (schema `AllowExecutionAfterDayChange`) | no | Can the schedule be executed after the day changes? For single and transfer schedules that are scheduled for after 11:30pm UTC, this field is required to be `true`. | default: false; example: false |

<!-- schema: #/components/schemas/BulkTransferItemRequest -->
### Schema `BulkTransferItemRequest`

Pointer: `#/components/schemas/BulkTransferItemRequest`. Type: object (schema `BulkTransferItemRequest`).

> Individual transfer within a schedule. Account IDs in the `from` and `to` fields are required; other fields can use defaults.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | no | Credit or debit amount | format: "float"; example: 100.23 |
| `description` | string (schema `Description`) | no | Optional text that describes the operation | maxLength: 100; example: "Custom purchase" |
| `from` | object (schema `BulkTransferFrom`) | yes | Source of a transfer. `account_id` is required; `processing_code` can use the default value. |  |
| `to` | object (schema `BulkTransferTo`) | yes | Destination of a transfer. `account_id` is required; `processing_code` can use the default value. |  |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

<!-- schema: #/components/schemas/Statement -->
### Schema `Statement`

Pointer: `#/components/schemas/Statement`. Type: object (schema `Statement`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Pismo ID of the statement linked to the pre-schedule | example: 1234455 |

<!-- schema: #/components/schemas/Authorization -->
### Schema `Authorization`

Pointer: `#/components/schemas/Authorization`. Type: object (schema `Authorization`).

> Authorization

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 8675309 |
| `tracking_id` | string (schema `TrackingID`) | no | Unique tracking ID for this operation | minLength: 36; maxLength: 50; example: "249fbd1c-cfcd-48aa-8bcb-1ffe3a5f7978" |
| `payment_date` | string (schema `PaymentDatetime`) | no | Effective payment date in the UTC-0 RFC3339 format. Format: YYYY-MM-DDTHH:mm:ss.sssZ.<br>Payments can be backdated, but future dates are not allowed.<br> | format: "date-time"; example: "2023-01-02T07:35:05.125Z" |
| `status` | string (schema `StatusAuthorization`) | no | Authorization status | enum: ["APPROVED", "REJECTED"]; example: "REJECTED" |
| `response_code` | string (schema `ResponseCode`) | no | Alphanumeric two-character standard card network response code or an alternative custom response code, which provides the precise reason for the success or denial of the operation by the card network, platform, or anti-fraud solution. | example: "00" |
| `denial_code` | string (schema `DenialCode`) | no | Authorization denial code | example: "DAL" |

<!-- schema: #/components/schemas/BulkTransferFrom -->
### Schema `BulkTransferFrom`

Pointer: `#/components/schemas/BulkTransferFrom`. Type: object (schema `BulkTransferFrom`).

> Source of a transfer. `account_id` is required; `processing_code` can use the default value.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 8675309 |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |

<!-- schema: #/components/schemas/BulkTransferTo -->
### Schema `BulkTransferTo`

Pointer: `#/components/schemas/BulkTransferTo`. Type: object (schema `BulkTransferTo`).

> Destination of a transfer. `account_id` is required; `processing_code` can use the default value.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 8675309 |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code that identifies the credit or debit operation | example: "219803" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | tag `Schedules`: POST /v1/schedules, POST /v1/schedules/bulk, POST /v1/transfers, POST /v1/transfers/bulk, POST /v1/pre-schedules, POST /v1/pre-schedules/bulk, POST /v1/accounts/{accountId}/pre-schedules/{scheduleId}/execute, GET /v1/accounts/{accountId}/schedules, GET /v1/accounts/{accountId}/schedules/{scheduleId}/executions, GET /v1/accounts/{accountId}/schedules/{scheduleId}, DELETE /v1/accounts/{accountId}/schedules/{scheduleId}, PATCH /v1/accounts/{accountId}/schedules/{scheduleId} | https://github.com/PismoDevEx/pismo-api-specs | `dbe6a1a7f7485280…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-scheduler` — Event catalogue: scheduler
- `KU-EVT-payments-data-events` — Core platform - Payments
- `KU-PAY-payment-scheduler` — Payment scheduler
