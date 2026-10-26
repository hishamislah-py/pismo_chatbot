---
ku_id: KU-AUTH-authentication-methods
title: 'API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys'
category: authentication_and_security
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/authentication-with-oauth2.md
  sha256: f2d99ccb149ebbf04a88b6531664746abed5f2790dd2603717b9075850907f25
  url: https://developers.pismo.io/pismo-docs/docs/authentication-with-oauth2
  role: primary_guide
  updated_at: '2026-07-15T20:21:36.000Z'
- path: docs/get-started/authentication-with-openid.md
  sha256: db8abce2b52fb6952e257d81159a802049998a224d2f30381003542cf5ed4643
  url: https://developers.pismo.io/pismo-docs/docs/authentication-with-openid
  role: primary_guide
  updated_at: '2026-08-04T15:36:51.000Z'
- path: docs/get-started/basic-authentication-with-client-credentials.md
  sha256: f8cba3ba9ed956e91669684e3744ec6da07c91e9a084a55dacbf0ff04ae4b69c
  url: https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials
  role: primary_guide
  updated_at: '2026-08-06T15:09:08.000Z'
- path: docs/get-started/third-party-authentication-with-openid.md
  sha256: 49a927340cdbc916aa1ee2ad48427af30a3dc583c612f671dc03a92837061528
  url: https://developers.pismo.io/pismo-docs/docs/third-party-authentication-with-openid
  role: primary_guide
  updated_at: '2026-07-16T15:03:19.000Z'
- path: docs/control-center/access-keys-for-basic-authentication.md
  sha256: 161f106285ce0ef72d2572a8d25fa7ad9528fd79629978b00221e28d90806c86
  url: https://developers.pismo.io/pismo-docs/docs/access-keys-for-basic-authentication
  role: primary_guide
  updated_at: '2026-08-05T11:14:10.000Z'
operations:
- post-passport-v2-s2s-access-token
related_kus:
- KU-API-platform-authentication--authentication
- KU-AUTH-control-center-security
- KU-CC-dual-approval
- KU-EVT-verifying-webhook-requests
grouping_rationale: Alternative ways to obtain API credentials and tokens; access keys are the credentials used by basic authentication.
---

# API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys

**KU ID:** `KU-AUTH-authentication-methods` · **Category:** Authentication and security · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 5 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Alternative ways to obtain API credentials and tokens; access keys are the credentials used by basic authentication.

Scope as stated in `docs/get-started/authentication-with-oauth2.md`:

> The Pismo platform supports OAuth2 authentication using stored credentials. Pismo's OAuth2 implementation follows the RFC 6749 specification, providing secure token-based authentication for API access. This guide explains how to obtain access tokens using the Client Credentials grant type.

Scope as stated in `docs/get-started/authentication-with-openid.md`:

> OpenID Connect (OIDC) for Servers is the preferred way to authenticate with the Pismo platform. It provides greater security guarantees in service communications than basic authentication using client credentials. OIDC authentication uses permission groups to control access to Pismo API endpoints. Through these permission groups, you can give targeted access to only a specific set of endpoints to different groups within your organization or to a third party. To request an access token, use the <Anchor label="Get_OpenID_access_token" target="_blank" href="ref:post-passport-v1-oauth2-token">Get\_OpenID\_access\_token</Anchor> endpoint.

Scope as stated in `docs/get-started/basic-authentication-with-client-credentials.md`:

> The Pismo platform supports server-to-server (S2S) authentication using stored credentials. This is similar to a username/password system, except it uses a `server_key` and a `server_secret` key.

Scope as stated in `docs/get-started/third-party-authentication-with-openid.md`:

> Regardless of the authentication type you use (basic authentication with client credentials, authentication with OAuth2, or authentication with OpenID Connect), the Pismo platform enables you to give a third party access to a restricted set of Pismo endpoints that they can use within your organization.

Scope as stated in `docs/control-center/access-keys-for-basic-authentication.md`:

> If you're using basic authentication (also known as server-to-server or S2S), Pismo provides you with an encryption key pair—a server key and a server secret. These are the credentials your client applications will use to connect to the Pismo platform.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/authentication-with-oauth2.md`: Authentication with OAuth2; Endpoint information; Grant type; Request parameters; Scope attribute; UID Attribute; Using the access token; Renewing an expired token; Best practices; Security considerations; Third-party authentication with OAuth2
- `docs/get-started/authentication-with-openid.md`: Authentication with OpenID Connect; Server authentication; Generate your JWT; Using the JWT to request an access token; Handling the response; Calling Pismo APIs; Third-party authentication with OIDC
- `docs/get-started/basic-authentication-with-client-credentials.md`: Basic authentication with client credentials; Initial authentication; Renewing an expired token; Best practices; Security considerations; Third-party authentication with Basic authentication
- `docs/get-started/third-party-authentication-with-openid.md`: Third-party authentication; Setting up third-party authentication; Third-party authentication with Basic or OAuth2 authentication; Third-party authentication with OpenID Connect
- `docs/control-center/access-keys-for-basic-authentication.md`: Access keys

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/authentication-with-oauth2.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/authentication-with-oauth2 · updatedAt: 2026-07-15T20:21:36.000Z

