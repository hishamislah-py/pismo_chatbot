---
ku_id: KU-LIFE-api-endpoint-deprecation-and-removal-schedule
title: API endpoint deprecation and removal schedule
category: api_lifecycle
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/resources/api-endpoint-deprecation-and-removal-schedule.md
  sha256: a64c24d14bc086fca25f439cea62c70460686c82799d33bfe6c173243935f72a
  url: https://developers.pismo.io/pismo-docs/docs/api-endpoint-deprecation-and-removal-schedule
  role: primary_guide
  updated_at: '2026-10-08T03:38:36.000Z'
operations:
- CreateInstallmentAdvancementV2
- GetInstallmentAdvancementV2ById
- SearchTranscationMetaDataCount
- SimulateInstallmentAdvancement
- cancelInstallmentAdvanceV2
- corporate-v2-get-multileg-payment
- corporate-v2-post-multileg-payments
- corporate-v3-get-multileg-payment
- corporate-v3-post-multileg-payments
- getTransactionTypes_1
- merchants-advancements
- merchants-advancements-data
related_kus:
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-core-platform-transactions--transactions
- KU-API-revolving-credit-installment-management--installment-advancements
- KU-API-revolving-credit-installment-management--simulations
- KU-API-revolving-credit-statements--transaction-types
- KU-API-seller-management-merchant-advance--merchant-advancement
- KU-EVT-catalogue-account
- KU-EVT-catalogue-balance
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-merchants
- KU-EVT-catalogue-other-domains
- KU-LIFE-api-deprecation-strategy
grouping_rationale: single source page
---

# API endpoint deprecation and removal schedule

**KU ID:** `KU-LIFE-api-endpoint-deprecation-and-removal-schedule` · **Category:** API lifecycle · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/resources/api-endpoint-deprecation-and-removal-schedule.md`:

> This guide lists the current API endpoint deprecation schedule. For detailed information about each item, refer to the sections below.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/resources/api-endpoint-deprecation-and-removal-schedule.md`: API endpoint deprecation and removal schedule

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 12 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/resources/api-endpoint-deprecation-and-removal-schedule.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/api-endpoint-deprecation-and-removal-schedule · updatedAt: 2026-10-08T03:38:36.000Z

<!-- source:begin path=docs/resources/api-endpoint-deprecation-and-removal-schedule.md part=0-end -->

# API endpoint deprecation and removal schedule

This guide lists the current API endpoint deprecation schedule. For detailed information about each item, refer to the sections below.

| API                                              | Sunset date | Decommission date – Test (EXT) | Decommission date – Production |
| :----------------------------------------------- | :---------- | :----------------------------- | :----------------------------- |
| Holidays and admin divisions                     | Apr 2026    | 30 Oct 2026                    | 30 Oct 2026                    |
| Installments: Installment advancement endpoints  | Aug 2026    | 24 Feb, 2027                   | 24 Feb, 2027                   |
| Merchant advancements                            | Nov 2026    | 15 May 2026                    | 15 May 2026                    |
| Statements: List program transaction types       | Mar 2026    | 26 Sep 2026                    | 28 Sep 2026                    |
| Transaction banking: Multi-leg payment endpoints | Nov 2025    | 6 Nov 2026                     | 6 Nov 2026                     |
| Transactions: Get transaction count              | Aug 2026    | 22 Feb 2027                    | 22 Feb 2027                    |

