---
ku_id: KU-API-revolving-credit-interest-accruals--post-interest-accruals
title: 'API reference: Revolving credit - Interest accruals — Post interest accruals'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Interest_accruals.yaml
  sha256: c741d2a41ac47207d0bbbc8f40d9492a64f36e979006c8170c14a065a96978af
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
- postInterestAccruals
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CORE-program-parameters-reference-table
- KU-CRED-accrual-rate-types-and-limits
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wiac-to-wstm
- KU-EVT-catalogue-transaction
specification_version: 2.74.0
---

# API reference: Revolving credit - Interest accruals — Post interest accruals

**KU ID:** `KU-API-revolving-credit-interest-accruals--post-interest-accruals` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Post interest accruals` in `api-specs/Revolving_credit_-_Interest_accruals.yaml` (“Revolving credit - Interest accruals”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for posting interest accrual by account

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/accounts/{accountId}/interest-accruals` | `postInterestAccruals` | Post interest accruals | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Interest_accruals.yaml method=POST path=/v1/accounts/{accountId}/interest-accruals operationId=postInterestAccruals -->
### `POST /v1/accounts/{accountId}/interest-accruals` — Post interest accruals

- **operationId:** `postInterestAccruals`
- **Specification:** `api-specs/Revolving_credit_-_Interest_accruals.yaml` (Revolving credit - Interest accruals)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-interest-accruals`
- **Tags:** `Post interest accruals`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> The Pismo platform filters all accruals by `accrual_status` and, optionally, by `start_date` and `end_date`. For each accrual type in the results, it adds the values and posts one transaction for the total amount.
>
> The status for each accrual filtered is changed to `PROCESSED`.
>
> The `201 Created` HTTP status response code indicates that the accruals were processed. However, the process that posts the transactions on the account's statement is asynchronous. To check if all transactions were created, check the [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1) event to verify that a transaction was created for each `tracking_id` returned by the endpoint.
>
> You can use `start_date` and `end_date` to restrict the search to accruals in a specific date range (where the accrual date indicates when the client issued the asset). If you do not provide either date field, then the search returns results from any date.
>
> NOTE: This endpoint requires an account-specific access token. Getting an account token requires you to call [Get OpenID access token](ref:post-passport-v1-oauth2-token) with an external account ID. Tokens can expire quickly, which can result in an Unauthorized message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 5689 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `InterestAccrualRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accrual_statuses` | array of object (schema `AccrualStatusesForPost`) | yes | Accrual statuses that you can use for filtering the interest accruals (`PENDING`, `STOP_ACCRUAL`, or both). |  |
| `start_date` | string (schema `StartDate`) | no | Start date. Format = YYYY-MM-DD. | format: "date"; example: "2024-01-01" |
| `end_date` | string (schema `EndDate`) | no | End date. Format = YYYY-MM-DD. | format: "date"; example: "2025-06-22" |
| `accrual_type` | string (schema `AccrualType2`) | no | Accrual type enables selective posting, instead of posting all types at once. If not passed, the original behavior is preserved (posts all accrual types).<br><br>The following are some of the possible values. (This is not an exhaustive list.)<br>  `REFINANCING`<br>  `OVERDUE`<br>  `WITHDRAWAL_INTEREST`<br>  `BILLPAYMENT_INTEREST`<br>  `OVERDRAFT_INTEREST`<br>  `FINANCIAL_TAX`<br> | maxLength: 20; example: "REFINANCING" |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code. Allows overriding the processing code used for posting the transaction, instead of using the one configured in `accrual-type-post-config`.<br><br>**Notes:**<br>- If you pass `processing_code`, you must also pass the `accrual_type` field.<br>- The provided processing code must exist in the transaction-flow service (validated via HTTP call).<br>- If not passed, the processing code from the existing configuration (created using the [Create accrual type post configuration endpoint](ref:createaccrualtypepostconfig)) or from the default mapping is used.<br> | example: "PROC123" |
| `processing_code_fine` | string (schema `ProcessingCodeFine`) | no | Processing code for fine. Allows overriding the processing code used specifically for posting FINE (penalty) when `accrual_type` is `OVERDUE`.<br><br>**Notes:**<br>- Only allowed when `accrual_type` = `OVERDUE` and `processing_code` is passed.<br>- If you pass `processing_code_fine`, you must also pass `processing_code`.<br><br>**Special case:** if `accrual_type` = `OVERDUE` and `processing_code` is passed, but `processing_code_fine` is **not**, and there are `FINE` accruals for the account, the endpoint returns a 409 Conflict error.<br> | example: "FINE123" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `InterestAccrualResponse`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 403 | Forbidden | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `StandardErrorResponse`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `StandardErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorizations` | array of object (schema `Authorization`) | yes | Authorizations created to post the accruals on the current statement. `tracking_id` can be used to check if each transaction was created after receiving a [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1) event. |  |

##### Response 400

400 Example `example`:

```json
{
  "Missing request header or param": {
    "description": "accrual_statuses",
    "value": {
      "code": "EIAC0002",
      "message": "The header {HeaderName} is required | The property {PropertyName} is required. | Can't find [BalanceAccount] with params: [AccountID: XXX, OrgID: XXX]."
    }
  }
}
```

##### Response 403

403 Example `processing_code_fine without processing_code`:

```json
{
  "code": "WIAC0005",
  "message": "The use of processing_code_fine is not allowed without processing_code"
}
```

403 Example `processing_code_fine with non-OVERDUE accrual type`:

```json
{
  "code": "WIAC0005",
  "message": "The use of processing_code_fine is only allowed for accrual_type OVERDUE"
}
```

##### Response 404

404 Example `example`:

```json
{
  "There are no accruals to be posted": {
    "description": "There are no accruals to be posted.",
    "value": {
      "code": "WIAC0002",
      "message": "There are no accruals to be posted."
    }
  }
}
```

##### Response 422

422 Example `example`:

```json
{
  "There are no processing codes configured to post the accrual": {
    "description": "There are no processing codes configured to post the accrual types [XXXX, YYYYY, ZZZZZ].",
    "value": {
      "code": "WIAC0003",
      "message": "There are no processing codes configured to post the accrual types [XXXX, YYYYY, ZZZZZ]."
    }
  }
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
| 400 | `EIAC0002` | The header {HeaderName} is required \| The property {PropertyName} is required. \| Can't find [BalanceAccount] with params: [AccountID: XXX, OrgID: XXX]. |
| 403 | `WIAC0005` | The use of processing_code_fine is not allowed without processing_code |
| 404 | `WIAC0002` | There are no accruals to be posted. |
| 422 | `WIAC0003` | There are no processing codes configured to post the accrual types [XXXX, YYYYY, ZZZZZ]. |
| 500 | `GN0001` | Service is unavailable |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `transaction-creation-1` | https://developers.pismo.io/events/docs/transaction-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;404;422;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CORE-program-parameters-reference-table`, `KU-CRED-accrual-rate-types-and-limits`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccrualStatusesForPost -->
### Schema `AccrualStatusesForPost`

Pointer: `#/components/schemas/AccrualStatusesForPost`. Type: object (schema `AccrualStatusesForPost`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string | yes | Accrual status.<br><br>`PENDING` — Accrual has not been processed.<br><br>`STOP_ACCRUAL` — An accrual is generated with this status when the account has been in `OVERDUE` status for at least X number of days, where X is configured in the program parameter `Stop accrual # of days`. Accruals with STOP_ACCRUAL status are not posted at cycle closing.<br> | enum: ["PENDING", "STOP_ACCRUAL"]; example: "PENDING" |

<!-- schema: #/components/schemas/Authorization -->
### Schema `Authorization`

Pointer: `#/components/schemas/Authorization`. Type: object (schema `Authorization`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accrual_type` | string (schema `AccrualType`) | yes | Accrual type. Should be one of the following values:<br>  `REFINANCING`<br>  `OVERDUE`<br>  `WITHDRAWAL_INTEREST`<br>  `BILLPAYMENT_INTEREST`<br>  `OVERDRAFT_INTEREST`<br>  `FINANCIAL_TAX`<br> | maxLength: 20; example: "REFINANCING" |
| `tracking_id` | string (schema `TrackingID`) | yes | Generated tracking ID. Identifies the authorization for the debit transaction used to post the total accrual for the given accrual type. | example: "18573154-bcb8-42c4-bd52-3f74e6939f47" |
| `amount` | number (schema `Amount`) | yes | Transaction amount | format: "float"; example: 25.36 |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "1020030" |
| `message` | string | no |  | example: "Error message" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Interest_accruals.yaml` | tag `Post interest accruals`: POST /v1/accounts/{accountId}/interest-accruals | https://github.com/PismoDevEx/pismo-api-specs | `c741d2a41ac47207…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-CRED-accrual-rate-types-and-limits` — Accrual rate types, accrual-free transaction types and accrual-day limits
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
