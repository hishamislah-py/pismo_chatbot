---
ku_id: KU-EVT-catalogue-cardsonfile
title: 'Event catalogue: cardsonfile'
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
- create-a-cardsonfile
- create-a-new-validation-for-a-given-card
- delete-a-metadata-field-for-a-given-card
- submit-a-validation-try
- updates-a-cardsonfile
related_kus:
- KU-API-card-issuing-cards-on-file--cards-on-file
- KU-API-card-issuing-cards-on-file--metadata
- KU-API-card-issuing-cards-on-file--validation
- KU-EVT-cards-data-events
events:
- cardsonfile-delete-metadata-1
- cardsonfile-exclusion-1
- cardsonfile-patch-cards-1
- cardsonfile-provision-1
- cardsonfile-verification-1
---

# Event catalogue: cardsonfile

**KU ID:** `KU-EVT-catalogue-cardsonfile` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 5 event type(s) whose inventory domain is cardsonfile, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `cardsonfile-delete-metadata-1` | cardsonfile | 1 | https://developers.pismo.io/events/docs/cardsonfile-delete-metadata-1 | 1 | Card_issuing_-_Cards_on_file |
| `cardsonfile-exclusion-1` | cardsonfile | 1 | https://developers.pismo.io/events/docs/cardsonfile-exclusion-1 | 3 | Card_issuing_-_Cards_on_file |
| `cardsonfile-patch-cards-1` | cardsonfile | 1 | https://developers.pismo.io/events/docs/cardsonfile-patch-cards-1 | 1 | Card_issuing_-_Cards_on_file |
| `cardsonfile-provision-1` | cardsonfile | 1 | https://developers.pismo.io/events/docs/cardsonfile-provision-1 | 1 | Card_issuing_-_Cards_on_file |
| `cardsonfile-verification-1` | cardsonfile | 1 | https://developers.pismo.io/events/docs/cardsonfile-verification-1 | 2 | Card_issuing_-_Cards_on_file |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `cardsonfile-delete-metadata-1` | `DELETE /cardsonfile/v2/cardsonfile/cards/{uuid}/metadata` | `delete-a-metadata-field-for-a-given-card` | `Card_issuing_-_Cards_on_file` | KU-API-card-issuing-cards-on-file--metadata |
| `cardsonfile-exclusion-1` | `PATCH /cardsonfile/v2/cardsonfile/cards` | `updates-a-cardsonfile` | `Card_issuing_-_Cards_on_file` | KU-API-card-issuing-cards-on-file--cards-on-file |
| `cardsonfile-exclusion-1` | `POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations` | `create-a-new-validation-for-a-given-card` | `Card_issuing_-_Cards_on_file` | KU-API-card-issuing-cards-on-file--validation |
| `cardsonfile-exclusion-1` | `POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/tries` | `submit-a-validation-try` | `Card_issuing_-_Cards_on_file` | KU-API-card-issuing-cards-on-file--validation |
| `cardsonfile-patch-cards-1` | `PATCH /cardsonfile/v2/cardsonfile/cards` | `updates-a-cardsonfile` | `Card_issuing_-_Cards_on_file` | KU-API-card-issuing-cards-on-file--cards-on-file |
| `cardsonfile-provision-1` | `POST /cardsonfile/v2/cardsonfile/cards` | `create-a-cardsonfile` | `Card_issuing_-_Cards_on_file` | KU-API-card-issuing-cards-on-file--cards-on-file |
| `cardsonfile-verification-1` | `POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations` | `create-a-new-validation-for-a-given-card` | `Card_issuing_-_Cards_on_file` | KU-API-card-issuing-cards-on-file--validation |
| `cardsonfile-verification-1` | `POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/tries` | `submit-a-validation-try` | `Card_issuing_-_Cards_on_file` | KU-API-card-issuing-cards-on-file--validation |

## Guides that link to these events

- `cardsonfile-exclusion-1`: `KU-EVT-cards-data-events`
- `cardsonfile-patch-cards-1`: `KU-EVT-cards-data-events`
- `cardsonfile-provision-1`: `KU-EVT-cards-data-events`
- `cardsonfile-verification-1`: `KU-EVT-cards-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: cardsonfile-delete-metadata-1, cardsonfile-exclusion-1, cardsonfile-patch-cards-1, cardsonfile-provision-1, cardsonfile-verification-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-card-issuing-cards-on-file--cards-on-file` — API reference: Card issuing - Cards on file — Cards on file
- `KU-API-card-issuing-cards-on-file--metadata` — API reference: Card issuing - Cards on file — Metadata
- `KU-API-card-issuing-cards-on-file--validation` — API reference: Card issuing - Cards on file — Validation
- `KU-EVT-cards-data-events` — Card issuing - Cards
