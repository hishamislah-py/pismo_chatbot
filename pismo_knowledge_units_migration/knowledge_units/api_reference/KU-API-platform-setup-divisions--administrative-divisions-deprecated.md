---
ku_id: KU-API-platform-setup-divisions--administrative-divisions-deprecated
title: 'API reference: Platform setup - Divisions — Administrative divisions (deprecated)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Platform_setup_-_Divisions.yaml
  sha256: 96de390559b33b89009174f8f2d481cc5a03eac6b91eb93b61fcb7768cbb0289
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
- post-v1-admin-division
- get-v1-admin-division-external-id
- get-v1-admin-division
- put-v1-admin-division
- delete-v1-admin-division
- get-v1-admin-division-tree-parent-id
- get-v1-admin-division-tree-external-id
- get-v1-admin-division-ancestors-administrative-division-id
- get-v1-admin-division-ancestors-external-id
related_kus:
- KU-CORE-platform-setup-holidays
- KU-CRED-holidays-in-credit-card-accounts
specification_version: v1.0
---

# API reference: Platform setup - Divisions — Administrative divisions (deprecated)

**KU ID:** `KU-API-platform-setup-divisions--administrative-divisions-deprecated` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 9 operation(s) tagged `Administrative divisions (deprecated)` in `api-specs/Platform_setup_-_Divisions.yaml` (“Platform setup - Divisions”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> View and manage administrative divisions.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /divisions-core/v1/administrative-division` | `post-v1-admin-division` | Create administrative division (deprecated) | **yes** |
| `GET /divisions-core/v1/administrative-division/external-id/{id}` | `get-v1-admin-division-external-id` | Get admin division info by external ID (deprecated) | **yes** |
| `GET /divisions-core/v1/administrative-division/{id}` | `get-v1-admin-division` | Get admin division info (deprecated) | **yes** |
| `PUT /divisions-core/v1/administrative-division/{id}` | `put-v1-admin-division` | Update administrative division (deprecated) | **yes** |
| `DELETE /divisions-core/v1/administrative-division/{id}` | `delete-v1-admin-division` | Delete administrative division (deprecated) | **yes** |
| `GET /divisions-core/v1/administrative-division/{id}/tree` | `get-v1-admin-division-tree-parent-id` | Get admin division tree by admin division ID (deprecated) | **yes** |
| `GET /divisions-core/v1/administrative-division/external-id/{id}/tree` | `get-v1-admin-division-tree-external-id` | Get admin division tree by external ID (deprecated) | **yes** |
| `GET /divisions-core/v1/administrative-division/{id}/ancestors` | `get-v1-admin-division-ancestors-administrative-division-id` | Get admin division ancestors by admin division ID (deprecated) | **yes** |
| `GET /divisions-core/v1/administrative-division/external-id/{id}/ancestors` | `get-v1-admin-division-ancestors-external-id` | Get admin division ancestors by external ID (deprecated) | **yes** |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must be previously authenticated with an account token.

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=POST path=/divisions-core/v1/administrative-division operationId=post-v1-admin-division -->
### `POST /divisions-core/v1/administrative-division` — Create administrative division (deprecated)

- **operationId:** `post-v1-admin-division`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call [Create holiday calendar](ref:post-create-holiday-calendar) instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Create an administrative division. 
>
> Administrative divisions are used to divide an organization's territory into separate areas. An organization covering Great Britian for example, might want to have separate divisions for England, Scotland, and Ireland. Each of these countries may have different holidays and need to be administered in different ways. 
>
> There is a [Create administrative division](ref:post-v2-admin-division) V2 endpoint designed for greater flexibility in defining non-business days to accommodate specific business requirements. For details about the differences, refer to [Platform setup - Holidays and administrative divisions](doc:platform-setup-holidays#endpoints-for-transaction-banking).

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `presenter.v1CreateAdministrativeDivisionRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `AdminDivisionName`) | yes | Administrative division name | example: "Scotland" |
| `type` | string (schema `AdminDivisionType`) | yes | Admin division type | enum: ["City", "State", "Country"]; example: "State" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |
| `external_id_reference` | string (schema `AdminDivisionExternalIdReference`) | no | External ID reference. Must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "CRM-software-ID" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `presenter.v1CreateAdministrativeDivisionResponse`) |
| 400 | Bad request error. | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found error. | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AdminDivisionID`) | no | Admininistrative division ID | example: 84849 |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |
| `name` | string (schema `AdminDivisionName`) | no | Administrative division name | example: "Scotland" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `type` | string (schema `AdminDivisionType`) | no | Admin division type | enum: ["City", "State", "Country"]; example: "State" |

##### Response 400

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```

