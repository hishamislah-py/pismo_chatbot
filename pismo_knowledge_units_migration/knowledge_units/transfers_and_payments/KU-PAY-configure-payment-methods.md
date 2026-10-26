---
ku_id: KU-PAY-configure-payment-methods
title: Configure payment methods
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/configure-payment-methods.md
  sha256: ab60364e649d0a36a602a9ec325c6e57d092c99a97cbb6f13b10fa7797aec3a2
  url: https://developers.pismo.io/pismo-docs/docs/configure-payment-methods
  role: primary_guide
  updated_at: '2026-06-04T11:25:50.000Z'
operations:
- get-acceptance-by-tenant
- get-config-by-tenant
- patch-acceptance-by-tenant
- patch-config-by-tenant
- post-acceptance-by-account
- post-acceptance-by-program
- post-acceptance-by-tenant
- post-authorization
- post-config-by-account
- post-config-by-program
- post-config-by-tenant
- post-transfers
- put-acceptance-by-tenant
- put-config-by-tenant
related_kus:
- KU-API-core-platform-balance-watcher--limit-acceptance-configurations
- KU-API-core-platform-balance-watcher--limit-configurations
- KU-API-core-platform-payment-configurations--payment-method-acceptances
- KU-API-core-platform-payment-configurations--payment-method-configurations
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-CORE-authorization-validation-rules-for-platform-operations-part-01
- KU-CORE-authorization-validation-rules-for-platform-operations-part-02
- KU-EVT-catalogue-other-domains
- KU-PAY-payment-configurations
- KU-PAY-payment-methods
grouping_rationale: single source page
---

# Configure payment methods

**KU ID:** `KU-PAY-configure-payment-methods` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/configure-payment-methods.md`:

> You can define any combination of platform configurations, acceptance configurations, and validation rules according to your business needs.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/configure-payment-methods.md`: Configure payment methods; Prerequisites; Define platform configurations; Define acceptance configurations; Define validation rules; Examples in configurations and acceptances; Example 1 - Override response and denial codes; Example 2 - Skip anti-fraud evaluation; Example 3 - Skip balance validations; Example 4 - Update acceptance configuration setting; Example 5 - Update platform configuration setting; Examples in requests; Example 1 - Create cash-in or cash-out request; Example 2 - Create transfer request; Other request examples

## Prerequisites and dependencies

- Prerequisites are described in `docs/core-platform/configure-payment-methods.md` section "Prerequisites".
- Depends on 24 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/configure-payment-methods.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/configure-payment-methods · updatedAt: 2026-06-04T11:25:50.000Z

<!-- source:begin path=docs/core-platform/configure-payment-methods.md part=0-end -->

# Configure payment methods

You can define any combination of platform configurations, acceptance configurations, and validation rules according to your business needs.

# Prerequisites

