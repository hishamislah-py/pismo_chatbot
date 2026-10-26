---
ku_id: KU-API-instant-payments-pix-management--participants
title: 'API reference: Instant payments - Pix management — Participants'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Instant_payments_-_Pix_management.yaml
  sha256: 7d7fee078ccf55696a5fdd1a00ea559d88a6148a11b28529395dab8f2405a750
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
- get-v2-pix-dict-participants
related_kus:
- KU-ERR-codes-epda
specification_version: 0.0.1
---

# API reference: Instant payments - Pix management — Participants

**KU ID:** `KU-API-instant-payments-pix-management--participants` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Participants` in `api-specs/Instant_payments_-_Pix_management.yaml` (“Instant payments - Pix management”, version `0.0.1`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> List Pix participants registered in BCB DICT

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/pix/dict/participants` | `get-v2-pix-dict-participants` | List Pix participants | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v2/pix/dict/participants operationId=get-v2-pix-dict-participants -->
### `GET /v2/pix/dict/participants` — List Pix participants

- **operationId:** `get-v2-pix-dict-participants`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Participants`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Returns the list of all Pix participants (institutions) registered in the BCB DICT, including each participant's ISPB, institution name, type and Pix participation modality.
>
> This endpoint proxies the request in real time to the configured DICT provider — no local cache or database is involved — so response latency reflects the upstream provider.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization/tenant ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `x-cid` | header | no | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> | example: "B20220921145635222303062944CA66F" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `participant.ListParticipantsResponse`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `participants` | array of object (schema `participant.Participant`) | yes | List of Pix participants. |  |

200 Example `Success`:

```json
{
  "participants": [
    {
      "ispb": "19875244",
      "name": "COOPERATIVA DE ECONOMIA E CRÉDITO MÚTUO DAS EMPRESAS, EMPREGADOS E PRESTADORES DE SERVIÇO DAS METALÚRGICAS, SIDERÚRGICAS E INDUSTRIAIS – SICOOB COPESITA",
      "short_name": "CECM EMPR EMP PREST SERV METAL SIDER E IND SICOOB COPESITA",
      "type": "IDRT",
      "modality": "PDCT",
      "start_operation_datetime": "2020-11-03T09:30:00+00:00",
      "date": "2021-09-30"
    }
  ]
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `Missing required header 'x-tenant'`:

```json
{
  "code": "EPDA0009",
  "message": "Missing required header 'x-tenant'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `Provider not found`:

```json
{
  "code": "EPDA0187",
  "message": "SPI Dict Gateway - Not found"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `Internal error`:

```json
{
  "code": "EPDA0004",
  "message": "Internal error"
}
```

##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider returned 5xx`:

```json
{
  "code": "EPDA0018",
  "message": "SPI Gateway - API returned error"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Provider timeout`:

```json
{
  "code": "EPDA0030",
  "message": "SPI Gateway - API returned a timeout error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 404 | `EPDA0187` | SPI Dict Gateway - Not found |
| 500 | `EPDA0004` | Internal error |
| 502 | `EPDA0018` | SPI Gateway - API returned error |
| 504 | `EPDA0030` | SPI Gateway - API returned a timeout error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;403;404;500;502;504`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/participant.Participant -->
### Schema `participant.Participant`

Pointer: `#/components/schemas/participant.Participant`. Type: object (schema `participant.Participant`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `ispb` | string (schema `Ispb`) | yes | ISPB identifier - the Brazilian payment system identifier, an 8-digit value.<br> | maxLength: 8; example: "19875244" |
| `name` | string | yes | Full institution name. | maxLength: 200; example: "COOPERATIVA DE ECONOMIA E CRÉDITO MÚTUO DAS EMPRESAS, EMPREGADOS E PRESTADORES DE SERVIÇO DAS METALÚRGICAS, SIDERÚRGICAS E INDUSTRIAIS – SICOOB COPESITA" |
| `short_name` | string | yes | Short institution name. | maxLength: 60; example: "CECM EMPR EMP PREST SERV METAL SIDER E IND SICOOB COPESITA" |
| `type` | string (schema `ParticipantType`) | yes | Pix institution type: <br>  * `DRCT` = Direct participant<br>  * `IDRT` = Indirect participant<br> | enum: ["DRCT", "IDRT"]; example: "IDRT" |
| `modality` | string (schema `ParticipantModality`) | yes | Pix modality: <br>  * `PDCT` = Transactional account provider<br>  * `PSTI` = Payment initiation service provider<br> | enum: ["PDCT", "PSTI"]; example: "PDCT" |
| `start_operation_datetime` | string | yes | Datetime when the institution started operating in Pix. RFC 3339 format. | format: "date-time"; example: "2020-11-03T09:30:00+00:00" |
| `date` | string | yes | Participant data reference date. Format = YYYY-MM-DD. For example - `2021-09-30`. | format: "date"; example: "2021-09-30" |

<!-- schema: #/components/schemas/message.Message -->
### Schema `message.Message`

Pointer: `#/components/schemas/message.Message`. Type: object (schema `message.Message`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

<!-- schema: #/components/schemas/message.DetailMessage -->
### Schema `message.DetailMessage`

Pointer: `#/components/schemas/message.DetailMessage`. Type: object (schema `message.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `message.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `message.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `message.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/message.ExternalMessage -->
### Schema `message.ExternalMessage`

Pointer: `#/components/schemas/message.ExternalMessage`. Type: object (schema `message.ExternalMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Error code | example: "PBE315" |
| `message` | string | yes | Error message | example: "Generic error" |

<!-- schema: #/components/schemas/message.ParameterMessage -->
### Schema `message.ParameterMessage`

Pointer: `#/components/schemas/message.ParameterMessage`. Type: object (schema `message.ParameterMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Parameter in error | example: "query parameter" |
| `message` | string | yes | Error message | example: "Generic error" |

<!-- schema: #/components/schemas/message.PayloadMessage -->
### Schema `message.PayloadMessage`

Pointer: `#/components/schemas/message.PayloadMessage`. Type: object (schema `message.PayloadMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Field in error | example: "Entity.field" |
| `message` | string | yes | Error messsage | example: "Generic error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_Pix_management.yaml` | tag `Participants`: GET /v2/pix/dict/participants | https://github.com/PismoDevEx/pismo-api-specs | `7d7fee078ccf5569…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-epda` — Error codes: EPDA
