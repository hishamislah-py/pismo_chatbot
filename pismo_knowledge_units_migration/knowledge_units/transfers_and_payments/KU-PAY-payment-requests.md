---
ku_id: KU-PAY-payment-requests
title: Payment requests
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/payment-requests.md
  sha256: 8a7ef9efd5e8e3447d0c14f27562c82a92e6a557629db8018ba40e211a559ad8
  url: https://developers.pismo.io/pismo-docs/docs/payment-requests
  role: primary_guide
  updated_at: '2026-03-18T15:13:13.000Z'
operations:
- get-payments-v1-payment-requests
- post-payments-v1-payment-requests
- post-payments-v1-payments
related_kus:
- KU-API-core-platform-payment-methods--payment-requests
- KU-API-core-platform-payment-methods--payments
- KU-EVT-catalogue-other-domains
- KU-PAY-payments
- KU-PAY-transfers-make-and-cancel
grouping_rationale: single source page
---

# Payment requests

**KU ID:** `KU-PAY-payment-requests` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/payment-requests.md`:

> The Pismo platform enables you to give users an easy way to send payment requests to their peers, such as splitting the barbecue bill or reminding a friend about a group birthday present. Payment requests can be set to expire, contain personalized messages, and more.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/payment-requests.md`: Payment requests; Send a payment request; API reference; Sample payload request; Sample response; Confirm a payment request; Sample payload request; List all payment requests; Related pages

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/payment-requests.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/payment-requests · updatedAt: 2026-03-18T15:13:13.000Z

<!-- source:begin path=docs/core-platform/payment-requests.md part=0-end -->

# Payment requests

The Pismo platform enables you to give users an easy way to send payment requests to their peers, such as splitting the barbecue bill or reminding a friend about a group birthday present. Payment requests can be set to expire, contain personalized messages, and more.

# Send a payment request

A payment request is essentially a step before a payment transfer. When sending a payment request, the request must contain the required destination `account id` and the `amount` fields and can contain other optional fields such as `expiration date` or `metadata`. In case of success, the response returns a token in the field `code`. You can use this token to further process the transfer. The payment request can be accepted (paid) or declined by the receiver, or even canceled by the sender.

