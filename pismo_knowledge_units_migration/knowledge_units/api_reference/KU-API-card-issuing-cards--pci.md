---
ku_id: KU-API-card-issuing-cards--pci
title: 'API reference: Card issuing - Cards — PCI'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Cards.yaml
  sha256: 687df76f123e41a762721ae0b3fe344c701d22f47bdd929d033b1ad2d14ca406
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
- put-v2-card-password
- get-v1-pin-as-pinblock
- put-v1-update-pin-from-pinblock
- post-v2-card-search-by-pan
- post-v1-card-search-by-pan
- get-v2-card-info
- get-v2-card-password
- post-v1-append-update-pin-script
- post-v1-append-scripts
- post-v1-sync-offline-pin
- post-v3-card-search-by-pan
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-card-reissuing
- KU-CARD-card-scripts
- KU-CARD-cards-overview-1
- KU-EVT-cards-data-events
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — PCI

**KU ID:** `KU-API-card-issuing-cards--pci` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 11 operation(s) tagged `PCI` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Card PCI/sensitive information endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `PUT /pcicards/v2/pcicards/card/{cardId}` | `put-v2-card-password` | Change card password | no |
| `GET /pcicards/v1/pcicards/{cardId}/pinblock` | `get-v1-pin-as-pinblock` | Get PIN as PINblock | no |
| `PUT /pcicards/v1/pcicards/{cardId}/pinblock` | `put-v1-update-pin-from-pinblock` | Update PIN from PINblock | no |
| `POST /pcicards/v2/pcicards/cards/search` | `post-v2-card-search-by-pan` | Get card info with encrypted PAN | no |
| `POST /pcicards/v1/pcicards/cards/search` | `post-v1-card-search-by-pan` | Get card info with PAN | no |
| `GET /pcicards/v2/pcicards/info/{cardId}` | `get-v2-card-info` | Get card PCI information | no |
| `GET /pcicards/v2/pcicards/password/{cardId}` | `get-v2-card-password` | Get card password | no |
| `POST /pcicards/v1/pcicards/{cardId}/scripts/pin-update` | `post-v1-append-update-pin-script` | Append update PIN script | no |
| `POST /pcicards/v1/pcicards/{cardId}/scripts` | `post-v1-append-scripts` | Append issuer script | no |
| `POST /pcicards/v1/pcicards/{cardId}/scripts/sync-offline-pin` | `post-v1-sync-offline-pin` | Synchronize offline PIN | no |
| `POST /v3/pcicards/cards/search` | `post-v3-card-search-by-pan` | Get card info with encrypted PAN V3 [beta] | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/pcicards/v2/pcicards/card/{cardId} operationId=put-v2-card-password -->
### `PUT /pcicards/v2/pcicards/card/{cardId}` — Change card password

