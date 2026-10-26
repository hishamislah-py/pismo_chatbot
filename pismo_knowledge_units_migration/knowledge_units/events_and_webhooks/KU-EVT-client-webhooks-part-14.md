---
ku_id: KU-EVT-client-webhooks-part-14
title: Client webhooks (part 14 of 14)
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

# Client webhooks (part 14 of 14)

**KU ID:** `KU-EVT-client-webhooks-part-14` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/core-platform/client-webhooks.md`:

> The `original_network_data` field contains all fields present in the ISO message coming from the network, except the PCI-sensitive information. The content varies according to the request being processed, where some fields may or may not be present. Refer to your card network's specification to find all possible fields.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/client-webhooks.md`: Examples of the original\_network\_data field

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/client-webhooks.md` lines 3815–4116 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/client-webhooks · updatedAt: 2026-09-18T17:12:01.000Z

<!-- source:begin path=docs/core-platform/client-webhooks.md part=3814-4116 -->
  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Sample response</summary>

    ```json
    {
      "approve": true,
      "force_approve": true,
      "referral": true,
      "response_code": "00",
      "metadata": {},
      "account": {
        "id": 123,
        "first_name": "firstName",
        "middle_name": "middleName",
        "last_name": "lastName",
        "document_number": "00000000000000"
      },
      "customer": {
        "id": 123,
        "first_name": "firstName",
        "middle_name": "MiddleName",
        "last_name": "lastName",
        "document_number": "00000000000000"
      },
      "validation_results": {
        "name": {
          "account": {
            "full_name": "MATCH",
            "last_name": "MATCH",
            "middle_name": "NO_MATCH",
            "first_name": "PARTIAL_MATCH"
          },
          "customer": {
            "full_name": "MATCH",
            "last_name": "MATCH",
            "middle_name": "NO_MATCH",
            "first_name": "PARTIAL_MATCH"
          }
        },
        "address": {
          "postal_code": "MATCH",
          "street": "NO_MATCH",
          "number": "PARTIAL_MATCH"
        }
      }
    }
    ```
  </details>
</details>

## Examples of the original\_network\_data field

The `original_network_data` field contains all fields present in the ISO message coming from the network, except the PCI-sensitive information. The content varies according to the request being processed, where some fields may or may not be present. Refer to your card network's specification to find all possible fields.

<details>
  <summary>Visa</summary>

  ```json Visa example of the original_network_data field
  {
    "panSource": "MOBILE_BANKING_APP",
    "tokenInfo": {
      "tokenType": "HCE",
      "numberOfActiveTokensForPAN": 0,
      "numberOfInactiveTokensForPAN": 0,
      "numberOfSuspendedTokensForPAN": 0
    },
    "deviceInfo": {
      "osType": "ANDROID",
      "deviceID": "i6LnmH740g4EKb1HC7eyy123",
      "osVersion": "14",
      "deviceName": "WGlhb21pIC0gMjIxMTEzMTdooo..",
      "deviceType": "MOBILEPHONE_OR_TABLET",
      "deviceBrand": "POCO",
      "deviceModel": "22111317OO",
      "deviceNumber": "9806",
      "deviceLocation": "-22.69/-43.12",
      "deviceIPAddressV4": "45.999.0.12",
      "deviceLanguageCode": "por",
      "deviceManufacturer": "Xiaomi",
      "tokenProtectionMethod": "SOFTWARE"
    },
    "encryptedData": "*****",
    "cardholderInfo": {
      "name": "JOHN DOE",
      "billingAddress": {},
      "expirationDate": {
        "year": "2031",
        "month": "01"
      },
      "highValueCustomer": false,
      "riskAssessmentScore": "23",
      "primaryAccountNumber": "*****"
    },
    "panReferenceID": "V-3026089583794218905123",
    "riskInformation": {
      "deviceIMEI": "17",
      "deviceTimeZone": "Ameri",
      "userAccountAge": "9999",
      "visaTokenScore": "04",
      "simSerialNumber": "23",
      "walletAccountAge": "256",
      "accountHolderName": "JOHN DOE",
      "deviceSerialNumber": "23",
      "riskAssessmentScore": "23",
      "visaTokenDecisioning": "00",
      "walletProviderPANAge": "0",
      "deviceTimeZoneSetting": "NETWORK_SET",
      "distinctCardholderNames": "1",
      "accountToDeviceBindingAge": "1",
      "walletProviderDeviceScore": "3",
      "walletProviderReasonCodes": "AG,AO,A0,A2",
      "walletProviderAccountScore": "5"
    },
    "lifeCycleTraceID": 356089583803123,
    "tokenReferenceID": "DNITHE352608958380350123",
    "tokenRequestorID": "40010075123",
    "clientWalletAccountID": "-9c4zaFD8bfEcLX2MAfDLOOO",
    "paymentAccountReference": "V0010013026085581472569655123",
    "walletAccountEmailAddressHash": "4D76566CD536BD24599AE9AA515960C1F9565FB341631A23A5D772B3CC4D4123"
  }
  ```
</details>

<details>
  <summary>Mastercard</summary>

  ```json Mastercard example of the original_network_data field
  {
    "de2_primary_account_number": "[card-hash]",
    "de3_processing_code": {
      "sf1_cardholder_transaction_type_code": "00",
      "sf2_cardholder_from_account_type_code": "30",
      "sf3_cardholder_to_account_type_code": "00"
    },
    "de4_amount_transaction": "000000001000",
    "de5_amount_settlement": "000000000251",
    "de6_amount_cardholder_billing": "000000001000",
    "de7_tranmission_date_and_time": {
      "sf1_date": "1110",
      "sf2_time": "175808"
    },
    "de9_conversion_rate_settlement": {
      "sf1_decimal_indicator": "7",
      "sf2_conversion_rate": "1859259"
    },
    "de10_conversion_rate_cardholder_billing": {
      "sf1_decimal_indicator": "6",
      "sf2_cardholderbilling_conversion_rate": "1000000"
    },
    "de11_stan": "637470",
    "de12_time_local_transaction": "145808",
    "de13_date_local_transaction": "0727",
    "de14_date_expiration": "2704",
    "de15_date_settlement": "0727",
    "de16_date_conversion": "0726",
    "de18_merchant_type": "7994",
    "de22_pos_entry_mode": {
      "sf1_pos_terminal_pan_entry_mode": "81",
      "sf2_pos_terminal_pin_entry_mode": "0"
    },
    "de28_amount_transaction_fee": {},
    "de29_amount_settlement_fee": {},
    "de30_amount_transaction_processing_fee": {},
    "de31_amount_settlement_processing_fee": {},
    "de32_acquiring_institution_id_code": "016800",
    "de33_forwarding_institution_id_code": "016800",
    "de37_retrieval_reference_number": {
      "sf1_transaction_date_and_initiator_discretionary_data": "0727499",
      "sf2_terminal_transaction_number": "51999"
    },
    "de41_card_acceptor_terminal_id": "WA000001",
    "de42_card_acceptor_id_code": "00027427823    ",
    "de43_card_acceptor_name_location_for_all_transactions": {
      "sf1_card_acceptor_name": "MerchantName           ",
      "sf3_card_acceptor_city": "SAO PAULO     ",
      "sf5_card_acceptor_state_or_country_code": "BRA"
    },
    "de48_additional_data_private_user": {
      "de48_tcc": "T",
      "de48_start": "224",
      "de48_size": "123",
      "de48SubElements": [
        "37",
        "42",
        "92",
        "56",
        "75",
        "71"
      ],
      "se11_key_exchange_block_data": {},
      "se13_mastercard_hosted_mobile_phone_top_up_request_data": {},
      "se15_authorization_system_advice_date_and_time": {},
      "se18_service_parameters": {},
      "se23_payment_initiation_channel": {},
      "se25_mastercard_cash_program_data": {},
      "se26_wallet_program_data": {},
      "se33_pan_mapping_file_information": {},
      "se34_atc_information": {},
      "se36_visa_mmv": {},
      "se37_additional_merchant_data": {
        "sf1_payment_facilitador_id": "00000231811",
        "sf3_sub_merchant_id": "00027427823    "
      },
      "se40_eletronic_commerce_merchant_cardholder_certificate_serial_number": {},
      "se41_eletronic_commercer_certificate_qualifying_information": {},
      "se42_eletronic_commerce_indicator": {
        "sf1_eletronic_commerce_security_level_indicator_ucaf_collection_indicator": "910"
      },
      "se43_ucaf": {},
      "se48_mobile_program_indicator": {},
      "se49_time_validation_information": {},
      "se51_merchant_on_behalf_services": {},
      "se55_merchant_fraud_scoring_data": {},
      "se56_security_services_additional_data_for_issuers": [
        {
          "sf1_security_services_indicator": "AQV",
          "sf2_security_services_data": "600"
        },
        {
          "sf1_security_services_indicator": "AQS",
          "sf2_security_services_data": "408"
        },
        {
          "sf1_security_services_indicator": "AQF",
          "sf2_security_services_data": "500"
        }
      ],
      "se57_security_services_additional_data_for_acquirers": {},
      "se58_atm_additional_data": {},
      "se61_pos_data_extended_condition_codes": {},
      "se64_transit_program": {},
      "se65_terminal_compliant_indicator": {},
      "se66_authentication_data": {},
      "se67_money_send_information": {},
      "se71_onbehalf_services": [
        {
          "sf1_ob_service": "18",
          "sf2_onbehalf_result1": "C",
          "sf3_onbehalf_result2": " "
        }
      ],
      "se74_additional_processing_information": {},
      "se75_fraud_scoring_data": {
        "sf1_fraud_score": "036",
        "sf2_score_reason_code": "91",
        "sf3_rules_score": "036",
        "sf4_rules_reason_code1": "91",
        "sf5_rules_reason_code2": "00"
      },
      "se78_payment_service_indicator": {},
      "se79_chip_cvr_or_tvr_bit_error_results": {},
      "se87_card_validation_code_result_or_cvv2": "U",
      "se93_fleet_card_id_request_data": {}
    },
    "de49_currency_code_transaction": "986",
    "de50_currency_code_settlement": "840",
    "de51_currency_code_cardholder_billing": "986",
    "de55_integrated_circuit_card": {
    	"sf2_cryptogram_information_data": "80",
      "sf3_issuer_application_data": "0120B04009990000000000000000000000FF",
      "sf5_terminal_verification_result": "0000048000",
      "sf6_transaction_date": "221205",
      "sf7_transaction_type": "00",
      "sf8_amount_authorized": "000000009910",
      "sf9_transaction_currency_code": "0986",
      "sf10_application_interchange_profile": "3900",
      "sf11_terminal_country_code": "0076",
      "sf12_cardholder_verification_method": "420300",
      "sf13_terminal_capabilities": "E0F0C8",
      "sf23_application_transaction_counter": "0050"
    },
    "de60_advice_reason_code": {},
    "de61_pos_data": {
      "sf1_pos_terminal_attendance": "1",
      "sf2_reserved_for_future_use": "0",
      "sf3_pos_terminal_location": "2",
      "sf4_pos_cardholder_presence": "5",
      "sf5_pos_card_presence": "1",
      "sf6_pos_card_capture_capabilities": "0",
      "sf7_pos_transaction_status": "4",
      "sf8_pos_transaction_security": "0",
      "sf9_reserved_for_future_use": "0",
      "sf10_cardholder_activated_terminal_level": "6",
      "sf11_pos_card_data_terminal_input_capability_indicator": "0",
      "sf12_pos_authorization_life_cycle": "05",
      "sf13_pos_country_code_or_submerchant": "076",
      "sf14_postal_code_or_submerchant": "01452002  "
    },
    "de63_network_data": {
      "sf1_financial_network_code": "MPL",
      "sf2_banknet_reference_number": "JMPDOT"
    },
    "de90_original_data_elements": {},
    "de94_service_indicator": {},
    "de95_replacement_amounts": {},
    "de97_amount_net_settlement": {},
    "de112_additional_data_national_use": {},
    "de120_record_data": {},
    "de124_member_defined_data": {},
  }
  ```
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
| `docs/core-platform/client-webhooks.md` | body lines 3815–4116 | https://developers.pismo.io/pismo-docs/docs/client-webhooks | `cd35b3bad1d1b22b…` | 2026-09-18T17:12:01.000Z |

## Related knowledge units

- None.
