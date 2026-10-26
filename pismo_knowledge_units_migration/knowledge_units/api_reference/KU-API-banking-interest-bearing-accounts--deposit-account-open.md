---
ku_id: KU-API-banking-interest-bearing-accounts--deposit-account-open
title: 'API reference: Banking - Interest-bearing accounts — Deposit account open'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Interest-bearing_accounts.yaml
  sha256: 89fc3f8ed0222a57b553ff94305ed0b9cb03db5dd58afd0c3f23ba1474ec87a2
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
- interest-bearing-v1-deposit-account-open
related_kus:
- KU-BANK-interest-bearing-accounts
- KU-ERR-codes-eibacc
- KU-EVT-catalogue-deposit
specification_version: 1.0.0
---

# API reference: Banking - Interest-bearing accounts — Deposit account open

**KU ID:** `KU-API-banking-interest-bearing-accounts--deposit-account-open` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Deposit account open` in `api-specs/Banking_-_Interest-bearing_accounts.yaml` (“Banking - Interest-bearing accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints that create deposit accounts and attach products in a single operation

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/deposits/accounts/open` | `interest-bearing-v1-deposit-account-open` | Open deposit account | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=POST path=/v1/deposits/accounts/open operationId=interest-bearing-v1-deposit-account-open -->
### `POST /v1/deposits/accounts/open` — Open deposit account

