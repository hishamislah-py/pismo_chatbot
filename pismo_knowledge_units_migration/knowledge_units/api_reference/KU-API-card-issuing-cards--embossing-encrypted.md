---
ku_id: KU-API-card-issuing-cards--embossing-encrypted
title: 'API reference: Card issuing - Cards — Embossing encrypted'
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
- post-generate-embossing
- post-generate-embossing-no-iv
- post-generate-embossing-encrypted-noname
- post-generate-embossing-noname
related_kus:
- KU-CARD-physical-card-embossing
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Embossing encrypted

**KU ID:** `KU-API-card-issuing-cards--embossing-encrypted` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Embossing encrypted` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Embossing encrypted data endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /embossing/v1/cards/generate-embossing` | `post-generate-embossing` | Get nominal encrypted card data for embossing | no |
| `POST /embossing/v2/cards/generate-embossing` | `post-generate-embossing-no-iv` | Get nominal encrypted card data for embossing V2 [beta] | no |
| `POST /embossing/v1/cards/generate-embossing/noname` | `post-generate-embossing-encrypted-noname` | Get noname encrypted card data for embossing [beta] | no |
| `POST /embossing/v2/cards/generate-embossing/noname` | `post-generate-embossing-noname` | Get noname encrypted card data for embossing V2 [beta] | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/embossing/v1/cards/generate-embossing operationId=post-generate-embossing -->
### `POST /embossing/v1/cards/generate-embossing` — Get nominal encrypted card data for embossing

