---
ku_id: KU-API-card-issuing-disputes--state-check
title: 'API reference: Card issuing - Disputes — State check'
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
- get-v1-disputes-disputeId-possible-status
- get-v1-disputes-possible-status
related_kus:
- KU-CARD-disputes-overview
- KU-CARD-disputes-state-machine
specification_version: 1.0.0
---

# API reference: Card issuing - Disputes — State check

**KU ID:** `KU-API-card-issuing-disputes--state-check` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `State check` in `api-specs/Card_issuing_-_Disputes.yaml` (“Card issuing - Disputes”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to check a dispute's current or possible states

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/disputes/{disputeId}/possible-status` | `get-v1-disputes-disputeId-possible-status` | Get possible dispute states | no |
| `GET /v1/disputes/possible-status` | `get-v1-disputes-possible-status` | Get possible states | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v1/disputes/{disputeId}/possible-status operationId=get-v1-disputes-disputeId-possible-status -->
### `GET /v1/disputes/{disputeId}/possible-status` — Get possible dispute states

- **operationId:** `get-v1-disputes-disputeId-possible-status`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `State check`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get possible states for a specified dispute.
>
> See <a href="https://developers.pismo.io/pismo-docs/docs/disputes-state-machine" target="_blank">Disputes state machine</a>.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeId` | path | yes | number | Dispute ID |  |
| `disputeInstallmentId` | query | no | number | Dispute installment ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `StateMachineConfigResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `Sample result of possibles status`:

```json
[
  {
    "source": "PENDING",
    "target": "OPENED",
    "event": "OPEN"
  }
]
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-overview`, `KU-CARD-disputes-state-machine`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v1/disputes/possible-status operationId=get-v1-disputes-possible-status -->
### `GET /v1/disputes/possible-status` — Get possible states

- **operationId:** `get-v1-disputes-possible-status`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `State check`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get possible dispute states given a state machine and dispute status.
>
> See <a href="https://developers.pismo.io/pismo-docs/docs/disputes-state-machine">Disputes state machine</a> for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `type` | header | yes | string | State machine type | enum: ["PRIMITIVE", "PRIMITIVE_ON_US"] |
| `source` | header | yes | string | Dispute status enums | enum: ["OPENED", "PENDING", "CANCELED", "FAILED", "CHARGEBACK_REJECTED", "CHARGEBACK_CREATED", "CHARGEBACK_ACCEPTED", "CHARGEBACK_CLOSED", "SECOND_PRESENTMENT", "PRE_ARBITRATION_OPENED", "PRE_ARBITRATION_ACCEPTED", "PRE_ARBITRATION_DECLINED", "PRE_ARBITRATION_RECALL", "PRE_ARB_ALLOCATION_OPENED", "FAILED_PRE_ARBITRATION", "PRE_ARB_ALLOCATION_ACCEPTED", "PRE_ARB_ALLOCATION_DECLINED", "PRE_ARB_ALLOCATION_RECALLED", "FAILED_DECLINE_PRE_ARB", "FAILED_ACCEPT_PRE_ARB", "FAILED_ON_CLOSE", "EXPIRED", "ISSUER_LOSS", "MIGRATION", "FAILED_MIGRATION"]; example: "OPENED"; example: "OPENED" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `StateMachineConfigResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `Sample result of possibles status`:

```json
[
  {
    "source": "PENDING",
    "target": "OPENED",
    "event": "OPEN"
  }
]
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-state-machine`.

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
| `api-specs/Card_issuing_-_Disputes.yaml` | tag `State check`: GET /v1/disputes/{disputeId}/possible-status, GET /v1/disputes/possible-status | https://github.com/PismoDevEx/pismo-api-specs | `5c1d5513e1f3a4d1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-disputes-overview` — Disputes overview
- `KU-CARD-disputes-state-machine` — Disputes state machine
