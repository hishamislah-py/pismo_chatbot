---
ku_id: KU-API-platform-setup-programs--programs-part-01
title: 'API reference: Platform setup - Programs — Programs (part 1 of 2)'
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
- CreateProgramBasedOnTemplate
- CreateProgramBasedOnTemplateAsync
- CopyProgram
- CopyProgramAsync
related_kus:
- KU-BANK-get-started-core-banking
- KU-BANK-get-started-demand-deposit-accounts
- KU-BANK-get-started-transaction-banking
- KU-CARD-implementation-steps
- KU-CC-programs
- KU-CRED-calendar-management-strategies
- KU-ERR-codes-eoa
- KU-EVT-catalogue-other-domains
- KU-GS-get-started-with-pismo-apis
- KU-GS-program-types
- KU-GS-setup-overview
- KU-LEND-get-started-lending
- KU-SELL-get-started-seller-management
- KU-SELL-seller-management-overview-and-onboarding
- KU-SELL-seller-marketplace-implementation-steps
specification_version: v1.0
---

# API reference: Platform setup - Programs — Programs (part 1 of 2)

**KU ID:** `KU-API-platform-setup-programs--programs-part-01` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Programs` in `api-specs/Platform_setup_-_Programs.yaml` (“Platform setup - Programs”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Create and manage programs

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | no |
| `POST /programs/v2/programs/template` | `CreateProgramBasedOnTemplateAsync` | Create program (async) | no |
| `POST /programs/v1/programs/copy` | `CopyProgram` | Copy program | no |
| `POST /programs/v2/programs/copy` | `CopyProgramAsync` | Copy program (async) | no |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must be previoulsy authenticated.

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=POST path=/programs/v1/programs/template operationId=CreateProgramBasedOnTemplate -->
### `POST /programs/v1/programs/template` — Create program

- **operationId:** `CreateProgramBasedOnTemplate`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Programs`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Create a program synchronously. 
>
> For more information about programs, refer to [Core objects](doc:setup-overview#program).
>
> This endpoint executes synchronously, meaning, a network timeout or similar network delay could occur. In this case, an error is generated. To avoid this possibility, call the [Create program (async)](ref:createprogrambasedontemplateasync) endpoint instead.
>
> Thie endpoint generates a [Program created](https://developers.pismo.io/events/docs/programs-creation-1) event. 
>
> To get your Organization's programs, call the [List programs](ref:programs-1) endpoint, or view them in the [Pismo Control Center](doc:get-started-with-control-center).

#### Request body

Required: yes

> Create program from template request

**Content type `application/json`** — schema: object (schema `ProgramFromTemplate`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `ProgramName`) | yes | Program name | maxLength: 50; example: "Acme debit program" |
| `type` | string (schema `ProgramType`) | yes | Program type:<br /><br>  `CREDITO` — Full balance credit accounts<br /><br>  `PRE-PAGO` — Full balance prepaid accounts<br /><br>  `DEBITO` — Full balance debit accounts<br /><br>  `MERCHANT` — Merchant accounts<br /><br>  `CREDITO ZERO-BALANCE` — Zero balance credit accounts<br /><br>  `PRE-PAGO ZERO-BALANCE` — Zero balance prepaid accounts<br /><br>  `DEBITO ZERO-BALANCE` — Zero balance debit accounts<br /><br>  `CURRENT ACCOUNTS` — Current accounts<br /><br>  `INTERNAL ACCOUNTS` — Internal accounts<br /><br>  `CORRESPONDENT ACCOUNTS` — Correspondent accounts<br /><br>  `VOUCHER` - Prepaid voucher meal/food card<br /><br><br>For more information, refer to [Program types](https://developers.pismo.io/pismo-docs/docs/program-types)<br> | enum: ["CREDITO", "PRE-PAGO", "DEBITO", "MERCHANT", "CREDITO ZERO-BALANCE", "PRE-PAGO ZERO-BALANCE", "DEBITO ZERO-BALANCE", "CURRENT ACCOUNTS", "INTERNAL ACCOUNTS", "CORRESPONDENT ACCOUNTS", "VOUCHER"]; example: "CREDITO" |
| `timezone` | string (schema `TimeZone`) | yes | Program timezone. This is the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank"> IANA (Internet Assigned Numbers Authority) time zone database</a> "Region/City" format.<br> | example: "America/Anchorage" |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | yes | Program ISO 4217 currency code. | example: "986" |
| `country_code` | string (schema `CountryCode`) | yes | <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3" target="_blank">ISO 3166 Alpha-3</a> program country code. For example, `BRA` = Brazil. | example: "BRA" |
| `bin` | object (schema `Bin`) | no | Bank Identification Number (BIN) object. **REQUIRED** for card-issuing programs. <br> |  |
| `brand` | string (schema `Brand`) | no | Program's card brand.  **REQUIRED** for card-issuing programs.<br> | enum: ["VISA", "MASTERCARD", "ELO", "RUPAY", "PRIVATE", "CABAL", "GOODCARD"]; example: "VISA" |
| `due_dates` | array of object (schema `ProgramDueDate`) (schema `DueDates`) | no | Array of available program due dates. Every program account specifies a due date to use.<br><br>A due date is **REQUIRED** for Full balance credit programs.<br><br>For each due date, `day` and `active` are **REQUIRED**, as in the following example:<br>```<br>{<br>    "due_dates": [<br>          {<br>            "day": 1,<br>            "active": true<br>          },<br>          {<br>            "day": 2,<br>            "active": false<br>          }<br>    ]<br>}<br>```<br>**Note:** The due date ID is passed as a **numeric value**. For example, for due date `1` (first day of the month) the ID could be something like `3063`. This is the value you should use. `day` must be between 1 and 28.<br> |  |
| `language` | string (schema `ProgramLanguage`) | no | Program Language:<br><br>* `en-US` - US English<br>* `pt-BR` - Brazilian Portuguese<br><br>Default is `en-US`<br> | enum: ["pt-BR", "en-US"]; example: "en-US" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramResponse`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not Found | `application/json`: object (schema `handler.HTTPError`) |
| 416 | Range not satisfiable | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal Server Error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bin` | object (schema `Bin`) | no | Bank Identification Number (BIN) object. **REQUIRED** for card-issuing programs. <br> |  |
| `brand` | string (schema `Brand`) | no | Program's card brand.  **REQUIRED** for card-issuing programs.<br> | enum: ["VISA", "MASTERCARD", "ELO", "RUPAY", "PRIVATE", "CABAL", "GOODCARD"]; example: "VISA" |
| `channels` | array of object (schema `Channel`) (schema `Channels`) | no | Program channels |  |
| `created_at` | string (schema `CreatedAt`) | no | Program creation datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-07-06T13:11:05Z" |
| `css` | string (schema `CSS`) | no | Card image. [Legacy - restricted] |  |
| `timezone` | string (schema `TimeZone`) | no | Program timezone. This is the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank"> IANA (Internet Assigned Numbers Authority) time zone database</a> "Region/City" format.<br> | example: "America/Anchorage" |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | Program ISO 4217 currency code. | example: "986" |
| `country_code` | string (schema `CountryCode`) | no | <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3" target="_blank">ISO 3166 Alpha-3</a> program country code. For example, `BRA` = Brazil. | example: "BRA" |
| `due_dates` | array of object (schema `ProgramDueDate`) (schema `DueDates`) | no | Array of available program due dates. Every program account specifies a due date to use.<br><br>A due date is **REQUIRED** for Full balance credit programs.<br><br>For each due date, `day` and `active` are **REQUIRED**, as in the following example:<br>```<br>{<br>    "due_dates": [<br>          {<br>            "day": 1,<br>            "active": true<br>          },<br>          {<br>            "day": 2,<br>            "active": false<br>          }<br>    ]<br>}<br>```<br>**Note:** The due date ID is passed as a **numeric value**. For example, for due date `1` (first day of the month) the ID could be something like `3063`. This is the value you should use. `day` must be between 1 and 28.<br> |  |
| `id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `initial_card_status` | string (schema `InitialCardStatus`) | no | Initial status for cards created in this program. | enum: ["CREATED", "BLOCKED", "UNBLOCKED"]; example: "CREATED" |
| `name` | string (schema `ProgramName`) | no | Program name | maxLength: 50; example: "Acme debit program" |
| `print_card` | boolean (schema `PrintCardBoolean`) | no | Should physical cards be issued by default on creation? Default is `false`. [Legacy - restricted] | example: true |
| `provider` | object (schema `Provider`) | no | [Legacy - restricted] |  |
| `status` | string (schema `ProgramStatus`) | no | Program status:<br> * `ACTIVE` - A program is active when PCI settings and accounting stages are configured.<br> * `PENDING` - A program is pending when PCI settings and accounting stages are not configured. A program that is pending is not ready for use.<br> | enum: ["ACTIVE", "PENDING"]; example: "PENDING" |
| `type` | string (schema `ProgramType`) | no | Program type:<br /><br>  `CREDITO` — Full balance credit accounts<br /><br>  `PRE-PAGO` — Full balance prepaid accounts<br /><br>  `DEBITO` — Full balance debit accounts<br /><br>  `MERCHANT` — Merchant accounts<br /><br>  `CREDITO ZERO-BALANCE` — Zero balance credit accounts<br /><br>  `PRE-PAGO ZERO-BALANCE` — Zero balance prepaid accounts<br /><br>  `DEBITO ZERO-BALANCE` — Zero balance debit accounts<br /><br>  `CURRENT ACCOUNTS` — Current accounts<br /><br>  `INTERNAL ACCOUNTS` — Internal accounts<br /><br>  `CORRESPONDENT ACCOUNTS` — Correspondent accounts<br /><br>  `VOUCHER` - Prepaid voucher meal/food card<br /><br><br>For more information, refer to [Program types](https://developers.pismo.io/pismo-docs/docs/program-types)<br> | enum: ["CREDITO", "PRE-PAGO", "DEBITO", "MERCHANT", "CREDITO ZERO-BALANCE", "PRE-PAGO ZERO-BALANCE", "DEBITO ZERO-BALANCE", "CURRENT ACCOUNTS", "INTERNAL ACCOUNTS", "CORRESPONDENT ACCOUNTS", "VOUCHER"]; example: "CREDITO" |
| `url_image` | string (schema `UrlImage`) | no | Program image URL [Legacy - restricted] |  |
| `language` | string (schema `ProgramLanguage`) | no | Program Language:<br><br>* `en-US` - US English<br>* `pt-BR` - Brazilian Portuguese<br><br>Default is `en-US`<br> | enum: ["pt-BR", "en-US"]; example: "en-US" |

##### Response 400

400 Example `missing-x-tenant` — from `#/components/examples/ErrorMissingXTenantResponse`:

```json
{
  "code": "EOA0017",
  "message": "Missing x-tenant header"
}
```

400 Example `error-to-binder` — from `#/components/examples/ErrorToBinderResponse`:

```json
{
  "code": "EOA0018",
  "message": "Error to Binder"
}
```

400 Example `field-required` — from `#/components/examples/FieldRequiredResponse`:

```json
{
  "code": "EOA0086",
  "message": "fieldName' field is required"
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

##### Response 404

404 Example `program-not-found` — from `#/components/examples/ProgramNotFoundResponse`:

```json
{
  "code": "EOA0020",
  "message": "Program x not found"
}
```

404 Example `program-type-not-found` — from `#/components/examples/ProgramTypeNotFoundResponse`:

```json
{
  "code": "EOA0031",
  "message": "Program type not found"
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

500 Example `template-not-found` — from `#/components/examples/TemplateFileNotFoundResponse`:

```json
{
  "code": "EOA0030",
  "message": "Template file not found"
}
```

500 Example `invalid-channel-name` — from `#/components/examples/InvalidChannelNameResponse`:

```json
{
  "code": "EOA0021",
  "message": "Invalid channel name: xxx"
}
```

500 Example `fail-create-channel` — from `#/components/examples/FailCreateChannelResponse`:

```json
{
  "code": "EOA0022",
  "message": "Failed to create program channel"
}
```

500 Example `fail-create-due-dates` — from `#/components/examples/FailCreateDueDatesResponse`:

```json
{
  "code": "EOA0034",
  "message": "Failed to create program due dates"
}
```

500 Example `fail-create-transaction-category` — from `#/components/examples/FailCreateTransactionCategoryResponse`:

```json
{
  "code": "EOA0035",
  "message": "Failed to create transaction category"
}
```

500 Example `transaction-category-not-found` — from `#/components/examples/TransactionCategoryNotFoundResponse`:

```json
{
  "code": "EOA0036",
  "message": "Failed to find a transaction category by description"
}
```

500 Example `fail-create-coporate-configuration` — from `#/components/examples/FailCreateCorporateConfigurationResponse`:

```json
{
  "code": "EOA0058",
  "message": "Failed to create corporate configuration"
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
| 400 | `EOA0018` | Error to Binder |
| 400 | `EOA0086` | fieldName' field is required |
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
| 404 | `EOA0020` | Program x not found |
| 404 | `EOA0031` | Program type not found |
| 404 | `EOA0064` | Brand not found |
| 500 | `EOA0030` | Template file not found |
| 500 | `EOA0021` | Invalid channel name: xxx |
| 500 | `EOA0022` | Failed to create program channel |
| 500 | `EOA0034` | Failed to create program due dates |
| 500 | `EOA0035` | Failed to create transaction category |
| 500 | `EOA0036` | Failed to find a transaction category by description |
| 500 | `EOA0058` | Failed to create corporate configuration |
| 500 | `EOA0009` | Connection failed with message: |
| 500 | `EOA0010` | Connection failed with message: |
| 500 | `EOA0008` | Error parsing utils body with message: |
| 500 | `EOA0011` | Error parsing utils body with message: |
| 500 | `EOA0015` | Something went wrong, please try again later |
| 500 | `EOA0016` | Something went wrong, please try again later |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `programs-creation-1` | https://developers.pismo.io/events/docs/programs-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;416;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-get-started-core-banking`, `KU-BANK-get-started-demand-deposit-accounts`, `KU-BANK-get-started-transaction-banking`, `KU-CARD-implementation-steps`, `KU-CC-programs`, `KU-CRED-calendar-management-strategies`, `KU-GS-get-started-with-pismo-apis`, `KU-GS-program-types`, `KU-GS-setup-overview`, `KU-LEND-get-started-lending`, `KU-SELL-get-started-seller-management`, `KU-SELL-seller-management-overview-and-onboarding`, `KU-SELL-seller-marketplace-implementation-steps`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=POST path=/programs/v2/programs/template operationId=CreateProgramBasedOnTemplateAsync -->
### `POST /programs/v2/programs/template` — Create program (async)

- **operationId:** `CreateProgramBasedOnTemplateAsync`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Programs`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Create a program asynchronously. 
>
> For more information about programs, refer to [Core objects](doc:setup-overview#program).
>
> This endpoint creates a program asynchronously; meaning, your app can continue executing during this. It could take 2 minutes or more for the platform to finish creating the program. Alternatively, you can use the [Create program](ref:createprogrambasedontemplate) endpoint, which executes synchronously and throws an error if the program cannot be created.
>
> This endpoint generates a [Program created](https://developers.pismo.io/events/docs/programs-creation-1) event. Given that creation is done asynchronously, it is recommended you do not try to access the program object via Pismo endpoints until this event is received.
>
> To get your Organization's programs, call the [List programs](ref:programs-1) endpoint, or view them in the [Pismo Control Center](doc:get-started-with-control-center).

#### Request body

Required: yes

> Create program from template request

**Content type `application/json`** — schema: object (schema `ProgramFromTemplate`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `ProgramName`) | yes | Program name | maxLength: 50; example: "Acme debit program" |
| `type` | string (schema `ProgramType`) | yes | Program type:<br /><br>  `CREDITO` — Full balance credit accounts<br /><br>  `PRE-PAGO` — Full balance prepaid accounts<br /><br>  `DEBITO` — Full balance debit accounts<br /><br>  `MERCHANT` — Merchant accounts<br /><br>  `CREDITO ZERO-BALANCE` — Zero balance credit accounts<br /><br>  `PRE-PAGO ZERO-BALANCE` — Zero balance prepaid accounts<br /><br>  `DEBITO ZERO-BALANCE` — Zero balance debit accounts<br /><br>  `CURRENT ACCOUNTS` — Current accounts<br /><br>  `INTERNAL ACCOUNTS` — Internal accounts<br /><br>  `CORRESPONDENT ACCOUNTS` — Correspondent accounts<br /><br>  `VOUCHER` - Prepaid voucher meal/food card<br /><br><br>For more information, refer to [Program types](https://developers.pismo.io/pismo-docs/docs/program-types)<br> | enum: ["CREDITO", "PRE-PAGO", "DEBITO", "MERCHANT", "CREDITO ZERO-BALANCE", "PRE-PAGO ZERO-BALANCE", "DEBITO ZERO-BALANCE", "CURRENT ACCOUNTS", "INTERNAL ACCOUNTS", "CORRESPONDENT ACCOUNTS", "VOUCHER"]; example: "CREDITO" |
| `timezone` | string (schema `TimeZone`) | yes | Program timezone. This is the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank"> IANA (Internet Assigned Numbers Authority) time zone database</a> "Region/City" format.<br> | example: "America/Anchorage" |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | yes | Program ISO 4217 currency code. | example: "986" |
| `country_code` | string (schema `CountryCode`) | yes | <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3" target="_blank">ISO 3166 Alpha-3</a> program country code. For example, `BRA` = Brazil. | example: "BRA" |
| `bin` | object (schema `Bin`) | no | Bank Identification Number (BIN) object. **REQUIRED** for card-issuing programs. <br> |  |
| `brand` | string (schema `Brand`) | no | Program's card brand.  **REQUIRED** for card-issuing programs.<br> | enum: ["VISA", "MASTERCARD", "ELO", "RUPAY", "PRIVATE", "CABAL", "GOODCARD"]; example: "VISA" |
| `due_dates` | array of object (schema `ProgramDueDate`) (schema `DueDates`) | no | Array of available program due dates. Every program account specifies a due date to use.<br><br>A due date is **REQUIRED** for Full balance credit programs.<br><br>For each due date, `day` and `active` are **REQUIRED**, as in the following example:<br>```<br>{<br>    "due_dates": [<br>          {<br>            "day": 1,<br>            "active": true<br>          },<br>          {<br>            "day": 2,<br>            "active": false<br>          }<br>    ]<br>}<br>```<br>**Note:** The due date ID is passed as a **numeric value**. For example, for due date `1` (first day of the month) the ID could be something like `3063`. This is the value you should use. `day` must be between 1 and 28.<br> |  |
| `language` | string (schema `ProgramLanguage`) | no | Program Language:<br><br>* `en-US` - US English<br>* `pt-BR` - Brazilian Portuguese<br><br>Default is `en-US`<br> | enum: ["pt-BR", "en-US"]; example: "en-US" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | OK | `application/json`: object (schema `ProgramTemplateV2Response`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not Found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal Server Error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_import_id` | integer | no | Program import ID | example: 1 |
| `message` | string | no | Process started message | example: "Your request has been submitted successfully. It may take some time to finish. You can track the progress on the programs dashboard." |

##### Response 400

400 Example `missing-x-tenant` — from `#/components/examples/ErrorMissingXTenantResponse`:

```json
{
  "code": "EOA0017",
  "message": "Missing x-tenant header"
}
```

400 Example `error-to-binder` — from `#/components/examples/ErrorToBinderResponse`:

```json
{
  "code": "EOA0018",
  "message": "Error to Binder"
}
```

400 Example `field-required` — from `#/components/examples/FieldRequiredResponse`:

```json
{
  "code": "EOA0086",
  "message": "fieldName' field is required"
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

##### Response 404

404 Example `program-type-not-found` — from `#/components/examples/ProgramTypeNotFoundResponse`:

```json
{
  "code": "EOA0031",
  "message": "Program type not found"
}
```

##### Response 500

500 Example `template-not-found` — from `#/components/examples/TemplateFileNotFoundResponse`:

```json
{
  "code": "EOA0030",
  "message": "Template file not found"
}
```

500 Example `connection-fail` — from `#/components/examples/ConnectionFailResponse`:

```json
{
  "code": "EOA0009",
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
| 400 | `EOA0018` | Error to Binder |
| 400 | `EOA0086` | fieldName' field is required |
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
| 404 | `EOA0031` | Program type not found |
| 500 | `EOA0030` | Template file not found |
| 500 | `EOA0009` | Connection failed with message: |
| 500 | `EOA0008` | Error parsing utils body with message: |
| 500 | `EOA0015` | Something went wrong, please try again later |
| 500 | `EOA0016` | Something went wrong, please try again later |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `programs-creation-1` | https://developers.pismo.io/events/docs/programs-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CC-programs`, `KU-CRED-calendar-management-strategies`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=POST path=/programs/v1/programs/copy operationId=CopyProgram -->
### `POST /programs/v1/programs/copy` — Copy program

- **operationId:** `CopyProgram`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Programs`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Copy an existing program to create a new one synchronously. 
>
> For more information about programs, refer to [Core objects](doc:setup-overview#program).
>
> For information on what properties are copied, refer to [Cloned and exported program properties](doc:cc-cloned-and-exported-data).
>
> This endpoint executes synchronously; meaning, a network timeout or similar delay could occur. In this case, an error is generated. To avoid this possibility, call the [Copy program (async)](ref:copyprogramasync) endpoint instead. 
>
> This endpoint generates a [Program created](https://developers.pismo.io/events/docs/programs-creation-1) event.
>
>  To get your Organization's programs, call the [List programs](ref:programs-1) endpoint, or view them in the [Pismo Control Center](doc:get-started-with-control-center).

#### Request body

Required: yes

> Copy program request

**Content type `application/json`** — schema: object (schema `CopyProgram`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `base_program_id` | integer (schema `BaseProgramID`) | yes | ID of program that was used to create this program. | format: "int64"; example: 2 |
| `name` | string (schema `ProgramName`) | yes | Program name | maxLength: 50; example: "Acme debit program" |
| `timezone` | string (schema `TimeZone`) | yes | Program timezone. This is the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank"> IANA (Internet Assigned Numbers Authority) time zone database</a> "Region/City" format.<br> | example: "America/Anchorage" |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | yes | Program ISO 4217 currency code. | example: "986" |
| `country_code` | string (schema `CountryCode`) | yes | <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3" target="_blank">ISO 3166 Alpha-3</a> program country code. For example, `BRA` = Brazil. | example: "BRA" |
| `due_dates` | array of object (schema `ProgramDueDate`) (schema `DueDates`) | no | Array of available program due dates. Every program account specifies a due date to use.<br><br>A due date is **REQUIRED** for Full balance credit programs.<br><br>For each due date, `day` and `active` are **REQUIRED**, as in the following example:<br>```<br>{<br>    "due_dates": [<br>          {<br>            "day": 1,<br>            "active": true<br>          },<br>          {<br>            "day": 2,<br>            "active": false<br>          }<br>    ]<br>}<br>```<br>**Note:** The due date ID is passed as a **numeric value**. For example, for due date `1` (first day of the month) the ID could be something like `3063`. This is the value you should use. `day` must be between 1 and 28.<br> |  |
| `brand` | string (schema `Brand`) | no | Program's card brand.  **REQUIRED** for card-issuing programs.<br> | enum: ["VISA", "MASTERCARD", "ELO", "RUPAY", "PRIVATE", "CABAL", "GOODCARD"]; example: "VISA" |
| `bin` | object (schema `Bin`) | no | Bank Identification Number (BIN) object. **REQUIRED** for card-issuing programs. <br> |  |
| `language` | string (schema `ProgramLanguage`) | no | Program Language:<br><br>* `en-US` - US English<br>* `pt-BR` - Brazilian Portuguese<br><br>Default is `en-US`<br> | enum: ["pt-BR", "en-US"]; example: "en-US" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `Program`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not Found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal Server Error | `application/json`: object (schema `handler.HTTPError`) |

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

##### Response 400

400 Example `missing-x-tenant` — from `#/components/examples/ErrorMissingXTenantResponse`:

```json
{
  "code": "EOA0017",
  "message": "Missing x-tenant header"
}
```

400 Example `error-to-binder` — from `#/components/examples/ErrorToBinderResponse`:

```json
{
  "code": "EOA0018",
  "message": "Error to Binder"
}
```

400 Example `field-required` — from `#/components/examples/FieldRequiredResponse`:

```json
{
  "code": "EOA0086",
  "message": "fieldName' field is required"
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

500 Example `invalid-channel-name` — from `#/components/examples/InvalidChannelNameResponse`:

```json
{
  "code": "EOA0021",
  "message": "Invalid channel name: xxx"
}
```

500 Example `fail-create-channel` — from `#/components/examples/FailCreateChannelResponse`:

```json
{
  "code": "EOA0022",
  "message": "Failed to create program channel"
}
```

500 Example `fail-create-due-dates` — from `#/components/examples/FailCreateDueDatesResponse`:

```json
{
  "code": "EOA0034",
  "message": "Failed to create program due dates"
}
```

500 Example `fail-create-transaction-category` — from `#/components/examples/FailCreateTransactionCategoryResponse`:

```json
{
  "code": "EOA0035",
  "message": "Failed to create transaction category"
}
```

500 Example `transaction-category-not-found` — from `#/components/examples/TransactionCategoryNotFoundResponse`:

```json
{
  "code": "EOA0036",
  "message": "Failed to find a transaction category by description"
}
```

500 Example `fail-create-coporate-configuration` — from `#/components/examples/FailCreateCorporateConfigurationResponse`:

```json
{
  "code": "EOA0058",
  "message": "Failed to create corporate configuration"
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
| 400 | `EOA0018` | Error to Binder |
| 400 | `EOA0086` | fieldName' field is required |
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
| 404 | `EOA0020` | Program x not found |
| 404 | `EOA0064` | Brand not found |
| 500 | `EOA0021` | Invalid channel name: xxx |
| 500 | `EOA0022` | Failed to create program channel |
| 500 | `EOA0034` | Failed to create program due dates |
| 500 | `EOA0035` | Failed to create transaction category |
| 500 | `EOA0036` | Failed to find a transaction category by description |
| 500 | `EOA0058` | Failed to create corporate configuration |
| 500 | `EOA0009` | Connection failed with message: |
| 500 | `EOA0010` | Connection failed with message: |
| 500 | `EOA0008` | Error parsing utils body with message: |
| 500 | `EOA0011` | Error parsing utils body with message: |
| 500 | `EOA0015` | Something went wrong, please try again later |
| 500 | `EOA0016` | Something went wrong, please try again later |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `programs-creation-1` | https://developers.pismo.io/events/docs/programs-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-implementation-steps`, `KU-CC-programs`, `KU-LEND-get-started-lending`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=POST path=/programs/v2/programs/copy operationId=CopyProgramAsync -->
### `POST /programs/v2/programs/copy` — Copy program (async)

- **operationId:** `CopyProgramAsync`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Programs`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Copy an existing program to create a new one. 
>
> Refer to [Core objects](doc:setup-overview) for more information about programs.
>
> For information on what properties are copied, refer to [Cloned and exported program properties](doc:cc-cloned-and-exported-data).
>
> This endpoint operates asynchronously; meaning, your program can continue executing while the program is being copied. It can take 2 minutes or more to copy the program. 
>
> Alternatively, you can call [Copy program](ref:copyprogram), which executes synchronously and returns a response indicating failure or success.
>
> This endpoint generates a [Program created](https://developers.pismo.io/events/docs/programs-creation-1) event. Given that creation is done asynchronously, it is recommended you do not try to access the program object via Pismo endpoints until this event is received.
>
> To get your Organization's programs, call the [List programs](ref:programs-1) endpoint, or view them in the [Pismo Control Center](doc:get-started-with-control-center).

#### Request body

Required: yes

> Program copy body request

**Content type `application/json`** — schema: object (schema `CopyProgram`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `base_program_id` | integer (schema `BaseProgramID`) | yes | ID of program that was used to create this program. | format: "int64"; example: 2 |
| `name` | string (schema `ProgramName`) | yes | Program name | maxLength: 50; example: "Acme debit program" |
| `timezone` | string (schema `TimeZone`) | yes | Program timezone. This is the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank"> IANA (Internet Assigned Numbers Authority) time zone database</a> "Region/City" format.<br> | example: "America/Anchorage" |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | yes | Program ISO 4217 currency code. | example: "986" |
| `country_code` | string (schema `CountryCode`) | yes | <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3" target="_blank">ISO 3166 Alpha-3</a> program country code. For example, `BRA` = Brazil. | example: "BRA" |
| `due_dates` | array of object (schema `ProgramDueDate`) (schema `DueDates`) | no | Array of available program due dates. Every program account specifies a due date to use.<br><br>A due date is **REQUIRED** for Full balance credit programs.<br><br>For each due date, `day` and `active` are **REQUIRED**, as in the following example:<br>```<br>{<br>    "due_dates": [<br>          {<br>            "day": 1,<br>            "active": true<br>          },<br>          {<br>            "day": 2,<br>            "active": false<br>          }<br>    ]<br>}<br>```<br>**Note:** The due date ID is passed as a **numeric value**. For example, for due date `1` (first day of the month) the ID could be something like `3063`. This is the value you should use. `day` must be between 1 and 28.<br> |  |
| `brand` | string (schema `Brand`) | no | Program's card brand.  **REQUIRED** for card-issuing programs.<br> | enum: ["VISA", "MASTERCARD", "ELO", "RUPAY", "PRIVATE", "CABAL", "GOODCARD"]; example: "VISA" |
| `bin` | object (schema `Bin`) | no | Bank Identification Number (BIN) object. **REQUIRED** for card-issuing programs. <br> |  |
| `language` | string (schema `ProgramLanguage`) | no | Program Language:<br><br>* `en-US` - US English<br>* `pt-BR` - Brazilian Portuguese<br><br>Default is `en-US`<br> | enum: ["pt-BR", "en-US"]; example: "en-US" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | OK | `application/json`: object (schema `ProgramCopyV2Response`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not Found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal Server Error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_export_id` | integer | no | Through `program_export_id`, it is possible to check the creation stage | example: 1504 |
| `message` | string | no | Process started message | example: "Your request has been submitted successfully. It may take some time to finish. You can track the progress on the programs dashboard." |

##### Response 400

400 Example `missing-x-tenant` — from `#/components/examples/ErrorMissingXTenantResponse`:

```json
{
  "code": "EOA0017",
  "message": "Missing x-tenant header"
}
```

400 Example `error-to-binder` — from `#/components/examples/ErrorToBinderResponse`:

```json
{
  "code": "EOA0018",
  "message": "Error to Binder"
}
```

400 Example `field-required` — from `#/components/examples/FieldRequiredResponse`:

```json
{
  "code": "EOA0086",
  "message": "fieldName' field is required"
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

400 Example `program-not-operation` — from `#/components/examples/ProgramNotOperationalResponse`:

```json
{
  "code": "EOA0085",
  "message": "Program xxx isn't operational"
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

500 Example `connection-fail` — from `#/components/examples/ConnectionFailResponse`:

```json
{
  "code": "EOA0009",
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
| 400 | `EOA0018` | Error to Binder |
| 400 | `EOA0086` | fieldName' field is required |
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
| 400 | `EOA0085` | Program xxx isn't operational |
| 404 | `EOA0020` | Program x not found |
| 404 | `EOA0064` | Brand not found |
| 500 | `EOA0009` | Connection failed with message: |
| 500 | `EOA0008` | Error parsing utils body with message: |
| 500 | `EOA0015` | Something went wrong, please try again later |
| 500 | `EOA0016` | Something went wrong, please try again later |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `programs-creation-1` | https://developers.pismo.io/events/docs/programs-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CC-programs`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Bin -->
### Schema `Bin`

Pointer: `#/components/schemas/Bin`. Type: object (schema `Bin`).

> Bank Identification Number (BIN) object. **REQUIRED** for card-issuing programs. 

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `start_range` | string | no | BIN range start.  **REQUIRED** for card-issuing programs. | example: "0" |
| `end_range` | string | no | BIN range end.  **REQUIRED** for card-issuing programs. | example: "999999999" |
| `value` | string | no | Card network-issued Bank Identification Number (BIN). <br>6 or 8-digit BIN identifying the card network, issuer, and product.<br> **REQUIRED** for card-issuing programs.<br> | example: "999999" |

<!-- schema: #/components/schemas/ProgramDueDate -->
### Schema `ProgramDueDate`

Pointer: `#/components/schemas/ProgramDueDate`. Type: object (schema `ProgramDueDate`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `active` | boolean (schema `DueDateActiveBoolean`) | yes | Is due date active? | example: true |
| `day` | integer (schema `DueDateDay`) | yes | Day of the month (1 to 28) for the statement due date. | format: "int32"; example: 10 |
| `id` | integer | no | Program due date ID | format: "int64"; example: 12345 |

<!-- schema: #/components/schemas/Channel -->
### Schema `Channel`

Pointer: `#/components/schemas/Channel`. Type: object (schema `Channel`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Acquisition channel ID. ID of How the customer was referrred, such as from a web page or mobile app. Acquisition channels are configured at the program level.<br> | format: "int64" |
| `name` | string | no | Customer-supplied acquistion channel name |  |
| `type` | string | no | Customer-supplied Acquisition channel type.<br> |  |

<!-- schema: #/components/schemas/Provider -->
### Schema `Provider`

Pointer: `#/components/schemas/Provider`. Type: object (schema `Provider`).

> [Legacy - restricted]

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Provider ID (outdated) | format: "int64"; example: 12 |
| `name` | string | no | Provider name (outdated) | example: "Acme Services" |

<!-- schema: #/components/schemas/handler.HTTPError -->
### Schema `handler.HTTPError`

Pointer: `#/components/schemas/handler.HTTPError`. Type: object (schema `handler.HTTPError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Bad request code | example: "EOA0017" |
| `message` | string | no | Bad request response | example: "Bad Request" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Programs.yaml` | tag `Programs`: POST /programs/v1/programs/template, POST /programs/v2/programs/template, POST /programs/v1/programs/copy, POST /programs/v2/programs/copy | https://github.com/PismoDevEx/pismo-api-specs | `aec6c882f89e07d6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-get-started-core-banking` — Get started with core banking
- `KU-BANK-get-started-demand-deposit-accounts` — Get started with demand deposit accounts (DDAs)
- `KU-BANK-get-started-transaction-banking` — Get started with transaction banking
- `KU-CARD-implementation-steps` — Card issuing implementation steps 1 to 7
- `KU-CC-programs` — Control Center programs: create, edit, clone, export and import
- `KU-CRED-calendar-management-strategies` — Calendar management strategies (cycle closing and due dates)
- `KU-ERR-codes-eoa` — Error codes: EOA
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
- `KU-GS-program-types` — Program types
- `KU-GS-setup-overview` — Core objects
- `KU-LEND-get-started-lending` — Get started with lending
- `KU-SELL-get-started-seller-management` — Get started with seller management
- `KU-SELL-seller-management-overview-and-onboarding` — Seller management overview and onboarding
- `KU-SELL-seller-marketplace-implementation-steps` — Seller marketplace implementation steps 1 to 6