- **operationId:** `post-generate-embossing`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing encrypted`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get encrypted card embossing data. This is for issuers doing their own embossing and require a card's data, which needs to be encrypted as per regulations.
>
> **To use this endpoint:**
>   * Open a [Jira ticket](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket) with type = **Settings** and ask to use on-demand embossing.
>   * Generate and register a symmetric key with Pismo: open a Jira ticket with type = **Settings** and request an asymmetric key (RSA 2048 PKCS1) to send the symmetric key.
>
> While the return values are shown as JSON, they are encrypted and not returned as clear text.
>
> The endpoint generates a [Card embossing notification received](https://developers.pismo.io/events/docs/cards-embossing-1) event.
>
> **Notes:** 
>
>  * This endpoint requires an account token - an access token encoded with a Pismo account ID. 
>
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `GetEncryptedCardDataRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | object (schema `CardID`) | yes | Pismo card ID object |  |
| `iv` | string (schema `InitialVector`) | yes | Initial vector (IV) value, needs to be 16 bytes and hexadecimal. An IV is a random or pseudo-random value used as the starting point for an encryption algorithm to generate a unique cipher text for each message. The IV is used in combination with a secret key (`key_id`) to ensure that the same message encrypted with the same key does not result in the same cipher text.<br> |  |
| `key_id` | string (schema `KeyID3`) | yes | Encryption key ID to embossing, used in conjunction with the initial vector value.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Encrypted card embossing data (shown here as unencrypted JSON) | `application/json`: object (schema `EncryptedCardContent`) |
| 400 | Bad Request | `application/json`: object |
| 401 | Access token is missing or invalid |  |
| 404 | Not found | `application/json`: object |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `card_id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID | example: 7654776 |
| `customer_id` | integer (schema `CustomerID`) | no | Pismo customer ID | example: 765476676 |
| `program_id` | integer (schema `ProgramID`) | no | Pismo program ID | example: 7654 |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `encrypted_card_data` | string (schema `EncryptedCardData`) | no | Encrypted card data<br><br>When decrypted, this field will have the following JSON:  <br><br>* **`card_number`**<br>  type: string<br>  description: Primary Account Number (PAN)<br><br>* **`printed_name`** <br>  type: string <br>  description: Printed/embossed card holder name.<br><br>* **`expiration_date`**<br>  type: string<br>  description: Card expiration date (format:yymm)<br><br>* **`pinblock`**  <br>  type: string<br>  description: <br>    PINBlocks are 64-bit strings that encode a PIN ready for encryption and secure transmission in banking networks. PIN block ISO 9564-1 format 0. It contains both the PIN and additional data needed to encrypt it for transmission. The PIN block is typically encrypted using a secure cryptographic algorithm to prevent unauthorized access or tampering during transmission. <br><br>* **`cvv`** <br>  type: string <br>  description: \|<br>    Card Verification Value (CVV) is a three- or four-digit security code that is printed on payment cards to help verify that the cardholder is the one making a transaction. <br><br>* **`cvv2`**: <br>  type: string <br>  description: \|<br>    Card Verification Value 2 (CVV2) is also a three-digit code printed on the back of the card. While CVV and CVV2 are both three-digit codes, CVV is numeric only, while CVV2 can contain letters and numbers. <br><br>* **`service_code_cvv1`**:  <br>  type: string<br>  description: \|<br>   Service code for the card verification value 1 (CVV1) is a three-digit code that is encoded on the magnetic stripe of a payment card  and is used to verify the card's authenticity during a transaction. It is different from the CVV2 or CVC2 codes, which are three- or four-digit codes printed on the back of the card and used for online or phone transactions. <br><br>* **`service_code_cvv2`**:  <br>  type: string<br>  description: \|<br>    Service code for the card verification value 2 (CVV2) is a three- or four-digit security code. It is a security feature that helps verify that the card is physically present during card-not-present transactions. It is not encoded on the card's magnetic stripe.<br><br>* **`service_code_icvv`**:  <br>  type: string<br>  description: \|<br>     Service code for the ICVV (Issuer Controlled Card Verification Value) is a dynamic security code the issuing bank generates generated and is used to verify the payment card authenticity during transactions.<br><br>* **`track2_chip`**:  <br>  type: string<br>  description: \|<br>    Analogous to the `track2_magnetic_stripe`, but instead of being recorded on the magnetic stripe it is stored inside the chip. Instead of the CVV2, which is included on the magnetic stripe's track 2, the chip (and therefore this field) contains the iCVV. The same applies for the service code: on the magnetic track2 it `service_code_cvv2`, but here it is `service_code_icvv`.<br><br>* **`track1_magnetic_stripe`**:  <br>  type: string<br>  description: \|<br>  Track 1 of the card's magnetic stripe located on the back of the card and is read by card readers and point-of-sale (POS) terminals. It contains several fields of information, including the cardholder's name, account number, expiration date, and other identifying information.<br><br>* **`track2_magnetic_stripe`**:  <br>  type: string<br>  description: \|<br>    Track 2 of the magnetic stripe is similar to track 1 magnetic stripes but contains less information and include only the cardholder's account number, expiration date, and a discretionary data field.<br> |  |

200 Example `example`:

```json
{
  "org_id": "TN-5aea4104-7994-46d5-83d6-a55cxxxxxxxx",
  "card_id": 0,
  "correlation_id": "9f46663d-34dc-9e37-a89a-a1d6ef56039a",
  "password_updated": true,
  "account_id": 0,
  "card_number": "123456******7890",
  "program_id": 0,
  "printed_name": "Some person",
  "expiration_date": "2805",
  "customer_id": 0,
  "cvv": "000",
  "cvv2": "000",
  "icvv": "000",
  "track1_magnetic_stripe": "B65...^NOT/REAL...00000?",
  "track1_chip": "B650...NOT/REAL...0000000?",
  "track2_chip": "B650...NOT/REAL...0000000?",
  "track2_magnetic_stripe": "B65...^NOT/REAL...00000?",
  "pinblock": "000000000000",
  "service_code_cvv1": "000",
  "service_code_cvv2": "000",
  "service_code_icvv": "000"
}
```

##### Response 404

404 Example `example-bad-request`:

```json
{
  "message": "Not found configurations ondemand to org",
  "error": "Not_found",
  "status": 404
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-embossing-1` | https://developers.pismo.io/events/docs/cards-embossing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/embossing/v2/cards/generate-embossing operationId=post-generate-embossing-no-iv -->
### `POST /embossing/v2/cards/generate-embossing` — Get nominal encrypted card data for embossing V2 [beta]

- **operationId:** `post-generate-embossing-no-iv`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing encrypted`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get encrypted card embossing data.
>
> Issuers who do their own embossing can use this endpoint to get a card's data, which needs to be encrypted as per regulations.
>
> This endpoint uses AES256 with the GCM mode. AES-256 GCM is an authenticated encryption mode that uses the Advanced Encryption Standard (AES) with a 256-bit key in Galois/Counter Mode (GCM) to provide both confidentiality and integrity for data. In AES, an initialization vector (IV) is a fixed-size, non-secret randomized number used alongside the secret key to jumpstart the encryption process. The caller is responsible for generating the IV.  The Additional Authenticated Data (AAD) parameter used is the organization/tenant ID. AAD, in AES-GCM, is unencrypted data that is authenticated alongside the ciphertext to ensure the message's integrity and authenticity.
>
> **To use this endpoint:**
>   * Open a [Jira ticket](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket) with type = **Settings** and ask to use on-demand embossing.
>   * Generate and register a symmetric key with Pismo: open a Jira ticket with type = **Settings** and request an asymmetric key (RSA 2048 PKCS1) to send the symmetric key.
>
> While the return values are shown as JSON, they are encrypted and not returned as clear text.
>
> The endpoint generates a [Card embossing notification received](https://developers.pismo.io/events/docs/cards-embossing-1) event.
>
> **Notes:** 
>
>  * This endpoint requires an account token - an access token encoded with a Pismo account ID. 
>
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.
>

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `GetEncryptedCardDataRequest2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | object (schema `CardID`) | yes | Pismo card ID object |  |
| `key_id` | string (schema `KeyID3`) | yes | Encryption key ID to embossing, used in conjunction with the initial vector value.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Encrypted card embossing data (shown here as unencrypted JSON) | `application/json`: object (schema `EncryptedCardContent2`) |
| 400 | Bad Request | `application/json`: object |
| 401 | Access token is missing or invalid |  |
| 404 | Not found | `application/json`: object |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `card_id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID | example: 7654776 |
| `customer_id` | integer (schema `CustomerID`) | no | Pismo customer ID | example: 765476676 |
| `program_id` | integer (schema `ProgramID`) | no | Pismo program ID | example: 7654 |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `iv` | string (schema `InitialVector`) | no | Initial vector (IV) value, needs to be 16 bytes and hexadecimal. An IV is a random or pseudo-random value used as the starting point for an encryption algorithm to generate a unique cipher text for each message. The IV is used in combination with a secret key (`key_id`) to ensure that the same message encrypted with the same key does not result in the same cipher text.<br> |  |
| `encrypted_card_data` | string (schema `EncryptedCardData`) | no | Encrypted card data<br><br>When decrypted, this field will have the following JSON:  <br><br>* **`card_number`**<br>  type: string<br>  description: Primary Account Number (PAN)<br><br>* **`printed_name`** <br>  type: string <br>  description: Printed/embossed card holder name.<br><br>* **`expiration_date`**<br>  type: string<br>  description: Card expiration date (format:yymm)<br><br>* **`pinblock`**  <br>  type: string<br>  description: <br>    PINBlocks are 64-bit strings that encode a PIN ready for encryption and secure transmission in banking networks. PIN block ISO 9564-1 format 0. It contains both the PIN and additional data needed to encrypt it for transmission. The PIN block is typically encrypted using a secure cryptographic algorithm to prevent unauthorized access or tampering during transmission. <br><br>* **`cvv`** <br>  type: string <br>  description: \|<br>    Card Verification Value (CVV) is a three- or four-digit security code that is printed on payment cards to help verify that the cardholder is the one making a transaction. <br><br>* **`cvv2`**: <br>  type: string <br>  description: \|<br>    Card Verification Value 2 (CVV2) is also a three-digit code printed on the back of the card. While CVV and CVV2 are both three-digit codes, CVV is numeric only, while CVV2 can contain letters and numbers. <br><br>* **`service_code_cvv1`**:  <br>  type: string<br>  description: \|<br>   Service code for the card verification value 1 (CVV1) is a three-digit code that is encoded on the magnetic stripe of a payment card  and is used to verify the card's authenticity during a transaction. It is different from the CVV2 or CVC2 codes, which are three- or four-digit codes printed on the back of the card and used for online or phone transactions. <br><br>* **`service_code_cvv2`**:  <br>  type: string<br>  description: \|<br>    Service code for the card verification value 2 (CVV2) is a three- or four-digit security code. It is a security feature that helps verify that the card is physically present during card-not-present transactions. It is not encoded on the card's magnetic stripe.<br><br>* **`service_code_icvv`**:  <br>  type: string<br>  description: \|<br>     Service code for the ICVV (Issuer Controlled Card Verification Value) is a dynamic security code the issuing bank generates generated and is used to verify the payment card authenticity during transactions.<br><br>* **`track2_chip`**:  <br>  type: string<br>  description: \|<br>    Analogous to the `track2_magnetic_stripe`, but instead of being recorded on the magnetic stripe it is stored inside the chip. Instead of the CVV2, which is included on the magnetic stripe's track 2, the chip (and therefore this field) contains the iCVV. The same applies for the service code: on the magnetic track2 it `service_code_cvv2`, but here it is `service_code_icvv`.<br><br>* **`track1_magnetic_stripe`**:  <br>  type: string<br>  description: \|<br>  Track 1 of the card's magnetic stripe located on the back of the card and is read by card readers and point-of-sale (POS) terminals. It contains several fields of information, including the cardholder's name, account number, expiration date, and other identifying information.<br><br>* **`track2_magnetic_stripe`**:  <br>  type: string<br>  description: \|<br>    Track 2 of the magnetic stripe is similar to track 1 magnetic stripes but contains less information and include only the cardholder's account number, expiration date, and a discretionary data field.<br> |  |

200 Example `example`:

```json
{
  "org_id": "TN-5aea4104-7994-46d5-83d6-a55cxxxxxxxx",
  "card_id": 0,
  "correlation_id": "9f46663d-34dc-9e37-a89a-a1d6ef56039a",
  "password_updated": true,
  "account_id": 0,
  "card_number": "123456******7890",
  "program_id": 0,
  "printed_name": "Some person",
  "expiration_date": "2805",
  "customer_id": 0,
  "cvv": "000",
  "cvv2": "000",
  "icvv": "000",
  "track1_magnetic_stripe": "B65...^NOT/REAL...00000?",
  "track1_chip": "B650...NOT/REAL...0000000?",
  "track2_chip": "B650...NOT/REAL...0000000?",
  "track2_magnetic_stripe": "B65...^NOT/REAL...00000?",
  "pinblock": "000000000000000",
  "service_code_cvv1": "000",
  "service_code_cvv2": "000",
  "service_code_icvv": "000"
}
```

##### Response 404

404 Example `example-bad-request`:

```json
{
  "message": "Not found configurations ondemand to org",
  "error": "Not_found",
  "status": 404
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-embossing-1` | https://developers.pismo.io/events/docs/cards-embossing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/embossing/v1/cards/generate-embossing/noname operationId=post-generate-embossing-encrypted-noname -->
### `POST /embossing/v1/cards/generate-embossing/noname` — Get noname encrypted card data for embossing [beta]

- **operationId:** `post-generate-embossing-encrypted-noname`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing encrypted`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get noname encrypted card embossing data. This is for issuers doing their own embossing and require a card's data, which needs to be encrypted as per regulations.
>
> **To use this endpoint:**
>   * Open a [Jira ticket](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket) with type = **Settings** and ask to use on-demand embossing.
>   * Generate and register a symmetric key with Pismo: open a Jira ticket with type = **Settings** and request an asymmetric key (RSA 2048 PKCS1) to send the symmetric key.
>
> While the return values are shown as JSON, they are encrypted and not returned as clear text.
>
> The endpoint generates a [Card embossing notification received](https://developers.pismo.io/events/docs/cards-embossing-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `GetEncryptedCardDataRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | object (schema `CardID`) | yes | Pismo card ID object |  |
| `iv` | string (schema `InitialVector`) | yes | Initial vector (IV) value, needs to be 16 bytes and hexadecimal. An IV is a random or pseudo-random value used as the starting point for an encryption algorithm to generate a unique cipher text for each message. The IV is used in combination with a secret key (`key_id`) to ensure that the same message encrypted with the same key does not result in the same cipher text.<br> |  |
| `key_id` | string (schema `KeyID3`) | yes | Encryption key ID to embossing, used in conjunction with the initial vector value.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Encrypted card embossing data (shown here as unencrypted JSON) | `application/json`: object (schema `EncryptedCardContent`) |
| 400 | Bad Request | `application/json`: object |
| 401 | Access token is missing or invalid |  |
| 404 | Not found | `application/json`: object |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `card_id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID | example: 7654776 |
| `customer_id` | integer (schema `CustomerID`) | no | Pismo customer ID | example: 765476676 |
| `program_id` | integer (schema `ProgramID`) | no | Pismo program ID | example: 7654 |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `encrypted_card_data` | string (schema `EncryptedCardData`) | no | Encrypted card data<br><br>When decrypted, this field will have the following JSON:  <br><br>* **`card_number`**<br>  type: string<br>  description: Primary Account Number (PAN)<br><br>* **`printed_name`** <br>  type: string <br>  description: Printed/embossed card holder name.<br><br>* **`expiration_date`**<br>  type: string<br>  description: Card expiration date (format:yymm)<br><br>* **`pinblock`**  <br>  type: string<br>  description: <br>    PINBlocks are 64-bit strings that encode a PIN ready for encryption and secure transmission in banking networks. PIN block ISO 9564-1 format 0. It contains both the PIN and additional data needed to encrypt it for transmission. The PIN block is typically encrypted using a secure cryptographic algorithm to prevent unauthorized access or tampering during transmission. <br><br>* **`cvv`** <br>  type: string <br>  description: \|<br>    Card Verification Value (CVV) is a three- or four-digit security code that is printed on payment cards to help verify that the cardholder is the one making a transaction. <br><br>* **`cvv2`**: <br>  type: string <br>  description: \|<br>    Card Verification Value 2 (CVV2) is also a three-digit code printed on the back of the card. While CVV and CVV2 are both three-digit codes, CVV is numeric only, while CVV2 can contain letters and numbers. <br><br>* **`service_code_cvv1`**:  <br>  type: string<br>  description: \|<br>   Service code for the card verification value 1 (CVV1) is a three-digit code that is encoded on the magnetic stripe of a payment card  and is used to verify the card's authenticity during a transaction. It is different from the CVV2 or CVC2 codes, which are three- or four-digit codes printed on the back of the card and used for online or phone transactions. <br><br>* **`service_code_cvv2`**:  <br>  type: string<br>  description: \|<br>    Service code for the card verification value 2 (CVV2) is a three- or four-digit security code. It is a security feature that helps verify that the card is physically present during card-not-present transactions. It is not encoded on the card's magnetic stripe.<br><br>* **`service_code_icvv`**:  <br>  type: string<br>  description: \|<br>     Service code for the ICVV (Issuer Controlled Card Verification Value) is a dynamic security code the issuing bank generates generated and is used to verify the payment card authenticity during transactions.<br><br>* **`track2_chip`**:  <br>  type: string<br>  description: \|<br>    Analogous to the `track2_magnetic_stripe`, but instead of being recorded on the magnetic stripe it is stored inside the chip. Instead of the CVV2, which is included on the magnetic stripe's track 2, the chip (and therefore this field) contains the iCVV. The same applies for the service code: on the magnetic track2 it `service_code_cvv2`, but here it is `service_code_icvv`.<br><br>* **`track1_magnetic_stripe`**:  <br>  type: string<br>  description: \|<br>  Track 1 of the card's magnetic stripe located on the back of the card and is read by card readers and point-of-sale (POS) terminals. It contains several fields of information, including the cardholder's name, account number, expiration date, and other identifying information.<br><br>* **`track2_magnetic_stripe`**:  <br>  type: string<br>  description: \|<br>    Track 2 of the magnetic stripe is similar to track 1 magnetic stripes but contains less information and include only the cardholder's account number, expiration date, and a discretionary data field.<br> |  |

200 Example `example`:

```json
{
  "org_id": "TN-5aea4104-7994-46d5-83d6-a55cxxxxxxxx",
  "card_id": 0,
  "correlation_id": "9f46663d-34dc-9e37-a89a-a1d6ef56039a",
  "password_updated": true,
  "account_id": 0,
  "card_number": "123456******7890",
  "program_id": 0,
  "printed_name": "Some person",
  "expiration_date": "2805",
  "customer_id": 0,
  "cvv": "000",
  "cvv2": "000",
  "icvv": "000",
  "track1_magnetic_stripe": "B65...^NOT/REAL...00000?",
  "track1_chip": "B650...NOT/REAL...0000000?",
  "track2_chip": "B650...NOT/REAL...0000000?",
  "track2_magnetic_stripe": "B65...^NOT/REAL...00000?",
  "pinblock": "000000000000000",
  "service_code_cvv1": "000",
  "service_code_cvv2": "000",
  "service_code_icvv": "000"
}
```

##### Response 404

404 Example `example-bad-request`:

```json
{
  "message": "Not found configurations ondemand to org",
  "error": "Not_found",
  "status": 404
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-embossing-1` | https://developers.pismo.io/events/docs/cards-embossing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/embossing/v2/cards/generate-embossing/noname operationId=post-generate-embossing-noname -->
### `POST /embossing/v2/cards/generate-embossing/noname` — Get noname encrypted card data for embossing V2 [beta]

- **operationId:** `post-generate-embossing-noname`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing encrypted`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get noname encrypted card embossing data. 
>
> Issuers who do their own embossing can use this endpoint to get a card's data, which needs to be encrypted as per regulations.
>
> This endpoint uses AES256 with the GCM mode. AES-256 GCM is an authenticated encryption mode that uses the Advanced Encryption Standard (AES) with a 256-bit key in Galois/Counter Mode (GCM) to provide both confidentiality and integrity for data. In AES, an initialization vector (IV) is a fixed-size, non-secret randomized number used alongside the secret key to jumpstart the encryption process. The caller is responsible for generating the IV.  The Additional Authenticated Data (AAD) parameter used is the organization/tenant ID. AAD, in AES-GCM, is unencrypted data that is authenticated alongside the ciphertext to ensure the message's integrity and authenticity.
>
> **To use this endpoint:**
>   * Open a [Jira ticket](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket) with type = **Settings** and ask to use on-demand embossing.
>   * Generate and register a symmetric key with Pismo: open a Jira ticket with type = **Settings** and request an asymmetric key (RSA 2048 PKCS1) to send the symmetric key.
>
> While the return values are shown as JSON, they are encrypted and not returned as clear text.
>
> The endpoint generates a [Card embossing notification received](https://developers.pismo.io/events/docs/cards-embossing-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `GetEncryptedCardDataRequest2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | object (schema `CardID`) | yes | Pismo card ID object |  |
| `key_id` | string (schema `KeyID3`) | yes | Encryption key ID to embossing, used in conjunction with the initial vector value.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Encrypted card embossing data (shown here as unencrypted JSON) | `application/json`: object (schema `EncryptedCardContent2`) |
| 400 | Bad Request | `application/json`: object |
| 401 | Access token is missing or invalid |  |
| 404 | Not found | `application/json`: object |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `card_id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID | example: 7654776 |
| `customer_id` | integer (schema `CustomerID`) | no | Pismo customer ID | example: 765476676 |
| `program_id` | integer (schema `ProgramID`) | no | Pismo program ID | example: 7654 |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `iv` | string (schema `InitialVector`) | no | Initial vector (IV) value, needs to be 16 bytes and hexadecimal. An IV is a random or pseudo-random value used as the starting point for an encryption algorithm to generate a unique cipher text for each message. The IV is used in combination with a secret key (`key_id`) to ensure that the same message encrypted with the same key does not result in the same cipher text.<br> |  |
| `encrypted_card_data` | string (schema `EncryptedCardData`) | no | Encrypted card data<br><br>When decrypted, this field will have the following JSON:  <br><br>* **`card_number`**<br>  type: string<br>  description: Primary Account Number (PAN)<br><br>* **`printed_name`** <br>  type: string <br>  description: Printed/embossed card holder name.<br><br>* **`expiration_date`**<br>  type: string<br>  description: Card expiration date (format:yymm)<br><br>* **`pinblock`**  <br>  type: string<br>  description: <br>    PINBlocks are 64-bit strings that encode a PIN ready for encryption and secure transmission in banking networks. PIN block ISO 9564-1 format 0. It contains both the PIN and additional data needed to encrypt it for transmission. The PIN block is typically encrypted using a secure cryptographic algorithm to prevent unauthorized access or tampering during transmission. <br><br>* **`cvv`** <br>  type: string <br>  description: \|<br>    Card Verification Value (CVV) is a three- or four-digit security code that is printed on payment cards to help verify that the cardholder is the one making a transaction. <br><br>* **`cvv2`**: <br>  type: string <br>  description: \|<br>    Card Verification Value 2 (CVV2) is also a three-digit code printed on the back of the card. While CVV and CVV2 are both three-digit codes, CVV is numeric only, while CVV2 can contain letters and numbers. <br><br>* **`service_code_cvv1`**:  <br>  type: string<br>  description: \|<br>   Service code for the card verification value 1 (CVV1) is a three-digit code that is encoded on the magnetic stripe of a payment card  and is used to verify the card's authenticity during a transaction. It is different from the CVV2 or CVC2 codes, which are three- or four-digit codes printed on the back of the card and used for online or phone transactions. <br><br>* **`service_code_cvv2`**:  <br>  type: string<br>  description: \|<br>    Service code for the card verification value 2 (CVV2) is a three- or four-digit security code. It is a security feature that helps verify that the card is physically present during card-not-present transactions. It is not encoded on the card's magnetic stripe.<br><br>* **`service_code_icvv`**:  <br>  type: string<br>  description: \|<br>     Service code for the ICVV (Issuer Controlled Card Verification Value) is a dynamic security code the issuing bank generates generated and is used to verify the payment card authenticity during transactions.<br><br>* **`track2_chip`**:  <br>  type: string<br>  description: \|<br>    Analogous to the `track2_magnetic_stripe`, but instead of being recorded on the magnetic stripe it is stored inside the chip. Instead of the CVV2, which is included on the magnetic stripe's track 2, the chip (and therefore this field) contains the iCVV. The same applies for the service code: on the magnetic track2 it `service_code_cvv2`, but here it is `service_code_icvv`.<br><br>* **`track1_magnetic_stripe`**:  <br>  type: string<br>  description: \|<br>  Track 1 of the card's magnetic stripe located on the back of the card and is read by card readers and point-of-sale (POS) terminals. It contains several fields of information, including the cardholder's name, account number, expiration date, and other identifying information.<br><br>* **`track2_magnetic_stripe`**:  <br>  type: string<br>  description: \|<br>    Track 2 of the magnetic stripe is similar to track 1 magnetic stripes but contains less information and include only the cardholder's account number, expiration date, and a discretionary data field.<br> |  |

200 Example `example`:

```json
{
  "org_id": "TN-5aea4104-7994-46d5-83d6-a55cxxxxxxxx",
  "card_id": 0,
  "correlation_id": "9f46663d-34dc-9e37-a89a-a1d6ef56039a",
  "password_updated": true,
  "account_id": 0,
  "card_number": "123456******7890",
  "program_id": 0,
  "printed_name": "Some person",
  "expiration_date": "2805",
  "customer_id": 0,
  "cvv": "000",
  "cvv2": "000",
  "icvv": "000",
  "track1_magnetic_stripe": "B65....^NOT/REAL...00000?",
  "track1_chip": "B650...NOT/REAL...0000000?",
  "track2_chip": "B650...NOT/REAL...0000000?",
  "track2_magnetic_stripe": "B65...^NOT/REAL...00000?",
  "pinblock": "000000000000000",
  "service_code_cvv1": "000",
  "service_code_cvv2": "000",
  "service_code_icvv": "000"
}
```

##### Response 404

404 Example `example-bad-request`:

```json
{
  "message": "Not found configurations ondemand to org",
  "error": "Not_found",
  "status": 404
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-embossing-1` | https://developers.pismo.io/events/docs/cards-embossing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/CardID -->
### Schema `CardID`

Pointer: `#/components/schemas/CardID`. Type: object (schema `CardID`).

> Pismo card ID object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cardId` | string | no | Card ID | example: "737040484" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Embossing encrypted`: POST /embossing/v1/cards/generate-embossing, POST /embossing/v2/cards/generate-embossing, POST /embossing/v1/cards/generate-embossing/noname, POST /embossing/v2/cards/generate-embossing/noname | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-EVT-catalogue-cards` — Event catalogue: cards
