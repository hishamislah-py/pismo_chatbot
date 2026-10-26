---
ku_id: KU-API-pismo-clearing-rules-engine--clearing-rules
title: 'API reference: Pismo clearing rules engine — Clearing rules'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Pismo_clearing_rules_engine.yaml
  sha256: 523a8cba44b75a373714cf31c289e230e035a8f2033c193ab0f54c1a29dcdfbe
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: openapi_specification
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/operations_catalog.csv
  sha256: b218bf75940b0c374ca9e3a48fe92fb615b559e3192f263aff99b738b50a71cf
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/request_response_examples.csv
  sha256: ac921f2e8d0d154511b4550462e609cf6bebe3e6ce05dada157e0ed645a80856
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- dlq-get-clearing-rules
- dlq-update-clearing-rules
related_kus:
- KU-CARD-clearing
- KU-EVT-catalogue-other-domains
specification_version: 1.0.0
---

# API reference: Pismo clearing rules engine — Clearing rules

**KU ID:** `KU-API-pismo-clearing-rules-engine--clearing-rules` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Clearing rules` in `api-specs/Pismo_clearing_rules_engine.yaml` (“Pismo clearing rules engine”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Operations related to clearing rules

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/rules` | `dlq-get-clearing-rules` | Get latest clearing rules configuration | no |
| `PUT /v1/rules` | `dlq-update-clearing-rules` | Update clearing rules configuration | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer"}

## Operation contracts

<!-- op: spec=api-specs/Pismo_clearing_rules_engine.yaml method=GET path=/v1/rules operationId=dlq-get-clearing-rules -->
### `GET /v1/rules` — Get latest clearing rules configuration

- **operationId:** `dlq-get-clearing-rules`
- **Specification:** `api-specs/Pismo_clearing_rules_engine.yaml` (Pismo clearing rules engine)
- **Server base URL(s):** `https://sandbox.pismolabs.io/clearing-rules`
- **Tags:** `Clearing rules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Return the latest stored config JSON with metadata for the requested organization

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `orgId` | query | yes | string | Organization ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Configuration found | `application/json`: object (schema `GetConfigResponse`) |
| 400 | Invalid parameters | `application/json`: object (schema `HTTPError`) |
| 403 | Forbidden | `application/json`: object (schema `HTTPError`) |
| 404 | Configuration not found | `application/json`: object (schema `HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `checksum` | string | no | SHA256 checksum of the stored configuration, prefixed with `sha256:`. Used to detect configuration changes. | example: "sha256:597ea4051f151bde9c96ea5d1713e69c9a712255146bafc6dc7de22c385004b1" |
| `config` | object (schema `ClearingRulesConfig`) | no | Clearing rules currently in effect |  |
| `description` | string | no | Note explaining why the configuration changed, stored with the version for auditing | example: "Enable DLQ routing for key reasons org-wide" |
| `orgId` | string | no | Organization that owns the configuration | example: "TN-ddce7e50-0485-49ec-a910-866dff0bfd0f" |
| `scope` | string (schema `ScopeType`) | no | Scope the configuration applies to | enum: ["ORG", "PROGRAM"]; example: "ORG" |
| `updated_at` | string | no | Date and time the configuration was updated, in UTC. Format = yyyy-mm-ddThh:mm:ssZ. | example: "2026-04-15T01:07:13Z" |
| `updated_by` | string | no | User or service account that requested the update | example: "admin@pismo.com" |
| `version` | integer | no | Version assigned to this configuration, increased by one on every change | format: "int64"; example: 18 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-clearing`.

<!-- op: spec=api-specs/Pismo_clearing_rules_engine.yaml method=PUT path=/v1/rules operationId=dlq-update-clearing-rules -->
### `PUT /v1/rules` — Update clearing rules configuration

- **operationId:** `dlq-update-clearing-rules`
- **Specification:** `api-specs/Pismo_clearing_rules_engine.yaml` (Pismo clearing rules engine)
- **Server base URL(s):** `https://sandbox.pismolabs.io/clearing-rules`
- **Tags:** `Clearing rules`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Updates the latest configuration for a given scope, organization or program, and returns the new version and checksum. Persistence is asynchronous—the endpoint publishes an event and the immutable snapshot is written afterward, so it isn't guaranteed at response time. The [Pending transactions sent](https://developers.pismo.io/events/docs/networktransactions-pending-transactions-2) event reports clearing events that these rules route to the DLQ, and you can reprocess them with [Perform clearing reconciliation](https://developers.pismo.io/pismo-docs/reference/performclearingreconciliation). For background on the clearing flow, see [Clearing/Base II](https://developers.pismo.io/pismo-docs/docs/clearingbase).

