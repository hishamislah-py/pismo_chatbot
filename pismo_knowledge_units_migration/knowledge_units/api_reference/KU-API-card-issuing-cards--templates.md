---
ku_id: KU-API-card-issuing-cards--templates
title: 'API reference: Card issuing - Cards — Templates'
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
operations:
- get-card-template-by-id
- get-card-templates
related_kus:
- KU-CARD-bin-override-feature
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Templates

**KU ID:** `KU-API-card-issuing-cards--templates` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Templates` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Card template (BIN override) endpoints.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /cards/v1/templates/{templateID}` | `get-card-template-by-id` | Get card template | no |
| `GET /cards/v1/templates` | `get-card-templates` | List card templates | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/cards/v1/templates/{templateID} operationId=get-card-template-by-id -->
### `GET /cards/v1/templates/{templateID}` — Get card template

- **operationId:** `get-card-template-by-id`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Templates`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get card template. Templates are used to overwrite program card BIN defaults. 
>
> To create a template, you need to open a Pismo [Service Desk](doc:service-desk) request. The ticket type should be **Settings**. For more information, refer to the [BIN override](doc:bin-override-feature) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `templateID` | path | yes | string | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the BIN override documentation in the [Cards overview](doc:cards-overview-1#bin-override---shared-account-option) guide. To create a template, you need to open a Pismo [Service Desk](doc:service-desk) request. The ticket type should be **Settings**.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Card template | `application/json`: object (schema `GetTemplateByIdResponse`) |
| 400 | Bad Request |  |
| 404 | The specified resource was not found |  |
| 409 | Specified resource status conflict with current request |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `override_program_id` | integer | no | Program ID | example: 8675 |
| `bin_range_beginning` | string | no | BIN range beginning | example: "1500" |
| `bin_range_end` | string | no | BIN range end | example: "2500" |
| `bin` | string (schema `BIN`) | no | Bank Identification Number (BIN). A 6 or 8 digit number identitying the card network, issuer, and product. | example: "87634277" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-bin-override-feature`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/cards/v1/templates operationId=get-card-templates -->
### `GET /cards/v1/templates` — List card templates

- **operationId:** `get-card-templates`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Templates`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets the BIN data for an organization's card templates with paging options. For complete information on a specific template, call the [Get card template](ref:get-card-template-by-id) endpoint. The organization is identified in the access token.
>
> To create a template, you need to open a Pismo [Service Desk](doc:service-desk) request. The ticket type should be **Settings**. For more information, refer to the [BIN override](doc:bin-override-feature) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page_size` | query | yes | integer | Page size, 1-50 |  |
| `last_page_id` | query | no | string | Last page ID, required for paging. This field is returned if there is more data and it must be passed to get the next page. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Your Orgs's paged templates list | `application/json`: object (schema `GetTemplatesResponse`) |
| 400 | Bad Request |  |
| 404 | The specified resource was not found |  |
| 409 | Specified resource status conflict with current request |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `SummaryTemplate`) | no | Template summaries - 50 maximum. | minLength: 1; maxLength: 50 |
| `last_page_id` | string | no | If not null there is more data. Pass this field in the next request for additional content. | format: "uuid" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-bin-override-feature`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/SummaryTemplate -->
### Schema `SummaryTemplate`

Pointer: `#/components/schemas/SummaryTemplate`. Type: object (schema `SummaryTemplate`).

> Template summary. Templates are used for the BIN override feature.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `template_id` | string (schema `TemplateID`) | no | Template ID. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](doc:bin-override-feature) guide.<br> | example: "EAFA693A-57B2-4029-97F3-D20D6F06D79B" |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `override_program_id` | integer | no | Override program ID | example: 8849 |
| `bin_range_beginning` | string | no | BIN range beginning | example: "1500" |
| `bin_range_end` | string | no | BIN range end | example: "2500" |
| `bin` | string (schema `BIN`) | no | Bank Identification Number (BIN). A 6 or 8 digit number identitying the card network, issuer, and product. | example: "87634277" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Templates`: GET /cards/v1/templates/{templateID}, GET /cards/v1/templates | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-bin-override-feature` — BIN override - shared account option
