---
ku_id: KU-API-card-issuing-tokenization--token-lifecycle
title: 'API reference: Card issuing - Tokenization — Token lifecycle'
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
operations:
- gettokeninfo
- performtokenop
- post-run-visa-device-lifecycle
related_kus:
- KU-CARD-card-tokenization-process-and-onboarding
- KU-ERR-codes-acq-to-esma
- KU-EVT-client-webhooks-part-01
specification_version: 1.0.0
---

# API reference: Card issuing - Tokenization — Token lifecycle

**KU ID:** `KU-API-card-issuing-tokenization--token-lifecycle` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Token lifecycle` in `api-specs/Card_issuing_-_Tokenization.yaml` (“Card issuing - Tokenization”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Token lifecycle endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/cards/{cardId}/network-tokens/{tokenId}` | `gettokeninfo` | Get token information | no |
| `POST /v1/cards/{cardId}/network-tokens/{tokenId}` | `performtokenop` | Perform token operation | no |
| `POST /v1/cards/{cardId}/network-tokens/{tokenId}/devices/{deviceId}/binding` | `post-run-visa-device-lifecycle` | Bind Visa device and token | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a "**401 Unauthorized**" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=GET path=/v1/cards/{cardId}/network-tokens/{tokenId} operationId=gettokeninfo -->
### `GET /v1/cards/{cardId}/network-tokens/{tokenId}` — Get token information

- **operationId:** `gettokeninfo`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Token lifecycle`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets token information given a card ID and token ID in the path.
>
> **Notes**:
>   * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |
| `tokenId` | path | yes | string | Token ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 |  | `application/json`: object (schema `TokenInfoCardTokenResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `token` | object (schema `TokenObject`) | no |  |  |
| `token_id` | string (schema `TokenID`) | no | Pismo token ID | example: "412" |
| `card_id` | number (schema `CardID`) | no | Card ID | example: 6743052 |
| `wallet_id` | string (schema `WalletID`) | no | Wallet ID. Identifies the wallet (Samsung Pay, Google Pay, and so on) on the network. | example: "ANDROID_PAY" |
| `account_id` | number (schema `AccountID`) | no | Pismo account ID | example: 8675309 |
| `program_id` | string (schema `ProgramID`) | no | Pismo program ID | example: "8675" |
| `org_id` | string (schema `OrgID`) | no | Pismo organiztion/tenant ID | example: "TN-ddce7e50-0485-49ec-a910-866dff0bfd0f" |
| `payment_app_instance_id` | string (schema `PaymentAppInstanceID`) | no | Payment app instance ID |  |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID |  |
| `status` | string (schema `TokenStatus`) | no | Token status | enum: ["ACTIVE", "SUSPENDED", "DEACTIVATED", "INACTIVE"]; example: "ACTIVE" |
| `network_data` | object (schema `NetworkDetails`) | no | Dynamic data that varies according to network |  |

200 Example `mastercard` (Example Mastercard response):

```json
{
  "token": {
    "key": {
      "token_ref": "PISMOMOCK481138760dec4cf8ad407deeff4d8a3d",
      "pan_ref": "PISMOMOCK00000c790c134701d4ba48c9dc3003ba433c8",
      "payment_network": "mdes"
    }
  },
  "token_id": "1011781234",
  "card_id": 90241234,
  "wallet_id": "216",
  "account_id": 183701234,
  "program_id": "4321",
  "org_id": "TN-d9abe1c7-f6b4-4b0a-b796-d3b512341234",
  "payment_app_instance_id": "PISMOMOCKK3XvRHPjIDWFZErHEDytVg2MPJ6P7OM4JUq",
  "tracking_id": "D0000203850882",
  "status": "ACTIVE",
  "updated_at": "2024-05-10T16:40:20-03:00",
  "devices": [
    {
      "device_id": "12345",
      "device_index": 1
    }
  ],
  "network_data": {
    "AccountPanSequenceNumber": "000",
    "CorrelationId": "D0000203851234",
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
    "PaymentAppInstanceId": "PISMOMOCKRRS8ZK3XvRHPjIDWFZErHEDytVg2MPJ6P7OM4JUq",
    "PrimaryAccountNumberUniqueReference": "PISMOMOCK0000000c790c134701d4ba48c9dc3003ba433c8",
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
    "TokenUniqueReference": "DSHRMC1BR0000000481138760dec4cf8ad407dee12345678",
    "WalletId": "216"
  }
}
```

