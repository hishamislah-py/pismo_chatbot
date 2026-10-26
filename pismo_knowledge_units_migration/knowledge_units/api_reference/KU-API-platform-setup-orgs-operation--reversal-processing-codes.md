---
ku_id: KU-API-platform-setup-orgs-operation--reversal-processing-codes
title: 'API reference: Platform setup - Orgs operation — Reversal processing codes'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Platform_setup_-_Orgs_Operation.yaml
  sha256: 28c0217338b191bd66f500ec18d4aa50e4d49a2b4e6d3045bc7643f0cda69418
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
- ReversalProcessingCode
related_kus:
- KU-EVT-catalogue-other-domains
specification_version: v1.0
---

# API reference: Platform setup - Orgs operation — Reversal processing codes

**KU ID:** `KU-API-platform-setup-orgs-operation--reversal-processing-codes` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Reversal processing codes` in `api-specs/Platform_setup_-_Orgs_Operation.yaml` (“Platform setup - Orgs operation”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage reversal processing codes

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /orgs-operation/v1/reversal-processing-codes` | `ReversalProcessingCode` | Create reversal processing code | no |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must be previously authenticated with an account token

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Orgs_Operation.yaml method=POST path=/orgs-operation/v1/reversal-processing-codes operationId=ReversalProcessingCode -->
### `POST /orgs-operation/v1/reversal-processing-codes` — Create reversal processing code

- **operationId:** `ReversalProcessingCode`
- **Specification:** `api-specs/Platform_setup_-_Orgs_Operation.yaml` (Platform setup - Orgs operation)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Reversal processing codes`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Create a reversal processing code for an existing processing code.
>
> This endpoint creates a `REVERSAL` type processing code and a [Orgs operation created](https://developers.pismo.io/events/docs/orgs-operation-create-1) event.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ReversalProcessingCodeCreateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string | yes | Processing code ID |  |
| `balance_impact` | integer (schema `BalanceImpact`) | no | Balance impact associated with processing code:<br>  * `1` - Credit <br>  * `0` - No impact. Zero balance operations have no impact. Zero balance customers are responsible for settling accounts and generating transactions.<br>  * `-1` - Debit<br> | enum: [1, 0, -1]; example: 1 |
| `description` | string (schema `PcDescription`) | yes | Processing code description | maxLength: 50 |
| `translations` | array of object (schema `Translations`) | no | Processing code descriptions translation in different languages |  |
| `translations[].language` | string (schema `TranslatedLanguage`) | no | Translation language. <br><br>For example, the code for English (United States) is `en-US`. The prefix, `en`, is a language code following the ISO 639-1 standard. The suffix, `US`, is a country code following the ISO 3166-1 Alpha-2 standard.<br> | example: "en-US" |
| `translations[].description` | string | no | Translated description | maxLength: 50 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ReversalOrgsOperationCreateResponse`) |
| 400 | Bad request error. | `application/json`: object (schema `HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string (schema `ProcessingCode`) | no | A processing code identifies a financial operation on the Pismo platform. Processing codes need to be mapped to transaction type codes to create a transaction flow. <br><br>A custom processing code is created with a `PENDING` status . Initially, its use is not allowed in authorizations. Once the transaction flow for a custom processing code is completely configured, its status changes to `SUCCESS` and it is ready for use. <br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types)<br> |  |
| `status` | string (schema `Status`) | no | Processing code status:<br>  * `PENDING` - Missing required configurations. A custom processing code is initially created with a `PENDING` status and its use is not allowed in authorizations. Once the transaction flow for a custom processing code is completely configured, its status changes to `SUCCESS` and it is ready for use. All standard processing codes have a `SUCCESS` status.<br><br>  * `SUCCESS` - Required configurations done<br> | enum: ["SUCCESS", "PENDING"]; example: "SUCCESS" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `orgs-operation-create-1` | https://developers.pismo.io/events/docs/orgs-operation-create-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400`, has examples `False`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/HTTPError -->
### Schema `HTTPError`

Pointer: `#/components/schemas/HTTPError`. Type: object (schema `HTTPError`).

> Code and error message.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | HTTP error code |  |
| `message` | string | no | HTTP error message |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Orgs_Operation.yaml` | tag `Reversal processing codes`: POST /orgs-operation/v1/reversal-processing-codes | https://github.com/PismoDevEx/pismo-api-specs | `28c0217338b191bd…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
