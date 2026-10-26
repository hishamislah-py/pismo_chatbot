---
ku_id: KU-API-card-issuing-cards--card-status
title: 'API reference: Card issuing - Cards — Card status'
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
- put-v1-card-status
- get-v1-card-statuses
- get-v1-card-satus-history
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-card-lifecycle-and-statuses
- KU-EVT-cards-data-events
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Card status

**KU ID:** `KU-API-card-issuing-cards--card-status` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Card status` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Card status endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/status` | `put-v1-card-status` | Update card status | no |
| `GET /wallet/v1/cards/statuses` | `get-v1-card-statuses` | Get card statuses | no |
| `GET /wallet/v1/cards/{cardId}/status-history` | `get-v1-card-satus-history` | List card status history | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/status operationId=put-v1-card-status -->
### `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/status` — Update card status

- **operationId:** `put-v1-card-status`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Card status`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Change a card's status. For more information, Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide.
>
> This endpoint generates a [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `accountId` | path | yes | integer | Pismo account ID | example: 8675309 |
| `customerId` | path | yes | string | Customer ID | example: "125555" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `UpdateCardStatus`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string (schema `CardStatus`) | no | Card status enum. Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete list.<br> | example: "NORMAL" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Card information | `application/json`: object (schema `UpdateCardStatusResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program` | object | no |  |  |
| `program.id` | string | no | Program ID |  |
| `account` | object | no |  |  |
| `account.id` | string | no | Account ID |  |
| `customer` | object | no |  |  |
| `customer.id` | string | no | Customer ID |  |
| `org` | object | no |  |  |
| `org.id` | string | no | Org ID |  |
| `id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `hash` | string (schema `Hash`) | no | Encrypted Primary Account Number (PAN). This field does not exist until the card PCI data is asynchronously created.<br> | example: "WEPvOQuZvjfYEd0iBmr43bhWyOsylIsW95ebYrLD89App2iEq9IizP+8w73pxKQ4mI47EdhzYHF9RfXjrBOyug==" |
| `last_4_digits` | string (schema `Last4Digits`) | no | Last four Primary Account Number (PAN) digits. This field does not exist until the card PCI data is asynchronously created.<br> | example: "4321" |
| `first_4_digits` | string | no | First 4 PAN digits.  This field is DEPRECATED and it is recommended you use the `bin` field instead. | deprecated: true |
| `brand` | string (schema `Brand`) | no | Card network, i.e., Visa, Mastercard, ELO, RuPay, Private, GPN | example: "Visa" |
| `number_of_transactions` | integer (schema `NumberOfTransactions`) | no | Maximum transactions allowed | example: 40 |
| `bin` | string (schema `BIN`) | no | Bank Identification Number (BIN). A 6 or 8 digit number identitying the card network, issuer, and product. | example: "87634277" |
| `atc` | string (schema `ATC`) | no | Application Transaction Counter (ATC). The chip card application maintains the ATC as a counter that the chip increments. It provides a reference for each transaction. A duplicate ATC, a decrease in ATC, or a large jump in ATC values may indicate data copying or other fraud. <br><br>Though the ATC is a string, it takes the form of an array of integers containing up to 1000 numbers showing the counter's sequence. <br><br>For more information on how Pismo uses the ATC, refer to the [Application Transaction Counter](doc:application-transaction-counter-atc) guide.<br> | example: "[5, 4, 3, 2, 1]" |
| `status` | string (schema `CardStatus`) | no | Card status enum. Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete list.<br> | example: "NORMAL" |
| `previous_status` | string (schema `PreviousStatus`) | no | Previous card status. <br><br>Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete list.<br> | example: "NORMAL" |
| `issuing_date` | string (schema `IssuingDate`) | no | Date/time when card was issued in RFC3339 format, i.e., 2019-07-03T17:23:18Z | example: "2019-07-03T17:23:18Z" |
| `expiration_date` | string (schema `ExpirationDate`) | no | Card expiration date (format = yymm). If passed, the card expiration date is not calculated using the "Card expiration (# of months)" program parameter.<br> | example: "2803" |
| `printed_name` | string (schema `PrintedName`) | no | Printed/embossed card name.<br><br>Currently, you have 3 ways to populate this field:<br>   <br>   1. During account creation via the `application.applicant.personal.social_name` field.<br>   2. During account creation via the `application.applicant.personal.name` field when the field in #1 is not set.<br>   3. Passing the `printed_name` field during card creation, updating a card, or when reissuing a card. This takes priority over #1 and #2.<br><br>No letters with accents, numbers, or special characters - only letters (a-z\|A-Z) and space, as specified in the <a href="https://emvlab.org/emvtags/show/t5F20/" target="_blank">ISO EMV tag 5F20</a> for cardholder name.<br><br>**REQUIRED** for an `UNNUMBERED` card (Card created without PIN or PAN that issuer defines at some point in the future.)<br> | minLength: 2; maxLength: 26 |
| `name` | string (schema `CardAlias`) | no | Card alias name for a `VIRTUAL` card. <br><br>This field is **REQUIRED** to be unique for each `VIRTUAL` card a customer owns.<br><br>No matter what is passed for a `PLASTIC` card, the value is always `PLASTIC`.<br> | minLength: 1; maxLength: 50; example: "Vacation card" |
| `tracking` | integer | no | File sent to embosser tracking ID |  |
| `track_number` | integer | no | Sequential counter incremented every time card is reissued. | example: 2 |
| `migration_id` | string | no | Migration ID (if card migrated to Pismo). |  |
| `transaction_limit` | string (schema `TransactionLimit`) | no | Optional for virtual cards. Maximum amount allowed per transaction. Set up to the approved limit. If not set, account limit is used. | example: "500.00" |
| `password_tries` | integer (schema `PasswordTries`) | no | Number of times the password was tried | example: 1 |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |
| `reissued_card_id` | integer (schema `ReissuedCardID`) | no | Last issued card ID | example: 123456 |
| `type` | string (schema `CardType`) | no | Card type enum:<br> * `PLASTIC` - Physical card - plastic or metal.<br> * `VIRTUAL` - Digital card with fixed PAN and dynamic CVV.<br> * `TEMPORARY` - Virtual card with a fixed PAN and CVV meant for short-term use, typically 24 hours. For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards) in the Cards management guide.<br> * `RECURRING` - Virtual card with a fixed PAN and CVV originally meant for use with recurring subscriptions. This type is being **DEPRECATED** and it is recommended you use `VIRTUAL` instead. <br> | enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: "VIRTUAL" |
| `metadata` | object (schema `Metadata`) | no | <br>Any key-value object. Max length = 3200 bytes. This **must** be valid JSON data.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | maxLength: 3200; example: {"my-custom-key": "my-custom-value"} |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `valid_until` | string (schema `ValidUntil`) | no | Card validation date in UTC time (format:yyyy-MM-ddThh:mm:ssZ). For `TEMPORARY` virtual cards, which have a limited time frame, typically 24 hours (default), or according to the program parameter for this, which is why the date/time here is more granular than `expiration_date`.  <br><br>For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards).<br> | example: "2021-07-03T17:23:18Z" |
| `bulk_id` | string | no | Noname bulk/batch ID |  |
| `external_id` | string | no | Client internal tracking ID | maxLength: 255 |
| `mode` | string (schema `Mode`) | no | Mode enum:<br>`CREDIT` - Single credit card<br>`DEBIT` - Single debit card<br>`COMBO` - Card has both a credit and debit *mode*, meaning it is associated with both a credit and debit program and account.<br>`MULTIPLE` -  Combination card created with the DEPRECATED [Create combo card](ref:post-v1-combocard-relationship) endpoint. <br><br>For more information, refer to the [mode documentation](doc:cards-overview-1#create-a-combination-card-with-card-modes) in the Card management guide.<br> | enum: ["CREDIT", "DEBIT", "COMBO", "MULTIPLE"]; example: "CREDIT" |
| `dual_message_debit` | boolean (schema `DualMessageDebit`) | no | For Mastercard - if card is DMC, where the debit has authorization and confirmation at different times, base I and base II, respectively. Unlike Mastercard's Maestro debit, where authorization and confirmation take place at the same time (base I). <br><br>Default is `false`.<br> |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-update-1` | https://developers.pismo.io/events/docs/cards-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-card-lifecycle-and-statuses`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/wallet/v1/cards/statuses operationId=get-v1-card-statuses -->
### `GET /wallet/v1/cards/statuses` — Get card statuses

- **operationId:** `get-v1-card-statuses`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Card status`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get all possible card statuses, including those used for card reissuing.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Card statuses list | `application/json`: array of string (schema `AllCardStatusesResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/wallet/v1/cards/{cardId}/status-history operationId=get-v1-card-satus-history -->
### `GET /wallet/v1/cards/{cardId}/status-history` — List card status history

- **operationId:** `get-v1-card-satus-history`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Card status`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets a list of a card's status history. The IDs of the card's account and org/tenant are parsed from the access token.
>
> **Note**: 
>
>   * Only cards with status changes after September/2022 are returned.
>
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID.
>
> For more information, refer to [Card lifecycle and statuses](doc:card-lifecycle-and-statuses).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-customer-id` | header | yes | integer | Pismo customer ID | example: 125555 |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `page` | query | no | string | Page number. Default is initial page - `0`. To navigate between pages, set `format=paged`. | example: "1" |
| `perPage` | query | no | string | Items per page. Default is `10`. | example: "10" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Array of card statuses. | `application/json`: object (schema `CardStatusListResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object | no |  |  |
| `items[].status` | string (schema `CardStatus`) | no | Card status enum. Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete list.<br> | example: "NORMAL" |
| `items[].previous_status` | string (schema `PreviousStatus`) | no | Previous card status. <br><br>Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete list.<br> | example: "NORMAL" |
| `items[].event_datetime` | string | no | Date/time card status changed, formatted as a RFC3339 string | example: "2021-07-03T17:23:18Z" |
| `items[].operation` | string (schema `Operation`) | no | Operation that changed the card status:  <br>* `ACTIVATE`&mdash;When the card is activated via the [Activate physical card](ref:put-v1-card-activate) endpoint.<br>* `UPDATE_STATUS_PUT`&mdash;When the card has its status changed via the [Update card status](ref:put-v1-card-status) endpoint.<br>* `UPDATE_STATUS_PATCH`&mdash;When any card data changed via the end [Update card information](ref:patch-v2-card) endpoint.<br>* `REISSUE`&mdash;When a card is reissued via the [Reissue card](ref:post-v1-card-reissue) endpoint. <br>* `RESET_PASSWORD_TRIES`&mdash;When the password try counter is reset via the [Reset password try count](ref:post-v2-card-password-reset) endpoint.<br>* `BIND_NONAME`&mdash;When the card noname and the cardholder are bound via the [Associate noname card with customer](ref:post-v2-card-bind) endpoint.<br>* `BIND_REISSUE`&mdash;When the card noname and the holder are bound with reissue use case via the [Associate noname card with customer](ref:post-v2-card-bind) <br>* `TEMPORARY_CARD_INOPERATIVE_EVENT`&mdash;When the `TEMPORARY` card is renewed and has its status changed to `NORMAL`. More details about `TEMPORARY` cards at [Cards management](doc:cards-overview-1) <br>* `TEMPORARY_CARD_RENEWAL_EVENT`&mdash;When the `TEMPORARY` card is renewed and has its status changed to `INOPERATIVE`. More details about `TEMPORARY` cards at [Cards management](doc:cards-overview-1)  <br>* `AUTH_PASSWORD_TRIES_EXCEEDED`&mdash;When at the time network authorization (OffUs), the number of password tries made reaches the allowed try limit.<br>* `AUTHONUS_PASSWORD_TRIES_EXCEEDED`&mdash;When at the time authorization (OnUs), the number of password tries made reaches the allowed try limit.<br>* `INCREASE_PASSWORD_TRIES_EXCEEDED`&mdash;When the number of attempts is increased through the endpoint<br>* `MIGRATION`&mdash;When in the card migration flow to Pismo the card status changes.<br>* `AUTH_REFERRED`&mdash;When at the time authorization and performing fraud analysis, the issuer can return a flag so that the card is blocked<br> | enum: ["ACTIVATE", "UPDATE_STATUS_PUT", "UPDATE_STATUS_PATCH", "REISSUE", "RESET_PASSWORD_TRIES", "BIND_NONAME", "BIND_REISSUE", "TEMPORARY_CARD_INOPERATIVE_EVENT", "TEMPORARY_CARD_RENEWAL_EVENT", "AUTH_PASSWORD_TRIES_EXCEEDED", "AUTHONUS_PASSWORD_TRIES_EXCEEDED", "INCREASE_PASSWORD_TRIES_EXCEEDED", "MIGRATION", "AUTH_REFERRED"]; example: "ACTIVATE" |
| `currentPage` | integer | no | Current page | example: 1 |
| `perPage` | integer | no | Items per page | example: 10 |
| `totalItems` | integer | no | Total items | example: 17 |
| `pages` | integer | no | Total number of pages | example: 2 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

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
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Card status`: PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/status, GET /wallet/v1/cards/statuses, GET /wallet/v1/cards/{cardId}/status-history | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-card-lifecycle-and-statuses` — Card lifecycle and statuses
- `KU-EVT-cards-data-events` — Card issuing - Cards
- `KU-EVT-catalogue-cards` — Event catalogue: cards
