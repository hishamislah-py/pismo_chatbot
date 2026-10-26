---
ku_id: KU-API-revolving-credit-delinquent-account--delinquent-account-closure
title: 'API reference: Revolving credit - Delinquent account — Delinquent account closure'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Delinquent_account.yaml
  sha256: 07df8bb5c17143f2dbaf9a7dcf0bf129a09f9722b77a2b66a46eb3f61c2890fb
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
- delinquent-account-closure-post
- delinquent-account-closure-get
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CRED-credit-liquidation
- KU-EVT-catalogue-other-domains
- KU-GS-get-started-with-pismo-apis
specification_version: 1.0.0
---

# API reference: Revolving credit - Delinquent account — Delinquent account closure

**KU ID:** `KU-API-revolving-credit-delinquent-account--delinquent-account-closure` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Delinquent account closure` in `api-specs/Revolving_credit_-_Delinquent_account.yaml` (“Revolving credit - Delinquent account”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage delinquent account closure.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/accounts/{account_id}/close` | `delinquent-account-closure-post` | Close delinquent account | no |
| `GET /v1/accounts/{account_id}` | `delinquent-account-closure-get` | Get delinquent account closure process information | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Delinquent_account.yaml method=POST path=/v1/accounts/{account_id}/close operationId=delinquent-account-closure-post -->
### `POST /v1/accounts/{account_id}/close` — Close delinquent account

