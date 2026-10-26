---
ku_id: KU-API-platform-authentication--authentication
title: 'API reference: Platform authentication — Authentication'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Platform_authentication.yaml
  sha256: 31cad866e67d7eebcf06f8f4bad4409ad2ac287b72d1f440c0f9acc1a0576c2e
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
operations:
- post-passport-v1-oauth2-token
- post-passport-v2-s2s-access-token
related_kus:
- KU-AUTH-authentication-methods
- KU-BANK-earmarks
- KU-GS-get-started-with-pismo-apis
- KU-GS-welcome
specification_version: 2.0.0
---

# API reference: Platform authentication — Authentication

**KU ID:** `KU-API-platform-authentication--authentication` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Authentication` in `api-specs/Platform_authentication.yaml` (“Platform authentication”, version `2.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for obtaining an access token

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/oauth2/token` | `post-passport-v1-oauth2-token` | Get OpenID access token | no |
| `POST /v2/s2s/access-token` | `post-passport-v2-s2s-access-token` | Get basic authentication access token | no |

## Operation contracts

<!-- op: spec=api-specs/Platform_authentication.yaml method=POST path=/v1/oauth2/token operationId=post-passport-v1-oauth2-token -->
### `POST /v1/oauth2/token` — Get OpenID access token

- **operationId:** `post-passport-v1-oauth2-token`
- **Specification:** `api-specs/Platform_authentication.yaml` (Platform authentication)
- **Server base URL(s):** `https://sandbox.pismolabs.io/passport`, `https://sandbox.pismolabs.io/passport`
- **Tags:** `Authentication`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get an access token for OpenID authentication
>
> A JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties. The JWT must be signed using the RS256 algorithm with your server's private key, and include specific claims as outlined in [Authentication with OpenID Connect](doc:authentication-with-openid).
>
> **Note**: Many of the endpoints in the Pismo API require you to pass a JWT that you generated which includes a Pismo account ID (`uid` or `account_id`) or an account ID from an external system used in place of the Pismo account ID (`external_account_id`). Further calls to Pismo endpoints will require this token in the Authorization header.
>
>  For more information about account-specific tokens, refer to [Endpoints that require an account-specific token](ref:endpoints-that-require-an-account-specific-token) and [Endpoints that require an external ID-specific token](ref:endpoints-that-require-an-external-id-token).

#### Request body

Required: no

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `token` | string | yes | JSON Web Token (JWT) created using the RS256 algorithm and including the required claims as outlined in [Authentication with OpenID Connect](doc:authentication-with-openid). For more information, refer to [Generating a JWT](doc:authentication-with-openid#generate-your-jwt). |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object |
| 401 | Unauthorized | `application/json`: object (schema `SimpleError`) |
| 500 | Internal Server Error | `application/json`: object (schema `SimpleError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `token` | string | no | Pismo-signed JWT used to make authenticated requests |  |
| `refresh_token` | string | no | JWT used to refresh an expired Pismo access token |  |
| `expires_in` | string | no | Expiration time (in seconds) for the Pismo access token | example: "3600" |

201 Example `Logged-in server`:

```json
{
  "expires_in": "3600"
}
```

##### Response 401

401 Example `Bad credentials`:

```json
{
  "message": "Invalid credentials"
}
```

##### Response 500

500 Example `Internal error`:

```json
{
  "message": "Error authenticating server"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;401;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-earmarks`, `KU-GS-get-started-with-pismo-apis`, `KU-GS-welcome`.

<!-- op: spec=api-specs/Platform_authentication.yaml method=POST path=/v2/s2s/access-token operationId=post-passport-v2-s2s-access-token -->
### `POST /v2/s2s/access-token` — Get basic authentication access token

- **operationId:** `post-passport-v2-s2s-access-token`
- **Specification:** `api-specs/Platform_authentication.yaml` (Platform authentication)
- **Server base URL(s):** `https://sandbox.pismolabs.io/passport`, `https://sandbox.pismolabs.io/passport`
- **Tags:** `Authentication`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Generate an access token for use with basic authentication. <br/><br/> For more information, refer to [Endpoints that require an account-specific token](ref:endpoints-that-require-an-account-specific-token) and [Endpoints that require an external ID-specific token](ref:endpoints-that-require-an-external-id-token).

#### Request body

Required: no

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `server_key` | string | yes | Server credential ID | example: "5d8252ea2e6729223f30d477d79a5c3cb45f8e03" |
| `server_secret` | string | yes | Server credential secret |  |
| `account_id` | number | no | Account ID for [endpoints that require an account token](ref:endpoints-that-require-an-account-specific-token) | example: 123 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object |
| 401 | Unauthorized | `application/json`: object (schema `SimpleError`) |
| 500 | Internal Server Error | `application/json`: object (schema `SimpleError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tenant` | string | no | Tenant ID | example: "TN-ab8b08af-8a20-44e3-a7ad-8329b3e42fa4" |
| `server_key` | string | no | Server credential ID | example: "5d8252ea2e6729223f30d477d79a5c3cb45f8e03" |
| `program_ids` | array of integer | no | Array of program IDs for which the server is allowed to make authenticated requests | example: [101, 102, 103] |
| `account_id` | number | no | Account ID | example: 123 |
| `external_account_id` | string | no | Account ID for [endpoints that require an external account token](ref:endpoints-that-require-an-external-id-token). Used in place of the Pismo account ID. | example: "5512990-642" |
| `roles` | array of string | no | Permissions roles associated with the generated access token | example: ["onboarding-server", "account-server"] |
| `token` | string | no | Pismo access token used to make authenticated requests |  |
| `refresh` | string | no | JWT used to refresh an expired Pismo access token |  |

201 Example `Logged-in server`:

```json
{
  "server_key": "5d8252ea2e6729223f30d477d79a5c3cb45f8e03",
  "tenant": "TN-ab8b08af-8a20-44e3-a7ad-8329b3e42fa4",
  "account_id": 123,
  "external_account_id": "5512990-642",
  "program_ids": [
    1,
    2,
    3
  ],
  "roles": [
    "onboarding-server",
    "account-server",
    "crm-server"
  ]
}
```

##### Response 401

401 Example `Bad credentials`:

```json
{
  "message": "Invalid credentials"
}
```

##### Response 500

500 Example `Internal error`:

```json
{
  "message": "Error authenticating server"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;401;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-authentication-methods`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/SimpleError -->
### Schema `SimpleError`

Pointer: `#/components/schemas/SimpleError`. Type: object (schema `SimpleError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Message describing the error |  |
| `examples` | (type not declared) | no |  |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_authentication.yaml` | tag `Authentication`: POST /v1/oauth2/token, POST /v2/s2s/access-token | https://github.com/PismoDevEx/pismo-api-specs | `31cad866e67d7eeb…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-authentication-methods` — API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys
- `KU-BANK-earmarks` — Earmarks
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
- `KU-GS-welcome` — Get started with the Pismo Developers Portal
