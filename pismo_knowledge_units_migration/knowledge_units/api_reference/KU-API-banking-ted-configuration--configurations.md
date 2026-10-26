---
ku_id: KU-API-banking-ted-configuration--configurations
title: 'API reference: Banking - TED configuration — Configurations'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_TED_configuration.yaml
  sha256: 734521e4deb1a0e6a2f38309107afff86e30add02aa013275c410369aa95573c
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
- post-save-provider-configuration
related_kus:
- KU-BANK-banking-overview
- KU-BANK-get-started-core-banking
- KU-ERR-codes-acq-to-esma
specification_version: '1.0'
---

# API reference: Banking - TED configuration — Configurations

**KU ID:** `KU-API-banking-ted-configuration--configurations` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Configurations` in `api-specs/Banking_-_TED_configuration.yaml` (“Banking - TED configuration”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage provider configurations for SPB (Brazil payment system) integration and TED transfers

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/provider-configuration` | `post-save-provider-configuration` | Register for TED transfers | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token.

## Operation contracts

<!-- op: spec=api-specs/Banking_-_TED_configuration.yaml method=POST path=/v1/provider-configuration operationId=post-save-provider-configuration -->
### `POST /v1/provider-configuration` — Register for TED transfers

- **operationId:** `post-save-provider-configuration`
- **Specification:** `api-specs/Banking_-_TED_configuration.yaml` (Banking - TED configuration)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacen-spb`
- **Tags:** `Configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a client's configuration at a provider who is authorized to use the Brazil Central Bank's (BCB) payment system (SPB) for TED transfers. 
>
> TED stands for Transferência Eletrônica Disponível (Electronic transfer available) and is a Brazilian electronic funds transfer system that allows businesses and individuals to transfer funds between different banks. Pismo uses this configuration to authorize TED transfers on clients' behalf.

#### Request body

Required: yes

> Save configuration request body

**Content type `application/json`** — schema: object (schema `spb.CreateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `branch` | string (schema `Branch`) | yes | Client organization's branch ID | example: "1234" |
| `code` | string (schema `Code`) | yes | Code that identifies Pismo to the provider. | example: "Legacy" |
| `document_number` | string (schema `DocumentNumber`) | yes | Client organization's government document number such as a Tax ID. | example: "Client CNPJ (Brazilian business tax ID)" |
| `password` | string (schema `Password`) | yes | Password | example: "123456" |
| `provider` | string (schema `Provider`) | yes | Payment provider. Right now, only JD Consultores. | enum: ["JD"]; example: "JD" |
| `url` | string (schema `Url`) | yes | URL that identifies the client at the provider. | example: "https://jdspb12345678homl" |
| `user` | string (schema `User`) | yes | Username | example: "userSpb" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Response Body | `application/json`: object (schema `spb.Response`) |
| 400 | Bad Request | `application/json`: object (schema `Domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `Domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `Domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `Domain.Error`) |

##### Response 201

- Response header `x-cid`:  (string (schema `Xcid`))
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | message | example: "Configuration saved" |

##### Response 400

- Response header `x-cid`:  (string (schema `Xcid`))
400 Example `EBS0002` (Validation error):

```json
{
  "code": "EBS0009",
  "message": "(Field 'code' is required)"
}
```

##### Response 403

- Response header `x-cid`:  (string (schema `Xcid`))
##### Response 404

- Response header `x-cid`:  (string (schema `Xcid`))
##### Response 500

- Response header `x-cid`:  (string (schema `Xcid`))
500 Example `EBS0002` (Error on save BCB SPB configuration):

```json
{
  "code": "EBS0065",
  "message": "Error on save configuration"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBS0009` | (Field 'code' is required) |
| 500 | `EBS0065` | Error on save configuration |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-banking-overview`, `KU-BANK-get-started-core-banking`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Domain.Error -->
### Schema `Domain.Error`

Pointer: `#/components/schemas/Domain.Error`. Type: object (schema `Domain.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code | example: "EBS0001" |
| `details` | string | no | Error details | example: "Error detail" |
| `message` | string | no | Error message | example: "Error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_TED_configuration.yaml` | tag `Configurations`: POST /v1/provider-configuration | https://github.com/PismoDevEx/pismo-api-specs | `734521e4deb1a0e6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-banking-overview` — Banking overview
- `KU-BANK-get-started-core-banking` — Get started with core banking
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
