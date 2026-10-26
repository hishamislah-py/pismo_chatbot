---
ku_id: KU-CARD-pan-encryption-for-3ds-authentication
title: PAN encryption for 3DS authentication
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/pan-encryption-for-3ds-authentication.md
  sha256: d289017f3d02c0690fdfc0a24a30493120ff90082f52aa6e35ff00f9223d1cb0
  url: https://developers.pismo.io/pismo-docs/docs/pan-encryption-for-3ds-authentication
  role: primary_guide
  updated_at: '2026-04-02T20:23:12.000Z'
operations:
- postPreAuthenticate
related_kus:
- KU-API-card-issuing-3ds-authentication--pre-authentication
grouping_rationale: single source page
---

# PAN encryption for 3DS authentication

**KU ID:** `KU-CARD-pan-encryption-for-3ds-authentication` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/pan-encryption-for-3ds-authentication.md`:

> 3-D Secure (3DS) authentication is a card-payment security protocol that adds an extra layer of verification for online card-not-present transactions before authorization. This protocol confirms that the person making the payment is the legitimate cardholder and helps to reduce fraud.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/pan-encryption-for-3ds-authentication.md`: PAN encryption for 3DS authentication; Implementation steps; Step 1: Obtain the public key; Step 2: Configure the cipher; Step 3: Encrypt the data; Step 4: Encode the result; Complete examples; Java implementation:; Go implementation; Test your implementation

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/pan-encryption-for-3ds-authentication.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pan-encryption-for-3ds-authentication · updatedAt: 2026-04-02T20:23:12.000Z

<!-- source:begin path=docs/card-issuing/pan-encryption-for-3ds-authentication.md part=0-end -->

# PAN encryption for 3DS authentication

3-D Secure (3DS) authentication is a card-payment security protocol that adds an extra layer of verification for online card-not-present transactions before authorization. This protocol confirms that the person making the payment is the legitimate cardholder and helps to reduce fraud.

The [Send pre-authentication info](https://developers.pismo.io/pismo-docs/reference/postpreauthenticate) endpoint sends information to the client's anti-fraud validator to evaluate. The Pismo platform calls the validator's webhook and gets a response before sending a response to the caller.

Pismo provides the encrypt/decrypt keys for the hashed Primary Account Number (PAN). Pismo's PAN encryption uses RSA with Optimal Asymmetric Encryption Padding (OAEP) and Secure Hash Algorithm3, 256-bit (SHA3-256) hashing to securely encrypt sensitive data. The following describes the steps to encrypt the PAN to use with the Send pre-authentication info endpoint.

# Implementation steps

<Callout icon="📘" theme="info">
  Prerequisites

  * RSA public key (2048-bit or 4096-bit recommended)
  * Support for SHA3-256 hashtag algorithm
</Callout>

## Step 1: Obtain the public key

Open an internal service desk (ISD) ticket to request the RSA public key. You must provide the following information:

* The environment you are using: test or production
* Org ID

Please note that the process to generate and store the private key and to complete the client setup on the 3DS API involves multiple teams and can take some time.

<Callout icon="📘" theme="info">
  3DS providers

  If you are a 3DS provider, you cannot open an ISD ticket. You must contact your client and ask them to request the key and provide it to you.

  If you serve more than one issuer with Pismo, each of them will have its own key for PAN encryption.
</Callout>

## Step 2: Configure the cipher

Set up the RSA encryption with these specific parameters:

* Algorithm: **RSA**
* Padding: **OAEP**
* Hash function: **SHA3-256**
* Mask Generation Function (MFG): **MFG1 with SHA3-256**

## Step 3: Encrypt the data

1. Convert your sensitive data (PAN) to bytes.
2. Use the public key to encrypt the data.\
   The encryption will produce a byte array.

## Step 4: Encode the result

Encode the encrypted bytes using Base64 Standard Encoding.

This produces a string safe for transmission in the JSON/HTTP.

# Complete examples

## Java implementation:

```java
public String encryptPAN(PublicKey publicKey, String pan) throws Exception {
    // Step 1: Initialize cipher
    Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPWithSHA3-256AndMGF1Padding");
    // Step 2: Configure OAEP parameters
    OAEPParameterSpec oaepParams = new OAEPParameterSpec(
        "SHA3-256",                    // Hash algorithm
        "MGF1",                        // Mask generation function
        MGF1ParameterSpec.SHA3_256,   // MGF hash
        PSource.PSpecified.DEFAULT     // No label
    );
    // Step 3: Initialize for encryption
    cipher.init(Cipher.ENCRYPT_MODE, publicKey, oaepParams, new SecureRandom());
    // Step 4: Encrypt
    byte[] encryptedBytes = cipher.doFinal(pan.getBytes());
    // Step 5: Encode to Base64
    return Base64.getEncoder().encodeToString(encryptedBytes);
}
```

**Note:** If SHA3-256 is not available, add Bouncy Castle dependency.

```
<dependency>
    <groupId>org.bouncycastle</groupId>
    <artifactId>bcprov-jdk18on</artifactId>
    <version>1.78</version>
</dependency>
```

## Go implementation

```go
func encryptPAN(publicKey *rsa.PublicKey, pan string) (string, error) {
    // Step 1: Encrypt using OAEP with SHA3-256
    encryptedBytes, err := rsa.EncryptOAEP(
        sha3.New256(),           // Hash function
        rand.Reader,             // Random source
        publicKey,               // Public key
        []byte(pan),            // Data to encrypt
        nil,                    // Optional label (not used)
    )
    if err != nil {
        return "", err
    }
    // Step 2: Encode to Base64
    return base64.StdEncoding.EncodeToString(encryptedBytes), nil
}
```

# Test your implementation

1. Test with sample data. Use a known PAN value.
2. Verify Base64 output. Ensure the result is valid Base64.
3. Complete a length check. Encrypted output should match your key size (for example, 256 bytes for 2048-bit key).
4. Complete an integration test. Send the encrypted value to the API endpoint.
5. If you encounter any errors, reach out to your Pismo representative.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/preauthenticate` | `postPreAuthenticate` | Send pre-authentication info | `api-specs/Card_issuing_-_3DS_authentication.yaml` | no | KU-API-card-issuing-3ds-authentication--pre-authentication |

### Operation essentials

- **`POST /v1/preauthenticate`** (`postPreAuthenticate`): security not declared; required parameters none declared; required body fields `id`, `pan`; response statuses 200, 400, 422, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/card-issuing/pan-encryption-for-3ds-authentication.md`: updatedAt 2026-04-02T20:23:12.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/pan-encryption-for-3ds-authentication.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pan-encryption-for-3ds-authentication | `d289017f3d02c069…` | 2026-04-02T20:23:12.000Z |

## Related knowledge units

- `KU-API-card-issuing-3ds-authentication--pre-authentication` — API reference: Card issuing - 3DS authentication — Pre-authentication
