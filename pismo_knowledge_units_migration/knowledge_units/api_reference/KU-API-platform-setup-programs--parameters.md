---
ku_id: KU-API-platform-setup-programs--parameters
title: 'API reference: Platform setup - Programs — Parameters'
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
operations:
- programParameter
- createProgramParameter
- setProgramsParameters
- setProgramParameters
- updateProgramParameter
- programParameterV2
related_kus:
- KU-CARD-rule-list-part-03
- KU-CC-programs
- KU-CORE-program-parameters-reference-table
- KU-CRED-calculating-interest-accruals
- KU-CRED-configuring-accrual-rates
- KU-CRED-minimum-amount-due-calculation
- KU-GS-program-types
specification_version: v1.0
---

# API reference: Platform setup - Programs — Parameters

**KU ID:** `KU-API-platform-setup-programs--parameters` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Parameters` in `api-specs/Platform_setup_-_Programs.yaml` (“Platform setup - Programs”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage program parameters

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /programs/v1/programs/{program_id}/parameters` | `programParameter` | List program parameters | no |
| `POST /programs/v1/programs/{program_id}/parameters` | `createProgramParameter` | Link optional parameter to program | no |
| `POST /programs/v1/programs/parameters/batch` | `setProgramsParameters` | Update program(s) parameters | no |
| `POST /programs/v1/programs/{id}/parameters/batch` | `setProgramParameters` | Update program parameters | no |
| `PUT /programs/v1/programs/{program_id}/parameters/{program_parameter_id}` | `updateProgramParameter` | Update program parameter | no |
| `GET /programs/v2/programs/{program_id}/parameters` | `programParameterV2` | List program parameters with localization | no |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must be previoulsy authenticated.

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v1/programs/{program_id}/parameters operationId=programParameter -->
### `GET /programs/v1/programs/{program_id}/parameters` — List program parameters

- **operationId:** `programParameter`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Parameters`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Retrieves a paginated list of program parameters.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `program_id` | path | yes | integer | Program ID | format: "int64"; example: 12345 |
| `page` | query | no | integer | Current page number. Must be greater than `0`. Default = `1`. | format: "int32"; example: 2 |
| `perPage` | query | no | integer | Maximum number of items per page. Must be greater than `0`. Default = `10`. | format: "int32"; example: 20 |
| `order` | query | no | string | Sort order. Default = `ASC`. | enum: ["ASC", "DESC"]; example: "DESC" |
| `status` | query | no | string | Program status filter. Can be `ACTIVE` and/or `INACTIVE`. Use ',' as separator. | example: "ACTIVE" |
| `names` | query | no | string | One or more program names. Use `,` as separator. | example: "Pismolabs, Acme Testing" |
| `category` | query | no | string | One or more program parameter categories. Use `,` as separator. <br /><br>`CREDITO` - Credit<br /><br>`TAXA` - Tax<br /><br>`TARIFA` -  Fee<br /><br>`PARAMETRO` - Parameter<br /><br>`ARQUIVOS` - Archives<br /><br>`COBRANCA` - Collection<br /><br>`FISCAL` - Fiscal<br /><br>`FATURAMENTO` - Billing<br /><br>`CARTAO` - Card<br /><br>`FRAUDE` - Fraud<br /><br>`TIPO DE TRANSACAO` -  Type of transaction<br /><br> | example: "CREDITO" |
| `validUntil` | query | no | string | Return results less than or equal to the parameter expiration date. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-07-06T13:11:05Z" |
| `validFrom` | query | no | string | Return results greater than or equal to the parameter's expiration date. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-07-06T13:11:05Z" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramParameterPage`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `items` | array of object (schema `ProgramParameter`) (schema `ProgramParameters`) | no |  |  |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum items per page | format: "int32"; example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int32"; example: 3 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-program-parameters-reference-table`, `KU-GS-program-types`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=POST path=/programs/v1/programs/{program_id}/parameters operationId=createProgramParameter -->
### `POST /programs/v1/programs/{program_id}/parameters` — Link optional parameter to program

