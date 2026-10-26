---
ku_id: KU-PAY-scheduled-payments
title: Schedule payment overview
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/scheduled-payments.md
  sha256: ed513d0718220daccc5c387d619faf589d3e3e646be712991bfb4188c57bb285
  url: https://developers.pismo.io/pismo-docs/docs/scheduled-payments
  role: primary_guide
  updated_at: '2026-09-02T19:47:23.000Z'
operations:
- corporate-v2-get-scheduled-payment
- corporate-v2-post-scheduled-payments
- corporate-v3-post-multileg-payments
related_kus:
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Schedule payment overview

**KU ID:** `KU-PAY-scheduled-payments` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/scheduled-payments.md`:

> The [Schedule payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments) feature of the Pismo platform enables you to postdate payments; that is, to schedule a payment for a specific future date. The most common scenario is  to schedule a recurring monthly payment for a later date.  The Pismo platform validates that the scheduled date does not occur on a holiday.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/scheduled-payments.md`: Schedule payment overview; Initial considerations; Tracking ID; Status; Example; Sample request; Sample response

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/scheduled-payments.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/scheduled-payments · updatedAt: 2026-09-02T19:47:23.000Z

<!-- source:begin path=docs/core-banking/scheduled-payments.md part=0-end -->

# Schedule payment overview

The [Schedule payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments) feature of the Pismo platform enables you to postdate payments; that is, to schedule a payment for a specific future date. The most common scenario is  to schedule a recurring monthly payment for a later date.  The Pismo platform validates that the scheduled date does not occur on a holiday.

# Initial considerations

Consider the following before using scheduled payments:

* There is no endpoint you can use to update scheduled payments once you have submitted them to Pismo, as these scheduled payments are considered active.
* If you want to update an active scheduled payment request; for example, to postdate  it, you must cancel the existing payment request and schedule a new one with the desired date.
* You must schedule your payment for at least one minute in the future. There are no restrictions on the maximum date or time you can schedule it.
* Only the debtor can schedule a payment for a fund transfer.
* You can reuse a tracking ID when scheduling a new payment, provided that there are no active or processed payments using that same tracking ID. If there are active or processed payments, the endpoint throws an error and scheduling is denied.
* You cannot schedule payments using a different currency for both credit and debit accounts.
* [Schedule payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments) does not support [multi-leg payments](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments).

# Tracking ID

When using this endpoint, you must provide a unique tracking ID (`tracking_id`) that identifies your scheduled payment request. This ID you provide must satisfy the following criteria:

* **Unique**: The tracking ID must be unique within the organization.
* **Immutable**: It cannot be updated.
* **Non-reusable**: You cannot reuse the same `tracking_id` for existing scheduled payments, and the tracking ID must be unique for both scheduled and regular transactions. However, you can reuse the tracking ID of a canceled schedule payment when creating a new one.

The tracking ID must be unique for both scheduled and regular transactions.

# Status

The following table lists the possible result statuses for a scheduled payment request:

| Status        | Description                                                                    |
| :------------ | :----------------------------------------------------------------------------- |
| **Active**    | The scheduled payment was successfully created, but has not yet been executed. |
| **Completed** | The scheduled payment was successfully posted.                                 |
| **Failed**    | The scheduled payment was not successfully posted.                             |
| **Aborted**   | The scheduled payment was canceled before its scheduled time.                  |

# Example

## Sample request

For example, you schedule a $200 payment for March 10th, 2023 using  [Schedule payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments).

```curl
curl --location 'https://sandbox.pismolabs.io/corporate/v1/scheduled-payments' \
--header 'Content-Type: application/json' \
--header 'Cookie: <cookie_data>' \
--data '{
    "debit": {
        "external_account_id": "973f4c7c-ac1e-4da2-9ac6-2724a2a8f79e",
        "processing_code": "220037"
    },
    "amount": {
        "value": 200,
        "currency": "USD"
    },
    "soft_descriptor": "Debit operation",
    "tracking_id": "99208f24-6318-4c19-8700-8b9ccf8ee25a",
    "schedule_datetime": "2024-03-10T19:05:56.743Z"
}'
```

## Sample response

If the request is successful, it should return a schedule ID similar to the following:

```json JSON
{
    "id": "5476ddac-351a-4bf0-94d0-169490824d57"
}
```

You can use the returned schedule ID with the [Get scheduled payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-get-scheduled-payment) endpoint to retrieve details about the scheduled payment:

```json JSON
{
    "id": "5476ddac-351a-4bf0-94d0-169490824d57",
    "status": "ACTIVE",
    "payment": {
        "debit": {
            "external_account_id": "973f4c7c-ac1e-4da2-9ac6-2724a2a8f79e",
            "processing_code": "220037",
            "earmark_id": ""
        },
        "amount": {
            "value": 200,
            "currency": "USD"
        },
        "soft_descriptor": "Debit operation",
        "tracking_id": "cc895998-7b76-447f-bf08-8d973f883f05",
        "metadata": {
            "corporate_metadata": {
                "debit_external_account_id": "973f4c7c-ac1e-4da2-9ac6-2724a2a8f79e",
                "payment_datetime": "2024-03-10T19:05:56.743Z"
            }
        },
        "allow_suspense_posting": false,
        "skip_account_date_validation": false,
        "force_post": false,
        "payment_datetime": "2024-03-10T19:05:56.743Z",
        "schedule_datetime": "2024-03-10T19:05:56.743Z"
    }
}
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /corporate/v2/scheduled-payments` | `corporate-v2-post-scheduled-payments` | Schedule payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-02 |
| `POST /corporate/v3/payments/multileg` | `corporate-v3-post-multileg-payments` | Post multi-leg payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `GET /corporate/v2/scheduled-payments/{scheduledPaymentId}` | `corporate-v2-get-scheduled-payment` | Get scheduled payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-02 |

### Operation essentials

- **`POST /corporate/v2/scheduled-payments`** (`corporate-v2-post-scheduled-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`, `schedule_datetime`; response statuses 201, 400, 401, 403, 500; error codes in examples `WPMT0017`, `WPMT0018`, `WCMN0002`, `WCAC0010`, `WPMT0005`, `WPMT0006`, `WPMT0014`, `WPMT0053`, `WCAC0001`, `ECMN9999`; events `availables-change-available-1`, `corporate-schedule-payment-1`, `platform-authorization-platform-authorization-1`.
- **`POST /corporate/v3/payments/multileg`** (`corporate-v3-post-multileg-payments`): security `BearerAuth`; required parameters none declared; required body fields `multileg_id`; response statuses 202, 400, 403, 409, 500; error codes in examples `WMLP0001`, `WMLP0002`, `WMLP0003`, `WMLP0004`, `WMLP0008`, `WMLP1044`, `WMLP0005`, `WMLP1026`, `WMLP1028`, `WMLP1027`, `WMLP1049`, `WMLP1002`, `WMLP1003`, `WMLP1004`, `WMLP1005`, `WMLP1039`, `WMLP1006`, `WMLP1022`, `WMLP1007`, `WMLP1008`, `WMLP1009`, `WMLP1010`, `WMLP1011`, `WMLP1013`, `WMLP1014`, `WMLP1015`, `WMLP1016`, `WMLP1017`, `WMLP1019`, `WMLP1048`, `WMLP1023`, `WMLP1036`, `WMLP1034`, `WMLP1035`, `WMLP1024`, `WMLP1037`, `WMLP1038`, `WMLP1030`, `WMLP1040`, `WMLP1041`, `WMLP1042`, `WMLP1043`, `WMLP1046`, `WMLP0009`, `ECMN9999`; events `corporate-multi-leg-creation-2`, `corporate-multi-leg-status-change-2`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`GET /corporate/v2/scheduled-payments/{scheduledPaymentId}`** (`corporate-v2-get-scheduled-payment`): security `BearerAuth`; required parameters `scheduledPaymentId` (path); required body fields none declared; response statuses 200, 401, 403, 500; error codes in examples `ECMN9999`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-v2-post-scheduled-payments` | `availables-change-available-1` |
| `corporate-v3-post-multileg-payments` | `corporate-multi-leg-creation-2` |
| `corporate-v3-post-multileg-payments` | `corporate-multi-leg-status-change-2` |
| `corporate-v2-post-scheduled-payments` | `corporate-schedule-payment-1` |
| `corporate-v2-post-scheduled-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v3-post-multileg-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v3-post-multileg-payments` | `rules-evaluation-requested-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/scheduled-payments.md`: updatedAt 2026-09-02T19:47:23.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/scheduled-payments.md` | whole document | https://developers.pismo.io/pismo-docs/docs/scheduled-payments | `ed513d0718220dac…` | 2026-09-02T19:47:23.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
