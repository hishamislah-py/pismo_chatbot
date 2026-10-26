---
ku_id: KU-EVT-catalogue-cards
title: 'Event catalogue: cards'
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
- cancel-bulk
- delete-v2-card-delete-rotation
- delete-v2-card-validity
- get-embossing-download-file
- patch-migrate-card
- patch-migrate-card-mode
- patch-v2-card
- patch-v2-card-change-rotation
- patch-v2-card-validity-renew
- post-generate-embossing
- post-generate-embossing-encrypted-noname
- post-generate-embossing-no-iv
- post-generate-embossing-noname
- post-v1-benefits-cards-cancel
- post-v1-benefits-cards-freeze
- post-v1-benefits-segments-assign
- post-v1-benefits-segments-cancel
- post-v1-benefits-segments-replace
- post-v1-card-reissue
- post-v1-clicktopay-delete_card
- post-v1-clicktopay-delete_customer
- post-v1-clicktopay-enroll_card
- post-v1-clicktopay-enroll_customer
- post-v1-clicktopay-manage_customer
- post-v1-sync-offline-pin
- post-v2-card
- post-v2-card-bind
- post-v2-card-password-increase
- post-v2-card-password-reset
- post-v2-reset-cvv
- post-vau-opt-in
- post-vau-opt-out
- put-cards-embossing
- put-v1-card-activate
- put-v1-card-status
- put-v1-clicktopay-manage_card
- put-v1-update-pan-nominal
- put-v1-update-pan-noname
- put-v1-update-pin-from-pinblock
- put-v2-card-password
- start-bulk
- start-reembossing
- transfertokens
related_kus:
- KU-API-card-issuing-cards--automatic-updater
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-cards--card-status
- KU-API-card-issuing-cards--card-validity
- KU-API-card-issuing-cards--cards
- KU-API-card-issuing-cards--cvv-rotation
- KU-API-card-issuing-cards--embossing
- KU-API-card-issuing-cards--embossing-data
- KU-API-card-issuing-cards--embossing-encrypted
- KU-API-card-issuing-cards--issuer-pan-pin
- KU-API-card-issuing-cards--mastercard-benefits
- KU-API-card-issuing-cards--migration
- KU-API-card-issuing-cards--noname
- KU-API-card-issuing-cards--pci
- KU-API-card-issuing-tokenization--card-lifecycle
- KU-API-card-issuing-tokenization--visa-click-to-pay
- KU-CARD-card-tokenization-process-and-onboarding
- KU-CARD-digital-wallets
- KU-CARD-physical-card-embossing
- KU-CARD-protection-bulletin
- KU-EVT-cards-data-events
events:
- cards-automatic-updater-1
- cards-benefits-allocation-1
- cards-bind-card-1
- cards-create-1
- cards-embossing-1
- cards-embossing-card-ingress-1
- cards-embossing-summary-1
- cards-issuer-script-1
- cards-migration-1
- cards-noname-cancellation-1
- cards-reembossing-1
- cards-rotate-cvv-1
- cards-tokenization-click-to-pay-1
- cards-tokenization-pan-update-1
- cards-update-1
- cards-update-password-1
---

# Event catalogue: cards