- **operationId:** `createProgramParameter`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Parameters`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

>
> Link an optional parameter to a program. Some program parameters are optional and not automatically linked to a program when it is created. 
>
> For more information, refer to [Edit program details and parameters](doc:cc-manage-program-details-and-parameters) or the [Program parameters](doc:program-parameters-reference-table) reference table.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `program_id` | path | yes | integer | Program ID | format: "int64"; example: 12345 |

#### Request body

Required: yes

> Link parameter to program request

**Content type `application/json`** — schema: object (schema `CreateProgramParameter`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `parameter_name` | string (schema `ProgramParameterName`) | yes | Program parameter name.<br><br>For more information, refer to the [program parameters](doc:program-parameters-reference-table) reference table.<br> | maxLength: 50; example: "CONTROL EXPIRATION CHANGES" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreateProgramParameterResponse`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ProgramParameterID`) | no | Program parameter ID. An ID, specific to the program itself, that identifies the program's setting for a specific program parameter.<br><br>For example, suppose you have a program parameter named `CONTROL EXPIRATION CHANGES`, and its `id` is `15`. One program might set the value for that parameter like this:<br>```json<br>{<br>  "account_parameter": false,<br>  "category": "PARAMETER",<br>  "description": "Turn the control on and off.",<br>  "id": 2,<br>  "parameter_id": 15,<br>  "name": "CONTROL EXPIRATION CHANGES",<br>  "type": "DECIMAL",<br>  "valid_from": "2020-01-01T00:00:00.000Z",<br>  "valid_until": "2020-12-31T23:59:59.999Z",<br>  "value": 0<br>}<br>```<br><br>Another program might set the value for same program parameter like this:<br>```json<br>{<br>  "account_parameter": false,<br>  "category": "PARAMETER",<br>  "description": "Turn the control on and off.",<br>  "id": 4,<br>  "parameter_id": 15,<br>  "name": "CONTROL EXPIRATION CHANGES",<br>  "type": "DECIMAL",<br>  "valid_from": "2020-02-04T00:00:00.000Z",<br>  "valid_until": "2020-11-25T22:36:55.999Z",<br>  "value": 1<br>}<br>```<br><br>In both cases, `parameter_id` is `15` because the programs are setting the same program parameter - the one with `id` = `15`. However, the `id` value is different for each program, because it is used to identify that program's specific parameter setting.<br> | format: "int64"; example: 1 |
| `parameter_name` | string (schema `ProgramParameterName`) | no | Program parameter name.<br><br>For more information, refer to the [program parameters](doc:program-parameters-reference-table) reference table.<br> | maxLength: 50; example: "CONTROL EXPIRATION CHANGES" |
| `value` | number (schema `FloatParameterValue`) | no | Parameter value | format: "float"; example: 1.5 |
| `valid_from` | string (schema `ValidFrom`) | no | Provided value start datetime. Format = yyyy-mm-ddThh:mm:ss. | format: "date-time"; example: "2020-01-01T00:00:00.000Z" |
| `status` | string (schema `ProgramParameterStatus`) | no | Program parameter status:<br> * `ACTIVE` - Parameter is operational <br> * `INACTIVE` Parameter cannot be used<br> | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CC-programs`, `KU-CORE-program-parameters-reference-table`, `KU-CRED-configuring-accrual-rates`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=POST path=/programs/v1/programs/parameters/batch operationId=setProgramsParameters -->
### `POST /programs/v1/programs/parameters/batch` — Update program(s) parameters

- **operationId:** `setProgramsParameters`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Parameters`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Update program parameter values for one or more programs. 
>
> For more information, refer to the [program parameters](doc:program-parameters-reference-table) reference table.

#### Request body

Required: yes

> Update parameter for one or more programs request

**Content type `application/json`** — schema: array of object (schema `SetProgramParameter`) (schema `SetProgramsParameters`)

_No fields declared in the schema._

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-program-parameters-reference-table`, `KU-CRED-minimum-amount-due-calculation`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=POST path=/programs/v1/programs/{id}/parameters/batch operationId=setProgramParameters -->
### `POST /programs/v1/programs/{id}/parameters/batch` — Update program parameters

