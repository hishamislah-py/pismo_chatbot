---
ku_id: KU-API-card-issuing-cards--card-reissue
title: 'API reference: Card issuing - Cards — Card reissue'
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
- post-v1-card-reissue
- get-reissue-reasons
- create-reissue-reason
- update-reissue-reason
- get-v1-card-reissue-reasons
related_kus:
- KU-CARD-bin-override-feature
- KU-CARD-card-lifecycle-and-statuses
- KU-CARD-card-reissuing
- KU-CARD-card-tokenization-process-and-onboarding
- KU-CARD-cards-overview-1
- KU-CARD-physical-card-embossing
- KU-EVT-cards-data-events
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Card reissue

**KU ID:** `KU-API-card-issuing-cards--card-reissue` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Card reissue` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Card reissue endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` | `post-v1-card-reissue` | Reissue card | no |
| `GET /cards/v1/reissue/reasons` | `get-reissue-reasons` | List reissue reasons | no |
| `POST /cards/v1/reissue/reasons` | `create-reissue-reason` | Create reissue reason | no |
| `PATCH /cards/v1/reissue/reasons/{id}` | `update-reissue-reason` | Update reissue reason | no |
| `GET /wallet/v1/cards/reissue/reasons` | `get-v1-card-reissue-reasons` | Get card reissue reasons (outdated) | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue operationId=post-v1-card-reissue -->
### `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` — Reissue card

