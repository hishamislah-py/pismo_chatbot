---
ku_id: KU-CORE-flex-controls
title: 'Flexible transaction controls: concepts, examples and simulation'
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/flex-controls.md
  sha256: 04e61fe396bb4110aa8646c2b658ecae191a9c85955f777d4622973902285905
  url: https://developers.pismo.io/pismo-docs/docs/flex-controls
  role: primary_guide
  updated_at: '2026-10-01T00:42:59.000Z'
- path: docs/core-platform/flex-controls-examples.md
  sha256: b2807be45f9cf0a4463836d0eda23360c670b81694521b1743b60da4ae5e4d2c
  url: https://developers.pismo.io/pismo-docs/docs/flex-controls-examples
  role: primary_guide
  updated_at: '2026-10-01T00:21:11.000Z'
- path: docs/core-platform/simulate-flex-control-creation.md
  sha256: 882c045fe3e73bf6e8f48088c635feb457886fd0f3a2e899a23703e5608c881b
  url: https://developers.pismo.io/pismo-docs/docs/simulate-flex-control-creation
  role: primary_guide
  updated_at: '2026-10-01T00:15:24.000Z'
operations:
- get-v1-accounts-flex-controls
- patch-v1-accounts-flex-control
- post-v1-accounts-flex-controls
- post-v1-customers-flex-controls
- post_v1-authorizations
related_kus:
- KU-API-card-issuing-authorization--authorizations
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-flex-controls--customer-flex-controls-part-01
- KU-CARD-simulate-authorizations
- KU-CC-get-started-control-center
- KU-CORE-attribute-groups
- KU-CORE-program-parameters-reference-table
- KU-EVT-catalogue-audit
- KU-EVT-catalogue-other-domains
- KU-EVT-flex-controls-data-events
- KU-GS-developer-tooling
- KU-PAY-pix-instant-payments
grouping_rationale: One feature.
---

# Flexible transaction controls: concepts, examples and simulation

**KU ID:** `KU-CORE-flex-controls` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: One feature.

Scope as stated in `docs/core-platform/flex-controls.md`:

> The Pismo platform supports creation of different types and levels of flexible transaction controls (flex controls), which are rules that restrict your customers' financial operations, such as spending mode or maximum spending limit restrictions. [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) allows you to manage program-level flex controls through a user interface. The flex controls API allows you to create and manage [account-level](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls),  [customer-level](https://developers.pismo.io/pismo-docs/reference/post-v1-customers-flex-controls), and card-level flex controls.

Scope as stated in `docs/core-platform/flex-controls-examples.md`:

> The following examples show common flex control implementation scenarios that can be created with the [Create account flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls)  and [Create customer flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-customers-flex-controls)  endpoints.

Scope as stated in `docs/core-platform/simulate-flex-control-creation.md`:

> This guide explains how to simulate and verify flexible transaction controls (flex controls) using Postman before applying them in production. By testing controls in a simulated environment, you can confirm that authorization rules restrict or permit transactions as expected without affecting live operations.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/flex-controls.md`: Flexible transaction controls; Flex control types; Related topics
- `docs/core-platform/flex-controls-examples.md`: Flex controls examples; Deny purchase by merchant category; Deny purchase by entry mode; Define maximum usage limit; Restrict purchase authorizations within a time window; Limit the quantity of purchase transactions within a time window; Create flex control per transaction type; Create flex control for a beneficiary overriding existing controls; Pix and accounts; Related topics
- `docs/core-platform/simulate-flex-control-creation.md`: Simulate flex control creation; Prerequisites; Step 1: Authenticate and set up test entities; Step 2: Verify baseline transaction authorization; Step 3: Create a test flex control; Step 4: Simulate a restricted authorization; Next steps; Related topics

## Prerequisites and dependencies

- Prerequisites are described in `docs/core-platform/simulate-flex-control-creation.md` section "Prerequisites".
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/flex-controls.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/flex-controls · updatedAt: 2026-10-01T00:42:59.000Z

<!-- source:begin path=docs/core-platform/flex-controls.md part=0-end -->

# Flexible transaction controls

The Pismo platform supports creation of different types and levels of flexible transaction controls (flex controls), which are rules that restrict your customers' financial operations, such as spending mode or maximum spending limit restrictions. [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) allows you to manage program-level flex controls through a user interface. The flex controls API allows you to create and manage [account-level](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls),  [customer-level](https://developers.pismo.io/pismo-docs/reference/post-v1-customers-flex-controls), and card-level flex controls.

You can define a flex control at each entity's respective level. For a program, define the flex control at the program level to affect all accounts or cards. To apply a flex control for a specific account, customer, or card, define the flex control at that level. After choosing the applicability level, define which conditions need to be considered at the time of evaluation.

# Flex control types

A flex control can be of a *cumulative*  or *restriction* type.

*Cumulative* controls (with `type` set to `usage_limit`, `spending_limit`, `cumulative_limit`) are used to restrict how many transactions a customer can perform or how much they can spend in a given time period. Cumulative spending controls calculate and maintain values of past transactions. These calculated values can either be a counter, such as the number of transactions, or the sum of the transactions.

*Restriction* controls (with `type` set to `restriction`) are used to restrict where, how, or when customers can perform financial operations. For example, restriction controls can deny purchases by merchant category code (MCC), by entry mode, or within a time window. The restriction control type defines the control condition(s) without any additional calculations.

| Type               | Description                                                                                                                                                                                            |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `usage_limit`      | Cumulative flex control that increases by one until `max_limit`                                                                                                                                        |
| `spending_limit`   | Cumulative flex control that increases by the current transaction's amount until `max_limit`                                                                                                           |
| `cumulative_limit` | Cumulative flex control that increases by one transaction or by transaction amount until a condition is met, applies only to flex controls with associated `card_ids`, and requires a `reset_strategy` |
| `restriction`      | Restriction flex control that only validates specified conditions                                                                                                                                      |

> 📘 Flex controls limit
>
> The Pismo platform limits the number of flex controls you can create:
>
> * Up to 200 flex controls at the program level
> * Up to 200 flex controls per account
> * Up to 200 controls that apply to either a customer or a card (customer and card entities share the same underlying data structure)

After you create a control, the Pismo platform uses it to evaluate authorizations on your customers' accounts. Evaluations happen at the account or customer level, not at the program level. If the authorization characteristics match the conditions configured in the control, the Pismo platform might deny a transaction. During flex control operations, the platform generates [flex control data events](https://developers.pismo.io/pismo-docs/docs/flex-controls-data-events) asynchronously.

![Flex control possibilities such as usage limits or number of transactions within a timespan](https://files.readme.io/69a648a-diagram-FlexControls-22x.png "diagram-FlexControls-2@2x.png")

<Callout icon="📘" theme="info">
  Flex controls can be used to control [Pix transactions](https://developers.pismo.io/pismo-docs/docs/pix-instant-payments), like the daily and nightly limits.
</Callout>

<Callout icon="📘" theme="info">
  To use flex controls in card network transactions, you must enable the **Send rules authorization** [program parameter](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table).
</Callout>

When an account is created, the Pismo platform copies all flex controls from the program to the accounts and/or cards, so every account has a copy of the flex controls attached to that program.

When a program-level flex control is changed, the Pismo platform does not immediately update flex controls copied to accounts in the original program. The platform waits for a flex control evaluation during the authorization flow to detect the differences between the account and program flex controls, and then incrementally updates the flex controls. For this update to occur, the flex control of the account must not be customized.

<Callout icon="📘" theme="info">
  To apply controls at the program level, you must use [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/cc-get-started).
</Callout>

## Related topics

[Simulate flex control creation](https://developers.pismo.io/pismo-docs/docs/simulate-flex-control-creation)

[Flex controls use cases](https://developers.pismo.io/pismo-docs/docs/flex-controls-use-cases)

[Attribute groups](https://developers.pismo.io/pismo-docs/docs/attribute-groups)
<!-- source:end -->

### Source 2: `docs/core-platform/flex-controls-examples.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/flex-controls-examples · updatedAt: 2026-10-01T00:21:11.000Z

<!-- source:begin path=docs/core-platform/flex-controls-examples.md part=0-end -->

# Flex controls examples

The following examples show common flex control implementation scenarios that can be created with the [Create account flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls)  and [Create customer flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-customers-flex-controls)  endpoints.

## Deny purchase by merchant category

This example denies purchases by merchant category code (MCC) for airlines carriers (4511) and travel agencies/tour operators (4722). The flex control evaluates and restricts a purchase when the `4511` and `4722` values are present in the request.

In this type of restrictive flex control,`type` is set to `restriction` and the following `conditions` are defined.

* `"attribute": "merchant_category_code"`
* `"operator": "in"` means "include". This setting causes the Pismo platform to return `true` if  `merchant_category_code` is equal to any of the MCC codes listed  in `value`.
* `"value": "4511, 4722"` lists applicable MCC codes.

