---
ku_id: KU-EVT-international-bank-accounts-data-events
title: Banking - Bank accounts
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/international-bank-accounts-data-events.md
  sha256: 1efa1dc9fdf6f20dd27d8b64cddc5838e3cedb182c31b3897c15f1ee26f522b7
  url: https://developers.pismo.io/pismo-docs/docs/international-bank-accounts-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:15:05.000Z'
operations:
- delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-bban
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan
related_kus:
- KU-API-banking-bank-accounts--bank-accounts-part-01
- KU-API-banking-bank-accounts--bank-accounts-part-02
- KU-EVT-catalogue-other-domains
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Banking - Bank accounts

**KU ID:** `KU-EVT-international-bank-accounts-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/international-bank-accounts-data-events.md`:

> This table lists the international bank account endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/international-bank-accounts-data-events.md`: Banking - Bank accounts

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/international-bank-accounts-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/international-bank-accounts-data-events · updatedAt: 2026-03-18T15:15:05.000Z

<!-- source:begin path=docs/data-and-reporting/international-bank-accounts-data-events.md part=0-end -->

# Banking - Bank accounts

This table lists the international bank account endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

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
        [Register BBAN account](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-bban)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1" target="_blank">Bank account registered</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Register IBAN account](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1" target="_blank">Bank account registered</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Register Brazilian bank account](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1" target="_blank">Bank account registered</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Register UK bank account](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1" target="_blank">Bank account registered</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [Delete bank account](https://developers.pismo.io/pismo-docs/reference/delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name)
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-update-1" target="_blank">Bank account updated</a>
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v2/accounts/{accountId}/bank-accounts/bban` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-bban` | Register BBAN account | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-02 |
| `POST /v2/accounts/{accountId}/bank-accounts/iban` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban` | Register IBAN account | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `POST /v2/accounts/{accountId}/bank-accounts/brazil` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil` | Register Brazilian bank account | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `POST /v2/accounts/{accountId}/bank-accounts/uk-scan` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan` | Register UK bank account | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName}` | `delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name` | Delete bank account | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-02 |

### Operation essentials

- **`POST /v2/accounts/{accountId}/bank-accounts/bban`** (`post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-bban`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `scheme`; response statuses 201, 400, 403, 404, 409, 500; error codes in examples `EIBA0009`, `EIBA0012`, `EIBA0006`, `EIBA0007`, `EIBA0023`, `EIBA0010`, `EIBA0028`, `EIBA0005`, `EIBA0011`, `EIBA0013`, `EIBA0015`; events `intl-bankaccounts-intl-bankaccount-register-1`.
- **`POST /v2/accounts/{accountId}/bank-accounts/iban`** (`post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `scheme`; response statuses 201, 400, 403, 404, 409, 500; error codes in examples `EIBA0009`, `EIBA0012`, `EIBA0006`, `EIBA0007`, `EIBA0023`, `EIBA0010`, `EIBA0028`, `EIBA0005`, `EIBA0011`, `EIBA0013`, `EIBA0015`; events `intl-bankaccounts-intl-bankaccount-register-1`.
- **`POST /v2/accounts/{accountId}/bank-accounts/brazil`** (`post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `scheme`; response statuses 201, 400, 403, 404, 409, 500; error codes in examples `EIBA0009`, `EIBA0012`, `EIBA0006`, `EIBA0007`, `EIBA0023`, `EIBA0010`, `EIBA0028`, `EIBA0005`, `EIBA0011`, `EIBA0013`, `EIBA0015`; events `intl-bankaccounts-intl-bankaccount-register-1`.
- **`POST /v2/accounts/{accountId}/bank-accounts/uk-scan`** (`post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `scheme`; response statuses 201, 400, 403, 404, 409, 500; error codes in examples `EIBA0009`, `EIBA0012`, `EIBA0006`, `EIBA0007`, `EIBA0023`, `EIBA0010`, `EIBA0028`, `EIBA0005`, `EIBA0011`, `EIBA0013`, `EIBA0015`; events `intl-bankaccounts-intl-bankaccount-register-1`.
- **`DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName}`** (`delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path), `schemeName` (path); required body fields none declared; response statuses 204, 400, 403, 404, 500; error codes in examples `EIBA0012`, `EIBA0016`, `EIBA0006`, `EIBA0007`, `EIBA0023`, `EIBA0010`, `EIBA0005`, `EIBA0011`, `EIBA0013`, `EIBA0015`; events `intl-bankaccounts-intl-bankaccount-update-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-bban` | `intl-bankaccounts-intl-bankaccount-register-1` |
| `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil` | `intl-bankaccounts-intl-bankaccount-register-1` |
| `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban` | `intl-bankaccounts-intl-bankaccount-register-1` |
| `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan` | `intl-bankaccounts-intl-bankaccount-register-1` |
| `delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name` | `intl-bankaccounts-intl-bankaccount-update-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `intl-bankaccounts-intl-bankaccount-register-1` | intl | 1 | https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1 | 7 | KU-EVT-catalogue-other-domains |
| `intl-bankaccounts-intl-bankaccount-update-1` | intl | 1 | https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-update-1 | 2 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/international-bank-accounts-data-events.md`: updatedAt 2026-03-18T15:15:05.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/international-bank-accounts-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/international-bank-accounts-data-events | `1efa1dc9fdf6f20d…` | 2026-03-18T15:15:05.000Z |

## Related knowledge units

- `KU-API-banking-bank-accounts--bank-accounts-part-01` — API reference: Banking - Bank accounts — Bank accounts (part 1 of 2)
- `KU-API-banking-bank-accounts--bank-accounts-part-02` — API reference: Banking - Bank accounts — Bank accounts (part 2 of 2)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
