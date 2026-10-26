---
ku_id: KU-PAY-payment-configurations
title: Payment methods configurations overview
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/payment-configurations.md
  sha256: ff0057671d090055940433c092c7286d7e1c37504ac0fbd0a837683cf9efcc19
  url: https://developers.pismo.io/pismo-docs/docs/payment-configurations
  role: primary_guide
  updated_at: '2026-06-15T21:42:14.000Z'
operations:
- post-acceptance-by-tenant
- post-authorization
- post-config-by-tenant
- post-payments
- post-transfers
related_kus:
- KU-API-core-platform-balance-watcher--limit-acceptance-configurations
- KU-API-core-platform-balance-watcher--limit-configurations
- KU-API-core-platform-payment-configurations--payment-method-acceptances
- KU-API-core-platform-payment-configurations--payment-method-configurations
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-EVT-catalogue-other-domains
- KU-PAY-configure-payment-methods
- KU-PAY-payment-methods
grouping_rationale: single source page
---

# Payment methods configurations overview

**KU ID:** `KU-PAY-payment-configurations` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/payment-configurations.md`:

> The Payment methods configurations API provides advanced scalability and flexibility for [payment methods](https://developers.pismo.io/pismo-docs/docs/payment-methods). Highly customizable configuration options enable you to modify the Pismo platform’s default authorization behaviors to better serve different business needs and use cases and to improve processing times. This functionality supports multiple levels of configurations for [authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization), [payment](https://developers.pismo.io/pismo-docs/reference/post-payments), and [transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers) operations at different hierarchy levels.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/payment-configurations.md`: Payment methods configurations overview; Hierarchy; Configuration types; Platform configurations; Acceptance configurations; Validation rules; Related topics

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/payment-configurations.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/payment-configurations · updatedAt: 2026-06-15T21:42:14.000Z

<!-- source:begin path=docs/core-platform/payment-configurations.md part=0-end -->

# Payment methods configurations overview