**KU ID:** `KU-EVT-catalogue-cards` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 16 event type(s) whose inventory domain is cards, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `cards-automatic-updater-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-automatic-updater-1 | 2 | Card_issuing_-_Cards |
| `cards-benefits-allocation-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-benefits-allocation-1 | 5 | Card_issuing_-_Cards |
| `cards-bind-card-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-bind-card-1 | 1 | Card_issuing_-_Cards |
| `cards-create-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-create-1 | 4 | Card_issuing_-_Cards |
| `cards-embossing-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-embossing-1 | 5 | Card_issuing_-_Cards |
| `cards-embossing-card-ingress-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-embossing-card-ingress-1 | 2 | Card_issuing_-_Cards |
| `cards-embossing-summary-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-embossing-summary-1 | 1 | Card_issuing_-_Cards |
| `cards-issuer-script-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-issuer-script-1 | 1 | Card_issuing_-_Cards |
| `cards-migration-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-migration-1 | 2 | Card_issuing_-_Cards |
| `cards-noname-cancellation-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-noname-cancellation-1 | 1 | Card_issuing_-_Cards |
| `cards-reembossing-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-reembossing-1 | 1 | Card_issuing_-_Cards |
| `cards-rotate-cvv-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-rotate-cvv-1 | 3 | Card_issuing_-_Cards |
| `cards-tokenization-click-to-pay-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1 | 6 | Card_issuing_-_Tokenization |
| `cards-tokenization-pan-update-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-tokenization-pan-update-1 | 1 | Card_issuing_-_Tokenization |
| `cards-update-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-update-1 | 11 | Card_issuing_-_Cards |
| `cards-update-password-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-update-password-1 | 2 | Card_issuing_-_Cards |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `cards-automatic-updater-1` | `POST /cards/v1/automatic-updater/{cardID}/opt-in` | `post-vau-opt-in` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--automatic-updater |
| `cards-automatic-updater-1` | `POST /cards/v1/automatic-updater/{cardID}/opt-out` | `post-vau-opt-out` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--automatic-updater |
| `cards-benefits-allocation-1` | `POST /pcicards/v1/pcicards/benefits/segments/assign` | `post-v1-benefits-segments-assign` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--mastercard-benefits |
| `cards-benefits-allocation-1` | `PUT /pcicards/v1/pcicards/benefits/segments/replace` | `post-v1-benefits-segments-replace` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--mastercard-benefits |
| `cards-benefits-allocation-1` | `PUT /pcicards/v1/pcicards/benefits/segments/cancel` | `post-v1-benefits-segments-cancel` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--mastercard-benefits |
| `cards-benefits-allocation-1` | `POST /pcicards/v1/pcicards/benefits/cards/replace` | `post-v1-benefits-cards-cancel` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--mastercard-benefits |
| `cards-benefits-allocation-1` | `PUT /pcicards/v1/pcicards/benefits/cards/freeze` | `post-v1-benefits-cards-freeze` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--mastercard-benefits |
| `cards-bind-card-1` | `PUT /wallet/v2/cards/{cardId}/noname/bind` | `post-v2-card-bind` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--noname |
| `cards-create-1` | `POST /wallet/v2/cards` | `post-v2-card` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--cards |
| `cards-create-1` | `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` | `post-v1-card-reissue` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--card-reissue |
| `cards-create-1` | `POST /cards/v1/bulks/{bulkID}/start` | `start-bulk` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--noname |
| `cards-create-1` | `PUT /wallet/v2/cards/{cardId}/noname/bind` | `post-v2-card-bind` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--noname |
| `cards-embossing-1` | `GET /embossing/v1/download-file` | `get-embossing-download-file` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--embossing-data |
| `cards-embossing-1` | `POST /embossing/v1/cards/generate-embossing` | `post-generate-embossing` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--embossing-encrypted |
| `cards-embossing-1` | `POST /embossing/v2/cards/generate-embossing` | `post-generate-embossing-no-iv` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--embossing-encrypted |
| `cards-embossing-1` | `POST /embossing/v1/cards/generate-embossing/noname` | `post-generate-embossing-encrypted-noname` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--embossing-encrypted |
| `cards-embossing-1` | `POST /embossing/v2/cards/generate-embossing/noname` | `post-generate-embossing-noname` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--embossing-encrypted |
| `cards-embossing-card-ingress-1` | `PUT /embossing/v1/cards/{cardId}/embossing` | `put-cards-embossing` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--embossing |
| `cards-embossing-card-ingress-1` | `PATCH /wallet/v2/cards/{cardId}/program-migration` | `patch-migrate-card` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--migration |
| `cards-embossing-summary-1` | `GET /embossing/v1/download-file` | `get-embossing-download-file` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--embossing-data |
| `cards-issuer-script-1` | `POST /pcicards/v1/pcicards/{cardId}/scripts/sync-offline-pin` | `post-v1-sync-offline-pin` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--pci |
| `cards-migration-1` | `PATCH /wallet/v2/cards/{cardId}/program-migration` | `patch-migrate-card` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--migration |
| `cards-migration-1` | `PATCH /wallet/v2/cards/{cardId}/mode/{modeId}/program-migration` | `patch-migrate-card-mode` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--migration |
| `cards-noname-cancellation-1` | `POST /cards/v1/bulks/{bulkID}/cancel` | `cancel-bulk` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--noname |
| `cards-reembossing-1` | `POST /embossing/v1/cards/reembossing` | `start-reembossing` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--embossing |
| `cards-rotate-cvv-1` | `POST /pcicards/v2/pcicards/cvv/{cardId}/reset` | `post-v2-reset-cvv` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--cvv-rotation |
| `cards-rotate-cvv-1` | `PATCH /pcicards/v2/pcicards/cvv/{cardId}/change-rotation` | `patch-v2-card-change-rotation` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--cvv-rotation |
| `cards-rotate-cvv-1` | `DELETE /pcicards/v2/pcicards/cvv/{cardId}/delete-rotation` | `delete-v2-card-delete-rotation` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--cvv-rotation |
| `cards-tokenization-click-to-pay-1` | `POST /v1/clicktopay/visa/enroll/customer` | `post-v1-clicktopay-enroll_customer` | `Card_issuing_-_Tokenization` | KU-API-card-issuing-tokenization--visa-click-to-pay |
| `cards-tokenization-click-to-pay-1` | `POST /v1/clicktopay/visa/enroll/card` | `post-v1-clicktopay-enroll_card` | `Card_issuing_-_Tokenization` | KU-API-card-issuing-tokenization--visa-click-to-pay |
| `cards-tokenization-click-to-pay-1` | `PUT /v1/clicktopay/visa/manage/customer` | `post-v1-clicktopay-manage_customer` | `Card_issuing_-_Tokenization` | KU-API-card-issuing-tokenization--visa-click-to-pay |
| `cards-tokenization-click-to-pay-1` | `PUT /v1/clicktopay/visa/manage/card` | `put-v1-clicktopay-manage_card` | `Card_issuing_-_Tokenization` | KU-API-card-issuing-tokenization--visa-click-to-pay |
| `cards-tokenization-click-to-pay-1` | `POST /v1/clicktopay/visa/delete/customer` | `post-v1-clicktopay-delete_customer` | `Card_issuing_-_Tokenization` | KU-API-card-issuing-tokenization--visa-click-to-pay |
| `cards-tokenization-click-to-pay-1` | `POST /v1/clicktopay/visa/delete/card` | `post-v1-clicktopay-delete_card` | `Card_issuing_-_Tokenization` | KU-API-card-issuing-tokenization--visa-click-to-pay |
| `cards-tokenization-pan-update-1` | `POST /v1/cards/{cardId}/network-tokens/pan-update` | `transfertokens` | `Card_issuing_-_Tokenization` | KU-API-card-issuing-tokenization--card-lifecycle |
| `cards-update-1` | `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/activate` | `put-v1-card-activate` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--cards |
| `cards-update-1` | `PATCH /wallet/v2/cards/{cardId}` | `patch-v2-card` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--cards |
| `cards-update-1` | `POST /wallet/v2/cards/{cardId}/password-tries/reset` | `post-v2-card-password-reset` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--cards |
| `cards-update-1` | `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/status` | `put-v1-card-status` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--card-status |
| `cards-update-1` | `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` | `post-v1-card-reissue` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--card-reissue |
| `cards-update-1` | `PUT /wallet/v2/cards/{cardId}/noname/bind` | `post-v2-card-bind` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--noname |
| `cards-update-1` | `POST /wallet/v2/cards/{cardId}/password-tries/increase` | `post-v2-card-password-increase` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--cards |
| `cards-update-1` | `PATCH /wallet/v2/cards/{cardId}/validity/renew` | `patch-v2-card-validity-renew` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--card-validity |
| `cards-update-1` | `DELETE /wallet/v2/cards/{cardId}/validity` | `delete-v2-card-validity` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--card-validity |
| `cards-update-1` | `PUT /pcicards/v1/pcicards/cards/{cardId}/pan` | `put-v1-update-pan-nominal` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--issuer-pan-pin |
| `cards-update-1` | `PUT /pcicards/v1/pcicards/cards/noname/{cardId}/pan` | `put-v1-update-pan-noname` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--issuer-pan-pin |
| `cards-update-password-1` | `PUT /pcicards/v2/pcicards/card/{cardId}` | `put-v2-card-password` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--pci |
| `cards-update-password-1` | `PUT /pcicards/v1/pcicards/{cardId}/pinblock` | `put-v1-update-pin-from-pinblock` | `Card_issuing_-_Cards` | KU-API-card-issuing-cards--pci |

