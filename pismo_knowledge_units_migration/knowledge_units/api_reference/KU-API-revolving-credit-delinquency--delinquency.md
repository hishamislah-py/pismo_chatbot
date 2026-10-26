---
ku_id: KU-API-revolving-credit-delinquency--delinquency
title: 'API reference: Revolving credit - Delinquency — Delinquency'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Delinquency.yaml
  sha256: de89bd8a0d8714d47ec224562976e5cff57fe41f9ad5715b56bed9487f1dd377
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
- getdelinquencybuckets
- listdelinquencybuckets
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CRED-delinquency-buckets
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 3.0.0
---

# API reference: Revolving credit - Delinquency — Delinquency

**KU ID:** `KU-API-revolving-credit-delinquency--delinquency` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Delinquency` in `api-specs/Revolving_credit_-_Delinquency.yaml` (“Revolving credit - Delinquency”, version `3.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints associated with account delinquency buckets

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accounts/{accountId}/buckets/{delinquencyBucketId}` | `getdelinquencybuckets` | Get delinquency bucket | no |
| `GET /v1/accounts/{accountId}/buckets` | `listdelinquencybuckets` | List delinquency buckets | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Delinquency.yaml method=GET path=/v1/accounts/{accountId}/buckets/{delinquencyBucketId} operationId=getdelinquencybuckets -->
### `GET /v1/accounts/{accountId}/buckets/{delinquencyBucketId}` — Get delinquency bucket

- **operationId:** `getdelinquencybuckets`
- **Specification:** `api-specs/Revolving_credit_-_Delinquency.yaml` (Revolving credit - Delinquency)
- **Server base URL(s):** `https://sandbox.pismolabs.io/delinquency-bucket-api`
- **Tags:** `Delinquency`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get account delinquency bucket given an account ID and bucket ID in the path. You can get delinquency bucket IDs from the [List delinquency buckets](ref:listdelinquencybuckets) endpoint. You can use delinquency buckets to control and manage cardholder delinquency. Buckets are created at cycle close. For more information, see the [Delinquency buckets](doc:delinquency-buckets) guide.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 18898 |
| `delinquencyBucketId` | path | yes | integer | Delinquency bucket ID.  You can get delinquency bucket IDs from the [List delinquency buckets](ref:listdelinquencybuckets) endpoint. | format: "int64"; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `DelinquencyBucketResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `statement_id` | integer | no | Statement ID | example: 847490277 |
| `cycle_closing_date` | string | no | Cycle closing date | example: "2024-01-02T00:00:00.000Z" |
| `due_date` | string | no | Due date | example: "2024-01-02T00:00:00.000Z" |
| `statement_cycle` | integer | no | Statement cycle | example: 1 |
| `delinquencyBucket_id` | integer | no | Delinquency bucket ID | example: 21 |
| `calculation_memory` | object (schema `CalcMemory`) | no |  |  |
| `overdue_amount` | number | no | Overdue amount | example: 87 |
| `unexpired_bucket` | boolean | no | Informs if the bucket is unexpired | example: true |
| `bucket_amount` | number | no | Bucket amount | example: 87 |
| `bucket_balance` | number | no | Bucket balance | example: 99 |
| `created_at` | string | no | Bucket creation date in ISO-8601 UTC time | format: "date-time"; example: "2022-11-09T18:57:49.000Z" |
| `updated_at` | string | no | Bucket last updated date in ISO-8601 UTC time | format: "date-time"; example: "2022-11-09T18:57:49.000Z" |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-delinquency-buckets`.

<!-- op: spec=api-specs/Revolving_credit_-_Delinquency.yaml method=GET path=/v1/accounts/{accountId}/buckets operationId=listdelinquencybuckets -->
### `GET /v1/accounts/{accountId}/buckets` — List delinquency buckets