<!-- source:begin path=docs/get-started/authentication-with-oauth2.md part=0-end -->

# Authentication with OAuth2

The Pismo platform supports OAuth2 authentication using stored credentials. Pismo's OAuth2 implementation follows the RFC 6749 specification, providing secure token-based authentication for API access. This guide explains how to obtain access tokens using the Client Credentials grant type.

### Endpoint information

Token Endpoint

Sandbox: `POST https://sandbox.pismolabs.io/passport/v2/oauth/token`

### Grant type

Pismo supports the Client Credentials grant type (`client_credentials`), which is designed for server-to-server authentication where the client application needs to access resources under its own identity.

### Request parameters

**Required parameters**

| Parameter       | Type   | Description                                                                    |
| :-------------- | :----- | :----------------------------------------------------------------------------- |
| `grant_type`    | string | Must be set to `client_credentials`                                            |
| `client_id`     | string | Your application's client identifier (server key)                              |
| `client_secret` | string | Your application's client secret (server secret)                               |
| `scope`         | string | Space-separated list of permission groups that define the token's access scope |

**Optional parameter**

| Parameter | Type   | Description                                                                       |
| :-------- | :----- | :-------------------------------------------------------------------------------- |
| `uid`     | string | Account ID for account-specific token generation (required for certain endpoints) |

### Scope attribute

Use the `scope` parameter to specify which groups of endpoints your token can access. You can pass:

* A single group: `pismo-v1:accounts:rw`
* Multiple groups separated by spaces: `pismo-v1:accounts:rw pismo-v1:cards:rw pismo-v1:bankaccounts:rw`

Pismo strongly recommends segregating tokens by using a reduced scope that includes only the specific permissions your application requires for each operation. This approach follows the principle of least privilege and provides several critical security benefits:

* Minimizes the potential damage from token compromise by limiting access to only necessary resources
* Reduces the attack surface by preventing unauthorized access to unrelated endpoints
* Enables better audit trails by clearly defining what each token can access
* Allows for more granular access control that can be easily monitored and revoked if suspicious activity is detected.

You can check all available scopes through Control Center. Refer to the Control Center <Anchor label="Permission groups" target="_blank" href="doc:cc-api-permission-groups">Permission groups</Anchor> guide for details.

### UID Attribute

Use the `uid` parameter for account-specific token generation. If you intend to make calls on behalf of a specific account, you must also include the corresponding account identifier (`uid`). If you provide an account identifier, subsequent calls can only access resources that belong to that particular account.

You can find a complete list of the endpoints that you can use for requests in the API Reference. For a list of the endpoints that require the account identifier, refer to <Anchor label="Endpoints that require an account-specific token" target="_blank" href="ref:endpoints-that-require-an-account-specific-token">Endpoints that require an account-specific token</Anchor>.

To request an access token, use the following endpoint: `Get Oauth access token`

```json
curl --request POST \ 

  --url https://sandbox.pismolabs.io/passport/v2/oauth/token \ 

  --header 'Content-Type: application/x-www-form-urlencoded' \ 

  --data-urlencode grant_type=client_credentials \ 

  --data-urlencode 'scope=pismo-v1:accounts:rw pismo-v1:cards:rw pismo-v1:bankaccounts:rw' \ 

  --data-urlencode 'client_id=<your_client_id>' \ 

  --data-urlencode 'client_secret=<your_client_secret>' \ 

  --data-urlencode uid=12345 

```

**Sample response**

The following code shows an example of a response body for this request. It includes an access token (`token`), which you can use as an authorization header in future requests.

```json
{ 

  "access_token": "<JWT_ACCESS_TOKEN>", 

  "token_type": "Bearer", 

  "expires_in": 3599, 

  "scope": "pismo-v1:accounts:rw pismo-v1:cards:rw pismo-v1:bankaccounts:rw" 

} 
```

# Using the access token

Include the access token in the Authorization header of your API requests:

`Authorization: Bearer <your_bearer_token>`

> 📘 Access tokens expire after one hour (3600 seconds)
>
> Your application should catch the error generated when this happens. It can then generate another JWT.

# Renewing an expired token

Pismo does not support renewing `access_token`. The access token has a predefined lifetime. There is an `exp` field in the JWT that contains the date/time of expiration in <Anchor label="Unix Epoch time" target="_blank" href="https://www.unixtutorial.org/epoch-time/">Unix Epoch time</Anchor>. After the access token expires, the Pismo platform rejects additional requests. If you make a request using an expired token, the request returns `Unauthorized`. You should check for this message in your code and request a new access token when you receive it.

