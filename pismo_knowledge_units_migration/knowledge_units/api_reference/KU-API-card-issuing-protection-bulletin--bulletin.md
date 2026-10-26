---
ku_id: KU-API-card-issuing-protection-bulletin--bulletin
title: 'API reference: Card issuing - Protection Bulletin — Bulletin'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Protection_Bulletin.yaml
  sha256: 6c5641a54569d51d4df8b976968622e18c8c6710cb93bf06b7088ccdadcc7a8f
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
- list-v1-bulletin
- post-v1-bulletin
- get-v1-bulletin
- delete-v1-bulletin
related_kus:
- KU-CARD-protection-bulletin
- KU-ERR-codes-acq-to-esma
specification_version: 2.0.3
---

# API reference: Card issuing - Protection Bulletin — Bulletin

**KU ID:** `KU-API-card-issuing-protection-bulletin--bulletin` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Bulletin` in `api-specs/Card_issuing_-_Protection_Bulletin.yaml` (“Card issuing - Protection Bulletin”, version `2.0.3`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage cards with the Protection Bulletin

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/bulletin` | `list-v1-bulletin` | List cards in Protection Bulletin | no |
| `POST /v1/bulletin` | `post-v1-bulletin` | Register card with Protection Bulletin | no |
| `GET /v1/bulletin/{card_id}` | `get-v1-bulletin` | Get Protection Bulletin card | no |
| `DELETE /v1/bulletin/{card_id}` | `delete-v1-bulletin` | Delete card from Protection Bulletin | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error.<br>

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Protection_Bulletin.yaml method=GET path=/v1/bulletin operationId=list-v1-bulletin -->
### `GET /v1/bulletin` — List cards in Protection Bulletin

- **operationId:** `list-v1-bulletin`
- **Specification:** `api-specs/Card_issuing_-_Protection_Bulletin.yaml` (Card issuing - Protection Bulletin)
- **Server base URL(s):** `https://sandbox.pismolabs.io/protection-bulletin`
- **Tags:** `Bulletin`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get all Pismo-issued cards in the Protection Bulletin with filtering options.
>
>  **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `begin_date` | query | yes | string | Beginning date filter, format = `yyyy-mm-dd` | example: "2025-01-01" |
| `end_date` | query | yes | string | End date filter, format = `yyyy-mm-dd` | example: "2025-01-30" |
| `per_page` | query | no | integer | Number of items per page to return. Default is `10`. | default: 10; minimum: 1; example: 20 |
| `page` | query | no | integer | Page to return. Default is `1`. | default: 1; minimum: 1; example: 2 |
| `program_id` | query | no | number | Pismo program ID | example: 1010 |
| `network_brand_type` | query | no | string | Card network brand. | enum: ["ELO", "MASTERCARD", "VISA"]; example: "ELO" |
| `status` | query | no | string | Request processing status. | enum: ["PENDING", "SUCCESS", "FAILED"]; example: "PENDING" |
| `state` | query | no | string | Is card blocked or not in the network brand? <br><br>When empty, it means the network did not successfully receive the action.<br> | enum: ["", "BLOCKED", "UNBLOCKED"]; example: "BLOCKED" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `BulletinResponseListModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorMessageModel`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorMessageModel`) |
| 504 | Gateway Timeout | `application/json`: object (schema `ErrorMessageModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page. | example: 1 |
| `pages` | integer (schema `Pages`) | no | Total number of pages. | example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Items per page. | example: 100 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items in page. | example: 10 |
| `items` | array of object (schema `Items`) | no | List of Bulletin Cards |  |
| `items[].card_id` | number (schema `CardID`) | no | Pismo card ID. | example: 10203040 |
| `items[].org_id` | string (schema `OrgID`) | no | Pismo organization/tenant ID. | example: "TN-123XXX-XXXXXX-XXXXXXX" |
| `items[].program_id` | number (schema `ProgramID`) | no | Pismo program ID. | example: 1010 |
| `items[].network_brand_type` | string (schema `NetworkBrandType`) | no | Card network brand. | enum: ["ELO", "MASTERCARD", "VISA"]; example: "ELO" |
| `items[].created_at` | string (schema `CreatedAt`) | no | Date and time when the Protection Bulletin registration was created. Format = ISO 8601. | format: "yyyy-mm-dd hh:mm:ss"; example: "2025-04-22 20:31:50" |
| `items[].updated_at` | string (schema `UpdatedAt`) | no | Date and time when the Protection Bulletin was updated. Format = ISO 8601.<br> | format: "yyyy-mm-dd hh:mm:ss"; example: "2025-04-22 20:31:50" |
| `items[].network_track_number` | string (schema `NetworkTrackNumber`) | no | Created in the internal system to track the card's event history. This is a combination between the tenant and the truncated random uuid. | example: "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c" |
| `items[].state` | string (schema `State`) | no | Is card blocked or not in the network brand? When the state is empty, it means the network brand did not successfully receive any action.<br> | enum: ["", "BLOCKED", "UNBLOCKED"]; example: "BLOCKED" |
| `items[].status` | string (schema `Status`) | no | Request processing status. | enum: ["PENDING", "SUCCESS", "FAILED"]; example: "PENDING" |
| `items[].purge_date` | string (schema `PurgeDate`) | no | Date when the card will be removed from the Protection Bulletin in the network brand. Format = yyyy-mm-dd.<br> | format: "yyyy-mm-dd"; example: "2025-04-22" |
| `items[].was_automatically_purged` | boolean (schema `WasAutomaticallyPurged`) | no | Was card removed from the network brand on the purge date?<br> | example: true |
| `items[].card_track_number` | number (schema `CardTrackNumber`) | no | Pismo card track number. | example: 1 |
| `items[].region_code` | array of string (schema `RegionCode`) | no | Region code contains one or more Account Screen Authorization File (ASAF) region codes that define the distribution of a Visa cardholder account number in Card Recovery Bulletin Service files. **REQUIRED** for Visa. <br /><br>  `0` - No Bulletin / V.I.P. Only (cannot be combined with other region codes)<br /><br>  `A` - All Asia-Pacific region countries<br /><br>  `B` - All  Central Europe, Middle East, and Africa (CEMEA) region countries.<br /><br>  `C` - All Visa Canada<br /><br>  `D` - National Card Recovery Bulletin<br /><br>  `E` - All European countries<br /><br>  `F` - All Latin America and Caribbean (LAC) region countries <br /><br><br>Region codes can be in any order, except no other region code can be specified in combination with region code 0.<br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Table 215: Field 127E.2 Account Screen Authorization File (ASAF) Region Codes<br> | items.enum: ["0", "A", "B", "C", "D", "E", "F"] |

##### Response 401

401 Example `Missing or invalid Authorization header`:

