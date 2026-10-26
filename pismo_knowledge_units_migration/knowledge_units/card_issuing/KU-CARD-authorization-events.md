---
ku_id: KU-CARD-authorization-events
title: Authorization events
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/authorization-events.md
  sha256: 945278ecf54fbe95fee2606fc9fa1efcb731ad7bec5d6a8c665ea3de0dbbc5c8
  url: https://developers.pismo.io/pismo-docs/docs/authorization-events
  role: primary_guide
  updated_at: '2026-06-26T15:38:51.000Z'
operations:
- performClearingReconciliation
related_kus:
- KU-API-card-issuing-reconciliation--network-transactions-backoffice
- KU-CARD-full-and-zero-balance-workflows
- KU-CARD-linking-events-in-an-authorization-workflow
- KU-EVT-catalogue-other-domains
- KU-EVT-timeline-overview
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Authorization events

**KU ID:** `KU-CARD-authorization-events` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/authorization-events.md`:

> During the authorization workflow, the Pismo platform generates [events](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview) that allow you to verify transaction status and other information. For information about using these events to map the lifecycle of an authorization, refer to [Linking authorization events](https://developers.pismo.io/pismo-docs/docs/linking-events-in-an-authorization-workflow).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/authorization-events.md`: Authorization events; Authorization event characteristics; Base contract; Authorization event types; Network authorization ISO8583 message event; Network authorization event; Authorization discard process; Card network authorization return event; Timeline events; Clearing/Base II events

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/authorization-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/authorization-events · updatedAt: 2026-06-26T15:38:51.000Z

<!-- source:begin path=docs/card-issuing/authorization-events.md part=0-end -->

# Authorization events

