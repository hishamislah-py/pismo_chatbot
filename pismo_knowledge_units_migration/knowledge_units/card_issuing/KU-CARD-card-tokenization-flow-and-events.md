---
ku_id: KU-CARD-card-tokenization-flow-and-events
title: Card tokenization flow and events
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/card-tokenization-flow-and-events.md
  sha256: 2ccc85848c54735d11d2da65bc61f94e06639ee97f8673fce9224f15b4dd43c4
  url: https://developers.pismo.io/pismo-docs/docs/card-tokenization-flow-and-events
  role: primary_guide
  updated_at: '2026-07-20T22:51:12.000Z'
operations: []
related_kus:
- KU-EVT-client-webhooks-part-01
- KU-EVT-client-webhooks-part-02
- KU-EVT-client-webhooks-part-03
- KU-EVT-client-webhooks-part-04
- KU-EVT-client-webhooks-part-05
- KU-EVT-client-webhooks-part-06
- KU-EVT-client-webhooks-part-07
- KU-EVT-client-webhooks-part-08
- KU-EVT-client-webhooks-part-09
- KU-EVT-client-webhooks-part-10
- KU-EVT-client-webhooks-part-11
- KU-EVT-client-webhooks-part-12
- KU-EVT-client-webhooks-part-13
- KU-EVT-client-webhooks-part-14
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Card tokenization flow and events

**KU ID:** `KU-CARD-card-tokenization-flow-and-events` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/card-tokenization-flow-and-events.md`:

> Credit card tokenization converts sensitive cardholder data to a randomly-generated string of numbers called a *token* that can be used in payments or other financial transactions. Similar to encryption, tokenization obfuscates the original data to render it unreadable during a digital transmission breach or other exposure.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/card-tokenization-flow-and-events.md`: Card tokenization flow and events; Pismo provisioning refusal reasons; Tokenization events; Mastercard Digital Enablement Service (MDES); MDES token authorization (TA) provisioning; MDES activation code (AC); MDES tokenization complete (TC); MDES TV (tokenization event); MDES TE refusal; Visa Token Service (VTS); VTS token create; VTS approve provisioning; VTS get cardholder verification method (CVM); VTS passcode verification; VTS token status updated; VTS token deactivated; VTS token suspended; VTS token resume

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/card-tokenization-flow-and-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/card-tokenization-flow-and-events · updatedAt: 2026-07-20T22:51:12.000Z

<!-- source:begin path=docs/card-issuing/card-tokenization-flow-and-events.md part=0-end -->

# Card tokenization flow and events

Credit card tokenization converts sensitive cardholder data to a randomly-generated string of numbers called a *token* that can be used in payments or other financial transactions. Similar to encryption, tokenization obfuscates the original data to render it unreadable during a digital transmission breach or other exposure.

The network communication to Pismo during tokenization involves five basic operations. Depending on network (Visa, Mastercard), they may vary slightly, but they are roughly the same.

1. **Eligibility**—The token requestor, such as Samsung Pay or Android Pay, checks if a card can be digitized according to configurations the issuer previously made with the network.

2. **Authentication**—The card is ready to be digitized and the authentication process begins. There are three different results depending on eligibility. The card networks refer to these flows with colors - green flow, red flow and yellow flow.

   * **Approved** (green flow)—The card is digitized.

   * **Conditional** (yellow flow)—The card is only digitized after cardholder's identity is verified.

   * **Not approved** (red flow)—The card is not digitized and the denial reason is sent to the network and issuer.

3. **OTP**—In the conditional flow, Pismo sends  a challenge to cardholder to confirm identity. This is known as OTP (One-Time Passcode).

4. **Token activated**—Once approved, the token is activated.

5. **Token update**—The network notify Pismo of  any token changes, such as a change in status.

The table below shows the operations and how the two main networks refer to them:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Token operation
      </th>

      <th>
        Mastercard (MDES)
      </th>

      <th>
        Visa (VTS)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Eligibility
      </td>

      <td>
        TE
      </td>

      <td>
        Check eligibility
      </td>
    </tr>

    <tr>
      <td>
        Authentication
      </td>

      <td>
        TA
      </td>

      <td>
        Approve provisioning

        Retrieve step-up methods
      </td>
    </tr>

    <tr>
      <td>
        OTP
      </td>

      <td>
        AC
      </td>

      <td>
        Send passcode
      </td>
    </tr>

    <tr>
      <td>
        Token activated
      </td>

      <td>
        TC
      </td>

      <td>
        Token create notification
      </td>
    </tr>

    <tr>
      <td>
        Update notification
      </td>

      <td>
        TV
      </td>

      <td>
        Token notification
      </td>
    </tr>
  </tbody>
</Table>

## Pismo provisioning refusal reasons

