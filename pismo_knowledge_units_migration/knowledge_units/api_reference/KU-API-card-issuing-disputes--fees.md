---
ku_id: KU-API-card-issuing-disputes--fees
title: 'API reference: Card issuing - Disputes — Fees'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- get-v1-fee
- post-v1-fee
- get-v1-fee-disputeFeeId
- put-v1-fee-disputeFeeId
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-disputes-overview
- KU-EVT-catalogue-disputes
- KU-EVT-disputes-endpoint-generated-events
specification_version: 1.0.0
---

# API reference: Card issuing - Disputes — Fees

**KU ID:** `KU-API-card-issuing-disputes--fees` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Fees` in `api-specs/Card_issuing_-_Disputes.yaml` (“Card issuing - Disputes”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to create and check status for fees

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/fee` | `get-v1-fee` | List dispute fees | no |
| `POST /v1/fee` | `post-v1-fee` | Create dispute fee | no |
| `GET /v1/fee/{disputeFeeId}` | `get-v1-fee-disputeFeeId` | Get dispute fee | no |
| `PUT /v1/fee/{disputeFeeId}` | `put-v1-fee-disputeFeeId` | Update dispute fee | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v1/fee operationId=get-v1-fee -->
### `GET /v1/fee` — List dispute fees

- **operationId:** `get-v1-fee`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Fees`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a list of fees with filter and paging options.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization/tenant ID |  |
| `beginDate` | query | no | string | Beginning date filter, format= yyyy-mm-dd | example: "2020-01-31" |
| `endDate` | query | no | string | End date filter, format= yyyy-mm-dd | example: "2020-01-31" |
| `claimId` | query | no | string | Fee item claim ID. |  |
| `cardId` | query | no | string | Fee item card ID. Return dispute fees associated with a specific card.<br> |  |
| `networkFeeId` | query | no | string | Fee ID from network. |  |
| `status` | query | no | string | Status filter. | enum: ["PENDING", "PROCESSED", "FAILED"]; example: "PROCESSED" |
| `page` | query | no | integer | Page to return. | default: 1; minimum: 1; example: 2 |
| `perPage` | query | no | integer | Number of items per page | default: 30; minimum: 1; example: 20 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `DisputeFeeResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 422 | Unprocessable entity |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;422;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-overview`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v1/fee operationId=post-v1-fee -->
### `POST /v1/fee` — Create dispute fee

- **operationId:** `post-v1-fee`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Fees`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> A dispute fee, or *fee collection* in network terminology, is a way for an acquirer and issuer to exchange money outside the normal chargeback process. Typically, this means reversing a settled chargeback, but not always,
>
> You can use this endpoint to create a dispute fee with or without a chargeback claim ID. You can create a dispute fee for a claim that already exists or, if it doesn't, you can pass the necessary authorization information to create it.
>
> For more information, refer to [Dispute fees](doc:disputes-overview#dispute-fees) in the Disputes overview guide. This feature is only available for Mastercard and Elo.
>
> This endpoint generates a [Dispute fee status created](https://developers.pismo.io/events/docs/disputes-dispute-fee-events-1) event.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |

#### Request body

Required: yes

> Dispute fee data

**Content type `application/json`** — schema: object (schema `DisputeFee`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | yes | Fee amount. | format: "double"; example: 100 |
| `card_id` | number (schema `CardID`) | yes | Pismo card ID. | example: 123456 |
| `credit_sender` | boolean | yes | Credit the sender? Default is `false`. | default: false |
| `credit_receiver` | boolean | yes | Credit the receiver? Default is `false`. | default: false |
| `currency` | string | yes | ISO 4217 fee currency code. | maxLength: 3; example: "USD" |
| `destination_member` | string | yes | Destination member for the fee collection. These values are known to the network and identify either the issuer or acquirer. | maxLength: 6; example: "002083" |
| `fee_date` | string | yes | Date the fee was attached to the claim, format = yyyy-mm-dd. | format: "date"; maxLength: 10; example: "2021-02-15" |
| `network_brand_type` | string (schema `NetworkBrand`) | yes | Network brand | enum: ["Visa", "Mastercard", "Elo"]; example: "Visa" |
| `reason_code` | string | yes | Collection reason code. These codes can be found in Mastercard's [Global Clearing Management System Reference Manual](https://pismoassets.pismo.io/pismo-docs/mc_gcms_rm.pdf) starting on page 408.<br> | maxLength: 4; example: "7604" |
| `authorization_id` | number | no | Authorization ID. **REQUIRED** if `claim_id` and `arn` is not passed. |  |
| `arn` | string | no | Acquirer reference number. **REQUIRED** if `claim_id` is not passed. | example: "1564984" |
| `transaction_amount` | number | no | Transaction amount. **REQUIRED** if `claim_id` is not passed. | format: "double"; example: 100 |
| `transaction_date` | string | no | Transaction date, format = yyyy-mm-dd hh:mm:ss. **REQUIRED** if `claim_id` is not passed. | format: "date-time"; example: "2022-06-01 10:25:36" |
| `claim_id` | string | no | Fee item claim ID | maxLength: 19; example: "121698491" |
| `card_acceptor_code` | string | no | Merchant ID associated with this fee collection, if any. | maxLength: 15; example: "Test1234" |
| `country_code` | string | no | ISO 3166 3-letter country code. | maxLength: 3; example: "USA" |
| `message` | string | no | Message regarding fee - 100 chars maximum. | maxLength: 100; example: "Cardholder recognized the transaction" |
| `settlement_date` | string | no | Settlement date, format = yyyy-mm-dd. | format: "date"; maxLength: 10; example: "2021-09-22" |
| `reply_fee_id` | string | no | Fee ID to be sent in reply to created Fee. | maxLength: 19; example: "300009520876" |
| `control_number` | string | no | Control number. Used in routing chargeback and retrieval documentation - either a MasterCom endpoint suffix, in case of 2 characters, or a full MasterCom endpoint in case of 7 characters. When MasterCom control number is present, it cannot be all spaces or all zeros.<br> | maxLength: 7; example: "1589457" |

Example `Dispute fee with clam id`:

```json
{
  "card_id": 15595,
  "claim_id": "15465165165",
  "card_acceptor_code": "125",
  "country_code": "125",
  "destination_member": "125485",
  "fee_date": "2022-05-31",
  "currency": "840",
  "amount": 15.56,
  "message": "test",
  "reason_code": "1515",
  "settlement_date": "2022-05-31",
  "control_number": "1564989",
  "credit_sender": false,
  "credit_receiver": true,
  "network_brand_type": "Mastercard"
}
```

Example `Dispute fee when there is no claim id`:

```json
{
  "authorization_id": 31241,
  "arn": "15641616",
  "transaction_amount": 36.25,
  "transaction_date": "2022-05-31 23:00:25",
  "card_id": 15595,
  "card_acceptor_code": "125",
  "country_code": "125",
  "destination_member": "125485",
  "fee_date": "2022-05-31",
  "currency": "840",
  "amount": 15.56,
  "message": "test",
  "reason_code": "1515",
  "settlement_date": "2022-05-31",
  "reply_fee_id": "1949884",
  "control_number": "1564989",
  "credit_sender": false,
  "credit_receiver": true,
  "network_brand_type": "Mastercard"
}
```

Example `Dispute fee with replay ID`:

```json
{
  "card_id": 15595,
  "claim_id": "15465165165",
  "card_acceptor_code": "125",
  "country_code": "125",
  "destination_member": "125485",
  "fee_date": "2022-05-31",
  "currency": "840",
  "amount": 15.56,
  "message": "test",
  "reason_code": "1515",
  "settlement_date": "2022-05-31",
  "reply_fee_id": "12345645",
  "control_number": "1564989",
  "credit_sender": false,
  "credit_receiver": true,
  "network_brand_type": "Mastercard"
}
```

**Content type `application/xml`** — schema: object

_No fields declared in the schema._

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `DisputeFeeResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 422 | Unprocessable entity |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number | no | Dispute fee ID | example: 152 |
| `arn` | string | no | Acquirer reference number. **REQUIRED** if `claim_id` is not passed. | example: "1564984" |
| `transaction_amount` | number | no | Transaction amount. **REQUIRED** if `claim_id` is not passed. | format: "double" |
| `transaction_date` | string | no | Transaction date, format = yyyy-mm-dd hh:mm:ss.  **REQUIRED**  if `claim_id` is not passed. | format: "date-time"; example: "2022-06-01 10:25:36" |
| `card_id` | number (schema `CardID`) | no | Pismo card ID. | example: 123456 |
| `card_acceptor_code` | string | no | Merchant ID associated with this fee collection..if any. | maxLength: 15; example: "Test1234" |
| `country_code` | string | no | ISO country code. | maxLength: 3; example: "USA" |
| `destination_member` | string | no | Destination member for the fee collection. These values are known to the network and identify either the acquirer or issuer. | maxLength: 6; example: "002083" |
| `fee_date` | string | no | Date the fee was attached to the claim, format = yyyy-mm-dd | format: "date"; maxLength: 10; example: "2021-02-15" |
| `currency` | string | no | ISO 4217 currency code. | maxLength: 3; example: "USD" |
| `amount` | number | no | Fee amount. | format: "double"; example: 100 |
| `message` | string | no | Message regarding fee - 100 chars maximum. | maxLength: 100; example: "Cardholder recognized transaction" |
| `reason_code` | string | no | Collection reason code. These codes can be found in Mastercard's [Global Clearing Management System Reference Manual](https://pismoassets.pismo.io/pismo-docs/mc_gcms_rm.pdf) starting on page 408.<br> | maxLength: 4; example: "7604" |
| `settlement_date` | string | no | Settlement date, format = yyyy-mm-dd. | format: "date"; maxLength: 10; example: "2021-09-22" |
| `control_number` | string | no | Control number | maxLength: 7; example: "1589457" |
| `credit_sender` | boolean (schema `CreditSender`) | no | Credit the sender? Default is `false`. | default: false |
| `credit_receiver` | boolean (schema `CreditReceiver`) | no | Should receiver be credited? |  |
| `network_brand_type` | string (schema `NetworkBrand`) | no | Network brand | enum: ["Visa", "Mastercard", "Elo"]; example: "Visa" |
| `status` | string | no | Dispute fee status - `PENDING`, `PROCESSED`, or  `FAILED`. | enum: ["PENDING", "PROCESSED", "FAILED"]; example: "PENDING" |
| `chargeback_ref_num` | string | no | Chargeback reference number | maxLength: 100; example: "9000000006" |
| `reconciliation_amount` | number | no | Reconciliation amount | format: "double"; example: 123.22 |
| `reconciliation_currency` | string | no | Reconciliation currency | maxLength: 3; example: "EUR" |
| `japan_common_merchant_code` | string | no | Japanese common merchant codes | maxLength: 100; example: "0410" |
| `installment_data` | string | no | Installment data | maxLength: 255; example: "1234567890" |
| `reply_fee_id` | string | no | Fee ID to send to reply to created fee. | maxLength: 19; example: "300009520876" |
| `reject_reason` | string | no | Reject reason | maxLength: 515; example: "Code1=0142(00):D0063/002;DE072=D0063\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\8000000808\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ " |
| `created_at` | string | no | When dispute created, format = yyyy-mm-ddThh:mm:ss" | example: "2222-10-07T11:21:45" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime when updated, format = yyyy-mm-dd hh:mm:ss | example: "2024-10-18 11:21:45" |
| `created_at_utc` | string (schema `CreatedAtUTC`) | no | Dispute created in UTC date/time. | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `updated_at_utc` | string (schema `UpdatedAtUTC`) | no | When dispute updated in UTC date/time. | example: "2022-10-13T19:56:010000000Z" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `disputes-dispute-fee-events-1` | https://developers.pismo.io/events/docs/disputes-dispute-fee-events-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;422;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-disputes-overview`, `KU-EVT-disputes-endpoint-generated-events`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v1/fee/{disputeFeeId} operationId=get-v1-fee-disputeFeeId -->
### `GET /v1/fee/{disputeFeeId}` — Get dispute fee

- **operationId:** `get-v1-fee-disputeFeeId`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Fees`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get information about a specific dispute fee given its ID in the path. You can get fee IDs with the [List dispute fees](ref:get-v1-fee) endpoint.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeFeeId` | path | yes | string | Dispute fee ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `DisputeFeeResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 422 | Unprocessable entity |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number | no | Dispute fee ID | example: 152 |
| `arn` | string | no | Acquirer reference number. **REQUIRED** if `claim_id` is not passed. | example: "1564984" |
| `transaction_amount` | number | no | Transaction amount. **REQUIRED** if `claim_id` is not passed. | format: "double" |
| `transaction_date` | string | no | Transaction date, format = yyyy-mm-dd hh:mm:ss.  **REQUIRED**  if `claim_id` is not passed. | format: "date-time"; example: "2022-06-01 10:25:36" |
| `card_id` | number (schema `CardID`) | no | Pismo card ID. | example: 123456 |
| `card_acceptor_code` | string | no | Merchant ID associated with this fee collection..if any. | maxLength: 15; example: "Test1234" |
| `country_code` | string | no | ISO country code. | maxLength: 3; example: "USA" |
| `destination_member` | string | no | Destination member for the fee collection. These values are known to the network and identify either the acquirer or issuer. | maxLength: 6; example: "002083" |
| `fee_date` | string | no | Date the fee was attached to the claim, format = yyyy-mm-dd | format: "date"; maxLength: 10; example: "2021-02-15" |
| `currency` | string | no | ISO 4217 currency code. | maxLength: 3; example: "USD" |
| `amount` | number | no | Fee amount. | format: "double"; example: 100 |
| `message` | string | no | Message regarding fee - 100 chars maximum. | maxLength: 100; example: "Cardholder recognized transaction" |
| `reason_code` | string | no | Collection reason code. These codes can be found in Mastercard's [Global Clearing Management System Reference Manual](https://pismoassets.pismo.io/pismo-docs/mc_gcms_rm.pdf) starting on page 408.<br> | maxLength: 4; example: "7604" |
| `settlement_date` | string | no | Settlement date, format = yyyy-mm-dd. | format: "date"; maxLength: 10; example: "2021-09-22" |
| `control_number` | string | no | Control number | maxLength: 7; example: "1589457" |
| `credit_sender` | boolean (schema `CreditSender`) | no | Credit the sender? Default is `false`. | default: false |
| `credit_receiver` | boolean (schema `CreditReceiver`) | no | Should receiver be credited? |  |
| `network_brand_type` | string (schema `NetworkBrand`) | no | Network brand | enum: ["Visa", "Mastercard", "Elo"]; example: "Visa" |
| `status` | string | no | Dispute fee status - `PENDING`, `PROCESSED`, or  `FAILED`. | enum: ["PENDING", "PROCESSED", "FAILED"]; example: "PENDING" |
| `chargeback_ref_num` | string | no | Chargeback reference number | maxLength: 100; example: "9000000006" |
| `reconciliation_amount` | number | no | Reconciliation amount | format: "double"; example: 123.22 |
| `reconciliation_currency` | string | no | Reconciliation currency | maxLength: 3; example: "EUR" |
| `japan_common_merchant_code` | string | no | Japanese common merchant codes | maxLength: 100; example: "0410" |
| `installment_data` | string | no | Installment data | maxLength: 255; example: "1234567890" |
| `reply_fee_id` | string | no | Fee ID to send to reply to created fee. | maxLength: 19; example: "300009520876" |
| `reject_reason` | string | no | Reject reason | maxLength: 515; example: "Code1=0142(00):D0063/002;DE072=D0063\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\8000000808\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ " |
| `created_at` | string | no | When dispute created, format = yyyy-mm-ddThh:mm:ss" | example: "2222-10-07T11:21:45" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime when updated, format = yyyy-mm-dd hh:mm:ss | example: "2024-10-18 11:21:45" |
| `created_at_utc` | string (schema `CreatedAtUTC`) | no | Dispute created in UTC date/time. | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `updated_at_utc` | string (schema `UpdatedAtUTC`) | no | When dispute updated in UTC date/time. | example: "2022-10-13T19:56:010000000Z" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;422;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-overview`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=PUT path=/v1/fee/{disputeFeeId} operationId=put-v1-fee-disputeFeeId -->
### `PUT /v1/fee/{disputeFeeId}` — Update dispute fee

- **operationId:** `put-v1-fee-disputeFeeId`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Fees`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update dispute fee - only if status is `PENDING` or `FAILED`. Requires a dispute fee ID in the path. You can get fee IDs with the [List dispute fees](ref:get-v1-fee) endpoint.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeFeeId` | path | yes | string | Dispute fee ID |  |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `DisputeFee`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | yes | Fee amount. | format: "double"; example: 100 |
| `card_id` | number (schema `CardID`) | yes | Pismo card ID. | example: 123456 |
| `credit_sender` | boolean | yes | Credit the sender? Default is `false`. | default: false |
| `credit_receiver` | boolean | yes | Credit the receiver? Default is `false`. | default: false |
| `currency` | string | yes | ISO 4217 fee currency code. | maxLength: 3; example: "USD" |
| `destination_member` | string | yes | Destination member for the fee collection. These values are known to the network and identify either the issuer or acquirer. | maxLength: 6; example: "002083" |
| `fee_date` | string | yes | Date the fee was attached to the claim, format = yyyy-mm-dd. | format: "date"; maxLength: 10; example: "2021-02-15" |
| `network_brand_type` | string (schema `NetworkBrand`) | yes | Network brand | enum: ["Visa", "Mastercard", "Elo"]; example: "Visa" |
| `reason_code` | string | yes | Collection reason code. These codes can be found in Mastercard's [Global Clearing Management System Reference Manual](https://pismoassets.pismo.io/pismo-docs/mc_gcms_rm.pdf) starting on page 408.<br> | maxLength: 4; example: "7604" |
| `authorization_id` | number | no | Authorization ID. **REQUIRED** if `claim_id` and `arn` is not passed. |  |
| `arn` | string | no | Acquirer reference number. **REQUIRED** if `claim_id` is not passed. | example: "1564984" |
| `transaction_amount` | number | no | Transaction amount. **REQUIRED** if `claim_id` is not passed. | format: "double"; example: 100 |
| `transaction_date` | string | no | Transaction date, format = yyyy-mm-dd hh:mm:ss. **REQUIRED** if `claim_id` is not passed. | format: "date-time"; example: "2022-06-01 10:25:36" |
| `claim_id` | string | no | Fee item claim ID | maxLength: 19; example: "121698491" |
| `card_acceptor_code` | string | no | Merchant ID associated with this fee collection, if any. | maxLength: 15; example: "Test1234" |
| `country_code` | string | no | ISO 3166 3-letter country code. | maxLength: 3; example: "USA" |
| `message` | string | no | Message regarding fee - 100 chars maximum. | maxLength: 100; example: "Cardholder recognized the transaction" |
| `settlement_date` | string | no | Settlement date, format = yyyy-mm-dd. | format: "date"; maxLength: 10; example: "2021-09-22" |
| `reply_fee_id` | string | no | Fee ID to be sent in reply to created Fee. | maxLength: 19; example: "300009520876" |
| `control_number` | string | no | Control number. Used in routing chargeback and retrieval documentation - either a MasterCom endpoint suffix, in case of 2 characters, or a full MasterCom endpoint in case of 7 characters. When MasterCom control number is present, it cannot be all spaces or all zeros.<br> | maxLength: 7; example: "1589457" |

Example `Update all fields`:

```json
{
  "arn": "1564984",
  "transaction_amount": 100,
  "transaction_date": "2022-06-01 10:25:36",
  "network_brand_type": "Visa",
  "card_id": 29484059,
  "claim_id": "121698491",
  "card_acceptor_code": "Test1234",
  "country_code": "USA",
  "destination_member": "002083",
  "fee_date": "2021-02-15",
  "currency": "USD",
  "amount": 100,
  "message": "This is a test message",
  "reason_code": "7604",
  "settlement_date": "2021-09-22",
  "reply_fee_id": "300009520876",
  "control_number": "1589457",
  "credit_sender": false,
  "credit_receiver": false
}
```

Example `Update some fields`:

```json
{
  "arn": "1564984",
  "transaction_amount": 100,
  "transaction_date": "2022-06-01 10:25:36",
  "destination_member": "599849",
  "fee_date": "2021-02-15",
  "card_id": 3995067,
  "currency": "986",
  "amount": 45.88,
  "reason_code": "4885",
  "credit_sender": true,
  "credit_receiver": false,
  "network_brand_type": "Visa"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `DisputeFeeResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 422 | Unprocessable entity |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number | no | Dispute fee ID | example: 152 |
| `arn` | string | no | Acquirer reference number. **REQUIRED** if `claim_id` is not passed. | example: "1564984" |
| `transaction_amount` | number | no | Transaction amount. **REQUIRED** if `claim_id` is not passed. | format: "double" |
| `transaction_date` | string | no | Transaction date, format = yyyy-mm-dd hh:mm:ss.  **REQUIRED**  if `claim_id` is not passed. | format: "date-time"; example: "2022-06-01 10:25:36" |
| `card_id` | number (schema `CardID`) | no | Pismo card ID. | example: 123456 |
| `card_acceptor_code` | string | no | Merchant ID associated with this fee collection..if any. | maxLength: 15; example: "Test1234" |
| `country_code` | string | no | ISO country code. | maxLength: 3; example: "USA" |
| `destination_member` | string | no | Destination member for the fee collection. These values are known to the network and identify either the acquirer or issuer. | maxLength: 6; example: "002083" |
| `fee_date` | string | no | Date the fee was attached to the claim, format = yyyy-mm-dd | format: "date"; maxLength: 10; example: "2021-02-15" |
| `currency` | string | no | ISO 4217 currency code. | maxLength: 3; example: "USD" |
| `amount` | number | no | Fee amount. | format: "double"; example: 100 |
| `message` | string | no | Message regarding fee - 100 chars maximum. | maxLength: 100; example: "Cardholder recognized transaction" |
| `reason_code` | string | no | Collection reason code. These codes can be found in Mastercard's [Global Clearing Management System Reference Manual](https://pismoassets.pismo.io/pismo-docs/mc_gcms_rm.pdf) starting on page 408.<br> | maxLength: 4; example: "7604" |
| `settlement_date` | string | no | Settlement date, format = yyyy-mm-dd. | format: "date"; maxLength: 10; example: "2021-09-22" |
| `control_number` | string | no | Control number | maxLength: 7; example: "1589457" |
| `credit_sender` | boolean (schema `CreditSender`) | no | Credit the sender? Default is `false`. | default: false |
| `credit_receiver` | boolean (schema `CreditReceiver`) | no | Should receiver be credited? |  |
| `network_brand_type` | string (schema `NetworkBrand`) | no | Network brand | enum: ["Visa", "Mastercard", "Elo"]; example: "Visa" |
| `status` | string | no | Dispute fee status - `PENDING`, `PROCESSED`, or  `FAILED`. | enum: ["PENDING", "PROCESSED", "FAILED"]; example: "PENDING" |
| `chargeback_ref_num` | string | no | Chargeback reference number | maxLength: 100; example: "9000000006" |
| `reconciliation_amount` | number | no | Reconciliation amount | format: "double"; example: 123.22 |
| `reconciliation_currency` | string | no | Reconciliation currency | maxLength: 3; example: "EUR" |
| `japan_common_merchant_code` | string | no | Japanese common merchant codes | maxLength: 100; example: "0410" |
| `installment_data` | string | no | Installment data | maxLength: 255; example: "1234567890" |
| `reply_fee_id` | string | no | Fee ID to send to reply to created fee. | maxLength: 19; example: "300009520876" |
| `reject_reason` | string | no | Reject reason | maxLength: 515; example: "Code1=0142(00):D0063/002;DE072=D0063\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\8000000808\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ " |
| `created_at` | string | no | When dispute created, format = yyyy-mm-ddThh:mm:ss" | example: "2222-10-07T11:21:45" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime when updated, format = yyyy-mm-dd hh:mm:ss | example: "2024-10-18 11:21:45" |
| `created_at_utc` | string (schema `CreatedAtUTC`) | no | Dispute created in UTC date/time. | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `updated_at_utc` | string (schema `UpdatedAtUTC`) | no | When dispute updated in UTC date/time. | example: "2022-10-13T19:56:010000000Z" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;422;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-overview`.

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
| `api-specs/Card_issuing_-_Disputes.yaml` | tag `Fees`: GET /v1/fee, POST /v1/fee, GET /v1/fee/{disputeFeeId}, PUT /v1/fee/{disputeFeeId} | https://github.com/PismoDevEx/pismo-api-specs | `5c1d5513e1f3a4d1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-disputes-overview` — Disputes overview
- `KU-EVT-catalogue-disputes` — Event catalogue: disputes
- `KU-EVT-disputes-endpoint-generated-events` — Card issuing - Disputes