<Callout icon="📘" theme="info">
  You can use the <Anchor label="JWT Debugger" target="_blank" href="https://jwt.io/">JWT Debugger</Anchor> website to view the fields in a JWT. Holding the mouse pointer over the decoded `exp` value displays it as a human-readable date/time.

  If you need to access the field values in your code, refer to <Anchor label="Parsing the JWT" target="_blank" href="doc:verifying-webhook-requests#parsing-the-jwt">Parsing the JWT</Anchor>.
</Callout>

## Best practices

* **Secure storage**—Store your client credentials securely and never expose them in client-side code.
* **Token Caching**—Cache tokens and reuse them until they expire to reduce unnecessary requests.
* **Error Handling**—Implement proper error handling for token expiration (401).
* **Least Privilege**—Request only the scopes your application actually needs.
* **Keep JWT scope focused**—Generate the JWT with the group for the intended API making the request.

## Security considerations

* Monitor for unauthorized access attempts
* Rotate client credentials regularly

# Third-party authentication with OAuth2

The Pismo platform enables you to give a third-party access to a restricted set of Pismo endpoints that they can use within your organization. This would enable them to authenticate with the Pismo platform, but they would only get access to the specific endpoints that you want them to access. For more information, refer to the <Anchor label="Third-party authentication" target="_blank" href="doc:third-party-authentication-with-openid">Third-party authentication</Anchor> guide.

<br />
<!-- source:end -->

### Source 2: `docs/get-started/authentication-with-openid.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/authentication-with-openid · updatedAt: 2026-08-04T15:36:51.000Z

<!-- source:begin path=docs/get-started/authentication-with-openid.md part=0-end -->

# Authentication with OpenID Connect

OpenID Connect (OIDC) for Servers is the preferred way to authenticate with the Pismo platform. It provides greater security guarantees in service communications than basic authentication using client credentials. OIDC authentication uses permission groups to control access to Pismo API endpoints. Through these permission groups, you can give targeted access to only a specific set of endpoints to different groups within your organization or to a third party. To request an access token, use the <Anchor label="Get_OpenID_access_token" target="_blank" href="ref:post-passport-v1-oauth2-token">Get\_OpenID\_access\_token</Anchor> endpoint.

# Server authentication

During onboarding to production, you must generate at least one pair of public and private keys for OpenID authentication. Then, you must generate and sign a **JSON Web Token** (JWT) for each key pair that you generate. For more information about JWTs, refer to <Anchor label="Generate your JWT" target="_blank" href="#generate-your-jwt">Generate your JWT</Anchor>.

1. Use the <Anchor label="OpenSSL" target="_blank" href="https://www.openssl.org/">OpenSSL</Anchor> toolkit to generate a private key and a public key, using the following commands:

```text Generating private and public keys
Generate a private key:
  $ openssl genpkey -out rsakey.pem -algorithm RSA -pkeyopt rsa_keygen_bits:2048
Generate a public key based on the private key you generated:
  $ openssl rsa -in rsakey.pem -out rsa.pub -pubout -outform PEM
```

2. Store your private key securely, and then create an OIDC authentication configuration in Control Center. For more information, refer to the Control Center <Anchor label="OpenID Connect" target="_blank" href="doc:openid-configurations">OpenID Connect</Anchor> guide.
3. Generate your JWT using the private key associated with the public key you shared, using the <Anchor label="claims values here" target="_blank" href="#generate-your-jwt">claims values here</Anchor>.
   <Callout icon="📘" theme="info">
     Note that if you are giving third-party access, the third party needs to be able to generate JWTs, as described in <Anchor label="Generate your JWT" target="_blank" href="doc:authentication-with-openid#generate-your-jwt">Generate your JWT</Anchor>. The JWT generated for this authentication must have a unique value for the `aud`claim. This is how the Pismo platform can tell that a request comes from a third party, not the direct client.
   </Callout>
4. Request an access token using the endpoint <Anchor label="Get OpenID access token" target="_blank" href="ref:post-passport-v1-oauth2-token-1">Get OpenID access token</Anchor>.
   <Callout icon="📘" theme="info">
     The response to this call includes an access token that you can use with an API endpoint. If the response does not include an access token, your JWT might not be properly formed.
   </Callout>
5. Retrieve the access token returned in the Pismo response.
6. Use this access token to make API calls.

The following diagram illustrates steps 3 to 6:

<Image align="center" alt="Diagram illustrating token requests and responses" border={true} src="https://files.readme.io/2676e0d-Authentication_with_OpenID_Connect_for_Servers_V6.png" className="border" />

# Generate your JWT

<a name="generate-your-jwt" />

