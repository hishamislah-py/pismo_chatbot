---
ku_id: KU-API-card-issuing-cards--noname
title: 'API reference: Card issuing - Cards — Noname'
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
- create-bulk
- increment-bulk
- start-bulk
- post-v2-card-bind
- cancel-bulk
- post-v2-validate-card-cvv
related_kus:
- KU-CARD-card-lifecycle-and-statuses
- KU-CARD-card-reissuing
- KU-CARD-cards-overview-1
- KU-CARD-physical-card-embossing
- KU-EVT-cards-data-events
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Noname

**KU ID:** `KU-API-card-issuing-cards--noname` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Noname` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Noname card endpoints. Noname cards are batch-generated and not initially associated with customers, which occurs later.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /cards/v1/bulks` | `create-bulk` | Create noname card bulk | no |
| `PUT /cards/v1/bulks/{bulkID}` | `increment-bulk` | Increment noname card bulk | no |
| `POST /cards/v1/bulks/{bulkID}/start` | `start-bulk` | Start noname card bulk process | no |
| `PUT /wallet/v2/cards/{cardId}/noname/bind` | `post-v2-card-bind` | Associate noname card with customer | no |
| `POST /cards/v1/bulks/{bulkID}/cancel` | `cancel-bulk` | Cancel noname bulk operation | no |
| `POST /pcicards/v2/pcicards/cvv/{cardId}/noname/validate` | `post-v2-validate-card-cvv` | Validate noname card CVV | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/cards/v1/bulks operationId=create-bulk -->
### `POST /cards/v1/bulks` — Create noname card bulk

