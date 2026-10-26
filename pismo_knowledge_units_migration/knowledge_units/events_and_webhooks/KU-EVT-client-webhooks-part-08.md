---
ku_id: KU-EVT-client-webhooks-part-08
title: Client webhooks (part 8 of 14)
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/client-webhooks.md
  sha256: cd35b3bad1d1b22bcca9904923038c09b3581f0196a1afc2f4a7a436effd79f4
  url: https://developers.pismo.io/pismo-docs/docs/client-webhooks
  role: primary_guide
  updated_at: '2026-09-18T17:12:01.000Z'
operations: []
related_kus:
- KU-CARD-anti-fraud-integration
- KU-CARD-full-and-zero-balance-workflows
grouping_rationale: single source page; split into parts because the page is very large
---

# Client webhooks (part 8 of 14)

**KU ID:** `KU-EVT-client-webhooks-part-08` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/core-platform/client-webhooks.md`:

> This section details how Full balance customers should code their anti-fraud webhook for the transaction authorization process. This webhook request to Full balance clients occurs during step 5 in the  [Full and Zero balance workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).  This webhook is optional, but if you want to provide one, you should register it during setup.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/client-webhooks.md`: Full balance anti-fraud  webhook

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/client-webhooks.md` lines 2355–2453 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/client-webhooks · updatedAt: 2026-09-18T17:12:01.000Z

<!-- source:begin path=docs/core-platform/client-webhooks.md part=2354-2453 -->
  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Sample response </summary>

    ```json

    {
    "is_approved": true,
    "response_code": "00",
    "merchant_denial_code": "03",
    "limit_amount": 12.34,
    "account_owner_data": [
    {
      "account_owner_type": "PRIMARY_OWNER",
      "account_owner_name_first": "Abbie",
      "account_owner_name_middle ": "Beth",
      "account_owner_name_last": "Norman",
      "document_number": "83493028"
    },
    {
      "account_owner_type": "SECONDARY_OWNER",
      "account_owner_name_first": "John",
      "account_owner_name_middle": "Wade",
      "account_owner_name_last": "Garrison",
      "document_number": "83493028"
    }
    ],
    "address": {
      "street": "Av. del Libertador",
      "number": 174
    },
    "additional_service_result_data": {
       "account_name_request_result": "NAME_MATCH_PERFORMED",
       "full_name_account_match_decision ": "MATCH",
       "last_name_account_match_decision": "MATCH",
       "middle_name_account_match_decision ": "NO_MATCH",
       "first_name_account_match_decision": "PARTIAL_MATCH"
    },
    "match_address": true,
    "match_postal_code": true,
    "no_address_data": false
    }

    ```
  </details>
</details>

## Full balance anti-fraud  webhook

This section details how Full balance customers should code their anti-fraud webhook for the transaction authorization process. This webhook request to Full balance clients occurs during step 5 in the  [Full and Zero balance workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).  This webhook is optional, but if you want to provide one, you should register it during setup.

For more information, refer to the [Anti-fraud integration](https://developers.pismo.io/pismo-docs/docs/anti-fraud-integration) guide.

<details>
  <summary style={{fontSize: "18px"}}><b>Webhook specifications</b></summary>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Request headers</summary>

    <HTMLBlock>
      {`
                                                                                                                                                                                                                                                                                                                          <table>
                                                                                                                                                                                                                                                                                                                            <tr  style="background-color: lightgrey;">
                                                                                                                                                                                                                                                                                                                            <th>Field</th>
                                                                                                                                                                                                                                                                                                                            <th>Type</th>
                                                                                                                                                                                                                                                                                                                            <th>Description</th>
                                                                                                                                                                                                                                                                                                                            <th>Req</th>
                                                                                                                                                                                                                                                                                                                            </tr>
                                                                                                                                                                                                                                                                                                                           <tr>
                                                                                                                                                                                                                                                                                                                             <td><pre>x-tenant</pre></td>
                                                                                                                                                                                                                                                                                                                             <td>string</td>
                                                                                                                                                                                                                                                                                                                             <td>Organization/tenant ID</td>
                                                                                                                                                                                                                                                                                                                             <td>N</td>
                                                                                                                                                                                                                                                                                                                            </tr>
                                                                                                                                                                                                                                                                                                                           <tr> 
                                                                                                                                                                                                                                                                                                                             <td><code>x-account-id</code></td>
                                                                                                                                                                                                                                                                                                                             <td>number</td>
                                                                                                                                                                                                                                                                                                                             <td>Transaction cardholder account ID</td>
                                                                                                                                                                                                                                                                                                                             <td>N</td>
                                                                                                                                                                                                                                                                                                                            </tr>
                                                                                                                                                                                                                                                                                                                             <tr> 
                                                                                                                                                                                                                                                                                                                             <td><code>Authorization</code></td>
                                                                                                                                                                                                                                                                                                                             <td>string</td>
                                                                                                                                                                                                                                                                                                                             <td>Access token </td>
                                                                                                                                                                                                                                                                                                                             <td>N</td>
                                                                                                                                                                                                                                                                                                                            </tr>
                                                                                                                                                                                                                                                                                                                             <tr> 
                                                                                                                                                                                                                                                                                                                             <td><code>x-amount</code></td>
                                                                                                                                                                                                                                                                                                                             <td>number</td>
                                                                                                                                                                                                                                                                                                                             <td>Transaction amount</td>
                                                                                                                                                                                                                                                                                                                             <td>N</td>
                                                                                                                                                                                                                                                                                                                            </tr>
                                                                                                                                                                                                                                                                                                                          </table>
          `}
    </HTMLBlock>
  </details>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Request fields</summary>
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/client-webhooks.md`: updatedAt 2026-09-18T17:12:01.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/client-webhooks.md` | body lines 2355–2453 | https://developers.pismo.io/pismo-docs/docs/client-webhooks | `cd35b3bad1d1b22b…` | 2026-09-18T17:12:01.000Z |

## Related knowledge units

- `KU-CARD-anti-fraud-integration` — Anti-fraud integration
- `KU-CARD-full-and-zero-balance-workflows` — Full and Zero balance transaction workflows
