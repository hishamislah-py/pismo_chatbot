---
ku_id: KU-API-platform-setup-programs--programs-part-02
title: 'API reference: Platform setup - Programs — Programs (part 2 of 2)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Platform_setup_-_Programs.yaml
  sha256: aec6c882f89e07d6f0531e8d644e31301ada4d679526437ef4762f5598bb0bb3
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
- programs
- program
- get-program-v1
- UpdateProgramInfo
related_kus:
- KU-CC-programs
- KU-CORE-accounts-overview
- KU-ERR-codes-eoa
- KU-EVT-catalogue-other-domains
specification_version: v1.0
---

# API reference: Platform setup - Programs — Programs (part 2 of 2)

**KU ID:** `KU-API-platform-setup-programs--programs-part-02` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Programs` in `api-specs/Platform_setup_-_Programs.yaml` (“Platform setup - Programs”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Create and manage programs

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /programs/v1/programs` | `programs` | List programs | no |
| `GET /programs/v2/programs/{id}` | `program` | Get program V2 | no |
| `GET /programs/v1/programs/{id}` | `get-program-v1` | Get program V1 | no |
| `PATCH /programs/v1/programs/{id}` | `UpdateProgramInfo` | Update program | no |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must be previoulsy authenticated.

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v1/programs operationId=programs -->
### `GET /programs/v1/programs` — List programs

- **operationId:** `programs`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Programs`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> List an organization's programs. The organization ID is parsed from the token.
>
> For information about programs and organizations, refer to [Core objects](doc:setup-overview).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | no | integer | Current page number. Must be greater than `0`. Default = `1`. | format: "int32"; example: 2 |
| `perPage` | query | no | integer | Maximum number of items per page. Must be greater than `0`. Default = `10`. | format: "int32"; example: 20 |
| `order` | query | no | string | Sort order. Default = `ASC`. | enum: ["ASC", "DESC"]; example: "DESC" |
| `orderBy` | query | no | string | Field to sort on. Default = `ID`. | enum: ["ID", "NAME"]; example: "NAME" |
| `id` | query | no | integer | Program ID filter | format: "int64"; example: 12345 |
| `name` | query | no | string | Program name filter | maxLength: 50; example: "Pismolabs" |
| `type` | query | no | string | Program type:<br /><br>  `CREDITO` — Full balance credit accounts<br /><br>  `PRE-PAGO` — Full balance prepaid accounts<br /><br>  `DEBITO` — Full balance debit accounts<br /><br>  `MERCHANT` — Merchant accounts<br /><br>  `CREDITO ZERO-BALANCE` — Zero balance credit accounts<br /><br>  `PRE-PAGO ZERO-BALANCE` — Zero balance prepaid accounts<br /><br>  `DEBITO ZERO-BALANCE` — Zero balance debit accounts<br /><br>  `CURRENT ACCOUNTS` — Current accounts<br /><br>  `INTERNAL ACCOUNTS` — Internal accounts<br /><br>  `CORRESPONDENT ACCOUNTS` — Correspondent accounts<br /><br>  `VOUCHER` - Prepaid voucher meal/food card<br /><br><br>For more information, refer to [Program types](https://developers.pismo.io/pismo-docs/docs/program-types).<br> | enum: ["CREDITO", "PRE-PAGO", "DEBITO", "MERCHANT", "CREDITO ZERO-BALANCE", "PRE-PAGO ZERO-BALANCE", "DEBITO ZERO-BALANCE", "CURRENT ACCOUNTS", "INTERNAL ACCOUNTS", "CORRESPONDENT ACCOUNTS", "VOUCHER"]; maxLength: 30; example: "CURRENT ACCOUNTS" |
| `binValue` | query | no | string | Bank Identification Number (BIN) value filter. Card network-issued 6 or 8 digit value identifying the card network, issuer, and product. | maxLength: 8; example: "123456" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramPage`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `items` | array of object (schema `Program`) (schema `ProgramItems`) | no |  |  |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum items per page | format: "int32"; example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int32"; example: 3 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v2/programs/{id} operationId=program -->
### `GET /programs/v2/programs/{id}` — Get program V2