- **operationId:** `create-bulk`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Noname`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create up to 1000 noname cards per bulk/batch process. After calling this endpoint, call [Start noname card bulk process](ref:start-bulk) to begin the bulk/batch card creation and embossing process.
>
> Noname cards are batch-generated and not initially associated with customers, which occurs later. Noname cards work well for special use cases like gift cards or in countries or scenarios where a password or chip might be required but not necessarily a printed card name.
>
> One card is created for each `external_id` entered.
>
> For more information on embossing, refer to the [Physical card embossing](doc:physical-card-embossing) guide.
>
> For detailed information about embossing flows, refer to [Embossing flows](doc:physical-card-embossing#embossing-flows).

#### Request body

Required: yes

> Create bulk request body

**Content type `application/json`** — schema: object (schema `CreateBulk`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_ids` | array of string (schema `ExternalIDs`) | yes | Client assigned IDs for internal tracking purposes. One card is created for each ID. The maximum number of cards in one bulk/batch is 1000.<br><br>If you want to use more than 36 characters for your external IDs, please request a change in the embossing layout via a Jira ticket. By default, an embossing layout supports 36 digits for external IDs.<br> | minLength: 1; maxLength: 1000; example: ["8675309", "586038", "585603"]; items.minLength: 1; items.maxLength: 255 |
| `program_id` | integer (schema `ProgramID`) | yes | Pismo program ID | example: 7654 |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `pin_length` | integer (schema `PinLength`) | no | PIN length - 4 or 6 digits. Default is `4`. | enum: [4, 6]; default: 4 |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `embossing_group` | string (schema `EmbossingGroup`) | no | Embossing group name. Clients can work with multi-embossers. You can use this field to notify an embosser about a card request. If this parameter is not passed, and you work with multi-embossers, the default embosser is used. For more information, refer to the [Physical card embossing](doc:physical-card-embossing) guide.<br> | minLength: 2; maxLength: 32; example: "EM1-embosser" |
| `metadata` | object (schema `Metadata`) | no | <br>Any key-value object. Max length = 3200 bytes. This **must** be valid JSON data.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | maxLength: 3200; example: {"my-custom-key": "my-custom-value"} |
| `mode_type` | string (schema `ModeType`) | no | Mode type enum - `SINGLE` or `COMBO`.  A combo card can have both a credit and debit *mode*, meaning it is associated with both a credit and debit program and  account. A single card has one mode - credit or debit. Refer to the [mode documentation](doc:cards-overview-1#create-a-combination-card-with-card-modes) in the Card overview guide for more information.<br> | enum: ["SINGLE", "COMBO"]; example: "COMBO" |
| `validity_period_hours` | integer (schema `ValidityPeriodHours`) | no | How long, in hours, the card is valid. Cannot exceed the card's `expiration_date`. Once this period is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br><br>This field is used to calculate the datetime value for `valid_until`.<br><br>For `VIRTUAL` and `PLASTIC` cards. Setting this field for `TEMPORARY` or `RECURRING` cards returns a **400 Bad request** error.  <br> | example: 240 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Bulk created successfully | `application/json`: object (schema `BulkResponse`) |
| 400 | Bad Request |  |
| 409 | Specified resource status conflict with current request |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `id` | string | no | Bulk ID. | example: "Bkdj9999" |
| `metadata` | object (schema `Metadata`) | no | <br>Any key-value object. Max length = 3200 bytes. This **must** be valid JSON data.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | maxLength: 3200; example: {"my-custom-key": "my-custom-value"} |
| `program_id` | integer (schema `ProgramID`) | no | Pismo program ID | example: 7654 |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `size` | integer | no | Bulk size - number of cards | example: 1200 |
| `status` | string (schema `BulkStatus`) | no | Bulk noname card job status. | enum: ["CREATED", "RUNNING", "COMPLETED"]; example: "CREATED" |
| `validity_period_hours` | integer (schema `ValidityPeriodHours`) | no | How long, in hours, the card is valid. Cannot exceed the card's `expiration_date`. Once this period is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br><br>This field is used to calculate the datetime value for `valid_until`.<br><br>For `VIRTUAL` and `PLASTIC` cards. Setting this field for `TEMPORARY` or `RECURRING` cards returns a **400 Bad request** error.  <br> | example: 240 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-cards-overview-1`, `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/cards/v1/bulks/{bulkID} operationId=increment-bulk -->
### `PUT /cards/v1/bulks/{bulkID}` — Increment noname card bulk

- **operationId:** `increment-bulk`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Noname`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Increment noname card bulk/batch with up to 1000 additional cards.
> Use the bulk ID returned from [Create noname card bulk](ref:create-bulk).
>
> One card is created for each `external_id` entered.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bulkID` | path | yes | string | Bulk ID returned from `/cards/v1/bulks` (Create noname card bulk) endpoint |  |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `IncrementBulk`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_ids` | array of string (schema `ExternalIDs`) | yes | Client assigned IDs for internal tracking purposes. One card is created for each ID. The maximum number of cards in one bulk/batch is 1000.<br><br>If you want to use more than 36 characters for your external IDs, please request a change in the embossing layout via a Jira ticket. By default, an embossing layout supports 36 digits for external IDs.<br> | minLength: 1; maxLength: 1000; example: ["8675309", "586038", "585603"]; items.minLength: 1; items.maxLength: 255 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Bulk was incremented | `application/json`: object (schema `BulkResponse`) |
| 400 | Bad Request |  |
| 404 | The specified resource was not found |  |
| 409 | Specified resource status conflict with current request |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `id` | string | no | Bulk ID. | example: "Bkdj9999" |
| `metadata` | object (schema `Metadata`) | no | <br>Any key-value object. Max length = 3200 bytes. This **must** be valid JSON data.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | maxLength: 3200; example: {"my-custom-key": "my-custom-value"} |
| `program_id` | integer (schema `ProgramID`) | no | Pismo program ID | example: 7654 |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `size` | integer | no | Bulk size - number of cards | example: 1200 |
| `status` | string (schema `BulkStatus`) | no | Bulk noname card job status. | enum: ["CREATED", "RUNNING", "COMPLETED"]; example: "CREATED" |
| `validity_period_hours` | integer (schema `ValidityPeriodHours`) | no | How long, in hours, the card is valid. Cannot exceed the card's `expiration_date`. Once this period is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br><br>This field is used to calculate the datetime value for `valid_until`.<br><br>For `VIRTUAL` and `PLASTIC` cards. Setting this field for `TEMPORARY` or `RECURRING` cards returns a **400 Bad request** error.  <br> | example: 240 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;409;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/cards/v1/bulks/{bulkID}/start operationId=start-bulk -->
### `POST /cards/v1/bulks/{bulkID}/start` — Start noname card bulk process

- **operationId:** `start-bulk`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Noname`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Start noname card bulk/batch process. Each card is identified with an `external_id`.  This endpoint starts the process begun with [Create noname card bulk](ref:create-bulk). Pass the bulk ID returned from that endpoint here.
>
> Each card created generates an event - [Card created](https://developers.pismo.io/events/docs/cards-create-1) - with event data that includes the card ID, bulk ID, and external ID. You pass the card ID to the [Associate noname card with customer](ref:post-v2-card-bind) endpoint. For more information on events and setting up event notifications, rerfer to the [Data and reporting](doc:data-reporting-overview) guide.
>
> For more information on embossing, refer to the [Physical card embossing](doc:physical-card-embossing) guide.
>
> For detailed information about embossing flows, refer to [Embossing flows](doc:physical-card-embossing#embossing-flows).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bulkID` | path | yes | string | Bulk ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Bulk was started and will be processed asynchronously | `application/json`: object (schema `BulkResponse`) |
| 400 | Bad Request |  |
| 404 | The specified resource was not found |  |
| 409 | Specified resource status conflict with current request |  |
| 500 | Internal server error |  |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `abu_enabled` | boolean (schema `ABUenabled`) | no | <br>This field is **DEPRECATED**. For more information, refer to the [ABU documentation](doc:cards-overview-1#mastercards-automatic-billing-updater-option) in the Cards overview guide.<br><br><br>When a card is created or reissued, or its account credentials change, Mastercard is notified if this feaure is enabled. Notification updates are sent to Mastercard on a daily basis. <br><br>For more information, refer to Mastercard's <a href="https://developer.mastercard.com/product/automatic-billing-updater-abu/" target="_blank">ABU</a> documentation.<br> | deprecated: true; example: true |
| `contactless_enabled` | boolean (schema `Contactless`) | no | For physical cards. Is card enabled for contactless transactions? <br> <br>With contactless transactions, you hold or tap the card on contactless-enabled card reader to complete a transaction. This requires that both the card and the terminal have Near Field Communication (NFC) technology. Most embossers can create plastic contactless cards.<br><br>Default is `true`.<br> | default: true; example: false |
| `embossing_custom_field` | string (schema `EmbossingCustomField`) | no | For physical cards. Additional information for embossing company. For example: tracking number or whether the card should be plastic or metal. <br><br>You can use this field for any embossing needs specific to your business.  Whatever is sent must be agreed upon with the embosser&mdash;what to send, what values to send, what format to send, what size to send for each value, and so on.<br> | maxLength: 1000; example: "Tracking ID = 5859930" |
| `id` | string | no | Bulk ID. | example: "Bkdj9999" |
| `metadata` | object (schema `Metadata`) | no | <br>Any key-value object. Max length = 3200 bytes. This **must** be valid JSON data.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | maxLength: 3200; example: {"my-custom-key": "my-custom-value"} |
| `program_id` | integer (schema `ProgramID`) | no | Pismo program ID | example: 7654 |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `size` | integer | no | Bulk size - number of cards | example: 1200 |
| `status` | string (schema `BulkStatus`) | no | Bulk noname card job status. | enum: ["CREATED", "RUNNING", "COMPLETED"]; example: "CREATED" |
| `validity_period_hours` | integer (schema `ValidityPeriodHours`) | no | How long, in hours, the card is valid. Cannot exceed the card's `expiration_date`. Once this period is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br><br>This field is used to calculate the datetime value for `valid_until`.<br><br>For `VIRTUAL` and `PLASTIC` cards. Setting this field for `TEMPORARY` or `RECURRING` cards returns a **400 Bad request** error.  <br> | example: 240 |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-create-1` | https://developers.pismo.io/events/docs/cards-create-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;404;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/wallet/v2/cards/{cardId}/noname/bind operationId=post-v2-card-bind -->
### `PUT /wallet/v2/cards/{cardId}/noname/bind` — Associate noname card with customer

- **operationId:** `post-v2-card-bind`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Noname`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Bind an account and customer to a noname card, which changes its status to `CREATED`. The card is then treated as a normal physical plastic or metal card.
>
> You have to pass this endpoint a noname card's ID. Card IDs are generated when the [Start noname card bulk process](ref:start-bulk) endpoint is called.  This endpoint generates an event for each card - [Card created](https://developers.pismo.io/events/docs/cards-create-1) - with event data that includes the card ID, bulk ID, and external ID. Refer to the [Data and reporting](doc:data-reporting-overview) guide for information on events and setting up event notifications.
>
> The bind operation is completed asynchronously and generates a [Customer bound to noname card](https://developers.pismo.io/events/docs/cards-bind-card-1) event. Make sure the operation has completed and the event generated before attempting to access or use the associated card. 
>
> **Card reissuing**
>
> * You can use this endpoint to reissue a card&mdash;replacing the card to be reissued with a noname card, which is then treated as a normal physical card. If a card to be replaced is entered (`reissued_card_id`), the [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event is also generated. 
>
> * If you attempt to reissue a card to a card that has already been associated, meaning it is no longer a noname card and no longer has an `UNBOUND` status, you will get a **409 Conflict** error. 
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `x-account-id` | header | yes | string | Account ID | example: "8675309" |
| `x-customer-id` | header | yes | integer | Pismo customer ID | example: 125555 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `BindRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reissued_card_id` | integer (schema `ReissuedCardID`) | no | Last issued card ID | example: 123456 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Your request was accepted. The bind operation is made asynchronously, check the event [Customer bound to noname card](https://developers.pismo.io/events/docs/cards-bind-card-1). |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 409 | Specified resource status conflict with current request |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-bind-card-1` | https://developers.pismo.io/events/docs/cards-bind-card-1 |
| `cards-create-1` | https://developers.pismo.io/events/docs/cards-create-1 |
| `cards-update-1` | https://developers.pismo.io/events/docs/cards-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;409;500`, has examples `False`, emits events `3`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-lifecycle-and-statuses`, `KU-CARD-card-reissuing`, `KU-CARD-cards-overview-1`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/cards/v1/bulks/{bulkID}/cancel operationId=cancel-bulk -->
### `POST /cards/v1/bulks/{bulkID}/cancel` — Cancel noname bulk operation

- **operationId:** `cancel-bulk`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Noname`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel noname bulk operation.
>
> The canceling operation is executed asynchronously and generates a [Noname cancellation](https://developers.pismo.io/events/docs/cards-noname-cancellation-1) event when done.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bulkID` | path | yes | string | Bulk ID | example: "48894-kkfi8-9484-kdkd" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CancelBulkRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cancel_type` | string | yes |  | enum: ["FULL", "PARTIAL"] |
| `external_ids` | array of string | no | External ID array. If `cancel_type` = `PARTIAL`, this field is **REQUIRED**. The maximum number of cards in one bulk/batch is 1000.<br> | minLength: 1; maxLength: 1000; items.minLength: 1; items.maxLength: 255 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Bulk will be canceled asynchronously |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 406 | Request is out-of-range. |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-noname-cancellation-1` | https://developers.pismo.io/events/docs/cards-noname-cancellation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;406;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/pcicards/v2/pcicards/cvv/{cardId}/noname/validate operationId=post-v2-validate-card-cvv -->
### `POST /pcicards/v2/pcicards/cvv/{cardId}/noname/validate` — Validate noname card CVV

- **operationId:** `post-v2-validate-card-cvv`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Noname`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Validates the given card's CVV. Only for cards that have not yet been [bound to an account and customer](ref:post-v2-card-bind).
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

> Request with CVV to be validated

**Content type `application/json`** — schema: object (schema `ValidateCVV`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cvv` | string | yes | CVV to be validated against card info | minLength: 3; maxLength: 3 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | CVV was validated successfully |  |
| 400 | CVV was not validated |  |
| 500 | Internal server error |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;500`, has examples `False`, emits events `0`, deprecated `False`.

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
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Noname`: POST /cards/v1/bulks, PUT /cards/v1/bulks/{bulkID}, POST /cards/v1/bulks/{bulkID}/start, PUT /wallet/v2/cards/{cardId}/noname/bind, POST /cards/v1/bulks/{bulkID}/cancel, POST /pcicards/v2/pcicards/cvv/{cardId}/noname/validate | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-card-lifecycle-and-statuses` — Card lifecycle and statuses
- `KU-CARD-card-reissuing` — Card reissuing
- `KU-CARD-cards-overview-1` — Cards management
- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-EVT-cards-data-events` — Card issuing - Cards
- `KU-EVT-catalogue-cards` — Event catalogue: cards
