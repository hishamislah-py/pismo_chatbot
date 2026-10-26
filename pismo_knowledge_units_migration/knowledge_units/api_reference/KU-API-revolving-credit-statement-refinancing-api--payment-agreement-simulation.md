---
ku_id: KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation
title: 'API reference: Revolving credit - Statement refinancing — Payment agreement simulation'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Statement_refinancing_API.yaml
  sha256: da61958debc1471e98bd56db02b8026a49d892798d7f9f63597d051a892ea0f8
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
- create-payment-agreement-simulation
- get-payment-agreement-simulation
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
- KU-EVT-catalogue-balance
- KU-EVT-catalogue-other-domains
specification_version: 1.0.0
---

# API reference: Revolving credit - Statement refinancing — Payment agreement simulation

**KU ID:** `KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Payment agreement simulation` in `api-specs/Revolving_credit_-_Statement_refinancing_API.yaml` (“Revolving credit - Statement refinancing”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage payment agreement simulations

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/accounts/{accountId}/payment-agreement-simulations` | `create-payment-agreement-simulation` | Create payment agreement simulation | no |
| `GET /v1/accounts/{accountId}/payment-agreement-simulations/{paymentAgreementSimulationId}` | `get-payment-agreement-simulation` | Get payment agreement simulation | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statement_refinancing_API.yaml method=POST path=/v1/accounts/{accountId}/payment-agreement-simulations operationId=create-payment-agreement-simulation -->
### `POST /v1/accounts/{accountId}/payment-agreement-simulations` — Create payment agreement simulation

- **operationId:** `create-payment-agreement-simulation`
- **Specification:** `api-specs/Revolving_credit_-_Statement_refinancing_API.yaml` (Revolving credit - Statement refinancing)
- **Server base URL(s):** `https://sandbox.pismolabs.io/statement-refinancing`
- **Tags:** `Payment agreement simulation`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a payment agreement simulation.
>
> If successful, this endpoint generates a [Payment agreement simulation processed](https://developers.pismo.io/events/docs/balance-installment-payment-processed-1) event.
> If it fails, it generates a [Payment agreement simulation not processed](https://developers.pismo.io/events/docs/statement-refinancing-payment-agreement-simulation-not-processed-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 101 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `PaymentAgreementSimulationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `plan_ids` | array of string (schema `SimulationPlanIDs`) | no | List of plan IDs used in the payment agreement simulation | example: ["id1", "id2", "id3"] |
| `down_payment` | number (schema `DownPayment`) | no | Down payment amount | format: "double"; example: 500.99 |
| `type` | string (schema `PaymentAgreementType`) | no | Payment agreement type. Possible values:<br>- `STATEMENT_INSTALLMENT`: Customer makes an agreement with their credit card issuer stating that they aren't able to pay off their debt within the current month, so they intend to settle the amount over the next few bills.<br>- `STATEMENT_INSTALLMENT_COMPULSORY`: Issuer-imposed installment agreement renegotiated without customer input.<br>- `STATEMENT_AGREEMENT`: Customer renegotiates all pending debt for all their statements.<br><br>For more information, refer to the [Create payment agreement](ref:installmentpaymentsv4) endpoint and the [Credit card refinancing](doc:negotiating-credit-card-debt) guide.<br> | enum: ["STATEMENT_INSTALLMENT", "STATEMENT_INSTALLMENT_COMPULSORY", "STATEMENT_AGREEMENT"]; example: "STATEMENT_AGREEMENT" |
| `payment_date` | string (schema `SimulationPaymentDate`) | no | Date of first payment. Format = YYYY-MM-DD. | format: "date"; example: "2025-06-20" |
| `overridden_amount_due` | number (schema `OverriddenAmountDue`) | no | Overridden amount due. If provided, it overrides the total amount due for the account in the payment agreement simulation. Must be greater than zero and less than or equal to the current amount due. | format: "double"; example: 2000 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the simulation was successfully created. | `application/json`: object (schema `PaymentAgreementSimulationResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `created_at` | string (schema `PaymentAgreementSimulationCreatedAt`) | no | Timestamp when the payment agreement simulation was created. Format = YYYY-MM-DDThh:mm:ss.ssssssZ. | format: "date-time"; example: "2025-06-17T15:22:51.978005295" |
| `plan_ids` | array of string (schema `SimulationPlanIDs`) | no | List of plan IDs used in the payment agreement simulation | example: ["id1", "id2", "id3"] |
| `down_payment` | number (schema `DownPayment`) | no | Down payment amount | format: "double"; example: 500.99 |
| `overridden_amount_due` | number (schema `OverriddenAmountDue`) | no | Overridden amount due. If provided, it overrides the total amount due for the account in the payment agreement simulation. Must be greater than zero and less than or equal to the current amount due. | format: "double"; example: 2000 |
| `payment_date` | string (schema `SimulationPaymentDate`) | no | Date of first payment. Format = YYYY-MM-DD. | format: "date"; example: "2025-06-20" |
| `type` | string (schema `PaymentAgreementType`) | no | Payment agreement type. Possible values:<br>- `STATEMENT_INSTALLMENT`: Customer makes an agreement with their credit card issuer stating that they aren't able to pay off their debt within the current month, so they intend to settle the amount over the next few bills.<br>- `STATEMENT_INSTALLMENT_COMPULSORY`: Issuer-imposed installment agreement renegotiated without customer input.<br>- `STATEMENT_AGREEMENT`: Customer renegotiates all pending debt for all their statements.<br><br>For more information, refer to the [Create payment agreement](ref:installmentpaymentsv4) endpoint and the [Credit card refinancing](doc:negotiating-credit-card-debt) guide.<br> | enum: ["STATEMENT_INSTALLMENT", "STATEMENT_INSTALLMENT_COMPULSORY", "STATEMENT_AGREEMENT"]; example: "STATEMENT_AGREEMENT" |
| `status` | string (schema `PaymentAgreementSimulationStatus`) | no | Status of payment agreement simulation | enum: ["PENDING", "PROCESSED", "ERROR"]; example: "PENDING" |
| `cid` | string (schema `PaymentAgreementSimulationCorrelationID`) | no | Correlation ID for tracking the simulation request | format: "uuid"; example: "1144f6a7-ed73-4fd2-ba45-80d3b881cad6" |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-e7091464-cd1e-4c20-8c68-1e4c5774d972" |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
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
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 500 | `GN0001` | Service is unavailable |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-installment-payment-processed-1` | https://developers.pismo.io/events/docs/balance-installment-payment-processed-1 |
| `statement-refinancing-payment-agreement-simulation-not-processed-1` | https://developers.pismo.io/events/docs/statement-refinancing-payment-agreement-simulation-not-processed-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;423;500`, has examples `False`, emits events `2`, deprecated `False`.

<!-- op: spec=api-specs/Revolving_credit_-_Statement_refinancing_API.yaml method=GET path=/v1/accounts/{accountId}/payment-agreement-simulations/{paymentAgreementSimulationId} operationId=get-payment-agreement-simulation -->
### `GET /v1/accounts/{accountId}/payment-agreement-simulations/{paymentAgreementSimulationId}` — Get payment agreement simulation

- **operationId:** `get-payment-agreement-simulation`
- **Specification:** `api-specs/Revolving_credit_-_Statement_refinancing_API.yaml` (Revolving credit - Statement refinancing)
- **Server base URL(s):** `https://sandbox.pismolabs.io/statement-refinancing`
- **Tags:** `Payment agreement simulation`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a payment agreement simulation by its ID

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 101 |
| `paymentAgreementSimulationId` | path | yes | integer | Payment agreement simulation ID | example: 101023 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the simulation was successfully retrieved. | `application/json`: object (schema `GetPaymentAgreementSimulationResponse`) |
| 404 | Not Found - The specified simulation does not exist. |  |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payment_agreement_simulation_id` | integer (schema `PaymentAgreementSimulationID`) | no | Payment agreement simulation ID | format: "int64"; example: 12345678 |
| `created_at` | string (schema `PaymentAgreementSimulationCreatedAt`) | no | Timestamp when the payment agreement simulation was created. Format = YYYY-MM-DDThh:mm:ss.ssssssZ. | format: "date-time"; example: "2025-06-17T15:22:51.978005295" |
| `plan_ids` | array of string (schema `SimulationPlanIDs`) | no | List of plan IDs used in the payment agreement simulation | example: ["id1", "id2", "id3"] |
| `down_payment` | number (schema `DownPayment`) | no | Down payment amount | format: "double"; example: 500.99 |
| `payment_date` | string (schema `SimulationPaymentDate`) | no | Date of first payment. Format = YYYY-MM-DD. | format: "date"; example: "2025-06-20" |
| `type` | string (schema `PaymentAgreementType`) | no | Payment agreement type. Possible values:<br>- `STATEMENT_INSTALLMENT`: Customer makes an agreement with their credit card issuer stating that they aren't able to pay off their debt within the current month, so they intend to settle the amount over the next few bills.<br>- `STATEMENT_INSTALLMENT_COMPULSORY`: Issuer-imposed installment agreement renegotiated without customer input.<br>- `STATEMENT_AGREEMENT`: Customer renegotiates all pending debt for all their statements.<br><br>For more information, refer to the [Create payment agreement](ref:installmentpaymentsv4) endpoint and the [Credit card refinancing](doc:negotiating-credit-card-debt) guide.<br> | enum: ["STATEMENT_INSTALLMENT", "STATEMENT_INSTALLMENT_COMPULSORY", "STATEMENT_AGREEMENT"]; example: "STATEMENT_AGREEMENT" |
| `status` | string (schema `PaymentAgreementSimulationStatus`) | no | Status of payment agreement simulation | enum: ["PENDING", "PROCESSED", "ERROR"]; example: "PENDING" |
| `creation_cid` | string (schema `PaymentAgreementSimulationCorrelationID`) | no | Correlation ID for tracking the simulation request | format: "uuid"; example: "1144f6a7-ed73-4fd2-ba45-80d3b881cad6" |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-e7091464-cd1e-4c20-8c68-1e4c5774d972" |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1010 |
| `error_message` | object (schema `StandardErrorResponse`) | no |  |  |
| `simulations` | array of object (schema `SimulationObject`) | no | List of simulations generated based on the provided parameters |  |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "1020030" |
| `message` | string | no |  | example: "Error message" |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Internal error" |

<!-- schema: #/components/schemas/SimulationObject -->
### Schema `SimulationObject`

Pointer: `#/components/schemas/SimulationObject`. Type: object (schema `SimulationObject`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `NumberOfInstallments`) | no | Number of installments | format: "int32"; example: 8 |
| `plan_id` | string (schema `SimulationPlanID`) | no | Simulation plan ID | format: "uuid"; example: "5695f64c-ed54-4f52-ba45-80d3b121cad6" |
| `options` | object | no | Options used in the payment agreement simulation |  |
| `options.installments` | integer (schema `NumberOfInstallments`) | no | Number of installments | format: "int32"; example: 8 |
| `options.contract_amount` | number (schema `ContractAmount`) | no | Contract amount | format: "float"; example: 500 |
| `options.principal_amount` | number (schema `PrincipalAmount`) | no | Principal amount. (The sum of all overdue transactions.) | format: "float"; example: 1855 |
| `options.effective_annual_cost` | number (schema `EffectiveAnnualCost`) | no | Annual percentage rate (APR) | format: "double"; example: 100.56 |
| `options.first_installment_value` | number (schema `FirstInstallmentValue`) | no | First installment value | format: "double"; example: 80.5 |
| `options.installment_value` | number (schema `InstallmentValue`) | no | Value for each installment | format: "double"; example: 150.08 |
| `options.postings` | object | no | Postings used in the simulation |  |
| `options.postings.iof_amount` | number (schema `IofAmount`) | no | IOF (Brazilian tax) amount. Maximum of 2 digits allowed after the decimal place. | format: "float"; example: 1.35 |
| `options.postings.fixed_iof_amount` | number (schema `FixedIofAmount`) | no | Fixed IOF (Brazilian tax) Amount | format: "float"; example: 1.15 |
| `options.postings.interest_amount` | number (schema `InterestAmount`) | no | Interest amount. Maximum of 2 digits allowed after the decimal place. | format: "float"; example: 12.35 |
| `options.postings.fee_amount` | number (schema `FeeAmount`) | no | Fees amount | format: "double"; example: 30.5 |
| `options.rates` | object | no | Rates |  |
| `options.rates.conversion_rate` | number (schema `ConversionRate`) | no | Conversion rate | format: "double"; example: 5.5 |
| `options.rates.daily_iof_rate` | number (schema `DailyIofRate`) | no | Daily IOF (Brazilian tax) rate | format: "float"; example: 0.001 |
| `options.rates.fixed_iof_rate` | number (schema `FixedIofRate`) | no | Fixed IOF (Brazilian tax) rate | format: "float"; example: 0.1 |
| `options.rates.interest_rate` | number (schema `InterestRate`) | no | Interest rate | format: "double"; example: 10.99 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Statement_refinancing_API.yaml` | tag `Payment agreement simulation`: POST /v1/accounts/{accountId}/payment-agreement-simulations, GET /v1/accounts/{accountId}/payment-agreement-simulations/{paymentAgreementSimulationId} | https://github.com/PismoDevEx/pismo-api-specs | `da61958debc1471e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
