---
ku_id: KU-CORE-exchange-rate
title: Exchange rates
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/exchange-rate.md
  sha256: 649fd445bbacf233da05c73acbba6031323637d0254269403b4ebff24ec56d52
  url: https://developers.pismo.io/pismo-docs/docs/exchange-rate
  role: primary_guide
  updated_at: '2026-05-29T15:12:57.000Z'
operations:
- createExchangeRates
- getExchange
related_kus:
- KU-API-platform-setup-rates-and-fees--exchange-rates
- KU-ERR-validation-code-definitions
grouping_rationale: single source page
---

# Exchange rates

**KU ID:** `KU-CORE-exchange-rate` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/exchange-rate.md`:

> The Pismo platform supports multi-currency exchange rates for international transactions. You **must** use the [Create exchange rate](https://developers.pismo.io/pismo-docs/reference/createexchangerates) endpoint to create an exchange rate for today or tomorrow for your organization (org) or a specific program.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/exchange-rate.md`: Exchange rates; Exchange rates for international transactions; Sample Create exchange rate endpoint request payload; Multi-currency setup (MCS) and same-currency pairs

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/exchange-rate.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/exchange-rate · updatedAt: 2026-05-29T15:12:57.000Z

<!-- source:begin path=docs/core-platform/exchange-rate.md part=0-end -->

# Exchange rates

The Pismo platform supports multi-currency exchange rates for international transactions. You **must** use the [Create exchange rate](https://developers.pismo.io/pismo-docs/reference/createexchangerates) endpoint to create an exchange rate for today or tomorrow for your organization (org) or a specific program.

## Exchange rates for international transactions

You do not need to register exchange rates for international transactions daily. The last rate configured less than or equal to the rate date is used.

> 📘 What if no exchange rate is configured?
>
> If no exchange rate is created for a specific date, the last rate configured earlier than or equal to the rate date is used.
>
> If no exchange rate is created at all, an error is returned.

If you have a flex control that blocks international purchases, it's important to register them as you may have a flex control override for a specific account / customer\_id / card\_id.

Configured exchange rates are retained in the Pismo database and are not purged.

If you do not configure exchange rates for international purchases:

* International authorizations will return the  [Rates API denial](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#rad---rates-api-denial) (RAD) denial code.
* Network authorization validation results will return the following object:

```json
{
  "name": "RATES_LOGICAL",
  "status": "REJECTED",
  "reason": "RATES_LOGICAL_ERROR",
  "description": "Denied by application while performing amounts calculation.",
  "additional_data": {}
}
```

## Sample Create exchange rate endpoint request payload

```json
{
   "program_id": 1985,
   "date": "2022-04-05",
   "exchange_rate": 4.8123,
   "spread": 1.1205,
   "origin_currency_id": "840",
   "destination_currency_id": "986"
}
```

The purchase is made in U.S. dollars, but the payment for it is in Brazilian reals, so the `origin_currency_id` is `840` and `destination_currency_id` is `986`.  These are ISO 4217 currency code values.

The `exchange_rate` in the example is `4.8123`, which means that 1 U.S. dollar (origin currency) equals 4.8123 Brazilian reals (destination currency).

The `spread` value of `1.1205` is equivalent to 1.1205% , which represents the percentage rate multiplier on the day. The platform adds this percentage that the issuer wants to charge for the conversion to the value of exchange rates.

If this request is successful, the platform creates the exchange rate and applies it to the program, since the `program_id` is specified in the request.

Use the [Get exchange rates](https://developers.pismo.io/pismo-docs/reference/getexchange) endpoint to get exchange rates for your org or for a specific program.

## Multi-currency setup (MCS) and same-currency pairs

Rates configuration is required for every pair used in MCS as well as same-currency pairs. Even when origin and destination currencies are the same (for example, USD → USD child account or EUR → EUR child account), the Rates API is still called for every non-zero transaction. You cannot skip the call to the Rates API. If there is no rate configuration for that pair, the Rates API call fails and the authorization is denied.

After MCS routing, the destination currency sent to the Rates API is already the child account's currency—this happens automatically. No additional configuration is needed on the authorization side to trigger that routing. The Pismo platform correctly identifies the child account and uses its currency as the destination.

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/exchange-rates` | `createExchangeRates` | Create exchange rate | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--exchange-rates |
| `GET /v1/exchange-rates` | `getExchange` | Get exchange rates | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--exchange-rates |

### Operation essentials

- **`POST /v1/exchange-rates`** (`createExchangeRates`): security `bearerAuth`; required parameters `Authorization` (header); required body fields `date`, `destination_currency_id`, `origin_currency_id`, `exchange_rate`, `spread`; response statuses 201, 400, 401, 422, 500; error codes in examples none; events none listed.
- **`GET /v1/exchange-rates`** (`getExchange`): security `bearerAuth`; required parameters `beginCreatedAt` (query), `endCreatedAt` (query), `perPage` (query), `page` (query), `Authorization` (header); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/core-platform/exchange-rate.md`: updatedAt 2026-05-29T15:12:57.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/exchange-rate.md` | whole document | https://developers.pismo.io/pismo-docs/docs/exchange-rate | `649fd445bbacf233…` | 2026-05-29T15:12:57.000Z |

## Related knowledge units

- `KU-API-platform-setup-rates-and-fees--exchange-rates` — API reference: Platform setup - Rates and fees — Exchange rates
- `KU-ERR-validation-code-definitions` — Validation code definitions