These appear in the tokenization events and are also detailed in the [anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#client-anti-fraud-webhook-for-card-tokenization) guide, but here are the possible Pismo reasons for refusing a tokenization request contained in the `custom_code` field:

* **998**  - Card Not Found
* **BNB**  - Card Other
* **CCS** - Card is in CANCELLED status
* **CED** - Invalid expiration date
* **CNF** - Config Not Found
* **CNN** - Card is not in `NORMAL` status
* **ELFR2** - Exceeded CVV2 validation tries
* **EXPCRD** - Expired card
* **FDR** - Failed Decrypt Request
* **FLE** - Generic refusal
* **FR1** - Failed CVV2 validation
* **FR2** - CVV2 is invalid
* **FRB** - `CREATED` status not allowed
* **FSC** - Fail Send Challenge
* **HSE** - HSM validation error
* **IRFD** - Invalid Request Fields
* **IRJD** - Invalid Request Json
* **MOT** - SMS Template not configured
* **NPL** - Virtual card not allowed
* **OP1** - Internal Error
* **PFT** - Anti Fraud Refusal
* **TNF** - Token Not Found
* **VNM** - Invalid card
* **WLB** - Card not in whitelist

# Tokenization events

The following are examples of events that occur during the card tokenization process. Except where noted, all of these are [Token provisioning request received](https://developers.pismo.io/events/docs/cards-tokenization-notification-1) event examples.

For information on setting up event notifications, refer to the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview) .

For information on interpreting event data from the network, refer to the [VISA Token Service (VTS) Issuer API Specifications (JSON) manual](https://developer.visa.com/capabilities/token-service-provisioning) or the [Mastercard Customer Interface Specification manual](https://www.scribd.com/doc/45861572/Customer-Interface-Specification).

## Mastercard Digital Enablement Service (MDES)

### MDES token authorization (TA) provisioning

**Important fields:**

* `network_data.de48_additional_data_private_user.se26_wallet_program_data.sf1_wallet_identifier`\
  Wallet identifier:\
  103 = apple pay\
  216 = google pay\
  217 = samsung pay\
  327 = merchant tokenization program

* `network_data.de124_member_defined_data.mdes_data.token_authorization.sf2_primary_account_number_source`\
  PAN source identifier:\
  1 = Card on file\
  2 = Card added manually\
  3 = Card added via application

<details>
  <summary>MDES TA example event</summary>

  ```json
  {
    "event_id": "b537543c-4aa7-4163-8566-4cc788b1390d",
    "domain": "cards-tokenization",
    "event_type": "notification",
    "schema_version": "1",
    "org_id": "TN-3a897b16-a18e-47bc-88d2-cf10fb0612b6",
    "cid": "8f4b0482-fac6-4433-8664-5db1523ad75c",
    "timestamp": "2020-12-10T22:36:56.098Z",
    "data": {
      "account_id": 100001185,
      "card_id": 4995608,
      "token_id": 17556,
      "network_call_method": "TA",
      "network_data": {
        "de3_processing_code": {
          "sf1_cardholder_transaction_type_code": "00",
          "sf2_cardholder_from_account_type_code": "00",
          "sf3_cardholder_to_account_type_code": "00"
        },
        "de4_amount_transaction": "000000000000",
        "de5_amount_settlement": "000000000000",
        "de6_amount_cardholder_billing": "000000000000",
        "de7_tranmission_date_and_time": {
          "sf1_date": "1210",
          "sf2_time": "223654"
        },
        "de9_conversion_rate_settlement": {
          "sf1_decimal_indicator": "6",
          "sf2_conversion_rate": "1000000"
        },
        "de10_conversion_rate_cardholder_billing": {
          "sf1_decimal_indicator": "6",
          "sf2_cardholderbilling_conversion_rate": "5178611"
        },
        "de11_stan": "019416",
        "de14_date_expiration": "2607",
        "de15_date_settlement": "1210",
        "de16_date_conversion": "1210",
        "de18_merchant_type": "5969",
        "de22_pos_entry_mode": {
          "sf1_pos_terminal_pan_entry_mode": "01",
          "sf2_pos_terminal_pin_entry_mode": "0"
        },
        "de28_amount_transaction_fee": {},
        "de29_amount_settlement_fee": {},
        "de30_amount_transaction_processing_fee": {},
        "de31_amount_settlement_processing_fee": {},
        "de32_acquiring_institution_id_code": "015611",
        "de37_retrieval_reference_number": {},
        "de42_card_acceptor_id_code": "CARD ACCPT IDC ",
        "de43_card_acceptor_name_location_for_all_transactions": {
          "sf1_card_acceptor_name": "Mastercard             ",
          "sf3_card_acceptor_city": "St. Louis     ",
          "sf5_card_acceptor_state_or_country_code": "MO "
        },
        "de48_additional_data_private_user": {
          "de48_tcc": "T",
          "de48_start": "194",
          "de48_size": "129",
          "de48SubElements": [
            "23",
            "26",
            "33",
            "82",
            "92",
            "56",
            "75",
            "71"
          ],
          "se11_key_exchange_block_data": {},
          "se13_mastercard_hosted_mobile_phone_top_up_request_data": {},
          "se15_authorization_system_advice_date_and_time": {},
          "se18_service_parameters": {},
          "se23_payment_initiation_channel": {
            "sf1_device_type": "21"
          },
          "se25_mastercard_cash_program_data": {},
          "se26_wallet_program_data": {
            "sf1_wallet_identifier": "216"
          },
          "se33_pan_mapping_file_information": {
            "sf1_account_number_indicator": "H",
            "sf6_token_requestor_id": "50120834693",
            "sf8_storage_technology": "01"
          },
          "se34_atc_information": {},
          "se36_visa_mmv": {},
          "se37_additional_merchant_data": {},
          "se40_eletronic_commerce_merchant_cardholder_certificate_serial_number": {},
          "se41_eletronic_commercer_certificate_qualifying_information": {},
          "se42_eletronic_commerce_indicator": {},
          "se43_ucaf": {},
          "se48_mobile_program_indicator": {},
          "se49_time_validation_information": {},
          "se51_merchant_on_behalf_services": {},
          "se55_merchant_fraud_scoring_data": {},
          "se56_security_services_additional_data_for_issuers": [
            {
              "sf1_security_services_indicator": "AIQ",
              "sf2_security_services_data": "5EZ"
            },
            {
              "sf1_security_services_indicator": "AQV",
              "sf2_security_services_data": "445"
            },
            {
              "sf1_security_services_indicator": "AQF",
              "sf2_security_services_data": "144"
            },
            {
              "sf1_security_services_indicator": "AQS",
              "sf2_security_services_data": "007"
            }
          ],
          "se57_security_services_additional_data_for_acquirers": {},
          "se58_atm_additional_data": {},
          "se61_pos_data_extended_condition_codes": {},
          "se64_transit_program": {},
          "se65_terminal_compliant_indicator": {},
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
            "sf1_fraud_score": "100",
            "sf2_score_reason_code": "R0",
            "sf3_rules_score": "200",
            "sf4_rules_reason_code1": "R1",
            "sf5_rules_reason_code2": "R2"
          },
          "se78_payment_service_indicator": {},
          "se79_chip_cvr_or_tvr_bit_error_results": {},
          "se82_address_verification_service_request": "52",
          "se87_card_validation_code_result_or_cvv2": "M",
          "se93_fleet_card_id_request_data": {}
        },
        "de49_currency_code_transaction": "840",
        "de50_currency_code_settlement": "840",
        "de51_currency_code_cardholder_billing": "986",
        "de60_advice_reason_code": {},
        "de61_pos_data": {
          "sf1_pos_terminal_attendance": "1",
          "sf2_reserved_for_future_use": "0",
          "sf3_pos_terminal_location": "2",
          "sf4_pos_cardholder_presence": "5",
          "sf5_pos_card_presence": "1",
          "sf6_pos_card_capture_capabilities": "0",
          "sf7_pos_transaction_status": "9",
          "sf8_pos_transaction_security": "0",
          "sf9_reserved_for_future_use": "0",
          "sf10_cardholder_activated_terminal_level": "0",
          "sf11_pos_card_data_terminal_input_capability_indicator": "0",
          "sf12_pos_authorization_life_cycle": "00",
          "sf13_pos_country_code_or_submerchant": "840",
          "sf14_postal_code_or_submerchant": "63368"
        },
        "de63_network_data": {
          "sf1_financial_network_code": "MPL",
          "sf2_banknet_reference_number": "C1WSOE"
        },
        "de90_original_data_elements": {},
        "de94_service_indicator": {},
        "de95_replacement_amounts": {},
        "de97_amount_net_settlement": {},
        "de112_additional_data_national_use": {},
        "de120_record_data": {
          "de120_start": "371",
          "de120_size": "033",
          "sf1_avs_service_indicator1": "04571090 Rua Teste           "
        },
        "de124_member_defined_data": {
          "mdes_data": {
            "sf1_message_type": "TA",
            "token_authorization": {
              "sf1_correlation_id": "D0000009418034",
              "sf2_primary_account_number_source": "2",
              "sf3_payment_application_instance_id": "I_Fdk0fO41xalfllEZl4Gq4jHiIKFPSwyn6BXBk4RzitgSMk",
              "sf4_device_source_ip": "FD8F4942    ",
              "sf5_wallet_provider_account_hash": "123CCB2F30BA420B89F9BD5E7151540EE44DDDB8B5140CDEA34AA61F625EF215",
              "sf6_cardholder_name": "Teste                      ",
              "sf7_wallet_provider_token_recomendation": "2",
              "sf8_wallet_provider_standard_token_recomendation": "01",
              "sf9_wallet_provider_device_score": "1",
              "sf10_wallet_provider_account_score": "4",
              "sf11_number_of_active_tokens": "02",
              "sf12_wallet_service_provider_reason_codes": "00080C",
              "sf13_device_location": "135E2B5D3",
              "sf14_mobile_last_4_digits": "    ",
              "sf15_token_type": "C"
            }
          }
        }
      }
    }
  }
  ```
</details>

### MDES activation code (AC)

The AC message brings a code from the network which we have to reply back to the user.

Event occurs if the user chooses the challenges `OTPSMS` or `OTPEMAIL`. If the user chooses other challenge methods (app-to-app `OTPAPP`, call center `OTPCALL`) the process takes place between the app/call center and the network.

**Important fields**

* `network_data.de124_member_defined_data.mdes_data.activation_code.sf2_activation_code`\
  Activation code that should be sent to the cardholder.

* `network_data.de124_member_defined_data.mdes_data.activation_code.sf3_activation_code_expiration_date_time`\
  Activation code expiration datetime

* `network_data.de124_member_defined_data.mdes_data.activation_code.sf4_consumer_activation_pref_method`\
  Authentication method choose by cardholder:\
  1 - otp SMS\
  2 - otp E-MAIL\
  3 - otp Call center\
  6 - otp APP to APP

<details>
  <summary> MDES AC example event</summary>

  ```json
    {
      "event_id": "82352f8e-aec5-42d1-940d-c39f3b683039",
      "domain": "cards-tokenization",
      "event_type": "notification",
      "schema_version": "1",
      "org_id": "TN-3a897b16-a18e-47bc-88d2-cf10fb0612b6",
      "cid": "5e7671c2-69cd-4554-9ca5-9f49bc11629a",
      "timestamp": "2020-12-10T22:37:27.933Z",
      "data": {
          "account_id": 100001185,
          "card_id": 4995608,
          "token_id": 17556,
          "network_call_method": "AC",
          "network_data": {
              "de3_processing_code": {
                  "sf1_cardholder_transaction_type_code": "00",
                  "sf2_cardholder_from_account_type_code": "00",
                  "sf3_cardholder_to_account_type_code": "00"
              },
              "de4_amount_transaction": "000000000000",
              "de5_amount_settlement": "000000000000",
              "de6_amount_cardholder_billing": "000000000000",
              "de7_tranmission_date_and_time": {
                  "sf1_date": "1210",
                  "sf2_time": "223727"
              },
              "de9_conversion_rate_settlement": {
                  "sf1_decimal_indicator": "6",
                  "sf2_conversion_rate": "1000000"
              },
              "de10_conversion_rate_cardholder_billing": {
                  "sf1_decimal_indicator": "6",
                  "sf2_cardholderbilling_conversion_rate": "5178611"
              },
              "de11_stan": "778092",
              "de14_date_expiration": "2607",
              "de15_date_settlement": "1210",
              "de16_date_conversion": "1210",
              "de18_merchant_type": "5969",
              "de22_pos_entry_mode": {
                  "sf1_pos_terminal_pan_entry_mode": "01",
                  "sf2_pos_terminal_pin_entry_mode": "0"
              },
              "de28_amount_transaction_fee": {},
              "de29_amount_settlement_fee": {},
              "de30_amount_transaction_processing_fee": {},
              "de31_amount_settlement_processing_fee": {},
              "de32_acquiring_institution_id_code": "015611",
              "de37_retrieval_reference_number": {},
              "de42_card_acceptor_id_code": "CARD ACCPT IDC ",
              "de43_card_acceptor_name_location_for_all_transactions": {
                  "sf1_card_acceptor_name": "Mastercard             ",
                  "sf3_card_acceptor_city": "St. Louis     ",
                  "sf5_card_acceptor_state_or_country_code": "MO "
              },
              "de48_additional_data_private_user": {
                  "de48_tcc": "T",
                  "de48_start": "194",
                  "de48_size": "110",
                  "de48SubElements": [
                      "23",
                      "26",
                      "33",
                      "56",
                      "75",
                      "71"
                  ],
                  "se11_key_exchange_block_data": {},
                  "se13_mastercard_hosted_mobile_phone_top_up_request_data": {},
                  "se15_authorization_system_advice_date_and_time": {},
                  "se18_service_parameters": {},
                  "se23_payment_initiation_channel": {
                      "sf1_device_type": "21"
                  },
                  "se25_mastercard_cash_program_data": {},
                  "se26_wallet_program_data": {
                      "sf1_wallet_identifier": "216"
                  },
                  "se33_pan_mapping_file_information": {
                      "sf1_account_number_indicator": "H",
                      "sf6_token_requestor_id": "50120834693"
                  },
                  "se34_atc_information": {},
                  "se36_visa_mmv": {},
                  "se37_additional_merchant_data": {},
                  "se40_eletronic_commerce_merchant_cardholder_certificate_serial_number": {},
                  "se41_eletronic_commercer_certificate_qualifying_information": {},
                  "se42_eletronic_commerce_indicator": {},
                  "se43_ucaf": {},
                  "se48_mobile_program_indicator": {},
                  "se49_time_validation_information": {},
                  "se51_merchant_on_behalf_services": {},
                  "se55_merchant_fraud_scoring_data": {},
                  "se56_security_services_additional_data_for_issuers": [
                      {
                          "sf1_security_services_indicator": "AIQ",
                          "sf2_security_services_data": "5EZ"
                      },
                      {
                          "sf1_security_services_indicator": "AQV",
                          "sf2_security_services_data": "445"
                      },
                      {
                          "sf1_security_services_indicator": "AQF",
                          "sf2_security_services_data": "144"
                      },
                      {
                          "sf1_security_services_indicator": "AQS",
                          "sf2_security_services_data": "007"
                      }
                  ],
                  "se57_security_services_additional_data_for_acquirers": {},
                  "se58_atm_additional_data": {},
                  "se61_pos_data_extended_condition_codes": {},
                  "se64_transit_program": {},
                  "se65_terminal_compliant_indicator": {},
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
                      "sf1_fraud_score": "100",
                      "sf2_score_reason_code": "R0",
                      "sf3_rules_score": "200",
                      "sf4_rules_reason_code1": "R1",
                      "sf5_rules_reason_code2": "R2"
                  },
                  "se78_payment_service_indicator": {},
                  "se79_chip_cvr_or_tvr_bit_error_results": {},
                  "se93_fleet_card_id_request_data": {}
              },
              "de49_currency_code_transaction": "840",
              "de50_currency_code_settlement": "840",
              "de51_currency_code_cardholder_billing": "986",
              "de60_advice_reason_code": {},
              "de61_pos_data": {
                  "sf1_pos_terminal_attendance": "1",
                  "sf2_reserved_for_future_use": "0",
                  "sf3_pos_terminal_location": "2",
                  "sf4_pos_cardholder_presence": "5",
                  "sf5_pos_card_presence": "1",
                  "sf6_pos_card_capture_capabilities": "0",
                  "sf7_pos_transaction_status": "9",
                  "sf8_pos_transaction_security": "0",
                  "sf9_reserved_for_future_use": "0",
                  "sf10_cardholder_activated_terminal_level": "0",
                  "sf11_pos_card_data_terminal_input_capability_indicator": "0",
                  "sf12_pos_authorization_life_cycle": "00",
                  "sf13_pos_country_code_or_submerchant": "840",
                  "sf14_postal_code_or_submerchant": "63368"
              },
              "de63_network_data": {
                  "sf1_financial_network_code": "MPL",
                  "sf2_banknet_reference_number": "C112OE"
              },
              "de90_original_data_elements": {},
              "de94_service_indicator": {},
              "de95_replacement_amounts": {},
              "de97_amount_net_settlement": {},
              "de112_additional_data_national_use": {},
              "de120_record_data": {},
              "de124_member_defined_data": {
                  "mdes_data": {
                      "sf1_message_type": "AC",
                      "activation_code": {
                          "sf1_correlation_id": "D0000009418034",
                          "sf2_activation_code": "523894  ",
                          "sf3_activation_code_expiration_date_time": "2012102307",
                          "sf4_consumer_activation_pref_method": "1(###)###7728"
                      }
                  }
              },
              "start": 1607639847750012370,
              "card_profile": "          "
          }
      }
  }
  ```
</details>

### MDES tokenization complete (TC)

Indicates the network has provisioned the token. This is when the token becomes active and can be used in a tokenized transaction

**Important fields**

* `network_data.de124_member_defined_data.mdes_data.tokenization_complete.sf2_number_of_active_tokens`

  Identify total activated tokens

* `network_data.de124_member_defined_data.mdes_data.tokenization_complete.sf4_device_name`

  Device name

<details>
  <summary>MDES TC example event</summary>

  ```json
  {
      "event_id": "7e67766b-df74-41b8-8d5f-96f918752873",
      "domain": "cards-tokenization",
      "event_type": "notification",
      "schema_version": "1",
      "org_id": "TN-3a897b16-a18e-47bc-88d2-cf10fb0612b6",
      "cid": "290f392a-2e14-422e-9646-cfc68c0ff154",
      "timestamp": "2020-12-10T22:37:57.342Z",
      "data": {
          "account_id": 100001185,
          "card_id": 4995608,
          "token_id": 17556,
          "network_call_method": "TC",
          "network_data": {
              "de3_processing_code": {
                  "sf1_cardholder_transaction_type_code": "00",
                  "sf2_cardholder_from_account_type_code": "00",
                  "sf3_cardholder_to_account_type_code": "00"
              },
              "de4_amount_transaction": "000000000000",
              "de5_amount_settlement": "000000000000",
              "de6_amount_cardholder_billing": "000000000000",
              "de7_tranmission_date_and_time": {
                  "sf1_date": "1210",
                  "sf2_time": "223756"
              },
              "de9_conversion_rate_settlement": {
                  "sf1_decimal_indicator": "6",
                  "sf2_conversion_rate": "1000000"
              },
              "de10_conversion_rate_cardholder_billing": {
                  "sf1_decimal_indicator": "6",
                  "sf2_cardholderbilling_conversion_rate": "5178611"
              },
              "de11_stan": "619104",
              "de14_date_expiration": "2607",
              "de15_date_settlement": "1210",
              "de16_date_conversion": "1210",
              "de18_merchant_type": "5969",
              "de22_pos_entry_mode": {
                  "sf1_pos_terminal_pan_entry_mode": "01",
                  "sf2_pos_terminal_pin_entry_mode": "0"
              },
              "de28_amount_transaction_fee": {},
              "de29_amount_settlement_fee": {},
              "de30_amount_transaction_processing_fee": {},
              "de31_amount_settlement_processing_fee": {},
              "de32_acquiring_institution_id_code": "015611",
              "de37_retrieval_reference_number": {},
              "de42_card_acceptor_id_code": "CARD ACCPT IDC ",
              "de43_card_acceptor_name_location_for_all_transactions": {
                  "sf1_card_acceptor_name": "Mastercard             ",
                  "sf3_card_acceptor_city": "St. Louis     ",
                  "sf5_card_acceptor_state_or_country_code": "MO "
              },
              "de48_additional_data_private_user": {
                  "de48_tcc": "T",
                  "de48_start": "194",
                  "de48_size": "144",
                  "de48SubElements": [
                      "23",
                      "26",
                      "33",
                      "56",
                      "75",
                      "71"
                  ],
                  "se11_key_exchange_block_data": {},
                  "se13_mastercard_hosted_mobile_phone_top_up_request_data": {},
                  "se15_authorization_system_advice_date_and_time": {},
                  "se18_service_parameters": {},
                  "se23_payment_initiation_channel": {
                      "sf1_device_type": "21"
                  },
                  "se25_mastercard_cash_program_data": {},
                  "se26_wallet_program_data": {
                      "sf1_wallet_identifier": "216"
                  },
                  "se33_pan_mapping_file_information": {
                      "sf1_account_number_indicator": "H",
                      "sf3_expiration_date": "2401",
                      "sf6_token_requestor_id": "50120834693",
                      "sf8_storage_technology": "01"
                  },
                  "se34_atc_information": {},
                  "se36_visa_mmv": {},
                  "se37_additional_merchant_data": {},
                  "se40_eletronic_commerce_merchant_cardholder_certificate_serial_number": {},
                  "se41_eletronic_commercer_certificate_qualifying_information": {},
                  "se42_eletronic_commerce_indicator": {},
                  "se43_ucaf": {},
                  "se48_mobile_program_indicator": {},
                  "se49_time_validation_information": {},
                  "se51_merchant_on_behalf_services": {},
                  "se55_merchant_fraud_scoring_data": {},
                  "se56_security_services_additional_data_for_issuers": [
                      {
                          "sf1_security_services_indicator": "AIQ",
                          "sf2_security_services_data": "5EZ"
                      },
                      {
                          "sf1_security_services_indicator": "AQV",
                          "sf2_security_services_data": "445"
                      },
                      {
                          "sf1_security_services_indicator": "AQF",
                          "sf2_security_services_data": "144"
                      },
                      {
                          "sf1_security_services_indicator": "AQS",
                          "sf2_security_services_data": "007"
                      }
                  ],
                  "se57_security_services_additional_data_for_acquirers": {},
                  "se58_atm_additional_data": {},
                  "se61_pos_data_extended_condition_codes": {},
                  "se64_transit_program": {},
                  "se65_terminal_compliant_indicator": {},
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
                      "sf1_fraud_score": "100",
                      "sf2_score_reason_code": "R0",
                      "sf3_rules_score": "200",
                      "sf4_rules_reason_code1": "R1",
                      "sf5_rules_reason_code2": "R2"
                  },
                  "se78_payment_service_indicator": {},
                  "se79_chip_cvr_or_tvr_bit_error_results": {},
                  "se93_fleet_card_id_request_data": {}
              },
              "de49_currency_code_transaction": "840",
              "de50_currency_code_settlement": "840",
              "de51_currency_code_cardholder_billing": "986",
              "de56_payment_account_data": "013301295001847TESXGZ22AAJD0O5UNXUWQ8",
              "de60_advice_reason_code": {},
              "de61_pos_data": {
                  "sf1_pos_terminal_attendance": "1",
                  "sf2_reserved_for_future_use": "0",
                  "sf3_pos_terminal_location": "2",
                  "sf4_pos_cardholder_presence": "5",
                  "sf5_pos_card_presence": "1",
                  "sf6_pos_card_capture_capabilities": "0",
                  "sf7_pos_transaction_status": "9",
                  "sf8_pos_transaction_security": "0",
                  "sf9_reserved_for_future_use": "0",
                  "sf10_cardholder_activated_terminal_level": "0",
                  "sf11_pos_card_data_terminal_input_capability_indicator": "0",
                  "sf12_pos_authorization_life_cycle": "00",
                  "sf13_pos_country_code_or_submerchant": "840",
                  "sf14_postal_code_or_submerchant": "63368"
              },
              "de63_network_data": {
                  "sf1_financial_network_code": "MPL",
                  "sf2_banknet_reference_number": "C16LOE"
              },
              "de90_original_data_elements": {},
              "de94_service_indicator": {},
              "de95_replacement_amounts": {},
              "de97_amount_net_settlement": {},
              "de112_additional_data_national_use": {},
              "de120_record_data": {},
              "de124_member_defined_data": {
                  "mdes_data": {
                      "sf1_message_type": "TC",
                      "tokenization_complete": {
                          "sf1_correlation_id": "D0000009418034",
                          "sf2_number_of_active_tokens": "03",
                          "sf3_issuer_product_conf_id": "BTGMCPLAT ",
                          "sf3_consumer_language": "en",
                          "sf4_device_name": "!samsung!samsung!SM-",
                          "sf5_final_token_decision": "2",
                          "sf6_final_token_decision_indicator": "2",
                          "sf7_tc_indicator": "3b65cc85292b471b8225a78685a62d86",
                          "sf8_tc_date_time": "2012102236",
                          "sf9_number_of_activation_attemps": "1",
                          "sf10_token_unique_ref": "DSHRMC0000259339fc95457145a841599b4b25b6c1da653e",
                          "sf11_pan_unique_ref": "FSHRMC00002593398d3715eb2b0b4189b07e0853c37fe073",
                          "sf12_token_type": "C"
                      }
                  }
              }
          }
      }
  }
  ```
</details>

### MDES TV (tokenization event)

Token lifecycle messages, such as token status changes. The network can send, for example, a token cancellation of a token.

**Important fields**

* `network_data.de124_member_defined_data.mdes_data.tokenization_event_notification.sf2_event_indicator`

  Lifecycle event type:\
  3 = Deleted token\
  4 = Deleted from consumer device\
  7 = Resumed token\
  9 = Token replaced

* `network_data.de124_member_defined_data.mdes_data.tokenization_event_notification.sf4_event_requestor`

  Agent that started the tokenization provisioning:\
  0 = Wallet\
  1 = Funding account\
  2 = Cardholder\
  3 = Systematically

<details>
  <summary>MDES TV example event</summary>

  ```json
  {
      "event_id": "cd5fa2c5-5a3e-4fc7-96db-41abf848b5ab",
      "domain": "cards-tokenization",
      "event_type": "notification",
      "schema_version": "1",
      "org_id": "TN-3a897b16-a18e-47bc-88d2-cf10fb0612b6",
      "cid": "9aa65e4a-cece-4f54-a568-43473e14e9c2",
      "timestamp": "2020-12-10T22:41:32.203Z",
      "data": {
          "account_id": 100001185,
          "card_id": 4995608,
          "token_id": 17556,
          "network_call_method": "TV",
          "network_data": {
              "de3_processing_code": {
                  "sf1_cardholder_transaction_type_code": "00",
                  "sf2_cardholder_from_account_type_code": "00",
                  "sf3_cardholder_to_account_type_code": "00"
              },
              "de4_amount_transaction": "000000000000",
              "de5_amount_settlement": "000000000000",
              "de6_amount_cardholder_billing": "000000000000",
              "de7_tranmission_date_and_time": {
                  "sf1_date": "1210",
                  "sf2_time": "224131"
              },
              "de9_conversion_rate_settlement": {
                  "sf1_decimal_indicator": "6",
                  "sf2_conversion_rate": "1000000"
              },
              "de10_conversion_rate_cardholder_billing": {
                  "sf1_decimal_indicator": "6",
                  "sf2_cardholderbilling_conversion_rate": "5178611"
              },
              "de11_stan": "422542",
              "de14_date_expiration": "2607",
              "de15_date_settlement": "1210",
              "de16_date_conversion": "1210",
              "de18_merchant_type": "5969",
              "de22_pos_entry_mode": {
                  "sf1_pos_terminal_pan_entry_mode": "01",
                  "sf2_pos_terminal_pin_entry_mode": "0"
              },
              "de28_amount_transaction_fee": {},
              "de29_amount_settlement_fee": {},
              "de30_amount_transaction_processing_fee": {},
              "de31_amount_settlement_processing_fee": {},
              "de32_acquiring_institution_id_code": "015611",
              "de37_retrieval_reference_number": {},
              "de42_card_acceptor_id_code": "CARD ACCPT IDC ",
              "de43_card_acceptor_name_location_for_all_transactions": {
                  "sf1_card_acceptor_name": "Mastercard             ",
                  "sf3_card_acceptor_city": "St. Louis     ",
                  "sf5_card_acceptor_state_or_country_code": "MO "
              },
              "de48_additional_data_private_user": {
                  "de48_tcc": "T",
                  "de48_start": "194",
                  "de48_size": "138",
                  "de48SubElements": [
                      "23",
                      "26",
                      "33",
                      "56",
                      "75",
                      "71"
                  ],
                  "se11_key_exchange_block_data": {},
                  "se13_mastercard_hosted_mobile_phone_top_up_request_data": {},
                  "se15_authorization_system_advice_date_and_time": {},
                  "se18_service_parameters": {},
                  "se23_payment_initiation_channel": {
                      "sf1_device_type": "21"
                  },
                  "se25_mastercard_cash_program_data": {},
                  "se26_wallet_program_data": {
                      "sf1_wallet_identifier": "216"
                  },
                  "se33_pan_mapping_file_information": {
                      "sf1_account_number_indicator": "H",
                      "sf3_expiration_date": "2401",
                      "sf6_token_requestor_id": "50120834693"
                  },
                  "se34_atc_information": {},
                  "se36_visa_mmv": {},
                  "se37_additional_merchant_data": {},
                  "se40_eletronic_commerce_merchant_cardholder_certificate_serial_number": {},
                  "se41_eletronic_commercer_certificate_qualifying_information": {},
                  "se42_eletronic_commerce_indicator": {},
                  "se43_ucaf": {},
                  "se48_mobile_program_indicator": {},
                  "se49_time_validation_information": {},
                  "se51_merchant_on_behalf_services": {},
                  "se55_merchant_fraud_scoring_data": {},
                  "se56_security_services_additional_data_for_issuers": [
                      {
                          "sf1_security_services_indicator": "AIQ",
                          "sf2_security_services_data": "5EZ"
                      },
                      {
                          "sf1_security_services_indicator": "AQV",
                          "sf2_security_services_data": "445"
                      },
                      {
                          "sf1_security_services_indicator": "AQF",
                          "sf2_security_services_data": "144"
                      },
                      {
                          "sf1_security_services_indicator": "AQS",
                          "sf2_security_services_data": "007"
                      }
                  ],
                  "se57_security_services_additional_data_for_acquirers": {},
                  "se58_atm_additional_data": {},
                  "se61_pos_data_extended_condition_codes": {},
                  "se64_transit_program": {},
                  "se65_terminal_compliant_indicator": {},
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
                      "sf1_fraud_score": "100",
                      "sf2_score_reason_code": "R0",
                      "sf3_rules_score": "200",
                      "sf4_rules_reason_code1": "R1",
                      "sf5_rules_reason_code2": "R2"
                  },
                  "se78_payment_service_indicator": {},
                  "se79_chip_cvr_or_tvr_bit_error_results": {},
                  "se93_fleet_card_id_request_data": {}
              },
              "de49_currency_code_transaction": "840",
              "de50_currency_code_settlement": "840",
              "de51_currency_code_cardholder_billing": "986",
              "de60_advice_reason_code": {},
              "de61_pos_data": {
                  "sf1_pos_terminal_attendance": "1",
                  "sf2_reserved_for_future_use": "0",
                  "sf3_pos_terminal_location": "2",
                  "sf4_pos_cardholder_presence": "5",
                  "sf5_pos_card_presence": "1",
                  "sf6_pos_card_capture_capabilities": "0",
                  "sf7_pos_transaction_status": "9",
                  "sf8_pos_transaction_security": "0",
                  "sf9_reserved_for_future_use": "0",
                  "sf10_cardholder_activated_terminal_level": "0",
                  "sf11_pos_card_data_terminal_input_capability_indicator": "0",
                  "sf12_pos_authorization_life_cycle": "00",
                  "sf13_pos_country_code_or_submerchant": "840",
                  "sf14_postal_code_or_submerchant": "63368"
              },
              "de63_network_data": {
                  "sf1_financial_network_code": "MPL",
                  "sf2_banknet_reference_number": "C23WOE"
              },
              "de90_original_data_elements": {},
              "de94_service_indicator": {},
              "de95_replacement_amounts": {},
              "de97_amount_net_settlement": {},
              "de112_additional_data_national_use": {},
              "de120_record_data": {},
              "de124_member_defined_data": {
                  "mdes_data": {
                      "sf1_message_type": "TV",
                      "tokenization_event_notification": {
                          "sf1_correlation_id": "D0000009418034",
                          "sf2_event_indicator": "3",
                          "sf3_event_reason_code": "  ",
                          "sf4_event_requestor": "2"
                      }
                  }
              },
              "start": 160760000000006,
              "card_profile": "          "
          }
      }
  }
  ```
</details>

### MDES TE refusal

Event: [notification\_refusal-1](https://developers.pismo.io/events/docs/cards-tokenization-notification-refusal-1)

**Important fields**

* `custom_codes[]` - Array of codes from Pismo indicating reasons for rejection. Refer to [Third-party wallets (such as Apple Pay)](https://developers.pismo.io/pismo-docs/docs/third-party-wallets#anti-fraud-webhook-request)  for list of codes.

<details>
  <summary>MDES TE refusal example event</summary>

  ```json
  {
      "event_id": "e21be45e-39a6-4909-8dec-2d6cadafe2b9",
      "domain": "cards-tokenization",
      "event_type": "notification_refusal",
      "schema_version": "1",
      "org_id": "TN-3a897b16-a18e-47bc-88d2-cf10fb0612b6",
      "cid": "c562dd34-7f76-4bad-8797-fbd392085634",
      "timestamp": "2021-02-09T18:13:16.375Z",
      "data": {
          "account_id": 100001185,
          "card_id": 4995608,
          "token_id": null,
          "network_call_method": "TE",
          "custom_codes": [
              "BNR"
          ],
          "network_data": {
              "de3_processing_code": {
                  "sf1_cardholder_transaction_type_code": "00",
                  "sf2_cardholder_from_account_type_code": "00",
                  "sf3_cardholder_to_account_type_code": "00"
              },
              "de4_amount_transaction": "000000000000",
              "de5_amount_settlement": "000000000000",
              "de6_amount_cardholder_billing": "000000000000",
              "de7_tranmission_date_and_time": {
                  "sf1_date": "0209",
                  "sf2_time": "181316"
              },
              "de9_conversion_rate_settlement": {
                  "sf1_decimal_indicator": "6",
                  "sf2_conversion_rate": "1000000"
              },
              "de10_conversion_rate_cardholder_billing": {
                  "sf1_decimal_indicator": "6",
                  "sf2_cardholderbilling_conversion_rate": "5418830"
              },
              "de11_stan": "115186",
              "de14_date_expiration": "2607",
              "de15_date_settlement": "0209",
              "de16_date_conversion": "0208",
              "de18_merchant_type": "5969",
              "de22_pos_entry_mode": {
                  "sf1_pos_terminal_pan_entry_mode": "01",
                  "sf2_pos_terminal_pin_entry_mode": "0"
              },
              "de28_amount_transaction_fee": {},
              "de29_amount_settlement_fee": {},
              "de30_amount_transaction_processing_fee": {},
              "de31_amount_settlement_processing_fee": {},
              "de32_acquiring_institution_id_code": "015611",
              "de37_retrieval_reference_number": {},
              "de42_card_acceptor_id_code": "CARD ACCPT IDC ",
              "de43_card_acceptor_name_location_for_all_transactions": {
                  "sf1_card_acceptor_name": "Mastercard             ",
                  "sf3_card_acceptor_city": "St. Louis     ",
                  "sf5_card_acceptor_state_or_country_code": "MO "
              },
              "de48_additional_data_private_user": {
                  "de48_tcc": "T",
                  "de48_start": "194",
                  "de48_size": "116",
                  "de48SubElements": [
                      "23",
                      "26",
                      "33",
                      "56",
                      "75",
                      "71"
                  ],
                  "se11_key_exchange_block_data": {},
                  "se13_mastercard_hosted_mobile_phone_top_up_request_data": {},
                  "se15_authorization_system_advice_date_and_time": {},
                  "se18_service_parameters": {},
                  "se23_payment_initiation_channel": {
                      "sf1_device_type": "21"
                  },
                  "se25_mastercard_cash_program_data": {},
                  "se26_wallet_program_data": {
                      "sf1_wallet_identifier": "216"
                  },
                  "se33_pan_mapping_file_information": {
                      "sf1_account_number_indicator": "H",
                      "sf6_token_requestor_id": "50120834693",
                      "sf8_storage_technology": "01"
                  },
                  "se34_atc_information": {},
                  "se36_visa_mmv": {},
                  "se37_additional_merchant_data": {},
                  "se40_eletronic_commerce_merchant_cardholder_certificate_serial_number": {},
                  "se41_eletronic_commercer_certificate_qualifying_information": {},
                  "se42_eletronic_commerce_indicator": {},
                  "se43_ucaf": {},
                  "se48_mobile_program_indicator": {},
                  "se49_time_validation_information": {},
                  "se51_merchant_on_behalf_services": {},
                  "se55_merchant_fraud_scoring_data": {},
                  "se56_security_services_additional_data_for_issuers": [
                      {
                          "sf1_security_services_indicator": "AIQ",
                          "sf2_security_services_data": "5EZ"
                      },
                      {
                          "sf1_security_services_indicator": "AQV",
                          "sf2_security_services_data": "445"
                      },
                      {
                          "sf1_security_services_indicator": "AQF",
                          "sf2_security_services_data": "144"
                      },
                      {
                          "sf1_security_services_indicator": "AQS",
                          "sf2_security_services_data": "007"
                      }
                  ],
                  "se57_security_services_additional_data_for_acquirers": {},
                  "se58_atm_additional_data": {},
                  "se61_pos_data_extended_condition_codes": {},
                  "se64_transit_program": {},
                  "se65_terminal_compliant_indicator": {},
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
                      "sf1_fraud_score": "100",
                      "sf2_score_reason_code": "R0",
                      "sf3_rules_score": "200",
                      "sf4_rules_reason_code1": "R1",
                      "sf5_rules_reason_code2": "R2"
                  },
                  "se78_payment_service_indicator": {},
                  "se79_chip_cvr_or_tvr_bit_error_results": {},
                  "se93_fleet_card_id_request_data": {}
              },
              "de49_currency_code_transaction": "840",
              "de50_currency_code_settlement": "840",
              "de51_currency_code_cardholder_billing": "986",
              "de60_advice_reason_code": {},
              "de61_pos_data": {
                  "sf1_pos_terminal_attendance": "1",
                  "sf2_reserved_for_future_use": "0",
                  "sf3_pos_terminal_location": "2",
                  "sf4_pos_cardholder_presence": "5",
                  "sf5_pos_card_presence": "1",
                  "sf6_pos_card_capture_capabilities": "0",
                  "sf7_pos_transaction_status": "9",
                  "sf8_pos_transaction_security": "0",
                  "sf9_reserved_for_future_use": "0",
                  "sf10_cardholder_activated_terminal_level": "0",
                  "sf11_pos_card_data_terminal_input_capability_indicator": "0",
                  "sf12_pos_authorization_life_cycle": "00",
                  "sf13_pos_country_code_or_submerchant": "840",
                  "sf14_postal_code_or_submerchant": "63368"
              },
              "de63_network_data": {
                  "sf1_financial_network_code": "MPL",
                  "sf2_banknet_reference_number": "QRV7O0"
              },
              "de90_original_data_elements": {},
              "de94_service_indicator": {},
              "de95_replacement_amounts": {},
              "de97_amount_net_settlement": {},
              "de112_additional_data_national_use": {},
              "de120_record_data": {},
              "de124_member_defined_data": {
                  "mdes_data": {
                      "sf1_message_type": "TE",
                      "token_eligibility": {
                          "sf1_correlation_id": "D0000009790684",
                          "sf2_primary_account_number_source": "2",
                          "sf3_payment_application_instance_id": "2ph-0sOsCvQcvxrLpYbCdm3WuLtLinwXfhvbZxgOa6bWYJ0h",
                          "sf4_number_of_active_tokens": "03",
                          "sf5_wallet_provider_account_hash": "                                                                ",
                          "sf6_cardholder_name": "                           ",
                          "sf7_token_type": "C"
                      }
                  }
              },
              "start": 161289000000000,
              "card_profile": "          ",
              "messageType": "TE",
              "correlationId": "",
              "panSource": null,
              "paymentApplicationInstanceId": "",
              "numberOfActiveTokens": "0",
              "walletProviderAccountHash": "",
              "cardholderName": "",
              "tokenType": null,
              "token": "",
              "numberOfActivationAttempts": "",
              "finalTokenDecision": "",
              "tcIdentifier": "",
              "tcDateTime": "",
              "tokenUniqueRef": "",
              "panUniqueRef": "",
              "expiryDate": "",
              "eventIndicator": null,
              "eventReasonCode": null,
              "eventRequestor": "",
              "last4MobileDigits": "",
              "deviceLocation": "",
              "activationCode": "",
              "activationCodeExpiration": "",
              "preferencialActivationMethod": ""
          }
      }
  }
  ```
</details>

## Visa Token Service (VTS)

### VTS token create

<details>
  <summary>VTS token create example</summary>

  ```json
  {
        "event_id": "17dd5566-e354-4045-ac9c-99999999999",
        "id": "17dd5566-e354-4045-ac9c-9999999999",
        "schema_version": "1",
        "domain": "cards-tokenization",
        "event_type": "notification",
        "org_id": "TN-9ba58591-7cf3-43bd-8501-9999999999",
        "cid": "c63fd719-7153-4410-abd3-9999999999",
        "timestamp": "2026-07-15T16:24:53.77Z",
        "data": {
            "card_id": 123,
            "token_id": 515,
            "account_id": 9,
            "program_id": 7,
            "token_status": "ACTIVE",
            "token": "4118820300000000",
            "network_data": {
                "actionCode": "00",
                "cardholderInfo": {
                    "billingAddress": {},
                    "expirationDate": {
                        "month": "06",
                        "year": "2031"
                    },
                    "highValueCustomer": false,
                    "name": "John Doe",
                    "primaryAccountNumber": "*****"
                },
                "clientWalletAccountID": "753A429999999999",
                "cvv2ResultsCode": "M",
                "dateTimeOfEvent": "2026-07-15T16:24:52Z",
                "deviceInfo": {
                    "deviceID": "043D109B7C239002429900642532838203D93E9999999999",
                    "deviceIPAddressV4": "223.181.58.14",
                    "deviceLanguageCode": "eng",
                    "deviceName": "abcde25lICgyKQ..",
                    "deviceNumber": "9999999999",
                    "deviceType": "MOBILE_PHONE"
                },
                "encryptedData": "*****",
                "eventType": "TOKEN_CREATED",
                "lifeCycleTraceID": 306199999999999,
                "messageReasonCode": "TOKEN_CREATED",
                "panReferenceID": "V-3426034595279999999999",
                "panSource": "MOBILE_BANKING_APP",
                "paymentAccountReference": "V0010014625218501359999999999",
                "riskInformation": {
                    "accountHolderName": "John Doe",
                    "visaTokenDecisioning": "85",
                    "visaTokenScore": "15",
                    "walletAccountEmailAddressAge": "330",
                    "walletProviderAccountScore": "3",
                    "walletProviderDeviceScore": "3",
                    "walletProviderReasonCodes": "03,0D,0E,0G",
                    "walletProviderRiskAssessment": "0",
                    "walletProviderRiskAssessmentVersion": "0002.00"
                },
                "termsAndConditions": {
                    "date": "2026-07-15T16:24:51.924+00:00",
                    "id": "84948a15901fe11a9069999999999"
                },
                "tokenInfo": {
                    "numberOfActiveTokensForPAN": 1,
                    "numberOfInactiveTokensForPAN": 0,
                    "numberOfSuspendedTokensForPAN": 0,
                    "token": "4118820300000000",
                    "tokenAssuranceMethod": "14",
                    "tokenExpirationDate": {
                        "month": "12",
                        "year": "2031"
                    },
                    "tokenStatus": "ACTIVE",
                    "tokenType": "SECURE_ELEMENT"
                },
                "tokenReferenceID": "DNITHE302619999999999",
                "tokenRequestorID": "40010030273",
                "walletAccountEmailAddressHash": "753A428D8E529369EC83C5977FE2F3AA81D1D43646C74431FC7219999999999"
            },
            "network_event_out_of_order": false,
            "pismo_response": null,
            "send_challenge": null,
            "network_call_method": "VTS_TOKEN_CREATED",
            "bin": "",
            "token_requestor_id": "40010030273",
            "token_unique_reference": "DNITHE3026181509999999999"
        },
        "_rid": "QjJ7AJUtmBBBBBBAAAAAAA==",
        "_self": "dbs/QjJ7AA==/colls/QjJ7AJUtmo4=/docs/QjJ7AJUtmoBBBBBBAAAAAAA==/",
        "_etag": "\"6503169f-0000-1100-0000-000000000000\"",
        "_attachments": "attachments/",
        "_ts": 1784132695
    }
  ```
</details>

### VTS approve provisioning

**Important fields**

* `deviceInfo.deviceBrand`

  Identify device’s brand

* `panSource`

  Identify PAN source

<details>
  <summary>VTS approve example event</summary>

  ```json
   {
      "event_id": "56c9db26-94b9-4d86-9c2f-aabffbe8eba6",
      "domain": "cards-tokenization",
      "event_type": "notification",
      "timestamp": "2020-12-19T12:37:31.837Z",
      "data": {
          "card_id": 5271995,
          "token_id": 17579,
          "network_data": {
              "cardholderInfo": {
                  "billingAddress": {},
                  "cvv2": "*****",
                  "expirationDate": {
                      "month": "11",
                      "year": "2026"
                  },
                  "highValueCustomer": false,
                  "name": "Daniel Kanczuk",
                  "primaryAccountNumber": "*****",
                  "riskAssessmentScore": "9"
              },
              "clientWalletAccountID": "hWg9hRxCSOCCBm1qiXFxZQ",
              "cvv2ResultsCode": "M",
              "deviceInfo": {
                  "deviceBrand": "samsung",
                  "deviceID": "MTUwMjIyMDEwNjAwMzA3MDUz",
                  "deviceIDType": "Derived",
                  "deviceIPAddressV4": "189.121.201.167",
                  "deviceLanguageCode": "eng",
                  "deviceLocation": "-19.9388/-43.9327",
                  "deviceManufacturer": "samsung",
                  "deviceModel": "SM-G928G",
                  "deviceName": "R2FsYXh5IFM2IGVkZ2Ur",
                  "deviceType": "MOBILE_PHONE",
                  "locationSource": "GPS",
                  "osBuildID": "G928GUBU5CSJ2",
                  "osType": "ANDROID",
                  "osVersion": "7.0",
                  "tokenProtectionMethod": "TRUSTED_EXECUTION_ENVIRONMENT"
              },
              "encryptedData": "*****",
              "lifeCycleTraceID": 87373737,
              "panReferenceID": "V-00000000089935214",
              "panSource": "KEY_ENTERED",
              "riskInformation": {
                  "accountHolderName": "Daniel Kanczuk",
                  "accountToDeviceBindingAge": "65",
                  "activeTokensOnAllDeviceForAccount": "0",
                  "daysSinceConsumerDataLastAccountChange": "0",
                  "daysSinceLastAccountActivity": "0",
                  "deviceBluetoothMac": "02:00:00:00:00:00",
                  "deviceCountry": "BR",
                  "deviceSerialNumber": "8425434b344e3034",
                  "deviceTimeZoneSetting": "NETWORK_SET",
                  "deviceWithActiveTokens": "0",
                  "distinctCardholderNames": "1",
                  "numberOfActiveTokens": "0",
                  "numberOfTransactionsInLast12months": "0",
                  "provisioningAttemptsOnDeviceIn24Hours": "3",
                  "riskAssessmentScore": "9",
                  "simSerialNumber": "8425434b344e3034",
                  "suspendedCardsInAccount": "0",
                  "userAccountAge": "1105",
                  "visaTokenDecisioning": "00",
                  "visaTokenScore": "08",
                  "walletAccountAge": "65",
                  "walletAccountCountry": "BR",
                  "walletProviderAccountScore": "3",
                  "walletProviderDeviceScore": "3",
                  "walletProviderPANAge": "31",
                  "walletProviderReasonCodes": "AC,A0"
              },
              "tokenInfo": {
                  "numberOfActiveTokensForPAN": 1,
                  "numberOfInactiveTokensForPAN": 0,
                  "numberOfSuspendedTokensForPAN": 0,
                  "tokenType": "HCE"
              },
              "walletAccountEmailAddressHash": "DF7C1D317DF3A83838BBAB39F0844FD86F42774EA17AEB06C500DEB95345199B"
          },
          "network_call_method": "VTS_APPROVE_PROVISIONING"
      },
      "schema_version": 1,
      "org_id": "TN-ddce7e50-0485-49ec-a910-866dff0bfd0f",
      "cid": "996e933f-4fc4-44ef-9c4c-e75a02378ba1"
  }
  ```
</details>

### VTS get cardholder verification method (CVM)

<details>
  <summary>VTS get CVM example event</summary>

  ```json
  {
      "event_id": "64c95af7-61ad-4e67-80ac-8c0fc82dca3c",
      "domain": "cards-tokenization",
      "event_type": "notification",
      "timestamp": "2020-12-19T12:37:33.931Z",
      "data": {
          "card_id": 5271995,
          "token_id": 17579,
          "network_data": {
              "clientWalletAccountID": "hWg9hRxCSOCCBm1qiXFxZQ",
              "deviceInfo": {
                  "deviceID": "MTUwMjIyMDEwNjAwMzA3MDUz",
                  "deviceType": "MOBILE_PHONE"
              },
              "encryptedData": "*****",
              "lifeCycleTraceID": 87788,
              "otpMaxReached": false,
              "otpReason": "PROVISIONING",
              "panReferenceID": "V-00000000089935214",
              "tokenReferenceID": "DNITHE0000000003963",
              "tokenRequestorID": 40010043095
          },
          "network_call_method": "VTS_GET_CVM"
      },
      "schema_version": 1,
      "org_id": "TN-ddce7e50-0485-49ec-a910-866dff0bfd0f",
      "cid": "ecb2d4a7-cc39-4b08-9707-eec5dab671ed"
  }
  ```
</details>

### VTS passcode verification

**Important fields**

* `otpValue`

  One time passcode value

* `otpMethodIdentifier`

  One time passcode method:

  ```
      kdaufuf783jnch = otpSMS
      kda74290fjfn84 = otpEmail
      jjfa8f7jnfyfgg = otp App to App
      kfa87fjrnnyuvy = otp call center
  ```

<details>
  <summary>VTS passcode example event</summary>

  ```json
  {
      "event_id": "84eb4b8a-a86e-454a-b756-c01c0975e6a6",
      "domain": "cards-tokenization",
      "event_type": "notification",
      "timestamp": "2020-12-19T12:37:43.659Z",
      "data": {
          "card_id": 5271995,
          "token_id": 17579,
          "network_data": {
              "cardholderInfo": {
                  "cvv2": "*****",
                  "name": "",
                  "primaryAccountNumber": "*****"
              },
              "clientWalletAccountID": "hWg9hRxCSOCCBm1qiXFxZQ",
              "deviceInfo": {
                  "deviceID": "MTUwMjIyMDEwNjAwMzA3MDUz",
                  "deviceType": "MOBILE_PHONE"
              },
              "encryptedData": "*****",
              "lifeCycleTraceID": 878889,
              "otpExpirationDate": "2020-12-19T13:07:43.000Z",
              "otpMethodIdentifier": "kdaufuf783jnch",
              "otpValue": "927945",
              "panReferenceID": "V-00000000089935214",
              "tokenInfo": {
                  "token": "",
                  "tokenType": ""
              },
              "tokenReferenceID": "DNITHE0000000003963",
              "tokenRequestorID": 40010043095
          },
          "network_call_method": "VTS_PASSCODE"
      },
      "schema_version": 1,
      "org_id": "TN-ddce7e50-0485-49ec-a910-866dff0bfd0f",
      "cid": "09723795-ef60-43cd-97f0-f12c773e9293"
  }
  ```
</details>

### VTS token status updated

<details>
  <summary>VTS token status updated example event</summary>

  ```json
  {
          "event_id": "e27d8b4c-4917-4570-9184-99999999999",
          "id": "e27d8b4c-4917-4570-9184-99999999999",
          "schema_version": "1",
          "domain": "cards-tokenization",
          "event_type": "notification",
          "org_id": "TN-9ba58591-7cf3-43bd-8501-99999999999",
          "cid": "d3c93954-9990-4f2e-8b3d-99999999999",
          "timestamp": "2026-07-15T16:53:04.903Z",
          "data": {
              "card_id": 123,
              "token_id": 515,
              "account_id": 9,
              "program_id": 7,
              "token_status": "ACTIVE",
              "token": "4118820300000000",
              "network_data": {
                  "actionCode": "00",
                  "cardholderInfo": {
                      "primaryAccountNumber": "*****"
                  },
                  "dateTimeOfEvent": "2026-07-15T16:24:56Z",
                  "deviceID": "043D109B7C239002429900642532838203D9399999999999",
                  "encryptedData": "*****",
                  "eventType": "TOKEN_STATUS_UPDATED",
                  "lifeCycleTraceID": 306196590832257,
                  "messageReasonCode": "DEVICE_PROVISIONING_RESULT",
                  "panReferenceID": "V-3426034595271499999999999",
                  "riskInformation": {},
                  "tokenInfo": {
                      "token": "4118820300000000",
                      "tokenAssuranceMethod": "14",
                      "tokenExpirationDate": {
                          "month": "12",
                          "year": "2031"
                      },
                      "tokenStatus": "ACTIVE",
                      "tokenType": "SECURE_ELEMENT"
                  },
                  "tokenReferenceID": "DNITHE3026181599999999999",
                  "tokenRequestorID": "40010030273"
              },
              "network_event_out_of_order": false,
              "pismo_response": null,
              "send_challenge": null,
              "network_call_method": "VTS_STATUS_UPDATED_DEVICE_PROVISIONING_RESULT",
              "bin": "",
              "token_requestor_id": "40010030273",
              "token_unique_reference": "DNITHE30261899999999999"
          },
          "_rid": "QjJ7AJUtmoBBBBBAAAAAAA==",
          "_self": "dbs/QjJ7AA==/colls/QjJ7AJUtmo4=/docs/QjJ7AJUtmoBBBBBAAAAAAA==/",
          "_etag": "\"68030813-0000-1100-0000-99999999999\"",
          "_attachments": "attachments/",
          "_ts": 1784134386
      },
  ```

  <br />
</details>

### VTS token deactivated

<details>
  <summary>VTS token deactivated example event</summary>

  ```json
  {
      "event_id": "938285b2-6deb-46d8-871a-5d149c549368",
      "domain": "cards-tokenization",
      "event_type": "notification",
      "timestamp": "2020-12-19T12:35:50.943Z",
      "data": {
          "card_id": 5272036,
          "token_id": 17577,
          "network_data": {
              "actionCode": "00",
              "cardholderInfo": {
                  "primaryAccountNumber": "*****"
              },
              "dateTimeOfEvent": "2020-12-19T12:35:49.000Z",
              "deviceID": "MTUwMjIyMDEwNjAwMzA3MDUz",
              "encryptedData": "*****",
              "lifeCycleTraceID": 87887,
              "messageReason": "*CUSTOMER_CONFIRMED||Delete initiated by device.",
              "messageReasonCode": "TOKEN_DEACTIVATED",
              "panReferenceID": "V-00000000057824435",
              "tokenInfo": {
                  "token": "000000000",
                  "tokenExpirationDate": {
                      "month": "11",
                      "year": "2029"
                  },
                  "tokenStatus": "DEACTIVATED",
                  "tokenType": "HCE"
              }
          },
          "network_call_method": "VTS_STATUS_UPDATED_TOKEN_DEACTIVATED"
      },
      "schema_version": 1,
      "org_id": "TN-ddce7e50-0485-49ec-a910-866dff0bfd0f",
      "cid": "9e57c38b-481e-48f0-bc34-96ee0659acde"
  }
  ```
</details>

### VTS token suspended

<details>
  <summary>VTS token suspended example event</summary>

  ```json
  {
      "event_id": "3c4fdf08-d9bb-4982-ab8a-0a31abcbce06",
      "domain": "cards-tokenization",
      "event_type": "notification",
      "timestamp": "2020-12-23T10:15:55.378Z",
      "data": {
          "card_id": 5271995,
          "token_id": 17580,
          "network_data": {
              "actionCode": "00",
              "cardholderInfo": {
                  "primaryAccountNumber": "*****"
              },
              "dateTimeOfEvent": "2020-12-23T10:15:53.000Z",
              "deviceID": "MTUwMjIyMDEwNjAwMzA3MDUz",
              "encryptedData": "*****",
              "lifeCycleTraceID": 952828,
              "messageReason": "*a reason",
              "messageReasonCode": "TOKEN_SUSPEND",
              "panReferenceID": "V-00000000089935214",
              "tokenInfo": {
                  "token": "000000000",
                  "tokenExpirationDate": {
                      "month": "11",
                      "year": "2029"
                  },
                  "tokenStatus": "SUSPENDED",
                  "tokenType": "HCE"
              }
          },
          "network_call_method": "VTS_STATUS_UPDATED_TOKEN_SUSPEND"
      },
      "schema_version": 1,
      "org_id": "TN-ddce7e50-0485-49ec-a910-866dff0bfd0f",
      "cid": "b15a4ff4-ad69-4ca3-be92-3488ec8d37f3"
  }
  ```
</details>

### VTS token resume

<details>
  <summary>VTS token resume example event</summary>

  ```json
  {
      "event_id": "1e7fde7c-0b7c-4d26-91af-c2b35dedceb4",
      "domain": "cards-tokenization",
      "event_type": "notification",
      "timestamp": "2020-12-23T10:22:18.384Z",
      "data": {
          "card_id": 5271995,
          "token_id": 17580,
          "network_data": {
              "actionCode": "00",
              "cardholderInfo": {
                  "primaryAccountNumber": "*****"
              },
              "dateTimeOfEvent": "2020-12-23T10:22:15.000Z",
              "deviceID": "MTUwMjIyMDEwNjAwMzA3MDUz",
              "encryptedData": "*****",
              "lifeCycleTraceID": 76788866,
              "messageReason": "*a reason",
              "messageReasonCode": "TOKEN_RESUME",
              "panReferenceID": "V-00000000089935214",
              "tokenInfo": {
                  "token": "000000000",
                  "tokenExpirationDate": {
                      "month": "11",
                      "year": "2029"
                  },
                  "tokenStatus": "ACTIVE",
                  "tokenType": "HCE"
              }
          },
          "network_call_method": "VTS_STATUS_UPDATED_TOKEN_RESUME"
      },
      "schema_version": 1,
      "org_id": "TN-ddce7e50-0485-49ec-a910-866dff0bfd0f",
      "cid": "61820b68-9e9c-4608-a072-94918f9c6bf3"
  }
  ```
</details>
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/card-tokenization-flow-and-events.md`: updatedAt 2026-07-20T22:51:12.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/card-tokenization-flow-and-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/card-tokenization-flow-and-events | `2ccc85848c54735d…` | 2026-07-20T22:51:12.000Z |

## Related knowledge units

- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-EVT-client-webhooks-part-02` — Client webhooks (part 2 of 14)
- `KU-EVT-client-webhooks-part-03` — Client webhooks (part 3 of 14)
- `KU-EVT-client-webhooks-part-04` — Client webhooks (part 4 of 14)
- `KU-EVT-client-webhooks-part-05` — Client webhooks (part 5 of 14)
- `KU-EVT-client-webhooks-part-06` — Client webhooks (part 6 of 14)
- `KU-EVT-client-webhooks-part-07` — Client webhooks (part 7 of 14)
- `KU-EVT-client-webhooks-part-08` — Client webhooks (part 8 of 14)
- `KU-EVT-client-webhooks-part-09` — Client webhooks (part 9 of 14)
- `KU-EVT-client-webhooks-part-10` — Client webhooks (part 10 of 14)
- `KU-EVT-client-webhooks-part-11` — Client webhooks (part 11 of 14)
- `KU-EVT-client-webhooks-part-12` — Client webhooks (part 12 of 14)
- `KU-EVT-client-webhooks-part-13` — Client webhooks (part 13 of 14)
- `KU-EVT-client-webhooks-part-14` — Client webhooks (part 14 of 14)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
