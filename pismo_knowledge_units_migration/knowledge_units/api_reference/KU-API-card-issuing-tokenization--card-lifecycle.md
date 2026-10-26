---
ku_id: KU-API-card-issuing-tokenization--card-lifecycle
title: 'API reference: Card issuing - Tokenization — Card lifecycle'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Tokenization.yaml
  sha256: dd1e776cfe20b0d67cfcc866bc3663b044f224c72ea9b70658facb672666a03e
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
- transfertokens
- get-card-token-info
- card-token-operation
- get-card-config
- patch-card-config-reset-cvv2-try-counter
related_kus:
- KU-CARD-card-reissuing
- KU-CARD-card-tokenization-process-and-onboarding
- KU-ERR-codes-acq-to-esma
- KU-EVT-catalogue-cards
specification_version: 1.0.0
---

# API reference: Card issuing - Tokenization — Card lifecycle

**KU ID:** `KU-API-card-issuing-tokenization--card-lifecycle` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Card lifecycle` in `api-specs/Card_issuing_-_Tokenization.yaml` (“Card issuing - Tokenization”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Card lifecycle endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/cards/{cardId}/network-tokens/pan-update` | `transfertokens` | Transfer card tokens to other card | no |
| `GET /v1/cards/{cardId}/network-tokens` | `get-card-token-info` | Get card tokens | no |
| `POST /v1/cards/{card_id}` | `card-token-operation` | Card token operation | no |
| `GET /v1/cards/{cardId}/config` | `get-card-config` | Get card configuration | no |
| `PATCH /v1/cards/{cardId}/config/reset-cvv2-try-counter` | `patch-card-config-reset-cvv2-try-counter` | Reset CVV2 retry counter | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a "**401 Unauthorized**" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/cards/{cardId}/network-tokens/pan-update operationId=transfertokens -->
### `POST /v1/cards/{cardId}/network-tokens/pan-update` — Transfer card tokens to other card