- **operationId:** `program`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Programs`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Retrieve program details.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Program ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramDetails`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bin` | object (schema `Bin`) | no | Bank Identification Number (BIN) object. **REQUIRED** for card-issuing programs. <br> |  |
| `assignor_charge` | object (schema `Assignor`) | no | Assignor |  |
| `assignor_invoice` | object (schema `Assignor`) | no | Assignor |  |
| `brand` | object (schema `BrandData`) | no |  |  |
| `css` | string (schema `CSS`) | no | Card image. [Legacy - restricted] |  |
| `id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `base_program_id` | integer (schema `BaseProgramID`) | no | ID of program that was used to create this program. | format: "int64"; example: 2 |
| `initial_card_status` | string (schema `InitialCardStatus`) | no | Initial status for cards created in this program. | enum: ["CREATED", "BLOCKED", "UNBLOCKED"]; example: "CREATED" |
| `name` | string (schema `ProgramName`) | no | Program name | maxLength: 50; example: "Acme debit program" |
| `print_card` | boolean (schema `PrintCardBoolean`) | no | Should physical cards be issued by default on creation? Default is `false`. [Legacy - restricted] | example: true |
| `type` | object (schema `ProgramTypeData`) | no |  |  |
| `url_image` | string (schema `UrlImage`) | no | Program image URL [Legacy - restricted] |  |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | Program ISO 4217 currency code. | example: "986" |
| `timezone` | string (schema `TimeZone`) | no | Program timezone. This is the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank"> IANA (Internet Assigned Numbers Authority) time zone database</a> "Region/City" format.<br> | example: "America/Anchorage" |
| `country_code` | string (schema `CountryCode`) | no | <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3" target="_blank">ISO 3166 Alpha-3</a> program country code. For example, `BRA` = Brazil. | example: "BRA" |
| `created_at` | string (schema `CreatedAt`) | no | Program creation datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-07-06T13:11:05Z" |
| `status` | string (schema `ProgramStatus`) | no | Program status:<br> * `ACTIVE` - A program is active when PCI settings and accounting stages are configured.<br> * `PENDING` - A program is pending when PCI settings and accounting stages are not configured. A program that is pending is not ready for use.<br> | enum: ["ACTIVE", "PENDING"]; example: "PENDING" |
| `language` | string (schema `ProgramLanguage`) | no | Program Language:<br><br>* `en-US` - US English<br>* `pt-BR` - Brazilian Portuguese<br><br>Default is `en-US`<br> | enum: ["pt-BR", "en-US"]; example: "en-US" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v1/programs/{id} operationId=get-program-v1 -->
### `GET /programs/v1/programs/{id}` — Get program V1

