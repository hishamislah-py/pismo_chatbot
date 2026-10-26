---
ku_id: KU-PAY-force-operation
title: Force operation
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/force-operation.md
  sha256: f7ec6fdb2e772df0d9e1af6e34f6e02669891f4422be3702b5be0a4875978e05
  url: https://developers.pismo.io/pismo-docs/docs/force-operation
  role: primary_guide
  updated_at: '2026-07-24T14:37:11.000Z'
operations:
- post-payments-v1-force
- post-payments-v1-force-cancel
- post-payments-v1-payments
related_kus:
- KU-API-core-platform-payment-methods--force-operations
- KU-API-core-platform-payment-methods--payments
- KU-EVT-catalogue-other-domains
- KU-PAY-payments
grouping_rationale: single source page
---

# Force operation

**KU ID:** `KU-PAY-force-operation` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/force-operation.md`:

> You can force a credit or a debit operation for a specified account, and the Pismo platform guarantees idempotence and integrity of this operation. A forced operation uses a `processing_code`, generates a new authorization, and directly impacts the account balance.  However, it does not include any of the validations that are performed in the [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) endpoint, such as validating the account status, account balance, or flexible transaction controls. You can choose to include or exclude a forced operation from the account timeline.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/force-operation.md`: Force operation; Force operation; Forced credit example; Sample request details; Sample response details; Cancel forced operation; Cancel forced operation examples; Response details; Related pages

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/force-operation.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/force-operation · updatedAt: 2026-07-24T14:37:11.000Z

<!-- source:begin path=docs/core-platform/force-operation.md part=0-end -->

# Force operation

You can force a credit or a debit operation for a specified account, and the Pismo platform guarantees idempotence and integrity of this operation. A forced operation uses a `processing_code`, generates a new authorization, and directly impacts the account balance.  However, it does not include any of the validations that are performed in the [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) endpoint, such as validating the account status, account balance, or flexible transaction controls. You can choose to include or exclude a forced operation from the account timeline.

