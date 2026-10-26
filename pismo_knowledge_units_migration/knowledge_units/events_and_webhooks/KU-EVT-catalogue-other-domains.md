---
ku_id: KU-EVT-catalogue-other-domains
title: 'Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)'
category: events_and_webhooks
ku_type: event_catalogue
lifecycle: current
sources:
- path: api-reference-data/event_type_inventory.csv
  sha256: 7eed7e3056f6f22e154bae7f22d25760a66c9e243ee0367953d1e935f823aed5
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- CopyProgram
- CopyProgramAsync
- CreateAccountingEntry
- CreateProcessingCode
- CreateProgramBasedOnTemplate
- CreateProgramBasedOnTemplateAsync
- ProcessingCodeUpdate
- ReversalProcessingCode
- UpdateProgramInfo
- advance-pix-out-execution
- bookLoanV2
- cancel-network-authorizations
- cancel-pix-out-execution
- cash-management-v2-post-cancel-payments
- cash-management-v2-post-confirm-payments
- cash-management-v2-post-payments
- cash-management-v2-post-scheduled-payments
- corporate-post-v1-checks
- corporate-v2-post-cancel-payments
- corporate-v2-post-confirm-payments
- corporate-v2-post-multileg-payments
- corporate-v2-post-payments
- corporate-v2-post-scheduled-payments
- corporate-v3-post-multileg-payments
- create-payment-agreement-simulation
- delete-cancel-pix-out
- delete-corporate-v1-channels
- delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name
- delinquent-account-closure-post
- dlq-update-clearing-rules
- emi-select
- get-v1-bulletin-rule
- interest-bearing-calculate-average-balance
- interest-bearing-v1-create-savings-account-product
- interest-bearing-v1-patch-savings-account-product
- patch-acquisitions-v2-s2s-applications
- patch-cash-management-v2-earmarks-earmarkid
- patch-corporate-v1-channels-channel
- patch-corporate-v1-restricted-funds
- patch-corporate-v2-earmarks-earmarkid
- patch-corporate-v2-restricted-funds
- patch-v1-account-limit
- patch-v1-account-limits
- post-account
- post-acquisitions-v2-s2s-applications
- post-acquisitions-v3-s2s-applications
- post-authorization
- post-cash-management-v2-earmarks
- post-cash-management-v2-earmarks-earmarkid-cancel
- post-corporate-v1-channels
- post-corporate-v1-checks-checkId-cancel
- post-corporate-v1-checks-release
- post-corporate-v1-restricted-funds
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-funds-transfer
- post-integrated-payments-api-v1-bankslips-pay
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-ach
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-bban
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-clabe
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-fedwire
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan
- post-payment-confirm
- post-payments
- post-payments-cancel
- post-payments-v1-force
- post-payments-v1-force-cancel
- post-payments-v1-hold-funds-block
- post-payments-v1-hold-funds-transfer
- post-payments-v1-hold-funds-transfer-cancel
- post-payments-v1-hold-funds-unblock
- post-payments-v1-installments
- post-payments-v1-installments-cancel
- post-payments-v1-payments
- post-payments-v2-cancel
- post-schedule-pix-payment
- post-transfers
- post-transfers-cancel
- post-transfers-confirm
- post-v1-bulletin-setup
- post-v2-fraud-report
- postProgramImport
- post_v1-authorizations
- put-v2-fraud-report
- update-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name
related_kus:
- KU-API-banking-bank-accounts--bank-accounts-part-01
- KU-API-banking-bank-accounts--bank-accounts-part-02
- KU-API-banking-integrated-payments--bank-slip
- KU-API-banking-interest-bearing-accounts--average-balance
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--channels
- KU-API-banking-transaction-banking--check-posting
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--earmarking-pismo-account-id
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--payments-pismo-account-id
- KU-API-banking-transaction-banking--restricted-funds
- KU-API-card-issuing-authorization--authorizations
- KU-API-card-issuing-disputes--fraud-report
- KU-API-card-issuing-protection-bulletin--rules
- KU-API-core-platform-accounting--accounting-entry
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-balances-and-limits--account-limits
- KU-API-core-platform-ledger--account-limits
- KU-API-core-platform-payment-methods--force-operations
- KU-API-core-platform-payment-methods--hold-funds
- KU-API-core-platform-payment-methods--installments-payments
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-API-core-platform-payment-methods--payment-methods-part-03
- KU-API-core-platform-payment-methods--payments
- KU-API-instant-payments-pix-payments--scheduled-transfers-v2
- KU-API-instant-payments-rupay-on-upi--upi
- KU-API-lending--loans
- KU-API-pismo-clearing-rules-engine--clearing-rules
- KU-API-platform-setup-orgs-operation--processing-codes
- KU-API-platform-setup-orgs-operation--reversal-processing-codes
- KU-API-platform-setup-programs--export-and-import
- KU-API-platform-setup-programs--programs-part-01
- KU-API-platform-setup-programs--programs-part-02
- KU-API-revolving-credit-delinquent-account--delinquent-account-closure
- KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation
- KU-BANK-banking-overview
- KU-BANK-dated-transactions
- KU-CARD-authorization-events
- KU-CARD-authorization-validation-rules-for-card-network-operations
- KU-CARD-card-tokenization-process-and-onboarding
- KU-CARD-clearing
- KU-CARD-full-and-zero-balance-workflows
- KU-CARD-simulate-authorizations
- KU-CARD-visa-dispute-use-case
- KU-CORE-over-limit-fee
- KU-CORE-transactions-overview
- KU-CORE-transactiontypes
- KU-CRED-credit-liquidation
- KU-ERR-validation-code-definitions
- KU-EVT-accounting-data-events
- KU-EVT-accounts-data-events
- KU-EVT-bank-slips-data-events
- KU-EVT-client-webhooks-part-13
- KU-EVT-corporate-banking-data-events
- KU-EVT-delinquency-account-data-events
- KU-EVT-disputes-endpoint-generated-events
- KU-EVT-interest-management-data-events
- KU-EVT-international-bank-accounts-data-events
- KU-EVT-ledger-data-events
- KU-EVT-payments-data-events
- KU-LEND-book-a-loan
- KU-PAY-bank-slips
- KU-PAY-check-posting-and-settlement
- KU-PAY-faster-payment-system
- KU-PAY-hold-funds
- KU-PAY-installments-payment
- KU-PAY-payment-methods
events:
- accounting-entry-creation-1
- authorization-authorization-cancellation-event-1
- authorization-authorization-event-1
- availables-change-available-1
- average-balance-calculated-average-balance-1
- bulletin-bulletin-rule-1
- cash-management-channel-1
- cash-management-check-status-change-1
- delinquent-account-delinquent-account-1
- fraud-report-fraud-report-change-1
- fraud-report-fraud-report-creation-1
- instantpay-scheduler-execution-status-change-1
- instantpay-scheduler-scheduler-status-change-1
- intl-bankaccounts-intl-bankaccount-register-1
- intl-bankaccounts-intl-bankaccount-update-1
- ledger-limit-changed-1
- networktransactions-network-authorization-1
- networktransactions-pending-transactions-2
- onboarding-prospect-1
- onboarding-succeeded-1
- orgs-operation-create-1
- orgs-operation-update-1
- payment-methods-authorization-1
- platform-authorization-platform-authorization-1
- programs-creation-1
- programs-update-1
- rules-evaluation-requested-1
- savings-account-product-creation-1
- savings-account-product-update-1
- statement-refinancing-payment-agreement-simulation-not-processed-1
---

# Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)

**KU ID:** `KU-EVT-catalogue-other-domains` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 30 event type(s) whose inventory domain is accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `accounting-entry-creation-1` | accounting | 1 | https://developers.pismo.io/events/docs/accounting-entry-creation-1 | 4 | Banking_-_Transaction_banking;Core_platform_-_Accounting |
| `authorization-authorization-cancellation-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-cancellation-event-1 | 2 | Core_platform_-_Payment_methods |
| `authorization-authorization-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-event-1 | 9 | Banking_-_Integrated_payments;Core_platform_-_Payment_methods |
| `availables-change-available-1` | availables | 1 | https://developers.pismo.io/events/docs/availables-change-available-1 | 22 | Banking_-_Transaction_banking;Core_platform_-_Payment_methods |
| `average-balance-calculated-average-balance-1` | average | 1 | https://developers.pismo.io/events/docs/average-balance-calculated-average-balance-1 | 1 | Banking_-_Interest-bearing_accounts |
| `bulletin-bulletin-rule-1` | bulletin | 1 | https://developers.pismo.io/events/docs/bulletin-bulletin-rule-1 | 2 | Card_issuing_-_Protection_Bulletin |
| `cash-management-channel-1` | cash | 1 | https://developers.pismo.io/events/docs/cash-management-channel-1 | 3 | Banking_-_Transaction_banking |
| `cash-management-check-status-change-1` | cash | 1 | https://developers.pismo.io/events/docs/cash-management-check-status-change-1 | 3 | Banking_-_Transaction_banking |
| `delinquent-account-delinquent-account-1` | delinquent | 1 | https://developers.pismo.io/events/docs/delinquent-account-delinquent-account-1 | 1 | Revolving_credit_-_Delinquent_account |
| `fraud-report-fraud-report-change-1` | fraud | 1 | https://developers.pismo.io/events/docs/fraud-report-fraud-report-change-1 | 1 | Card_issuing_-_Disputes |
| `fraud-report-fraud-report-creation-1` | fraud | 1 | https://developers.pismo.io/events/docs/fraud-report-fraud-report-creation-1 | 1 | Card_issuing_-_Disputes |
| `instantpay-scheduler-execution-status-change-1` | instantpay | 1 | https://developers.pismo.io/events/docs/instantpay-scheduler-execution-status-change-1 | 2 | Instant_payments_-_Pix_payments |
| `instantpay-scheduler-scheduler-status-change-1` | instantpay | 1 | https://developers.pismo.io/events/docs/instantpay-scheduler-scheduler-status-change-1 | 2 | Instant_payments_-_Pix_payments |
| `intl-bankaccounts-intl-bankaccount-register-1` | intl | 1 | https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1 | 7 | Banking_-_Bank_accounts |
| `intl-bankaccounts-intl-bankaccount-update-1` | intl | 1 | https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-update-1 | 2 | Banking_-_Bank_accounts |
| `ledger-limit-changed-1` | ledger | 1 | https://developers.pismo.io/events/docs/ledger-limit-changed-1 | 2 | Core_platform_-_Balances_and_limits;Core_platform_-_Ledger |
| `networktransactions-network-authorization-1` | networktransactions | 1 | https://developers.pismo.io/events/docs/networktransactions-network-authorization-1 | 2 | Card_issuing_-_Authorization |
| `networktransactions-pending-transactions-2` | networktransactions | 2 | https://developers.pismo.io/events/docs/networktransactions-pending-transactions-2 | 1 | Pismo_clearing_rules_engine |
| `onboarding-prospect-1` | onboarding | 1 | https://developers.pismo.io/events/docs/onboarding-prospect-1 | 2 | Core_platform_-_Accounts |
| `onboarding-succeeded-1` | onboarding | 1 | https://developers.pismo.io/events/docs/onboarding-succeeded-1 | 4 | Banking_-_Transaction_banking;Core_platform_-_Accounts |
| `orgs-operation-create-1` | orgs | 1 | https://developers.pismo.io/events/docs/orgs-operation-create-1 | 2 | Platform_setup_-_Orgs_Operation |
| `orgs-operation-update-1` | orgs | 1 | https://developers.pismo.io/events/docs/orgs-operation-update-1 | 1 | Platform_setup_-_Orgs_Operation |
| `payment-methods-authorization-1` | payment | 1 | https://developers.pismo.io/events/docs/payment-methods-authorization-1 | 3 | Core_platform_-_Payment_methods;Instant_payments_-_RuPay_on_UPI |
| `platform-authorization-platform-authorization-1` | platform | 1 | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 | 32 | Banking_-_Transaction_banking;Core_platform_-_Payment_methods;Instant_payments_-_RuPay_on_UPI;Lending |
| `programs-creation-1` | programs | 1 | https://developers.pismo.io/events/docs/programs-creation-1 | 5 | Platform_setup_-_Programs |
| `programs-update-1` | programs | 1 | https://developers.pismo.io/events/docs/programs-update-1 | 1 | Platform_setup_-_Programs |
| `rules-evaluation-requested-1` | rules | 1 | https://developers.pismo.io/events/docs/rules-evaluation-requested-1 | 4 | Banking_-_Transaction_banking |
| `savings-account-product-creation-1` | savings | 1 | https://developers.pismo.io/events/docs/savings-account-product-creation-1 | 1 | Banking_-_Interest-bearing_accounts |
| `savings-account-product-update-1` | savings | 1 | https://developers.pismo.io/events/docs/savings-account-product-update-1 | 1 | Banking_-_Interest-bearing_accounts |
| `statement-refinancing-payment-agreement-simulation-not-processed-1` | statement | 1 | https://developers.pismo.io/events/docs/statement-refinancing-payment-agreement-simulation-not-processed-1 | 1 | Revolving_credit_-_Statement_refinancing_API |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `accounting-entry-creation-1` | `POST /corporate/v2/payments` | `corporate-v2-post-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `accounting-entry-creation-1` | `POST /corporate/v2/payments/multileg` | `corporate-v2-post-multileg-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-03 |
| `accounting-entry-creation-1` | `POST /cash-management/v2/payments` | `cash-management-v2-post-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `accounting-entry-creation-1` | `POST /v1/accounting-entries` | `CreateAccountingEntry` | `Core_platform_-_Accounting` | KU-API-core-platform-accounting--accounting-entry |
| `authorization-authorization-cancellation-event-1` | `POST /payments/v1/payments/force/cancel` | `post-payments-v1-force-cancel` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--force-operations |
| `authorization-authorization-cancellation-event-1` | `POST /payments/v2/cancel` | `post-payments-v2-cancel` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--payments |
| `authorization-authorization-event-1` | `POST /v1/bankslips/pay` | `post-integrated-payments-api-v1-bankslips-pay` | `Banking_-_Integrated_payments` | KU-API-banking-integrated-payments--bank-slip |
| `authorization-authorization-event-1` | `POST /payments/v1/payments` | `post-payments-v1-payments` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--payments |
| `authorization-authorization-event-1` | `POST /payments/v1/payments/force` | `post-payments-v1-force` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--force-operations |
| `authorization-authorization-event-1` | `POST /payments/v1/payments/hold-funds/block` | `post-payments-v1-hold-funds-block` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--hold-funds |
| `authorization-authorization-event-1` | `POST /payments/v1/payments/hold-funds/unblock` | `post-payments-v1-hold-funds-unblock` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--hold-funds |
| `authorization-authorization-event-1` | `POST /payments/v1/payments/hold-funds/transfer` | `post-payments-v1-hold-funds-transfer` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--hold-funds |
| `authorization-authorization-event-1` | `POST /payments/v1/payments/hold-funds/transfer/cancel` | `post-payments-v1-hold-funds-transfer-cancel` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--hold-funds |
| `authorization-authorization-event-1` | `POST /payments/v1/payments/installments` | `post-payments-v1-installments` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--installments-payments |
| `authorization-authorization-event-1` | `POST /payments/v1/payments/installments/cancel` | `post-payments-v1-installments-cancel` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--installments-payments |
| `availables-change-available-1` | `POST /corporate/v2/earmarks` | `post-corporate-v2-earmarks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `availables-change-available-1` | `PATCH /corporate/v2/earmarks/{earmarkId}` | `patch-corporate-v2-earmarks-earmarkid` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `availables-change-available-1` | `POST /corporate/v2/earmarks/{earmarkId}/cancel` | `post-corporate-v2-earmarks-earmarkid-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `availables-change-available-1` | `POST /corporate/v2/payments` | `corporate-v2-post-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `availables-change-available-1` | `POST /corporate/v2/payments/confirm` | `corporate-v2-post-confirm-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `availables-change-available-1` | `POST /corporate/v2/payments/cancel` | `corporate-v2-post-cancel-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `availables-change-available-1` | `POST /corporate/v2/scheduled-payments` | `corporate-v2-post-scheduled-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-02 |
| `availables-change-available-1` | `POST /corporate/v2/payments/multileg` | `corporate-v2-post-multileg-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-03 |
| `availables-change-available-1` | `POST /corporate/v1/restricted-funds` | `post-corporate-v1-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `availables-change-available-1` | `PATCH /corporate/v1/restricted-funds/{restrictedFundsId}` | `patch-corporate-v1-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `availables-change-available-1` | `PATCH /corporate/v2/restricted-funds/{restrictedFundsId}` | `patch-corporate-v2-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `availables-change-available-1` | `POST /cash-management/v2/payments` | `cash-management-v2-post-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `availables-change-available-1` | `POST /cash-management/v2/payments/confirm` | `cash-management-v2-post-confirm-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `availables-change-available-1` | `POST /cash-management/v2/payments/cancel` | `cash-management-v2-post-cancel-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `availables-change-available-1` | `POST /cash-management/v2/scheduled-payments` | `cash-management-v2-post-scheduled-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `availables-change-available-1` | `POST /cash-management/v2/earmarks` | `post-cash-management-v2-earmarks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `availables-change-available-1` | `PATCH /cash-management/v2/earmarks/{earmarkId}` | `patch-cash-management-v2-earmarks-earmarkid` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `availables-change-available-1` | `POST /cash-management/v2/earmarks/{earmarkId}/cancel` | `post-cash-management-v2-earmarks-earmarkid-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `availables-change-available-1` | `POST /payments/v1/payments/hold-funds/block` | `post-payments-v1-hold-funds-block` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--hold-funds |
| `availables-change-available-1` | `POST /payments/v1/payments/hold-funds/unblock` | `post-payments-v1-hold-funds-unblock` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--hold-funds |
| `availables-change-available-1` | `POST /payments/v1/payments/hold-funds/transfer` | `post-payments-v1-hold-funds-transfer` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--hold-funds |
| `availables-change-available-1` | `POST /payments/v1/payments/hold-funds/transfer/cancel` | `post-payments-v1-hold-funds-transfer-cancel` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--hold-funds |
| `average-balance-calculated-average-balance-1` | `POST /v1/accounts/{accountId}/average-balance` | `interest-bearing-calculate-average-balance` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--average-balance |
| `bulletin-bulletin-rule-1` | `POST /v1/bulletin/setup` | `post-v1-bulletin-setup` | `Card_issuing_-_Protection_Bulletin` | KU-API-card-issuing-protection-bulletin--rules |
| `bulletin-bulletin-rule-1` | `GET /v1/bulletin/setup/{program_id}` | `get-v1-bulletin-rule` | `Card_issuing_-_Protection_Bulletin` | KU-API-card-issuing-protection-bulletin--rules |
| `cash-management-channel-1` | `POST /corporate/v1/channels` | `post-corporate-v1-channels` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--channels |
| `cash-management-channel-1` | `PATCH /corporate/v1/channels/{channel}` | `patch-corporate-v1-channels-channel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--channels |
| `cash-management-channel-1` | `DELETE /corporate/v1/channels/{channel}` | `delete-corporate-v1-channels` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--channels |
| `cash-management-check-status-change-1` | `POST /corporate/v1/checks` | `corporate-post-v1-checks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--check-posting |
| `cash-management-check-status-change-1` | `POST /corporate/v1/checks/release` | `post-corporate-v1-checks-release` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--check-posting |
| `cash-management-check-status-change-1` | `POST /corporate/v1/checks/{checkId}/cancel` | `post-corporate-v1-checks-checkId-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--check-posting |
| `delinquent-account-delinquent-account-1` | `POST /v1/accounts/{account_id}/close` | `delinquent-account-closure-post` | `Revolving_credit_-_Delinquent_account` | KU-API-revolving-credit-delinquent-account--delinquent-account-closure |
| `fraud-report-fraud-report-change-1` | `PUT /v2/fraud-report/{fraudReportId}` | `put-v2-fraud-report` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--fraud-report |
| `fraud-report-fraud-report-creation-1` | `POST /v2/fraud-report` | `post-v2-fraud-report` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--fraud-report |
| `instantpay-scheduler-execution-status-change-1` | `POST /pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id}/advance` | `advance-pix-out-execution` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `instantpay-scheduler-execution-status-change-1` | `DELETE /pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id}` | `cancel-pix-out-execution` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `instantpay-scheduler-scheduler-status-change-1` | `POST /pix/v2/pix/out/scheduler` | `post-schedule-pix-payment` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `instantpay-scheduler-scheduler-status-change-1` | `DELETE /pix/v2/pix/out/scheduler/{scheduler_id}` | `delete-cancel-pix-out` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `intl-bankaccounts-intl-bankaccount-register-1` | `POST /v2/accounts/{accountId}/bank-accounts/iban` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban` | `Banking_-_Bank_accounts` | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `intl-bankaccounts-intl-bankaccount-register-1` | `POST /v2/accounts/{accountId}/bank-accounts/ach` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-ach` | `Banking_-_Bank_accounts` | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `intl-bankaccounts-intl-bankaccount-register-1` | `POST /v2/accounts/{accountId}/bank-accounts/fedwire` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-fedwire` | `Banking_-_Bank_accounts` | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `intl-bankaccounts-intl-bankaccount-register-1` | `POST /v2/accounts/{accountId}/bank-accounts/clabe` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-clabe` | `Banking_-_Bank_accounts` | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `intl-bankaccounts-intl-bankaccount-register-1` | `POST /v2/accounts/{accountId}/bank-accounts/uk-scan` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan` | `Banking_-_Bank_accounts` | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `intl-bankaccounts-intl-bankaccount-register-1` | `POST /v2/accounts/{accountId}/bank-accounts/brazil` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil` | `Banking_-_Bank_accounts` | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `intl-bankaccounts-intl-bankaccount-register-1` | `POST /v2/accounts/{accountId}/bank-accounts/bban` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-bban` | `Banking_-_Bank_accounts` | KU-API-banking-bank-accounts--bank-accounts-part-02 |
| `intl-bankaccounts-intl-bankaccount-update-1` | `DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName}` | `delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name` | `Banking_-_Bank_accounts` | KU-API-banking-bank-accounts--bank-accounts-part-02 |
| `intl-bankaccounts-intl-bankaccount-update-1` | `PATCH /v2/accounts/{accountId}/bank-accounts/{schemeName}` | `update-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name` | `Banking_-_Bank_accounts` | KU-API-banking-bank-accounts--bank-accounts-part-02 |
| `ledger-limit-changed-1` | `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limits` | `Core_platform_-_Balances_and_limits` | KU-API-core-platform-balances-and-limits--account-limits |
| `ledger-limit-changed-1` | `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limit` | `Core_platform_-_Ledger` | KU-API-core-platform-ledger--account-limits |
| `networktransactions-network-authorization-1` | `POST /networktransactions/v1/authorizations` | `post_v1-authorizations` | `Card_issuing_-_Authorization` | KU-API-card-issuing-authorization--authorizations |
| `networktransactions-network-authorization-1` | `POST /direct-network-transactions/v1/cancellation` | `cancel-network-authorizations` | `Card_issuing_-_Authorization` | KU-API-card-issuing-authorization--authorizations |
| `networktransactions-pending-transactions-2` | `PUT /v1/rules` | `dlq-update-clearing-rules` | `Pismo_clearing_rules_engine` | KU-API-pismo-clearing-rules-engine--clearing-rules |
| `onboarding-prospect-1` | `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--accounts |
| `onboarding-prospect-1` | `POST /acquisitions/v2/s2s/applications` | `post-acquisitions-v2-s2s-applications` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--accounts |
| `onboarding-succeeded-1` | `POST /corporate/v1/corporate-accounts` | `post-account` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--accounts |
| `onboarding-succeeded-1` | `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--accounts |
| `onboarding-succeeded-1` | `PATCH /acquisitions/v2/s2s/applications/{applicationId}` | `patch-acquisitions-v2-s2s-applications` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--accounts |
| `onboarding-succeeded-1` | `POST /acquisitions/v2/s2s/applications` | `post-acquisitions-v2-s2s-applications` | `Core_platform_-_Accounts` | KU-API-core-platform-accounts--accounts |
| `orgs-operation-create-1` | `POST /orgs-operation/v1/processing-codes` | `CreateProcessingCode` | `Platform_setup_-_Orgs_Operation` | KU-API-platform-setup-orgs-operation--processing-codes |
| `orgs-operation-create-1` | `POST /orgs-operation/v1/reversal-processing-codes` | `ReversalProcessingCode` | `Platform_setup_-_Orgs_Operation` | KU-API-platform-setup-orgs-operation--reversal-processing-codes |
| `orgs-operation-update-1` | `PATCH /orgs-operation/v1/processing-codes/{processingCode}` | `ProcessingCodeUpdate` | `Platform_setup_-_Orgs_Operation` | KU-API-platform-setup-orgs-operation--processing-codes |
| `payment-methods-authorization-1` | `POST /payment-methods/v1/authorization` | `post-authorization` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `payment-methods-authorization-1` | `POST /v1/cards/transfer` | `post-funds-transfer` | `Instant_payments_-_RuPay_on_UPI` | KU-API-instant-payments-rupay-on-upi--upi |
| `payment-methods-authorization-1` | `POST /v1/cards/emi-select` | `emi-select` | `Instant_payments_-_RuPay_on_UPI` | KU-API-instant-payments-rupay-on-upi--upi |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v2/earmarks` | `post-corporate-v2-earmarks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `platform-authorization-platform-authorization-1` | `PATCH /corporate/v2/earmarks/{earmarkId}` | `patch-corporate-v2-earmarks-earmarkid` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v2/earmarks/{earmarkId}/cancel` | `post-corporate-v2-earmarks-earmarkid-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v2/payments` | `corporate-v2-post-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v2/payments/confirm` | `corporate-v2-post-confirm-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v2/payments/cancel` | `corporate-v2-post-cancel-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v3/payments/multileg` | `corporate-v3-post-multileg-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v2/scheduled-payments` | `corporate-v2-post-scheduled-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-02 |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v2/payments/multileg` | `corporate-v2-post-multileg-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-03 |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v1/checks` | `corporate-post-v1-checks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--check-posting |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v1/checks/release` | `post-corporate-v1-checks-release` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--check-posting |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v1/checks/{checkId}/cancel` | `post-corporate-v1-checks-checkId-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--check-posting |
| `platform-authorization-platform-authorization-1` | `POST /corporate/v1/restricted-funds` | `post-corporate-v1-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `platform-authorization-platform-authorization-1` | `PATCH /corporate/v1/restricted-funds/{restrictedFundsId}` | `patch-corporate-v1-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `platform-authorization-platform-authorization-1` | `PATCH /corporate/v2/restricted-funds/{restrictedFundsId}` | `patch-corporate-v2-restricted-funds` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--restricted-funds |
| `platform-authorization-platform-authorization-1` | `POST /cash-management/v2/payments` | `cash-management-v2-post-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `platform-authorization-platform-authorization-1` | `POST /cash-management/v2/payments/confirm` | `cash-management-v2-post-confirm-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `platform-authorization-platform-authorization-1` | `POST /cash-management/v2/payments/cancel` | `cash-management-v2-post-cancel-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `platform-authorization-platform-authorization-1` | `POST /cash-management/v2/scheduled-payments` | `cash-management-v2-post-scheduled-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `platform-authorization-platform-authorization-1` | `POST /cash-management/v2/earmarks` | `post-cash-management-v2-earmarks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `platform-authorization-platform-authorization-1` | `PATCH /cash-management/v2/earmarks/{earmarkId}` | `patch-cash-management-v2-earmarks-earmarkid` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `platform-authorization-platform-authorization-1` | `POST /cash-management/v2/earmarks/{earmarkId}/cancel` | `post-cash-management-v2-earmarks-earmarkid-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `platform-authorization-platform-authorization-1` | `POST /payment-methods/v1/authorization` | `post-authorization` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `platform-authorization-platform-authorization-1` | `POST /payment-methods/v2/payments` | `post-payments` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `platform-authorization-platform-authorization-1` | `POST /payment-methods/v2/payments/cancel` | `post-payments-cancel` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `platform-authorization-platform-authorization-1` | `POST /payment-methods/v2/payments/confirm` | `post-payment-confirm` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--payment-methods-part-02 |
| `platform-authorization-platform-authorization-1` | `POST /payment-methods/v2/transfers` | `post-transfers` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--payment-methods-part-02 |
| `platform-authorization-platform-authorization-1` | `POST /payment-methods/v2/transfers/cancel` | `post-transfers-cancel` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--payment-methods-part-02 |
| `platform-authorization-platform-authorization-1` | `POST /payment-methods/v2/transfers/confirm` | `post-transfers-confirm` | `Core_platform_-_Payment_methods` | KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `platform-authorization-platform-authorization-1` | `POST /v1/cards/transfer` | `post-funds-transfer` | `Instant_payments_-_RuPay_on_UPI` | KU-API-instant-payments-rupay-on-upi--upi |
| `platform-authorization-platform-authorization-1` | `POST /v1/cards/emi-select` | `emi-select` | `Instant_payments_-_RuPay_on_UPI` | KU-API-instant-payments-rupay-on-upi--upi |
| `platform-authorization-platform-authorization-1` | `POST /v2/loans` | `bookLoanV2` | `Lending` | KU-API-lending--loans |
| `programs-creation-1` | `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | `Platform_setup_-_Programs` | KU-API-platform-setup-programs--programs-part-01 |
| `programs-creation-1` | `POST /programs/v2/programs/template` | `CreateProgramBasedOnTemplateAsync` | `Platform_setup_-_Programs` | KU-API-platform-setup-programs--programs-part-01 |
| `programs-creation-1` | `POST /programs/v1/programs/copy` | `CopyProgram` | `Platform_setup_-_Programs` | KU-API-platform-setup-programs--programs-part-01 |
| `programs-creation-1` | `POST /programs/v2/programs/copy` | `CopyProgramAsync` | `Platform_setup_-_Programs` | KU-API-platform-setup-programs--programs-part-01 |
| `programs-creation-1` | `POST /programs/v1/programs/import` | `postProgramImport` | `Platform_setup_-_Programs` | KU-API-platform-setup-programs--export-and-import |
| `programs-update-1` | `PATCH /programs/v1/programs/{id}` | `UpdateProgramInfo` | `Platform_setup_-_Programs` | KU-API-platform-setup-programs--programs-part-02 |
| `rules-evaluation-requested-1` | `POST /corporate/v2/payments` | `corporate-v2-post-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `rules-evaluation-requested-1` | `POST /corporate/v3/payments/multileg` | `corporate-v3-post-multileg-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-01 |
| `rules-evaluation-requested-1` | `POST /corporate/v2/payments/multileg` | `corporate-v2-post-multileg-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-part-03 |
| `rules-evaluation-requested-1` | `POST /cash-management/v2/payments` | `cash-management-v2-post-payments` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `savings-account-product-creation-1` | `POST /v1/savings-accounts` | `interest-bearing-v1-create-savings-account-product` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--product |
| `savings-account-product-update-1` | `PATCH /v1/savings-accounts/{productId}` | `interest-bearing-v1-patch-savings-account-product` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--product |
| `statement-refinancing-payment-agreement-simulation-not-processed-1` | `POST /v1/accounts/{accountId}/payment-agreement-simulations` | `create-payment-agreement-simulation` | `Revolving_credit_-_Statement_refinancing_API` | KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation |

## Guides that link to these events

- `accounting-entry-creation-1`: `KU-EVT-accounting-data-events`, `KU-EVT-corporate-banking-data-events`
- `authorization-authorization-cancellation-event-1`: `KU-EVT-payments-data-events`
- `authorization-authorization-event-1`: `KU-BANK-banking-overview`, `KU-CORE-over-limit-fee`, `KU-CORE-transactions-overview`, `KU-CORE-transactiontypes`, `KU-EVT-bank-slips-data-events`, `KU-EVT-payments-data-events`, `KU-PAY-bank-slips`, `KU-PAY-hold-funds`, `KU-PAY-installments-payment`
- `availables-change-available-1`: `KU-BANK-banking-overview`, `KU-EVT-corporate-banking-data-events`, `KU-EVT-ledger-data-events`, `KU-PAY-hold-funds`
- `cash-management-channel-1`: `KU-BANK-dated-transactions`
- `cash-management-check-status-change-1`: `KU-EVT-corporate-banking-data-events`, `KU-PAY-check-posting-and-settlement`
- `delinquent-account-delinquent-account-1`: `KU-CRED-credit-liquidation`, `KU-EVT-delinquency-account-data-events`
- `fraud-report-fraud-report-change-1`: `KU-EVT-disputes-endpoint-generated-events`
- `fraud-report-fraud-report-creation-1`: `KU-CARD-visa-dispute-use-case`, `KU-EVT-disputes-endpoint-generated-events`
- `intl-bankaccounts-intl-bankaccount-register-1`: `KU-EVT-international-bank-accounts-data-events`, `KU-PAY-faster-payment-system`
- `intl-bankaccounts-intl-bankaccount-update-1`: `KU-EVT-international-bank-accounts-data-events`
- `ledger-limit-changed-1`: `KU-EVT-accounts-data-events`, `KU-EVT-ledger-data-events`
- `networktransactions-network-authorization-1`: `KU-CARD-authorization-events`, `KU-CARD-authorization-validation-rules-for-card-network-operations`, `KU-CARD-card-tokenization-process-and-onboarding`, `KU-CARD-full-and-zero-balance-workflows`, `KU-CARD-simulate-authorizations`, `KU-CORE-over-limit-fee`, `KU-ERR-validation-code-definitions`, `KU-EVT-client-webhooks-part-13`
- `networktransactions-pending-transactions-2`: `KU-CARD-clearing`
- `onboarding-prospect-1`: `KU-EVT-accounts-data-events`
- `onboarding-succeeded-1`: `KU-EVT-accounts-data-events`, `KU-EVT-corporate-banking-data-events`, `KU-PAY-faster-payment-system`
- `platform-authorization-platform-authorization-1`: `KU-CORE-over-limit-fee`, `KU-EVT-corporate-banking-data-events`, `KU-EVT-payments-data-events`, `KU-LEND-book-a-loan`, `KU-PAY-check-posting-and-settlement`, `KU-PAY-payment-methods`
- `savings-account-product-creation-1`: `KU-EVT-interest-management-data-events`
- `savings-account-product-update-1`: `KU-EVT-interest-management-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: accounting-entry-creation-1, authorization-authorization-cancellation-event-1, authorization-authorization-event-1, availables-change-available-1, average-balance-calculated-average-balance-1, bulletin-bulletin-rule-1, cash-management-channel-1, cash-management-check-status-change-1, delinquent-account-delinquent-account-1, fraud-report-fraud-report-change-1, fraud-report-fraud-report-creation-1, instantpay-scheduler-execution-status-change-1, instantpay-scheduler-scheduler-status-change-1, intl-bankaccounts-intl-bankaccount-register-1, intl-bankaccounts-intl-bankaccount-update-1, ledger-limit-changed-1, networktransactions-network-authorization-1, networktransactions-pending-transactions-2, onboarding-prospect-1, onboarding-succeeded-1, orgs-operation-create-1, orgs-operation-update-1, payment-methods-authorization-1, platform-authorization-platform-authorization-1, programs-creation-1, programs-update-1, rules-evaluation-requested-1, savings-account-product-creation-1, savings-account-product-update-1, statement-refinancing-payment-agreement-simulation-not-processed-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-bank-accounts--bank-accounts-part-01` — API reference: Banking - Bank accounts — Bank accounts (part 1 of 2)
- `KU-API-banking-bank-accounts--bank-accounts-part-02` — API reference: Banking - Bank accounts — Bank accounts (part 2 of 2)
- `KU-API-banking-integrated-payments--bank-slip` — API reference: Banking - Integrated payments — Bank slip
- `KU-API-banking-interest-bearing-accounts--average-balance` — API reference: Banking - Interest-bearing accounts — Average balance
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--channels` — API reference: Banking - Transaction banking — Channels
- `KU-API-banking-transaction-banking--check-posting` — API reference: Banking - Transaction banking — Check posting
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--earmarking-pismo-account-id` — API reference: Banking - Transaction banking — Earmarking (Pismo account ID)
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--payments-pismo-account-id` — API reference: Banking - Transaction banking — Payments (Pismo account ID)
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-API-card-issuing-authorization--authorizations` — API reference: Card issuing - Authorization — Authorizations
- `KU-API-card-issuing-disputes--fraud-report` — API reference: Card issuing - Disputes — Fraud report
- `KU-API-card-issuing-protection-bulletin--rules` — API reference: Card issuing - Protection Bulletin — Rules
- `KU-API-core-platform-accounting--accounting-entry` — API reference: Core platform - Accounting — Accounting entry
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-balances-and-limits--account-limits` — API reference: Core platform - Balances and limits — Account limits
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-API-core-platform-payment-methods--force-operations` — API reference: Core platform - Payment methods — Force operations
- `KU-API-core-platform-payment-methods--hold-funds` — API reference: Core platform - Payment methods — Hold funds
- `KU-API-core-platform-payment-methods--installments-payments` — API reference: Core platform - Payment methods — Installments payments
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-03` — API reference: Core platform - Payment methods — Payment methods (part 3 of 3)
- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` — API reference: Instant payments - Pix payments — Scheduled transfers V2
- `KU-API-instant-payments-rupay-on-upi--upi` — API reference: Instant payments - RuPay on UPI — UPI
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-pismo-clearing-rules-engine--clearing-rules` — API reference: Pismo clearing rules engine — Clearing rules
- `KU-API-platform-setup-orgs-operation--processing-codes` — API reference: Platform setup - Orgs operation — Processing codes
- `KU-API-platform-setup-orgs-operation--reversal-processing-codes` — API reference: Platform setup - Orgs operation — Reversal processing codes
- `KU-API-platform-setup-programs--export-and-import` — API reference: Platform setup - Programs — Export and import
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-platform-setup-programs--programs-part-02` — API reference: Platform setup - Programs — Programs (part 2 of 2)
- `KU-API-revolving-credit-delinquent-account--delinquent-account-closure` — API reference: Revolving credit - Delinquent account — Delinquent account closure
- `KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation` — API reference: Revolving credit - Statement refinancing — Payment agreement simulation
- `KU-BANK-banking-overview` — Banking overview
- `KU-BANK-dated-transactions` — Business-dated and value-dated transactions
- `KU-CARD-authorization-events` — Authorization events
- `KU-CARD-authorization-validation-rules-for-card-network-operations` — Authorization validation rules for card network operations
- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-CARD-clearing` — Clearing: Base II and the clearing rules engine
- `KU-CARD-full-and-zero-balance-workflows` — Full and Zero balance transaction workflows
- `KU-CARD-simulate-authorizations` — Simulate authorizations
- `KU-CARD-visa-dispute-use-case` — Visa dispute use case
- `KU-CORE-over-limit-fee` — Over-limit fees
- `KU-CORE-transactions-overview` — Transactions overview
- `KU-CORE-transactiontypes` — Transaction types
- `KU-CRED-credit-liquidation` — Credit liquidation
- `KU-ERR-validation-code-definitions` — Validation code definitions
- `KU-EVT-accounting-data-events` — Core platform - Accounting
- `KU-EVT-accounts-data-events` — Core platform - Accounts
- `KU-EVT-bank-slips-data-events` — Banking - Integrated payments
- `KU-EVT-client-webhooks-part-13` — Client webhooks (part 13 of 14)
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
- `KU-EVT-delinquency-account-data-events` — Revolving credit - Delinquent account
- `KU-EVT-disputes-endpoint-generated-events` — Card issuing - Disputes
- `KU-EVT-interest-management-data-events` — Banking - Interest management
- `KU-EVT-international-bank-accounts-data-events` — Banking - Bank accounts
- `KU-EVT-ledger-data-events` — Core platform - Ledger
- `KU-EVT-payments-data-events` — Core platform - Payments
- `KU-LEND-book-a-loan` — Book loans
- `KU-PAY-bank-slips` — Bank slips
- `KU-PAY-check-posting-and-settlement` — Check posting and settlement
- `KU-PAY-faster-payment-system` — Faster Payments (UK)
- `KU-PAY-hold-funds` — Hold funds
- `KU-PAY-installments-payment` — Installments payment
- `KU-PAY-payment-methods` — Payment methods