##### Response 404

404 Example `not-found-response` — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "404",
  "message": "{target_name} not found"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-CORE-platform-setup-holidays`, `KU-CRED-holidays-in-credit-card-accounts`.

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=GET path=/divisions-core/v1/administrative-division/external-id/{id} operationId=get-v1-admin-division-external-id -->
### `GET /divisions-core/v1/administrative-division/external-id/{id}` — Get admin division info by external ID (deprecated)

- **operationId:** `get-v1-admin-division-external-id`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call [Get calendar by external ID](ref:get-holiday-calendar-by-external-id) instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Get detailed administrative division information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | string | Administrative division external ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Administrative division details | `application/json`: object (schema `presenter.v1AdministrativeDivisionResponse`) |
| 400 | Bad request error. | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found error. | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AdminDivisionID`) | no | Admininistrative division ID | example: 84849 |
| `name` | string (schema `AdminDivisionName`) | no | Administrative division name | example: "Scotland" |
| `type` | string (schema `AdminDivisionType`) | no | Admin division type | enum: ["City", "State", "Country"]; example: "State" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |

200 Example `response-v1-administrative-division` — from `#/components/examples/GetV1AdministrativeDivisionResponse`:

```json
{
  "id": 1,
  "name": "Brazil",
  "type": "Country",
  "parent_id": 0,
  "external_id": "BR"
}
```

##### Response 400

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```

##### Response 404

404 Example `not-found-response` — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "404",
  "message": "{target_name} not found"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=GET path=/divisions-core/v1/administrative-division/{id} operationId=get-v1-admin-division -->
### `GET /divisions-core/v1/administrative-division/{id}` — Get admin division info (deprecated)

- **operationId:** `get-v1-admin-division`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

>
> **DEPRECATED**. Call [Get holiday calendar](ref:get-holiday-calendar) instead. 
>
>  This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
>  Get detailed administrative division information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Administrative division ID. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Administrative division details. | `application/json`: object (schema `presenter.v1AdministrativeDivisionResponse`) |
| 400 | Bad request error. | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found error. | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AdminDivisionID`) | no | Admininistrative division ID | example: 84849 |
| `name` | string (schema `AdminDivisionName`) | no | Administrative division name | example: "Scotland" |
| `type` | string (schema `AdminDivisionType`) | no | Admin division type | enum: ["City", "State", "Country"]; example: "State" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |

200 Example `response-v1-administrative-division` — from `#/components/examples/GetV1AdministrativeDivisionResponse`:

```json
{
  "id": 1,
  "name": "Brazil",
  "type": "Country",
  "parent_id": 0,
  "external_id": "BR"
}
```

##### Response 400

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```

##### Response 404

404 Example `not-found-response` — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "404",
  "message": "{target_name} not found"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-CORE-platform-setup-holidays`.

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=PUT path=/divisions-core/v1/administrative-division/{id} operationId=put-v1-admin-division -->
### `PUT /divisions-core/v1/administrative-division/{id}` — Update administrative division (deprecated)

- **operationId:** `put-v1-admin-division`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call [Update holiday calendar](ref:update-holiday-calendar) instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Update administrative division.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Administrative division ID. |  |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `presenter.v1UpdateAdministrativeDivisionRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `AdminDivisionName`) | yes | Administrative division name | example: "Scotland" |
| `type` | string (schema `AdminDivisionType`) | yes | Admin division type | enum: ["City", "State", "Country"]; example: "State" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated. | `application/json`: object (schema `presenter.v1AdministrativeDivisionResponse`) |
| 400 | Bad request error. | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found error. | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AdminDivisionID`) | no | Admininistrative division ID | example: 84849 |
| `name` | string (schema `AdminDivisionName`) | no | Administrative division name | example: "Scotland" |
| `type` | string (schema `AdminDivisionType`) | no | Admin division type | enum: ["City", "State", "Country"]; example: "State" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |

200 Example `response-v1-administrative-division` — from `#/components/examples/GetV1AdministrativeDivisionResponse`:

```json
{
  "id": 1,
  "name": "Brazil",
  "type": "Country",
  "parent_id": 0,
  "external_id": "BR"
}
```

##### Response 400

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```

##### Response 404

404 Example `not-found-response` — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "404",
  "message": "{target_name} not found"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=DELETE path=/divisions-core/v1/administrative-division/{id} operationId=delete-v1-admin-division -->
### `DELETE /divisions-core/v1/administrative-division/{id}` — Delete administrative division (deprecated)

- **operationId:** `delete-v1-admin-division`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call [Delete holiday calendar](ref:delete-holiday-calendar) instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Delete an administrative division.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Administrative division ID. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content. |  |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found error. | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal Server Error. | `application/json`: object (schema `handler.HTTPError`) |

##### Response 400

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```

##### Response 404

404 Example `response-missing-tenant` — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "404",
  "message": "{target_name} not found"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "500",
  "message": "The parent_id {parent_id} causes a circular hierarchy loop with the administrative_division id {id}."
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=GET path=/divisions-core/v1/administrative-division/{id}/tree operationId=get-v1-admin-division-tree-parent-id -->
### `GET /divisions-core/v1/administrative-division/{id}/tree` — Get admin division tree by admin division ID (deprecated)

- **operationId:** `get-v1-admin-division-tree-parent-id`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call [List holiday calendars](ref:list-holiday-calendars) instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Get the complete tree of child administrative divisions using the parent's administrative division ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | string | Client-supplied external ID |  |
| `page` | query | yes | integer | Page must be greater than `0`. Default = `1`. |  |
| `perPage` | query | yes | integer | PerPage must be greater than `0`. Default = `10`. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Paginated list of administrative divisions. | `application/json`: object (schema `pagination.Pagination`) |
| 400 | Bad request error. | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pages` | integer | no | Total number of result pages. | example: 1 |
| `current_page` | integer | no | Current result page. | example: 1 |
| `per_page` | integer | no | Maximum results per page. | example: 10 |
| `total_items` | integer | no | Total number of result items. | example: 1 |
| `items` | array of object (schema `presenter.v1AdministrativeDivisionResponse`) | no |  |  |

200 Example `PaginatedListOfAdministrativeDivisionsTree` — from `#/components/examples/GetPaginatedListOfAdministrativeDivisionsTree`:

```json
{
  "pages": 1,
  "current_page": 1,
  "per_page": 10,
  "total_items": 3,
  "items": [
    {
      "id": 43,
      "name": "Brazil",
      "type": "Country",
      "parent_id": 41,
      "external_id": "BR"
    },
    {
      "id": 44,
      "name": "Minas Gerais",
      "type": "State",
      "parent_id": 43,
      "external_id": "MG"
    },
    {
      "id": 45,
      "name": "Rio de Janeiro",
      "type": "State",
      "parent_id": 43,
      "external_id": "RJ"
    },
    {
      "id": 4533,
      "name": "Itaboraí",
      "type": "City",
      "parent_id": 45,
      "external_id": "RJ-Itaboraí"
    }
  ]
}
```

200 Example `PaginatedListOfAdministrativeDivisionsTreeWithMetadata` — from `#/components/examples/GetPaginatedListOfAdministrativeDivisionsTreeWithMetadata`:

```json
{
  "pages": 1,
  "current_page": 1,
  "per_page": 10,
  "total_items": 3,
  "items": [
    {
      "id": 43,
      "name": "Brazil",
      "type": "Country",
      "external_id": "BR",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    },
    {
      "id": 44,
      "name": "Minas Gerais",
      "type": "State",
      "parent_id": 43,
      "external_id": "MG",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    },
    {
      "id": 45,
      "name": "Rio de Janeiro",
      "type": "State",
      "parent_id": 43,
      "external_id": "RJ",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    },
    {
      "id": 4533,
      "name": "Itaboraí",
      "type": "City",
      "parent_id": 45,
      "external_id": "RJ-Itaboraí",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    }
  ]
}
```

