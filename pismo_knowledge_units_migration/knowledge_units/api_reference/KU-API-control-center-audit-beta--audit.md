---
ku_id: KU-API-control-center-audit-beta--audit
title: 'API reference: Control Center — Audit'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Control_Center_audit_beta.yaml
  sha256: b3d88b1826f281e5d94f65b4f3610f999d89ce65ef60e10308087454eda75146
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
- listAuditRecords
related_kus:
- KU-ERR-codes-acq-to-esma
specification_version: 1.0.0
---

# API reference: Control Center — Audit

**KU ID:** `KU-API-control-center-audit-beta--audit` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Audit` in `api-specs/Control_Center_audit_beta.yaml` (“Control Center”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Audit record information search and retrieval

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/audit` | `listAuditRecords` | List audit records | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Control_Center_audit_beta.yaml method=GET path=/v1/audit operationId=listAuditRecords -->
### `GET /v1/audit` — List audit records

- **operationId:** `listAuditRecords`
- **Specification:** `api-specs/Control_Center_audit_beta.yaml` (Control Center)
- **Server base URL(s):** `https://sandbox.pismolabs.io/audit-api`
- **Tags:** `Audit`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Returns paginated audit records based on filter parameters.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | no | integer | Page number to return | default: 1; format: "int32"; minimum: 1; example: 12 |
| `perPage` | query | no | integer | Number of items per page | default: 10; format: "int32"; minimum: 1; maximum: 100; example: 10 |
| `order` | query | no | string | Sort order by operation date. Supported values: `asc` (oldest first), `desc` (newest first)<br> | enum: ["asc", "desc"]; default: "asc"; example: "desc" |
| `beginDate` | query | no | string | Inclusive begin datetime filter in RFC 3339 format. Format = `YYYY-MM-DDTHH:mm:ssZ`.<br> | format: "date-time"; example: "2025-09-15T00:00:00Z" |
| `endDate` | query | no | string | Exclusive end datetime filter in RFC 3339 format. Format = `YYYY-MM-DDTHH:mm:ssZ`.<br> | format: "date-time"; example: "2025-09-30T00:00:00Z" |
| `user` | query | no | string | Email address of the user who performed the action | maxLength: 80; example: "jrones@example.com" |
| `action` | query | no | string | Comma-separated list of actions to filter by | maxLength: 80; example: "create,update" |
| `feature` | query | no | string | Comma-separated list of features to filter by. Feature names are mapped to specific values such as `account-status`, `program-parameter`, or `account-phone`. | maxLength: 80; example: "account-status, program-parameter, account-phone" |
| `featureID` | query | no | string | Feature ID to filter by. Feature IDs are mapped to specific values such as `user`, `card`, `transaction`. | maxLength: 80; example: "56789" |
| `cid` | query | no | string | Correlation ID for request tracing, used to group related operations across services. | maxLength: 40; example: "4a9d2f3c-b617-4e82-a3f1-9c7d5b0eaf42" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `SearchAuditPage`) |
| 400 | Bad Request | `application/json`: object (schema `Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer | no | Current page number | example: 1 |
| `items` | array of object (schema `Audit`) | no |  | example: [] |
| `pages` | integer | no | Total number of pages | example: 136 |
| `per_page` | integer | no | Number of items per page | example: 10 |
| `total_items` | integer | no | Total number of items matching the query | example: 1357 |

200 Example `example`:

```json
{
  "pages": 136,
  "current_page": 1,
  "per_page": 1,
  "total_items": 1357,
  "items": [
    {
      "id": 1,
      "operation": {
        "tenant": "TN_12345678-1234-1234-1234-123456789012",
        "action": "update",
        "feature": "program",
        "feature_id": "5678",
        "origin": "console",
        "cid": "4a9d2f3c-b617-4e82-a3f1-9c7d5b0eaf42",
        "date": "2025-11-21T10:30:00Z",
        "feature_translation": {
          "en": "Programs",
          "pt": "Programas"
        },
        "audit_details": {
          "en": [
            {
              "label": "Program ID",
              "value": "3579"
            },
            {
              "label": "Program name",
              "value": "program_123"
            }
          ],
          "pt": [
            {
              "label": "ID do Programa",
              "value": "3579"
            },
            {
              "label": "Nome do Programa",
              "value": "program_123"
            }
          ]
        },
        "description": {
          "en": "Update program details or BIN or Due Date",
          "pt": "Atualizar detalhes do programa OU BIN OU data de vencimento"
        }
      },
      "user": {
        "id": "7c4a1f92-3e6d-4c81-9b27-ae5f0d8c41b6",
        "email": "rjones@example.com",
        "roles": [
          "controlc-admin",
          "controlc-setup-viewer"
        ]
      },
      "user_agent": {
        "user_agent_label": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "device_ip": "192.0.2.1"
      },
      "geographic_location": {
        "latitude": -23.5505199,
        "longitude": -46.6333094
      },
      "http": {
        "code": 204,
        "request": "{\"bin\":{\"value\":\"49382810\",\"end_range\":\"1999999\",\"start_range\":\"0\"},\"name\":\"Z+ Global Full balance (AUD)\",\"timezone\":\"Asia/Kolkata\",\"country_code\":\"AUS\",\"currency_numeric_code\":\"036\"}",
        "response": "{}"
      }
    }
  ]
}
```

##### Response 400

400 Example `bindingError` (Binding error — invalid query parameter type or format):

```json
{
  "message": {
    "code": "ECAD0007",
    "message": "Error binding request"
  }
}
```

400 Example `validationError` (Validation error — one or more parameters violate constraints):

```json
{
  "message": {
    "code": "ECAD0005",
    "message": "Key: 'SearchAuditParams.Page' Error:Field validation for 'Page' failed on the 'min' tag"
  }
}
```

400 Example `dateRangeError` (Date range error — beginDate is after endDate):

```json
{
  "message": {
    "code": "ECAD0006",
    "message": "beginDate must be before or equal to endDate"
  }
}
```

##### Response 500

500 Example `example`:

```json
{
  "message": {
    "code": "ECAD0000",
    "message": "Something went wrong, please try again later"
  }
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ECAD0007` | Error binding request |
| 400 | `ECAD0005` | Key: 'SearchAuditParams.Page' Error:Field validation for 'Page' failed on the 'min' tag |
| 400 | `ECAD0006` | beginDate must be before or equal to endDate |
| 500 | `ECAD0000` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Audit -->
### Schema `Audit`

Pointer: `#/components/schemas/Audit`. Type: object (schema `Audit`).

> Audit record describing an action performed in the Pismo Control Center, including an action's operation, user, geographic location, and HTTP details

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `http` | object | yes | Audit HTTP details | example: {"code": 201} |
| `http.code` | integer | yes | HTTP status code returned by the operation | format: "int32"; example: 201 |
| `http.request` | string | yes | Raw HTTP request payload | example: "{\\"name\\": \\"Rosetta Jones\\", \\"email\\": \\"rjones@example.com\\", \\"roles\\": [\\"controlc-admin\\"]}" |
| `http.response` | string | yes | Raw HTTP response payload | example: "{\\"name\\": \\"Rosetta Jones\\", \\"email\\": \\"rjones@example.com\\", \\"roles\\": [\\"controlc-admin\\"]}" |
| `id` | integer | yes | Identifier for the audit record | format: "int64"; example: 3644 |
| `operation` | object | yes | Audit operation details |  |
| `operation.action` | string | yes | Action performed in the system. These values vary based on the specific operation being audited, but common examples include: `create`, `update`, `delete`, `login`, and `logout`. | example: "create" |
| `operation.audit_details` | object | yes | Additional audit context details | example: {"en": [{"label": "Program ID", "value": "3579"}, {"label": "Program name", "value": "program_123"}], "pt": [{"label": "ID do Programa", "value": "3579"}, {"label": "Nome do Programa", "value": "program_123"}], "description": {"en": "Update program details or BIN or Due Date", "pt": "Atualizar detalhes do programa OU BIN OU data de vencimento"}} |
| `operation.changes` | object | yes | Map of field-level changes applied during the operation | example: {} |
| `operation.cid` | string | yes | Correlation ID for request tracing | example: "4a9d2f3c-b617-4e82-a3f1-9c7d5b0eaf42" |
| `operation.date` | string | yes | Datetime the operation was performed. Format = `yyyy-MM-ddTHH:mm:ssZ` | format: "date-time"; example: "2025-09-19T16:59:15Z" |
| `operation.description` | object | yes | Human-readable description of the operation | example: {} |
| `operation.feature` | string | yes | Feature area where the operation was performed. Values are specific to the service being audited, but common examples include: `user`, `card`, `transaction`. | example: "user" |
| `operation.feature_id` | string | yes | Identifier of the resource within the feature | example: "12345" |
| `operation.feature_translation` | object | yes | Feature-specific translation details | example: {} |
| `operation.tenant` | string | yes | Tenant ID where the operation was performed | example: "TN_12345678-1234-1234-1234-123456789012" |
| `operation.origin` | string | no | Origin identifier when the operation was triggered by another service. Common examples include: `console`, `api`, `scheduler` | example: "console" |
| `operation.source_id` | string | no | Source system identifier | example: "pismo-control-center" |
| `user` | object | yes | Audit user details | example: {"id": "user-123", "email": "user@example.com", "roles": ["owner"]} |
| `user.email` | string | yes | Email of the user who performed the action | example: "rjones@example.com" |
| `user.id` | string | yes | ID of the user who performed the action | example: "user-123" |
| `user.roles` | array of string | yes | List of roles assigned to the user who performed the action | example: ["owner", "backoffice-operator"] |
| `user_agent` | object | yes | Audit user agent details | example: {"user_agent_label": "Mozilla/5.0", "device_ip": "192.0.2.1"} |
| `user_agent.device_ip` | string | yes | Device IP address | example: "192.0.2.1" |
| `user_agent.user_agent_label` | string | yes | User-agent string from the device | example: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" |
| `geographic_location` | object | no | Audit geographic location details | example: {"latitude": -23.592049, "longitude": -46.685087} |
| `geographic_location.latitude` | number | yes | Request origin's geographic latitude | format: "double"; example: 37 |
| `geographic_location.longitude` | number | yes | Request origin's geographic longitude | format: "double"; example: -122 |

<!-- schema: #/components/schemas/Error -->
### Schema `Error`

Pointer: `#/components/schemas/Error`. Type: object (schema `Error`).

> Error response details

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | object | no | Error message details | example: {"code": "ECAD0007", "message": "Error binding request"} |
| `message.code` | string | no | Internal error code (e.g. ECAD0004). | example: "ECAD0004" |
| `message.message` | string | no | Human-readable error message. | example: "Error fetching audit details" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Control_Center_audit_beta.yaml` | tag `Audit`: GET /v1/audit | https://github.com/PismoDevEx/pismo-api-specs | `b3d88b1826f281e5…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
