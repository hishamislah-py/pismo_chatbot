---
ku_id: KU-API-data-and-reporting-timeline--timeline
title: 'API reference: Data and reporting - Timeline — Timeline'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Data_and_reporting_-_Timeline.yaml
  sha256: ecdae53dc1fafe1f91372e5a66a26204673be43b69a1452404f766c8f433526d
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
- list-timeline-events
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-EVT-timeline-overview
- KU-GS-get-started-with-pismo-apis
specification_version: v1.0
---

# API reference: Data and reporting - Timeline — Timeline

**KU ID:** `KU-API-data-and-reporting-timeline--timeline` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Timeline` in `api-specs/Data_and_reporting_-_Timeline.yaml` (“Data and reporting - Timeline”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> View timeline events

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /timeline/v1/timeline` | `list-timeline-events` | List account timeline events | no |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must be previoulsy authenticated with an account token

## Operation contracts

<!-- op: spec=api-specs/Data_and_reporting_-_Timeline.yaml method=GET path=/timeline/v1/timeline operationId=list-timeline-events -->
### `GET /timeline/v1/timeline` — List account timeline events

- **operationId:** `list-timeline-events`
- **Specification:** `api-specs/Data_and_reporting_-_Timeline.yaml` (Data and reporting - Timeline)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Timeline`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> List the events in an account timeline using cursor pagination.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `limit` | query | no | number | A maximum of 1 MB of data or the maximum number of items given as the limit value will be evaluated by the operation before any filtering is applied to the results. Default: `100`. |  |
| `category` | query | no | string | Filter only items with the provided category. Your Pismo representative works with you to define the categories and types for your organization. For more information, see [Timeline events overview](https://developers.pismo.io/pismo-docs/docs/timeline-overview). |  |
| `type` | query | no | string | Filter only items with the provided type. Your Pismo representative works with you to define the categories and types for your organization. For more information, see [Timeline events overview](https://developers.pismo.io/pismo-docs/docs/timeline-overview). |  |
| `beginDate` | query | no | string | Filter only items with timestamp greater than or equal to, using RFC 3339 format (`yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`). | format: "date-time" |
| `endDate` | query | no | string | Filter only items with timestamp less than or equal to, using RFC 3339 format (`yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`). | format: "date-time" |
| `order` | query | no | string | Order results as `asc` (ascending) or `desc` (descending) by date. Default: `desc` |  |
| `nextCursor` | query | no | string | Cursor value to apply in a subsequent query to continue the operation. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Paginated timeline items using cursor paging. | `application/json`: object (schema `PaginatedTimelineV1`) |
| 400 | Invalid request. |  |
| 401 | Access token is missing or invalid. |  |
| 404 | The specified resource was not found. |  |
| 500 | Internal Server Error. |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean | no | Has next page | example: false |
| `next_cursor` | string | no | `nextCursor` value to apply in a subsequent query to continue the operation | example: "ewogICJUZW5hbnRBY2NvdW50VGltZXN0YW1wIjogIlRFTkFOVDo6QUNDT1VOVDo6VElNRVNUQU1QIiwKICAiVGVuYW50QWNjb3VudCI6ICJURU5BTlQ6OkFDQ09VTlRfSUQiLAogICJUaW1lc3RhbXAiOiAiVElNRVNUQU1QIgp9" |
| `count` | number | no | Number of items | example: 10 |
| `items` | array of object (schema `Event`) | no |  |  |

200 Example `response-v1-timeline` — from `#/components/examples/GetV1TimelineResponse`:

```json
{
  "has_next": true,
  "next_cursor": "ewogICJUZW5hbnRBY2NvdW50VGltZXN0YW1wIjogIlRFTkFOVDo6QUNDT1VOVDo6VElNRVNUQU1QIiwKICAiVGVuYW50QWNjb3VudCI6ICJURU5BTlQ6OkFDQ09VTlRfSUQiLAogICJUaW1lc3RhbXAiOiAiVElNRVNUQU1QIgp9",
  "count": 2,
  "items": [
    {
      "type": "TYPE",
      "account_id": 123456,
      "category": "CATEGORY",
      "tenant_account_timestamp": "TENANT::ACCOUNT::TIMESTAMP",
      "data": {
        "item": {
          "item-1": "ONE",
          "item-2": 2
        }
      },
      "correlation_id": "cb6d3dc1-be6d-4abf-8ed1-7b40f4d24654",
      "timestamp": "2021-01-01T01:12:23.123456789Z"
    },
    {
      "type": "OTHER_TYPE",
      "account_id": 123456,
      "category": "OTHER_CATEGORY",
      "tenant_account_timestamp": "TENANT::ACCOUNT::TIMESTAMP",
      "data": {
        "item": {
          "item-3": 3,
          "item-4": "FOUR"
        }
      },
      "correlation_id": "cb6d3dc1-be6d-4abf-8ed1-7b40f4d24654",
      "timestamp": "2020-08-04T18:08:10.172955069Z"
    }
  ]
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-timeline-overview`, `KU-GS-get-started-with-pismo-apis`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Event -->
### Schema `Event`

Pointer: `#/components/schemas/Event`. Type: object (schema `Event`).

> Timeline items

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | no |  |  |
| `account_id` | number | no |  |  |
| `category` | string | no |  |  |
| `tenant_account_timestamp` | string | no |  |  |
| `data` | object | no |  |  |
| `correlation_id` | string | no |  |  |
| `timestamp` | string | no |  | format: "date-time" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Data_and_reporting_-_Timeline.yaml` | tag `Timeline`: GET /timeline/v1/timeline | https://github.com/PismoDevEx/pismo-api-specs | `ecdae53dc1fafe1f…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-EVT-timeline-overview` — Timeline events
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