```json JSON
{
    "id": "ecd6a1e7-a283-49d6-aa88-d8f4a9601f7b",
    "type": "restriction",
    "name": "restrict_airlines_and_travel",
    "conditions": [
        {
            "id": "950b76b9-eefb-41be-bde7-ef82a8c11821",
            "attribute": "merchant_category_code",
            "operator": "in",
            "value": "4511,4722"
        }
    ],
    "deny_code": "RESTRICT_BY_MCC",
    "active": true,
    "customized": true
}
```

## Deny purchase by entry mode

This example denies purchases by entry mode for contactless purchases on a terminal that is not capable of receiving a password. The entry mode in this case is `072`, where the first two characters `07` indicate contactless mode, and the third character `2` indicates that the terminal doesn't have PIN entry capability.

```json JSON
{
    "type": "restriction",
    "name": "restrict_purchase_contactless",
    "conditions": [
        {
            "attribute": "entry_mode",
            "operator": "eq",
            "value": "072"
        }
    ],
    "deny_code": "RESTRICT_BY_ENTRY_MODE",
    "active": true
}
```

## Define maximum usage limit

This example creates a maximum usage flex control for limiting the quantity of purchases per month to 100 transactions. The processing code `00` references purchase transactions.

```json
{
  "type": "usage_limit",
  "name": "limit_purchase_per_month",
  "processing_codes": [
    "00"
  ],
  "max_limit": 100,
  "limit_duration": "P1M",
  "deny_code": "MAX_USAGE_P1M",
  "active": true
}
```

## Restrict purchase authorizations within a time window

This example denies purchases made between 11:00 PM and 07:00 AM.

```json
{
  "type": "restriction",
  "name": "restrict_purchase",
  "description": "Deny purchases between 11:00 PM and 07:00 AM",
  "processing_codes": [
    "00"
  ],
  "conditions": [
     {
      "attribute": "time_now",
      "operator": "in",
      "value": "11:00PM-07:00AM"
    }
  ],
  "deny_code": "RESTRICT_BY_TIME",
  "active": true
}
```

## Limit the quantity of purchase transactions within a time window

This example limits the number of purchases to 10 transactions between 11:00 PM to 07:00 AM.

```json
{
  "type": "usage_limit",
  "name": "limit_purchase_night",
  "description": "Limit purchases to 10 transactions between 11:00 PM to 07:00 AM",
  "processing_codes": [
    "00"
  ],
  "conditions": [
    {
      "attribute": "time_now",
      "operator": "in",
      "value": "11:00PM-07:00AM"
    }
  ],
  "max_limit": 10,
  "limit_duration": "P1D", 
  "reset_period": 
    { 
       "time": "10:59PM" 
    },
  "deny_code": "MAX_USAGE_PURCHASE_NIGHT",
  "active": true
}
```

## Create flex control per transaction type

Use the `processing_codes` filter for the following purposes.

* Evaluate a flex control for a certain transaction type.
* Apply a flex control to several transaction types.
* Create different flex controls for different transaction types.

The following example creates a flex control for purchase (`00`) and withdrawal (`01`) transactions.

```json
{
  "type": "spending_limit",
  "name": "limit_amount_purchase",
  "processing_codes": [
    "00", "01"
  ],
  "max_limit": 49999,
  "limit_duration": "P1M",
  "deny_code": "MAX_VALUE_AMOUNT_P1M",
  "active": true
}
```

## Create flex control for a beneficiary overriding existing controls

This example does the following.

* Creates flex control for an account.
* Defines a beneficiary.
* Lists existing controls that the new spending control overrides.

```json
{
  "type": "spending_limit",
  "name": "Purchase 1 Month credit card",
  "beneficiary_id": "a10efbf9-e67c-4c3c-b52c-d1218427a81b",
  "override_controls": [
    "9186bafe-a077-4cab-bc42-08db41410d52",
    "12565ce9-050f-41d5-8c63-8d1a13c817ae"
  ],
  "processing_codes": [
    "007000"
  ],
  "max_limit": 49999,
  "limit_duration": "P1M",
  "deny_code": "MAX_VALUE_P1M",
  "active": true
}
```

## Pix and accounts

