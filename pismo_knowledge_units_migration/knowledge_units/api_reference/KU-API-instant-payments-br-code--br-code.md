---
ku_id: KU-API-instant-payments-br-code--br-code
title: 'API reference: Instant payments - BR Code — BR Code'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Instant_payments_BR_Code.yaml
  sha256: f37ab75e09b3af92e0d019b764b9e8d28811a6adb99fd6c287c38be04d9a4b68
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
- post-brcode-encode
- post-brcode-decode
related_kus: []
specification_version: '1.0'
---

# API reference: Instant payments - BR Code — BR Code

**KU ID:** `KU-API-instant-payments-br-code--br-code` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `BR Code` in `api-specs/Instant_payments_BR_Code.yaml` (“Instant payments - BR Code”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoint for encoding and decoding Brazilian BR Codes

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/emv/brcode/encode` | `post-brcode-encode` | Encode BR Code | no |
| `POST /v1/emv/brcode/decode` | `post-brcode-decode` | Decode BR Code | no |

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_BR_Code.yaml method=POST path=/v1/emv/brcode/encode operationId=post-brcode-encode -->
### `POST /v1/emv/brcode/encode` — Encode BR Code

- **operationId:** `post-brcode-encode`
- **Specification:** `api-specs/Instant_payments_BR_Code.yaml` (Instant payments - BR Code)
- **Server base URL(s):** `https://sandbox.pismolabs.io/qrcps`
- **Tags:** `BR Code`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Encode a Brazilian BR Code (short for "Brazilian Barcode") - a standard barcode format used in Brazil for electronic payments. It is part of the Brazilian Payment System (SPB) and is regulated by the Central Bank of Brazil. The BR Code contains information about the payee, transaction details, and other data.
>
> A BR Code is typically used with [Pix](doc:pix-instant-payments), a Brazilian instant payments system. For more information about BR Codes, see <a href="https://www.bcb.gov.br/content/config/Documents/BR_Code_MANUAL_Version_2_May_2020.pdf" target="_blank">BR Code Manual</a>

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | yes | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |
| `x-tenant` | header | no | string | Organization/tenant ID |  |

#### Request body

Required: no

> Encode Brcode request body

**Content type `application/json`** — schema: object (schema `brcode.barCode`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `country_code` | string | yes | Country code - ISO 3166-1 alpha 2. For example: "BR" = Brazil<br> | maxLength: 2; example: "BR" |
| `merchant_account_information` | array of object (schema `brcode.GenericSubBlock`) | yes | Merchant account information |  |
| `merchant_category_code` | string | yes | ISO 18245 merchant category code. | maxLength: 4; example: "5446" |
| `merchant_city` | string | yes | Merchant's city | maxLength: 15; example: "Brasilia" |
| `merchant_name` | string | yes | Merchant name | maxLength: 25; example: "Acme Widgets" |
| `additional_data_field_template` | object (schema `brcode.AdditionalDataFieldTemplate`) | yes |  |  |
| `payload_format_indicator` | string | yes | For Brazilian BR Codes associated with Pix transactions, this is fixed at "01". This value indicates that the data following conforms to the Brazilan Payment System's specifications for Pix transactions.<br> | maxLength: 2; example: "01" |
| `transaction_currency` | integer | yes | ISO 4217 transaction currency. For example: 986 = Brazilin Real<br> | maximum: 999; example: 986 |
| `point_initiation_method` | string | no | Point initiation method. A value = "12" means that the BR Code can only be used once.<br> | maxLength: 2; example: "12" |
| `postal_code` | string | no | Código de Endereçamento Postal (CEP - Postal Addressing Code). 8 digits separated by a hyphen. | example: "86753-090" |
| `transaction_amount` | number | no | Transaction amount | maximum: 9999999999999; example: 86753.09 |
| `unreserved_templates` | array of object (schema `brcode.GenericSubBlock`) | no | Unreserved template |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `brcode.Marshaled`) |
| 400 | Success | `application/json`: object (schema `httpserver.Error`) |
| 500 | Success | `application/json`: object (schema `httpserver.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `brcode` | string | no | Encoded BR Code in EMV (Europay Mastercard and Visa) format. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_BR_Code.yaml method=POST path=/v1/emv/brcode/decode operationId=post-brcode-decode -->
### `POST /v1/emv/brcode/decode` — Decode BR Code

- **operationId:** `post-brcode-decode`
- **Specification:** `api-specs/Instant_payments_BR_Code.yaml` (Instant payments - BR Code)
- **Server base URL(s):** `https://sandbox.pismolabs.io/qrcps`
- **Tags:** `BR Code`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Decode a Brazilian BR Code.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | yes | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |
| `x-tenant` | header | no | string | Organization/tenant ID |  |

#### Request body

Required: no

> Decode Brcode request body

**Content type `application/json`** — schema: object (schema `brcode.Marshaled`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `brcode` | string | no | Encoded BR Code in EMV (Europay Mastercard and Visa) format. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `brcode.barCode`) |
| 400 | Success | `application/json`: object (schema `httpserver.Error`) |
| 500 | Success | `application/json`: object (schema `httpserver.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `country_code` | string | yes | Country code - ISO 3166-1 alpha 2. For example: "BR" = Brazil<br> | maxLength: 2; example: "BR" |
| `merchant_account_information` | array of object (schema `brcode.GenericSubBlock`) | yes | Merchant account information |  |
| `merchant_category_code` | string | yes | ISO 18245 merchant category code. | maxLength: 4; example: "5446" |
| `merchant_city` | string | yes | Merchant's city | maxLength: 15; example: "Brasilia" |
| `merchant_name` | string | yes | Merchant name | maxLength: 25; example: "Acme Widgets" |
| `additional_data_field_template` | object (schema `brcode.AdditionalDataFieldTemplate`) | yes |  |  |
| `payload_format_indicator` | string | yes | For Brazilian BR Codes associated with Pix transactions, this is fixed at "01". This value indicates that the data following conforms to the Brazilan Payment System's specifications for Pix transactions.<br> | maxLength: 2; example: "01" |
| `transaction_currency` | integer | yes | ISO 4217 transaction currency. For example: 986 = Brazilin Real<br> | maximum: 999; example: 986 |
| `point_initiation_method` | string | no | Point initiation method. A value = "12" means that the BR Code can only be used once.<br> | maxLength: 2; example: "12" |
| `postal_code` | string | no | Código de Endereçamento Postal (CEP - Postal Addressing Code). 8 digits separated by a hyphen. | example: "86753-090" |
| `transaction_amount` | number | no | Transaction amount | maximum: 9999999999999; example: 86753.09 |
| `unreserved_templates` | array of object (schema `brcode.GenericSubBlock`) | no | Unreserved template |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/brcode.GenericSubBlock -->
### Schema `brcode.GenericSubBlock`

Pointer: `#/components/schemas/brcode.GenericSubBlock`. Type: object (schema `brcode.GenericSubBlock`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `additional_information` | string | no | Additional information in the BR Code content.  Relies on ID 02 of the BR Code standards. <br> |  |
| `gui` | string | no | Globally unique identifier. | maxLength: 14; example: "BR.COM.OTHER" |
| `items` | array of string | no | BR Code properties.<br><br>Example BR Code:<br><br> `00020126940014br.gov.bcb.pix2572qr-h.sandbox.pix.bcb.gov.br/rest/api/v1/dde3049e944b49818c82a55aa8312ea45204000053039865802BR5903Pix6008BRASILIA62070503***63040576`<br><br>All the chars inside a BR Code must respect the following rule: <br> {ID-2chars}{SIZE-2chars}{VALUE-N}{ID-2chars}{SIZE-2chars}{VALUE-N}{ID-2chars}{SIZE-2chars}{VALUE-N}...<br><br>For the BR Code example, it will be parsed to:<br>    {ID: "00", Size: 02, Value: "01"}<br>    {ID: "26", Size: 94, Value: "0014br.gov.bcb.pix2572qr-h.sandbox.pix.bcb.gov.br/rest/api/v1/dde3049e944b49818c82a55aa8312ea4"}<br><br>The items list will look like this:   <br><pre><br>[ <br>  "01",<br>  "0014br.gov.bcb.pix2572qr-h.sandbox.pix.bcb.gov.br/rest/api/v1/dde3049e944b49818c82a55aa8312ea4"  <br>] </pre><br> |  |
| `key` | string | no | Pix key. | maxLength: 36; example: "123e4567-e12b-12d1-a456-426655440000" |
| `pss` | string | no | Prestador de Serviço de Saque (PSS) means the Bank Brazilian payment system ID.  Also known as an ISPB (Identifcador do Sistema de Pagamento Brazil) number, an 8-digit value.<br> | maxLength: 8; example: "86753009" |
| `url` | string | no | The URL location in the Pix DICT where the payment will be settled. <br> | example: "br.gov.bcb.pix2572qr-h.sandbox.pix.bcb.gov.br/rest/api/v1/dde3049e944b49" |

<!-- schema: #/components/schemas/brcode.AdditionalDataFieldTemplate -->
### Schema `brcode.AdditionalDataFieldTemplate`

Pointer: `#/components/schemas/brcode.AdditionalDataFieldTemplate`. Type: object (schema `brcode.AdditionalDataFieldTemplate`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reference_label` | string | no | Reference label | maxLength: 25 |

<!-- schema: #/components/schemas/httpserver.Error -->
### Schema `httpserver.Error`

Pointer: `#/components/schemas/httpserver.Error`. Type: object (schema `httpserver.Error`).

> Server error

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | (type not declared) | no |  |  |
| `message` | string | no | Error message |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_BR_Code.yaml` | tag `BR Code`: POST /v1/emv/brcode/encode, POST /v1/emv/brcode/decode | https://github.com/PismoDevEx/pismo-api-specs | `f37ab75e09b3af92…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
