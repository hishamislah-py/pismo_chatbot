---
ku_id: KU-API-banking-credit-receivables--receivable
title: 'API reference: Banking - Credit receivables — Receivable'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Credit_receivables.yaml
  sha256: eb38b8a710548b184944b0c66db4d4e7de1065f7b76aebc6eb5d1985647e0759
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
- get-receivable
- create-receivable
- findByInternalNumber
- delete-receivable
- update
- validateUnicity
related_kus:
- KU-EVT-catalogue-depositary
- KU-EVT-depositary-data-events
specification_version: v1
---

# API reference: Banking - Credit receivables — Receivable

**KU ID:** `KU-API-banking-credit-receivables--receivable` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Receivable` in `api-specs/Banking_-_Credit_receivables.yaml` (“Banking - Credit receivables”, version `v1`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage receivables

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/credit-rights` | `get-receivable` | Get receivable (deprecated) | **yes** |
| `POST /v1/credit-rights` | `create-receivable` | Register receivable | no |
| `GET /v1/credit-rights/{internalNumber}` | `findByInternalNumber` | Get credit rights | no |
| `DELETE /v1/credit-rights/{internalNumber}` | `delete-receivable` | Delete receivable | no |
| `PATCH /v1/credit-rights/{internalNumber}` | `update` | Update receivable | no |
| `POST /v1/credit-rights/unicity` | `validateUnicity` | Validate receivable | no |

## Authentication

- `bearerAuth`: {"bearerFormat": "JWT", "scheme": "bearer", "type": "http"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Credit_receivables.yaml method=GET path=/v1/credit-rights operationId=get-receivable -->
### `GET /v1/credit-rights` — Get receivable (deprecated)

- **operationId:** `get-receivable`
- **Specification:** `api-specs/Banking_-_Credit_receivables.yaml` (Banking - Credit receivables)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/credit-rights-receivable`
- **Tags:** `Receivable`
- **Deprecated in specification:** **yes**
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get unique receivable. This endpoint is **DEPRECATED**, use the <a href="https://developers.pismo.io/pismo-docs/reference/validateunicity">Validate receivable</a> endpoint instead.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `interop_holding_number` | query | yes | string | Client-assigned interop holding number. Same as `holding_number` passed in the Register receivable endpoint. | minLength: 1; maxLength: 10 |
| `lender_document_number` | query | yes | string | Lender document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Must not be the same as the debtor document number.<br> |  |
| `debtor_document_number` | query | yes | string | Debtor document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Must not be the same as the lender document number.<br> |  |
| `maturity_date` | query | no | string | Maturity date. Format = yyyy-mm-dd. |  |
| `face_value` | query | no | string | Face value refers to the nominal or stated value of a financial instrument or asset, typically printed or stated on the instrument itself. It represents the initial value assigned to the instrument at the time of issuance or purchase. Can be up to 16 digits and two decimal places.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Success message is sent to the client while an unicity validation is processed asynchronously | `application/json:`: object (schema `GetUniqueReceivableResponse`) |
| 400 | Bad Request | `application/json`: object (schema `GlobalErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `GlobalErrorResponse`) |

##### Response 202

**202 `application/json:` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `debtor_document_number` | string (schema `DebtorDocumentNumber`) | no | Debtor document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Must not be the same as the lender document number. <br> | maxLength: 14 |
| `face_value` | number (schema `FaceValue`) | no | Face value refers to the nominal or stated value of a financial instrument or asset, typically printed or stated on the instrument itself. It represents the initial value assigned to the instrument at the time of issuance or purchase.<br> | example: 499.23 |
| `interop_holding_number` | string (schema `InteropHoldingNumber`) | no | Client-assigned interoperation holding number. Called `holding_number` when passed in the Register receivable endpoint.<br> | example: "017917411A" |
| `lender_document_number` | string (schema `LenderDocumentNumber`) | no | Lender document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Should not be the same as the debtor document number. <br> | example: "51407165000113" |
| `maturity_date` | string (schema `MaturityDate`) | no | Maturity date. Format = yyyy-mm-dd. Must be equal to today or later. | example: "2023-06=22" |
| `message` | string (schema `Message`) | no | Message | maxLength: 500; example: "Credit rights update request is being processed" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `False`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Banking_-_Credit_receivables.yaml method=POST path=/v1/credit-rights operationId=create-receivable -->
### `POST /v1/credit-rights` — Register receivable

