---
ku_id: KU-CARD-run-the-configuration-requests
title: Run the configuration requests
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/run-the-configuration-requests.md
  sha256: eec8b8fae534784c8fa9e32e945b85fc69a04845c5fbaffb53eeac7e59cd54f4
  url: https://developers.pismo.io/pismo-docs/docs/run-the-configuration-requests
  role: primary_guide
  updated_at: '2026-05-04T15:17:33.000Z'
operations:
- post-authorization-config-by-tenant
related_kus:
- KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01
grouping_rationale: single source page
---

# Run the configuration requests

**KU ID:** `KU-CARD-run-the-configuration-requests` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/run-the-configuration-requests.md`:

> You can create your configurations in the sandbox environment with the endpoints defined in the [Authorization configurations](https://developers.pismo.io/pismo-docs/reference/post-authorization-config-by-tenant) API reference. The following code samples show how to run the basic configuration create (POST), read (GET), update (PUT), and delete requests.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/run-the-configuration-requests.md`: Run the configuration requests; Run the configuration create (POST) request; Run the configuration read (GET) request; Run the configuration update (PUT) request; Run the configuration DELETE request; Examples; Example to override BIN validations; Example to update an existing configuration

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/run-the-configuration-requests.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/run-the-configuration-requests · updatedAt: 2026-05-04T15:17:33.000Z

<!-- source:begin path=docs/card-issuing/run-the-configuration-requests.md part=0-end -->

# Run the configuration requests

You can create your configurations in the sandbox environment with the endpoints defined in the [Authorization configurations](https://developers.pismo.io/pismo-docs/reference/post-authorization-config-by-tenant) API reference. The following code samples show how to run the basic configuration create (POST), read (GET), update (PUT), and delete requests.

## Run the configuration create (POST) request

To create an org configuration, send the request without the `programId` and `accountId`:

```
curl --request POST \              
  --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config' \
  --header 'Content-Type: application/json' \
  --header 'x-tenant: <Org ID>' \
  --data '{
    // Put your configurations here
}
'
```

<Callout icon="📘" theme="info">
  If you have both Full balance and Zero balance programs within your org, it is recommended to create your configurations at the program level rather than the org level. This is because for Zero balance programs, the `zero_balance_url` field is mandatory and configuring it for Full balance programs causes inconsistency in behavior.
</Callout>

To create a program configuration, send the request with the `programId`:

```
curl --request POST \              
  --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config/program/{programId}' \
  --header 'Content-Type: application/json' \
  --header 'x-tenant: <Org ID>' \
  --data '{
    // Put your configurations here
}
'
```

To create an account configuration, send the request with the `accountId`:

```
curl --request POST \              
  --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config/account/{accountId}' \
  --header 'Content-Type: application/json' \
  --header 'x-tenant: <Org ID>' \
  --data '{
    // Put your configurations here
}
'
```

## Run the configuration read (GET) request

To get the org-level configuration:

```
curl --request GET \
     --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config' \
     --header 'accept: application/json'
     --header 'x-tenant: <Org ID>' 
```

To get the program-level configuration:

```
curl --request GET \
     --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config/program/{programId}' \
     --header 'accept: application/json'
     --header 'x-tenant: <Org ID>'
```

To get the account-level configuration:

```
curl --request GET \
     --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config/account/{accountId}' \
     --header 'accept: application/json'
     --header 'x-tenant: <Org ID>' 
```

## Run the configuration update (PUT) request

To update a configuration, follow these steps:

1. Run the GET request for the desired level configuration.
2. Copy the configuration parameters.
3. Paste the existing parameters into the request body.
4. Add or update the configuration.
5. Run the request to update the desired level configuration.

<Callout icon="📘" theme="info">
  You must follow these five steps to ensure the configuration is replicated in the updated record, since a new record is created during the update for history purposes.
</Callout>

To update the org-level configuration, send the request without the `programId` and `accountId`:

```
curl --request PUT \
     --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'x-tenant: <Org ID>' \
     --data '
{
  "disable_dcc": true, //existing parameter
  "use_rates_fee_models": true //new parameter
}
'
```

To update the program-level configuration, send the request with the `programId`:

```
curl --request PUT \
     --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config/program/{programId}' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'x-tenant: <Org ID>' \
     --data '
{
  "disable_dcc": true, //existing parameter
  "use_rates_fee_models": true //new parameter
}
'
```

To update the account-level configuration, send the request with the `accountId`:

```
curl --request PUT \
     --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config/account/{accountId}' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'x-tenant: <Org ID>' \
     --data '
{
  "disble_dcc": true, //existing parameter
  "use_rates_fee_models": true //new parameter
}
'
```

## Run the configuration DELETE request

To delete the org-level configuration:

```
curl --request DELETE \
     --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config' \
     --header 'accept: application/json'
     --header 'x-tenant: <Org ID>'
```

To delete the program-level configuration:

```
curl --request DELETE \
     --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config/program/{programId}' \
     --header 'accept: application/json'
     --header 'x-tenant: <Org ID>' 
```

To delete the account-level configuration:

```
curl --request DELETE \
     --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config/account/{accountId}' \
     --header 'accept: application/json'
     --header 'x-tenant: <Org ID>' 
```

# Examples

## Example to override BIN validations

The result of this example configuration is twofold within the organization. BIN 123456 has all authorizations denied. Authorizations within BIN 87654321 have card status validation ignored for a recurring transaction with card status CANCELED.

```
curl --request POST \              
  --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config' \
  --header 'Content-Type: application/json' \
  --header 'x-tenant: <Org ID>' \
  --data '{
    "override_bins": { 
      "123456":
      {
        "deny_all_authorizations":true
      },
      "87654321":
      {
        "bypass_card_status_canceled":true
      }
    }
}
'
```

## Example to update an existing configuration

At the end of this example configuration, the specified program starts using the Anti-fraud API and the Fee Models configured together with the Anti-fraud team.

1. First, get the configurations for the org/program/account you want to update. In this example, the configuration of a program is updated.

```
curl --request GET \
     --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config/program/{programId}' \
     --header 'accept: application/json'
     --header 'x-tenant: <Org ID>' 
```

2. Copy the GET result.

```
 {"disable_dcc":true}
```

3. Paste the GET result into the update request and add or update the desired parameters.

```
curl --request PUT \
     --url 'https://sandbox.pismolabs.io/network-transactions-config/v1/config/program/{programId}' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'x-tenant: <Org ID>' \
     --data '
{
  "disble_dcc": true, //put the existing parameter
  "use_rates_fee_models": true //add the new parameter
}
'
```

4. \[Optional] If you want to check the result of your configuration, perform a new GET. For this example, the result is this:

```
{"disable_dcc":true, "use_rates_fee_models": true}
```
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/config` | `post-authorization-config-by-tenant` | Create authorization configuration by organization | `api-specs/Card_issuing_-_Authorization_configurations.yaml` | no | KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01 |

### Operation essentials

- **`POST /v1/config`** (`post-authorization-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/card-issuing/run-the-configuration-requests.md`: updatedAt 2026-05-04T15:17:33.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/run-the-configuration-requests.md` | whole document | https://developers.pismo.io/pismo-docs/docs/run-the-configuration-requests | `eec8b8fae534784c…` | 2026-05-04T15:17:33.000Z |

## Related knowledge units

- `KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01` — API reference: Card issuing - Authorization configurations — Authorization configurations (part 1 of 2)