- **operationId:** `interest-bearing-v1-deposit-account-open`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Deposit account open`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates or locates a transaction banking account and attaches a validated deposit product in a single request. When the operation succeeds, the Pismo platform generates the [Deposit account opened](https://developers.pismo.io/events/docs/deposit-product-deposit-account-opened-1) and [Account attached](https://developers.pismo.io/events/docs/deposit-product-account-attach-1) events.
>
> This endpoint supports two scenarios:
>
> * **Existing account**: Provide both `account.account_id` and `account.external_account_id`. The Pismo platform locates the account via the transaction banking API and validates the IDs. If there is a mismatch, the request fails with a `400` error.
>
> * **New account**: Provide `account.external_account_id` and the `account_creation` object. The Pismo platform creates a new transaction banking account and attaches the deposit product. If the transaction banking API returns `409` because the account already exists, the Pismo platform locates the existing account and proceeds with product attachment.
>
> **Note**: The deposit product must exist, be of type `deposit`, and have an `ACTIVE` status.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `UnifiedDepositOpenRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account` | object (schema `UnifiedOpenAccount`) | yes | Identifies the account to which the deposit product is attached |  |
| `deposit_attachment` | object (schema `UnifiedOpenDepositAttachment`) | yes | Deposit product attachment configuration |  |
| `account_creation` | object (schema `UnifiedOpenAccountCreation`) | no | Account creation parameters. Required when `account.account_id` is not provided.<br>Pismo platform uses these fields to create a new transaction banking account via the transaction banking API.<br> |  |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that provide additional context or custom information.<br><br>Metadata content is not controlled by the Pismo platform and is instead controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"key": "value"} |

Example `newAccount` (Create new account and attach deposit):

```json
{
  "account": {
    "external_account_id": "ext-acct-001"
  },
  "account_creation": {
    "program_id": 100,
    "currency_code": "USD",
    "division_code": "001",
    "applicant": {
      "document_number": "12345678900",
      "name": "John Doe"
    }
  },
  "deposit_attachment": {
    "product_id": "2c336e9d-d04f-4fd0-8f6e-25808f48d70c",
    "deposit_configs": {
      "maturity_period": {
        "unit": "MONTHS",
        "value": 6
      }
    }
  },
  "metadata": {
    "source": "mobile-app"
  }
}
```

Example `existingAccount` (Attach deposit to existing account):

```json
{
  "account": {
    "account_id": 123456,
    "external_account_id": "ext-acct-001"
  },
  "deposit_attachment": {
    "product_id": "2c336e9d-d04f-4fd0-8f6e-25808f48d70c",
    "deposit_configs": {
      "maturity_period": {
        "calendar_maturity_date": "2027-06-15"
      }
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Deposit account opened successfully | `application/json`: object (schema `UnifiedDepositOpenResponse`) |
| 400 | Bad Request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 403 | Forbidden | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 422 | Unprocessable Entity | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 502 | Bad Gateway | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 504 | Gateway Timeout | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | Pismo account ID (new or existing) | format: "int64"; example: 123456 |
| `external_account_id` | string | no | External account ID | example: "ext-acct-001" |
| `product_id` | string | no | Product ID of the attached deposit product | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `deposit_configs` | object | no | Deposit configuration after attachment |  |
| `deposit_configs.maturity_period` | object (schema `MaturityPeriod`) | no | Defines when the deposit matures. There are three usage modes:<br><br>* **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).<br>* **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).<br>* **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.<br><br>**NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.<br><br>In the **attach** endpoints, the response returns exactly what was sent in the request:<br>* Send `unit` + `value` returns `unit` + `value`<br>* Send `calendar_maturity_date` returns `calendar_maturity_date`<br>* Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`<br><br>**NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.<br> |  |
| `deposit_configs.renewal_term` | object | no | Renewal term configuration, present only when the override includes a renewal term. |  |
| `deposit_configs.renewal_term.unit` | string (schema `MaturityPeriodUnit`) | no | Time unit for the relative maturity period. It's used together with `value` and cannot coincide with `calendar_maturity_date`.<br><br>- `DAYS`: Uses `value` directly. Example: `value=90` → 90 days.<br>- `WEEKS`: Multiplies `value` by 7. Example: `value=4` → 28 days.<br>- `MONTHS`: Calculates calendar-month with end-of-month (EOM) clamping when the target day does not exist. Example: `2024-01-31` + 1 month = `2024-02-29` (leap year) or `2025-02-28` (non-leap year).<br>- `YEARS`: Calculates calendar-year, for example: `2024-02-29` + 1 year = `2025-02-28`. Note that there is no Feb 29 in 2025.<br><br>For `WEEKS`, `MONTHS`, and `YEARS`, the resulting calendar date is converted back to a day count to validate against the product's configured minimum or maximum term.<br> | enum: ["DAYS", "WEEKS", "MONTHS", "YEARS"]; example: "MONTHS" |
| `deposit_configs.renewal_term.value` | integer (schema `MaturityPeriodValue`) | no | Number of time units until maturity. Must be greater than `0`. Mutually exclusive with `calendar_maturity_date`.<br> | minimum: 1; example: 6 |
| `deposit_configs.renewal_term.renewal_calendar_maturity_date` | string | no | Explicit renewal maturity date | format: "date"; example: "2028-06-15" |
| `deposit_configs.payout_account` | object (schema `PayoutAccount`) | no | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |
| `deposit_configs.maturity_instructions` | object (schema `MaturityInstructionsOverrideRequest`) | no | Overrides the deposit’s behavior at maturity. If a field is omitted, the Pismo platform uses the value defined at the higher‑level configuration that governs this deposit.<br> |  |
| `deposit_configs.penalties` | object (schema `PenaltiesOverrideRequest`) | no | Per-type penalty overrides. Each type independently uses three-state semantics:<br>omit (inherit) · `{waived: true}` (exempt) · `{waived: false, <fields>}` (customize).<br> |  |
| `deposit_configs.interest_capitalization_mode` | string | no | Present only when the attachment explicitly defines `interest_capitalization_mode`. Reflects the value stored on the attachment.<br> | enum: ["PAYOUT", "REINVEST"]; example: "REINVEST" |

201 Example `success` (Successful response):

```json
{
  "account_id": 123456,
  "external_account_id": "ext-acct-001",
  "product_id": "2c336e9d-d04f-4fd0-8f6e-25808f48d70c",
  "deposit_configs": {
    "maturity_period": {
      "unit": "MONTHS",
      "value": 6,
      "calendar_maturity_date": "2027-03-10"
    },
    "payout_account": {
      "type": "EXTERNAL",
      "external_account": {
        "account_number": "123456789",
        "bank_code": "001"
      }
    },
    "maturity_instructions": {
      "principal": "ROLLOVER",
      "interest": "PAY",
      "reason": "VIP retention package"
    },
    "penalties": {
      "reason": "VIP retention package",
      "grace_period": {
        "waived": false,
        "duration_days": 10,
        "penalty_interest_days": 15
      },
      "early_withdrawal_after_opening": {
        "waived": false,
        "applicable_within_days": 30,
        "penalty_interest_days": 90
      },
      "withdrawal_fee": {
        "waived": false,
        "type": "PERCENTAGE",
        "value": 2.5
      }
    },
    "interest_capitalization_mode": "REINVEST"
  }
}
```

##### Response 400

400 Example `validationError` (Request body validation error):

```json
{
  "code": "EIBACC0008",
  "message": "Bad Request",
  "details": "error EIBACC0008: Validation error [(Field 'external_account_id' is required)]"
}
```

400 Example `accountCreationRequired` (account_creation is required when account_id is not provided):

```json
{
  "code": "EIBACC0325",
  "message": "Field 'account_creation' is required when 'account_id' is not provided"
}
```

400 Example `invalidAccountCreationDatetime` (account_creation_datetime is not a valid RFC 3339 value):

```json
{
  "code": "EIBACC0380",
  "message": "Invalid account_creation_datetime format. Expected RFC3339"
}
```

400 Example `accountMismatch` (Provided account_id does not match external_account_id):

```json
{
  "code": "EIBACC0331",
  "message": "Provided account_id does not match the resolved external_account_id"
}
```

400 Example `productNotActive` (Product is not in ACTIVE status):

```json
{
  "code": "EIBACC0108",
  "message": "Product isn't ACTIVE. Activate to proceed with the attachment"
}
```

400 Example `corporateValidationError` (Corporate API validation error (wraps underlying WCAC error in details)):

```json
{
  "code": "EIBACC0330",
  "message": "Corporate API validation error",
  "details": "[WCAC0005] account_creation_datetime cannot be a future date"
}
```

400 Example `accountsApiError` (Accounts API returned a 4xx error):

```json
{
  "code": "EIBACC0018",
  "message": "Accounts API - Request returned error 4xx"
}
```

400 Example `invalidProductType` (Product type is not valid for deposit attachment):

```json
{
  "code": "EIBACC0065",
  "message": "Product Type is not valid"
}
```

400 Example `programsApiError` (Programs API returned a 4xx error):

```json
{
  "code": "EIBACC0103",
  "message": "Programs API - Request returned error 4xx"
}
```

400 Example `programOrAccountAlreadyAttached` (Program or account already has a product attached):

```json
{
  "code": "EIBACC0107",
  "message": "Informed program or account already has an attached product"
}
```

400 Example `maturityPeriodBelowMinTerm` (Maturity period is below the product minimum term):

```json
{
  "code": "EIBACC0109",
  "message": "Maturity period is below the configured MinTerm of the product"
}
```

400 Example `maturityPeriodAboveMaxTerm` (Maturity period is above the product maximum term):

```json
{
  "code": "EIBACC0110",
  "message": "Maturity period is above the configured MaxTerm of the product"
}
```

400 Example `productStartDateNotReached` (Product start date has not been reached yet):

```json
{
  "code": "EIBACC0236",
  "message": "Product cannot be attached before its start date"
}
```

400 Example `invalidPayoutAccount` (Payout account configuration is invalid):

```json
{
  "code": "EIBACC0284",
  "message": "Payout account is configured but is invalid"
}
```

400 Example `capitalizationPayoutRequiresPayoutAccount` (interest_capitalization_mode PAYOUT requires a payout_account):

```json
{
  "code": "EIBACC0379",
  "message": "interest_capitalization_mode PAYOUT requires a fully resolved payout_account",
  "details": "payout_account is required when interest_capitalization_mode is PAYOUT."
}
```

400 Example `maturityPeriodInvalidUnit` (maturity_period unit is not a supported value):

```json
{
  "code": "EIBACC0298",
  "message": "Validation error",
  "details": "Invalid maturity_period unit. Supported values: DAYS, WEEKS, MONTHS, YEARS"
}
```

400 Example `maturityPeriodInvalidValue` (maturity_period value is not a positive integer):

```json
{
  "code": "EIBACC0299",
  "message": "Validation error",
  "details": "maturity_period value must be a positive integer (>= 1)"
}
```

400 Example `productEndDateExpired` (Product end date has passed):

```json
{
  "code": "EIBACC0303",
  "message": "New attachments are not allowed after the deposit product end_date."
}
```

400 Example `maturityDateInvalidFormat` (calendar_maturity_date is not in YYYY-MM-DD format):

```json
{
  "code": "EIBACC0305",
  "message": "Validation error",
  "details": "calendar_maturity_date must be in YYYY-MM-DD format"
}
```

400 Example `maturityDateMustBeFuture` (calendar_maturity_date must be a future date):

```json
{
  "code": "EIBACC0306",
  "message": "Validation error",
  "details": "calendar_maturity_date must be a future date (after today)"
}
```

400 Example `maturityPeriodMutuallyExclusive` (calendar_maturity_date and unit+value are mutually exclusive):

```json
{
  "code": "EIBACC0307",
  "message": "Validation error",
  "details": "maturity_period accepts either calendar_maturity_date OR unit+value, not both"
}
```

400 Example `overrideValidUntilInvalid` (override valid_until must be a future datetime):

```json
{
  "code": "EIBACC0308",
  "message": "valid_until must be a future datetime"
}
```

400 Example `effectiveDateTooFarInPast` (Effective date exceeds maximum backdating limit):

```json
{
  "code": "EIBACC0319",
  "message": "Effective date exceeds maximum backdating limit"
}
```

400 Example `effectiveDateInvalidFormat` (effective_date is not in YYYY-MM-DD format):

```json
{
  "code": "EIBACC0320",
  "message": "Invalid effective date format. Expected YYYY-MM-DD"
}
```

400 Example `effectiveDateInFuture` (effective_date cannot be in the future):

```json
{
  "code": "EIBACC0321",
  "message": "Effective date cannot be in the future"
}
```

##### Response 403

403 Example `missingTenantHeader` (Missing tenant header):

```json
{
  "code": "EIBACC0005",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `accountStatusNotNormal` (Account status is not NORMAL):

```json
{
  "code": "EIBACC0104",
  "message": "Account status isn't NORMAL"
}
```

##### Response 404

404 Example `productNotFound` (Product not found):

```json
{
  "code": "EIBACC0064",
  "message": "Product not found"
}
```

##### Response 409

409 Example `accountAlreadyAttached` (Account already has a product attached):

```json
{
  "code": "EIBACC0106",
  "message": "The product ID provided is already attached"
}
```

409 Example `accountAlreadyExistsNotAttachable` (Existing account cannot be attached (status not NORMAL)):

```json
{
  "code": "EIBACC0396",
  "message": "Account already exists but could not be attached, status is not \"NORMAL\""
}
```

##### Response 422

422 Example `programNotValid` (Program is not valid for attachment):

```json
{
  "code": "EIBACC0297",
  "message": "Program is not valid for attachment. Program must be DEBIT type and ACTIVE status"
}
```

##### Response 500

500 Example `internalError` (Internal processing error):

```json
{
  "code": "EIBACC0007",
  "message": "Internal error"
}
```

500 Example `getProductError` (Failed to retrieve product):

```json
{
  "code": "EIBACC0066",
  "message": "Failed on get product"
}
```

500 Example `corporateRequestError` (Corporate API network or request error):

```json
{
  "code": "EIBACC0328",
  "message": "Corporate API request error"
}
```

500 Example `corporateUnmarshalError` (Failed to parse Corporate API response):

```json
{
  "code": "EIBACC0324",
  "message": "Failed to unmarshal Corporate API response"
}
```

##### Response 502

502 Example `corporateUnavailable` (Corporate API unavailable):

```json
{
  "code": "EIBACC0322",
  "message": "Corporate API unavailable"
}
```

##### Response 504

504 Example `corporateTimeout` (Corporate API timeout):

```json
{
  "code": "EIBACC0329",
  "message": "Corporate API timeout"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBACC0008` | Bad Request |
| 400 | `EIBACC0325` | Field 'account_creation' is required when 'account_id' is not provided |
| 400 | `EIBACC0380` | Invalid account_creation_datetime format. Expected RFC3339 |
| 400 | `EIBACC0331` | Provided account_id does not match the resolved external_account_id |
| 400 | `EIBACC0108` | Product isn't ACTIVE. Activate to proceed with the attachment |
| 400 | `EIBACC0330` | Corporate API validation error |
| 400 | `EIBACC0018` | Accounts API - Request returned error 4xx |
| 400 | `EIBACC0065` | Product Type is not valid |
| 400 | `EIBACC0103` | Programs API - Request returned error 4xx |
| 400 | `EIBACC0107` | Informed program or account already has an attached product |
| 400 | `EIBACC0109` | Maturity period is below the configured MinTerm of the product |
| 400 | `EIBACC0110` | Maturity period is above the configured MaxTerm of the product |
| 400 | `EIBACC0236` | Product cannot be attached before its start date |
| 400 | `EIBACC0284` | Payout account is configured but is invalid |
| 400 | `EIBACC0379` | interest_capitalization_mode PAYOUT requires a fully resolved payout_account |
| 400 | `EIBACC0298` | Validation error |
| 400 | `EIBACC0299` | Validation error |
| 400 | `EIBACC0303` | New attachments are not allowed after the deposit product end_date. |
| 400 | `EIBACC0305` | Validation error |
| 400 | `EIBACC0306` | Validation error |
| 400 | `EIBACC0307` | Validation error |
| 400 | `EIBACC0308` | valid_until must be a future datetime |
| 400 | `EIBACC0319` | Effective date exceeds maximum backdating limit |
| 400 | `EIBACC0320` | Invalid effective date format. Expected YYYY-MM-DD |
| 400 | `EIBACC0321` | Effective date cannot be in the future |
| 403 | `EIBACC0005` | Missing required header: 'x-tenant' |
| 403 | `EIBACC0104` | Account status isn't NORMAL |
| 404 | `EIBACC0064` | Product not found |
| 409 | `EIBACC0106` | The product ID provided is already attached |
| 409 | `EIBACC0396` | Account already exists but could not be attached, status is not "NORMAL" |
| 422 | `EIBACC0297` | Program is not valid for attachment. Program must be DEBIT type and ACTIVE status |
| 500 | `EIBACC0007` | Internal error |
| 500 | `EIBACC0066` | Failed on get product |
| 500 | `EIBACC0328` | Corporate API request error |
| 500 | `EIBACC0324` | Failed to unmarshal Corporate API response |
| 502 | `EIBACC0322` | Corporate API unavailable |
| 504 | `EIBACC0329` | Corporate API timeout |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `deposit-product-account-attach-1` | https://developers.pismo.io/events/docs/deposit-product-account-attach-1 |
| `deposit-product-deposit-account-opened-1` | https://developers.pismo.io/events/docs/deposit-product-deposit-account-opened-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;404;409;422;500;502;504`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-BANK-interest-bearing-accounts`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/UnifiedOpenAccount -->
### Schema `UnifiedOpenAccount`

Pointer: `#/components/schemas/UnifiedOpenAccount`. Type: object (schema `UnifiedOpenAccount`).

> Identifies the account to which the deposit product is attached

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_account_id` | string | yes | The external account ID identifies the transaction banking account. The Pismo platform uses this ID to find the account via the transaction banking API and attach the specified deposit product.<br> | example: "ext-acct-001" |
| `account_id` | integer | no | Pismo account ID. When provided, the Pismo platform locates the account using `external_account_id` and validates the ID.<br>If omitted, the Pismo platform uses `account_creation` to create a new account.<br> | format: "int64"; example: 123456 |

<!-- schema: #/components/schemas/UnifiedOpenDepositAttachment -->
### Schema `UnifiedOpenDepositAttachment`

Pointer: `#/components/schemas/UnifiedOpenDepositAttachment`. Type: object (schema `UnifiedOpenDepositAttachment`).

> Deposit product attachment configuration

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_id` | string | yes | Product ID of the deposit product to attach | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `deposit_configs` | object (schema `DepositConfigs`) | no |  |  |

<!-- schema: #/components/schemas/UnifiedOpenAccountCreation -->
### Schema `UnifiedOpenAccountCreation`

Pointer: `#/components/schemas/UnifiedOpenAccountCreation`. Type: object (schema `UnifiedOpenAccountCreation`).

> Account creation parameters. Required when `account.account_id` is not provided.
> Pismo platform uses these fields to create a new transaction banking account via the transaction banking API.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_id` | integer | yes | Program ID to associate the new account with | format: "int64"; example: 100 |
| `division_code` | string | yes | Division code for the new account | example: "001" |
| `applicant` | object (schema `UnifiedOpenApplicant`) | yes | Applicant information for account creation |  |
| `currency_code` | string | no | ISO 4217 currency code for the account. If omitted, the default currency for the program is used. | example: "USD" |
| `account_creation_datetime` | string | no | Account creation timestamp in RFC 3339 (a strict profile of ISO 8601). That is, the format should be `yyyy-mm-ddThh:mm:ss.sssZ` (24 characters). Optional. It is forwarded to the transaction-banking API for account creation and is also used by the deposit flow to anchor the attachment's effective date. The timestamp is converted to the account division's local calendar day, and the `calendar_maturity_date` plus the interest cycle are computed from that day. So, a retroactive open (a past timestamp) backdates maturity and interest accrual accordingly. When omitted, the current instant expressed in the division timezone is used. When the division has no timezone configured, the day is resolved in UTC. | format: "date-time"; minLength: 24; maxLength: 24; example: "2026-06-24T14:49:36.017Z" |

<!-- schema: #/components/schemas/MaturityPeriod -->
### Schema `MaturityPeriod`

Pointer: `#/components/schemas/MaturityPeriod`. Type: object (schema `MaturityPeriod`).

> Defines when the deposit matures. There are three usage modes:
>
> * **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).
> * **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).
> * **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.
>
> **NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.
>
> In the **attach** endpoints, the response returns exactly what was sent in the request:
> * Send `unit` + `value` returns `unit` + `value`
> * Send `calendar_maturity_date` returns `calendar_maturity_date`
> * Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`
>
> **NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `unit` | string (schema `MaturityPeriodUnit`) | no | Time unit for the relative maturity period. It's used together with `value` and cannot coincide with `calendar_maturity_date`.<br><br>- `DAYS`: Uses `value` directly. Example: `value=90` → 90 days.<br>- `WEEKS`: Multiplies `value` by 7. Example: `value=4` → 28 days.<br>- `MONTHS`: Calculates calendar-month with end-of-month (EOM) clamping when the target day does not exist. Example: `2024-01-31` + 1 month = `2024-02-29` (leap year) or `2025-02-28` (non-leap year).<br>- `YEARS`: Calculates calendar-year, for example: `2024-02-29` + 1 year = `2025-02-28`. Note that there is no Feb 29 in 2025.<br><br>For `WEEKS`, `MONTHS`, and `YEARS`, the resulting calendar date is converted back to a day count to validate against the product's configured minimum or maximum term.<br> | enum: ["DAYS", "WEEKS", "MONTHS", "YEARS"]; example: "MONTHS" |
| `value` | integer (schema `MaturityPeriodValue`) | no | Number of time units until maturity. Must be greater than `0`. Mutually exclusive with `calendar_maturity_date`.<br> | minimum: 1; example: 6 |
| `calendar_maturity_date` | string (schema `CalendarMaturityDate`) | no | Maturity date. Format is `YYYY-MM-DD`. The date must be a future date.<br><br>This date cannot coincide with `unit`/`value`, sending both in the same request returns a `400` validation error.<br> | format: "date"; example: "2027-06-15" |

<!-- schema: #/components/schemas/PayoutAccount -->
### Schema `PayoutAccount`

Pointer: `#/components/schemas/PayoutAccount`. Type: object (schema `PayoutAccount`).