```json
{
  "code": "EBLT0005",
  "message": "Missing or invalid Authorization header",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing account-id`:

```json
{
  "code": "EBLT0006",
  "message": "Invalid Authorization header, missing account-id",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing tenant`:

```json
{
  "code": "EBLT0007",
  "message": "Invalid Authorization header, missing tenant",
  "http_status_code": 401
}
```

##### Response 500

500 Example `Something went wrong when try to process a request in another service`:

```json
{
  "code": "EBLT9998",
  "message": "Something went wrong when try to process a request in Programs API using ID: 123",
  "http_status_code": 500
}
```

500 Example `Something went wrong, please try again later`:

```json
{
  "code": "EBLT9999",
  "message": "Something went wrong, please try again later",
  "http_status_code": 500
}
```

##### Response 504

504 Example `Request timeout`:

```json
{
  "code": "EBLT0001",
  "message": "Request timeout",
  "http_status_code": 504
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 401 | `EBLT0005` | Missing or invalid Authorization header |
| 401 | `EBLT0006` | Invalid Authorization header, missing account-id |
| 401 | `EBLT0007` | Invalid Authorization header, missing tenant |
| 500 | `EBLT9998` | Something went wrong when try to process a request in Programs API using ID: 123 |
| 500 | `EBLT9999` | Something went wrong, please try again later |
| 504 | `EBLT0001` | Request timeout |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;500;504`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Protection_Bulletin.yaml method=POST path=/v1/bulletin operationId=post-v1-bulletin -->
### `POST /v1/bulletin` — Register card with Protection Bulletin

- **operationId:** `post-v1-bulletin`
- **Specification:** `api-specs/Card_issuing_-_Protection_Bulletin.yaml` (Card issuing - Protection Bulletin)
- **Server base URL(s):** `https://sandbox.pismolabs.io/protection-bulletin`
- **Tags:** `Bulletin`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a Pismo-issued card with the Protection Bulletin. This feature is available for Elo, Mastercard and Visa.
>
> The Protection Bulletin is used before a transaction takes place in cases where the issuer is temporarily offline and unable to authorize or decline a transaction. In a process known as *stand-in*, the card network authorizes or declines the transaction to avoid creating problems for the cardholder and merchant, based on how the card was added to the Protection Bulletin. Once the issuer is back online, the card network lets them know what was authorized or declined while they were down.
>
> You can add a card to the Protection Bulletin with this endpoint or [setting a card rule](ref:post-v1-bulletin-setup) so that when a card's status changes to a rule's configured status, the card is automatically added to the Protection Bulletin.
>
> For more information, refer to [Protection Bulletin](doc:protection-bulletin).
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `x-customer-id` | header | yes | number | Pismo customer ID. Must be associated with account whose ID is embedded in the access token.<br> |  |

#### Request body

Required: yes

> Bulletin data. Enter data for one object, depending on brand (Elo, Visa, or Mastercard)

**Content type `application/json`** — schema: anyOf: object (schema `Bulletin_Post_Elo_Model`), object (schema `Bulletin_Post_Mastercard_Model`), object (schema `Bulletin_Post_Visa_Model`)

_anyOf option 1: schema `Bulletin_Post_Elo_Model`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | number (schema `CardID`) | yes | Pismo card ID. | example: 10203040 |

_anyOf option 2: schema `Bulletin_Post_Mastercard_Model`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | number (schema `CardID`) | yes | Pismo card ID. | example: 10203040 |
| `reason` | string (schema `ReasonMastercard`) | yes | Reason for adding card to Protection Bulletin. **REQUIRED** for Mastercard. <br /><br>  `C` - Credit <br /><br>  `F` - Fraud <br /><br>  `G` - ATM premium listing <br /><br>  `L` - Lost <br /><br>  `O` - Other <br /><br>  `P` - Capture card <br /><br>  `S` - Stolen <br /><br>  `U` - Unauthorized use <br /><br>  `V` - Premium listing <br /><br>  `X` - Counterfeit <br /><br><br>Mastercard documentation: Customer Interface Specification - DE 120 (Record Data) Layout for MCC102 - Field ID 2 (Entry Reason)<br> | enum: ["C", "F", "G", "L", "O", "P", "S", "U", "V", "X"]; example: "F" |
| `purge_date` | string (schema `PurgeDateMastercard`) | no | Date when the card should be removed from the Protection Bulletin. Format = yyyy-mm-dd.<br><br>Mastercard documentation: Customer Interface Specification - DE 120 (Record Data) Layout for MCC102 - Field ID 8 (Issuer-defined Purge Date)<br> | example: "2024-10-22" |

_anyOf option 3: schema `Bulletin_Post_Visa_Model`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | number (schema `CardID`) | yes | Pismo card ID. | example: 10203040 |
| `reason` | string (schema `ReasonVisa`) | yes | Reason for adding card to Protection Bulletin. **REQUIRED** for Visa.<br /><br>  `04` - Pickup card<br /><br>  `05` - Do not honor<br /><br>  `07` - Pickup card, special condition<br /><br>  `11` - Approval for **VIP**<br /><br>  `14` - Invalid account number (no such number)<br /><br>  `41` - Lost card, pickup<br /><br>  `43` - Stolen card, pickup<br /><br>  `46` - Closed account<br /><br>  `54` - Expired card<br /><br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Table 214: Field 127E.1 Account Screen Authorization File (ASAF) Action Codes.<br> | enum: ["04", "05", "07", "11", "14", "41", "43", "46", "54"]; example: "04" |
| `region_code` | array of string (schema `RegionCode`) | yes | Region code contains one or more Account Screen Authorization File (ASAF) region codes that define the distribution of a Visa cardholder account number in Card Recovery Bulletin Service files. **REQUIRED** for Visa. <br /><br>  `0` - No Bulletin / V.I.P. Only (cannot be combined with other region codes)<br /><br>  `A` - All Asia-Pacific region countries<br /><br>  `B` - All  Central Europe, Middle East, and Africa (CEMEA) region countries.<br /><br>  `C` - All Visa Canada<br /><br>  `D` - National Card Recovery Bulletin<br /><br>  `E` - All European countries<br /><br>  `F` - All Latin America and Caribbean (LAC) region countries <br /><br><br>Region codes can be in any order, except no other region code can be specified in combination with region code 0.<br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Table 215: Field 127E.2 Account Screen Authorization File (ASAF) Region Codes<br> | items.enum: ["0", "A", "B", "C", "D", "E", "F"] |
| `card_track_number` | number (schema `CardTrackNumberVisa`) | yes | Pismo card track number.<br><br>The card track number sent to the Account Screen Authorization File (ASAF). If `1`, the first copy is sent. If `2`, the second copy is sent. If `0`, all copies are sent. A card might be added to the Protection Bulletin, before being voided and reissued, resulting in more than one copy. <br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Field 23: Card Sequence Number<br> | example: 1 |
| `purge_date` | string (schema `PurgeDateVisa`) | yes | Date when the card should be removed from the Protection Bulletin. Format = yyyy-mm-dd.<br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Field 73: Action Date<br> | example: "2024-10-22" |


