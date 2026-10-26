---
ku_id: KU-API-banking-transaction-banking--channels
title: 'API reference: Banking - Transaction banking — Channels'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Transaction_banking.yaml
  sha256: dec6c4900eb2db35c29c0f0380763da5ae0e1a18c4ad1e293216b2b6effdab56
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
- get-corporate-v1-channels
- post-corporate-v1-channels
- get-corporate-v1-channels-channel
- delete-corporate-v1-channels
- patch-corporate-v1-channels-channel
related_kus:
- KU-BANK-dated-transactions
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-other-domains
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Channels

**KU ID:** `KU-API-banking-transaction-banking--channels` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Channels` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Channel management endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /corporate/v1/channels` | `get-corporate-v1-channels` | List channels | no |
| `POST /corporate/v1/channels` | `post-corporate-v1-channels` | Create channel | no |
| `GET /corporate/v1/channels/{channel}` | `get-corporate-v1-channels-channel` | Get channel | no |
| `DELETE /corporate/v1/channels/{channel}` | `delete-corporate-v1-channels` | Delete channel | no |
| `PATCH /corporate/v1/channels/{channel}` | `patch-corporate-v1-channels-channel` | Update channel | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/channels operationId=get-corporate-v1-channels -->
### `GET /corporate/v1/channels` — List channels

- **operationId:** `get-corporate-v1-channels`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Channels`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Lists all active channels.<br>
>
> Returns only active (non-deleted) channels. Supports optional date range filtering and cursor-based pagination.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `createdAtStart` | query | no | string | Filter channels created on or after this date. Format = `YYYY-MM-DD`. | format: "date"; example: "2026-01-01" |
| `createdAtEnd` | query | no | string | Filter channels created on or before this date. Format = `YYYY-MM-DD`. | format: "date"; example: "2026-06-30" |
| `cursor` | query | no | string | Cursor to the next page of results. If no value is specified, it fetches the first page. | example: "1234" |
| `limit` | query | no | integer | Maximum number of items per page. Defaults to `10`. Maximum is `100`. | default: 10; format: "int32"; maximum: 100; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK. Returns list of active channels with pagination. | `application/json`: object (schema `ListChannelsResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `channels` | array of object (schema `GetChannelResponse`) | yes |  |  |
| `pagination` | object (schema `ListChannelsPagination`) | yes | Pagination metadata for channel listing |  |

200 Example `Channels list`:

```json
{
  "channels": [
    {
      "channel": "GDP",
      "description": "Global Direct Payments",
      "created_at": "2026-02-26T10:30:00.123Z",
      "deleted_at": null
    },
    {
      "channel": "GCE",
      "description": "GCE sweep operations channel",
      "created_at": "2026-02-15T08:30:00.000Z",
      "deleted_at": null
    }
  ],
  "pagination": {
    "limit": 10,
    "cursor": "eyJpZCI6MTI4fQ=="
  }
}
```

200 Example `Empty list`:

```json
{
  "channels": [],
  "pagination": {
    "limit": 10,
    "cursor": ""
  }
}
```

##### Response 400

400 Example `Invalid date format` (Invalid date format):

```json
{
  "code": "WCCL0002",
  "message": "CreatedAtStart 10-12-2026 should be formatted as yyyy-mm-dd and be a valid date"
}
```

400 Example `Invalid cursor` (Invalid cursor):

```json
{
  "code": "WCMN0004",
  "message": "Invalid cursor"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCCL0002` | CreatedAtStart 10-12-2026 should be formatted as yyyy-mm-dd and be a valid date |
| 400 | `WCMN0004` | Invalid cursor |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v1/channels operationId=post-corporate-v1-channels -->
### `POST /corporate/v1/channels` — Create channel

- **operationId:** `post-corporate-v1-channels`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Channels`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates a new channel for transaction routing and control.<br>
>
> A channel is a client‑defined code that identifies the source of a payment or cash‑management operation. It controls how back‑business‑date transactions are handled and determines whether a transaction can bypass cutoff rules, since only active channels in the allowed set can override the cutoff. Channels also enable routing based on the transaction’s source.
>
> This endpoint generates the following events:
> - [Channel created, updated, or deleted](https://developers.pismo.io/events/docs/cash-management-channel-1)
>
> Refer to [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.

#### Request body

Required: yes

> Create channel request body

**Content type `application/json`** — schema: object (schema `CreateChannelRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `channel` | string (schema `ChannelCode`) | yes | Alphanumeric channel code identifier | pattern: "^[a-zA-Z0-9]+$"; minLength: 1; maxLength: 20; example: "GDP" |
| `description` | string (schema `ChannelDescription`) | no | Text describing the channel | maxLength: 255; example: "GDP channel" |

Example `New channel`:

```json
{
  "channel": "GDP",
  "description": "GDP channel"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created. Returns the created channel. | `application/json`: object (schema `CreateChannelResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict. Channel already exists. | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `channel` | string (schema `ChannelCodeResponse`) | yes | Alphanumeric channel code | example: "GDP" |
