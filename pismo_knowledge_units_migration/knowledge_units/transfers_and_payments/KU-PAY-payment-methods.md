---
ku_id: KU-PAY-payment-methods
title: Payment methods
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/payment-methods-overview.md
  sha256: b4713f69a2f381392aa3efe56dc63d8cdcc2b09c2cf9acb192fea7ba5613bfd8
  url: https://developers.pismo.io/pismo-docs/docs/payment-methods-overview
  role: primary_guide
  updated_at: '2026-03-18T15:12:50.000Z'
- path: docs/core-platform/payment-methods.md
  sha256: 20be19a9caeb890a2e981693dbdf9957054a26c0298e7dd3f1bdf3c97c506810
  url: https://developers.pismo.io/pismo-docs/docs/payment-methods
  role: primary_guide
  updated_at: '2026-05-01T01:59:56.000Z'
operations:
- post-acceptance-by-tenant
- post-authorization
- post-config-by-tenant
- post-payment-confirm
- post-payments
- post-payments-cancel
- post-payments-v1-payments
- post-payments-v2-cancel
- post-transfers
- post-transfers-cancel
- post-transfers-confirm
related_kus:
- KU-API-core-platform-balance-watcher--limit-acceptance-configurations
- KU-API-core-platform-balance-watcher--limit-configurations
- KU-API-core-platform-payment-configurations--payment-method-acceptances
- KU-API-core-platform-payment-configurations--payment-method-configurations
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-API-core-platform-payment-methods--payment-methods-part-03
- KU-API-core-platform-payment-methods--payments
- KU-CORE-authorization-validation-rules-for-platform-operations-part-01
- KU-CORE-authorization-validation-rules-for-platform-operations-part-02
- KU-EVT-catalogue-other-domains
- KU-PAY-payments
grouping_rationale: Overview stub and its main page.
---

# Payment methods

**KU ID:** `KU-PAY-payment-methods` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Overview stub and its main page.

Scope as stated in `docs/core-platform/payment-methods-overview.md`:

> The Pismo platform supports a wide range of payment methods, which fall into two major categories.

Scope as stated in `docs/core-platform/payment-methods.md`:

> The [Payment methods](https://developers.pismo.io/pismo-docs/reference/post-authorization) API is the enhanced application interface for managing platform operations, which are operations such as bank transfers and payments that don’t involve card networks like Visa and Mastercard. The Payment methods API offers flexible payments and authorization processes to support different business models. The endpoints in this API are dedicated to specific types of operations and are scaled to simplify payloads and improve performance. The API supports advanced features such as external authentication, pre-authorization, and configuration options.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/payment-methods-overview.md`: Payment methods overview
- `docs/core-platform/payment-methods.md`: Payment methods; Payment and authorization; Cancel operation; Confirm pre-authorized operation; Authorization categories; Validation results array

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 13 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/payment-methods-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/payment-methods-overview · updatedAt: 2026-03-18T15:12:50.000Z

<!-- source:begin path=docs/core-platform/payment-methods-overview.md part=0-end -->

# Payment methods overview

The Pismo platform supports a wide range of payment methods, which fall into two major categories.

* **Card network operations** are operations that involve card networks such as Visa. Card network operations are covered in the [Card issuing](https://developers.pismo.io/pismo-docs/docs/card-issuing-with-pismo)  section of the guides.
* **Platform operations** are operations such as bank transfers and payments that don’t involve card networks. Platform operations are covered in this section of the guides. The [Payment methods](https://developers.pismo.io/pismo-docs/docs/payment-methods)  API is the enhanced application interface for managing platform operations.
<!-- source:end -->

### Source 2: `docs/core-platform/payment-methods.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/payment-methods · updatedAt: 2026-05-01T01:59:56.000Z

<!-- source:begin path=docs/core-platform/payment-methods.md part=0-end -->

# Payment methods

The [Payment methods](https://developers.pismo.io/pismo-docs/reference/post-authorization) API is the enhanced application interface for managing platform operations, which are operations such as bank transfers and payments that don’t involve card networks like Visa and Mastercard. The Payment methods API offers flexible payments and authorization processes to support different business models. The endpoints in this API are dedicated to specific types of operations and are scaled to simplify payloads and improve performance. The API supports advanced features such as external authentication, pre-authorization, and configuration options.

<Callout icon="📘" theme="info">
  The Payment methods API is the recommended approach for any new deployments. It offers enhanced features that streamline processes and function differently from the [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) and [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-payments-v2-cancel) endpoints that are described in the [Payments and transfers](https://developers.pismo.io/pismo-docs/docs/payments) guide. All new feature developments will be available only in the Payment methods API. For more information, contact your Pismo representative.
</Callout>

The Payment methods API includes the following endpoints.

* [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization) to request a new authorization and cancel or confirm an existing authorization.
* The following endpoints to manage cash-in, cash-out, and transfer operations.
  * [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments)
  * [Cancel cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments-cancel)
  * [Confirm pre-authorized cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payment-confirm)
  * [Create transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers)
  * [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers-cancel)
  * [Confirm pre-authorized transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers-confirm)
* All configuration endpoints in the following sections.
  * [Payment method configs](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) to manage payment methods configurations.
  * [Payment method acceptances](https://developers.pismo.io/pismo-docs/reference/post-acceptance-by-tenant) to manage acceptance configurations for processing code operations.

The transactions that can take place on the Pismo platform can be grouped into three categories:

* **cash-in**, where money is deposited to the platform account from an external environment
* **internal transfer**, where money is transferred between the platform accounts
* **cash-out**, where money is withdrawn from the platform account to an external environment

The diagram below illustrates your possibilities:

<Image align="center" alt="Graphic showing the transaction categories. " src="https://files.readme.io/ff318b5-diagram-payments2x.png" title="diagram-payments@2x.png" />

## Payment and authorization

You can create platform operations such as cash-in, cash-out, cancellations, pre-authorizations, confirmations, denied authorizations, and peer-to-peer (p2p) transfers.

* To create a cash-in or cash-out operation on the indicated account, use the [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments) endpoint. The type of operation depends on the processing code (credit for cash-in and debit for cash-out).
* To make transfers between two Pismo accounts, use the [Create transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers) endpoint.

You can also mark both operation types for pre-authorization by setting the `pre_authorization` parameter to `true` and then [confirm pre-authorized operation](https://developers.pismo.io/pismo-docs/docs/payment-methods#confirm-preauthorized-operation).

## Cancel operation

Every authorization is subject to partial or total cancellation. To cancel authorizations that have been successfully carried out and approved on the platform, use the following endpoints according to the type of original operation to be canceled.

* [Cancel cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments-cancel)
* [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers-cancel)

## Confirm pre-authorized operation

When you mark an operation for pre-authorization by setting the `pre_authorization` parameter to `true`, you need to confirm it so that the platform can create the transaction corresponding to this authorization.

* [Confirm pre-authorized cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payment-confirm)
* [Confirm pre-authorized transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers-confirm)

There are three scenarios for confirming a pre-authorization.

* **Debit pre-authorization (cash-out)**: the financial impact occurs during the pre-authorization, and the confirmation finalizes the operation and creates the transaction.

* **Credit pre-authorization (cash-in)**: the financial impact occurs only during the confirmation, avoiding financial loss if the confirmation is not executed, preventing anyone who will receive the money from moving it into the account before the confirmation.

* **Transfer pre-authorization**

## Authorization categories

The payment methods endpoints support advanced authorization concepts and features. At the end of the operation authorization flow, the platform generates the following categories of authorizations and reflects them in the [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)  event.

* `AUTHORIZATION` - a cash-in, cash-out, or transfer authorization was carried out successfully.
* `CANCELLATION` - a cash-in, cash-out, or transfer authorization was successfully canceled.
* `PARTIAL_CANCELLATION` - the approved authorization refers to a partial cancellation of a previously approved operation.
* `DENIED` - the authorization operation cannot be approved.
* `DENIED_CANCELLATION` - the cancellation operation cannot be approved.
* `CONFIRMATION` - the confirmation was authorized successfully.

## Validation results array

The transaction authorization flow on the Pismo platform goes through a series of validations to ensure that a financial transaction can be approved. During this flow, the platform validates data associated with the operation such as the account information, flexible transaction controls, balances and limits, anti-fraud and external validations, and various configurations.

Each financial transaction operation returns a validation results array in the response. The array contains details of each validation step taken during the authorization process. Each validation within the authorization flow generates a result with one of the following statuses: `APPROVED`, `SKIPPED`, or `REJECTED`. If there are any denied entries in the array, this results in a denied authorization.

In the following example, the array contains the validation that is approved by anti-fraud and the validation that is rejected by ledger. In this example, the operation is denied.

```json
"validation_results": [
    {
        "name": "ANTI_FRAUD",
        "status": "APPROVED",
        "reason": "ANTI_FRAUD_APPROVED",
        "description": "Authorization passed anti-fraud evaluation.",
        "additional_data": {}
    },
    {
        "name": "LEDGER",
        "status": "REJECTED",
        "reason": "LEDGER_INSUFFICIENT_FUNDS",
        "description": "The authorization amount is greater than the account available limit.",
        "additional_data": {
            "denial_code": "LE003",
            "response_code": "04"
        }
    }
]
```

For details, see [Authorization validation rules for platform operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /payment-methods/v1/authorization` | `post-authorization` | Request authorization | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `POST /payments/v1/payments` | `post-payments-v1-payments` | Transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /payments/v2/cancel` | `post-payments-v2-cancel` | Cancel transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /payment-methods/v2/payments` | `post-payments` | Create cash-in or cash-out | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `POST /payment-methods/v2/payments/cancel` | `post-payments-cancel` | Cancel cash-in or cash-out | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `POST /payment-methods/v2/payments/confirm` | `post-payment-confirm` | Confirm pre-authorized cash-in or cash-out | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-02 |
| `POST /payment-methods/v2/transfers` | `post-transfers` | Create transfer | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-02 |
| `POST /payment-methods/v2/transfers/cancel` | `post-transfers-cancel` | Cancel transfer | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-02 |
| `POST /payment-methods/v2/transfers/confirm` | `post-transfers-confirm` | Confirm pre-authorized transfer | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /v1/config` | `post-config-by-tenant` | Create limit config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-configurations |
| `POST /payment-methods-configs/v1/configs` | `post-config-by-tenant` | Create org configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `POST /v1/acceptance/processing-code/{processingCode}` | `post-acceptance-by-tenant` | Create limit acceptance config by Org | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-acceptance-configurations |
| `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `post-acceptance-by-tenant` | Create org acceptance configuration | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-acceptances |

### Operation essentials

- **`POST /payment-methods/v1/authorization`** (`post-authorization`): security `BearerAuth`; required parameters none declared; required body fields `currency_code`, `mti`, `network`; response statuses 200, 201, 400, 401, 403, 422, 500; error codes in examples `WONA0001`, `WONA0004`, `WONA0005`, `WONA0006`, `WONA0011`, `WONA0012`, `WONA0013`, `WONA0015`, `WONA0016`, `WONA0018`, `WONA0019`, `WONA0020`, `WONA0032`, `WONA0033`, `WONA0036`, `WONA039`, `WONA040`, `WONA041`, `WONA042`, `WONA043`, `EINS0004`, `EINS0005`, `EINS0006`, `EINS0010`, `EINS0011`, `EINS0012`, `EINS0015`, `EINS0016`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `payment-methods-authorization-1`, `platform-authorization-platform-authorization-1`.
- **`POST /payments/v1/payments`** (`post-payments-v1-payments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `from`, `to`; response statuses 201, 202, 400, 409, 422, 500, 502; error codes in examples `WP2P0000`, `WP2P0019`, `EP2P9999`, `WP2P0005`, `WP2P0006`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WP2P0020`, `WP2P0013`, `WLDG0006`, `WP2P0010`, `WP2P0000`, `WP2P0000`, `ELDG500`, `EPCG501`, `EP2P9999`, `EP2P0001`, `EP2P0002`; events `authorization-authorization-event-1`.
- **`POST /payments/v2/cancel`** (`post-payments-v2-cancel`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `amount`; response statuses 200, 202, 208, 400, 404, 409, 500, 502; error codes in examples `AMON0004`, `WP2P0009`, `WP2P0000`, `AMON0000`, `WP2P0000`, `WP2P1005`, `EP2P0005`, `WP2P1111`, `EP2P0011`, `EP2P0013`, `WP2P0003`, `EP2P9999`, `WP2P3003`, `WP2P0033`, `WP2P0008`, `WP2P0000`, `WLDG0019`, `WLDG0004`, `WLDG0006`, `WLDG0005`, `WP2P0010`, `AMON0004`, `WP2P0009`, `WP2P0000`, `WP2P0000`, `ACQ0001`, `ACQ0000`, `EP2P9999`, `ELDG500`, `EP2P0001`; events `authorization-authorization-cancellation-event-1`.
- **`POST /payment-methods/v2/payments`** (`post-payments`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `amount`, `processing_code`, `tracking_id`; response statuses 200, 201, 400, 401, 409, 422, 500; error codes in examples `WONP0001`, `WONB0001`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/payments/cancel`** (`post-payments-cancel`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `original_tracking_id`; response statuses 200, 201, 400, 404, 409, 422, 500; error codes in examples `WONP0001`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/payments/confirm`** (`post-payment-confirm`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `original_tracking_id`; response statuses 200, 202, 400, 404, 409, 422, 500; error codes in examples `WONP0010`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/transfers`** (`post-transfers`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `from`, `to`, `tracking_id`; response statuses 200, 201, 400, 401, 409, 422, 500; error codes in examples `WONP0001`, `WONB0001`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/transfers/cancel`** (`post-transfers-cancel`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `original_tracking_id`; response statuses 200, 201, 400, 404, 409, 422, 500; error codes in examples `WONP0001`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/transfers/confirm`** (`post-transfers-confirm`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `original_tracking_id`; response statuses 200, 202, 400, 404, 409, 422, 500; error codes in examples `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`POST /v1/config`** (`post-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-config-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/configs`** (`post-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-config-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /v1/acceptance/processing-code/{processingCode}`** (`post-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 201, 400, 401, 409, 500; error codes in examples `BW0008`, `BW0031`, `BW0032`, `BW0007`; events none listed. Note: operationId `post-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.
- **`POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}`** (`post-acceptance-by-tenant`): security `BearerAuth`; required parameters `processingCode` (path); required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed. Note: operationId `post-acceptance-by-tenant` occurs in 2 specification files; the link does not say which one.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v2-cancel` | `authorization-authorization-cancellation-event-1` |
| `post-payments-v1-payments` | `authorization-authorization-event-1` |
| `post-authorization` | `payment-methods-authorization-1` |
| `post-authorization` | `platform-authorization-platform-authorization-1` |
| `post-payment-confirm` | `platform-authorization-platform-authorization-1` |
| `post-payments` | `platform-authorization-platform-authorization-1` |
| `post-payments-cancel` | `platform-authorization-platform-authorization-1` |
| `post-transfers` | `platform-authorization-platform-authorization-1` |
| `post-transfers-cancel` | `platform-authorization-platform-authorization-1` |
| `post-transfers-confirm` | `platform-authorization-platform-authorization-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `platform-authorization-platform-authorization-1` | platform | 1 | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 | 32 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/payment-methods-overview.md`: updatedAt 2026-03-18T15:12:50.000Z.
- `docs/core-platform/payment-methods.md`: updatedAt 2026-05-01T01:59:56.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/payment-methods-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/payment-methods-overview | `b4713f69a2f38139…` | 2026-03-18T15:12:50.000Z |
| `docs/core-platform/payment-methods.md` | whole document | https://developers.pismo.io/pismo-docs/docs/payment-methods | `20be19a9caeb890a…` | 2026-05-01T01:59:56.000Z |

## Related knowledge units

- `KU-API-core-platform-balance-watcher--limit-acceptance-configurations` — API reference: Core platform - Balance watcher — Limit acceptance configurations
- `KU-API-core-platform-balance-watcher--limit-configurations` — API reference: Core platform - Balance watcher — Limit configurations
- `KU-API-core-platform-payment-configurations--payment-method-acceptances` — API reference: Core platform - Payment configurations — Payment method acceptances
- `KU-API-core-platform-payment-configurations--payment-method-configurations` — API reference: Core platform - Payment configurations — Payment method configurations
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-03` — API reference: Core platform - Payment methods — Payment methods (part 3 of 3)
- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-CORE-authorization-validation-rules-for-platform-operations-part-01` — Authorization validation rules for platform operations (part 1 of 2)
- `KU-CORE-authorization-validation-rules-for-platform-operations-part-02` — Authorization validation rules for platform operations (part 2 of 2)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-payments` — Payments and transfers