#### Request body

Required: yes

> Clearing rules configuration

**Content type `application/json`** — schema: object (schema `PutClearingRulesRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `config` | object (schema `PatchableConfig`) | yes | Clearing rules to apply. Send only the fields you want to change. |  |
| `orgId` | string | yes | Organization that owns the configuration | example: "TN-ddce7e50-0485-49ec-a910-866dff0bfd0f" |
| `description` | string | no | Note explaining why the configuration changed, stored with the version for auditing | maxLength: 500; example: "Enable DLQ routing for key reasons org-wide" |
| `programId` | string | no | Program the configuration applies to. Send it only for a program-scoped configuration. | example: "prog456" |
| `scope` | string (schema `ScopeType`) | no | Scope the configuration applies to. When omitted, it's `PROGRAM` if programId is present and `ORG` otherwise. | enum: ["ORG", "PROGRAM"]; example: "ORG" |
| `updated_by` | string | no | User or service account that requested the update. | example: "admin@pismo.com" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Configuration updated or no changes detected | `application/json`: oneOf: object (schema `ClearingRulesResponse`), object |
| 201 | Configuration created | `application/json`: object (schema `ClearingRulesResponse`) |
| 400 | Validation error | `application/json`: object (schema `HTTPError`) |
| 403 | Forbidden - orgId does not match x-tenant header | `application/json`: object (schema `HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `checksum` | string | no | SHA256 checksum of the stored configuration, prefixed with `sha256:`. Use it to detect configuration changes. | example: "sha256:597ea4051f151bde9c96ea5d1713e69c9a712255146bafc6dc7de22c385004b1" |
| `orgId` | string | no | Organization that owns the configuration | example: "TN-ddce7e50-0485-49ec-a910-866dff0bfd0f" |
| `programId` | string | no | Program the configuration applies to. Returned only for a program-scoped configuration. | example: "prog456" |
| `scope` | string (schema `ScopeType`) | no | Scope the configuration applies to | enum: ["ORG", "PROGRAM"]; example: "ORG" |
| `updated_at` | string | no | Date and time the configuration was updated, in UTC. Format = yyyy-mm-ddThh:mm:ssZ. | example: "2026-02-20T10:30:00Z" |
| `updated_by` | string | no | User or service account that requested the update | example: "admin@pismo.com" |
| `version` | integer | no | Version assigned to this configuration, increased by one on every change | format: "int64"; example: 18 |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `networktransactions-pending-transactions-2` | https://developers.pismo.io/events/docs/networktransactions-pending-transactions-2 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;201;400;403;500`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ClearingRulesConfig -->
### Schema `ClearingRulesConfig`

Pointer: `#/components/schemas/ClearingRulesConfig`. Type: object (schema `ClearingRulesConfig`).

> Clearing rules configuration shared across request and response models

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_status` | boolean | no | Route the clearing event to pending transactions when the account status isn't `NORMAL`? (If `false`, the platform processes the clearing normally.) | example: true |
| `card_not_found` | boolean | no | Route the clearing event to pending transactions when the card isn't found in Pismo's records? (If `false`, the platform discards the event.) | example: true |
| `card_region_restriction` | boolean | no | Route the clearing event to pending transactions when an international transaction was made with a domestic card? (If `false`, the platform processes the clearing normally.) | example: true |
| `clearing_with_zero_amount` | boolean | no | Route the clearing event to pending transactions when the clearing amount is zero? (If `false`, the platform discards the event.) | example: false |
| `conciliation_deadline` | integer | no | Maximum number of days after the authorization date in which the clearing transaction can still be received and processed. Past this deadline, the event goes to pending transactions | format: "int32"; example: 30 |
| `different_processing_code` | boolean | no | Route the clearing event to pending transactions when the clearing processing code doesn't match the authorization processing code? (If `false`, the platform discards the clearing.) | example: true |
| `installment_plan_verification` | boolean | no | Route the clearing event to pending transactions when the installment plan differs from the authorized installment plan? (If `false`, the platform processes the clearing normally.) | example: true |
| `invalid_card_mode` | boolean | no | Route the clearing event to pending transactions when the card mode is incompatible with the transaction type, such as credit or debit? (If `false`, the platform processes the clearing normally.) | example: false |
| `invalid_julian_date` | boolean | no | Route the clearing event to pending transactions when the transaction carries an invalid Julian date? (If `false`, the platform uses the clearing date instead.) | example: true |
| `mcc_amount_exceeds_authorization` | object (schema `MCCAmountExceedsAuthorizationConfig`) | no | Merchant category codes routed to pending transactions when the cleared amount differs from the authorized amount. Codes outside this list keep the platform's current behavior |  |
| `mcc_authorization_not_found` | array of string | no | List of merchant category codes routed to pending transactions when the matching authorization isn't found. Codes outside this list keep the platform's current behavior |  |
| `not_permitted_operation` | boolean | no | Route the clearing event to pending transactions when the operation isn't permitted for the program or the processing code? (If `false`, the clearing is discarded.) | example: false |
| `not_refundable_authorization` | boolean | no | Route the clearing event to pending transactions when a cancellation is invalid or out of order? (If `false`, the cancellation is retained or discarded according to the current rule.) | example: true |

<!-- schema: #/components/schemas/HTTPError -->
### Schema `HTTPError`

Pointer: `#/components/schemas/HTTPError`. Type: object (schema `HTTPError`).

> Standard error response envelope

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Human-readable error message | example: "orgId does not match x-tenant header" |

<!-- schema: #/components/schemas/PatchableConfig -->
### Schema `PatchableConfig`

Pointer: `#/components/schemas/PatchableConfig`. Type: object (schema `PatchableConfig`).

> Clearing rules to apply. Every field is optional. Only the fields you send are changed, and the others keep their current values.

Composition: includes the fields of schema `ClearingRulesConfig` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_status` | boolean | no | Route the clearing event to pending transactions when the account status isn't `NORMAL`? (If `false`, the platform processes the clearing normally.) | example: true |
| `card_not_found` | boolean | no | Route the clearing event to pending transactions when the card isn't found in Pismo's records? (If `false`, the platform discards the event.) | example: true |
| `card_region_restriction` | boolean | no | Route the clearing event to pending transactions when an international transaction was made with a domestic card? (If `false`, the platform processes the clearing normally.) | example: true |
| `clearing_with_zero_amount` | boolean | no | Route the clearing event to pending transactions when the clearing amount is zero? (If `false`, the platform discards the event.) | example: false |
| `conciliation_deadline` | integer | no | Maximum number of days after the authorization date in which the clearing transaction can still be received and processed. Past this deadline, the event goes to pending transactions | format: "int32"; example: 30 |
| `different_processing_code` | boolean | no | Route the clearing event to pending transactions when the clearing processing code doesn't match the authorization processing code? (If `false`, the platform discards the clearing.) | example: true |
| `installment_plan_verification` | boolean | no | Route the clearing event to pending transactions when the installment plan differs from the authorized installment plan? (If `false`, the platform processes the clearing normally.) | example: true |
| `invalid_card_mode` | boolean | no | Route the clearing event to pending transactions when the card mode is incompatible with the transaction type, such as credit or debit? (If `false`, the platform processes the clearing normally.) | example: false |
| `invalid_julian_date` | boolean | no | Route the clearing event to pending transactions when the transaction carries an invalid Julian date? (If `false`, the platform uses the clearing date instead.) | example: true |
| `mcc_amount_exceeds_authorization` | object (schema `MCCAmountExceedsAuthorizationConfig`) | no | Merchant category codes routed to pending transactions when the cleared amount differs from the authorized amount. Codes outside this list keep the platform's current behavior |  |
| `mcc_authorization_not_found` | array of string | no | List of merchant category codes routed to pending transactions when the matching authorization isn't found. Codes outside this list keep the platform's current behavior |  |
| `not_permitted_operation` | boolean | no | Route the clearing event to pending transactions when the operation isn't permitted for the program or the processing code? (If `false`, the clearing is discarded.) | example: false |
| `not_refundable_authorization` | boolean | no | Route the clearing event to pending transactions when a cancellation is invalid or out of order? (If `false`, the cancellation is retained or discarded according to the current rule.) | example: true |

<!-- schema: #/components/schemas/MCCAmountExceedsAuthorizationConfig -->
### Schema `MCCAmountExceedsAuthorizationConfig`

Pointer: `#/components/schemas/MCCAmountExceedsAuthorizationConfig`. Type: object (schema `MCCAmountExceedsAuthorizationConfig`).

> Merchant category codes and percentage tolerance used when the cleared amount exceeds the authorized amount

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `mcc` | array of string | no | List of merchant category codes sensitive to an amount mismatch between the authorization and the clearing |  |
| `percentage` | integer | no | Percentage tolerance applied to the difference between the authorized and cleared amounts | format: "int32"; example: 10 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Pismo_clearing_rules_engine.yaml` | tag `Clearing rules`: GET /v1/rules, PUT /v1/rules | https://github.com/PismoDevEx/pismo-api-specs | `523a8cba44b75a37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-clearing` — Clearing: Base II and the clearing rules engine
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
