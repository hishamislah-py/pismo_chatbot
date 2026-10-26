---
ku_id: KU-PAY-transfers-make-and-cancel
title: 'Transfers: making and cancelling transfers'
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/make-transfer.md
  sha256: f25a2f222e1b8b44b5f011013fd21403730d2fbf1109a03fd425216bc3277a1b
  url: https://developers.pismo.io/pismo-docs/docs/make-transfer
  role: primary_guide
  updated_at: '2026-03-31T19:28:09.000Z'
- path: docs/core-platform/cancel-transfer.md
  sha256: 33ca87717def31974d4e43692b6ac53a1713c89f0e91a43b22cdadc0ee41ce3b
  url: https://developers.pismo.io/pismo-docs/docs/cancel-transfer
  role: primary_guide
  updated_at: '2026-03-31T19:28:15.000Z'
operations:
- post-payments-v1-payments
- post-payments-v2-cancel
related_kus:
- KU-API-core-platform-payment-methods--payments
- KU-CARD-digital-wallets
- KU-EVT-catalogue-other-domains
- KU-PAY-payment-methods
grouping_rationale: One workflow (create, then optionally cancel).
---

# Transfers: making and cancelling transfers

**KU ID:** `KU-PAY-transfers-make-and-cancel` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: One workflow (create, then optionally cancel).

Scope as stated in `docs/core-platform/make-transfer.md`:

> You can make a transfer by using the following endpoint. For more information, go to the [API reference](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments).

Scope as stated in `docs/core-platform/cancel-transfer.md`:

> The Payments API provides the POST `payments/v2/cancel` endpoint that allows you to perform:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/make-transfer.md`: How to make transfer; API reference; Transfer (P2P); Sample payload request; Sample response; Response details; Transfer from card; Sample payload request; Sample response; Cash-in; Sample payload request; Sample response; Cash-out; Sample payload request; Sample response
- `docs/core-platform/cancel-transfer.md`: How to cancel transfer; Cancel transfer payload request; Total cancellation; Partial cancellation; Example; Original cash-in request; Original cash-in response; Partial cancellation request of the cash-in; Partial cancellation response

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/make-transfer.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/make-transfer · updatedAt: 2026-03-31T19:28:09.000Z

<!-- source:begin path=docs/core-platform/make-transfer.md part=0-end -->

# How to make transfer

> 📘
>
> For any new deployments, the recommendation is to use the enhanced [Payment methods](https://developers.pismo.io/pismo-docs/docs/payment-methods) API instead of the [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) endpoint described in this guide. All new feature developments will be available only in the Payment methods API. For more information, contact your Pismo representative.

# API reference

You can make a transfer by using the following endpoint. For more information, go to the [API reference](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments).

```json
POST <URL>payments/v1/payments
```

# Transfer (P2P)

To perform a transfer of funds between two accounts inside the Pismo platform using the account balance:

* in the `from` object, provide the `account id` of the source Pismo account.
* in the `to` object, provide the `account id` of the destination Pismo account.

![Image showing a result of a transfer.](https://files.readme.io/4d17cbd-payments-p2p2x.png "payments-p2p@2x.png")

| Request payload        | Response                  |
| :--------------------- | :------------------------ |
| *(A) - from*           | *(H) - event\_date*       |
| *(B) - to*             | *(I) - authorization\_id* |
| *(C) - account id*     |                           |
| *(D) - amount*         |                           |
| *(E) - currency*       |                           |
| *(F) - payment method* |                           |
| *(G) - metadata*       |                           |

## Sample payload request

```json P2P sample payload request
{
   "tracking_id":"2436f48b-d57d-472c-aea4-47581a492502",
   "descriptor":"P2P payment",
   "from":[
      {
         "amount":150,
         "currency":"USD",
         "account":{
            "id":125487
         }
      }
   ],
   "to":[
      {
         "account":{
            "id":126789
         }
      }
   ],
   "metadata":{
      "source":"account balance",
      "message":"Sunday's barbecue share"
   }
}
```

## Sample response

```json P2P sample response
{
   "authorization_id": 31042116,
   "authorization_ids": {
     "credit": 31042117,
     "debit": 31042116
     },
   "available_credit_limit": 1874.68,
   "event_date": "2022-01-12T12:16:17.646Z",
   "tracking_id": "b970c8a9-5ec9-4e46-8c0d-f411e0bd6ce7"
}
```

## Response details

| Field                      | Type   | Description                                                                      |
| :------------------------- | :----- | :------------------------------------------------------------------------------- |
| `tracking_id`              | string | The identifier provided or the one generated by Pismo.                           |
| `event_date`               | string | The date and time of the moment the transaction was successfully made, in UTC-0. |
| `authorization_ids`        | object | The credit and debit authorization identifiers.                                  |
| `authorization_ids.credit` | number | The credit authorization identifier.                                             |
| `authorization_ids.debit`  | number | The debit authorization identifier.                                              |
| `metadata`                 | object | The metadata returned from the acquirer, if applicable.                          |

***

# Transfer from card

To perform a transfer from a card that was previously registered in the [wallet](https://developers.pismo.io/pismo-docs/docs/wallet-overview) to an account within the Pismo platform, you must:

* in the `from` object, provide the card's unique identifier, `card_uuid`, and the `account id` that the card is bound to.
* in the `to` object, provide the `account id` of the destination Pismo account.

![Image showing the parts of the transfer on a mobile phone. ](https://files.readme.io/62ee8b0-payments-p2p-withCard2x.png "payments-p2p-withCard@2x.png")

| Request payload      | Response                  |
| :------------------- | :------------------------ |
| *(A) - from*         | *(H) - event\_date*       |
| *(B) to*             | *(I) - authorization\_id* |
| *(C) account id*     |                           |
| *(D) amount*         |                           |
| *(E) currency*       |                           |
| *(F) payment method* |                           |
| *(G) metadata*       |                           |

## Sample payload request

```json Transfer from card sample request
{
  "descriptor": "P2P payment with card",
  "from": [
    {
      "amount": 150,
      "currency": "USD",
      "card": {
        "id": "f45dbe01-4109-11ea-ab1d-3286e4ea7ade",
        "account_id": 5487
      }   
    }
	],
  "to": [
    {
      "account": {
        "id": 126789
      }
    }
  ],
  "metadata": {
    "source": "account balance",
    "message": "Sunday's barbecue share"
  }
}
```

## Sample response

```json Transfer from card sample response
{
    "authorization_id": 31042111,
    "authorization_ids": {
      "credit": 31042112,
      "debit": 31042111
      },
    "event_date": "2022-01-12T12:11:58.952Z",
    "metadata": {
      "authorization_code": "154856",
      "nsu": "893681195173",
      "tid": "13042201120912190001"
      },
    "tracking_id": "1641989519"
}
```

***

# Cash-in

A cash-in operation moves funds from an external party into an account on the Pismo platform. To perform cash-in operations, you need to:

* in the `to` object, provide the `account ` object that contains a valid Pismo account id.
* in the `from` object, provide the `custom_info` object that contains the `type` of the operation.

![Image showing the parts of the transfer on a mobile phone. ](https://files.readme.io/bb5ce9a-payments-cashinBankTransfer2x.png "payments-cashinBankTransfer@2x.png")

| Request payload         | Response                  |
| :---------------------- | :------------------------ |
| *(A) - to*              | *(F) - event\_date*       |
| *(B) - account id*      | *(G) - descriptor*        |
| *(C) - account balance* | *(H) - metadata*          |
| *(D) - descriptor*      | *(I) - authorization\_id* |
| *(E) - amount*          |                           |

## Sample payload request

```json Cash-in sample request
{
	"descriptor": "BANK TRANSFER",
	"from": [
		{
			"custom_info": {
				"type": "CASHIN",
				"external_id": "be6474e8-b849-4213-9e1f-bdf619a27a63"
			}
		}
	],
	"to": [
		{
			"amount": 150,
      "currency": "USD",
			"account": {
				"id": 105708
			}
		}
	],
  "metadata":{
    "sender": "Andrew Foster",
    "bank": "OneBank",
    "branch_code": "0089",
    "account_id": "13000-7"
  }
}
```

## Sample response

```json Cash-in sample response
{
   "authorization_id": 31042107,
   "authorization_ids": {
     "credit": 31042107,
     "debit": null
     },
   "available_credit_limit": 1200.00,
   "event_date": "2022-01-12T12:06:06.377Z",
   "status_code": 1,
   "tracking_id": "63c8f39c-6a79-4250-ad33-34b89f28deff"
}
```

***

# Cash-out

To perform cash-out operations using the account balance, you need to:

* in the `from` object, provide the `account` object that contains a valid Pismo account id.
* in the `to` object, provide the `custom_info` object that contains the `type` of the operation you are performing.

The `custom_info` object allows multiple possibilities, such as withdrawing funds, topping up mobile devices, paying registered bills, and more.

![Image showing the parts of the transfer on a mobile phone. ](https://files.readme.io/6ffbeff-payments-withdrawal2x.png "payments-withdrawal@2x.png")

| Request payload        | Response                  |
| :--------------------- | :------------------------ |
| *(A) - from*           | *(F) - event\_date*       |
| *(B) - currency*       | *(G) - descriptor*        |
| *(C) - amount*         | *(H) - metadata*          |
| *(D) - payment method* | *(I) - authorization\_id* |
| *(E) - entry\_mode*    |                           |

## Sample payload request

```json Cash-out sample request
{
  "descriptor": "ATM's withdrawal",
  "from": [
    {
      "amount": 50.00,
      "currency": "USD",
      "account": {
        "id": 125487,
      }
    }
  ],
  "to": [
    {
      "custom_info": {
        "type": "WITHDRAWAL",
        "external_id": "2343646-2139867-09897776"
      }
    }
  ]
}
```

***

# Sample response

```json Cash-out sample response
{
  "authorization_id": 31042110,
  "authorization_ids": {
    "credit": null,
    "debit": 31042110
    },
  "available_credit_limit": 1875.68,
  "event_date": "2022-01-12T12:09:26.627Z",
  "tracking_id": "eea76b3c-46c0-4c6c-9312-27e9ee48acbf"
}
```
<!-- source:end -->

### Source 2: `docs/core-platform/cancel-transfer.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cancel-transfer · updatedAt: 2026-03-31T19:28:15.000Z