> The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br>
>
> * **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.
> * **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.
>
> Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `label` | string | no | Label to identify the account<br> | example: "My payout account" |
| `type` | string | no | Payout account type, either `INTERNAL` or `EXTERNAL`<br> | enum: ["INTERNAL", "EXTERNAL"]; example: "INTERNAL" |
| `internal_account_id` | number | no | Internal account ID for the account that receives the payments.<br>Required for type `INTERNAL` and not allowed for `EXTERNAL`.<br> | example: 123456 |
| `external_account` | object | no | Contains user-defined key-value pairs that identify the external account receiving the payments.<br>Note that external account information is client-provided.<br><br>Required for type `EXTERNAL` and not allowed for `INTERNAL`.<br> | example: {"key": "value"} |

<!-- schema: #/components/schemas/MaturityInstructionsOverrideRequest -->
### Schema `MaturityInstructionsOverrideRequest`

Pointer: `#/components/schemas/MaturityInstructionsOverrideRequest`. Type: object (schema `MaturityInstructionsOverrideRequest`).

> Overrides the deposit’s behavior at maturity. If a field is omitted, the Pismo platform uses the value defined at the higher‑level configuration that governs this deposit.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `principal` | string | no | Specifies how the principal is handled once the deposit matures. | enum: ["ROLLOVER", "PAY"]; example: "ROLLOVER" |
| `interest` | string | no | Specifies how the interest is handled once the deposit matures. | enum: ["ROLLOVER", "PAY"]; example: "PAY" |
| `reason` | string | no | Optional audit-trail reason. | maxLength: 100; example: "Customer preference at onboarding" |

