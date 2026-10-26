---
ku_id: KU-CORE-over-limit-fee
title: Over-limit fees
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/over-limit-fee.md
  sha256: 6c7a5fb6d93a1bd1ac4a07be1c67b05c7699b7e163b13b5c0c1df438e6477050
  url: https://developers.pismo.io/pismo-docs/docs/over-limit-fee
  role: primary_guide
  updated_at: '2026-08-06T20:04:30.000Z'
operations:
- patch-v1-account-limit
- post-v1-balances-config
related_kus:
- KU-API-core-platform-balance-config-beta--balance-configurations
- KU-API-core-platform-ledger--account-limits
- KU-CC-get-started-control-center
- KU-CORE-balance-configurations
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Over-limit fees

**KU ID:** `KU-CORE-over-limit-fee` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/over-limit-fee.md`:

> You can configure your accounts to allow account holders to go over their maximum credit limit (`max_credit_limit`) when making purchases. To do this, you must define the allowable over-limit percentage. Normally, you also specify a fee that is charged at the end of the cycle whenever the account goes over the maximum credit limit during that cycle.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/over-limit-fee.md`: Over-limit fees; Enable over-limit fees; Configure over-limit fees; Example; Use Merchant Category Codes to allow or disallow over-limits

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/over-limit-fee.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/over-limit-fee · updatedAt: 2026-08-06T20:04:30.000Z

<!-- source:begin path=docs/core-platform/over-limit-fee.md part=0-end -->

# Over-limit fees

You can configure your accounts to allow account holders to go over their maximum credit limit (`max_credit_limit`) when making purchases. To do this, you must define the allowable over-limit percentage. Normally, you also specify a fee that is charged at the end of the cycle whenever the account goes over the maximum credit limit during that cycle.

<Callout icon="🚧" theme="warn">
  The Pismo platform doesn't allow an account to have a negative balance if `total_credit_limit`  is not equal to `max_credit_limit`, so a credit account can only go over-limit if these two fields are equal.
</Callout>

# Enable over-limit fees

To configure the over-limit fees, first enable them using the [Balance watcher](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant-1) API. This API listens for platform and card network events and triggers actions based on these events. To determine if an account should go into over-limit, the balance watcher listens for the following authorization events.

* [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1): authorizations from different payment domains
* [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1): platform authorizations from payment methods
* [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1): card network authorizations

You can enable over-limit settings at the  **<Glossary>organization</Glossary> (org)** , **program**, and **account** levels using the following configuration types.

* [Limit configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant-1) are more general. If set at the global level of the org, the platform uses these configurations as the default.
* [Limit acceptances](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant-1) are more specific. They are always associated with a processing code for a financial operation and are applied on a more granular level. Acceptances take precedence over configurations.

The Pismo platform evaluates acceptances and configurations in order from more specific to more general. For example: acceptance → account → program → org. This means that the more specific levels take precedence over the more general ones.

<Callout icon="🚧" theme="warn">
  Account-level configurations and acceptances are disabled by default. Contact your Pismo representative to enable them for your organization.
</Callout>

With acceptances, you can choose to enable the over-limit setting for each type of authorization for the financial operation (specified by its processing code). For example, you can use the following payload to enable over-limit fees for card network authorizations and disable them for all other authorizations.

```json
{  
	"network_authorization": {  
		"overlimit": {  
			"enabled": true  
		}  
	},  
	"platform_authorization": {  
		"overlimit": {  
			"enabled": false  
		}  
	},  
	"authorization": {  
		"overlimit": {  
			"enabled": false  
		}  
	}  
}
```

# Configure over-limit fees

To configure over-limit fees, perform the following steps.

