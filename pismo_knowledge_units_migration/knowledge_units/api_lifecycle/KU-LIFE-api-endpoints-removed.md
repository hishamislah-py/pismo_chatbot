---
ku_id: KU-LIFE-api-endpoints-removed
title: API endpoints removed
category: api_lifecycle
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/resources/api-endpoints-removed.md
  sha256: 56c7e4a8ba7d9b6f7eb4a3bd48037ef82b36e19f1cacc6d7584616782a710609
  url: https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed
  role: primary_guide
  updated_at: '2026-10-08T20:06:59.000Z'
operations: []
related_kus:
- KU-LIFE-marketplace-endpoint-removal
grouping_rationale: single source page
---

# API endpoints removed

**KU ID:** `KU-LIFE-api-endpoints-removed` · **Category:** API lifecycle · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/resources/api-endpoints-removed.md`:

> The following table lists API endpoints and when they were removed from Pismo's public documentation. This occurs after the endpoint has been removed from production.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/resources/api-endpoints-removed.md`: API endpoints removed

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/resources/api-endpoints-removed.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed · updatedAt: 2026-10-08T20:06:59.000Z

<!-- source:begin path=docs/resources/api-endpoints-removed.md part=0-end -->

# API endpoints removed

The following table lists API endpoints and when they were removed from Pismo's public documentation. This occurs after the endpoint has been removed from production.

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        API
      </th>

      <th style={{ textAlign: "left" }}>
        API section
      </th>

      <th style={{ textAlign: "left" }}>
        Endpoint name
      </th>

      <th style={{ textAlign: "left" }}>
        Endpoint URL
      </th>

      <th style={{ textAlign: "left" }}>
        Date removed
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Transaction banking
      </td>

      <td style={{ textAlign: "left" }}>
        Payments and Payment (Pismo account ID)
      </td>

      <td style={{ textAlign: "left" }}>
        Settle float payment

        Post float cash-in (Pismo account ID)
      </td>

      <td style={{ textAlign: "left" }}>
        POST /corporate/v1/corporate-float-cashin/:trackingId\
        POST /corporate/v1/corporate-float-cashin
      </td>

      <td style={{ textAlign: "left" }}>
        8/12/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Marketplace
      </td>

      <td style={{ textAlign: "left" }}>
        Seller Management - Marketplace
      </td>

      <td style={{ textAlign: "left" }}>
        List marketplace merchants

        List marketplace merchants

        Link merchant and marketplace

        Delete merchant and marketplace link

        Get marketplace

        Update marketplace

        Create marketplace

        <br />
      </td>

      <td style={{ textAlign: "left" }}>
        GET /marketplaces/v1/{'{marketplaceId}'}/        merchants

        GET /marketplace/v2/market        places/{'{marketplaceId'}/        merchants

        POST  /marketplaces/v1/{'{marketplaceId}'}/        merchants/{'{merchantId}'}

        DELETE /market        places/v1/{'{marketplaceId}'}/merchants/{'{merchantId}'}

        GET /marketplace/v1/        marketplaces/{'{marketplaceId}'}

        PUT /marketplace/v1/        marketplaces/{'{marketplaceId}'}

        POST /marketplace/v2/        marketplaces

        <br />
      </td>

      <td style={{ textAlign: "left" }}>
        10/6/26
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Cards
      </td>

      <td style={{ textAlign: "left" }}>
        Cards
      </td>

      <td style={{ textAlign: "left" }}>
        Create combo card
      </td>

      <td style={{ textAlign: "left" }}>
        POST /wallet/v1/relationship
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Seller Management
      </td>

      <td style={{ textAlign: "left" }}>
        Merchant transactions
      </td>

      <td style={{ textAlign: "left" }}>
        Create merchant transaction

        Create reversal transaction
      </td>

      <td style={{ textAlign: "left" }}>
        POST /merchants/v1/merchants/{'{merchantId}'}/transactions\
        POST /merchants/v1/merchants/{'{merchantId}'}/reversal-transactions
      </td>

      <td style={{ textAlign: "left" }}>
        7/24/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Banking
      </td>

      <td style={{ textAlign: "left" }}>
        Interest-bearing accounts
      </td>

      <td style={{ textAlign: "left" }}>
        Create maturity instruction override

        Update maturity instruction override

        Delete maturity instruction override

        Get maturity instruction override
      </td>

      <td style={{ textAlign: "left" }}>
        POST /v1/deposits/:productId/accounts/:accountId/maturity-instructions/overrides\
        PATCH /v1/deposits/:productId/accounts/:accountId/maturity-instructions/overrides DELETE /v1/deposits/:productId/accounts/:accountId/maturity-instructions/overrides\
        GET /v1/deposits/accounts/:accountId/maturity-instructions/overrides
      </td>

      <td style={{ textAlign: "left" }}>
        7/12/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Card issuing
      </td>

      <td style={{ textAlign: "left" }}>
        Statements
      </td>

      <td style={{ textAlign: "left" }}>
        List statements
      </td>

      <td style={{ textAlign: "left" }}>
        {'GET /statements/v2/accounts//{accountId/}/statements'}
      </td>

      <td style={{ textAlign: "left" }}>
        7/10/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Lending v1
      </td>

      <td style={{ textAlign: "left" }}>
        Create, simulate, manage loans
      </td>

      <td style={{ textAlign: "left" }}>
        Create loan product

        List loan products

        Get loan product

        Simulate loan booking

        Create charge plan

        Create loan booking

        Get loan details

        List loans

        Disburse loan

        Register repayment

        Register simulation for EFS

        Apply EFS simulation

        Simulate prepayment

        Apply prepayment simulation

        Create repayment hierarchy

        List repayment hierarchies

        Create penalty plan

        Get penalty plan

        Cancel loan

        Enable repayment hierarchy

        Disable repayment hierarchy

        Get repayment hierarchy

        Delete repayment hierarchy

        Get loan simulation

        Enable charge plan

        Disable charge plan

        List charge plan

        Get charge plan

        Delete charge plan

        Enable penalty plan

        Disable penalty plan

        List penalty plans

        Delete penalty plan

        Get program configuration

        Update program configuration
      </td>

      <td style={{ textAlign: "left" }}>
        POST /lending/v1/loan-products

        GET /lending/v1/loan-products

        <br />

        {'GET /lending/v1/loan-products/{productId}'}

        POST /lending/v1/simulations

        POST /lending/v1/charge-plans

        POST /lending/v1/loans

        <br />

        {'GET /lending/v1/loans/{loanId}'}

        GET /lending/v1/loans

        <br />

        {'POST /lending/v1/loans/{loanId}/disburse'}

        <br />

        {'POST /lending/v1/loans/{loanId}/repayment'}

        <br />

        {'POST /lending/v1/loans/{loanId}/early-settlement/simulate'}

        <br />

        {'POST /lending/v1/loans/{loanId}/early-settlement/{efsId}/register'}

        <br />

        {'POST /lending/v1/loans/{loanId}/prepayment/simulate'}

        <br />

        {'POST /lending/v1/loans/{loanId}/prepayment/{prepaymentId}/register'}

        <br />POST /lending/v1/repayment-hierarchies

        GET /lending/v1/repayment-hierarchies

        POST /lending/v1/penalty-plans

        GET /lending/v1/penalty-plans

        <br />

        {'DELETE /lending/v1/loans/{loanId}'}

        <br />

        {'PUT /lending/v1/repayment-hierarchies/{code}/enable'}

        <br />

        {'PUT /lending/v1/repayment-hierarchies/{code}/disable'}

        <br />

        {'GET /lending/v1/repayment-hierarchies/{code}'}

        <br />

        <br />

        {'DELETE /lending/v1/repayment-hierarchies/{code}'}

        <br />

        {'GET /lending/v1/simulations/{loanSimulationId}'}

        <br />

        {'PUT /lending/v1/charge-plans/{code}/enable'}

        <br />

        {'PUT /lending/v1/charge-plans/{code}/disable'}

        GET /lending/v1/charge-plans

        <br />

        {'GET /lending/v1/charge-plans/{code}'}

        <br />

        {'DELETE /lending/v1/charge-plans/{code}'}

        <br />

        {'PUT /lending/v1/penalty-plans/{code}/enable'}

        <br />

        {'PUT /lending/v1/penalty-plans/{code}/disable'}

        GET /lending/v1/penalty-plans

        <br />

        {'DELETE /lending/v1/penalty-plans/{code}'}

        <br />

        {'GET /lending/v1/program-configurations/{programId}'}

        <br />

        {'PUT /lending/v1/program-configurations/{programId}'}
      </td>

      <td style={{ textAlign: "left" }}>
        7/1/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        CRM
      </td>

      <td style={{ textAlign: "left" }}>
        Core platform
      </td>

      <td style={{ textAlign: "left" }}>
        All endpoints
      </td>

      <td style={{ textAlign: "left" }}>
        POST /crm/customers/\{customerId}/accounts/\{accountId} /crm/\*
      </td>

      <td style={{ textAlign: "left" }}>
        6/26/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Platform setup
      </td>

      <td style={{ textAlign: "left" }}>
        Programs
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        GET /v1/programs/\{program\_id}/parameters <br />GET /v1/programs\
        <br />GET /v1/programs/\{program\_id} <br />GET /v1/programs/\{program\_id}/duedates <br />GET /v2/programs/\{program\_id}/duedates
      </td>

      <td style={{ textAlign: "left" }}>
        6/1/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Platform setup
      </td>

      <td style={{ textAlign: "left" }}>
        Orgs
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        GET /orgs/v1/programs/\{program\_id}/parameters <br />GET /orgs/v1/programs\
        <br />GET /orgs/v1/programs/\{program\_id} <br />GET /orgs/v1/programs/\{program\_id}/duedates <br />GET /orgs/v2/programs/\{program\_id}/duedates
      </td>

      <td style={{ textAlign: "left" }}>
        6/1/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Cardsonfile
      </td>

      <td style={{ textAlign: "left" }}>
        Validation
      </td>

      <td style={{ textAlign: "left" }}>
        Get card validation amount

        <br />
      </td>

      <td style={{ textAlign: "left" }}>
        <br />GET /cardsonfile/v2/cardsonfile/cards/\{uuid}/validations/\{validationid}/amount
      </td>

      <td style={{ textAlign: "left" }}>
        5/12/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payment configurations
      </td>

      <td style={{ textAlign: "left" }}>
        Core platform
      </td>

      <td style={{ textAlign: "left" }}>
        Create processing code

        List processing codes

        Update processing code
      </td>

      <td style={{ textAlign: "left" }}>
        POST /payments-config/v1/processing-codes

        GET /payments-config/v1/processing-codes

        PATCH /payments-config/v1/processing-codes
      </td>

      <td style={{ textAlign: "left" }}>
        5/6/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Card issuing
      </td>

      <td style={{ textAlign: "left" }}>
        Statements
      </td>

      <td style={{ textAlign: "left" }}>
        Get account total due
      </td>

      <td style={{ textAlign: "left" }}>
        {'GET /statements-v2/v2/accounts/{accountId}/total-due'}
      </td>

      <td style={{ textAlign: "left" }}>
        5/4/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Revolving
      </td>

      <td style={{ textAlign: "left" }}>
        Statements
      </td>

      <td style={{ textAlign: "left" }}>
        Get program future calendars
      </td>

      <td style={{ textAlign: "left" }}>
        GET /statements-v2/v1/calendars
      </td>

      <td style={{ textAlign: "left" }}>
        5/4/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Seller Management - Marketplace
      </td>

      <td style={{ textAlign: "left" }}>
        Marketplace
      </td>

      <td style={{ textAlign: "left" }}>
        Create merchants relationships

        Remove merchant relationship with all branches

        Disable the merchant-branch relationship
      </td>

      <td style={{ textAlign: "left" }}>
        POST marketplaces/\{marketplaceId}/merchants/\{merchantId}/branches

        DELETE marketplaces/\{marketplaceId}/merchants/\{merchantId}/branches

        DELETE\
        marketplaces/\{marketplaceId}/merchants/\{merchantId}/branches/\{merchantBranchId}
      </td>

      <td style={{ textAlign: "left" }}>
        2/11/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Banking
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction banking
      </td>

      <td style={{ textAlign: "left" }}>
        Get AES key

        Create operation block

        List operation blocks

        Revoke operation block
      </td>

      <td style={{ textAlign: "left" }}>
        GET  /corporate/v1/bulk-payments/encryption-keys/\{bulkId}

        POST /corporate/v1/operations-blocks

        GET /corporate/v1/operations-blocks

        DELETE /corporate/v1/operations-blocks/\{operationsBlockId}
      </td>

      <td style={{ textAlign: "left" }}>
        2/20/2026
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Banking
      </td>

      <td style={{ textAlign: "left" }}>
        Bank accounts
      </td>

      <td style={{ textAlign: "left" }}>
        Create Transfer (v1)

        Cancel Transfer (v1)

        Change Account Status (v1)

        Account Cancellation (v1)

        Create Payment Request (v1)

        Create Adjustment (Back Office) (v1)

        Create Transfer (Back Office) (v1)

        Change Account Status (Back Office) (v1)
      </td>

      <td style={{ textAlign: "left" }}>
        POST /bankaccounts-sec/v1/transfers

        POST /bankaccounts-sec/v1/transfers/\{tracking-id}/cancel

        POST /bankaccounts-sec/v1/account-status-change

        POST /bankaccounts-sec/v1/account-cancellation

        POST /bankaccounts-sec/v1/payment-requests

        POST /v1/roles-approve/adjustments

        POST /v1/roles-approve/transfers

        POST /v1/roles-approve/account-status-change
      </td>

      <td style={{ textAlign: "left" }}>
        1/15/26
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Core platform - Adjustments
      </td>

      <td style={{ textAlign: "left" }}>
        Adjustments
      </td>

      <td style={{ textAlign: "left" }}>
        Create adjustment

        Get reversal types

        Get adjustment types

        Get adjustment
      </td>

      <td style={{ textAlign: "left" }}>
        POST adjustments/v1/adjustments

        GET adjustments/v1/reversals-types

        GET adjustments/v1/types

        GET adjustments/v1/adjustments/\{adjustmentId}
      </td>

      <td style={{ textAlign: "left" }}>
        11/12/2025
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Core platform - Migrations
      </td>

      <td style={{ textAlign: "left" }}>
        Accounts
      </td>

      <td style={{ textAlign: "left" }}>
        Migrate accounts
      </td>

      <td style={{ textAlign: "left" }}>
        POST migrations/v1/migrations/accounts
      </td>

      <td style={{ textAlign: "left" }}>
        10/17/2025
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Seller management - Merchants
      </td>

      <td style={{ textAlign: "left" }}>
        Merchants
      </td>

      <td style={{ textAlign: "left" }}>
        List active merchant states

        List active merchant cities

        List active merchant neighborhoods
      </td>

      <td style={{ textAlign: "left" }}>
        GET merchants/v1/locations/states

        GET merchants/v1/locations/cities

        GET merchants/v1/locations/neighborhoods
      </td>

      <td style={{ textAlign: "left" }}>
        10/8/2025
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Accounts
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        GET /v2/accounts/\{accountld}/statements <br />GET /v1/accounts/\{accountld}/statements <br />POST /v2/customers/document-number\
        <br />GET /v1/customers/\{customerId}/authorizations <br />PUT /v1/accounts/\{accountld}/duedate <br />GET /v1/accounts/\{accountld}/authorizations
      </td>

      <td style={{ textAlign: "left" }}>
        9/2025
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Card issuing - Disputes
      </td>

      <td style={{ textAlign: "left" }}>
        ELO fraud
      </td>

      <td style={{ textAlign: "left" }}>
        Create authorization fraud report

        List authorization fraud reports

        Count authorization fraud reports
      </td>

      <td style={{ textAlign: "left" }}>
        POST v1/authorization-fraud-report

        GET v1/authorization-fraud-report

        GET /v1/authorization-fraud-report/count
      </td>

      <td style={{ textAlign: "left" }}>
        8/18/2025
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Platform setup - Programs
      </td>

      <td style={{ textAlign: "left" }}>
        Programs
      </td>

      <td style={{ textAlign: "left" }}>
        List due dates for all statements
      </td>

      <td style={{ textAlign: "left" }}>
        GET orgs/v2/programs/\{id}/duedates
      </td>

      <td style={{ textAlign: "left" }}>
        7/1/2025
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Data and reporting - Banking reports
      </td>

      <td style={{ textAlign: "left" }}>
        Reports  Transaction types
      </td>

      <td style={{ textAlign: "left" }}>
        Get account annual fees report

        Get account income report

        Create transaction types

        List transaction types
      </td>

      <td style={{ textAlign: "left" }}>
        GET /banking-reports/v1/accounts/\{accountId}/fees

        GET /banking-reports/v1/accounts/\{accountId}/incomes

        POST /banking-reports/v1/transaction-types

        GET /banking-reports/v1/transaction-types
      </td>

      <td style={{ textAlign: "left" }}>
        6/30/2025
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## Structured removal register (migration extract)