- **operationId:** `create-receivable`
- **Specification:** `api-specs/Banking_-_Credit_receivables.yaml` (Banking - Credit receivables)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/credit-rights-receivable`
- **Tags:** `Receivable`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Register an account receivable - Brazil only. A receivable represents money expected to be collected from an entity (*debtor*) who has purchased products or services, but has not yet paid for them in full. The *lender*, the person or entity owed the money, can sell this debt to a new *owner*, who may package it as part of another financial instrument, in much the same way a mortgage is sold to become part of a mortgage-backed security. 
>
> Pismo works with <a href="https://www.b3.com.br/en_us/" target="_blank">B3</a> - a large financial market infrastructure provider in Brazil - to register invoices. 
>
> If creation fails, a <a href="https://developers.pismo.io/events/docs/depositary-credit-rights-registration-failure-1" target="_blank">credit_rights_registration_failure-1</a> event is generated. If creation succeeds, a <a href="https://developers.pismo.io/events/docs/depositary-credit-rights-registration-success-1" target="_blank">credit_rights_registration_success-1</a> event is generated 

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CreateReceivableRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `credit_rights_receivable_type` | integer (schema `CreditRightsReceivableType`) | yes | Credit receivable type:<br><br>1 - Mercantile<br>2 - Service  <br> | enum: [1, 2]; format: "int32"; minimum: 1; maximum: 2 |
| `debtor_name` | string (schema `DebtorName`) | yes | Debtor name | minLength: 1; maxLength: 100; example: "Bonnie Ann Clyde" |
| `debtor_document_number` | string (schema `DebtorDocumentNumber`) | yes | Debtor document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Must not be the same as the lender document number. <br> | maxLength: 14 |
| `face_value` | number (schema `FaceValue`) | yes | Face value refers to the nominal or stated value of a financial instrument or asset, typically printed or stated on the instrument itself. It represents the initial value assigned to the instrument at the time of issuance or purchase.<br> | example: 499.23 |
| `holding_number` | string (schema `HoldingNumber`) | yes | Holding number - the number of the invoice (min size 1, max size 9) + '.' + the number of installments (min 1 - max 99).<br> | minLength: 3; maxLength: 12; example: "1234.8" |
| `ibge_code` | integer (schema `IbgeCode`) | yes | IBGE stands for Instituto Brasileiro de Geografia e Estatística, which translates to the Brazilian Institute of Geography and Statistics. This Brazilian national statistical agency is responsible for collecting and providing official data on various aspects of the country. An IBGE code is a specific numerical code assigned to various administrative divisions and geographical areas in Brazil.<br><br>For this application, the IBGE code identifies the town and **must** have 7 digits (1000000 to 9999999).<br> | format: "int32"; minLength: 7; maxLength: 7; example: 3304557 |
| `internal_number` | string (schema `InternalNumber`) | yes | Client-assigned internal number. | minLength: 1; maxLength: 40; example: "5eae1070-28cc-4e99-ad45-c380731d5c0a" |
| `invoice_number` | integer (schema `InvoiceNumber`) | yes | Invoice number. Generated when receivable is created. | format: "int64"; minLength: 1; maxLength: 9; example: 88 |
| `invoice_serie` | integer (schema `InvoiceSerie`) | yes | Invoice series number. "Serie" is the Portuguese word for "series". | format: "int64"; minLength: 1; maxLength: 3; example: 1 |
| `invoice_total_value` | number (schema `InvoiceTotalValue`) | yes | Invoice total value. Can be up to 16 digits and two decimal places. | maxLength: 19; example: 5678.99 |
| `issuing_date` | string (schema `IssuingDate`) | yes | Issuing date. Must be before or equal to today. Format = yyyy-mm-dd. | format: "date"; example: "2023-06-07" |
| `lender_name` | string (schema `LenderName`) | yes | Lender name | minLength: 1; maxLength: 100; example: "Al Dente" |
| `lender_document_number` | string (schema `LenderDocumentNumber`) | yes | Lender document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Should not be the same as the debtor document number. <br> | example: "51407165000113" |
| `maturity_date` | string (schema `MaturityDate`) | yes | Maturity date. Format = yyyy-mm-dd. Must be equal to today or later. | example: "2023-06=22" |
| `payment_method` | integer (schema `PaymentMethod`) | yes | Payment method: <br><br>1 - **Boleto**: The Boleto payment method is a popular payment system in Brazil. It is a widely used alternative to traditional credit card payments and bank transfers. Boleto Bancário, commonly referred to as "Boleto," is a payment voucher that allows individuals and businesses to make payments for goods and services.<br><br>2 - **TED**: The TED (Transferência Eletrônica Disponível) payment method is a popular electronic funds transfer system in Brazil. It is commonly used for interbank transfers, allowing individuals and businesses to transfer funds between different financial institutions within the country.<br><br>3 - **DOC**: The DOC (Documento de Ordem de Crédito) payment method is another electronic funds transfer system in Brazil, similar to TED (Transferência Eletrônica Disponível). DOC is primarily used for interbank transfers but differs from TED in terms of timing, limits, and processing.<br><br>4 - **Dinheiro**: "Dinheiro" is the Portuguese word for "money" or a general term for cash payments. Cash is a widely used payment method in various countries, including Brazil, where the official currency is the Brazilian Real (BRL).<br><br>5 - **Título**: "Titulo" means title in Portuguese.<br><br>6 - **Pix**: The Pix payment method is a new and instant electronic payment system introduced by the Central Bank of Brazil. It was launched in November 2020 and has gained significant popularity in a short period. Pix allows individuals and businesses to make real-time transfers and payments between different financial institutions in Brazil. It operates 24/7, including weekends and holidays, providing a fast and alternative to traditional payment methods such as TED and DOC transfers.  <br> | enum: [1, 2, 3, 4, 5, 6]; format: "int32"; minimum: 1; maximum: 6; example: 2 |
| `payment_status` | integer (schema `PaymentStatus`) | yes | Payment Status:<br>  1 - PAID  <br>  2 - UNPAID<br> | enum: [1, 2]; format: "int32"; minimum: 1; maximum: 2; example: 1 |
| `recorder_account` | integer (schema `RecorderAccount`) | yes | Recorder account | format: "int64"; minLength: 1; maxLength: 8; example: 12345678 |
| `access_key` | string (schema `AccessKey`) | no | Client-generated identifier. This field is used for the [Get invoice](ref:findbyaccesskey) endpoint. | minLength: 1; maxLength: 44; example: "KAB6J8903CNMH01892749JKSNOAXMCA7199382ABCERL" |
| `collateral_type` | integer (schema `CollateralType`) | no | Collateral type:  <br><br>  1 - Aval. In Brazil, the term "aval collateral" refers to a specific type of collateral used in financial transactions. "Aval" is a Portuguese term that means "endorsement" or "guarantee," and it is commonly used in the Brazilian financial system. Aval collateral is a form of guarantee where a third party, known as the "avalista" or guarantor, pledges their assets or credit worthiness to secure a loan or financial obligation on behalf of the borrower. The avalista becomes jointly liable for the debt and agrees to fulfill the obligations if the borrower fails to do so. <br> | enum: [1]; format: "int32"; minimum: 1; maximum: 1; example: 1 |
| `credit_operations` | array of object (schema `CreditOperation`) (schema `CreditOperationsArray`) | no |  | minItems: 1; maxItems: 2147483647 |
| `debtor_signing_date` | string (schema `DebtorSigningDate`) | no | Debtor signing date. Format = yyyy-mm-dd | format: "date"; example: "2023-06-07" |
| `description` | string (schema `Description`) | no | Receivable description | maxLength: 500; example: "Receivable description..." |
| `guarantor_name` | string (schema `GuarantorName`) | no | Guarantor name | minLength: 1; maxLength: 100; example: "Lansky Loan" |
| `lender_signing_date` | string (schema `LenderSigningDate`) | no | Lender signing date. Format = yyyy-mm-dd. Must be before or equal to today. | format: "date"; example: "2023-06-22" |
| `owner_document_number` | string (schema `OwnerDocumentNumber`) | no | Owner document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). <br> | example: "51008931000177" |
| `owner_name` | string (schema `OwnerName`) | no | Owner name | minLength: 1; maxLength: 100; example: "Biff Wellington" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Success message is sent to the client while registration is processed asynchronously | `application/json`: object (schema `CreateReceivableResponse`) |
| 400 | Bad Request | `application/json`: object (schema `GlobalErrorResponse`) |
| 401 | Missing or invalid access token | `application/json`: object (schema `GlobalErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `GlobalErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Credit receivable response message |  |
| `recorder_account` | integer | no | Recorder account number | format: "int64" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `depositary-credit-rights-registration-failure-1` | https://developers.pismo.io/events/docs/depositary-credit-rights-registration-failure-1 |
| `depositary-credit-rights-registration-success-1` | https://developers.pismo.io/events/docs/depositary-credit-rights-registration-success-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;500`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-depositary-data-events`.

<!-- op: spec=api-specs/Banking_-_Credit_receivables.yaml method=GET path=/v1/credit-rights/{internalNumber} operationId=findByInternalNumber -->
### `GET /v1/credit-rights/{internalNumber}` — Get credit rights

- **operationId:** `findByInternalNumber`
- **Specification:** `api-specs/Banking_-_Credit_receivables.yaml` (Banking - Credit receivables)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/credit-rights-receivable`
- **Tags:** `Receivable`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get credit rights with internal number.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `internalNumber` | path | yes | string | Client-assigned internal number. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `GetReceivableResponse`) |
| 204 | Credit Rights not found | `application/json`: object (schema `GetReceivableResponse`) |
| 400 | Bad Request | `application/json`: object (schema `GlobalErrorResponse`) |
| 401 | Missing or invalid access token | `application/json`: object (schema `GlobalErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `GlobalErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `access_key` | string (schema `AccessKey`) | no | Client-generated identifier. This field is used for the [Get invoice](ref:findbyaccesskey) endpoint. | minLength: 1; maxLength: 44; example: "KAB6J8903CNMH01892749JKSNOAXMCA7199382ABCERL" |
| `collateral_type` | integer (schema `CollateralType`) | no | Collateral type:  <br><br>  1 - Aval. In Brazil, the term "aval collateral" refers to a specific type of collateral used in financial transactions. "Aval" is a Portuguese term that means "endorsement" or "guarantee," and it is commonly used in the Brazilian financial system. Aval collateral is a form of guarantee where a third party, known as the "avalista" or guarantor, pledges their assets or credit worthiness to secure a loan or financial obligation on behalf of the borrower. The avalista becomes jointly liable for the debt and agrees to fulfill the obligations if the borrower fails to do so. <br> | enum: [1]; format: "int32"; minimum: 1; maximum: 1; example: 1 |
| `created_at` | string (schema `CreatedAt`) | no | Created at time (UTC) | format: "date-time"; example: "2021-07-06T13:11:05.000Z" |
| `credit_operations` | array of object (schema `CreditOperation`) (schema `CreditOperationsArray`) | no |  | minItems: 1; maxItems: 2147483647 |
| `credit_rights_receivable_type` | integer (schema `CreditRightsReceivableType`) | no | Credit receivable type:<br><br>1 - Mercantile<br>2 - Service  <br> | enum: [1, 2]; format: "int32"; minimum: 1; maximum: 2 |
| `debtor_document_number` | string (schema `DebtorDocumentNumber`) | no | Debtor document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Must not be the same as the lender document number. <br> | maxLength: 14 |
| `debtor_name` | string (schema `DebtorName`) | no | Debtor name | minLength: 1; maxLength: 100; example: "Bonnie Ann Clyde" |
| `debtor_signing_date` | string (schema `DebtorSigningDate`) | no | Debtor signing date. Format = yyyy-mm-dd | format: "date"; example: "2023-06-07" |
| `description` | string (schema `Description`) | no | Receivable description | maxLength: 500; example: "Receivable description..." |
| `face_value` | number (schema `FaceValue`) | no | Face value refers to the nominal or stated value of a financial instrument or asset, typically printed or stated on the instrument itself. It represents the initial value assigned to the instrument at the time of issuance or purchase.<br> | example: 499.23 |
| `guarantor_name` | string (schema `GuarantorName`) | no | Guarantor name | minLength: 1; maxLength: 100; example: "Lansky Loan" |
| `holding_number` | string (schema `HoldingNumber`) | no | Holding number - the number of the invoice (min size 1, max size 9) + '.' + the number of installments (min 1 - max 99).<br> | minLength: 3; maxLength: 12; example: "1234.8" |
| `ibge_code` | integer (schema `IbgeCode`) | no | IBGE stands for Instituto Brasileiro de Geografia e Estatística, which translates to the Brazilian Institute of Geography and Statistics. This Brazilian national statistical agency is responsible for collecting and providing official data on various aspects of the country. An IBGE code is a specific numerical code assigned to various administrative divisions and geographical areas in Brazil.<br><br>For this application, the IBGE code identifies the town and **must** have 7 digits (1000000 to 9999999).<br> | format: "int32"; minLength: 7; maxLength: 7; example: 3304557 |
| `internal_number` | string (schema `InternalNumber`) | no | Client-assigned internal number. | minLength: 1; maxLength: 40; example: "5eae1070-28cc-4e99-ad45-c380731d5c0a" |
| `interop_holding_number` | string (schema `InteropHoldingNumber`) | no | Client-assigned interoperation holding number. Called `holding_number` when passed in the Register receivable endpoint.<br> | example: "017917411A" |
| `invoice_number` | integer (schema `InvoiceNumber`) | no | Invoice number. Generated when receivable is created. | format: "int64"; minLength: 1; maxLength: 9; example: 88 |
| `invoice_serie` | integer (schema `InvoiceSerie`) | no | Invoice series number. "Serie" is the Portuguese word for "series". | format: "int64"; minLength: 1; maxLength: 3; example: 1 |
| `invoice_total_value` | number (schema `InvoiceTotalValue`) | no | Invoice total value. Can be up to 16 digits and two decimal places. | maxLength: 19; example: 5678.99 |
| `issuing_date` | string (schema `IssuingDate`) | no | Issuing date. Must be before or equal to today. Format = yyyy-mm-dd. | format: "date"; example: "2023-06-07" |
| `lender_document_number` | string (schema `LenderDocumentNumber`) | no | Lender document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Should not be the same as the debtor document number. <br> | example: "51407165000113" |
| `lender_name` | string (schema `LenderName`) | no | Lender name | minLength: 1; maxLength: 100; example: "Al Dente" |
| `lender_signing_date` | string (schema `LenderSigningDate`) | no | Lender signing date. Format = yyyy-mm-dd. Must be before or equal to today. | format: "date"; example: "2023-06-22" |
| `maturity_date` | string (schema `MaturityDate`) | no | Maturity date. Format = yyyy-mm-dd. Must be equal to today or later. | example: "2023-06=22" |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `owner_document_number` | string (schema `OwnerDocumentNumber`) | no | Owner document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). <br> | example: "51008931000177" |
| `owner_name` | string (schema `OwnerName`) | no | Owner name | minLength: 1; maxLength: 100; example: "Biff Wellington" |
| `payment_method` | integer (schema `PaymentMethod`) | no | Payment method: <br><br>1 - **Boleto**: The Boleto payment method is a popular payment system in Brazil. It is a widely used alternative to traditional credit card payments and bank transfers. Boleto Bancário, commonly referred to as "Boleto," is a payment voucher that allows individuals and businesses to make payments for goods and services.<br><br>2 - **TED**: The TED (Transferência Eletrônica Disponível) payment method is a popular electronic funds transfer system in Brazil. It is commonly used for interbank transfers, allowing individuals and businesses to transfer funds between different financial institutions within the country.<br><br>3 - **DOC**: The DOC (Documento de Ordem de Crédito) payment method is another electronic funds transfer system in Brazil, similar to TED (Transferência Eletrônica Disponível). DOC is primarily used for interbank transfers but differs from TED in terms of timing, limits, and processing.<br><br>4 - **Dinheiro**: "Dinheiro" is the Portuguese word for "money" or a general term for cash payments. Cash is a widely used payment method in various countries, including Brazil, where the official currency is the Brazilian Real (BRL).<br><br>5 - **Título**: "Titulo" means title in Portuguese.<br><br>6 - **Pix**: The Pix payment method is a new and instant electronic payment system introduced by the Central Bank of Brazil. It was launched in November 2020 and has gained significant popularity in a short period. Pix allows individuals and businesses to make real-time transfers and payments between different financial institutions in Brazil. It operates 24/7, including weekends and holidays, providing a fast and alternative to traditional payment methods such as TED and DOC transfers.  <br> | enum: [1, 2, 3, 4, 5, 6]; format: "int32"; minimum: 1; maximum: 6; example: 2 |
| `payment_status` | integer (schema `PaymentStatus`) | no | Payment Status:<br>  1 - PAID  <br>  2 - UNPAID<br> | enum: [1, 2]; format: "int32"; minimum: 1; maximum: 2; example: 1 |
| `recorder_account` | integer (schema `RecorderAccount`) | no | Recorder account | format: "int64"; minLength: 1; maxLength: 8; example: 12345678 |
| `status` | string (schema `Status`) | no | Status | enum: ["ACTIVE", "COMPLETED", "INACTIVE", "REJECTED", "ACTIVE_PENDING"]; example: "ACTIVE" |
| `updated_at` | string (schema `UpdatedAt`) | no | Updated at time (UTC) | format: "date-time"; example: "2021-07-06T13:11:05.000Z" |

