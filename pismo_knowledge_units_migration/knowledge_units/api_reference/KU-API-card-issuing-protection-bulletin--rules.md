---
ku_id: KU-API-card-issuing-protection-bulletin--rules
title: 'API reference: Card issuing - Protection Bulletin — Rules'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Protection_Bulletin.yaml
  sha256: 6c5641a54569d51d4df8b976968622e18c8c6710cb93bf06b7088ccdadcc7a8f
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
- post-v1-bulletin-setup
- get-v1-bulletin-rule
related_kus:
- KU-CARD-protection-bulletin
- KU-ERR-codes-acq-to-esma
- KU-EVT-catalogue-other-domains
specification_version: 2.0.3
---

# API reference: Card issuing - Protection Bulletin — Rules

**KU ID:** `KU-API-card-issuing-protection-bulletin--rules` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Rules` in `api-specs/Card_issuing_-_Protection_Bulletin.yaml` (“Card issuing - Protection Bulletin”, version `2.0.3`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage Protection Bulletin rules

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/bulletin/setup` | `post-v1-bulletin-setup` | Create Protection Bulletin rule | no |
| `GET /v1/bulletin/setup/{program_id}` | `get-v1-bulletin-rule` | Get Protection Bulletin rule | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error.<br>

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Protection_Bulletin.yaml method=POST path=/v1/bulletin/setup operationId=post-v1-bulletin-setup -->
### `POST /v1/bulletin/setup` — Create Protection Bulletin rule