- **operationId:** `post-v1-card-reissue`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Card reissue`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Reissue a physical (plastic/metal) or virtual card for a given customer/account.
>
> For information on card reissue scenarios and statuses, refer to the [Card reissuing](doc:card-reissuing) guide. 
>
> This endpoint generates a [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event for the old card, and a [Card created](https://developers.pismo.io/events/docs/cards-create-1) event for the new card. The Card created event is generated asynchronously - any operation that tries to access a card before this event, such as update password or get PCI information, is going to return a **404, not found** error. 
>
> **Notes:**
> * If an attempt is made to reissue a card that has already been reissued, the new card's data created in the previous reissue is returned, that is, another card is not created and events are not generated.
> * To update the new card with the old card's PIN, call [Get password ](ref:get-v2-card-password) for the old card, then update the new card's password with [Change card password](ref:put-v2-card-password) 
> * To transfer tokens to the new card, set the `update_tokens` field to `true`. You can also do this later with the [Transfer card tokens to other card](ref:transfertokens) endpoint. 
> * Currently, there is no way to transfer a card's PAN
> * This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `customerId` | path | yes | string | Customer ID | example: "125555" |
| `accountId` | path | yes | integer | Pismo account ID | example: 8675309 |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `x-idempotency-key` | header | no | string | A unique identifier to ensure the operation remains idempotent, allowing for operation repetition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies. 36 chars max. <br> | maxLength: 36; example: "123e4567-e89b-12d3-a456-426614174000" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `SubmitReissue`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reason_id` | integer (schema `ReasonId`) | yes | Reissue reason identifier. You can get reason IDs using the [List reissue reasons](ref:get-reissue-reasons) endpoint. The `must_block` flag comes from the reissue reason object. <br> | example: 123 |
| `printed_name` | string (schema `PrintedName`) | no | Printed/embossed card name.<br><br>Currently, you have 3 ways to populate this field:<br>   <br>   1. During account creation via the `application.applicant.personal.social_name` field.<br>   2. During account creation via the `application.applicant.personal.name` field when the field in #1 is not set.<br>   3. Passing the `printed_name` field during card creation, updating a card, or when reissuing a card. This takes priority over #1 and #2.<br><br>No letters with accents, numbers, or special characters - only letters (a-z\|A-Z) and space, as specified in the <a href="https://emvlab.org/emvtags/show/t5F20/" target="_blank">ISO EMV tag 5F20</a> for cardholder name.<br><br>**REQUIRED** for an `UNNUMBERED` card (Card created without PIN or PAN that issuer defines at some point in the future.)<br> | minLength: 2; maxLength: 26 |
| `pin_length` | integer (schema `PinLength`) | no | PIN length - 4 or 6 digits. Default is `4`. | enum: [4, 6]; default: 4 |
| `cvv_rotation_interval_hours` | integer (schema `cvvRotationInterval`) | no | <b>REQUIRED</b> for a virtual card.  Virtual card CVV rotation interval in hours.<br><br>To force a rotation manually, call the [Rotate virtual card CVV](ref:post-v2-reset-cvv) endpoint.<br><br>If `0` is passed, the CVV will **NOT** be rotated.<br> | minimum: 1; maximum: 4320 |
| `embossing_group` | string (schema `EmbossingGroup`) | no | Embossing group name. Clients can work with multi-embossers. You can use this field to notify an embosser about a card request. If this parameter is not passed, and you work with multi-embossers, the default embosser is used. For more information, refer to the [Physical card embossing](doc:physical-card-embossing) guide.<br> | minLength: 2; maxLength: 32; example: "EM1-embosser" |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `metadata` | object (schema `Metadata`) | no | <br>Any key-value object. Max length = 3200 bytes. This **must** be valid JSON data.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | maxLength: 3200; example: {"my-custom-key": "my-custom-value"} |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `mode_type` | string (schema `ModeType`) | no | Mode type enum - `SINGLE` or `COMBO`.  A combo card can have both a credit and debit *mode*, meaning it is associated with both a credit and debit program and  account. A single card has one mode - credit or debit. Refer to the [mode documentation](doc:cards-overview-1#create-a-combination-card-with-card-modes) in the Card overview guide for more information.<br> | enum: ["SINGLE", "COMBO"]; example: "COMBO" |
| `update_tokens` | boolean (schema `UpdateTokens`) | no | Should the card be updated with associated tokens? <br><br>If `true`, the cardholder will not need to redigitize their card for their current wallet apps. <br><br>Default is `false`.<br><br>**IMPORTANT:** This feature requires additional access setup. Contact your Pismo representative for details. <br> | default: false; example: true |
| `status` | string (schema `Status`) | no | Card status, sent when an `UNNUMBERED` card is requested. For issuers who want to create cards on the Pismo platform that will not have PCI data (PAN, PIN) generated here but that they will provide at some point in the future. <br> | enum: ["UNNUMBERED"]; example: "UNNUMBERED" |
| `brand` | string (schema `SentBrand`) | no | Card network that overrides the one set up by the card's program. <br><br>**REQUIRED** when the `status` field is used for `UNNUMBERED` cards.<br> | enum: ["VISA", "MASTERCARD", "ELO", "RUPAY", "PRIVATE", "GPN"]; example: "VISA" |
| `generate_pvv` | boolean (schema `GeneratePvv`) | no | For physical cards. Should a PIN Verification Value (PVV) be generated and inserted into the card tracks during embossing, or should the PVV be generated and sent to Visa when updating the card's PIN? Visa's PIN Verification Service (PVS) **must** be enabled. The default is `false`.<br> | default: false; example: true |
| `expiration_date` | string (schema `ExpirationDate`) | no | Card expiration date (format = yymm). If passed, the card expiration date is not calculated using the "Card expiration (# of months)" program parameter.<br> | example: "2803" |
| `validity_period_hours` | integer (schema `ValidityPeriodHours`) | no | How long, in hours, the card is valid. Cannot exceed the card's `expiration_date`. Once this period is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br><br>This field is used to calculate the datetime value for `valid_until`.<br><br>For `VIRTUAL` and `PLASTIC` cards. Setting this field for `TEMPORARY` or `RECURRING` cards returns a **400 Bad request** error.  <br> | example: 240 |
| `atm_change_online_pin_when_script_sent` | boolean (schema `ATMchangeOnlinePinWhenScriptSent`) | no | During ATM transactions, should the card's online PIN be updated when the offline PIN change script is sent to the terminal for execution? <br><br>If `false`, the online PIN is only updated after a subsequent transaction, once the Pismo platform verifies - via the card's CVR (Card Verification Results) — that the offline script was successfully applied. <br><br>Default is `false`.<br> | default: false; example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Reissue card response | `application/json`: object (schema `ReissueCardResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 409 | Specified resource status conflict with current request |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program` | object | no |  |  |
| `program.id` | string | no | Program ID |  |
| `account` | object | no |  |  |
| `account.id` | integer (schema `AccountID`) | no | Pismo account ID | example: 7654776 |
| `customer` | object | no |  |  |
| `customer.id` | integer (schema `CustomerID`) | no | Pismo customer ID | example: 765476676 |
| `org` | object | no |  |  |
| `org.id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `id` | integer | no | Update ID |  |
| `status` | string (schema `CardStatus`) | no | Card status enum. Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete list.<br> | example: "NORMAL" |
| `issuing_date` | string (schema `IssuingDate`) | no | Date/time when card was issued in RFC3339 format, i.e., 2019-07-03T17:23:18Z | example: "2019-07-03T17:23:18Z" |
| `expiration_date` | string (schema `ExpirationDate`) | no | Card expiration date (format = yymm). If passed, the card expiration date is not calculated using the "Card expiration (# of months)" program parameter.<br> | example: "2803" |
| `printed_name` | string (schema `PrintedName`) | no | Printed/embossed card name.<br><br>Currently, you have 3 ways to populate this field:<br>   <br>   1. During account creation via the `application.applicant.personal.social_name` field.<br>   2. During account creation via the `application.applicant.personal.name` field when the field in #1 is not set.<br>   3. Passing the `printed_name` field during card creation, updating a card, or when reissuing a card. This takes priority over #1 and #2.<br><br>No letters with accents, numbers, or special characters - only letters (a-z\|A-Z) and space, as specified in the <a href="https://emvlab.org/emvtags/show/t5F20/" target="_blank">ISO EMV tag 5F20</a> for cardholder name.<br><br>**REQUIRED** for an `UNNUMBERED` card (Card created without PIN or PAN that issuer defines at some point in the future.)<br> | minLength: 2; maxLength: 26 |
| `name` | string (schema `CardAlias`) | no | Card alias name for a `VIRTUAL` card. <br><br>This field is **REQUIRED** to be unique for each `VIRTUAL` card a customer owns.<br><br>No matter what is passed for a `PLASTIC` card, the value is always `PLASTIC`.<br> | minLength: 1; maxLength: 50; example: "Vacation card" |
| `mode` | string (schema `Mode`) | no | Mode enum:<br>`CREDIT` - Single credit card<br>`DEBIT` - Single debit card<br>`COMBO` - Card has both a credit and debit *mode*, meaning it is associated with both a credit and debit program and account.<br>`MULTIPLE` -  Combination card created with the DEPRECATED [Create combo card](ref:post-v1-combocard-relationship) endpoint. <br><br>For more information, refer to the [mode documentation](doc:cards-overview-1#create-a-combination-card-with-card-modes) in the Card management guide.<br> | enum: ["CREDIT", "DEBIT", "COMBO", "MULTIPLE"]; example: "CREDIT" |
| `track_number` | integer | no | Sequential counter incremented every time card is reissued. | example: 2 |
| `transaction_limit` | string (schema `TransactionLimit`) | no | Optional for virtual cards. Maximum amount allowed per transaction. Set up to the approved limit. If not set, account limit is used. | example: "500.00" |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |
| `type` | string (schema `CardType`) | no | Card type enum:<br> * `PLASTIC` - Physical card - plastic or metal.<br> * `VIRTUAL` - Digital card with fixed PAN and dynamic CVV.<br> * `TEMPORARY` - Virtual card with a fixed PAN and CVV meant for short-term use, typically 24 hours. For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards) in the Cards management guide.<br> * `RECURRING` - Virtual card with a fixed PAN and CVV originally meant for use with recurring subscriptions. This type is being **DEPRECATED** and it is recommended you use `VIRTUAL` instead. <br> | enum: ["PLASTIC", "VIRTUAL", "RECURRING", "TEMPORARY"]; example: "VIRTUAL" |
| `validity_period_hours` | integer (schema `ValidityPeriodHours`) | no | How long, in hours, the card is valid. Cannot exceed the card's `expiration_date`. Once this period is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br><br>This field is used to calculate the datetime value for `valid_until`.<br><br>For `VIRTUAL` and `PLASTIC` cards. Setting this field for `TEMPORARY` or `RECURRING` cards returns a **400 Bad request** error.  <br> | example: 240 |
| `valid_until` | string (schema `ValidUntil2`) | no | Card is valid until this datetime. ISO 8601 format. Once this time is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br>This field's value is calculated using the `validity_period_hours`. <br> | example: "2021-07-03T17:23:18Z" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-create-1` | https://developers.pismo.io/events/docs/cards-create-1 |
| `cards-update-1` | https://developers.pismo.io/events/docs/cards-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;409;500`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-CARD-bin-override-feature`, `KU-CARD-card-lifecycle-and-statuses`, `KU-CARD-card-reissuing`, `KU-CARD-card-tokenization-process-and-onboarding`, `KU-CARD-cards-overview-1`, `KU-CARD-physical-card-embossing`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/cards/v1/reissue/reasons operationId=get-reissue-reasons -->
### `GET /cards/v1/reissue/reasons` — List reissue reasons

- **operationId:** `get-reissue-reasons`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Card reissue`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Returns a paginated list of reissue reasons for the tenant.
>
> Supports filtering by enabled status and cursor-based pagination.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `limit` | query | no | integer | Maximum number of items to return per page | default: 10; minimum: 1; maximum: 50; example: 10 |
| `nextCursor` | query | no | integer | Pagination cursor | minimum: 0; example: 124 |
| `enabled` | query | no | boolean | Enabled status filter | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `GetReasonsResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `ReasonResponse`) | no |  |  |
| `pagination` | object (schema `Pagination`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-reissuing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/cards/v1/reissue/reasons operationId=create-reissue-reason -->
### `POST /cards/v1/reissue/reasons` — Create reissue reason

- **operationId:** `create-reissue-reason`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Card reissue`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a new reissue reason.
>
> All fields are required when creating a new reason.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `CreateReasonRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `ReissueDescription`) | yes | Reissue reason description | minLength: 1; maxLength: 255; example: "Card was lost by the customer" |
| `must_block` | boolean (schema `MustBlock`) | yes | Should a `PLASTIC` card be canceled upon reissue or can it be used until the new card is activated?<br><br> `VIRTUAL` cards are automatically canceled when reissued, regardless of this setting.<br> | example: true |
| `must_charge` | boolean (schema `MustCharge`) | yes | Should the reissue be charged?<br><br> This field is information only as only issuers can make debit entries to a customer's account.<br> | example: true |
| `cost` | number (schema `ReissueCost`) | yes | Reissue card cost | example: 20.5 |
| `type` | string (schema `ReissueType`) | yes | Issuer-defined reissue reason enum |  |
| `enabled` | boolean (schema `ReissueEnabled`) | yes | Is reason active?<br><br> This field is for information only and allows the issuer to provide only active reasons for re-issuance.<br> | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ReasonResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ReasonId`) | no | Reissue reason identifier. You can get reason IDs using the [List reissue reasons](ref:get-reissue-reasons) endpoint. The `must_block` flag comes from the reissue reason object. <br> | example: 123 |
| `description` | string (schema `ReissueDescription`) | no | Reissue reason description | minLength: 1; maxLength: 255; example: "Card was lost by the customer" |
| `must_block` | boolean (schema `MustBlock`) | no | Should a `PLASTIC` card be canceled upon reissue or can it be used until the new card is activated?<br><br> `VIRTUAL` cards are automatically canceled when reissued, regardless of this setting.<br> | example: true |
| `must_charge` | boolean (schema `MustCharge`) | no | Should the reissue be charged?<br><br> This field is information only as only issuers can make debit entries to a customer's account.<br> | example: true |
| `cost` | number (schema `ReissueCost`) | no | Reissue card cost | example: 20.5 |
| `type` | string (schema `ReissueType`) | no | Issuer-defined reissue reason enum |  |
| `enabled` | boolean (schema `ReissueEnabled`) | no | Is reason active?<br><br> This field is for information only and allows the issuer to provide only active reasons for re-issuance.<br> | example: true |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-reissuing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PATCH path=/cards/v1/reissue/reasons/{id} operationId=update-reissue-reason -->
### `PATCH /cards/v1/reissue/reasons/{id}` — Update reissue reason

- **operationId:** `update-reissue-reason`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Card reissue`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Updates an existing reissue reason.
>
> At least one field must be provided. Only the fields provided will be updated.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Reissue reason identifier. You can get reason IDs using the [List reissue reasons](ref:get-reissue-reasons) endpoint. The `must_block` flag comes from the reissue reason object. <br> | example: 123 |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `UpdateReasonRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `ReissueDescription`) | no | Reissue reason description | minLength: 1; maxLength: 255; example: "Card was lost by the customer" |
| `must_block` | boolean (schema `MustBlock`) | no | Should a `PLASTIC` card be canceled upon reissue or can it be used until the new card is activated?<br><br> `VIRTUAL` cards are automatically canceled when reissued, regardless of this setting.<br> | example: true |
| `must_charge` | boolean (schema `MustCharge`) | no | Should the reissue be charged?<br><br> This field is information only as only issuers can make debit entries to a customer's account.<br> | example: true |
| `cost` | number (schema `ReissueCost`) | no | Reissue card cost | example: 20.5 |
| `type` | string (schema `ReissueType`) | no | Issuer-defined reissue reason enum |  |
| `enabled` | boolean (schema `ReissueEnabled`) | no | Is reason active?<br><br> This field is for information only and allows the issuer to provide only active reasons for re-issuance.<br> | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `ReasonResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ReasonId`) | no | Reissue reason identifier. You can get reason IDs using the [List reissue reasons](ref:get-reissue-reasons) endpoint. The `must_block` flag comes from the reissue reason object. <br> | example: 123 |
| `description` | string (schema `ReissueDescription`) | no | Reissue reason description | minLength: 1; maxLength: 255; example: "Card was lost by the customer" |
| `must_block` | boolean (schema `MustBlock`) | no | Should a `PLASTIC` card be canceled upon reissue or can it be used until the new card is activated?<br><br> `VIRTUAL` cards are automatically canceled when reissued, regardless of this setting.<br> | example: true |
| `must_charge` | boolean (schema `MustCharge`) | no | Should the reissue be charged?<br><br> This field is information only as only issuers can make debit entries to a customer's account.<br> | example: true |
| `cost` | number (schema `ReissueCost`) | no | Reissue card cost | example: 20.5 |
| `type` | string (schema `ReissueType`) | no | Issuer-defined reissue reason enum |  |
| `enabled` | boolean (schema `ReissueEnabled`) | no | Is reason active?<br><br> This field is for information only and allows the issuer to provide only active reasons for re-issuance.<br> | example: true |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/wallet/v1/cards/reissue/reasons operationId=get-v1-card-reissue-reasons -->
### `GET /wallet/v1/cards/reissue/reasons` — Get card reissue reasons (outdated)

- **operationId:** `get-v1-card-reissue-reasons`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Card reissue`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> This endpoint is outdated, call the [List reissue reasons](ref:get-reissue-reasons) endpoint instead.
>
> Get all reissue reasons together with associated costs.
>
> To register reasons for reissue:
>
> [Open a Jira ticket](doc:opening-a-service-desk-ticket) with type  = **Settings** and enter the data below:
>
> `cost` - Reissue cost value. This field is for information only - only issuers can make debit entries to a customer's account.
>
> `must_block` - Whether the card is canceled at reissue time or can transact until new card is activated.
>
> `description` - Reason description.
>
> `must_charge` - Will reissue be charged? This field is for information only as only the issuer can make debit entries to a customer's account.
>
> `type` - Issuer defined reissue reason enum value

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Reissue reasons | `application/json`: array of object (schema `ReissueReasons`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-reissuing`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ReasonResponse -->
### Schema `ReasonResponse`

Pointer: `#/components/schemas/ReasonResponse`. Type: object (schema `ReasonResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ReasonId`) | no | Reissue reason identifier. You can get reason IDs using the [List reissue reasons](ref:get-reissue-reasons) endpoint. The `must_block` flag comes from the reissue reason object. <br> | example: 123 |
| `description` | string (schema `ReissueDescription`) | no | Reissue reason description | minLength: 1; maxLength: 255; example: "Card was lost by the customer" |
| `must_block` | boolean (schema `MustBlock`) | no | Should a `PLASTIC` card be canceled upon reissue or can it be used until the new card is activated?<br><br> `VIRTUAL` cards are automatically canceled when reissued, regardless of this setting.<br> | example: true |
| `must_charge` | boolean (schema `MustCharge`) | no | Should the reissue be charged?<br><br> This field is information only as only issuers can make debit entries to a customer's account.<br> | example: true |
| `cost` | number (schema `ReissueCost`) | no | Reissue card cost | example: 20.5 |
| `type` | string (schema `ReissueType`) | no | Issuer-defined reissue reason enum |  |
| `enabled` | boolean (schema `ReissueEnabled`) | no | Is reason active?<br><br> This field is for information only and allows the issuer to provide only active reasons for re-issuance.<br> | example: true |

<!-- schema: #/components/schemas/Pagination -->
### Schema `Pagination`

Pointer: `#/components/schemas/Pagination`. Type: object (schema `Pagination`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `next_cursor` | integer | no | Cursor to get the next page | nullable: true; example: 124 |
| `has_next` | boolean | no | Are more pages available? | example: true |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Card reissue`: POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue, GET /cards/v1/reissue/reasons, POST /cards/v1/reissue/reasons, PATCH /cards/v1/reissue/reasons/{id}, GET /wallet/v1/cards/reissue/reasons | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-bin-override-feature` — BIN override - shared account option
- `KU-CARD-card-lifecycle-and-statuses` — Card lifecycle and statuses
- `KU-CARD-card-reissuing` — Card reissuing
- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-CARD-cards-overview-1` — Cards management
- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-EVT-cards-data-events` — Card issuing - Cards
- `KU-EVT-catalogue-cards` — Event catalogue: cards
