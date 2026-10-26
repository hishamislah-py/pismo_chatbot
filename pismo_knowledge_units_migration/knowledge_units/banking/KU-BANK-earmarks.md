---
ku_id: KU-BANK-earmarks
title: Earmarks
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/earmarks.md
  sha256: 8b907acf2e923d2217c3323fd401685438c50dec711effb8068c1be9c1b999af
  url: https://developers.pismo.io/pismo-docs/docs/earmarks
  role: primary_guide
  updated_at: '2026-05-27T21:46:12.000Z'
operations:
- find-corporate-earmark
- get-corporate-earmarks
- patch-corporate-v2-earmarks-earmarkid
- post-account
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-passport-v1-oauth2-token
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-platform-authentication--authentication
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-PAY-hold-funds
grouping_rationale: single source page
---

# Earmarks

**KU ID:** `KU-BANK-earmarks` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/earmarks.md`:

> The **earmark** feature enables you to set aside funds for some purpose. An account holder can create an earmark to schedule a cash-out (usually a payment), holding needed funds in reserve until a scheduled date and time. At the specified time, an automatic process releases the earmarked funds and settles the cash-out.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/earmarks.md`: Earmarks; Examples of earmark actions; Create earmark; Modify earmark; Cancel earmark; Accessing earmark information; List earmarks; Get an earmark; Custom processing codes

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/earmarks.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/earmarks · updatedAt: 2026-05-27T21:46:12.000Z

<!-- source:begin path=docs/core-banking/earmarks.md part=0-end -->

# Earmarks

The **earmark** feature enables you to set aside funds for some purpose. An account holder can create an earmark to schedule a cash-out (usually a payment), holding needed funds in reserve until a scheduled date and time. At the specified time, an automatic process releases the earmarked funds and settles the cash-out.

Organizations can earmark funds for any purpose. Setting no release date or time sets funds aside in perpetuity. An organization might want to do this, for example, to keep some money in an account in reserve for emergencies.