## Guides that link to these events

- `cards-automatic-updater-1`: `KU-EVT-cards-data-events`
- `cards-bind-card-1`: `KU-EVT-cards-data-events`
- `cards-create-1`: `KU-CARD-physical-card-embossing`, `KU-EVT-cards-data-events`
- `cards-embossing-1`: `KU-CARD-physical-card-embossing`, `KU-EVT-cards-data-events`
- `cards-embossing-card-ingress-1`: `KU-CARD-physical-card-embossing`, `KU-EVT-cards-data-events`
- `cards-embossing-summary-1`: `KU-CARD-physical-card-embossing`, `KU-EVT-cards-data-events`
- `cards-issuer-script-1`: `KU-EVT-cards-data-events`
- `cards-rotate-cvv-1`: `KU-EVT-cards-data-events`
- `cards-tokenization-click-to-pay-1`: `KU-CARD-digital-wallets`
- `cards-tokenization-pan-update-1`: `KU-CARD-card-tokenization-process-and-onboarding`
- `cards-update-1`: `KU-CARD-protection-bulletin`, `KU-EVT-cards-data-events`
- `cards-update-password-1`: `KU-EVT-cards-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: cards-automatic-updater-1, cards-benefits-allocation-1, cards-bind-card-1, cards-create-1, cards-embossing-1, cards-embossing-card-ingress-1, cards-embossing-summary-1, cards-issuer-script-1, cards-migration-1, cards-noname-cancellation-1, cards-reembossing-1, cards-rotate-cvv-1, cards-tokenization-click-to-pay-1, cards-tokenization-pan-update-1, cards-update-1, cards-update-password-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-card-issuing-cards--automatic-updater` — API reference: Card issuing - Cards — Automatic updater
- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-cards--card-status` — API reference: Card issuing - Cards — Card status
- `KU-API-card-issuing-cards--card-validity` — API reference: Card issuing - Cards — Card validity
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-card-issuing-cards--cvv-rotation` — API reference: Card issuing - Cards — CVV rotation
- `KU-API-card-issuing-cards--embossing` — API reference: Card issuing - Cards — Embossing
- `KU-API-card-issuing-cards--embossing-data` — API reference: Card issuing - Cards — Embossing data
- `KU-API-card-issuing-cards--embossing-encrypted` — API reference: Card issuing - Cards — Embossing encrypted
- `KU-API-card-issuing-cards--issuer-pan-pin` — API reference: Card issuing - Cards — Issuer PAN/PIN
- `KU-API-card-issuing-cards--mastercard-benefits` — API reference: Card issuing - Cards — Mastercard benefits
- `KU-API-card-issuing-cards--migration` — API reference: Card issuing - Cards — Migration
- `KU-API-card-issuing-cards--noname` — API reference: Card issuing - Cards — Noname
- `KU-API-card-issuing-cards--pci` — API reference: Card issuing - Cards — PCI
- `KU-API-card-issuing-tokenization--card-lifecycle` — API reference: Card issuing - Tokenization — Card lifecycle
- `KU-API-card-issuing-tokenization--visa-click-to-pay` — API reference: Card issuing - Tokenization — Visa Click to Pay
- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-CARD-digital-wallets` — Digital wallets, MDES Token Connect and Click to Pay
- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-CARD-protection-bulletin` — Protection Bulletin
- `KU-EVT-cards-data-events` — Card issuing - Cards