##### Response 400

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=GET path=/divisions-core/v1/administrative-division/external-id/{id}/tree operationId=get-v1-admin-division-tree-external-id -->
### `GET /divisions-core/v1/administrative-division/external-id/{id}/tree` — Get admin division tree by external ID (deprecated)

- **operationId:** `get-v1-admin-division-tree-external-id`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call [List holiday calendars](ref:list-holiday-calendars) instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Get the full tree of administrative divisions using an external ID

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | string | Client-supplied external ID |  |
| `page` | query | yes | integer | Page must be greater than `0`. Default = `1`. |  |
| `perPage` | query | yes | integer | PerPage must be greater than `0`. Default = `10`. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Paginated list of administrative divisions. | `application/json`: object (schema `pagination.Pagination`) |
| 400 | Bad request error. | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pages` | integer | no | Total number of result pages. | example: 1 |
| `current_page` | integer | no | Current result page. | example: 1 |
| `per_page` | integer | no | Maximum results per page. | example: 10 |
| `total_items` | integer | no | Total number of result items. | example: 1 |
| `items` | array of object (schema `presenter.v1AdministrativeDivisionResponse`) | no |  |  |

200 Example `PaginatedListOfAdministrativeDivisionsTree` — from `#/components/examples/GetPaginatedListOfAdministrativeDivisionsTree`:

```json
{
  "pages": 1,
  "current_page": 1,
  "per_page": 10,
  "total_items": 3,
  "items": [
    {
      "id": 43,
      "name": "Brazil",
      "type": "Country",
      "parent_id": 41,
      "external_id": "BR"
    },
    {
      "id": 44,
      "name": "Minas Gerais",
      "type": "State",
      "parent_id": 43,
      "external_id": "MG"
    },
    {
      "id": 45,
      "name": "Rio de Janeiro",
      "type": "State",
      "parent_id": 43,
      "external_id": "RJ"
    },
    {
      "id": 4533,
      "name": "Itaboraí",
      "type": "City",
      "parent_id": 45,
      "external_id": "RJ-Itaboraí"
    }
  ]
}
```

200 Example `PaginatedListOfAdministrativeDivisionsTreeWithMetadata` — from `#/components/examples/GetPaginatedListOfAdministrativeDivisionsTreeWithMetadata`:

```json
{
  "pages": 1,
  "current_page": 1,
  "per_page": 10,
  "total_items": 3,
  "items": [
    {
      "id": 43,
      "name": "Brazil",
      "type": "Country",
      "external_id": "BR",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    },
    {
      "id": 44,
      "name": "Minas Gerais",
      "type": "State",
      "parent_id": 43,
      "external_id": "MG",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    },
    {
      "id": 45,
      "name": "Rio de Janeiro",
      "type": "State",
      "parent_id": 43,
      "external_id": "RJ",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    },
    {
      "id": 4533,
      "name": "Itaboraí",
      "type": "City",
      "parent_id": 45,
      "external_id": "RJ-Itaboraí",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    }
  ]
}
```

##### Response 400

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=GET path=/divisions-core/v1/administrative-division/{id}/ancestors operationId=get-v1-admin-division-ancestors-administrative-division-id -->
### `GET /divisions-core/v1/administrative-division/{id}/ancestors` — Get admin division ancestors by admin division ID (deprecated)