During the authorization workflow, the Pismo platform generates [events](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview) that allow you to verify transaction status and other information. For information about using these events to map the lifecycle of an authorization, refer to [Linking authorization events](https://developers.pismo.io/pismo-docs/docs/linking-events-in-an-authorization-workflow).

The [Network authorization event](#network-authorization-event) is the primary event for verifying an authorization. However, you should consume all the authorization events to make sure that you don't miss anything.

The [Full and Zero balance workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows) detail the events that Full balance and Zero balance issuers will receive. They are similar, but slightly different.

## Authorization event characteristics

The Pismo platform generates events related to specific authorization messages received from the card network. For any given transaction, Pismo might or might not generate all of the events, depending on the transaction life cycle. Also, various steps in the authorization process might issue the same event, so an event could be issued many times for one transaction.

### Base contract

Each event contains a [common set of fields](https://developers.pismo.io/events/docs/event-base-main-event), (*base contract*) such as `event_id`, `domain`, and `event_type`.  These fields uniquely identify each event. The `data` field contains  data unique to each event.

> 📘 Recurring transactions
>
> You can determine if a transaction is recurring (as with subscription transactions) or not by looking at specific fields.
>
> For Mastercard:\
> Check the object `de61_pos_data`, subfield POS cardholder presence, `sf4_pos_cardholder_presence`.\
> If the value is **4**, the transaction is a recurring transaction.\
> If the field is blank, it is not a recurring transaction.\
> Refer to the [Mastercard example - iso8583 - message event](https://developers.pismo.io/pismo-docs/docs/authorization-events#iso8583-message-event-examples) for the full code example.
>
> For Visa:\
> Check the `f126_visa_private_use_fields`.\
> A value of **R** indicates a recurring transaction.\
> A value of **C** indicates card on file.\
> If the field is blank, it is not a recurring transaction or card on file.\
> Refer to the [Visa example - iso8583 - message event](https://developers.pismo.io/pismo-docs/docs/authorization-events-copy#iso8583-message-event-examples) for the full code example.

## Authorization event types

The Pismo platform supports the following authorization event types:

* Network authorization [ISO8583](https://en.wikipedia.org/wiki/ISO_8583) message
* Network authorization
* Card network authorization return
* Timeline
* Clearing/Base II (raw messages)

These events are described in the following sections.

### Network authorization ISO8583 message event

**Domain**: networktransactions

**Type**:

* [iso8583-message](https://developers.pismo.io/events/docs/networktransactions-iso8583-message-1)

This event represents the raw message received from the card network in the authorization workflow. You can use it to verify all non-sensitive data received for a specific message (that is, messages other than Clearing/Base II messages). The Pismo platform issues an ISO8583 event after parsing the message and removing any sensitive data from the payload. The event is not issued if an error or timeout prevents the message from reaching the platform.

An ISO8583 event payload contains a base contract with any custom data included in the `data` field.

> 📘 Zero balance
>
> Zero balance issuers receive this authorization event and they get the raw message as part of what is sent when Pismo calls the issuer's webhook as detailed in Steps 4 and 5 in the [Full and Zero balance workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).

You can use the base contract's `cid` field to relate this event to other related events.  For more details, visit [Linking events in an authorization workflow](https://developers.pismo.io/pismo-docs/docs/linking-events-in-an-authorization-workflow).

> 📘 Message type indicator field
>
> You can identify what kind of message is associated with an event using the `mti` field of the message. Here are a few examples of values for `mti` and the type of message each one represents.
>
> * **0100** - Authorization request
> * **0120** - Authorization advice
> * **0400** - Reversal request
>
> For more information, refer to [message type indicator](https://en.wikipedia.org/wiki/ISO_8583#Message_type_indicator_\(MTI\)).

In the message field, there's a JSON payload representing all the fields present in the message received from the card network. The payload does not include fields for sensitive messages. The message field does not have a fixed payload, because it varies depending on the network. To identify each field present in the message, you need to look up the field in the network manual.

#### ISO8583-message event examples

The following ISO8583-message event examples illustrate the fields coming from different card networks. The content varies according to the request being processed, where some fields may or may not be present. Refer to the network specification to find all possible fields.

<details>
  <summary>Mastercard example - iso8583-message event</summary>

  ```json
  {
    "event_id": "[valid-uuid]",
    "domain": "networktransactions",
    "event_type": "iso8583-message",
    "schema_version": "1",
    "org_id": "[tenant]",
    "cid": "[valid-uuid-correlation-id]",
    "data": {
      "card_hash": "[card-hash]",
      "caller": "Mastercard",
      "mti": "0100",
      "message": {
        "de2_primary_account_number": "[card-hash]",
        "de3_processing_code": {
          "sf1_cardholder_transaction_type_code": "00",
          "sf2_cardholder_from_account_type_code": "30",
          "sf3_cardholder_to_account_type_code": "00"
        },
        "de4_amount_transaction": "000000000750",
        "de5_amount_settlement": "000000000143",
        "de6_amount_cardholder_billing": "000000000750",
        "de7_tranmission_date_and_time": {
          "sf1_date": "1208",
          "sf2_time": "133633"
        },
        "de9_conversion_rate_settlement": {
          "sf1_decimal_indicator": "7",
          "sf2_conversion_rate": "1906667"
        },
        "de10_conversion_rate_cardholder_billing": {
          "sf1_decimal_indicator": "6",
          "sf2_cardholderbilling_conversion_rate": "1000000"
        },
        "de11_stan": "268820",
        "de12_time_local_transaction": "103633",
        "de13_date_local_transaction": "1208",
        "de14_date_expiration": "2811",
        "de15_date_settlement": "1208",
        "de16_date_conversion": "1207",
        "de18_merchant_type": "5814",
        "de22_pos_entry_mode": {
          "sf1_pos_terminal_pan_entry_mode": "07",
          "sf2_pos_terminal_pin_entry_mode": "1"
        },
        "de23_card_sequence_number": "000",
        "de28_amount_transaction_fee": {},
        "de29_amount_settlement_fee": {},
        "de30_amount_transaction_processing_fee": {},
        "de31_amount_settlement_processing_fee": {},
        "de32_acquiring_institution_id_code": "012088",
        "de33_forwarding_institution_id_code": "012088",
        "de37_retrieval_reference_number": {
          "sf1_transaction_date_and_initiator_discretionary_data": "7777777",
          "sf2_terminal_transaction_number": "55555"
        },
        "de41_card_acceptor_terminal_id": "00000001",
        "de42_card_acceptor_id_code": "033350555550001",
        "de43_card_acceptor_name_location_for_all_transactions": {
          "sf1_card_acceptor_name": "MERCHANT NAME    ",
          "sf3_card_acceptor_city": "MERCHANT CITY  ",
          "sf5_card_acceptor_state_or_country_code": "BRA"
        },
        "de48_additional_data_private_user": {
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
              "sf1_security_services_indicator": "AQV",
              "sf2_security_services_data": "000"
            },
            {
              "sf1_security_services_indicator": "AQS",
              "sf2_security_services_data": "000"
            },
            {
              "sf1_security_services_indicator": "AQF",
              "sf2_security_services_data": "000"
            }
          ],
          "se57_security_services_additional_data_for_acquirers": {},
          "se58_atm_additional_data": {},
          "se61_pos_data_extended_condition_codes": {
            "sf1_partial_approval_terminal_support_indicator": "0",
            "sf2_purchase_amount_only_terminal_support_indicator": "0",
            "sf3_realtime_substantiation_indicator": "0",
            "sf4_merchant_transaction_fraud_scoring_indicator": "0",
            "sf5_final_authorization_indicator": "1"
          },
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
            "sf1_fraud_score": "009",
            "sf2_score_reason_code": "90",
            "sf3_rules_score": "009",
            "sf4_rules_reason_code1": "90",
            "sf5_rules_reason_code2": "00"
          },
          "se78_payment_service_indicator": {},
          "se79_chip_cvr_or_tvr_bit_error_results": {},
          "se87_card_validation_code_result_or_cvv2": "M",
          "se93_fleet_card_id_request_data": {}
        },
        "de49_currency_code_transaction": "986",
        "de50_currency_code_settlement": "840",
        "de51_currency_code_cardholder_billing": "986",
        "de55_integrated_circuit_card": {
          "sf2_cryptogram_information_data": "80",
          "sf3_issuer_application_data": "0333B04005550000000000000000000000FF",
          "sf5_terminal_verification_result": "0000008001",
          "sf6_transaction_date": "221208",
          "sf7_transaction_type": "00",
          "sf8_amount_authorized": "000000000750",
          "sf9_transaction_currency_code": "0986",
          "sf10_application_interchange_profile": "1980",
          "sf11_terminal_country_code": "0076",
          "sf12_cardholder_verification_method": "1F0302",
          "sf13_terminal_capabilities": "E008E8",
          "sf15_amount_other": "000000000000",
          "sf23_application_transaction_counter": "001E"
        },
        "de60_advice_reason_code": {},
        "de61_pos_data": {
          "sf1_pos_terminal_attendance": "0",
          "sf2_reserved_for_future_use": "0",
          "sf3_pos_terminal_location": "0",
          "sf4_pos_cardholder_presence": "0",
          "sf5_pos_card_presence": "0",
          "sf6_pos_card_capture_capabilities": "0",
          "sf7_pos_transaction_status": "0",
          "sf8_pos_transaction_security": "0",
          "sf9_reserved_for_future_use": "0",
          "sf10_cardholder_activated_terminal_level": "0",
          "sf11_pos_card_data_terminal_input_capability_indicator": "3",
          "sf12_pos_authorization_life_cycle": "00",
          "sf13_pos_country_code_or_submerchant": "076",
          "sf14_postal_code_or_submerchant": "0555551000"
        },
        "de63_network_data": {
          "sf1_financial_network_code": "MBK",
          "sf2_banknet_reference_number": "ABCXYZ"
        },
        "de90_original_data_elements": {},
        "de94_service_indicator": {},
        "de95_replacement_amounts": {},
        "de97_amount_net_settlement": {},
        "de112_additional_data_national_use": {},
        "de120_record_data": {},
        "de124_member_defined_data": {}
      }
    }
  }
  ```
</details>

<details>
  <summary> Visa  example - iso8583-message event</summary>

  ```json
  {
    "event_id": "[valid-uuid]",
    "domain": "networktransactions",
    "event_type": "iso8583-message",
    "schema_version": "1",
    "org_id": "[tenant]",
    "cid": "[valid-uuid-correlation-id]",
    "timestamp": "2022-12-08T10:00:00.707Z",
    "data": {
      "card_hash": "[card-hash]",
      "caller": "Visa",
      "mti": "0100",
      "message": {
        "f2_primary_account_number": "[card-hash]",
        "f3_processing_code": "002000",
        "f4_amount_transaction": "000000000200",
        "f6_amount_cardholder_billing": "000000000039",
        "f7_transmission_date_and_time": "1208135000",
        "f10_conversion_rate_cardholder_billing": "71950000",
        "f11_stan": "777777",
        "f14_date_expiration": "2710",
        "f15_date_liquidation": "1209",
        "f18_merchant_type": "5411",
        "f19_acquiring_institution_country_code": "0076",
        "f22_pos_entry_mode": "0510",
        "f23_card_sequence_number": "0000",
        "f25_pos_condition_code": "00",
        "f32_acquiring_institution_id_code": "417939",
        "f34_electronic_ecommerce_data": {
          "sf01_authentication_data": {}
        },
        "f37_retrieval_reference_number": "123456789012",
        "f41_card_acceptor_terminal_id": "PGWD99FE",
        "f42_card_acceptor_id_code": "000000091075999",
        "f43_card_acceptor_location": "Merchant Name Merchant City Country",
        "f48_additional_data_private": {},
        "f49_currency_code_transaction": "0986",
        "f51_currency_code_cardholder_billing": "0840",
        "f55_integrated_circuit_card": {
          "sf3_issuer_application_data": "06033304B99002",
          "sf5_terminal_verification_result": "0080008000",
          "sf6_transaction_date": "221208",
          "sf7_transaction_type": "00",
          "sf8_amount_authorized": "000000000200",
          "sf9_transaction_currency_code": "0986",
          "sf10_application_interchange_profile": "3800",
          "sf11_terminal_country_code": "0076",
          "sf13_terminal_capabilities": "E0F0C8",
          "sf15_amount_other": "000000000000",
          "sf23_application_transaction_counter": "0050"
        },
        "f56_payment_account_reference_data": {},
        "f59_national_point_of_service_geographic_data": "0000099902200",
        "f60_additional_pos_data": "05000010",
        "f62_custom_payment_services": {
          "sf2_transaction_identifier": "123456789012345"
        },
        "f63_private_use": {
          "sf1_network_id": "0002"
        },
        "f104_transaction_description_transaction_specific_data": {
          "sf5d_installments_data": {},
          "sf69_payment_format": {},
          "sf67_national_payment_format": {}
        },
        "f117_national_use": {
          "usage_6_argentina_agro": {}
        },
        "f123_verification_data": {
          "token_data": {},
          "address_verification_data": {},
          "activation_verification_data": {}
        },
        "f125_supporting_information_data": {
          "token_device": {},
          "wallet_provider": {}
        },
        "f126_visa_private_use_fields": {
        sf10_cvv2_authorization_request_data: ""
         }
      }
    }
  ```
</details>

<details>
  <summary>TecBan example - iso8583-message event</summary>

  ```json
  {
      "event_id": "[valid-uuid]",
      "domain": "networktransactions",
      "event_type": "iso8583-message",
      "schema_version": "1",
      "org_id": "[tenant]",
      "cid": "[valid-uuid-correlation-id]",
      "timestamp": "2022-12-09T10:00:00.421Z",
      "data": {
        "card_hash": "[card-hash]",
        "caller": "tecban",
        "mti": "0200",
        "message": {
          "de2_primary_account_number": "[card-hash]",
          "de3_processing_code": {
            "sf1_cardholder_transaction_type_code": "01",
            "sf2_cardholder_from_account_type_code": "20",
            "sf3_cardholder_to_account_type_code": "00"
          },
          "de4_amount_transaction": "000000100000",
          "de7_tranmission_date_and_time": {
            "sf1_date": "1209",
            "sf2_time": "150000"
          },
          "de11_nsu": "999999",
          "de12_time_local_transaction": "120000",
          "de13_date_local_transaction": "1209",
          "de15_date_settlement": "1209",
          "de22_pos_entry_mode": {
            "sf1_pos_terminal_pan_entry_mode": "05",
            "sf2_pos_terminal_pin_entry_mode": "1"
          },
          "de23_card_sequence_number": "000",
          "de32_institution_id_code": "00088888888",
          "de37_retrieval_reference_number": "123456789012",
          "de41_card_acceptor_terminal_id": "00055555",
          "de42_card_acceptor_id_code": "000000007777777",
          "de49_currency_code_transaction": "076",
          "de55_integrated_circuit_card": {
            "sf3_issuer_application_data": "0333B00009990000000000000000000000FF",
            "sf5_terminal_verification_result": "8000040000",
            "sf6_transaction_date": "221209",
            "sf7_transaction_type": "01",
            "sf8_amount_authorized": "000000100000",
            "sf9_transaction_currency_code": "0986",
            "sf10_application_interchange_profile": "3900",
            "sf11_terminal_country_code": "0076",
            "sf12_cardholder_verification_method": "020300",
            "sf13_terminal_capabilities": "6040C0",
            "sf15_amount_other": "000000000000",
            "sf23_application_transaction_counter": "0095"
          },
          "de61_pos_data": "B88888888",
          "de127_response_nsu": "000999999"
        }
      }
    }   
  ```
</details>

<details>
  <summary>ELO example - iso8583-message event</summary>

  ```json
  {
      "event_id": "[valid-uuid]",
      "domain": "networktransactions",
      "event_type": "iso8583-message",
      "schema_version": "1",
      "org_id": "[tenant]",
      "cid": "[valid-uuid-correlation-id]",
      "timestamp": "2024-10-10T19:11:03.119Z",
      "data": {
          "correlation_id": "e0aebd86-ae29-4e01-8584-f7c0a815f2e5",
          "card_hash": "[card-hash]",
          "org_id": "TN-5aea4104-7994-46d5-83d6-a55c8439a00c",
          "mti": "0100",
          "transaction_identifier": "123456789012345",
          "caller": "elo",
          "message": {
              "b2_primary_account_number": "[card-hash]",
              "b3_processing_code": {
                  "sf1_cardholder_transaction_type_code": "00",
                  "sf2_cardholder_from_account_type_code": "20",
                  "sf3_cardholder_to_account_type_code": "00"
              },
              "b4_amount_transaction": "000000009600",
              "b7_transmission_date_and_time": "1010191102",
              "b11_stan": "595343",
              "b12_time_local_transaction": "161102",
              "b13_date_local_transaction": "1010",
              "b14_date_card_expiration": "2711",
              "b18_merchant_category_code": "1910",
              "b19_acquiring_institution_country_code": "076",
              "b22_pos_entry_mode": {
                  "Sf1PosTerminalPanEntryMode": "83",
                  "Sf2PosTerminalPinEntryMode": "1"
              },
              "b23_card_sequence_number": "000",
              "b24_function_code": "100",
              "b32_acquiring_institution_id_code": "0025",
              "b37_nsu": "412669675245",
              "b41_card_acceptor_terminal_id": "20172289",
              "b42_card_acceptor_id_code": "01708801000179 ",
              "b43_card_acceptor_location": {
                  "sf1_card_acceptor_name": "Kalunga               ",
                  "sf2_space": " ",
                  "sf3_card_acceptor_city": "Sao Paulo    ",
                  "sf4_space": " ",
                  "sf5_card_acceptor_state_or_country_code": "076"
              },
              "b46_additional_response_data": {},
              "b47_additional_national_data": {},
              "b48_additional_data": {
                  "fields_present": [
                      "CDT",
                      "BAN",
                      "PRD"
                  ],
                  "vps": {},
                  "cdt": {
                      "track1_flag": "T0"
                  },
                  "bnd": {},
                  "pre": {},
                  "prd": "071",
                  "ban": {
                      "node_id": "1234",
                      "elo_reserved_value": "  ",
                      "network_atm_id": "1234",
                      "elo_reference_id": "123456789012345",
                      "elo_reserved_value2": "    "
                  }
              },
              "b49_currency_code_transaction": "986",
              "b55_integrated_circuit_card": {
                  "sf9F02_ammount_authorized": "000000009600",
                  "sf9F03_ammount_orther": "000000000000",
                  "sf9F1A_terminal_country_code": "0076",
                  "sf95_terminal_verification_results": "220004E000",
                  "sf5F2A_transaction_currency_code": "0986",
                  "sf9A_transaction_date": "241010",
                  "sf9C_transaction_type": "00",
                  "sf9F33_termainal_capabilities": "E0A0C0",
                  "sf9F34_cvm_results": "020300",
                  "sf82_application_interchange_profile": "1900",
                  "sf9F36_application_transaction_counter": "02AF",
                  "sf9F10_issuer_application_data": "0FA501000000000000000000000000000F000000000000000000000000000000",
                  "sf9F27_cryptogram_information_data": "80"
              },
              "b58_national_point_of_service_geographic_data": "Alameda Xingu         05155083 07612345          ShopsCentis",
              "b60_additional_pos_data": {
                  "sf1_terminal_type": "0",
                  "sf2_partial_authorization_flag": "0",
                  "sf3_terminal_location_flag": "0",
                  "sf4_cardholder_present_flag": "0",
                  "sf5_card_present_flag": "0",
                  "sf6_card_capture_capability_flag": "1",
                  "sf7_transaction_status_flag": "0",
                  "sf8_transaction_fraud_flag": "0",
                  "sf9_resever": "0",
                  "sf10_pos_type": "P",
                  "sf11_input_terminal_capability": "H",
                  "sf12_special_condition_indicator": "0",
                  "sf13_reserved": "0"
              },
              "b62_custom_payment_services": {},
              "b95_replacement_values": {},
              "b106_transactional_data": {
                  "dataset61_payment_token_data": {},
                  "dataset64_original_transaction_data": {}
              },
              "b107_custom_transaction_data": {
                  "dataset56_gift_card_data": {},
                  "dataset57_transaction_fund_data": {},
                  "dataset58_paypal_data": {},
                  "dataset59_default_address_data": {},
                  "dataset60_fraudulent_data": {}
              },
              "b123_promotional_fields": {
                  "dataset_56_pay_with_rewards": {},
                  "dataset_57_doken_data": {},
                  "dataset_58_offers_paypal": {},
                  "dataset_59_fidelity_program": {}
              },
              "b124_transaction_qualifier": {
                  "cd6_fraud_data": {},
                  "cd8_data_compromised_account": {}
              },
              "b127_version_indicator_text": "12242",
              "start": 1728587462727465485,
              "anti_fraud_url": "https://pismo-hml.2rpnet.io/api/case/pismo/analyzeMessage/card"
          },
          "invalid": false
      }
  } to sns topic: arn:aws:sns:sa-east-1: 270036487593:NetworkAuthorizationsEvents
  ```
</details>

### Network authorization event

**Domain**: networktransactions

**Type**:

* [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1)

This event represents an authorization action. All authorization actions generate a Network authorization event. The Pismo platform issues the event after the message is processed and a decision is made about the action to take. Note that this does not apply to balance inquiry authorizations or transactions. Balance inquiries do not generate a Network authorization event.

The enum field `authorization_category` identifies the event action such as authorization or confirmation. An operation can issue one or more Network authorization events. Each event identifies an action performed during the operation. For example, if an operation is authorized, confirmed, and then canceled, three Network authorization events are issued with the categories AUTHORIZATION, CONFIRMATION, and CANCELLATION, respectively.

The Network authorization event payload includes the base contract and the `data` field, which contains the event details in JSON format.

A Network authorization event can be used as a base point to link other events issued in the authorization workflow. The Pismo platform sends this event for all actions related to an authorization record. The event contains all the information you need to identify the relationship between events, including the authorization id (`authorization_id`), correlation id (`cid`), and other values. For more details, refer to [Linking events in an authorization workflow](https://developers.pismo.io/pismo-docs/docs/linking-events-in-an-authorization-workflow).

> 📘 Airport tax
>
> The AIRPORT\_TAX authorization category is emitted when a Visa clearing record carries an airport tax surcharge indicator. The AIRPORT\_TAX marker event is a lifecycle/surcharge-record signal carrying no tax amount. Its purpose is to signal that the authorization involves an airport tax and trigger the internal confirmation pairing process. The field is populated on the confirmation that actually carried the tax.

> 📘 Zero balance
>
> Zero balance issuers receive this authorization event and they get the raw message as part of what is sent when Pismo calls the issuer's webhook as detailed in Steps 4 and 5 in the [Full and Zero balance workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).

### Authorization discard process

There are two ways for a purchaser to cancel a purchase:

* Cancel online with an `mti 0400` request
* Cancel via Base II: note that a purchase confirmed via Base II cannot be cancelled by a `0400` message; a Base II message is required to complete the cancellation.

Purchase transactions are generated only in Base II and the accounting is also impacted only in Base II. Therefore, if a transaction is performed (message `0100`) and canceled (message `0400`) online, without receiving Base II, there is no impact on the accounting.

The expiration of the term occurs when a purchase does not receive a confirmation via base II or it receives a cancellation, either online or via base II. Therefore, there was no impact on the accounting of this account for this transaction and the cancellation due to the expiration of the term will also not impact the accounting. Only the refund is made for the account balance.

> 📘 Expiry of term
>
> The expiry of term occurs with the lapse of time when a purchase does not receive confirmation via Base II and does not receive a cancellation (online or via Base II).
>
> The authorization discard time is:
>
> * 10 calendar days for normal authorizations
> * 35 calendar days for pre-authorizations and international authorizations
>
> Note: Authorizations registered directly from Base II do not expire due to the expiration of a term, as they arise from a confirmation.

### Card network authorization return event

**Domain**: networktransactions

**Type**:

* [Card network authorization return sent](https://developers.pismo.io/events/docs/networktransactions-network-message-1)

This event represents the response the Pismo platform sends to the card network in the online workflow for one operation. The platform issues it immediately before it sends the same response to the network. It can be used to verify that the authorization event emitted for this operation has the same result as the one sent to the network.

It's possible that the Pismo platform will approve an operation, issuing a Network authorization event, but an error in processing will occur after the approval. In this case, the online response event will show a declined response while the Network Authorization event will show an approved response. The platform will notify the cardholder that the transaction was declined for an unknown reason and that they should try again. You can use both events to identify the error in the processing.

The platform uses the Card network authorization return event to reconcile the previously saved operation status against the response sent to the network. If the two values are different, it indicates that an error occurred between the time when the decision was made and when the decision was sent to the network. In this case, an appropriate action is taken. For example, an authorization might be canceled, or the authorization team might be alerted so that they can fix the inconsistency.

The event [payload](https://developers.pismo.io/events/docs/networktransactions-network-message-1) contains the base contract and the `data` field contents in JSON format.

> 📘 Full and Zero balance
>
> A Card network authorization return event is issued in both Full and Zero balance workflows. See step 6 in the [Full and Zero balance workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).

### Timeline events

The platform generates [timeline events](https://developers.pismo.io/pismo-docs/docs/timeline-overview) at the same time as the [Network authorization](#network-authorization-iso8583-message-event) event and they contain similar information. You can use the information from both events to obtain all information about the authorization, but the Network authorization event is the primary source.

**Domain**: timeline

**Types**:

* [authorization\_authorize](https://developers.pismo.io/events/docs/timeline-authorization-authorize-1)
* [authorization\_cancellation](https://developers.pismo.io/events/docs/timeline-authorization-cancellation-1)
* [authorization\_cancellation\_refusal](https://developers.pismo.io/events/docs/timeline-authorization-cancellation-refusal-1)
* [authorization\_cancellation\_reversal](https://developers.pismo.io/events/docs/timeline-authorization-cancellation-reversal-1)
* [authorization\_partial\_cancellation](https://developers.pismo.io/events/docs/timeline-authorization-partial-cancellation-1)
* [authorization-refusal](https://developers.pismo.io/events/docs/timeline-authorization-refusal-1)
* [authorization-referral](https://developers.pismo.io/events/docs/timeline-authorization-referral-1)
* [authorization\_replacement](https://developers.pismo.io/events/docs/timeline-authorization-replacement-1)
* [authorization\_incremental](https://developers.pismo.io/events/docs/timeline-authorization-incremental-1)
* [confirmation-authorize](https://developers.pismo.io/events/docs/timeline-confirmation-authorize-1)
* [confirmation-cancellation](https://developers.pismo.io/events/docs/timeline-confirmation-cancellation-1)
* [confirmation\_replacement](https://developers.pismo.io/events/docs/timeline-confirmation-replacement-1)

<Callout icon="📘" theme="info">
  Timeline events are not issued if you use a Zero balance workflow, because you control the authorization life cycle.
</Callout>

### Clearing/Base II events

Clearing/Base II events are emitted in two domains – `networktransactions` and `authorization`.

**Domain**: `networktransactions`

**Types**:

* [Network authorization clearing message received](https://developers.pismo.io/events/docs/networktransactions-clearing-1)  – This is the recommended Clearing/Base II event to use. In addition to raw data, it contains useful information to identify the account, card, program, file type, and network.

**Domain**: authorization

**Types**:

* [Mastercard raw credit authorization received](https://developers.pismo.io/events/docs/authorization-raw-credit-mastercard-1)
* [Mastercard raw debit authorization received](https://developers.pismo.io/events/docs/authorization-raw-debit-mastercard-1)
* [Visa raw credit authorization received](https://developers.pismo.io/events/docs/authorization-raw-credit-visa-1)
* [Visa raw debit authorization received](https://developers.pismo.io/events/docs/authorization-raw-debit-visa-1)

A Clearing/Base II event should be used to verify all non-sensitive data received for Clearing/Base II messages. These events have the same purpose as iso8583 events, since they also represent raw messages received from the card network. The Pismo platform issues a Clearing/Base II event after parsing the message and removing any sensitive data from the payload.

To identify each field present in the message, you need to look up the field in the network manual. The field names are the same as in the manual.

> 📘 Full vs Zero balance
>
> Clearing/Base II events are issued in both Full and Zero balance workflows.

#### Clearing event examples

The following  [Network authorization clearing message received](https://developers.pismo.io/events/docs/networktransactions-clearing-1) event examples show the fields from different card networks. The content varies according to the request being processed, where some fields may or may not be present. Refer to the network specification to find all possible fields.

<details>
  <summary>Mastercard T112 dual message example - clearing event</summary>

  ```json
    {
      "event_id": "[valid-uuid]",
      "domain": "networktransactions",
      "event_type": "clearing",
      "schema_version": "1",
      "org_id": "[tenant]",
      "cid": "[valid-uuid-correlation-id]",
      "timestamp": "2022-12-08T11:00:00.000Z",
      "data": {
        "card_id": 99999,
        "account_id": 88888,
        "program_id": 123,
        "file_type": "T112",
        "network": "Mastercard",
        "raw_message": {
          "mti": "FIRST_PRESENTMENT",
          "primaryAccountNumber": "[card-hash]",
          "processingCode": {
            "transactionTypeCode": "00",
            "codeFromAccountTypeCode": "00",
            "codeToAccountTypeCode": "00"
          },
          "transactionAmount": 100.00,
          "reconciliationAmount": "000000010000",
          "cardholderBillingAmount": "000000010000",
          "reconciliationConversionRate": "61000000",
          "cardholderBillingConversionRate": "61000000",
          "localTransactionDateTime": {
            "date": "2022-12-07T03:00:00+0000",
            "time": "1970-01-01T06:04:34+0000"
          },
          "posEntryMode": "B90550799001",
          "cardSequenceNumber": "000",
          "functionCode": 200,
          "cardAcceptorBusinessCode": "6300",
          "acquirerReferenceDate": {
            "mixedUse": "0",
            "acquirersBin": "548087",
            "julianProcessingDate": "2342",
            "acquirersSequenceNumber": "97777199999",
            "checkDigitNumeric": "2"
          },
          "forwardingInstitutionIdCode": "006207",
          "approvalCode": "ABC123",
          "cardAcceptorIdCode": "099990167      ",
          "cardAcceptorNameLocation": "MERCHANTNAME\\\\MERCHANTADDRESS\\\\CITY\\\\POSTALCODE  SP BRA",
          "additionalData": {
            "p0002": "MBK",
            "p0003": "MBK",
            "p0015": "2212061",
            "terminalType": "CT6",
            "p0052": "210",
            "transactionFeeAmounts": [
              {
                "feeTypeCode": "00",
                "feeProcessingCode": "29",
                "feeSettlementIndicator": "01",
                "feeCurrencyCode": "986",
                "feeAmount": "000000000080",
                "feeReconciliationCurrencyCode": "986",
                "feeReconciliationAmount": "000000000080"
              }
            ],
            "currencyExponents": "9862",
            "businessActivity": "MCC4082000HU221209940MBKNNNNNNN",
            "p0159": "99999      0000000099999               1LA00098610N2212070422120701",
            "settlementIndicator": "M",
            "p0177": "N ",
            "originatingMessageFormat": "2"
          },
          "transactionCurrencyCode": "986",
          "reconcilliationCurrencyCode": "986",
          "cardholderBillingCurrencyCode": "986",
          "transactionLifeCycleId": " MBK9999991207  ",
          "messageNumber": "00025718",
          "transactionDestinationInstitutionIdCode": "[card-hash]",
          "transactionOriginatorInstitutionIdCode": "006207",
          "receivingInstitutionIdCode": "099999",
          "correlationId": "[valid-uuid-correlation-id]",
          "orgId": "[tenant]",
          "caller": "Mastercard",
          "network": "Mastercard",
          "authorizationCode": "ABC123",
          "instituionId": "099999",
          "endpoint": "[endpointId]",
          "zeroBalanceUrl": null,
          "clearingType": "CREDIT",
          "category": null,
          "origin": null,
          "fileDate": "2022-12-07",
          "businessActivity": {
            "businessServiceArrangementTypeCode": "4",
            "corporateIncentiveRatesApplyIndicator": "N",
            "businessServiceIdCode": "076000",
            "masterPassIncentiveIndicator": "N",
            "specialsConditionsIndicator": "N",
            "interchangeRateDesignator": "HU",
            "rateIndicator": "N",
            "accountLevelManagementAccountCategoryCode": "N",
            "mastercardAssignedIdOverrideIndicator": "N",
            "centralSiteBusinessDate": "221208",
            "businessCycle": "04",
            "cardAcceptorClassificationOverrideIndicator": "0",
            "productClassOverrideIndicator": "MBK",
            "cardProgramIdentifier": "MCC"
          },
          "settlementData": {
            "settlementForeignExchangeRateClassCode": "N",
            "settlementServiceTransferAgentIdCode": "99999      ",
            "settlementServiceIdCode": "LA00098610",
            "settlementServiceLevelCode": "3",
            "settlementDate": "221207",
            "reconciliationCycle": "04",
            "settlementCycle": "01",
            "settlementServiceTransferAgentAccount": "0000000099999               ",
            "reconciliationDate": "221208"
          }
        }
      }
    }

  ```
</details>

<details>
  <summary>Mastercard T464 single message example - clearing event</summary>

  ```json
    {
      "event_id": "[valid-uuid]",
      "domain": "networktransactions",
      "event_type": "clearing",
      "schema_version": "1",
      "org_id": "[tenant]",
      "cid": "[valid-uuid-correlation-id]",
      "timestamp": "2022-12-08T10:00:00.761Z",
      "data": {
        "card_id": 99999,
        "account_id": 88888,
        "program_id": 123,
        "file_type": "T464",
        "network": "Mastercard",
        "raw_message": {
          "caller": "Mastercard",
          "transactionTime": "010905",
          "crossBorderCurrencyIndicator": "X",
          "correlationId": "[valid-uuid-correlation-id]",
          "currencyCodeSettlement": "986",
          "authorizationId": "ABC123",
          "interchangeFeeIndicator": "C",
          "clearingType": "DEBIT",
          "isaFeeIndicator": " ",
          "traceNumberAdjustmentTrans": "000000",
          "intracurrencyAgreementCode": "X986",
          "posEntry": "051",
          "processingCode": "002000",
          "messageTypeIndicator": "FREC",
          "completedAmountTransactionIndicator": "D",
          "requestedAmountTransaction": "000000010000",
          "processorId": "1507",
          "impliedDecimalTransaction": "2",
          "reconActivity": " ",
          "completedAmountTransaction": "000000010000",
          "zeroBalanceUrl": null,
          "traceNumber": "866999",
          "positiveIdIndicator": "4",
          "serviceLevelIndicator": "   ",
          "accessFee": "00000000",
          "messageNumber": "333855555",
          "cashBackAmountIndicator": "D",
          "recordType": "FREC",
          "transactionDate": "120722",
          "accessFeeIndicator": "D",
          "conversionRateSettlement": "11000000",
          "atmSurcharge": "N",
          "responseCodeDE39": "00",
          "brand": "MS2",
          "orgId": "[tenant]",
          "transactionDestinationInstitutionIdCode": "[card-hash]",
          "crossBorderIndicator": "N",
          "authorizationCode": "ABC123",
          "responseCode": "  ",
          "cashBackAmount": "000000000000",
          "network": "Mastercard",
          "referenceNumber": "777777799999",
          "merchantType": "5965",
          "acquirerInstitutionId": "1994444073",
          "pan": "[card-hash]",
          "impliedDecimalSettlement": "2",
          "endpoint": "[endpoint]",
          "currencyCodeTransaction": "986",
          "completedAmountSettlementIndicator": "D",
          "institutionId": null,
          "terminalId": "ABC88888  ",
          "processorType": "I",
          "adviceReasonCode": "       ",
          "completedAmountSettlement": "000000010000",
          "addendums": [
            {
              "caller": null,
              "cardIssuerInstitution": "1997777777",
              "correlationId": null,
              "merchantId": "340644440000000",
              "orgId": null,
              "account2Length": "19",
              "account2To": "0000000000000000000",
              "cardAcceptorCity": "Merchant City",
              "clearingType": "DEBIT",
              "standinTransaction": "N",
              "paymentTypeIndicator": "   ",
              "impliedDecimalCardholderBilling": "2",
              "transactionDestinationInstitutionIdCode": null,
              "authorizationCode": null,
              "amountIndicator": "D",
              "debitMastercardOffline": "N",
              "network": null,
              "messageTypeIndicator": "FPST",
              "processorId": "001507",
              "s3Path": null,
              "currencyCodeCardholderBilling": "986",
              "endpoint": null,
              "filler3": "                                   ",
              "account1From": "0000000000000000000",
              "cardAcceptorNameAddress": "MERCHANT NAME",
              "account1Length": "19",
              "zeroBalanceUrl": null,
              "paymentFacilitatorId": "00000249333",
              "amountCardholderBilling": "000000010000",
              "submerchantId": "000007777777804",
              "cardAcceptorStateOrCountryCode": "BRA",
              "institutionId": null,
              "posData": "00000000003",
              "messageNumber": null,
              "switchSerialNumber": "999999999",
              "filler1": "         ",
              "independentSalesOrganizationId": "           ",
              "filler2": "         ",
              "recordType": "FPST"
            }
          ],
          "interchangeFee": "0000000014",
          "switchSerialNumber": "999999999",
          "filler1": "          ",
          "panLength": "16",
          "filler2": "            "
        }
      }
  }
  ```
</details>

<details>
  <summary>Mastercard  fee collection  event example</summary>

  ```json
  {
     "event_id":"[valid-uuid]",
     "org_id":"[tenant]",
     "cid":"[valid-uuid-correlation-id]",
     "domain":"authorization",
     "event_type":"raw_credit_mastercard",
     "schema_version": "1"
     "timestamp":"2023-01-18T18:44:59Z",
     "data" : {
         "mti":"FEE_COLLECTION",
         "processingCode":{
            "transactionTypeCode":"19",
            "codeFromAccountTypeCode":"00",
            "codeToAccountTypeCode":"00"
         },
         "transactionAmount":1232,
         "reconciliationAmount":"34324543",
         "reconciliationConversionRate":"4324",
         "functionCode":783,
         "messageReasonCode":7804,
         "forwardingInstitutionIdCode":"002202",
         "additionalData":{
            "p0015":"2301130",
            "p0137":"19721830300000000",
            "currencyExponents":"5553",
            "businessActivity":"MMNN",
            "p0159":"234342",
            "settlementIndicator":"MMM****",
            "originatingMessageFormat":"2",
            "p1083":"X234"
         },
         "transactionCurrencyCode":"986",
         "reconcilliationCurrencyCode":"986",
         "messageNumber":"54535",
         "dataRecord":"FEES ",
         "dateAction":"230113",
         "transactionDestinationInstitutionIdCode":null,
         "transactionOriginatorInstitutionIdCode":"045532",
         "receivingInstitutionIdCode":"065332",
         "correlationId":"[cid]",
         "orgId":"[tenant]",
         "caller":"Mastercard",
         "network":"Mastercard",
         "authorizationCode":null,
         "instituionId":"345644",
         "endpoint":"004535",
         "zeroBalanceUrl":null,
         "clearingType":"CREDIT",
         "category":null,
         "origin":null,
         "file_date":"2023-01-14",
         "businessActivity":{
            "businessServiceArrangementTypeCode":"2",
            "corporateIncentiveRatesApplyIndicator":"N",
            "businessServiceIdCode":"076000",
            "masterPassIncentiveIndicator":"N",
            "specialsConditionsIndicator":"N",
            "interchangeRateDesignator":"  ",
            "rateIndicator":"N",
            "accountLevelManagementAccountCategoryCode":"N",
            "mastercardAssignedIdOverrideIndicator":"N",
            "centralSiteBusinessDate":"230114",
            "businessCycle":"04",
            "cardAcceptorClassificationOverrideIndicator":" ",
            "productClassOverrideIndicator":"   ",
            "cardProgramIdentifier":"MCC"
         },
         "settlementData":{
            "settlementForeignExchangeRateClassCode":"N",
            "settlementServiceTransferAgentIdCode":"23432      ",
            "settlementServiceIdCode":"AV34242",
            "settlementServiceLevelCode":"3",
            "settlementDate":"230113",
            "reconciliationCycle":"04",
            "settlementCycle":"01",
            "settlementServiceTransferAgentAccount":"2342342342",
            "reconciliationDate":"230114"
         },
         "localTransactionDateTime":{
            "date":"2023-01-18T04:16:25+0000",
            "time":"1970-01-01T18:44:59+0000"
         }
      }
  }
  ```
</details>

<details>
  <summary> Visa EPIN example - clearing event</summary>

  ```json
    {
      "event_id": "[valid-uuid]",
      "domain": "networktransactions",
      "event_type": "clearing",
      "schema_version": "1",
      "org_id": "[tenant]",
      "cid": "[valid-uuid-correlation-id]",
      "timestamp": "2022-12-08T03:00:00.813Z",
      "data": {
        "card_id": 99999,
        "account_id": 88888,
        "program_id": 123,
        "file_type": "EPIN",
        "network": "Visa",
        "raw_message": {
          "caller": "Visa",
          "org": null,
          "tcr02Data": {
            "nationalReimbursementFee": "0000000000",
            "reserved2": "",
            "installmentPaymentCount": "00",
            "specialMerchantIdentifier": "",
            "reserved3": "",
            "countryCode": "BR",
            "transactionSequenceNumber": "2",
            "specialPurchaseIdentifier": "",
            "transactionQualifier": "0",
            "centralProcessingDate": "0000",
            "transactionCode": "05",
            "settlementType": "027",
            "reserved": ""
          },
          "correlationId": "[valid-uuid-correlation-id]",
          "tcr03Data": null,
          "origin": null,
          "orgId": "[tenant]",
          "tcr0EData": null,
          "tcr05Data": {
            "additionalDataIndicator": "",
            "authorizationResponseCode": "00",
            "excludedTransactionIdenfierReason": "",
            "interchangeFeeSign": "C",
            "authorizedAmount": "000000010000",
            "transactionSequenceNumber": "5",
            "dynamicCurrencyConversionIndicator": "",
            "totalAuthorizedAmount": "000000000000",
            "baseCurrencyToDestinationCurrencyExchangeRate": "00000000",
            "multipleClearingSequenceNumber": "00",
            "reserved1": "",
            "informationIndicator": "N",
            "accountTypeIdentification": "",
            "chargebackRightsIndicator": "",
            "merchantTelephoneNumber": "",
            "multipleClearingSequenceCount": "00",
            "authorizationCurrencyCode": "986",
            "cvv2ResultCode": "",
            "transactionIdentifier": "123450770799999",
            "interchangeFeeAmount": "000000000199900",
            "crsProcessingCode": "",
            "productId": "N",
            "programId": "",
            "optionalIssuerISAAmount": "000000000000",
            "sourceCurrencyToBaseCurrencyExchangeRate": "00000000",
            "merchantVolumeIndicator": "",
            "validationCode": "",
            "merchantVerificationValue": "",
            "panToken": "0000000000000000",
            "transactionQualifier": "0",
            "transactionCode": "05",
            "marketSpecificAuthorizationDataIndicator": "",
            "spendQualifiedIndicator": "",
            "eletronicCommerceGoodsIndicator": ""
          },
          "transactionDestinationInstitutionIdCode": "[cardhash]",
          "authorizationCode": "ABC123",
          "type": "05",
          "zeroBalanceUrl": null,
          "fileDate": "2022-12-07",
          "tcr07Data": {
            "formFactorIndicator": "20700000",
            "issuerApplicationDataByte3": "0A",
            "cryptogramAmount": "000000010000",
            "terminalVerificationResults": "0000000000",
            "issuerApplicationDataByte8": "",
            "terminalCapabilityProfile": "E0D8C8",
            "applicationTransactionCounter": "027D",
            "issuerApplicationDataByte17": "",
            "issuerApplicationDataByte9to16": "",
            "transactionSequenceNumber": "7",
            "transactionType": "00",
            "issuerApplicationDataByte18to32": "",
            "issuerApplicationDataByte1": "06",
            "terminalCountryCode": "076",
            "applicationInterchangeProfile": "2000",
            "issuerApplicationDataByte4to7": "03A06000",
            "terminalTransactionDate": "221206",
            "issuerApplicationDataByte2": "01",
            "unpredictableNumber": "1234567F",
            "issuerScript1Results": "",
            "cryptogram": "ABC1239999977777",
            "transactionQualifier": "0",
            "transactionCode": "05",
            "cardSequenceNumber": "000",
            "terminalSerialNumber": ""
          },
          "tcr0DData": null,
          "tcr04Data": {
            "agentUniqueId": "",
            "transactionSequenceNumber": "4",
            "businessFormatCode": "SP",
            "transactionQualifier": "0",
            "dataContent": "0000                              00000000                                             00000000V005555509999999994425077777770000000000",
            "transactionCode": "05",
            "reserved": ""
          },
          "tcr06Data": null,
          "messageNumber": "999999",
          "tcr01Data": {
            "nationalReimbursementFee": "000000000000",
            "reserved2": "",
            "installmentPaymentCount": "01",
            "specialChargebackIndicator": "",
            "issuerCharge": "",
            "acceptanceTerminalIndicator": "",
            "reserved3": "0",
            "specialConditionIndicators": "",
            "prePaidCardIndicator": "",
            "transactionSequenceNumber": "1",
            "serviceDevelopmentField": "0",
            "cashback": "000000000",
            "reserved1": "",
            "documentationIndicator": "",
            "authorizationSourceCode": "V",
            "purchaseIdentifier": "",
            "posEnvironment": "",
            "tokenAssuredLevel": "",
            "mailPhoneEletronicIndicator": "",
            "purchaseIndentifierFormat": "",
            "accountSelection": "3",
            "feeProgramIndicator": "",
            "chargeBackReferenceNumber": "000000",
            "chipConditionCode": "0",
            "businessFormatCode": "",
            "transactionQualifier": "0",
            "memberMessageText": "0001007777700123499999",
            "terminalId": "AN779999",
            "transactionCode": "05",
            "cardAcceptorId": "00116659999",
            "additionalTokenResponse": "",
            "avsResponseCode": "",
            "conversionDate": "2341"
          },
          "tcr00Data": {
            "collectionOnlyFlag": "",
            "reimbursementAttribute": "A",
            "merchantName": "MerchantName",
            "usageCode": "1",
            "accountNumber": "[card-hash]",
            "destinationCurrencyCode": "986",
            "accountNumberExtension": "000",
            "acquirerBussinessId": "10074215",
            "transactionSequenceNumber": "0",
            "reserved1": "",
            "sourceAmount": "000000010000",
            "authorizationCode": "ABC123",
            "authorizationCharacteristicsIndicator": "E",
            "positiveCardholderAuthorizationServiceIndicator": "",
            "merchantZipCode": "99999",
            "settlementFlag": "8",
            "cardholderIdMethod": "1",
            "posTerminalCapabilities": "5",
            "posEntryMode": "07",
            "merchantCountryCode": "BR",
            "merchantCity": "MERCHANTCITY",
            "floorLimitIndicator": "B",
            "requestedPaymentService": "A",
            "destinationAmount": "000000010000",
            "acquirerReferenceNumber": "29999952340777777763331",
            "reasonCode": "00",
            "transactionQualifier": "0",
            "sourceCurrencyCode": "986",
            "centralProcessingDate": "2341",
            "transactionCode": "05",
            "purchaseDate": "1206",
            "merchantCategoryCode": "8999",
            "exceptionFileIndicator": "",
            "merchantStateProvinceCode": "",
            "numberOfPaymentForms": ""
          }
        }
      }
    }
  ```
</details>

<details>
  <summary> TecBan ServiceB example - clearing event</summary>

  ```json
    {
    "event_id": "[valid-uuid]",
    "domain": "networktransactions",
    "event_type": "clearing",
    "schema_version": "1",
    "org_id": "[tenant]",
    "cid": "[valid-uuid-correlation-id]",
    "timestamp": "2022-12-09T12:07:56.082Z",
    "data": {
      "card_id": 999999,
      "account_id": 888888,
      "program_id": 123,
      "file_type": "ServiceB",
      "network": "Tecban",
      "raw_message": {
        "caller": "TECBAN",
        "correlationId": "[valid-uuid-correlation-id]",
        "occurrenceRecord": null,
        "origin": null,
        "serviceTrailer": null,
        "headerFile": {
          "maskedPasswordForTransmission": "",
          "registryNsu": "00001",
          "physicalMeansTransportingFile": "T",
          "centralizingUnit": "01",
          "filler": "",
          "registrationCode": "A0",
          "extensionIndicator": "N",
          "financialInstituitionCode": "1208"
        },
        "orgId": "[tenant]",
        "transactionDestinationInstitutionIdCode": "[",
        "fileTrailer": null,
        "headerServiceFile": {
          "transmissionType": "1",
          "processingType": "2",
          "referenceData": "20221208",
          "onlineTransactionFormat": null,
          "currency": "RE",
          "registryNsu": "00002",
          "fileSequencialNumber": "0042",
          "processingSequencialNumber": "1065",
          "formatterOnlineTransactions": "2",
          "filler": "",
          "formatVersion": "03.6",
          "registrationCode": "B0",
          "extensionIndicator": "N"
        },
        "s3Path": null,
        "mainTransactionRecord": {
          "operationMode": "1",
          "transactionNsu": "999999",
          "transactionTime": "1713",
          "transactionDate": "1208",
          "operationUnitCode": "01",
          "viaCard": "0",
          "transactionAmount": "00000000002000",
          "registrationCode": "B1",
          "extensionIndicator": "S",
          "releaseDate": "1208",
          "numberOfInstallmentsForPaymentOfInstallments": "00",
          "billingIndicator": "1",
          "movementAccount": "[card-hash]",
          "registryNsu": "99999",
          "transactionStatus": "1",
          "accountTypeMovementTransaction": "1",
          "terminalId": "0061333",
          "transactionCode": "000100"
        },
        "zeroBalanceUrl": null,
        "messageNumber": "3643",
        "supplementTransactionRecord": {
          "transactionNsu": "999999",
          "transactionTime": "1713",
          "transactionDate": "1208",
          "operationUnitCode": "01",
          "backgroundCode": "0000000000",
          "protectionPassword": "0",
          "originCode": "0000",
          "hostNsu": "000999999",
          "registrationCode": "B2",
          "extensionIndicator": "N",
          "mainAccount": "[card-hash]",
          "chipIndicator": "2",
          "registryNsu": "03644",
          "language": "0",
          "terminalId": "0061574",
          "filler1": "0000",
          "filler2": "0"
        },
        "supplementOccurrenceRecord": null
      }
    }
  }
  ```
</details>

<details>
  <summary>ELO settlement file example - clearing event</summary>

  ```json
  {
      "messageNumber": "3",
      "transactionDestinationInstitutionIdCode": "S5mkas7SjpRypzwuVp33NKLTDQwoK5yD9DNCFyXVE7+2Cu3mWZYVLUOtfqowOZMvj0VJ9qD5ntOnJtAdqI0i1w==",
      "receivingInstitutionIdCode": "0623",
      "authorizationCode": "131573",
      "correlationId": "f83b4f68-7cef-4274-9667-df88d00dd11e",
      "s3Path": "TN-137dcf67-51c3-4e47-b1d0-677a9ec5405b/fromElo/000002/TE05/2025/86/00706233102C20250327184358_ENV.txt",
      "orgId": "TN-137dcf67-51c3-4e47-b1d0-677a9ec5405b",
      "zeroBalanceUrl": null,
      "origin": null,
      "endpoint": "000002",
      "encryptedPan": null,
      "fileDate": "2025-03-27",
      "partialRejectionCode": null,
      "headerServiceFile": {
          "serviceCode": "10",
          "shippingDate": "20250327",
          "shipmentNumber": "0117",
          "windowNumber": "1",
          "futureUse": "",
          "sendDate": "20250327",
          "shippingTimeArchive": "183632",
          "returnDateArchive": "20250327",
          "returnTimeArchive": "184225",
          "emittingBank": "0623",
          "codeProcessor": "3102",
          "futureUse1": "",
          "futureUse2": "0",
          "fileVersion": "251",
          "codeAcquirer": "0025",
          "flagCode": "007",
          "routeIndicatorArchive": "1",
          "transactionSubCode": "B0"
      },
      "mainDataRecord": null,
      "additionalDataRecord": null,
      "settlementCountryDataRecord": null,
      "registrationFundsTransferData": null,
      "registrationPaymentServiceData": null,
      "cardChipDataRegistration": null,
      "airlineDataRegistration": null,
      "recordReasonPartialRejection": null,
      "mainDataForFinancialDisput": null,
      "additionalDataForFinancialDisput": null,
      "mainDataForFraudWarning": {
          "transactionCode": "40",
          "cardNumber": "S5mkas7SjpRypzwuVp33NKLTEQwoK5yD9DNCFyXVE7+2Cu3mWZYVLUOtfqowOZMvj0VJ9qD5ntOfJtBdqI0i1w==",
          "cardNumberComplement": "",
          "transactionReferenceNumber": "20000255086483859640370",
          "futureUse": "0000",
          "acquirerCode": "0025",
          "dateOfSale": "20250327",
          "codeOfError": "I20",
          "futureUse2": "",
          "idOfReferenceOfFlag": "192159595157611",
          "pointOfSaleCity": "BARUERI",
          "pointOfSaleCountryCode": "BR",
          "pointOfSaleMcc": "5411",
          "valueOfFraud": "000000000200",
          "currencyCodeFraudulent": "986",
          "dateNotificationFraud": "20210211",
          "indicatorOriginAuthorization": "Y",
          "codeNotification": "1",
          "typeFraud": "10",
          "dateMaturityCard": "1130",
          "futureUse3": "0000000000",
          "typePlatform": "CR",
          "codeFlag": "007",
          "futureUse4": "0",
          "futureUse5": "0000",
          "futureUse6": "",
          "transactionSubCode": "00"
      },
      "additionalDataForFraudWarning": {
          "transactionCode": "40",
          "identifierTransaction": "652400000001",
          "futureUse": "",
          "futureUse2": "00",
          "pointOfSale": "19132053000194",
          "logicalNumberEquipment": "20172289",
          "futureUse3": "",
          "indicatorTransactionThing": "N",
          "codeAuthorizationTransaction": "131573",
          "middleIdentificationCarrier": "1",
          "inputModeTransactionPOS": "07",
          "identificationTechnologyTerminal": "V",
          "technologyCard": "C",
          "futureUse4": "",
          "changeValue": "000000000",
          "futureUse5": "",
          "indicatorOfTransactionOrigin": "0",
          "cardholderZipCode": "0009910500",
          "cityCarrier": "DIADEMA",
          "stateHolder": "SP",
          "dateConfirmationFraud": "20210211",
          "indicatorSaleOff": "8",
          "nameCarrier": "DANILO CASTRO",
          "tokenPAN": "",
          "futureUse6": "",
          "transactionSubCode": "02"
      },
      "serviceTrailer": {
          "transactionSubCode": "BZ",
          "serviceCode": "10",
          "shipmentNumber": "0117",
          "quantityOfCreditTransactionsUsingReal": "00000000",
          "totalValueOfCreditTransactionsUsingReal": "000000000000000",
          "quantityOfDebitTransactionsUsingReal": "00000000",
          "totalValueOfDebitTransactionsUsingReal": "000000000000000",
          "quantityOfCreditTransactionsUsingDollar": "00000000",
          "totalValueOfCreditTransactionsUsingDollar": "000000000000000",
          "quantityOfDebitTransactionsUsingDollar": "00000000",
          "totalValueOfDebitTransactionsUsingDollar": "000000000000000",
          "totalQuantityRecords": "00000004",
          "futureUse1": "00000000",
          "futureUse2": "000000000000000",
          "quantityOfCreditTransactionsUsingRealRejectedByElo": "000000",
          "totalValueOfCreditTransactionsUsingRealRejectedByElo": "000000000000",
          "quantityOfDebitTransactionsUsingRealRejectedByElo": "000000",
          "totalValueOfDebitTransactionsUsingRealRejectedByElo": "000000000000",
          "routeIndicatorArchive": "1"
      },
      "caller": "ELO"
  }
  ```
</details>

#### Clearing reconciliation

<Callout icon="📘" theme="info">
  If a problem is encountered during the clearing process for Clearing/Base II authorization events, a report is sent from the Dead Letter Queue (DLQ) stating that the unprocessed clearing message needs to be reconciled. All messages that are sent to the DLQ can be reconciled and reprocessed through the [clearing-reconciliation](https://developers.pismo.io/pismo-docs/reference/performclearingreconciliation) endpoint.

  This endpoint allows you to take over the reprocessing of messages in the DLQ, assuming the responsibility to reconcile unprocessed clearing message sent to DLQ. All messages that have been sent to the DLQ can be reconciled through this endpoint.

  Note: This endpoint is available only for Visa and Mastercard and is not available for ELO.

  Once common scenario for this would be a Cancellation/Confirmation/Installment with a Julian date error.

  * Issue—This issue occurs when Pismo receives a Base II / Clearing that contains a Julian date smaller than the last one processed.
  * Action—Adjust Julian Date field and perform the reconciliation. Note that the field that represents the Julian Date varies according to the card brand.
  * Example:

  ```
  curl --location '[valid-test-environment-url]' \
  --header 'x-tenant: [tenant]' \
  --header 'x-cid: [valid-uuid-correlation-id]' \
  --header 'Content-Type: application/json' \
  --data '{
    "card_network": "[network name]",
    "card_hash": "[card-hash]",
    "reconciliation_reason": "INVALID_JULIAN_DATE",
    "adjustments": [
      {
        "field": "julianProcessingDate",     
        "new_value": "5040"
      }
     ]
  }'
  ```
</Callout>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/clearing-reconciliation` | `performClearingReconciliation` | Perform clearing reconciliation | `api-specs/Card_issuing_-_Reconciliation.yaml` | no | KU-API-card-issuing-reconciliation--network-transactions-backoffice |

### Operation essentials

- **`POST /v1/clearing-reconciliation`** (`performClearingReconciliation`): security `BearerAuth`; required parameters none declared; required body fields `card_network`, `card_hash`, `reconciliation_reason`; response statuses 202, 400, 401, 403, 404, 500; error codes in examples none; events none listed.

## Events

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `networktransactions-network-authorization-1` | networktransactions | 1 | https://developers.pismo.io/events/docs/networktransactions-network-authorization-1 | 2 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/authorization-events.md`: updatedAt 2026-06-26T15:38:51.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 21 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/authorization-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/authorization-events | `945278ecf54fbe95…` | 2026-06-26T15:38:51.000Z |

## Related knowledge units

- `KU-API-card-issuing-reconciliation--network-transactions-backoffice` — API reference: Card issuing - Reconciliation — Network transactions backoffice
- `KU-CARD-full-and-zero-balance-workflows` — Full and Zero balance transaction workflows
- `KU-CARD-linking-events-in-an-authorization-workflow` — Linking authorization events
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-timeline-overview` — Timeline events
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