1. Use the [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit) endpoint to do the following.
   * Set the maximum credit limit (`max_credit_limit`) for the account (if it hasn't already been set).
   * Set the `percentage_overlimit` field to a percentage of `max_credit_limit`. The amount by which the cardholder can go over the maximum credit limit is given by `percentage_overlimit` × `max_credit_limit`.
2. Use [Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) to set the **Overlimit fee amount** program parameter. This is a fixed fee that is charged at the end of the cycle if the account went over-limit at any time during the cycle. (It's only charged once, even if the account went over-limit multiple times during the cycle.)

When an account goes into over-limit, the available balance (that is, the `available_credit_limit field`) is shown as negative up to the over-limit amount. The Pismo platform generates an [Over-limit created](https://developers.pismo.io/events/docs/authorization-overlimit-creation-1) event. This event applies both to platform and card network operations.

<Callout icon="📘" theme="info">
  You can only configure the percentage over-limit at the account level.
</Callout>

# Example

In this example, suppose an account with a credit limit of $100 is marked to use the over-limit fee if its balance goes above this limit by 10%. The over-limit fee is $20, as defined in the **Overlimit fee amount** program parameter.

<Image align="center" src="https://files.readme.io/f9ebc0583dc2f89a0e61a6eed9a4ff1cce15cb10193176325152f1341ec2e77f-Over_limit_fees.png" />

During cycle 1, the account holder makes a purchase for $110, which is 10% over the credit limit and triggers the over-limit fee of $20. At the end of cycle 1, the statement balance amount is $130, which includes the purchase amount $110 and the over-limit fee $20.  If the account holder doesn’t pay this amount, the balance of $130 carries over to cycle 2.

At the end of cycle 2, the statement balance amount is $136.60, which includes the carried over balance $130, the fine $1.10, and the overdue interest $5.50. The platform continues to apply fines and interest charges until the account holder pays the full amount owed.

# Use Merchant Category Codes to allow or disallow over-limits

You can configure approval logic based on the Merchant Category Code (MCC) to allow or disallow the use of over-limits depending on the type of establishment. You do this by setting up specific conditions in the balance configuration.

Use the [Create balance configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config) endpoint to configure the approval logic to use MCCs. Add a configuration object using the `configs` body parameter, following these steps to configure the MCCs:

1. **Define filters**—Use the `filters` object to specify the MCCs for which you want to apply the configuration.
2. **Set scenarios**—Create scenarios with conditions that check the MCC and determine whether the over-limit can be used.
3. **`impact` and`consider` fields** —Use these fields to specify how the transaction should affect the available credit and over-limit.

For more information, refer to the [Balance configurations overview](https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview) guide.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limit` | Update account limits (outdated) | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |
| `POST /v1/balances-config` | `post-v1-balances-config` | Create balance configuration | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--balance-configurations |

### Operation essentials

- **`PATCH /v1/accounts/{accountId}/limits`** (`patch-v1-account-limit`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `WLDG0021`, `WLDG0010`, `WLDG0025`, `WLDG0022`, `ELDG9999`; events `ledger-limit-changed-1`.
- **`POST /v1/balances-config`** (`post-v1-balances-config`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields none declared; response statuses 201, 400, 404, 500; error codes in examples `EBCF0321`, `EBCF0320`, `EBCF0317`, `EBLC9999`; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `post-config-by-tenant-1` | Authorization configurations; Balance watcher; Create configuration by org; Limit configurations | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-acceptance-by-tenant-1` | Limit acceptances | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-v1-account-limit` | `ledger-limit-changed-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `authorization-authorization-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-event-1 | 9 | KU-EVT-catalogue-other-domains |
| `networktransactions-network-authorization-1` | networktransactions | 1 | https://developers.pismo.io/events/docs/networktransactions-network-authorization-1 | 2 | KU-EVT-catalogue-other-domains |
| `platform-authorization-platform-authorization-1` | platform | 1 | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 | 32 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/over-limit-fee.md`: updatedAt 2026-08-06T20:04:30.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 4 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.
- Operation link `post-config-by-tenant-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)
- Operation link `post-acceptance-by-tenant-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/over-limit-fee.md` | whole document | https://developers.pismo.io/pismo-docs/docs/over-limit-fee | `6c7a5fb6d93a1bd1…` | 2026-08-06T20:04:30.000Z |

## Related knowledge units

- `KU-API-core-platform-balance-config-beta--balance-configurations` — API reference: Core platform - Balance configurations — Balance configurations
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CORE-balance-configurations` — Balance configurations and filter templates
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
