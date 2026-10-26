---
ku_id: KU-EVT-verifying-webhook-requests
title: Verifying webhook requests
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/verifying-webhook-requests.md
  sha256: 6b7990115348f73b398fcc06ad7b16e067ecc0f1fec777296eed17b373c7c964
  url: https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests
  role: primary_guide
  updated_at: '2026-06-16T14:28:40.000Z'
operations: []
related_kus:
- KU-EVT-client-webhooks-part-01
- KU-EVT-client-webhooks-part-02
- KU-EVT-client-webhooks-part-03
- KU-EVT-client-webhooks-part-04
- KU-EVT-client-webhooks-part-05
- KU-EVT-client-webhooks-part-06
- KU-EVT-client-webhooks-part-07
- KU-EVT-client-webhooks-part-08
- KU-EVT-client-webhooks-part-09
- KU-EVT-client-webhooks-part-10
- KU-EVT-client-webhooks-part-11
- KU-EVT-client-webhooks-part-12
- KU-EVT-client-webhooks-part-13
- KU-EVT-client-webhooks-part-14
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Verifying webhook requests

**KU ID:** `KU-EVT-verifying-webhook-requests` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/get-started/verifying-webhook-requests.md`:

> You can code  webhooks (user-defined HTTP callbacks) to interact with the Pismo platform during certain operations. For example, Pismo could request approval from you to authorize a purchase. For information on possible webhooks you can code and implement with Pismo, refer to [Client webhooks](https://developers.pismo.io/pismo-docs/docs/client-webhooks).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/verifying-webhook-requests.md`: Verifying webhook requests; Verification process; Parsing the JWT; Retrieving a list of public keys; Renewing your list of public keys; Verifying the token signature; Checking message integrity; Request mTLS support for webhook requests

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/verifying-webhook-requests.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests · updatedAt: 2026-06-16T14:28:40.000Z

<!-- source:begin path=docs/get-started/verifying-webhook-requests.md part=0-end -->

# Verifying webhook requests