For more information about Pismo's API life cycle, refer to [API life cycle and deprecation strategy](https://developers.pismo.io/pismo-docs/docs/api-deprecation-strategy).

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Holidays and admin divisions</summary>

  > 🚧 Decommission and removal date
  >
  > The deprecated endpoints listed here will be decommissioned (removed) on **October 2026** (PISMO-312616).

  <Table align={["left","left"]}>
    <thead>
      <tr>
        <th>
          Deprecated endpoints
        </th>

        <th>
          Replacement endpoints
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-holiday">Create holiday</a><br />
          POST  /holidays-core/v2/holiday
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-add-holiday-to-calendar">Add holiday</a><br />
          POST /v1/holiday-calendar/holiday
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-v1-orgs-holidays">List holidays</a><br />
          GET /orgs-core/v1/orgs/holidays
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-holiday-new">List holidays</a><br />
          GET /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_id}/holiday
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/put-v1-orgs-holidays">Update holiday</a><br />
          PUT /orgs-core/v1/orgs/holidays/\{id}
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/update-holiday">Update holiday</a><br />
          PATCH /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_id}/holiday/\{holiday\_id}
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/delete-v1-orgs-holidays">Delete holiday</a><br />
          DELETE /orgs-core/v1/orgs/holidays/\{id}
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/delete-holiday">Delete holiday</a><br />
          DELETE /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_id}/holiday/\{holiday\_id}
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-holiday">Create holiday</a><br />
          POST /holidays-core/v1/holiday
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-add-holiday-to-calendar">Add holiday</a><br />
          POST /holidays-core/v1/holiday-calendar/holiday
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-v1-holidays">List holidays</a><br />
          GET /holidays-core/v1/holiday
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-holiday-new">List holidays</a><br />
          GET /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_id}/holiday
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/validate-v1-holiday">Get holiday</a><br />
          POST /holidays-core/v1/holiday/validate
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-search-business-day">Get business day</a><br />
          POST /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_id}/business-day
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/validate-v1-holiday">Update holiday name</a><br />
          PUT /holidays-core/v1/holiday/\{holiday\_id}
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/update-holiday">Update holiday</a><br />
          PATCH /holidays-core/v1/holiday-Update holidaycalendar/\{holiday\_calendar\_id}/holiday/\{holiday\_id}
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/delete-v1-holiday">Delete holiday</a><br />
          DELETE /holidays-core/v1/holiday/\{holiday\_id}
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/delete-holiday">Delete holiday</a><br />
          DELETE /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_id}/holiday/\{holiday\_id}
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/v1-search-business-day">Check if business day</a><br />
          POST /holidays-core/v1/search-business-day
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-search-business-day">Get business day</a><br />
          POST /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_id}/business-day
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/v1-get-non-business-days">List non-business days</a><br />
          GET /holidays-core/v1/non-business-days
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-non-business-days">Get non-business days</a><br />
          GET /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_id}/non-business-days
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-v1-holidays-with-administrative-divisions-ancestors">List holidays with admin division ancestors</a><br />
          GET /holidays-core/v1/holiday/administrative-division/\{administrative\_division\_id}/ancestors
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/list-holiday-calendars">List holiday calendars</a><br />
          GET /holidays-core/v1/holiday-calendar
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-holiday">Create holiday</a><br />
          POST /holidays-core/v2/holiday
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-add-holiday-to-calendar">Add holiday</a><br />
          POST /holidays-core/v1/holiday-calendar/holiday
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-v1-holidays">List holidays</a><br />
          GET /holidays-core/v2/holiday
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/list-holiday-calendars">List holiday calendars</a><br />
          GET /holidays-core/v1/holiday-calendarOST /holidays-core/v1/holiday-calendar/holiday
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/update-holiday">Update holiday</a><br />
          PUT /holidays-core/v2/holiday/\{holiday\_id}
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/list-holiday-calendars">Update holiday</a><br />
          PATCH /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_id}/holiday/\{holiday\_id}
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-v1-admin-division">Create administrative division</a><br />
          POST /divisions-core/v1/administrative-division
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-create-holiday-calendar">Create holiday calendar</a><br />
          POST /holidays-core/v1/holiday-calendar
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-v1-admin-division-external-id">Get admin division info by external ID </a><br />
          GET /divisions-core/v1/administrative-division/external-id/\{id}
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-holiday-calendar-by-external-id">Get calendar by external ID</a><br />
          GET /holidays-core/v1/holiday-calendar/external-id/\{holiday\_external\_id}
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-v1-admin-division">Get admin division info </a><br />
          GET /divisions-core/v1/administrative-division/\{id}
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-holiday-calendar">Get holiday calendar</a><br />
          GET /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_ID}
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/put-v2-admin-division">Update administrative division </a><br />
          PUT /divisions-core/v1/administrative-division/\{id}
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/update-holiday-calendar">Update holiday calendar</a><br />
          PATCH /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_ID}
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/delete-v1-admin-division">Delete administrative division </a><br />
          DELETE /divisions-core/v1/administrative-division/\{id}
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/delete-holiday-calendar">Delete holiday calendar</a><br />
          DELETE /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_ID}
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-v1-admin-division-tree-parent-id">Get admin division tree by admin division ID  </a><br />
          GET /divisions-core/v1/administrative-division/\{id}/tree
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/list-holiday-calendars">List holiday calendars</a><br />
          GET /holidays-core/v1/holiday-calendar
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-v1-admin-division-tree-external-id">Get admin division tree by external ID  </a><br />
          GET /divisions-core/v1/administrative-division/external-id/\{id}/tree
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/list-holiday-calendars">List holiday calendars</a><br />
          GET /holidays-core/v1/holiday-calendar
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-v1-admin-division-ancestors-administrative-division-id">Get admin division ancestors by admin division ID </a><br />
          GET /divisions-core/v1/administrative-division/external-id/\{id}/tree
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/list-holiday-calendars">List holiday calendars</a><br />
          GET /holidays-core/v1/holiday-calendar
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-v1-admin-division-ancestors-external-id">Get admin division ancestors by external ID </a><br />
          GET /divisions-core/v1/administrative-division/external-id/\{id}/ancestors
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/list-holiday-calendars">List holiday calendars</a><br />
          GET /holidays-core/v1/holiday-calendar
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-v1-admin-division">Create administrative division</a><br />
          POST /divisions-core/v2/administrative-division
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/post-create-holiday-calendar">Create holiday calendar</a><br />
          POST /holidays-core/v1/holiday-calendar
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-v1-admin-division">Get admin division info</a><br />
          GET /divisions-core/v2/administrative-division/\{id}
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/get-holiday-calendar">Get holiday calendar</a><br />
          GET /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_ID}
        </td>
      </tr>

      <tr>
        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/put-v1-admin-division">Update administrative division</a><br />
          PUT /divisions-core/v2/administrative-division/\{id}
        </td>

        <td>
          <a href="https://developers.pismo.io/pismo-docs/reference/update-holiday-calendar">Update holiday calendar</a><br />
          PATCH /holidays-core/v1/holiday-calendar/\{holiday\_calendar\_ID}
        </td>
      </tr>
    </tbody>
  </Table>