- **operationId:** `get-v1-admin-division-ancestors-administrative-division-id`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call [List holiday calendars](ref:list-holiday-calendars) instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> List ancestors for an administrative division using administrative division ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Administrative division ID. |  |
| `page` | query | yes | integer | Page must be greater than `0`. Default = `1`. |  |
| `perPage` | query | yes | integer | PerPage must be greater than `0`. Default = `10`. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Paginated list of administrative divisions. | `application/json`: object (schema `pagination.Pagination`) |
| 400 | Bad request error. | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pages` | integer | no | Total number of result pages. | example: 1 |
| `current_page` | integer | no | Current result page. | example: 1 |
| `per_page` | integer | no | Maximum results per page. | example: 10 |
| `total_items` | integer | no | Total number of result items. | example: 1 |
| `items` | array of object (schema `presenter.v1AdministrativeDivisionResponse`) | no |  |  |

200 Example `PaginatedListOfAdministrativeDivisionsTree` — from `#/components/examples/GetPaginatedListOfAdministrativeDivisionsAncestors`:

```json
{
  "pages": 1,
  "current_page": 1,
  "per_page": 10,
  "total_items": 3,
  "items": [
    {
      "id": 5222005,
      "name": "Vianópolis",
      "type": "City",
      "parent_id": 1052,
      "external_id": "GO-Vianópolis"
    },
    {
      "id": 1052,
      "name": "Goiás",
      "type": "State",
      "parent_id": 1001,
      "external_id": "GO"
    },
    {
      "id": 1001,
      "name": "Brasil",
      "type": "Country",
      "external_id": "BR"
    }
  ]
}
```

200 Example `PaginatedListOfAdministrativeDivisionsTreeWithMetadata` — from `#/components/examples/GetPaginatedListOfAdministrativeDivisionsAncestorsWithMetadata`:

```json
{
  "pages": 1,
  "current_page": 1,
  "per_page": 10,
  "total_items": 3,
  "items": [
    {
      "id": 5222005,
      "name": "Vianópolis",
      "type": "City",
      "parent_id": 1052,
      "external_id": "GO-Vianópolis",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    },
    {
      "id": 1052,
      "name": "Goiás",
      "type": "State",
      "parent_id": 1001,
      "external_id": "GO",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    },
    {
      "id": 1001,
      "name": "Brasil",
      "type": "Country",
      "external_id": "BR",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    }
  ]
}
```

##### Response 400

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=GET path=/divisions-core/v1/administrative-division/external-id/{id}/ancestors operationId=get-v1-admin-division-ancestors-external-id -->
### `GET /divisions-core/v1/administrative-division/external-id/{id}/ancestors` — Get admin division ancestors by external ID (deprecated)

- **operationId:** `get-v1-admin-division-ancestors-external-id`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call [List holiday calendars](ref:list-holiday-calendars) instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> List ancestors for an administrative division using an external ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | string | Client-supplied external ID |  |
| `page` | query | yes | integer | Page must be greater than `0`. Default = `1`. |  |
| `perPage` | query | yes | integer | PerPage must be greater than `0`. Default = `10`. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Paginated list of administrative divisions. | `application/json`: object (schema `pagination.Pagination`) |
| 400 | Bad request error. | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pages` | integer | no | Total number of result pages. | example: 1 |
| `current_page` | integer | no | Current result page. | example: 1 |
| `per_page` | integer | no | Maximum results per page. | example: 10 |
| `total_items` | integer | no | Total number of result items. | example: 1 |
| `items` | array of object (schema `presenter.v1AdministrativeDivisionResponse`) | no |  |  |

200 Example `PaginatedListOfAdministrativeDivisionsTree` — from `#/components/examples/GetPaginatedListOfAdministrativeDivisionsAncestors`:

```json
{
  "pages": 1,
  "current_page": 1,
  "per_page": 10,
  "total_items": 3,
  "items": [
    {
      "id": 5222005,
      "name": "Vianópolis",
      "type": "City",
      "parent_id": 1052,
      "external_id": "GO-Vianópolis"
    },
    {
      "id": 1052,
      "name": "Goiás",
      "type": "State",
      "parent_id": 1001,
      "external_id": "GO"
    },
    {
      "id": 1001,
      "name": "Brasil",
      "type": "Country",
      "external_id": "BR"
    }
  ]
}
```

200 Example `PaginatedListOfAdministrativeDivisionsTreeWithMetadata` — from `#/components/examples/GetPaginatedListOfAdministrativeDivisionsAncestorsWithMetadata`:

```json
{
  "pages": 1,
  "current_page": 1,
  "per_page": 10,
  "total_items": 3,
  "items": [
    {
      "id": 5222005,
      "name": "Vianópolis",
      "type": "City",
      "parent_id": 1052,
      "external_id": "GO-Vianópolis",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    },
    {
      "id": 1052,
      "name": "Goiás",
      "type": "State",
      "parent_id": 1001,
      "external_id": "GO",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    },
    {
      "id": 1001,
      "name": "Brasil",
      "type": "Country",
      "external_id": "BR",
      "working_days": [
        1,
        2,
        3,
        4,
        5
      ],
      "metadata": {
        "accrue_interest": true,
        "check_dormancy": true,
        "create_account": false,
        "defer_statement_due_date": true,
        "defer_transactions": true,
        "post_interest": false,
        "post_transactions": false,
        "run_cycle_closing": false
      }
    }
  ]
}
```

##### Response 400

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `True`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/handler.HTTPError -->
### Schema `handler.HTTPError`

Pointer: `#/components/schemas/handler.HTTPError`. Type: object (schema `handler.HTTPError`).

> Code and error message.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code |  |
| `message` | string | no | Error message |  |

<!-- schema: #/components/schemas/presenter.v1AdministrativeDivisionResponse -->
### Schema `presenter.v1AdministrativeDivisionResponse`

Pointer: `#/components/schemas/presenter.v1AdministrativeDivisionResponse`. Type: object (schema `presenter.v1AdministrativeDivisionResponse`).

> Administrative division data.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AdminDivisionID`) | no | Admininistrative division ID | example: 84849 |
| `name` | string (schema `AdminDivisionName`) | no | Administrative division name | example: "Scotland" |
| `type` | string (schema `AdminDivisionType`) | no | Admin division type | enum: ["City", "State", "Country"]; example: "State" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |

## Lifecycle status

- `POST /divisions-core/v1/administrative-division` (`post-v1-admin-division`) is marked `deprecated: true` in the specification.
- `GET /divisions-core/v1/administrative-division/external-id/{id}` (`get-v1-admin-division-external-id`) is marked `deprecated: true` in the specification.
- `GET /divisions-core/v1/administrative-division/{id}` (`get-v1-admin-division`) is marked `deprecated: true` in the specification.
- `PUT /divisions-core/v1/administrative-division/{id}` (`put-v1-admin-division`) is marked `deprecated: true` in the specification.
- `DELETE /divisions-core/v1/administrative-division/{id}` (`delete-v1-admin-division`) is marked `deprecated: true` in the specification.
- `GET /divisions-core/v1/administrative-division/{id}/tree` (`get-v1-admin-division-tree-parent-id`) is marked `deprecated: true` in the specification.
- `GET /divisions-core/v1/administrative-division/external-id/{id}/tree` (`get-v1-admin-division-tree-external-id`) is marked `deprecated: true` in the specification.
- `GET /divisions-core/v1/administrative-division/{id}/ancestors` (`get-v1-admin-division-ancestors-administrative-division-id`) is marked `deprecated: true` in the specification.
- `GET /divisions-core/v1/administrative-division/external-id/{id}/ancestors` (`get-v1-admin-division-ancestors-external-id`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Divisions.yaml` | tag `Administrative divisions (deprecated)`: POST /divisions-core/v1/administrative-division, GET /divisions-core/v1/administrative-division/external-id/{id}, GET /divisions-core/v1/administrative-division/{id}, PUT /divisions-core/v1/administrative-division/{id}, DELETE /divisions-core/v1/administrative-division/{id}, GET /divisions-core/v1/administrative-division/{id}/tree, GET /divisions-core/v1/administrative-division/external-id/{id}/tree, GET /divisions-core/v1/administrative-division/{id}/ancestors, GET /divisions-core/v1/administrative-division/external-id/{id}/ancestors | https://github.com/PismoDevEx/pismo-api-specs | `96de390559b33b89…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-platform-setup-holidays` — Platform setup - Holidays and administrative divisions
- `KU-CRED-holidays-in-credit-card-accounts` — Holidays in credit card accounts
