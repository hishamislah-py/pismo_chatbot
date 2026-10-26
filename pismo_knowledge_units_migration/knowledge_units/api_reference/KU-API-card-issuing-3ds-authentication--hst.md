---
ku_id: KU-API-card-issuing-3ds-authentication--hst
title: 'API reference: Card issuing - 3DS authentication — HST'
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
- postEvaluate
- postChallengeRequest
- postChallengeResult
related_kus: []
specification_version: 1.0.0
---

# API reference: Card issuing - 3DS authentication — HST

**KU ID:** `KU-API-card-issuing-3ds-authentication--hst` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `HST` in `api-specs/Card_issuing_-_3DS_authentication.yaml` (“Card issuing - 3DS authentication”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to provide integration with HST

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /customer_evaluation_provided_url` | `postEvaluate` | Send pre-authentication for evaluation | no |
| `POST /customer_challenge_request_provided_url` | `postChallengeRequest` | Send challenge information | no |
| `POST /v1/challenge-result` | `postChallengeResult` | Get challenge result | no |

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_3DS_authentication.yaml method=POST path=/customer_evaluation_provided_url operationId=postEvaluate -->
### `POST /customer_evaluation_provided_url` — Send pre-authentication for evaluation

- **operationId:** `postEvaluate`
- **Specification:** `api-specs/Card_issuing_-_3DS_authentication.yaml` (Card issuing - 3DS authentication)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/3ds-acs`
- **Tags:** `HST`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Send pre authentication information to customer to evaluate the authentication.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `account_id` | header | yes | integer | Account ID | example: 10045896 |
| `card_id` | header | yes | integer | Card ID | example: 869572 |

#### Request body

Required: yes

> Send information to evaluation

**Content type `application/json`** — schema: object (schema `Evaluate`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `PismoAuthID`) | yes | Pismo-generated unique authentication ID | example: "ff77635e-1cd6-4fda-992d-5ceb71d75644" |
| `external_id` | string (schema `ExternalID`) | yes | Provider-generated unique ID for client monitoring and tracking | example: "ABC123456" |
| `provider` | string (schema `Provider`) | yes | Third-party provider name | enum: ["HST"]; example: "HST" |
| `type` | string (schema `Type`) | yes | Evaluation intention | enum: ["authentication", "challenge-request"]; example: "authentication" |
| `card` | object (schema `Card`) | yes |  |  |
| `account` | object (schema `Account`) | yes |  |  |
| `program` | object (schema `Program`) | yes |  |  |
| `customer` | object (schema `Customer`) | yes |  |  |
| `raw_provider` | object (schema `RawProvider`) | yes | All non-PCI information received from provider. Check provider documentation for details. |  |

Example `Basic example`:

```json
{
  "id": "ff77635e-1cd6-4fda-992d-5ceb71d75644",
  "external_id": "ABC123456",
  "provider": "HST",
  "type": "authentication",
  "card": {
    "id": 869572,
    "mode_id": 102,
    "type": "PLASTIC",
    "hash": "WEPvOQuZvjfYEd0iBmr43bhWyOsylIsW95ebYrLD89App2iEq9IizP+8w73pxKQ4mI47EdhzYHF9RfXjrBOyug==",
    "bin": "0153",
    "last_four_digits": "0153"
  },
  "account": {
    "id": 10045896,
    "document_number": "00011122233",
    "postal_code": "01701000"
  },
  "customer": {
    "id": 12045896
  },
  "program": {
    "id": 986
  },
  "raw_provider": {
    "valueA": "a",
    "valueB": 1,
    "valueC": false,
    "valueD": {
      "valueD1": "x"
    },
    "valueN": "..."
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `EvaluateResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `decision` | string (schema `EvaluatedDecision`) | yes | Client's anti-fraud evaluated decision | enum: ["approve", "reject", "request_challenge"]; example: "approve" |
| `challenge_info` | object (schema `challenge_info`) | no | Customer challenge information including cardholder data |  |
| `subissuer_id` | string (schema `SubIssuerId`) | no | Client's subissuer override, we will use this one to override the issuerSpecificData.subissuerID, if empty, we will use the org_id value. | example: "ANOTHER_BANK" |
| `product_id` | string (schema `ProductId`) | no | Client's product override, we will use this one to override the issuerSpecificData.productID, if empty, we will use the program_id value. | example: "CREDIT" |
| `metadata` | object (schema `Metadata`) | no | Metadata returned from client's anti-fraud validator<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"valueA": "a", "valueB": 1, "valueC": false, "valueD": {"valueD1": "x"}, "valueN": "..."} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_3DS_authentication.yaml method=POST path=/customer_challenge_request_provided_url operationId=postChallengeRequest -->
### `POST /customer_challenge_request_provided_url` — Send challenge information

- **operationId:** `postChallengeRequest`
- **Specification:** `api-specs/Card_issuing_-_3DS_authentication.yaml` (Card issuing - 3DS authentication)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/3ds-acs`
- **Tags:** `HST`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Send pre-authentication information to customer for challenge.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `account_id` | header | yes | integer | Account ID | example: 10045896 |
| `card_id` | header | yes | integer | Card ID | example: 869572 |

#### Request body

Required: yes

> Send information to challenge solicitation

**Content type `application/json`** — schema: object (schema `ChallengeRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `PismoAuthID`) | yes | Pismo-generated unique authentication ID | example: "ff77635e-1cd6-4fda-992d-5ceb71d75644" |
| `external_id` | string (schema `ExternalID`) | yes | Provider-generated unique ID for client monitoring and tracking | example: "ABC123456" |
| `provider` | string (schema `Provider`) | yes | Third-party provider name | enum: ["HST"]; example: "HST" |
| `type` | string (schema `Type`) | yes | Evaluation intention | enum: ["authentication", "challenge-request"]; example: "authentication" |
| `raw_provider` | object (schema `RawProvider`) | yes | All non-PCI information received from provider. Check provider documentation for details. |  |