</details>

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Installments</summary>

  > 🚧 Decommission and removal date
  >
  > The deprecated endpoints listed here will be decommissioned (removed) on **24 February, 2027** (PISMO-340196).

  | Deprecated endpoints                                                                         | Replacement endpoints                                                  |
  | :------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
  | POST installment-management/v1/accounts/\{accountId}/installment-advance                     | [Create installment advancement](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancementv2)   |
  | POST /statements/v2/accounts/\{accountId}/installment-advance                                | [Create installment advancement](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancementv2)   |
  | GET /installment-management/v1/accounts/\{accountId}/installment-advance/\{advancementId}    | [Get installment advancement](https://developers.pismo.io/pismo-docs/reference/getinstallmentadvancementv2byid)     |
  | GET /statements/v2/accounts/\{accountId}/installment-advance/\{id}                           | [Get installment advancement](https://developers.pismo.io/pismo-docs/reference/getinstallmentadvancementv2byid)     |
  | DELETE /installment-management/v1/accounts/\{accountId}/installment-advance/\{advancementId} | [Cancel installment advancement](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentadvancev2)       |
  | DELETE /statements/v2/accounts/\{accountId}/installment-advance/\{id}                        | [Cancel installment advancement](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentadvancev2)       |
  | GET /statements/v2/accounts/\{accountId}/installment-advance                                 | [Simulate installment advancement](https://developers.pismo.io/pismo-docs/reference/simulateinstallmentadvancement) |
</details>

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Merchant advancements</summary>

  > 🚧 Decommission and removal date
  >
  > The deprecated endpoints listed here will be decommissioned (removed) on **21 November 2026** (PISMO–350162).

  <Table align={["left","left"]}>
    <thead>
      <tr>
        <th>
          Deprecated endpoints
        </th>

        <th>
          Replacement endpoints
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          POST /merchants/v2/merchants/{'{merchantId}'}/advancements

          GET /merchants/v1/merchants/{'{merchantId}'}/advancements/requests/{'{advancementRequestId}'}
        </td>

        <td>
          [Simulate merchant advancement](https://developers.pismo.io/pismo-docs/reference/merchants-advancements)
          [Get advancement](https://developers.pismo.io/pismo-docs/reference/merchants-advancements-data)
        </td>
      </tr>
    </tbody>
  </Table>
</details>

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Statements</summary>

  > 🚧 Decommission and removal date
  >
  > The deprecated endpoint listed here will be decommissioned (removed) on **28 September 2026** (PISMO-331027).

  | Deprecated endpoints                     | Replacement endpoints                                       |
  | :--------------------------------------- | :---------------------------------------------------------- |
  | GET /statements-v2/v1/transactions-types | [List program transaction types](https://developers.pismo.io/pismo-docs/reference/gettransactiontypes_1) |
</details>

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Transaction banking</summary>

  > 🚧 Decommission and removal date
  >
  > The deprecated endpoints listed here will be decommissioned (removed) on **6 November 2026** and replaced by their corresponding v3 endpoints (PISMO-298216).

  | Deprecated endpoint                                                      | Replacement endpoint                                                     |
  | :----------------------------------------------------------------------- | :----------------------------------------------------------------------- |
  | [Post multi-leg payment v2](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments)     | [Post multi-leg payment v3](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments)     |
  | [Get multi-leg payment status v2](https://developers.pismo.io/pismo-docs/reference/corporate-v2-get-multileg-payment) | [Get multi-leg payment status v3](https://developers.pismo.io/pismo-docs/reference/corporate-v3-get-multileg-payment) |
</details>

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Transactions</summary>

  > 🚧 Decommission and removal date
  >
  > The deprecated endpoint listed here will be decommissioned (removed) on **22 February 2027** (391709).

  | Deprecated endpoint                                         | Replacement endpoint |
  | :---------------------------------------------------------- | :------------------- |
  | [Get transaction count](https://developers.pismo.io/pismo-docs/reference/searchtranscationmetadatacount) | None                 |
</details>

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v2/accounts/{accountId}/installment-advance` | `CreateInstallmentAdvancementV2` | Create installment advancement | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `GET /v2/accounts/{accountId}/installment-advance/{advancementId}` | `GetInstallmentAdvancementV2ById` | Get installment advancement | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `DELETE /v2/accounts/{accountId}/installment-advance/{advancementId}` | `cancelInstallmentAdvanceV2` | Cancel installment advancement | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `GET /v1/accounts/{accountId}/installment-advance/simulations` | `SimulateInstallmentAdvancement` | Simulate installment advancement | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--simulations |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements` | `merchants-advancements` | Simulate merchant advancement | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement |
| `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/{advancementId}` | `merchants-advancements-data` | Get advancement | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement |
| `GET /statements-v2/v1/programs-transactions-types` | `getTransactionTypes_1` | List program transaction types | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--transaction-types |
| `POST /corporate/v2/payments/multileg` | `corporate-v2-post-multileg-payments` | Post multi-leg payment (deprecated) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v3/payments/multileg` | `corporate-v3-post-multileg-payments` | Post multi-leg payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `GET /corporate/v2/payments/multileg/{trackingId}` | `corporate-v2-get-multileg-payment` | Get multi-leg payment status (deprecated) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-03 |
| `GET /corporate/v3/payments/multileg/{multilegId}` | `corporate-v3-get-multileg-payment` | Get multi-leg payment status | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-02 |
| `GET /v2/transactions/total-items` | `SearchTranscationMetaDataCount` | Get transaction count (deprecated) | `api-specs/Core_platform_-_Transactions.yaml` | **yes** | KU-API-core-platform-transactions--transactions |

### Operation essentials

- **`POST /v2/accounts/{accountId}/installment-advance`** (`CreateInstallmentAdvancementV2`): security `BearerAuth`; required parameters `accountId` (path); required body fields `condition`, `tracking_id`; response statuses 202, 400, 409, 500; error codes in examples `EX0002`, `GN0001`; events none listed.
- **`GET /v2/accounts/{accountId}/installment-advance/{advancementId}`** (`GetInstallmentAdvancementV2ById`): security `BearerAuth`; required parameters `accountId` (path), `advancementId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `EX307`, `GN0001`; events none listed.
- **`DELETE /v2/accounts/{accountId}/installment-advance/{advancementId}`** (`cancelInstallmentAdvanceV2`): security `BearerAuth`; required parameters `accountId` (path), `advancementId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `EX307`, `GN0001`; events none listed.
- **`GET /v1/accounts/{accountId}/installment-advance/simulations`** (`SimulateInstallmentAdvancement`): security `BearerAuth`; required parameters `accountId` (path), `condition` (query), `reschedule` (query); required body fields none declared; response statuses 200, 400, 409, 500; error codes in examples `EX0002`, `GN0001`; events `balance-installment-advancement-1`.
- **`POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements`** (`merchants-advancements`): security not declared; required parameters `Authorization` (header), `marketplaceId` (path), `merchantId` (path); required body fields `begin_date`, `request_date`, `amount`, `real_time_settlement`; response statuses 200, 400, 404; error codes in examples `EPT0303`, `EPT0303`; events `merchants-advancement-request-1`.
- **`GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/{advancementId}`** (`merchants-advancements-data`): security not declared; required parameters `Authorization` (header), `marketplaceId` (path), `merchantId` (path), `advancementId` (path); required body fields none declared; response statuses 200, 400, 404; error codes in examples `EPT0303`, `EPT0303`; events none listed.
- **`GET /statements-v2/v1/programs-transactions-types`** (`getTransactionTypes_1`): security `BearerAuth`; required parameters `program-id` (header); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`POST /corporate/v2/payments/multileg`** (`corporate-v2-post-multileg-payments`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`; response statuses 202, 400, 403, 500; error codes in examples `WMLP0001`, `WMLP0002`, `WMLP0003`, `WMLP0004`, `WMLP0006`, `WMLP0005`, `WMLP1026`, `WMLP1028`, `WMLP1027`, `WMLP1002`, `WMLP1003`, `WMLP1004`, `WMLP1005`, `WMLP1039`, `WMLP1006`, `WMLP1022`, `WMLP1007`, `WMLP1008`, `WMLP1009`, `WMLP1010`, `WMLP1011`, `WMLP1013`, `WMLP1014`, `WMLP1015`, `WMLP1016`, `WMLP1017`, `WMLP1019`, `WMLP1048`, `WMLP1023`, `WMLP1036`, `WMLP1034`, `WMLP1035`, `WMLP1024`, `WMLP1037`, `WMLP1038`, `WMLP1030`, `WMLP1041`, `WMLP1042`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `corporate-multi-leg-creation-1`, `corporate-multi-leg-status-change-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`POST /corporate/v3/payments/multileg`** (`corporate-v3-post-multileg-payments`): security `BearerAuth`; required parameters none declared; required body fields `multileg_id`; response statuses 202, 400, 403, 409, 500; error codes in examples `WMLP0001`, `WMLP0002`, `WMLP0003`, `WMLP0004`, `WMLP0008`, `WMLP1044`, `WMLP0005`, `WMLP1026`, `WMLP1028`, `WMLP1027`, `WMLP1049`, `WMLP1002`, `WMLP1003`, `WMLP1004`, `WMLP1005`, `WMLP1039`, `WMLP1006`, `WMLP1022`, `WMLP1007`, `WMLP1008`, `WMLP1009`, `WMLP1010`, `WMLP1011`, `WMLP1013`, `WMLP1014`, `WMLP1015`, `WMLP1016`, `WMLP1017`, `WMLP1019`, `WMLP1048`, `WMLP1023`, `WMLP1036`, `WMLP1034`, `WMLP1035`, `WMLP1024`, `WMLP1037`, `WMLP1038`, `WMLP1030`, `WMLP1040`, `WMLP1041`, `WMLP1042`, `WMLP1043`, `WMLP1046`, `WMLP0009`, `ECMN9999`; events `corporate-multi-leg-creation-2`, `corporate-multi-leg-status-change-2`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`GET /corporate/v2/payments/multileg/{trackingId}`** (`corporate-v2-get-multileg-payment`): security `BearerAuth`; required parameters `trackingId` (path); required body fields none declared; response statuses 200, 400, 401, 403, 500; error codes in examples `WMLP0007`, `ECMN9999`; events none listed.
- **`GET /corporate/v3/payments/multileg/{multilegId}`** (`corporate-v3-get-multileg-payment`): security `BearerAuth`; required parameters `multilegId` (path); required body fields none declared; response statuses 200, 404; error codes in examples `WPMT0010`, `WOBK0007`, `WMLP0007`; events none listed.
- **`GET /v2/transactions/total-items`** (`SearchTranscationMetaDataCount`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `WTRC00002`, `WTRC00003`, `WTRC00001`, `ETRC00001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-v2-post-multileg-payments` | `account-balances-balance-change-1` |
| `corporate-v2-post-multileg-payments` | `accounting-entry-creation-1` |
| `corporate-v2-post-multileg-payments` | `availables-change-available-1` |
| `SimulateInstallmentAdvancement` | `balance-installment-advancement-1` |
| `corporate-v2-post-multileg-payments` | `corporate-multi-leg-creation-1` |
| `corporate-v3-post-multileg-payments` | `corporate-multi-leg-creation-2` |
| `corporate-v2-post-multileg-payments` | `corporate-multi-leg-status-change-1` |
| `corporate-v3-post-multileg-payments` | `corporate-multi-leg-status-change-2` |
| `merchants-advancements` | `merchants-advancement-request-1` |
| `corporate-v2-post-multileg-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v3-post-multileg-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-multileg-payments` | `rules-evaluation-requested-1` |
| `corporate-v3-post-multileg-payments` | `rules-evaluation-requested-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/resources/api-endpoint-deprecation-and-removal-schedule.md`: updatedAt 2026-10-08T03:38:36.000Z.
- Links to `corporate-v2-post-multileg-payments`, which is marked `deprecated: true` in `api-specs/Banking_-_Transaction_banking.yaml`.
- Links to `corporate-v2-get-multileg-payment`, which is marked `deprecated: true` in `api-specs/Banking_-_Transaction_banking.yaml`.
- Links to `SearchTranscationMetaDataCount`, which is marked `deprecated: true` in `api-specs/Core_platform_-_Transactions.yaml`.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/resources/api-endpoint-deprecation-and-removal-schedule.md` | whole document | https://developers.pismo.io/pismo-docs/docs/api-endpoint-deprecation-and-removal-schedule | `a64c24d14bc086fc…` | 2026-10-08T03:38:36.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-API-revolving-credit-installment-management--installment-advancements` — API reference: Revolving credit - Installment management — Installment advancements
- `KU-API-revolving-credit-installment-management--simulations` — API reference: Revolving credit - Installment management — Simulations
- `KU-API-revolving-credit-statements--transaction-types` — API reference: Revolving credit - Statements — Transaction types
- `KU-API-seller-management-merchant-advance--merchant-advancement` — API reference: Seller management - Merchant advancements — Merchant advancement
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-LIFE-api-deprecation-strategy` — API lifecycle and deprecation strategy
