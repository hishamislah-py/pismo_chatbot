---
ku_id: KU-API-banking-assets--assets
title: 'API reference: Banking - Assets — Assets'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Assets.yaml
  sha256: 4571af460975f34c49953e1f6b989175441ee84e84142cca7450503fba10458b
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
- AssetRegistration
- AssetbyId
- AssetCancellation
- UpdateAsset
- AssetRedemptionV2
- AssetRedemption
- AssetBalance
- AssetBlock
- postAssetBlock
related_kus:
- KU-EVT-assets-data-events
- KU-EVT-catalogue-assets
specification_version: 1.0.0
---

# API reference: Banking - Assets — Assets

**KU ID:** `KU-API-banking-assets--assets` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 9 operation(s) tagged `Assets` in `api-specs/Banking_-_Assets.yaml` (“Banking - Assets”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Asset endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/issuer/{issuer_id}/assets` | `AssetRegistration` | Register banking asset | no |
| `GET /v1/issuer/{issuer_id}/assets/{asset_id}` | `AssetbyId` | Get banking asset | no |
| `DELETE /v1/issuer/{issuer_id}/assets/{asset_id}` | `AssetCancellation` | Delete banking asset | no |
| `PATCH /v1/issuer/{issuer_id}/assets/{asset_id}` | `UpdateAsset` | Update banking asset | no |
| `PUT /v2/issuer/{issuer_id}/assets/{asset_id}/redemption` | `AssetRedemptionV2` | Create banking asset redemption | no |
| `GET /v1/issuer/{issuer_id}/assets/{asset_id}/redemption` | `AssetRedemption` | List banking asset redemptions | no |
| `GET /v1/issuer/{issuer_id}/assets/{asset_id}/balance` | `AssetBalance` | Get banking asset balance | no |
| `POST /v1/issuer/{issuer_id}/assets/{asset_id}/block` | `AssetBlock` | Block/unblock banking asset | no |
| `POST /v1/issuer/{issuer_id}/assets/{asset_id}/migrate` | `postAssetBlock` | Migrate banking asset | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Assets.yaml method=POST path=/v1/issuer/{issuer_id}/assets operationId=AssetRegistration -->
### `POST /v1/issuer/{issuer_id}/assets` — Register banking asset

- **operationId:** `AssetRegistration`
- **Specification:** `api-specs/Banking_-_Assets.yaml` (Banking - Assets)
- **Server base URL(s):** `https://sandbox.pismolabs.io/assets-accrual`, `https://sandbox.pismolabs.io/assets-accrual`, `https://api.pismolabs.io/assets-accrual`
- **Tags:** `Assets`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a banking asset with the Pismo platform. A banking asset is either a certificate of deposit or a bank receipt.
>
> This endpoint generates an [Asset registration succeeded](https://developers.pismo.io/events/docs/assets-asset-registration-success-1) event if it succeeds or an [Asset registration failed](https://developers.pismo.io/events/docs/assets-asset-registration-failure-1) event if it doesn't.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `issuer_id` | path | yes | string | Issuer ID. For more information, refer to [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp) | example: "24" |

#### Request body

Required: yes

> Requested body of authorization

**Content type `application/json`** — schema: object (schema `AssetRegistration`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `asset_id` | string (schema `AssetID`) | yes | Asset ID. This ID is client-generated. It must be between 1 and 128 characters long and consist of only the characters [a-z,A-Z,0-9,-,:]. | minLength: 1; maxLength: 128; example: "6ea8094b-73ba-4737-93ad-370c27c54813" |
| `registration_mode` | string (schema `RegistrationMode`) | yes | Registration mode — `single` or `many` | enum: ["single", "many"]; example: "single" |
| `asset_type` | string (schema `AssetType`) | yes | Asset type, `cdb` (certificate of deposit) or `rdb` (bank deposit receipt) | enum: ["cdb", "rdb"]; example: "cdb" |
| `issuing_date` | string (schema `IssuingDate`) | yes | Issuing date, format = yyyy/mm/dd. | example: "2023/03/22" |
| `maturity_date` | string (schema `MaturityDate`) | yes | Asset maturity date, format = yyyy/mm/dd. | example: "2023/03/22" |
| `issued_units` | integer (schema `IssuedUnits`) | yes | Number of issued units | format: "int32"; example: 10 |
| `unit_value` | number (schema `UnitValue`) | yes | Per unit value | format: "double"; example: 65.56 |
| `index_type` | string (schema `IndexType`) | yes | Index type:<br>* `di` — DI rate is the average rate of interbank transactions carried out through interbank certificates of deposits. It is calculated based on fixed interbank deposits transactions settled within one business day.<br>* `ipca` — The Extended National Consumer Price Index (IPCA) is the reference for the Brazilian inflation-targeting system. The Banco Central do Brasil (BCB) works to ensure that the IPCA's annual inflation is centered at the inflation target set by the National Monetary Council (CMN). The IPCA is also the price index of the National Treasury's Notes Series B (NTN-B).  <br>* `pre` — Use when there is a tax defined for the asset.<br> | enum: ["di", "pre", "ipca"]; example: "pre" |
| `index_rate` | number (schema `IndexRate`) | yes | Index rate | format: "double"; example: 2 |
| `customer_type` | string (schema `CustomerType`) | yes | Customer type - `natural` or `legal`. A `natural` customer is an individual, a `legal` customer is a corporation or other legal entitiy type. | enum: ["natural", "legal"]; example: "natural" |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a social security number (US). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `deposit_number` | integer (schema `DepositNumber`) | yes | Deposit number | format: "int32"; example: 567339022 |
| `early_redemption_terms` | string (schema `EarlyRedemptionTerms`) | yes | Early redemption terms:<br>* `yes` — Has early redemption terms<br>* `no` — Does not have early redemption terms<br>* `market` — Redeem at market<br> | enum: ["yes", "no", "market"]; example: "market" |
| `currency` | string (schema `Currency`) | yes | 1SO 4217 currency code | example: "986" |
| `customer_name` | string (schema `CustomerName`) | no | Customer name - max length is 128 chars | minLength: 1; maxLength: 128; example: "Bud Whyser" |
| `purchased_units` | integer (schema `PurchasedUnits`) | no | Number of purchased units | format: "int32"; example: 20 |
| `additional_data` | object (schema `AdditionalData`) | no |  | example: {"early_redemption_attributes": [{"date": "2021-02-01", "interest_rate": 1.09, "floating_rate": 1.18}, {"date": "2021-03-01", "interest_rate": 100000000000001.1, "floating_rate": 1.15}]} |
| `external_id` | string (schema `ExternalID`) | no | Client-provided external asset ID. No longer than 128 alphanumeric characters. | minLength: 0; maxLength: 128; example: "93830-FFFF-84940" |
| `accrual_frequency` | string (schema `AccrualFrequency`) | no | Accrual frequency:<br>* `daily` — Accrual for assets daily<br>* `monthly` — Accrual for assets monthly<br> | enum: ["daily", "monthly"]; example: "daily" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | OK | `application/json`: object (schema `AssetRegistrationResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `asset_id` | string (schema `AssetID`) | yes | Asset ID. This ID is client-generated. It must be between 1 and 128 characters long and consist of only the characters [a-z,A-Z,0-9,-,:]. | minLength: 1; maxLength: 128; example: "6ea8094b-73ba-4737-93ad-370c27c54813" |
| `message` | string (schema `Message`) | yes | Message about asset/quote operation | minLength: 0; maxLength: 128; example: "Message about request operation" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `assets-asset-registration-failure-1` | https://developers.pismo.io/events/docs/assets-asset-registration-failure-1 |
| `assets-asset-registration-success-1` | https://developers.pismo.io/events/docs/assets-asset-registration-success-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;404;500`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-assets-data-events`.

<!-- op: spec=api-specs/Banking_-_Assets.yaml method=GET path=/v1/issuer/{issuer_id}/assets/{asset_id} operationId=AssetbyId -->
### `GET /v1/issuer/{issuer_id}/assets/{asset_id}` — Get banking asset

- **operationId:** `AssetbyId`
- **Specification:** `api-specs/Banking_-_Assets.yaml` (Banking - Assets)
- **Server base URL(s):** `https://sandbox.pismolabs.io/assets-accrual`, `https://sandbox.pismolabs.io/assets-accrual`, `https://api.pismolabs.io/assets-accrual`
- **Tags:** `Assets`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get banking asset using issuer and asset IDs

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `issuer_id` | path | yes | string | Issuer ID. For more information, refer to [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp) | example: "24" |
| `asset_id` | path | yes | string | Client assigned asset ID. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br> | example: "2345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `Asset`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `asset_id` | string (schema `AssetID`) | yes | Asset ID. This ID is client-generated. It must be between 1 and 128 characters long and consist of only the characters [a-z,A-Z,0-9,-,:]. | minLength: 1; maxLength: 128; example: "6ea8094b-73ba-4737-93ad-370c27c54813" |
| `asset_type` | string (schema `AssetType`) | yes | Asset type, `cdb` (certificate of deposit) or `rdb` (bank deposit receipt) | enum: ["cdb", "rdb"]; example: "cdb" |
| `registration_mode` | string (schema `RegistrationMode`) | yes | Registration mode — `single` or `many` | enum: ["single", "many"]; example: "single" |
| `issuing_date` | string (schema `IssuingDate`) | yes | Issuing date, format = yyyy/mm/dd. | example: "2023/03/22" |
| `maturity_date` | string (schema `MaturityDate`) | yes | Asset maturity date, format = yyyy/mm/dd. | example: "2023/03/22" |
| `issued_units` | integer (schema `IssuedUnits`) | yes | Number of issued units | format: "int32"; example: 10 |
| `unit_value` | number (schema `UnitValue`) | yes | Per unit value | format: "double"; example: 65.56 |
| `index_type` | string (schema `IndexType`) | yes | Index type:<br>* `di` — DI rate is the average rate of interbank transactions carried out through interbank certificates of deposits. It is calculated based on fixed interbank deposits transactions settled within one business day.<br>* `ipca` — The Extended National Consumer Price Index (IPCA) is the reference for the Brazilian inflation-targeting system. The Banco Central do Brasil (BCB) works to ensure that the IPCA's annual inflation is centered at the inflation target set by the National Monetary Council (CMN). The IPCA is also the price index of the National Treasury's Notes Series B (NTN-B).  <br>* `pre` — Use when there is a tax defined for the asset.<br> | enum: ["di", "pre", "ipca"]; example: "pre" |
| `index_rate` | number (schema `IndexRate`) | yes | Index rate | format: "double"; example: 2 |
| `currency` | string (schema `Currency`) | yes | 1SO 4217 currency code | example: "986" |
| `status` | string (schema `Status`) | no | Asset status | enum: ["ACTIVE", "BLOCKED", "PENDING", "CANCELED", "COMPLETED", "REDEEMED"]; example: "ACTIVE" |
| `issuer_id` | string (schema `IssuerID`) | no | Issuer ID. For more information, see [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp)<br> | example: "98400-0-0d" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (UTC) asset registered on Pismo platform | example: "2023-03-30T12:26:41" |
| `updated_at` | string (schema `UpdatedAt`) | no | Date/time (UTC) asset last updated on Pismo platform | example: "2023-03-30T12:26:41" |
| `interest_rate` | number (schema `InterestRate`) | no | Interest rate | format: "double"; example: 2.3 |
| `additional_data` | object (schema `AdditionalData`) | no |  | example: {"early_redemption_attributes": [{"date": "2021-02-01", "interest_rate": 1.09, "floating_rate": 1.18}, {"date": "2021-03-01", "interest_rate": 100000000000001.1, "floating_rate": 1.15}]} |
| `external_id` | string (schema `ExternalID`) | no | Client-provided external asset ID. No longer than 128 alphanumeric characters. | minLength: 0; maxLength: 128; example: "93830-FFFF-84940" |
| `accrual_frequency` | string (schema `AccrualFrequency`) | no | Accrual frequency:<br>* `daily` — Accrual for assets daily<br>* `monthly` — Accrual for assets monthly<br> | enum: ["daily", "monthly"]; example: "daily" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Assets.yaml method=DELETE path=/v1/issuer/{issuer_id}/assets/{asset_id} operationId=AssetCancellation -->
### `DELETE /v1/issuer/{issuer_id}/assets/{asset_id}` — Delete banking asset

- **operationId:** `AssetCancellation`
- **Specification:** `api-specs/Banking_-_Assets.yaml` (Banking - Assets)
- **Server base URL(s):** `https://sandbox.pismolabs.io/assets-accrual`, `https://sandbox.pismolabs.io/assets-accrual`, `https://api.pismolabs.io/assets-accrual`
- **Tags:** `Assets`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete a banking asset previously registered with the Pismo platform
>
> This endpoint generates an [Asset status changed](https://developers.pismo.io/events/docs/assets-asset-status-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `issuer_id` | path | yes | string | Issuer ID. For more information, refer to [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp) | example: "24" |
| `asset_id` | path | yes | string | Client assigned asset ID. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br> | example: "2345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `Asset`) |
| 400 | Bad Request |  |
| 401 | Unauthorized |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `asset_id` | string (schema `AssetID`) | yes | Asset ID. This ID is client-generated. It must be between 1 and 128 characters long and consist of only the characters [a-z,A-Z,0-9,-,:]. | minLength: 1; maxLength: 128; example: "6ea8094b-73ba-4737-93ad-370c27c54813" |
| `asset_type` | string (schema `AssetType`) | yes | Asset type, `cdb` (certificate of deposit) or `rdb` (bank deposit receipt) | enum: ["cdb", "rdb"]; example: "cdb" |
| `registration_mode` | string (schema `RegistrationMode`) | yes | Registration mode — `single` or `many` | enum: ["single", "many"]; example: "single" |
| `issuing_date` | string (schema `IssuingDate`) | yes | Issuing date, format = yyyy/mm/dd. | example: "2023/03/22" |
| `maturity_date` | string (schema `MaturityDate`) | yes | Asset maturity date, format = yyyy/mm/dd. | example: "2023/03/22" |
| `issued_units` | integer (schema `IssuedUnits`) | yes | Number of issued units | format: "int32"; example: 10 |
| `unit_value` | number (schema `UnitValue`) | yes | Per unit value | format: "double"; example: 65.56 |
| `index_type` | string (schema `IndexType`) | yes | Index type:<br>* `di` — DI rate is the average rate of interbank transactions carried out through interbank certificates of deposits. It is calculated based on fixed interbank deposits transactions settled within one business day.<br>* `ipca` — The Extended National Consumer Price Index (IPCA) is the reference for the Brazilian inflation-targeting system. The Banco Central do Brasil (BCB) works to ensure that the IPCA's annual inflation is centered at the inflation target set by the National Monetary Council (CMN). The IPCA is also the price index of the National Treasury's Notes Series B (NTN-B).  <br>* `pre` — Use when there is a tax defined for the asset.<br> | enum: ["di", "pre", "ipca"]; example: "pre" |
| `index_rate` | number (schema `IndexRate`) | yes | Index rate | format: "double"; example: 2 |
| `currency` | string (schema `Currency`) | yes | 1SO 4217 currency code | example: "986" |
| `status` | string (schema `Status`) | no | Asset status | enum: ["ACTIVE", "BLOCKED", "PENDING", "CANCELED", "COMPLETED", "REDEEMED"]; example: "ACTIVE" |
| `issuer_id` | string (schema `IssuerID`) | no | Issuer ID. For more information, see [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp)<br> | example: "98400-0-0d" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (UTC) asset registered on Pismo platform | example: "2023-03-30T12:26:41" |
| `updated_at` | string (schema `UpdatedAt`) | no | Date/time (UTC) asset last updated on Pismo platform | example: "2023-03-30T12:26:41" |
| `interest_rate` | number (schema `InterestRate`) | no | Interest rate | format: "double"; example: 2.3 |
| `additional_data` | object (schema `AdditionalData`) | no |  | example: {"early_redemption_attributes": [{"date": "2021-02-01", "interest_rate": 1.09, "floating_rate": 1.18}, {"date": "2021-03-01", "interest_rate": 100000000000001.1, "floating_rate": 1.15}]} |
| `external_id` | string (schema `ExternalID`) | no | Client-provided external asset ID. No longer than 128 alphanumeric characters. | minLength: 0; maxLength: 128; example: "93830-FFFF-84940" |
| `accrual_frequency` | string (schema `AccrualFrequency`) | no | Accrual frequency:<br>* `daily` — Accrual for assets daily<br>* `monthly` — Accrual for assets monthly<br> | enum: ["daily", "monthly"]; example: "daily" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `assets-asset-status-change-1` | https://developers.pismo.io/events/docs/assets-asset-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-assets-data-events`.

<!-- op: spec=api-specs/Banking_-_Assets.yaml method=PATCH path=/v1/issuer/{issuer_id}/assets/{asset_id} operationId=UpdateAsset -->
### `PATCH /v1/issuer/{issuer_id}/assets/{asset_id}` — Update banking asset

- **operationId:** `UpdateAsset`
- **Specification:** `api-specs/Banking_-_Assets.yaml` (Banking - Assets)
- **Server base URL(s):** `https://sandbox.pismolabs.io/assets-accrual`, `https://sandbox.pismolabs.io/assets-accrual`, `https://api.pismolabs.io/assets-accrual`
- **Tags:** `Assets`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a banking asset using issuer and asset IDs
>
> This endpoint generates an [Asset updated](https://developers.pismo.io/events/docs/assets-asset-update-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `issuer_id` | path | yes | string | Issuer ID. For more information, refer to [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp) | example: "24" |
| `asset_id` | path | yes | string | Client assigned asset ID. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br> | example: "2345" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `UpdateAsset`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `operation_type` | string (schema `OperationType`) | yes | Quota operation type. Must be `amendment` (update quota). | enum: ["amendment"] |
| `early_redemption_terms` | string (schema `EarlyRedemptionTerms`) | no | Early redemption terms:<br>* `yes` — Has early redemption terms<br>* `no` — Does not have early redemption terms<br>* `market` — Redeem at market<br> | enum: ["yes", "no", "market"]; example: "market" |
| `additional_data` | object (schema `AdditionalData`) | no |  | example: {"early_redemption_attributes": [{"date": "2021-02-01", "interest_rate": 1.09, "floating_rate": 1.18}, {"date": "2021-03-01", "interest_rate": 100000000000001.1, "floating_rate": 1.15}]} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AssetUpdateResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `asset_id` | string (schema `AssetID`) | no | Asset ID. This ID is client-generated. It must be between 1 and 128 characters long and consist of only the characters [a-z,A-Z,0-9,-,:]. | minLength: 1; maxLength: 128; example: "6ea8094b-73ba-4737-93ad-370c27c54813" |
| `asset_type` | string (schema `AssetType`) | no | Asset type, `cdb` (certificate of deposit) or `rdb` (bank deposit receipt) | enum: ["cdb", "rdb"]; example: "cdb" |
| `issuer_id` | string (schema `IssuerID`) | no | Issuer ID. For more information, see [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp)<br> | example: "98400-0-0d" |
| `isin_code` | string (schema `IsinCode`) | no | An International Securities Identification Number (ISIN) uniquely identifies a security. Its structure is defined in ISO 6166. The ISIN code is a 12-character alphanumeric code that serves for uniform identification of a security through normalization of the assigned National Number, where one exists, at trading and settlement. <br> | example: "isin12341234" |
| `registration_mode` | string (schema `RegistrationMode`) | no | Registration mode — `single` or `many` | enum: ["single", "many"]; example: "single" |
| `issuing_date` | string (schema `IssuingDate`) | no | Issuing date, format = yyyy/mm/dd. | example: "2023/03/22" |
| `maturity_date` | string (schema `MaturityDate`) | no | Asset maturity date, format = yyyy/mm/dd. | example: "2023/03/22" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (UTC) asset registered on Pismo platform | example: "2023-03-30T12:26:41" |
| `updated_at` | string (schema `UpdatedAt`) | no | Date/time (UTC) asset last updated on Pismo platform | example: "2023-03-30T12:26:41" |
| `issued_units` | integer (schema `IssuedUnits`) | no | Number of issued units | format: "int32"; example: 10 |
| `unit_value` | number (schema `UnitValue`) | no | Per unit value | format: "double"; example: 65.56 |
| `index_type` | string (schema `IndexType`) | no | Index type:<br>* `di` — DI rate is the average rate of interbank transactions carried out through interbank certificates of deposits. It is calculated based on fixed interbank deposits transactions settled within one business day.<br>* `ipca` — The Extended National Consumer Price Index (IPCA) is the reference for the Brazilian inflation-targeting system. The Banco Central do Brasil (BCB) works to ensure that the IPCA's annual inflation is centered at the inflation target set by the National Monetary Council (CMN). The IPCA is also the price index of the National Treasury's Notes Series B (NTN-B).  <br>* `pre` — Use when there is a tax defined for the asset.<br> | enum: ["di", "pre", "ipca"]; example: "pre" |
| `index_rate` | number (schema `IndexRate`) | no | Index rate | format: "double"; example: 2 |
| `status` | string (schema `Status`) | no | Asset status | enum: ["ACTIVE", "BLOCKED", "PENDING", "CANCELED", "COMPLETED", "REDEEMED"]; example: "ACTIVE" |
| `currency` | string (schema `Currency`) | no | 1SO 4217 currency code | example: "986" |
| `early_redemption_terms` | string (schema `EarlyRedemptionTerms`) | no | Early redemption terms:<br>* `yes` — Has early redemption terms<br>* `no` — Does not have early redemption terms<br>* `market` — Redeem at market<br> | enum: ["yes", "no", "market"]; example: "market" |
| `interest_rate` | number (schema `InterestRate`) | no | Interest rate | format: "double"; example: 2.3 |
| `additional_data` | object (schema `AdditionalData`) | no |  | example: {"early_redemption_attributes": [{"date": "2021-02-01", "interest_rate": 1.09, "floating_rate": 1.18}, {"date": "2021-03-01", "interest_rate": 100000000000001.1, "floating_rate": 1.15}]} |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `assets-asset-update-1` | https://developers.pismo.io/events/docs/assets-asset-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-assets-data-events`.

<!-- op: spec=api-specs/Banking_-_Assets.yaml method=PUT path=/v2/issuer/{issuer_id}/assets/{asset_id}/redemption operationId=AssetRedemptionV2 -->
### `PUT /v2/issuer/{issuer_id}/assets/{asset_id}/redemption` — Create banking asset redemption

- **operationId:** `AssetRedemptionV2`
- **Specification:** `api-specs/Banking_-_Assets.yaml` (Banking - Assets)
- **Server base URL(s):** `https://sandbox.pismolabs.io/assets-accrual`, `https://sandbox.pismolabs.io/assets-accrual`, `https://api.pismolabs.io/assets-accrual`
- **Tags:** `Assets`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a banking asset redemption. A banking asset redemption is the repayment of the original value of the asset to the investor.
>
> If the request succeeds, this endpoint generates an [Asset redeemed](https://developers.pismo.io/events/docs/assets-asset-redemption-1) event and an [Asset status changed](https://developers.pismo.io/events/docs/assets-asset-status-change-1) event.
> If it fails, it generates an [Asset redemption failed](https://developers.pismo.io/events/docs/assets-asset-redemption-failure-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `issuer_id` | path | yes | string | Issuer ID. For more information, refer to [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp) | example: "24" |
| `asset_id` | path | yes | string | Client assigned asset ID. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br> | example: "2345" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `AssetRedemption`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `units` | integer (schema `Units`) | yes | Number of asset units | format: "int32"; example: 20 |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a social security number (US). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `external_id` | string (schema `ExternalID`) | yes | Client-provided external asset ID. No longer than 128 alphanumeric characters. | minLength: 0; maxLength: 128; example: "93830-FFFF-84940" |
| `redemption_date` | string (schema `RedemptionDate`) | no | Redemption date, format = yyyy/mm/dd | example: "2023/03/30" |
| `deposit_number` | integer (schema `DepositNumber`) | no | Deposit number | format: "int32"; example: 567339022 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | OK | `application/json`: object (schema `AssetRegistrationResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `asset_id` | string (schema `AssetID`) | yes | Asset ID. This ID is client-generated. It must be between 1 and 128 characters long and consist of only the characters [a-z,A-Z,0-9,-,:]. | minLength: 1; maxLength: 128; example: "6ea8094b-73ba-4737-93ad-370c27c54813" |
| `message` | string (schema `Message`) | yes | Message about asset/quote operation | minLength: 0; maxLength: 128; example: "Message about request operation" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `assets-asset-redemption-1` | https://developers.pismo.io/events/docs/assets-asset-redemption-1 |
| `assets-asset-redemption-failure-1` | https://developers.pismo.io/events/docs/assets-asset-redemption-failure-1 |
| `assets-asset-status-change-1` | https://developers.pismo.io/events/docs/assets-asset-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;404;500`, has examples `False`, emits events `3`, deprecated `False`.

Guides that link to this operation: `KU-EVT-assets-data-events`.

<!-- op: spec=api-specs/Banking_-_Assets.yaml method=GET path=/v1/issuer/{issuer_id}/assets/{asset_id}/redemption operationId=AssetRedemption -->
### `GET /v1/issuer/{issuer_id}/assets/{asset_id}/redemption` — List banking asset redemptions

- **operationId:** `AssetRedemption`
- **Specification:** `api-specs/Banking_-_Assets.yaml` (Banking - Assets)
- **Server base URL(s):** `https://sandbox.pismolabs.io/assets-accrual`, `https://sandbox.pismolabs.io/assets-accrual`, `https://api.pismolabs.io/assets-accrual`
- **Tags:** `Assets`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List banking asset redemptions using asset and issuer IDs

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `issuer_id` | path | yes | string | Issuer ID. For more information, refer to [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp) | example: "24" |
| `page` | query | yes | integer | Page number, default is 1. | format: "int32"; example: 1 |
| `perPage` | query | yes | integer | Number of items per page, default is 10. | format: "int32"; example: 10 |
| `asset_id` | path | yes | string | Client assigned asset ID. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br> | example: "2345" |
| `externalId` | query | yes | string | Client-provided external asset ID. No longer than 128 alphanumeric characters. | example: "3456" |
| `beginDate` | query | no | string | Date asset was issued | format: "date"; example: "2023-01-10" |
| `endDate` | query | no | string | Date asset was redeemed, format = yyyy-mm-dd. | format: "date"; example: "2023-01-10" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AssetRedemptionsResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | number (schema `CurrentPage`) | no | Current page | example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Number of items per page, default is 10. | format: "Int32"; example: 1 |
| `pages` | integer (schema `Pages`) | no | Total number of pages, default is 1. | format: "Int32"; example: 1 |
| `total_items` | number (schema `TotalItems`) | no | Total number of items | example: 1 |
| `items` | array of object | no |  |  |
| `items[].redemption_id` | string (schema `RedemptionID`) | no | Redemption ID | example: "d72a234c-9cbe-4ad0-9b7c-8dd18e958bc0" |
| `items[].asset_id` | string (schema `AssetID`) | no | Asset ID. This ID is client-generated. It must be between 1 and 128 characters long and consist of only the characters [a-z,A-Z,0-9,-,:]. | minLength: 1; maxLength: 128; example: "6ea8094b-73ba-4737-93ad-370c27c54813" |
| `items[].issuer_id` | string (schema `IssuerID`) | no | Issuer ID. For more information, see [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp)<br> | example: "98400-0-0d" |
| `items[].document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a social security number (US). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `items[].deposit_number` | integer (schema `DepositNumber`) | no | Deposit number | format: "int32"; example: 567339022 |
| `items[].redeemed_units` | number (schema `RedeemedUnits`) | no | Number of redeemed units | example: 10 |
| `items[].currency` | string (schema `Currency`) | no | 1SO 4217 currency code | example: "986" |
| `items[].redemption_date` | string (schema `RedemptionDate`) | no | Redemption date, format = yyyy/mm/dd | example: "2023/03/30" |
| `items[].created_at` | string (schema `CreatedAt`) | no | Date/time (UTC) asset registered on Pismo platform | example: "2023-03-30T12:26:41" |
| `items[].external_id` | string (schema `ExternalID`) | no | Client-provided external asset ID. No longer than 128 alphanumeric characters. | minLength: 0; maxLength: 128; example: "93830-FFFF-84940" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Assets.yaml method=GET path=/v1/issuer/{issuer_id}/assets/{asset_id}/balance operationId=AssetBalance -->
### `GET /v1/issuer/{issuer_id}/assets/{asset_id}/balance` — Get banking asset balance

- **operationId:** `AssetBalance`
- **Specification:** `api-specs/Banking_-_Assets.yaml` (Banking - Assets)
- **Server base URL(s):** `https://sandbox.pismolabs.io/assets-accrual`, `https://sandbox.pismolabs.io/assets-accrual`, `https://api.pismolabs.io/assets-accrual`
- **Tags:** `Assets`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get banking asset balance using asset ID

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `issuer_id` | path | yes | string | Issuer ID. For more information, refer to [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp) | example: "24" |
| `asset_id` | path | yes | string | Client assigned asset ID. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br> | example: "2345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AssetBalance`) |
| 400 | Bad Request |  |
| 401 | Unauthorized |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `units` | integer (schema `Units`) | no | Number of asset units | format: "int32"; example: 20 |
| `redeemed_units` | number (schema `RedeemedUnits`) | no | Number of redeemed units | example: 10 |
| `units_available` | number (schema `UnitsAvailable`) | no | total units available after redemption operation | format: "integer"; example: 3000 |
| `latest_accrual_date` | string (schema `LatestAccrualDate`) | no | Latest accrual date, format = yyyy/mm/dd. | example: "2023/03/22" |
| `daily_rate` | number (schema `DailyRate`) | no | Daily rate | format: "double"; example: 1.2 |
| `accum_daily_rate` | number (schema `AccumDailyRate`) | no | Accumulative daily rate | format: "double"; example: 1.2 |
| `factor` | string (schema `Factor`) | no | Calculated pre-rate factor based on how many days the asset has accrued (base unit value x factor = new unit value accrued). The pre-rate factor is used to calculate how much ROI the customer can expect to receive.<br> |  |
| `unit_value` | number (schema `UnitValue`) | no | Per unit value | format: "double"; example: 65.56 |
| `current_amount` | number (schema `CurrentAmount`) | no | Current amount | format: "double"; example: 45.8 |
| `currency` | string (schema `Currency`) | no | 1SO 4217 currency code | example: "986" |
| `status` | string (schema `Status`) | no | Asset status | enum: ["ACTIVE", "BLOCKED", "PENDING", "CANCELED", "COMPLETED", "REDEEMED"]; example: "ACTIVE" |
| `position_date` | string (schema `PositionDate`) | no | Updated position date, format = yyyy/mm/dd. | example: "2023-03-22" |
| `accrual_frequency` | string (schema `AccrualFrequency`) | no | Accrual frequency:<br>* `daily` — Accrual for assets daily<br>* `monthly` — Accrual for assets monthly<br> | enum: ["daily", "monthly"]; example: "daily" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Assets.yaml method=POST path=/v1/issuer/{issuer_id}/assets/{asset_id}/block operationId=AssetBlock -->
### `POST /v1/issuer/{issuer_id}/assets/{asset_id}/block` — Block/unblock banking asset

- **operationId:** `AssetBlock`
- **Specification:** `api-specs/Banking_-_Assets.yaml` (Banking - Assets)
- **Server base URL(s):** `https://sandbox.pismolabs.io/assets-accrual`, `https://sandbox.pismolabs.io/assets-accrual`, `https://api.pismolabs.io/assets-accrual`
- **Tags:** `Assets`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Block or unblock a banking asset
>
> If the request succeeds, this endpoint generates an [Asset blocked](https://developers.pismo.io/events/docs/assets-asset-block-1) event;
> otherwise, generates an [Asset block failed](https://developers.pismo.io/events/docs/assets-asset-block-failure-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `issuer_id` | path | yes | string | Issuer ID. For more information, refer to [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp) | example: "24" |
| `asset_id` | path | yes | string | Client assigned asset ID. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br> | example: "2345" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `AssetBlock`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `units` | integer (schema `Units`) | yes | Number of asset units | format: "int32"; example: 20 |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a social security number (US). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `status` | string (schema `AssetBlockStatus`) | no | Asset block status | enum: ["BLOCK", "UNBLOCK"]; example: "BLOCK" |
| `external_id` | string (schema `ExternalID`) | no | Client-provided external asset ID. No longer than 128 alphanumeric characters. | minLength: 0; maxLength: 128; example: "93830-FFFF-84940" |
| `reason` | string (schema `BlockedReason`) | no | Reason asset was blocked | minLength: 0; maxLength: 64; example: "Delinquent account" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | ACCEPTED | `application/json`: (type not declared) (schema `202AssetBlockedResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 202

**202 `application/json` body fields:**

_No fields declared in the schema._


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `assets-asset-block-1` | https://developers.pismo.io/events/docs/assets-asset-block-1 |
| `assets-asset-block-failure-1` | https://developers.pismo.io/events/docs/assets-asset-block-failure-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;404;500`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-assets-data-events`.

<!-- op: spec=api-specs/Banking_-_Assets.yaml method=POST path=/v1/issuer/{issuer_id}/assets/{asset_id}/migrate operationId=postAssetBlock -->
### `POST /v1/issuer/{issuer_id}/assets/{asset_id}/migrate` — Migrate banking asset

- **operationId:** `postAssetBlock`
- **Specification:** `api-specs/Banking_-_Assets.yaml` (Banking - Assets)
- **Server base URL(s):** `https://sandbox.pismolabs.io/assets-accrual`, `https://sandbox.pismolabs.io/assets-accrual`, `https://api.pismolabs.io/assets-accrual`
- **Tags:** `Assets`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Migrate banking asset
>
> If the request succeeds, this endpoint generates an <a href="https://json-schemas.data.pismo.io/docs/assets/asset_block-1.html">asset_block-1</a> event.
> If it fails, it generates an <a href="https://json-schemas.data.pismo.io/docs/assets/asset_block_failure-1.html">asset_block_failure-1</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `issuer_id` | path | yes | string | Issuer ID. For more information, refer to [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp) | example: "24" |
| `asset_id` | path | yes | string | Client assigned asset ID. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br> | example: "2345" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `AssetMigrate`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `asset_type` | string (schema `AssetType`) | no | Asset type, `cdb` (certificate of deposit) or `rdb` (bank deposit receipt) | enum: ["cdb", "rdb"]; example: "cdb" |
| `document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a social security number (US). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `deposit_number` | integer (schema `DepositNumber`) | no | Deposit number | format: "int32"; example: 567339022 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | ACCEPTED | `application/json`: object |
| 400 | Bad Request |  |
| 401 | Unauthorized |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `asset_id` | string (schema `AssetID`) | no | Asset ID. This ID is client-generated. It must be between 1 and 128 characters long and consist of only the characters [a-z,A-Z,0-9,-,:]. | minLength: 1; maxLength: 128; example: "6ea8094b-73ba-4737-93ad-370c27c54813" |
| `message` | string (schema `Message`) | no | Message about asset/quote operation | minLength: 0; maxLength: 128; example: "Message about request operation" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AdditionalData -->
### Schema `AdditionalData`

Pointer: `#/components/schemas/AdditionalData`. Type: object (schema `AdditionalData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `early_redemption_attributes` | array of object (schema `EarlyRedemptionAttribute`) | no |  |  |

<!-- schema: #/components/schemas/EarlyRedemptionAttribute -->
### Schema `EarlyRedemptionAttribute`

Pointer: `#/components/schemas/EarlyRedemptionAttribute`. Type: object (schema `EarlyRedemptionAttribute`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `date` | string (schema `Date`) | no | Redemption date, format = yyyy/mm/dd. | example: "2023/03/22" |
| `interest_rate` | number (schema `InterestRate`) | no | Interest rate | format: "double"; example: 2.3 |
| `floating_rate` | number (schema `FloatingRate`) | no | Floating rate | format: "double"; example: 2.33 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Assets.yaml` | tag `Assets`: POST /v1/issuer/{issuer_id}/assets, GET /v1/issuer/{issuer_id}/assets/{asset_id}, DELETE /v1/issuer/{issuer_id}/assets/{asset_id}, PATCH /v1/issuer/{issuer_id}/assets/{asset_id}, PUT /v2/issuer/{issuer_id}/assets/{asset_id}/redemption, GET /v1/issuer/{issuer_id}/assets/{asset_id}/redemption, GET /v1/issuer/{issuer_id}/assets/{asset_id}/balance, POST /v1/issuer/{issuer_id}/assets/{asset_id}/block, POST /v1/issuer/{issuer_id}/assets/{asset_id}/migrate | https://github.com/PismoDevEx/pismo-api-specs | `4571af460975f34c…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-assets-data-events` — Banking - Assets
- `KU-EVT-catalogue-assets` — Event catalogue: assets