The [Force operation](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-force) API is recommended for all new implementations that need to force some anticipated operations, such as cashback credits or transaction fees. For differences between a forced operation and an adjustment, see the [comparison table](https://developers.pismo.io/pismo-docs/docs/force-operation#forced-operation-vs-adjustment) in this guide.

# Force operation

To force an operation, use the [Force operation](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-force) endpoint and provide the required `account_id`, `processing_code`, and `amount`. In the request header, you can provide a value for the `x-skip-timeline` parameter. If set to `true`, this prevents the generation of timeline events in the customer timeline.

```json
POST <URL>payments/v1/payments/force
```

## Forced credit example

In the following example, the `processing_code` `090907` defines a credit type. The following payload executes a forced credit operation.

```json Forced credit example - request
{
	"tracking_id": "ba7f42b9-9bd1-4840-a747-f1b59037b798",
	"account_id": 1234,
	"amount": 40.25,
	"processing_code": "090907",
	"currency": "USD",
	"descriptor": "Forced single credit operation ",
	"metadata": {
		"any-key": "any-value"
	}
}
```

### Sample request details

| Field             | Type         | Optional or required | Description                                                                                                                               |
| :---------------- | :----------- | :------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| `tracking_id`     | string       | optional             | The unique 36-character identifier of the forced operation. If you don't provide an identifier, the Pismo platform generates one for you. |
| `account_id`      | integer      | required             | The unique identifier of an account in the Pismo platform.                                                                                |
| `amount`          | float number | required             | The credit or debit amount.                                                                                                               |
| `processing_code` | string       | required             | The 6-character processing code that identifies the credit or debit operation.                                                            |
| `currency`        | string       | optional             | Currency code of the requested operation, in ISO 4217.                                                                                    |
| `descriptor`      | string       | optional             | The description of the created operation.                                                                                                 |
| `metadata`        | object       | optional             | Any valid JSON key-value object that allows you to add complementary custom information.                                                  |

### Sample response details

If the operation is successful (status code `201`), the response returns the following three parameters.

```json Forced credit example - response
{
  "authorization_id": 31812823,
  "tracking_id": "ba7f42b9-9bd1-4840-a747-f1b59037b798",
  "event_date": "2022-02-02T14:05:51.688"
}
```

| Field              | Type    | Description                                                                                                                                                                         |
| :----------------- | :------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `authorization_id` | integer | The generated identifier for the authorization.                                                                                                                                     |
| `tracking_id`      | string  | The unique 36-character identifier for the forced operation. If you didn't provide an identifier, then the Pismo platform automatically generates and includes one in the response. |
| `event_date`       | string  | The date and time of the transaction, in the UTC-0 (RFC3339) format.                                                                                                                |

If the operation is accepted but there is a delay in processing (status code `202`), the response shows the corresponding `code` and the `message`. The request will process and finish asynchronously.

If the operation fails (status codes `400`, `500`), the response returns the `code` and the corresponding `message` that describes the error.

If a tracking ID is already in use (status code `409`),  in addition to the `code` and the `message`, the response also returns the related `authorizations` object.

# Cancel forced operation

To cancel a forced operation, use the [Cancel forced operation](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-force-cancel) endpoint. This endpoint allows you to cancel the total or partial amount of an existing forced operation.

```json
POST <URL>payments/v1/payments/force/cancel
```

In the request header, you can provide a value for the `x-skip-timeline` parameter. If set to `true`, this prevents generation of timeline events in the customer timeline.

In the request body, provide one of the following required identifiers of the original forced operation:

* `authorization_id`, the authorization ID which was returned in the forced operation response (`v1/payments/force`) as `authorization_id`.
* `original_tracking_id`, the tracking ID which was returned in the forced operation response (`v1/payments/force`) as `tracking_id`.

By default, the request to this endpoint cancels the full amount of the original forced operation. Optionally, you can provide the partial amount to cancel in the `amount` field. This value should be less than or equal to the amount of the original operation, and greater than 0.

By default, whenever a total or a partial cancellation of an operation with a fee occurs , the platform doesn't cancel this fee automatically (the `cancel_fees` field is set to `false`). To cancel the associated fee, set the `cancel_fees` field to `true`.

You can also optionally provide the `tracking_id`, `descriptor`, and any `metadata` in the request.

## Cancel forced operation examples

The following example request cancels the full amount of the forced credit operation from the previous example.

```json Cancel forced credit example - request
{
  "authorization_id": 31812823,
  "tracking_id": "1ff51e99-3a05-448a-bc19-7b5c05274174",
  "original_tracking_id": "ba7f42b9-9bd1-4840-a747-f1b59037b798",
  "descriptor": "Cancel forced single credit operation",
  "metadata": {
    "my-custom-key": "my-custom-value"
  }
}
```

The following example request cancels the partial amount of the forced credit operation and any associated fees.

```json Cancel forced credit example - request
{
  "authorization_id": 31812823,
  "tracking_id": "1ff51e99-3a05-448a-bc19-7b5c05274174",
  "original_tracking_id": "ba7f42b9-9bd1-4840-a747-f1b59037b798",
  "amount": 20.00,
  "cancel_fees": true,
  "descriptor": "Cancel forced single credit operation",
  "metadata": {
    "my-custom-key": "my-custom-value"
  }
}
```

### Response details

If the cancel forced operation is successful (status code `200`), the response returns `authorization_id`, `tracking_id`, and `event_date` of the cancellation.

If the operation is accepted but there is a delay in processing (status code `202`), the response shows the corresponding `code` and the `message`. The request will process and finish asynchronously.

If the operation fails (status codes `400`, `404`, `500`), the response returns the `code` and the corresponding `message` that describes the error.

If a tracking ID is already in use (status code `409`) and the operation has been canceled already, the response returns the `authorization_id`,`tracking_id`, and `event_date` of the previously generated cancellation operation.

# Related pages

[API reference / Force operation](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-force)\
[API reference / Cancel forced operation](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-force-cancel)\
[Guides / Payments and transfers](https://developers.pismo.io/pismo-docs/docs/payments)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /payments/v1/payments` | `post-payments-v1-payments` | Transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /payments/v1/payments/force` | `post-payments-v1-force` | Force operation | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--force-operations |
| `POST /payments/v1/payments/force/cancel` | `post-payments-v1-force-cancel` | Cancel forced operation | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--force-operations |

### Operation essentials

- **`POST /payments/v1/payments`** (`post-payments-v1-payments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `from`, `to`; response statuses 201, 202, 400, 409, 422, 500, 502; error codes in examples `WP2P0000`, `WP2P0019`, `EP2P9999`, `WP2P0005`, `WP2P0006`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WP2P0020`, `WP2P0013`, `WLDG0006`, `WP2P0010`, `WP2P0000`, `WP2P0000`, `ELDG500`, `EPCG501`, `EP2P9999`, `EP2P0001`, `EP2P0002`; events `authorization-authorization-event-1`.
- **`POST /payments/v1/payments/force`** (`post-payments-v1-force`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields none declared; response statuses 201, 202, 400, 409, 500; error codes in examples `WP2P0000`, `WP2P1005`, `WRAT00001`, `WP2P0022`, `WP2P0023`, `WP2P0000`, `ERAT00001`, `ERAT00002`, `ERAT00003`, `EP2P0012`; events `authorization-authorization-event-1`.
- **`POST /payments/v1/payments/force/cancel`** (`post-payments-v1-force-cancel`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 202, 400, 404, 409, 500; error codes in examples `WP2P0000`, `WP2P0022`, `WP2P0003`, `WP2P1005`, `EP2P0005`, `EP2P0014`, `WP2P0008`, `WP2P0000`; events `authorization-authorization-cancellation-event-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v1-force-cancel` | `authorization-authorization-cancellation-event-1` |
| `post-payments-v1-force` | `authorization-authorization-event-1` |
| `post-payments-v1-payments` | `authorization-authorization-event-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/force-operation.md`: updatedAt 2026-07-24T14:37:11.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/force-operation.md` | whole document | https://developers.pismo.io/pismo-docs/docs/force-operation | `f7ec6fdb2e772df0…` | 2026-07-24T14:37:11.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--force-operations` — API reference: Core platform - Payment methods — Force operations
- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-payments` — Payments and transfers
