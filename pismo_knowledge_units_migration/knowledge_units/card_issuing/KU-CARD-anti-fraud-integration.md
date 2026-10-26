---
ku_id: KU-CARD-anti-fraud-integration
title: Anti-fraud integration
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/anti-fraud-integration.md
  sha256: 3d36be126a0a84f2f195b632bae61bf5f14552cfe8f524dd2091b80d8a809a43
  url: https://developers.pismo.io/pismo-docs/docs/anti-fraud-integration
  role: primary_guide
  updated_at: '2026-04-02T15:24:31.000Z'
operations:
- postPreAuthenticate
related_kus:
- KU-API-card-issuing-3ds-authentication--pre-authentication
- KU-CARD-full-and-zero-balance-workflows
- KU-CARD-pan-encryption-for-3ds-authentication
- KU-CARD-zero-balance-integration
- KU-ERR-validation-codes-for-authorization-events-part-01
- KU-ERR-validation-codes-for-authorization-events-part-02
- KU-EVT-client-webhooks-part-01
- KU-EVT-client-webhooks-part-02
- KU-EVT-client-webhooks-part-03
- KU-EVT-client-webhooks-part-04
- KU-EVT-client-webhooks-part-05
- KU-EVT-client-webhooks-part-06
- KU-EVT-client-webhooks-part-07
- KU-EVT-client-webhooks-part-08
- KU-EVT-client-webhooks-part-09
- KU-EVT-client-webhooks-part-10
- KU-EVT-client-webhooks-part-11
- KU-EVT-client-webhooks-part-12
- KU-EVT-client-webhooks-part-13
- KU-EVT-client-webhooks-part-14
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Anti-fraud integration

**KU ID:** `KU-CARD-anti-fraud-integration` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/anti-fraud-integration.md`:

> The Pismo platform can integrate with third-party fraud prevention systems to enable security checks on customer transactions. This is done through configuring the anti-fraud call to Full balance customers' webhook during step 5 in the [Full and zero balance workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).  For Zero balance integration, see [Zero balance anti-fraud and validations integration](https://developers.pismo.io/pismo-docs/docs/zero-balance-anti-fraud-integration-1).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/anti-fraud-integration.md`: Anti-fraud integration; Anti-fraud webhook; Workflow; Per-program settings; Overwrite the Pismo platform decision; Overwrite the Pismo platform decision only for the current request; Example response

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/anti-fraud-integration.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/anti-fraud-integration · updatedAt: 2026-04-02T15:24:31.000Z

<!-- source:begin path=docs/card-issuing/anti-fraud-integration.md part=0-end -->

# Anti-fraud integration

The Pismo platform can integrate with third-party fraud prevention systems to enable security checks on customer transactions. This is done through configuring the anti-fraud call to Full balance customers' webhook during step 5 in the [Full and zero balance workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).  For Zero balance integration, see [Zero balance anti-fraud and validations integration](https://developers.pismo.io/pismo-docs/docs/zero-balance-anti-fraud-integration-1).

