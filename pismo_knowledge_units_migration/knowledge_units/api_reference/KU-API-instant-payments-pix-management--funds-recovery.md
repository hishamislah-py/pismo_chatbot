---
ku_id: KU-API-instant-payments-pix-management--funds-recovery
title: 'API reference: Instant payments - Pix management — Funds recovery'
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
- list-account-fund-recoveries
- post-create-funds-recovery
- post-get-funds-recovery-infractions
- post-get-funds-recovery-refunds
- post-get-funds-recovery
- patch-funds-recovery
- get-refund-recovery
- post-refund-recovery
- post-cancel-funds-recovery
related_kus:
- KU-ERR-codes-epda
- KU-ERR-codes-epdg
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-pix
- KU-PAY-pix-funds-recovery
specification_version: 0.0.1
---

# API reference: Instant payments - Pix management — Funds recovery

**KU ID:** `KU-API-instant-payments-pix-management--funds-recovery` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 9 operation(s) tagged `Funds recovery` in `api-specs/Instant_payments_-_Pix_management.yaml` (“Instant payments - Pix management”, version `0.0.1`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/pix/funds-recoveries` | `list-account-fund-recoveries` | List account fund recoveries [beta] | no |
| `POST /v1/pix/funds-recoveries` | `post-create-funds-recovery` | Create funds recovery [beta] | no |
| `GET /v1/pix/funds-recoveries/{funds_recovery_id}/infractions` | `post-get-funds-recovery-infractions` | List funds recovery infractions [beta] | no |
| `GET /v1/pix/funds-recoveries/{funds_recovery_id}/refunds` | `post-get-funds-recovery-refunds` | List funds recovery refund requests [beta] | no |
| `GET /v1/pix/funds-recoveries/{funds_recovery_id}` | `post-get-funds-recovery` | Get funds recovery [beta] | no |
| `PATCH /v1/pix/funds-recoveries/{funds_recovery_id}` | `patch-funds-recovery` | Update funds recovery | no |
| `GET /v1/pix/funds-recoveries/{funds_recovery_id}/tracking-graph` | `get-refund-recovery` | Get tracking graph [beta] | no |
| `POST /v1/pix/funds-recoveries/{funds_recovery_id}/refund` | `post-refund-recovery` | Initiate refund funds recovery [beta] | no |
| `POST /v1/pix/funds-recoveries/{funds_recovery_id}/cancel` | `post-cancel-funds-recovery` | Cancel funds recovery [beta] | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v1/pix/funds-recoveries operationId=list-account-fund-recoveries -->
### `GET /v1/pix/funds-recoveries` — List account fund recoveries [beta]

- **operationId:** `list-account-fund-recoveries`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Funds recovery`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get all fund recoveries for an account

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `status` | query | no | string (schema `FundsRecoveryStatus`) |  | enum: ["CREATED", "AWAITING_ANALYSIS", "TRACKED", "ANALYSED", "REFUNDING", "COMPLETED", "CANCELLED"]; example: "CREATED" |
| `modified_after` | query | no | string | Only return fund recoveries modified at this datetime or after. Format = RFC 3339. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `modified_before` | query | no | string | Only return fund recoveries modified at this datetime or before.  Format = RFC 3339.  For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `limit` | query | no | integer | Maximum results to return. Default is `20`. Maximum is `200`. | default: 20; maximum: 200; example: 20 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - success | `application/json`: object (schema `ListAccountFundRecoveriesResponse`) |
| 400 | Invalid funds recovery ID | `application/json`: object (schema `message.Message`) |
| 403 | No permission | `application/json`: object (schema `message.Message`) |
| 404 | Not found | `application/json`: object (schema `message.Message`) |
| 504 | Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_more_elements` | boolean (schema `HasMoreElements`) | no | Are there more items? | example: true |
| `items` | array of object (schema `FundsRecovery`) | no |  |  |

##### Response 400

400 Example `Provider service error`:

```json
{
  "code": "EPDA0000",
  "message": "Invalid funds recovery ID format"
}
```

##### Response 403

403 Example `Participant no permission`:

```json
{
  "code": "EPDA0000",
  "message": "Participant does not have access to this funds recovery"
}
```

##### Response 404

404 Example `Funds recovery not found`:

```json
{
  "code": "EPDA0000",
  "message": "Funds recovery not found"
}
```

##### Response 504

504 Example `DICT timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout communicating with DICT"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPDA0000` | Invalid funds recovery ID format |
| 403 | `EPDA0000` | Participant does not have access to this funds recovery |
| 404 | `EPDA0000` | Funds recovery not found |
| 504 | `EPDA0000` | Timeout communicating with DICT |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;504`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v1/pix/funds-recoveries operationId=post-create-funds-recovery -->
### `POST /v1/pix/funds-recoveries` — Create funds recovery [beta]

- **operationId:** `post-create-funds-recovery`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Funds recovery`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates and establishes a new funds recovery to track and block diverted funds in Pix fraud cases. 
>
> The tracking follows the chain of subsequent transactions starting from the contested transaction.
>
> DICT manages the entire process. You define the initial `tracking_graph_parameters` and DICT
> executes tracking, prioritization, and blocking, then opens the infraction notifications that
> the receiving PSPs analyze.
>
> **Notes:**
>
>   * The contested transaction must have occurred less than **80 days** ago. This limit is the same for an original transaction and for a reversal transaction.
>   * Only the payer **of the contested transaction** can create funds recovery. When contesting a reversal, the payer is the participant that sent the reversal — that is, the PSP of the party who received the original transaction.
>   * `root_transaction_id` takes the **end-to-end ID** of the original transaction, or the **reversal end-to-end ID** when contesting a reversal.
>   * A reversal issued to settle an **operational flaw cannot be contested**. If the refund behind the reversal had `refund_reason` of `OPERATIONAL_FLAW`, DICT rejects the funds recovery as ineligible. This is the only restriction on contesting a reversal.
>   * When contesting a reversal, `situation_type` must be `OTHER`, which makes `report_details` mandatory.
>   * Recipient PSPs have **7 calendar days** to analyze infraction notifications
>   * Refund must be initiated within **72 hours** after analysis completion
>   * Once refunding starts, the process **cannot be cancelled**
>
> **Terminology:** the DICT operating manual refers to an original transaction as `pacs.008`
> and to a reversal transaction as `pacs.004`.
>
> Thie endpoint generates a [Pix funds recovery status changed](https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1) event.
>
> For more information refer to [Pix funds recovery](doc:pix-funds-recovery).

#### Request body

Required: no

> CheckRequest Body

**Content type `application/json`** — schema: object (schema `CreateFundsRecoveryRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `root_transaction_id` | string (schema `RootTransactionID`) | yes | Identifier of the contested transaction, 32 characters.<br><br>  * Contesting an original transaction — its **end-to-end ID**, which begins with `E`.<br>  * Contesting a reversal transaction — its **reversal end-to-end ID**, which begins with `D`.<br> | minLength: 32; maxLength: 32; example: "E1234567890123456789012345678901" |
| `situation_type` | string (schema `SituationType`) | yes | Situation type:<br>  * `SCAM` - Scam/fraud through social engineering<br>  * `ACCOUNT_TAKEOVER` - Unauthorized transaction without digital authentication<br>  * `COERCION` - Coercion crime (kidnapping, extortion)<br>  * `FRAUDULENT_ACCESS` - Fraudulent access and authorization (phishing, stolen password) \|<br>  * `OTHER` - Other cases. This option **REQUIRES** you pass `report_details`.<br>  * `UNKNOWN` - Unknown state<br><br>When the contested transaction is a reversal, the DICT operating manual requires<br>`situation_type` to be `OTHER`, which in turn makes `report_details` mandatory.<br> | enum: ["SCAM", "ACCOUNT_TAKEOVER", "COERCION", "FRAUDULENT_ACCESS", "OTHER", "UNKNOWN"] |
| `contact_information` | object (schema `ContactInformation`) | yes |  |  |
| `report_details` | string (schema `ReportDetails2`) | no | Details about report | maxLength: 500; example: "Details that can help the receiving participant to analyze the suspected violation" |
| `tracking_graph_parameters` | object (schema `TrackingGraphParameters`) | no | Graph parameters. <br><br>Higher values for `min_transaction_amount` and lower values for `max_transactions`,`max_hops`, and `hop_window` generate smaller and faster graphs. The opposite generates larger and more complete graphs.<br> |  |

Example `originalTransaction` (Contesting an original transaction):

```json
{
  "root_transaction_id": "E9876543210987654321098765432109",
  "situation_type": "COERCION",
  "contact_information": {
    "email": "security@yourbank.com",
    "phone": "+5511988888888"
  },
  "report_details": "Customer under coercion transferred R$ 10,000. Police report #12345/2025.",
  "tracking_graph_parameters": {
    "min_transaction_amount": 100,
    "max_transactions": 5,
    "hop_window": "PT2H",
    "max_hops": 5
  }
}
```

Example `reversalTransaction` (Contesting a reversal transaction):

```json
{
  "root_transaction_id": "D2721411220260831204766547975600",
  "situation_type": "OTHER",
  "contact_information": {
    "email": "security@yourbank.com",
    "phone": "+5511988888888"
  },
  "report_details": "Reversal of the root transaction of a funds recovery that was opened by the payer in order to defraud the payee.",
  "tracking_graph_parameters": {
    "min_transaction_amount": 100,
    "max_transactions": 5,
    "hop_window": "PT2H",
    "max_hops": 5
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created - synchronous success | `application/json`: object (schema `CreateFundsRecoveryResponse`) |
| 202 | Funds recovery creation continues asynchronously | `application/json`: object (schema `AsyncResponse`) |
| 400 | Invalid request data | `application/json`: object (schema `message.Message`) |
| 404 | Transaction not found.<br><br>This response is also returned when the transaction **does** exist in Pismo but the<br>requesting organization is not the payer of it. The root transaction is resolved from<br>the leg where the organization is the payer: a `PIX-OUT` for an original transaction,<br>or a `PIX-IN` of type `PIX-IN-REVERSAL` for a reversal. A plain `PIX-IN` is rejected,<br>since the party that received a transaction is not its payer.<br> | `application/json`: object (schema `message.Message`) |
| 409 | Recovery already exists | `application/json`: object (schema `message.Message`) |
| 422 | Transaction is not eligible for funds recovery | `application/json`: object (schema `message.Message`) |
| 504 | Timeout | `application/json`: object (schema `message.Message`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `status` | string (schema `FundsRecoveryStatus`) | no | Funds recovery status:<br>* `CREATED` - Recovery created, awaiting next action.<br>* `TRACKED` - The transaction tracking graph has been created.<br>* `AWAITING_ANALYSIS` - Awaiting analysis from receiver PSPs (deadline: 7 calendar days).<br>* `ANALYSED` - Analysis completed, ready for refund.<br>* `REFUNDING` - Refund process in progress.<br>* `COMPLETED` - Recovery successfully completed.<br>* `CANCELLED` - Recovery cancelled.<br> | enum: ["CREATED", "AWAITING_ANALYSIS", "TRACKED", "ANALYSED", "REFUNDING", "COMPLETED", "CANCELLED"]; example: "CREATED" |
| `root_transaction_id` | string (schema `RootTransactionID`) | no | Identifier of the contested transaction, 32 characters.<br><br>  * Contesting an original transaction — its **end-to-end ID**, which begins with `E`.<br>  * Contesting a reversal transaction — its **reversal end-to-end ID**, which begins with `D`.<br> | minLength: 32; maxLength: 32; example: "E1234567890123456789012345678901" |
| `situation_type` | string (schema `SituationType`) | no | Situation type:<br>  * `SCAM` - Scam/fraud through social engineering<br>  * `ACCOUNT_TAKEOVER` - Unauthorized transaction without digital authentication<br>  * `COERCION` - Coercion crime (kidnapping, extortion)<br>  * `FRAUDULENT_ACCESS` - Fraudulent access and authorization (phishing, stolen password) \|<br>  * `OTHER` - Other cases. This option **REQUIRES** you pass `report_details`.<br>  * `UNKNOWN` - Unknown state<br><br>When the contested transaction is a reversal, the DICT operating manual requires<br>`situation_type` to be `OTHER`, which in turn makes `report_details` mandatory.<br> | enum: ["SCAM", "ACCOUNT_TAKEOVER", "COERCION", "FRAUDULENT_ACCESS", "OTHER", "UNKNOWN"] |
| `reporter_participant` | string (schema `ReporterParticipant`) | no | Reporter participant ID | example: "12345678" |
| `contact_information` | object (schema `ContactInformation`) | no |  |  |
| `report_details` | string (schema `ReportDetails2`) | no | Details about report | maxLength: 500; example: "Details that can help the receiving participant to analyze the suspected violation" |
| `created_at` | string (schema `CreationDatetime`) | no | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `updated_at` | string (schema `UpdatedDatetime`) | no | Updated datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Response code | example: "EPDA0000" |
| `message` | string | no | Descriptive message about the asynchronous operation | example: "Operation will continue asynchronously. Monitor events for completion" |

202 Example `example`:

```json
{
  "code": "EPDA0169",
  "message": "Funds recovery creation will continue asynchronously. Monitor events for completion."
}
```

##### Response 400

400 Example `invalidData` (Invalid data):

```json
{
  "code": "EPDA0001",
  "message": "Invalid request payload"
}
```

400 Example `accountDoesNotOwnTransaction` (Account is not the payer of the contested transaction):

```json
{
  "code": "EPDA0192",
  "message": "AccountID does not belong to the payer transaction"
}
```

##### Response 404

404 Example `Transaction not found`:

```json
{
  "code": "EPDA0079",
  "message": "Transaction not found"
}
```

##### Response 409

409 Example `Recovery already exists`:

```json
{
  "code": "EPDA0190",
  "message": "An active funds recovery already exists for the given root transaction"
}
```

##### Response 422

422 Example `transactionTooOld` (Outside the 80-day eligibility window):

```json
{
  "code": "EPDA0191",
  "message": "Transaction is outside the 80-day eligibility period for funds recovery"
}
```

422 Example `invalidTransactionStatus` (Transaction is not settled):

```json
{
  "code": "EPDA0192",
  "message": "Funds recovery cannot be initiated for this transaction due to its current status"
}
```

##### Response 504

504 Example `Timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout communicating with DICT"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `EPDA0169` | Funds recovery creation will continue asynchronously. Monitor events for completion. |
| 400 | `EPDA0001` | Invalid request payload |
| 400 | `EPDA0192` | AccountID does not belong to the payer transaction |
| 404 | `EPDA0079` | Transaction not found |
| 409 | `EPDA0190` | An active funds recovery already exists for the given root transaction |
| 422 | `EPDA0191` | Transaction is outside the 80-day eligibility period for funds recovery |
| 422 | `EPDA0192` | Funds recovery cannot be initiated for this transaction due to its current status |
| 504 | `EPDA0000` | Timeout communicating with DICT |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-funds-recoveries-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;404;409;422;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-funds-recovery`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v1/pix/funds-recoveries/{funds_recovery_id}/infractions operationId=post-get-funds-recovery-infractions -->
### `GET /v1/pix/funds-recoveries/{funds_recovery_id}/infractions` — List funds recovery infractions [beta]

- **operationId:** `post-get-funds-recovery-infractions`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Funds recovery`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a list of infractions for a funds recovery

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `funds_recovery_id` | path | yes | string | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | List funds recovery infractions response | `application/json`: object (schema `ListFundsRecoveryInfractionsResponse`) |
| 400 | Invalid funds recovery ID | `application/json`: object (schema `message.Message`) |
| 403 | No permission | `application/json`: object (schema `message.Message`) |
| 404 | Not found | `application/json`: object (schema `message.Message`) |
| 504 | Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `response_date_time` | string (schema `ResponseDateTime`) | no | Response date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `infractions` | array of object (schema `InfractionReportResponse2`) | no |  |  |

##### Response 400

400 Example `Provider service error`:

```json
{
  "code": "EPDA0000",
  "message": "Invalid funds recovery ID format"
}
```

##### Response 403

403 Example `Participant no permission`:

```json
{
  "code": "EPDA0000",
  "message": "Participant does not have access to this funds recovery"
}
```

##### Response 404

404 Example `Funds recovery not found`:

```json
{
  "code": "EPDA0000",
  "message": "Funds recovery not found"
}
```

##### Response 504

504 Example `DICT timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout communicating with DICT"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPDA0000` | Invalid funds recovery ID format |
| 403 | `EPDA0000` | Participant does not have access to this funds recovery |
| 404 | `EPDA0000` | Funds recovery not found |
| 504 | `EPDA0000` | Timeout communicating with DICT |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;504`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v1/pix/funds-recoveries/{funds_recovery_id}/refunds operationId=post-get-funds-recovery-refunds -->
### `GET /v1/pix/funds-recoveries/{funds_recovery_id}/refunds` — List funds recovery refund requests [beta]

- **operationId:** `post-get-funds-recovery-refunds`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Funds recovery`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a list of refund requests for a funds recovery

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `funds_recovery_id` | path | yes | string | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | List funds recovery refunds response | `application/json`: object (schema `ListFundsRecoveryRefundsResponse`) |
| 400 | Invalid funds recovery ID | `application/json`: object (schema `message.Message`) |
| 403 | No permission | `application/json`: object (schema `message.Message`) |
| 404 | Not found | `application/json`: object (schema `message.Message`) |
| 504 | Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `response_date_time` | string (schema `ResponseDateTime`) | no | Response date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `infractions` | array of object (schema `Refund`) | no |  |  |

##### Response 400

400 Example `Provider service error`:

```json
{
  "code": "EPDA0000",
  "message": "Invalid funds recovery ID format"
}
```

##### Response 403

403 Example `Participant no permission`:

```json
{
  "code": "EPDA0000",
  "message": "Participant does not have access to this funds recovery"
}
```

##### Response 404

404 Example `Funds recovery not found`:

```json
{
  "code": "EPDA0000",
  "message": "Funds recovery not found"
}
```

##### Response 504

504 Example `DICT timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout communicating with DICT"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPDA0000` | Invalid funds recovery ID format |
| 403 | `EPDA0000` | Participant does not have access to this funds recovery |
| 404 | `EPDA0000` | Funds recovery not found |
| 504 | `EPDA0000` | Timeout communicating with DICT |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;504`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v1/pix/funds-recoveries/{funds_recovery_id} operationId=post-get-funds-recovery -->
### `GET /v1/pix/funds-recoveries/{funds_recovery_id}` — Get funds recovery [beta]

- **operationId:** `post-get-funds-recovery`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Funds recovery`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a funds recovery.
>
> Customers should use this endpoint to monitor and track progress, such as checking status after asynchronous operations or audit closed cases.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `useProvider` | query | no | boolean | Query directly from DICT or do a faster local query with automatic fallback to DICT? Default is `false`.<br> | default: false; example: true |
| `funds_recovery_id` | path | yes | string | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - success | `application/json`: object (schema `CreateFundsRecoveryResponse`) |
| 400 | Invalid funds recovery ID | `application/json`: object (schema `message.Message`) |
| 403 | No permission | `application/json`: object (schema `message.Message`) |
| 404 | Not found | `application/json`: object (schema `message.Message`) |
| 504 | Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `status` | string (schema `FundsRecoveryStatus`) | no | Funds recovery status:<br>* `CREATED` - Recovery created, awaiting next action.<br>* `TRACKED` - The transaction tracking graph has been created.<br>* `AWAITING_ANALYSIS` - Awaiting analysis from receiver PSPs (deadline: 7 calendar days).<br>* `ANALYSED` - Analysis completed, ready for refund.<br>* `REFUNDING` - Refund process in progress.<br>* `COMPLETED` - Recovery successfully completed.<br>* `CANCELLED` - Recovery cancelled.<br> | enum: ["CREATED", "AWAITING_ANALYSIS", "TRACKED", "ANALYSED", "REFUNDING", "COMPLETED", "CANCELLED"]; example: "CREATED" |
| `root_transaction_id` | string (schema `RootTransactionID`) | no | Identifier of the contested transaction, 32 characters.<br><br>  * Contesting an original transaction — its **end-to-end ID**, which begins with `E`.<br>  * Contesting a reversal transaction — its **reversal end-to-end ID**, which begins with `D`.<br> | minLength: 32; maxLength: 32; example: "E1234567890123456789012345678901" |
| `situation_type` | string (schema `SituationType`) | no | Situation type:<br>  * `SCAM` - Scam/fraud through social engineering<br>  * `ACCOUNT_TAKEOVER` - Unauthorized transaction without digital authentication<br>  * `COERCION` - Coercion crime (kidnapping, extortion)<br>  * `FRAUDULENT_ACCESS` - Fraudulent access and authorization (phishing, stolen password) \|<br>  * `OTHER` - Other cases. This option **REQUIRES** you pass `report_details`.<br>  * `UNKNOWN` - Unknown state<br><br>When the contested transaction is a reversal, the DICT operating manual requires<br>`situation_type` to be `OTHER`, which in turn makes `report_details` mandatory.<br> | enum: ["SCAM", "ACCOUNT_TAKEOVER", "COERCION", "FRAUDULENT_ACCESS", "OTHER", "UNKNOWN"] |
| `reporter_participant` | string (schema `ReporterParticipant`) | no | Reporter participant ID | example: "12345678" |
| `contact_information` | object (schema `ContactInformation`) | no |  |  |
| `report_details` | string (schema `ReportDetails2`) | no | Details about report | maxLength: 500; example: "Details that can help the receiving participant to analyze the suspected violation" |
| `created_at` | string (schema `CreationDatetime`) | no | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `updated_at` | string (schema `UpdatedDatetime`) | no | Updated datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

200 Example `example`:

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "CREATED",
  "root_transaction_id": "E1234567890123456789012345678901",
  "situation_type": "SCAM",
  "reporter_participant": "12345678",
  "contact_information": {
    "email": "fraud@yourbank.com",
    "phone": "+5511999999999"
  },
  "report_details": "Customer victim of fake seller scam. Purchase of R$ 1,000 not delivered.",
  "created_at": "2025-11-03T14:30:00Z",
  "updated_at": "2025-11-03T14:30:00Z"
}
```

##### Response 400

400 Example `Provider service error`:

```json
{
  "code": "EPDA0000",
  "message": "Invalid funds recovery ID format"
}
```

##### Response 403

403 Example `Participant no permission`:

```json
{
  "code": "EPDA0000",
  "message": "Participant does not have access to this funds recovery"
}
```

##### Response 404

404 Example `Funds recovery not found`:

```json
{
  "code": "EPDA0000",
  "message": "Funds recovery not found"
}
```

##### Response 504

504 Example `DICT timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout communicating with DICT"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPDA0000` | Invalid funds recovery ID format |
| 403 | `EPDA0000` | Participant does not have access to this funds recovery |
| 404 | `EPDA0000` | Funds recovery not found |
| 504 | `EPDA0000` | Timeout communicating with DICT |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;504`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-funds-recovery`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=PATCH path=/v1/pix/funds-recoveries/{funds_recovery_id} operationId=patch-funds-recovery -->
### `PATCH /v1/pix/funds-recoveries/{funds_recovery_id}` — Update funds recovery

- **operationId:** `patch-funds-recovery`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Funds recovery`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update some funds recovery fields. 
>
> **Note:** The update is only possible when the record is in `CREATED`, `TRACKED`, or `AWAITING_ANALYSIS` states.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `funds_recovery_id` | path | yes | string | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `x-tenant` | header | yes | string | Organization/tenant ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `x-account-id` | header | no | string | Pismo account ID | example: "8675309" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |
| `x-cid` | header | no | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> | example: "B20220921145635222303062944CA66F" |

#### Request body

Required: no

> Update funds recovery request body

**Content type `application/json`** — schema: object (schema `FundsRecoveryUpdateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `FundsRecoveryId`) | yes | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `contact_information` | object (schema `ContactInformation`) | no |  |  |
| `situation_type` | string (schema `SituationType`) | no | Situation type:<br>  * `SCAM` - Scam/fraud through social engineering<br>  * `ACCOUNT_TAKEOVER` - Unauthorized transaction without digital authentication<br>  * `COERCION` - Coercion crime (kidnapping, extortion)<br>  * `FRAUDULENT_ACCESS` - Fraudulent access and authorization (phishing, stolen password) \|<br>  * `OTHER` - Other cases. This option **REQUIRES** you pass `report_details`.<br>  * `UNKNOWN` - Unknown state<br><br>When the contested transaction is a reversal, the DICT operating manual requires<br>`situation_type` to be `OTHER`, which in turn makes `report_details` mandatory.<br> | enum: ["SCAM", "ACCOUNT_TAKEOVER", "COERCION", "FRAUDULENT_ACCESS", "OTHER", "UNKNOWN"] |
| `report_details` | string (schema `ReportDetails2`) | no | Details about report | maxLength: 500; example: "Details that can help the receiving participant to analyze the suspected violation" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | OK - success |  |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

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

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `Provider service communication error`:

```json
{
  "code": "EPDA0029",
  "message": "Internal errors while attempting to communicate with the provider service"
}
```

500 Example `Invalid client error`:

```json
{
  "code": "EPDG0005",
  "message": "Invalid Pix provider '{provider_name}'"
}
```

500 Example `Failed marshalling object`:

```json
{
  "code": "EPDG0006",
  "message": "Failed to marshal JSON object"
}
```

500 Example `Failed unmarshalling object`:

```json
{
  "code": "EPDG0007",
  "message": "Failed to unmarshal JSON object"
}
```

500 Example `Error reading response data`:

```json
{
  "code": "EPDG0010",
  "message": "I/O error while reading response data: '{details}'"
}
```

500 Example `Provider service error`:

```json
{
  "code": "EPDG0016",
  "message": "Provider service returned an internal error while trying to access the resource",
  "details": {
    "external": [
      {
        "code": "PBE315",
        "message": "Generic error"
      }
    ]
  }
}
```

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
| 500 | `EPDA0029` | Internal errors while attempting to communicate with the provider service |
| 500 | `EPDG0005` | Invalid Pix provider '{provider_name}' |
| 500 | `EPDG0006` | Failed to marshal JSON object |
| 500 | `EPDG0007` | Failed to unmarshal JSON object |
| 500 | `EPDG0010` | I/O error while reading response data: '{details}' |
| 500 | `EPDG0016` | Provider service returned an internal error while trying to access the resource |
| 500 | `PBE315` | Generic error |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 504 | `EPDA0000` | Timeout while executing the request |
| 504 | `EPDG0000` | Timeout while executing the request |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;403;500;502;504`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v1/pix/funds-recoveries/{funds_recovery_id}/tracking-graph operationId=get-refund-recovery -->
### `GET /v1/pix/funds-recoveries/{funds_recovery_id}/tracking-graph` — Get tracking graph [beta]

- **operationId:** `get-refund-recovery`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Funds recovery`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get tracking graphs.
>
> Retrieves the tracking graph that maps the chain of subsequent transactions originated from the dispersion of fraudulent funds.
>
> The graph identifies people, accounts, and transactions involved in the movement of diverted funds.
>
> You can call this endpoint if you are:
>  * The funds recovery creator participant
>  * Counterparty participants who received related infraction notifications

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `funds_recovery_id` | path | yes | string | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `useProvider` | query | no | string | Search refund in provider? Default is `false`. | example: "true" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - success | `application/json`: object (schema `TrackingGraphResponse`) |
| 400 | Invalid ID format | `application/json`: object (schema `message.Message`) |
| 404 | Funds recovery or tracking graph not found | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `funds_recovery_id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `parameters` | object (schema `TrackingGraphParameters`) | no | Graph parameters. <br><br>Higher values for `min_transaction_amount` and lower values for `max_transactions`,`max_hops`, and `hop_window` generate smaller and faster graphs. The opposite generates larger and more complete graphs.<br> |  |
| `persons` | array of object (schema `Person`) | no | Identified people (account holders) |  |
| `accounts` | array of object (schema `Account`) | no | Identified transactional accounts |  |
| `transactions` | array of object (schema `Transaction`) | no | PIX transactions that compose the graph |  |
| `summary` | object (schema `GraphSummary`) | no | Graph summary |  |
| `created_at` | string (schema `CreationDatetime`) | no | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

200 Example `example`:

```json
{
  "graph_id": "graph-uuid-001",
  "funds_recovery_id": "550e8400-e29b-41d4-a716-446655440000",
  "parameters": {
    "min_transaction_amount": 100,
    "max_transactions": 50,
    "hop_window": "PT1H",
    "max_hops": 3
  },
  "persons": [
    {
      "id": "1",
      "type": "NATURAL_PERSON",
      "created_at": "2025-01-10T10:00:00Z"
    },
    {
      "id": "2",
      "type": "NATURAL_PERSON",
      "created_at": "2023-05-15T10:00:00Z"
    }
  ],
  "accounts": [
    {
      "id": "1",
      "owner_id": "1",
      "participant": "12345678",
      "created_at": "2024-01-10T10:00:00Z"
    },
    {
      "id": "2",
      "owner_id": "2",
      "participant": "87654321",
      "created_at": "2023-05-15T10:00:00Z"
    }
  ],
  "transactions": [
    {
      "id": "E1234567890123456789012345678901",
      "debtor_account_id": "1",
      "creditor_account_id": "2",
      "amount": 1000,
      "refundable_amount": 900,
      "settlement_time": "2025-10-23T09:00:00Z",
      "hop": 0
    },
    {
      "id": "E2345678901234567890123456789012",
      "debtor_account_id": "2",
      "creditor_account_id": "3",
      "amount": 500,
      "refundable_amount": 500,
      "settlement_time": "2025-10-23T09:05:00Z",
      "hop": 1
    }
  ],
  "summary": {
    "total_transactions": 2,
    "total_amount": 1500,
    "max_hop_reached": 1
  }
}
```

##### Response 400

400 Example `Invalid ID format`:

```json
{
  "code": "EPDA0000",
  "message": "Invalid funds recovery ID format"
}
```

##### Response 404

404 Example `Recovery not found`:

```json
{
  "code": "EPDA0000",
  "message": "Funds recovery not found or access denied"
}
```

404 Example `Graph not found`:

```json
{
  "code": "EPDA0000",
  "message": "Tracking graph not found"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPDA0000` | Invalid funds recovery ID format |
| 404 | `EPDA0000` | Funds recovery not found or access denied |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v1/pix/funds-recoveries/{funds_recovery_id}/refund operationId=post-refund-recovery -->
### `POST /v1/pix/funds-recoveries/{funds_recovery_id}/refund` — Initiate refund funds recovery [beta]

- **operationId:** `post-refund-recovery`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Funds recovery`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Initiate funds recovery refund stage, after the recipient PSPs have analyzed (`status` = `ANALYSED`) all the infraction notifications. This is the process' final step where funds are effectively returned to the victim's account.
>
> Before requesting the refund, make sure that:
>
>   * The recovery status = `ANALYSED`
>   * You are the **creator** recovery participant
>   * You are within the **72-hour** deadline after receiving the `FUNDS_RECOVERY_ANALYSED` event
>   * There is at least one **accepted** infraction notification (status = `ACCEPTED`)
>
> Thie endpoint generates a [Pix funds recovery status changed](https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1) event.
>
> For more information refer to [Pix funds recovery](doc:pix-funds-recovery).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `funds_recovery_id` | path | yes | string | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - synchronous success | `application/json`: object (schema `InitiateFundsRecoveryResponse`) |
| 202 | Ok - Asynchronous success | `application/json`: object (schema `AsyncResponse`) |
| 400 | Invalid status | `application/json`: object (schema `message.Message`) |
| 404 | No accepted infractions | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `funds_recovery_id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `status` | string (schema `FundsRecoveryStatus`) | no | Funds recovery status:<br>* `CREATED` - Recovery created, awaiting next action.<br>* `TRACKED` - The transaction tracking graph has been created.<br>* `AWAITING_ANALYSIS` - Awaiting analysis from receiver PSPs (deadline: 7 calendar days).<br>* `ANALYSED` - Analysis completed, ready for refund.<br>* `REFUNDING` - Refund process in progress.<br>* `COMPLETED` - Recovery successfully completed.<br>* `CANCELLED` - Recovery cancelled.<br> | enum: ["CREATED", "AWAITING_ANALYSIS", "TRACKED", "ANALYSED", "REFUNDING", "COMPLETED", "CANCELLED"]; example: "CREATED" |
| `total_refunds_created` | integer | no | Total refunds created | example: 4 |
| `updated_at` | string (schema `UpdatedDatetime`) | no | Updated datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Response code | example: "EPDA0000" |
| `message` | string | no | Descriptive message about the asynchronous operation | example: "Operation will continue asynchronously. Monitor events for completion" |

202 Example `example`:

```json
{
  "Asynchrnous success": {
    "value": {
      "code": "EPDA0000",
      "message": "Refund funds recovery flow will continue asynchronously"
    }
  }
}
```

##### Response 400

400 Example `Invalid status`:

```json
{
  "code": "EPDA0000",
  "message": "Refund deadline expired. Must initiate refund within 72 hours after ANALYSED status",
  "details": {
    "analyzed_at": "2025-10-13T10:00:00Z",
    "deadline": "2025-10-16T10:00:00Z",
    "current_time": "2025-10-17T12:00:00Z"
  }
}
```

##### Response 404

404 Example `No accepted infractions found`:

```json
{
  "code": "EPDA0000",
  "message": "No accepted infractions found. Cannot initiate refund without accepted infractions"
}
```

404 Example `Recovery not found`:

```json
{
  "code": "EPDA0000",
  "message": "Funds recovery not found"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `EPDA0000` | Refund funds recovery flow will continue asynchronously |
| 400 | `EPDA0000` | Refund deadline expired. Must initiate refund within 72 hours after ANALYSED status |
| 404 | `EPDA0000` | No accepted infractions found. Cannot initiate refund without accepted infractions |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-funds-recoveries-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;404`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-funds-recovery`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v1/pix/funds-recoveries/{funds_recovery_id}/cancel operationId=post-cancel-funds-recovery -->
### `POST /v1/pix/funds-recoveries/{funds_recovery_id}/cancel` — Cancel funds recovery [beta]

- **operationId:** `post-cancel-funds-recovery`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Funds recovery`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel funds recovery 
>
> Statuses that allow cancellation:
>
>   | Status | Can Cancel? | Note |
>   |--------|-------------|------|
>   | `CREATED` | Yes | Before any processing |
>   | `TRACKED` | Yes | After graph creation |
>   | `AWAITING_ANALYSIS` | Yes | During analysis period (7 days) |
>   | `ANALYSED` | Yes | After analysis completed, before refund |
>   | `REFUNDING` | No | Refunds already started - irreversible process |
>   | `COMPLETED` | No | Process already finished |
>
> When a recovery is cancelled:
>   * Status changes to `CANCELLED`
>   * All linked infraction notifications are automatically cancelled
>   * Receiver PSPs must unblock the resources that were blocked
>   * Tracking graph remains available for audit
>   * Process cannot be undone (but new recovery can be created)
>
> Thie endpoint generates a [Pix funds recovery status changed](https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `funds_recovery_id` | path | yes | string | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - synchronous success | `application/json`: object (schema `CancelFundsRecoveryResponse`) |
| 202 | Ok - Asynchronous success | `application/json`: object (schema `AsyncResponse`) |
| 400 | Invalid funds recovery ID | `application/json`: object (schema `message.Message`) |
| 404 | Not found | `application/json`: object (schema `message.Message`) |
| 409 | Not allowed | `application/json`: object (schema `message.Message`) |
| 504 | Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `status` | string (schema `FundsRecoveryStatus`) | no | Funds recovery status:<br>* `CREATED` - Recovery created, awaiting next action.<br>* `TRACKED` - The transaction tracking graph has been created.<br>* `AWAITING_ANALYSIS` - Awaiting analysis from receiver PSPs (deadline: 7 calendar days).<br>* `ANALYSED` - Analysis completed, ready for refund.<br>* `REFUNDING` - Refund process in progress.<br>* `COMPLETED` - Recovery successfully completed.<br>* `CANCELLED` - Recovery cancelled.<br> | enum: ["CREATED", "AWAITING_ANALYSIS", "TRACKED", "ANALYSED", "REFUNDING", "COMPLETED", "CANCELLED"]; example: "CREATED" |
| `updated_at` | string (schema `UpdatedDatetime`) | no | Updated datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Response code | example: "EPDA0000" |
| `message` | string | no | Descriptive message about the asynchronous operation | example: "Operation will continue asynchronously. Monitor events for completion" |

202 Example `Asynchrnous success`:

```json
{
  "code": "EPDA0000",
  "message": "Refund funds recovery flow will continue asynchronously"
}
```

##### Response 400

400 Example `Invalid funds recovery ID`:

```json
{
  "code": "EPDA0000",
  "message": "Invalid funds recovery ID format"
}
```

##### Response 404

404 Example `Funds recovery not found`:

```json
{
  "code": "EPDA0000",
  "message": "Funds recovery not found"
}
```

##### Response 409

409 Example `Status does not allow cancellation`:

```json
{
  "code": "EPDA0000",
  "message": "Cannot cancel funds recovery in current status"
}
```

##### Response 504

504 Example `DICT timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout communicating with DICT"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `EPDA0000` | Refund funds recovery flow will continue asynchronously |
| 400 | `EPDA0000` | Invalid funds recovery ID format |
| 404 | `EPDA0000` | Funds recovery not found |
| 409 | `EPDA0000` | Cannot cancel funds recovery in current status |
| 504 | `EPDA0000` | Timeout communicating with DICT |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-funds-recoveries-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;404;409;504`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/FundsRecovery -->
### Schema `FundsRecovery`

Pointer: `#/components/schemas/FundsRecovery`. Type: object (schema `FundsRecovery`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `status` | string (schema `FundsRecoveryStatus`) | no | Funds recovery status:<br>* `CREATED` - Recovery created, awaiting next action.<br>* `TRACKED` - The transaction tracking graph has been created.<br>* `AWAITING_ANALYSIS` - Awaiting analysis from receiver PSPs (deadline: 7 calendar days).<br>* `ANALYSED` - Analysis completed, ready for refund.<br>* `REFUNDING` - Refund process in progress.<br>* `COMPLETED` - Recovery successfully completed.<br>* `CANCELLED` - Recovery cancelled.<br> | enum: ["CREATED", "AWAITING_ANALYSIS", "TRACKED", "ANALYSED", "REFUNDING", "COMPLETED", "CANCELLED"]; example: "CREATED" |
| `root_transaction_id` | string (schema `RootTransactionID`) | no | Identifier of the contested transaction, 32 characters.<br><br>  * Contesting an original transaction — its **end-to-end ID**, which begins with `E`.<br>  * Contesting a reversal transaction — its **reversal end-to-end ID**, which begins with `D`.<br> | minLength: 32; maxLength: 32; example: "E1234567890123456789012345678901" |
| `situation_type` | string (schema `SituationType`) | no | Situation type:<br>  * `SCAM` - Scam/fraud through social engineering<br>  * `ACCOUNT_TAKEOVER` - Unauthorized transaction without digital authentication<br>  * `COERCION` - Coercion crime (kidnapping, extortion)<br>  * `FRAUDULENT_ACCESS` - Fraudulent access and authorization (phishing, stolen password) \|<br>  * `OTHER` - Other cases. This option **REQUIRES** you pass `report_details`.<br>  * `UNKNOWN` - Unknown state<br><br>When the contested transaction is a reversal, the DICT operating manual requires<br>`situation_type` to be `OTHER`, which in turn makes `report_details` mandatory.<br> | enum: ["SCAM", "ACCOUNT_TAKEOVER", "COERCION", "FRAUDULENT_ACCESS", "OTHER", "UNKNOWN"] |
| `reporter_participant` | string (schema `ReporterParticipant`) | no | Reporter participant ID | example: "12345678" |
| `report_details` | string (schema `ReportDetails2`) | no | Details about report | maxLength: 500; example: "Details that can help the receiving participant to analyze the suspected violation" |
| `contact_information` | object (schema `ContactInformation`) | no |  |  |
| `created_at` | string (schema `CreationDatetime`) | no | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `updated_at` | string (schema `UpdatedDatetime`) | no | Updated datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

<!-- schema: #/components/schemas/message.Message -->
### Schema `message.Message`

Pointer: `#/components/schemas/message.Message`. Type: object (schema `message.Message`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

<!-- schema: #/components/schemas/ContactInformation -->
### Schema `ContactInformation`

Pointer: `#/components/schemas/ContactInformation`. Type: object (schema `ContactInformation`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `phone` | string | yes | Contact phone number | maxLength: 16; example: "551154874551" |
| `email` | string | yes | Contact email | maxLength: 77; example: "polly_ester@email.com" |

<!-- schema: #/components/schemas/TrackingGraphParameters -->
### Schema `TrackingGraphParameters`

Pointer: `#/components/schemas/TrackingGraphParameters`. Type: object (schema `TrackingGraphParameters`).

> Graph parameters. 
>
> Higher values for `min_transaction_amount` and lower values for `max_transactions`,`max_hops`, and `hop_window` generate smaller and faster graphs. The opposite generates larger and more complete graphs.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `min_transaction_amount` | number | yes | Minimum amount in Brazilian reals to include transaction in tracking. |  |
| `max_transactions` | integer | yes | Maximum number of transactions to track |  |
| `hop_window` | string | yes | The window duration between transactions<br><br>  * `PT30M` -  30 minutes<br>  * `PT45M` - 45 minutes<br>  * `PT1H` - 1 hour<br>  * `PT2H` - 2 hours<br>  <br>  <br> | example: "PT2H" |
| `max_hops` | integer | yes | Maximum tracking depth, in graph layers. | default: 2; minimum: 1; maximum: 10; example: 5 |

<!-- schema: #/components/schemas/InfractionReportResponse2 -->
### Schema `InfractionReportResponse2`

Pointer: `#/components/schemas/InfractionReportResponse2`. Type: object (schema `InfractionReportResponse2`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `InfractionReportID`) | yes | Infraction report ID (UUID) | format: "uuid"; maxLength: 36; example: "cfdff46e-5d58-45b8-b7aa-591a65f74444" |
| `transaction_id` | string (schema `InfractionTransactionID`) | yes | Original transaction's end to end ID. | example: "E9999901012341234123412345678900" |
| `reason` | string (schema `InfractionReason`) | yes | Reason for opening infraction report | enum: ["REFUND_REQUEST", "REFUND_CANCELLED"]; example: "REFUND_REQUEST" |
| `situation_type` | string (schema `InfractionReportSituation`) | yes | What gave rise to the infraction notification | enum: ["SCAM", "ACCOUNT_TAKEOVER", "COERCION", "FRAUDULENT_ACCESS", "OTHER", "UNKNOWN"]; example: "SCAM" |
| `status` | string (schema `InfractionReportStatus`) | yes | Infraction report status | enum: ["OPEN", "ACKNOWLEDGED", "CLOSED", "CANCELLED"]; example: "OPEN" |
| `reporter_participant` | string (schema `InfractionReporterParticipant`) | yes | Transaction payer participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value.<br> | format: "number"; example: "78265328" |
| `counterparty_participant` | string (schema `InfractionCounterpartyParticipant`) | yes | Transaction recipient participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value.<br> | format: "number"; example: "78265328" |
| `creation_time` | string (schema `BacenCreationDateTime`) | no | Date of infraction report creation. RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `last_modified` | string (schema `BacenLastModifiedDateTime`) | yes | Date of infraction report modification. RFC 3339  date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `details` | string (schema `InfractionDetails`) | no | Details that can help the receiving participant to analyze the suspected violation<br> | maxLength: 2000; example: "Details about infraction" |
| `contact_information` | object (schema `ContactInformation`) | no |  |  |
| `funds_recovery_id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `infraction_amount` | number (schema `InfractionAmount`) | no | Infraction Amount. | example: 1050.44 |
| `fraud_marker_id` | string (schema `FraudMarkerID`) | no | Fraud marker ID | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |

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

<!-- schema: #/components/schemas/Person -->
### Schema `Person`

Pointer: `#/components/schemas/Person`. Type: object (schema `Person`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Person pseudo-identifier (protects CPF/CNPJ) | example: "1" |
| `type` | string (schema `PersonType`) | no | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `created_at` | string | no | Person record creation date | format: "date-time"; example: "2025-01-10T10:00:00Z" |

<!-- schema: #/components/schemas/Account -->
### Schema `Account`

Pointer: `#/components/schemas/Account`. Type: object (schema `Account`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Account pseudo-identifier | example: "1" |
| `owner_id` | string | no | Reference to holder in persons array | example: "1" |
| `participant` | string | no | Participant ISPB (8 digits) number | pattern: "^\\\\d{8}$"; example: "12345678" |
| `created_at` | string | no | Account opening date (identifies mule accounts) | format: "date-time"; example: "2024-01-10T10:00:00Z" |

<!-- schema: #/components/schemas/Transaction -->
### Schema `Transaction`

Pointer: `#/components/schemas/Transaction`. Type: object (schema `Transaction`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Transaction identifier, 32 characters. The **end-to-end ID** of an original transaction,<br>which begins with `E`, or the **reversal end-to-end ID** of a reversal transaction,<br>which begins with `D`.<br> | pattern: "^[ED][A-Za-z0-9]{31}$"; example: "E1234567890123456789012345678901" |
| `debtor_account_id` | string | no | Debtor account ID | example: "156704" |
| `creditor_account_id` | string | no | Creditor account ID | example: "257938" |
| `amount` | number | no | Original transaction amount | format: "decimal"; example: 1000 |
| `refundable_amount` | number | no | Amount available for refund (may be less than original) | format: "decimal"; example: 900 |
| `settlement_time` | string | no | Transaction settlement timestamp. RFC 3339 format. | format: "date-time"; example: "2025-10-23T09:00:00Z" |

<!-- schema: #/components/schemas/GraphSummary -->
### Schema `GraphSummary`

Pointer: `#/components/schemas/GraphSummary`. Type: object (schema `GraphSummary`).

> Graph summary

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `total_transactions` | integer | no | Total number of transactions in the graph | example: 2 |
| `total_amount` | number | no | Total amount of all transactions | format: "decimal"; example: 1500 |
| `max_hop_reached` | integer | no | Maximum hop depth reached in the graph | example: 1 |

<!-- schema: #/components/schemas/message.DetailMessage -->
### Schema `message.DetailMessage`

Pointer: `#/components/schemas/message.DetailMessage`. Type: object (schema `message.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `message.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `message.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `message.PayloadMessage`) | no |  |  |

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
| `api-specs/Instant_payments_-_Pix_management.yaml` | tag `Funds recovery`: GET /v1/pix/funds-recoveries, POST /v1/pix/funds-recoveries, GET /v1/pix/funds-recoveries/{funds_recovery_id}/infractions, GET /v1/pix/funds-recoveries/{funds_recovery_id}/refunds, GET /v1/pix/funds-recoveries/{funds_recovery_id}, PATCH /v1/pix/funds-recoveries/{funds_recovery_id}, GET /v1/pix/funds-recoveries/{funds_recovery_id}/tracking-graph, POST /v1/pix/funds-recoveries/{funds_recovery_id}/refund, POST /v1/pix/funds-recoveries/{funds_recovery_id}/cancel | https://github.com/PismoDevEx/pismo-api-specs | `7d7fee078ccf5569…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-epda` — Error codes: EPDA
- `KU-ERR-codes-epdg` — Error codes: EPDG
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-PAY-pix-funds-recovery` — Pix funds recovery [beta]