- **operationId:** `delinquent-account-closure-post`
- **Specification:** `api-specs/Revolving_credit_-_Delinquent_account.yaml` (Revolving credit - Delinquent account)
- **Server base URL(s):** `https://sandbox.pismolabs.io/delinquent-account`
- **Tags:** `Delinquent account closure`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Sends the specified account to the delinquent account closure process.
> This endpoint generates a [Delinquent account closed](https://developers.pismo.io/events/docs/delinquent-account-delinquent-account-1) event.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `account_id` | path | yes | integer | Account ID | example: 6912345 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `PostAccountCloseRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | yes | Tracking identifier. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128. If a client <br>clicks the button more than once when sending the command to close an account, the Pismo platform could create duplicate <br>requests. The tracking identifier enables the platform to identify duplicates and ignore them.<br> | minLength: 1; maxLength: 128; example: "3368328d-e4c6-4c75-99a9-9d59f3501d8c" |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code for the transaction that the Pismo platform creates to zero out the account balance. | example: "008000" |
| `reason` | string (schema `ReasonForClosure`) | no | `external_id` of the status reason. This is the external ID that was used to create the reason. | minLength: 1; maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |
| `final_account_status` | string (schema `FinalAccountStatus`) | no | Final status for the closed delinquent account. Use the [List statuses](ref:v4-get-account-status) endpoint to list the available account statuses.<br> | example: "CANCELLED" |
| `excluded_steps` | array of string (schema `ExcludedStep`) (schema `ExcludedSteps`) | no | Steps to skip when closing a delinquent account | example: ["SET_CARD_AS_BLOCKED"]; items.enum: ["POST_INTEREST_ACCRUAL", "POST_INSTALLMENT_ADVANCE", "POST_CREDIT_TRANSACTION", "SET_CARD_AS_BLOCKED"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted - Indicates that the server has accepted the request, and the specified account has been sent to the delinquent account closure process. | `application/json`: object (schema `PostAccountCloseResponse`) |
| 400 | Bad Request |  |
| 409 | The specified resource status conflicts with the current request. |  |
| 500 | Internal server error |  |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `open_due_date` | string (schema `OpenDueDate`) | no | Open due date. This is the first day that the account became overdue. BRT (Brazilian time zone = UTC-03). | example: "2023-01-01" |
| `due_days` | integer (schema `DueDays`) | no | Due days. The number of days the account has been overdue. (Today minus `open_due_date`). | example: 10 |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (UTC) that asset was registered on Pismo platform | example: "2023-03-30T12:26:41" |
| `status` | string (schema `AccountStatus`) | no | Delinquent account entity status<br><br>This field can have the following values.<br>`CREATED`—Created a delinquent account register to initiate the process.<br>`STARTED`—Started posting interest accruals.<br>`INTEREST_ACCRUAL_POSTED`—Finished posting nterest accruals.<br>`INSTALLMENT_ADVANCED`—Checked all transactions that need to be deducted separately.<br>`CREDIT_SEPARATED_TRANSACTION_REQUEST`—Requested a deduction for each transaction selected to be settled separately.<br>`CREDIT_SEPARATED_TRANSACTION_CREATED`—Created deduction transactions.<br>`CREDIT_TRANSACTION_REQUESTED`—Posted a credit transaction to the account.<br>`ACCOUNT_CANCELLED`—Cancelled account.<br>`CARD_BLOCKED`—Requested that all cards be blocked.<br>`SUCCESS`—Blocked all cards. Generated account [delinquent closure event](https://developers.pismo.io/events/docs/delinquent-account-delinquent-account-1).<br>`SUCCESS_EVENT_SENT`—Sent `SUCCESS` event to customer.<br> | enum: ["CREATED", "STARTED", "INTEREST_ACCRUAL_POSTED", "INSTALLMENTS_ADVANCED", "CREDIT_SEPARATED_TRANSACTION_REQUEST", "CREDIT_SEPARATED_TRANSACTION_CREATED", "CREDIT_TRANSACTION_REQUESTED", "ACCOUNT_CANCELLED", "CARD_BLOCKED", "SUCCESS", "SUCCESS_EVENT_SENT"]; example: "CREATED" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `delinquent-account-delinquent-account-1` | https://developers.pismo.io/events/docs/delinquent-account-delinquent-account-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-GS-get-started-with-pismo-apis`.

<!-- op: spec=api-specs/Revolving_credit_-_Delinquent_account.yaml method=GET path=/v1/accounts/{account_id} operationId=delinquent-account-closure-get -->
### `GET /v1/accounts/{account_id}` — Get delinquent account closure process information

- **operationId:** `delinquent-account-closure-get`
- **Specification:** `api-specs/Revolving_credit_-_Delinquent_account.yaml` (Revolving credit - Delinquent account)
- **Server base URL(s):** `https://sandbox.pismolabs.io/delinquent-account`
- **Tags:** `Delinquent account closure`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a delinquent account closure entity that was accepted in the process.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `account_id` | path | yes | integer | Account ID | example: 6912345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok - Indicates that the delinquent account process for the given account was found and returned. | `application/json`: object (schema `GetAccountCloseResponse`) |
| 400 | Bad Request |  |
| 404 | Not Found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `delinquent_account_closure_id` | integer (schema `DelinquentAccountClosureID`) | no | ID for the delinquent account closure | example: 1 |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking identifier. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128. If a client <br>clicks the button more than once when sending the command to close an account, the Pismo platform could create duplicate <br>requests. The tracking identifier enables the platform to identify duplicates and ignore them.<br> | minLength: 1; maxLength: 128; example: "3368328d-e4c6-4c75-99a9-9d59f3501d8c" |
| `open_due_date` | string (schema `OpenDueDate`) | no | Open due date. This is the first day that the account became overdue. BRT (Brazilian time zone = UTC-03). | example: "2023-01-01" |
| `due_days` | integer (schema `DueDays`) | no | Due days. The number of days the account has been overdue. (Today minus `open_due_date`). | example: 10 |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (UTC) that asset was registered on Pismo platform | example: "2023-03-30T12:26:41" |
| `updated_at` | string (schema `UpdatedAt`) | no | Date closure was updated. BRT (Brazilian time zone = UTC-03). | example: "2022-02-01" |
| `status` | string (schema `AccountStatus`) | no | Delinquent account entity status<br><br>This field can have the following values.<br>`CREATED`—Created a delinquent account register to initiate the process.<br>`STARTED`—Started posting interest accruals.<br>`INTEREST_ACCRUAL_POSTED`—Finished posting nterest accruals.<br>`INSTALLMENT_ADVANCED`—Checked all transactions that need to be deducted separately.<br>`CREDIT_SEPARATED_TRANSACTION_REQUEST`—Requested a deduction for each transaction selected to be settled separately.<br>`CREDIT_SEPARATED_TRANSACTION_CREATED`—Created deduction transactions.<br>`CREDIT_TRANSACTION_REQUESTED`—Posted a credit transaction to the account.<br>`ACCOUNT_CANCELLED`—Cancelled account.<br>`CARD_BLOCKED`—Requested that all cards be blocked.<br>`SUCCESS`—Blocked all cards. Generated account [delinquent closure event](https://developers.pismo.io/events/docs/delinquent-account-delinquent-account-1).<br>`SUCCESS_EVENT_SENT`—Sent `SUCCESS` event to customer.<br> | enum: ["CREATED", "STARTED", "INTEREST_ACCRUAL_POSTED", "INSTALLMENTS_ADVANCED", "CREDIT_SEPARATED_TRANSACTION_REQUEST", "CREDIT_SEPARATED_TRANSACTION_CREATED", "CREDIT_TRANSACTION_REQUESTED", "ACCOUNT_CANCELLED", "CARD_BLOCKED", "SUCCESS", "SUCCESS_EVENT_SENT"]; example: "CREATED" |
| `installment_advance_id` | integer (schema `InstallmentAdvanceID`) | no | Installment advance ID. If the account has any future installments, they need to be advanced to the current cycle <br>before the account can be closed. `installment-advance-id` is the ID of the debit transaction that is used to advance <br>those installments.<br> | example: 1 |
| `authorization_id` | integer (schema `AuthorizationID`) | no | Before the Pismo platform can close an account, the account's balance must be zero. If that is not the case, the platform creates a debit transaction for the non-zero amount. `authorization_id` is the authorization ID for this transaction.<br> | example: 1 |
| `cards` | array of object | no |  |  |
| `cards[].id` | integer | no | Card ID | example: 1 |
| `cards[].status` | string | no | Card status | enum: ["CREATED", "UNBOUND", "NORMAL", "REISSUED", "BLOCKED", "PENDING", "WARNING", "LOST", "ROBBED", "EXPIRED", "DAMAGED", "FRAUD", "CANCELED", "DELETED", "BROKEN", "THEFT", "DEFECT"]; example: "NORMAL" |
| `cards[].type` | string | no | Card type | enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: "PLASTIC" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-credit-liquidation`.

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
| `api-specs/Revolving_credit_-_Delinquent_account.yaml` | tag `Delinquent account closure`: POST /v1/accounts/{account_id}/close, GET /v1/accounts/{account_id} | https://github.com/PismoDevEx/pismo-api-specs | `07df8bb5c17143f2…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CRED-credit-liquidation` — Credit liquidation
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
