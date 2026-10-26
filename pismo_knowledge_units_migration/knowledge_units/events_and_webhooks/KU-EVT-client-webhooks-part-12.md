---
ku_id: KU-EVT-client-webhooks-part-12
title: Client webhooks (part 12 of 14)
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
related_kus: []
grouping_rationale: single source page; split into parts because the page is very large
---

# Client webhooks (part 12 of 14)

**KU ID:** `KU-EVT-client-webhooks-part-12` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/core-platform/client-webhooks.md`:

> `}

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/client-webhooks.md`: no headings

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/client-webhooks.md` lines 3368–3494 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/client-webhooks · updatedAt: 2026-09-18T17:12:01.000Z

<!-- source:begin path=docs/core-platform/client-webhooks.md part=3367-3494 -->
                              </tr>

                                                                                                                                                                                                             </table>
          `}
    </HTMLBlock>
  </details>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Sample request</summary>

    ```json
    {
      "id": "11114444555566667777888899991111222233",
      "entity": "transaction",
      "fields": {
        "mti": "0100",
        "card_id": 1234,
        "card_status": "NORMAL",
        "card_expiration_date": "2026-10-15T00:00:00.000Z",
        "card_type": "PLASTIC",
        "card_mode_type": "CREDIT",
        "pin_validated": "TRUE",
        "token_id": 1234,
        "wallet_id": "1234",
        "device_id_wallet": "1234",
        "account_id": 1234,
        "authorization_code": "ABCD12",
        "nsu": "15469",
        "advice_reason_code": "string",
        "advice_detail_code": "0110",
        "amount_transaction": 10,
        "amount_local": 10,
        "amount_settlement": 10,
        "transaction_timestamp": "2019-05-09 15:52:00",
        "payment_card_brand": "Mastercard",
        "currency": "986",
        "merchant_id_code": "687555537877464",
        "merchant_name": "PISMO",
        "merchant_city": "SAO PAULO",
        "merchant_state_or_country_code": "BRA",
        "merchant_terminal_id": "12300004",
        "security_cnp_transaction": "123",
        "atc_chip": "43",
        "atc_database": "[ 748, 652, 998 ]",
        "entry_mode": "string",
        "mcc": "string",
        "country_code": "076",
        "postal_code": "31404",
        "chip_cryptogram_information_data": "80",
        "chip_transaction_date": "190425",
        "chip_transaction_type": "string",
        "chip_amount_authorized": "000000000010",
        "chip_transaction_currency_code": "0076",
        "chip_application_interchange_profile": "0076",
        "chip_terminal_country_code": "076",
        "chip_cardholder_verification_method": "420300",
        "chip_terminal_capabilities": "E0F0C8",
        "chip_amount_other": "string",
        "chip_application_transaction_counter": "3900",
        "cardholder_postal_code": "22222222",
        "transaction_type": "00",
        "terminal_capability": "string",
        "tvr": "0000248000",
        "cvr": "0110A040002A00000000000000000000FF",
        "number_of_installments": 3,
        "available_limit": 200.55,
        "network_score": 0,
        "pos_postal_code": "22222222",
        "acquirer_code": "string",
        "cpf": "string",
        "total_limit": 5000,
        "max_credit_limit": 5000,
        "denial_code": "CED",
        "response_code": "00",
        "last_referral_reason": "",
        "id_last_referral_reason": "",
        "last_referral_unlock_date": "2019-05-09 15:52:00",
        "cvv_data": true,
        "cvv_response": true,
        "unlock_date": "string",
        "password_present": true,
        "last_four_digits": "string",
        "bin": "string",
        "program_id": 0,
        "pin_validated_offline": true,
        "validation_results": [
          {
            "name": "ARQC",
            "status": "APPROVED",
            "reason": "NO_CRYPTOGRAM",
            "description": "No cryptogram present"
          }
        ],
        "transaction_mode": "CREDIT",
        "three_domain_security": {
          "service_indicator": "S",
          "electronic_commerce_indicator": "05",
          "cardholder_authentication": "00",
          "authentication_data": "0201020590000000000000000000"
        },
        "account": {
          "id": 123,
          "first_name": " FirstName ",
          "middle_name": "middleName",
          "last_name": "lastName",
          "document_number": "00000000000000",
          "address": {
            "postal_code": "",
            "number": 999,
            "street": "Production St."
          }
        },
        "customer": {
          "id": 123,
          "first_name": "firstName",
          "middle_name": "middleName",
          "last_name": "lastName",
          "document_number": "00000000000000"
        }
      }
    }
    ```
  </details>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}> Response fields</summary>
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/client-webhooks.md`: updatedAt 2026-09-18T17:12:01.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/client-webhooks.md` | body lines 3368–3494 | https://developers.pismo.io/pismo-docs/docs/client-webhooks | `cd35b3bad1d1b22b…` | 2026-09-18T17:12:01.000Z |

## Related knowledge units

- None.