Generate and sign a JWT using the private key you generated (in Step 1 above). This JWT should contain the following claims:

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Claim (key)
      </th>

      <th>
        Type
      </th>

      <th>
        Mandatory
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
        Fixed string value
      </td>

      <td>
        Yes
      </td>

      <td>
        RS256
      </td>

      <td>
        This is part of the header.
      </td>
    </tr>

    <tr>
      <td>
        typ
      </td>

      <td>
        Fixed string value
      </td>

      <td>
        Yes
      </td>

      <td>
        JWT
      </td>

      <td>
        This is part of the header.
      </td>
    </tr>

    <tr>
      <td>
        iss
      </td>

      <td>
        Fixed string value
      </td>

      <td>
        Yes
      </td>

      <td />

      <td>
        This is the verifier Issuer. This value is provided by Pismo, automatically generated by Control Center when a user creates a new credential.
      </td>
    </tr>

    <tr>
      <td>
        sub
      </td>

      <td>
        Fixed string value
      </td>

      <td>
        Yes
      </td>

      <td />

      <td>
        This is the verifier Subject. This value is provided by Pismo, automatically generated by Control Center when a user creates a new credential.
      </td>
    </tr>

    <tr>
      <td>
        aud
      </td>

      <td>
        Fixed string value
      </td>

      <td>
        Yes
      </td>

      <td />

      <td>
        This is the verifier Audience. This value is provided by Pismo, automatically generated by Control Center when a user creates a new credential.
      </td>
    </tr>

    <tr>
      <td>
        iat
      </td>

      <td>
        Timestamp number
      </td>

      <td>
        Yes
      </td>

      <td>
        ex: 1697044489
      </td>

      <td>
        The current time in seconds since the UNIX epoch.
      </td>
    </tr>

    <tr>
      <td>
        exp
      </td>

      <td>
        Timestamp number
      </td>

      <td>
        Yes
      </td>

      <td>
        ex: 1697048089
      </td>

      <td>
        The time in seconds since the UNIX epoch at which the token expires. It can be a maximum of 3600 seconds later than the `iat`.
      </td>
    </tr>

    <tr>
      <td>
        tenant\_id
      </td>

      <td>
        Fixed string value
      </td>

      <td>
        Yes
      </td>

      <td>
        ex: YcjCAADMVI-TN-e3adf01
      </td>

      <td>
        The unique tenant identifier of the user/token.

        Value provided by Pismo, automatically generated by Control Center when a new OpenID key is registered.

        This is not to be confused with the Org ID.
      </td>
    </tr>

    <tr>
      <td>
        uid
      </td>

      <td>
        String value
      </td>

      <td>
        Yes (refer to <Anchor label="Endpoints that require an account-specific token" target="_blank" href="ref:endpoints-that-require-an-account-specific-token">Endpoints that require an account-specific token</Anchor>)
      </td>

      <td>
        ex: "uid": "104753059"
      </td>

      <td>
        The Account ID of the Pismo customer.

        If you want a token without Account ID,  do not send the claim **uid** on the JWT.
      </td>
    </tr>

    <tr>
      <td>
        pismo
      </td>

      <td>
        Object type
      </td>

      <td>
        Yes
      </td>

      <td>
        ex:\
        "pismo": \{\
        "group": "pismo-v1:accounts:rw,pismo-v1:admin:rw"\
        },
      </td>

      <td>
        The identifier of the group that you want your token to have access to. A group has access to a certain subset of endpoints. You can add more than one group, separated by a comma.

        You can find the list of valid groups on Control Center under the section **Permission groups** in the main menu. Otherwise, contact your Pismo representative.

        For full details on API permission groups, refer to the <Anchor label="Permission groups" target="_blank" href="doc:cc-api-permission-groups">Permission groups</Anchor> guide.
      </td>
    </tr>

    <tr>
      <td>
        customClaims
      </td>

      <td>
        Object type
      </td>

      <td>
        No
      </td>

      <td>
        "customClaims": \{\
        "custom1": "someValue",\
        "userexample": "myusername"\
        },
      </td>

      <td>
        Optional custom claims.
      </td>
    </tr>
  </tbody>
</Table>

Example of the structure of the JWT that you should generate on your side in order to use OpenID authentication:

```Text JWT sample header
Header
{
  "alg": "RS256",
  "typ": "JWT"
}
```

```json JWT sample payload
Payload
{
  "aud": "<value provided by Pismo>",
  "iss": "<value provided by Pismo>",
  "sub": "<Value provided by Pismo>",
  "tenant_id": "<Value provided by Pismo>",
  "pismo": {
    "group": "pismo-v1:some-samplegroup:rw"
  },
  "uid": "123123",
  "exp": 1724348241,
  "iat": 1724344641,
  "customClaims": {
    "custom1": "someValue",
    "userexample": "user@user.com"
  }
}
```

