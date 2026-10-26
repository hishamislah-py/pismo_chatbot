---
ku_id: KU-API-card-issuing-tokenization--pre-digitalization
title: 'API reference: Card issuing - Tokenization — Pre-digitalization'
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
- post-wallet-data
- post-wallet-data-samsung
- post-encrypted-applepay-data
related_kus:
- KU-CARD-card-tokenization-process-and-onboarding
- KU-ERR-codes-acq-to-esma
specification_version: 1.0.0
---

# API reference: Card issuing - Tokenization — Pre-digitalization

**KU ID:** `KU-API-card-issuing-tokenization--pre-digitalization` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Pre-digitalization` in `api-specs/Card_issuing_-_Tokenization.yaml` (“Card issuing - Tokenization”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Pre-digitalization endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/googlepay` | `post-wallet-data` | Create encrypted card data for Google Pay | no |
| `POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/samsungpay` | `post-wallet-data-samsung` | Create encrypted card data for Samsung Pay | no |
| `POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/applepay` | `post-encrypted-applepay-data` | Create encrypted card data for Apple Pay | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a "**401 Unauthorized**" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/cards/{cardId}/network-tokens/push-provisioning/wallets/googlepay operationId=post-wallet-data -->
### `POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/googlepay` — Create encrypted card data for Google Pay

- **operationId:** `post-wallet-data`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Pre-digitalization`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

>
> Get encrypted card data to provision a token via Goodle SDK push-provisioning. Also returned is cardholder identifying information.
>
> **Notes**:
>   * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `EncryptedDataObjectRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `client_wallet_account_id` | string | no | Client-provided wallet account holder ID. **REQUIRED** for Visa. See Visa documentation for more information. | example: "ABC-198" |
| `client_device_id` | string | no | Stable device identifcation from wallet provider.  **REQUIRED** for Visa. See Visa documentation for more information. | example: "ABC-198" |
| `client_app_id` | string | no | Client application unique ID from Visa.  **REQUIRED** for Visa.  See Visa documentation for more information. | example: "ABC-198" |
| `client_wallet_provider` | string | no | Client wallet provider - the token requestor's ID (TRID) given to the wallet provider during onboarding.  **REQUIRED** for Visa. | example: "ABC-198" |
| `tav_version` | string (schema `TAVversion`) | no | The Token Authorization Value (TAV) version. The TAV value contains the issuer's digital signature that approves the token digitization for a Primary Account Number (PAN). **REQUIRED** for Mastercard if the issuer wants to use model `TAV4`.<br> | enum: ["TAV3", "TAV4"]; example: "TAV4" |
| `key_alias` | string (schema `TokenKeyAlias`) | no | Mastercard provided Key alias value used to generate the signature on a TAV body request. **REQUIRED** if Mastercard and `TAV4` version.<br> | example: "2023-abd-deeg" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `EncryptedDataObject`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `push_data` | object (schema `PushData`) | no | Encrypted data |  |
| `additional_info` | object (schema `AdditionalInfo`) | no |  |  |
| `has_address_info` | boolean (schema `HasAddressInfo`) | no | If `true`,  cardholder address information exists on Pismo platform.  If `false`, some fields inside `additional_info` are not returned.<br> |  |
| `has_phone_info` | boolean (schema `HasPhoneInfo`) | no | If `true`, cardholder phone information exists on Pismo platform. If `false`, some fields inside `additional_info` are not returned.<br> |  |

200 Example `visa` (VISA sample response):

```json
{
  "push_data": {
    "Token": "eyJhbGciOiJBMjU2R0NNS1ciLCJjaGFu..."
  },
  "additional_info": {
    "name": "Colab Org Antiga Empresa\"",
    "address": "",
    "country": "",
    "city": "",
    "state": "",
    "phone": "",
    "printed_name": "Colab Org Antiga Empresa",
    "last_4_digits": "5112"
  },
  "has_address_info": false,
  "has_phone_info": false
}
```

200 Example `mastercard` (Mastercard sample response):

