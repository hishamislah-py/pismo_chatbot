---
ku_id: KU-API-card-issuing-3ds-authentication--vcas
title: 'API reference: Card issuing - 3DS authentication — VCAS'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_3DS_authentication.yaml
  sha256: 5d140d4d204b63636bd0bfe3340d388f92b83e6dde484693c1e52a0d33ee9437
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
- postStepUp
- postInitiateAction
- postValidation
related_kus: []
specification_version: 1.0.0
---

# API reference: Card issuing - 3DS authentication — VCAS

**KU ID:** `KU-API-card-issuing-3ds-authentication--vcas` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `VCAS` in `api-specs/Card_issuing_-_3DS_authentication.yaml` (“Card issuing - 3DS authentication”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to provide integration with VCAS

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /issuer-vcas-stepup-endpoint` | `postStepUp` | Issuer’s endpoint to handle VCAS stepup flow | no |
| `POST /issuer-vcas-initiateaction-endpoint` | `postInitiateAction` | Issuer’s endpoint to handle VCAs initiate action flow | no |
| `POST /issuer-vcas-validate-endpoint` | `postValidation` | Issuer’s endpoint to handle VCAs validate flow | no |

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_3DS_authentication.yaml method=POST path=/issuer-vcas-stepup-endpoint operationId=postStepUp -->
### `POST /issuer-vcas-stepup-endpoint` — Issuer’s endpoint to handle VCAS stepup flow

- **operationId:** `postStepUp`
- **Specification:** `api-specs/Card_issuing_-_3DS_authentication.yaml` (Card issuing - 3DS authentication)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/3ds-acs`
- **Tags:** `VCAS`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Informs VCAS which authentication types are available for a specific user.

#### Request body

Required: yes

> Request provided by Pismo containing transaction and information

**Content type `application/json`** — schema: object (schema `VCASStepUpRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `PismoAuthID`) | yes | Pismo-generated unique authentication ID | example: "ff77635e-1cd6-4fda-992d-5ceb71d75644" |
| `provider` | string | yes | Third-party provider name | enum: ["VCAS"]; example: "VCAS" |
| `type` | string | yes | Operation performed | enum: ["STEPUP"]; example: "STEPUP" |
| `card` | object (schema `Card`) | yes |  |  |
| `account` | object (schema `AccountV2`) | yes |  |  |
| `program` | object (schema `Program`) | yes |  |  |
| `customer` | object (schema `Customer`) | yes |  |  |
| `raw_provider` | object (schema `RawProvider`) | yes | All non-PCI information received from provider. Check provider documentation for details. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `VCASStepUpResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `raw_response` | object | no | Raw response to VCAS StepUp request, according with VCAS documentation. | example: {"ProcessorId": "5723ae630063ac1a9c3ab07976", "IssuerId": "5723ae630063ac1a9c3ab080", "TransactionId": "00ec043e-40b5-4ce4-95c2-9e83b644f412", "StepupRequestId": "00ec043e-40b5-4ce4-95c2-9e83b644f412", "StepupType": "OTPEMAIL", "Language": "en-US", "Status": "SUCCESS", "RiskIndicator": "string", "Credentials": [{"Id": "d94fd3fd-bef1-49cb-88ab-a6841261cea9", "Type": "OTPEMAIL", "Text": "jales@pismo.io"}], "Reason": {"ReasonCode": "string", "ReasonDescription": "string"}, "Error": {"ReferenceNumber": "string", "ReasonDescription": "string", "Description": "string", "Message": "string"}, "WhyInfo": {"Label": "string", "Text": "string"}} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_3DS_authentication.yaml method=POST path=/issuer-vcas-initiateaction-endpoint operationId=postInitiateAction -->
### `POST /issuer-vcas-initiateaction-endpoint` — Issuer’s endpoint to handle VCAs initiate action flow

- **operationId:** `postInitiateAction`
- **Specification:** `api-specs/Card_issuing_-_3DS_authentication.yaml` (Card issuing - 3DS authentication)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/3ds-acs`
- **Tags:** `VCAS`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Informs the issuer about the initiate action flow in the VCAS process.

#### Request body

Required: yes

> Request provided by Pismo containing transaction and information

**Content type `application/json`** — schema: object (schema `VCASInitiateActionRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `PismoAuthID`) | yes | Pismo-generated unique authentication ID | example: "ff77635e-1cd6-4fda-992d-5ceb71d75644" |
| `provider` | string | yes | Third-party provider name | enum: ["VCAS"]; example: "VCAS" |
| `type` | string | yes | The type of operation to be performed. | enum: ["INITIATE_ACTION_CALL"]; example: "INITIATE_ACTION_CALL" |
| `card` | object (schema `Card`) | yes |  |  |
| `account` | object (schema `AccountV2`) | yes |  |  |
| `program` | object (schema `Program`) | yes |  |  |
| `customer` | object (schema `Customer`) | yes |  |  |
| `raw_provider` | object (schema `RawProvider`) | yes | All non-PCI information received from provider. Check provider documentation for details. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `VCASInitiateActionResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `raw_response` | object | no | Raw response to VCAS InitiateAction request, according with VCAS documentation. | example: {"ProcessorId": "7723ae630063ac1a9c3ab07976", "IssuerId": "5723ae630063ac1a9c3ab080", "TransactionId": "00ec043e-40b5-4ce4-95c2-9e83b644f412", "StepupRequestId": "00ec043e-40b5-4ce4-95c2-9e83b644f412", "StepupType": "OTP", "Language": "string", "Status": "SUCCESS", "TransStatusReason": "string", "RiskIndicator": "string", "Credentials": [{"Id": "d94fd3fd-bef1-49cb-88ab-a6841261cea9", "Type": "OTPEMAIL", "Text": "******@cardinalcommerce.com"}], "Reason": {"ReasonCode": "string", "ReasonDescription": "string"}, "Error": {"ReferenceNumber": "string", "ReasonDescription": "string", "Description": "string", "Message": "string"}} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_3DS_authentication.yaml method=POST path=/issuer-vcas-validate-endpoint operationId=postValidation -->
### `POST /issuer-vcas-validate-endpoint` — Issuer’s endpoint to handle VCAs validate flow

- **operationId:** `postValidation`
- **Specification:** `api-specs/Card_issuing_-_3DS_authentication.yaml` (Card issuing - 3DS authentication)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/3ds-acs`
- **Tags:** `VCAS`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Informs the issuer about the validation flow.

#### Request body

Required: yes

> Request provided by Pismo containing transaction and information

**Content type `application/json`** — schema: object (schema `VCASValidateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `PismoAuthID`) | yes | Pismo-generated unique authentication ID | example: "ff77635e-1cd6-4fda-992d-5ceb71d75644" |
| `provider` | string | yes | Third-party provider name | enum: ["VCAS"]; example: "VCAS" |
| `type` | string | yes | To validate the credential (e.g., OTP) provided by the cardholder during a step-up authentication flow. | enum: ["VALIDATE"]; example: "VALIDATE" |
| `raw_provider` | object (schema `RawProvider`) | yes | All non-PCI information received from provider. Check provider documentation for details. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `VCASValidateResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `raw_response` | object | no | Raw response to VCAS Validate request, according with VCAS documentation. | example: {"ProcessorId": "5723ae630063ac1a9c3ab079", "IssuerId": "5723ae630063ac1a9c3ab671", "TransactionId": "00ec043e-40b5-4ce4-95c2-9e83b644f412", "StepupRequestId": "00ec043e-40b5-4ce4-95c2-9e83b644f618", "Language": "string", "CredentialId": "string", "Status": "SUCCESS", "TransStatusReason": "string", "RiskIndicator": "string", "Reason": {"ReasonCode": "string", "ReasonDescription": "string"}, "Error": {"ReferenceNumber": "string", "ReasonDescription": "string", "Description": "string", "Message": "string"}, "RReqOverrides": {"AuthenticationMethod": "SMS_OTP", "TransStatusReason": "CARD_AUTH_FAILED", "AuthenticationAttempts": "string", "CustomerCancel": true}} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Card -->
### Schema `Card`

Pointer: `#/components/schemas/Card`. Type: object (schema `Card`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CardID`) | no | Card ID | example: 869572 |
| `mode_id` | integer (schema `CardModeID`) | no | Card mode ID | example: 102 |
| `type` | string (schema `CardType`) | no | Card type | enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: "PLASTIC" |
| `hash` | string (schema `PANhash`) | no | Encrypted PAN using 2048 rsa key and base64 encoded.<br>Pismo provides the encrypt/decrypt keys for this field.<br> | example: "WEPvOQuZvjfYEd0iBmr43bhWyOsylIsW95ebYrLD89App2iEq9IizP+8w73pxKQ4mI47EdhzYHF9RfXjrBOyug==" |
| `bin` | string (schema `CardBIN`) | no | Card BIN (Bank Identification Number) | example: "885692" |
| `last_four_digits` | string (schema `CardLast4Digits`) | no | Card last four PAN digits | example: "0153" |

<!-- schema: #/components/schemas/AccountV2 -->
### Schema `AccountV2`

Pointer: `#/components/schemas/AccountV2`. Type: object (schema `AccountV2`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AccountID`) | no | Pismo account ID | example: 10045896 |
| `document_number` | string (schema `DocumentNumber`) | no | Cardholder document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). | example: "00011122233" |
| `phones` | array of object (schema `StructuredPhone`) | no |  |  |
| `email` | string (schema `Email`) | no | E-mail | example: "ho_lee_smokes@gmail.com" |

<!-- schema: #/components/schemas/Program -->
### Schema `Program`

Pointer: `#/components/schemas/Program`. Type: object (schema `Program`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Program ID | example: 986 |

<!-- schema: #/components/schemas/Customer -->
### Schema `Customer`

Pointer: `#/components/schemas/Customer`. Type: object (schema `Customer`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number (schema `CustomerID`) | no | Customer ID | example: 867604 |

<!-- schema: #/components/schemas/StructuredPhone -->
### Schema `StructuredPhone`

Pointer: `#/components/schemas/StructuredPhone`. Type: object (schema `StructuredPhone`).

> Phone number structure

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `area_code` | string | no | Area code of the phone number | example: "31" |
| `country_code` | string | no | Country code of the phone number | example: "55" |
| `number` | string | no | Phone number without area code | example: "998675309" |
| `type` | string | no | Type of phone number (e.g., mobile, commercial, residential) | example: "mobile" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_3DS_authentication.yaml` | tag `VCAS`: POST /issuer-vcas-stepup-endpoint, POST /issuer-vcas-initiateaction-endpoint, POST /issuer-vcas-validate-endpoint | https://github.com/PismoDevEx/pismo-api-specs | `5d140d4d204b6363…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