- **operationId:** `listdelinquencybuckets`
- **Specification:** `api-specs/Revolving_credit_-_Delinquency.yaml` (Revolving credit - Delinquency)
- **Server base URL(s):** `https://sandbox.pismolabs.io/delinquency-bucket-api`
- **Tags:** `Delinquency`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get an account's delinquency buckets with filtering options.
> For more information, see the [Delinquency buckets](doc:delinquency-buckets) guide.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 18899 |
| `page` | query | no | integer | Current page | format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |
| `hasDelinquencyBalance` | query | no | boolean | `false` = return all account's existing delinquency buckets.<br>`true` = return only delinquency bucket with balance amount greater than zero. <br>Default is `false`.<br> | example: true |
| `allBuckets` | query | no | boolean | `true` = return all buckets.<br>`false` = return all buckets with DueDate less than today (or DueDate null for legacy buckets).<br>Default is `false`.<br> | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `DelinquencyBucketListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `DelinquencyBucketResponse`) | no |  |  |
| `current_page` | integer | no | Current page | format: "int32"; example: 1 |
| `per_page` | integer | no | Number of elements, default is 10 | format: "int32"; example: 10 |
| `total_items` | integer | no | Total elements found for the request | format: "int32"; example: 100 |
| `items_on_page` | integer | no | Total elements on this page | format: "int32"; example: 5 |
| `pages` | integer | no | Total pages for the request | format: "int32"; example: 1 |
| `is_last_page` | boolean | no | Is the current page the last page flag | example: true |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-delinquency-buckets`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/CalcMemory -->
### Schema `CalcMemory`

Pointer: `#/components/schemas/CalcMemory`. Type: object (schema `CalcMemory`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Strategy used to calculate the delinquency amount<br>Defines whether delinquency buckets should be calculated for tracking an account's debt.<br>  0 - Does not calculate<br>  1 - Calculate and amortize buckets from oldest to newest (DEFAULT)<br> | enum: ["DEFAULT"]; example: "DEFAULT" |
| `mad` | number | no | Minimum amount due | example: 52.5 |
| `overdue_amount` | number | no | Overdue amount | example: 0 |
| `preivous_bucket_balance` | number | no | Previous bucket balance | example: 0 |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "1020030" |
| `message` | string | no |  | example: "Error message" |

<!-- schema: #/components/schemas/DelinquencyBucketResponse -->
### Schema `DelinquencyBucketResponse`

Pointer: `#/components/schemas/DelinquencyBucketResponse`. Type: object (schema `DelinquencyBucketResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `statement_id` | integer | no | Statement ID | example: 847490277 |
| `cycle_closing_date` | string | no | Cycle closing date | example: "2024-01-02T00:00:00.000Z" |
| `due_date` | string | no | Due date | example: "2024-01-02T00:00:00.000Z" |
| `statement_cycle` | integer | no | Statement cycle | example: 1 |
| `delinquencyBucket_id` | integer | no | Delinquency bucket ID | example: 21 |
| `calculation_memory` | object (schema `CalcMemory`) | no |  |  |
| `overdue_amount` | number | no | Overdue amount | example: 87 |
| `unexpired_bucket` | boolean | no | Informs if the bucket is unexpired | example: true |
| `bucket_amount` | number | no | Bucket amount | example: 87 |
| `bucket_balance` | number | no | Bucket balance | example: 99 |
| `created_at` | string | no | Bucket creation date in ISO-8601 UTC time | format: "date-time"; example: "2022-11-09T18:57:49.000Z" |
| `updated_at` | string | no | Bucket last updated date in ISO-8601 UTC time | format: "date-time"; example: "2022-11-09T18:57:49.000Z" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Delinquency.yaml` | tag `Delinquency`: GET /v1/accounts/{accountId}/buckets/{delinquencyBucketId}, GET /v1/accounts/{accountId}/buckets | https://github.com/PismoDevEx/pismo-api-specs | `de89bd8a0d8714d4…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CRED-delinquency-buckets` — Delinquency buckets
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