<Callout icon="📘" theme="info">
  In the Payload example above, all values marked as "value provided by Pismo" are automatically generated in Control Center when a new OpenID is generated. You can find the values on the OpenID Connect details page.

  <Image align="center" alt="Screenshot of Control Center OpenID Connect details page" src="https://files.readme.io/c21cab544c25a9000f64f7d652d496fb408341ce2304dde36f640fc17a6a2f6f-OpenID-ControlCenter2.png" />
</Callout>

You can find the list of groups available for your organization in Control Center. For more information, refer to <Anchor label="Permission groups" target="_blank" href="doc:cc-api-permission-groups">Permission groups</Anchor>.

**uid** is required on all <Anchor label="endpoints that require an account-specific token" target="_blank" href="ref:endpoints-that-require-an-account-specific-token">endpoints that require an account-specific token</Anchor>.

To generate JWTs, we recommend you use one of the libraries provided at <Anchor label="jwt.io" target="_blank" href="https://jwt.io/">jwt.io</Anchor>. You can use any trusted helper library that is compatible with your stack.

The following code sample shows how to create a signed JWT in a few languages:

```go GoLang
package main

import (
    "fmt"
    "time"

    "github.com/dgrijalva/jwt-go"
)

var mySigningKey = []byte(`
-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
`)

func main() {

    key, err := jwt.ParseRSAPrivateKeyFromPEM(mySigningKey)
    fmt.Println(err)

    token := jwt.NewWithClaims(jwt.SigningMethodRS256, jwt.MapClaims{
        "iss":       "test-123@test-7a65.iam.gserviceaccount.com",
        "aud":       "https://identitytoolkit.googleapis.com/google.identity.identitytoolkit.v1.IdentityToolkit",
        "exp":       time.Now().Add(time.Hour).Unix(),
        "iat":       time.Now().Unix(),
        "sub":       "test-123@test-7a65.iam.gserviceaccount.com",
        "uid":       "12345678910",
        "tenant_id": "test-pbrj4",
    })

    // Sign and get the complete encoded token as a string using the secret
    tokenString, err := token.SignedString(key)
    fmt.Println(tokenString, err)

}
```

```java Java
package com.star.sud;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.security.*;
import java.security.interfaces.RSAPrivateKey;
import java.security.spec.PKCS8EncodedKeySpec;
import java.time.Instant;
import java.util.*;

import io.jsonwebtoken.*;


public class JwtTokenwithRsa {

	//Reference to your private key
	public static final String PRIVATE_KEY_FILE_PATH = "RSA/rsakey.pem";

	public static void main(String[] args) {
		try {
			JwtTokenwithRsa tokenwithRsa = new JwtTokenwithRsa();
			tokenwithRsa.generateJWTWithRsa();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public String generateJwtToken(PrivateKey privateKey) {
		JwtBuilder builder = Jwts.builder().signWith(SignatureAlgorithm.RS256, privateKey);

		long issuedAt = Instant.now().getEpochSecond();
		long expiresAt = Instant.now().plusSeconds(3600).getEpochSecond();
		Map<String,String> pismoClaims = new HashMap<String,String>();
		pismoClaims.put("group","pismo-v1:samplegroup:rw");

		builder.claim("aud", "value provided by Pismo");
		builder.claim("sub", "value provided by Pismo");
		builder.claim("iss", "value provided by Pismo");
		builder.claim("exp", expiresAt);
		builder.claim("iat",issuedAt);
		builder.claim("pismo", pismoClaims);
		builder.claim("tenant_id", "Your Tenant ID");
		builder.claim("uid", "Account Id or Tenant Id");


		String token = builder.compact();
		return token;
	}

	public void generateJWTWithRsa() throws Exception {
		KeyPairGenerator keyGenerator = KeyPairGenerator.getInstance("RSA");
		keyGenerator.initialize(1024);

		File f = new File(PRIVATE_KEY_FILE_PATH);
		PrivateKey privateKey = readPrivateKey(f);


		// Generate Token
		String id = UUID.randomUUID().toString();
		String token = generateJwtToken(privateKey);
		System.out.println("TOKEN:");
		System.out.println(token);

	}

	public RSAPrivateKey readPrivateKey(File file) throws Exception {
		String key = new String(Files.readAllBytes(file.toPath()), Charset.defaultCharset());

		String privateKeyPEM = key
				.replace("-----BEGIN PRIVATE KEY-----", "")
				.replaceAll(System.lineSeparator(), "")
				.replace("-----END PRIVATE KEY-----", "");

		byte[] encoded = Base64.getDecoder().decode(privateKeyPEM);

		KeyFactory keyFactory = KeyFactory.getInstance("RSA");
		PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(encoded);
		return (RSAPrivateKey) keyFactory.generatePrivate(keySpec);
	}

}
```

```node Node
To be released
```