You can code  webhooks (user-defined HTTP callbacks) to interact with the Pismo platform during certain operations. For example, Pismo could request approval from you to authorize a purchase. For information on possible webhooks you can code and implement with Pismo, refer to [Client webhooks](https://developers.pismo.io/pismo-docs/docs/client-webhooks).

Webhook requests use <a href="https://jwt.io/" target="_blank">**JSON Web Tokens** </a>(JWTs). Each token is signed with a public/private key pair. Pismo retains the private key and shares the public key with clients. Each token also includes a body hash you can use to verify payload integrity.

## Verification process

The following diagram summarizes the process of verifying a webhook request from the Pismo platform.

<Image align="center" alt="Image shows the process of verifying a webhook request from the Pismo platform." border={true} src="https://files.readme.io/4cddafb-Overview_of_the_verification_process_diagram_V4.png" className="border" />

A request received from Pismo contains a JWT. The JWT contains a signature, along with the name of a public key that you can use to validate the signature.

1. Check the cache to determine whether it contains a public key with that name. If not, request a new list of public keys from the Pismo platform.

2. Use the public key to verify the signature. If successfully verified, you can be assured the request came from Pismo.

3. Verify that the message payload has not been changed in route to your server. To do this, the JWT includes a hash. Run the message payload through SHA256 encryption. The result should match the hash.

The following sections provide a more detailed explanation of these steps.

## Parsing the JWT

When the Pismo platform sends an HTTP request to a client server, the request includes an `Authorization` header containing a JWT. Use this token to authenticate and authorize the request, but you first need to parse it.

JWT is an open standard, and there are many great open-source libraries for parsing a JWT, verifying the cryptographic signature, and retrieving the data contained in the token. Pismo recommends that you use a well maintained and tested library. Here are some good choices:

* [Go](https://github.com/dgrijalva/jwt-go)
* [Python](https://github.com/jpadilla/pyjwt/)
* [NodeJS](https://github.com/auth0/node-jsonwebtoken)
* [Java](https://github.com/auth0/java-jwt)
* [.NET](https://github.com/MSOpenTech/azure-activedirectory-identitymodel-extensions-for-dotnet)

If you need further assistance, contact your Technical Account Manager (TAM) or open a ticket with the [Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk).

A JWT token contains the claims listed in the table below. Use these claims for the next steps in the verification process.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Claim (key)
      </th>

      <th>
        Value
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        alg
      </td>

      <td>
        RS256
      </td>

      <td>
        Algorithm used to generate the JWT signature
      </td>
    </tr>

    <tr>
      <td>
        kid
      </td>

      <td />

      <td>
        This is the ID of the key used to generate the signature. This must be one of the public keys provided by the Pismo platform. Refer to [Retrieving a list of public keys](#retrieving-a-list-of-public-keys).

        Example: 1f88b81429cc451a335c2f5cdb3dfb34eb3bbc7f
      </td>
    </tr>

    <tr>
      <td>
        iss
      </td>

      <td>
        api.pismo.io
      </td>

      <td>
        Issuer of the JWT
      </td>
    </tr>

    <tr>
      <td>
        sub
      </td>

      <td />

      <td>
        The subject claim is the Account ID of the account associated with the request.

        Example: 1000001
      </td>
    </tr>

    <tr>
      <td>
        iat
      </td>

      <td />

      <td>
        The time of the JWT generation in seconds since the UNIX epoch.

        Example: 1584990931
      </td>
    </tr>

    <tr>
      <td>
        exp
      </td>

      <td />

      <td>
        The time at which the token expires in seconds since the UNIX epoch. It can be a maximum of 3600 seconds later than the `iat`.

        Example: 1584990931
      </td>
    </tr>

    <tr>
      <td>
        body-hash
      </td>

      <td />

      <td>
        A SHA256 digest of the base64 encoded request message body.

        Example: dX5GKSLmA9o7lijdQrm7kR4om6rLTHssk1GJQiDGuUk=
      </td>
    </tr>
  </tbody>
</Table>

<br />

## Retrieving a list of public keys

Pismo uses private and public keys to sign JWTs. You don't need to worry about the private keys – those are only used by Pismo – but you will need to get a list of the public keys. To do this, call the public keys endpoint.

```shell Public key request
# These are endpoints where you can get Pismo's public keys:
Sandbox: curl -i https://sandbox.pismolabs.io/v1/certs
Production: curl -i https://<Production Domain>/v1/certs
```

Note: In the request above, `<Production Domain>` needs to be the domain for your production environment.

Once you get the list of public keys, you can cache it and use it to verify the signatures of subsequent requests.

> 🚧 "Should I call the public keys endpoint for every request?"
>
> No. The public keys endpoint has a rate limit of 5 requests per second. To avoid getting rate limited, you should only use the public keys endpoint in the two scenarios listed below.

You should only call the public keys endpoint in the following scenarios:

1. You don’t have the list of public keys yet. You should call the public keys endpoint when you first log in.

2. To renew an expired list, according to the period specified in the **Renewing your list of public keys** section.

## Renewing your list of public keys

The public keys in your list will eventually expire, so your service must include logic for refreshing the public keys. The Pismo platform relies on the HTTP cache-control mechanism to let you know when it's time to renew the public keys in your cache, so you can look at the `Cache-Control` header for instructions on when to call the public keys endpoint again.

The `max-age` component tells you the number of seconds that the requested content will remain valid.

Here's a sample of the contents of a cache-control header:

```
cache-control: public, max-age=23638, must-revalidate, no-transform
```

In this case, you can wait 23638 seconds (6 hours and 34 minutes) before renewing the cached public keys.

<Callout icon="🚧" theme="warn">
  If you can't find the specified public key in your list of public keys, your list has expired and you need to renew it.
</Callout>

## Verifying the token signature

After parsing the JWT, you need to verify that it was signed by Pismo. Start by finding out which public key the Pismo platform used to sign the request by looking for the `kid` (key id) claim in the token.

Next, check to see if you already have the specified key in your local cache. If so, you're ready to verify the signature.

If you don't already have the key, request a new list of public keys using the public keys endpoint. Refer to **Retrieving a list of public keys** for details.

Once you have the specified public key, you can use it to verify the signature. Pismo recommends that you use one of the libraries listed in the **Parsing the JWT** section to do this. For an example signature verification process, go to [JSON Web Signature (JWS) with RSA](https://connect2id.com/products/nimbus-jose-jwt/examples/jws-with-rsa-signature).

If the signature matches, this verifies that the request came from Pismo, and you can proceed to the next step.

> ❗ ️ Signature not matching
>
> If the key names match, but the signature doesn't, it may be the result of some sort of attack. Deny the request immediately and notify the security team.

## Checking message integrity

The next step is to make sure the request payload was not modified during transit. The JWT includes the claim `body-hash`. The `body-hash` value is the hash of the payload of the request. Use this to check the message integrity.

1. Get the whole payload Pismo sent to you on the request.
2. Apply a `SHA256` hash function on the payload and then encode the resulting hash in `base64` format.
3. Get the claim value `body-hash` from JWT.
4. Compare the computed encrypted and encoded payload from Step 2 with the `body-hash` claim value from Step 3. If equal, the verification process is complete and successful.

## Request mTLS support for webhook requests

If you would like to use mTLS for webhook requests, you need to contact your Pismo representative.

This is the general process flow for the request:

1. Open a ticket to request to have mTLS set up.
2. Pismo sends you the Certificate Sign Request (CSR).
3. Sign the certificate and send it back.
4. Pismo uses the certificate to set up mTLS.
<!-- source:end -->

## Lifecycle status

- `docs/get-started/verifying-webhook-requests.md`: updatedAt 2026-06-16T14:28:40.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/verifying-webhook-requests.md` | whole document | https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests | `6b7990115348f73b…` | 2026-06-16T14:28:40.000Z |

## Related knowledge units

- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-EVT-client-webhooks-part-02` — Client webhooks (part 2 of 14)
- `KU-EVT-client-webhooks-part-03` — Client webhooks (part 3 of 14)
- `KU-EVT-client-webhooks-part-04` — Client webhooks (part 4 of 14)
- `KU-EVT-client-webhooks-part-05` — Client webhooks (part 5 of 14)
- `KU-EVT-client-webhooks-part-06` — Client webhooks (part 6 of 14)
- `KU-EVT-client-webhooks-part-07` — Client webhooks (part 7 of 14)
- `KU-EVT-client-webhooks-part-08` — Client webhooks (part 8 of 14)
- `KU-EVT-client-webhooks-part-09` — Client webhooks (part 9 of 14)
- `KU-EVT-client-webhooks-part-10` — Client webhooks (part 10 of 14)
- `KU-EVT-client-webhooks-part-11` — Client webhooks (part 11 of 14)
- `KU-EVT-client-webhooks-part-12` — Client webhooks (part 12 of 14)
- `KU-EVT-client-webhooks-part-13` — Client webhooks (part 13 of 14)
- `KU-EVT-client-webhooks-part-14` — Client webhooks (part 14 of 14)
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