If you want to enable a different time range and limit for each account, set up the following control using the [Update account flex control](https://developers.pismo.io/pismo-docs/reference/patch-v1-accounts-flex-control) endpoint. In this example, the start time is changed from 8 PM to 10 PM and the limit is decreased from R$1,000 to R$500 for a specific account:

```json
{  
    "conditions": [  
        {  
            "id": "1c61caa5-ab07-48dd-9f56-8419090116d6",  
            "attribute": "time_now",  
            "operator": "in",  
            "value": "10:00PM-6:00AM"  
        }  
    ],  
    "max_limit": 50000,  
    "active": true,  
    "customized": true  
}
```

## Related topics

[Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls)

[Simulate flex control creation](https://developers.pismo.io/pismo-docs/docs/simulate-flex-control-creation)

<br />
<!-- source:end -->

### Source 3: `docs/core-platform/simulate-flex-control-creation.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/simulate-flex-control-creation · updatedAt: 2026-10-01T00:15:24.000Z

<!-- source:begin path=docs/core-platform/simulate-flex-control-creation.md part=0-end -->

# Simulate flex control creation

This guide explains how to simulate and verify flexible transaction controls (flex controls) using Postman before applying them in production. By testing controls in a simulated environment, you can confirm that authorization rules restrict or permit transactions as expected without affecting live operations.

# Prerequisites

Before starting this task, ensure you have:

* Installed Postman and imported the Pismo environment and collections as described in the [Access Pismo Postman collections](https://developers.pismo.io/pismo-docs/docs/access-pismo-postman-collections)  guide.
* A valid API client credentials pair with permissions to create accounts, issue cards, and manage flex controls.
* Reviewed the [Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls)  overview guide to understand control types and evaluation logic.

![Graphical diagram displaying steps of simulating flex control creation](https://files.readme.io/89b95d6-diagram-FlexControls-12x.png "diagram-FlexControls-1@2x.png")

## Step 1: Authenticate and set up test entities

Authenticate with the Pismo platform and create the necessary account and card entities to test against.

1. In Postman, open the credit card collection.
2. Select **Platform > Server Authentication** and send the request to generate a server access token.
3. Select **Platform > Acquisitions > Create an application form** and send the request to generate a new test account. Save the returned `account_id`.
4. Select **Enduser > Server Login with Account** and send the request to authenticate on behalf of the account.
5. Select **Enduser > Cards > virtual > Create virtual card** and send the request to issue a virtual card. Save the returned `card_id`.

## Step 2: Verify baseline transaction authorization

Run a baseline transaction to verify that transactions authorize normally before applying any restrictions.

1. In Postman, select **Enduser > Cards > BrandedCardPurchaseSimulator > Branded authorization simulation**.
2. Pass the generated `card_id` and test purchase details in the request payload.
3. Verify that the response returns `response_code: "00"`, confirming that the purchase is authorized without restrictions.

## Step 3: Create a test flex control

Define and apply a restrictive control to evaluate against subsequent purchases.

1. In the Flex controls API, call [List account flex controls](https://developers.pismo.io/pismo-docs/reference/get-v1-accounts-flex-controls)  to list and view existing controls.
2. Call the [Create account flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) endpoint.
3. Pass a restriction payload to block transactions where `entry_mode` equals `051` (chip-and-PIN):
   ```json
   {
     "type": "restriction",
     "name": "restrict-entry-mode-051",
     "description": "Restrict purchase for chipset card",
     "processing_codes": [
       "00"
     ],
     "conditions": [
       {
         "attribute": "entry_mode",
         "operator": "eq",
         "value": "051"
       }
     ],
     "deny_code": "RESTRICT_ENTRY_MODE_051", 
     "active": true
   }
   ```
4. Confirm that the endpoint returns a `201 Created` status with the generated control `id`.

## Step 4: Simulate a restricted authorization

Test that the newly applied flex control intercepts and blocks the transaction.

1. Refer to [Simulate authorizations](https://developers.pismo.io/pismo-docs/docs/simulate-authorizations) for information on building a test transaction.
2. Call the [Simulate authorization](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations) endpoint.
   ```json
   {
     "card_id": "12345667890",
     "local_amount": 50,
     "local_currency": "986",
     "settlement_amount": 50,
     "entry_mode": "051",
     "merchant": {
       "name": "Wolley's Wool",
       "city": "New York",
       "country": "USA"
     },
     "processing_code": "00",
     "mti": "0100",
     "account_type": "20",
     "invoice_address": "101 Main St, City",
     "authorization_code": "123456"
   }
   ```
3. Verify that the transaction is declined.

## Next steps

1. Call the [List account flex controls](https://developers.pismo.io/pismo-docs/reference/get-v1-accounts-flex-controls)  to inspect all active controls assigned to the account.
2. If control parameters need adjustments, call the [Update account flex control](https://developers.pismo.io/pismo-docs/reference/patch-v1-accounts-flex-control)  endpoint.

## Related topics

[Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls)

[Access Pismo Postman collections](https://developers.pismo.io/pismo-docs/docs/access-pismo-postman-collections)

[Flex controls use cases](https://developers.pismo.io/pismo-docs/docs/flex-controls-use-cases)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/accounts/{accountId}/flex-controls` | `post-v1-accounts-flex-controls` | Create account flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /v1/customers/{customerId}/flex-controls` | `post-v1-customers-flex-controls` | Create customer flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--customer-flex-controls-part-01 |
| `PATCH /v1/accounts/{accountId}/flex-controls/{flexControlId}` | `patch-v1-accounts-flex-control` | Update account flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `GET /v1/accounts/{accountId}/flex-controls` | `get-v1-accounts-flex-controls` | List account flex controls | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /networktransactions/v1/authorizations` | `post_v1-authorizations` | Simulate authorization | `api-specs/Card_issuing_-_Authorization.yaml` | no | KU-API-card-issuing-authorization--authorizations |

### Operation essentials

- **`POST /v1/accounts/{accountId}/flex-controls`** (`post-v1-accounts-flex-controls`): security `BearerAuth`; required parameters `accountId` (path); required body fields `type`, `name`, `deny_code`; response statuses 201, 400, 403, 409, 500; error codes in examples `ERUL0701`, `RULVAL0400`, `ERUL0702`, `ERUL0703`, `ERUL0704`, `ERUL0706`, `ERUL0004`, `ERUL0002`, `RULVAL0403`, `WRUL0707`, `RULVAL0409`, `ERUL0001`, `RULREP0500`; events `audit-account-spending-limit-created-1`.
- **`POST /v1/customers/{customerId}/flex-controls`** (`post-v1-customers-flex-controls`): security `BearerAuth`; required parameters `customerId` (path); required body fields `type`, `name`, `account_id`; response statuses 201, 400, 403, 409, 500; error codes in examples `ERUL1101`, `RULVAL0400`, `ERUL1102`, `ERUL1106`, `ERUL0002`, `RULVAL0403`, `WRUL1207`, `RULVAL0409`, `ERUL0005`, `RULREP0500`, `ERUL1105`; events `audit-customer-spending-limit-created-1`.
- **`PATCH /v1/accounts/{accountId}/flex-controls/{flexControlId}`** (`patch-v1-accounts-flex-control`): security `BearerAuth`; required parameters `accountId` (path), `flexControlId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `ERUL1001`, `RULVAL0400`, `ERUL1002`, `ERUL1003`, `ERUL1004`, `ERUL1005`, `ERUL1006`, `ERUL1007`, `ERUL0003`, `RULREP0404`, `ERUL0001`, `RULREP0500`; events `audit-account-spending-limit-updated-1`.
- **`GET /v1/accounts/{accountId}/flex-controls`** (`get-v1-accounts-flex-controls`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `ERUL0801`, `RULVAL0400`, `ERUL0802`, `ERUL0803`, `RULVAL0400`, `ERUL0001`, `RULREP0500`; events none listed.
- **`POST /networktransactions/v1/authorizations`** (`post_v1-authorizations`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events `networktransactions-network-authorization-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-accounts-flex-controls` | `audit-account-spending-limit-created-1` |
| `patch-v1-accounts-flex-control` | `audit-account-spending-limit-updated-1` |
| `post-v1-customers-flex-controls` | `audit-customer-spending-limit-created-1` |
| `post_v1-authorizations` | `networktransactions-network-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/flex-controls.md`: updatedAt 2026-10-01T00:42:59.000Z.
- `docs/core-platform/flex-controls-examples.md`: updatedAt 2026-10-01T00:21:11.000Z.
- `docs/core-platform/simulate-flex-control-creation.md`: updatedAt 2026-10-01T00:15:24.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/flex-controls.md` | whole document | https://developers.pismo.io/pismo-docs/docs/flex-controls | `04e61fe396bb4110…` | 2026-10-01T00:42:59.000Z |
| `docs/core-platform/flex-controls-examples.md` | whole document | https://developers.pismo.io/pismo-docs/docs/flex-controls-examples | `b2807be45f9cf0a4…` | 2026-10-01T00:21:11.000Z |
| `docs/core-platform/simulate-flex-control-creation.md` | whole document | https://developers.pismo.io/pismo-docs/docs/simulate-flex-control-creation | `882c045fe3e73bf6…` | 2026-10-01T00:15:24.000Z |

## Related knowledge units

- `KU-API-card-issuing-authorization--authorizations` — API reference: Card issuing - Authorization — Authorizations
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-01` — API reference: Core platform - Flex controls — Customer flex controls (part 1 of 2)
- `KU-CARD-simulate-authorizations` — Simulate authorizations
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CORE-attribute-groups` — Attribute groups
- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-EVT-catalogue-audit` — Event catalogue: audit
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-flex-controls-data-events` — Core platform - Flex controls
- `KU-GS-developer-tooling` — Developer tooling: OpenAPI files, Postman collections and API testing
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