Example `Register a Elo card`:

```json
{
  "card_id": 10203040
}
```

Example `Register a Mastercard card with purge date`:

```json
{
  "card_id": 10203040,
  "reason": "L",
  "purge_date": "2026-01-01T00:00:00.000Z"
}
```

Example `Register a Mastercard card without purge date`:

```json
{
  "card_id": 10203040,
  "reason": "L"
}
```

Example `Register a Visa card with purge date`:

```json
{
  "card_id": 10203040,
  "card_track_number": 0,
  "reason": "04",
  "region_code": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"
  ],
  "purge_date": "2026-01-01T00:00:00.000Z"
}
```

Example `Register a Visa card without purge date`:

```json
{
  "card_id": 10203040,
  "card_track_number": 0,
  "reason": "04",
  "region_code": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `BulletinResponseModel`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorMessageModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorMessageModel`) |
| 404 | Not Found | `application/json`: object (schema `ErrorMessageModel`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `ErrorMessageModel`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorMessageModel`) |
| 504 | Gateway Timeout | `application/json`: object (schema `ErrorMessageModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | number (schema `CardID`) | no | Pismo card ID. | example: 10203040 |
| `org_id` | string (schema `OrgID`) | no | Pismo organization/tenant ID. | example: "TN-123XXX-XXXXXX-XXXXXXX" |
| `program_id` | number (schema `ProgramID`) | no | Pismo program ID. | example: 1010 |
| `network_brand_type` | string (schema `NetworkBrandType`) | no | Card network brand. | enum: ["ELO", "MASTERCARD", "VISA"]; example: "ELO" |
| `created_at` | string (schema `CreatedAt`) | no | Date and time when the Protection Bulletin registration was created. Format = ISO 8601. | format: "yyyy-mm-dd hh:mm:ss"; example: "2025-04-22 20:31:50" |
| `updated_at` | string (schema `UpdatedAt`) | no | Date and time when the Protection Bulletin was updated. Format = ISO 8601.<br> | format: "yyyy-mm-dd hh:mm:ss"; example: "2025-04-22 20:31:50" |
| `network_track_number` | string (schema `NetworkTrackNumber`) | no | Created in the internal system to track the card's event history. This is a combination between the tenant and the truncated random uuid. | example: "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c" |
| `state` | string (schema `State`) | no | Is card blocked or not in the network brand? When the state is empty, it means the network brand did not successfully receive any action.<br> | enum: ["", "BLOCKED", "UNBLOCKED"]; example: "BLOCKED" |
| `status` | string (schema `Status`) | no | Request processing status. | enum: ["PENDING", "SUCCESS", "FAILED"]; example: "PENDING" |
| `purge_date` | string (schema `PurgeDate`) | no | Date when the card will be removed from the Protection Bulletin in the network brand. Format = yyyy-mm-dd.<br> | format: "yyyy-mm-dd"; example: "2025-04-22" |
| `was_automatically_purged` | boolean (schema `WasAutomaticallyPurged`) | no | Was card removed from the network brand on the purge date?<br> | example: true |
| `card_track_number` | number (schema `CardTrackNumber`) | no | Pismo card track number. | example: 1 |
| `region_code` | array of string (schema `RegionCode`) | no | Region code contains one or more Account Screen Authorization File (ASAF) region codes that define the distribution of a Visa cardholder account number in Card Recovery Bulletin Service files. **REQUIRED** for Visa. <br /><br>  `0` - No Bulletin / V.I.P. Only (cannot be combined with other region codes)<br /><br>  `A` - All Asia-Pacific region countries<br /><br>  `B` - All  Central Europe, Middle East, and Africa (CEMEA) region countries.<br /><br>  `C` - All Visa Canada<br /><br>  `D` - National Card Recovery Bulletin<br /><br>  `E` - All European countries<br /><br>  `F` - All Latin America and Caribbean (LAC) region countries <br /><br><br>Region codes can be in any order, except no other region code can be specified in combination with region code 0.<br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Table 215: Field 127E.2 Account Screen Authorization File (ASAF) Region Codes<br> | items.enum: ["0", "A", "B", "C", "D", "E", "F"] |
| `histories` | array of object (schema `BulletinResponseHistoryModel`) | no | Response history model for the Bulletin API. |  |
| `histories[].event` | string (schema `Event`) | no | Event performed in the request | enum: ["POST", "UPDATE", "DELETE"]; example: "POST" |
| `histories[].event_date` | string (schema `EventDate`) | no | Date and time when the event was received in the Protection Bulletin. | format: "yyyy-mm-dd hh:mm:ss"; example: "2025-04-22 20:31:50" |
| `histories[].status` | string (schema `Status`) | no | Request processing status. | enum: ["PENDING", "SUCCESS", "FAILED"]; example: "PENDING" |
| `histories[].reason` | string (schema `Reason`) | no | Reason that indicates why the card was added to the Protection Bulletin. | example: "L" |
| `histories[].network_track_number` | string (schema `NetworkTrackNumber`) | no | Created in the internal system to track the card's event history. This is a combination between the tenant and the truncated random uuid. | example: "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c" |
| `histories[].was_automatically_purged` | boolean (schema `WasAutomaticallyPurged`) | no | Was card removed from the network brand on the purge date?<br> | example: true |
| `histories[].card_track_number` | number (schema `CardTrackNumber`) | no | Pismo card track number. | example: 1 |
| `histories[].network_response_data` | string (schema `NetworkResponseData`) | no | Response JSON data received from the network brand.<br><br>The content of this field will indicate the original response from the network brand, whether success or failure. The example provided in this model is for illustrative purposes only.<br> | example: "{\\"status\\":\\"SUCCESS\\",\\"message\\":\\"Card added to Protection Bulletin\\"}" |
| `histories[].region_code` | array of string (schema `RegionCode`) | no | Region code contains one or more Account Screen Authorization File (ASAF) region codes that define the distribution of a Visa cardholder account number in Card Recovery Bulletin Service files. **REQUIRED** for Visa. <br /><br>  `0` - No Bulletin / V.I.P. Only (cannot be combined with other region codes)<br /><br>  `A` - All Asia-Pacific region countries<br /><br>  `B` - All  Central Europe, Middle East, and Africa (CEMEA) region countries.<br /><br>  `C` - All Visa Canada<br /><br>  `D` - National Card Recovery Bulletin<br /><br>  `E` - All European countries<br /><br>  `F` - All Latin America and Caribbean (LAC) region countries <br /><br><br>Region codes can be in any order, except no other region code can be specified in combination with region code 0.<br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Table 215: Field 127E.2 Account Screen Authorization File (ASAF) Region Codes<br> | items.enum: ["0", "A", "B", "C", "D", "E", "F"] |

201 Example `Register a Elo card`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "ELO",
  "created_at": "2025-04-22 20:31:50",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "status": "PENDING",
  "was_automatically_purged": true,
  "histories": [
    {
      "event": "POST",
      "event_date": "2025-04-22 20:31:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "was_automatically_purged": true,
      "network_response_data": "null",
      "card_track_number": 1
    }
  ]
}
```

201 Example `Register a Mastercard card`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "MASTERCARD",
  "created_at": "2025-04-22 20:31:50",
  "purge_date": "2026-01-01",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "status": "PENDING",
  "was_automatically_purged": true,
  "histories": [
    {
      "event": "POST",
      "event_date": "2025-04-22 20:31:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "reason": "O",
      "was_automatically_purged": false,
      "network_response_data": "null",
      "card_track_number": 1
    }
  ]
}
```

