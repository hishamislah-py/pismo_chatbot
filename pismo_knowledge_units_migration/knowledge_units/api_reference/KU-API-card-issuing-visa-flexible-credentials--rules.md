---
ku_id: KU-API-card-issuing-visa-flexible-credentials--rules
title: 'API reference: Card issuing - Visa Flexible Credentials [beta] — Rules'
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
- get-card-rules
- update-card-rules
- create-card-rules
- delete-card-rules
- delete-specific-card-rule
related_kus:
- KU-CARD-visa-flexible-credentials
- KU-ERR-codes-acq-to-esma
specification_version: 1.0.0
---

# API reference: Card issuing - Visa Flexible Credentials [beta] — Rules

**KU ID:** `KU-API-card-issuing-visa-flexible-credentials--rules` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Rules` in `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` (“Card issuing - Visa Flexible Credentials [beta]”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Creation and management of rules to be applied during transactions using VFC credentials.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /flex_credentials/v1/vfc/rules/cards/{cardId}` | `get-card-rules` | List card rules | no |
| `PUT /flex_credentials/v1/vfc/rules/cards/{cardId}` | `update-card-rules` | Update card rules | no |
| `POST /flex_credentials/v1/vfc/rules/cards/{cardId}` | `create-card-rules` | Create rules | no |
| `DELETE /flex_credentials/v1/vfc/rules/cards/{cardId}` | `delete-card-rules` | Delete card rules | no |
| `DELETE /flex_credentials/v1/vfc/rules/cards/{cardId}/rule/{ruleId}` | `delete-specific-card-rule` | Delete rule | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a "**401 Unauthorized**" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml method=GET path=/flex_credentials/v1/vfc/rules/cards/{cardId} operationId=get-card-rules -->
### `GET /flex_credentials/v1/vfc/rules/cards/{cardId}` — List card rules