- **operationId:** `post-v1-bulletin-setup`
- **Specification:** `api-specs/Card_issuing_-_Protection_Bulletin.yaml` (Card issuing - Protection Bulletin)
- **Server base URL(s):** `https://sandbox.pismolabs.io/protection-bulletin`
- **Tags:** `Rules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a new Protection Bulletin setup rule. This feature is available for Elo, Mastercard and Visa.
>
> When you set a card rule, for example, when a card status is changed to `LOST`, it is automatically added to the Protection Bulletin.
>
> This operation executes asynchronously. When complete, a [Bulletin rule event](https://developers.pismo.io/events/docs/bulletin-bulletin-rule-1) is generated.
>
> **Notes:** 
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.
>   * Deactivating a rule after it has been created requires re-calling this endpoint  with `active` set to `false`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |

#### Request body

Required: no

**Content type `application/json`** — schema: anyOf: object (schema `Bulletin_Setup_Elo_Model`), object (schema `Bulletin_Setup_Mastercard_Model`), object (schema `Bulletin_Setup_Visa_Model`)

_anyOf option 1: schema `Bulletin_Setup_Elo_Model`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `active` | boolean (schema `Active`) | yes | Is rule active? An inactive rule is not applied to transactions.<br> | example: true |
| `program_id` | number (schema `ProgramID`) | yes | Pismo program ID. | example: 1010 |
| `allowed_status` | array of object (schema `AllowedStatusEloModel`) | no | If `allowed_status` is passed, the Pismo Protection Bulletin service starts monitoring [Card updated events](https://developers.pismo.io/events/docs/cards-update-1). <br><br>The `status_pismo` status determines if the card is sent to the network via the Protection Bulletin.<br> |  |
| `allowed_status[].status_pismo` | string (schema `StatusPismo`) | no | Pismo card status. For more information, see [Card lifecycle and statuses](https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses).<br> | example: "LOST" |
| `allowed_status[].default_purge_days` | number (schema `DefaultPurgeDays`) | no | After the specified number of days, a request to remove the card will be automatically sent to the network through the Protection Bulletin.<br><br>The `default_purge_days` field is optional, and if not provided, no action will be taken to remove this card from the Protection Bulletin.<br> | example: 30 |

_anyOf option 2: schema `Bulletin_Setup_Mastercard_Model`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `active` | boolean (schema `Active`) | yes | Is rule active? An inactive rule is not applied to transactions.<br> | example: true |
| `ica` | string (schema `Ica`) | yes | Interbank Card Association (ICA) number - a six-digit account number that identifies a financial institution or third-party processor operating in the Mastercard network. **REQUIRED** for Mastercard.<br><br>It must be padded with leading zeros.<br> | example: "012345" |
| `program_id` | number (schema `ProgramID`) | yes | Pismo program ID. | example: 1010 |
| `allowed_status` | array of object (schema `AllowedStatusMastercardModel`) | no | If `allowed_status` is provided, the Pismo Protection Bulletin service starts monitoring [Card updated events](https://developers.pismo.io/events/docs/cards-update-1). <br><br>The `status_pismo` status determines if the card is sent to the network via the Protection Bulletin.<br> |  |
| `allowed_status[].status_pismo` | string (schema `StatusPismo`) | no | Pismo card status. For more information, see [Card lifecycle and statuses](https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses).<br> | example: "LOST" |
| `allowed_status[].status_network` | string (schema `StatusNetworkMastercard`) | no | Network status equivalent to Pismo status. **REQUIRED** for Mastercard. <br /><br>  `C` - Credit <br /><br>  `F` - Fraud <br /><br>  `G` - ATM Premium Listing <br /><br>  `L` - Lost <br /><br>  `O` - Other <br /><br>  `P` - Capture card <br /><br>  `S` - Stolen <br /><br>  `U` - Unauthorized use <br /><br>  `V` - Premium listing <br /><br>  `X` - Counterfeit <br /><br><br>Mastercard documentation: Customer Interface Specification - DE 120 (Record Data) Layout for MCC102 - Field ID 2 (Entry Reason).<br> | enum: ["C", "F", "G", "L", "O", "P", "S", "U", "V", "X"]; example: "F" |
| `allowed_status[].default_purge_days` | number (schema `DefaultPurgeDays`) | no | After the specified number of days, a request to remove the card will be automatically sent to the network through the Protection Bulletin.<br><br>The `default_purge_days` field is optional, and if not provided, no action will be taken to remove this card from the Protection Bulletin.<br> | example: 30 |

_anyOf option 3: schema `Bulletin_Setup_Visa_Model`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `active` | boolean (schema `Active`) | yes | Is rule active? An inactive rule is not applied to transactions.<br> | example: true |
| `bid` | string (schema `Bid`) | yes | Business ID (BID) number - a six to 11 digit account number that Visa uses to bill clients. **REQUIRED** for Visa.<br><br>**Note:** It **must** be padded with leading zeros if less than 6 digits. <br> | minLength: 6; maxLength: 11; example: "001234" |
| `program_id` | number (schema `ProgramID`) | yes | Pismo program ID. | example: 1010 |
| `region_code` | array of string (schema `RegionCode`) | yes | Region code contains one or more Account Screen Authorization File (ASAF) region codes that define the distribution of a Visa cardholder account number in Card Recovery Bulletin Service files. **REQUIRED** for Visa. <br /><br>  `0` - No Bulletin / V.I.P. Only (cannot be combined with other region codes)<br /><br>  `A` - All Asia-Pacific region countries<br /><br>  `B` - All  Central Europe, Middle East, and Africa (CEMEA) region countries.<br /><br>  `C` - All Visa Canada<br /><br>  `D` - National Card Recovery Bulletin<br /><br>  `E` - All European countries<br /><br>  `F` - All Latin America and Caribbean (LAC) region countries <br /><br><br>Region codes can be in any order, except no other region code can be specified in combination with region code 0.<br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Table 215: Field 127E.2 Account Screen Authorization File (ASAF) Region Codes<br> | items.enum: ["0", "A", "B", "C", "D", "E", "F"] |
| `allowed_status` | array of object (schema `AllowedStatusVisaModel`) | yes | When passed, the Pismo Protection Bulletin service starts monitoring [Card updated events](https://developers.pismo.io/events/docs/cards-update-1). <br> <br> The `status_pismo` status determines if the card is sent to the network via the Protection Bulletin.<br> |  |
| `allowed_status[].status_pismo` | string (schema `StatusPismo`) | yes | Pismo card status. For more information, see [Card lifecycle and statuses](https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses).<br> | example: "LOST" |
| `allowed_status[].status_network` | string (schema `StatusNetworkVisa`) | yes | Network status equivalent to Pismo status. **REQUIRED** for Visa.<br /><br>  `04` - Pickup card<br /><br>  `05` - Do not honor<br /><br>  `07` - Pickup card, special condition<br /><br>  `11` - Approval for **VIP**<br /><br>  `14` - Invalid account number (no such number)<br /><br>  `41` - Lost card, pickup<br /><br>  `43` - Stolen card, pickup<br /><br>  `46` - Closed account<br /><br>  `54` - Expired card<br /><br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Table 214: Field 127E.1 Account Screen Authorization File (ASAF) Action Codes.<br> | enum: ["04", "05", "07", "11", "14", "41", "43", "46", "54"]; example: "04" |
| `allowed_status[].default_purge_days` | number (schema `DefaultPurgeDaysVisa`) | yes | After the specified number of days, a request to remove the card is automatically sent to the Protection Bulletin.<br> | example: 30 |


Example `Setup Rule Elo with allowed status`:

```json
{
  "active": true,
  "program_id": 1010,
  "allowed_status": [
    {
      "status_pismo": "LOST",
      "default_purge_days": 30
    },
    {
      "status_pismo": "ROBBED",
      "default_purge_days": 15
    }
  ]
}
```

Example `Setup Rule Elo without allowed status`:

```json
{
  "active": true,
  "program_id": 1010
}
```

Example `Setup Rule Mastercard with allowed status`:

```json
{
  "active": true,
  "ica": "012345",
  "program_id": 1010,
  "allowed_status": [
    {
      "status_pismo": "LOST",
      "status_network": "L",
      "default_purge_days": 30
    },
    {
      "status_pismo": "ROBBED",
      "status_network": "O",
      "default_purge_days": 15
    }
  ]
}
```

Example `Setup Rule Mastercard without allowed status`:

```json
{
  "active": true,
  "ica": "012345",
  "program_id": 1010
}
```

Example `Setup Rule Visa with allowed status`:

```json
{
  "active": true,
  "bid": "012345",
  "program_id": 1010,
  "region_code": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"
  ],
  "allowed_status": [
    {
      "status_pismo": "LOST",
      "status_network": "41",
      "default_purge_days": 30
    },
    {
      "status_pismo": "ROBBED",
      "status_network": "43",
      "default_purge_days": 15
    }
  ]
}
```

Example `Setup Rule Visa without allowed status`:

```json
{
  "active": true,
  "bid": "012345",
  "program_id": 1010,
  "region_code": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad Request | `application/json`: object (schema `ErrorMessageModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorMessageModel`) |
| 404 | Not Found | `application/json`: object (schema `ErrorMessageModel`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `ErrorMessageModel`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorMessageModel`) |
| 504 | Gateway Timeout | `application/json`: object (schema `ErrorMessageModel`) |

##### Response 400

400 Example `Failed to parse request payload`:

```json
{
  "code": "EBLT0003",
  "message": "Failed to parse request payload",
  "http_status_code": 400
}
```

##### Response 401

401 Example `Missing or invalid Authorization header`:

```json
{
  "code": "EBLT0005",
  "message": "Missing or invalid Authorization header",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing account-id`:

```json
{
  "code": "EBLT0006",
  "message": "Invalid Authorization header, missing account-id",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing tenant`:

```json
{
  "code": "EBLT0007",
  "message": "Invalid Authorization header, missing tenant",
  "http_status_code": 401
}
```

##### Response 404

404 Example `Programs API returned not found`:

```json
{
  "code": "EBLT0009",
  "message": "Programs API returned [Not found] using ID: {program_id}",
  "http_status_code": 404
}
```

##### Response 422

422 Example `Required fields for all brands`:

```json
{
  "code": "BBLT0001",
  "message": "Error while validating fields",
  "http_status_code": 422,
  "details": {
    "payload": [
      {
        "field": "program_id",
        "message": "This field is required"
      },
      {
        "field": "active",
        "message": "This field is required"
      }
    ]
  }
}
```

422 Example `Required fields for Mastercard brand`:

```json
{
  "code": "BBLT0001",
  "message": "Error while validating fields",
  "http_status_code": 422,
  "details": {
    "payload": [
      {
        "field": "ica",
        "message": "This field need to be length equals 6"
      },
      {
        "field": "allowed_status.status_network",
        "message": "This field has an invalid value (A). The accepted values are: C, F, G, L, O, P, S, U, V, X"
      }
    ]
  }
}
```

422 Example `Required fields for Visa brand`:

```json
{
  "code": "BBLT0001",
  "message": "Error while validating fields",
  "http_status_code": 422,
  "details": {
    "payload": [
      {
        "field": "bid",
        "message": "This field need to be length equals 6"
      },
      {
        "field": "region_code",
        "message": "This field is required"
      },
      {
        "field": "region_code",
        "message": "This field has an invalid value (Z). The accepted values are: 0, A, B, C, D, E, F"
      },
      {
        "field": "region_code",
        "message": "The value '0' in region_code is not allowed with other region_code."
      },
      {
        "field": "allowed_status.status_network",
        "message": "This field has an invalid value (00). The accepted values are: 04, 05, 07, 11, 14, 41, 43, 46, 54"
      }
    ]
  }
}
```

422 Example `The program with ID does not have a network brand`:

```json
{
  "code": "BBLT0006",
  "message": "The program with ID 123 does not have a network brand.",
  "http_status_code": 422
}
```

##### Response 500

500 Example `Something went wrong when try to process a request in another service`:

```json
{
  "code": "EBLT9998",
  "message": "Something went wrong when try to process a request in Programs API using ID: 123",
  "http_status_code": 500
}
```

500 Example `Something went wrong, please try again later`:

```json
{
  "code": "EBLT9999",
  "message": "Something went wrong, please try again later",
  "http_status_code": 500
}
```

##### Response 504

504 Example `Request timeout`:

```json
{
  "code": "EBLT0001",
  "message": "Request timeout",
  "http_status_code": 504
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBLT0003` | Failed to parse request payload |
| 401 | `EBLT0005` | Missing or invalid Authorization header |
| 401 | `EBLT0006` | Invalid Authorization header, missing account-id |
| 401 | `EBLT0007` | Invalid Authorization header, missing tenant |
| 404 | `EBLT0009` | Programs API returned [Not found] using ID: {program_id} |
| 422 | `BBLT0001` | Error while validating fields |
| 422 | `BBLT0006` | The program with ID 123 does not have a network brand. |
| 500 | `EBLT9998` | Something went wrong when try to process a request in Programs API using ID: 123 |
| 500 | `EBLT9999` | Something went wrong, please try again later |
| 504 | `EBLT0001` | Request timeout |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bulletin-bulletin-rule-1` | https://developers.pismo.io/events/docs/bulletin-bulletin-rule-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;404;422;500;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-protection-bulletin`.

<!-- op: spec=api-specs/Card_issuing_-_Protection_Bulletin.yaml method=GET path=/v1/bulletin/setup/{program_id} operationId=get-v1-bulletin-rule -->
### `GET /v1/bulletin/setup/{program_id}` — Get Protection Bulletin rule

- **operationId:** `get-v1-bulletin-rule`
- **Specification:** `api-specs/Card_issuing_-_Protection_Bulletin.yaml` (Card issuing - Protection Bulletin)
- **Server base URL(s):** `https://sandbox.pismolabs.io/protection-bulletin`
- **Tags:** `Rules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets a Protection Bulletin rule.
>
> The information requested is not returned in the endpoint response. Instead, the information is sent in a [Bulletin rule event](https://developers.pismo.io/events/docs/bulletin-bulletin-rule-1).
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `program_id` | path | yes | number | Pismo program ID. | example: 8765 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad Request | `application/json`: object (schema `ErrorMessageModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorMessageModel`) |
| 404 | Not Found | `application/json`: object (schema `ErrorMessageModel`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorMessageModel`) |
| 504 | Gateway Timeout | `application/json`: object (schema `ErrorMessageModel`) |

##### Response 400

400 Example `Invalid param`:

```json
{
  "code": "EBLT0004",
  "message": "Invalid program_id param",
  "http_status_code": 400
}
```

##### Response 401

401 Example `Missing or invalid Authorization header`:

```json
{
  "code": "EBLT0005",
  "message": "Missing or invalid Authorization header",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing account-id`:

```json
{
  "code": "EBLT0006",
  "message": "Invalid Authorization header, missing account-id",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing tenant`:

```json
{
  "code": "EBLT0007",
  "message": "Invalid Authorization header, missing tenant",
  "http_status_code": 401
}
```

##### Response 404

404 Example `Programs API returned not found`:

```json
{
  "code": "EBLT0009",
  "message": "Programs API returned [Not found] using ID: {program_id}",
  "http_status_code": 404
}
```

##### Response 500

500 Example `Something went wrong when try to process a request in another service`:

```json
{
  "code": "EBLT9998",
  "message": "Something went wrong when try to process a request in Programs API using ID: 123",
  "http_status_code": 500
}
```

500 Example `Something went wrong, please try again later`:

```json
{
  "code": "EBLT9999",
  "message": "Something went wrong, please try again later",
  "http_status_code": 500
}
```

##### Response 504

504 Example `Request timeout`:

```json
{
  "code": "EBLT0001",
  "message": "Request timeout",
  "http_status_code": 504
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBLT0004` | Invalid program_id param |
| 401 | `EBLT0005` | Missing or invalid Authorization header |
| 401 | `EBLT0006` | Invalid Authorization header, missing account-id |
| 401 | `EBLT0007` | Invalid Authorization header, missing tenant |
| 404 | `EBLT0009` | Programs API returned [Not found] using ID: {program_id} |
| 500 | `EBLT9998` | Something went wrong when try to process a request in Programs API using ID: 123 |
| 500 | `EBLT9999` | Something went wrong, please try again later |
| 504 | `EBLT0001` | Request timeout |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bulletin-bulletin-rule-1` | https://developers.pismo.io/events/docs/bulletin-bulletin-rule-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;404;500;504`, has examples `False`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorMessageModel -->
### Schema `ErrorMessageModel`

Pointer: `#/components/schemas/ErrorMessageModel`. Type: object (schema `ErrorMessageModel`).

> API generic returned error.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code. |  |
| `message` | string | no | Error description. |  |
| `http_status_code` | integer | no | HTTP status code. |  |
| `details` | object (schema `ErrorDetailMessageModel`) | no | Detailed information about the error. |  |

<!-- schema: #/components/schemas/ErrorDetailMessageModel -->
### Schema `ErrorDetailMessageModel`

Pointer: `#/components/schemas/ErrorDetailMessageModel`. Type: object (schema `ErrorDetailMessageModel`).

> Detailed information about the error.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payload` | array of object (schema `ErrorPayloadMessageModel`) | no | List of payload-related error details. |  |
| `header` | array of object (schema `ErrorHeaderMessageModel`) | no | List of header-related error details. |  |
| `parameters` | array of object (schema `ErrorParameterMessageModel`) | no | List of parameter-related error details. |  |

<!-- schema: #/components/schemas/ErrorPayloadMessageModel -->
### Schema `ErrorPayloadMessageModel`

Pointer: `#/components/schemas/ErrorPayloadMessageModel`. Type: object (schema `ErrorPayloadMessageModel`).

> Details about payload-related errors.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | no | Field name related to the error. | example: "field" |
| `message` | string | no | Error message for the field. | example: "Generic error" |

<!-- schema: #/components/schemas/ErrorHeaderMessageModel -->
### Schema `ErrorHeaderMessageModel`

Pointer: `#/components/schemas/ErrorHeaderMessageModel`. Type: object (schema `ErrorHeaderMessageModel`).

> Details about header-related errors.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | no | Header name related to the error. | example: "x-field" |
| `message` | string | no | Error message for the header. | example: "Generic error" |

<!-- schema: #/components/schemas/ErrorParameterMessageModel -->
### Schema `ErrorParameterMessageModel`

Pointer: `#/components/schemas/ErrorParameterMessageModel`. Type: object (schema `ErrorParameterMessageModel`).

> Details about parameter-related errors.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | no | Parameter name related to the error. | example: "query_parameter" |
| `message` | string | no | Parameter error message |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Protection_Bulletin.yaml` | tag `Rules`: POST /v1/bulletin/setup, GET /v1/bulletin/setup/{program_id} | https://github.com/PismoDevEx/pismo-api-specs | `6c5641a54569d51d…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-protection-bulletin` — Protection Bulletin
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