Example `Basic example`:

```json
{
  "id": "ff77635e-1cd6-4fda-992d-5ceb71d75644",
  "external_id": "ABC123456",
  "provider": "HST",
  "type": "challenge-request",
  "raw_provider": {
    "valueA": "a",
    "valueB": 1,
    "valueC": false,
    "valueD": {
      "valueD1": "x"
    },
    "valueN": "..."
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_3DS_authentication.yaml method=POST path=/v1/challenge-result operationId=postChallengeResult -->
### `POST /v1/challenge-result` — Get challenge result

- **operationId:** `postChallengeResult`
- **Specification:** `api-specs/Card_issuing_-_3DS_authentication.yaml` (Card issuing - 3DS authentication)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/3ds-acs`
- **Tags:** `HST`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Receive challenge result.

#### Request body

Required: yes

> Receive challenge result.

**Content type `application/json`** — schema: object (schema `ChallengeResponse`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `PismoAuthID`) | yes | Pismo-generated unique authentication ID | example: "ff77635e-1cd6-4fda-992d-5ceb71d75644" |
| `decision` | string (schema `Decision`) | yes | Client's anti-fraud decision | enum: ["approve", "reject"]; example: "approve" |
| `answered_at` | string (schema `AnsweredAt`) | yes | End-user action RFC3339 timestamp | example: "2022-12-21T10:08:58Z" |
| `metadata` | object (schema `Metadata`) | yes | Metadata returned from client's anti-fraud validator<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"valueA": "a", "valueB": 1, "valueC": false, "valueD": {"valueD1": "x"}, "valueN": "..."} |

Example `Basic example`:

```json
{
  "id": "ff77635e-1cd6-4fda-992d-5ceb71d75644",
  "decision": "approve",
  "answered_at": "2022-12-21T10:08:58Z",
  "metadata": {
    "valueA": "a",
    "valueB": 1,
    "valueC": false,
    "valueD": {
      "valueD1": "x"
    },
    "valueN": "..."
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ChallengeResultResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authenticated` | boolean (schema `Authenticated`) | no |  | example: false |
| `description` | string (schema `Description`) | no | Challenge result | example: "Challenge expired" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200`, has examples `True`, emits events `0`, deprecated `False`.

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

<!-- schema: #/components/schemas/Account -->
### Schema `Account`

Pointer: `#/components/schemas/Account`. Type: object (schema `Account`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AccountID`) | no | Pismo account ID | example: 10045896 |
| `document_number` | string (schema `DocumentNumber`) | no | Cardholder document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). | example: "00011122233" |
| `postal_code` | string (schema `PostalCode`) | no | Cardholder postal code | example: "01701000" |

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

<!-- schema: #/components/schemas/challenge_info -->
### Schema `challenge_info`

Pointer: `#/components/schemas/challenge_info`. Type: object (schema `challenge_info`).

> Customer challenge information including cardholder data

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cardholder_name` | string | no | Cardholder name | example: "John Doe" |
| `method` | string | no | Method to be used to challenge the cardholder. Possible values:<br>- OTP<br>- OOB<br> | enum: ["OTP", "OOB"]; example: "OTP" |
| `cardholder_phone` | object | no | Cardholder phone number details |  |
| `cardholder_phone.country_code` | string | no | Country code | example: "55" |
| `cardholder_phone.area_code` | string | no | Area code | example: "11" |
| `cardholder_phone.number` | string | no | Phone number without area code | example: "912345678" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_3DS_authentication.yaml` | tag `HST`: POST /customer_evaluation_provided_url, POST /customer_challenge_request_provided_url, POST /v1/challenge-result | https://github.com/PismoDevEx/pismo-api-specs | `5d140d4d204b6363…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