<!-- schema: #/components/schemas/PenaltiesOverrideRequest -->
### Schema `PenaltiesOverrideRequest`

Pointer: `#/components/schemas/PenaltiesOverrideRequest`. Type: object (schema `PenaltiesOverrideRequest`).

> Per-type penalty overrides. Each type independently uses three-state semantics:
> omit (inherit) · `{waived: true}` (exempt) · `{waived: false, <fields>}` (customize).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reason` | string | no | Optional audit-trail reason for the entire penalties block. | maxLength: 100; example: "Q4 2026 VIP retention package" |
| `grace_period` | object (schema `GracePeriodOverrideRequest`) | no | Grace period override. Type-specific fields are optional pointers, when omitted, the Pismo platform follows the normal fallback sequence, moving from the account level to the program and then to the product defaults. |  |
| `early_withdrawal_after_opening` | object (schema `EarlyWithdrawalAfterOpeningOverrideRequest`) | no | Override for early withdrawal after account opening. |  |
| `withdrawal_fee` | object (schema `WithdrawalFeeOverrideRequest`) | no | Withdrawal fee override. |  |
| `tiered_interest_forfeiture` | object (schema `TieredInterestForfeitureOverrideRequest`) | no | Tiered interest forfeiture override. Tiers replace the product's tiers when provided. |  |
| `subsequent_withdrawals` | object (schema `SubsequentWithdrawalsOverrideRequest`) | no | Subsequent withdrawals (Regulation D) override. |  |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code | example: "EIBACC0003" |
| `details` | string | no | Error details | example: "error EIBACC0008: Validation error [(Field 'Order' is invalid)]" |
| `message` | string | no | Error message | example: "Bad Request" |

<!-- schema: #/components/schemas/DepositConfigs -->
### Schema `DepositConfigs`

Pointer: `#/components/schemas/DepositConfigs`. Type: object (schema `DepositConfigs`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `maturity_period` | object (schema `MaturityPeriod`) | no | Defines when the deposit matures. There are three usage modes:<br><br>* **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).<br>* **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).<br>* **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.<br><br>**NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.<br><br>In the **attach** endpoints, the response returns exactly what was sent in the request:<br>* Send `unit` + `value` returns `unit` + `value`<br>* Send `calendar_maturity_date` returns `calendar_maturity_date`<br>* Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`<br><br>**NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.<br> |  |
| `payout_account` | object (schema `PayoutAccount`) | no | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |
| `interest_capitalization_mode` | string | no | Controls the treatment of capitalized interest. Optional field.<br><br><br>* `REINVEST` (default): The Pismo platform adds the capitalized amount to the principal. The new principal becomes the foundation for the next accrual cycle. No `payout_account` is required.<br>* `PAYOUT` (explicit): The capitalized amount is routed to `payout_account`. A valid `payout_account` is **required** in this request when this value is passed explicitly—omitting it returns `400 EIBACC0379`.<br>* `Omitted`: The Pismo platform applies `REINVEST`. Both the GET operation and events return `REINVEST`.<br><br>This setting affects only the capitalization process. The maturity instruction flow always uses `payout_account`, regardless of the value of this field.<br> | enum: ["REINVEST", "PAYOUT"]; default: "REINVEST"; example: "REINVEST" |
| `overrides` | object (schema `AttachmentOverridesRequest`) | no | Per-attachment overrides applied on top of the product defaults. All sub-fields are optional.<br>This object contains the per‑attachment overrides that supplement the product defaults. All sub‑fields are optional. Omitting a section causes the Pismo platform to follow the normal fallback sequence, moving from the account level to the program and then to the product defaults. Each penalty type provides `waived` as a required field, optional type‑specific fields, and an optional `valid_until` to schedule the revert.<br> |  |

