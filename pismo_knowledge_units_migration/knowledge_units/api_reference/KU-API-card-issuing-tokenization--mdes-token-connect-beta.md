---
ku_id: KU-API-card-issuing-tokenization--mdes-token-connect-beta
title: 'API reference: Card issuing - Tokenization — MDES Token Connect [Beta]'
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
- token_connet_push_multiple_accounts
- token_connect_get_eligible_token_requestors
- token_connect_get_asset
related_kus: []
specification_version: 1.0.0
---

# API reference: Card issuing - Tokenization — MDES Token Connect [Beta]

**KU ID:** `KU-API-card-issuing-tokenization--mdes-token-connect-beta` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `MDES Token Connect [Beta]` in `api-specs/Card_issuing_-_Tokenization.yaml` (“Card issuing - Tokenization”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Mastercard's Token Connect service endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/token-connect/push-multiple-accounts` | `token_connet_push_multiple_accounts` | Push multiple accounts | no |
| `POST /v1/token-connect` | `token_connect_get_eligible_token_requestors` | Get eligible token requestors | no |
| `GET /v1/token-connect/assets/{assetId}` | `token_connect_get_asset` | Get token requestor logo | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a "**401 Unauthorized**" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/token-connect/push-multiple-accounts operationId=token_connet_push_multiple_accounts -->
### `POST /v1/token-connect/push-multiple-accounts` — Push multiple accounts

- **operationId:** `token_connet_push_multiple_accounts`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `MDES Token Connect [Beta]`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Push card and account(s) to a token requestor.
>
> A token requestor is an entity that initiates the tokenization process. Wallets, merchants, payments service providers (PSPs) are collectively referred to as **token requestors**.
>
> **Notes:**
>
>   * Pismo acts as a proxy for the <a href="https://developer.mastercard.com/mdes-token-connect/documentation/api-reference/" target="_blank">Mastercard Token Connect API</a>
>
>   * This endpoint does not generate an event
>
>   * For more information, refer to the [MDES Token Connect](doc:mdes-token-connect) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `access_token` | header | yes | string | Access token. Tokens can expire quickly, which can result in a **401 Unauthorized** error. |  |
| `x-account-id` | header | yes | integer | Account ID | format: "int64" |
| `x-customer-id` | header | yes | integer | Customer ID |  |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `PushAccountsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | number (schema `CardID`) | yes | Card ID | example: 6743052 |
| `accounts` | object (schema `AccountData`) | yes |  |  |
| `token_requestor_id` | string (schema `TokenRequestorId`) | yes | Token requestor ID (TRID), a numeric 11-digit value.<br><br>A token requestor is an entity that initiates the tokenization process. Wallets, merchants, payments service providers (PSPs) are collectively referred to as **token requestors**.<br><br>Card networks use TRIDs to enforce usage boundaries at the network level, know who is reponsible if fraud occurs, and to prevent tokens from being used elsewhere.<br> | maxLength: 11; example: "01234567890" |
| `locale` | string (schema `Locale`) | yes | Consumer preferred locale (language and country).<br><br>**Format**: two-letter ISO-639-1 language in lowercase + underscore ("_") + two-letter ISO 3166-1 country code in uppercase.<br> | example: "en_US" |
| `callback_url` | string | no | Callback URL token requestor uses to pass control back to the issuer.<br> | maxLength: 256; example: "https://callback.example.com" |
| `complete_issuer_app_activation` | boolean | no | Should token requestor complete app activation if provisioning request receives a `REQUIRE_ADDITIONAL_AUTHENTICATION` and the cardholder chooses the `CARDHOLDER_TO_USE_ISSUER_MOBILE_APP` authentication method?<br> | default: false |
| `complete_website_activation` | boolean | no | Should token requestor complete website activation if provisioning request receives a `REQUIRE_ADDITIONAL_AUTHENTICATION` and the cardholder chooses the `CARDHOLDER_TO_VISIT_WEBSITE` authentication method?<br> | default: false |
| `account_holder_data_supplied` | boolean | no | Is cardholder information stored in MDES along with funding account information? | default: false |
| `request_issuer_initiated_digitization_data` | boolean | no | Return issuer initiated digitization data? | default: false |
| `push_account_receipts_validity_period` | number | no | Push account receipts validity period in minutes. If issuer is pushing more than one account, the provided value is applicable to all receipts.<br><br>Default is `15`. **Must** be greater or equal to `5` and less than or equal to `15`.<br> | enum: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]; default: 15; minimum: 5; maximum: 15; example: 15 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successful response | `application/json`: object (schema `PushAccountsResponse`) |
| 400 | Bad request |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `push_account_receipts` | array of object (schema `PushAccountReceipt`) | no | Push account receipts |  |
| `available_push_methods` | array of object (schema `PushMethod`) | no | Available push methods |  |
| `signature` | string | no | JWS signature output. **REQUIRED** if `token_reqiest_signature_support` is `true` and at least one push account receipt is returned.<br> |  |
| `token_requestor_signature_support` | boolean | no | Does token requestor support signature verification? |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/token-connect operationId=token_connect_get_eligible_token_requestors -->
### `POST /v1/token-connect` — Get eligible token requestors

- **operationId:** `token_connect_get_eligible_token_requestors`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `MDES Token Connect [Beta]`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve information about token requestors that have been enabled for one or more of the issuer's account ranges.
>
> Pismo acts as a proxy for the <a href="https://developer.mastercard.com/mdes-token-connect/documentation/api-reference/" target="_blank">Mastercard Token Connect API</a>
>
> For more information, refer to the [MDES Token Connect](doc:mdes-token-connect) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `access_token` | header | yes | string | Access token. Tokens can expire quickly, which can result in a **401 Unauthorized** error. |  |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `TokenRequestorRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accounts` | array of string | yes | Account ranges to check for eligibility.<br><br>The starting numbers are numeric strings between 9 and 19 in length. If the starting numbers are less than 19, MDES  zero pads the starting numbers to 19 in length. The padded value must exactly match the account range start number enabled for the token requestor.<br> | example: ["5412346789", "5412346780"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successful response | `application/json`: object (schema `TokenRequestorResponse`) |
| 400 | Bad request |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `token_requestors` | array of object (schema `TokenRequestor`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=GET path=/v1/token-connect/assets/{assetId} operationId=token_connect_get_asset -->
### `GET /v1/token-connect/assets/{assetId}` — Get token requestor logo

- **operationId:** `token_connect_get_asset`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `MDES Token Connect [Beta]`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Returns a token requestor's logo, in `PNG` and `SVG` format.
>
> For more information, refer to the <a href="https://developer.mastercard.com/mdes-token-connect/documentation/api-reference/" target="_blank">Mastercard Token Connect API</a>.
>
> Pismo acts as a proxy for the Mastercard Token Connect API.
>
> For more information, refer to the [MDES Token Connect](doc:mdes-token-connect) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |
| `assetId` | path | yes | string | Image asset ID.  This is the `image_asset_id` field returned from the [Get eligible token requestors](ref:token_connect_get_eligible_token_requestors) endpoint.<br> |  |
| `access_token` | header | yes | string | Access token. Tokens can expire quickly, which can result in a **401 Unauthorized** error. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successful response | `application/json`: object (schema `GetAssetResponse`) |
| 400 | Bad request |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `media_contents` | array of object (schema `MediaContent`) | no | List of media content items | example: [{"type": "image/png", "data": "base64EncodedImageData...", "height": "100", "width": "100"}] |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccountData -->
### Schema `AccountData`

Pointer: `#/components/schemas/AccountData`. Type: object (schema `AccountData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `holder_details` | object (schema `HolderDetails`) | yes | Account holder details object |  |
| `validity_details` | object (schema `ValidityDetails`) | yes |  |  |

<!-- schema: #/components/schemas/PushAccountReceipt -->
### Schema `PushAccountReceipt`

Pointer: `#/components/schemas/PushAccountReceipt`. Type: object (schema `PushAccountReceipt`).

> Push account receipts object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `push_account_id` | string | yes | Push account ID | maxLength: 36; example: "pa_123456789" |
| `push_account_receipt` | string | yes | Push account receipt to token requestor. Contains pushed account details and expires after 15 minutes.<br><br>A valid receipt =  3-character prefix identifying product associated with funding account + UUID.<br><br>Prefic values:<br>  * `MCC` - Mastercard credit<br>  * `DMC` - Mastercard debit<br>  * `MSI` - Maestro<br>  * `PVL` - Private label<br> | maxLength: 64; example: "MCC-C307FOAE-298E-48EB-AA43-A7C40B32DDDE" |
| `issuer_initiated_digitization_data` | string | no | Base64 encoded string issuer can pass to token requestor proprietary communication. Present if `request_issuer_initiated_digitization_data` is `true` in the request.<br> | maxLength: 256000 |

<!-- schema: #/components/schemas/PushMethod -->
### Schema `PushMethod`

Pointer: `#/components/schemas/PushMethod`. Type: object (schema `PushMethod`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | yes | Push method type<br><br>* `ANDROID` - Android app intent URI<br>* `IOS` - iOS app intent URI<br>* `WEB` - Browser URL<br> | enum: ["ANDROID", "IOS", "WEB"]; example: "WEB" |
| `uri` | string | yes | URI to open the token requestor's application or website. | format: "uri"; maxLength: 128; example: "https://tokenize.example.com" |

<!-- schema: #/components/schemas/TokenRequestor -->
### Schema `TokenRequestor`

Pointer: `#/components/schemas/TokenRequestor`. Type: object (schema `TokenRequestor`).

> Token requestor information. Wallets, Merchants, Payment Service Providers are collectively referred to as token requestors

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `token_requestor_id` | string (schema `TokenRequestorId`) | yes | Token requestor ID (TRID), a numeric 11-digit value.<br><br>A token requestor is an entity that initiates the tokenization process. Wallets, merchants, payments service providers (PSPs) are collectively referred to as **token requestors**.<br><br>Card networks use TRIDs to enforce usage boundaries at the network level, know who is reponsible if fraud occurs, and to prevent tokens from being used elsewhere.<br> | maxLength: 11; example: "01234567890" |
| `name` | string | yes | Token requestor legal name | maxLength: 64; example: "Acme Widgets, Inc." |
| `consumer_facing_entity_name` | string | yes | Consumer facing entity name. Token requestor display name. | maxLength: 100; example: "Acme Widgets Online" |
| `token_requestor_type` | string (schema `TokenRequestorType`) | yes | Token requestor type<br><br>* `MERCHANT` - Merchant token requestor. For example - Netflix, Uber, Amazon, and so on.<br><br>* `WALLET`- Wallet or commerce platform token requestor. For example - Apple Pay, Google Wallet, Samsung Pay, and so on.<br> | enum: ["MERCHANT", "WALLET"]; example: "MERCHANT" |
| `enabled_account_ranges` | array of integer | yes | Array of account range start numbers enabled for token requestor. The start numbers are 19 digits in length.<br> | items.format: "int64" |
| `image_asset_id` | string | no | Token requestor image (for instance a logo) asset ID.<br>Call the [Get asset](ref:token_connect_get_asset) endpoint to retrieve the image.<br> |  |
| `wallet_id` | string (schema `WalletID2`) | no | Wallet provider ID. Returned if token requestor is a wallet like Google Pay or Samsung Pay.<br> | maxLength: 3; example: "123" |
| `supported_push_methods` | array of string | no | Web-to-web or app-to-web push methods token requestor supports. Not returned if the token requestor does not participate in the MDES Token Connect program.<br> | items.enum: ["ANDROID", "IOS", "WEB"] |
| `supports_multiple_pushed_cards` | boolean | no | Does token requestor support up to 5 push account receipts in a single request?  Present if the token requestor participates in MDES Token Connect program.<br> |  |
| `supported_account_holder_data` | array of string | no | <br>Account holder data elements the token requestor expects to receive from the issuer with a pushed card or account.<br><br>Only returned if the token requestor participates in MDES Token Connect.<br><br>If the token requestor participates but doesn't accept account holder data, then an empty array is returned. To ensure forward-compatibility, all API client implementations must be resilient to new data element values being added to responses from MDES.<br><br>*  `NAME` - Account holder first and last name<br>*  `ADDRESS` - Account holder billing address<br>*  `EMAIL_ADDRESS` - Account holder email address<br>*  `MOBILE_PHONE_NUMBER` - Account holder mobile phone number<br> | items.enum: ["NAME", "ADDRESS", "EMAIL_ADDRESS", "MOBILE_PHONE_NUMBER"] |
| `supports_card_holder_authentication` | boolean | no | Does token requestor support cardholder authentication after the token is activated?<br> |  |
| `supports_token_connect` | boolean | no | Does token requestor support Token Connect?<br> |  |
| `available_push_methods` | array of object (schema `PushMethod`) | no | Available push methods |  |
| `support_issuer_initiated_digitization_data` | boolean | no | Does token requestor support Issuer Initiated Digitization Data?<br> |  |

<!-- schema: #/components/schemas/MediaContent -->
### Schema `MediaContent`

Pointer: `#/components/schemas/MediaContent`. Type: object (schema `MediaContent`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | yes | <br>Media content MIME type<br><br>* `application/pdf` - For images (must be a vector PDF image)<br>* `image/png` -  Includes alpha channel<br>* `image/svg+xml` -  Image in SVG format<br>* `text/plain` - Plain text<br>* `text/html` - HTML text<br> | enum: ["application/pdf", "image/png", "image/svg+xml", "text/plain", "text/html"]; example: "image/png" |
| `data` | string | yes | Base64 encoded media data. | example: "base64EncodedImageData..." |
| `height` | string | no | For non-SVG image assets, the image height in pixels.<br> | maxLength: 6; example: "100" |
| `width` | string | no | For non-SVG image assets, the image width in pixels.<br> | maxLength: 6; example: "100" |

<!-- schema: #/components/schemas/HolderDetails -->
### Schema `HolderDetails`

Pointer: `#/components/schemas/HolderDetails`. Type: object (schema `HolderDetails`).

> Account holder details object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | no | Account holder name in the format Last name/First name or first name last name. | maxLength: 27; example: "Cee Biskit" |
| `address` | object (schema `Address`) | no |  |  |
| `contact` | object (schema `Contact`) | no | Contact object |  |

<!-- schema: #/components/schemas/ValidityDetails -->
### Schema `ValidityDetails`

Pointer: `#/components/schemas/ValidityDetails`. Type: object (schema `ValidityDetails`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `data_valid_until_timestamp` | string | no | Data valid until timestamp.<br>Format: ISO 8601 extended format as one of the following: * YYYY-MM-DDThh:mm:ss[.sss]Z * YYYY-MM-DDThh:mm:ss[.sss]±hh:mm where [.sss] is optional and can be 1 to 3 digits<br> | format: "date-time"; maxLength: 29; example: "2025-12-31T23:59:59Z" |

<!-- schema: #/components/schemas/Address -->
### Schema `Address`

Pointer: `#/components/schemas/Address`. Type: object (schema `Address`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `line1` | string | no | Address line one | maxLength: 64; example: "1313 Mockingbird Lane" |
| `line2` | string | no | Address line two | maxLength: 64; example: "Apt 4B" |
| `country` | string | yes | Billing address country - ISO-3166-1 3-letter code.<br> | maxLength: 3; example: "USA" |
| `country_subdivision` | string | no | Country subdivision such as state or sultanate | maxLength: 12; example: "CA" |
| `city` | string | no | Billing address city | maxLength: 32; example: "San Francisco" |
| `postal_code` | string | no | Billing address postal code, such as zip code in the United States. | maxLength: 16; example: "8675309" |

<!-- schema: #/components/schemas/Contact -->
### Schema `Contact`

Pointer: `#/components/schemas/Contact`. Type: object (schema `Contact`).

> Contact object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `email_address` | string | no | Email address | format: "email"; maxLength: 320; example: "barbie_kew@roadhouse.com" |
| `country_dial_in_code` | string | no | International dial-in prefix code associated with country.<br> | maxLength: 4; example: "1" |
| `phone_number` | string | no | Phone number following `country_dial_in_code` prefix. | maxLength: 20; example: "4155551234" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Tokenization.yaml` | tag `MDES Token Connect [Beta]`: POST /v1/token-connect/push-multiple-accounts, POST /v1/token-connect, GET /v1/token-connect/assets/{assetId} | https://github.com/PismoDevEx/pismo-api-specs | `dd1e776cfe20b0d6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
