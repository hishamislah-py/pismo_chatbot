---
ku_id: KU-API-card-issuing-disputes--disputes-part-02
title: 'API reference: Card issuing - Disputes — Disputes (part 2 of 2)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Disputes.yaml
  sha256: 5c1d5513e1f3a4d1daa4d6bd654885c4edfeb5135eaa60b50f1a74d62031baad
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
operations:
- get-v1-disputes-count
- post-v1-disputes-acknowledge
- post-v1-disputes-close
- network-reversal
related_kus: []
specification_version: 1.0.0
---

# API reference: Card issuing - Disputes — Disputes (part 2 of 2)

**KU ID:** `KU-API-card-issuing-disputes--disputes-part-02` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Disputes` in `api-specs/Card_issuing_-_Disputes.yaml` (“Card issuing - Disputes”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to create and manage disputes

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/disputes/count` | `get-v1-disputes-count` | Count disputes per group status | no |
| `POST /v1/disputes/acknowledge` | `post-v1-disputes-acknowledge` | Acknowledge dispute | no |
| `POST /v1/disputes/close` | `post-v1-disputes-close` | Close dispute | no |
| `POST /v1/disputes/network-reversal` | `network-reversal` | Network chargeback reversal | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v1/disputes/count operationId=get-v1-disputes-count -->
### `GET /v1/disputes/count` — Count disputes per group status

- **operationId:** `get-v1-disputes-count`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Disputes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Count disputes aggregated by group status.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | query | no | number | Account ID. **REQUIRED** if `beginDate` not provided. | format: "int64"; minimum: 1; example: 123 |
| `beginDate` | query | no | string | Beginning date filter,  format = yyyy-mm-dd. **REQUIRED** if `accountId` not provided. | example: "2020-01-31" |
| `endDate` | query | no | string | End date filter, format = yyyy-mm-dd. | example: "2020-02-01" |
| `isNetwork` | query | no | boolean | Return only network disputes? Default is `false`. | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `CountDisputes`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `OPEN` | number | no | Number of disputes in status group `OPEN`. | example: 1 |
| `APPROVED` | number | no | Number of disputes in status group `APPROVED`. | example: 0 |
| `DENIED` | number | no | Number of disputes in status group `DENIED`. | example: 2 |
| `CARDNETWORK_CHARGEBACK` | number | no | Number of disputes in status group `CARDNETWORK_CHARGEBACK`. | example: 0 |
| `ANALYSING` | number | no | Number of disputes in status group `ANALYSING`. | example: 1 |
| `CARDNETWORK_SECOND_PRESENTMENT` | number | no | Number of disputes in status group `CARDNETWORK_SECOND_PRESENTMENT`. | example: 0 |
| `FAILED` | number | no | Number of disputes in status group `FAILED`. | example: 1 |
| `CARDNETWORK_PREARBITRATION` | number | no | Number of disputes in status group `CARDNETWORK_PREARBITRATION`. | example: 0 |
| `RESEND` | number | no | Number of disputes in status group `RESEND`. | example: 1 |
| `LOSS` | number | no | Number of disputes in status group `LOSS`. | example: 1 |
| `WON` | number | no | Number of disputes in status group `WON`. | example: 1 |
| `REJECTED` | number | no | Number of disputes in status group `REJECTED`. | example: 1 |
| `FAILED_PROCESSED` | number | no | Number of disputes in status group FAILED_PROCESSED. | example: 1 |

200 Example `Dispute count`:

```json
{
  "OPEN": 1,
  "APPROVED": 0,
  "DENIED": 2,
  "CARDNETWORK_CHARGEBACK": 3,
  "ANALYSING": 1,
  "CARDNETWORK_SECOND_PRESENTMENT": 2,
  "FAILED": 0,
  "CARDNETWORK_PREARBITRATION": 1,
  "RESEND": 0,
  "LOSS": 1,
  "WON": 4,
  "REJECTED": 2,
  "FAILED_PROCESSED": 0
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v1/disputes/acknowledge operationId=post-v1-disputes-acknowledge -->
### `POST /v1/disputes/acknowledge` — Acknowledge dispute

- **operationId:** `post-v1-disputes-acknowledge`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Disputes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Mark a processed installment. This feature is only available for Mastercard.

#### Request body

Required: no

**Content type `application/json`** — schema: array of object

_No fields declared in the schema._

Example `Acknowledge a Dispute with success`:

```json
[
  {
    "dispute_id": 0,
    "dispute_installment_id": 0,
    "network_brand_type": "Mastercard"
  }
]
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `Response with success`:

```json
[
  {
    "dispute_id": 0,
    "dispute_installment_id": 0,
    "error": false,
    "reason": "string"
  }
]
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v1/disputes/close operationId=post-v1-disputes-close -->
### `POST /v1/disputes/close` — Close dispute

- **operationId:** `post-v1-disputes-close`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Disputes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Close a dispute. This feature is only available for Mastercard.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `ProcessedDataRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dispute_id` | number (schema `DisputeID`) | yes | Dispute ID | example: 48670 |
| `close_claim_reason_code` | string (schema `closeClaimReasonCode`) | yes | Reason code for closing the claim. **REQUIRED** when network is Mastercard.<br><br>`10` = Won<br>`20` = Lost<br>`30` = Lost, below threshold<br>`40` = Cardholder liable<br> | enum: ["10", "20", "30", "40"] |
| `dispute_installment_id` | number | no | Related dispute installment ID. If not passed, first installment is used. | example: 1 |
| `open_claim_due_date` | string | no | Due date for opening the claim. Optional when network is Mastercard. | format: "date"; example: "2022-01-01" |

Example `Close a Dispute at Mastercard`:

```json
{
  "dispute_id": 1,
  "dispute_installment_id": 1,
  "close_claim_reason_code": "10",
  "open_claim_due_date": "2022-01-01"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProcessedDataResponse`) |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 422 | Unprocessable entity |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dispute_id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `dispute_installment_id` | number | no | Related dispute installment ID. If not passed, first Installment is used. | example: 1 |
| `close_claim_reason_code` | string (schema `closeClaimReasonCode`) | no | Reason code for closing the claim. **REQUIRED** when network is Mastercard.<br><br>`10` = Won<br>`20` = Lost<br>`30` = Lost, below threshold<br>`40` = Cardholder liable<br> | enum: ["10", "20", "30", "40"] |
| `open_claim_due_date` | string | no | Due date for opening the claim. Optional when network is Mastercard. | format: "date"; example: "2022-01-01" |
| `claim_id` | string | no | Network claim identifier. | example: "00058678" |

200 Example `Request sent with success - Mastercard`:

```json
{
  "dispute_id": 1,
  "dispute_installment_id": 1,
  "close_claim_reason_code": "10",
  "open_claim_due_date": "2022-01-01",
  "claim_id": "00058678"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;422`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v1/disputes/network-reversal operationId=network-reversal -->
### `POST /v1/disputes/network-reversal` — Network chargeback reversal

- **operationId:** `network-reversal`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Disputes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel a chargeback.
>
> You can use this endpoint to cancel a chargeback if you realize it is in error.
>
> Note: You can reverse a chargeback after the Global Clearing Management System has processed it.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | no | string | Organization/tenant ID |  |
| `x-cid` | header | no | string | The Correlation IDentifier field links related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |

#### Request body

Required: yes

> Network reversal object

**Content type `application/json`** — schema: object (schema `networkReversalRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dispute_id` | number (schema `DisputeID`) | yes | Dispute ID | example: 48670 |
| `installment_id` | number | no | Dispute installment ID | example: 686994 |
| `reversal_reason` | string | no | Reason for reversal - 5000 chars maximum | maxLength: 5000; example: "Chargeback not valid because customer now recognizes it" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `FullDisputeResponse`) |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 422 | Unprocessable entity |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID. | example: "TN-34778262-f4f0-464d-b4c6-a14exxxxxxxx" |
| `account_id` | number (schema `AccountID`) | no | Pismo account ID | example: 577830 |
| `authorization_id` | integer | no | Authorization ID. | example: 4352243 |
| `disputed_amount` | number (schema `DisputedAmount`) | no | Disputed amount. | example: 10 |
| `comment` | string (schema `Comment`) | no | Client custom dispute comment.<br><br>**REQUIRED** for Visa partial dispute to explain why partial.<br> | maxLength: 5000; nullable: true; example: "Custom comment" |
| `airport_tax` | boolean | no | For ELO card network, should dispute for airport tax be created? Default is `true` for ELO. | example: false |
| `airport_tax_partial` | boolean | no | For ELO card network, should airport tax be partially disputed? Default is `false`. | default: false; example: false |
| `airport_tax_amount` | number | no | Airport tax amount to be disputed. **REQUIRED** if `airport_tax_partial` is `true`. | example: 25 |
| `dispute_reason` | number (schema `reasonCode`) | no | Each card network, such as Visa or Mastercard, defines and maintains their own unique set of reason codes, which banks that issue credit and debit cards under their brands apply to disputes. Here's a reason code [quick reference](https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide) for the major credit card networks.<br><br>For Visa, this would be either `10` (fraud - card present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).<br><br>For more infomation, refer to the [Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/chargeback-management-guidelines-for-visa-merchants-vbs-19-may-16-%20v2.pdf) or [Mastercard](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf) chargeback quides.<br><br>For example - `4853` (Mastercard - cardholder dispute), `12` (Visa - processing error) or `72` (ELO - denied authorization)<br> | example: 4853 |
| `modality` | number | no | Dispute *modality* - legacy term for reason code to file the dispute. | example: 4855 |
| `dispute_status` | string (schema `DisputeStatus`) | no | Dispute status enums.<br> | enum: ["OPENED", "PENDING", "CANCELED", "FAILED", "CHARGEBACK_REJECTED", "CHARGEBACK_CREATED", "CHARGEBACK_ACCEPTED", "CHARGEBACK_CLOSED", "SECOND_PRESENTMENT", "PRE_ARBITRATION_OPENED", "PRE_ARBITRATION_ACCEPTED", "PRE_ARBITRATION_DECLINED", "PRE_ARBITRATION_RECALL", "PRE_ARB_ALLOCATION_OPENED", "FAILED_PRE_ARBITRATION", "PRE_ARB_ALLOCATION_ACCEPTED", "PRE_ARB_ALLOCATION_DECLINED", "PRE_ARB_ALLOCATION_RECALLED", "FAILED_DECLINE_PRE_ARB", "FAILED_ACCEPT_PRE_ARB", "FAILED_ON_CLOSE", "EXPIRED", "ISSUER_LOSS", "MIGRATION", "FAILED_MIGRATION"]; example: "PENDING" |
| `dispute_group_status` | string (schema `DisputeGroupStatus`) | no | Group status enums<br> | enum: ["OPEN", "APPROVED", "DENIED", "CARDNETWORK_CHARGEBACK", "ANALYSING", "CARDNETWORK_SECOND_PRESENTMENT", "FAILED", "CARDNETWORK_PREARBITRATION", "RESEND", "LOSS", "WON", "REJECTED", "FAILED_PROCESSED"]; example: "OPEN" |
| `timeline` | string | no | Client custom timeline information. | example: "{ \\"data\\": \\"test\\"}" |
| `protocol` | string (schema `Protocol`) | no | Client custom protocol ID. This is primarily for you to internally identify a request. If not provided, Pismo creates a CID (correlation ID) field for this purpose.<br> | maxLength: 500; example: "20251128111532456" |
| `metadata` | object (schema `Metadata`) | no | Can be used for caller's dispute information and process. Objects and name-value pairs.<br><br> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"field1": "value", "field2": "value"} |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime, format = yyyy-mm-dd hh:mm:ss" | example: "2024-10-18 11:21:45" |
| `updated_at` | string (schema `UpdatedAt2`) | no | Dispute last updated date, format = yyyy-mm-dd. | format: "date"; example: "2021-02-22" |
| `created_at_utc` | string (schema `CreatedAtUTC`) | no | Dispute created in UTC date/time. | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `updated_at_utc` | string (schema `UpdatedAtUTC`) | no | When dispute updated in UTC date/time. | example: "2022-10-13T19:56:010000000Z" |
| `is_network` | boolean | no | Open a dispute over a network authorization. | example: true |
| `is_dispute_migrated` | boolean | no | Has this dispute been migrated to the Pismo platform? | example: false |
| `reversal_id` | number | no | Dispute credit reversal ID. | example: 10042 |
| `network_return_reason_code` | string | no | Network reason code response. | example: "2833" |
| `network_brand_type` | string (schema `NetworkBrand`) | no | Network brand | enum: ["Visa", "Mastercard", "Elo"]; example: "Visa" |
| `transaction_date` | string | no | Transaction date related to authorization, format = yyyy-mm-dd | example: "2021-02-02" |
| `stop_automated_installment` | boolean (schema `stopAutomatedInstallment`) | no | Automated dispute installment control flag. If an issuer opens a dispute for a transaction that has more than one installment, with installments that can still be posted, the issuer will need to open a dispute for subsequent installments as well. With automated dispute installment control, once you open a chargeback for the first installment, the same information can be used for subsequent transaction installments.<br> | example: true |
| `card_hash` | string | no | Card number hash. | example: "XYZddue74kd8" |
| `authorization_code` | string (schema `AuthorizationCode`) | no | Authorization code | example: "F0JR9H" |
| `transaction_amount` | number (schema `TransactionAmount`) | no | Transaction amount | example: 86753.09 |
| `is_dispute_invalid_transaction` | boolean | no | Is this an invalid authorization dispute? | example: false |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;404;422;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.


## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Disputes.yaml` | tag `Disputes`: GET /v1/disputes/count, POST /v1/disputes/acknowledge, POST /v1/disputes/close, POST /v1/disputes/network-reversal | https://github.com/PismoDevEx/pismo-api-specs | `5c1d5513e1f3a4d1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