<!-- schema: #/components/schemas/UnifiedOpenApplicant -->
### Schema `UnifiedOpenApplicant`

Pointer: `#/components/schemas/UnifiedOpenApplicant`. Type: object (schema `UnifiedOpenApplicant`).

> Applicant information for account creation

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string | yes | Applicant document number. For example, CPF or the US social security number. | example: "12345678900" |
| `name` | string | yes | Applicant's full name | example: "John Doe" |

<!-- schema: #/components/schemas/GracePeriodOverrideRequest -->
### Schema `GracePeriodOverrideRequest`

Pointer: `#/components/schemas/GracePeriodOverrideRequest`. Type: object (schema `GracePeriodOverrideRequest`).

> Grace period override. Type-specific fields are optional pointers, when omitted, the Pismo platform follows the normal fallback sequence, moving from the account level to the program and then to the product defaults.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `waived` | boolean | yes | `true` = fully exempt; `false` = penalty active (customize via the fields below). |  |
| `duration_days` | integer | no |  | minimum: 0 |
| `penalty_interest_days` | integer | no |  | minimum: 0 |
| `valid_until` | string | no | Schedules the revert of this override via EventBridge. This value must be a future date and follows the ISO 8601 standard. | format: "date-time" |

<!-- schema: #/components/schemas/EarlyWithdrawalAfterOpeningOverrideRequest -->
### Schema `EarlyWithdrawalAfterOpeningOverrideRequest`