##### Response 204

**204 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `access_key` | string (schema `AccessKey`) | no | Client-generated identifier. This field is used for the [Get invoice](ref:findbyaccesskey) endpoint. | minLength: 1; maxLength: 44; example: "KAB6J8903CNMH01892749JKSNOAXMCA7199382ABCERL" |
| `collateral_type` | integer (schema `CollateralType`) | no | Collateral type:  <br><br>  1 - Aval. In Brazil, the term "aval collateral" refers to a specific type of collateral used in financial transactions. "Aval" is a Portuguese term that means "endorsement" or "guarantee," and it is commonly used in the Brazilian financial system. Aval collateral is a form of guarantee where a third party, known as the "avalista" or guarantor, pledges their assets or credit worthiness to secure a loan or financial obligation on behalf of the borrower. The avalista becomes jointly liable for the debt and agrees to fulfill the obligations if the borrower fails to do so. <br> | enum: [1]; format: "int32"; minimum: 1; maximum: 1; example: 1 |
| `created_at` | string (schema `CreatedAt`) | no | Created at time (UTC) | format: "date-time"; example: "2021-07-06T13:11:05.000Z" |
| `credit_operations` | array of object (schema `CreditOperation`) (schema `CreditOperationsArray`) | no |  | minItems: 1; maxItems: 2147483647 |
| `credit_rights_receivable_type` | integer (schema `CreditRightsReceivableType`) | no | Credit receivable type:<br><br>1 - Mercantile<br>2 - Service  <br> | enum: [1, 2]; format: "int32"; minimum: 1; maximum: 2 |
| `debtor_document_number` | string (schema `DebtorDocumentNumber`) | no | Debtor document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Must not be the same as the lender document number. <br> | maxLength: 14 |
| `debtor_name` | string (schema `DebtorName`) | no | Debtor name | minLength: 1; maxLength: 100; example: "Bonnie Ann Clyde" |
| `debtor_signing_date` | string (schema `DebtorSigningDate`) | no | Debtor signing date. Format = yyyy-mm-dd | format: "date"; example: "2023-06-07" |
| `description` | string (schema `Description`) | no | Receivable description | maxLength: 500; example: "Receivable description..." |
| `face_value` | number (schema `FaceValue`) | no | Face value refers to the nominal or stated value of a financial instrument or asset, typically printed or stated on the instrument itself. It represents the initial value assigned to the instrument at the time of issuance or purchase.<br> | example: 499.23 |
| `guarantor_name` | string (schema `GuarantorName`) | no | Guarantor name | minLength: 1; maxLength: 100; example: "Lansky Loan" |
| `holding_number` | string (schema `HoldingNumber`) | no | Holding number - the number of the invoice (min size 1, max size 9) + '.' + the number of installments (min 1 - max 99).<br> | minLength: 3; maxLength: 12; example: "1234.8" |
| `ibge_code` | integer (schema `IbgeCode`) | no | IBGE stands for Instituto Brasileiro de Geografia e Estatística, which translates to the Brazilian Institute of Geography and Statistics. This Brazilian national statistical agency is responsible for collecting and providing official data on various aspects of the country. An IBGE code is a specific numerical code assigned to various administrative divisions and geographical areas in Brazil.<br><br>For this application, the IBGE code identifies the town and **must** have 7 digits (1000000 to 9999999).<br> | format: "int32"; minLength: 7; maxLength: 7; example: 3304557 |
| `internal_number` | string (schema `InternalNumber`) | no | Client-assigned internal number. | minLength: 1; maxLength: 40; example: "5eae1070-28cc-4e99-ad45-c380731d5c0a" |
| `interop_holding_number` | string (schema `InteropHoldingNumber`) | no | Client-assigned interoperation holding number. Called `holding_number` when passed in the Register receivable endpoint.<br> | example: "017917411A" |
| `invoice_number` | integer (schema `InvoiceNumber`) | no | Invoice number. Generated when receivable is created. | format: "int64"; minLength: 1; maxLength: 9; example: 88 |
| `invoice_serie` | integer (schema `InvoiceSerie`) | no | Invoice series number. "Serie" is the Portuguese word for "series". | format: "int64"; minLength: 1; maxLength: 3; example: 1 |
| `invoice_total_value` | number (schema `InvoiceTotalValue`) | no | Invoice total value. Can be up to 16 digits and two decimal places. | maxLength: 19; example: 5678.99 |
| `issuing_date` | string (schema `IssuingDate`) | no | Issuing date. Must be before or equal to today. Format = yyyy-mm-dd. | format: "date"; example: "2023-06-07" |
| `lender_document_number` | string (schema `LenderDocumentNumber`) | no | Lender document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Should not be the same as the debtor document number. <br> | example: "51407165000113" |
| `lender_name` | string (schema `LenderName`) | no | Lender name | minLength: 1; maxLength: 100; example: "Al Dente" |
| `lender_signing_date` | string (schema `LenderSigningDate`) | no | Lender signing date. Format = yyyy-mm-dd. Must be before or equal to today. | format: "date"; example: "2023-06-22" |
| `maturity_date` | string (schema `MaturityDate`) | no | Maturity date. Format = yyyy-mm-dd. Must be equal to today or later. | example: "2023-06=22" |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `owner_document_number` | string (schema `OwnerDocumentNumber`) | no | Owner document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). <br> | example: "51008931000177" |
| `owner_name` | string (schema `OwnerName`) | no | Owner name | minLength: 1; maxLength: 100; example: "Biff Wellington" |
| `payment_method` | integer (schema `PaymentMethod`) | no | Payment method: <br><br>1 - **Boleto**: The Boleto payment method is a popular payment system in Brazil. It is a widely used alternative to traditional credit card payments and bank transfers. Boleto Bancário, commonly referred to as "Boleto," is a payment voucher that allows individuals and businesses to make payments for goods and services.<br><br>2 - **TED**: The TED (Transferência Eletrônica Disponível) payment method is a popular electronic funds transfer system in Brazil. It is commonly used for interbank transfers, allowing individuals and businesses to transfer funds between different financial institutions within the country.<br><br>3 - **DOC**: The DOC (Documento de Ordem de Crédito) payment method is another electronic funds transfer system in Brazil, similar to TED (Transferência Eletrônica Disponível). DOC is primarily used for interbank transfers but differs from TED in terms of timing, limits, and processing.<br><br>4 - **Dinheiro**: "Dinheiro" is the Portuguese word for "money" or a general term for cash payments. Cash is a widely used payment method in various countries, including Brazil, where the official currency is the Brazilian Real (BRL).<br><br>5 - **Título**: "Titulo" means title in Portuguese.<br><br>6 - **Pix**: The Pix payment method is a new and instant electronic payment system introduced by the Central Bank of Brazil. It was launched in November 2020 and has gained significant popularity in a short period. Pix allows individuals and businesses to make real-time transfers and payments between different financial institutions in Brazil. It operates 24/7, including weekends and holidays, providing a fast and alternative to traditional payment methods such as TED and DOC transfers.  <br> | enum: [1, 2, 3, 4, 5, 6]; format: "int32"; minimum: 1; maximum: 6; example: 2 |
| `payment_status` | integer (schema `PaymentStatus`) | no | Payment Status:<br>  1 - PAID  <br>  2 - UNPAID<br> | enum: [1, 2]; format: "int32"; minimum: 1; maximum: 2; example: 1 |
| `recorder_account` | integer (schema `RecorderAccount`) | no | Recorder account | format: "int64"; minLength: 1; maxLength: 8; example: 12345678 |
| `status` | string (schema `Status`) | no | Status | enum: ["ACTIVE", "COMPLETED", "INACTIVE", "REJECTED", "ACTIVE_PENDING"]; example: "ACTIVE" |
| `updated_at` | string (schema `UpdatedAt`) | no | Updated at time (UTC) | format: "date-time"; example: "2021-07-06T13:11:05.000Z" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;204;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Credit_receivables.yaml method=DELETE path=/v1/credit-rights/{internalNumber} operationId=delete-receivable -->
### `DELETE /v1/credit-rights/{internalNumber}` — Delete receivable

