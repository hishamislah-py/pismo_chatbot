---
ku_id: KU-EVT-client-webhooks-part-03
title: Client webhooks (part 3 of 14)
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
- KU-CARD-full-and-zero-balance-workflows
grouping_rationale: single source page; split into parts because the page is very large
---

# Client webhooks (part 3 of 14)

**KU ID:** `KU-EVT-client-webhooks-part-03` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/core-platform/client-webhooks.md`:

> This section details how Zero balance customers should code their validations and anti-fraud webhook for the transaction authorization process. The webhook request to Zero balance clients occurs during step 5 in the [Full and Zero balance workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/client-webhooks.md`: Zero balance validations webhook

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/client-webhooks.md` lines 1071–1240 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/client-webhooks · updatedAt: 2026-09-18T17:12:01.000Z

<!-- source:begin path=docs/core-platform/client-webhooks.md part=1070-1240 -->
## Zero balance validations webhook

This section details how Zero balance customers should code their validations and anti-fraud webhook for the transaction authorization process. The webhook request to Zero balance clients occurs during step 5 in the [Full and Zero balance workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).

Unlike Full balance issuers, Zero balance issuers need to do their own account and limit checks as well as validations and anti-fraud checks. Pismo performs basic card validations for Zero balance customers and, if any of the validations fail, this webhook is not called. This webhook is optional, but if you want to provide one, you should register it during setup.

In the Request and Response fields table Required columns, Y = required, N = not required, C = conditional.

<details>
  <summary style={{fontSize: "18px"}}><b>Webhook specifications</b></summary>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Request headers</summary>

    <HTMLBlock>
      {`
                                                                                                                                                                                                          <table>
                                                                                                                                                                                                          <tr style={{backgroundColor: "lightgrey"}}>
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
                                                                                                                                                                                                          <td><code>x-cid</code></td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Authorization correlation ID. The CID is used to link related API requests and events. For example, if a user makes an authorization request with 10 installments, this generates 1 authorization event and 10 transaction events all containing the same correlation ID. The x-cid can help the Pismo engineering team track everything related to a call. If one isn't passed, it is automatically generated. You can find it in a response header.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td><code>Authorization</code></td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Access token </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td><code>Content-type</code></td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>A specification for a structured, used application/json</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td><code>User-Agent</code></td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>The user agent responsible for making a given HTTP request. For example, pismo/http-client.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          </table>
          `}
    </HTMLBlock>
  </details>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Request fields</summary>

    <HTMLBlock>
      {`
                                                                                                                                                                                                          <table>
                                                                                                                                                                                                          <tr style={{backgroundColor: "lightgrey"}}>
                                                                                                                                                                                                          <th>Field</th>
                                                                                                                                                                                                          <th>Type</th>
                                                                                                                                                                                                          <th>Description</th>
                                                                                                                                                                                                          <th>Req</th>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td>
                                                                                                                                                                                                          <code>id</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Database transaction ID</td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td>
                                                                                                                                                                                                          <code>entity</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string </td>
                                                                                                                                                                                                          <td>Entity type enum:
                                                                                                                                                                                                          <br>-
                                                                                                                                                                                                          <code>transaction</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr >
                                                                                                                                                                                                          <tr style="background-color: beige;">
                                                                                                                                                                                                          <td>
                                                                                                                                                                                                          <code>fields</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>object</td>
                                                                                                                                                                                                          <td>Fields submitted through zero balance anti-fraud ingress requests. Note that each entity type has some exclusive fields (Those fields have an additional note between []).</td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>mti</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Message type ID. For example:
                                                                                                                                                                                                          <br><code>0100</code> = auth. request
                                                                                                                                                                                                          <br><code>0110</code> = auth. response
                                                                                                                                                                                                          <br><code>0120</code> = auth. advice
                                                                                                                                                                                                          <br>For more information, refer to
                                                                                                                                                                                                          <a href="https://en.wikipedia.org/wiki/ISO_8583#Message_type_indicator_(MTI)" target="_blank">MTI</a>.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>card_id</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>int</td>
                                                                                                                                                                                                          <td>Transaction cardholder card ID</td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>account_id</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>int</td>
                                                                                                                                                                                                          <td>Transaction cardholder account ID</td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>amount_transaction</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>number</td>
                                                                                                                                                                                                          <td>Transaction amount in the customer's  currency</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>amount_local</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>number</td>
                                                                                                                                                                                                          <td>Transaction amount in the merchant's local currency</td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>transaction_timestamp</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Transaction date and hour (format:yyyy-MM-ddThh:mm:ss) local time, no TZ.
                                                                                                     <br>This is the <code>data.transaction.localDateTime</code> from the network, fields DE12/DE13, when present. 
                                                                                                     <br>If DE12/DE13 are not present, this is the authorization's current time, not the real transaction time. 
                                                                                                     <br>For transmission time, use the UTC DE7 carried as <code>transmission_date_time</code>.</td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>amount_settlement</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>number</td>
                                                                                                                                                                                                          <td>Amount in settlement currency defined by the issuer</td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>processing_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>This is the transaction's effect on the customer account and the type of accounts affected.
                                                                                                                                                                                                          <br>This is the 6-digit Pismo processing code which identifies financial operations on the Pismo platform.
                                                                                                                                                           
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/client-webhooks.md`: updatedAt 2026-09-18T17:12:01.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/client-webhooks.md` | body lines 1071–1240 | https://developers.pismo.io/pismo-docs/docs/client-webhooks | `cd35b3bad1d1b22b…` | 2026-09-18T17:12:01.000Z |

## Related knowledge units

- `KU-CARD-full-and-zero-balance-workflows` — Full and Zero balance transaction workflows