Each row of the published table, extracted from the MDX source. Cell text is shown with line breaks inside a cell replaced by ` ⏎ `; no path was repaired. “In current specs?” checks each `METHOD path` in the URL cell against current operations (server base path + path, placeholders normalised).

| # | API | API section | Endpoint names | Endpoint URLs (raw) | Date removed (raw) | In current specs? |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Transaction banking | Payments and Payment (Pismo account ID) | Settle float payment; Post float cash-in (Pismo account ID) | POST /corporate/v1/corporate-float-cashin/:trackingId\\ ⏎ POST /corporate/v1/corporate-float-cashin | `8/12/2026` | no match |
| 2 | Marketplace | Seller Management - Marketplace | List marketplace merchants; List marketplace merchants; Link merchant and marketplace; Delete merchant and marketplace link; Get marketplace; Update marketplace; Create marketplace | GET /marketplaces/v1/{'{marketplaceId}'}/ ⏎ merchants ⏎ GET /marketplace/v2/market ⏎ places/{'{marketplaceId'}/ ⏎ merchants ⏎ POST  /marketplaces/v1/{'{marketplaceId}'}/ ⏎ merchants/{'{merchantId}'} ⏎ DELETE /market ⏎ places/v1/{'{marketplaceId}'}/merchants/{'{merchantId}'} ⏎ GET /marketplace/v1/ ⏎ marketplaces/{'{marketplaceId}'} ⏎ PUT /marketplace/v1/ ⏎ marketplaces/{'{marketplaceId}'} ⏎ POST /marketplace/v2/ ⏎ marketplaces ⏎ <br /> | `10/6/26` | no match |
| 3 | Cards | Cards | Create combo card | POST /wallet/v1/relationship | `(blank)` | no match |
| 4 | Seller Management | Merchant transactions | Create merchant transaction; Create reversal transaction | POST /merchants/v1/merchants/{'{merchantId}'}/transactions\\ ⏎ POST /merchants/v1/merchants/{'{merchantId}'}/reversal-transactions | `7/24/2026` | no match |
| 5 | Banking | Interest-bearing accounts | Create maturity instruction override; Update maturity instruction override; Delete maturity instruction override; Get maturity instruction override | POST /v1/deposits/:productId/accounts/:accountId/maturity-instructions/overrides\\ ⏎ PATCH /v1/deposits/:productId/accounts/:accountId/maturity-instructions/overrides DELETE /v1/deposits/:productId/accounts/:accountId/maturity-instructions/overrides\\ ⏎ GET /v1/deposits/accounts/:accountId/maturity-instructions/overrides | `7/12/2026` | no match |
| 6 | Card issuing | Statements | List statements | {'GET /statements/v2/accounts//{accountId/}/statements'} | `7/10/2026` | no match |
| 7 | Lending v1 | Create, simulate, manage loans | Create loan product; List loan products; Get loan product; Simulate loan booking; Create charge plan; Create loan booking; Get loan details; List loans; Disburse loan; Register repayment; Register simulation for EFS; Apply EFS simulation; Simulate prepayment; Apply prepayment simulation; Create repayment hierarchy; List repayment hierarchies; Create penalty plan; Get penalty plan; Cancel loan; Enable repayment hierarchy; Disable repayment hierarchy; Get repayment hierarchy; Delete repayment hierarchy; Get loan simulation; Enable charge plan; Disable charge plan; List charge plan; Get charge plan; Delete charge plan; Enable penalty plan; Disable penalty plan; List penalty plans; Delete penalty plan; Get program configuration; Update program configuration | POST /lending/v1/loan-products ⏎ GET /lending/v1/loan-products ⏎ <br /> ⏎ {'GET /lending/v1/loan-products/{productId}'} ⏎ POST /lending/v1/simulations ⏎ POST /lending/v1/charge-plans ⏎ POST /lending/v1/loans ⏎ <br /> ⏎ {'GET /lending/v1/loans/{loanId}'} ⏎ GET /lending/v1/loans ⏎ <br /> ⏎ {'POST /lending/v1/loans/{loanId}/disburse'} ⏎ <br /> ⏎ {'POST /lending/v1/loans/{loanId}/repayment'} ⏎ <br /> ⏎ {'POST /lending/v1/loans/{loanId}/early-settlement/simulate'} ⏎ <br /> ⏎ {'POST /lending/v1/loans/{loanId}/early-settlement/{efsId}/register'} ⏎ <br /> ⏎ {'POST /lending/v1/loans/{loanId}/prepayment/simulate'} ⏎ <br /> ⏎ {'POST /lending/v1/loans/{loanId}/prepayment/{prepaymentId}/register'} ⏎ <br />POST /lending/v1/repayment-hierarchies ⏎ GET /lending/v1/repayment-hierarchies ⏎ POST /lending/v1/penalty-plans ⏎ GET /lending/v1/penalty-plans ⏎ <br /> ⏎ {'DELETE /lending/v1/loans/{loanId}'} ⏎ <br /> ⏎ {'PUT /lending/v1/repayment-hierarchies/{code}/enable'} ⏎ <br /> ⏎ {'PUT /lending/v1/repayment-hierarchies/{code}/disable'} ⏎ <br /> ⏎ {'GET /lending/v1/repayment-hierarchies/{code}'} ⏎ <br /> ⏎ <br /> ⏎ {'DELETE /lending/v1/repayment-hierarchies/{code}'} ⏎ <br /> ⏎ {'GET /lending/v1/simulations/{loanSimulationId}'} ⏎ <br /> ⏎ {'PUT /lending/v1/charge-plans/{code}/enable'} ⏎ <br /> ⏎ {'PUT /lending/v1/charge-plans/{code}/disable'} ⏎ GET /lending/v1/charge-plans ⏎ <br /> ⏎ {'GET /lending/v1/charge-plans/{code}'} ⏎ <br /> ⏎ {'DELETE /lending/v1/charge-plans/{code}'} ⏎ <br /> ⏎ {'PUT /lending/v1/penalty-plans/{code}/enable'} ⏎ <br /> ⏎ {'PUT /lending/v1/penalty-plans/{code}/disable'} ⏎ GET /lending/v1/penalty-plans ⏎ <br /> ⏎ {'DELETE /lending/v1/penalty-plans/{code}'} ⏎ <br /> ⏎ {'GET /lending/v1/program-configurations/{programId}'} ⏎ <br /> ⏎ {'PUT /lending/v1/program-configurations/{programId}'} | `7/1/2026` | no match |
| 8 | CRM | Core platform | All endpoints | POST /crm/customers/\\{customerId}/accounts/\\{accountId} /crm/\\* | `6/26/2026` | no match |
| 9 | Platform setup | Programs |  | GET /v1/programs/\\{program\\_id}/parameters <br />GET /v1/programs\\ ⏎ <br />GET /v1/programs/\\{program\\_id} <br />GET /v1/programs/\\{program\\_id}/duedates <br />GET /v2/programs/\\{program\\_id}/duedates | `6/1/2026` | no match |
| 10 | Platform setup | Orgs |  | GET /orgs/v1/programs/\\{program\\_id}/parameters <br />GET /orgs/v1/programs\\ ⏎ <br />GET /orgs/v1/programs/\\{program\\_id} <br />GET /orgs/v1/programs/\\{program\\_id}/duedates <br />GET /orgs/v2/programs/\\{program\\_id}/duedates | `6/1/2026` | no match |
| 11 | Cardsonfile | Validation | Get card validation amount | <br />GET /cardsonfile/v2/cardsonfile/cards/\\{uuid}/validations/\\{validationid}/amount | `5/12/2026` | yes: `get-a-specific-validation-amount-for-a-given-card` in `api-specs/Card_issuing_-_Cards_on_file.yaml` |
| 12 | Payment configurations | Core platform | Create processing code; List processing codes; Update processing code | POST /payments-config/v1/processing-codes ⏎ GET /payments-config/v1/processing-codes ⏎ PATCH /payments-config/v1/processing-codes | `5/6/2026` | no match |
| 13 | Card issuing | Statements | Get account total due | {'GET /statements-v2/v2/accounts/{accountId}/total-due'} | `5/4/2026` | no match |
| 14 | Revolving | Statements | Get program future calendars | GET /statements-v2/v1/calendars | `5/4/2026` | no match |
| 15 | Seller Management - Marketplace | Marketplace | Create merchants relationships; Remove merchant relationship with all branches; Disable the merchant-branch relationship | POST marketplaces/\\{marketplaceId}/merchants/\\{merchantId}/branches ⏎ DELETE marketplaces/\\{marketplaceId}/merchants/\\{merchantId}/branches ⏎ DELETE\\ ⏎ marketplaces/\\{marketplaceId}/merchants/\\{merchantId}/branches/\\{merchantBranchId} | `2/11/2026` | no match |
| 16 | Banking | Transaction banking | Get AES key; Create operation block; List operation blocks; Revoke operation block | GET  /corporate/v1/bulk-payments/encryption-keys/\\{bulkId} ⏎ POST /corporate/v1/operations-blocks ⏎ GET /corporate/v1/operations-blocks ⏎ DELETE /corporate/v1/operations-blocks/\\{operationsBlockId} | `2/20/2026` | no match |
| 17 | Banking | Bank accounts | Create Transfer (v1); Cancel Transfer (v1); Change Account Status (v1); Account Cancellation (v1); Create Payment Request (v1); Create Adjustment (Back Office) (v1); Create Transfer (Back Office) (v1); Change Account Status (Back Office) (v1) | POST /bankaccounts-sec/v1/transfers ⏎ POST /bankaccounts-sec/v1/transfers/\\{tracking-id}/cancel ⏎ POST /bankaccounts-sec/v1/account-status-change ⏎ POST /bankaccounts-sec/v1/account-cancellation ⏎ POST /bankaccounts-sec/v1/payment-requests ⏎ POST /v1/roles-approve/adjustments ⏎ POST /v1/roles-approve/transfers ⏎ POST /v1/roles-approve/account-status-change | `1/15/26` | no match |
| 18 | Core platform - Adjustments | Adjustments | Create adjustment; Get reversal types; Get adjustment types; Get adjustment | POST adjustments/v1/adjustments ⏎ GET adjustments/v1/reversals-types ⏎ GET adjustments/v1/types ⏎ GET adjustments/v1/adjustments/\\{adjustmentId} | `11/12/2025` | no match |
| 19 | Core platform - Migrations | Accounts | Migrate accounts | POST migrations/v1/migrations/accounts | `10/17/2025` | no match |
| 20 | Seller management - Merchants | Merchants | List active merchant states; List active merchant cities; List active merchant neighborhoods | GET merchants/v1/locations/states ⏎ GET merchants/v1/locations/cities ⏎ GET merchants/v1/locations/neighborhoods | `10/8/2025` | no match |
| 21 | Accounts |  |  | GET /v2/accounts/\\{accountld}/statements <br />GET /v1/accounts/\\{accountld}/statements <br />POST /v2/customers/document-number\\ ⏎ <br />GET /v1/customers/\\{customerId}/authorizations <br />PUT /v1/accounts/\\{accountld}/duedate <br />GET /v1/accounts/\\{accountld}/authorizations | `9/2025` | no match |
| 22 | Card issuing - Disputes | ELO fraud | Create authorization fraud report; List authorization fraud reports; Count authorization fraud reports | POST v1/authorization-fraud-report ⏎ GET v1/authorization-fraud-report ⏎ GET /v1/authorization-fraud-report/count | `8/18/2025` | no match |
| 23 | Platform setup - Programs | Programs | List due dates for all statements | GET orgs/v2/programs/\\{id}/duedates | `7/1/2025` | no match |
| 24 | Data and reporting - Banking reports | Reports Transaction types | Get account annual fees report; Get account income report; Create transaction types; List transaction types | GET /banking-reports/v1/accounts/\\{accountId}/fees ⏎ GET /banking-reports/v1/accounts/\\{accountId}/incomes ⏎ POST /banking-reports/v1/transaction-types ⏎ GET /banking-reports/v1/transaction-types | `6/30/2025` | no match |

## Lifecycle status

- `docs/resources/api-endpoints-removed.md`: updatedAt 2026-10-08T20:06:59.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/resources/api-endpoints-removed.md` | whole document | https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed | `56c7e4a8ba7d9b6f…` | 2026-10-08T20:06:59.000Z |

## Related knowledge units

- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