- **operationId:** `delete-receivable`
- **Specification:** `api-specs/Banking_-_Credit_receivables.yaml` (Banking - Credit receivables)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/credit-rights-receivable`
- **Tags:** `Receivable`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Delete receivable.
>
>  If deletion fails, a <a href="https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-failure-1" target="_blank">credit_rights_status_change_failure-1</a> event is generated. If deletion succeeds, a <a href="https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-success-1" target="_blank">credit_rights_status_change_success-1</a> event is generated.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `internalNumber` | path | yes | string | Client-assigned internal number. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Success message is sent to the client while delete is processed asynchronously | `application/json:`: object (schema `DeleteReceivableResponse`) |
| 400 | Bad Request | `application/json`: object (schema `GlobalErrorResponse`) |
| 401 | Missing or invalid access token | `application/json`: object (schema `GlobalErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `GlobalErrorResponse`) |

##### Response 202

**202 `application/json:` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `internal_number` | string | no | Client-assigned internal number |  |
| `message` | string | no | Deletion message |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `depositary-credit-rights-status-change-failure-1` | https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-failure-1 |
| `depositary-credit-rights-status-change-success-1` | https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-success-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;500`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-depositary-data-events`.

<!-- op: spec=api-specs/Banking_-_Credit_receivables.yaml method=PATCH path=/v1/credit-rights/{internalNumber} operationId=update -->
### `PATCH /v1/credit-rights/{internalNumber}` — Update receivable