Pointer: `#/components/schemas/EarlyWithdrawalAfterOpeningOverrideRequest`. Type: object (schema `EarlyWithdrawalAfterOpeningOverrideRequest`).

> Override for early withdrawal after account opening.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `waived` | boolean | yes |  |  |
| `applicable_within_days` | integer | no |  | minimum: 0 |
| `penalty_interest_days` | integer | no |  | minimum: 0 |
| `valid_until` | string | no |  | format: "date-time" |

<!-- schema: #/components/schemas/WithdrawalFeeOverrideRequest -->
### Schema `WithdrawalFeeOverrideRequest`

Pointer: `#/components/schemas/WithdrawalFeeOverrideRequest`. Type: object (schema `WithdrawalFeeOverrideRequest`).

> Withdrawal fee override.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `waived` | boolean | yes |  |  |
| `type` | string | no |  | enum: ["PERCENTAGE", "FIXED"] |
| `value` | number | no |  | exclusiveMinimum: 0 |
| `valid_until` | string | no |  | format: "date-time" |

<!-- schema: #/components/schemas/TieredInterestForfeitureOverrideRequest -->
### Schema `TieredInterestForfeitureOverrideRequest`

Pointer: `#/components/schemas/TieredInterestForfeitureOverrideRequest`. Type: object (schema `TieredInterestForfeitureOverrideRequest`).