201 Example `Register a Visa card`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "VISA",
  "created_at": "2025-04-22 20:31:50",
  "purge_date": "2026-01-01",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "status": "PENDING",
  "was_automatically_purged": true,
  "card_track_number": 1,
  "region_code": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"
  ],
  "histories": [
    {
      "event": "POST",
      "event_date": "2025-04-22 20:31:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "reason": "04",
      "was_automatically_purged": false,
      "network_response_data": "null",
      "card_track_number": 1,
      "region_code": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F"
      ]
    }
  ]
}
```

##### Response 400

400 Example `Failed to parse request payload`:

```json
{
  "code": "EBLT0003",
  "message": "Failed to parse request payload",
  "http_status_code": 400
}
```

##### Response 401

401 Example `Missing or invalid Authorization header`:

```json
{
  "code": "EBLT0005",
  "message": "Missing or invalid Authorization header",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing account-id`:

```json
{
  "code": "EBLT0006",
  "message": "Invalid Authorization header, missing account-id",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing tenant`:

```json
{
  "code": "EBLT0007",
  "message": "Invalid Authorization header, missing tenant",
  "http_status_code": 401
}
```

##### Response 404

404 Example `Wallets returned not found`:

```json
{
  "code": "EBLT0009",
  "message": "Wallets returned [Not found] using ID: 123",
  "http_status_code": 404
}
```

##### Response 422

422 Example `Error while validating fields for all brands (header and payload)`:

```json
{
  "code": "BBLT0001",
  "message": "Error while validating fields",
  "http_status_code": 422,
  "details": {
    "header": [
      {
        "field": "x-customer-id",
        "message": "This field is required"
      }
    ],
    "payload": [
      {
        "field": "card_id",
        "message": "This field is required"
      },
      {
        "field": "purge_date",
        "message": "This field has an invalid date format. The correct format is yyyy-MM-dd"
      }
    ]
  }
}
```

422 Example `Error while validating fields for Mastercard`:

```json
{
  "code": "BBLT0001",
  "message": "Error while validating fields",
  "http_status_code": 422,
  "details": {
    "payload": [
      {
        "field": "reason",
        "message": "This field is required"
      },
      {
        "field": "reason",
        "message": "This field has an invalid value (A). The accepted values are: C, F, G, L, O, P, S, U, V, X"
      },
      {
        "field": "purge_date",
        "message": "This field need to be greater than 2025-10-20 (180 days)"
      }
    ]
  }
}
```

422 Example `Error while validating fields for Visa`:

```json
{
  "code": "BBLT0001",
  "message": "Error while validating fields",
  "http_status_code": 422,
  "details": {
    "payload": [
      {
        "field": "reason",
        "message": "This field is required"
      },
      {
        "field": "reason",
        "message": "This field has an invalid value (00). The accepted values are: 04, 05, 07, 11, 14, 41, 43, 46, 54"
      },
      {
        "field": "region_code",
        "message": "This field has an invalid value (X). The accepted values are: 0, A, B, C, D, E, F"
      },
      {
        "field": "region_code",
        "message": "The value '0' in region_code is not allowed with other region_code."
      }
    ]
  }
}
```

422 Example `Bulletin card has an ongoing event in the network brand`:

```json
{
  "code": "BBLT0003",
  "message": "Bulletin card has an ongoing event in the network brand.",
  "http_status_code": 422
}
```

422 Example `Bulletin card is already BLOCKED`:

```json
{
  "code": "BBLT0004",
  "message": "Bulletin card is already BLOCKED",
  "http_status_code": 422
}
```

422 Example `The card with ID does not have a network brand`:

```json
{
  "code": "BBLT0005",
  "message": "The card with ID 123 does not have a network brand.",
  "http_status_code": 422
}
```

##### Response 500

500 Example `Something went wrong when try to process a request in another service`:

```json
{
  "code": "EBLT9998",
  "message": "Something went wrong when try to process a request in Programs API using ID: 123",
  "http_status_code": 500
}
```

500 Example `Something went wrong, please try again later`:

```json
{
  "code": "EBLT9999",
  "message": "Something went wrong, please try again later",
  "http_status_code": 500
}
```

##### Response 504

504 Example `Request timeout`:

```json
{
  "code": "EBLT0001",
  "message": "Request timeout",
  "http_status_code": 504
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBLT0003` | Failed to parse request payload |
| 401 | `EBLT0005` | Missing or invalid Authorization header |
| 401 | `EBLT0006` | Invalid Authorization header, missing account-id |
| 401 | `EBLT0007` | Invalid Authorization header, missing tenant |
| 404 | `EBLT0009` | Wallets returned [Not found] using ID: 123 |
| 422 | `BBLT0001` | Error while validating fields |
| 422 | `BBLT0003` | Bulletin card has an ongoing event in the network brand. |
| 422 | `BBLT0004` | Bulletin card is already BLOCKED |
| 422 | `BBLT0005` | The card with ID 123 does not have a network brand. |
| 500 | `EBLT9998` | Something went wrong when try to process a request in Programs API using ID: 123 |
| 500 | `EBLT9999` | Something went wrong, please try again later |
| 504 | `EBLT0001` | Request timeout |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;404;422;500;504`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-protection-bulletin`.

<!-- op: spec=api-specs/Card_issuing_-_Protection_Bulletin.yaml method=GET path=/v1/bulletin/{card_id} operationId=get-v1-bulletin -->
### `GET /v1/bulletin/{card_id}` — Get Protection Bulletin card

- **operationId:** `get-v1-bulletin`
- **Specification:** `api-specs/Card_issuing_-_Protection_Bulletin.yaml` (Card issuing - Protection Bulletin)
- **Server base URL(s):** `https://sandbox.pismolabs.io/protection-bulletin`
- **Tags:** `Bulletin`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets a Pismo-issued card in the Protection Bulletin and its history.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `card_id` | path | yes | number | Pismo card ID. | example: 10203040 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `BulletinResponseModel`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorMessageModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorMessageModel`) |
| 404 | Not Found | `application/json`: object (schema `ErrorMessageModel`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorMessageModel`) |
| 504 | Gateway Timeout | `application/json`: object (schema `ErrorMessageModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | number (schema `CardID`) | no | Pismo card ID. | example: 10203040 |
| `org_id` | string (schema `OrgID`) | no | Pismo organization/tenant ID. | example: "TN-123XXX-XXXXXX-XXXXXXX" |
| `program_id` | number (schema `ProgramID`) | no | Pismo program ID. | example: 1010 |
| `network_brand_type` | string (schema `NetworkBrandType`) | no | Card network brand. | enum: ["ELO", "MASTERCARD", "VISA"]; example: "ELO" |
| `created_at` | string (schema `CreatedAt`) | no | Date and time when the Protection Bulletin registration was created. Format = ISO 8601. | format: "yyyy-mm-dd hh:mm:ss"; example: "2025-04-22 20:31:50" |
| `updated_at` | string (schema `UpdatedAt`) | no | Date and time when the Protection Bulletin was updated. Format = ISO 8601.<br> | format: "yyyy-mm-dd hh:mm:ss"; example: "2025-04-22 20:31:50" |
| `network_track_number` | string (schema `NetworkTrackNumber`) | no | Created in the internal system to track the card's event history. This is a combination between the tenant and the truncated random uuid. | example: "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c" |
| `state` | string (schema `State`) | no | Is card blocked or not in the network brand? When the state is empty, it means the network brand did not successfully receive any action.<br> | enum: ["", "BLOCKED", "UNBLOCKED"]; example: "BLOCKED" |
| `status` | string (schema `Status`) | no | Request processing status. | enum: ["PENDING", "SUCCESS", "FAILED"]; example: "PENDING" |
| `purge_date` | string (schema `PurgeDate`) | no | Date when the card will be removed from the Protection Bulletin in the network brand. Format = yyyy-mm-dd.<br> | format: "yyyy-mm-dd"; example: "2025-04-22" |
| `was_automatically_purged` | boolean (schema `WasAutomaticallyPurged`) | no | Was card removed from the network brand on the purge date?<br> | example: true |
| `card_track_number` | number (schema `CardTrackNumber`) | no | Pismo card track number. | example: 1 |
| `region_code` | array of string (schema `RegionCode`) | no | Region code contains one or more Account Screen Authorization File (ASAF) region codes that define the distribution of a Visa cardholder account number in Card Recovery Bulletin Service files. **REQUIRED** for Visa. <br /><br>  `0` - No Bulletin / V.I.P. Only (cannot be combined with other region codes)<br /><br>  `A` - All Asia-Pacific region countries<br /><br>  `B` - All  Central Europe, Middle East, and Africa (CEMEA) region countries.<br /><br>  `C` - All Visa Canada<br /><br>  `D` - National Card Recovery Bulletin<br /><br>  `E` - All European countries<br /><br>  `F` - All Latin America and Caribbean (LAC) region countries <br /><br><br>Region codes can be in any order, except no other region code can be specified in combination with region code 0.<br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Table 215: Field 127E.2 Account Screen Authorization File (ASAF) Region Codes<br> | items.enum: ["0", "A", "B", "C", "D", "E", "F"] |
| `histories` | array of object (schema `BulletinResponseHistoryModel`) | no | Response history model for the Bulletin API. |  |
| `histories[].event` | string (schema `Event`) | no | Event performed in the request | enum: ["POST", "UPDATE", "DELETE"]; example: "POST" |
| `histories[].event_date` | string (schema `EventDate`) | no | Date and time when the event was received in the Protection Bulletin. | format: "yyyy-mm-dd hh:mm:ss"; example: "2025-04-22 20:31:50" |
| `histories[].status` | string (schema `Status`) | no | Request processing status. | enum: ["PENDING", "SUCCESS", "FAILED"]; example: "PENDING" |
| `histories[].reason` | string (schema `Reason`) | no | Reason that indicates why the card was added to the Protection Bulletin. | example: "L" |
| `histories[].network_track_number` | string (schema `NetworkTrackNumber`) | no | Created in the internal system to track the card's event history. This is a combination between the tenant and the truncated random uuid. | example: "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c" |
| `histories[].was_automatically_purged` | boolean (schema `WasAutomaticallyPurged`) | no | Was card removed from the network brand on the purge date?<br> | example: true |
| `histories[].card_track_number` | number (schema `CardTrackNumber`) | no | Pismo card track number. | example: 1 |
| `histories[].network_response_data` | string (schema `NetworkResponseData`) | no | Response JSON data received from the network brand.<br><br>The content of this field will indicate the original response from the network brand, whether success or failure. The example provided in this model is for illustrative purposes only.<br> | example: "{\\"status\\":\\"SUCCESS\\",\\"message\\":\\"Card added to Protection Bulletin\\"}" |
| `histories[].region_code` | array of string (schema `RegionCode`) | no | Region code contains one or more Account Screen Authorization File (ASAF) region codes that define the distribution of a Visa cardholder account number in Card Recovery Bulletin Service files. **REQUIRED** for Visa. <br /><br>  `0` - No Bulletin / V.I.P. Only (cannot be combined with other region codes)<br /><br>  `A` - All Asia-Pacific region countries<br /><br>  `B` - All  Central Europe, Middle East, and Africa (CEMEA) region countries.<br /><br>  `C` - All Visa Canada<br /><br>  `D` - National Card Recovery Bulletin<br /><br>  `E` - All European countries<br /><br>  `F` - All Latin America and Caribbean (LAC) region countries <br /><br><br>Region codes can be in any order, except no other region code can be specified in combination with region code 0.<br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Table 215: Field 127E.2 Account Screen Authorization File (ASAF) Region Codes<br> | items.enum: ["0", "A", "B", "C", "D", "E", "F"] |

200 Example `Retrieve a Elo card without network response`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "ELO",
  "created_at": "2025-04-22 20:31:50",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "status": "PENDING",
  "was_automatically_purged": true,
  "card_track_number": 1,
  "histories": [
    {
      "event": "POST",
      "event_date": "2025-04-22 20:31:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "was_automatically_purged": true,
      "network_response_data": "null",
      "card_track_number": 1
    }
  ]
}
```

200 Example `Retrieve a Elo card with network response`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "ELO",
  "created_at": "2025-04-22 20:31:50",
  "updated_at": "2025-04-22 20:32:50",
  "purge_date": "2026-01-01",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "state": "BLOCKED",
  "status": "SUCCESS",
  "was_automatically_purged": true,
  "card_track_number": 1,
  "histories": [
    {
      "event": "POST",
      "event_date": "2025-04-22 20:31:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "was_automatically_purged": true,
      "network_response_data": "null",
      "card_track_number": 1
    },
    {
      "event": "UPDATE",
      "event_date": "2025-04-22 20:32:50",
      "status": "SUCCESS",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "was_automatically_purged": true,
      "purge_date": "2026-01-01",
      "network_response_data": "{\"network\": \"response\"}",
      "card_track_number": 1
    }
  ]
}
```

200 Example `Retrieve a Mastercard card without network response`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "MASTERCARD",
  "created_at": "2025-04-22 20:31:50",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "status": "PENDING",
  "was_automatically_purged": true,
  "card_track_number": 1,
  "histories": [
    {
      "event": "POST",
      "event_date": "2025-04-22 20:31:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "reason": "O",
      "was_automatically_purged": true,
      "network_response_data": "null",
      "card_track_number": 1
    }
  ]
}
```

200 Example `Retrieve a Mastercard card with network response`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "MASTERCARD",
  "created_at": "2025-04-22 20:31:50",
  "updated_at": "2025-04-22 20:32:50",
  "purge_date": "2026-01-01",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "state": "BLOCKED",
  "status": "SUCCESS",
  "was_automatically_purged": true,
  "card_track_number": 1,
  "histories": [
    {
      "event": "POST",
      "event_date": "2025-04-22 20:31:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "reason": "O",
      "was_automatically_purged": true,
      "network_response_data": "null",
      "card_track_number": 1
    },
    {
      "event": "UPDATE",
      "event_date": "2025-04-22 20:32:50",
      "status": "SUCCESS",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "reason": "O",
      "was_automatically_purged": true,
      "purge_date": "2026-01-01",
      "network_response_data": "{\"network\": \"response\"}",
      "card_track_number": 1
    }
  ]
}
```

200 Example `Retrieve a Visa card without network response`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "VISA",
  "created_at": "2025-04-22 20:31:50",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "status": "PENDING",
  "was_automatically_purged": true,
  "card_track_number": 1,
  "histories": [
    {
      "event": "POST",
      "event_date": "2025-04-22 20:31:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "reason": "04",
      "was_automatically_purged": true,
      "network_response_data": "null",
      "card_track_number": 1
    }
  ]
}
```

200 Example `Retrieve a Visa card with network response`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "MASTERCARD",
  "created_at": "2025-04-22 20:31:50",
  "updated_at": "2025-04-22 20:32:50",
  "purge_date": "2026-01-01",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "state": "BLOCKED",
  "status": "SUCCESS",
  "was_automatically_purged": true,
  "card_track_number": 1,
  "region_code": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"
  ],
  "histories": [
    {
      "event": "POST",
      "event_date": "2025-04-22 20:31:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "reason": "04",
      "was_automatically_purged": true,
      "network_response_data": "null",
      "card_track_number": 1,
      "region_code": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F"
      ]
    },
    {
      "event": "UPDATE",
      "event_date": "2025-04-22 20:32:50",
      "status": "SUCCESS",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "reason": "O",
      "was_automatically_purged": true,
      "purge_date": "2026-01-01",
      "network_response_data": "{\"network\": \"response\"}",
      "card_track_number": 1,
      "region_code": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F"
      ]
    }
  ]
}
```

##### Response 400

400 Example `Invalid param`:

```json
{
  "code": "EBLT0004",
  "message": "Invalid card_id param",
  "http_status_code": 400
}
```

##### Response 401

401 Example `Missing or invalid Authorization header`:

```json
{
  "code": "EBLT0005",
  "message": "Missing or invalid Authorization header",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing account-id`:

```json
{
  "code": "EBLT0006",
  "message": "Invalid Authorization header, missing account-id",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing tenant`:

```json
{
  "code": "EBLT0007",
  "message": "Invalid Authorization header, missing tenant",
  "http_status_code": 401
}
```

##### Response 404

404 Example `Bulletin card not found`:

```json
{
  "code": "BBLT0002",
  "message": "Bulletin card not found",
  "http_status_code": 404
}
```

404 Example `Wallets returned not found`:

```json
{
  "code": "EBLT0009",
  "message": "Wallets returned [Not found] using ID: 123",
  "http_status_code": 404
}
```

##### Response 500

500 Example `Something went wrong when try to process a request in another service`:

```json
{
  "code": "EBLT9998",
  "message": "Something went wrong when try to process a request in Programs API using ID: 123",
  "http_status_code": 500
}
```

500 Example `Something went wrong, please try again later`:

```json
{
  "code": "EBLT9999",
  "message": "Something went wrong, please try again later",
  "http_status_code": 500
}
```

##### Response 504

504 Example `Request timeout`:

```json
{
  "code": "EBLT0001",
  "message": "Request timeout",
  "http_status_code": 504
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBLT0004` | Invalid card_id param |
| 401 | `EBLT0005` | Missing or invalid Authorization header |
| 401 | `EBLT0006` | Invalid Authorization header, missing account-id |
| 401 | `EBLT0007` | Invalid Authorization header, missing tenant |
| 404 | `BBLT0002` | Bulletin card not found |
| 404 | `EBLT0009` | Wallets returned [Not found] using ID: 123 |
| 500 | `EBLT9998` | Something went wrong when try to process a request in Programs API using ID: 123 |
| 500 | `EBLT9999` | Something went wrong, please try again later |
| 504 | `EBLT0001` | Request timeout |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500;504`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Protection_Bulletin.yaml method=DELETE path=/v1/bulletin/{card_id} operationId=delete-v1-bulletin -->
### `DELETE /v1/bulletin/{card_id}` — Delete card from Protection Bulletin

- **operationId:** `delete-v1-bulletin`
- **Specification:** `api-specs/Card_issuing_-_Protection_Bulletin.yaml` (Card issuing - Protection Bulletin)
- **Server base URL(s):** `https://sandbox.pismolabs.io/protection-bulletin`
- **Tags:** `Bulletin`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Remove a Pismo-issued card from the Protection Bulletin.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `card_id` | path | yes | number | Pismo card ID. | example: 10203040 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `BulletinResponseModel`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorMessageModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorMessageModel`) |
| 404 | Not Found | `application/json`: object (schema `ErrorMessageModel`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `ErrorMessageModel`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorMessageModel`) |
| 504 | Gateway Timeout | `application/json`: object (schema `ErrorMessageModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | number (schema `CardID`) | no | Pismo card ID. | example: 10203040 |
| `org_id` | string (schema `OrgID`) | no | Pismo organization/tenant ID. | example: "TN-123XXX-XXXXXX-XXXXXXX" |
| `program_id` | number (schema `ProgramID`) | no | Pismo program ID. | example: 1010 |
| `network_brand_type` | string (schema `NetworkBrandType`) | no | Card network brand. | enum: ["ELO", "MASTERCARD", "VISA"]; example: "ELO" |
| `created_at` | string (schema `CreatedAt`) | no | Date and time when the Protection Bulletin registration was created. Format = ISO 8601. | format: "yyyy-mm-dd hh:mm:ss"; example: "2025-04-22 20:31:50" |
| `updated_at` | string (schema `UpdatedAt`) | no | Date and time when the Protection Bulletin was updated. Format = ISO 8601.<br> | format: "yyyy-mm-dd hh:mm:ss"; example: "2025-04-22 20:31:50" |
| `network_track_number` | string (schema `NetworkTrackNumber`) | no | Created in the internal system to track the card's event history. This is a combination between the tenant and the truncated random uuid. | example: "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c" |
| `state` | string (schema `State`) | no | Is card blocked or not in the network brand? When the state is empty, it means the network brand did not successfully receive any action.<br> | enum: ["", "BLOCKED", "UNBLOCKED"]; example: "BLOCKED" |
| `status` | string (schema `Status`) | no | Request processing status. | enum: ["PENDING", "SUCCESS", "FAILED"]; example: "PENDING" |
| `purge_date` | string (schema `PurgeDate`) | no | Date when the card will be removed from the Protection Bulletin in the network brand. Format = yyyy-mm-dd.<br> | format: "yyyy-mm-dd"; example: "2025-04-22" |
| `was_automatically_purged` | boolean (schema `WasAutomaticallyPurged`) | no | Was card removed from the network brand on the purge date?<br> | example: true |
| `card_track_number` | number (schema `CardTrackNumber`) | no | Pismo card track number. | example: 1 |
| `region_code` | array of string (schema `RegionCode`) | no | Region code contains one or more Account Screen Authorization File (ASAF) region codes that define the distribution of a Visa cardholder account number in Card Recovery Bulletin Service files. **REQUIRED** for Visa. <br /><br>  `0` - No Bulletin / V.I.P. Only (cannot be combined with other region codes)<br /><br>  `A` - All Asia-Pacific region countries<br /><br>  `B` - All  Central Europe, Middle East, and Africa (CEMEA) region countries.<br /><br>  `C` - All Visa Canada<br /><br>  `D` - National Card Recovery Bulletin<br /><br>  `E` - All European countries<br /><br>  `F` - All Latin America and Caribbean (LAC) region countries <br /><br><br>Region codes can be in any order, except no other region code can be specified in combination with region code 0.<br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Table 215: Field 127E.2 Account Screen Authorization File (ASAF) Region Codes<br> | items.enum: ["0", "A", "B", "C", "D", "E", "F"] |
| `histories` | array of object (schema `BulletinResponseHistoryModel`) | no | Response history model for the Bulletin API. |  |
| `histories[].event` | string (schema `Event`) | no | Event performed in the request | enum: ["POST", "UPDATE", "DELETE"]; example: "POST" |
| `histories[].event_date` | string (schema `EventDate`) | no | Date and time when the event was received in the Protection Bulletin. | format: "yyyy-mm-dd hh:mm:ss"; example: "2025-04-22 20:31:50" |
| `histories[].status` | string (schema `Status`) | no | Request processing status. | enum: ["PENDING", "SUCCESS", "FAILED"]; example: "PENDING" |
| `histories[].reason` | string (schema `Reason`) | no | Reason that indicates why the card was added to the Protection Bulletin. | example: "L" |
| `histories[].network_track_number` | string (schema `NetworkTrackNumber`) | no | Created in the internal system to track the card's event history. This is a combination between the tenant and the truncated random uuid. | example: "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c" |
| `histories[].was_automatically_purged` | boolean (schema `WasAutomaticallyPurged`) | no | Was card removed from the network brand on the purge date?<br> | example: true |
| `histories[].card_track_number` | number (schema `CardTrackNumber`) | no | Pismo card track number. | example: 1 |
| `histories[].network_response_data` | string (schema `NetworkResponseData`) | no | Response JSON data received from the network brand.<br><br>The content of this field will indicate the original response from the network brand, whether success or failure. The example provided in this model is for illustrative purposes only.<br> | example: "{\\"status\\":\\"SUCCESS\\",\\"message\\":\\"Card added to Protection Bulletin\\"}" |
| `histories[].region_code` | array of string (schema `RegionCode`) | no | Region code contains one or more Account Screen Authorization File (ASAF) region codes that define the distribution of a Visa cardholder account number in Card Recovery Bulletin Service files. **REQUIRED** for Visa. <br /><br>  `0` - No Bulletin / V.I.P. Only (cannot be combined with other region codes)<br /><br>  `A` - All Asia-Pacific region countries<br /><br>  `B` - All  Central Europe, Middle East, and Africa (CEMEA) region countries.<br /><br>  `C` - All Visa Canada<br /><br>  `D` - National Card Recovery Bulletin<br /><br>  `E` - All European countries<br /><br>  `F` - All Latin America and Caribbean (LAC) region countries <br /><br><br>Region codes can be in any order, except no other region code can be specified in combination with region code 0.<br><br>Visa documentation: VisaNet Authorization-Only Online Messages – Technical Specifications - Table 215: Field 127E.2 Account Screen Authorization File (ASAF) Region Codes<br> | items.enum: ["0", "A", "B", "C", "D", "E", "F"] |

201 Example `Delete a Elo card`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "ELO",
  "created_at": "2025-04-22 20:31:50",
  "updated_at": "2025-04-22 20:32:50",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "status": "PENDING",
  "was_automatically_purged": true,
  "histories": [
    {
      "event": "DELETE",
      "event_date": "2025-04-22 20:32:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "was_automatically_purged": true,
      "network_response_data": "null",
      "card_track_number": 1
    }
  ]
}
```

201 Example `Delete a Mastercard card`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "MASTERCARD",
  "created_at": "2025-04-22 20:31:50",
  "updated_at": "2025-04-22 20:32:50",
  "purge_date": "2026-01-01",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "status": "PENDING",
  "was_automatically_purged": true,
  "histories": [
    {
      "event": "DELETE",
      "event_date": "2025-04-22 20:32:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "reason": "O",
      "was_automatically_purged": false,
      "network_response_data": "null",
      "card_track_number": 1
    }
  ]
}
```

201 Example `Delete a Visa card`:

```json
{
  "card_id": 10203040,
  "org_id": "TN-123XXX-XXXXXX-XXXXXXX",
  "program_id": 1010,
  "network_brand_type": "VISA",
  "created_at": "2025-04-22 20:31:50",
  "updated_at": "2025-04-22 20:32:50",
  "purge_date": "2026-01-01",
  "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
  "status": "PENDING",
  "was_automatically_purged": true,
  "card_track_number": 1,
  "region_code": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"
  ],
  "histories": [
    {
      "event": "DELETE",
      "event_date": "2025-04-22 20:32:50",
      "status": "PENDING",
      "network_track_number": "TN-123XXX-XXXXXX-XXXXXXX::1a2b3c",
      "reason": "04",
      "was_automatically_purged": false,
      "network_response_data": "null",
      "card_track_number": 1,
      "region_code": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F"
      ]
    }
  ]
}
```

##### Response 400

400 Example `Invalid param`:

```json
{
  "code": "EBLT0004",
  "message": "Invalid card_id param",
  "http_status_code": 400
}
```

##### Response 401

401 Example `Missing or invalid Authorization header`:

```json
{
  "code": "EBLT0005",
  "message": "Missing or invalid Authorization header",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing account-id`:

```json
{
  "code": "EBLT0006",
  "message": "Invalid Authorization header, missing account-id",
  "http_status_code": 401
}
```

401 Example `Invalid Authorization header, missing tenant`:

```json
{
  "code": "EBLT0007",
  "message": "Invalid Authorization header, missing tenant",
  "http_status_code": 401
}
```

##### Response 404

404 Example `Bulletin card not found`:

```json
{
  "code": "BBLT0002",
  "message": "Bulletin card not found",
  "http_status_code": 404
}
```

404 Example `Wallets returned not found`:

```json
{
  "code": "EBLT0009",
  "message": "Wallets returned [Not found] using ID: 123",
  "http_status_code": 404
}
```

##### Response 422

422 Example `Error while validating fields`:

```json
{
  "code": "BBLT0001",
  "message": "Error while validating fields",
  "http_status_code": 422,
  "details": {
    "header": [
      {
        "field": "x-customer-id",
        "message": "This field is required"
      }
    ]
  }
}
```

422 Example `Bulletin card has an ongoing event in the network brand`:

```json
{
  "code": "BBLT0003",
  "message": "Bulletin card has an ongoing event in the network brand.",
  "http_status_code": 422
}
```

422 Example `The card with ID does not have a network brand`:

```json
{
  "code": "BBLT0005",
  "message": "The card with ID 123 does not have a network brand.",
  "http_status_code": 422
}
```

##### Response 500

500 Example `Something went wrong when try to process a request in another service`:

```json
{
  "code": "EBLT9998",
  "message": "Something went wrong when try to process a request in Programs API using ID: 123",
  "http_status_code": 500
}
```

500 Example `Something went wrong, please try again later`:

```json
{
  "code": "EBLT9999",
  "message": "Something went wrong, please try again later",
  "http_status_code": 500
}
```

##### Response 504

504 Example `Request timeout`:

```json
{
  "code": "EBLT0001",
  "message": "Request timeout",
  "http_status_code": 504
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBLT0004` | Invalid card_id param |
| 401 | `EBLT0005` | Missing or invalid Authorization header |
| 401 | `EBLT0006` | Invalid Authorization header, missing account-id |
| 401 | `EBLT0007` | Invalid Authorization header, missing tenant |
| 404 | `BBLT0002` | Bulletin card not found |
| 404 | `EBLT0009` | Wallets returned [Not found] using ID: 123 |
| 422 | `BBLT0001` | Error while validating fields |
| 422 | `BBLT0003` | Bulletin card has an ongoing event in the network brand. |
| 422 | `BBLT0005` | The card with ID 123 does not have a network brand. |
| 500 | `EBLT9998` | Something went wrong when try to process a request in Programs API using ID: 123 |
| 500 | `EBLT9999` | Something went wrong, please try again later |
| 504 | `EBLT0001` | Request timeout |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;404;422;500;504`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorMessageModel -->
### Schema `ErrorMessageModel`

Pointer: `#/components/schemas/ErrorMessageModel`. Type: object (schema `ErrorMessageModel`).

> API generic returned error.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code. |  |
| `message` | string | no | Error description. |  |
| `http_status_code` | integer | no | HTTP status code. |  |
| `details` | object (schema `ErrorDetailMessageModel`) | no | Detailed information about the error. |  |

<!-- schema: #/components/schemas/ErrorDetailMessageModel -->
### Schema `ErrorDetailMessageModel`

Pointer: `#/components/schemas/ErrorDetailMessageModel`. Type: object (schema `ErrorDetailMessageModel`).

> Detailed information about the error.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payload` | array of object (schema `ErrorPayloadMessageModel`) | no | List of payload-related error details. |  |
| `header` | array of object (schema `ErrorHeaderMessageModel`) | no | List of header-related error details. |  |
| `parameters` | array of object (schema `ErrorParameterMessageModel`) | no | List of parameter-related error details. |  |

<!-- schema: #/components/schemas/ErrorPayloadMessageModel -->
### Schema `ErrorPayloadMessageModel`

Pointer: `#/components/schemas/ErrorPayloadMessageModel`. Type: object (schema `ErrorPayloadMessageModel`).

> Details about payload-related errors.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | no | Field name related to the error. | example: "field" |
| `message` | string | no | Error message for the field. | example: "Generic error" |

<!-- schema: #/components/schemas/ErrorHeaderMessageModel -->
### Schema `ErrorHeaderMessageModel`

Pointer: `#/components/schemas/ErrorHeaderMessageModel`. Type: object (schema `ErrorHeaderMessageModel`).

> Details about header-related errors.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | no | Header name related to the error. | example: "x-field" |
| `message` | string | no | Error message for the header. | example: "Generic error" |

<!-- schema: #/components/schemas/ErrorParameterMessageModel -->
### Schema `ErrorParameterMessageModel`

Pointer: `#/components/schemas/ErrorParameterMessageModel`. Type: object (schema `ErrorParameterMessageModel`).

> Details about parameter-related errors.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | no | Parameter name related to the error. | example: "query_parameter" |
| `message` | string | no | Parameter error message |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Protection_Bulletin.yaml` | tag `Bulletin`: GET /v1/bulletin, POST /v1/bulletin, GET /v1/bulletin/{card_id}, DELETE /v1/bulletin/{card_id} | https://github.com/PismoDevEx/pismo-api-specs | `6c5641a54569d51d…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-protection-bulletin` — Protection Bulletin
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
