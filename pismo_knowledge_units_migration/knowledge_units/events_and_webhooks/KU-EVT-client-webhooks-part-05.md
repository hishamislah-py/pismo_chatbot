---
ku_id: KU-EVT-client-webhooks-part-05
title: Client webhooks (part 5 of 14)
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
- KU-CARD-authorization-validation-rules-for-card-network-operations
- KU-CARD-rule-list-part-01
- KU-CARD-rule-list-part-02
- KU-CARD-rule-list-part-03
- KU-CARD-rule-list-part-04
grouping_rationale: single source page; split into parts because the page is very large
---

# Client webhooks (part 5 of 14)

**KU ID:** `KU-EVT-client-webhooks-part-05` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/core-platform/client-webhooks.md`:

> `}

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/client-webhooks.md`: no headings

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/client-webhooks.md` lines 1650–1943 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/client-webhooks · updatedAt: 2026-09-18T17:12:01.000Z

<!-- source:begin path=docs/core-platform/client-webhooks.md part=1649-1943 -->
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>password_present</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>bool</td>
                                                                                                                                                                                                          <td>Is password used flag</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>account_type</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Account type:
                                                                                                                                                                                                          <br><code>00</code> for non specified
                                                                                                                                                                                                          <br><code>10</code> for savings
                                                                                                                                                                                                          <br><code>20</code> for checking
                                                                                                                                                                                                          <br><code>30</code> for credit card
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr style="background-color: beige;">
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>validation_results</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>object array</td>
                                                                                                                                                                                                          <td>Performed validations list</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>name</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Validation ID
                                                                                                                                                                                                          <br>See <a href="https://developers.pismo.io/pismo-docs/docs/rule-list#authorization-amounts-calculation" target="_blank">Authorization rule list</a> for more information.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>status</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Execution status:
                                                                                                                                                                                                          <br><code> APPROVED</code>
                                                                                                                                                                                                          <br><code>REJECTED</code>
                                                                                                                                                                                                          <br><code>SKIPPED</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>reason</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Reason enum
                                                                                                                                                                                                          <br>For more information, refer to the
                                                                                                                                                                                                          <a href='https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations#list-of-rules' target='_blank'>authorization list of rules</a> guide.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>description</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Human-readable result reason</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>program_id</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>integer</td>
                                                                                                                                                                                                          <td>Program ID</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>token_id</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>integer</td>
                                                                                                                                                                                                          <td>Transaction cardholder token ID</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>wallet_id</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Transaction cardholder wallet ID</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>cardholder_postal_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Card holder's postal code in support of the Address Verification System (AVS) in Canada and Europe.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>cardholder_street_number</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Card holder's street number in support of the Address Verification System (AVS) in Canada and Europe.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>cardholder_street_address</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Card holder's street address in support of the Address Verification System (AVS) in Canada and Europe.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>match_address</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>bool</td>
                                                                                                                                                                                                          <td>If <code>cardholder_street_address</code> and <code>Cardholder_street_number</code> passed in the request matches the customer's street address according to the Pismo database, this flag is set to <code>true</code>, otherwise it is set to <code>false</code>. If <code>no_address_data</code> is <code>true</code>, this field is set to <code>false</code>.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>match_postal_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>bool</td>
                                                                                                                                                                                                          <td>If <code>cardholder_postal_code</code> matches the customer's postal code according to the Pismo database, this flag is set to <code>true</code>, otherwise it is set to <code>false</code>. If <code>no_address_data</code> is <code>true</code>, this field is set to <code>false</code>.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>no_address_data</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>bool</td>
                                                                                                                                                                                                          <td>If the customer's is not in the Pismo database and cannot be verified, this flag is set to <code>true</code>, otherwise it is set to <code>false</code>.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>card_metadata</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Any key-value object, information provided by customer for a specific card.
                                                                                                                                                                                                          </td>
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
                                                                                                                                                                                                          <tr style="background-color: beige;">
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>additional_service_result_data</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>object</td>
                                                                                                                                                                                                          <td>An array that contains the account name request result information.
                                                                                                                                                                                                          <br>This is only required if account_name_request="Y".</td>
                                                                                                                                                                                                          <td> </td>
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
                                                                                                                                                                                                          <td> </td>
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
                                                                                                                                                                                                          <td> </td>
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
                                                                                                                                                                                                          <td> </td>
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
                                                                                                                                                                                                          <td> </td>
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
                                                                                                                                                                                                          <td> </td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr style="background-color: beige;">
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>additional_service_request_data</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>object</td>
                                                                                                                                                                                                          <td>An array that contains the account name request information.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td> </td>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 60px">
                                                                                                                                                                                                          <code>account_name_request</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Determines request for account name information. Possible values:
                                                                                                                                                                                                          <br> <code>I</code> - issuer needs to send the name
                                                                                                                                                                                                          </br> <code>Y</code> - issuer needs to send matching result
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td> </td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          </table>
          `}
    </HTMLBlock>
  </details>
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/client-webhooks.md`: updatedAt 2026-09-18T17:12:01.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/client-webhooks.md` | body lines 1650–1943 | https://developers.pismo.io/pismo-docs/docs/client-webhooks | `cd35b3bad1d1b22b…` | 2026-09-18T17:12:01.000Z |

## Related knowledge units

- `KU-CARD-authorization-validation-rules-for-card-network-operations` — Authorization validation rules for card network operations
- `KU-CARD-rule-list-part-01` — Rule list (part 1 of 4)
- `KU-CARD-rule-list-part-02` — Rule list (part 2 of 4)
- `KU-CARD-rule-list-part-03` — Rule list (part 3 of 4)
- `KU-CARD-rule-list-part-04` — Rule list (part 4 of 4)
