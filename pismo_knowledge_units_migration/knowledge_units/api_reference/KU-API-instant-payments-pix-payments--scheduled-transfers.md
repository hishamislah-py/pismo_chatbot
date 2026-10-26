---
ku_id: KU-API-instant-payments-pix-payments--scheduled-transfers
title: 'API reference: Instant payments - Pix payments — Scheduled transfers'
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
- post-schedule
- get-schedules
- delete-transfer
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-ERR-codes-epix
- KU-EVT-catalogue-pix
- KU-EVT-pix-payments-data-events
specification_version: '1.0'
---

# API reference: Instant payments - Pix payments — Scheduled transfers

**KU ID:** `KU-API-instant-payments-pix-payments--scheduled-transfers` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Scheduled transfers` in `api-specs/Instant_payments_-_Pix_payments.yaml` (“Instant payments - Pix payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /pix/v1/pix/out/schedule` | `post-schedule` | Schedule transfer [deprecated] | **yes** |
| `GET /pix/v1/pix/out/accounts/{account_id}/schedules` | `get-schedules` | List account scheduled transfers | no |
| `DELETE /pix/v1/pix/out/schedule/{scheduler_id}` | `delete-transfer` | Cancel scheduled transfer | no |

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=POST path=/pix/v1/pix/out/schedule operationId=post-schedule -->
### `POST /pix/v1/pix/out/schedule` — Schedule transfer [deprecated]

