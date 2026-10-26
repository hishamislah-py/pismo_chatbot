---
ku_id: KU-EVT-client-webhooks-part-06
title: Client webhooks (part 6 of 14)
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

# Client webhooks (part 6 of 14)

**KU ID:** `KU-EVT-client-webhooks-part-06` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

`docs/core-platform/client-webhooks.md` has no introductory paragraph.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/client-webhooks.md`: no headings

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/client-webhooks.md` lines 1944–2062 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/client-webhooks · updatedAt: 2026-09-18T17:12:01.000Z

<!-- source:begin path=docs/core-platform/client-webhooks.md part=1943-2062 -->
  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Sample request </summary>

    ```json
    {
    "id": "1111",
    "entity": "transaction",
    "fields": {
    "mti": "0100",
    "card_id": 1234,
    "account_id": 1234,
    "amount_transaction": 10,
    "amount_local": 10,
    "amount_settlement": 10,
    "transaction_timestamp": "2019-05-09 15:52:00",
    "processing_code": "00",
    "payment_card_brand": "Mastercard",
    "currency": "986",
    "merchant_id_code": "687555537877464",
    "merchant_name": "PISMO",
    "merchant_city": "SAO PAULO",
    "merchant_state_or_country_code": "BRA",
    "merchant_terminal_id": "12300004",
    "atc_chip": "43",
    "atc_database": "[748,652,998]",
    "cvv_data": "CVV_PRESENT",
    "entry_mode": "string",
    "mcc": "string",
    "card_type": "PLASTIC",
    "country_code": "076",
    "chip_validation": true,
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
    "cardholder_postal_code": 12345,
    "transaction_type": "00",
    "nsu": "15469",
    "retrieval_reference_number": "5600001085571",
    "authorization_code": "ABCD12",
    "incoming_authorization_code": "ABCD12",
    "response_code": "00",
    "terminal_capability": "string",
    "tvr": "0000248000",
    "cvr": "0110A040002A00000000000000000000FF",
    "number_of_installments": 3,
    "network_score": "0",
    "pos_postal_code": "22222222",
    "acquirer_code": "string",
    "denial_code": "CED",
    "financial_network_code": "ABC",
    "banknet_reference_number": "123456",
    "cvv_presence": true,
    "password_present": true,
    "original_network_data": "...",
    "account_type": "30",
    "validation_results": [
      {
        "name": "ARQC",
        "status": "APPROVED",
        "reason": "NO_CRYPTOGRAM",
        "description": "No cryptogram present"
      }
    ],
    "program_id": 0,
    "token_id": 1234,
    "wallet_id": "1234",
    "cardholder_street_number": 999,
    "cardholder_street_address": "Production St.",
    "match_address": true,
    "match_postal_code": true,
    "no_address_data": false
    },
    "card_metadata": {
    "olalongerkey1": "helloworld",
    "olalongerkey2": {
      "FgHiJ": "nestedValue2",
      "aBcDe": "nestedValue1"
    },
    "olalongerkey3": "helloworld",
    "olalongerkey4": {
      "kLmNo": "nestedValue1",
      "pQrSt": "nestedValue2"
    },
    "olalongerkey5": "helloworld",
    "account_owner_data": [
      {
        "account_owner_type": "PRIMARY_OWNER",
        "account_owner_name_first": "FirstName",
        "account_owner_name_middle": "MiddleName",
        "account_owner_name_last": "LastName",
        "additional_service_result_data": {
          "account_name_request_result": "NAME_MATCH_PERFORMED",
          "full_name_account_match_decision": "MATCH",
          "last_name_account_match_decision": "MATCH",
          "middle_name_account_match_decision": "MATCH",
          "first_name_account_match_decision": "MATCH"
        }
      }
    ],
    "additional_service_request_data": {
      "account_name_request": "I"
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
| `docs/core-platform/client-webhooks.md` | body lines 1944–2062 | https://developers.pismo.io/pismo-docs/docs/client-webhooks | `cd35b3bad1d1b22b…` | 2026-09-18T17:12:01.000Z |

## Related knowledge units

- None.
