---
ku_id: KU-BANK-file-based-processing
title: File-based processing, file signature and encryption
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/file-based-processing.md
  sha256: 65405d1a8fac9d76f1beb1c2e568e06703a7e1bccfeb1b589236123d0a95285d
  url: https://developers.pismo.io/pismo-docs/docs/file-based-processing
  role: primary_guide
  updated_at: '2026-04-24T22:11:15.000Z'
- path: docs/core-banking/file-signature-and-encryption.md
  sha256: 378afcc127a89ac4c5c0838f233e0d5225a984ae793254334630c531a3293f2c
  url: https://developers.pismo.io/pismo-docs/docs/file-signature-and-encryption
  role: primary_guide
  updated_at: '2026-04-24T21:57:56.000Z'
operations:
- corporate-bulk-payments-put-aes-keys-jwe
- corporate-put-bulk-file
- get-bulk-keys
- patch-corporate-v1-restricted-funds
- post-bulk-keys
- post-corporate-v1-restricted-funds
related_kus:
- KU-API-banking-transaction-banking--bulk-payment-files
- KU-API-banking-transaction-banking--restricted-funds
- KU-BANK-restrictions
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
grouping_rationale: Processing and the file security it requires.
---

# File-based processing, file signature and encryption

**KU ID:** `KU-BANK-file-based-processing` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Processing and the file security it requires.

Scope as stated in `docs/core-banking/file-based-processing.md`:

> Managing cash positions often involves blocking or releasing funds across thousands of accounts simultaneously—a scale that can overwhelm systems designed for single‑transaction API calls. To simplify this process, the Pismo platform provides a file‑based processing solution. You can upload UTF‑8 NDJSON files containing a specific operation type, such as `RESTRICT_FUNDS`, to execute multiple transactions in bulk. Each file is processed asynchronously, line by line, ensuring that a failure in one instruction does not halt the rest.

Scope as stated in `docs/core-banking/file-signature-and-encryption.md`:

> Encrypting and signing digital files before sending them to the Pismo platform is crucial for ensuring both security and authenticity. Encryption protects the data by converting it into a format that can only be read by someone who has the appropriate decryption key, thereby safeguarding it from unauthorized access and potential breaches. This ensures that sensitive information, such as personal details, financial data, or confidential business documents, remains private and secure during transmission.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/file-based-processing.md`: File-based processing; Send and process files for restrict funds; Notes; Prepare your input and output files; Input file; Input file format; Operation type JSON payload for restrict funds; Input file example (`RESTRICT_FUNDS`); Input file example (`RELEASE_RESTRICTION`); Output file; Sample responses; Error codes; File retention policy
- `docs/core-banking/file-signature-and-encryption.md`: File signature and encryption; File signature; Before you begin; Create public and private keys; Retrieve a public key using the key ID; Prepare signature envelope file; Sign the bulk file; Generate the base64-encoded signature; Signature envelope file output; Verify Pismo's signature envelope file; Decode the base64 into a temporary file; Retrieve Pismo's public key; Create a der file; Verify signature; File encryption; Encryption specification

## Prerequisites and dependencies

- Prerequisites are described in `docs/core-banking/file-signature-and-encryption.md` section "Before you begin".
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/file-based-processing.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/file-based-processing · updatedAt: 2026-04-24T22:11:15.000Z

<!-- source:begin path=docs/core-banking/file-based-processing.md part=0-end -->

# File-based processing

Managing cash positions often involves blocking or releasing funds across thousands of accounts simultaneously—a scale that can overwhelm systems designed for single‑transaction API calls. To simplify this process, the Pismo platform provides a file‑based processing solution. You can upload UTF‑8 NDJSON files containing a specific operation type, such as `RESTRICT_FUNDS`, to execute multiple transactions in bulk. Each file is processed asynchronously, line by line, ensuring that a failure in one instruction does not halt the rest.

This diagram illustrates the step‑by‑step flow of file-based processing.

<Image alt="File-based processing flow" align="center" src="https://files.readme.io/942ceca27ebb75cc4006126ddbf8721c1ed77d5093afd94e4e72071b372827fd-Bulk_file_loading_feature_2.png" />  Figure 1: File-based processing flow

The diagram summarizes the process as follows.

1. **Sign** the plaintext bulk file.
2. **Request** an AES-256 key from Pismo using the encryption key endpoint.
3. **Decrypt** the JWE payload with your private key to retrieve `aes_key` and `iv`.
4. **Encrypt** the signed file using AES-256-CBC with the retrieved key and IV.
5. **Upload** the encrypted file to Pismo.

# Send and process files for restrict funds

To facilitate file-based processing, the Pismo platform builds an extensible, AWS-based bulk-processing platform capable of ingesting and executing large file-driven workloads. Its plugin architecture allows new operational workflows to be added quickly. All capabilities available through the single-operation endpoint can be invoked through files that contain hundreds or thousands of instructions.

One of the solutions supported by file-based processing is [restrict funds](https://developers.pismo.io/pismo-docs/docs/restrict-funds). These are the endpoints.

* [Create fund restriction](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds)
* [Release restriction](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v1-restricted-funds)

  ### Notes
* Each line in the file is executed independently. A failure on one instruction does not halt the rest, and the response file lists both successes and errors.
  * Files are UTF-8 NDJSON—a header line followed by one JSON object per operation, conforming to the prescribed schema.
  * No in-flight tracking or cancellation. You can monitor progress through the output event/response file when your bulk file loading completes.
  * This is a deferred validation upload, meaning the file is accepted on upload, but full transaction validation occurs later during asynchronous processing.
  * Validation results are included in the output file once processing is complete.

By consolidating thousands of restrict and release requests into a handful of files, the Pismo platform reduces API traffic while maintaining fault isolation and horizontal scalability.

# Prepare your input and output files

Before you upload your files to Pismo, you must prepare an input and output file according to these guidelines.

## Input file

The Pismo platform processes file requests by reading a UTF-8 input file that begins with a single header line and is followed by numerous NDJSON lines, with each one describing an operation that follows the schema described in the [Operation type JSON payload for restrict funds](#operation-type-json-payload-for-restrict-funds) section.

## Input file format

**Name**

Because you upload the file through an endpoint, the filename is irrelevant and does not appear in the output.

**Header**

Here is an example of a header file.

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Example</summary>

  ```json
  {
    "bulk_id": "TESTE-3-TRANSFER-20250905",
    "org_id": "TN-097d9c0e-0331-492a-93e2-95c8c2019fd1",
    "header_version": "1.0.0",
    "operation_type": "RESTRICT_FUNDS",
    "n_entries": 4
  }
  ```

  | Attribute        | Description                                                             |
  | :--------------- | :---------------------------------------------------------------------- |
  | `bulk_id`        | Client-generated ID for file-based processing.                          |
  | `org_id`         | Your organization ID.                                                   |
  | `header_version` | Must be exactly `1.0.0`.                                                |
  | `operation_type` | Operation to perform: either `RESTRICT_FUNDS` or `RELEASE_RESTRICTION`. |
  | `n_entries`      | Total number of entries contained in the file (e.g., `10000`).          |
</details>

### Operation type JSON payload for restrict funds

After the header object, add a JSON payload in which each row corresponds to the operation type you specified in the header. There are only two allowable operation types.

* `RESTRICT_FUNDS`: This operation specifies that each row in the file transfers the amount from the available balance to restricted funds.
* `RELEASE_RESTRICTION`: This operation specifies that each row in the file transfers the amount from restricted funds back to the available balance.

### Input file example (`RESTRICT_FUNDS`)

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>RESTRICT\_FUNDS</summary>

  ```json
  {"bulk_id": "HOLD-CSIID-Uniqueid", "org_id": "<your_org_id>", "header_version": "1.0.0", "operation_type": "RESTRICT_FUNDS", "n_entries": 2}
  {"external_account_id": "f94eb97c-43e2-4069-9720-5b08d17f03aa", "tracking_id": "f94eb97c-43e2-4069-9720-5b08d174510001", "restricted_funds_id": "8a4bfca4-d2e7-441a-8e5c-2dda797d0001", "hold_method": "FLEXIBLE", "amount": 1500.44, "soft_descriptor": "Hold for transaction processing", "metadata": {}}
  {"external_account_id": "f94eb97c-43e2-4069-9720-5b08d17f03ab", "tracking_id": "f94eb97c-43e2-4069-9720-5b08d174510002", "restricted_funds_id": "8a4bfca4-d2e7-441a-8e5c-2dda797d0002", "hold_method": "FLEXIBLE", "amount": 1500.01, "soft_descriptor": "Hold for transaction processing", "metadata": {}}
  ```

  | Attribute             | Description                                                                                                                                                        |
  | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | `external_account_id` | Client-provided account ID used as the primary key for all related operations.                                                                                     |
  | `tracking_id`         | Pismo-generated ID that pinpoints this specific hold request.                                                                                                      |
  | `restricted_funds_id` | Optional ID that labels the hold. If not provided, one is created automatically.                                                                                   |
  | `hold_method`         | Determines how funds are locked: `FLEXIBLE` holds as much as possible up to the requested amount, while `STRICT` requires the full amount or the hold is rejected. |
  | `amount`              | Exact monetary value to be reserved on the account.                                                                                                                |
  | `soft_descriptor`     | Optional text that can appear in transaction statements or reports for added context.                                                                              |
  | `metadata`            | Custom key–value data supplied by the client for any additional information.                                                                                       |
</details>

### Input file example (`RELEASE_RESTRICTION`)

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>RELEASE\_RESTRICTION</summary>

  ```json
  {"bulk_id": "RELEASE-CSIID-Uniqueid", "org_id": "TN-097d9c0e-0331-492a-93e2-95c8c2019fd1", "header_version": "1.0.0", "operation_type": "RELEASE_RESTRICTION", "n_entries": 2}
  {"external_account_id": "f94eb97c-43e2-4069-9720-5b08d17f03aa", "tracking_id": "f94eb97c-43e2-4069-9720-5b08d1745130001", "restricted_funds_id": "8a4bfca4-d2e7-441a-8e5c-2dda797d0001", "hold_method": "STRICT", "amount": 1500.44, "soft_descriptor": "Release for transaction processing", "metadata": {}}
  {"external_account_id": "f94eb97c-43e2-4069-9720-5b08d17f03ab", "tracking_id": "f94eb97c-43e2-4069-9720-5b08d1745130002", "restricted_funds_id": "8a4bfca4-d2e7-441a-8e5c-2dda797d0002", "hold_method": "STRICT", "amount": 1500.01, "soft_descriptor": "Release for transaction processing", "metadata": {}}
  ```

  | Attribute             | Description                                                                                                 |
  | --------------------- | ----------------------------------------------------------------------------------------------------------- |
  | `external_account_id` | Client-supplied account ID, used as the primary key for all corporate-level operations.                     |
  | `tracking_id`         | ID that traces the specific amount being held.                                                              |
  | `restricted_funds_id` | ID for the fund hold operation. If omitted, Pismo automatically generates an ID for you.                    |
  | `hold_method`         | Holding strategy. Strategy must be set to `STRICT`, guaranteeing that the exact amount requested is locked. |
  | `amount`              | Monetary value to be reserved.                                                                              |
  | `soft_descriptor`     | Free-text note for additional context (e.g., appears in statements or reports).                             |
  | `metadata`            | Flexible key–value pairs supplied by the client for any extra information.                                  |
</details>

# Output file

An output file contains the results of file‑based processing. After the Pismo platform processes your input file, it generates an output file detailing the outcome of each transaction. This file is then stored in the Amazon S3 bucket you specified.

Here are the details of output file format.

* Output files follow this naming convention: `{creation-datetime}-{bulk-id}-out.original`.
* `creation-datetime`: This is a UTC timestamp that conforms to the format of `YYYY-MM-DD-hh-mm-ss`.
* `bulk-id`: An alphanumeric string (letters, digits, and hyphens only) that represents your file-based processing operation. The ID cannot exceed 50 characters.
* The complete file name does not exceed 120 characters.

This table summarizes the output file format.

<Table>
  <thead>
    <tr>
      <th>
        Item
      </th>

      <th>
        Details
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Output file name format
      </td>

      <td>
        `&#123;timestamp&#125;-&#123;bulk_id&#125;-out.original`
      </td>
    </tr>

    <tr>
      <td>
        timestamp
      </td>

      <td>
        UTC date‐time of file creation in the format `YYYY-MM-DD-hh-mm-ss`.
      </td>
    </tr>

    <tr>
      <td>
        bulk\_id
      </td>

      <td>
        Client-supplied ID (letters, digits, hyphens) with a maximum length of 50 characters.
      </td>
    </tr>

    <tr>
      <td>
        File-name length
      </td>

      <td>
        The entire file name must not exceed 120 characters.
      </td>
    </tr>

    <tr>
      <td>
        Example
      </td>

      <td>
        `2024-09-10-20-40-15-b109e822-d2e7-4ee8-a06f-02f582ce4d10-out.original`\
        └─ timestamp ──┘ └──────  bulk\_id ────────┘ └ suffix ┘
      </td>
    </tr>

    <tr>
      <td>
        Storage location
      </td>

      <td>
        The output file is delivered to your designated Amazon S3 bucket.
      </td>
    </tr>
  </tbody>
