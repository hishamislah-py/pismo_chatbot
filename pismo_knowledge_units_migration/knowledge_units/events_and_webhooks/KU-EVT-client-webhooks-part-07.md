---
ku_id: KU-EVT-client-webhooks-part-07
title: Client webhooks (part 7 of 14)
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
- KU-ERR-validation-codes-for-authorization-events-part-01
- KU-ERR-validation-codes-for-authorization-events-part-02
grouping_rationale: single source page; split into parts because the page is very large
---

# Client webhooks (part 7 of 14)

**KU ID:** `KU-EVT-client-webhooks-part-07` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/core-platform/client-webhooks.md`:

> For example:<br>
>                                                                                                                                                                                                           02 - Cannot approve at this time<br>
>                                                                                                                                                                                                           03 - Do not try again

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/client-webhooks.md`: no headings

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/client-webhooks.md` lines 2063–2354 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/client-webhooks · updatedAt: 2026-09-18T17:12:01.000Z

<!-- source:begin path=docs/core-platform/client-webhooks.md part=2062-2354 -->
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
                                                                                                                                                                                                          <code>is_approved</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>bool</td>
                                                                                                                                                                                                          <td>Is transaction approved flag</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td>
                                                                                                                                                                                                          <code>response_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Network two digit response code. For example:
                                                                                                                                                                                                          <br><code>00</code> = approve
                                                                                                                                                                                                          <br><code>51</code> = insufficient funds
                                                                                                                                                                                                          <br><code>57</code> = card not active
                                                                                                                                                                                                          <br><code>96</code> = system failure, etc. For more information, refer to
                                                                                                                                                                                                          <a href="https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events" target="_blank">Validation codes for authorization events</a>. If <code>approve</code> = <code>false</code>, you can use this value to respond to the network.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td>
                                                                                                                                                                                                          <code>merchant_denial_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>The merchant denial code indicates the reason for declined authorizations and the course of action that merchants can take.<br>
                                                                                                                                                                                                          For example:<br>
                                                                                                                                                                                                          02 - Cannot approve at this time<br>
                                                                                                                                                                                                          03 - Do not try again
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td>
                                                                                                                                                                                                          <code>limit_amount</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>number</td>
                                                                                                                                                                                                          <td>Limit available. An ordinary case is balance inquiry. Return null if there is no need to pass it. [entity:"transaction" only]</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr style="background-color: beige;">
                                                                                                                                                                                                          <td>
                                                                                                                                                                                                          <code>available_credit_limit</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>object</td>
                                                                                                                                                                                                          <td>Balance limit for processing code 30 (balance inquiry) <br> or <br> Voucher authorizations - account_type 70</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>amount</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>number</td>
                                                                                                                                                                                                          <td>Available credit limit amount</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>currency_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>integer</td>
                                                                                                                                                                                                          <td>ISO 4217 currency code. For example: 986 = Brazilian real.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr style="background-color: beige;">
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>account_owner_data</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>array</td>
                                                                                                                                                                                                          <td>An array that contains the account owner information (sent by Visa for validation).
                                                                                                                                                                                                          <br>This is only required if account_name_request="Y".</td>
                                                                                                                                                                                                          <td> </td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>account_owner_type</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Account owner type can be <code>PRIMARY</code> or <code>SECONDARY</code>.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>account_owner_name_first</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Primary or secondary account owner's first name</td>
                                                                                                                                                                                                          <td>This is only required for transactions that occur between merchant acquirers and issuers in Brazilian territories and/or if accountNameRequest="Y".</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>account_owner_name_middle</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Primary or secondary account owner's middle name</td>
                                                                                                                                                                                                          <td>This is only required for transactions that occur between merchant acquirers and issuers in Brazilian territories and/or if accountNameRequest="Y".</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>account_owner_name_last</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Primary or secondary account owner's last name</td>
                                                                                                                                                                                                          <td>This is only required for transactions that occur between merchant acquirers and issuers in Brazilian territories and/or if accountNameRequest="Y".</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>document_number</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Document number</td>
                                                                                                                                                                                                          <td>This is only required for transactions that occur between merchant acquirers and issuers in Brazilian territories</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr style="background-color: beige;">
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>address</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>object</td>
                                                                                                                                                                                                          <td>Account owner address
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>Address data is only required with authorization OCT (processing code 26) and when the merchant is from Canada or the U.S. </td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 90px;">
                                                                                                                                                                                                          <code>street</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Street name for account owner address
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>Address data is only required with authorization OCT (processing code 26) and when the merchant is from Canada or the U.S. </td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 90px;">
                                                                                                                                                                                                          <code>number</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Address number for account owner
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>Address data is only required with authorization OCT (processing code 26) and when the merchant is from Canada or the U.S. </td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr style="background-color: beige;">
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>additional_service_result_data</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>object</td>
                                                                                                                                                                                                          <td>An array that contains the account name request result information.
                                                                                                                                                                                                          <br>This is only required if account_name_request="Y".</td>
                                                                                                                                                                                                          <td>C</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 90px">
                                                                                                                                                                                                          <code>account_name_request_result</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Indicates if a match was performed. This is only required if accountNameRequest="I". Possible values:
                                                                                                                                                                                                          <br><code>NAME_MATCH_PERFORMED</code>
                                                                                                                                                                                                          <br><code>NAME_MATCH_NOT_PERFORMED</code>
                                                                                                                                                                                                          <br><code>NAME_MATCH_NOT_SUPPORTED</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>C</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 90px">
                                                                                                                                                                                                          <code>full_name_account_match_decision</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Match decision value is only required if account_name_request="Y". Possible values:
                                                                                                                                                                                                          <br><code>MATCH</code>
                                                                                                                                                                                                          <br><code>PARTIAL_MATCH</code>
                                                                                                                                                                                                          <br><code>NO_MATCH</code>
                                                                                                                                                                                                          <br><code>UNVERIFIED</code> = when for some reason the validation is not performed.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>C</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 90px">
                                                                                                                                                                                                          <code>last_name_account_match_decision</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Match decision value is only required if account_name_request="Y". Possible values:
                                                                                                                                                                                                          <br><code>MATCH</code>
                                                                                                                                                                                                          <br><code>PARTIAL_MATCH</code>
                                                                                                                                                                                                          <br><code>NO_MATCH</code>
                                                                                                                                                                                                          <br><code>UNVERIFIED</code> = when for some reason the validation is not performed.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>C</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 90px">
                                                                                                                                                                                                          <code>middle_name_account_match_decision</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Match decision value is only required if account_name_request="Y". Possible values:
                                                                                                                                                                                                          <br><code>MATCH</code>
                                                                                                                                                                                                          <br><code>PARTIAL_MATCH</code>
                                                                                                                                                                                                          <br><code>NO_MATCH</code>
                                                                                                                                                                                                          <br><code>UNVERIFIED</code> = when for some reason the validation is not performed.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>C</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 90px">
                                                                                                                                                                                                          <code>first_name_account_match_decision</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Match decision value is only required if account_name_request="Y". Possible values:
                                                                                                                                                                                                          <br><code>MATCH</code>
                                                                                                                                                                                                          <br><code>PARTIAL_MATCH</code>
                                                                                                                                                                                                          <br><code>NO_MATCH</code>
                                                                                                                                                                                                          <br><code>UNVERIFIED</code> = when for some reason the validation is not performed.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>C</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td>
                                                                                                                                                                                                          <code>match_address</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>bool</td>
                                                                                                                                                                                                          <td>If <code>cardholder_street_address</code> and <code>cardholder_street_number</code> passed in the request matches the customer's street address, this flag is set to <code>true</code>, otherwise it is set to <code>false</code>. The value of this field will override Pismo's matching results when informed.<br>
                                                                                                                                                                                                          <br>If <code>no_address_data</code> is <code>true</code>, this field is not required.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td>
                                                                                                                                                                                                          <code>match_postal_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>bool</td>
                                                                                                                                                                                                          <td>If <code>cardholder_postal_code</code> matches the customer's postal code, this flag is set to <code>true</code>, otherwise it is set to <code>false</code>. The value of this field will override Pismo's matching results when informed.<br>
                                                                                                                                                                                                          <br>If <code>no_address_data</code> is <code>true</code>, this field is not required.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td>
                                                                                                                                                                                                          <code>no_address_data</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>bool</td>
                                                                                                                                                                                                          <td>If the customer's address is not in the system and cannot be verified, this flag is set to <code>true</code>, otherwise it is set to <code>false</code>. The value of this field will override Pismo's matching results when informed.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                      </tr>
                                                                                                                                                                                                          <tr style="background-color: beige;">
                                                                                                                                                                                                          <td>
                                                                                                                                                                                                          <code>partial_approval_info</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>object</td>
                                                                                                                                                                                                          <td>Partial authorization addresses insufficient fund declines at point-of-sale when the available Visa card or account balance is not sufficient to approve a transaction in full. </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>local_amount</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>number</td>
                                                                                                                                                                                                          <td>Amount that was partially approved in the transaction's local currency.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                      <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>settlement_amount</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>number</td>
                                                                                                                                                                                                          <td>Amount that was partially approved in the reconciliation currency.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                      <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>cardholder_amount</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>number</td>
                                                                                                                                                                                                          <td>Amount that was partially approved in the cardholder's local currency.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          </table>
          `}
    </HTMLBlock>
  </details>
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/client-webhooks.md`: updatedAt 2026-09-18T17:12:01.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/client-webhooks.md` | body lines 2063–2354 | https://developers.pismo.io/pismo-docs/docs/client-webhooks | `cd35b3bad1d1b22b…` | 2026-09-18T17:12:01.000Z |

## Related knowledge units

- `KU-ERR-validation-codes-for-authorization-events-part-01` — Validation codes for authorization events (part 1 of 2)
- `KU-ERR-validation-codes-for-authorization-events-part-02` — Validation codes for authorization events (part 2 of 2)
