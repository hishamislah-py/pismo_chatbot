---
ku_id: KU-EVT-accounts-data-events
title: Core platform - Accounts
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/accounts-data-events.md
  sha256: dc3d4222e81abc6715017e223397b4a0a430010054673a273ea0bec9157e80f7
  url: https://developers.pismo.io/pismo-docs/docs/accounts-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:14:48.000Z'
operations:
- PostMigrationProgram
- customerV1patch
- customerV2Post
- customerV2Put
- patch-accounts-v1-accounts
- patch-accounts-v1-accounts-accountId-addresses-addressId
- patch-accounts-v1-accounts-accountId-phones-phoneId
- patch-accounts-v2-accounts-accountId-status
- patch-v1-account-limit
- patch-v2-accounts-accountId-status-rollback
- post-accounts-v1-accounts-accountId-addresses
- post-accounts-v1-accounts-accountId-phones
- post-acquisitions-v2-s2s-applications
- post-acquisitions-v3-s2s-applications
related_kus:
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--addresses
- KU-API-core-platform-accounts--customers
- KU-API-core-platform-accounts--phones
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-API-core-platform-accounts--transfer-account
- KU-API-core-platform-ledger--account-limits
- KU-EVT-catalogue-account
- KU-EVT-catalogue-audit
- KU-EVT-catalogue-other-domains
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Core platform - Accounts

**KU ID:** `KU-EVT-accounts-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/accounts-data-events.md`:

> This table lists the accounts endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/accounts-data-events.md`: Core platform - Accounts

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 14 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/accounts-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accounts-data-events · updatedAt: 2026-03-18T15:14:48.000Z

<!-- source:begin path=docs/data-and-reporting/accounts-data-events.md part=0-end -->

# Core platform - Accounts

This table lists the accounts endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Endpoint
      </th>

      <th style={{ textAlign: "left" }}>
        Event
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) (with `submit=false`)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account application prospect created](https://developers.pismo.io/events/docs/onboarding-prospect-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) (with `submit=true`)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account application created](https://developers.pismo.io/events/docs/onboarding-succeeded-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create account application (outdated)](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v2-s2s-applications) (with `submit=false`)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account application prospect created](https://developers.pismo.io/events/docs/onboarding-prospect-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create account application (outdated)](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v2-s2s-applications) (with `submit=true`)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account application created](https://developers.pismo.io/events/docs/onboarding-succeeded-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update account status](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v2-accounts-accountid-status)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Roll back account status](https://developers.pismo.io/pismo-docs/reference/patch-v2-accounts-accountid-status-rollback)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Migrate account to different program](https://developers.pismo.io/pismo-docs/reference/postmigrationprogram)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account migrated to different program](https://developers.pismo.io/events/docs/account-program-migration-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update account custom fields](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v1-accounts)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account information changed](https://developers.pismo.io/events/docs/account-account-change-2)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account limit changed](https://developers.pismo.io/events/docs/ledger-limit-changed-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create customer](https://developers.pismo.io/pismo-docs/reference/customerv2post)
      </td>

      <td style={{ textAlign: "left" }}>
        [Customer created](https://developers.pismo.io/events/docs/account-customer-creation-1)

        [Account owner changed](https://developers.pismo.io/events/docs/account-account-owner-change-1)  (if `customer.is_owner ` is  `true`)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update customer information](https://developers.pismo.io/pismo-docs/reference/customerv2put)
      </td>

      <td style={{ textAlign: "left" }}>
        [Customer changed](https://developers.pismo.io/events/docs/account-customer-change-2)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update customer information](https://developers.pismo.io/pismo-docs/reference/customerv1patch)
      </td>

      <td style={{ textAlign: "left" }}>
        [Account entity updated](https://developers.pismo.io/events/docs/audit-entity-change-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create phone number](https://developers.pismo.io/pismo-docs/reference/post-accounts-v1-accounts-accountid-phones)
      </td>

      <td style={{ textAlign: "left" }}>
        [Phone created](https://developers.pismo.io/events/docs/audit-phone-creation-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update phone number](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v1-accounts-accountid-phones-phoneid)
      </td>

      <td style={{ textAlign: "left" }}>
        [Phone updated](https://developers.pismo.io/events/docs/audit-phone-change-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Create address](https://developers.pismo.io/pismo-docs/reference/post-accounts-v1-accounts-accountid-addresses)
      </td>

      <td style={{ textAlign: "left" }}>
        [Address created](https://developers.pismo.io/events/docs/audit-address-creation-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Update address](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v1-accounts-accountid-addresses-addressid)
      </td>

      <td style={{ textAlign: "left" }}>
        [Address updated](https://developers.pismo.io/events/docs/audit-address-change-1)
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /acquisitions/v2/s2s/applications` | `post-acquisitions-v2-s2s-applications` | Create account application (deprecated) | `api-specs/Core_platform_-_Accounts.yaml` | **yes** | KU-API-core-platform-accounts--accounts |
| `PATCH /accounts/v2/accounts/{accountId}/status` | `patch-accounts-v2-accounts-accountId-status` | Update status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `PATCH /accounts/v2/accounts/{accountId}/status/rollback` | `patch-v2-accounts-accountId-status-rollback` | Roll back status | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `POST /accounts/v1/accounts/programs/migration` | `PostMigrationProgram` | Transfer account to different program | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--transfer-account |
| `PATCH /accounts/v1/accounts/{accountId}` | `patch-accounts-v1-accounts` | Update account | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limit` | Update account limits (outdated) | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |
| `POST /accounts/v2/customers` | `customerV2Post` | Create customer | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |
| `PUT /accounts/v2/customers/{customerId}` | `customerV2Put` | Overwrite customer | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |
| `PATCH /accounts/v1/accounts/{accountId}/customers/{customerId}/detail` | `customerV1patch` | Update person or company customer | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |
| `POST /accounts/v1/accounts/{accountId}/phones` | `post-accounts-v1-accounts-accountId-phones` | Create phone | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--phones |
| `PATCH /accounts/v1/accounts/{accountId}/phones/{phoneId}` | `patch-accounts-v1-accounts-accountId-phones-phoneId` | Update phone | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--phones |
| `POST /accounts/v1/accounts/{accountId}/addresses` | `post-accounts-v1-accounts-accountId-addresses` | Create address | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--addresses |
| `PATCH /accounts/v1/accounts/{accountId}/addresses/{addressId}` | `patch-accounts-v1-accounts-accountId-addresses-addressId` | Update address | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--addresses |

### Operation essentials

- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /acquisitions/v2/s2s/applications`** (`post-acquisitions-v2-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`PATCH /accounts/v2/accounts/{accountId}/status`** (`patch-accounts-v2-accounts-accountId-status`): security `BearerAuth`; required parameters `accountId` (path); required body fields `status`; response statuses 204, 400, 404, 500; error codes in examples none; events `account-status-change-2`.
- **`PATCH /accounts/v2/accounts/{accountId}/status/rollback`** (`patch-v2-accounts-accountId-status-rollback`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 204, 404, 500; error codes in examples none; events `account-status-change-2`.
- **`POST /accounts/v1/accounts/programs/migration`** (`PostMigrationProgram`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `program`; response statuses 200, 400, 404, 409, 500; error codes in examples none; events `account-program-migration-1`.
- **`PATCH /accounts/v1/accounts/{accountId}`** (`patch-accounts-v1-accounts`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 401, 404, 500; error codes in examples none; events `account-account-change-2`.
- **`PATCH /v1/accounts/{accountId}/limits`** (`patch-v1-account-limit`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `WLDG0021`, `WLDG0010`, `WLDG0025`, `WLDG0022`, `ELDG9999`; events `ledger-limit-changed-1`.
- **`POST /accounts/v2/customers`** (`customerV2Post`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `entity`, `customer`; response statuses 201, 400, 409, 500; error codes in examples none; events `account-account-owner-change-1`, `account-customer-creation-1`.
- **`PUT /accounts/v2/customers/{customerId}`** (`customerV2Put`): security `BearerAuth`; required parameters `customerId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events `account-customer-change-2`.
- **`PATCH /accounts/v1/accounts/{accountId}/customers/{customerId}/detail`** (`customerV1patch`): security `BearerAuth`; required parameters `x-tenant` (header), `accountId` (path), `customerId` (path); required body fields none declared; response statuses 200, 404, 500; error codes in examples none; events `account-owner-change-1`, `audit-entity-change-1`.
- **`POST /accounts/v1/accounts/{accountId}/phones`** (`post-accounts-v1-accounts-accountId-phones`): security `BearerAuth`; required parameters `accountId` (path); required body fields `number`, `type`; response statuses 200, 400, 409, 500; error codes in examples none; events `audit-phone-creation-1`.
- **`PATCH /accounts/v1/accounts/{accountId}/phones/{phoneId}`** (`patch-accounts-v1-accounts-accountId-phones-phoneId`): security `BearerAuth`; required parameters `accountId` (path), `phoneId` (path); required body fields none declared; response statuses 200, 400, 422, 500; error codes in examples none; events `audit-phone-change-1`.
- **`POST /accounts/v1/accounts/{accountId}/addresses`** (`post-accounts-v1-accounts-accountId-addresses`): security `BearerAuth`; required parameters `accountId` (path); required body fields `type`, `address`, `number`, `zip_code`, `city`, `state`, `country`, `neighborhood`; response statuses 201, 400, 500; error codes in examples none; events `audit-address-creation-1`.
- **`PATCH /accounts/v1/accounts/{accountId}/addresses/{addressId}`** (`patch-accounts-v1-accounts-accountId-addresses-addressId`): security `BearerAuth`; required parameters `accountId` (path), `addressId` (path); required body fields none declared; response statuses 201, 500; error codes in examples none; events `audit-address-change-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-accounts-v1-accounts` | `account-account-change-2` |
| `customerV2Post` | `account-account-owner-change-1` |
| `customerV2Put` | `account-customer-change-2` |
| `customerV2Post` | `account-customer-creation-1` |
| `customerV1patch` | `account-owner-change-1` |
| `PostMigrationProgram` | `account-program-migration-1` |
| `patch-accounts-v2-accounts-accountId-status` | `account-status-change-2` |
| `patch-v2-accounts-accountId-status-rollback` | `account-status-change-2` |
| `patch-accounts-v1-accounts-accountId-addresses-addressId` | `audit-address-change-1` |
| `post-accounts-v1-accounts-accountId-addresses` | `audit-address-creation-1` |
| `customerV1patch` | `audit-entity-change-1` |
| `patch-accounts-v1-accounts-accountId-phones-phoneId` | `audit-phone-change-1` |
| `post-accounts-v1-accounts-accountId-phones` | `audit-phone-creation-1` |
| `patch-v1-account-limit` | `ledger-limit-changed-1` |
| `post-acquisitions-v2-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v2-s2s-applications` | `onboarding-succeeded-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `account-account-change-2` | account | 2 | https://developers.pismo.io/events/docs/account-account-change-2 | 1 | KU-EVT-catalogue-account |
| `account-account-owner-change-1` | account | 1 | https://developers.pismo.io/events/docs/account-account-owner-change-1 | 2 | KU-EVT-catalogue-account |
| `account-customer-change-2` | account | 2 | https://developers.pismo.io/events/docs/account-customer-change-2 | 1 | KU-EVT-catalogue-account |
| `account-customer-creation-1` | account | 1 | https://developers.pismo.io/events/docs/account-customer-creation-1 | 1 | KU-EVT-catalogue-account |
| `account-program-migration-1` | account | 1 | https://developers.pismo.io/events/docs/account-program-migration-1 | 1 | KU-EVT-catalogue-account |
| `account-status-change-2` | account | 2 | https://developers.pismo.io/events/docs/account-status-change-2 | 6 | KU-EVT-catalogue-account |
| `audit-address-change-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-address-change-1 | 1 | KU-EVT-catalogue-audit |
| `audit-address-creation-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-address-creation-1 | 1 | KU-EVT-catalogue-audit |
| `audit-entity-change-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-entity-change-1 | 1 | KU-EVT-catalogue-audit |
| `audit-phone-change-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-phone-change-1 | 1 | KU-EVT-catalogue-audit |
| `audit-phone-creation-1` | audit | 1 | https://developers.pismo.io/events/docs/audit-phone-creation-1 | 1 | KU-EVT-catalogue-audit |
| `ledger-limit-changed-1` | ledger | 1 | https://developers.pismo.io/events/docs/ledger-limit-changed-1 | 2 | KU-EVT-catalogue-other-domains |
| `onboarding-prospect-1` | onboarding | 1 | https://developers.pismo.io/events/docs/onboarding-prospect-1 | 2 | KU-EVT-catalogue-other-domains |
| `onboarding-succeeded-1` | onboarding | 1 | https://developers.pismo.io/events/docs/onboarding-succeeded-1 | 4 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/accounts-data-events.md`: updatedAt 2026-03-18T15:14:48.000Z.
- Links to `post-acquisitions-v2-s2s-applications`, which is marked `deprecated: true` in `api-specs/Core_platform_-_Accounts.yaml`.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 14 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/accounts-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accounts-data-events | `dc3d4222e81abc67…` | 2026-03-18T15:14:48.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--addresses` — API reference: Core platform - Accounts — Addresses
- `KU-API-core-platform-accounts--customers` — API reference: Core platform - Accounts — Customers
- `KU-API-core-platform-accounts--phones` — API reference: Core platform - Accounts — Phones
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-API-core-platform-accounts--transfer-account` — API reference: Core platform - Accounts — Transfer account
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-audit` — Event catalogue: audit
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
