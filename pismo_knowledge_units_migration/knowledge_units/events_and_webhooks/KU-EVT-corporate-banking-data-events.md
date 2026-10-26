---
ku_id: KU-EVT-corporate-banking-data-events
title: Banking - Transaction banking
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/corporate-banking-data-events.md
  sha256: a9dd7fce44c9c2b9de194d5c8d2a4c3e7b937eac3b2bc081572f0930b9968a8b
  url: https://developers.pismo.io/pismo-docs/docs/corporate-banking-data-events
  role: primary_guide
  updated_at: '2026-08-25T20:51:22.000Z'
operations:
- corporate-post-v1-checks
- corporate-v2-delete-scheduled-payment
- corporate-v2-post-multileg-payments
- corporate-v2-post-payments
- corporate-v2-post-scheduled-payments
- patch-account
- patch-account-balances-history-configuration
- patch-corporate-v2-earmarks-earmarkid
- patch-division-v2
- patch-dormancy-config-v2
- post-account
- post-account-balance-history-configuration
- post-accounts-accountId-close
- post-corporate-v1-checks-checkId-cancel
- post-corporate-v1-checks-release
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-division-v2
- post-dormancy-config-v2
- post-hierarchies
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--check-posting
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--dormancy
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--hierarchies
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Banking - Transaction banking

**KU ID:** `KU-EVT-corporate-banking-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/corporate-banking-data-events.md`:

> This table lists the transaction banking endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/corporate-banking-data-events.md`: Banking - Transaction banking

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 20 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/corporate-banking-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/corporate-banking-data-events · updatedAt: 2026-08-25T20:51:22.000Z

<!-- source:begin path=docs/data-and-reporting/corporate-banking-data-events.md part=0-end -->

# Banking - Transaction banking

This table lists the transaction banking endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Endpoint
      </th>

      <th style={{ textAlign: "left" }}>
        Event
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        [Create transaction banking account](https://developers.pismo.io/pismo-docs/reference/post-account)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account application created](https://developers.pismo.io/events/docs/onboarding-succeeded-1)\
        [Corporate account created](https://developers.pismo.io/events/docs/corporate-corporate-account-creation-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates events when a client creates a corporate account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update transaction banking account](https://developers.pismo.io/pismo-docs/reference/patch-account)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when a client changes an account status.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Close transaction banking account](https://developers.pismo.io/pismo-docs/reference/post-accounts-accountid-close)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when a client closes an account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)
      </td>

      <td style={{ textAlign: "left" }}>
        [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)\
        [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1)\
        [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)\
        [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1)\
        [Evaluation requested](https://developers.pismo.io/events/docs/audit-evaluation-requested-1)\
        [Accounting entry created](https://developers.pismo.io/events/docs/accounting-entry-creation-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates two or more events during the validation process.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments)
      </td>

      <td style={{ textAlign: "left" }}>
        [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)\
        [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1)\
        [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)\
        [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1)\
        [Evaluation requested](https://developers.pismo.io/events/docs/audit-evaluation-requested-1)\
        [Accounting entry created](https://developers.pismo.io/events/docs/accounting-entry-creation-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Each leg generates all events except one. If flex controls are configured, the additional evaluation\_requested-1 is generated.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Schedule a payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments)
      </td>

      <td style={{ textAlign: "left" }}>
        [Current scheduled payment status displayed](https://developers.pismo.io/events/docs/corporate-schedule-payment-1)\
        [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)\
        [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1)\
        [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates schedule\_payment-1 event shortly after a client schedules a payment. Subsequent events are generated when the transaction is executed.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Cancel scheduled payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-delete-scheduled-payment)
      </td>

      <td style={{ textAlign: "left" }}>
        [Current scheduled payment status displayed](https://developers.pismo.io/events/docs/corporate-schedule-payment-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when a client cancels a scheduled payment.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)
      </td>

      <td style={{ textAlign: "left" }}>
        [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)\
        [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1)\
        [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)\
        [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1)\
        [Earmark created, updated, or canceled](https://developers.pismo.io/events/docs/corporate-earmark-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates events when a client creates an  earmark. The earmarking process generates all these events because it triggers an internal transfer in the platform.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid)
      </td>

      <td style={{ textAlign: "left" }}>
        [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)\
        [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1)\
        [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)\
        [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1)\
        [Earmark created, updated, or canceled](https://developers.pismo.io/events/docs/corporate-earmark-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates events when a client updates an  earmark. The earmarking process generates all these events because it triggers an internal transfer in the platform.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel)
      </td>

      <td style={{ textAlign: "left" }}>
        [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)\
        [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1)\
        [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)\
        [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1)\
        [Earmark created, updated, or canceled](https://developers.pismo.io/events/docs/corporate-earmark-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates events when a client cancels an earmark. The earmarking process generates all these events because it triggers an internal transfer in the platform.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create hierarchy](https://developers.pismo.io/pismo-docs/reference/post-hierarchies)
      </td>

      <td style={{ textAlign: "left" }}>
        [Corporate hierarchy created](https://developers.pismo.io/events/docs/corporate-hierarchy-creation-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when a client creates a hierarchy.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2)
      </td>

      <td style={{ textAlign: "left" }}>
        [Corporate division created (deprecated)](https://developers.pismo.io/events/docs/corporate-division-creation-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when a client creates a division.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2)
      </td>

      <td style={{ textAlign: "left" }}>
        [Corporate division updated (deprecated)](https://developers.pismo.io/events/docs/corporate-division-change-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when a client modifies a division.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create account balance history configuration](https://developers.pismo.io/pismo-docs/reference/post-account-balance-history-configuration)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account balance history configuration created](https://developers.pismo.io/events/docs/account-balances-balance-history-config-creation-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when a client creates a balance history configuration.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update account balance history configuration](https://developers.pismo.io/pismo-docs/reference/patch-account-balances-history-configuration)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account balance history configuration changed](https://developers.pismo.io/events/docs/account-balances-balance-history-config-change-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when client changes account balance history configuration.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2)
      </td>

      <td style={{ textAlign: "left" }}>
        [Dormancy configuration created](https://developers.pismo.io/events/docs/corporate-dormancy-config-creation-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when dormancy is configured.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update dormancy configuration](https://developers.pismo.io/pismo-docs/reference/patch-dormancy-config-v2)
      </td>

      <td style={{ textAlign: "left" }}>
        [Dormancy configuration updated](https://developers.pismo.io/events/docs/corporate-dormancy-config-change-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when client changes dormancy configuration.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create check posting](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-checks)
      </td>

      <td style={{ textAlign: "left" }}>
        [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when client creates check posting.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create check posting](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-checks)
      </td>

      <td style={{ textAlign: "left" }}>
        [Check posting status changed](https://developers.pismo.io/events/docs/cash-management-check-status-change-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when client creates check posting.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Release check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-release)
      </td>

      <td style={{ textAlign: "left" }}>
        [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when client releases checks.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Release check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-release)
      </td>

      <td style={{ textAlign: "left" }}>
        [Check posting status changed](https://developers.pismo.io/events/docs/cash-management-check-status-change-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when client releases checks.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Cancel check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-checkid-cancel)
      </td>

      <td style={{ textAlign: "left" }}>
        [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when client cancels checks.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Cancel check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-checkid-cancel)
      </td>

      <td style={{ textAlign: "left" }}>
        [Check posting status changed](https://developers.pismo.io/events/docs/cash-management-check-status-change-1)
      </td>

      <td style={{ textAlign: "left" }}>
        Platform generates event when client cancels checks.
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /corporate/v1/corporate-accounts` | `post-account` | Create transaction banking account | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `PATCH /corporate/v1/corporate-accounts/{externalAccountId}` | `patch-account` | Update transaction banking account | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /corporate/v1/corporate-accounts/{externalAccountId}/close` | `post-accounts-accountId-close` | Close transaction banking account | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /corporate/v2/payments` | `corporate-v2-post-payments` | Post payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `POST /corporate/v2/payments/multileg` | `corporate-v2-post-multileg-payments` | Post multi-leg payment (deprecated) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/scheduled-payments` | `corporate-v2-post-scheduled-payments` | Schedule payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-02 |
| `DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId}` | `corporate-v2-delete-scheduled-payment` | Cancel scheduled payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/earmarks` | `post-corporate-v2-earmarks` | Create earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/earmarks/{earmarkId}` | `patch-corporate-v2-earmarks-earmarkid` | Update earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` | `post-corporate-v2-earmarks-earmarkid-cancel` | Cancel earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v1/hierarchies` | `post-hierarchies` | Create hierarchy | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--hierarchies |
| `POST /corporate/v2/divisions` | `post-division-v2` | Create division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `PATCH /corporate/v2/divisions/{divisionCode}` | `patch-division-v2` | Update division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `POST /bank-statements/v1/account-balances/history/config` | `post-account-balance-history-configuration` | Create account balance history config v1 | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `PATCH /bank-statements/v1/account-balances/history/config/{divisionCode}` | `patch-account-balances-history-configuration` | Update account balance history config v1 | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01 |
| `POST /corporate/v2/dormancy-config` | `post-dormancy-config-v2` | Create dormancy configuration | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `PATCH /corporate/v2/dormancy-config/{dormancyConfigId}` | `patch-dormancy-config-v2` | Update dormancy configuration | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `POST /corporate/v1/checks` | `corporate-post-v1-checks` | Create check posting | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/checks/release` | `post-corporate-v1-checks-release` | Release check | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/checks/{checkId}/cancel` | `post-corporate-v1-checks-checkId-cancel` | Cancel check | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |

### Operation essentials

- **`POST /corporate/v1/corporate-accounts`** (`post-account`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `program_id`, `applicant`, `external_account_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WCAC0013`, `WCAC0005`, `WCAC0006`, `WCAC0004`, `WCAC0016`, `WCAC0009`, `WDIV0002`, `WCAC0011`, `WCAC0014`, `ECMN9999`; events `corporate-corporate-account-creation-1`, `onboarding-succeeded-1`.
- **`PATCH /corporate/v1/corporate-accounts/{externalAccountId}`** (`patch-account`): security `BearerAuth`; required parameters `externalAccountId` (path); required body fields none declared; response statuses 204, 400, 401, 403, 404, 500; error codes in examples `WCAC0013`, `WCAC0012`, `WCAC0006`, `WCAC0004`, `WCAC0005`, `WCAC0031`, `WCAC0032`, `WCAC0033`, `WDIV0002`, `ECMN9999`; events `account-status-change-2`, `corporate-corporate-account-change-1`.
- **`POST /corporate/v1/corporate-accounts/{externalAccountId}/close`** (`post-accounts-accountId-close`): security `BearerAuth`; required parameters `externalAccountId` (path); required body fields none declared; response statuses 204, 400, 401, 403, 422, 500; error codes in examples `WCAC0012`, `WCAC0018`, `WCAC0019`, `WCAC0028`, `WCAC0029`, `WCAC0035`, `WCAC0040`, `WCAC0045`, `ECMN9999`; events `account-status-change-2`.
- **`POST /corporate/v2/payments`** (`corporate-v2-post-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`; response statuses 201, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WPMT0017`, `WPMT0011`, `WPMT0053`, `WPMT0018`, `WPMT0029`, `WPMT0030`, `WPMT0031`, `WPMT0062`, `WPMT0063`, `WCAC0010`, `WPMT0001`, `WPMT0061`, `WPMT0015`, `WPMT0016`, `WPMT0003`, `WPMT0004`, `WPMT0005`, `WPMT0006`, `WPMT0009`, `WPMT0010`, `WPMT0021`, `WEAM0008`, `WEAM0006`, `WPMT0050`, `WEAM0017`, `WEAM0019`, `WPMT0022`, `WPMT0023`, `WPMT0024`, `WPMT0025`, `WPMT0026`, `WCMN0002`, `WPMT0028`, `WPMT0045`, `WPMT0049`, `WPMT0036`, `WPMT0044`, `WPMT0051`, `WPMT0035`, `WPMT0046`, `WPMT0054`, `WPMT0055`, `WPMT0056`, `WPMT0058`, `WPMT0008`, `WPMT0014`, `WPMT0019`, `WCAC0002`, `WCAC0012`, `WPMT0002`, `WCAC0001`, `WEAM0007`, `WPMT0007`, `WPMT0052`, `WEAM0049`, `WPMT0047`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`POST /corporate/v2/payments/multileg`** (`corporate-v2-post-multileg-payments`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`; response statuses 202, 400, 403, 500; error codes in examples `WMLP0001`, `WMLP0002`, `WMLP0003`, `WMLP0004`, `WMLP0006`, `WMLP0005`, `WMLP1026`, `WMLP1028`, `WMLP1027`, `WMLP1002`, `WMLP1003`, `WMLP1004`, `WMLP1005`, `WMLP1039`, `WMLP1006`, `WMLP1022`, `WMLP1007`, `WMLP1008`, `WMLP1009`, `WMLP1010`, `WMLP1011`, `WMLP1013`, `WMLP1014`, `WMLP1015`, `WMLP1016`, `WMLP1017`, `WMLP1019`, `WMLP1048`, `WMLP1023`, `WMLP1036`, `WMLP1034`, `WMLP1035`, `WMLP1024`, `WMLP1037`, `WMLP1038`, `WMLP1030`, `WMLP1041`, `WMLP1042`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `corporate-multi-leg-creation-1`, `corporate-multi-leg-status-change-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`POST /corporate/v2/scheduled-payments`** (`corporate-v2-post-scheduled-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`, `schedule_datetime`; response statuses 201, 400, 401, 403, 500; error codes in examples `WPMT0017`, `WPMT0018`, `WCMN0002`, `WCAC0010`, `WPMT0005`, `WPMT0006`, `WPMT0014`, `WPMT0053`, `WCAC0001`, `ECMN9999`; events `availables-change-available-1`, `corporate-schedule-payment-1`, `platform-authorization-platform-authorization-1`.
- **`DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId}`** (`corporate-v2-delete-scheduled-payment`): security `BearerAuth`; required parameters `scheduledPaymentId` (path); required body fields none declared; response statuses 204, 400, 401, 403, 500; error codes in examples `WCAC0010`, `WPMT0012`, `WPMT0013`, `WCAC0001`, `ECMN9999`; events `corporate-schedule-payment-1`.
- **`POST /corporate/v2/earmarks`** (`post-corporate-v2-earmarks`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `internal_operation`; response statuses 201, 400, 401, 403, 409, 423, 500; error codes in examples `WOBK0007`, `WEAM0014`, `WEAM0015`, `WEAM0005`, `WEAM0006`, `WEAM0017`, `WEAM0019`, `WEAM0026`, `WEAM0036`, `WEAM0037`, `WEAM0039`, `WEAM0040`, `WEAM0047`, `WEAM0042`, `WEAM0043`, `WEAM0044`, `WEAM0045`, `WEAM0046`, `WEAM0016`, `WEAM0018`, `WEAM0009`, `WEAM0020`, `WEAM0023`, `WEAM0024`, `WEAM0001`, `WEAM0025`, `WEAM0034`, `WEAM0033`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-earmark-1`, `platform-authorization-platform-authorization-1`, `transaction-creation-1`.
- **`PATCH /corporate/v2/earmarks/{earmarkId}`** (`patch-corporate-v2-earmarks-earmarkid`): security `BearerAuth`; required parameters `earmarkId` (path); required body fields `internal_operation`; response statuses 200, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WEAM0014`, `WEAM0015`, `WEAM0016`, `WEAM0017`, `WEAM0018`, `WEAM0019`, `WEAM0026`, `WEAM0027`, `WEAM0030`, `WEAM0031`, `WEAM0036`, `WEAM0038`, `WEAM0039`, `WEAM0040`, `WEAM0047`, `WEAM0041`, `WEAM0042`, `WEAM0043`, `WEAM0044`, `WEAM0045`, `WEAM0046`, `WEAM0023`, `WEAM0024`, `WEAM0025`, `WEAM0034`, `WEAM0049`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-earmark-1`, `platform-authorization-platform-authorization-1`, `transaction-creation-1`.
- **`POST /corporate/v2/earmarks/{earmarkId}/cancel`** (`post-corporate-v2-earmarks-earmarkid-cancel`): security `BearerAuth`; required parameters `earmarkId` (path); required body fields `internal_operation`; response statuses 200, 400, 401, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WEAM0014`, `WEAM0015`, `WEAM0008`, `WEAM0017`, `WEAM0018`, `WEAM0019`, `WEAM0022`, `WCAC0012`, `WEAM0036`, `WEAM0039`, `WEAM0040`, `WEAM0047`, `WEAM0041`, `WEAM0042`, `WEAM0043`, `WEAM0044`, `WEAM0045`, `WEAM0046`, `WEAM0024`, `WEAM0007`, `WEAM0025`, `WEAM0034`, `WEAM0049`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-earmark-1`, `platform-authorization-platform-authorization-1`, `transaction-creation-1`.
- **`POST /corporate/v1/hierarchies`** (`post-hierarchies`): security `BearerAuth`; required parameters none declared; required body fields `name`, `levels`; response statuses 201, 400, 401, 403, 500; error codes in examples `WHIE0001`, `WHIE0002`, `WHIE0003`, `WHIE0004`, `WHIE0005`, `WHIE0007`, `ECMN9999`; events `corporate-hierarchy-creation-1`.
- **`POST /corporate/v2/divisions`** (`post-division-v2`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `hierarchy_id`, `level_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WDIV0015`, `WDIV0011`, `WDIV0005`, `WDIV0007`, `WDIV0006`, `WDIV0012`, `WDIV0018`, `WDIV0019`, `WDIV0017`, `WDIV0016`, `ECMN9999`; events `corporate-division-creation-2`.
- **`PATCH /corporate/v2/divisions/{divisionCode}`** (`patch-division-v2`): security `BearerAuth`; required parameters `divisionCode` (path); required body fields none declared; response statuses 204, 400, 401, 403, 404, 500; error codes in examples `WDIV0015`, `WDIV0011`, `WDIV0005`, `WDIV0007`, `WDIV0006`, `WDIV0008`, `WDIV0009`, `WDIV0010`, `WDIV0012`, `WDIV0018`, `WDIV0019`, `WDIV0002`, `WDIV0017`, `ECMN9999`; events `corporate-division-change-2`.
- **`POST /bank-statements/v1/account-balances/history/config`** (`post-account-balance-history-configuration`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `cycle_closing_time`, `cycle_event_delay`; response statuses 201, 400, 404, 409, 500; error codes in examples `WCFG0002`, `WCFG0001`, `WCFG0003`, `WCFG0004`, `ECMN9999`; events `account-balances-balance-history-config-creation-1`.
- **`PATCH /bank-statements/v1/account-balances/history/config/{divisionCode}`** (`patch-account-balances-history-configuration`): security `BearerAuth`; required parameters `divisionCode` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `WCFG0002`, `WCFG0001`, `WCFG0003`, `WCFG0005`, `ECMN9999`; events `account-balances-balance-history-config-change-1`.
- **`POST /corporate/v2/dormancy-config`** (`post-dormancy-config-v2`): security `BearerAuth`; required parameters none declared; required body fields `check_time`, `target_type`, `target_id`, `statuses`; response statuses 201, 400, 401, 403, 404, 500; error codes in examples `WDOR0001`, `WDOR0002`, `WDOR0010`, `WDOR0011`, `WDOR0005`, `WDOR0006`, `WDOR0008`, `WDOR0009`, `WDOR0004`, `WDOR0003`, `ECMN9999`; events `corporate-dormancy-config-creation-1`.
- **`PATCH /corporate/v2/dormancy-config/{dormancyConfigId}`** (`patch-dormancy-config-v2`): security `BearerAuth`; required parameters `dormancyConfigId` (path); required body fields none declared; response statuses 204, 400, 401, 403, 404, 500; error codes in examples `WDOR0001`, `WDOR0002`, `WDOR0010`, `WDOR0011`, `WDOR0005`, `WDOR0006`, `WDOR0009`, `WDOR0007`, `ECMN9999`; events `corporate-dormancy-config-change-1`.
- **`POST /corporate/v1/checks`** (`corporate-post-v1-checks`): security `BearerAuth`; required parameters none declared; required body fields `check_id`, `check_amount`, `settlement_type`, `settlements`; response statuses 202, 400, 401, 403, 409, 500; error codes in examples `WCPT0001`, `WCPT0002`, `WCMN0002`, `WCPT0006`, `WCPT0007`, `WCPT0008`, `WCPT0010`, `WCPT0011`, `WCPT0004`, `WCPT0018`, `WCPT0009`, `WCPT0012`, `WCPT0014`, `WCPT0016`, `WCPT0017`, `WCAC0001`, `WCPT0005`, `WCPT0013`, `ECMN9999`; events `cash-management-check-status-change-1`, `platform-authorization-platform-authorization-1`.
- **`POST /corporate/v1/checks/release`** (`post-corporate-v1-checks-release`): security `BearerAuth`; required parameters none declared; required body fields `check_id`; response statuses 202, 400, 401, 403, 404, 409, 500; error codes in examples `WCPT0001`, `WCPT0002`, `WCPT0004`, `WCPT0018`, `WOBK0007`, `WCPT0011`, `WCPT0015`, `WCPT0003`, `WCPT0013`, `WCPT0019`, `ECMN9999`; events `cash-management-check-status-change-1`, `platform-authorization-platform-authorization-1`.
- **`POST /corporate/v1/checks/{checkId}/cancel`** (`post-corporate-v1-checks-checkId-cancel`): security `BearerAuth`; required parameters `checkId` (path); required body fields none declared; response statuses 202, 400, 401, 403, 404, 409, 500; error codes in examples `WCPT0002`, `WCPT0004`, `WCPT0018`, `WOBK0007`, `WCPT0011`, `WCPT0003`, `WCPT0013`, `WCPT0019`, `ECMN9999`; events `cash-management-check-status-change-1`, `platform-authorization-platform-authorization-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-v2-post-multileg-payments` | `account-balances-balance-change-1` |
| `corporate-v2-post-payments` | `account-balances-balance-change-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `account-balances-balance-change-1` |
| `post-corporate-v2-earmarks` | `account-balances-balance-change-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `account-balances-balance-change-1` |
| `patch-account-balances-history-configuration` | `account-balances-balance-history-config-change-1` |
| `post-account-balance-history-configuration` | `account-balances-balance-history-config-creation-1` |
| `patch-account` | `account-status-change-2` |
| `post-accounts-accountId-close` | `account-status-change-2` |
| `corporate-v2-post-multileg-payments` | `accounting-entry-creation-1` |
| `corporate-v2-post-payments` | `accounting-entry-creation-1` |
| `corporate-v2-post-multileg-payments` | `availables-change-available-1` |
| `corporate-v2-post-payments` | `availables-change-available-1` |
| `corporate-v2-post-scheduled-payments` | `availables-change-available-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `availables-change-available-1` |
| `post-corporate-v2-earmarks` | `availables-change-available-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `availables-change-available-1` |
| `corporate-post-v1-checks` | `cash-management-check-status-change-1` |
| `post-corporate-v1-checks-checkId-cancel` | `cash-management-check-status-change-1` |
| `post-corporate-v1-checks-release` | `cash-management-check-status-change-1` |
| `patch-account` | `corporate-corporate-account-change-1` |
| `post-account` | `corporate-corporate-account-creation-1` |
| `patch-division-v2` | `corporate-division-change-2` |
| `post-division-v2` | `corporate-division-creation-2` |
| `patch-dormancy-config-v2` | `corporate-dormancy-config-change-1` |
| `post-dormancy-config-v2` | `corporate-dormancy-config-creation-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `corporate-earmark-1` |
| `post-corporate-v2-earmarks` | `corporate-earmark-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `corporate-earmark-1` |
| `post-hierarchies` | `corporate-hierarchy-creation-1` |
| `corporate-v2-post-multileg-payments` | `corporate-multi-leg-creation-1` |
| `corporate-v2-post-multileg-payments` | `corporate-multi-leg-status-change-1` |
| `corporate-v2-delete-scheduled-payment` | `corporate-schedule-payment-1` |
| `corporate-v2-post-scheduled-payments` | `corporate-schedule-payment-1` |
| `post-account` | `onboarding-succeeded-1` |
| `corporate-post-v1-checks` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-multileg-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-scheduled-payments` | `platform-authorization-platform-authorization-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v1-checks-checkId-cancel` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v1-checks-release` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v2-earmarks` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-multileg-payments` | `rules-evaluation-requested-1` |
| `corporate-v2-post-payments` | `rules-evaluation-requested-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `transaction-creation-1` |
| `post-corporate-v2-earmarks` | `transaction-creation-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `transaction-creation-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `account-balances-balance-change-1` | account | 1 | https://developers.pismo.io/events/docs/account-balances-balance-change-1 | 16 | KU-EVT-catalogue-account |
| `account-balances-balance-history-config-change-1` | account | 1 | https://developers.pismo.io/events/docs/account-balances-balance-history-config-change-1 | 2 | KU-EVT-catalogue-account |
| `account-balances-balance-history-config-creation-1` | account | 1 | https://developers.pismo.io/events/docs/account-balances-balance-history-config-creation-1 | 2 | KU-EVT-catalogue-account |
| `account-status-change-2` | account | 2 | https://developers.pismo.io/events/docs/account-status-change-2 | 6 | KU-EVT-catalogue-account |
| `accounting-entry-creation-1` | accounting | 1 | https://developers.pismo.io/events/docs/accounting-entry-creation-1 | 4 | KU-EVT-catalogue-other-domains |
| `availables-change-available-1` | availables | 1 | https://developers.pismo.io/events/docs/availables-change-available-1 | 22 | KU-EVT-catalogue-other-domains |
| `cash-management-check-status-change-1` | cash | 1 | https://developers.pismo.io/events/docs/cash-management-check-status-change-1 | 3 | KU-EVT-catalogue-other-domains |
| `corporate-corporate-account-creation-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-corporate-account-creation-1 | 1 | KU-EVT-catalogue-corporate |
| `corporate-dormancy-config-change-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-dormancy-config-change-1 | 1 | KU-EVT-catalogue-corporate |
| `corporate-dormancy-config-creation-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-dormancy-config-creation-1 | 1 | KU-EVT-catalogue-corporate |
| `corporate-earmark-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-earmark-1 | 6 | KU-EVT-catalogue-corporate |
| `corporate-hierarchy-creation-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-hierarchy-creation-1 | 1 | KU-EVT-catalogue-corporate |
| `corporate-schedule-payment-1` | corporate | 1 | https://developers.pismo.io/events/docs/corporate-schedule-payment-1 | 3 | KU-EVT-catalogue-corporate |
| `onboarding-succeeded-1` | onboarding | 1 | https://developers.pismo.io/events/docs/onboarding-succeeded-1 | 4 | KU-EVT-catalogue-other-domains |
| `platform-authorization-platform-authorization-1` | platform | 1 | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 | 32 | KU-EVT-catalogue-other-domains |
| `transaction-creation-1` | transaction | 1 | https://developers.pismo.io/events/docs/transaction-creation-1 | 7 | KU-EVT-catalogue-transaction |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/corporate-banking-data-events.md`: updatedAt 2026-08-25T20:51:22.000Z.
- Links to `corporate-v2-post-multileg-payments`, which is marked `deprecated: true` in `api-specs/Banking_-_Transaction_banking.yaml`.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 19 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/corporate-banking-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/corporate-banking-data-events | `a9dd7fce44c9c2b9…` | 2026-08-25T20:51:22.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--check-posting` — API reference: Banking - Transaction banking — Check posting
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--hierarchies` — API reference: Banking - Transaction banking — Hierarchies
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