Earmarks leverage the [Hold funds](https://developers.pismo.io/pismo-docs/docs/hold-funds) feature of the Pismo core platform, but for the specific purpose of corporate banking. To get information about current and historical earmarks, use [List earmarks](https://developers.pismo.io/pismo-docs/reference/get-corporate-earmarks). To get information about a specific earmark, use [Get earmark](https://developers.pismo.io/pismo-docs/reference/find-corporate-earmark) and provide the earmark\_id.

The earmarks feature offers three different actions:

* [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) holds needed funds in reserve until a specified date and time for release. The amount to earmark must be available in the client account.
* [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid) changes the value of an earmark, increasing or decreasing the value, and the release date or time. The updated amount must be available in the client account. Decreasing the earmark amount reduces the held funds, making them available for other purposes.
* [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel) removes an earmark associated with an account. This releases held funds and invalidates the scheduled earmark.

# Examples of earmark actions

## Create earmark

You can set aside a certain amount of funds using the [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint. Once an earmark is created, the funds are set aside for release at a specified date and time, or if a release date is not specified, in perpetuity. This endpoint requires an account-specific access token, acquired by calling the [Get OpenID access token](https://developers.pismo.io/pismo-docs/reference/post-passport-v1-oauth2-token) endpoint with an external account ID.

Find below a sample of a request to create an earmark.

`POST /corporate/v1/earmarks`

```json
{
    "earmark_id": "604cd837-8bfc-4423-b785-36448f3563b7",
    "account_id": 250318,
    "external_account_id": "61a05298-7579-4ff8-ac32-3f5eeef632e7",
    "release_datetime": "2023-06-20T16:09:13.121Z",
    "amount": 10,
    "balance": 10,
    "description": "string",
    "internal_operations": [
        {
            "type": "HOLD_FUNDS",
            "tracking_id": "83b31d6e-b714-cd00-7b1e-87f1583faa85",
            "processing_code": "219248",
            "amount": 10,
            "created_at": "2023-06-19T16:09:13.291946274Z"
        }
    ]
}

```

There are several things unique to earmarks to note here.

* **earmark\_id** 	Every earmark has an earmark ID that you can use to view, update, or cancel it. You can specify the earmark ID by populating the `earmark_id` field when you create the earmark. If you don't supply a value for this field, the Pismo platform generates one automatically and returns it in the request result.
* **external\_account\_id**	The required ‘external\_account\_id’ is generated when you use the [Create transaction banking account](https://developers.pismo.io/pismo-docs/reference/post-account) endpoint to create a corporate account. The code below shows the result of running this endpoint, showing both the standard Pismo account ID and the external account ID.

```json
{
    "account_id": 250318,
    "external_account_id": "61a05298-7579-4ff8-ac32-3f5eeef632e7",
    "program_id": 16
}
```

* **internal\_operations**	The internal operations fields are generated or altered during the earmark creation/update/cancel processes. These fields enable Pismo to hold and release funds from and to the proper accounts. The internal operations fields enable interaction between the corporate banking earmarking endpoints and the Pismo core platform Payments API Hold funds endpoints.

Note the “type” above shows “HOLD FUNDS,” which indicates that this earmark has held funds currently. Other options for “type” include these:

`"type": "INCREASE",
"type": "DECREASE",
"type": "RELEASE_FUNDS",`

As the names indicate, “INCREASE” means the earmark has raised the amount of funds held. “DECREASE” means the opposite, that the earmark has lowered the amount of funds held. ‘RELEASE\_FUNDS” means that the earmark has reached its date and time release point and transferred the funds appropriately.

## Modify earmark

The [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid) endpoint enables you to modify an existing earmark. The following sample code shows the result of updating an earmark’s amount from $10 to $20. Note that the `internal_operations` object shows exactly how the earmark was affected by the request.

`PATCH /corporate/v1/earmarks/{earmarkId}`

```json
{
    "earmark_id": "e894e8d2-c788-44ad-9440-7320e9b7ee45",
    "account_id": 250318,
    "external_account_id": "61a05298-7579-4ff8-ac32-3f5eeef632e7",
    "release_datetime": "2023-06-02T20:24:43.786Z",
    "amount": 20,
    "balance": 20,
    "description": "string",
    "internal_operations": [
        {
            "type": "INCREASE",
            "tracking_id": "e8202372-a92b-4ae4-a8a4-e722fd0d3367",
            "processing_code": "219248",
            "amount": 10,
            "created_at": "2023-06-01T21:11:02.002501187Z"
        },
        {
            "type": "HOLD_FUNDS",
            "tracking_id": "9b61daac-6125-e25e-8b66-4778d03be920",
            "processing_code": "219248",
            "amount": 10,
            "created_at": "2023-06-01T20:24:43.979438613Z"
        }
    ]
}

```

Leaving the `release_datetime` field blank in the Request body makes no change to the currently active earmark release date and time.

Pismo earmarks enable organizations to react to changing circumstances fluidly and rapidly. This helps you address those scenarios where you ‘thought’ you had the right amount of funds set aside to handle a payment but added expenses require a change.

When you initially create an earmark, you can choose not to insert a release date and time. This sets the earmarked funds aside indefinitely, until you choose to release them. Use the [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid) endpoint to change an indefinite release date and time to a definite one.

## Cancel earmark

If an earmark becomes irrelevant or funds set aside need to be accessed for more pressing needs, you can remove the earmark using [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel). You need the earmarkId, but nothing else. Running the endpoint successfully generates a 204 No Content message, showing no remaining earmark for that earmarkId.

The following sample code shows the result of canceling a  $20 earmark. Note that the `balance` has changed from 20 to 0.

`DELETE /corporate/v1/earmarks/{earmarkId}`

```json
{
    "earmark_id": "e894e8d2-c788-44ad-9440-7320e9b7ee45",
    "account_id": 250318,
    "external_account_id": "61a05298-7579-4ff8-ac32-3f5eeef632e7",
    "release_datetime": "2023-06-02T20:24:43.786Z",
    "amount": 20,
    "balance": 0,
    "description": "Client X",
    "internal_operations": [
        {
            "type": "RELEASE_FUNDS",
            "tracking_id": "b065adcc-6af4-c513-e76c-47088265dc8c",
            "processing_code": "219251",
            "amount": 20,
            "created_at": "2023-06-01T21:36:25.817205064Z"
        },
        {
            "type": "HOLD_FUNDS",
            "tracking_id": "9b61daac-6125-e25e-8b66-4778d03be920",
            "processing_code": "219248",
            "amount": 10,
            "created_at": "2023-06-01T20:24:43.979438613Z"
        },
        {
            "type": "INCREASE",
            "tracking_id": "e8202372-a92b-4ae4-a8a4-e722fd0d3367",
            "processing_code": "219248",
            "amount": 10,
            "created_at": "2023-06-01T21:11:02.002501187Z"
        }
    ]
}
```

# Accessing earmark information

Two endpoints enable you to review earmarks:

* List earmarks
* Get earmark

## List earmarks

[List earmarks](https://developers.pismo.io/pismo-docs/reference/get-corporate-earmarks) retrieves all the earmarks for an organization, including those that have already been executed and deleted.

The following is an example of the information returned by the List earmarks endpoint.

`GET /corporate/v1/earmarks`

```json
{
    "earmarks": [
        {
            "earmark_id": "8b9e91d3-fd40-44e0-8c04-751a74c3b946",
            "account_id": 250318,
            "external_account_id": "61a05298-7579-4ff8-ac32-3f5eeef632e7",
            "release_datetime": "2023-06-02T14:20:25.106Z",
            "amount": 10,
            "balance": 0,
            "description": "Client X",
            "internal_operations": [
                {
                    "type": "HOLD_FUNDS",
                    "tracking_id": "474b7d5a-9835-e577-058c-9cc2125bd185",
                    "processing_code": "219248",
                    "amount": 10,
                    "created_at": "2023-06-01T16:37:40.463488702Z"
                },
                {
                    "type": "RELEASE_FUNDS",
                    "tracking_id": "e515f589-bf38-9c5c-70f2-8f4f7f03c9cd",
                    "processing_code": "219251",
                    "amount": 10,
                    "created_at": "2023-06-01T16:38:15.583657716Z"
                }
            ]
        },
        {
            "earmark_id": "e894e8d2-c788-44ad-9440-7320e9b7ee45",
            "account_id": 250318,
            "external_account_id": "61a05298-7579-4ff8-ac32-3f5eeef632e7",
            "release_datetime": "2023-06-02T14:20:25.106Z",
            "amount": 10,
            "balance": 10,
            "description": "Client X",
            "internal_operations": [
                {
                    "type": "HOLD_FUNDS",
                    "tracking_id": "9b61daac-6125-e25e-8b66-4778d03be920",
                    "processing_code": "219248",
                    "amount": 10,
                    "created_at": "2023-06-01T20:24:43.979438613Z"
                }
            ]
        },
        {
            "earmark_id": "f9784be5-addf-4ef0-ae4b-2322118b40e6",
            "account_id": 250318,
            "external_account_id": "61a05298-7579-4ff8-ac32-3f5eeef632e7",
            "release_datetime": "2023-06-02T14:20:25.106Z",
            "amount": 10,
            "balance": 0,
            "description": "Client X",
            "internal_operations": [
                {
                    "type": "HOLD_FUNDS",
                    "tracking_id": "019341de-5c73-04c3-1cae-8229228badec",
                    "processing_code": "219248",
                    "amount": 10,
                    "created_at": "2023-06-01T14:20:25.229144451Z"
                },
                {
                    "type": "RELEASE_FUNDS",
                    "tracking_id": "860a9fa2-0566-e7fa-5c6a-a8203f8a7526",
                    "processing_code": "219251",
                    "amount": 10,
                    "created_at": "2023-06-01T16:36:29.558453818Z"
                }
            ]
        }
    ],
    "pagination": {
        "limit": 10,
        "cursor": ""
    }
}
```

## Get an earmark

The [Get earmark](https://developers.pismo.io/pismo-docs/reference/find-corporate-earmark) endpoint enables you to access information about an earmark based on the earmark ID. The following shows the output of [Get earmark](https://developers.pismo.io/pismo-docs/reference/find-corporate-earmark) for the account earmarked in the “Create earmark” section previously in this document.

`GET /corporate/v1/earmarks{earmarkId}`

```json
{
    "earmark_id": "8b9e91d3-fd40-44e0-8c04-751a74c3b946",
    "account_id": 250318,
    "external_account_id": "61a05298-7579-4ff8-ac32-3f5eeef632e7",
    "release_datetime": "2023-06-02T16:37:40.372Z",
    "amount": 10,
    "balance": 10,
    "description": "string",
    "internal_operations": [
        {
            "type": "HOLD_FUNDS",
            "tracking_id": "474b7d5a-9835-e577-058c-9cc2125bd185",
            "processing_code": "219248",
            "amount": 10,
            "created_at": "2023-06-01T16:37:40.463488702Z"
        },
        {
            "type": "RELEASE_FUNDS",
            "tracking_id": "e515f589-bf38-9c5c-70f2-8f4f7f03c9cd",
            "processing_code": "219251",
            "amount": 10,
            "created_at": "2023-06-01T16:38:15.583657716Z"
        }
    ]
}
```

# Custom processing codes

To use custom processing codes for earmark, you must contact Pismo to create the necessary configurations for all environments to ensure proper functionality. Failure to do so can result in the following error:

```json
{ 
    "message": "Invalid debit earmark processing code",
    "code":"WPMT0021"
}
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /corporate/v1/earmarks` | `get-corporate-earmarks` | List earmarks | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `GET /corporate/v1/earmarks/{earmarkId}` | `find-corporate-earmark` | Get earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks` | `post-corporate-v2-earmarks` | Create earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/earmarks/{earmarkId}` | `patch-corporate-v2-earmarks-earmarkid` | Update earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` | `post-corporate-v2-earmarks-earmarkid-cancel` | Cancel earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /v1/oauth2/token` | `post-passport-v1-oauth2-token` | Get OpenID access token | `api-specs/Platform_authentication.yaml` | no | KU-API-platform-authentication--authentication |
| `POST /corporate/v1/corporate-accounts` | `post-account` | Create transaction banking account | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |

### Operation essentials

- **`GET /corporate/v1/earmarks`** (`get-corporate-earmarks`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 403, 500; error codes in examples `WCMN0005`, `ECMN9999`; events none listed.
- **`GET /corporate/v1/earmarks/{earmarkId}`** (`find-corporate-earmark`): security `BearerAuth`; required parameters `earmarkId` (path); required body fields none declared; response statuses 200, 404, 500; error codes in examples `ECMN9999`; events none listed.
- **`POST /corporate/v2/earmarks`** (`post-corporate-v2-earmarks`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `internal_operation`; response statuses 201, 400, 401, 403, 409, 423, 500; error codes in examples `WOBK0007`, `WEAM0014`, `WEAM0015`, `WEAM0005`, `WEAM0006`, `WEAM0017`, `WEAM0019`, `WEAM0026`, `WEAM0036`, `WEAM0037`, `WEAM0039`, `WEAM0040`, `WEAM0047`, `WEAM0042`, `WEAM0043`, `WEAM0044`, `WEAM0045`, `WEAM0046`, `WEAM0016`, `WEAM0018`, `WEAM0009`, `WEAM0020`, `WEAM0023`, `WEAM0024`, `WEAM0001`, `WEAM0025`, `WEAM0034`, `WEAM0033`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-earmark-1`, `platform-authorization-platform-authorization-1`, `transaction-creation-1`.
- **`PATCH /corporate/v2/earmarks/{earmarkId}`** (`patch-corporate-v2-earmarks-earmarkid`): security `BearerAuth`; required parameters `earmarkId` (path); required body fields `internal_operation`; response statuses 200, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WEAM0014`, `WEAM0015`, `WEAM0016`, `WEAM0017`, `WEAM0018`, `WEAM0019`, `WEAM0026`, `WEAM0027`, `WEAM0030`, `WEAM0031`, `WEAM0036`, `WEAM0038`, `WEAM0039`, `WEAM0040`, `WEAM0047`, `WEAM0041`, `WEAM0042`, `WEAM0043`, `WEAM0044`, `WEAM0045`, `WEAM0046`, `WEAM0023`, `WEAM0024`, `WEAM0025`, `WEAM0034`, `WEAM0049`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-earmark-1`, `platform-authorization-platform-authorization-1`, `transaction-creation-1`.
- **`POST /corporate/v2/earmarks/{earmarkId}/cancel`** (`post-corporate-v2-earmarks-earmarkid-cancel`): security `BearerAuth`; required parameters `earmarkId` (path); required body fields `internal_operation`; response statuses 200, 400, 401, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WEAM0014`, `WEAM0015`, `WEAM0008`, `WEAM0017`, `WEAM0018`, `WEAM0019`, `WEAM0022`, `WCAC0012`, `WEAM0036`, `WEAM0039`, `WEAM0040`, `WEAM0047`, `WEAM0041`, `WEAM0042`, `WEAM0043`, `WEAM0044`, `WEAM0045`, `WEAM0046`, `WEAM0024`, `WEAM0007`, `WEAM0025`, `WEAM0034`, `WEAM0049`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-earmark-1`, `platform-authorization-platform-authorization-1`, `transaction-creation-1`.
- **`POST /v1/oauth2/token`** (`post-passport-v1-oauth2-token`): security not declared; required parameters none declared; required body fields `token`; response statuses 201, 401, 500; error codes in examples none; events none listed.
- **`POST /corporate/v1/corporate-accounts`** (`post-account`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `program_id`, `applicant`, `external_account_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WCAC0013`, `WCAC0005`, `WCAC0006`, `WCAC0004`, `WCAC0016`, `WCAC0009`, `WDIV0002`, `WCAC0011`, `WCAC0014`, `ECMN9999`; events `corporate-corporate-account-creation-1`, `onboarding-succeeded-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-corporate-v2-earmarks-earmarkid` | `account-balances-balance-change-1` |
| `post-corporate-v2-earmarks` | `account-balances-balance-change-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `account-balances-balance-change-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `availables-change-available-1` |
| `post-corporate-v2-earmarks` | `availables-change-available-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `availables-change-available-1` |
| `post-account` | `corporate-corporate-account-creation-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `corporate-earmark-1` |
| `post-corporate-v2-earmarks` | `corporate-earmark-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `corporate-earmark-1` |
| `post-account` | `onboarding-succeeded-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v2-earmarks` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `platform-authorization-platform-authorization-1` |
| `patch-corporate-v2-earmarks-earmarkid` | `transaction-creation-1` |
| `post-corporate-v2-earmarks` | `transaction-creation-1` |
| `post-corporate-v2-earmarks-earmarkid-cancel` | `transaction-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/earmarks.md`: updatedAt 2026-05-27T21:46:12.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/earmarks.md` | whole document | https://developers.pismo.io/pismo-docs/docs/earmarks | `8b907acf2e923d22…` | 2026-05-27T21:46:12.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-platform-authentication--authentication` — API reference: Platform authentication — Authentication
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-PAY-hold-funds` — Hold funds
