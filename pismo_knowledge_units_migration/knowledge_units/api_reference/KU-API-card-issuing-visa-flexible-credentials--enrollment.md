---
ku_id: KU-API-card-issuing-visa-flexible-credentials--enrollment
title: 'API reference: Card issuing - Visa Flexible Credentials [beta] — Enrollment'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml
  sha256: 5144b0a0d49f5c691528cec17b73bc1e31f1668295b15b42813142ee32364980
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
- get-card-enrollment
- enroll-card-enrollment
- delete-card-enrollment
- update-card-enrollment
related_kus:
- KU-CARD-visa-flexible-credentials
- KU-ERR-codes-acq-to-esma
specification_version: 1.0.0
---

# API reference: Card issuing - Visa Flexible Credentials [beta] — Enrollment

**KU ID:** `KU-API-card-issuing-visa-flexible-credentials--enrollment` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Enrollment` in `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` (“Card issuing - Visa Flexible Credentials [beta]”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Card enrollment and management endpoints.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /flex_credentials/v1/vfc/enrollment/cards/{cardId}` | `get-card-enrollment` | Get card enrollment | no |
| `POST /flex_credentials/v1/vfc/enrollment/cards/{cardId}` | `enroll-card-enrollment` | Enroll card in VFC | no |
| `DELETE /flex_credentials/v1/vfc/enrollment/cards/{cardId}` | `delete-card-enrollment` | Delete card enrollment | no |
| `PUT /flex_credentials/v1/vfc/enrollment/cards` | `update-card-enrollment` | Update card enrollment | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a "**401 Unauthorized**" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml method=GET path=/flex_credentials/v1/vfc/enrollment/cards/{cardId} operationId=get-card-enrollment -->
### `GET /flex_credentials/v1/vfc/enrollment/cards/{cardId}` — Get card enrollment