<!-- source:begin path=docs/core-platform/cancel-transfer.md part=0-end -->

# How to cancel transfer

> 📘
>
> For any new deployments, the recommendation is to use the enhanced [Payment methods](https://developers.pismo.io/pismo-docs/docs/payment-methods) API instead of the  [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-payments-v2-cancel) endpoint described in this guide. All new feature developments will be available only in the Payment methods API. For more information, contact your Pismo representative.

The Payments API provides the POST `payments/v2/cancel` endpoint that allows you to perform:

* a [total cancellation](https://developers.pismo.io/pismo-docs/docs/cancel-transfer#total-cancellation) of a previously authorized transfer, which fully reverts the transaction and restores balances of the sender and receiver accounts.
* a [partial cancellation](https://developers.pismo.io/pismo-docs/docs/cancel-transfer#partial-cancellation) of a previously authorized transfer, which cancels a portion of the original transaction.

> 📘
>
> A cancellation operation has its own logic and internal controls that follow different flows from the operations performed on the `payments/v1/payments` endpoint. For example, performing a cash-out transaction to revert a cash-in transaction with the `payments/v1/payments` endpoint is different from performing a cancellation transaction with the `payments/v2/cancel` endpoint to cancel the original cash-in. The cash-out will be considered a new transfer that is not related to the cash-in performed previously.

![Image showing the results of cancelling a payment on a mobile phone. ](https://files.readme.io/7f7599f-payments-cancel2x.png "payments-cancel@2x.png")

|                                            |                                          |
| :----------------------------------------- | :--------------------------------------- |
| *(A) - from*                               | *(G) - event\_date*                      |
| *(B) - account id*                         | *(H) - status after cancellation*        |
| *(C) - account balance after cancellation* | *(I) - original transaction information* |
| *(D) - calculated by event\_date*          | *(J) - original authorization\_id*       |
| *(E) - descriptor*                         |                                          |
| *(F) - amount to cancel*                   |                                          |

<Callout icon="📘" theme="info">
  * In transactions with cards on file (COF), the platform sends the refund operation to the acquirer to reverse the transaction on the card.
  * In transactions made for a merchant, the platform posts a debit to the merchant's schedule, corresponding to the original transaction.
</Callout>

# Cancel transfer payload request

To cancel a previously authorized transfer that was made with the [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) (`payments/v1/payments`) endpoint, use the [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-payments-v2-cancel) (`payments/v2/cancel`) endpoint.

```json
POST <URL>payments/v2/cancel
```

1. Identify the original transfer either by its `tracking_id` or the `authorization_id`.
2. In the cancellation request, pass the following required fields to the [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-payments-v2-cancel) endpoint.
   * either the `original_tracking_id` or the `authorization_id` to identify the original transfer.
   * the `amount` to be canceled.

The complete list of parameters and their details are provided in the [API reference](https://developers.pismo.io/pismo-docs/reference/post-payments-v2-cancel).

## Total cancellation

To make a total cancellation of a previously authorized transfer, provide the original authorization identifier and the same value amount as in the original authorization.

For example, if the original transfer amount was $100 and it generated the `authorization_id` of `15301234`, pass the following parameters in the cancellation payload request:

```json Total cancellation request
{
  "authorization_id": 15301234, 
  "amount": 100.0
}
```

By default, if there are any fees associated with the original transfer, when you perform a total cancellation, the Pismo platform cancels the fees automatically (`cancel_fees` field is `true`).  If you don't want the fees to be cancelled, set the `cancel_fees` field to `false`.

## Partial cancellation

To partially cancel a previously authorized transfer, provide the value amount that is less than the amount of the original authorization. For example, if the original transfer amount was $85, its `tracking_id` was `unique-uuid-12345`, and you'd like to make the partial cancellation of $50.00, pass the following parameters in the cancellation payload request:

```json Partial cancellation request
{
  "original_tracking_id": "unique-uuid-12345", 
  "amount": 50.0
}
```

If the above request returns a successful response, there will be $35.00 remaining that can still be canceled. The Pismo platform controls the outstanding cancellation balance. If the sum of partial cancellations exceeds the total amount of the original transaction, the platform denies a partial cancellation attempt to ensure integrity.

By default, if there are any fees associated with the original transfer, when you perform a partial cancellation, the Pismo platform does not cancel the fees automatically (`cancel_fees` field is `false`).  If you want the fees to be cancelled, set the `cancel_fees` field to `true`.

## Example

The following example shows how to perform a partial cancellation of the original cash-in transfer and to cancel any associated fees.

### Original cash-in request

The request to [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) (`payments/v1/payments`) identifies the `amount` of the original cash-in transfer as $100.

```json Original request
{
  "descriptor": "DESCRIPTOR CASH-IN",
  "from": [
    {
      "custom_info": {
        "type": "DEPOSIT",
        "external_id": "my-external-id-test-01"
      }
    }
  ],
  "to": [
    {
      "amount": 100,
      "account": {
        "id": 12387
      }
    }
  ]
}
```

### Original cash-in response

The original cash-in transfer response from the [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) (`payments/v1/payments`) provides the `tracking_id` that you can use in the subsequent cancellation request.

```json Original response
{
   "authorization_id": 31251246,
   "authorization_ids": {
   "credit": 31251246,
   "debit": null
},
   "available_credit_limit": 1403.35,
   "event_date": "2022-01-19T01:11:38.783Z",
   "status_code": 1,
   "tracking_id": "6c078af3-4510-4511-b60d-502db9a6c0c9"
}
```

### Partial cancellation request of the cash-in

To cancel $50 of the original cash-in transfer and all associated fees, provide the following in the request to the [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-payments-v2-cancel) (`payments/v2/cancel`) endpoint:

* `original_tracking_id`, which contains  `tracking_id` returned by the original cash-in response
* partial cancellation value of $50 in the `amount` field
* `cancel_fees` field set to `true`

```json Cancellation request
{
  "original_tracking_id": "6c078af3-4510-4511-b60d-502db9a6c0c9",
  "amount": 50,
  "cancel_fees": true
}
```

### Partial cancellation response

```json Cancellation response
{
  "tracking_id": "08bcbccc-4dae-4c0b-8a67-1b0cf245ab44",
  "authorization_datetime": "2023-01-02T15:04:05.000Z",
  "authorization_ids": {
    "credit": 0,
    "debit": 16647083
  },
  "metadata": {
    "my-custom-key": "my-custom-value"
  }
}
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /payments/v1/payments` | `post-payments-v1-payments` | Transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /payments/v2/cancel` | `post-payments-v2-cancel` | Cancel transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |

### Operation essentials

- **`POST /payments/v1/payments`** (`post-payments-v1-payments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `from`, `to`; response statuses 201, 202, 400, 409, 422, 500, 502; error codes in examples `WP2P0000`, `WP2P0019`, `EP2P9999`, `WP2P0005`, `WP2P0006`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WP2P0020`, `WP2P0013`, `WLDG0006`, `WP2P0010`, `WP2P0000`, `WP2P0000`, `ELDG500`, `EPCG501`, `EP2P9999`, `EP2P0001`, `EP2P0002`; events `authorization-authorization-event-1`.
- **`POST /payments/v2/cancel`** (`post-payments-v2-cancel`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `amount`; response statuses 200, 202, 208, 400, 404, 409, 500, 502; error codes in examples `AMON0004`, `WP2P0009`, `WP2P0000`, `AMON0000`, `WP2P0000`, `WP2P1005`, `EP2P0005`, `WP2P1111`, `EP2P0011`, `EP2P0013`, `WP2P0003`, `EP2P9999`, `WP2P3003`, `WP2P0033`, `WP2P0008`, `WP2P0000`, `WLDG0019`, `WLDG0004`, `WLDG0006`, `WLDG0005`, `WP2P0010`, `AMON0004`, `WP2P0009`, `WP2P0000`, `WP2P0000`, `ACQ0001`, `ACQ0000`, `EP2P9999`, `ELDG500`, `EP2P0001`; events `authorization-authorization-cancellation-event-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v2-cancel` | `authorization-authorization-cancellation-event-1` |
| `post-payments-v1-payments` | `authorization-authorization-event-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/make-transfer.md`: updatedAt 2026-03-31T19:28:09.000Z.
- `docs/core-platform/cancel-transfer.md`: updatedAt 2026-03-31T19:28:15.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/make-transfer.md` | whole document | https://developers.pismo.io/pismo-docs/docs/make-transfer | `f25a2f222e1b8b44…` | 2026-03-31T19:28:09.000Z |
| `docs/core-platform/cancel-transfer.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cancel-transfer | `33ca87717def3197…` | 2026-03-31T19:28:15.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-CARD-digital-wallets` — Digital wallets, MDES Token Connect and Click to Pay
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-payment-methods` — Payment methods