- **operationId:** `setProgramParameters`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Parameters`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Update one or more parameters for a specific program. 
>
> For more information, refer to the [program parameters](doc:program-parameters-reference-table) reference table.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Program ID | format: "int64"; example: 12345 |

#### Request body

Required: yes

> Update one or more parameters for program request

**Content type `application/json`** — schema: array of object (schema `SetParameterBatch`) (schema `SetProgramParametersBatch`)

_No fields declared in the schema._

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=PUT path=/programs/v1/programs/{program_id}/parameters/{program_parameter_id} operationId=updateProgramParameter -->
### `PUT /programs/v1/programs/{program_id}/parameters/{program_parameter_id}` — Update program parameter

- **operationId:** `updateProgramParameter`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Parameters`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Update a program parameter value.
>
> For more information, refer to the [program parameters](doc:program-parameters-reference-table) reference table.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `program_id` | path | yes | integer | Program ID | format: "int64"; example: 12345 |
| `program_parameter_id` | path | yes | integer | Program parameter ID. Parameter IDs can change depending on the environment and, consequently, are not listed in the [program parameters reference table](doc:program-parameters-reference-table). Call [List program parameters](ref:programparameter) endpoint to get the IDs (`parameter_id` in the response) for your program parameters. <br> | format: "int64"; example: 23 |

#### Request body

Required: yes

> Update program parameter request