- **operationId:** `get-card-enrollment`
- **Specification:** `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` (Card issuing - Visa Flexible Credentials [beta])
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Enrollment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get VFC card enrolled/registered credentials.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `access_token` | header | yes | string | Access token. Tokens can expire quickly, which can result in a **401 Unauthorized** error. |  |
| `cardId` | path | yes | string | Card ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Success | `application/json`: object (schema `EnrollmentResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | integer (schema `CardID`) | yes | Enrolled card ID | format: "int64"; example: 6743052 |
| `document_id` | string (schema `DocumentId`) | yes | Enrollment document ID. UUID from Visa that identifies card in VFC. | example: "v-301-923113d1-c87e-460f-a504-9eb7999163ff" |

201 Example `example`:

```json
{
  "card_id": 186283623,
  "document_id": "v-301-923113d1-c87e-460f-a504-9eb7999163ff"
}
```

##### Response 400

400 Example `example`:

```json
{
  "error_code": "ERR9993",
  "message": "card not found"
}
```

##### Response 401

401 Example `example`:

```json
{
  "error_code": "ERR9786",
  "message": "Access token is missing or invalid"
}
```

##### Response 500

500 Example `example`:

```json
{
  "error_code": "ERR5446",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERR9993` | card not found |
| 401 | `ERR9786` | Access token is missing or invalid |
| 500 | `ERR5446` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml method=POST path=/flex_credentials/v1/vfc/enrollment/cards/{cardId} operationId=enroll-card-enrollment -->
### `POST /flex_credentials/v1/vfc/enrollment/cards/{cardId}` — Enroll card in VFC

- **operationId:** `enroll-card-enrollment`
- **Specification:** `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` (Card issuing - Visa Flexible Credentials [beta])
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Enrollment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Enrolls/registers a card in Visa Flexible Credentials (VFC).
>
> VFC enables a single card to access multiple funding sources, such as debit, credit, prepaid, and installment plans.
>
> For more information, refer to [Visa Flexible Credentials](doc:visa-flexible-credentials).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `access_token` | header | yes | string | Access token. Tokens can expire quickly, which can result in a **401 Unauthorized** error. |  |
| `cardId` | path | yes | string | Card ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Success | `application/json`: object (schema `EnrollmentResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | integer (schema `CardID`) | yes | Enrolled card ID | format: "int64"; example: 6743052 |
| `document_id` | string (schema `DocumentId`) | yes | Enrollment document ID. UUID from Visa that identifies card in VFC. | example: "v-301-923113d1-c87e-460f-a504-9eb7999163ff" |

201 Example `example`:

```json
{
  "card_id": 186283623,
  "document_id": "v-301-923113d1-c87e-460f-a504-9eb7999163ff"
}
```

##### Response 400

400 Example `example`:

```json
{
  "error_code": "ERR9993",
  "message": "card not found"
}
```

##### Response 401

401 Example `example`:

```json
{
  "error_code": "ERR9786",
  "message": "Access token is missing or invalid"
}
```

##### Response 500

500 Example `example`:

```json
{
  "error_code": "ERR5446",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERR9993` | card not found |
| 401 | `ERR9786` | Access token is missing or invalid |
| 500 | `ERR5446` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-visa-flexible-credentials`.

<!-- op: spec=api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml method=DELETE path=/flex_credentials/v1/vfc/enrollment/cards/{cardId} operationId=delete-card-enrollment -->
### `DELETE /flex_credentials/v1/vfc/enrollment/cards/{cardId}` — Delete card enrollment

- **operationId:** `delete-card-enrollment`
- **Specification:** `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` (Card issuing - Visa Flexible Credentials [beta])
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Enrollment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete card enrolled/registered credentials in VFC accounts.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `access_token` | header | yes | string | Access token. Tokens can expire quickly, which can result in a **401 Unauthorized** error. |  |
| `cardId` | path | yes | string | Card ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Success |  |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 400

400 Example `example`:

```json
{
  "error_code": "ERR9993",
  "message": "card not found"
}
```

##### Response 401

401 Example `example`:

```json
{
  "error_code": "ERR9786",
  "message": "Access token is missing or invalid"
}
```

##### Response 500

500 Example `example`:

```json
{
  "error_code": "ERR5446",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERR9993` | card not found |
| 401 | `ERR9786` | Access token is missing or invalid |
| 500 | `ERR5446` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml method=PUT path=/flex_credentials/v1/vfc/enrollment/cards operationId=update-card-enrollment -->
### `PUT /flex_credentials/v1/vfc/enrollment/cards` — Update card enrollment

- **operationId:** `update-card-enrollment`
- **Specification:** `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` (Card issuing - Visa Flexible Credentials [beta])
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Enrollment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update card existing enrolled/registered credentials in VFC accounts.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `UpdateEnrollmentRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `newCardId` | integer (schema `NewCardID`) | yes | The new card ID to update enrollment for | format: "int64"; example: 186283624 |
| `existingCardId` | integer (schema `ExistingCardId`) | yes | Existing card ID with enrollment | format: "int64"; example: 186248443 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `EnrollmentResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | integer (schema `CardID`) | yes | Enrolled card ID | format: "int64"; example: 6743052 |
| `document_id` | string (schema `DocumentId`) | yes | Enrollment document ID. UUID from Visa that identifies card in VFC. | example: "v-301-923113d1-c87e-460f-a504-9eb7999163ff" |

200 Example `example`:

```json
{
  "card_id": 186283624,
  "document_id": "v-301-923113d1-c87e-460f-a504-9eb7999163f1"
}
```

##### Response 400

400 Example `example`:

```json
{
  "error_code": "ERR9993",
  "message": "card not found"
}
```

##### Response 401

401 Example `example`:

```json
{
  "error_code": "ERR9786",
  "message": "Access token is missing or invalid"
}
```

##### Response 500

500 Example `example`:

```json
{
  "error_code": "ERR5446",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERR9993` | card not found |
| 401 | `ERR9786` | Access token is missing or invalid |
| 500 | `ERR5446` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorObject -->
### Schema `ErrorObject`

Pointer: `#/components/schemas/ErrorObject`. Type: object (schema `ErrorObject`).

> Standard error object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code |  |
| `message` | string | no | Error message |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` | tag `Enrollment`: GET /flex_credentials/v1/vfc/enrollment/cards/{cardId}, POST /flex_credentials/v1/vfc/enrollment/cards/{cardId}, DELETE /flex_credentials/v1/vfc/enrollment/cards/{cardId}, PUT /flex_credentials/v1/vfc/enrollment/cards | https://github.com/PismoDevEx/pismo-api-specs | `5144b0a0d49f5c69…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-visa-flexible-credentials` — Visa Flexible Credentials [beta]
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
