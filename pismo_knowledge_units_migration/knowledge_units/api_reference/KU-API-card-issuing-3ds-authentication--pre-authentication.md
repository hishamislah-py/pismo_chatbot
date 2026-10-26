---
ku_id: KU-API-card-issuing-3ds-authentication--pre-authentication
title: 'API reference: Card issuing - 3DS authentication — Pre-authentication'
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
- postPreAuthenticate
related_kus:
- KU-CARD-anti-fraud-integration
- KU-CARD-pan-encryption-for-3ds-authentication
specification_version: 1.0.0
---

# API reference: Card issuing - 3DS authentication — Pre-authentication

**KU ID:** `KU-API-card-issuing-3ds-authentication--pre-authentication` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Pre-authentication` in `api-specs/Card_issuing_-_3DS_authentication.yaml` (“Card issuing - 3DS authentication”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoint to provide pre authentication integration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/preauthenticate` | `postPreAuthenticate` | Send pre-authentication info | no |

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_3DS_authentication.yaml method=POST path=/v1/preauthenticate operationId=postPreAuthenticate -->
### `POST /v1/preauthenticate` — Send pre-authentication info

- **operationId:** `postPreAuthenticate`
- **Specification:** `api-specs/Card_issuing_-_3DS_authentication.yaml` (Card issuing - 3DS authentication)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/3ds-acs`
- **Tags:** `Pre-authentication`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Send pre-authentication information to the client's anti-fraud validator to evaluate. Pismo calls the validator's webhook and gets a response before sending a response to the caller.
>
> Pismo provides the encrypt/decrypt keys for the hashed PAN. Talk to your Pismo representative about getting these keys.
>
> For information on PAN encryption, refer to the [PAN encryption for 3DS authentication](doc:pan-encryption-for-3ds-authentication) guide.

#### Request body

Required: yes

> Send information to evaluation

**Content type `application/json`** — schema: object (schema `PreAuthenticationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `ProviderID`) | yes | Client-generated caller ID. | example: "ff77635e-1cd6-4fda-992d-5ceb71d75644" |
| `pan` | string (schema `PANhash`) | yes | Encrypted PAN using 2048 rsa key and base64 encoded.<br>Pismo provides the encrypt/decrypt keys for this field.<br> | example: "WEPvOQuZvjfYEd0iBmr43bhWyOsylIsW95ebYrLD89App2iEq9IizP+8w73pxKQ4mI47EdhzYHF9RfXjrBOyug==" |
| `raw_provider` | object (schema `RawProvider`) | no | All non-PCI information received from provider. Check provider documentation for details. |  |

Example `Basic example`:

```json
{
  "id": "ff77635e-1cd6-4fda-992d-5ceb71d75644",
  "pan": "SdEwfAxa93DJkuBvsfuRfOuqV+Gl3WJIJg4UkL9uK8/2up5UjxsJGNppELuQaad5xb04BE21uy7V0W9fvvGmQmLEpqomG/3J6ppEE0Ufs/CjV2MUacXYwu/Shvl81PPHdEm5gqoOgF4Pter0VVq8YLOEEgiO89htuzuxq8UdOPpFz48ojVLlWb6RYM8XdqPJ0MK/cmlygvpXiYlz/bmsIpinUztvejimyHIi+4Yw2ZjiuG+4Ie+3nndB17vHgNLCtD5krRukD28Y81QDvIzbWAUnqxzESA9gcVHzoWsRPrPksRUH/uce+25qnXnvNbyW0VsHYN2/vLkMhiGkeYBoCg==",
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
| 200 | OK | `application/json`: object (schema `PreAuthenticationResponse`) |
| 400 | Bad request | `application/json`: object (schema `BadRequest`) |
| 422 | Unprocessable entity error | `application/json`: object (schema `UnprocessableEntityError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `CorrelationID`) | no | The Correlation identifier field is used to link related API requests and events. The CID can help the Pismo engineering team track everything related to a call. If not passed, a random one is generated. You can find the CID in the response header.<br> | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |
| `external_id` | string (schema `ExternalID`) | no | Provider-generated unique ID for client monitoring and tracking | example: "ABC123456" |
| `decision` | string (schema `Decision`) | no | Client's anti-fraud decision | enum: ["approve", "reject"]; example: "approve" |
| `account` | object (schema `PreAuthenticationAccount`) | no |  |  |
| `customer` | object (schema `PreAuthenticationCustomer`) | no |  |  |
| `card` | object (schema `PreAuthenticationCard`) | no |  |  |
| `metadata` | object (schema `Metadata`) | no | Metadata returned from client's anti-fraud validator<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"valueA": "a", "valueB": 1, "valueC": false, "valueD": {"valueD1": "x"}, "valueN": "..."} |

##### Response 422

422 Example `E3DS-001`:

```json
{
  "code": "E3DS-001",
  "message": "No account were found with the specified parameters"
}
```

422 Example `E3DS-002`:

```json
{
  "code": "E3DS-002",
  "message": "No account were found with address"
}
```

422 Example `E3DS-003`:

```json
{
  "code": "E3DS-003",
  "message": "No account were found with active phone"
}
```

422 Example `E3DS-004`:

```json
{
  "code": "E3DS-004",
  "message": "The account is not in a valid state"
}
```

422 Example `E3DS-005`:

```json
{
  "code": "E3DS-005",
  "message": "No card were found with the specified parameters"
}
```

422 Example `E3DS-006`:

```json
{
  "code": "E3DS-006",
  "message": "No card were found with this PAN"
}
```

422 Example `E3DS-007`:

```json
{
  "code": "E3DS-007",
  "message": "The card is not in a valid state"
}
```

422 Example `E3DS-008`:

```json
{
  "code": "E3DS-008",
  "message": "No customer were found with the specified parameters"
}
```

422 Example `E3DS-009`:

```json
{
  "code": "E3DS-009",
  "message": "There is no configuration to process this request"
}
```

422 Example `E3DS-010`:

```json
{
  "code": "E3DS-010",
  "message": "Entity not found"
}
```

422 Example `E3DS-011`:

```json
{
  "code": "E3DS-011",
  "message": "There was a failure communicating with an external service"
}
```

422 Example `E3DS-012`:

```json
{
  "code": "E3DS-012",
  "message": "Error while fetching customer phone"
}
```

422 Example `E3DS-013`:

```json
{
  "code": "E3DS-013",
  "message": "No active phones found to this customer"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;422;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-anti-fraud-integration`, `KU-CARD-pan-encryption-for-3ds-authentication`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/PreAuthenticationAccount -->
### Schema `PreAuthenticationAccount`

Pointer: `#/components/schemas/PreAuthenticationAccount`. Type: object (schema `PreAuthenticationAccount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AccountID`) | no | Pismo account ID | example: 10045896 |
| `status` | string (schema `AccountStatus`) | no | Account status | enum: ["NORMAL", "BLOCKED", "CANCELLED"]; example: "NORMAL" |
| `name` | string (schema `Name`) | no | name | example: "Paul Bearer" |
| `phone` | string (schema `Phone`) | no | Phone number | example: "+5531998675309" |
| `email` | string (schema `Email`) | no | E-mail | example: "ho_lee_smokes@gmail.com" |

<!-- schema: #/components/schemas/PreAuthenticationCustomer -->
### Schema `PreAuthenticationCustomer`

Pointer: `#/components/schemas/PreAuthenticationCustomer`. Type: object (schema `PreAuthenticationCustomer`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number (schema `CustomerID`) | no | Customer ID | example: 867604 |
| `name` | string (schema `Name`) | no | name | example: "Paul Bearer" |
| `phone` | string (schema `Phone`) | no | Phone number | example: "+5531998675309" |
| `email` | string (schema `Email`) | no | E-mail | example: "ho_lee_smokes@gmail.com" |

<!-- schema: #/components/schemas/PreAuthenticationCard -->
### Schema `PreAuthenticationCard`

Pointer: `#/components/schemas/PreAuthenticationCard`. Type: object (schema `PreAuthenticationCard`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CardID`) | no | Card ID | example: 869572 |
| `status` | string (schema `CardStatus`) | no | Card status | enum: ["NORMAL", "BLOCKED", "PENDING", "LOST", "ROBBED", "EXPIRED", "DAMAGED", "FRAUD", "WARNING", "CANCELED", "CREATED", "DELETED"]; example: "BLOCKED" |
| `type` | string (schema `CardType`) | no | Card type | enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: "PLASTIC" |
| `hash` | string (schema `PANhash`) | no | Encrypted PAN using 2048 rsa key and base64 encoded.<br>Pismo provides the encrypt/decrypt keys for this field.<br> | example: "WEPvOQuZvjfYEd0iBmr43bhWyOsylIsW95ebYrLD89App2iEq9IizP+8w73pxKQ4mI47EdhzYHF9RfXjrBOyug==" |
| `printed_name` | string (schema `PrintedName`) | no | Printed card name | minLength: 2; maxLength: 26; example: "Nan Tucket" |

<!-- schema: #/components/schemas/BadRequest -->
### Schema `BadRequest`

Pointer: `#/components/schemas/BadRequest`. Type: object (schema `BadRequest`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "INVALID-REQUEST-PAYLOAD" |
| `message` | string | no |  | example: "The request payload is invalid" |

<!-- schema: #/components/schemas/UnprocessableEntityError -->
### Schema `UnprocessableEntityError`

Pointer: `#/components/schemas/UnprocessableEntityError`. Type: object (schema `UnprocessableEntityError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Error code |  |
| `message` | string | yes | Error message |  |

<!-- schema: #/components/schemas/InternalServerError -->
### Schema `InternalServerError`

Pointer: `#/components/schemas/InternalServerError`. Type: object (schema `InternalServerError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "INVALID-STRUCT-SIGNATURE" |
| `message` | string | no |  | example: "An error occurred while interpreting a structure" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_3DS_authentication.yaml` | tag `Pre-authentication`: POST /v1/preauthenticate | https://github.com/PismoDevEx/pismo-api-specs | `5d140d4d204b6363…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-anti-fraud-integration` — Anti-fraud integration
- `KU-CARD-pan-encryption-for-3ds-authentication` — PAN encryption for 3DS authentication
