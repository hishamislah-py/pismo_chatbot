---
ku_id: KU-API-platform-setup-programs--export-and-import
title: 'API reference: Platform setup - Programs — Export and import'
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
- getProgramExport
- postProgramExport
- postProgramExportBatch
- getProgramExportRecord
- getProgramExportDownload
- getProgramImport
- postProgramImport
- getProgramImportRecord
- getProgramImportRecordByID
- getProgramImportDownload
related_kus:
- KU-CARD-implementation-steps
- KU-ERR-codes-eoa
- KU-EVT-catalogue-other-domains
- KU-LEND-get-started-lending
specification_version: v1.0
---

# API reference: Platform setup - Programs — Export and import

**KU ID:** `KU-API-platform-setup-programs--export-and-import` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 10 operation(s) tagged `Export and import` in `api-specs/Platform_setup_-_Programs.yaml` (“Platform setup - Programs”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Export and import programs

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /programs/v1/programs/export` | `getProgramExport` | List exported programs | no |
| `POST /programs/v1/programs/export` | `postProgramExport` | Export program | no |
| `POST /programs/v1/programs/export/batch` | `postProgramExportBatch` | Export programs | no |
| `GET /programs/v1/programs/export/{id}` | `getProgramExportRecord` | Get program export record | no |
| `GET /programs/v1/programs/export/{id}/download` | `getProgramExportDownload` | Download exported program | no |
| `GET /programs/v1/programs/import` | `getProgramImport` | List imported programs | no |
| `POST /programs/v1/programs/import` | `postProgramImport` | Import program | no |
| `GET /programs/v1/programs/import/{id}` | `getProgramImportRecord` | Get program import record | no |
| `GET /programs/v1/programs/import/program/{id}` | `getProgramImportRecordByID` | Get program import record by program ID | no |
| `GET /programs/v1/programs/import/{id}/download` | `getProgramImportDownload` | Download imported program | no |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must be previoulsy authenticated.

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v1/programs/export operationId=getProgramExport -->
### `GET /programs/v1/programs/export` — List exported programs

- **operationId:** `getProgramExport`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Export and import`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Get your organization's exported programs in a paginated list. The organization ID is parsed from the token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | no | integer | Current page number. Must be greater than `0`. Default = `1`. | format: "int32"; example: 2 |
| `perPage` | query | no | integer | Maximum number of items per page. Must be greater than `0`. Default = `10`. | format: "int32"; example: 20 |
| `order` | query | no | string | Sort order. Default = `ASC`. | enum: ["ASC", "DESC"]; example: "DESC" |
| `orderBy` | query | no | string | Field to sort on. Default = `ID`. | enum: ["ID", "NAME"]; example: "NAME" |
| `text` | query | no | string | Filter items with provided text in the program name or the base program name. | maxLength: 50; example: "Pismo test" |
| `status` | query | no | string | Program status. Possible values are `PENDING`, `PROCESS`, `SUCCESS`, and/or `ERROR`. Use `,` as separator. | example: "PENDING" |
| `user` | query | no | string | User filter | maxLength: 255; example: "Test User" |
| `beginDate` | query | no | string | Return programs exported on or after this date. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-22T15:00:00Z" |
| `endDate` | query | no | string | Return programs exported on or before this date. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-22T15:00:00Z" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramExportPage`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `items` | array of object (schema `ProgramExport`) | no |  |  |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum items per page | format: "int32"; example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int32"; example: 3 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=POST path=/programs/v1/programs/export operationId=postProgramExport -->
### `POST /programs/v1/programs/export` — Export program

- **operationId:** `postProgramExport`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Export and import`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Export a program to a JSON file. 
>
> While this endpoint returns an immediate response, it also kicks off an asynchronous export process. You can check its progress with the [Get program export record](ref:getprogramexportrecord) endpoint. When done, the program status changes to `SUCCESS`. 
>
> To download the exported file, call [Download exported program](ref:getprogramexportdownload).

#### Request body

Required: yes

> Program export request

**Content type `application/json`** — schema: object (schema `ProgramExportRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_id` | integer (schema `ProgramID`) | yes | Program ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ProgramExport`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ProgramExportID`) | no | Program export ID | format: "int64"; example: 1 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `program_name` | string (schema `ProgramName`) | no | Program name | maxLength: 50; example: "Acme debit program" |
| `program_type_id` | integer (schema `ProgramTypeID`) | no | Program type ID:<br />  <br><br>  `1` =  `CREDITO`<br />  <br>  `2` =  `PRE-PAGO`<br />  <br>  `3` = `DEBITO`<br />  <br>  `5` = `MERCHANT`<br />  <br>  `7` = `CREDITO ZERO-BALANCE`<br />  <br>  `8` = `PRE-PAGO ZERO-BALANCE`<br />  <br>  `9` = `DEBITO ZERO-BALANCE`<br />  <br>  `11` =` CURRENT ACCOUNTS`<br />  <br>  `12` = `INTERNAL ACCOUNTS`<br />  <br>  `13` = `CORRESPONDENT ACCOUNTS`<br />  <br>  `15` = `VOUCHER`<br />  <br><br>For more information, refer to [Program types](doc:program-types).<br> | format: "int64"; example: 1 |
| `status` | string (schema `ProgramExporterStatus`) | no | Program exporter status | enum: ["PENDING", "PROCESS", "SUCCESS", "ERROR"]; example: "SUCCESS" |
| `details` | string (schema `ExporterDetails`) | no | Program exporter details | example: "Details of program export 484" |
| `file_url` | string (schema `ExportFileUrl`) | no | File URL for download export | example: "export/TN-00001/484/export.json" |
| `started_at` | string (schema `ExportCreatedAt`) | no | Program export creation datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2023-07-10 15:30:14" |
| `finished_at` | string (schema `ExportFinishedAt`) | no | Datetime when program export finished. Format = yyyy-mm-ddThh:mm:ss. | example: "2023-07-10 18:31:18" |
| `user` | string (schema `ExportUser`) | no | User who created the export's email address | example: "example@pismo.io" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-implementation-steps`, `KU-LEND-get-started-lending`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=POST path=/programs/v1/programs/export/batch operationId=postProgramExportBatch -->
### `POST /programs/v1/programs/export/batch` — Export programs

- **operationId:** `postProgramExportBatch`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Export and import`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Exports one or more programs to a ZIP file. 
>
> This endpoint starts an async export process. When that process is done, the program status, for each exported program, changes to `SUCCESS`. 
>
> To download the exported file, call the [Download exported program](ref:getprogramexportdownload) endpoint.

#### Request body

Required: yes

> Program export batch request

**Content type `application/json`** — schema: object (schema `ProgramExportBatchRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `export_ids` | array of integer (schema `ProgramExportID`) | yes |  | example: [1, 2]; items.format: "int64" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: array of object (schema `ProgramExport`) (schema `ProgramExportArray`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v1/programs/export/{id} operationId=getProgramExportRecord -->
### `GET /programs/v1/programs/export/{id}` — Get program export record

- **operationId:** `getProgramExportRecord`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Export and import`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Gets a program's detailed export record, including the export steps and their statuses.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Exported program ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramExportWithStepResponse`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not Found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal Server Error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ProgramExporterID`) | no | Program exporter ID | format: "int64"; example: 12 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `status` | string (schema `ProgramExporterStatus`) | no | Program exporter status | enum: ["PENDING", "PROCESS", "SUCCESS", "ERROR"]; example: "SUCCESS" |
| `file_url` | string (schema `ExportFileUrl`) | no | File URL for download export | example: "export/TN-00001/484/export.json" |
| `details` | string (schema `ExporterDetails`) | no | Program exporter details | example: "Details of program export 484" |
| `started_at` | string (schema `ExportCreatedAt`) | no | Program export creation datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2023-07-10 15:30:14" |
| `finished_at` | string (schema `ExportFinishedAt`) | no | Datetime when program export finished. Format = yyyy-mm-ddThh:mm:ss. | example: "2023-07-10 18:31:18" |
| `program_export_steps` | array of object (schema `ProgramExportSteps`) | no |  |  |

##### Response 400

400 Example `program-export-not-found` — from `#/components/examples/ProgramExportNotFoundResponse`:

```json
{
  "code": "EOA0072",
  "message": "Program export xxx not found"
}
```

400 Example `program-export-steps-not-found` — from `#/components/examples/ProgramExportStepsNotFoundResponse`:

```json
{
  "code": "EOA0090",
  "message": "Steps for program export xxx not found"
}
```

##### Response 500

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
| 400 | `EOA0072` | Program export xxx not found |
| 400 | `EOA0090` | Steps for program export xxx not found |
| 500 | `EOA0015` | Something went wrong, please try again later |
| 500 | `EOA0016` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v1/programs/export/{id}/download operationId=getProgramExportDownload -->
### `GET /programs/v1/programs/export/{id}/download` — Download exported program

- **operationId:** `getProgramExportDownload`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Export and import`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Download an exported program as a JSON file. 
>
> Use this endpoint after exporting the program (using either [Export program](ref:postprogramexport) or [Export programs](ref:postprogramexportbatch).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Exported program ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-implementation-steps`, `KU-LEND-get-started-lending`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v1/programs/import operationId=getProgramImport -->
### `GET /programs/v1/programs/import` — List imported programs

- **operationId:** `getProgramImport`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Export and import`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Get your organization's imported programs in a paginated list.
>
> The org ID is parsed from the access token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | no | integer | Current page number. Must be greater than `0`. Default = `1`. | format: "int32"; example: 2 |
| `perPage` | query | no | integer | Maximum number of items per page. Must be greater than `0`. Default = `10`. | format: "int32"; example: 20 |
| `order` | query | no | string | Sort order. Default = `ASC`. | enum: ["ASC", "DESC"]; example: "DESC" |
| `orderBy` | query | no | string | Field to sort on. Default = `ID`. | enum: ["ID", "NAME"]; example: "NAME" |
| `text` | query | no | string | Filter items with provided text in the program name or the base program name. | maxLength: 50; example: "Pismo test" |
| `status` | query | no | string | Program status. Possible values are `PENDING`, `PROCESS`, `SUCCESS`, and/or `ERROR`. Use `,` as separator. | example: "PENDING" |
| `user` | query | no | string | User filter | maxLength: 255; example: "Test User" |
| `beginDate` | query | no | string | Return programs exported on or after this date. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-22T15:00:00Z" |
| `endDate` | query | no | string | Return programs exported on or before this date. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-22T15:00:00Z" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramExportPage`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `items` | array of object (schema `ProgramExport`) | no |  |  |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum items per page | format: "int32"; example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int32"; example: 3 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=POST path=/programs/v1/programs/import operationId=postProgramImport -->
### `POST /programs/v1/programs/import` — Import program

- **operationId:** `postProgramImport`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Export and import`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Uploads a JSON file to import a program.
>
> This endpoint generates a [Program created](https://developers.pismo.io/events/docs/programs-creation-1) event.

#### Request body

Required: yes

> Program import request

**Content type `multipart/form-data`** — schema: object (schema `ProgramImportRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `ProgramName`) | yes | Program name | maxLength: 50; example: "Acme debit program" |
| `file` | string | yes | JSON file to import | format: "binary"; example: "file=@\\"/Users/pismo/Desktop/program-export-484.json" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ProgramExport`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ProgramExportID`) | no | Program export ID | format: "int64"; example: 1 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `program_name` | string (schema `ProgramName`) | no | Program name | maxLength: 50; example: "Acme debit program" |
| `program_type_id` | integer (schema `ProgramTypeID`) | no | Program type ID:<br />  <br><br>  `1` =  `CREDITO`<br />  <br>  `2` =  `PRE-PAGO`<br />  <br>  `3` = `DEBITO`<br />  <br>  `5` = `MERCHANT`<br />  <br>  `7` = `CREDITO ZERO-BALANCE`<br />  <br>  `8` = `PRE-PAGO ZERO-BALANCE`<br />  <br>  `9` = `DEBITO ZERO-BALANCE`<br />  <br>  `11` =` CURRENT ACCOUNTS`<br />  <br>  `12` = `INTERNAL ACCOUNTS`<br />  <br>  `13` = `CORRESPONDENT ACCOUNTS`<br />  <br>  `15` = `VOUCHER`<br />  <br><br>For more information, refer to [Program types](doc:program-types).<br> | format: "int64"; example: 1 |
| `status` | string (schema `ProgramExporterStatus`) | no | Program exporter status | enum: ["PENDING", "PROCESS", "SUCCESS", "ERROR"]; example: "SUCCESS" |
| `details` | string (schema `ExporterDetails`) | no | Program exporter details | example: "Details of program export 484" |
| `file_url` | string (schema `ExportFileUrl`) | no | File URL for download export | example: "export/TN-00001/484/export.json" |
| `started_at` | string (schema `ExportCreatedAt`) | no | Program export creation datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2023-07-10 15:30:14" |
| `finished_at` | string (schema `ExportFinishedAt`) | no | Datetime when program export finished. Format = yyyy-mm-ddThh:mm:ss. | example: "2023-07-10 18:31:18" |
| `user` | string (schema `ExportUser`) | no | User who created the export's email address | example: "example@pismo.io" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `programs-creation-1` | https://developers.pismo.io/events/docs/programs-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-implementation-steps`, `KU-LEND-get-started-lending`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v1/programs/import/{id} operationId=getProgramImportRecord -->
### `GET /programs/v1/programs/import/{id}` — Get program import record

- **operationId:** `getProgramImportRecord`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Export and import`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Get a detailed program import record, including the import steps and their statuses.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Program import ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramImportWithStepResponse`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not Found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal Server Error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ProgramImportID`) | no | Program import ID | format: "int64"; example: 1234 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `status` | string (schema `ProgramImporterStatus`) | no | Program import status | enum: ["PENDING", "PROCESS", "SUCCESS", "ERROR"]; example: "SUCCESS" |
| `file_url` | string (schema `ImportFileUrl`) | no | File URL for downloading the import. Contains part of the path and JSON file name. | example: "https://programs-api.s3.amazonaws.com/TENANT/import/file.json" |
| `details` | string (schema `ProgramImporterDetails`) | no | Program importer details | example: "Import process details" |
| `started_at` | string (schema `ImportStartedAt`) | no | Program import start datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-22T15:00:00Z" |
| `finished_at` | string (schema `ImportFinishedAt`) | no | When program import finished. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-22T15:45:00Z" |
| `program_import_steps` | array of object (schema `ProgramImportStep`) | no | Program import process steps |  |

##### Response 404

404 Example `program-import-not-found` — from `#/components/examples/ProgramImportNotFoundResponse`:

```json
{
  "code": "EOA0091",
  "message": "Program import xxx not found"
}
```

404 Example `program-import-steps-not-found` — from `#/components/examples/ProgramImportStepsNotFoundResponse`:

```json
{
  "code": "EOA0092",
  "message": "Steps for program import xxx not found"
}
```

##### Response 500

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
| 404 | `EOA0091` | Program import xxx not found |
| 404 | `EOA0092` | Steps for program import xxx not found |
| 500 | `EOA0015` | Something went wrong, please try again later |
| 500 | `EOA0016` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v1/programs/import/program/{id} operationId=getProgramImportRecordByID -->
### `GET /programs/v1/programs/import/program/{id}` — Get program import record by program ID

- **operationId:** `getProgramImportRecordByID`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Export and import`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Get a detailed programn import record, including the import steps and their statuses.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Program ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramImportWithStepResponse`) |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not Found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal Server Error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ProgramImportID`) | no | Program import ID | format: "int64"; example: 1234 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `status` | string (schema `ProgramImporterStatus`) | no | Program import status | enum: ["PENDING", "PROCESS", "SUCCESS", "ERROR"]; example: "SUCCESS" |
| `file_url` | string (schema `ImportFileUrl`) | no | File URL for downloading the import. Contains part of the path and JSON file name. | example: "https://programs-api.s3.amazonaws.com/TENANT/import/file.json" |
| `details` | string (schema `ProgramImporterDetails`) | no | Program importer details | example: "Import process details" |
| `started_at` | string (schema `ImportStartedAt`) | no | Program import start datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-22T15:00:00Z" |
| `finished_at` | string (schema `ImportFinishedAt`) | no | When program import finished. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-22T15:45:00Z" |
| `program_import_steps` | array of object (schema `ProgramImportStep`) | no | Program import process steps |  |

##### Response 404

404 Example `program-import-not-found` — from `#/components/examples/ProgramImportNotFoundResponse`:

```json
{
  "code": "EOA0091",
  "message": "Program import xxx not found"
}
```

404 Example `program-import-steps-not-found` — from `#/components/examples/ProgramImportStepsNotFoundResponse`:

```json
{
  "code": "EOA0092",
  "message": "Steps for program import xxx not found"
}
```

##### Response 500

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
| 404 | `EOA0091` | Program import xxx not found |
| 404 | `EOA0092` | Steps for program import xxx not found |
| 500 | `EOA0015` | Something went wrong, please try again later |
| 500 | `EOA0016` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Programs.yaml method=GET path=/programs/v1/programs/import/{id}/download operationId=getProgramImportDownload -->
### `GET /programs/v1/programs/import/{id}/download` — Download imported program

- **operationId:** `getProgramImportDownload`
- **Specification:** `api-specs/Platform_setup_-_Programs.yaml` (Platform setup - Programs)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Export and import`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Download a previously imported program in JSON format. 
>
> You can use this endpoint to review (audit) what program data was imported.
>
> If this call is via Postman, the JSON is returned in the response. In the Control Center, a browser dialog prompts you where to save the file.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Program import ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad Request | `application/json`: object (schema `handler.HTTPError`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ProgramExport -->
### Schema `ProgramExport`

Pointer: `#/components/schemas/ProgramExport`. Type: object (schema `ProgramExport`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ProgramExportID`) | no | Program export ID | format: "int64"; example: 1 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `program_name` | string (schema `ProgramName`) | no | Program name | maxLength: 50; example: "Acme debit program" |
| `program_type_id` | integer (schema `ProgramTypeID`) | no | Program type ID:<br />  <br><br>  `1` =  `CREDITO`<br />  <br>  `2` =  `PRE-PAGO`<br />  <br>  `3` = `DEBITO`<br />  <br>  `5` = `MERCHANT`<br />  <br>  `7` = `CREDITO ZERO-BALANCE`<br />  <br>  `8` = `PRE-PAGO ZERO-BALANCE`<br />  <br>  `9` = `DEBITO ZERO-BALANCE`<br />  <br>  `11` =` CURRENT ACCOUNTS`<br />  <br>  `12` = `INTERNAL ACCOUNTS`<br />  <br>  `13` = `CORRESPONDENT ACCOUNTS`<br />  <br>  `15` = `VOUCHER`<br />  <br><br>For more information, refer to [Program types](doc:program-types).<br> | format: "int64"; example: 1 |
| `status` | string (schema `ProgramExporterStatus`) | no | Program exporter status | enum: ["PENDING", "PROCESS", "SUCCESS", "ERROR"]; example: "SUCCESS" |
| `details` | string (schema `ExporterDetails`) | no | Program exporter details | example: "Details of program export 484" |
| `file_url` | string (schema `ExportFileUrl`) | no | File URL for download export | example: "export/TN-00001/484/export.json" |
| `started_at` | string (schema `ExportCreatedAt`) | no | Program export creation datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2023-07-10 15:30:14" |
| `finished_at` | string (schema `ExportFinishedAt`) | no | Datetime when program export finished. Format = yyyy-mm-ddThh:mm:ss. | example: "2023-07-10 18:31:18" |
| `user` | string (schema `ExportUser`) | no | User who created the export's email address | example: "example@pismo.io" |