- **operationId:** `post-schedule`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Scheduled transfers`
- **Deprecated in specification:** **yes**
- **Security requirement:** not declared

**Description (from the specification):**

> This endpoint is `DEPRECATED`. It is recommended you call [Schedule Transfer(s) V2](ref:post-schedule-pix-payment) instead.
>
> Schedule a Pix-out transfer for a future date.
>
> As with the [Pix-out transfer](ref:post-pix-out-transfer) endpoint, if you are using a key or QR Code, you need to call  <a href="https://developers.pismo.io/pismo-docs/reference/post-v2-pix-keys-validate">Validate DICT key</a> or <a href="https://developers.pismo.io/pismo-docs/reference/post-qr-code">Get and validate QR Code</a> before calling this endpoint. You need to enter the `end_to_end_id` returned from those calls here. If you are not using a key or QR Code, this endpoint generates and returns an `end_to_end_id` value you can use in other endpoints.
>
> The `end_to_end_id` field is a Brazil Central Bank (BCB) requirement to track Pix transactions.  Basically, there are two steps to a Pix transaction: 1. Initialize a transaction and 2. Confirm a transaction. The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. 
>
> When the transfer takes place, <a href="https://developers.pismo.io/events/docs/pix-pix-out-1">Pix out notification received</a> and <a href="https://developers.pismo.io/events/docs/pix-financial-reconciliation-1">Pix reconciliation notification received </a> events are generated.
>
> Also, when the transfer takes place, a <a href="https://developers.pismo.io/events/docs/pix-pix-in-1">Pix-in notification received</a> event is generated when the funds are deposited in the payee's account, which can be a Pismo account or an external account.
>
> For all events, the `status` or `result` field indicates operation success or failure.
>
> For more information, see the [Pix instant payments](doc:pix-instant-payments) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique ID to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `pix.PixOutScheduleRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Pismo account ID. | example: 5869300 |
| `amount` | number (schema `Amount`) | yes | Amount to be transferred. | example: 1050.44 |
| `bank_account` | object (schema `pix.ScheduleBankAccount`) | yes |  |  |
| `initiation_type` | string (schema `ScheduleInitiationType`) | yes | Initiation type:  <br><br>  `MANUAL` - Manually initiated. Key is not used - bank account, bank code, document number, and branch are used for identification.<br><br>  `DICT` - Diretorio de Identificadores de Contas de Transação (Transaction accounts ID directory). Pix/DICT key is used for identification.<br><br>  `DYNAMIC_QRCODE` - The amount and other details for a dynamic code are included automatically. <br> | enum: ["MANUAL", "DICT", "STATIC_QRCODE", "DYNAMIC_QRCODE"]; maxLength: 20; example: "DICT" |
| `ispb` | string (schema `ISPB`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |
| `payee` | object (schema `pix.SchedulePayee`) | yes |  |  |
| `schedule_datetime` | string (schema `ScheduleDatetime`) | yes | Date to schedule the process. RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | example: "2020-08-13T13:49:03.000Z" |
| `remittance_information` | string (schema `RemittanceInformation`) | no | Remittance information. Information from payee when transaction is a static QR Code.<br> | maxLength: 140 |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `pix.PixOutScheduleResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `customer.Error`) |

##### Response 201

- Response header `x-cid`: Request tracking ID. (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | yes | Amount to be transferred. | example: 1050.44 |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `payee` | object | yes | Payee's information. |  |
| `payee.document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `payee.ispb` | string (schema `ISPB`) | no | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |
| `payee.name` | string (schema `Name`) | no | Name | maxLength: 200; example: "Walter Melon" |
| `payer` | object | yes | Payer's information. |  |
| `payer.document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `payer.ispb` | string (schema `ISPB`) | no | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |
| `payer.name` | string (schema `Name`) | no | Name | maxLength: 200; example: "Walter Melon" |
| `schedule_creation_datetime` | string (schema `ScheduleCreationDatetime`) | yes | Scheduled transfer creation datetime. RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | example: "2020-08-13T13:49:03.000Z" |
| `schedule_datetime` | string (schema `ScheduleDatetime`) | yes | Date to schedule the process. RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | example: "2020-08-13T13:49:03.000Z" |
| `schedule_id` | string (schema `SchedulerID`) | yes | Scheduled PIX transaction ID | example: "7b29a055-00e1-41e5-b880-aebe517b3bf6" |
| `status` | string (schema `TransferStatus`) | yes | Scheduled transfer status. | enum: ["SCHEDULED", "CANCELLED", "SETTLED", "FAILED"]; example: "SCHEDULED" |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
400 Example `EPIX0003` (Account not found):

```json
{
  "code": "EPIX0003",
  "message": "Account not found"
}
```

400 Example `EPIX0019` (Accounts - API returned 4xx error):

```json
{
  "code": "EPIX0019",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EPIX0020` (SPI Gateway - API returned 4xx error):

```json
{
  "code": "EPIX0020",
  "message": "SPI Gateway - API returned 4xx error"
}
```

400 Example `EPIX0032` (Error unmarshalling request body):

```json
{
  "code": "EPIX0032",
  "message": "Error unmarshalling request body"
}
```

400 Example `EPIX0049` (Payload validation):

```json
{
  "code": "EPIX0049",
  "message": "Validation error",
  "details": {
    "payload": [
      {
        "field": "schedule_datetime",
        "message": "Field \"schedule_datetime\" is required"
      },
      {
        "field": "initiation_type",
        "message": "Field \"initiation_type\" is required"
      }
    ]
  }
}
```

400 Example `EPIX0091` (Pix Schedule - schedule date is invalid):

```json
{
  "code": "EPIX0091",
  "message": "Pix Schedule - schedule date is invalid"
}
```

400 Example `EPIX0092` (Pix Schedule - EndToEndId should be provided):

```json
{
  "code": "EPIX0092",
  "message": "Pix Schedule - EndToEndId should be provided"
}
```

400 Example `EPIX0099` (Account id header does not match request body):

```json
{
  "code": "EPIX0099",
  "message": "Account id header does not match request body"
}
```

400 Example `EPIX0125` (Key cannot be sent when `initiation_type` is `MANUAL`):

```json
{
  "code": "EPIX0125",
  "message": "Key cannot be sent when `initiation_type` is `MANUAL`"
}
```

400 Example `EPIX0126` (Required Key):

```json
{
  "code": "EPIX0126",
  "message": "Required Key"
}
```

##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
403 Example `EPIX0009` (Missing required header: "x-tenant"):

```json
{
  "code": "EPIX0009",
  "message": "Missing required header: \"x-tenant\""
}
```

403 Example `EPIX0010` (Invalid account id header: "x-account-id"):

```json
{
  "code": "EPIX0010",
  "message": "Invalid account id header: \"x-account-id\""
}
```

403 Example `EPIX0069` (Missing required header: "Idempotency-Key"):

```json
{
  "code": "EPIX0069",
  "message": "Missing required header: \"Idempotency-Key\""
}
```

403 Example `EPIX0132` (Invalid field size for Idempotency-Key):

```json
{
  "code": "EPIX0132",
  "message": "Invalid field size for Idempotency-Key"
}
```

##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
404 Example `EPIX0041` (SPI Gateway - Not found error. Check details):

```json
{
  "code": "EPIX0041",
  "message": "SPI Gateway - Not found error. Check details"
}
```

##### Response 409

- Response header `x-cid`: Request tracking ID. (string)
409 Example `EPIX0008` (Account blocked or cancelled):

```json
{
  "code": "EPIX0008",
  "message": "Account blocked or cancelled"
}
```

##### Response 429

- Response header `x-cid`: Request tracking ID. (string)
429 Example `EPIX0031` (SPI Gateway - API returned a rate limit error):

```json
{
  "code": "EPIX0031",
  "message": "SPI Gateway - API returned a rate limit error"
}
```

##### Response 500

- Response header `x-cid`: Request tracking ID. (string)
500 Example `EPIX0004` (Internal server error):

```json
{
  "code": "EPIX0004",
  "message": "Internal server error"
}
```

500 Example `EPIX0005` (Error unmarshalling object):

```json
{
  "code": "EPIX0005",
  "message": "Error unmarshalling object"
}
```

500 Example `EPIX0007` (HTTP error):

```json
{
  "code": "EPIX0007",
  "message": "HTTP error"
}
```

500 Example `EPIX0017` (Accounts - API returned 5xx error):

```json
{
  "code": "EPIX0017",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EPIX0042` (Accounts API timeout error):

```json
{
  "code": "EPIX0042",
  "message": "Accounts API timeout error"
}
```

500 Example `EPIX0095` (Pix Schedule - Error marshalling schedule transfer):

```json
{
  "code": "EPIX0095",
  "message": "Pix Schedule - Error marshalling schedule transfer"
}
```

500 Example `EPIX0096` (Pix Schedule - Error on start queue scheduler):

```json
{
  "code": "EPIX0096",
  "message": "Pix Schedule - Error on start queue scheduler"
}
```

500 Example `EPIX0097` (Pix Schedule - Error persisting transaction):

```json
{
  "code": "EPIX0097",
  "message": "Pix Schedule - Error persisting transaction"
}
```

500 Example `EPIX0098` (Pix Schedule - Error persisting scheduled transfers):

```json
{
  "code": "EPIX0098",
  "message": "Pix Schedule - Error persisting scheduled transfers"
}
```

##### Response 502

- Response header `x-cid`: Request tracking ID. (string)
502 Example `EPIX0018` (SPI Gateway - API returned error):

```json
{
  "code": "EPIX0018",
  "message": "SPI Gateway - API returned error"
}
```

##### Response 504

- Response header `x-cid`: Request tracking ID. (string)
504 Example `EPIX0030` (SPI Gateway - API returned a timeout error):

```json
{
  "code": "EPIX0030",
  "message": "SPI Gateway - API returned a timeout error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPIX0003` | Account not found |
| 400 | `EPIX0019` | Accounts - API returned 4xx error |
| 400 | `EPIX0020` | SPI Gateway - API returned 4xx error |
| 400 | `EPIX0032` | Error unmarshalling request body |
| 400 | `EPIX0049` | Validation error |
| 400 | `EPIX0091` | Pix Schedule - schedule date is invalid |
| 400 | `EPIX0092` | Pix Schedule - EndToEndId should be provided |
| 400 | `EPIX0099` | Account id header does not match request body |
| 400 | `EPIX0125` | Key cannot be sent when `initiation_type` is `MANUAL` |
| 400 | `EPIX0126` | Required Key |
| 403 | `EPIX0009` | Missing required header: "x-tenant" |
| 403 | `EPIX0010` | Invalid account id header: "x-account-id" |
| 403 | `EPIX0069` | Missing required header: "Idempotency-Key" |
| 403 | `EPIX0132` | Invalid field size for Idempotency-Key |
| 404 | `EPIX0041` | SPI Gateway - Not found error. Check details |
| 409 | `EPIX0008` | Account blocked or cancelled |
| 429 | `EPIX0031` | SPI Gateway - API returned a rate limit error |
| 500 | `EPIX0004` | Internal server error |
| 500 | `EPIX0005` | Error unmarshalling object |
| 500 | `EPIX0007` | HTTP error |
| 500 | `EPIX0017` | Accounts - API returned 5xx error |
| 500 | `EPIX0042` | Accounts API timeout error |
| 500 | `EPIX0095` | Pix Schedule - Error marshalling schedule transfer |
| 500 | `EPIX0096` | Pix Schedule - Error on start queue scheduler |
| 500 | `EPIX0097` | Pix Schedule - Error persisting transaction |
| 500 | `EPIX0098` | Pix Schedule - Error persisting scheduled transfers |
| 502 | `EPIX0018` | SPI Gateway - API returned error |
| 504 | `EPIX0030` | SPI Gateway - API returned a timeout error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-financial-reconciliation-1` | https://developers.pismo.io/events/docs/pix-financial-reconciliation-1 |
| `pix-pix-in-1` | https://developers.pismo.io/events/docs/pix-pix-in-1 |
| `pix-pix-out-1` | https://developers.pismo.io/events/docs/pix-pix-out-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;404;409;429;500;502;504`, has examples `True`, emits events `3`, deprecated `True`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-pix-payments-data-events`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=GET path=/pix/v1/pix/out/accounts/{account_id}/schedules operationId=get-schedules -->
### `GET /pix/v1/pix/out/accounts/{account_id}/schedules` — List account scheduled transfers

- **operationId:** `get-schedules`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Scheduled transfers`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Retrieve an account's scheduled transfers.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `account_id` | path | yes | integer | Pismo account ID. | example: 5869300 |
| `perPage` | query | yes | string | Per page amount (min=1, max=100). Default is `20`. |  |
| `lastEvaluatedCreationDatetime` | query | no | string | This is the `last_evaluated_creation_datetime` field in the returned result and is used to get the next page of results in a subsequent request.<br>RFC 3339 format. For example -  "2023-04-12T23:20:50.52Z". |  |
| `schedulerId` | query | no | string | Schedule ID filter | maxLength: 36; example: "8675309" |
| `scheduleCreationBeginDatetime` | query | no | string | Schedule creation datetime begin filter. RFC 3339 value, for example: `2023-04-12T23:20:50.52Z`. <br> |  |
| `scheduleCreationEndDatetime` | query | no | string | Schedule creation datetime end filter. RFC 3339 value, for example: `2023-04-12T23:20:50.52Z`. <br> |  |
| `scheduleBeginDatetime` | query | no | string | Schedule datetime begin filter. RFC 3339 value, for example: `2023-04-12T23:20:50.52Z`. <br> |  |
| `scheduleEndDatetime` | query | no | string | Schedule datetime end filter. RFC 3339 value, for example: `2023-04-12T23:20:50.52Z`. <br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `pix.SchedulesFindResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking ID. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `pix.SimpleScheduledTransfer`) | no | Page list of items. |  |
| `last_evaluated_creation_datetime` | string | no | Last evaluated creation date time. Used to fetch the next page of results.<br><br>RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". <br> |  |
| `per_page` | integer (schema `PerPage`) | yes | Max number of items per page. | example: 10 |
| `total_items` | integer (schema `TotalItems`) | yes | Total number of items | example: 1000 |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
400 Example `EPIX0100` (Invalid account id in parameter):

```json
{
  "code": "EPIX0100",
  "message": "Invalid account id in parameter"
}
```

400 Example `EPIX0061` (Invalid value for query param):

```json
{
  "code": "EPIX0061",
  "message": "Invalid value for query param"
}
```

400 Example `EPIX0103` (Invalid value for datetime query parameter. RFC3339 format must be used):

```json
{
  "code": "EPIX0103",
  "message": "Invalid value for datetime query parameter. RFC3339 format must be used"
}
```

##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
403 Example `EPIX0009` (Missing required header: "x-tenant"):

```json
{
  "code": "EPIX0009",
  "message": "Missing required header: \"x-tenant\""
}
```

403 Example `EPIX0010` (Invalid account id header: "x-account-id"):

```json
{
  "code": "EPIX0010",
  "message": "Invalid account id header: \"x-account-id\""
}
```

403 Example `EPIX0102` (Entity"s account id does not match x-account-id header):

```json
{
  "code": "EPIX0102",
  "message": "Entity\"s account id does not match x-account-id header"
}
```

##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
404 Example `EPIX0101` (Pix Schedule - Error scheduled transfers not found):

```json
{
  "code": "EPIX0101",
  "message": "Pix Schedule - Error scheduled transfers not found"
}
```

##### Response 500

- Response header `x-cid`: Request tracking ID. (string)
500 Example `EPIX0004` (Internal server error):

```json
{
  "code": "EPIX0004",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPIX0100` | Invalid account id in parameter |
| 400 | `EPIX0061` | Invalid value for query param |
| 400 | `EPIX0103` | Invalid value for datetime query parameter. RFC3339 format must be used |
| 403 | `EPIX0009` | Missing required header: "x-tenant" |
| 403 | `EPIX0010` | Invalid account id header: "x-account-id" |
| 403 | `EPIX0102` | Entity"s account id does not match x-account-id header |
| 404 | `EPIX0101` | Pix Schedule - Error scheduled transfers not found |
| 500 | `EPIX0004` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=DELETE path=/pix/v1/pix/out/schedule/{scheduler_id} operationId=delete-transfer -->
### `DELETE /pix/v1/pix/out/schedule/{scheduler_id}` — Cancel scheduled transfer

- **operationId:** `delete-transfer`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Scheduled transfers`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Cancel a scheduled Pix-out transfer.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `scheduler_id` | path | yes | string | Schedule ID | maxLength: 36; example: "8675309" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 |  |  |
| 403 | Forbidden | `Application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `Application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `Application/json`: object (schema `customer.Error`) |

##### Response 204

- Response header `x-cid`: Request tracking ID. (string)
##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
403 Example `EPIX0009` (Missing required header: "x-tenant"):

```json
{
  "code": "EPIX0009",
  "message": "Missing required header: \"x-tenant\""
}
```

403 Example `EPIX0010` (Invalid account id header: "x-account-id"):

```json
{
  "code": "EPIX0010",
  "message": "Invalid account id header: \"x-account-id\""
}
```

403 Example `EPIX0102` (Entity"s account id does not match x-account-id header):

```json
{
  "code": "EPIX0102",
  "message": "Entity\"s account id does not match x-account-id header"
}
```

##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
404 Example `EPIX0101` (Pix Schedule - Error scheduled transfers not found):

```json
{
  "code": "EPIX0101",
  "message": "Pix Schedule - Error scheduled transfers not found"
}
```

##### Response 500

- Response header `x-cid`: Request tracking ID. (string)
500 Example `EPIX0004` (Internal server error):

```json
{
  "code": "EPIX0004",
  "message": "Internal server error"
}
```

500 Example `EPIX0014` (Database internal Error):

```json
{
  "code": "EPIX0014",
  "message": "Database internal Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 403 | `EPIX0009` | Missing required header: "x-tenant" |
| 403 | `EPIX0010` | Invalid account id header: "x-account-id" |
| 403 | `EPIX0102` | Entity"s account id does not match x-account-id header |
| 404 | `EPIX0101` | Pix Schedule - Error scheduled transfers not found |
| 500 | `EPIX0004` | Internal server error |
| 500 | `EPIX0014` | Database internal Error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/pix.ScheduleBankAccount -->
### Schema `pix.ScheduleBankAccount`

Pointer: `#/components/schemas/pix.ScheduleBankAccount`. Type: object (schema `pix.ScheduleBankAccount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | yes | Account type:  <br /><br>  `CACC` - Checking/current account.  Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |

<!-- schema: #/components/schemas/pix.SchedulePayee -->
### Schema `pix.SchedulePayee`

Pointer: `#/components/schemas/pix.SchedulePayee`. Type: object (schema `pix.SchedulePayee`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | yes | Account type:  <br /><br>  `CACC` - Checking/current account.  Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `bank` | string (schema `Bank`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID for the receiving bank, an 8-digit value. | maxLength: 8; example: "237" |
| `branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |
| `key` | string | no | Key value. Cannot be passed when `initiation_type` is `MANUAL` | example: "45fe6866-21a5-4f6d-84c2-950a2a1df8e7" |
| `beneficiary_id` | string (schema `BeneficiaryID`) | no | Beneficiary ID. This ID created when the [Register beneficiary](ref:post-intl-bank-accounts-v1-bank-accounts-beneficiaries) endpoint is called.<br> | maxLength: 36; example: "97c96d96-9b87-404b-88e5-287f2b0e6e0a" |

<!-- schema: #/components/schemas/customer.Error -->
### Schema `customer.Error`

Pointer: `#/components/schemas/customer.Error`. Type: object (schema `customer.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error's code. | example: "EPT0001" |
| `details` | object (schema `customer.DetailMessage`) | no |  |  |
| `message` | string | no | Error's message. | example: "User not found" |

<!-- schema: #/components/schemas/pix.SimpleScheduledTransfer -->
### Schema `pix.SimpleScheduledTransfer`

Pointer: `#/components/schemas/pix.SimpleScheduledTransfer`. Type: object (schema `pix.SimpleScheduledTransfer`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | yes | Amount to be transferred. | example: 1050.44 |
| `cancel_datetime` | string | no | Scheduled transfer cancellation datetime. RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | example: "2020-08-13T13:49:03.000Z" |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `internal` | boolean (schema `Internal`) | no | Was transaction made between a Pismo organization's accounts? In this case, the instant payment system is not called. | example: false |
| `payee` | object | yes | Payee's information. |  |
| `payee.document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `payee.ispb` | string (schema `ISPB`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |
| `payee.name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |
| `schedule_creation_datetime` | string (schema `ScheduleCreationDatetime`) | yes | Scheduled transfer creation datetime. RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | example: "2020-08-13T13:49:03.000Z" |
| `schedule_datetime` | string (schema `ScheduleDatetime`) | yes | Date to schedule the process. RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | example: "2020-08-13T13:49:03.000Z" |
| `schedule_id` | string (schema `SchedulerID`) | yes | Scheduled PIX transaction ID | example: "7b29a055-00e1-41e5-b880-aebe517b3bf6" |
| `status` | string (schema `TransferStatus`) | yes | Scheduled transfer status. | enum: ["SCHEDULED", "CANCELLED", "SETTLED", "FAILED"]; example: "SCHEDULED" |

<!-- schema: #/components/schemas/customer.DetailMessage -->
### Schema `customer.DetailMessage`

Pointer: `#/components/schemas/customer.DetailMessage`. Type: object (schema `customer.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `customer.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `customer.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `customer.PayloadMessage`) | no |  |  |

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

- `POST /pix/v1/pix/out/schedule` (`post-schedule`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_Pix_payments.yaml` | tag `Scheduled transfers`: POST /pix/v1/pix/out/schedule, GET /pix/v1/pix/out/accounts/{account_id}/schedules, DELETE /pix/v1/pix/out/schedule/{scheduler_id} | https://github.com/PismoDevEx/pismo-api-specs | `034f2ce79f002354…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-ERR-codes-epix` — Error codes: EPIX
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-EVT-pix-payments-data-events` — Instant payments - Pix