| `created_at` | string (schema `ChannelCreatedAt`) | yes | Timestamp indicating when the channel was created, expressed in RFC3339 format with millisecond precision. | format: "date-time"; example: "2026-02-26T10:30:00.123Z" |
| `description` | string (schema `ChannelDescription`) | no | Text describing the channel | maxLength: 255; example: "GDP channel" |

201 Example `Created channel`:

```json
{
  "channel": "GDP",
  "description": "GDP channel",
  "created_at": "2026-02-26T10:30:00.123Z"
}
```

##### Response 400

400 Example `Invalid JSON` (Invalid JSON payload):

```json
{
  "code": "WCCL0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `channel required` (Channel required):

```json
{
  "code": "WCCL0002",
  "message": "channel is a required field"
}
```

400 Example `channel contains character not permitted` (channel contains character not permitted):

```json
{
  "code": "WCCL0002",
  "message": "channel contains character not permitted"
}
```

400 Example `channel max` (channel exceeds maximum length):

```json
{
  "code": "WCCL0002",
  "message": "channel must be a maximum of 20 characters in length"
}
```

400 Example `description max` (description exceeds maximum length):

```json
{
  "code": "WCCL0002",
  "message": "description must be a maximum of 255 characters in length"
}
```

##### Response 409

409 Example `Channel already exists`:

```json
{
  "code": "WCCL0003",
  "message": "Channel 'GDP' already exists"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCCL0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WCCL0002` | channel is a required field |
| 409 | `WCCL0003` | Channel 'GDP' already exists |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cash-management-channel-1` | https://developers.pismo.io/events/docs/cash-management-channel-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-dated-transactions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/channels/{channel} operationId=get-corporate-v1-channels-channel -->
### `GET /corporate/v1/channels/{channel}` — Get channel

- **operationId:** `get-corporate-v1-channels-channel`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Channels`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets a specific channel using channel code.<br>
>
> Returns the latest version of the channel, even if it has been soft‑deleted. The `deleted_at` field shows the channel’s lifecycle state: `null` indicates an active channel, while the timestamp indicates when it was deleted.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `channel` | path | yes | string | Channel code | pattern: "^[a-zA-Z0-9]+$"; minLength: 1; maxLength: 20; example: "GDP" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK. Returns the channel. | `application/json`: object (schema `GetChannelResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not Found. Channel does not exist. | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `channel` | string (schema `ChannelCodeResponse`) | yes | Alphanumeric channel code | example: "GDP" |
| `created_at` | string (schema `ChannelCreatedAt`) | yes | Timestamp indicating when the channel was created, expressed in RFC3339 format with millisecond precision. | format: "date-time"; example: "2026-02-26T10:30:00.123Z" |
| `description` | string (schema `ChannelDescription`) | no | Text describing the channel | maxLength: 255; example: "GDP channel" |
| `deleted_at` | string (schema `ChannelDeletedAt`) | no | Timestamp that indicates when the channel was soft-deleted. Null if the channel is active. | format: "date-time"; nullable: true; example: null |

200 Example `Active channel`:

```json
{
  "channel": "GDP",
  "description": "Global Direct Payments",
  "created_at": "2026-02-26T10:30:00.123Z",
  "deleted_at": null
}
```

200 Example `Deleted channel`:

```json
{
  "channel": "GDP",
  "description": "Global Direct Payments",
  "created_at": "2026-02-26T10:30:00.123Z",
  "deleted_at": "2026-05-10T09:00:00.000Z"
}
```

##### Response 404

404 Example `Channel not found` (Channel not found):

```json
{
  "code": "WCCL0004",
  "message": "Channel not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 404 | `WCCL0004` | Channel not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=DELETE path=/corporate/v1/channels/{channel} operationId=delete-corporate-v1-channels -->
### `DELETE /corporate/v1/channels/{channel}` — Delete channel

- **operationId:** `delete-corporate-v1-channels`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Channels`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Deletes an existing channel.<br>
>
> This operation prevents the channel from being used for new transactions.
>
> This endpoint generates the following events:
> - [Channel created, updated, or deleted](https://developers.pismo.io/events/docs/cash-management-channel-1)
>
> Refer to [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `channel` | path | yes | string | Channel code | pattern: "^[a-zA-Z0-9]+$"; minLength: 1; maxLength: 20; example: "GDP" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Channel successfully deleted. |  |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not Found. Channel does not exist. | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Channel not active` (Channel is not active):

```json
{
  "code": "WCCL0005",
  "message": "Channel not active"
}
```

##### Response 404

404 Example `Channel not found` (Channel not found):

```json
{
  "code": "WCCL0004",
  "message": "Channel not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCCL0005` | Channel not active |
| 404 | `WCCL0004` | Channel not found |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cash-management-channel-1` | https://developers.pismo.io/events/docs/cash-management-channel-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-dated-transactions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/corporate/v1/channels/{channel} operationId=patch-corporate-v1-channels-channel -->
### `PATCH /corporate/v1/channels/{channel}` — Update channel

- **operationId:** `patch-corporate-v1-channels-channel`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Channels`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Updates the description of an existing channel.<br>
>
> You can update `description`, but the channel code remains fixed.
>
> This endpoint generates the following events:
> - [Channel created, updated, or deleted](https://developers.pismo.io/events/docs/cash-management-channel-1)
>
> Refer to [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `channel` | path | yes | string | Channel code | pattern: "^[a-zA-Z0-9]+$"; minLength: 1; maxLength: 20; example: "GDP" |

#### Request body

Required: yes

> Update channel request body

**Content type `application/json`** — schema: object (schema `UpdateChannelRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `ChannelDescription`) | yes | Text describing the channel | maxLength: 255; example: "GDP channel" |

Example `Update description`:

```json
{
  "description": "Updated GDP channel description"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK. Returns the updated channel. | `application/json`: object (schema `UpdateChannelResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not Found. Channel does not exist. | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `channel` | string (schema `ChannelCodeResponse`) | yes | Alphanumeric channel code | example: "GDP" |
| `created_at` | string (schema `ChannelCreatedAt`) | yes | Timestamp indicating when the channel was created, expressed in RFC3339 format with millisecond precision. | format: "date-time"; example: "2026-02-26T10:30:00.123Z" |
| `description` | string (schema `ChannelDescription`) | no | Text describing the channel | maxLength: 255; example: "GDP channel" |
| `updated_at` | string (schema `ChannelUpdatedAt`) | no | Timestamp indicating the last update to the channel in RFC3339 format, displayed in milliseconds. | format: "date-time"; nullable: true; example: "2026-03-10T14:00:00.000Z" |
| `deleted_at` | string (schema `ChannelDeletedAt`) | no | Timestamp that indicates when the channel was soft-deleted. Null if the channel is active. | format: "date-time"; nullable: true; example: null |

200 Example `Updated channel`:

```json
{
  "channel": "GDP",
  "description": "Updated GDP channel description",
  "created_at": "2026-02-26T10:30:00.123Z",
  "updated_at": "2026-07-31T14:00:00.000Z",
  "deleted_at": null
}
```

##### Response 400

400 Example `Invalid JSON` (Invalid JSON payload):

```json
{
  "code": "WCCL0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `description required` (Description is required):

```json
{
  "code": "WCCL0002",
  "message": "description is a required field"
}
```

400 Example `description max` (Description exceeds maximum length):

```json
{
  "code": "WCCL0002",
  "message": "description must be a maximum of 255 characters in length"
}
```

400 Example `Channel not active` (Channel is not active):

```json
{
  "code": "WCCL0005",
  "message": "Channel not active"
}
```

##### Response 404

404 Example `Channel not found` (Channel not found):

```json
{
  "code": "WCCL0004",
  "message": "Channel not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCCL0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WCCL0002` | description is a required field |
| 400 | `WCCL0005` | Channel not active |
| 404 | `WCCL0004` | Channel not found |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cash-management-channel-1` | https://developers.pismo.io/events/docs/cash-management-channel-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/GetChannelResponse -->
### Schema `GetChannelResponse`

Pointer: `#/components/schemas/GetChannelResponse`. Type: object (schema `GetChannelResponse`).

> Response body for a single channel

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `channel` | string (schema `ChannelCodeResponse`) | yes | Alphanumeric channel code | example: "GDP" |
| `created_at` | string (schema `ChannelCreatedAt`) | yes | Timestamp indicating when the channel was created, expressed in RFC3339 format with millisecond precision. | format: "date-time"; example: "2026-02-26T10:30:00.123Z" |
| `description` | string (schema `ChannelDescription`) | no | Text describing the channel | maxLength: 255; example: "GDP channel" |
| `deleted_at` | string (schema `ChannelDeletedAt`) | no | Timestamp that indicates when the channel was soft-deleted. Null if the channel is active. | format: "date-time"; nullable: true; example: null |

<!-- schema: #/components/schemas/ListChannelsPagination -->
### Schema `ListChannelsPagination`

Pointer: `#/components/schemas/ListChannelsPagination`. Type: object (schema `ListChannelsPagination`).

> Pagination metadata for channel listing

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `limit` | integer | yes | Number of items per page | example: 10 |
| `cursor` | string | yes | Cursor to the next page of results | example: "eyJpZCI6MTMyfQ==" |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Channels`: GET /corporate/v1/channels, POST /corporate/v1/channels, GET /corporate/v1/channels/{channel}, DELETE /corporate/v1/channels/{channel}, PATCH /corporate/v1/channels/{channel} | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-dated-transactions` — Business-dated and value-dated transactions
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