200 Example `visa` (Example VISA response):

```json
{
  "token": {
    "key": {
      "token_ref": "DNITHE302414169012345678",
      "pan_ref": "V-3024135706614812345678",
      "payment_network": "vts"
    }
  },
  "token_id": "1011781234",
  "card_id": 71291234,
  "wallet_id": "40000000045",
  "account_id": 127021234,
  "program_id": "11234",
  "org_id": "TN-542d1ef4-ed10-4be2-a4e1-4ac123456789",
  "payment_app_instance_id": "",
  "tracking_id": "",
  "status": "ACTIVE",
  "network_data": {
    "panReferenceID": "V-3024135706614812345678",
    "entityOfLastAction": "TOKEN_REQUESTOR",
    "walletAccountEmailAddressHash": "PISMOMOCK6849994E08CADB975A95565C14F86FEE9792907B13A7D7332402988",
    "clientWalletAccountID": "40000000045",
    "panSource": "KEY_ENTERED",
    "lastFourOfPAN": "6893",
    "tokenInfo": {
      "token": "123456789",
      "tokenType": "CARD_ON_FILE",
      "tokenStatus": "ACTIVE",
      "tokenExpirationDate": {
        "month": "4",
        "year": "2029"
      }
    },
    "tokenAssuranceMethod": "10",
    "lastTokenStatusUpdatedTime": "2024-05-22T19:38:24.000Z",
    "deviceInfo": {},
    "riskInfo": {}
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

Guides that link to this operation: `KU-CARD-card-tokenization-process-and-onboarding`, `KU-EVT-client-webhooks-part-01`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/cards/{cardId}/network-tokens/{tokenId} operationId=performtokenop -->
### `POST /v1/cards/{cardId}/network-tokens/{tokenId}` — Perform token operation

- **operationId:** `performtokenop`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Token lifecycle`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Perform token operation.
>
> **Notes**:
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>  * This endpoint takes an account token - an access token encoded with a Pismo account ID

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |
| `tokenId` | path | yes | string | Token ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `TokenOperationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `operation_reason` | string (schema `OperationReason`) | yes | Operation reason. Be descriptive, it should be clear what the customer needs to do. For a suspended token, for example, the reason could say "Suspended due to lost device."<br> | maxLength: 254; example: "Suspended due to lost device" |
| `operation_type` | string (schema `OperationType`) | yes | Operation type:<br><br>* `DELETE` - Delete token<br><br>* `SUSPEND` - Suspend token<br><br>* `RESUME` - Resume suspended token<br><br>* `CALL_CENTER_ACTIVATION` - Call center verification<br><br>* `CARDHOLDER_STEPUP_APP_TO_APP` - App2App verification<br><br>* `TOKEN_DEVICE_BIDING_APPROVE` - Device verification, approve and activate the most recently inactive device (only Visa)<br><br>* `TOKEN_DEVICE_BINDING_APPROVE_CALL_CENTER` - Device verification with call center activation, approve and activate the most recently inactive device (only Visa)<br><br>* `TOKEN_DEVICE_BINDING_APPROVE_BANK_APP` - Device verification with bank app approval, approve and activate the most recently inactive device (only Visa)<br><br>**Note**: For App2App token activation, set this field to `CARDHOLDER_STEPUP_APP_TO_APP` (Mastercard) and `CALL_CENTER_ACTIVATION` (Visa).<br> | enum: ["DELETE", "SUSPEND", "RESUME", "CALL_CENTER_ACTIVATION", "CARDHOLDER_STEPUP_APP_TO_APP", "TOKEN_DEVICE_BIDING_APPROVE", "TOKEN_DEVICE_BINDING_APPROVE_BANK_APP"]; example: "DELETE" |
| `activation_code` | string (schema `ActivationCode`) | no | REQUIRED if `operation_type` is `CALL_CENTER_ACTIVATION`. These codes are known only to the issuer/caller. | maxLength: 8; example: "94" |
| `operator_id` | string (schema `OperatorID`) | no | Client-generated ID for person or system performing the operation. This is for client monitoring and internal record-keeping. | maxLength: 16 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success |  |
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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-tokenization-process-and-onboarding`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/cards/{cardId}/network-tokens/{tokenId}/devices/{deviceId}/binding operationId=post-run-visa-device-lifecycle -->
### `POST /v1/cards/{cardId}/network-tokens/{tokenId}/devices/{deviceId}/binding` — Bind Visa device and token