> Tiered interest forfeiture override. Tiers replace the product's tiers when provided.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `waived` | boolean | yes |  |  |
| `tiers` | array of object (schema `TieredInterestForfeitureTierRequest`) | no |  |  |
| `valid_until` | string | no |  | format: "date-time" |

<!-- schema: #/components/schemas/SubsequentWithdrawalsOverrideRequest -->
### Schema `SubsequentWithdrawalsOverrideRequest`

Pointer: `#/components/schemas/SubsequentWithdrawalsOverrideRequest`. Type: object (schema `SubsequentWithdrawalsOverrideRequest`).

> Subsequent withdrawals (Regulation D) override.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `waived` | boolean | yes |  |  |
| `applicable_within_days` | integer | no |  | minimum: 1 |
| `penalty_interest_days` | integer | no |  | minimum: 1 |
| `window_behavior` | string | no |  | enum: ["ROLLING", "FIXED"] |
| `valid_until` | string | no |  | format: "date-time" |

<!-- schema: #/components/schemas/AttachmentOverridesRequest -->
### Schema `AttachmentOverridesRequest`

Pointer: `#/components/schemas/AttachmentOverridesRequest`. Type: object (schema `AttachmentOverridesRequest`).

> Per-attachment overrides applied on top of the product defaults. All sub-fields are optional.
> This object contains the per‑attachment overrides that supplement the product defaults. All sub‑fields are optional. Omitting a section causes the Pismo platform to follow the normal fallback sequence, moving from the account level to the program and then to the product defaults. Each penalty type provides `waived` as a required field, optional type‑specific fields, and an optional `valid_until` to schedule the revert.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `maturity_instructions` | object (schema `MaturityInstructionsOverrideRequest`) | no | Overrides the deposit’s behavior at maturity. If a field is omitted, the Pismo platform uses the value defined at the higher‑level configuration that governs this deposit.<br> |  |
| `renewal_term` | object (schema `RenewalTermOverrideRequest`) | no | Specifies the recurring rollover term, not to be confused with the initial `maturity_period`.<br><br>You must provide either `unit` with `value` or `renewal_calendar_maturity_date`.<br><br>A `ROLLOVER` configuration in principal or interest is required.<br><br>When you pass `renewal_calendar_maturity_date`, the Pismo platform converts the interval from today into a day count and stores it at attach time in normalized form: `{unit: DAYS, value: <calculated>}`.<br> |  |
| `penalties` | object (schema `PenaltiesOverrideRequest`) | no | Per-type penalty overrides. Each type independently uses three-state semantics:<br>omit (inherit) · `{waived: true}` (exempt) · `{waived: false, <fields>}` (customize).<br> |  |