**Content type `application/json`** — schema: object (schema `PutProgramParameter`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `value` | number (schema `FloatParameterValue`) | yes | Parameter value | format: "float"; example: 1.5 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramParameter`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_parameter` | boolean (schema `AccountParameterBoolean`) | no | Can the parameter be customized at both the account and program levels? | example: false |
| `category` | string (schema `ProgramParameterCategory`) | no | Program parameter categories. When passing as a parameter, use `,` as separator. <br>`CREDITO` - Credit<br>`TAXA` -  Tax<br>`TARIFA` -  Fee<br>`PARAMETRO` -  Parameter<br>`ARQUIVOS` -  Archives<br>`COBRANCA` -  Collection<br>`FISCAL` -  Fiscal<br>`FATURAMENTO` -  Billing<br>`CARTAO` -  Card<br>`FRAUDE` -  Fraud<br>`TIPO DE TRANSACAO` -  Type of transaction<br> | example: "CREDITO" |
| `description` | string (schema `ProgramParameterDescription`) | no | Program parameter description | example: "Turn the control on and off." |
| `id` | integer (schema `ProgramParameterID`) | no | Program parameter ID. An ID, specific to the program itself, that identifies the program's setting for a specific program parameter.<br><br>For example, suppose you have a program parameter named `CONTROL EXPIRATION CHANGES`, and its `id` is `15`. One program might set the value for that parameter like this:<br>```json<br>{<br>  "account_parameter": false,<br>  "category": "PARAMETER",<br>  "description": "Turn the control on and off.",<br>  "id": 2,<br>  "parameter_id": 15,<br>  "name": "CONTROL EXPIRATION CHANGES",<br>  "type": "DECIMAL",<br>  "valid_from": "2020-01-01T00:00:00.000Z",<br>  "valid_until": "2020-12-31T23:59:59.999Z",<br>  "value": 0<br>}<br>```<br><br>Another program might set the value for same program parameter like this:<br>```json<br>{<br>  "account_parameter": false,<br>  "category": "PARAMETER",<br>  "description": "Turn the control on and off.",<br>  "id": 4,<br>  "parameter_id": 15,<br>  "name": "CONTROL EXPIRATION CHANGES",<br>  "type": "DECIMAL",<br>  "valid_from": "2020-02-04T00:00:00.000Z",<br>  "valid_until": "2020-11-25T22:36:55.999Z",<br>  "value": 1<br>}<br>```<br><br>In both cases, `parameter_id` is `15` because the programs are setting the same program parameter - the one with `id` = `15`. However, the `id` value is different for each program, because it is used to identify that program's specific parameter setting.<br> | format: "int64"; example: 1 |
| `parameter_id` | integer (schema `ParameterID`) | no | Parameter ID. Parameter IDs can change depending on the environment and, consequently, are not listed in the [program parameters reference table](doc:program-parameters-reference-table). Use the [List program parameters](ref:programparameter) endpoint to get the IDs (`parameter_id` in the response) for your program parameters.<br> | format: "int64"; example: 1 |
| `name` | string (schema `ProgramParameterName`) | no | Program parameter name.<br><br>For more information, refer to the [program parameters](doc:program-parameters-reference-table) reference table.<br> | maxLength: 50; example: "CONTROL EXPIRATION CHANGES" |
| `type` | string (schema `ProgramParameterValueType`) | no | Parameter value type | enum: ["INTEGER", "DECIMAL", "PERCENTAGE"]; example: "DECIMAL" |
| `valid_from` | string (schema `ValidFrom`) | no | Provided value start datetime. Format = yyyy-mm-ddThh:mm:ss. | format: "date-time"; example: "2020-01-01T00:00:00.000Z" |
| `valid_until` | string (schema `ValidUntil`) | no | Provided value expiration datetime. Format = yyyy-mm-ddThh:mm:ss. | format: "date-time"; example: "2020-12-31T23:59:59.999Z" |
| `value` | number (schema `FloatParameterValue`) | no | Parameter value | format: "float"; example: 1.5 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-rule-list-part-03`, `KU-CRED-calculating-interest-accruals`, `KU-CRED-configuring-accrual-rates`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v2/programs/{program_id}/parameters operationId=programParameterV2 -->
### `GET /programs/v2/programs/{program_id}/parameters` — List program parameters with localization

- **operationId:** `programParameterV2`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Parameters`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Get a paginated list of programs with localization parameters. 
>
> Returns a `translation` object with  language-specific parameter information. 
>
> For information about programs, refer to [Core objects](doc:setup-overview#program).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `program_id` | path | yes | integer | Program ID | format: "int64"; example: 12345 |
| `page` | query | no | integer | Current page number. Must be greater than `0`. Default = `1`. | format: "int32"; example: 2 |
| `perPage` | query | no | integer | Maximum number of items per page. Must be greater than `0`. Default = `10`. | format: "int32"; example: 20 |
| `order` | query | no | string | Sort order. Default = `ASC`. | enum: ["ASC", "DESC"]; example: "DESC" |
| `orderBy` | query | no | string | Field to sort on. Default = `ID`. | enum: ["ID", "NAME"]; example: "NAME" |
| `category` | query | no | string | One or more program parameter categories. Use `,` as separator. <br /><br>`CREDITO` - Credit<br /><br>`TAXA` - Tax<br /><br>`TARIFA` -  Fee<br /><br>`PARAMETRO` - Parameter<br /><br>`ARQUIVOS` - Archives<br /><br>`COBRANCA` - Collection<br /><br>`FISCAL` - Fiscal<br /><br>`FATURAMENTO` - Billing<br /><br>`CARTAO` - Card<br /><br>`FRAUDE` - Fraud<br /><br>`TIPO DE TRANSACAO` -  Type of transaction<br /><br> | example: "CREDITO" |
| `status` | query | no | string | Program status filter. Can be `ACTIVE` and/or `INACTIVE`. Use ',' as separator. | example: "ACTIVE" |
| `required` | query | no | string | Can be `REQUIRED` and/or `OPTIONAL`. Use `,` as separator. | example: "REQUIRED" |
| `names` | query | no | string | One or more program names. Use `,` as separator. | example: "Pismolabs, Acme Testing" |
| `validFrom` | query | no | string | Return results greater than or equal to the parameter's expiration date. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-07-06T13:11:05Z" |
| `validUntil` | query | no | string | Return results less than or equal to the parameter expiration date. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-07-06T13:11:05Z" |
| `search` | query | no | string | Filter for provided text in the localization object's `name` field. | example: "test" |
| `language` | query | no | string | Allows localization object content to be localized as specified.<br>* `en-US` - US English<br>* `pt-BR` - Brazilian Portuguese<br> | enum: ["en-US", "pt-BR"]; example: "en-US" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramParameterTranslatedPage`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `items` | array of object (schema `ProgramParameterTranslated`) | no |  |  |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum items per page | format: "int32"; example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int32"; example: 3 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ProgramParameter -->
### Schema `ProgramParameter`

Pointer: `#/components/schemas/ProgramParameter`. Type: object (schema `ProgramParameter`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_parameter` | boolean (schema `AccountParameterBoolean`) | no | Can the parameter be customized at both the account and program levels? | example: false |
| `category` | string (schema `ProgramParameterCategory`) | no | Program parameter categories. When passing as a parameter, use `,` as separator. <br>`CREDITO` - Credit<br>`TAXA` -  Tax<br>`TARIFA` -  Fee<br>`PARAMETRO` -  Parameter<br>`ARQUIVOS` -  Archives<br>`COBRANCA` -  Collection<br>`FISCAL` -  Fiscal<br>`FATURAMENTO` -  Billing<br>`CARTAO` -  Card<br>`FRAUDE` -  Fraud<br>`TIPO DE TRANSACAO` -  Type of transaction<br> | example: "CREDITO" |
| `description` | string (schema `ProgramParameterDescription`) | no | Program parameter description | example: "Turn the control on and off." |
| `id` | integer (schema `ProgramParameterID`) | no | Program parameter ID. An ID, specific to the program itself, that identifies the program's setting for a specific program parameter.<br><br>For example, suppose you have a program parameter named `CONTROL EXPIRATION CHANGES`, and its `id` is `15`. One program might set the value for that parameter like this:<br>```json<br>{<br>  "account_parameter": false,<br>  "category": "PARAMETER",<br>  "description": "Turn the control on and off.",<br>  "id": 2,<br>  "parameter_id": 15,<br>  "name": "CONTROL EXPIRATION CHANGES",<br>  "type": "DECIMAL",<br>  "valid_from": "2020-01-01T00:00:00.000Z",<br>  "valid_until": "2020-12-31T23:59:59.999Z",<br>  "value": 0<br>}<br>```<br><br>Another program might set the value for same program parameter like this:<br>```json<br>{<br>  "account_parameter": false,<br>  "category": "PARAMETER",<br>  "description": "Turn the control on and off.",<br>  "id": 4,<br>  "parameter_id": 15,<br>  "name": "CONTROL EXPIRATION CHANGES",<br>  "type": "DECIMAL",<br>  "valid_from": "2020-02-04T00:00:00.000Z",<br>  "valid_until": "2020-11-25T22:36:55.999Z",<br>  "value": 1<br>}<br>```<br><br>In both cases, `parameter_id` is `15` because the programs are setting the same program parameter - the one with `id` = `15`. However, the `id` value is different for each program, because it is used to identify that program's specific parameter setting.<br> | format: "int64"; example: 1 |
| `parameter_id` | integer (schema `ParameterID`) | no | Parameter ID. Parameter IDs can change depending on the environment and, consequently, are not listed in the [program parameters reference table](doc:program-parameters-reference-table). Use the [List program parameters](ref:programparameter) endpoint to get the IDs (`parameter_id` in the response) for your program parameters.<br> | format: "int64"; example: 1 |
| `name` | string (schema `ProgramParameterName`) | no | Program parameter name.<br><br>For more information, refer to the [program parameters](doc:program-parameters-reference-table) reference table.<br> | maxLength: 50; example: "CONTROL EXPIRATION CHANGES" |
| `type` | string (schema `ProgramParameterValueType`) | no | Parameter value type | enum: ["INTEGER", "DECIMAL", "PERCENTAGE"]; example: "DECIMAL" |
| `valid_from` | string (schema `ValidFrom`) | no | Provided value start datetime. Format = yyyy-mm-ddThh:mm:ss. | format: "date-time"; example: "2020-01-01T00:00:00.000Z" |
| `valid_until` | string (schema `ValidUntil`) | no | Provided value expiration datetime. Format = yyyy-mm-ddThh:mm:ss. | format: "date-time"; example: "2020-12-31T23:59:59.999Z" |
| `value` | number (schema `FloatParameterValue`) | no | Parameter value | format: "float"; example: 1.5 |

<!-- schema: #/components/schemas/handler.HTTPError -->
### Schema `handler.HTTPError`

Pointer: `#/components/schemas/handler.HTTPError`. Type: object (schema `handler.HTTPError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Bad request code | example: "EOA0017" |
| `message` | string | no | Bad request response | example: "Bad Request" |

<!-- schema: #/components/schemas/ProgramParameterTranslated -->
### Schema `ProgramParameterTranslated`

Pointer: `#/components/schemas/ProgramParameterTranslated`. Type: object (schema `ProgramParameterTranslated`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ProgramRelationshipID`) | no | Program relationship ID with parameter | format: "int64"; example: 1 |
| `parameter_id` | integer (schema `ParameterID`) | no | Parameter ID. Parameter IDs can change depending on the environment and, consequently, are not listed in the [program parameters reference table](doc:program-parameters-reference-table). Use the [List program parameters](ref:programparameter) endpoint to get the IDs (`parameter_id` in the response) for your program parameters.<br> | format: "int64"; example: 1 |
| `name` | string (schema `ProgramParameterName`) | no | Program parameter name.<br><br>For more information, refer to the [program parameters](doc:program-parameters-reference-table) reference table.<br> | maxLength: 50; example: "CONTROL EXPIRATION CHANGES" |
| `category` | string (schema `ProgramParameterCategory`) | no | Program parameter categories. When passing as a parameter, use `,` as separator. <br>`CREDITO` - Credit<br>`TAXA` -  Tax<br>`TARIFA` -  Fee<br>`PARAMETRO` -  Parameter<br>`ARQUIVOS` -  Archives<br>`COBRANCA` -  Collection<br>`FISCAL` -  Fiscal<br>`FATURAMENTO` -  Billing<br>`CARTAO` -  Card<br>`FRAUDE` -  Fraud<br>`TIPO DE TRANSACAO` -  Type of transaction<br> | example: "CREDITO" |
| `type` | string (schema `ProgramParameterValueType`) | no | Parameter value type | enum: ["INTEGER", "DECIMAL", "PERCENTAGE"]; example: "DECIMAL" |
| `value` | number (schema `FloatParameterValue`) | no | Parameter value | format: "float"; example: 1.5 |
| `valid_from` | string (schema `ValidFrom`) | no | Provided value start datetime. Format = yyyy-mm-ddThh:mm:ss. | format: "date-time"; example: "2020-01-01T00:00:00.000Z" |
| `valid_until` | string (schema `ValidUntil`) | no | Provided value expiration datetime. Format = yyyy-mm-ddThh:mm:ss. | format: "date-time"; example: "2020-12-31T23:59:59.999Z" |
| `account_parameter` | boolean (schema `AccountParameterBoolean`) | no | Can the parameter be customized at both the account and program levels? | example: false |
| `status` | string (schema `ProgramParameterStatus`) | no | Program parameter status:<br> * `ACTIVE` - Parameter is operational <br> * `INACTIVE` Parameter cannot be used<br> | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `required` | string (schema `RequiredOrOptional`) | no | Sets whether the parameter is required or optional. | enum: ["REQUIRED", "OPTIONAL"]; example: "REQUIRED" |
| `update_date` | string (schema `UpdateDate`) | no | Parameter last updated datetime. Format = yyyy-mm-ddThh:mm:ss. | format: "date-time"; example: "2020-12-31 23:59:59" |
| `legacy` | boolean (schema `LegacyBoolean`) | no | Is parameter from a legacy process and kept for compatibility only? | example: false |
| `translation` | object (schema `ProgramParameterTranslation`) | no |  |  |

<!-- schema: #/components/schemas/ProgramParameterTranslation -->
### Schema `ProgramParameterTranslation`

Pointer: `#/components/schemas/ProgramParameterTranslation`. Type: object (schema `ProgramParameterTranslation`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `TranslatedProgramParameterName`) | no | Localized program parameter name | example: "Interest projection reversal" |
| `description` | string (schema `ProgramParameterDescription`) | no | Program parameter description | example: "Turn the control on and off." |
| `details` | string (schema `TranslatedProgramParameterDetails`) | no | Localized program parameter details. | example: "Defines whether the projected interest..." |
| `language` | string (schema `TranslatedProgramParameterLanguage`) | no | Localized program parameter language | example: "en-us" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Programs.yaml` | tag `Parameters`: GET /programs/v1/programs/{program_id}/parameters, POST /programs/v1/programs/{program_id}/parameters, POST /programs/v1/programs/parameters/batch, POST /programs/v1/programs/{id}/parameters/batch, PUT /programs/v1/programs/{program_id}/parameters/{program_parameter_id}, GET /programs/v2/programs/{program_id}/parameters | https://github.com/PismoDevEx/pismo-api-specs | `aec6c882f89e07d6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-rule-list-part-03` — Rule list (part 3 of 4)
- `KU-CC-programs` — Control Center programs: create, edit, clone, export and import
- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-CRED-calculating-interest-accruals` — Calculating interest accruals
- `KU-CRED-configuring-accrual-rates` — Configuring accrual rates
- `KU-CRED-minimum-amount-due-calculation` — Minimum amount due calculation
- `KU-GS-program-types` — Program types