- **operationId:** `get-program-v1`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Programs`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Get details for a specific [program](doc:program-types).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Program ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `Program`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bin` | object (schema `Bin`) | no | Bank Identification Number (BIN) object. **REQUIRED** for card-issuing programs. <br> |  |
| `brand` | string (schema `Brand`) | no | Program's card brand.  **REQUIRED** for card-issuing programs.<br> | enum: ["VISA", "MASTERCARD", "ELO", "RUPAY", "PRIVATE", "CABAL", "GOODCARD"]; example: "VISA" |
| `css` | string (schema `CSS`) | no | Card image. [Legacy - restricted] |  |
| `id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `base_program_id` | integer (schema `BaseProgramID`) | no | ID of program that was used to create this program. | format: "int64"; example: 2 |
| `initial_card_status` | string (schema `InitialCardStatus`) | no | Initial status for cards created in this program. | enum: ["CREATED", "BLOCKED", "UNBLOCKED"]; example: "CREATED" |
| `name` | string (schema `ProgramName`) | no | Program name | maxLength: 50; example: "Acme debit program" |
| `print_card` | boolean (schema `PrintCardBoolean`) | no | Should physical cards be issued by default on creation? Default is `false`. [Legacy - restricted] | example: true |
| `provider` | object (schema `Provider`) | no | [Legacy - restricted] |  |
| `type` | string (schema `ProgramType`) | no | Program type:<br /><br>  `CREDITO` — Full balance credit accounts<br /><br>  `PRE-PAGO` — Full balance prepaid accounts<br /><br>  `DEBITO` — Full balance debit accounts<br /><br>  `MERCHANT` — Merchant accounts<br /><br>  `CREDITO ZERO-BALANCE` — Zero balance credit accounts<br /><br>  `PRE-PAGO ZERO-BALANCE` — Zero balance prepaid accounts<br /><br>  `DEBITO ZERO-BALANCE` — Zero balance debit accounts<br /><br>  `CURRENT ACCOUNTS` — Current accounts<br /><br>  `INTERNAL ACCOUNTS` — Internal accounts<br /><br>  `CORRESPONDENT ACCOUNTS` — Correspondent accounts<br /><br>  `VOUCHER` - Prepaid voucher meal/food card<br /><br><br>For more information, refer to [Program types](https://developers.pismo.io/pismo-docs/docs/program-types)<br> | enum: ["CREDITO", "PRE-PAGO", "DEBITO", "MERCHANT", "CREDITO ZERO-BALANCE", "PRE-PAGO ZERO-BALANCE", "DEBITO ZERO-BALANCE", "CURRENT ACCOUNTS", "INTERNAL ACCOUNTS", "CORRESPONDENT ACCOUNTS", "VOUCHER"]; example: "CREDITO" |
| `url_image` | string (schema `UrlImage`) | no | Program image URL [Legacy - restricted] |  |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | Program ISO 4217 currency code. | example: "986" |
| `timezone` | string (schema `TimeZone`) | no | Program timezone. This is the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank"> IANA (Internet Assigned Numbers Authority) time zone database</a> "Region/City" format.<br> | example: "America/Anchorage" |
| `country_code` | string (schema `CountryCode`) | no | <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3" target="_blank">ISO 3166 Alpha-3</a> program country code. For example, `BRA` = Brazil. | example: "BRA" |
| `created_at` | string (schema `CreatedAt`) | no | Program creation datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-07-06T13:11:05Z" |
| `status` | string (schema `ProgramStatus`) | no | Program status:<br> * `ACTIVE` - A program is active when PCI settings and accounting stages are configured.<br> * `PENDING` - A program is pending when PCI settings and accounting stages are not configured. A program that is pending is not ready for use.<br> | enum: ["ACTIVE", "PENDING"]; example: "PENDING" |
| `language` | string (schema `ProgramLanguage`) | no | Program Language:<br><br>* `en-US` - US English<br>* `pt-BR` - Brazilian Portuguese<br><br>Default is `en-US`<br> | enum: ["pt-BR", "en-US"]; example: "en-US" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=PATCH path=/programs/v1/programs/{id} operationId=UpdateProgramInfo -->
### `PATCH /programs/v1/programs/{id}` — Update program

- **operationId:** `UpdateProgramInfo`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Programs`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Update a program.
>
> This endpoint generates a [Program updated](https://developers.pismo.io/events/docs/programs-update-1) event.
>
> **Note:** Due date is a **REQUIRED** field for [Full balance credit programs](doc:full-balance-credit-program) types.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Program ID | format: "int64"; example: 12345 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ProgramPatch`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bin` | object (schema `Bin`) | no | Bank Identification Number (BIN) object. **REQUIRED** for card-issuing programs. <br> |  |
| `name` | string (schema `ProgramName`) | no | Program name | maxLength: 50; example: "Acme debit program" |
| `timezone` | string (schema `TimeZone`) | no | Program timezone. This is the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank"> IANA (Internet Assigned Numbers Authority) time zone database</a> "Region/City" format.<br> | example: "America/Anchorage" |
| `country_code` | string (schema `CountryCode`) | no | <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3" target="_blank">ISO 3166 Alpha-3</a> program country code. For example, `BRA` = Brazil. | example: "BRA" |
| `due_dates` | array of object (schema `ProgramDueDatePatch`) (schema `DueDatesPatch`) | no |  |  |
| `language` | string (schema `ProgramLanguage`) | no | Program Language:<br><br>* `en-US` - US English<br>* `pt-BR` - Brazilian Portuguese<br><br>Default is `en-US`<br> | enum: ["pt-BR", "en-US"]; example: "en-US" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not Found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal Server Error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 400

400 Example `missing-x-tenant` — from `#/components/examples/ErrorMissingXTenantResponse`:

```json
{
  "code": "EOA0017",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-request` — from `#/components/examples/InvalidRequestResponse`:

```json
{
  "code": "EOA0080",
  "message": "Invalid request"
}
```

400 Example `error-to-binder` — from `#/components/examples/ErrorToBinderResponse`:

```json
{
  "code": "EOA0018",
  "message": "Error to Binder"
}
```

400 Example `invalid-timezone` — from `#/components/examples/InvalidTimezoneResponse`:

```json
{
  "code": "EOA0029",
  "message": "Invalid timezone: xxx"
}
```

400 Example `invalid-currency-numeric-code` — from `#/components/examples/InvalidCurrencyNumericCodeResponse`:

```json
{
  "code": "EOA0033",
  "message": "Invalid currency_numeric_code: xxx"
}
```

400 Example `invalid-country-code` — from `#/components/examples/InvalidCountryCodeResponse`:

```json
{
  "code": "EOA0063",
  "message": "Invalid country_code: xxx"
}
```

400 Example `should-not-contain-card-info` — from `#/components/examples/ShouldNotContainCardInformationResponse`:

```json
{
  "code": "EOA0055",
  "message": "Should not contain card information (Bin, Brand and DueDate)"
}
```

400 Example `card-info-bin-brand-required` — from `#/components/examples/CardInformationBinBrandRequiredResponse`:

```json
{
  "code": "EOA0073",
  "message": "Card information is required (Bin and Brand)"
}
```

400 Example `card-info-required` — from `#/components/examples/CardInformationRequiredResponse`:

```json
{
  "code": "EOA0054",
  "message": "Card information is required (Bin, Brand and DueDate)"
}
```

400 Example `invalid-bin-value` — from `#/components/examples/BinValueNotAValidNumberResponse`:

```json
{
  "code": "EOA0040",
  "message": "bin.value is not a valid number"
}
```

400 Example `invalid-bin-start-range` — from `#/components/examples/BinStartRangeNotAValidNumberResponse`:

```json
{
  "code": "EOA0040",
  "message": "bin.start_range is not a valid number"
}
```

400 Example `invalid-bin-end-range` — from `#/components/examples/BinEndRangeNotAValidNumberResponse`:

```json
{
  "code": "EOA0040",
  "message": "bin.end_range is not a valid number"
}
```

400 Example `invalid-bin` — from `#/components/examples/InvalidBin68Response`:

```json
{
  "code": "EOA0037",
  "message": "Bin must be 6 or 8 digits"
}
```

400 Example `invalid-bin-6-range` — from `#/components/examples/InvalidBinRange6Response`:

```json
{
  "code": "EOA0038",
  "message": "When a BIN is 6, the range can be up to 9 digits"
}
```

400 Example `invalid-bin-8-range` — from `#/components/examples/InvalidBinRange8Response`:

```json
{
  "code": "EOA0039",
  "message": "When a BIN is 8, the range can be up to 7 digits"
}
```

400 Example `invalid-due-dates` — from `#/components/examples/InvalidDueDatesResponse`:

```json
{
  "code": "EOA0082",
  "message": "Due dates need at least one active day"
}
```

400 Example `invalid-brand-orverwrite` — from `#/components/examples/InvalidBrandOverwriteResponse`:

```json
{
  "code": "EOA0059",
  "message": "It is not possible to update the Brand value, the value is already filled"
}
```

##### Response 404

404 Example `program-not-found` — from `#/components/examples/ProgramNotFoundResponse`:

```json
{
  "code": "EOA0020",
  "message": "Program x not found"
}
```

404 Example `brand-not-found` — from `#/components/examples/BrandNotFoundResponse`:

```json
{
  "code": "EOA0064",
  "message": "Brand not found"
}
```

##### Response 500

500 Example `fail-create-due-dates` — from `#/components/examples/FailCreateDueDatesResponse`:

```json
{
  "code": "EOA0034",
  "message": "Failed to create program due dates"
}
```

500 Example `connection-fail` — from `#/components/examples/ConnectionFailResponse`:

```json
{
  "code": "EOA0009",
  "message": "Connection failed with message: "
}
```

500 Example `connection-fail-2` — from `#/components/examples/ConnectionFailErrorResponse`:

```json
{
  "code": "EOA0010",
  "message": "Connection failed with message: "
}
```

500 Example `body-parsing-error` — from `#/components/examples/BodyParsingErrorResponse`:

```json
{
  "code": "EOA0008",
  "message": "Error parsing utils body with message: "
}
```

500 Example `body-parsing-error-2` — from `#/components/examples/BodyParsingError2Response`:

```json
{
  "code": "EOA0011",
  "message": "Error parsing utils body with message: "
}
```

500 Example `generic-error` — from `#/components/examples/GenericErrorResponse`:

```json
{
  "code": "EOA0015",
  "message": "Something went wrong, please try again later"
}
```

500 Example `generic-error-2` — from `#/components/examples/GenericError2Response`:

```json
{
  "code": "EOA0016",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EOA0017` | Missing x-tenant header |
| 400 | `EOA0080` | Invalid request |
| 400 | `EOA0018` | Error to Binder |
| 400 | `EOA0029` | Invalid timezone: xxx |
| 400 | `EOA0033` | Invalid currency_numeric_code: xxx |
| 400 | `EOA0063` | Invalid country_code: xxx |
| 400 | `EOA0055` | Should not contain card information (Bin, Brand and DueDate) |
| 400 | `EOA0073` | Card information is required (Bin and Brand) |
| 400 | `EOA0054` | Card information is required (Bin, Brand and DueDate) |
| 400 | `EOA0040` | bin.value is not a valid number |
| 400 | `EOA0037` | Bin must be 6 or 8 digits |
| 400 | `EOA0038` | When a BIN is 6, the range can be up to 9 digits |
| 400 | `EOA0039` | When a BIN is 8, the range can be up to 7 digits |
| 400 | `EOA0082` | Due dates need at least one active day |
| 400 | `EOA0059` | It is not possible to update the Brand value, the value is already filled |
| 404 | `EOA0020` | Program x not found |
| 404 | `EOA0064` | Brand not found |
| 500 | `EOA0034` | Failed to create program due dates |
| 500 | `EOA0009` | Connection failed with message: |
| 500 | `EOA0010` | Connection failed with message: |
| 500 | `EOA0008` | Error parsing utils body with message: |
| 500 | `EOA0011` | Error parsing utils body with message: |
| 500 | `EOA0015` | Something went wrong, please try again later |
| 500 | `EOA0016` | Something went wrong, please try again later |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `programs-update-1` | https://developers.pismo.io/events/docs/programs-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CC-programs`, `KU-CORE-accounts-overview`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Program -->
### Schema `Program`

Pointer: `#/components/schemas/Program`. Type: object (schema `Program`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bin` | object (schema `Bin`) | no | Bank Identification Number (BIN) object. **REQUIRED** for card-issuing programs. <br> |  |
| `brand` | string (schema `Brand`) | no | Program's card brand.  **REQUIRED** for card-issuing programs.<br> | enum: ["VISA", "MASTERCARD", "ELO", "RUPAY", "PRIVATE", "CABAL", "GOODCARD"]; example: "VISA" |
| `css` | string (schema `CSS`) | no | Card image. [Legacy - restricted] |  |
| `id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `base_program_id` | integer (schema `BaseProgramID`) | no | ID of program that was used to create this program. | format: "int64"; example: 2 |
| `initial_card_status` | string (schema `InitialCardStatus`) | no | Initial status for cards created in this program. | enum: ["CREATED", "BLOCKED", "UNBLOCKED"]; example: "CREATED" |
| `name` | string (schema `ProgramName`) | no | Program name | maxLength: 50; example: "Acme debit program" |
| `print_card` | boolean (schema `PrintCardBoolean`) | no | Should physical cards be issued by default on creation? Default is `false`. [Legacy - restricted] | example: true |
| `provider` | object (schema `Provider`) | no | [Legacy - restricted] |  |
| `type` | string (schema `ProgramType`) | no | Program type:<br /><br>  `CREDITO` — Full balance credit accounts<br /><br>  `PRE-PAGO` — Full balance prepaid accounts<br /><br>  `DEBITO` — Full balance debit accounts<br /><br>  `MERCHANT` — Merchant accounts<br /><br>  `CREDITO ZERO-BALANCE` — Zero balance credit accounts<br /><br>  `PRE-PAGO ZERO-BALANCE` — Zero balance prepaid accounts<br /><br>  `DEBITO ZERO-BALANCE` — Zero balance debit accounts<br /><br>  `CURRENT ACCOUNTS` — Current accounts<br /><br>  `INTERNAL ACCOUNTS` — Internal accounts<br /><br>  `CORRESPONDENT ACCOUNTS` — Correspondent accounts<br /><br>  `VOUCHER` - Prepaid voucher meal/food card<br /><br><br>For more information, refer to [Program types](https://developers.pismo.io/pismo-docs/docs/program-types)<br> | enum: ["CREDITO", "PRE-PAGO", "DEBITO", "MERCHANT", "CREDITO ZERO-BALANCE", "PRE-PAGO ZERO-BALANCE", "DEBITO ZERO-BALANCE", "CURRENT ACCOUNTS", "INTERNAL ACCOUNTS", "CORRESPONDENT ACCOUNTS", "VOUCHER"]; example: "CREDITO" |
| `url_image` | string (schema `UrlImage`) | no | Program image URL [Legacy - restricted] |  |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | Program ISO 4217 currency code. | example: "986" |
| `timezone` | string (schema `TimeZone`) | no | Program timezone. This is the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank"> IANA (Internet Assigned Numbers Authority) time zone database</a> "Region/City" format.<br> | example: "America/Anchorage" |
| `country_code` | string (schema `CountryCode`) | no | <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3" target="_blank">ISO 3166 Alpha-3</a> program country code. For example, `BRA` = Brazil. | example: "BRA" |
| `created_at` | string (schema `CreatedAt`) | no | Program creation datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-07-06T13:11:05Z" |
| `status` | string (schema `ProgramStatus`) | no | Program status:<br> * `ACTIVE` - A program is active when PCI settings and accounting stages are configured.<br> * `PENDING` - A program is pending when PCI settings and accounting stages are not configured. A program that is pending is not ready for use.<br> | enum: ["ACTIVE", "PENDING"]; example: "PENDING" |
| `language` | string (schema `ProgramLanguage`) | no | Program Language:<br><br>* `en-US` - US English<br>* `pt-BR` - Brazilian Portuguese<br><br>Default is `en-US`<br> | enum: ["pt-BR", "en-US"]; example: "en-US" |

<!-- schema: #/components/schemas/handler.HTTPError -->
### Schema `handler.HTTPError`

Pointer: `#/components/schemas/handler.HTTPError`. Type: object (schema `handler.HTTPError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Bad request code | example: "EOA0017" |
| `message` | string | no | Bad request response | example: "Bad Request" |

<!-- schema: #/components/schemas/Bin -->
### Schema `Bin`

Pointer: `#/components/schemas/Bin`. Type: object (schema `Bin`).

> Bank Identification Number (BIN) object. **REQUIRED** for card-issuing programs. 

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `start_range` | string | no | BIN range start.  **REQUIRED** for card-issuing programs. | example: "0" |
| `end_range` | string | no | BIN range end.  **REQUIRED** for card-issuing programs. | example: "999999999" |
| `value` | string | no | Card network-issued Bank Identification Number (BIN). <br>6 or 8-digit BIN identifying the card network, issuer, and product.<br> **REQUIRED** for card-issuing programs.<br> | example: "999999" |

<!-- schema: #/components/schemas/Assignor -->
### Schema `Assignor`

Pointer: `#/components/schemas/Assignor`. Type: object (schema `Assignor`).

> Assignor

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Assignor ID. Assignors are configured at the program level.<br> | format: "int64" |
| `name` | string | no | Assignor name |  |

<!-- schema: #/components/schemas/BrandData -->
### Schema `BrandData`

Pointer: `#/components/schemas/BrandData`. Type: object (schema `BrandData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Brand ID. <br> | format: "int64" |
| `description` | string | no | Program's card brand.  **REQUIRED** for card-issuing programs. | enum: ["VISA", "MASTERCARD", "ELO", "RUPAY", "PRIVATE", "CABAL", "GOODCARD"]; example: "VISA" |
| `pci` | boolean | no | Is specified program PCI (Payment Card Industry)? | example: true |

<!-- schema: #/components/schemas/ProgramTypeData -->
### Schema `ProgramTypeData`

Pointer: `#/components/schemas/ProgramTypeData`. Type: object (schema `ProgramTypeData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ProgramTypeID`) | no | Program type ID:<br />  <br><br>  `1` =  `CREDITO`<br />  <br>  `2` =  `PRE-PAGO`<br />  <br>  `3` = `DEBITO`<br />  <br>  `5` = `MERCHANT`<br />  <br>  `7` = `CREDITO ZERO-BALANCE`<br />  <br>  `8` = `PRE-PAGO ZERO-BALANCE`<br />  <br>  `9` = `DEBITO ZERO-BALANCE`<br />  <br>  `11` =` CURRENT ACCOUNTS`<br />  <br>  `12` = `INTERNAL ACCOUNTS`<br />  <br>  `13` = `CORRESPONDENT ACCOUNTS`<br />  <br>  `15` = `VOUCHER`<br />  <br><br>For more information, refer to [Program types](doc:program-types).<br> | format: "int64"; example: 1 |
| `description` | string (schema `ProgramType`) | no | Program type:<br /><br>  `CREDITO` — Full balance credit accounts<br /><br>  `PRE-PAGO` — Full balance prepaid accounts<br /><br>  `DEBITO` — Full balance debit accounts<br /><br>  `MERCHANT` — Merchant accounts<br /><br>  `CREDITO ZERO-BALANCE` — Zero balance credit accounts<br /><br>  `PRE-PAGO ZERO-BALANCE` — Zero balance prepaid accounts<br /><br>  `DEBITO ZERO-BALANCE` — Zero balance debit accounts<br /><br>  `CURRENT ACCOUNTS` — Current accounts<br /><br>  `INTERNAL ACCOUNTS` — Internal accounts<br /><br>  `CORRESPONDENT ACCOUNTS` — Correspondent accounts<br /><br>  `VOUCHER` - Prepaid voucher meal/food card<br /><br><br>For more information, refer to [Program types](https://developers.pismo.io/pismo-docs/docs/program-types)<br> | enum: ["CREDITO", "PRE-PAGO", "DEBITO", "MERCHANT", "CREDITO ZERO-BALANCE", "PRE-PAGO ZERO-BALANCE", "DEBITO ZERO-BALANCE", "CURRENT ACCOUNTS", "INTERNAL ACCOUNTS", "CORRESPONDENT ACCOUNTS", "VOUCHER"]; example: "CREDITO" |
| `mode` | string (schema `ProgramMode`) | no | Mode of the program type. It can be either `CREDIT` or `DEBIT`. | enum: ["CREDIT", "DEBIT"]; example: "CREDIT" |

<!-- schema: #/components/schemas/Provider -->
### Schema `Provider`

Pointer: `#/components/schemas/Provider`. Type: object (schema `Provider`).

> [Legacy - restricted]

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Provider ID (outdated) | format: "int64"; example: 12 |
| `name` | string | no | Provider name (outdated) | example: "Acme Services" |

<!-- schema: #/components/schemas/ProgramDueDatePatch -->
### Schema `ProgramDueDatePatch`

Pointer: `#/components/schemas/ProgramDueDatePatch`. Type: object (schema `ProgramDueDatePatch`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `active` | boolean (schema `DueDateActiveBoolean`) | no | Is due date active? | example: true |
| `day` | integer (schema `DueDateDay`) | no | Day of the month (1 to 28) for the statement due date. | format: "int32"; example: 10 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Programs.yaml` | tag `Programs`: GET /programs/v1/programs, GET /programs/v2/programs/{id}, GET /programs/v1/programs/{id}, PATCH /programs/v1/programs/{id} | https://github.com/PismoDevEx/pismo-api-specs | `aec6c882f89e07d6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CC-programs` — Control Center programs: create, edit, clone, export and import
- `KU-CORE-accounts-overview` — Accounts
- `KU-ERR-codes-eoa` — Error codes: EOA
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
