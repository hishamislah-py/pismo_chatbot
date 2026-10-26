---
ku_id: KU-GS-environments
title: Environments
category: getting_started
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/environments.md
  sha256: 68baaf5dcd357bd6c0bacd7ba1c374dd5447f37acd73a1f6d21c1f3b5f67753c
  url: https://developers.pismo.io/pismo-docs/docs/environments
  role: primary_guide
  updated_at: '2026-06-25T22:03:52.000Z'
operations: []
related_kus:
- KU-AUTH-security-programme
- KU-GS-pismo-platform-onboarding
grouping_rationale: single source page
---

# Environments

**KU ID:** `KU-GS-environments` · **Category:** Getting started · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/get-started/environments.md`:

> The Pismo platform provides separate environments for testing and production.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/environments.md`: Environments; Endpoint structure; Components of a Pismo environment; PCI endpoints vs. non-PCI endpoints; Hostnames; Hostnames for the test environment; Hostnames for the production environment

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/environments.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/environments · updatedAt: 2026-06-25T22:03:52.000Z

<!-- source:begin path=docs/get-started/environments.md part=0-end -->

# Environments

The Pismo platform provides separate environments for testing and production.

* **Test environment**—A non‑production environment used to test new and updated features.

* **Production environment**—A live environment used to process actual customer data.

Your support team sets up access to these environments when you onboard. For more information, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

The endpoint you use determines the environment to which your call is routed, so each type of request has multiple endpoints associated with it, depending on the target environment. For example, if you send a request to the test environment, you'll need to use a different endpoint to send the same request to production.

<Callout icon="📘" theme="info">
  For information about authentication, see [Security](https://developers.pismo.io/pismo-docs/docs/security).
</Callout>

# Endpoint structure

An **endpoint** is a URL that you can use to send a request to the Pismo platform. An endpoint has the following syntax.

```
protocol:hostname/[prefix]/API version/path
```

Here's a sample endpoint that directs a request to Pismo's test environment:

```
https://sandbox.pismolabs.io/accounts/v1/accounts/10/balances/
```

The following table explains the different components in the sample endpoint.

| Name        | Component            | Details                                                                                                       |
| :---------- | :------------------- | :------------------------------------------------------------------------------------------------------------ |
| protocol    | https\://            | Always `https://`. This means the connection is encrypted and your data is safe.                              |
| hostname    | sandbox.pismolabs.io | Server name that identifies the environment.                                                                  |
| prefix      | accounts             | Name of the service you are accessing.                                                                        |
| API version | v1                   | Version of the API the endpoint uses. Used to avoid breaking changes to existing paths.                       |
| path        | accounts/10/balances | Path of the endpoint that specifies the method called by the endpoint. This follows REST API design standard. |

# Components of a Pismo environment

Every Pismo environment consists of the same components. Understanding a few core concepts will help you identify issues across environments.

## PCI endpoints vs. non-PCI endpoints

<a name="pci" />PCI (Payment Card Industry) certification requires extra security measures for endpoints that pass or return sensitive data, such as PAN and CVV. The following services use PCI endpoints (in both the test and production environments):

* `/cardsonfile/`
* `/cards-tokenization/`
* `/embossing/`
* `/payment-methods/`
* `/payment-methods-configs/`
* `/pcicards/`
* `/transactionsgateway/`

## Hostnames

A hostname is the entry point for an environment. Each environment has two servers:

* **Non-PCI**—Server that handles most API calls.

* **PCI**—Server than handles calls to <a href="#pci-endpoints-vs-non-pci-endpoints">PCI-related endpoints</a>.

### Hostnames for the test environment

Use the following servers in the test environment:

| Type of endpoint | Hostname             |
| :--------------- | :------------------- |
| Non-PCI          | sandbox.pismolabs.io |
| PCI              | gw-pci.pismolabs.io  |

### Hostnames for the production environment

In production, Pismo provides hostnames that are based on the specifics of your implementation. Ask your Pismo representative about the hostnames to use in production.

<Callout icon="🚧" theme="warn">
  In the test environment, some endpoints might work with either hostname. However, in production, you must use the appropriate hostname.
</Callout>
<!-- source:end -->

## Lifecycle status

- `docs/get-started/environments.md`: updatedAt 2026-06-25T22:03:52.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/environments.md` | whole document | https://developers.pismo.io/pismo-docs/docs/environments | `68baaf5dcd357bd6…` | 2026-06-25T22:03:52.000Z |

## Related knowledge units

- `KU-AUTH-security-programme` — Security programme: compliance, certifications, audits and incident response
- `KU-GS-pismo-platform-onboarding` — Onboarding for new customers