</Table>

## Sample responses

When the upload is complete and the operation is processed successfully, a `201 Created` response is returned. Refer to the endpoints for more details.

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>201 Created</summary>

  ```json
  {
    "response_status": 201,
    "tracking_id": "9d15bfd1-5db9-4e96-b846-8d8707454430",
    "cid": "ex-cid-1",
    "data": {
      "restricted_funds_id": "4a4060d5-3649-46e8-8d64-93949b212918",
      "amount”: 1932.22,
      "applied_amount": 1932.22,
      "status": "SUCCEEDED"
    }
  }
  ```
</details>

Otherwise, a `4xx` error is returned indicating the reason for the failure.

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>4xx error</summary>

  ```json
  {
    "response_status": 4xx,
    "tracking_id": "9d15bfd1-5db9-4e96-b846-8d8707454430",
    "cid": "ex-cid-1",
    "data": {
      "restricted_funds_id": "4a4060d5-3649-46e8-8d64-93949b212918",
      "amount”: 1932.22,
      "status": "FAILED"
    },
    "error": {
      "code": "AHF00##",
      "message": "The request attributes are different from the previous hold funds operation"
    }
  }
  ```
</details>

<br />

Once you finish preparing the input and output files, proceed to:

1. [Create a public key and a private key](https://developers.pismo.io/pismo-docs/docs/file-signature-and-encryption#create-public-and-private-keys)
2. [Prepare a signature envelope file](https://developers.pismo.io/pismo-docs/docs/file-signature-and-encryption#prepare-signature-envelope-file)
3. [Sign the bulk file](https://developers.pismo.io/pismo-docs/docs/file-signature-and-encryption#sign-the-bulk-file)
4. [Verify signature](https://developers.pismo.io/pismo-docs/docs/file-signature-and-encryption#verify-pismos-signature-envelope-file)
5. [Encrypt the bulk file](https://developers.pismo.io/pismo-docs/docs/file-signature-and-encryption#file-encryption)

The detailed steps are described in [File signature and encryption](https://developers.pismo.io/pismo-docs/docs/file-signature-and-encryption).

## Error codes

Refer to [Create fund restriction](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds) for error code details.

# File retention policy

To ensure sustainable cost management and secure file handling, the Pismo platform implements these file retention rules.

1. **First 30 days**: Files remain in the input and output buckets.
2. **After 30 days**: Files are migrated to a storage class with longer recovery times.
3. **After 365 days**: Files are migrated again to a storage class that requires at least 12 hours to recover.

It's best to implement a policy to delete files from long‑term storage once they are no longer needed.
<!-- source:end -->

### Source 2: `docs/core-banking/file-signature-and-encryption.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/file-signature-and-encryption · updatedAt: 2026-04-24T21:57:56.000Z

<!-- source:begin path=docs/core-banking/file-signature-and-encryption.md part=0-end -->

# File signature and encryption

Encrypting and signing digital files before sending them to the Pismo platform is crucial for ensuring both security and authenticity. Encryption protects the data by converting it into a format that can only be read by someone who has the appropriate decryption key, thereby safeguarding it from unauthorized access and potential breaches. This ensures that sensitive information, such as personal details, financial data, or confidential business documents, remains private and secure during transmission.

Digital signatures, on the other hand, provide a means to verify the authenticity and integrity of the files. By signing a file, the sender attaches a unique cryptographic signature that can be verified by the recipient to confirm that the file has not been altered in transit and that it indeed comes from the purported sender. This helps prevent tampering, forgery, and impersonation, thereby establishing trust and confidence in the communication process.

To this end, Pismo provides features for both signing and encrypting your files. These features meet the following criteria:

* **Authenticity**: They confirm that the file originates from the customer, verifying the sender's identity.
* **Integrity**: They ensure that the file remains unchanged and untampered from the moment it was signed.
* **Confidentiality**: They use managed encryption keys, allowing customers to encrypt files before sending, protecting their data from unauthorized access.

<Callout icon="📘" theme="info">
  **Note**

  Before uploading your bulk file, you must sign and encrypt it.
</Callout>

To verify the authenticity of your signature, Pismo requires your public key. Upload it using the Upload public key endpoint.

To submit a bulk file, choose one of the following:

* Use the [Upload bulk file](https://developers.pismo.io/pismo-docs/reference/corporate-put-bulk-file) endpoint.
* Upload the file directly to Pismo’s AWS S3 bucket.

If you use the AWS S3 option, you must also include a signature envelope containing the key ID and the signature data, sent alongside the bulk file.

<Callout icon="📘" theme="info">
  **About signature envelope**

  A signature envelope is a small companion file that carries the information needed to verify a digitally signed payload (your bulk file). It typically travels alongside the file and includes the signature and metadata about how it was produced.
</Callout>

# File signature

Digital signatures use asymmetric cryptography: a public key and a private key. Before sending your bulk file:

* Generate an RSA‑3072 key pair.
* Use your private key to sign the unencrypted bulk file with RSA and a SHA‑384 digest.
* Upload your public key via the [Upload public key](https://developers.pismo.io/pismo-docs/reference/post-bulk-keys) endpoint to enable signature verification during bulk file processing.

<Callout icon="📘" theme="info">
  **What is RSA-3072?**

  RSA-3072 refers to an RSA encryption key size that is 3072 bits long. RSA (Rivest-Shamir-Adleman) is an asymmetric cryptographic algorithm used for secure data transmission. The key size, in this case 3072 bits, determines the strength of the encryption. A larger key size generally means stronger security, but it also requires more computational power.

  RSA-3072 is considered secure for most purposes and provides a higher level of security compared to shorter key sizes like RSA-2048. It's often used in applications requiring long-term security, such as digital signatures, SSL/TLS certificates, and secure email communication.
</Callout>

# Before you begin

There are caveats you must follow before you begin creating your signature file.

* When sending a bulk file, include both the encrypted original file and the signature envelope file.\
  Exception: If you use Pismo’s Upload Bulk File endpoint, the signature envelope is not required. Instead, you can provide the key ID and signature data in the dedicated Signature header, as explained in [Upload bulk file](https://developers.pismo.io/pismo-docs/reference/corporate-put-bulk-file).
* The original file refers to the input bulk file.
* The original file must be signed first, then encrypted using an AES key provided by Pismo. You can request this AES key via the [Create AES key](https://developers.pismo.io/pismo-docs/reference/corporate-bulk-payments-put-aes-keys-jwe) endpoint.
* The encrypted original file and the signature envelope file must use the extensions `.original` and .`sign`, respectively.

## Create public and private keys

Create a RSA-3072 key pair to digitally sign the bulk file.  Here is how to generate a key pair, extract the public key, and upload it.

1. Run this command to generate an RSA‑3072 private key. In this example, `private-key.pem` is the output file. PEM (Privacy‑Enhanced Mail) is a standard format for storing and exchanging cryptographic keys and certificates.

```shell
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out private-key.pem
```

2. Create a public key (`public-key.der`) from the private key.

```shell
openssl pkey -in private-key.pem -outform der -out public-key.der -pubout 
```

<Callout icon="📘" theme="info">
  **About DER**

  All key materials are in the DER format and encoded in `base64`. DER (Distinguished Encoding Rules) is a binary format for encoding data structures described by ASN.1 (Abstract Syntax Notation One). It is commonly used in cryptography for encoding certificates, keys, and other data.
</Callout>

3. Generate **key material** from the public key.

```shell
base64 -i public-key.der
```

<Callout icon="📘" theme="info">
  **About key material**

  Key material represents the actual key data used for performing cryptographic operations such as encryption, decryption, signing, and verification.
</Callout>

4. Copy and paste the generated key material in the `key_material` field in [Upload public key](https://developers.pismo.io/pismo-docs/reference/post-bulk-keys) to upload your public key to Pismo.

The following is a sample request for uploading a public key:

```shell cURL
curl --request POST \
     --url https://api-sandbox.pismolabs.io/corporate/v1/bulk-payments/keys \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "id": "<key_id>",
  "key_material": "<key_material>",
  "expired_at": "2025-05-21T12:27:00Z"
}
'
```

For details about the fields in the request, see [Upload public key](https://developers.pismo.io/pismo-docs/reference/post-bulk-keys).

When the request is processed successfully, a `201 Created` response is returned confirming the key you sent previously.

```json
{
  "id": "<key_id>"
}
```

### Retrieve a public key using the key ID

If you need to retrieve a public key you've sent, you can use the [Get public key](https://developers.pismo.io/pismo-docs/reference/get-bulk-keys) endpoint with the public key ID. This endpoint allows you to query a Pismo public key to validate a signature or to retrieve a public key that you uploaded.

## Prepare signature envelope file

The signature envelope file is a text file containing a JSON object with the signature data, it contains the following fields.

* `org_id`: Tenant identification.
* `signing_key_id`: ID of the public key corresponding to the private key used to sign the file.
* `bulk_id`: Bulk ID specified in the original file.
* `signature`: Signature encoded in base64.

The following is an example of the JSON object in a signature envelope file.

```json
{
  "org_id": "<your_org_id>", 
  "signing_key_id": "<your_signing_key_id>",
  "bulk_id": "<your_bulk_id>",
  "signature": "<signature_encoded_in_base64>"
}
```

Note that the signature envelope format is identical for client-submitted signatures and Pismo‑generated output signatures. The public key corresponding to the signing private key must be uploaded in advance via the [Upload public key](https://developers.pismo.io/pismo-docs/reference/post-bulk-keys)  endpoint.

Before you proceed, there are some key points to consider regarding the format of the signature envelope file.

* Without the key ID (the `id` parameter in [Upload public key](https://developers.pismo.io/pismo-docs/reference/post-bulk-keys)), it is impossible to identify the public key that must be used to verify the signature. To pass the signature verification step during bulk processing, you must provide Pismo with three components: the bulk file, a digital signature, and the corresponding public key. There are two ways to do this. One, you can use the [Upload bulk file](https://developers.pismo.io/pismo-docs/reference/corporate-put-bulk-file) endpoint. In this scenario, you specify the key ID (`id`) and the signature in the request header. Another way is to create a signature envelope file that contains the key ID and the signature data, then upload it to a Pismo-designated AWS S3 bucket.
* The actual key material is uploaded and securely stored in Pismo’s database. It can be submitted only through the [Upload public key](https://developers.pismo.io/pismo-docs/reference/post-bulk-keys)  endpoint, which uses mutual authentication over a private network to ensure only the authorized client can transmit the key and to prevent unauthorized submissions.
* Only the key ID (`id`) is sent to Pismo, not the actual key.

## Sign the bulk file

These steps show how to sign the unencrypted bulk file and generate the signature envelope. Run this command to sign the unencrypted bulk file with your client‑generated private key.

```shell
openssl dgst -sha384 -sign private-key.pem -out signature.tmp  2024-05-21-15-55-00-<bulk_id>.plain
```

In this example:

* `private-key.pem` is the file containing your private key.
* `2024-05-21-15-55-00-<bulk_id>.plain` is the unencrypted version of the bulk file you intend to send to Pismo.
* `signature.tmp` is a temporary file used to store the generated signature data.

### Generate the base64-encoded signature

Generate base64-encoded content for the signature file.

```shell
base64 -i signature.tmp
```

This command outputs the base64 string that goes into the `signature` attribute of the signature envelope file.

## Signature envelope file output

A signature envelope file is generated, it contains a JSON object with three attributes: `bulk_id`, `key_id`, and `signature`.

* `bulk_id`: The bulk identifier as specified in the bulk file. This ID is client-generated. You must generate this ID and provide it to Pismo.
* `key_id`: The identifier of the public key corresponding to the private key used to sign the file.
* `signature`: The signature encoded in base64 that you generated in the [Generate the base64-encoded signature](#generate-the-base64-encoded-signature)  section.

This format is used for both the bulk file you send and the output file generated by Pismo.

After the bulk file is processed, Pismo returns an output file along with a corresponding signature envelope. The example below shows the envelope generated by Pismo. The `key_id` refers to Pismo’s public key used to sign the output file and is different from the customer’s signing key.

```json
{
  "bulk_id": "<bulk_id>",
  "key_id": "<key_id>",
  "signature": "<Pismo-signature>"
}
```

## Verify Pismo's signature envelope file

After processing a bulk file, Pismo generates an output file containing the results of the bulk processing. This file is digitally signed by Pismo, and the corresponding signature is provided to the customer in a signature envelope file. This envelope follows the same JSON format used by the customer when uploading a file via the AWS S3 bucket approach. The following example illustrates a manual verification process that can serve as a basis for implementation. The example contains the following steps:

1. Decode the base64 into a temporary file.
2. Retrieve Pismo's public key.
3. Create a DER file to contain the public key material.
4. Verify signature.

### Decode the base64 into a temporary file

To decode the base64 of the signature data into a temporary file, follow these steps:

Create a file named `pismo-signature.base64`, then copy and paste the value of the `signature` attribute from the Pismo's signature envelope file.

Use this command to create a `pismo-signature.data` file.

```shell
base64 -i pismo-signature.base64 -D > pismo-signature.data
```

### Retrieve Pismo's public key

Use [Get public key](https://developers.pismo.io/pismo-docs/reference/get-bulk-keys) to retrieve the Pismo's public key, this step is essential because you need the `key_material` value to create a `der` file in the subsequent step. Once successful, the following response is returned.

```json
200 Ok
{
  "id": "<key_id>",
  "key_material": "<key_material>",
  "expires_at": "2025-05-21T12:27:00Z"
}
```

### Create a der file

The `key_material` attribute in the returned response represents the public key. Copy and save it to a file (`pismo-key.base64`). Then use the following command to decode the string and output it to a `der` file (`pismo-key.der`).

```shell
base64 -i pismo-key.base64 -D > pismo-key.der
```

### Verify signature

To verify the signature, you need the DER file (`pismo-key.der`), the signature file (`pismo-signature.sign`), and the Pismo-signed bulk file. Use the following command to proceed with the verification.

To verify the signature, you need the DER file (`pismo-key.der`), the signature file (`pismo-signature.data`), and the Pismo-signed output file. Use this command to proceed with the verification.

```shell
openssl dgst -sha384 -verify pismo-key.der -keyform DER -signature pismo-signature.data 2024-05-21-15-55-00-<bulk_id>-out.original
```

If the verification is successful, a `Verified OK` message is returned in the command window

# File encryption

## Encryption specification

After signing the bulk file, it must be encrypted using an AES-256 symmetric key. You can obtain this key using the Get AES key endpoint. Keep in mind that each key is single-use, so every time you want to encrypt a bulk file, you must send a new request using a different client-generated bulk ID. The encryption must adhere to these specifications.

* **Algorithm**: AES-256-CBC
* **Key-type**: Symmetric

<Callout icon="📘" theme="info">
  **About the AES key and the symmetric key type**

  * An AES key is a cryptographic key used in the Advanced Encryption Standard (AES) algorithm, which is a symmetric encryption algorithm. The suffix 256 in AES-256 refers to the bit length of the key used in the algorithm. AES is widely used for securing data due to its efficiency and strong security properties.
  * The key type “symmetric” refers to a cryptographic system where the same key is used for both encryption and decryption.
</Callout>

If the request is successfully processed (`200 ok`), you should receive a response in this format.

```json
{
  "aes_key": "<your_aes_key>",
  "iv": "<your_iv>"
}
```

For details about `aes_key` and `iv` in the response, refer to Get AES key.

Run the following command using the values returned for `aes_key` and `iv`in the response to encrypt a bulk file.

```shell
openssl enc -aes-256-cbc -in 2024-05-21-15-55-00-<bulk_id>.plain -out 2024-05-21-15-55-00-<bulk_id>.original -K "<your_aes_key>" -iv "<your_iv>" 
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /corporate/v1/restricted-funds` | `post-corporate-v1-restricted-funds` | Create fund restriction | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `PATCH /corporate/v1/restricted-funds/{restrictedFundsId}` | `patch-corporate-v1-restricted-funds` | Release restriction | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `PUT /corporate/v1/bulk-payments/{bulkId}` | `corporate-put-bulk-file` | Upload bulk file | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-payment-files |
| `POST /corporate/v1/bulk-payments/keys` | `post-bulk-keys` | Upload public key | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-payment-files |
| `PUT /corporate/v2/bulk-payments/encryption-keys/{bulkId}` | `corporate-bulk-payments-put-aes-keys-jwe` | Create AES key (encrypted response) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-payment-files |
| `GET /corporate/v1/bulk-payments/keys/{id}` | `get-bulk-keys` | Get public key | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-payment-files |

### Operation essentials

- **`POST /corporate/v1/restricted-funds`** (`post-corporate-v1-restricted-funds`): security `BearerAuth`; required parameters none declared; required body fields `hold_method`, `amount`, `operation`; response statuses 201, 400, 401, 409, 429, 500; error codes in examples `WRFO0001`, `WRFO0006`, `WRFO0009`, `WOBK0007`, `WRFO0011`, `WRFO0012`, `WRFO0013`, `WRFO0014`, `WRFO0015`, `WRFO0016`, `WRFO0010`, `WRFO0004`, `WRFO0005`, `WRFO0003`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-restricted-funds-1`, `platform-authorization-platform-authorization-1`.
- **`PATCH /corporate/v1/restricted-funds/{restrictedFundsId}`** (`patch-corporate-v1-restricted-funds`): security `BearerAuth`; required parameters `restrictedFundsId` (path); required body fields `amount`, `operation`; response statuses 200, 400, 409, 429, 500; error codes in examples `WRFO0001`, `WRFO0008`, `WRFO0009`, `WOBK0007`, `WRFO0011`, `WRFO0005`, `WRFO0019`, `WRFO0003`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-restricted-funds-1`, `platform-authorization-platform-authorization-1`.
- **`PUT /corporate/v1/bulk-payments/{bulkId}`** (`corporate-put-bulk-file`): security `BearerAuth`; required parameters `bulkId` (path), `signature` (header); required body fields none declared; response statuses 200, 400, 401, 403, 409, 500; error codes in examples `WBUP0001`, `WBUP0004`, `WBUP0005`, `WBUP0006`, `WBUP0007`, `WBUP0008`, `WBUP0009`, `WBUP0010`, `WBUP0003`, `ECMN9999`; events none listed.
- **`POST /corporate/v1/bulk-payments/keys`** (`post-bulk-keys`): security `BearerAuth`; required parameters none declared; required body fields `id`, `key_material`; response statuses 201, 400, 401, 403, 500; error codes in examples `WBPK0001`, `WBPK0002`, `WBPK0004`, `WBPK0005`, `ECMN9999`; events none listed.
- **`PUT /corporate/v2/bulk-payments/encryption-keys/{bulkId}`** (`corporate-bulk-payments-put-aes-keys-jwe`): security `BearerAuth`; required parameters `bulkId` (path); required body fields `public_key_id`; response statuses 200, 401, 403, 404, 500; error codes in examples `ECMN9999`; events none listed.
- **`GET /corporate/v1/bulk-payments/keys/{id}`** (`get-bulk-keys`): security `BearerAuth`; required parameters `id` (path); required body fields none declared; response statuses 200, 401, 403, 404, 500; error codes in examples `ECMN9999`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `patch-corporate-v1-restricted-funds` | `account-balances-balance-change-1` |
| `post-corporate-v1-restricted-funds` | `account-balances-balance-change-1` |
| `patch-corporate-v1-restricted-funds` | `availables-change-available-1` |
| `post-corporate-v1-restricted-funds` | `availables-change-available-1` |
| `patch-corporate-v1-restricted-funds` | `corporate-restricted-funds-1` |
| `post-corporate-v1-restricted-funds` | `corporate-restricted-funds-1` |
| `patch-corporate-v1-restricted-funds` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v1-restricted-funds` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/file-based-processing.md`: updatedAt 2026-04-24T22:11:15.000Z.
- `docs/core-banking/file-signature-and-encryption.md`: updatedAt 2026-04-24T21:57:56.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/file-based-processing.md` | whole document | https://developers.pismo.io/pismo-docs/docs/file-based-processing | `65405d1a8fac9d76…` | 2026-04-24T22:11:15.000Z |
| `docs/core-banking/file-signature-and-encryption.md` | whole document | https://developers.pismo.io/pismo-docs/docs/file-signature-and-encryption | `378afcc127a89ac4…` | 2026-04-24T21:57:56.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--bulk-payment-files` — API reference: Banking - Transaction banking — Bulk payment files
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-BANK-restrictions` — Restrictions: restrict funds, restriction management and operation blocks
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