<!-- schema: #/components/schemas/handler.HTTPError -->
### Schema `handler.HTTPError`

Pointer: `#/components/schemas/handler.HTTPError`. Type: object (schema `handler.HTTPError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Bad request code | example: "EOA0017" |
| `message` | string | no | Bad request response | example: "Bad Request" |

<!-- schema: #/components/schemas/ProgramExportSteps -->
### Schema `ProgramExportSteps`

Pointer: `#/components/schemas/ProgramExportSteps`. Type: object (schema `ProgramExportSteps`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ExportStepID`) | no | Program export step ID | format: "int32"; example: 45 |
| `name` | string (schema `ImportExportStepName`) | no | Program export step name<br><br>Steps per [program type](doc:program-types): <br><br>Key: FBC = Full balance (FB) credit, ZBC = Zero balance (ZB) credit, FBD = FB debit, ZBD = ZB debit, FBPP = FB pre-paid, ZBPP= ZB pre-paid, Corp = Corporate<br><br>\| Step \| FBC \| ZBC \| FBD \| ZBD \| FBPP \| ZBPP\| Corp \|<br>\| ------------------------------\|---\|---\|---\|---\|---\|---\|---\|<br>\| `PROGRAM` \| X \| X \| X \| X \| X \| X \| X \|<br>\| `DUEDATES` \| X \|  \|  \|  \|  \|  \|  \|<br>\| `CHANNELS` \| X \| X \| X \| X \| X \| X \|  \|<br>\| `PROGRAMS_PARAMETERS` \| X \| X \| X \| X \| X \| X \| X \|<br>\| `TRANSACTIONS_CATEGORIES` \| X \|  \|  \|  \|  \|  \|  \|<br>\| `PROGRAMS_TRANSACTION_TYPES` \| X \|  \|  \|  \|  \|  \|  \|<br>\| `ORGS_OPERATIONS` \| X \|  \| X \|  \| X \|  \| X \|<br>\| `NETWORK_ACCEPTANCES` \| X \| X \|  \|  \|  \|  \|  \|<br> | enum: ["PROGRAM", "DUEDATES", "CHANNELS", "PROGRAMS_PARAMETERS", "TRANSACTIONS_CATEGORIES", "PROGRAMS_TRANSACTION_TYPES", "ORGS_OPERATIONS", "NETWORK_ACCEPTANCES"]; maxLength: 50; example: "PROGRAM" |
| `status` | string (schema `ExportStepStatus`) | no | Program export step status | enum: ["PENDING", "PROCESS", "SUCCESS", "ERROR"]; example: "PENDING" |
| `order` | integer (schema `ExportStepOrder`) | no | Program export step order, with `1` as the highest. | format: "int32"; example: 1 |
| `details` | string (schema `ExportStepDetails`) | no | Export step details | example: "Export step details" |
| `started_at` | string (schema `StepStartedAt`) | no | Step start datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-23T10:05:00Z" |
| `finished_at` | string (schema `StepFinishedAt`) | no | Step completion datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-23T10:15:45Z" |
| `deleted_at` | string (schema `StepDeletedAt`) | no | Step deletion datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-23T10:10:25Z" |

<!-- schema: #/components/schemas/ProgramImportStep -->
### Schema `ProgramImportStep`

Pointer: `#/components/schemas/ProgramImportStep`. Type: object (schema `ProgramImportStep`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `ImportStepID`) | no | Program import step ID | format: "int64"; example: 12 |
| `name` | string (schema `ImportExportStepName`) | no | Program export step name<br><br>Steps per [program type](doc:program-types): <br><br>Key: FBC = Full balance (FB) credit, ZBC = Zero balance (ZB) credit, FBD = FB debit, ZBD = ZB debit, FBPP = FB pre-paid, ZBPP= ZB pre-paid, Corp = Corporate<br><br>\| Step \| FBC \| ZBC \| FBD \| ZBD \| FBPP \| ZBPP\| Corp \|<br>\| ------------------------------\|---\|---\|---\|---\|---\|---\|---\|<br>\| `PROGRAM` \| X \| X \| X \| X \| X \| X \| X \|<br>\| `DUEDATES` \| X \|  \|  \|  \|  \|  \|  \|<br>\| `CHANNELS` \| X \| X \| X \| X \| X \| X \|  \|<br>\| `PROGRAMS_PARAMETERS` \| X \| X \| X \| X \| X \| X \| X \|<br>\| `TRANSACTIONS_CATEGORIES` \| X \|  \|  \|  \|  \|  \|  \|<br>\| `PROGRAMS_TRANSACTION_TYPES` \| X \|  \|  \|  \|  \|  \|  \|<br>\| `ORGS_OPERATIONS` \| X \|  \| X \|  \| X \|  \| X \|<br>\| `NETWORK_ACCEPTANCES` \| X \| X \|  \|  \|  \|  \|  \|<br> | enum: ["PROGRAM", "DUEDATES", "CHANNELS", "PROGRAMS_PARAMETERS", "TRANSACTIONS_CATEGORIES", "PROGRAMS_TRANSACTION_TYPES", "ORGS_OPERATIONS", "NETWORK_ACCEPTANCES"]; maxLength: 50; example: "PROGRAM" |
| `order` | integer (schema `ImportStepOrder`) | no | Program import step order. For example, `1` = first step, `2`  = second, and so on. | format: "int32"; example: 1 |
| `status` | string (schema `ImportStepStatus`) | no | Program import step status | enum: ["PENDING", "PROCESS", "SUCCESS", "ERROR"]; example: "SUCCESS" |
| `details` | string (schema `ImportStepDetails`) | no | Program import step details | example: "Import step details" |
| `started_at` | string (schema `StepStartedAt`) | no | Step start datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-23T10:05:00Z" |
| `finished_at` | string (schema `StepFinishedAt`) | no | Step completion datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-23T10:15:45Z" |
| `deleted_at` | string (schema `StepDeletedAt`) | no | Step deletion datetime. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-09-23T10:10:25Z" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Programs.yaml` | tag `Export and import`: GET /programs/v1/programs/export, POST /programs/v1/programs/export, POST /programs/v1/programs/export/batch, GET /programs/v1/programs/export/{id}, GET /programs/v1/programs/export/{id}/download, GET /programs/v1/programs/import, POST /programs/v1/programs/import, GET /programs/v1/programs/import/{id}, GET /programs/v1/programs/import/program/{id}, GET /programs/v1/programs/import/{id}/download | https://github.com/PismoDevEx/pismo-api-specs | `aec6c882f89e07d6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-implementation-steps` — Card issuing implementation steps 1 to 7
- `KU-ERR-codes-eoa` — Error codes: EOA
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-LEND-get-started-lending` — Get started with lending