```python Python
import jwt
import time
# Read the private key from a file
with open('/Users/agentle/tools/pismo-jwt/rsakey.pem', 'r') as key_file:
    private_key = key_file.read()
if not private_key:
    raise ValueError("You must provide a private key to generate the JWT.")
# Generate the current time in seconds since the UNIX epoch
current_time = int(time.time())
# Define the expiration time (such as 1 hour from now)
expiration_time = current_time + 3600  # 3600 seconds = 1 hour
payload = {"iss":       "MitXVzVtmT-TN-e3adf01@dev-gke-a4019.iam.gserviceaccount.com",
           "aud":       "https://identitytoolkit.googleapis.com/google.identity.identitytoolkit.v1.IdentityToolkit",
           "exp":       expiration_time,
           "iat":       current_time,
           "sub":       "MitXVzVtmT-TN-e3adf01@dev-gke-a4019.iam.gserviceaccount.com",
           "tenant_id": "MitXVzVtmT-TN-e3adf01",
           "pismo": {
                "group": "pismo-v1:accounts:rw,pismo-v1:admin:rw"
                    }
        }
# for an endpoint requiring account token here's an
# account ID "uid": "104753059"
token = jwt.encode(payload, private_key, algorithm='RS256')
print(token)
```

## Using the JWT to request an access token

After generating the signed JWT, you can use it to request an access token. This access token request is an HTTPS POST request.

Method: `POST`

Content-Type: `application/json`

Endpoint: `{environment}/passport/v1/oauth2/token`

Request body payload:

| Property Name | Type   | Description                                        |
| :------------ | :----- | :------------------------------------------------- |
| token         | string | A custom token you use to request an access token. |

The following sample code shows a cURL POST request for an access token in the Pismo Sandbox:

```curl
curl --request POST \
--url https://sandbox.pismolabs.io/passport/v1/oauth2/token \
--header 'Content-Type: application/json' \
--data '{
"token":"<your_bearer_token>"
}'
```

## Handling the response

If the JWT is properly formed and your service has permission to perform the operation, then the JSON response from the authorization server should include an access token. The following is an example response.

```json
{
  "access_token": "<your_bearer_token>",
  "refresh_token": "<your_refresh_token>",
  "expires_in": "3600"
}
```

> 📘 Access tokens expire after one hour
>
> Your application should catch the error generated when this happens. It can then generate another JWT, sign it, and request another access token.

# Calling Pismo APIs

After your application obtains an access token, you can use it to make calls to a Pismo API on behalf of the given user account. To do this, include the access token in the `authorization: Bearer` header  of each request, as example below.

```curl cURL on a service
curl --request POST \
  --url https://sandbox.pismolabs.io/service/v1/service/example/payment \
  --header 'Content-Type: application/json' \
  --header 'accept: application/json' \
  --header 'authorization: Bearer <your_bearer_token>' \
  --data '{< JSON body the service expects to receive>}'

```

# Third-party authentication with OIDC

OIDC authentication uses permission groups to control access to Pismo API endpoints. Through these permission groups, you can give a third party access to only a specific set of endpoints within your organization. For more information, refer to the <Anchor label="Third-party authentication" target="_blank" href="doc:third-party-authentication-with-openid">Third-party authentication</Anchor> guide.

<br />
<!-- source:end -->

### Source 3: `docs/get-started/basic-authentication-with-client-credentials.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials · updatedAt: 2026-08-06T15:09:08.000Z

<!-- source:begin path=docs/get-started/basic-authentication-with-client-credentials.md part=0-end -->

# Basic authentication with client credentials

The Pismo platform supports server-to-server (S2S) authentication using stored credentials. This is similar to a username/password system, except it uses a `server_key` and a `server_secret` key.

The Pismo platform's Passport API allows server-to-server authentication, so a proxy server can execute some operations. For example, in the case of a person using an app on a mobile device or an operator using a CRM system, the authentication process should go through a proxy server.

# Initial authentication

When first logging in from an external server, you need to send the Pismo platform a request to create an access token. Pismo will return a JSON Web Token (JWT). You must include your `server_key` and `server_secret` in the body of the request.

If you intend to make calls on behalf of a specific account, you must also include the corresponding account identifier (`account_id`). If you provide an account identifier, subsequent calls can only access resources that belong to that particular account.