<!-- schema: #/components/schemas/TieredInterestForfeitureTierRequest -->
### Schema `TieredInterestForfeitureTierRequest`

Pointer: `#/components/schemas/TieredInterestForfeitureTierRequest`. Type: object (schema `TieredInterestForfeitureTierRequest`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `min_days_held` | integer | yes |  | minimum: 0 |
| `max_days_held` | integer | no | Optional. Open-ended tier when omitted. | minimum: 0 |
| `forfeited_interest_days` | integer | yes |  | minimum: 0 |

<!-- schema: #/components/schemas/RenewalTermOverrideRequest -->
### Schema `RenewalTermOverrideRequest`

Pointer: `#/components/schemas/RenewalTermOverrideRequest`. Type: object (schema `RenewalTermOverrideRequest`).

> Specifies the recurring rollover term, not to be confused with the initial `maturity_period`.
>
> You must provide either `unit` with `value` or `renewal_calendar_maturity_date`.
>
> A `ROLLOVER` configuration in principal or interest is required.
>
> When you pass `renewal_calendar_maturity_date`, the Pismo platform converts the interval from today into a day count and stores it at attach time in normalized form: `{unit: DAYS, value: <calculated>}`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `unit` | string | no | Time unit of the renewal term. Required together with `value` when calendar form is not used. | enum: ["DAYS", "WEEKS", "MONTHS", "YEARS"]; example: "MONTHS" |
| `value` | integer | no | Number of units. Required together with `unit` when calendar form is not used. | minimum: 1; example: 6 |
| `renewal_calendar_maturity_date` | string | no | Explicit calendar date (`YYYY-MM-DD`), the date must be a future date, and does not coincide with `unit`+`value`. | format: "date"; example: "2027-05-22" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Interest-bearing_accounts.yaml` | tag `Deposit account open`: POST /v1/deposits/accounts/open | https://github.com/PismoDevEx/pismo-api-specs | `89fc3f8ed0222a57…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-interest-bearing-accounts` — Interest-bearing accounts
- `KU-ERR-codes-eibacc` — Error codes: EIBACC
- `KU-EVT-catalogue-deposit` — Event catalogue: deposit