![Image showing the results of a payment request on a mobile phone. ](https://files.readme.io/b2a40c2-payments-request2x.png "payments-request@2x.png")

|                                  |                       |
| :------------------------------- | :-------------------- |
| *(A) sender*                     | *(D) amount*          |
| *(B) account ID of the receiver* | *(E) expiration date* |
| *(C) currency*                   | *(F) metadata*        |

## API reference

You can send a payment request by using the following endpoint. For more information, go to [Create payment request](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payment-requests).

```json
POST <URL>payments/v1/payment-requests
```

## Sample payload request

```json Sample payload request
{
	"amount": 25.50,
	"from":{
    "currency": "USD",
		"account":{
    	"id": 8795
    }
  },
	"to":{
    "currency": "USD",
		"account":{
    	"id": 6789
    }
  },
	"expiration": "2020-02-01T21:22:12.800Z",
	"metadata":{
    "message": "David's birthday present"
  }
}
```

## Sample response

```json Sample response
{
  "type": "TOKEN",
  "code": "c8y4865-7654876-zdfi76-23436k"
}
```

# Confirm a payment request

If you want to confirm a payment request, you need to create a new payment using the following endpoint:

```json
POST <URL>payments/v1/payments
```

In the request, provide the attribute called `token` with the value generated while creating the original payment request. This is the value returned in the `code` field of the  [Create payment request](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payment-requests) endpoint. If the provided token does not exist or if it is expired, your request returns an error 400. For more information on creating a payment, go to [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) .

![Image showing the Confirm payment request on a mobile phone. ](https://files.readme.io/95c7614-payments-request-confirm2x.png "payments-request-confirm@2x.png")

## Sample payload request

```json Sample payload request
{
  "descriptor": "PAYMENT REQUEST ACCEPT",
  "token": "c8y4865-7654876-zdfi76-23436k",
  "from": [
    {
      "amount": 25.50,
      "currency": "USD",
      "account": {
        "id": 8795
      }
    }
	],
  "to": [
    {
      "currency": "USD",
      "account": {
        "id": 6789
      }
    }
  ],
  "metadata": [
    {
      "source": "account balance",
      "message": "David's birthday present"
    }
  ]
}
```

# List all payment requests

You can get a list of all payment requests sent from or to a given account by using the following endpoint. For more information, go to [List payment requests](https://developers.pismo.io/pismo-docs/reference/get-payments-v1-payment-requests).

```json
GET <URL>payments/v1/payments-requests
```

Fill in exclusively the `to` or `from` query parameter with a valid `account ID`, according to what kind of payment requests you want to list. For example, `payments/v1/payments-requests?to=6789`.

```json List all payments response example
[
  {
    "amount": 25.50,
    "to": 6789,
    "expiration": "2020-02-01T21:22:12.800Z",
    "location": {
       "lat": 12.2,
       "lng": -12.2
       },
     "status": "PAID",
     "id": "c8y4865-7654876-zdfi76-23436k",
     "creation_date": "2022-01-07T00:04:10.713Z",
     "metadata": {
       "source": "account balance",
       "message": "David's birthday present"
       }
   },
   {
     "amount": 10.0,
     "to": 6789,
     "expiration": "2022-01-06T10:39:00.000Z",
     "location": {
       "lat": 12.2,
       "lng": -12.2
       },
     "status": "EXPIRED",
     "id": "f197146f-463f-4cdf-96ac-50a3133801a0",
     "creation_date": "2022-01-02T00:04:20.649Z",
     "metadata": {
        "my-custom-key": "my-custom-value"
        }
   },
   {
     "amount": 50.0,
     "to": 6789,
     "expiration": "2022-02-25T10:39:00.000Z",
     "location": {
       "lat": 12.2,
       "lng": -12.2
       },
     "status": "PENDING",
     "id": "fa60cfc3-a5d5-4af1-a193-e20ca6446e5b",
     "creation_date": "2022-01-07T00:05:12.950Z",
     "metadata": {
       "some-key": "some-value"
       }
   }
]
```

# Related pages

[Guides / Payments and transfers](https://developers.pismo.io/pismo-docs/docs/payments)\
[Guides / Make a transfer](https://developers.pismo.io/pismo-docs/docs/make-transfer)\
[API reference / Create payment request](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payment-requests)\
[API reference / Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments)\
[API reference / List payment requests](https://developers.pismo.io/pismo-docs/reference/get-payments-v1-payment-requests)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /payments/v1/payment-requests` | `post-payments-v1-payment-requests` | Create payment request | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-requests |
| `POST /payments/v1/payments` | `post-payments-v1-payments` | Transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `GET /payments/v1/payment-requests` | `get-payments-v1-payment-requests` | List payment requests | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-requests |

### Operation essentials

- **`POST /payments/v1/payment-requests`** (`post-payments-v1-payment-requests`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `to`, `amount`; response statuses 200, 400, 500; error codes in examples `WP2P0000`, `WP2P0000`; events none listed.
- **`POST /payments/v1/payments`** (`post-payments-v1-payments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `from`, `to`; response statuses 201, 202, 400, 409, 422, 500, 502; error codes in examples `WP2P0000`, `WP2P0019`, `EP2P9999`, `WP2P0005`, `WP2P0006`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WP2P0020`, `WP2P0013`, `WLDG0006`, `WP2P0010`, `WP2P0000`, `WP2P0000`, `ELDG500`, `EPCG501`, `EP2P9999`, `EP2P0001`, `EP2P0002`; events `authorization-authorization-event-1`.
- **`GET /payments/v1/payment-requests`** (`get-payments-v1-payment-requests`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `WP2P0009`, `EP2P9999`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v1-payments` | `authorization-authorization-event-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/payment-requests.md`: updatedAt 2026-03-18T15:13:13.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/payment-requests.md` | whole document | https://developers.pismo.io/pismo-docs/docs/payment-requests | `8a7ef9efd5e8e344…` | 2026-03-18T15:13:13.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--payment-requests` — API reference: Core platform - Payment methods — Payment requests
- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-payments` — Payments and transfers
- `KU-PAY-transfers-make-and-cancel` — Transfers: making and cancelling transfers
