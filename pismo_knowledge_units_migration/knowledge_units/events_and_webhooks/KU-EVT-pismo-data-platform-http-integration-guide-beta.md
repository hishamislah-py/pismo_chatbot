---
ku_id: KU-EVT-pismo-data-platform-http-integration-guide-beta
title: Pismo data platform – HTTP integration guide (beta)
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/pismo-data-platform-http-integration-guide-beta.md
  sha256: 2d3fe473e04bec23e66ac58b326ae529e3d9df37f181f053718dcd3ff55fda20
  url: https://developers.pismo.io/pismo-docs/docs/pismo-data-platform-http-integration-guide-beta
  role: primary_guide
  updated_at: '2026-07-29T20:09:45.000Z'
operations: []
related_kus:
- KU-EVT-verifying-webhook-requests
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Pismo data platform – HTTP integration guide (beta)

**KU ID:** `KU-EVT-pismo-data-platform-http-integration-guide-beta` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/pismo-data-platform-http-integration-guide-beta.md`:

> Use this guide to integrate with the Pismo data platform using HTTP connectivity. It covers:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/pismo-data-platform-http-integration-guide-beta.md`: Pismo data platform – HTTP integration guide (beta); How HTTP connectivity works; Architecture; Fanout behavior; Encryption flow; Connectivity and authentication; HTTP endpoint; JWT Authentication; Verify the JWT; Security standards; Request the integration; Decrypt events; Step 1: Decrypt `enc_secret`; Step 2: Generate SHA-256 hash; Step 3: Decrypt `enc_data`

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/pismo-data-platform-http-integration-guide-beta.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pismo-data-platform-http-integration-guide-beta · updatedAt: 2026-07-29T20:09:45.000Z

<!-- source:begin path=docs/data-and-reporting/pismo-data-platform-http-integration-guide-beta.md part=0-end -->

# Pismo data platform – HTTP integration guide (beta)

Use this guide to integrate with the Pismo data platform using HTTP connectivity. It covers:

* How the integration works
* Architecture and encryption process
* Connectivity and authentication
* Security standards
* How to request the integration via ticket

## How HTTP connectivity works

Pismo’s event hub sends real-time events from the Pismo platform to your systems. Events are delivered through HTTPS using Visa-compliant encryption standards and JSON Web Tokens (JWTs) for authentication. This ensures data protection even if requests are intercepted.

To configure HTTP connectivity, provide the following information:

* HTTPS endpoint where the Pismo event hub sends events

* Public certificate encoded in Base64

* Certificate identifier (optional)

* Maximum transactions per second (TPS)

When the integration is configured:

* Your certificate is stored securely.

* The certificate identifier appears as the key ID (KID) in the `enc_secret` header information.

* A KID is generated for JWT authentication.

* Your public certificate encrypts the symmetric key used for event decryption.

* Each event generates one HTTP POST request to your endpoint.

## Architecture

### Fanout behavior

The Pismo event hub uses a one-to-one delivery model.

* Each event generates one HTTP request.

* Multiple events generate multiple requests.

* Request headers remain consistent across requests.

### Encryption flow

The integration uses the following encryption process:

* The event payload (`enc_data`) encrypted with a symmetric key generated at runtime using AES-GCM (256).

* The symmetric key (`enc_secret`) encrypted with your public certificate using RSA-OAEP-SHA256.

* Both `enc_data` and `enc_secret` are included in the request body:

```json
{
 "enc_data": "<encrypted_jwe_payload>",
 "enc_secret": "<encrypted_jwe_key>"
}
```

## Connectivity and authentication

### HTTP endpoint

Provide the HTTPS endpoint that receives event requests. The Pismo event hub sends HTTPS POST requests to this endpoint.

### JWT Authentication

Each request includes a JWT in the authorization header. The JWT is signed by Pismo using RS256 (RSA SHA-256). Verify the JWT before processing the request.

### Verify the JWT

