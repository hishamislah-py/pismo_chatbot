---
ku_id: KU-API-platform-setup-organizations--orgs
title: 'API reference: Platform setup - Organizations — Orgs'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Platform_setup_-_Organizations.yaml
  sha256: a1a72a2b080121e0dbaa5b67c207e5a4c60bf8106801fc485804a437c1acff0a
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
- patch-v1-orgs
- get-v1-org
related_kus:
- KU-ERR-codes-eoa
- KU-GS-get-started-with-pismo-apis
- KU-GS-setup-overview
specification_version: v1.0
---

# API reference: Platform setup - Organizations — Orgs

**KU ID:** `KU-API-platform-setup-organizations--orgs` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Orgs` in `api-specs/Platform_setup_-_Organizations.yaml` (“Platform setup - Organizations”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> View and manage some general origanization configurations

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `PATCH /orgs-core/v1/orgs` | `patch-v1-orgs` | Update organization | no |
| `GET /orgs-core/v1/orgs/{id}` | `get-v1-org` | Get organization | no |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — All requests must be previously authenticated with an account-specific token.

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Organizations.yaml method=PATCH path=/orgs-core/v1/orgs operationId=patch-v1-orgs -->
### `PATCH /orgs-core/v1/orgs` — Update organization

- **operationId:** `patch-v1-orgs`
- **Specification:** `api-specs/Platform_setup_-_Organizations.yaml` (Platform setup - Organizations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Orgs`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Performs a partial update of an organization's information. Fields not passed are not updated.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Pismo organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `PatchOrgRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `official_name` | string (schema `OfficialName`) | no | Your company's legal name | minLength: 1; maxLength: 100; example: "Acme Corporation" |
| `org_name` | string (schema `OrgName`) | no | Organization display name on the Pismo platform | minLength: 1; maxLength: 80; example: "Acme Corporation" |
| `start_date` | string (schema `StartDate`) | no | Organization start date, provided for client tracking. RFC 3339 format. <br> | example: "2019-07-03T17:23:18Z" |
| `expiration_date` | string (schema `ExpirationDate`) | no | Organization end date, provided for client tracking. RFC 3339 format. <br> | example: "2019-07-03T17:23:18Z" |
| `document_number` | string (schema `DocumentNumber`) | no | Numeric ID that identifies your company (such as a government tax ID number) | maxLength: 20; example: "08350504000143" |
| `address` | string (schema `StreetAddress`) | no | Your company's street name | maxLength: 80; example: "Main Street" |
| `number` | integer (schema `AddressNumber`) | no | Your company's address number | format: "int32"; example: 900 |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Any additional address information (unit, floor, and so on) | maxLength: 50; example: "Suite 123" |
| `neighborhood` | string (schema `Neighborhood`) | no | Neighborhood. Some countries use neighborhood in their addresses. | maxLength: 50; example: "Bunker Hill" |
| `zipcode` | string (schema `PostalCode`) | no | ZIP/postal code | maxLength: 9; example: "11203" |
| `city` | string (schema `City`) | no | City name | maxLength: 60; example: "New York" |
| `state` | string (schema `State`) | no | State/province/region. ISO 3166-2 (2 char) format. | maxLength: 2; example: "NY" |
| `country` | string (schema `Country`) | no | Country name | maxLength: 30; example: "United States of America" |
| `legal_proxy_name` | string (schema `LegalProxyName`) | no | Name of your organization's legal representative (person or other entity) | maxLength: 50; example: "Acme Corporation LTDA" |
| `responsible` | string (schema `Responsible`) | no | Email of person at organization who can be contacted if necessary. | maxLength: 255 |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | ISO 4217 3-digit currency numeric code. | maxLength: 3; example: "986" |
| `timezone` | string (schema `Timezone`) | no | Timezone in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank">TZ country/city or region format</a> | maxLength: 60; example: "America/New_York" |
| `language` | string (schema `Language`) | no | Language. Default is `en-US` | enum: ["en-US", "pt-BR"]; default: "en-US"; example: "en-US" |
| `country_code` | string (schema `CountryCode`) | no | <a href="https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes" target="_blank">ISO-3166</a> three-letter country code. | maxLength: 3; example: "USA" |
| `cycle_closing` | string (schema `CycleClosing`) | no | Cycle closing time. Format = HH:MM:SS | example: "12:00:00" |
| `holiday_calendar_id` | number (schema `HolidayCalendarId`) | no | Holiday calendar ID. | example: 8675309 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Org data | `application/json`: object (schema `OrgDetails`) |
| 400 | Bad Request | `application/json`: object (schema `HTTPError`) |
| 401 | Unauthorized |  |
| 404 | Not Found |  |
| 500 | Internal Server Error | `application/json`: object (schema `HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `OrgID`) | no | Pismo organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `official_name` | string (schema `OfficialName`) | no | Your company's legal name | minLength: 1; maxLength: 100; example: "Acme Corporation" |
| `org_name` | string (schema `OrgName`) | no | Organization display name on the Pismo platform | minLength: 1; maxLength: 80; example: "Acme Corporation" |
| `start_date` | string (schema `StartDate`) | no | Organization start date, provided for client tracking. RFC 3339 format. <br> | example: "2019-07-03T17:23:18Z" |
| `expiration_date` | string (schema `ExpirationDate`) | no | Organization end date, provided for client tracking. RFC 3339 format. <br> | example: "2019-07-03T17:23:18Z" |
| `document_number` | string (schema `DocumentNumber`) | no | Numeric ID that identifies your company (such as a government tax ID number) | maxLength: 20; example: "08350504000143" |
| `address` | string (schema `StreetAddress`) | no | Your company's street name | maxLength: 80; example: "Main Street" |
| `number` | integer (schema `AddressNumber`) | no | Your company's address number | format: "int32"; example: 900 |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Any additional address information (unit, floor, and so on) | maxLength: 50; example: "Suite 123" |
| `neighborhood` | string (schema `Neighborhood`) | no | Neighborhood. Some countries use neighborhood in their addresses. | maxLength: 50; example: "Bunker Hill" |
| `zipcode` | string (schema `PostalCode`) | no | ZIP/postal code | maxLength: 9; example: "11203" |
| `city` | string (schema `City`) | no | City name | maxLength: 60; example: "New York" |
| `state` | string (schema `State`) | no | State/province/region. ISO 3166-2 (2 char) format. | maxLength: 2; example: "NY" |
| `country` | string (schema `Country`) | no | Country name | maxLength: 30; example: "United States of America" |
| `legal_proxy_name` | string (schema `LegalProxyName`) | no | Name of your organization's legal representative (person or other entity) | maxLength: 50; example: "Acme Corporation LTDA" |
| `legal_proxy_document` | string (schema `LegalProxyDocument`) | no | ID (such as a government tax ID number) of your organization's legal representative | maxLength: 20; example: "123456" |
| `responsible` | string (schema `Responsible`) | no | Email of person at organization who can be contacted if necessary. | maxLength: 255 |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | ISO 4217 3-digit currency numeric code. | maxLength: 3; example: "986" |
| `timezone` | string (schema `Timezone`) | no | Timezone in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank">TZ country/city or region format</a> | maxLength: 60; example: "America/New_York" |
| `language` | string (schema `Language`) | no | Language. Default is `en-US` | enum: ["en-US", "pt-BR"]; default: "en-US"; example: "en-US" |
| `country_code` | string (schema `CountryCode`) | no | <a href="https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes" target="_blank">ISO-3166</a> three-letter country code. | maxLength: 3; example: "USA" |
| `cycle_closing` | string (schema `CycleClosing`) | no | Cycle closing time. Format = HH:MM:SS | example: "12:00:00" |
| `holiday_calendar_id` | number (schema `HolidayCalendarId`) | no | Holiday calendar ID. | example: 8675309 |

200 Example `response-v1-orgs` — from `#/components/examples/OrgDetails`:

```json
{
  "id": "TN-00000000000001",
  "official_name": "Acme Corp",
  "org_name": "Acme",
  "document_number": "123456789",
  "address": "Main Street",
  "number": 25,
  "complementary_address": "Suite 9",
  "neighborhood": "Brooklyn",
  "zipcode": "12345",
  "city": "New York",
  "state": "NY",
  "country": "United Stated of America",
  "legal_proxy_name": "Acme corporation LLC",
  "legal_proxy_document": "95123123123",
  "currency_numeric_code": "986",
  "timezone": "America/New York",
  "language": "en-US",
  "country_code": "USA"
}
```

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "EOA0030",
  "message": "Missing x-tenant header"
}
```

400 Example `tenant-not-found` — from `#/components/examples/TenantNotFoundResponse`:

```json
{
  "code": "EOA0100",
  "message": "Org TN-00000000000001 was not found"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EOA0001",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EOA0030` | Missing x-tenant header |
| 400 | `EOA0100` | Org TN-00000000000001 was not found |
| 500 | `EOA0001` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-GS-setup-overview`.

<!-- op: spec=api-specs/Platform_setup_-_Organizations.yaml method=GET path=/orgs-core/v1/orgs/{id} operationId=get-v1-org -->
### `GET /orgs-core/v1/orgs/{id}` — Get organization

- **operationId:** `get-v1-org`
- **Specification:** `api-specs/Platform_setup_-_Organizations.yaml` (Platform setup - Organizations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Orgs`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Returns information about a specific organization.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | string | Org ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `x-tenant` | header | yes | string | Pismo organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Org data | `application/json`: object (schema `OrgDetails`) |
| 400 | Bad Request | `application/json`: object (schema `HTTPError`) |
| 401 | Unauthorized |  |
| 404 | Not Found |  |
| 500 | Internal Server Error | `application/json`: object (schema `HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `OrgID`) | no | Pismo organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `official_name` | string (schema `OfficialName`) | no | Your company's legal name | minLength: 1; maxLength: 100; example: "Acme Corporation" |
| `org_name` | string (schema `OrgName`) | no | Organization display name on the Pismo platform | minLength: 1; maxLength: 80; example: "Acme Corporation" |
| `start_date` | string (schema `StartDate`) | no | Organization start date, provided for client tracking. RFC 3339 format. <br> | example: "2019-07-03T17:23:18Z" |
| `expiration_date` | string (schema `ExpirationDate`) | no | Organization end date, provided for client tracking. RFC 3339 format. <br> | example: "2019-07-03T17:23:18Z" |
| `document_number` | string (schema `DocumentNumber`) | no | Numeric ID that identifies your company (such as a government tax ID number) | maxLength: 20; example: "08350504000143" |
| `address` | string (schema `StreetAddress`) | no | Your company's street name | maxLength: 80; example: "Main Street" |
| `number` | integer (schema `AddressNumber`) | no | Your company's address number | format: "int32"; example: 900 |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Any additional address information (unit, floor, and so on) | maxLength: 50; example: "Suite 123" |
| `neighborhood` | string (schema `Neighborhood`) | no | Neighborhood. Some countries use neighborhood in their addresses. | maxLength: 50; example: "Bunker Hill" |
| `zipcode` | string (schema `PostalCode`) | no | ZIP/postal code | maxLength: 9; example: "11203" |
| `city` | string (schema `City`) | no | City name | maxLength: 60; example: "New York" |
| `state` | string (schema `State`) | no | State/province/region. ISO 3166-2 (2 char) format. | maxLength: 2; example: "NY" |
| `country` | string (schema `Country`) | no | Country name | maxLength: 30; example: "United States of America" |
| `legal_proxy_name` | string (schema `LegalProxyName`) | no | Name of your organization's legal representative (person or other entity) | maxLength: 50; example: "Acme Corporation LTDA" |
| `legal_proxy_document` | string (schema `LegalProxyDocument`) | no | ID (such as a government tax ID number) of your organization's legal representative | maxLength: 20; example: "123456" |
| `responsible` | string (schema `Responsible`) | no | Email of person at organization who can be contacted if necessary. | maxLength: 255 |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | ISO 4217 3-digit currency numeric code. | maxLength: 3; example: "986" |
| `timezone` | string (schema `Timezone`) | no | Timezone in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank">TZ country/city or region format</a> | maxLength: 60; example: "America/New_York" |
| `language` | string (schema `Language`) | no | Language. Default is `en-US` | enum: ["en-US", "pt-BR"]; default: "en-US"; example: "en-US" |
| `country_code` | string (schema `CountryCode`) | no | <a href="https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes" target="_blank">ISO-3166</a> three-letter country code. | maxLength: 3; example: "USA" |
| `cycle_closing` | string (schema `CycleClosing`) | no | Cycle closing time. Format = HH:MM:SS | example: "12:00:00" |
| `holiday_calendar_id` | number (schema `HolidayCalendarId`) | no | Holiday calendar ID. | example: 8675309 |

200 Example `response-v1-orgs` — from `#/components/examples/OrgDetails`:

```json
{
  "id": "TN-00000000000001",
  "official_name": "Acme Corp",
  "org_name": "Acme",
  "document_number": "123456789",
  "address": "Main Street",
  "number": 25,
  "complementary_address": "Suite 9",
  "neighborhood": "Brooklyn",
  "zipcode": "12345",
  "city": "New York",
  "state": "NY",
  "country": "United Stated of America",
  "legal_proxy_name": "Acme corporation LLC",
  "legal_proxy_document": "95123123123",
  "currency_numeric_code": "986",
  "timezone": "America/New York",
  "language": "en-US",
  "country_code": "USA"
}
```

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "EOA0030",
  "message": "Missing x-tenant header"
}
```

400 Example `different-x-tenant-header` — from `#/components/examples/XTenantDiffResponse`:

```json
{
  "code": "EOA0035",
  "message": "X-Tenant header and request are different"
}
```

400 Example `tenant-not-found` — from `#/components/examples/TenantNotFoundResponse`:

```json
{
  "code": "EOA0100",
  "message": "Org TN-00000000000001 was not found"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EOA0001",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EOA0030` | Missing x-tenant header |
| 400 | `EOA0035` | X-Tenant header and request are different |
| 400 | `EOA0100` | Org TN-00000000000001 was not found |
| 500 | `EOA0001` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-GS-get-started-with-pismo-apis`, `KU-GS-setup-overview`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/HTTPError -->
### Schema `HTTPError`

Pointer: `#/components/schemas/HTTPError`. Type: object (schema `HTTPError`).

> Error

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code |  |
| `message` | string | no |  |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Organizations.yaml` | tag `Orgs`: PATCH /orgs-core/v1/orgs, GET /orgs-core/v1/orgs/{id} | https://github.com/PismoDevEx/pismo-api-specs | `a1a72a2b080121e0…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-eoa` — Error codes: EOA
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
- `KU-GS-setup-overview` — Core objects