- **operationId:** `transfertokens`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Card lifecycle`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Transfer all active tokens (activated/suspended) from one card to another
>
> This endpoint generates a [PAN updated](https://developers.pismo.io/events/docs/cards-tokenization-pan-update-1) event.
>
>
> **Notes**:
>   * This endpoint requires an account token - an access token encoded with a Pismo account ID.
>
>   * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `new_card_id` | number | no | ID of card to receive tokens | example: 51331 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Success |  |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 400

400 Example `example-1`:

```json
{
  "error_code": "ERR93836",
  "message": "Card profile can't be null"
}
```

##### Response 401

401 Example `example-1`:

```json
{
  "error_code": "ERR9786",
  "message": "Access token is missing or invalid"
}
```

##### Response 500

500 Example `example-1`:

```json
{
  "error_code": "ERR5446",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERR93836` | Card profile can't be null |
| 401 | `ERR9786` | Access token is missing or invalid |
| 500 | `ERR5446` | Internal server error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-tokenization-pan-update-1` | https://developers.pismo.io/events/docs/cards-tokenization-pan-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-reissuing`, `KU-CARD-card-tokenization-process-and-onboarding`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=GET path=/v1/cards/{cardId}/network-tokens operationId=get-card-token-info -->
### `GET /v1/cards/{cardId}/network-tokens` — Get card tokens

- **operationId:** `get-card-token-info`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Card lifecycle`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets token information given a card ID in the path.
>
> **Notes**:
>
>   * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `TokenInfoCardResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tokens` | array of object | no |  |  |
| `tokens[].token` | object (schema `TokenObject`) | no |  |  |
| `tokens[].token_id` | string (schema `TokenID`) | no | Pismo token ID | example: "412" |
| `tokens[].card_id` | number (schema `CardID`) | no | Card ID | example: 6743052 |
| `tokens[].wallet_id` | string (schema `WalletID`) | no | Wallet ID. Identifies the wallet (Samsung Pay, Google Pay, and so on) on the network. | example: "ANDROID_PAY" |
| `tokens[].account_id` | number (schema `AccountID`) | no | Pismo account ID | example: 8675309 |
| `tokens[].program_id` | string (schema `ProgramID`) | no | Pismo program ID | example: "8675" |
| `tokens[].org_id` | string (schema `OrgID`) | no | Pismo organiztion/tenant ID | example: "TN-ddce7e50-0485-49ec-a910-866dff0bfd0f" |
| `tokens[].payment_app_instance_id` | string (schema `PaymentAppInstanceID`) | no | Payment app instance ID |  |
| `tokens[].tracking_id` | string (schema `TrackingID`) | no | Tracking ID |  |
| `tokens[].status` | string (schema `TokenStatus`) | no | Token status | enum: ["ACTIVE", "SUSPENDED", "DEACTIVATED", "INACTIVE"]; example: "ACTIVE" |
| `network_data` | object | no |  |  |

200 Example `visa` (Example Visa response):

```json
{
  "tokens": [
    {
      "key": {
        "token_ref": "DNITHE302414169033123456",
        "pan_ref": "V-3024135706614877123456",
        "payment_network": "vts"
      },
      "token_id": "101178",
      "card_id": 71298,
      "wallet_id": "40000000045",
      "account_id": 127020000,
      "program_id": "10000",
      "org_id": "TN-542d1ef4-ed10-4be2-a4e1-4ac00000000",
      "payment_app_instance_id": "PISMOMOCKK3XvRHPjIDWFZErHEDytVg2MPJ6P7OM4JUq",
      "tracking_id": "D0000203850882",
      "status": "ACTIVE",
      "updated_at": "2024-05-10T16:40:20-03:00"
    },
    {
      "key": {
        "token_ref": "DNITHE3024141600000000",
        "pan_ref": "V-3024135706600000000000",
        "payment_network": "vts"
      },
      "token_id": "101000000",
      "card_id": 71200000,
      "wallet_id": "40010075338",
      "account_id": 1270000,
      "program_id": "10000",
      "org_id": "TN-542d1ef4-ed10-4be2-a4e1-400000000",
      "payment_app_instance_id": "",
      "tracking_id": "",
      "status": "ACTIVE"
    },
    {
      "key": {
        "token_ref": "DNITHE30241416000000000",
        "pan_ref": "V-30241357066148777000000",
        "payment_network": "vts"
      },
      "token_id": "1011",
      "card_id": 7129,
      "wallet_id": "40000000044",
      "account_id": 12701,
      "program_id": "10000",
      "org_id": "TN-542d1ef4-ed10-4be2-a4e1-40000000000",
      "payment_app_instance_id": "",
      "tracking_id": "",
      "status": "ACTIVE"
    },
    {
      "key": {
        "token_ref": "DNITHE3024141700000000",
        "pan_ref": "V-3024135706614000000000",
        "payment_network": "vts"
      },
      "token_id": "1011",
      "card_id": 7125,
      "wallet_id": "40010075001",
      "account_id": 12750000,
      "program_id": "100000,",
      "org_id": "TN-542d1ef4-ed10-4be2-a4e1-00000000",
      "payment_app_instance_id": "",
      "tracking_id": "",
      "status": "DEACTIVATED"
    }
  ],
  "network_data": {
    "tokenDetails": [
      {
        "tokenRequestorID": 40000000045,
        "tokenReferenceID": "DNITHE30241416900000000",
        "panReferenceID": "V-3024135706614800000000",
        "entityOfLastAction": "TOKEN_REQUESTOR",
        "walletAccountEmailAddressHash": "CE62283F46849994E08CADB975A95565C14F86FEE9792907B13A700000000",
        "clientWalletAccountID": "40000000045",
        "panSource": "KEY_ENTERED",
        "tokenType": "CARD_ON_FILE",
        "tokenStatus": "ACTIVE",
        "lastFourOfPAN": "6893"
      },
      {
        "tokenRequestorID": 40010075338,
        "tokenReferenceID": "DNITHE30241416900000000",
        "panReferenceID": "V-3024135706614800000000",
        "entityOfLastAction": "TOKEN_REQUESTOR",
        "walletAccountEmailAddressHash": "CE62283F46849994E08CADB975A95565C14F86FEE9792907B1300000000",
        "clientWalletAccountID": "PM123",
        "panSource": "KEY_ENTERED",
        "tokenType": "ECOMMERCE",
        "tokenStatus": "ACTIVE",
        "lastFourOfPAN": "6893"
      },
      {
        "tokenRequestorID": 40000000044,
        "tokenReferenceID": "DNITHE30241416900000000",
        "panReferenceID": "V-3024135706614800000000",
        "entityOfLastAction": "TOKEN_REQUESTOR",
        "walletAccountEmailAddressHash": "CE62283F46849994E08CADB975A95565C14F86FEE9792907B13A000000008",
        "clientWalletAccountID": "Muj00000000",
        "panSource": "KEY_ENTERED",
        "tokenType": "ECOMMERCE",
        "tokenStatus": "ACTIVE",
        "lastFourOfPAN": "6893"
      }
    ]
  }
}
```

200 Example `mastercard` (Example Mastercard response):

```json
{
  "tokens": [
    {
      "key": {
        "token_ref": "DSHRMC1BR0000000481138760dec4cf8a00000000",
        "pan_ref": "FSHRMC1BR0000000c790c134701d4ba48c9d00000000",
        "payment_network": "mdes"
      },
      "token_id\"": 10117,
      "card_id": 9024,
      "wallet_id": "216",
      "account_id": 18,
      "program_id": "9000",
      "org_id": "TN-d9abe1c7-f6b4-4b0a-b796-00000000",
      "payment_app_instance_id": "jHfrTg8qRRS8ZK3XvRHPjIDWFZErHEDytV00000000",
      "tracking_id": "D0000203850882",
      "status": "ACTIVE"
    }
  ],
  "network_data": {
    "SearchResponse": {
      "Accounts": {
        "Account": {
          "AccountPanSuffix\"": "3733",
          "ExpirationDate\"": "0729",
          "Tokens": {
            "Token": [
              {
                "AccountPanSequenceNumber": "000",
                "CorrelationId": "D00000000000",
                "CurrentStatusCode": "D",
                "CurrentStatusDateTime": "2024-07-01T15:52:39-05:00",
                "CurrentStatusDescription": "Deleted",
                "Device": {
                  "DeviceType": "21"
                },
                "DigitizationRequestDateTime": "2024-07-01T15:18:09-05:00",
                "ExpirationDate": "0827",
                "FinalTokenizationDecision": "A",
                "LastCommentId": "676521782",
                "PaymentAppInstanceId\"": "jHfrTg8qRRS8ZK3XvRHPjIDWFZErHEDytVg2MP00000000",
                "PrimaryAccountNumberUniqueReference": "FSHRMC1BR0000000c790c13470100000000",
                "ProvisioningStatusCode": "S",
                "ProvisioningStatusDescription": "Provisioning successful",
                "Source": "ACCOUNT_ADDED_VIA_APPLICATION",
                "StorageTechnology": "D",
                "Suspenders": {},
                "TokenActivatedDateTime": "2024-07-01T15:18:31-05:00",
                "TokenDeletedFromConsumerApp": "false",
                "TokenRequestorId": "50120834693",
                "TokenRequestorName": "GOOGLE",
                "TokenSuffix": "5740",
                "TokenType": "C",
                "TokenUniqueReference": "DSHRMC1BR0000000481138760dec4cf800000000",
                "WalletId": "216"
              }
            ]
          }
        }
      }
    }
  }
}
```

##### Response 400

400 Example `example-1`:

```json
{
  "error_code": "ERR93836",
  "message": "Card profile can't be null"
}
```

##### Response 401

401 Example `example-1`:

```json
{
  "error_code": "ERR9786",
  "message": "Access token is missing or invalid"
}
```

##### Response 500

500 Example `example-1`:

```json
{
  "error_code": "ERR5446",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERR93836` | Card profile can't be null |
| 401 | `ERR9786` | Access token is missing or invalid |
| 500 | `ERR5446` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-tokenization-process-and-onboarding`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/cards/{card_id} operationId=card-token-operation -->
### `POST /v1/cards/{card_id}` — Card token operation

- **operationId:** `card-token-operation`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Card lifecycle`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Perform token operation for card identified in path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `card_id` | path | yes | string | Pismo card ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `TokenOperationByCard`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `operation_reason` | string | yes | Token operation reason. Be descriptive, it should be clear what the customer needs to do. | maxLength: 255; example: "Suspended due to lost device." |
| `operation_type` | string | yes | Token operation to execute | enum: ["SUSPEND", "RESUME", "DELETE"]; example: "SUSPEND" |
| `operator_id` | string | no | Client-generated ID for person or system performing the operation. | example: "NbChEH" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal server error |  |

##### Response 400

400 Example `example-1` (example errors):

```json
{
  "message": "Fail on send event"
}
```

400 Example `example-2` (400BadRequest):

```json
{
  "message": "network respond bad request error",
  "error_code": "ERR4021"
}
```

400 Example `example-3` (404NotFound):

```json
{
  "message": "Token not found",
  "error_code": "ERR4091"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERR4021` | network respond bad request error |
| 400 | `ERR4091` | Token not found |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=GET path=/v1/cards/{cardId}/config operationId=get-card-config -->
### `GET /v1/cards/{cardId}/config` — Get card configuration

- **operationId:** `get-card-config`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Card lifecycle`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get card configuration.
>
> **Notes**:
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>  * This endpoint takes an account token - an access token encoded with a Pismo account ID

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 |  | `application/json`: object (schema `GetCardConfigCardResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `google_try_counter` | integer | no | Google wallet CVV try counter | example: 0 |
| `apple_try_counter` | integer | no | Apple wallet CVV try counter | example: 3 |
| `samsung_try_counter` | integer | no | Samsung wallet CVV try counter | example: 1 |

##### Response 400

400 Example `example-1`:

```json
{
  "message": "Card profile can't be null"
}
```

##### Response 500

500 Example `example-1`:

```json
{
  "message": "Internal server error"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=PATCH path=/v1/cards/{cardId}/config/reset-cvv2-try-counter operationId=patch-card-config-reset-cvv2-try-counter -->
### `PATCH /v1/cards/{cardId}/config/reset-cvv2-try-counter` — Reset CVV2 retry counter

- **operationId:** `patch-card-config-reset-cvv2-try-counter`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Card lifecycle`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Reset card and wallet CVV2 try counter to zero.
>
> **Notes**:
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>  * This endpoint takes an account token - an access token encoded with a Pismo account ID

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ResetCvv2TryCounterRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `wallet` | string | no | Wallet identifier:<br>  Google Pay -  `216`<br>  Apple Pay - `103`<br>  Samsung Pay - `217`<br> | enum: ["216", "103", "217"]; example: "216" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 |  |  |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 400

400 Example `example-1`:

```json
{
  "message": "Card profile can't be null"
}
```

##### Response 500

500 Example `example-1`:

```json
{
  "message": "Internal server error"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;500`, has examples `False`, emits events `0`, deprecated `False`.

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

<!-- schema: #/components/schemas/TokenObject -->
### Schema `TokenObject`

Pointer: `#/components/schemas/TokenObject`. Type: object (schema `TokenObject`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `key` | object | no |  |  |
| `key.token_ref` | string | no | Identifies the token on the network. | example: "PISMOMOCK000007767550841" |
| `key.pan_ref` | string | no | PAN reference - identifies the card on the network. | example: "V-2271272911360823654091" |
| `key.payment_network` | string | no | Payment network - `vts` (VISA) or `mdes` (Mastercard) | enum: ["vts", "mdes"]; example: "mdes" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Tokenization.yaml` | tag `Card lifecycle`: POST /v1/cards/{cardId}/network-tokens/pan-update, GET /v1/cards/{cardId}/network-tokens, POST /v1/cards/{card_id}, GET /v1/cards/{cardId}/config, PATCH /v1/cards/{cardId}/config/reset-cvv2-try-counter | https://github.com/PismoDevEx/pismo-api-specs | `dd1e776cfe20b0d6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-card-reissuing` — Card reissuing
- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-EVT-catalogue-cards` — Event catalogue: cards