You can find a complete list of the endpoints that you can use for requests in the API Reference. For a list of the endpoints that require the account identifier, see [Endpoints that require an account-specific token](https://developers.pismo.io/pismo-docs/reference/endpoints-that-require-an-account-specific-token).

To request an access token, use the following endpoint.

[Get basic authentication access token](https://developers.pismo.io/pismo-docs/reference/post-passport-v2-s2s-access-token)\
Request body:

```json
{
  "server_key": "<server_key_provided>",
  "server_secret": "<server_secret_key_provided>",
  "account_id": <account_holder_identifier>
}
```

The following code shows an example of a response body for this request. It includes an access token (`token`), which you can use as an authorization header in future requests.

```json
{
  "server_key": "<server_key_provided>",
  "tenant": "<tenant>",
  "program_ids": [],
  "roles": [
    "account-server",
    "onboarding-server",
    "crm-server",
    "crm-operator"
  ],
  "token": "<your_bearer_token>",
  "refresh": "<your_refresh_token>"
}
```

> 📘 Access tokens expire after 10 minutes
>
> Your application should catch the error generated when this happens. It can then generate another JWT, sign it, and request another access token.

# Renewing an expired token

Pismo does not support renewing `access_token`.The access token has a predefined lifetime. There is an `exp` field in the JWT that contains the date/time of expiration in [Unix Epoch time](https://www.unixtutorial.org/epoch-time/). After the access token expires, the Pismo platform rejects additional requests. If you make a request using an expired token, the request returns `Unauthorized`. You should check for this message in your code and request a new access token when you receive it.

<Callout icon="📘" theme="info">
  You can use the [JWT Debugger](https://jwt.io/) website to view the fields in a JWT. Holding the mouse pointer over the decoded `exp` value displays it as a human-readable date/time.

  If you need to access the field values in your code, refer to [Parsing the JWT](https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests#parsing-the-jwt).
</Callout>

## Best practices

* **Secure storage**—Store your client credentials securely and never expose them in client-side code.
* **Token Caching**—Cache tokens and reuse them until they expire to reduce unnecessary requests.
* **Error Handling**—Implement proper error handling for token expiration (401).
* **Least Privilege**—Request only the scopes your application actually needs.
* **Keep JWT scope focused**—Generate the JWT with the group for the intended API making the request.

## Security considerations

* Monitor for unauthorized access attempts
* Rotate client credentials regularly

# Third-party authentication with Basic authentication

The Pismo platform enables you to give a third-party access to a restricted set of Pismo endpoints that they can use within your organization. This would enable them to authenticate with the Pismo platform, but they would only get access to the specific endpoints that you want them to access. For more information, refer to the <Anchor label="Third-party authentication" target="_blank" href="doc:third-party-authentication-with-openid">Third-party authentication</Anchor> guide.
<!-- source:end -->

### Source 4: `docs/get-started/third-party-authentication-with-openid.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/third-party-authentication-with-openid · updatedAt: 2026-07-16T15:03:19.000Z

<!-- source:begin path=docs/get-started/third-party-authentication-with-openid.md part=0-end -->

# Third-party authentication

Regardless of the authentication type you use (basic authentication with client credentials, authentication with OAuth2, or authentication with OpenID Connect), the Pismo platform enables you to give a third party access to a restricted set of Pismo endpoints that they can use within your organization.

For example, you could give a company access to only those endpoints that are included in the group `pismo-v2:bankaccounts:rw`. This would enable them to authenticate with the Pismo platform, but they would only get access to the endpoints for reading and writing to bank accounts.

By restricting third parties to just the endpoints they need to do their job, you improve your security and limit your liability.

<Callout icon="🚧" theme="warn">
  You should never give a third party full access to the Pismo APIs.
</Callout>

# Setting up third-party authentication

The way you can set up third-party authentication depends on the type of server authentication you've chosen. Refer to the applicable section for instructions.

## Third-party authentication with Basic or OAuth2 authentication

Every organization on the Pismo platform has an org ID that you can use to authenticate with the Pismo platform. To give a third party restricted access to your organization, you must open a ticket with the <Anchor label="Pismo Service Desk" target="_blank" href="https://pismolabs.atlassian.net/servicedesk/customer/portal/3">Pismo Service Desk</Anchor> requesting that the security team provide access for a party that works only for specific endpoints. Normally, you would specify the endpoints by indicating one or more access groups.

<Callout icon="🚧" theme="warn">
  You should never allow different third parties to use the same org ID, even if they are accessing the same subset of endpoints. Request a separate ID for each party instead. This way, you can always tell which party originated a request.
</Callout>

## Third-party authentication with OpenID Connect

OIDC authentication uses permission groups to control access to Pismo API endpoints. Through these permission groups, you can give a third party access to only a specific set of endpoints within your organization. You create OIDC configurations in Control Center. For more information, refer to the Control Center <Anchor label="OpenID Connect" target="_blank" href="doc:openid-configurations">OpenID Connect</Anchor> guide.

<Callout icon="📘" theme="info">
  Note that the third party needs to be able to generate JWTs, as described in <Anchor label="Generate your JWT" target="_blank" href="doc:authentication-with-openid#generate-your-jwt">Generate your JWT</Anchor>. Also, the JWT generated for this authentication must have a unique value for the `aud` claim. This is how the Pismo platform can tell that a request comes from a third party, not the direct client.
</Callout>

Once third-party authentication is configured, your third party can access the specified endpoints using the procedure described in <Anchor label="Authentication with OpenID Connect" target="_blank" href="doc:openid-configurations">Authentication with OpenID Connect</Anchor>.
<!-- source:end -->

### Source 5: `docs/control-center/access-keys-for-basic-authentication.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/access-keys-for-basic-authentication · updatedAt: 2026-08-05T11:14:10.000Z

<!-- source:begin path=docs/control-center/access-keys-for-basic-authentication.md part=0-end -->

# Access keys

If you're using basic authentication (also known as server-to-server or S2S), Pismo provides you with an encryption key pair—a server key and a server secret. These are the credentials your client applications will use to connect to the Pismo platform.

* **Server key** (`server_key`)—identifies and authenticates your server (public identifier)
* **Server secret** (`server_secret`)—used to prove identity (must remain confidential)

If you're a Control Center administrator, you can list all access keys related to your organization, create new keys, or deactivate keys from the **Access keys** screen.

> 📘 Dual approval
>
> If your company is using the dual approval feature, creating or deactivating an access key requires approval. With dual approval, you initiate the change and submit a request for approval. A second person must review and approve it. The change doesn't take effect until the request is approved.
>
> If you don't create an access key within 24 hours of approval, the approval expires and you must request approval for a new access key.
>
> For more information about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).

To create access keys:

1. From the main menu, select **Users & permissions** > **Access keys**.

2. On the **Access keys** screen, select **Create key** to generate a new key pair.\
   Note: you can only create access keys during business hours of the timezone defined for the environment. A highlighted message is displayed across the top of the screen if you are working outside of the defined environment's work hours.

3. Select **Copy credentials** to copy the keys to your computer's clipboard.

<Callout icon="🚧" theme="warn">
  The credentials are displayed only once. Store them in a safe place for later reference. If you lose them, you must generate a new pair.
</Callout>

To deactivate an existing access key:

1. From the main menu, select **Users & permissions** > **Access keys**.
2. On the **Access keys** screen, find the key you want to deactivate and slide the status indicator to the left to switch from **Active** to **Deactivated**.
3. A warning dialog displays to indicate that deactivating the access key is permanent and the key cannot be reactivated. If you need access again, you will need to create a new key. To continue to deactivate the key, select **Deactivate key**.

For more information about Control Center security, refer to [Security guide for Control Center](https://developers.pismo.io/pismo-docs/docs/security-guide-for-control-center).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v2/s2s/access-token` | `post-passport-v2-s2s-access-token` | Get basic authentication access token | `api-specs/Platform_authentication.yaml` | no | KU-API-platform-authentication--authentication |

### Operation essentials

- **`POST /v2/s2s/access-token`** (`post-passport-v2-s2s-access-token`): security not declared; required parameters none declared; required body fields `server_key`, `server_secret`; response statuses 201, 401, 500; error codes in examples none; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `endpoints-that-require-an-account-specific-token` | Endpoints that require an account-specific token | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Lifecycle status

- `docs/get-started/authentication-with-oauth2.md`: updatedAt 2026-07-15T20:21:36.000Z.
- `docs/get-started/authentication-with-openid.md`: updatedAt 2026-08-04T15:36:51.000Z.
- `docs/get-started/basic-authentication-with-client-credentials.md`: updatedAt 2026-08-06T15:09:08.000Z.
- `docs/get-started/third-party-authentication-with-openid.md`: updatedAt 2026-07-16T15:03:19.000Z.
- `docs/control-center/access-keys-for-basic-authentication.md`: updatedAt 2026-08-05T11:14:10.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- Operation link `endpoints-that-require-an-account-specific-token` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/authentication-with-oauth2.md` | whole document | https://developers.pismo.io/pismo-docs/docs/authentication-with-oauth2 | `f2d99ccb149ebbf0…` | 2026-07-15T20:21:36.000Z |
| `docs/get-started/authentication-with-openid.md` | whole document | https://developers.pismo.io/pismo-docs/docs/authentication-with-openid | `db8abce2b52fb695…` | 2026-08-04T15:36:51.000Z |
| `docs/get-started/basic-authentication-with-client-credentials.md` | whole document | https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials | `f8cba3ba9ed956e9…` | 2026-08-06T15:09:08.000Z |
| `docs/get-started/third-party-authentication-with-openid.md` | whole document | https://developers.pismo.io/pismo-docs/docs/third-party-authentication-with-openid | `49a927340cdbc916…` | 2026-07-16T15:03:19.000Z |
| `docs/control-center/access-keys-for-basic-authentication.md` | whole document | https://developers.pismo.io/pismo-docs/docs/access-keys-for-basic-authentication | `161f106285ce0ef7…` | 2026-08-05T11:14:10.000Z |

## Related knowledge units

- `KU-API-platform-authentication--authentication` — API reference: Platform authentication — Authentication
- `KU-AUTH-control-center-security` — Control Center security guide
- `KU-CC-dual-approval` — Dual approval
- `KU-EVT-verifying-webhook-requests` — Verifying webhook requests