- **operationId:** `get-card-rules`
- **Specification:** `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` (Card issuing - Visa Flexible Credentials [beta])
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Rules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve card rules for a given primary card.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `access_token` | header | yes | string | Access token. Tokens can expire quickly, which can result in a **401 Unauthorized** error. |  |
| `cardId` | path | yes | string | Card ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Success | `application/json`: object (schema `RulesResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cardId` | integer (schema `CardID3`) | yes | Primary card ID | format: "int64"; example: 6743052 |
| `rules` | array of object (schema `Rule`) | yes |  |  |

201 Example `example`:

```json
{
  "cardId": 186283623,
  "rules": [
    {
      "cardId": 186283615,
      "rulePriority": 2,
      "scope": {
        "controlType": "TCT_AUTO_PAY",
        "cardHolderBillAmount": {
          "minAmount": 0,
          "maxAmount": 201.5
        },
        "timeRange": {
          "startTime": "2025-05-13T23:30:52.123Z",
          "endTime": "2025-08-13T23:30:52.123Z"
        }
      },
      "definedBy": "CARDHOLDER",
      "ruleId": "v-301-b0c3dfae-0dd7-40b6-9272-5fa466804a8a"
    }
  ]
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

<!-- op: spec=api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml method=PUT path=/flex_credentials/v1/vfc/rules/cards/{cardId} operationId=update-card-rules -->
### `PUT /flex_credentials/v1/vfc/rules/cards/{cardId}` — Update card rules

- **operationId:** `update-card-rules`
- **Specification:** `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` (Card issuing - Visa Flexible Credentials [beta])
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Rules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update rules for a given primary card.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `access_token` | header | yes | string | Access token. Tokens can expire quickly, which can result in a **401 Unauthorized** error. |  |
| `cardId` | path | yes | string | Card ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `RulesRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `rules` | array of object (schema `Rule2`) | yes |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Success | `application/json`: object (schema `RulesResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cardId` | integer (schema `CardID3`) | yes | Primary card ID | format: "int64"; example: 6743052 |
| `rules` | array of object (schema `Rule`) | yes |  |  |

201 Example `example`:

```json
{
  "cardId": 186283623,
  "rules": [
    {
      "cardId": 186283615,
      "name": "",
      "rulePriority": 2,
      "scope": {
        "controlType": "TCT_AUTO_PAY",
        "cardHolderBillAmount": {
          "minAmount": 0,
          "maxAmount": 201.5
        },
        "timeRange": {
          "startTime": "2025-05-13T23:30:52.123Z",
          "endTime": "2025-08-13T23:30:52.123Z"
        }
      },
      "definedBy": "CARDHOLDER",
      "ruleId": "v-301-b0c3dfae-0dd7-40b6-9272-5fa466804a8a"
    }
  ]
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

<!-- op: spec=api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml method=POST path=/flex_credentials/v1/vfc/rules/cards/{cardId} operationId=create-card-rules -->
### `POST /flex_credentials/v1/vfc/rules/cards/{cardId}` — Create rules

- **operationId:** `create-card-rules`
- **Specification:** `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` (Card issuing - Visa Flexible Credentials [beta])
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Rules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create rules for a primary card.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `access_token` | header | yes | string | Access token. Tokens can expire quickly, which can result in a **401 Unauthorized** error. |  |
| `cardId` | path | yes | string | Card ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `RulesRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `rules` | array of object (schema `Rule2`) | yes |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Success | `application/json`: object (schema `RulesResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cardId` | integer (schema `CardID3`) | yes | Primary card ID | format: "int64"; example: 6743052 |
| `rules` | array of object (schema `Rule`) | yes |  |  |

201 Example `example`:

```json
{
  "cardId": 186283623,
  "rules": [
    {
      "cardId": 186283615,
      "name": "",
      "rulePriority": 2,
      "scope": {
        "controlType": "TCT_AUTO_PAY",
        "cardHolderBillAmount": {
          "minAmount": 0,
          "maxAmount": 201.5
        },
        "timeRange": {
          "startTime": "2025-05-13T23:30:52.123Z",
          "endTime": "2025-08-13T23:30:52.123Z"
        }
      },
      "definedBy": "CARDHOLDER",
      "ruleId": "v-301-b0c3dfae-0dd7-40b6-9272-5fa466804a8a"
    }
  ]
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

<!-- op: spec=api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml method=DELETE path=/flex_credentials/v1/vfc/rules/cards/{cardId} operationId=delete-card-rules -->
### `DELETE /flex_credentials/v1/vfc/rules/cards/{cardId}` — Delete card rules

- **operationId:** `delete-card-rules`
- **Specification:** `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` (Card issuing - Visa Flexible Credentials [beta])
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Rules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete rules for a given primary card. (Rules in response represents the remaining rules after deleting the rule mentioned in the request).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `access_token` | header | yes | string | Access token. Tokens can expire quickly, which can result in a **401 Unauthorized** error. |  |
| `cardId` | path | yes | string | Card ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `RulesRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `rules` | array of object (schema `Rule2`) | yes |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Success | `application/json`: object (schema `RulesResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cardId` | integer (schema `CardID3`) | yes | Primary card ID | format: "int64"; example: 6743052 |
| `rules` | array of object (schema `Rule`) | yes |  |  |

201 Example `example`:

```json
{
  "cardId": 186283623,
  "rules": [
    {
      "cardId": 186283615,
      "name": "",
      "rulePriority": 2,
      "scope": {
        "controlType": "TCT_AUTO_PAY",
        "cardHolderBillAmount": {
          "minAmount": 0,
          "maxAmount": 201.5
        },
        "timeRange": {
          "startTime": "2025-05-13T23:30:52.123Z",
          "endTime": "2025-08-13T23:30:52.123Z"
        }
      },
      "definedBy": "CARDHOLDER",
      "ruleId": "v-301-b0c3dfae-0dd7-40b6-9272-5fa466804a8a"
    }
  ]
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

<!-- op: spec=api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml method=DELETE path=/flex_credentials/v1/vfc/rules/cards/{cardId}/rule/{ruleId} operationId=delete-specific-card-rule -->
### `DELETE /flex_credentials/v1/vfc/rules/cards/{cardId}/rule/{ruleId}` — Delete rule

- **operationId:** `delete-specific-card-rule`
- **Specification:** `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` (Card issuing - Visa Flexible Credentials [beta])
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Rules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete specific rule for a given primary card. (Rules in response represents the remaining rules after deleting the rule mentioned in the request)

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `access_token` | header | yes | string | Access token. Tokens can expire quickly, which can result in a **401 Unauthorized** error. |  |
| `cardId` | path | yes | string | Card ID |  |
| `ruleId` | path | yes | string | Rule ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Success | `application/json`: object (schema `RulesResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cardId` | integer (schema `CardID3`) | yes | Primary card ID | format: "int64"; example: 6743052 |
| `rules` | array of object (schema `Rule`) | yes |  |  |

201 Example `example`:

```json
{
  "cardId": 186283623,
  "rules": [
    {
      "cardId": 186283615,
      "name": "",
      "rulePriority": 2,
      "scope": {
        "controlType": "TCT_AUTO_PAY",
        "cardHolderBillAmount": {
          "minAmount": 0,
          "maxAmount": 201.5
        },
        "timeRange": {
          "startTime": "2025-05-13T23:30:52.123Z",
          "endTime": "2025-08-13T23:30:52.123Z"
        }
      },
      "definedBy": "CARDHOLDER",
      "ruleId": "v-301-b0c3dfae-0dd7-40b6-9272-5fa466804a8a"
    }
  ]
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

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Rule -->
### Schema `Rule`

Pointer: `#/components/schemas/Rule`. Type: object (schema `Rule`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cardId` | integer (schema `CardID5`) | yes | ID of card the rule applies to | format: "int64"; example: 6743052 |
| `rulePriority` | integer (schema `RulePriority`) | yes | Rule priority, `1` being the highest. | minimum: 1; example: 1 |
| `scope` | object (schema `RuleScope2`) | yes |  |  |
| `definedBy` | string (schema `RuleDefinedBy`) | yes | Entity that defined the rule | enum: ["CARDHOLDER", "ISSUER"]; example: "CARDHOLDER" |
| `ruleId` | string (schema `RuleID`) | yes | Rule ID | example: "v-301-b0c3dfae-0dd7-40b6-9272-5fa466804a8a" |

<!-- schema: #/components/schemas/ErrorObject -->
### Schema `ErrorObject`

Pointer: `#/components/schemas/ErrorObject`. Type: object (schema `ErrorObject`).

> Standard error object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code |  |
| `message` | string | no | Error message |  |

<!-- schema: #/components/schemas/Rule2 -->
### Schema `Rule2`

Pointer: `#/components/schemas/Rule2`. Type: object (schema `Rule2`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cardId` | integer (schema `CardID5`) | yes | ID of card the rule applies to | format: "int64"; example: 6743052 |
| `name` | string (schema `RuleName`) | yes | Rule name | example: "My Debit Card" |
| `rulePriority` | integer (schema `RulePriority`) | yes | Rule priority, `1` being the highest. | minimum: 1; example: 1 |
| `scope` | object (schema `RuleScope`) | yes |  |  |

<!-- schema: #/components/schemas/RuleScope2 -->
### Schema `RuleScope2`

Pointer: `#/components/schemas/RuleScope2`. Type: object (schema `RuleScope2`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `controlType` | string (schema `ControlType`) | yes | Transaction control type: <br>* `TCT_GLOBAL`&mdash; Transaction control type (TCT) global<br>* `TCT_ATM_WITHDRAW`&mdash; TCT ATM withdrawal<br>* `TCT_AUTO_PAY`&mdash; TCT autopay<br>* `TCT_BRICK_AND_MORTAR`&mdash; TCT brick and mortar<br>* `TCT_CROSS_BORDER`&mdash; TCT cross border<br>* `TCT_E_COMMERCE`&mdash; TCT e-commerce<br>* `TCT_CONTACTLESS`&mdash; TCT contactless card<br>* `MCT_ADULT_ENTERTAINMENT`&mdash; Merchant category type (MCT) adult entertainment<br>* `MCT_AIRFARE`&mdash; MCT airfare<br>* `MCT_ALCOHOL`&mdash; MCT alcohol<br>* `MCT_APPAREL_AND_ACCESSORIES`&mdash; MCT apparel and accessories<br>* `MCT_AUTOMOTIVE`&mdash; MCT automotive<br>* `MCT_CAR_RENTAL`&mdash; MCT car rental<br>* `MCT_ELECTRONICS`&mdash; MCT electronics<br>* `MCT_SPORT_AND_RECREATION`&mdash; MCT sport and recreation<br>* `MCT_GAMBLING`&mdash; MCT gambling<br>* `MCT_GAS_AND_PETROLEUM`&mdash; MCT gas and petroleum<br>* `MCT_GROCERY`&mdash; MCT grocery<br>* `MCT_HOTEL_AND_LODGING`&mdash; MCT hotel and lodging <br>* `MCT_HOUSEHOLD`&mdash; MCT household<br>* `MCT_PERSONAL_CARE`&mdash; MCT personal car<br>* `MCT_SMOKE_AND_TOBACCO`&mdash; MCT smoke and tobacco <br>* `MCT_DINING`&mdash; MCT dining<br><br>**Note:** Visa provides and validates these values. Consult your Visa representative to know which control types are available in your region. The values listed here are examples — if Visa provides a new `controlType` option not listed here, you can send it and Pismo will be accept it.<br> | enum: ["TCT_GLOBAL", "TCT_ATM_WITHDRAW", "TCT_AUTO_PAY", "TCT_BRICK_AND_MORTAR", "TCT_CROSS_BORDER", "TCT_E_COMMERCE", "TCT_CONTACTLESS", "MCT_ADULT_ENTERTAINMENT", "MCT_AIRFARE", "MCT_ALCOHOL", "MCT_APPAREL_AND_ACCESSORIES", "MCT_AUTOMOTIVE", "MCT_CAR_RENTAL", "MCT_ELECTRONICS", "MCT_SPORT_AND_RECREATION", "MCT_GAMBLING", "MCT_GAS_AND_PETROLEUM", "MCT_GROCERY", "MCT_HOTEL_AND_LODGING", "MCT_HOUSEHOLD", "MCT_PERSONAL_CARE", "MCT_SMOKE_AND_TOBACCO", "MCT_DINING"]; example: "TCT_AUTO_PAY" |
| `cardHolderBillAmount` | object (schema `CardholderBillAmount`) | yes |  |  |
| `timeRange` | object (schema `RuleValidityTimeRange`) | yes |  |  |

<!-- schema: #/components/schemas/RuleScope -->
### Schema `RuleScope`

Pointer: `#/components/schemas/RuleScope`. Type: object (schema `RuleScope`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `controlType` | string (schema `ControlType`) | yes | Transaction control type: <br>* `TCT_GLOBAL`&mdash; Transaction control type (TCT) global<br>* `TCT_ATM_WITHDRAW`&mdash; TCT ATM withdrawal<br>* `TCT_AUTO_PAY`&mdash; TCT autopay<br>* `TCT_BRICK_AND_MORTAR`&mdash; TCT brick and mortar<br>* `TCT_CROSS_BORDER`&mdash; TCT cross border<br>* `TCT_E_COMMERCE`&mdash; TCT e-commerce<br>* `TCT_CONTACTLESS`&mdash; TCT contactless card<br>* `MCT_ADULT_ENTERTAINMENT`&mdash; Merchant category type (MCT) adult entertainment<br>* `MCT_AIRFARE`&mdash; MCT airfare<br>* `MCT_ALCOHOL`&mdash; MCT alcohol<br>* `MCT_APPAREL_AND_ACCESSORIES`&mdash; MCT apparel and accessories<br>* `MCT_AUTOMOTIVE`&mdash; MCT automotive<br>* `MCT_CAR_RENTAL`&mdash; MCT car rental<br>* `MCT_ELECTRONICS`&mdash; MCT electronics<br>* `MCT_SPORT_AND_RECREATION`&mdash; MCT sport and recreation<br>* `MCT_GAMBLING`&mdash; MCT gambling<br>* `MCT_GAS_AND_PETROLEUM`&mdash; MCT gas and petroleum<br>* `MCT_GROCERY`&mdash; MCT grocery<br>* `MCT_HOTEL_AND_LODGING`&mdash; MCT hotel and lodging <br>* `MCT_HOUSEHOLD`&mdash; MCT household<br>* `MCT_PERSONAL_CARE`&mdash; MCT personal car<br>* `MCT_SMOKE_AND_TOBACCO`&mdash; MCT smoke and tobacco <br>* `MCT_DINING`&mdash; MCT dining<br><br>**Note:** Visa provides and validates these values. Consult your Visa representative to know which control types are available in your region. The values listed here are examples — if Visa provides a new `controlType` option not listed here, you can send it and Pismo will be accept it.<br> | enum: ["TCT_GLOBAL", "TCT_ATM_WITHDRAW", "TCT_AUTO_PAY", "TCT_BRICK_AND_MORTAR", "TCT_CROSS_BORDER", "TCT_E_COMMERCE", "TCT_CONTACTLESS", "MCT_ADULT_ENTERTAINMENT", "MCT_AIRFARE", "MCT_ALCOHOL", "MCT_APPAREL_AND_ACCESSORIES", "MCT_AUTOMOTIVE", "MCT_CAR_RENTAL", "MCT_ELECTRONICS", "MCT_SPORT_AND_RECREATION", "MCT_GAMBLING", "MCT_GAS_AND_PETROLEUM", "MCT_GROCERY", "MCT_HOTEL_AND_LODGING", "MCT_HOUSEHOLD", "MCT_PERSONAL_CARE", "MCT_SMOKE_AND_TOBACCO", "MCT_DINING"]; example: "TCT_AUTO_PAY" |
| `cardHolderBillAmount` | object (schema `CardholderBillAmount`) | yes |  |  |
| `timeRange` | object (schema `RuleValidityTimeRange`) | yes |  |  |

<!-- schema: #/components/schemas/CardholderBillAmount -->
### Schema `CardholderBillAmount`

Pointer: `#/components/schemas/CardholderBillAmount`. Type: object (schema `CardholderBillAmount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `maxAmount` | number (schema `MaxTransAmountAllowed`) | yes | Maximum transaction amount allowed | format: "float"; example: 20.5 |
| `minAmount` | number (schema `MinTransAmountAllowed`) | no | Minimum transaction amount allowed | format: "float"; example: 10.5 |

<!-- schema: #/components/schemas/RuleValidityTimeRange -->
### Schema `RuleValidityTimeRange`

Pointer: `#/components/schemas/RuleValidityTimeRange`. Type: object (schema `RuleValidityTimeRange`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `startTime` | string (schema `StartTimeRuleValidity`) | yes | Start time for rule validity. RFC 3339 format. | format: "date-time"; example: "2025-05-13T23:30:52.123Z" |
| `endTime` | string (schema `EndTimeRuleValidity`) | yes | End time for rule validity. RFC 3339 format. | format: "date-time"; example: "2025-05-13T23:30:52.123Z" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` | tag `Rules`: GET /flex_credentials/v1/vfc/rules/cards/{cardId}, PUT /flex_credentials/v1/vfc/rules/cards/{cardId}, POST /flex_credentials/v1/vfc/rules/cards/{cardId}, DELETE /flex_credentials/v1/vfc/rules/cards/{cardId}, DELETE /flex_credentials/v1/vfc/rules/cards/{cardId}/rule/{ruleId} | https://github.com/PismoDevEx/pismo-api-specs | `5144b0a0d49f5c69…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-visa-flexible-credentials` — Visa Flexible Credentials [beta]
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