1. Parse the JWT using a trusted library. Supported languages include Go, Python, Node.js, Java, and .NET.
2. Retrieve the KID from the JWT header.
3. Check whether you already have the corresponding public key cached.
4. If the key is not cached, retrieve it from the appropriate public-key endpoint:
   * Test environment: <Anchor label="Pismo test certificates endpoint" target="_blank" href="https://sandbox.pismolabs.io/v1/certs">Pismo test certificates endpoint</Anchor>

   * Production environment: <Anchor label="Pismo production certificates endpoint" target="_blank" href="https://prod.pismo.io/v1/certs">Pismo production certificates endpoint</Anchor>
5. Verify the JWT signature with the public key.

**Important:**

* Cache public keys and refresh them based on the `cache-control`) header value (`max-age`).

* Do not call the public keys endpoint for every request. The endpoint is rate limited to five requests per second.

* For more information, refer to the <Anchor label="Verifying webhook requests" target="_blank" href="https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests">Verifying webhook requests</Anchor> guide.

## Security standards

HTTP connectivity uses Visa JWE and JWS standards for encryption and signing. JWT authentication helps verify request authenticity and maintain payload integrity. For additional information, see the following resources:

* <Anchor label="Visa Encryption Guide" target="_blank" href="https://developer.visa.com/pages/encryption_guide/jwe-jws">Visa Encryption Guide</Anchor> (refer to the Creating JWE > Using RSA PKI sections)
* <Anchor label="Visa Developer Center registration" target="_blank" href="https://developer.visa.com/identity/user/register">Visa Developer Center registration</Anchor>
* <Anchor label="Visa Developer Center sign-in" target="_blank" href="https://developer.visa.com/login/">Visa Developer Center sign-in</Anchor>

## Request the integration

Submit a <Anchor label="Pismo support ticket" target="_blank" href="https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket">Pismo support ticket</Anchor> to request HTTP connectivity. Include all required information in the initial request to help avoid delays.

#### Ticket Template

**Subject:**\
Request for HTTP event hub integration

**Description:**\
Request HTTP connectivity to receive Pismo events. Include the following information:

1. **Organization ID**
2. **Environment (PROD/STAGE)**
3. **HTTPS Endpoint URL**
   * Example: [https://yourdomain.com/events](https://yourdomain.com/events)
4. **Public Certificate**
   * Encode your PEM certificate in Base64.
5. **Certificate Identifier**
   * Provide a unique identifier such as `my-cert-2025`.
   * Used by Pismo for internal control and by you to identify which private key to use.
6. **Maximum TPS (Transactions per Second)**
   * Provide the agreed limit for your endpoint.

## Decrypt events

Use the following procedure to decrypt an event payload.

### Step 1: Decrypt `enc_secret`

Decrypt `enc_secret` with your private key using:

* Key Management: RSA-OAEP-SHA256
* Content Encryption: AES-GCM (256)

The result is a UUID.

### Step 2: Generate SHA-256 hash

Generate a SHA-256 hash from the UUID. The hash becomes the key used to decrypt `enc_data`.

### Step 3: Decrypt `enc_data`

**Decrypt** `enc_data` using:

* Key Management: AES-GCM Key Wrap (256)
* Content Encryption: AES-GCM (256)

The output is the original event payload.

The following workflow shows the overall process for verifying, decrypting, and consuming event payloads received from the Pismo event hub.

<Image align="left" alt="Customer event consumer image" border={true} width="210px" src="https://files.readme.io/7d176b1eff12d99f7e15333c905b749439e6eb4015b550d9e6fac2f9ee53537b-image.png" className="border" />

<br />

<br />

<br />

<br />

<br />

<br />

<br />
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/pismo-data-platform-http-integration-guide-beta.md`: updatedAt 2026-07-29T20:09:45.000Z.
- The source title marks the feature as beta: "Pismo data platform – HTTP integration guide (beta)".

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/pismo-data-platform-http-integration-guide-beta.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pismo-data-platform-http-integration-guide-beta | `2d3fe473e04bec23…` | 2026-07-29T20:09:45.000Z |

## Related knowledge units

- `KU-EVT-verifying-webhook-requests` — Verifying webhook requests
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