- **operationId:** `post-run-visa-device-lifecycle`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Token lifecycle`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Executes Visa device binding for a given token and device. Device binding establishes that a specific device belongs to a specific cardholder. Once bound, the device can be trusted more in future transactions.
>
> An issuer can use this endpoint to update the status of a specific device linked to a token.
>
> **Notes**:
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>  * This endpoint takes an account token - an access token encoded with a Pismo account ID

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |
| `tokenId` | path | yes | string | Token ID |  |
| `deviceId` | path | yes | string | Device ID (wallet device ID) |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `VisaDeviceBindingRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `operator_id` | string (schema `OperatorID`) | yes | Client-generated ID for person or system performing the operation. This is for client monitoring and internal record-keeping. | maxLength: 16 |
| `operation_type` | string (schema `OperationType2`) | yes | Visa device binding lifecycle operation type. | enum: ["TOKEN_DEVICE_BINDING_REMOVE", "TOKEN_DEVICE_BINDING_APPROVE", "TOKEN_DEVICE_BINDING_APPROVE_BANK_APP", "TOKEN_DEVICE_BINDING_APPROVE_CALL_CENTER"] |
| `operation_reason` | string (schema `OperationReason2`) | yes | Visa lifecycle operation reason. | enum: ["FRAUD", "LOST_CARD", "STOLEN_CARD", "LOST_DEVICE", "STOLEN_DEVICE", "CUSTOMER_REQUEST", "CLOSED", "FOUND_DEVICE"] |
| `activation_code` | string (schema `ActivationCode2`) | no | Activation code **REQUIRED** when `operation_type` = `TOKEN_DEVICE_BINDING_APPROVE_CALL_CENTER`. | maxLength: 8 |
| `device_index` | integer (schema `DeviceIndex`) | yes | Visa index number for device ID. | maxLength: 2; example: 99 |

Example `approve`:

```json
{
  "operator_id": "123",
  "operation_type": "TOKEN_DEVICE_BINDING_APPROVE",
  "operation_reason": "FOUND_DEVICE",
  "activation_code": "1",
  "device_id": "1",
  "device_index": 0
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Operation successfully executed. | `application/json`: object |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `network_ack` | boolean | no | Was the network operation acknowledged? |  |

200 Example `ok`:

```json
{
  "network_ack": true
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

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/TokenObject -->
### Schema `TokenObject`

Pointer: `#/components/schemas/TokenObject`. Type: object (schema `TokenObject`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `key` | object | no |  |  |
| `key.token_ref` | string | no | Identifies the token on the network. | example: "PISMOMOCK000007767550841" |
| `key.pan_ref` | string | no | PAN reference - identifies the card on the network. | example: "V-2271272911360823654091" |
| `key.payment_network` | string | no | Payment network - `vts` (VISA) or `mdes` (Mastercard) | enum: ["vts", "mdes"]; example: "mdes" |

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
| `api-specs/Card_issuing_-_Tokenization.yaml` | tag `Token lifecycle`: GET /v1/cards/{cardId}/network-tokens/{tokenId}, POST /v1/cards/{cardId}/network-tokens/{tokenId}, POST /v1/cards/{cardId}/network-tokens/{tokenId}/devices/{deviceId}/binding | https://github.com/PismoDevEx/pismo-api-specs | `dd1e776cfe20b0d6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