The Payment methods configurations API provides advanced scalability and flexibility for [payment methods](https://developers.pismo.io/pismo-docs/docs/payment-methods). Highly customizable configuration options enable you to modify the Pismo platform’s default authorization behaviors to better serve different business needs and use cases and to improve processing times. This functionality supports multiple levels of configurations for [authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization), [payment](https://developers.pismo.io/pismo-docs/reference/post-payments), and [transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers) operations at different hierarchy levels.

There are three types of payment methods configurations:

* **Platform configurations** (also called **configurations**) are more general. This configuration type uses the  [platform configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) endpoints.
* **Acceptance configurations** (also called **acceptances**) are more specific. This configuration type uses the [acceptance configurations](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant) endpoints and requires the processing code (PC) of the corresponding financial operation.
* **Validation rules** (also called **rules**) are specific configurations. This configuration type can be used in the requests of [payment](https://developers.pismo.io/pismo-docs/reference/post-payments) and [transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers) endpoints as well as in the [platform configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) and [acceptance configurations](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant).

You can define any combination of platform configurations, acceptance configurations, and validation rules according to your business operation needs.  The platform configuration fields can be different from the acceptance configuration fields.

* You define validation rules in the [platform configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) and [acceptance configurations](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant) in the `rules` request object.
* You define validation rules in the create [cash-in/cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments) and [transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers) operation endpoints in the `validation_rules` request object.

<Callout icon="📘" theme="info">
  For a specific financial operation identified by a processing code, you should create an acceptance configuration. For a general configuration, create a platform configuration.
</Callout>

# Hierarchy

The Pismo platform hierarchy supports the **<Glossary>organization</Glossary> (org)** , **program**, **account**, **acceptance**, and **request** configuration levels, in order from the most general to the most specific. The platform evaluates configurations in the following reversed order, from specific to general.

> request → acceptance → account → program → org

This means that the more specific levels take precedence over the more general ones.

* Request-level configurations supersede acceptance-level configurations.
* Acceptance-level configurations supersede account-level configurations.
* Account-level configurations supersede program-level configurations.
* Program-level configurations supersede org-level configurations.

If you have the same parameters configured at different levels, the platform only analyzes what it receives at the most specific level and ignores everything else. Here are a few examples:

* If you define the same parameter in both the program and org configuration levels, the program-level parameter takes precedence.
* If you define the same parameter in both account and program configuration levels, the account-level parameter takes precedence.
* If you define the same parameter in both a platform configuration and an acceptance configuration, the acceptance-level parameter takes precedence.
* If you have configured validation rules in [platform configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) or [acceptance configurations](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant) in the `rules` field and then send validation rules through the [cash-in/cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments) or [transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers) operation endpoint requests in the `validation_rules` field, the platform only analyzes what it receives in the requests and ignores everything else.
* If you have configured validation rules in both platform configurations and acceptance configurations, the platform only evaluates what it finds in the acceptance configurations and ignores  platform configurations for the same parameters.

# Configuration types

The Pismo platform uses separate configurations for  **authorization**, **payment**, and **transfer** operations as follows:

* The [authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization) endpoints use configurations defined in the  `authorization` object of the  [platform configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) and [acceptance configurations](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant) endpoints.
* The [cash-in/cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments) endpoints use configurations defined in the `payment` object of the [platform configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) and [acceptance configurations](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant) endpoints.
* The [transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers) endpoints use configurations defined in the `transfer` object of the [platform configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) and [acceptance configurations](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant) endpoints.

## Platform configurations

Platform configurations provide the broadest level of payment methods configurations. As each org, program, and account may need different forms of processing, platform configurations allow you to customize authorization flows according to your needs for each level of the Pismo platform hierarchy.

You define platform configurations in the [platform configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) endpoints.

## Acceptance configurations

Acceptance configurations provide a more specific level of payment method configurations and also require the processing code of the financial operation in every endpoint. This allows you to customize the authorization flow for each financial operation following the Pismo platform hierarchy.

The acceptance configuration fields can be different from the payment configuration fields. If the same parameters are defined in both acceptance configurations and platform configurations, the acceptance parameters take precedence.

You define acceptance configurations in the [acceptance configurations](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant) endpoints.

## Validation rules

Validation rules provide the most granular level of payment methods configurations. You can choose which validations to perform during the authorization flow at different hierarchy levels. This highly customizable approach offers the following advantages.

* Define custom validation characteristics that match your business needs.
* Improve processing time and performance by skipping unnecessary validations.
* Override the response and denial codes returned by the authorization flow to match the specifics of different systems to handle different responses in different ways.
* Force a validation if the operation has any impact on the account balance.

<Callout icon="📘" theme="info">
  Validation **rules** are different from validation **results**. Validation results are the results returned by each validation in the authorization process. For details, refer to [Validation results array](https://developers.pismo.io/pismo-docs/docs/payment-methods#validation-results-array) in the Payment methods guide.
</Callout>

There are two types of validation: those that make HTTP requests to another service and those that validate the data in the service itself.

# Related topics

For detailed instructions and examples of configuring payment methods, refer to the [Configure payment methods](https://developers.pismo.io/pismo-docs/docs/configure-payment-methods) guide.

For an overview of payment methods, refer to the [Payment methods](https://developers.pismo.io/pismo-docs/docs/payment-methods) guide.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /payment-methods/v1/authorization` | `post-authorization` | Request authorization | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `POST /payment-methods/v2/payments` | `post-payments` | Create cash-in or cash-out | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `POST /payment-methods/v2/transfers` | `post-transfers` | Create transfer | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-02 |
| `POST /v1/config` | `post-config-by-tenant` | Create limit config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-configurations |
| `POST /payment-methods-configs/v1/configs` | `post-config-by-tenant` | Create org configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `POST /v1/acceptance/processing-code/{processingCode}` | `post-acceptance-by-tenant` | Create limit acceptance config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-acceptance-configurations |
| `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `post-acceptance-by-tenant` | Create org acceptance configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-acceptances |

### Operation essentials

- **`POST /payment-methods/v1/authorization`** (`post-authorization`): security `BearerAuth`; required parameters none declared; required body fields `currency_code`, `mti`, `network`; response statuses 200, 201, 400, 401, 403, 422, 500; error codes in examples `WONA0001`, `WONA0004`, `WONA0005`, `WONA0006`, `WONA0011`, `WONA0012`, `WONA0013`, `WONA0015`, `WONA0016`, `WONA0018`, `WONA0019`, `WONA0020`, `WONA0032`, `WONA0033`, `WONA0036`, `WONA039`, `WONA040`, `WONA041`, `WONA042`, `WONA043`, `EINS0004`, `EINS0005`, `EINS0006`, `EINS0010`, `EINS0011`, `EINS0012`, `EINS0015`, `EINS0016`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `payment-methods-authorization-1`, `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/payments`** (`post-payments`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `amount`, `processing_code`, `tracking_id`; response statuses 200, 201, 400, 401, 409, 422, 500; error codes in examples `WONP0001`, `WONB0001`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/transfers`** (`post-transfers`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `from`, `to`, `tracking_id`; response statuses 200, 201, 400, 401, 409, 422, 500; error codes in examples `WONP0001`, `WONB0001`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`POST /v1/config`** (`post-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-config-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/configs`** (`post-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-config-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /v1/acceptance/processing-code/{processingCode}`** (`post-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}`** (`post-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-authorization` | `payment-methods-authorization-1` |
| `post-authorization` | `platform-authorization-platform-authorization-1` |
| `post-payments` | `platform-authorization-platform-authorization-1` |
| `post-transfers` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/payment-configurations.md`: updatedAt 2026-06-15T21:42:14.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/payment-configurations.md` | whole document | https://developers.pismo.io/pismo-docs/docs/payment-configurations | `ff0057671d090055…` | 2026-06-15T21:42:14.000Z |

## Related knowledge units

- `KU-API-core-platform-balance-watcher--limit-acceptance-configurations` — API reference: Core platform - Balance watcher — Limit acceptance configurations
- `KU-API-core-platform-balance-watcher--limit-configurations` — API reference: Core platform - Balance watcher — Limit configurations
- `KU-API-core-platform-payment-configurations--payment-method-acceptances` — API reference: Core platform - Payment configurations — Payment method acceptances
- `KU-API-core-platform-payment-configurations--payment-method-configurations` — API reference: Core platform - Payment configurations — Payment method configurations
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-configure-payment-methods` — Configure payment methods
- `KU-PAY-payment-methods` — Payment methods