- **operationId:** `put-v2-card-password`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `PCI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a card's password (PIN).
>
> **Note**: This does not change the password recorded on an embossed card's chip. If the card is configured for offline password verification, you need to change the password on the physical card. To do that, you can use a [card script](doc:card-scripts).
>
> This endpoint generates a [Card password changed](https://developers.pismo.io/events/docs/cards-update-password-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `UpdateCardPCI`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pin` | string (schema `PIN2`) | yes | New card Primary Identification Number (PIN)- 4 or 6 digits. | minLength: 4; maxLength: 6; example: "1234" |
| `sync_offline_pin` | boolean (schema `SyncOfflinePin`) | no | Synchronize the offline PIN with the current online PIN value?<br><br>If `true`, the platform generates a script with the new online PIN, sends the script in the response to the next authorization made with a chip (contact), and generates the [Card issuer script notification received](https://developers.pismo.io/events/docs/cards-issuer-script-1) event. <br> <br>Default is `false`.<br> | default: false; example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Response for Update password request | `application/json`: string (schema `CardUpdateResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

_No fields declared in the schema._


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-update-password-1` | https://developers.pismo.io/events/docs/cards-update-password-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;401;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-card-reissuing`, `KU-CARD-cards-overview-1`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/pcicards/v1/pcicards/{cardId}/pinblock operationId=get-v1-pin-as-pinblock -->
### `GET /pcicards/v1/pcicards/{cardId}/pinblock` — Get PIN as PINblock

- **operationId:** `get-v1-pin-as-pinblock`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `PCI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the card PIN (Personal Identification Number) as a PINblock. PINblocks are 64-bit strings that encode a PIN ready for encryption and secure transmission in banking networks.
>
> For more information, refer to the [PIN/PINBlock](doc:pinpinblock-tutorial) tutorial. 
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `key-id` | query | yes | string | A Zone PIN Key (ZPK) identifier. The ZPK is a data encrypting or decrypting key for PIN transfer between parties. For example, between issuers and processors or acquirers and networks or networks and processors, and so on.<br><br>In a sandbox environment, a fixed ZPK is used:<br><br>   key_id: 7d14ca2e-1057-11ee-8cee-060f666de710<br><br>   HSM key: 0404F2543B1C6E70AB61586E1304B6A7<br><br>For production, open a Jira ticket with type = **Configuration**. Request you need the key to use endpoints with PIN management such as PINBLOCK.<br> | example: "32a147ec-b2d9-4b0d-8c5b-557e6cf41e0e" |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Get card PIN as PINBlock success object | `application/json`: object (schema `GetPinAsPinblockResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 409 | Card PIN must not be null |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | integer | no | Pismo card ID |  |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID | example: 7654776 |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation ID is used to link related API requests and events. For example, if a user makes an authorization request with 10 installments, this generates 1 authorization event and 10 transaction events all containing the same correlation ID. The correlation ID can help the Pismo engineering team track everything related to a call. If this field isn't passed, one is generated. <br> | example: "3b56dbec-e509-9550-8c8c-ae5ab081e4d5" |
| `pinblock` | string (schema `PinBlock`) | no | PINBlocks are 64-bit strings that encode a PIN ready for encryption and secure transmission in banking networks. It contains both the PIN and additional data needed to encrypt it for transmission. The PIN block is typically encrypted using a secure cryptographic algorithm to prevent unauthorized access or tampering during transmission. <br> |  |
| `pan` | string (schema `PrimaryAccountNumber`) | no | Card's Primary Account Number (PAN) | example: "123456******789" |
| `key_id` | string | no | Generated key ID. <br><br>A Zone PIN Key (ZPK) identifier. The ZPK is a data encrypting or decrypting key for PIN transfer between parties. Ffor example, between issuers and processors or acquirers and networks or networks and processors, and so on.<br><br>In a sandbox environment, a fixed ZPK is used:<br><br>   key_id: 7d14ca2e-1057-11ee-8cee-060f666de710<br><br>   HSM key: 0404F2543B1C6E70AB61586E1304B6A7<br><br>For production, open a Jira ticket with type = **Configuration**. Request you need the key to use endpoints with PIN management such as PINBLOCK.<br> | example: "32a147ec-b2d9-4b0d-8c5b-557e6cf41e0e" |
| `password_updated` | boolean (schema `PasswordUpdated`) | no | Has password been updated? |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-cards-overview-1`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/pcicards/v1/pcicards/{cardId}/pinblock operationId=put-v1-update-pin-from-pinblock -->
### `PUT /pcicards/v1/pcicards/{cardId}/pinblock` — Update PIN from PINblock

- **operationId:** `put-v1-update-pin-from-pinblock`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `PCI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the card PIN (Personal Identification Number) from its PINBlock.  PINlBocks are 64-bit strings that encode a PIN ready for encryption and secure transmission in banking networks. 
>
> For more information, refer to the [PIN/PINBlock](doc:pinpinblock-tutorial) tutorial.
>
> **Note**: This does not change the password recorded on an embossed card's chip. If the card is configured for offline password verification, you need to change the password on the physical card. To do that, you can use a [card script](doc:card-scripts).
>
> This endpoint generates a [Card password changed](https://developers.pismo.io/events/docs/cards-update-password-1) event.
>
> **Notes:** 
>
>  * This endpoint requires an account token - an access token encoded with a Pismo account ID. 
>
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Request body

Required: yes

> Request body*

**Content type `application/json`** — schema: object (schema `UpdatePinFromPinblockBody`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pinblock` | string | no | PINBlock to update |  |
| `key_id` | string | no | ID of key used to generate the PINBlock. <br><br>A Zone PIN Key (ZPK) identifier. The ZPK is a data encrypting or decrypting key for PIN transfer between parties. For example, between issuers and processors or acquirers and networks or networks and processors, and so on.<br><br>In a sandbox environment, a fixed ZPK is used:<br><br>   key_id: `7d14ca2e-1057-11ee-8cee-060f666de710`<br><br>   HSM key: `0404F2543B1C6E70AB61586E1304B6A7`<br><br>For production, open a Jira ticket with type = **Configuration**. Request you need the key to use endpoints with PIN management such as PINBLOCK.<br> | example: "32a147ec-b2d9-4b0d-8c5b-557e6cf41e0e" |
| `sync_offline_pin` | boolean (schema `SyncOfflinePin`) | no | Synchronize the offline PIN with the current online PIN value?<br><br>If `true`, the platform generates a script with the new online PIN, sends the script in the response to the next authorization made with a chip (contact), and generates the [Card issuer script notification received](https://developers.pismo.io/events/docs/cards-issuer-script-1) event. <br> <br>Default is `false`.<br> | default: false; example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-update-password-1` | https://developers.pismo.io/events/docs/cards-update-password-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;401;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-cards-overview-1`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/pcicards/v2/pcicards/cards/search operationId=post-v2-card-search-by-pan -->
### `POST /pcicards/v2/pcicards/cards/search` — Get card info with encrypted PAN

- **operationId:** `post-v2-card-search-by-pan`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `PCI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get card information - card ID, account ID, customer ID - using a card's encrypted PAN (Primary Account Number). To set up encryption for this endpoint, contact your Pismo representative. Alternatively, to send the PAN as clear text, call the [Get card info with PAN](ref:post-v1-card-search-by-pan) endpoint.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

> Request body*

**Content type `application/json`** — schema: object (schema `SearchCardV2RequestBody`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pan` | string (schema `PANencrypted`) | no | Primary Account Number (PAN) encrypted with AES/GCM/NoPadding algorithm. The ciphertext (PAN encryption result) is **REQUIRED** to be base64 encoded.<br> | example: "/5yGTkBSoqGY+Ug5yJuHUSGk54VRMNoY0G5Ni2HSa64=" |
| `iv` | string (schema `InitializationVector`) | no | Array initialization vector, used as a initial state for the AES algorithm. This field is used on the requester side to encrypt the PAN. It must be an random array of 16 bytes of length encoded as base64<br> | example: "ZZ3cUcotvQeaGciyLZb1wA==" |
| `key_id` | string (schema `KeyID`) | no | Key ID used for encryption. To obtain the `key_id`, the sender will generate a symmetric key (AES), encrypt this key with an asymmetric key (public_key) and send it via secure email to the security team. <br><br>To obtain the asymmetric key, you must open a Configuration item for the Cards squad. After the Pismo security team registers the symmetric key, the `key_id` is shared with the issuer.<br> | example: "5c09cda4-8153-11ed-a1eb-0242ac120002" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response for find card success | `application/json`: object (schema `SearchCardResponse`) |
| 401 | Access token is missing or invalid |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | integer | no | Card ID |  |
| `account_id` | number | no | Account ID |  |
| `customer_id` | integer (schema `CustomerID`) | no | Pismo customer ID | example: 765476676 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/pcicards/v1/pcicards/cards/search operationId=post-v1-card-search-by-pan -->
### `POST /pcicards/v1/pcicards/cards/search` — Get card info with PAN

- **operationId:** `post-v1-card-search-by-pan`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `PCI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get card info - account ID, customer ID and card ID - with the card's unencrypted PAN (Primary Account Number). If you are not comfortable passing a clear text PAN, you can call the [Get card info with encrypted PAN](ref:post-v2-card-search-by-pan) endpoint. Doing this requires you contact Pismo to set up encryption using public and private keys.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `SearchCard`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pan` | string (schema `PrimaryAccountNumber`) | no | Card's Primary Account Number (PAN) | example: "123456******789" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Get card information response | `application/json`: object (schema `SearchCardResponse`) |
| 401 | Access token is missing or invalid |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | integer | no | Card ID |  |
| `account_id` | number | no | Account ID |  |
| `customer_id` | integer (schema `CustomerID`) | no | Pismo customer ID | example: 765476676 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/pcicards/v2/pcicards/info/{cardId} operationId=get-v2-card-info -->
### `GET /pcicards/v2/pcicards/info/{cardId}` — Get card PCI information

- **operationId:** `get-v2-card-info`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `PCI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets sensitive PCI (Payment Card Industry) card data.
>
> Calling this endpoint could change the status of `TEMPORARY` cards. For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards) in the [Cards management](https://developers.pismo.io/pismo-docs/docs/cards-overview-1) guide.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | PCI sensitive card data response | `application/json`: object (schema `CardPCIInfoResponse`) |
| 401 | Access token is missing or invalid |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `card_id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `service_code` | string (schema `ServiceCode`) | no | A 3 digit value, not to be confused with the CVV. Each number in the service code has a well-defined meaning, known to the card networks and other components of the interchange networks. The service code's purpose is to tell merchant terminals and acquiring networks about usage restrictions the issuer has placed on the card.<br><br>If passed, a new random service code value is not generated, and the passed value is used instead.<br> | minLength: 3; maxLength: 3 |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation ID is used to link related API requests and events. For example, if a user makes an authorization request with 10 installments, this generates 1 authorization event and 10 transaction events all containing the same correlation ID. The correlation ID can help the Pismo engineering team track everything related to a call. If this field isn't passed, one is generated. <br> | example: "3b56dbec-e509-9550-8c8c-ae5ab081e4d5" |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID | example: 7654776 |
| `type` | string (schema `CardType`) | no | Card type enum:<br> * `PLASTIC` - Physical card - plastic or metal.<br> * `VIRTUAL` - Digital card with fixed PAN and dynamic CVV.<br> * `TEMPORARY` - Virtual card with a fixed PAN and CVV meant for short-term use, typically 24 hours. For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards) in the Cards management guide.<br> * `RECURRING` - Virtual card with a fixed PAN and CVV originally meant for use with recurring subscriptions. This type is being **DEPRECATED** and it is recommended you use `VIRTUAL` instead. <br> | enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: "VIRTUAL" |
| `printed_name` | string (schema `PrintedName`) | no | Printed/embossed card name.<br><br>Currently, you have 3 ways to populate this field:<br>   <br>   1. During account creation via the `application.applicant.personal.social_name` field.<br>   2. During account creation via the `application.applicant.personal.name` field when the field in #1 is not set.<br>   3. Passing the `printed_name` field during card creation, updating a card, or when reissuing a card. This takes priority over #1 and #2.<br><br>No letters with accents, numbers, or special characters - only letters (a-z\|A-Z) and space, as specified in the <a href="https://emvlab.org/emvtags/show/t5F20/" target="_blank">ISO EMV tag 5F20</a> for cardholder name.<br><br>**REQUIRED** for an `UNNUMBERED` card (Card created without PIN or PAN that issuer defines at some point in the future.)<br> | minLength: 2; maxLength: 26 |
| `valid_until` | string (schema `ValidUntil`) | no | Card validation date in UTC time (format:yyyy-MM-ddThh:mm:ssZ). For `TEMPORARY` virtual cards, which have a limited time frame, typically 24 hours (default), or according to the program parameter for this, which is why the date/time here is more granular than `expiration_date`.  <br><br>For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards).<br> | example: "2021-07-03T17:23:18Z" |
| `expiration_date` | string (schema `ExpirationDate`) | no | Card expiration date (format = yymm). If passed, the card expiration date is not calculated using the "Card expiration (# of months)" program parameter.<br> | example: "2803" |
| `card_number` | string (schema `PAN`) | no | Card embossed Primary Account Number (PAN).<br><br>**Note:** The PAN shown here is a fictional example used for documentation purposes. It does not represent a real card number.<br> | example: "123456******7890" |
| `issuing_date` | string (schema `IssuingDate`) | no | Date/time when card was issued in RFC3339 format, i.e., 2019-07-03T17:23:18Z | example: "2019-07-03T17:23:18Z" |
| `cvv` | string (schema `CVV`) | no | <br>Card Verification Value 2 (CVV2, also known as CVC2), a 3-digit security code contained in a card's signature strip, used for cardholder verification.<br> | example: "678" |
| `cvv_next_rotation_date` | string (schema `cvvNextRotationDate`) | no | For virtual cards. Card CVV2/CVC2 next rotation in UTC date/time - format:yyyy-MM-ddThh:mm:ssZ<br> | format: "date-time" |
| `cvv_rotation_interval_hours` | integer (schema `cvvRotationInterval`) | no | <b>REQUIRED</b> for a virtual card.  Virtual card CVV rotation interval in hours.<br><br>To force a rotation manually, call the [Rotate virtual card CVV](ref:post-v2-reset-cvv) endpoint.<br><br>If `0` is passed, the CVV will **NOT** be rotated.<br> | minimum: 1; maximum: 4320 |
| `password_updated` | boolean (schema `PasswordUpdated`) | no | Has password been updated? |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-cards-overview-1`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/pcicards/v2/pcicards/password/{cardId} operationId=get-v2-card-password -->
### `GET /pcicards/v2/pcicards/password/{cardId}` — Get card password

- **operationId:** `get-v2-card-password`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `PCI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets card Personal Identification Number (PIN) used for authenticating purchases with Pinpads.
>
> **Notes:** 
>
>  * This endpoint requires an account token - an access token encoded with a Pismo account ID. 
>
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response for get password request | `application/json`: object (schema `GetPasswordResponse`) |
| 401 | Access token is missing or invalid |  |
| 404 | The specified resource was not found |  |
| 409 | Card PIN must not be null |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `card_id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation ID is used to link related API requests and events. For example, if a user makes an authorization request with 10 installments, this generates 1 authorization event and 10 transaction events all containing the same correlation ID. The correlation ID can help the Pismo engineering team track everything related to a call. If this field isn't passed, one is generated. <br> | example: "3b56dbec-e509-9550-8c8c-ae5ab081e4d5" |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID | example: 7654776 |
| `pin` | string (schema `PIN`) | no | Card Primary Identification Number (PIN) - 4 or 6 digits | minLength: 4; maxLength: 6; example: "7654" |
| `pan` | string (schema `PANencrypted`) | no | Primary Account Number (PAN) encrypted with AES/GCM/NoPadding algorithm. The ciphertext (PAN encryption result) is **REQUIRED** to be base64 encoded.<br> | example: "/5yGTkBSoqGY+Ug5yJuHUSGk54VRMNoY0G5Ni2HSa64=" |
| `password_updated` | boolean (schema `PasswordUpdated`) | no | Has password been updated? |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;404;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-card-reissuing`, `KU-CARD-cards-overview-1`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/pcicards/v1/pcicards/{cardId}/scripts/pin-update operationId=post-v1-append-update-pin-script -->
### `POST /pcicards/v1/pcicards/{cardId}/scripts/pin-update` — Append update PIN script

- **operationId:** `post-v1-append-update-pin-script`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `PCI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Append issuer script to update the card PIN that will be applied at the next authorization.
>
> You must work with Pismo to pre-register a script and get its script ID. For information on generating a PINBlock and key ID, refer to the [PIN/PINBlock tutorial](doc:pinpinblock-tutorial) guide.
>
> For more information, refer to the [Card scripts](doc:card-scripts) guide.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io/ environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `x-account-id` | header | yes | string | Account ID | example: "8675309" |

#### Request body

Required: yes

> Request body*

**Content type `application/json`** — schema: object (schema `AppendUpdatePinIssuerScriptBody`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `script_id` | string | yes | Issuer script ID. Pismo configures a script according to your needs. Contact your Pismo representative to create a script. Once created, Pismo gives you the script ID. <br> | example: "11a10bff-830b-4649-9660-1a01a5e1c192" |
| `pin_block` | string | no | New PIN encrypted as a PINblock using the Zone Pin Key (ZPK) `key_id` field that was pre-registered. | example: "86FA0CED8BDD40D1" |
| `key_id` | string (schema `KeyID2`) | no | Generated key ID. <br><br>A Zone PIN Key (ZPK) identifier. The ZPK is a data encrypting or decrypting key for PIN transfer between parties. Ffor example, between issuers and processors or acquirers and networks or networks and processors, and so on.<br><br>In a sandbox environment, a fixed ZPK is used:<br><br>  key_id: 7d14ca2e-1057-11ee-8cee-060f666de710<br><br>  HSM key: 0404F2543B1C6E70AB61586E1304B6A7<br><br>For production, open a Jira ticket with type = **Configuration**. Request you need the key to use endpoints with PIN management such as PINBLOCK.<br> | example: "32a147ec-b2d9-4b0d-8c5b-557e6cf41e0e" |
| `pin` | string (schema `PIN2`) | no | New card Primary Identification Number (PIN)- 4 or 6 digits. | minLength: 4; maxLength: 6; example: "1234" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response for success append issuer scripts | `application/json`: object (schema `AppendIssuerScriptResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_script_id` | string | no | ID of script added to card. | example: "11a10bff-830b-4649-9660-1a01a5e1c192" |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `card_id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID | example: 7654776 |
| `script_id` | string (schema `ScriptID`) | no | Issuer script ID. Pismo configures a script according to your needs. Contact your Pismo representative to create a script. Once created, Pismo gives you the script ID. <br> | example: "11a10bff-830b-4649-9660-1a01a5e1c192" |
| `created_at` | string | no | Card script creation date, format = yyyy-MM-dd'T'HH:mm:ss.SSS" | example: "2021-10-16T14:09:04.549" |
| `applied` | boolean | no | Has script been applied? | example: false |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-scripts`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/pcicards/v1/pcicards/{cardId}/scripts operationId=post-v1-append-scripts -->
### `POST /pcicards/v1/pcicards/{cardId}/scripts` — Append issuer script

- **operationId:** `post-v1-append-scripts`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `PCI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Append issuer script to card that will be applied at the next authorization.
> You must work with Pismo to pre-register a script and get its script ID.
>
> For more information, refer to the [Card scripts](doc:card-scripts) guide.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `x-account-id` | header | yes | string | Account ID | example: "8675309" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `AppendIssuerScriptBody`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `script_id` | string | yes | Issuer script ID. Pismo configures a script according to your needs. Contact your Pismo representative to create a script. Once created, Pismo gives you the script ID. <br> | example: "11a10bff-830b-4649-9660-1a01a5e1c192" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response for success append issuer scripts | `application/json`: object (schema `AppendIssuerScriptResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_script_id` | string | no | ID of script added to card. | example: "11a10bff-830b-4649-9660-1a01a5e1c192" |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `card_id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID | example: 7654776 |
| `script_id` | string (schema `ScriptID`) | no | Issuer script ID. Pismo configures a script according to your needs. Contact your Pismo representative to create a script. Once created, Pismo gives you the script ID. <br> | example: "11a10bff-830b-4649-9660-1a01a5e1c192" |
| `created_at` | string | no | Card script creation date, format = yyyy-MM-dd'T'HH:mm:ss.SSS" | example: "2021-10-16T14:09:04.549" |
| `applied` | boolean | no | Has script been applied? | example: false |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/pcicards/v1/pcicards/{cardId}/scripts/sync-offline-pin operationId=post-v1-sync-offline-pin -->
### `POST /pcicards/v1/pcicards/{cardId}/scripts/sync-offline-pin` — Synchronize offline PIN

- **operationId:** `post-v1-sync-offline-pin`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `PCI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Synchronize the offline PIN with the current online PIN value. The platform generates a script with the current online PIN, sends the script in response to the next authorization made with a chip (contact), and generates the [Card issuer script notification received](https://developers.pismo.io/events/docs/cards-issuer-script-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Request body

Required: no

> Request body should be empty

**Content type `application/json`** — schema: not declared


#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-issuer-script-1` | https://developers.pismo.io/events/docs/cards-issuer-script-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/v3/pcicards/cards/search operationId=post-v3-card-search-by-pan -->
### `POST /v3/pcicards/cards/search` — Get card info with encrypted PAN V3 [beta]

- **operationId:** `post-v3-card-search-by-pan`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `PCI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get card information - card ID, account ID, customer ID - using a card's encrypted PAN (Primary Account Number). To set up encryption for this endpoint, contact your Pismo representative. Alternatively, to send the PAN as clear text, call the [Get card info with PAN](ref:post-v1-card-search-by-pan) endpoint.
>
> This endpoint uses AES256 with the GCM mode. AES-256 GCM is an authenticated encryption mode that uses the Advanced Encryption Standard (AES) with a 256-bit key in Galois/Counter Mode (GCM) to provide both confidentiality and integrity for data. In AES, an initialization vector (IV) is a fixed-size, non-secret randomized number used alongside the secret key to jumpstart the encryption process. The caller is responsible for generating the IV.  The Additional Authenticated Data (AAD) parameter must be the organization/tenant ID. AAD, in AES-GCM, is unencrypted data that is authenticated alongside the ciphertext to ensure the message's integrity and authenticity.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `SearchCardV2RequestBody2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pan` | string (schema `PANencrypted`) | no | Primary Account Number (PAN) encrypted with AES/GCM/NoPadding algorithm. The ciphertext (PAN encryption result) is **REQUIRED** to be base64 encoded.<br> | example: "/5yGTkBSoqGY+Ug5yJuHUSGk54VRMNoY0G5Ni2HSa64=" |
| `iv` | string (schema `InitializationVector`) | no | Array initialization vector, used as a initial state for the AES algorithm. This field is used on the requester side to encrypt the PAN. It must be an random array of 16 bytes of length encoded as base64<br> | example: "ZZ3cUcotvQeaGciyLZb1wA==" |
| `key_id` | string (schema `KeyID`) | no | Key ID used for encryption. To obtain the `key_id`, the sender will generate a symmetric key (AES), encrypt this key with an asymmetric key (public_key) and send it via secure email to the security team. <br><br>To obtain the asymmetric key, you must open a Configuration item for the Cards squad. After the Pismo security team registers the symmetric key, the `key_id` is shared with the issuer.<br> | example: "5c09cda4-8153-11ed-a1eb-0242ac120002" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response for find card success | `application/json`: object (schema `SearchCardResponse`) |
| 401 | Access token is missing or invalid |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | integer | no | Card ID |  |
| `account_id` | number | no | Account ID |  |
| `customer_id` | integer (schema `CustomerID`) | no | Pismo customer ID | example: 765476676 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.


## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Cards.yaml` | tag `PCI`: PUT /pcicards/v2/pcicards/card/{cardId}, GET /pcicards/v1/pcicards/{cardId}/pinblock, PUT /pcicards/v1/pcicards/{cardId}/pinblock, POST /pcicards/v2/pcicards/cards/search, POST /pcicards/v1/pcicards/cards/search, GET /pcicards/v2/pcicards/info/{cardId}, GET /pcicards/v2/pcicards/password/{cardId}, POST /pcicards/v1/pcicards/{cardId}/scripts/pin-update, POST /pcicards/v1/pcicards/{cardId}/scripts, POST /pcicards/v1/pcicards/{cardId}/scripts/sync-offline-pin, POST /v3/pcicards/cards/search | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-card-reissuing` — Card reissuing
- `KU-CARD-card-scripts` — Card scripts
- `KU-CARD-cards-overview-1` — Cards management
- `KU-EVT-cards-data-events` — Card issuing - Cards
- `KU-EVT-catalogue-cards` — Event catalogue: cards
