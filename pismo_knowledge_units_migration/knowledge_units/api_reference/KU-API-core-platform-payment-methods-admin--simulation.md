---
ku_id: KU-API-core-platform-payment-methods-admin--simulation
title: 'API reference: Core platform - Payment methods admin — Simulation'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Payment_methods_admin.yaml
  sha256: de72dd3be625cdd63ac20a2fe2245feae5d0f1235d70acd5cfc1e7997a78556e
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
- post-v1-simulation
related_kus:
- KU-CC-lending
- KU-CORE-simulation-service
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-LEND-book-a-loan
- KU-LEND-simulate-loans
specification_version: beta
---

# API reference: Core platform - Payment methods admin — Simulation

**KU ID:** `KU-API-core-platform-payment-methods-admin--simulation` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Simulation` in `api-specs/Core_platform_-_Payment_methods_admin.yaml` (“Core platform - Payment methods admin”, version `beta`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to handle administrative operations for simulations.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/simulations` | `post-v1-simulation` | Create simulation | no |

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_methods_admin.yaml method=POST path=/v1/simulations operationId=post-v1-simulation -->
### `POST /v1/simulations` — Create simulation

- **operationId:** `post-v1-simulation`
- **Specification:** `api-specs/Core_platform_-_Payment_methods_admin.yaml` (Core platform - Payment methods admin)
- **Server base URL(s):** `https://sandbox.pismolabs.io/payment-methods-admin`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Create a simulation. 
>
> Prior to calling this endpoint to create a simulation, you must create a simulation configuration via the [Create simulation config](ref:simulationconfigs) endpoint.
>
> Refer to the [Simulation service](doc:simulation-service) guide for additional information.

#### Request body

Required: no

> Create simulation

**Content type `application/json`** — schema: object (schema `SimulationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | yes | Total simulation amount | example: 100 |
| `authorization_mode` | string | yes | Requested simulation authorization mode. Credit cards can operate only in `CREDIT` mode. Debit cards from savings or checking accounts can operate only in `DEBIT` mode. Combo and multi-application cards can operate in both modes. **REQUIRED** for simulation requests, where message type indicator (MTI) is `0100` or `0120`.<br> | enum: ["CREDIT", "DEBIT"] |
| `card` | object | no | Information related to the card used to perform this simulation. |  |
| `card.pan` | string | no | Primary account number (PAN) of the card being used for simulation. Provide this field when simulating from an existing card. | example: "5555550000000001" |
| `custom_filters` | array of string | no | Custom filters to be used in the simulation | example: ["custom filter1", "custom filter2", "custom filter3"] |
| `document_number` | string | no | Document number related to the account to be used as the owner of this request. Provide this field for simulations based on a client document number. | example: "39947739977" |
| `merchants` | array of string | no | Merchant IDs used to filter the simulation | example: ["MERCH01", "MERCH02", "MERCH03"] |
| `payment_agreement` | object | no | Payment agreement information |  |
| `payment_agreement.original_principal_amount` | number | no | Principal amount in the original contract | example: 80 |
| `payment_agreement.applied_interest_amount` | number | no | Applied interest amount in the original contract | example: 80 |
| `payment_agreement.down_payment` | number | no | Down payment | example: 50 |
| `plan_ids` | array of string | no | Plan IDs used to filter the simulation. **REQUIRED** when neither `card.pan` nor `document_number` is provided. | example: ["000700", "000800", "000900"] |
| `processing_codes` | array of string | no | Procesing codes used to filter the simulation | example: ["000700", "000800", "000900"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `SimulationResponse`) |
| 400 | Bad request | `application/json`: object (schema `UnexpectedError`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `UnexpectedError`) |
| 500 | Internal Server Error | `application/json`: object (schema `UnexpectedError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | Pismo ID of the account assigned as the owner of this request. Omitted for prospect simulations. | example: 123 |
| `program_id` | number | no | Program ID linked to the user account. Omitted for prospect simulations. | example: 1 |
| `amount` | number | no | Total simulation amount | example: 100 |
| `simulation` | object | no | Any valid JSON that contains useful simulation information |  |

##### Response 400

400 Example `Invalid payload`:

```json
{
  "code": "DO0002",
  "message": "Invalid Request.",
  "violations": [
    {
      "code": "field",
      "message": "required"
    }
  ]
}
```

##### Response 422

422 Example `Invalid payload`:

```json
{
  "code": "SI001",
  "message": "An unexpected error happened.",
  "violations": [
    {
      "code": "SI003",
      "message": "Card doesn't have authorization mode created."
    }
  ]
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `DO0002` | Invalid Request. |
| 422 | `SI001` | An unexpected error happened. |
| 422 | `SI003` | Card doesn't have authorization mode created. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;422;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CC-lending`, `KU-CORE-simulation-service`, `KU-LEND-book-a-loan`, `KU-LEND-simulate-loans`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/UnexpectedError -->
### Schema `UnexpectedError`

Pointer: `#/components/schemas/UnexpectedError`. Type: object (schema `UnexpectedError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "DO0001" |
| `message` | string | no | Error description | example: "An unexpected error happened." |
| `violations` | array of object | no |  |  |
| `violations[].code` | string | no | Violation error code | example: "AC000" |
| `violations[].message` | string | no | Violation error description | example: "An unexpected error has occurred" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Payment_methods_admin.yaml` | tag `Simulation`: POST /v1/simulations | https://github.com/PismoDevEx/pismo-api-specs | `de72dd3be625cdd6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CC-lending` — Control Center lending: loan products and loan management
- `KU-CORE-simulation-service` — Simulation service
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-LEND-book-a-loan` — Book loans
- `KU-LEND-simulate-loans` — Simulate loans
