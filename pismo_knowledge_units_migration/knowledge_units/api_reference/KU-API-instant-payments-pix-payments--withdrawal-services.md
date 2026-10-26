---
ku_id: KU-API-instant-payments-pix-payments--withdrawal-services
title: 'API reference: Instant payments - Pix payments — Withdrawal services'
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
operations:
- post-validate
- get-withdrawal-service-point
related_kus: []
specification_version: '1.0'
---

# API reference: Instant payments - Pix payments — Withdrawal services

**KU ID:** `KU-API-instant-payments-pix-payments--withdrawal-services` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Withdrawal services` in `api-specs/Instant_payments_-_Pix_payments.yaml` (“Instant payments - Pix payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /pix/v1/pix/transmitter-withdrawal/validate` | `post-validate` | Validate bank as withdrawal servicer | no |
| `GET /pix/v1/pix/withdrawal-service-point` | `get-withdrawal-service-point` | Get withdrawal service agent information | no |

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=POST path=/pix/v1/pix/transmitter-withdrawal/validate operationId=post-validate -->
### `POST /pix/v1/pix/transmitter-withdrawal/validate` — Validate bank as withdrawal servicer

- **operationId:** `post-validate`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Withdrawal services`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Validate if a participant (bank) is a withdrawal service facilitator or not.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation ID UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |
| `ispb` | query | yes | string | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `pix.ValidateTransmitterWithdrawalResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 429 | Too many requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway timeout | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `is_transmitter_withdrawal` | boolean | no | Is this a withdrawal servicer? |  |

##### Response 429

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;429;500;502;504`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=GET path=/pix/v1/pix/withdrawal-service-point operationId=get-withdrawal-service-point -->
### `GET /pix/v1/pix/withdrawal-service-point` — Get withdrawal service agent information

- **operationId:** `get-withdrawal-service-point`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Withdrawal services`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get information about withdrawal service agents (WSA) or the direct ISP participant providing the withdrawal service. 
>
> A WSA is a service provider that facilitates the withdrawal of funds in Pix. It acts as a bridge between Pix and customers who want to withdraw funds from their accounts.
>
> A WSA point is a location or access point where users can physically or digitally access WSA services. This could be a physical location such as a bank branch or retail store or digital acceess point such as a mobile app or web portal.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation ID UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |
| `ispbTransmitter` | query | yes | string | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. The ISPB transmitter ensures the payment request is directed to the correct receiving institution based on the ISPB code associated with the beneficiary's account. | maxLength: 8 |
| `page` | query | yes | string | Page number. Default = `1`. | example: "1" |
| `limit` | query | no | integer | Maximum number of agents to return. Default is all. | example: 20 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `pix.WithdrawalServicePointResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 429 | Too many requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway timeout | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `meta` | object (schema `pix.Meta`) | no |  |  |
| `records` | array of object (schema `pix.Records`) | no |  |  |

##### Response 429

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;429;500;502;504`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/customer.Error -->
### Schema `customer.Error`

Pointer: `#/components/schemas/customer.Error`. Type: object (schema `customer.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error's code. | example: "EPT0001" |
| `details` | object (schema `customer.DetailMessage`) | no |  |  |
| `message` | string | no | Error's message. | example: "User not found" |

<!-- schema: #/components/schemas/pix.Meta -->
### Schema `pix.Meta`

Pointer: `#/components/schemas/pix.Meta`. Type: object (schema `pix.Meta`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `date_time_data_generation` | string | no | Date/time date generated. RFC 3339 format. | example: "2023-04-12T23:20:50.52Z" |
| `ispb_transmitting` | string | no | ISPB (Brazilian bank ID) transmitting | example: "87653099" |
| `name_transmitting` | string | no | Name of ISPB transmitting | example: "Joe's bank" |
| `total_pages` | string | no | Total pages | example: "10" |
| `total_records` | string | no | Total records | example: "20" |

<!-- schema: #/components/schemas/pix.Records -->
### Schema `pix.Records`

Pointer: `#/components/schemas/pix.Records`. Type: object (schema `pix.Records`).

> Agent information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name_agent_withdrawal` | string | no | Withdrawal agent name | example: "Ruth Les" |
| `point_attendance` | array of object (schema `pix.PointAttendance`) | no | Where WSA service point is available - bank branches, ATMs, stores, and so on. |  |
| `tax_id_agent_withdrawal` | string | no | Withdrawal agent tax ID | example: "123412341234" |

<!-- schema: #/components/schemas/customer.DetailMessage -->
### Schema `customer.DetailMessage`

Pointer: `#/components/schemas/customer.DetailMessage`. Type: object (schema `customer.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `customer.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `customer.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `customer.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/pix.PointAttendance -->
### Schema `pix.PointAttendance`

Pointer: `#/components/schemas/pix.PointAttendance`. Type: object (schema `pix.PointAttendance`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `address` | string | no | Agent address | example: "Av Augusta, apt 1024" |
| `city` | string | no | Agent city | example: "Sao Paulo" |
| `latitude` | string | no | Latitude | example: "23.5558 S" |
| `longitude` | string | no | Longitude | example: "46.6396 W" |
| `name` | string | no | Name | example: "Jenny Side" |
| `neighborhood` | string | no | Neighborhood | example: "Bela Vista" |
| `observations` | string | no | Observations. Any additional text or information. |  |
| `period` | array of object (schema `pix.Period`) | no |  |  |
| `postal_code` | string | no | Postal code | example: "01000-000" |
| `products` | object (schema `pix.Products`) | no | Available agent services |  |
| `state` | string | no | State | example: "Rio de Janiero" |

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

<!-- schema: #/components/schemas/pix.Period -->
### Schema `pix.Period`

Pointer: `#/components/schemas/pix.Period`. Type: object (schema `pix.Period`).

> Date and times when access is available

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `maximum_value_available` | string | no | Maximum value available | example: "10000" |
| `weekly_day` | string | no | Weekly day | example: "Monday" |
| `working_period` | object (schema `pix.WorkingPeriod`) | no |  |  |

<!-- schema: #/components/schemas/pix.Products -->
### Schema `pix.Products`

Pointer: `#/components/schemas/pix.Products`. Type: object (schema `pix.Products`).

> Available agent services

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pix_change` | boolean | no | Is Pix change transaction available? |  |
| `pix_withdrawal` | boolean | no | Is Pix withdrawal transaction available? |  |

<!-- schema: #/components/schemas/pix.WorkingPeriod -->
### Schema `pix.WorkingPeriod`

Pointer: `#/components/schemas/pix.WorkingPeriod`. Type: object (schema `pix.WorkingPeriod`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `closing_withdrawal` | string | no | Closing withdrawal time | example: "18:00" |
| `opening_withdrawal` | string | no | Opening withdrawal time | example: "08:00" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_Pix_payments.yaml` | tag `Withdrawal services`: POST /pix/v1/pix/transmitter-withdrawal/validate, GET /pix/v1/pix/withdrawal-service-point | https://github.com/PismoDevEx/pismo-api-specs | `034f2ce79f002354…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
