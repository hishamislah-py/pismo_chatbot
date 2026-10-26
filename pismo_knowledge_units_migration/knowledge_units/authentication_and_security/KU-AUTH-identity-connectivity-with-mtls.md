---
ku_id: KU-AUTH-identity-connectivity-with-mtls
title: Identity connectivity with mTLS
category: authentication_and_security
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/identity-connectivity-with-mtls.md
  sha256: ec445b7ea3ac53084fe4e1cfb6bc6cfd1b4b0a222792a536b7df7a0234a4227e
  url: https://developers.pismo.io/pismo-docs/docs/identity-connectivity-with-mtls
  role: primary_guide
  updated_at: '2026-09-29T15:48:30.000Z'
operations: []
related_kus:
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Identity connectivity with mTLS

**KU ID:** `KU-AUTH-identity-connectivity-with-mtls` · **Category:** Authentication and security · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/get-started/identity-connectivity-with-mtls.md`:

> Mutual Transport Layer Security (mTLS) is an end-to-end security protocol that verifies the identity of both sides of a communication stream—the client and the Pismo platform. It provides mutual authentication between client and server, ensuring that both parties verify each other's identities before establishing a secure connection.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/identity-connectivity-with-mtls.md`: Identity connectivity with mTLS; How the mTLS process works; Important security details

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/identity-connectivity-with-mtls.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/identity-connectivity-with-mtls · updatedAt: 2026-09-29T15:48:30.000Z

<!-- source:begin path=docs/get-started/identity-connectivity-with-mtls.md part=0-end -->

# Identity connectivity with mTLS

Mutual Transport Layer Security (mTLS) is an end-to-end security protocol that verifies the identity of both sides of a communication stream—the client and the Pismo platform. It provides mutual authentication between client and server, ensuring that both parties verify each other's identities before establishing a secure connection.

mTLS is mandatory for all API calls to the Pismo platform. This protocol keeps the platform in compliance with legal requirements, such as the European Union's Electronic Identification, Authentication, and Trust Services (eIDAS) regulation and the revised Payment Services Directive (PSD2).

To configure mTLS, contact your Pismo representative.

1. Generate a private key and a Certificate Signing Request (CSR).
2. Ensure the CSR follows the Pismo-approved format and requirements.
3. Send only the CSR to Pismo through a secure channel.
4. Pismo validates and signs the CSR and returns the signed certificate.
5. Install the signed certificate together with the corresponding private key in your environment.

<Callout icon="⚠️" theme="warn">
  The private key must remain secure and must never be shared with Pismo or any third party under any circumstances. You should only provide the CSR to Pismo.
</Callout>

**CSR Requirements**

* To ensure the certificate can be successfully issued, the CSR must comply with Pismo's required format and specifications.
* Detailed instructions and the CSR template are not publicly available and are provided directly by the Pismo Customer Success or Implementation team upon request.
* Contact your Pismo representative to obtain the latest CSR requirements before you generate and submit a CSR.

# How the mTLS process works

The following is an overview of how the authentication process works on the Pismo platform. During the process, if either side fails to present a valid certificate, the connection drops and no data is transmitted in either direction.

1. You connect to the platform.
2. The platform sends its TLS certificate.
3. You verify the certificate.
4. You send your certificate to the platform.
5. The platform verifies the certificate.
6. The platform grants access to you.
7. Data exchange occurs securely over the encrypted TLS connection.

# Important security details

The Pismo platform enforces strict security controls for all API communications.

> ⚠️ Security notes
>
> * mTLS is mandatory for all API calls to the Pismo platform.
> * Client certificates are required for authentication and must be valid and trusted.
> * Certificates have a defined validity period of two years and must be renewed before expiration.
> * Additional security layers are in place to monitor and protect traffic against unauthorized access and malicious activity.
> * The private key must remain secure and must never be shared with Pismo or any third party under any circumstances. Only the CSR should be provided to Pismo.
>
> Requests that do not meet authentication or security requirements will be rejected.
>
> For security reasons, detailed error responses and specific validation rules are not publicly documented. If needed, please contact support for troubleshooting assistance: [report the incident to Pismo](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket).
<!-- source:end -->

## Lifecycle status

- `docs/get-started/identity-connectivity-with-mtls.md`: updatedAt 2026-09-29T15:48:30.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/identity-connectivity-with-mtls.md` | whole document | https://developers.pismo.io/pismo-docs/docs/identity-connectivity-with-mtls | `ec445b7ea3ac5308…` | 2026-09-29T15:48:30.000Z |

## Related knowledge units

- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