```json
{
  "push_data": {
    "base64_issuer_initiated_digitization_data": "ewogICJmdW5kaW5nQWNjb3VudEluZm8iOiB7...",
    "additional_info": {
      "name": "Ron Rico",
      "address": "221B Baker Street",
      "country": "Elbonia",
      "city": "Raccoon",
      "phone": "867-5309",
      "state": "Siege",
      "zip_code": "8675309",
      "printed_name": "Tupper Weir",
      "last_4_digits": "9999"
    },
    "has_address_info": false,
    "has_phone_info": true
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

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/cards/{cardId}/network-tokens/push-provisioning/wallets/samsungpay operationId=post-wallet-data-samsung -->
### `POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/samsungpay` — Create encrypted card data for Samsung Pay

- **operationId:** `post-wallet-data-samsung`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Pre-digitalization`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

>
> Get encrypted card data to provision a token via Samsung SDK push-provisioning. Also returned is cardholder identifying information.
>
> **Notes**:
>   * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID.
>   * Currently only available for Visa

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `PushProvisioningSamsungObjectRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `client_wallet_account_id` | string | no | Client-provided wallet account holder ID. **REQUIRED** for Visa. See Visa documentation for more information. | example: "ABC-198" |
| `client_device_id` | string | no | Stable device identifcation from wallet provider.  **REQUIRED** for Visa. See Visa documentation for more information. | example: "ABC-198" |
| `client_app_id` | string | no | Client application unique ID from Visa.  **REQUIRED** for Visa.  See Visa documentation for more information. | example: "ABC-198" |
| `client_wallet_provider` | string | no | Client wallet provider - the token requestor's ID (TRID) given to the wallet provider during onboarding.  **REQUIRED** for Visa. | example: "ABC-198" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `EncryptedDataObject`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `push_data` | object (schema `PushData`) | no | Encrypted data |  |
| `additional_info` | object (schema `AdditionalInfo`) | no |  |  |
| `has_address_info` | boolean (schema `HasAddressInfo`) | no | If `true`,  cardholder address information exists on Pismo platform.  If `false`, some fields inside `additional_info` are not returned.<br> |  |
| `has_phone_info` | boolean (schema `HasPhoneInfo`) | no | If `true`, cardholder phone information exists on Pismo platform. If `false`, some fields inside `additional_info` are not returned.<br> |  |

200 Example `visa` (VISA sample response):

```json
{
  "push_data": {
    "Token": "eyJhbGciOiJBMjU2R0NNS1ciLCJjaGFu..."
  },
  "additional_info": {
    "name": "Colab Org Antiga Empresa\"",
    "address": "",
    "country": "",
    "city": "",
    "state": "",
    "phone": "",
    "printed_name": "Colab Org Antiga Empresa",
    "last_4_digits": "5112"
  },
  "has_address_info": false,
  "has_phone_info": false
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

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/cards/{cardId}/network-tokens/push-provisioning/wallets/applepay operationId=post-encrypted-applepay-data -->
### `POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/applepay` — Create encrypted card data for Apple Pay

- **operationId:** `post-encrypted-applepay-data`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Pre-digitalization`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Generate encrypted card data to provision a token via push-provisioning and the Apple SDK. Also returned is cardholder identifying information.
>
> **Notes:**
>   * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ApplePayEncryptedDataRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `Apple_public_certificate_b64` | array of string | yes | Apple SDK Base64 encoded certificate from Apple<br>*You need to encode what you receive from Apple with Base64 and then send it here.<br> |  |
| `device_type` | string | yes | Device type that the token will be provisioned for. | enum: ["MOBILE_PHONE", "WATCH"] |
| `app_version` | string | yes | Application version from the provisioning request. |  |
| `Nonce` | string | yes | From Apple SDK. Nonce = "number used once", a one-time-use random generated value. | example: "48585930" |
| `product_type` | string | no | From Apple SDK. Product type identifier. if a specific identifier needs to be passed, it **must** be entered in this field. if not passed, Pismo uses default values from the networks. | example: "016:XX:A000000001010111101" |
| `Nonce_signature` | string | yes | From Apple SDK | example: "vdt5543" |
| `tav_version` | string (schema `TAVversion`) | no | The Token Authorization Value (TAV) version. The TAV value contains the issuer's digital signature that approves the token digitization for a Primary Account Number (PAN). **REQUIRED** for Mastercard if the issuer wants to use model `TAV4`.<br> | enum: ["TAV3", "TAV4"]; example: "TAV4" |
| `key_alias` | string (schema `TokenKeyAlias`) | no | Mastercard provided Key alias value used to generate the signature on a TAV body request. **REQUIRED** if Mastercard and `TAV4` version.<br> | example: "2023-abd-deeg" |
| `authcode` | string | no | An issuer-generated 6-character code specific to the current provisioning request. Issuer and Visa use this field to identify specific activation codes in problem resolution or authentication related questions. Format is alphanumeric. Allowed characters include 0-9 and A-Z. Characters must be in uppercase and not contain all zeros or all spaces. **REQUIRED** for Visa.<br> | example: "0CVBD9" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `ApplePayEncryptedDataResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `push_data` | object | no |  |  |
| `push_data.ephemeralPublicKey` | string | no | Key pair for Apple SDK |  |
| `push_data.encryptedData` | string | no | Encrypted card data for Apple SDK |  |
| `push_data.activationData` | string | no | Encrypted data for Apple SDK in base64 format |  |
| `additional_info` | object | no |  | example: {"push_data": {"ephemeralPublicKey": "BLv5wb8HKPTlabxWW6z2at67jDqLZlFbGrOmq0bc2A0BbhRCmwWpzcf8ST2kEBctYX1nNZ9fE5MRSPf/4Tpz698=", "encryptedData": "uOt1....T9TOebjAM6DI43juahDiaMvpUaQZU2KNaICA==", "activationData": "ewogICJmdW5...PSIKfQ=="}, "additional_info": {"name": "Ron Rico", "address": "221B Baker Street", "country": "Elbonia", "city": "Raccoon", "phone": "867-5309", "state": "Siege", "zip_code": "8675309", "printed_name": "Tupper Weir", "last_4_digits": "9999", "has_address_info": false, "has_phone_info": true}} |
| `additional_info.name` | string | no | Cardholder name |  |
| `additional_info.address` | string | no | Cardholder address |  |
| `additional_info.country` | string | no | Cardholder country |  |
| `additional_info.city` | string | no | Cardholder city |  |
| `additional_info.state` | string | no | Cardholder state |  |
| `additional_info.phone` | string | no | Cardholder phone number |  |
| `additional_info.printed_name` | string | no | Name printed on card |  |
| `additional_info.last_4_digits` | string | no | Last 4 PAN digits |  |
| `additional_info.has_address_info` | boolean (schema `HasAddressInfo`) | no | If `true`,  cardholder address information exists on Pismo platform.  If `false`, some fields inside `additional_info` are not returned.<br> |  |
| `additional_info.has_phone_info` | boolean (schema `HasPhoneInfo`) | no | If `true`, cardholder phone information exists on Pismo platform. If `false`, some fields inside `additional_info` are not returned.<br> |  |

200 Example `example`:

```json
{
  "push_data": {
    "ephemeralPublicKey": "BLv5wb8HKPTlabxWW6z2at67jDqLZlFbGrOmq0bc2A0BbhRCmwWpzcf8ST2kEBctYX1nNZ9fE5MRSPf/4Tpz698=",
    "encryptedData": "uOt1....T9TOebjAM6DI43juahDiaMvpUaQZU2KNaICA==",
    "activationData": "ewogICJmdW5...PSIKfQ=="
  },
  "additional_info": {
    "name": "Ron Rico",
    "address": "221B Baker Street",
    "country": "Elbonia",
    "city": "Raccoon",
    "phone": "867-5309",
    "state": "Siege",
    "zip_code": "8675309",
    "printed_name": "Tupper Weir",
    "last_4_digits": "9999",
    "has_address_info": false,
    "has_phone_info": true
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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-tokenization-process-and-onboarding`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AdditionalInfo -->
### Schema `AdditionalInfo`

Pointer: `#/components/schemas/AdditionalInfo`. Type: object (schema `AdditionalInfo`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | no | Name |  |
| `address` | string | no | Address |  |
| `country` | string | no | Country |  |
| `city` | string | no | City |  |
| `state` | string | no | State |  |
| `phone` | string | no | Phone |  |
| `printed_name` | string | no | Name printed on card |  |
| `last_4_digits` | string | no | Last 4 PAN digits |  |

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
| `api-specs/Card_issuing_-_Tokenization.yaml` | tag `Pre-digitalization`: POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/googlepay, POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/samsungpay, POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/applepay | https://github.com/PismoDevEx/pismo-api-specs | `dd1e776cfe20b0d6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