Read [Payment methods](https://developers.pismo.io/pismo-docs/docs/payment-methods)  and [Payment methods configurations](https://developers.pismo.io/pismo-docs/docs/payment-configurations) guides.

# Define platform configurations

To define a platform configuration:

1. Use the appropriate endpoint: [Org](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant), [Program](https://developers.pismo.io/pismo-docs/reference/post-config-by-program), or [Account](https://developers.pismo.io/pismo-docs/reference/post-config-by-account).
2. Provide configuration details in the `authorization`, `payment`, and `transfer` request objects as needed for your operations.

For details, refer to the [examples in configurations and acceptances](https://developers.pismo.io/pismo-docs/docs/configure-payment-methods#examples-in-configurations-and-acceptances).

# Define acceptance configurations

To define an acceptance configuration:

1. Use the appropriate endpoint: [Org](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant), [Program](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-program), or [Account](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-account).
2. Provide the `processingCode` for the financial operation.
3. Provide configuration details in the `authorization`, `payment`, and `transfer` request objects as needed for your operations.

For details, refer to the [examples in configurations and acceptances](https://developers.pismo.io/pismo-docs/docs/configure-payment-methods#examples-in-configurations-and-acceptances).

# Define validation rules

You can define validation rules at every available configuration level.

* **Platform configuration** level by [Org](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant), [Program](https://developers.pismo.io/pismo-docs/reference/post-config-by-program), and [Account](https://developers.pismo.io/pismo-docs/reference/post-config-by-account) in the `rules` object.
* **Acceptance configuration** level by [Org](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant), [Program](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-program), and [Account](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-account) in the `rules` object.
* **Request** level in the [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization), [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments-1), and [Create transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers) endpoints in the `validation_rules` object.

  To define validation rules at the request level, refer to the following request structure and use the `validation_rules` object in the [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization), [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments-1) or the [Create transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers) endpoints.

```json Structure
"validation_rules": {
	"[NAME]": {
        "disable": true,
        "force": false,
        "denial_reasons": {
            "[REASON_1]": {
            	"response_code": "57",
            	"denial_code": "ABC"
        	},
            "[REASON_2]": {
            	"response_code": "14",
              "denial_code": "XYZ"
        	}
    }
	}
}
```

The following table describes the fields to use when defining a validation rule. For additional details, refer to the [request examples](https://developers.pismo.io/pismo-docs/docs/configure-payment-methods#examples-in-requests).

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `[NAME]`
      </td>

      <td>
        Validation name, as defined in [Authorization validation rules for platform operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations).
      </td>
    </tr>

    <tr>
      <td>
        `disable`
      </td>

      <td>
        When set to `true`, this boolean disables the specified validation. Validations that support this flag:

        * `ACCOUNT_STATUS`
        * `FLEX_CONTROLS`
        * `LEDGER`
        * `ANTI_FRAUD`⚠️**Note:** The `disable` flag always takes precedence over the `force` flag.
      </td>
    </tr>

    <tr>
      <td>
        `force`
      </td>

      <td>
        When set to `true`, this boolean forces the specified validation. Validation that supports this flag:

        * `LEDGER`
      </td>
    </tr>

    <tr>
      <td>
        `denial_reasons`
      </td>

      <td>
        In this object, you can override the service's default response and denial code values.  For a full list of denial reasons for each rule as well as the returned response and denial codes, refer to [Authorization validation rules for platform operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations).
      </td>
    </tr>
  </tbody>
</Table>

# Examples in configurations and acceptances

## Example 1 - Override response and denial codes

To override the response and denial codes from ledger validations in all flows (authorization, payment, and transfer), use the following example for either platform configurations or acceptance configurations.

```json
{  
    "authorization": {  
        "rules": {  
            "LEDGER": {  
                "denial_reasons": {  
                    "LEDGER_INSUFFICIENT_FUNDS": {  
                        "response_code": "99",  
                        "denial_code": "ABC"  
                	},  
                    "LEDGER_ERROR": {  
                        "response_code": "88",  
                        "denial_code": "DEF"  
                	}  
            	}  
        	}  
    	}  
	},  
    "payment": {  
        "rules": {  
            "LEDGER": {  
                "denial_reasons": {  
                    "LEDGER_INSUFFICIENT_FUNDS": {  
                        "response_code": "99",  
                        "denial_code": "ABC"  
                	},  
                    "LEDGER_ERROR": {  
                        "response_code": "88",  
                        "denial_code": "DEF"  
                	}  
            	}  
        	}  
    	}  
	},  
    "transfer": {  
        "from": {  
            "rules": {  
                "LEDGER": {  
                    "denial_reasons": {  
                        "LEDGER_INSUFFICIENT_FUNDS": {  
                            "response_code": "99",  
                            "denial_code": "ABC"  
                    	},  
                        "LEDGER_ERROR": {  
                            "response_code": "88",  
                            "denial_code": "DEF"  
                        }  
                	}  
            	}  
        	}  
    	},  
        "to": {  
            "rules": {  
                "LEDGER": {  
                    "denial_reasons": {  
                        "LEDGER_INSUFFICIENT_FUNDS": {  
                            "response_code": "99",  
                            "denial_code": "ABC"  
                    	},  
                        "LEDGER_ERROR": {  
                            "response_code": "88",  
                            "denial_code": "DEF"  
                        }  
                	}  
            	}  
        	}  
    	}  
	}  
}
```

If the authorization request fails because of `LEDGER_INSUFFICIENT_FUNDS` or `LEDGER_ERROR`, the platform returns the `response_code` and `denial_code` with the newly configured values. For example, if the request fails due to insufficient funds, the `response_code` is `99` and the `denial_code` is `ABC`.

## Example 2 - Skip anti-fraud evaluation

To skip anti-fraud evaluation in all flows (authorization, payment, and transfer), use the following example for either platform configurations or acceptance configurations.

```json
{
    "authorization": {
        "rules": {
            "ANTI_FRAUD": {
                "disable": true
        	}
    	}
	},
    "payment": {
        "rules": {
            "ANTI_FRAUD": {
                "disable": true
        	}
    	}
	},
    "transfer": {
        "from": {
            "rules": {
                "ANTI_FRAUD": {
                    "disable": true
            	}
        	}
    	},
        "to": {
            "rules": {
                "ANTI_FRAUD": {
                    "disable": true
            	}
        	}
    	}
	}
}

```

## Example 3 - Skip balance validations

To skip available balance validation in all flows (authorization, payment, and transfer), use the following example for either platform configurations or acceptance configurations.

```json
{
    "authorization": {
        "rules": {
            "LEDGER": {
                "force": true
        	}
    	}
	},
    "payment": {
        "rules": {
            "LEDGER": {
                "force": true
        	}
    	}
	},
    "transfer": {
        "from": {
            "rules": {
                "LEDGER": {
                    "force": true
            	}
        	}
    	},
        "to": {
            "rules": {
                "LEDGER": {
                    "force": true
            	}
        	}
    	}
	}
}

```

## Example 4 - Update acceptance configuration setting

To change the `external_calculation_endpoint` configuration for your organization, use the PATCH [Update acceptance configuration by Org](https://developers.pismo.io/pismo-docs/reference/patch-acceptance-by-tenant) and pass the new value in the `external_calculation_endpoint` field.

Alternatively, you can use the PUT [Replace acceptance configuration by Org](https://developers.pismo.io/pismo-docs/reference/put-acceptance-by-tenant) endpoint, but with caution using the following approach.

<Callout icon="🚧" theme="warn">
  The HTTP PUT method replaces all configured fields that already exist. Before updating the configurations, the recommended approach is to use a GET to find the current configuration and then use this response to update only the fields you want.
</Callout>

1. Use [Get acceptance configuration by Org](https://developers.pismo.io/pismo-docs/reference/get-acceptance-by-tenant) to get the current configuration and take note of the response.

```json
{
    "authorization": {
        "external_calculation_endpoint": "https://calculationendpoint.com",
        "rules": {
            "ANTI_FRAUD": {
                "disable": true
        	}
    	}
	}
}
```

2. Use [Replace acceptance configuration by Org](https://developers.pismo.io/pismo-docs/reference/put-acceptance-by-tenant) and provide the following payload to update only the `external_calculation_endpoint` field and preserve the existing rules configurations.

```json
{
    "authorization": {
        "external_calculation_endpoint": "https://mynewcalculationendpoint123.com",
        "rules": {
            "ANTI_FRAUD": {
                "disable": true
        	}
    	}
	}
}

```

## Example 5 - Update platform configuration setting

To change the `confirmation_verification_endpoint` configuration for your organization, use the PATCH [Update configuration by Org](https://developers.pismo.io/pismo-docs/reference/patch-config-by-tenant) endpoint and pass the new value in the `external_calculation_endpoint` field.

Alternatively, you can use the PUT [Replace configuration by Org](https://developers.pismo.io/pismo-docs/reference/put-config-by-tenant) endpoint, but with caution using the following approach.

<Callout icon="🚧" theme="warn">
  The HTTP PUT method replaces all configured fields that already exist. Before updating the configurations, the recommended approach is to use a GET to find the current configuration and then use this response to update only the fields you want.
</Callout>

1. Use [Get configuration by Org](https://developers.pismo.io/pismo-docs/reference/get-config-by-tenant) to get the current configuration and take note of the response.

```json
{  
    "authorization": {  
        "confirmation_verification_endpoint": "https://verificationendpoint.com",  
        "rules": {  
            "ANTI_FRAUD": {  
                "disable": true  
        	}  
    	}  
	}  
}
```

2. Use [Replace configuration by Org](https://developers.pismo.io/pismo-docs/reference/put-config-by-tenant) and provide the following payload to update only the `external_calculation_endpoint` field and preserve the existing rules configurations.

```json
{  
       "authorization": {  
           "confirmation_verification_endpoint": "https://mynewverificationendpoint123.com",  
           "rules": {  
               "ANTI_FRAUD": {  
                   "disable": true  
           	}  
       	}  
   	}  
   }
```

# Examples in requests

## Example 1 - Create cash-in or cash-out request

In the [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments-1)  endpoint, the following request payload overrides response and denial codes for flex control and ledger validations.

```json
{
    "tracking_id": "e40b5122-b309-4220-bdab-b367664a93d5",
    "processing_code": "00",
    "account_id": 1,
    "amount": 100.00,
    "currency": "USD",
    "validation_rules": {
        "FLEX_CONTROLS": {
            "disable": false,
            "denial_reasons": {
                "FLEX_CONTROLS_ERROR": {
                	"response_code": "57",
                	"denial_code": "ABC"
            	},
                "FLEX_CONTROLS_NOT_APPROVED": {
                	"response_code": "14",
                    "denial_code": "XYZ"
            	}
        	}
    	},
        "LEDGER": {
            "disable": false,
            "denial_reasons": {
                "LEDGER_INSUFFICIENT_FUNDS": {
                	"response_code": "57",
                	"denial_code": "ABC"
            	},
                "LEDGER_ERROR": {
                	"response_code": "14",
                	"denial_code": "XYZ"
            	}
        	}
    	}
	}
}

```

## Example 2 - Create transfer request

In the [Create transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers) endpoint, the following request does the following:

* Overrides response and denial codes for insufficient funds in the `from` account
* Disables flex control validation in the `to` account
* Overrides response and denial codes for account status validations in the `to` account

```json
{
    "tracking_id": "e40b5122-b309-4220-bdab-b367664a93d5",
    "amount": 100.00,
		"from": {
        "processing_code": "00",
        "currency": "USD",
        "account_id": 1,
        "validation_rules": {
            "LEDGER": {
                "disable": false,
                "force": false,
                "denial_reasons": {
                    "LEDGER_INSUFFICIENT_FUNDS": {
                        "response_code": "99",
                        "denial_code": "ABC"
                	}
            	}
        	}
    	}
	},
		"to": {
        "processing_code": "01",
        "currency": "USD",
        "account_id": 2,
        "validation_rules": {
            "FLEX_CONTROLS": {
                "disable": true
        	},
            "ACCOUNT_STATUS": {
                "disable": false,
                "denial_reasons": {
                    "ACCOUNT_STATUS_NOT_PERMITTED": {
                        "response_code": "57",
                        "denial_code": "ABC"
                	}
            	}
        	}
    	}
	}
}

```

## Other request examples

To skip available account balance (ledger) validation, add the following to the request.

```json
{  
    "validation_rules": {  
        "LEDGER": {  
            "force": true  
    	}  
	}  
}
```

To skip flex control validations, add the following to the request.

```json
{  
    "validation_rules": {  
        "FLEX_CONTROLS": {  
            "disable": true  
    	}  
	}  
}
```

To skip operation's validation by the anti-fraud system, add the following to the request.

```json
{  
    "validation_rules": {  
        "ANTI_FRAUD": {  
            "disable": true  
    	}  
	}  
}
```

To skip account status validation, add the following to the request.

```json
{  
    "validation_rules": {  
         "ACCOUNT_STATUS": {  
            "disable": true  
    	}  
	}  
}
```

To skip account status and available balance (ledger) validations, add the following to the request.

```json
{  
    "validation_rules": {  
         "ACCOUNT_STATUS": {  
            "disable": true  
    	},  
       	 "LEDGER": {  
            "force": true  
    	}  
	}  
}
```

To override the response and denial codes from ledger validations, add the following to the request.

```json
{  
    "validation_rules": {  
        "LEDGER": {  
            "denial_reasons": {  
                "LEDGER_INSUFFICIENT_FUNDS": {  
                	"response_code": "99",  
                	"denial_code": "ABC"  
            	},  
                "LEDGER_ERROR": {  
                	"response_code": "88",  
                  "denial_code": "DEF"  
            	}  
        	}  
    	}  
	}  
}
```

If the authorization request fails because of `LEDGER_INSUFFICIENT_FUNDS` or `LEDGER_ERROR`, the platform returns the `response_code` and `denial_code` with the newly configured values. For example, if the request fails due to insufficient funds, the `response_code` is `99` and the `denial_code` is `ABC`.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/config` | `post-config-by-tenant` | Create limit config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-configurations |
| `POST /payment-methods-configs/v1/configs` | `post-config-by-tenant` | Create org configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `POST /v1/config/program/{programId}` | `post-config-by-program` | Create limit config by program | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-configurations |
| `POST /payment-methods-configs/v1/configs/programs/{programId}` | `post-config-by-program` | Create program configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `POST /v1/config/account/{accountId}` | `post-config-by-account` | Create limit config by account | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-configurations |
| `POST /payment-methods-configs/v1/configs/accounts/{accountId}` | `post-config-by-account` | Create account configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `POST /v1/acceptance/processing-code/{processingCode}` | `post-acceptance-by-tenant` | Create limit acceptance config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-acceptance-configurations |
| `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `post-acceptance-by-tenant` | Create org acceptance configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-acceptances |
| `POST /v1/acceptance/processing-code/{processingCode}/program/{programId}` | `post-acceptance-by-program` | Create limit acceptance config by program | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-acceptance-configurations |
| `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}` | `post-acceptance-by-program` | Create program acceptance configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-acceptances |
| `POST /v1/acceptance/processing-code/{processingCode}/account/{accountId}` | `post-acceptance-by-account` | Create limit acceptance config by account | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-acceptance-configurations |
| `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}` | `post-acceptance-by-account` | Create account acceptance configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-acceptances |
| `POST /payment-methods/v1/authorization` | `post-authorization` | Request authorization | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `POST /payment-methods/v2/transfers` | `post-transfers` | Create transfer | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-02 |
| `PATCH /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `patch-acceptance-by-tenant` | Update org acceptance configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-acceptances |
| `PUT /v1/acceptance/processing-code/{processingCode}` | `put-acceptance-by-tenant` | Update limit acceptance config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-acceptance-configurations |
| `PUT /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `put-acceptance-by-tenant` | Replace org acceptance configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-acceptances |
| `GET /v1/acceptance/processing-code/{processingCode}` | `get-acceptance-by-tenant` | Get limit acceptance config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-acceptance-configurations |
| `GET /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `get-acceptance-by-tenant` | Get org acceptance configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-acceptances |
| `PATCH /payment-methods-configs/v1/configs` | `patch-config-by-tenant` | Update org configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `PUT /v1/config` | `put-config-by-tenant` | Update limit config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-configurations |
| `PUT /payment-methods-configs/v1/configs` | `put-config-by-tenant` | Replace org configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `GET /v1/config` | `get-config-by-tenant` | Get limit config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-configurations |
| `GET /payment-methods-configs/v1/configs` | `get-config-by-tenant` | Get org configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |

### Operation essentials

- **`POST /v1/config`** (`post-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-config-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/configs`** (`post-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-config-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /v1/config/program/{programId}`** (`post-config-by-program`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-config-by-program` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/configs/programs/{programId}`** (`post-config-by-program`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-config-by-program` occurs in 2 specification files; the link does not say which one.
- **`POST /v1/config/account/{accountId}`** (`post-config-by-account`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-config-by-account` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/configs/accounts/{accountId}`** (`post-config-by-account`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-config-by-account` occurs in 2 specification files; the link does not say which one.
- **`POST /v1/acceptance/processing-code/{processingCode}`** (`post-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}`** (`post-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /v1/acceptance/processing-code/{processingCode}/program/{programId}`** (`post-acceptance-by-program`): security `BearerAuth`; required parameters `processingCode` (path), `programId` (path); required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-acceptance-by-program` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}`** (`post-acceptance-by-program`): security `BearerAuth`; required parameters `processingCode` (path), `programId` (path); required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-acceptance-by-program` occurs in 2 specification files; the link does not say which one.
- **`POST /v1/acceptance/processing-code/{processingCode}/account/{accountId}`** (`post-acceptance-by-account`): security `BearerAuth`; required parameters `processingCode` (path), `accountId` (path); required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-acceptance-by-account` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}`** (`post-acceptance-by-account`): security `BearerAuth`; required parameters `processingCode` (path), `accountId` (path); required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-acceptance-by-account` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods/v1/authorization`** (`post-authorization`): security `BearerAuth`; required parameters none declared; required body fields `currency_code`, `mti`, `network`; response statuses 200, 201, 400, 401, 403, 422, 500; error codes in examples `WONA0001`, `WONA0004`, `WONA0005`, `WONA0006`, `WONA0011`, `WONA0012`, `WONA0013`, `WONA0015`, `WONA0016`, `WONA0018`, `WONA0019`, `WONA0020`, `WONA0032`, `WONA0033`, `WONA0036`, `WONA039`, `WONA040`, `WONA041`, `WONA042`, `WONA043`, `EINS0004`, `EINS0005`, `EINS0006`, `EINS0010`, `EINS0011`, `EINS0012`, `EINS0015`, `EINS0016`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `payment-methods-authorization-1`, `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/transfers`** (`post-transfers`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `from`, `to`, `tracking_id`; response statuses 200, 201, 400, 401, 409, 422, 500; error codes in examples `WONP0001`, `WONB0001`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`PATCH /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}`** (`patch-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples none; events none listed.
- **`PUT /v1/acceptance/processing-code/{processingCode}`** (`put-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples `BW0008`, `BW0031`, `BW0001`, `BW0007`; events none listed. Note: operationId `put-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`PUT /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}`** (`put-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples none; events none listed. Note: operationId `put-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`GET /v1/acceptance/processing-code/{processingCode}`** (`get-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples `BW0008`, `BW0031`, `BW0001`, `BW0007`; events none listed. Note: operationId `get-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`GET /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}`** (`get-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples none; events none listed. Note: operationId `get-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`PATCH /payment-methods-configs/v1/configs`** (`patch-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples none; events none listed.
- **`PUT /v1/config`** (`put-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples `BW0008`, `BW0031`, `BW0001`, `BW0007`; events none listed. Note: operationId `put-config-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`PUT /payment-methods-configs/v1/configs`** (`put-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples none; events none listed. Note: operationId `put-config-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`GET /v1/config`** (`get-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples `BW0008`, `BW0031`, `BW0001`, `BW0007`; events none listed. Note: operationId `get-config-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`GET /payment-methods-configs/v1/configs`** (`get-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples none; events none listed. Note: operationId `get-config-by-tenant` occurs in 2 specification files; the link does not say which one.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `post-payments-1` | Create cash-in or cash-out | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-authorization` | `payment-methods-authorization-1` |
| `post-authorization` | `platform-authorization-platform-authorization-1` |
| `post-transfers` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/configure-payment-methods.md`: updatedAt 2026-06-04T11:25:50.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- Operation link `post-payments-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/configure-payment-methods.md` | whole document | https://developers.pismo.io/pismo-docs/docs/configure-payment-methods | `ab60364e649d0a36…` | 2026-06-04T11:25:50.000Z |

## Related knowledge units

- `KU-API-core-platform-balance-watcher--limit-acceptance-configurations` — API reference: Core platform - Balance watcher — Limit acceptance configurations
- `KU-API-core-platform-balance-watcher--limit-configurations` — API reference: Core platform - Balance watcher — Limit configurations
- `KU-API-core-platform-payment-configurations--payment-method-acceptances` — API reference: Core platform - Payment configurations — Payment method acceptances
- `KU-API-core-platform-payment-configurations--payment-method-configurations` — API reference: Core platform - Payment configurations — Payment method configurations
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-CORE-authorization-validation-rules-for-platform-operations-part-01` — Authorization validation rules for platform operations (part 1 of 2)
- `KU-CORE-authorization-validation-rules-for-platform-operations-part-02` — Authorization validation rules for platform operations (part 2 of 2)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-payment-configurations` — Payment methods configurations overview
- `KU-PAY-payment-methods` — Payment methods