- **operationId:** `update`
- **Specification:** `api-specs/Banking_-_Credit_receivables.yaml` (Banking - Credit receivables)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/credit-rights-receivable`
- **Tags:** `Receivable`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Update receivable for fields passed.
>
> If updating the status fails, a <a href="https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-failure-1" target="_blank">credit_rights_status_change_failure-1</a> event is generated. If updating the status succeeds, a <a href="https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-success-1" target="_blank">credit_rights_status_change_success-1</a> event is generated.
>
> If updating any other fields besides status fails, a <a href="https://developers.pismo.io/events/docs/depositary-credit-rights-change-failure-1" target="_blank">credit_rights_change_failure-1</a> event is generated. If updating a non-status field succeeds, a <a href="https://developers.pismo.io/events/docs/depositary-credit-rights-change-success-1" target="_blank">credit_rights_change_success-1</a> event is generated.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `internalNumber` | path | yes | string | Client-assigned internal number. |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `UpdateReceivableRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `access_key` | string (schema `AccessKey`) | no | Client-generated identifier. This field is used for the [Get invoice](ref:findbyaccesskey) endpoint. | minLength: 1; maxLength: 44; example: "KAB6J8903CNMH01892749JKSNOAXMCA7199382ABCERL" |
| `collateral_type` | integer (schema `CollateralType`) | no | Collateral type:  <br><br>  1 - Aval. In Brazil, the term "aval collateral" refers to a specific type of collateral used in financial transactions. "Aval" is a Portuguese term that means "endorsement" or "guarantee," and it is commonly used in the Brazilian financial system. Aval collateral is a form of guarantee where a third party, known as the "avalista" or guarantor, pledges their assets or credit worthiness to secure a loan or financial obligation on behalf of the borrower. The avalista becomes jointly liable for the debt and agrees to fulfill the obligations if the borrower fails to do so. <br> | enum: [1]; format: "int32"; minimum: 1; maximum: 1; example: 1 |
| `credit_operations` | array of object (schema `CreditOperation`) (schema `CreditOperationsArray`) | no |  | minItems: 1; maxItems: 2147483647 |
| `debtor_signing_date` | string (schema `DebtorSigningDate`) | no | Debtor signing date. Format = yyyy-mm-dd | format: "date"; example: "2023-06-07" |
| `description` | string (schema `Description`) | no | Receivable description | maxLength: 500; example: "Receivable description..." |
| `guarantor_name` | string (schema `GuarantorName`) | no | Guarantor name | minLength: 1; maxLength: 100; example: "Lansky Loan" |
| `ibge_code` | integer (schema `IbgeCode`) | no | IBGE stands for Instituto Brasileiro de Geografia e Estatística, which translates to the Brazilian Institute of Geography and Statistics. This Brazilian national statistical agency is responsible for collecting and providing official data on various aspects of the country. An IBGE code is a specific numerical code assigned to various administrative divisions and geographical areas in Brazil.<br><br>For this application, the IBGE code identifies the town and **must** have 7 digits (1000000 to 9999999).<br> | format: "int32"; minLength: 7; maxLength: 7; example: 3304557 |
| `lender_signing_date` | string (schema `LenderSigningDate`) | no | Lender signing date. Format = yyyy-mm-dd. Must be before or equal to today. | format: "date"; example: "2023-06-22" |
| `owner_document_number` | string (schema `OwnerDocumentNumber`) | no | Owner document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). <br> | example: "51008931000177" |
| `owner_name` | string (schema `OwnerName`) | no | Owner name | minLength: 1; maxLength: 100; example: "Biff Wellington" |
| `payment_method` | integer (schema `PaymentMethod`) | no | Payment method: <br><br>1 - **Boleto**: The Boleto payment method is a popular payment system in Brazil. It is a widely used alternative to traditional credit card payments and bank transfers. Boleto Bancário, commonly referred to as "Boleto," is a payment voucher that allows individuals and businesses to make payments for goods and services.<br><br>2 - **TED**: The TED (Transferência Eletrônica Disponível) payment method is a popular electronic funds transfer system in Brazil. It is commonly used for interbank transfers, allowing individuals and businesses to transfer funds between different financial institutions within the country.<br><br>3 - **DOC**: The DOC (Documento de Ordem de Crédito) payment method is another electronic funds transfer system in Brazil, similar to TED (Transferência Eletrônica Disponível). DOC is primarily used for interbank transfers but differs from TED in terms of timing, limits, and processing.<br><br>4 - **Dinheiro**: "Dinheiro" is the Portuguese word for "money" or a general term for cash payments. Cash is a widely used payment method in various countries, including Brazil, where the official currency is the Brazilian Real (BRL).<br><br>5 - **Título**: "Titulo" means title in Portuguese.<br><br>6 - **Pix**: The Pix payment method is a new and instant electronic payment system introduced by the Central Bank of Brazil. It was launched in November 2020 and has gained significant popularity in a short period. Pix allows individuals and businesses to make real-time transfers and payments between different financial institutions in Brazil. It operates 24/7, including weekends and holidays, providing a fast and alternative to traditional payment methods such as TED and DOC transfers.  <br> | enum: [1, 2, 3, 4, 5, 6]; format: "int32"; minimum: 1; maximum: 6; example: 2 |
| `payment_status` | integer (schema `PaymentStatus`) | no | Payment Status:<br>  1 - PAID  <br>  2 - UNPAID<br> | enum: [1, 2]; format: "int32"; minimum: 1; maximum: 2; example: 1 |
| `updated_face_value` | number (schema `UpdatedFaceValue`) | no | Updated face value. | example: 456.99 |
| `updated_maturity_date` | string (schema `UpdatedMaturityDate`) | no | Updated maturity date. Format = yyyy-mm-dd. | example: "2023-09-14" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Success message is sent to the client while update is processed asynchronously | `application/json`: object (schema `UpdateReceivableResponse`) |
| 400 | Bad Request | `application/json`: object (schema `GlobalErrorResponse`) |
| 401 | Missing or invalid access token | `application/json`: object (schema `GlobalErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `GlobalErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `internal_number` | string (schema `InternalNumber`) | no | Client-assigned internal number. | minLength: 1; maxLength: 40; example: "5eae1070-28cc-4e99-ad45-c380731d5c0a" |
| `message` | string (schema `Message`) | no | Message | maxLength: 500; example: "Credit rights update request is being processed" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `depositary-credit-rights-change-failure-1` | https://developers.pismo.io/events/docs/depositary-credit-rights-change-failure-1 |
| `depositary-credit-rights-change-success-1` | https://developers.pismo.io/events/docs/depositary-credit-rights-change-success-1 |
| `depositary-credit-rights-status-change-failure-1` | https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-failure-1 |
| `depositary-credit-rights-status-change-success-1` | https://developers.pismo.io/events/docs/depositary-credit-rights-status-change-success-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;500`, has examples `False`, emits events `4`, deprecated `False`.

Guides that link to this operation: `KU-EVT-depositary-data-events`.

<!-- op: spec=api-specs/Banking_-_Credit_receivables.yaml method=POST path=/v1/credit-rights/unicity operationId=validateUnicity -->
### `POST /v1/credit-rights/unicity` — Validate receivable

- **operationId:** `validateUnicity`
- **Specification:** `api-specs/Banking_-_Credit_receivables.yaml` (Banking - Credit receivables)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/credit-rights-receivable`
- **Tags:** `Receivable`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Validate a receivable's uniqueness in the credit rights registry.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `GetUniqueReceivableRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `params` | object (schema `GetUniqueReceivableRequestParams`) | yes |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Success response | `application/json`: object (schema `GetUniqueReceivableResponse`) |
| 400 | Bad Request | `application/json`: object (schema `GlobalErrorResponse`) |
| 401 | Missing or invalid access token | `application/json`: object (schema `GlobalErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `GlobalErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `debtor_document_number` | string (schema `DebtorDocumentNumber`) | no | Debtor document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Must not be the same as the lender document number. <br> | maxLength: 14 |
| `face_value` | number (schema `FaceValue`) | no | Face value refers to the nominal or stated value of a financial instrument or asset, typically printed or stated on the instrument itself. It represents the initial value assigned to the instrument at the time of issuance or purchase.<br> | example: 499.23 |
| `interop_holding_number` | string (schema `InteropHoldingNumber`) | no | Client-assigned interoperation holding number. Called `holding_number` when passed in the Register receivable endpoint.<br> | example: "017917411A" |
| `lender_document_number` | string (schema `LenderDocumentNumber`) | no | Lender document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Should not be the same as the debtor document number. <br> | example: "51407165000113" |
| `maturity_date` | string (schema `MaturityDate`) | no | Maturity date. Format = yyyy-mm-dd. Must be equal to today or later. | example: "2023-06=22" |
| `message` | string (schema `Message`) | no | Message | maxLength: 500; example: "Credit rights update request is being processed" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-EVT-depositary-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/GlobalErrorResponse -->
### Schema `GlobalErrorResponse`

Pointer: `#/components/schemas/GlobalErrorResponse`. Type: object (schema `GlobalErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `correlationId` | string (schema `CorrelationID`) | no | Correlation ID (CID). This field is used to link related API requests and events. The CID can help the Pismo engineering team track everything related to a call. If one isn't passed, one is automatically generated. You can find the CID in a response header. <br> | example: "88474990237-94940" |
| `errors` | array of string (schema `Errors`) | no |  |  |

<!-- schema: #/components/schemas/CreditOperation -->
### Schema `CreditOperation`

Pointer: `#/components/schemas/CreditOperation`. Type: object (schema `CreditOperation`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `contact_number` | string (schema `ContactNumber`) | no | Contact number | minLength: 1; maxLength: 15; example: "+14158675309" |
| `guarantee_percentage` | number (schema `GuaranteePercentage`) | no | Gurantor percentage | example: 5 |
| `operation_date` | string (schema `OperationDate`) | no | Operation date. Format = yyyy-mm-dd. | format: "date"; example: "2023-06-06" |
| `operation_maturity` | string (schema `OperationMaturity`) | no | Operation maturity. Format = yyyy-mm-dd. | format: "date"; example: "2023-09-08" |
| `operation_type` | string (schema `OperationType`) | no | Operation type. You need to configure the operation types with Pismo. | minLength: 1; maxLength: 50 |
| `operation_value` | number (schema `OperationValue`) | no | Operation value. Must be positive or zero. Can be up to 16 digits and two decimal places.<br> | example: 234.5 |

<!-- schema: #/components/schemas/GetUniqueReceivableRequestParams -->
### Schema `GetUniqueReceivableRequestParams`

Pointer: `#/components/schemas/GetUniqueReceivableRequestParams`. Type: object (schema `GetUniqueReceivableRequestParams`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `debtor_document_number` | string (schema `DebtorDocumentNumber`) | yes | Debtor document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Must not be the same as the lender document number. <br> | maxLength: 14 |
| `face_value` | number (schema `FaceValue`) | yes | Face value refers to the nominal or stated value of a financial instrument or asset, typically printed or stated on the instrument itself. It represents the initial value assigned to the instrument at the time of issuance or purchase.<br> | example: 499.23 |
| `interop_holding_number` | string (schema `InteropHoldingNumber`) | yes | Client-assigned interoperation holding number. Called `holding_number` when passed in the Register receivable endpoint.<br> | example: "017917411A" |
| `lender_document_number` | string (schema `LenderDocumentNumber`) | yes | Lender document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Fisicas number (Brazil). Should not be the same as the debtor document number. <br> | example: "51407165000113" |
| `maturity_date` | string (schema `MaturityDate`) | yes | Maturity date. Format = yyyy-mm-dd. Must be equal to today or later. | example: "2023-06=22" |

## Lifecycle status

- `GET /v1/credit-rights` (`get-receivable`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Credit_receivables.yaml` | tag `Receivable`: GET /v1/credit-rights, POST /v1/credit-rights, GET /v1/credit-rights/{internalNumber}, DELETE /v1/credit-rights/{internalNumber}, PATCH /v1/credit-rights/{internalNumber}, POST /v1/credit-rights/unicity | https://github.com/PismoDevEx/pismo-api-specs | `eb38b8a710548b18…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-depositary` — Event catalogue: depositary
- `KU-EVT-depositary-data-events` — Banking - Credit receivables
