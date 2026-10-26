---
ku_id: KU-API-revolving-credit-statements--advancements
title: 'API reference: Revolving credit - Statements — Advancements'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Statements.yaml
  sha256: 2ffe392a0e56ae3b5bf71474f241d08b9b078bb852ffaeff142b4dd32d278fd1
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
- GetInstallmentAdvancedSimulationV2
- InstallmentAdvancedV2
- GetInstallmentsAdvanceV2
- CancelInstallmentsAdvanceV2
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CRED-agreements
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-balance
- KU-EVT-statement-data-events
- KU-PAY-installments-payment
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Advancements

**KU ID:** `KU-API-revolving-credit-statements--advancements` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Advancements` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Installment advancement endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /statements/v2/accounts/{accountId}/installment-advance` | `GetInstallmentAdvancedSimulationV2` | Get simulation installment advancement (deprecated) | **yes** |
| `POST /statements/v2/accounts/{accountId}/installment-advance` | `InstallmentAdvancedV2` | Create installment advancement (no cancellation event) (deprecated) | **yes** |
| `GET /statements/v2/accounts/{accountId}/installment-advance/{id}` | `GetInstallmentsAdvanceV2` | Get installment advancement (no cancellation event) (deprecated) | **yes** |
| `DELETE /statements/v2/accounts/{accountId}/installment-advance/{id}` | `CancelInstallmentsAdvanceV2` | Cancel installments advancement (no cancellation event) (deprecated) | **yes** |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements/v2/accounts/{accountId}/installment-advance operationId=GetInstallmentAdvancedSimulationV2 -->
### `GET /statements/v2/accounts/{accountId}/installment-advance` — Get simulation installment advancement (deprecated)

- **operationId:** `GetInstallmentAdvancedSimulationV2`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Advancements`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a simulation installment advancement with filtering options. This is a DEPRECATED endpoint. Use the non-deprecated [Simulate installment advancement](ref:simulateinstallmentadvancement) endpoint instead.<br>

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `transactionId` | query | no | integer | Transaction ID for installment advance | format: "int32"; example: 10101 |
| `mode` | query | no | string | Mode for installment advances: `all` or `single`. If it is `all`, all future installments of the account are advanced. (Property `transactionId` is ignored.) | enum: ["all", "single"]; default: "single"; example: "all" |
| `installmentsToAdvance` | query | no | integer | Number of installments to advance | format: "int32"; example: 12 |
| `removeInterestFromCurrent` | query | no | boolean | Are the current interests removed (`true`) or not (`false`)? Default is `false`. | example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: oneOf: object (schema `InstallmentAdvancedSimutationV2ResponseSuccess`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `InvalidFieldErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `Account Not Found` — from `#/components/examples/AccountNotFound`:

```json
{
  "message": "Account not found."
}
```

400 Example `Installment Not Found to Advance` — from `#/components/examples/InstallmentNotFoundToAdvance`:

```json
{
  "message": "Not found installments to advance for accountId: 999999 and transactionId: 99999999"
}
```

400 Example `Invalid Number of Installments to Advance` — from `#/components/examples/InvalidNumberOfInstallmentsToAdvance`:

```json
{
  "message": "Invalid number of installments to advance. Number of installments to advance=10 Available installments=5)"
}
```

##### Response 423

423 Example `Account Locked`:

```json
{
  "message": "The operation could not be completed because another process is manipulating the account (the account lock could not be obtained). Try again in a moment."
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
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;423;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=POST path=/statements/v2/accounts/{accountId}/installment-advance operationId=InstallmentAdvancedV2 -->
### `POST /statements/v2/accounts/{accountId}/installment-advance` — Create installment advancement (no cancellation event) (deprecated)

- **operationId:** `InstallmentAdvancedV2`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Advancements`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an installment advancement. This is a DEPRECATED endpoint. Use the non-deprecated [Create installment advancement](ref:createinstallmentadvancementv2) endpoint instead.<br>
> An installment advancement is a transfer of one or more installments from future cycles to the present cycle. For more information, refer to [Manage installments on the customer statement](doc:installments-payment#manage-installments-on-the-customer-statement).
>
> This endpont generates an [Installment advanced](https://developers.pismo.io/events/docs/balance-installment-advancement-1) event.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.        

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Request body

Required: no

> Installment Advanced Request Body

**Content type `application/json`** — schema: object (schema `InstallmentAdvancedV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_id` | integer (schema `InstallmentAdvancedTransactionID`) | no | Installment advanced transaction ID.	**REQUIRED**  when mode = `single`.<br>This parameter can be from any transaction related to the contract.<br> | format: "int64"; example: 10101 |
| `mode` | string (schema `InstallmentAdvancedMode`) | no | Installment advanced mode. If `all`, all future account installments are advanced (and `transaction_id` is ignored). | enum: ["all", "single"]; example: "all" |
| `installments_to_advance` | integer (schema `InstallmentsToAdvanceWhenSingleMode`) | no | Number of installments to advance. Only considered when mode =  `single`. If not passed, all installments are advanced. | format: "int32"; example: 12 |
| `remove_interest_from_current` | boolean (schema `RemoveInterestFromCurrent`) | no | Are the current interests removed from the installment in the current statement (`true`) or not (`false`)? This field is considered when mode = `all`. Note that all interest from future installments are always removed when they are advanced. If mode = `single`, it is not possible to remove interest from the installment in the current statement. Default is `false`.<br> | example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: oneOf: object (schema `InstallmentAdvancedV2ResponseSuccess`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `InvalidFieldErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `Account Not Found` — from `#/components/examples/AccountNotFound`:

```json
{
  "message": "Account not found."
}
```

400 Example `Installment Not Found to Advance` — from `#/components/examples/InstallmentNotFoundToAdvance`:

```json
{
  "message": "Not found installments to advance for accountId: 999999 and transactionId: 99999999"
}
```

400 Example `Invalid Number of Installments to Advance` — from `#/components/examples/InvalidNumberOfInstallmentsToAdvance`:

```json
{
  "message": "Invalid number of installments to advance. Number of installments to advance=10 Available installments=5)"
}
```

##### Response 423

423 Example `Account Locked`:

```json
{
  "message": "The operation could not be completed because another process is manipulating the account (the account lock could not be obtained). Try again in a moment."
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
| 500 | `GN0001` | Service is unavailable |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-installment-advancement-1` | https://developers.pismo.io/events/docs/balance-installment-advancement-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;423;500`, has examples `True`, emits events `1`, deprecated `True`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-agreements`, `KU-EVT-statement-data-events`, `KU-PAY-installments-payment`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements/v2/accounts/{accountId}/installment-advance/{id} operationId=GetInstallmentsAdvanceV2 -->
### `GET /statements/v2/accounts/{accountId}/installment-advance/{id}` — Get installment advancement (no cancellation event) (deprecated)

- **operationId:** `GetInstallmentsAdvanceV2`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Advancements`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get an installments advancement by account ID and installments advancement ID. This is a DEPRECATED endpoint. Use the non-deprecated [Get installment advancement](ref:getinstallmentadvancementv2byid) endpoint instead.<br>
>
> This endpont generates an [Installment advanced](https://developers.pismo.io/events/docs/balance-installment-advancement-1) event.        
>
> **Notes:**
> - Cancelling an installment advancement created with this endpoint does not generate a cancellation event. Pismo recommends that you use the most advanced version of the installment advancement endpoints instead:
>   <br>[Create installment advancement](ref:createinstallmentadvancementv2)
>   <br>[Get installment advancement](ref:getinstallmentadvancementv2byid)
>   <br>[Cancel installment advancement](ref:cancelinstallmentadvancev2)      
> - This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.        

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `id` | path | yes | string | Payment agreement ID | example: "4101" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `InstallmentAdvancedV2ResponseSuccess`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `InvalidFieldErrorResponse`) |
| 404 | Not Found | `application/json`: anyOf: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `InstallmentsAdvancedID`) | no | Installments advanced ID | format: "int32"; example: 101010 |
| `status` | string (schema `InstallmentsAdvancedStatus`) | no | Installments advanced status | enum: ["processed", "cancelled", "pending", "error"]; example: "processed" |
| `transaction_id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 77489 |
| `transactions` | array of object | no | Installments advanced's transaction Id |  |
| `transactions[].id` | integer (schema `InstallmentsAdvancedTransactionID`) | no | Installments advanced transaction ID | format: "int32"; example: 101010 |
| `transactions[].statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `transactions[].amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; example: 150 |
| `transactions[].interest_amount` | number (schema `InterestAmount`) | no | Interest amount. Maximum of 2 digits allowed after the decimal place. | format: "float"; example: 12.35 |
| `transactions[].adjusted_amount` | number (schema `AdjustedAmount`) | no | Adjusted amount for transaction for installments advanced | format: "float"; example: 450 |
| `created_at` | string (schema `CreatedAt`) | no | Creation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-10T00:00:00" |
| `cancelled_at` | string (schema `CanceledAt`) | no | Cancellation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-20T00:00:00" |

##### Response 400

400 Example `Account Not Found` — from `#/components/examples/AccountNotFound`:

```json
{
  "message": "Account not found."
}
```

##### Response 404

404 Example `Installment Advanced Not Found`:

```json
{
  "message": "Installments advanced not found"
}
```

404 Example `Transaction Advanced Not Found`:

```json
{
  "message": "Transaction advanced with id 99999 not found"
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
| 500 | `GN0001` | Service is unavailable |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-installment-advancement-1` | https://developers.pismo.io/events/docs/balance-installment-advancement-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `1`, deprecated `True`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=DELETE path=/statements/v2/accounts/{accountId}/installment-advance/{id} operationId=CancelInstallmentsAdvanceV2 -->
### `DELETE /statements/v2/accounts/{accountId}/installment-advance/{id}` — Cancel installments advancement (no cancellation event) (deprecated)

- **operationId:** `CancelInstallmentsAdvanceV2`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Advancements`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel an installment advancement by account ID and advancement ID. This is a DEPRECATED endpoint. Use the non-deprecated [Get installment advancement](ref:getinstallmentadvancementv2byid) endpoint instead.<br>
>
> This endpont generates an [Installment advanced](https://developers.pismo.io/events/docs/balance-installment-advancement-1) event.        
>
> **Note:** Cancelling an installment advancement created with this endpoint does not generate a cancellation event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `id` | path | yes | string | Payment agreement ID | example: "4101" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `InstallmentAdvancedV2ResponseSuccess`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `InvalidFieldErrorResponse`) |
| 404 | Not Found | `application/json`: anyOf: object (schema `ErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `InstallmentsAdvancedID`) | no | Installments advanced ID | format: "int32"; example: 101010 |
| `status` | string (schema `InstallmentsAdvancedStatus`) | no | Installments advanced status | enum: ["processed", "cancelled", "pending", "error"]; example: "processed" |
| `transaction_id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 77489 |
| `transactions` | array of object | no | Installments advanced's transaction Id |  |
| `transactions[].id` | integer (schema `InstallmentsAdvancedTransactionID`) | no | Installments advanced transaction ID | format: "int32"; example: 101010 |
| `transactions[].statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `transactions[].amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; example: 150 |
| `transactions[].interest_amount` | number (schema `InterestAmount`) | no | Interest amount. Maximum of 2 digits allowed after the decimal place. | format: "float"; example: 12.35 |
| `transactions[].adjusted_amount` | number (schema `AdjustedAmount`) | no | Adjusted amount for transaction for installments advanced | format: "float"; example: 450 |
| `created_at` | string (schema `CreatedAt`) | no | Creation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-10T00:00:00" |
| `cancelled_at` | string (schema `CanceledAt`) | no | Cancellation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-20T00:00:00" |

##### Response 400

400 Example `Account Not Found` — from `#/components/examples/AccountNotFound`:

```json
{
  "message": "Account not found."
}
```

400 Example `Already Cancelled`:

```json
{
  "message": "Installments advanced already cancelled"
}
```

400 Example `Period expired`:

```json
{
  "message": "Cancellation not allowed, period expired"
}
```

400 Example `Out of cicle`:

```json
{
  "message": "Cancellation not allowed, out of cicle"
}
```

400 Example `Changed Transaction Balance`:

```json
{
  "message": "Cancellation not allowed, changed transaction balance."
}
```

##### Response 404

404 Example `Installment Advanced Not Found`:

```json
{
  "message": "Installments advanced not found"
}
```

404 Example `Transaction Advanced Not Found`:

```json
{
  "message": "Transaction advanced with id 99999 not found"
}
```

##### Response 423

423 Example `Account Locked`:

```json
{
  "message": "The operation could not be completed because another process is manipulating the account (the account lock could not be obtained). Try again in a moment."
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
| 500 | `GN0001` | Service is unavailable |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-installment-advancement-1` | https://developers.pismo.io/events/docs/balance-installment-advancement-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;423;500`, has examples `True`, emits events `1`, deprecated `True`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-statement-data-events`, `KU-PAY-installments-payment`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Internal error" |

<!-- schema: #/components/schemas/InvalidFieldErrorResponse -->
### Schema `InvalidFieldErrorResponse`

Pointer: `#/components/schemas/InvalidFieldErrorResponse`. Type: object (schema `InvalidFieldErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Amount must not be empty." |
| `field` | string | yes | Field where error occurred. | example: "amount" |

## Lifecycle status

- `GET /statements/v2/accounts/{accountId}/installment-advance` (`GetInstallmentAdvancedSimulationV2`) is marked `deprecated: true` in the specification.
- `POST /statements/v2/accounts/{accountId}/installment-advance` (`InstallmentAdvancedV2`) is marked `deprecated: true` in the specification.
- `GET /statements/v2/accounts/{accountId}/installment-advance/{id}` (`GetInstallmentsAdvanceV2`) is marked `deprecated: true` in the specification.
- `DELETE /statements/v2/accounts/{accountId}/installment-advance/{id}` (`CancelInstallmentsAdvanceV2`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Advancements`: GET /statements/v2/accounts/{accountId}/installment-advance, POST /statements/v2/accounts/{accountId}/installment-advance, GET /statements/v2/accounts/{accountId}/installment-advance/{id}, DELETE /statements/v2/accounts/{accountId}/installment-advance/{id} | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CRED-agreements` — Agreements: compulsory, statement, installment and payment agreements
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-EVT-statement-data-events` — Revolving credit - Statements
- `KU-PAY-installments-payment` — Installments payment
