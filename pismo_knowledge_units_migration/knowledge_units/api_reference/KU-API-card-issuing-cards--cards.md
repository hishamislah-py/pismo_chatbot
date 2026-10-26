---
ku_id: KU-API-card-issuing-cards--cards
title: 'API reference: Card issuing - Cards — Cards'
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
- post-v2-card
- put-v1-card-activate
- get-v1-cards
- get-v1-cards-by-account
- get-v1-card
- patch-v2-card
- post-v2-card-atc-reset
- post-v2-card-password-reset
- post-v2-card-password-increase
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-application-transaction-counter-atc
- KU-CARD-bin-override-feature
- KU-CARD-card-lifecycle-and-statuses
- KU-CARD-cards-overview-1
- KU-CARD-implementation-steps
- KU-CARD-physical-card-embossing
- KU-ERR-validation-code-definitions
- KU-EVT-cards-data-events
- KU-EVT-catalogue-cards
- KU-GS-get-started-with-pismo-apis
- KU-GS-setup-overview
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Cards

**KU ID:** `KU-API-card-issuing-cards--cards` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 9 operation(s) tagged `Cards` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Card management endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /wallet/v2/cards` | `post-v2-card` | Create card | no |
| `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/activate` | `put-v1-card-activate` | Activate physical card | no |
| `GET /wallet/v1/customers/{customerId}/accounts/{accountId}/cards` | `get-v1-cards` | Get cards for customer and account | no |
| `GET /wallet/v1/cards` | `get-v1-cards-by-account` | Get account cards | no |
| `GET /wallet/v1/cards/{cardId}` | `get-v1-card` | Get non-PCI card information | no |
| `PATCH /wallet/v2/cards/{cardId}` | `patch-v2-card` | Update card information | no |
| `POST /wallet/v2/cards/{cardId}/atc/reset` | `post-v2-card-atc-reset` | Reset card ATC | no |
| `POST /wallet/v2/cards/{cardId}/password-tries/reset` | `post-v2-card-password-reset` | Reset password try count | no |
| `POST /wallet/v2/cards/{cardId}/password-tries/increase` | `post-v2-card-password-increase` | Increase password try count | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/wallet/v2/cards operationId=post-v2-card -->
### `POST /wallet/v2/cards` — Create card

- **operationId:** `post-v2-card`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Cards`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a virtual or physical (plastic/metal) card.
>
> Refer to the [Cards management](doc:cards-overview-1) guide for more information about physical and virtual cards.
>
> For more information about embossing, refer to [Embossing flows](doc:physical-card-embossing#embossing-flow).
>
> This endpoint generates a [Card created](https://developers.pismo.io/events/docs/cards-create-1) event. The card's PCI data is created asynchronously as is the Card created event. Any operation that tries to access a card before this event, such as update password or get PCI information, is going to return a **404, not found** error.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-customer-id` | header | yes | integer | Pismo customer ID | example: 125555 |
| `x-idempotency-key` | header | no | string | A unique identifier to ensure the operation remains idempotent, allowing for operation repetition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies. 36 chars max. <br> | maxLength: 36; example: "123e4567-e89b-12d3-a456-426614174000" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `CreateCard`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `CardAlias`) | yes | Card alias name for a `VIRTUAL` card. <br><br>This field is **REQUIRED** to be unique for each `VIRTUAL` card a customer owns.<br><br>No matter what is passed for a `PLASTIC` card, the value is always `PLASTIC`.<br> | minLength: 1; maxLength: 50; example: "Vacation card" |
| `type` | string (schema `CardType`) | yes | Card type enum:<br> * `PLASTIC` - Physical card - plastic or metal.<br> * `VIRTUAL` - Digital card with fixed PAN and dynamic CVV.<br> * `TEMPORARY` - Virtual card with a fixed PAN and CVV meant for short-term use, typically 24 hours. For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards) in the Cards management guide.<br> * `RECURRING` - Virtual card with a fixed PAN and CVV originally meant for use with recurring subscriptions. This type is being **DEPRECATED** and it is recommended you use `VIRTUAL` instead. <br> | enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: "VIRTUAL" |
| `printed_name` | string (schema `PrintedName`) | no | Printed/embossed card name.<br><br>Currently, you have 3 ways to populate this field:<br>   <br>   1. During account creation via the `application.applicant.personal.social_name` field.<br>   2. During account creation via the `application.applicant.personal.name` field when the field in #1 is not set.<br>   3. Passing the `printed_name` field during card creation, updating a card, or when reissuing a card. This takes priority over #1 and #2.<br><br>No letters with accents, numbers, or special characters - only letters (a-z\|A-Z) and space, as specified in the <a href="https://emvlab.org/emvtags/show/t5F20/" target="_blank">ISO EMV tag 5F20</a> for cardholder name.<br><br>**REQUIRED** for an `UNNUMBERED` card (Card created without PIN or PAN that issuer defines at some point in the future.)<br> | minLength: 2; maxLength: 26 |
| `pin_length` | integer (schema `PinLength`) | no | PIN length - 4 or 6 digits. Default is `4`. | enum: [4, 6]; default: 4 |
| `cvv_rotation_interval_hours` | integer (schema `cvvRotationInterval`) | no | <b>REQUIRED</b> for a virtual card.  Virtual card CVV rotation interval in hours.<br><br>To force a rotation manually, call the [Rotate virtual card CVV](ref:post-v2-reset-cvv) endpoint.<br><br>If `0` is passed, the CVV will **NOT** be rotated.<br> | minimum: 1; maximum: 4320 |
| `transaction_limit` | string (schema `TransactionLimit`) | no | Optional for virtual cards. Maximum amount allowed per transaction. Set up to the approved limit. If not set, account limit is used. | example: "500.00" |
| `metadata` | object (schema `Metadata`) | no | <br>Any key-value object. Max length = 3200 bytes. This **must** be valid JSON data.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | maxLength: 3200; example: {"my-custom-key": "my-custom-value"} |
| `embossing_group` | string (schema `EmbossingGroup`) | no | Embossing group name. Clients can work with multi-embossers. You can use this field to notify an embosser about a card request. If this parameter is not passed, and you work with multi-embossers, the default embosser is used. For more information, refer to the [Physical card embossing](doc:physical-card-embossing) guide.<br> | minLength: 2; maxLength: 32; example: "EM1-embosser" |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `mode_type` | string (schema `ModeType`) | no | Mode type enum - `SINGLE` or `COMBO`.  A combo card can have both a credit and debit *mode*, meaning it is associated with both a credit and debit program and  account. A single card has one mode - credit or debit. Refer to the [mode documentation](doc:cards-overview-1#create-a-combination-card-with-card-modes) in the Card overview guide for more information.<br> | enum: ["SINGLE", "COMBO"]; example: "COMBO" |
| `generate_pvv` | boolean (schema `GeneratePvv`) | no | For physical cards. Should a PIN Verification Value (PVV) be generated and inserted into the card tracks during embossing, or should the PVV be generated and sent to Visa when updating the card's PIN? Visa's PIN Verification Service (PVS) **must** be enabled. The default is `false`.<br> | default: false; example: true |
| `validity_period_hours` | integer (schema `ValidityPeriodHours`) | no | How long, in hours, the card is valid. Cannot exceed the card's `expiration_date`. Once this period is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br><br>This field is used to calculate the datetime value for `valid_until`.<br><br>For `VIRTUAL` and `PLASTIC` cards. Setting this field for `TEMPORARY` or `RECURRING` cards returns a **400 Bad request** error.  <br> | example: 240 |
| `status` | string (schema `Status`) | no | Card status, sent when an `UNNUMBERED` card is requested. For issuers who want to create cards on the Pismo platform that will not have PCI data (PAN, PIN) generated here but that they will provide at some point in the future. <br> | enum: ["UNNUMBERED"]; example: "UNNUMBERED" |
| `brand` | string (schema `SentBrand`) | no | Card network that overrides the one set up by the card's program. <br><br>**REQUIRED** when the `status` field is used for `UNNUMBERED` cards.<br> | enum: ["VISA", "MASTERCARD", "ELO", "RUPAY", "PRIVATE", "GPN"]; example: "VISA" |
| `expiration_date` | string (schema `ExpirationDate`) | no | Card expiration date (format = yymm). If passed, the card expiration date is not calculated using the "Card expiration (# of months)" program parameter.<br> | example: "2803" |
| `atm_change_online_pin_when_script_sent` | boolean (schema `ATMchangeOnlinePinWhenScriptSent`) | no | During ATM transactions, should the card's online PIN be updated when the offline PIN change script is sent to the terminal for execution? <br><br>If `false`, the online PIN is only updated after a subsequent transaction, once the Pismo platform verifies - via the card's CVR (Card Verification Results) — that the offline script was successfully applied. <br><br>Default is `false`.<br> | default: false; example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Card creation response when `x-idempotency-key` is passed and the card had already been created in a preivous call. | `application/json`: object (schema `CreateCardResponse`) |
| 201 | Card creation response -  with or without `x-idempotency-key` passed. | `application/json`: object (schema `CreateCardResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 409 | You already have a card with this type and name active |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `name` | string (schema `CardAlias`) | no | Card alias name for a `VIRTUAL` card. <br><br>This field is **REQUIRED** to be unique for each `VIRTUAL` card a customer owns.<br><br>No matter what is passed for a `PLASTIC` card, the value is always `PLASTIC`.<br> | minLength: 1; maxLength: 50; example: "Vacation card" |
| `status` | string (schema `CardStatus`) | no | Card status enum. Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete list.<br> | example: "NORMAL" |
| `type` | string (schema `CardType`) | no | Card type enum:<br> * `PLASTIC` - Physical card - plastic or metal.<br> * `VIRTUAL` - Digital card with fixed PAN and dynamic CVV.<br> * `TEMPORARY` - Virtual card with a fixed PAN and CVV meant for short-term use, typically 24 hours. For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards) in the Cards management guide.<br> * `RECURRING` - Virtual card with a fixed PAN and CVV originally meant for use with recurring subscriptions. This type is being **DEPRECATED** and it is recommended you use `VIRTUAL` instead. <br> | enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: "VIRTUAL" |
| `transaction_limit` | string (schema `TransactionLimit`) | no | Optional for virtual cards. Maximum amount allowed per transaction. Set up to the approved limit. If not set, account limit is used. | example: "500.00" |
| `metadata` | object (schema `Metadata`) | no | <br>Any key-value object. Max length = 3200 bytes. This **must** be valid JSON data.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | maxLength: 3200; example: {"my-custom-key": "my-custom-value"} |
| `cvv_rotation_interval_hours` | integer (schema `cvvRotationInterval`) | no | <b>REQUIRED</b> for a virtual card.  Virtual card CVV rotation interval in hours.<br><br>To force a rotation manually, call the [Rotate virtual card CVV](ref:post-v2-reset-cvv) endpoint.<br><br>If `0` is passed, the CVV will **NOT** be rotated.<br> | minimum: 1; maximum: 4320 |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `mode_type` | string (schema `ModeType`) | no | Mode type enum - `SINGLE` or `COMBO`.  A combo card can have both a credit and debit *mode*, meaning it is associated with both a credit and debit program and  account. A single card has one mode - credit or debit. Refer to the [mode documentation](doc:cards-overview-1#create-a-combination-card-with-card-modes) in the Card overview guide for more information.<br> | enum: ["SINGLE", "COMBO"]; example: "COMBO" |
| `validity_period_hours` | integer (schema `ValidityPeriodHours`) | no | How long, in hours, the card is valid. Cannot exceed the card's `expiration_date`. Once this period is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br><br>This field is used to calculate the datetime value for `valid_until`.<br><br>For `VIRTUAL` and `PLASTIC` cards. Setting this field for `TEMPORARY` or `RECURRING` cards returns a **400 Bad request** error.  <br> | example: 240 |
| `valid_until` | string (schema `ValidUntil2`) | no | Card is valid until this datetime. ISO 8601 format. Once this time is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br>This field's value is calculated using the `validity_period_hours`. <br> | example: "2021-07-03T17:23:18Z" |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `name` | string (schema `CardAlias`) | no | Card alias name for a `VIRTUAL` card. <br><br>This field is **REQUIRED** to be unique for each `VIRTUAL` card a customer owns.<br><br>No matter what is passed for a `PLASTIC` card, the value is always `PLASTIC`.<br> | minLength: 1; maxLength: 50; example: "Vacation card" |
| `status` | string (schema `CardStatus`) | no | Card status enum. Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete list.<br> | example: "NORMAL" |
| `type` | string (schema `CardType`) | no | Card type enum:<br> * `PLASTIC` - Physical card - plastic or metal.<br> * `VIRTUAL` - Digital card with fixed PAN and dynamic CVV.<br> * `TEMPORARY` - Virtual card with a fixed PAN and CVV meant for short-term use, typically 24 hours. For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards) in the Cards management guide.<br> * `RECURRING` - Virtual card with a fixed PAN and CVV originally meant for use with recurring subscriptions. This type is being **DEPRECATED** and it is recommended you use `VIRTUAL` instead. <br> | enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: "VIRTUAL" |
| `transaction_limit` | string (schema `TransactionLimit`) | no | Optional for virtual cards. Maximum amount allowed per transaction. Set up to the approved limit. If not set, account limit is used. | example: "500.00" |
| `metadata` | object (schema `Metadata`) | no | <br>Any key-value object. Max length = 3200 bytes. This **must** be valid JSON data.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | maxLength: 3200; example: {"my-custom-key": "my-custom-value"} |
| `cvv_rotation_interval_hours` | integer (schema `cvvRotationInterval`) | no | <b>REQUIRED</b> for a virtual card.  Virtual card CVV rotation interval in hours.<br><br>To force a rotation manually, call the [Rotate virtual card CVV](ref:post-v2-reset-cvv) endpoint.<br><br>If `0` is passed, the CVV will **NOT** be rotated.<br> | minimum: 1; maximum: 4320 |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `mode_type` | string (schema `ModeType`) | no | Mode type enum - `SINGLE` or `COMBO`.  A combo card can have both a credit and debit *mode*, meaning it is associated with both a credit and debit program and  account. A single card has one mode - credit or debit. Refer to the [mode documentation](doc:cards-overview-1#create-a-combination-card-with-card-modes) in the Card overview guide for more information.<br> | enum: ["SINGLE", "COMBO"]; example: "COMBO" |
| `validity_period_hours` | integer (schema `ValidityPeriodHours`) | no | How long, in hours, the card is valid. Cannot exceed the card's `expiration_date`. Once this period is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br><br>This field is used to calculate the datetime value for `valid_until`.<br><br>For `VIRTUAL` and `PLASTIC` cards. Setting this field for `TEMPORARY` or `RECURRING` cards returns a **400 Bad request** error.  <br> | example: 240 |
| `valid_until` | string (schema `ValidUntil2`) | no | Card is valid until this datetime. ISO 8601 format. Once this time is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br>This field's value is calculated using the `validity_period_hours`. <br> | example: "2021-07-03T17:23:18Z" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-create-1` | https://developers.pismo.io/events/docs/cards-create-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;201;401;403;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-bin-override-feature`, `KU-CARD-cards-overview-1`, `KU-CARD-implementation-steps`, `KU-CARD-physical-card-embossing`, `KU-EVT-cards-data-events`, `KU-GS-get-started-with-pismo-apis`, `KU-GS-setup-overview`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/activate operationId=put-v1-card-activate -->
### `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/activate` — Activate physical card

- **operationId:** `put-v1-card-activate`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Cards`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> A physical card is initally blocked for transactions until activated.  This prevents unauthorized use until the cardholder takes delivery. You do not have to activate a card to tokenize it for a digital wallet.
> This endpoint generates a [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `customerId` | path | yes | string | Customer ID | example: "125555" |
| `accountId` | path | yes | integer | Pismo account ID | example: 8675309 |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `x-customer-id` | header | yes | integer | Pismo customer ID | example: 125555 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Card activated success response | `application/json`: object (schema `CardActivatedSuccessResponse`) |
| 204 | No Content |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Physical card activated message | example: "The card was successfully unblocked" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-update-1` | https://developers.pismo.io/events/docs/cards-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;204;401;403;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-card-lifecycle-and-statuses`, `KU-CARD-cards-overview-1`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/wallet/v1/customers/{customerId}/accounts/{accountId}/cards operationId=get-v1-cards -->
### `GET /wallet/v1/customers/{customerId}/accounts/{accountId}/cards` — Get cards for customer and account

- **operationId:** `get-v1-cards`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Cards`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get cards for specified account and customer with paging and filter options. 
>
> Accounts can have multiple customers, typically to accommodate primary and additional cardholders, but only one owner. There can only be one physical card per customer. A customer can have multiple virtual cards, but the card names have to be different.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `customerId` | path | yes | string | Customer ID | example: "125555" |
| `accountId` | path | yes | integer | Pismo account ID | example: 8675309 |
| `page` | query | no | string | Page number. Default is initial page - `0`. To navigate between pages, set `format=paged`. | example: "1" |
| `perPage` | query | no | string | Cards per page. Default is `10`.  To navigate between pages, set `format=paged`. | example: "10" |
| `format` | query | no | string | Set to `paged` to use paging for results. | enum: ["paged"]; example: "paged" |
| `status` | query | no | array of string | Card status filter:<br>  - If nothing is passed, cards with status `CREATED`, `NORMAL`, and `BLOCKED` are returned. <br>  - If `ALL` is passed, all cards, regardless of status, are returned. <br>  - If one or more specific statuses are passed, cards with those statuses are returned.<br><br>Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete status list.<br> |  |
| `modes` | query | no | array of string | Filter results using card mode. <br>  - If nothing is passed, all cards are returned. <br>  - If one or more specific modes are passed, cards with those modes are returned.<br> | items.enum: ["CREDIT", "DEBIT", "MULTIPLE", "COMBO"]; example: ["CREDIT"] |
| `types` | query | no | array of string | Card type filter:<br>  - If nothing is passed, all cards are returned. <br>  - If one or more specific types are passed, cards with those types are returned.<br> | items.enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: ["PLASTIC"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | CardInfoResponse object array | `application/json`: array of object (schema `CardInfoResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/wallet/v1/cards operationId=get-v1-cards-by-account -->
### `GET /wallet/v1/cards` — Get account cards

- **operationId:** `get-v1-cards-by-account`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Cards`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get cards for specified account with paging and filter options. The account is parsed from the token, which must be an account token.
>
> Accounts can have multiple customers, typically to accommodate primary and additional cardholders, but only one owner.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | no | string | Page number. Default is initial page - `0`. To navigate between pages, set `format=paged`. | example: "1" |
| `perPage` | query | no | string | Cards per page. Default is `10`.  To navigate between pages, set `format=paged`. | example: "10" |
| `format` | query | no | string | Set to `paged` to use paging for results. | enum: ["paged"]; example: "paged" |
| `status` | query | no | array of string | Card status filter:<br>  - If nothing is passed, cards with status `CREATED`, `NORMAL`, and `BLOCKED` are returned. <br>  - If `ALL` is passed, all cards, regardless of status, are returned. <br>  - If one or more specific statuses are passed, cards with those statuses are returned.<br><br>Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete status list.<br> |  |
| `modes` | query | no | array of string | Filter results using card mode. <br>  - If nothing is passed, all cards are returned. <br>  - If one or more specific modes are passed, cards with those modes are returned.<br> | items.enum: ["CREDIT", "DEBIT", "MULTIPLE", "COMBO"]; example: ["CREDIT"] |
| `types` | query | no | array of string | Card type filter:<br>  - If nothing is passed, all cards are returned. <br>  - If one or more specific types are passed, cards with those types are returned.<br> | items.enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: ["PLASTIC"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | CardInfoResponse object array | `application/json`: array of object (schema `CardInfoResponse2`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/wallet/v1/cards/{cardId} operationId=get-v1-card -->
### `GET /wallet/v1/cards/{cardId}` — Get non-PCI card information

- **operationId:** `get-v1-card`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Cards`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get card non-sensitive (non-PCI) information.
>
> NOTE: This endpoint requires an account-specific access token - a token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `x-customer-id` | header | yes | integer | Pismo customer ID | example: 125555 |
| `x-account-id` | header | yes | integer | Pismo account ID | example: 8675309 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Card information | `application/json`: object (schema `CardInfoResponse3`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `hash` | string (schema `Hash`) | no | Encrypted Primary Account Number (PAN). This field does not exist until the card PCI data is asynchronously created.<br> | example: "WEPvOQuZvjfYEd0iBmr43bhWyOsylIsW95ebYrLD89App2iEq9IizP+8w73pxKQ4mI47EdhzYHF9RfXjrBOyug==" |
| `status` | string (schema `CardStatus`) | no | Card status enum. Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete list.<br> | example: "NORMAL" |
| `printed_name` | string (schema `PrintedName`) | no | Printed/embossed card name.<br><br>Currently, you have 3 ways to populate this field:<br>   <br>   1. During account creation via the `application.applicant.personal.social_name` field.<br>   2. During account creation via the `application.applicant.personal.name` field when the field in #1 is not set.<br>   3. Passing the `printed_name` field during card creation, updating a card, or when reissuing a card. This takes priority over #1 and #2.<br><br>No letters with accents, numbers, or special characters - only letters (a-z\|A-Z) and space, as specified in the <a href="https://emvlab.org/emvtags/show/t5F20/" target="_blank">ISO EMV tag 5F20</a> for cardholder name.<br><br>**REQUIRED** for an `UNNUMBERED` card (Card created without PIN or PAN that issuer defines at some point in the future.)<br> | minLength: 2; maxLength: 26 |
| `name` | string (schema `CardAlias`) | no | Card alias name for a `VIRTUAL` card. <br><br>This field is **REQUIRED** to be unique for each `VIRTUAL` card a customer owns.<br><br>No matter what is passed for a `PLASTIC` card, the value is always `PLASTIC`.<br> | minLength: 1; maxLength: 50; example: "Vacation card" |
| `type` | string (schema `CardType`) | no | Card type enum:<br> * `PLASTIC` - Physical card - plastic or metal.<br> * `VIRTUAL` - Digital card with fixed PAN and dynamic CVV.<br> * `TEMPORARY` - Virtual card with a fixed PAN and CVV meant for short-term use, typically 24 hours. For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards) in the Cards management guide.<br> * `RECURRING` - Virtual card with a fixed PAN and CVV originally meant for use with recurring subscriptions. This type is being **DEPRECATED** and it is recommended you use `VIRTUAL` instead. <br> | enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: "VIRTUAL" |
| `bin` | string (schema `BIN`) | no | Bank Identification Number (BIN). A 6 or 8 digit number identitying the card network, issuer, and product. | example: "87634277" |
| `brand` | string (schema `Brand`) | no | Card network, i.e., Visa, Mastercard, ELO, RuPay, Private, GPN | example: "Visa" |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `program_id` | integer (schema `ProgramID`) | no | Pismo program ID | example: 7654 |
| `issuing_date` | string (schema `IssuingDate`) | no | Date/time when card was issued in RFC3339 format, i.e., 2019-07-03T17:23:18Z | example: "2019-07-03T17:23:18Z" |
| `transaction_limit` | string (schema `TransactionLimit`) | no | Optional for virtual cards. Maximum amount allowed per transaction. Set up to the approved limit. If not set, account limit is used. | example: "500.00" |
| `expiration_date` | string (schema `ExpirationDate2`) | no | Card expiration date. RFC 3339 format | example: "2023-02-09T15:29:04.000Z" |
| `last_4_digits` | string (schema `Last4Digits`) | no | Last four Primary Account Number (PAN) digits. This field does not exist until the card PCI data is asynchronously created.<br> | example: "4321" |
| `track_number` | integer | no | Sequential counter incremented every time card is reissued. | example: 1 |
| `reissued_card_id` | integer (schema `ReissuedCardID`) | no | Last issued card ID | example: 123456 |
| `password_tries` | integer (schema `PasswordTries`) | no | Number of times the password was tried | example: 1 |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |
| `dual_message_debit` | boolean (schema `DualMessageDebit`) | no | For Mastercard - if card is DMC, where the debit has authorization and confirmation at different times, base I and base II, respectively. Unlike Mastercard's Maestro debit, where authorization and confirmation take place at the same time (base I). <br><br>Default is `false`.<br> |  |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `mode` | string (schema `Mode`) | no | Mode enum:<br>`CREDIT` - Single credit card<br>`DEBIT` - Single debit card<br>`COMBO` - Card has both a credit and debit *mode*, meaning it is associated with both a credit and debit program and account.<br>`MULTIPLE` -  Combination card created with the DEPRECATED [Create combo card](ref:post-v1-combocard-relationship) endpoint. <br><br>For more information, refer to the [mode documentation](doc:cards-overview-1#create-a-combination-card-with-card-modes) in the Card management guide.<br> | enum: ["CREDIT", "DEBIT", "COMBO", "MULTIPLE"]; example: "CREDIT" |
| `validity_period_hours` | integer (schema `ValidityPeriodHours`) | no | How long, in hours, the card is valid. Cannot exceed the card's `expiration_date`. Once this period is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br><br>This field is used to calculate the datetime value for `valid_until`.<br><br>For `VIRTUAL` and `PLASTIC` cards. Setting this field for `TEMPORARY` or `RECURRING` cards returns a **400 Bad request** error.  <br> | example: 240 |
| `valid_until` | string (schema `ValidUntil2`) | no | Card is valid until this datetime. ISO 8601 format. Once this time is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br>This field's value is calculated using the `validity_period_hours`. <br> | example: "2021-07-03T17:23:18Z" |
| `metadata` | object (schema `Metadata`) | no | <br>Any key-value object. Max length = 3200 bytes. This **must** be valid JSON data.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | maxLength: 3200; example: {"my-custom-key": "my-custom-value"} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PATCH path=/wallet/v2/cards/{cardId} operationId=patch-v2-card -->
### `PATCH /wallet/v2/cards/{cardId}` — Update card information

- **operationId:** `patch-v2-card`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Cards`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update card information - `name`, `transaction_limit`, `printed_name`, `contactless_enabled`, `abu_enabled`, or `metadata`.<br>
>
> This endpoint generates a [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `x-customer-id` | header | yes | integer | Pismo customer ID | example: 125555 |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `UpdateCard`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `CardAlias`) | no | Card alias name for a `VIRTUAL` card. <br><br>This field is **REQUIRED** to be unique for each `VIRTUAL` card a customer owns.<br><br>No matter what is passed for a `PLASTIC` card, the value is always `PLASTIC`.<br> | minLength: 1; maxLength: 50; example: "Vacation card" |
| `printed_name` | string (schema `PrintedName`) | no | Printed/embossed card name.<br><br>Currently, you have 3 ways to populate this field:<br>   <br>   1. During account creation via the `application.applicant.personal.social_name` field.<br>   2. During account creation via the `application.applicant.personal.name` field when the field in #1 is not set.<br>   3. Passing the `printed_name` field during card creation, updating a card, or when reissuing a card. This takes priority over #1 and #2.<br><br>No letters with accents, numbers, or special characters - only letters (a-z\|A-Z) and space, as specified in the <a href="https://emvlab.org/emvtags/show/t5F20/" target="_blank">ISO EMV tag 5F20</a> for cardholder name.<br><br>**REQUIRED** for an `UNNUMBERED` card (Card created without PIN or PAN that issuer defines at some point in the future.)<br> | minLength: 2; maxLength: 26 |
| `transaction_limit` | string (schema `TransactionLimit`) | no | Optional for virtual cards. Maximum amount allowed per transaction. Set up to the approved limit. If not set, account limit is used. | example: "500.00" |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `abu_enabled` | boolean | no | To delete a card from the ABU database, submit Mastercard ABU reason code `O` (optout), and Mastercard will delete the card and all previous references to the card data chain. This prevents further merchant notifications. Removing a card from the ABU database using reason code O (Optout) does not result in associated MDES tokens being deleted. Mastercard maintains an audit trail for all deleted cards. <br><br>Set this field to `false`to optout.<br> |  |
| `metadata` | object (schema `Metadata`) | no | <br>Any key-value object. Max length = 3200 bytes. This **must** be valid JSON data.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | maxLength: 3200; example: {"my-custom-key": "my-custom-value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Card update response object | `application/json`: object (schema `UpdateCardResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 409 | You already have a card with this type and name active |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Card ID | example: 123456 |
| `status` | string (schema `CardStatus`) | no | Card status enum. Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete list.<br> | example: "NORMAL" |
| `printed_name` | string (schema `PrintedName`) | no | Printed/embossed card name.<br><br>Currently, you have 3 ways to populate this field:<br>   <br>   1. During account creation via the `application.applicant.personal.social_name` field.<br>   2. During account creation via the `application.applicant.personal.name` field when the field in #1 is not set.<br>   3. Passing the `printed_name` field during card creation, updating a card, or when reissuing a card. This takes priority over #1 and #2.<br><br>No letters with accents, numbers, or special characters - only letters (a-z\|A-Z) and space, as specified in the <a href="https://emvlab.org/emvtags/show/t5F20/" target="_blank">ISO EMV tag 5F20</a> for cardholder name.<br><br>**REQUIRED** for an `UNNUMBERED` card (Card created without PIN or PAN that issuer defines at some point in the future.)<br> | minLength: 2; maxLength: 26 |
| `name` | string (schema `CardAlias`) | no | Card alias name for a `VIRTUAL` card. <br><br>This field is **REQUIRED** to be unique for each `VIRTUAL` card a customer owns.<br><br>No matter what is passed for a `PLASTIC` card, the value is always `PLASTIC`.<br> | minLength: 1; maxLength: 50; example: "Vacation card" |
| `type` | string (schema `CardType`) | no | Card type enum:<br> * `PLASTIC` - Physical card - plastic or metal.<br> * `VIRTUAL` - Digital card with fixed PAN and dynamic CVV.<br> * `TEMPORARY` - Virtual card with a fixed PAN and CVV meant for short-term use, typically 24 hours. For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards) in the Cards management guide.<br> * `RECURRING` - Virtual card with a fixed PAN and CVV originally meant for use with recurring subscriptions. This type is being **DEPRECATED** and it is recommended you use `VIRTUAL` instead. <br> | enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: "VIRTUAL" |
| `issuing_date` | string (schema `IssuingDate`) | no | Date/time when card was issued in RFC3339 format, i.e., 2019-07-03T17:23:18Z | example: "2019-07-03T17:23:18Z" |
| `transaction_limit` | string (schema `TransactionLimit`) | no | Optional for virtual cards. Maximum amount allowed per transaction. Set up to the approved limit. If not set, account limit is used. | example: "500.00" |
| `tracking` | string | no | File sent to embosser tracking ID |  |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-update-1` | https://developers.pismo.io/events/docs/cards-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-cards-overview-1`, `KU-CARD-physical-card-embossing`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/wallet/v2/cards/{cardId}/atc/reset operationId=post-v2-card-atc-reset -->
### `POST /wallet/v2/cards/{cardId}/atc/reset` — Reset card ATC

- **operationId:** `post-v2-card-atc-reset`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Cards`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Reset card ATC (Application Transaction Counter) in case of sync failure between what is saved in a card's memory and the incremented data. The ATC is a counter, maintained by the chip card application (incremented by the chip), that provides a sequential reference to each transaction. A duplicate ATC, a decrease in ATC, or a large jump in ATC values  may indicate data copying or other fraud. For more information on how Pismo processes ATCs, refer to the [Application Transaction Counter (ATC)](https://developers.pismo.io/pismo-docs/docs/application-transaction-counter-atc) guide article.
>
> **Notes:** 
>   * ATC reset only occurs on the Pismo platform. When a new transaction occurs, the ATC is synchronized with the chip's ATC.
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID. For combo cards, whether the debit or credit ATC is reset depends on which account ID (credit or debit) is encoded with the access token.
>

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Card ATC reset | `application/json`: object (schema `CardsSuccessResponse`) |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `success` | boolean | no | Flag indicating success | example: true |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;403;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-application-transaction-counter-atc`, `KU-ERR-validation-code-definitions`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/wallet/v2/cards/{cardId}/password-tries/reset operationId=post-v2-card-password-reset -->
### `POST /wallet/v2/cards/{cardId}/password-tries/reset` — Reset password try count

- **operationId:** `post-v2-card-password-reset`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Cards`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Unblock a card after it has exceeded its maximum password tries count.
>
> If the card is `BLOCKED`:
>
>   * The status is changed to `NORMAL`
>   * The counter is reset 
>   * An [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event is generated.
>
> If the card is `NORMAL`, `PENDING`, or `WARNING`, the counter is reset.
>
> For any other status, a 406 - range not satisfiable - error is returned.
>
> **Note**: This does not change the password recorded on an embossed card's chip. If the card is configured for offline password verification, you need to change the password on the physical card. To do that, you can use a [card script](doc:card-scripts).
>
> For more information, refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Card password tries reset | `application/json`: object (schema `CardsSuccessResponse`) |
| 403 | You don't have permission to access this resource |  |
| 406 | Request is out-of-range. |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `success` | boolean | no | Flag indicating success | example: true |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-update-1` | https://developers.pismo.io/events/docs/cards-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;403;406;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-card-lifecycle-and-statuses`, `KU-CARD-cards-overview-1`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/wallet/v2/cards/{cardId}/password-tries/increase operationId=post-v2-card-password-increase -->
### `POST /wallet/v2/cards/{cardId}/password-tries/increase` — Increase password try count

- **operationId:** `post-v2-card-password-increase`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Cards`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Increase a card's password tries counter by 1. 
>
> If the counter reaches the maximum number of tries configured in the program parameter for this and `block_card_exceeds_counter` is `true`, the card is blocked.
> When this happens:
>
>   * The status is changed to `BLOCKED` 
>   * A [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event is generated.
>
> If the card's status is `CREATED`, the counter is increased, but the status does not change.
>
> For more information, refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `CardsIncreasePasswordBody`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `block_card_exceeds_counter` | boolean | yes | Block card if it exceeds counter | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Card password tries increased | `application/json`: object (schema `CardsIncreasePasswordTriesResponse`) |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `success` | string | no | Message indicating success | example: "Incremented password tries counter" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-update-1` | https://developers.pismo.io/events/docs/cards-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;403;500`, has examples `False`, emits events `1`, deprecated `False`.

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
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Cards`: POST /wallet/v2/cards, PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/activate, GET /wallet/v1/customers/{customerId}/accounts/{accountId}/cards, GET /wallet/v1/cards, GET /wallet/v1/cards/{cardId}, PATCH /wallet/v2/cards/{cardId}, POST /wallet/v2/cards/{cardId}/atc/reset, POST /wallet/v2/cards/{cardId}/password-tries/reset, POST /wallet/v2/cards/{cardId}/password-tries/increase | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-application-transaction-counter-atc` — Application Transaction Counter (ATC)
- `KU-CARD-bin-override-feature` — BIN override - shared account option
- `KU-CARD-card-lifecycle-and-statuses` — Card lifecycle and statuses
- `KU-CARD-cards-overview-1` — Cards management
- `KU-CARD-implementation-steps` — Card issuing implementation steps 1 to 7
- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-ERR-validation-code-definitions` — Validation code definitions
- `KU-EVT-cards-data-events` — Card issuing - Cards
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
- `KU-GS-setup-overview` — Core objects