> 📘 3DS/ACS validation
>
> For <a href="https://en.wikipedia.org/wiki/Card_not_present_transaction" target="_blank">card-not-present transactions</a>, Pismo recommends, but does not require, that a third-party <a href="https://en.wikipedia.org/wiki/3-D_Secure" target="_blank">3DS/ACS</a> validator be used. Pismo provides an endpoint - [Send pre-authentication info](https://developers.pismo.io/pismo-docs/reference/postpreauthenticate) - for third-party validators to get encrypted card information they can use during the validation process.
>
> For details on encrypting the PAN for use with the Send pre-authentication info endpoint, refer to the [PAN encryption for 3DS authentication](https://developers.pismo.io/pismo-docs/docs/pan-encryption-for-3ds-authentication) guide.

# Anti-fraud webhook

If you choose to implement anti-fraud integration, you need to register an anti-fraud webhook for this purpose during setup. The [Client webhooks](https://developers.pismo.io/pismo-docs/docs/client-webhooks) guide contains detailed specifications for ALL anti-fraud webhooks you can code to interact with Pismo platform operations. Note that this integration is totally optional. If not present, Pismo responds to the network with its own results.

# Workflow

The Pismo authorization process performs all stateless and stateful [validations](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events), assembles a request with the transaction data, and makes an HTTPS call to the webhook URL you specified during setup.

> 📘 Webhook request URL
>
> To change the URL at any time, open a [Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk) request.

The response you need to send to the Pismo platform is defined in the [Full balance anti-fraud integration](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook) webhook request specification, so that the platform can interpret and use the anti-fraud system's decision. This functionality enables you to integrate with any risk analysis provider at authorization time, making it possible to deny a purchase the platform approved.

> 🚧 Anti-fraud timeout - 2 seconds
>
> If the Pismo platform does not receive a valid response from your anti-fraud system within two seconds, the request times out. In this case, the authorization proceeds with Pismo's validation, which is then considered final.

# Per-program settings

The following settings can be defined on a program level. The settings below impact transactions that use a card related to a program. To activate these settings, [open a Service Desk ticket](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket) with Pismo.

> 📘 Program anti-fraud
>
> You can configure a different anti-fraud webhook for each program you create.

## Overwrite the Pismo platform decision

If the overwrite Pismo platform decision setting is active, your anti-fraud system's decision is final. In this case, the only restriction is that it must be a Pismo-managed card. If the card is not found in the Pismo database, there is no way to approve this transaction.

To enable this setting, you must open a service request with the authorization team. After enabling this setting, the final decision about approving or declining the purchase is always the anti-fraud response.

<Callout icon="❗️" theme="error">
  This overwrite platform decision setting must be analyzed thoroughly before being enabled since it allows the anti-fraud system to reverse an authorization denied by any of the validations performed by the Pismo platform.
</Callout>

**If the overwrite platform decision setting is active**, the authorization process performed by the Pismo platform denies the transaction, but the anti-fraud system approves the transaction, then the Pismo platform responds that the transaction is approved.

> 📘 Forced approval and ledger update
>
> If you force an approval, the `ledger_update_id` field is not sent in the network authorization events because the ledger update is being done in parallel.

## Overwrite the Pismo platform decision only for the current request

Your anti-fraud system can also overwrite a Pismo platform decision to force an approval for a specific transaction. This feature allows the anti-fraud system to approve an operation that Pismo previously declined  in a more granular manner, since it only applies to the current transaction. This feature doesn't require any parameter to be enabled in the platform and doesn't impact all requests, giving the anti-fraud system the option to decide when to overwrite a decision at the request level.

When forcing an approval, the authorization system responds to the request as approved even if  Pismo declines it. Forcing an approval impacts the account limit and makes it negative if the available funds are not sufficient to cover the requested amount.

To force an approval, your anti-fraud system must set `approve` and `force_approve`  to `true` in the response.  Setting `approve` to `true` does not override a Pismo-declined transaction, so both fields are necessary.

> 📘 Note about forced approval
>
> If the platform declines an operation because a card is not found, this operation can't be force approved since the platform can't connect this request with any account. In this case, the operation will remain declined even with the `force_approve` flag in the response.

## Example response

Below is an example of a response that Pismo receives from an anti-fraud system:

```json
{
    "approve": true,
    "force_approve": false,
    "response_code": "00",
    "metadata": {
        "custom_field_1": null,
        "custom_field_2": true,
        "custom_field_3": "Test",
        "custom_field_4": "2021-05-14 23:10:59",
        "custom_field_5": 10,
        "custom_field_6": {
          "custom_field_6_sf1": 10,
          "custom_field_6_sf2": false,
          "custom_field_6_sf3": null,
          "custom_field_6_sfN": "custom_field_6_sfN"
        },
        "custom_field_7": [
          "VALUE_1",
          "VALUE_2",
          "VALUE_N"
        ],
        "custom_field_N": ""
     },
}
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/preauthenticate` | `postPreAuthenticate` | Send pre-authentication info | `api-specs/Card_issuing_-_3DS_authentication.yaml` | no | KU-API-card-issuing-3ds-authentication--pre-authentication |

### Operation essentials

- **`POST /v1/preauthenticate`** (`postPreAuthenticate`): security not declared; required parameters none declared; required body fields `id`, `pan`; response statuses 200, 400, 422, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/card-issuing/anti-fraud-integration.md`: updatedAt 2026-04-02T15:24:31.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/anti-fraud-integration.md` | whole document | https://developers.pismo.io/pismo-docs/docs/anti-fraud-integration | `3d36be126a0a84f2…` | 2026-04-02T15:24:31.000Z |

## Related knowledge units

- `KU-API-card-issuing-3ds-authentication--pre-authentication` — API reference: Card issuing - 3DS authentication — Pre-authentication
- `KU-CARD-full-and-zero-balance-workflows` — Full and Zero balance transaction workflows
- `KU-CARD-pan-encryption-for-3ds-authentication` — PAN encryption for 3DS authentication
- `KU-CARD-zero-balance-integration` — Zero balance integration and anti-fraud validations
- `KU-ERR-validation-codes-for-authorization-events-part-01` — Validation codes for authorization events (part 1 of 2)
- `KU-ERR-validation-codes-for-authorization-events-part-02` — Validation codes for authorization events (part 2 of 2)
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-EVT-client-webhooks-part-02` — Client webhooks (part 2 of 14)
- `KU-EVT-client-webhooks-part-03` — Client webhooks (part 3 of 14)
- `KU-EVT-client-webhooks-part-04` — Client webhooks (part 4 of 14)
- `KU-EVT-client-webhooks-part-05` — Client webhooks (part 5 of 14)
- `KU-EVT-client-webhooks-part-06` — Client webhooks (part 6 of 14)
- `KU-EVT-client-webhooks-part-07` — Client webhooks (part 7 of 14)
- `KU-EVT-client-webhooks-part-08` — Client webhooks (part 8 of 14)
- `KU-EVT-client-webhooks-part-09` — Client webhooks (part 9 of 14)
- `KU-EVT-client-webhooks-part-10` — Client webhooks (part 10 of 14)
- `KU-EVT-client-webhooks-part-11` — Client webhooks (part 11 of 14)
- `KU-EVT-client-webhooks-part-12` — Client webhooks (part 12 of 14)
- `KU-EVT-client-webhooks-part-13` — Client webhooks (part 13 of 14)
- `KU-EVT-client-webhooks-part-14` — Client webhooks (part 14 of 14)
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
