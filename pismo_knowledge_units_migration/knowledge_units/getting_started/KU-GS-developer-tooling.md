---
ku_id: KU-GS-developer-tooling
title: 'Developer tooling: OpenAPI files, Postman collections and API testing'
category: getting_started
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/resources/access-pismo-openapi-files-on-github.md
  sha256: 25210cb68ac43293a2c54326f49ed62c794ca90dfc4311d025d25deb178466b5
  url: https://developers.pismo.io/pismo-docs/docs/access-pismo-openapi-files-on-github
  role: primary_guide
  updated_at: '2026-08-11T22:34:13.000Z'
- path: api-specs/README.md
  sha256: 5d9f9130a839624352bf28d7f65336237466831b4c189933949b65bda73321eb
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: spec_repository_readme
  updated_at: '2026-10-13T20:51:51+00:00'
- path: docs/resources/access-pismo-postman-collections.md
  sha256: 80e2887c5f367342306336528631f28619603546b69fffa77c264486ddeb6e0e
  url: https://developers.pismo.io/pismo-docs/docs/access-pismo-postman-collections
  role: primary_guide
  updated_at: '2026-08-05T17:19:27.000Z'
- path: docs/resources/pismo-api-testing-overview.md
  sha256: ed864ea6d4a4e731ad6857936d919586ffb45c1694bd50923d5b88c39e0f5e84
  url: https://developers.pismo.io/pismo-docs/docs/pismo-api-testing-overview
  role: primary_guide
  updated_at: '2026-08-05T17:26:03.000Z'
operations: []
related_kus:
- KU-AUTH-authentication-methods
- KU-CC-get-started-control-center
- KU-GS-get-started-with-pismo-apis
- KU-GS-program-types
- KU-GS-setup-overview
- KU-GS-welcome
- KU-SUP-service-desk-requests
grouping_rationale: All four describe how developers obtain and exercise the API definitions.
---

# Developer tooling: OpenAPI files, Postman collections and API testing

**KU ID:** `KU-GS-developer-tooling` · **Category:** Getting started · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 4 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: All four describe how developers obtain and exercise the API definitions.

Scope as stated in `docs/resources/access-pismo-openapi-files-on-github.md`:

> To access the source files for the API references available here on the Pismo Developers Portal, you can download them from the public Pismo GitHub repo. Once you have these files, you can generate SDKs or client libraries, create Postman collections, automated tests, or integration workflows.

Scope as stated in `api-specs/README.md`:

> This repository contains OpenAPI 3.1 specifications for the Pismo APIs. With these OpenAPI files, you can generate SDKs, code examples, test cases, and reference documentation.

Scope as stated in `docs/resources/access-pismo-postman-collections.md`:

> Use the Pismo Developers Postman page to find collections and workspaces to test Pismo APIs. The <Anchor label="Pismo workspace" target="_blank" href="https://www.postman.com/pismo-io/workspace/pismo-apis/overview">Pismo workspace</Anchor> has these collections:

Scope as stated in `docs/resources/pismo-api-testing-overview.md`:

> You have multiple options for testing Pismo APIs:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/resources/access-pismo-openapi-files-on-github.md`: Access Pismo OpenAPI files on GitHub; Get Pismo OpenAPI files; Next steps
- `api-specs/README.md`: Pismo API Specifications; 💻 Documentation; 💬 Get Support; ✅ Contributing
- `docs/resources/access-pismo-postman-collections.md`: Access Pismo Postman collections; Prerequisites; Fork Pismo Postman collections; Next steps
- `docs/resources/pismo-api-testing-overview.md`: Pismo API testing overview; Prerequisites; OpenAPI specifications; Postman collections; Related topics

## Prerequisites and dependencies

- Prerequisites are described in `docs/resources/access-pismo-postman-collections.md` section "Prerequisites".
- Prerequisites are described in `docs/resources/pismo-api-testing-overview.md` section "Prerequisites".

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/resources/access-pismo-openapi-files-on-github.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/access-pismo-openapi-files-on-github · updatedAt: 2026-08-11T22:34:13.000Z

<!-- source:begin path=docs/resources/access-pismo-openapi-files-on-github.md part=0-end -->

# Access Pismo OpenAPI files on GitHub

To access the source files for the API references available here on the Pismo Developers Portal, you can download them from the public Pismo GitHub repo. Once you have these files, you can generate SDKs or client libraries, create Postman collections, automated tests, or integration workflows.

You can use the Git commit history to review all changes to the OpenAPI specifications over time. For a curated list of changes published each month, review the [Pismo changelog](https://developers.pismo.io/pismo-docs/changelog).

## Get Pismo OpenAPI files

The repository for the Pismo OpenAPI files is at [github.com/PismoDevEx/pismo-api-specs](https://github.com/PismoDevEx/pismo-api-specs). You can clone or download the files, then open the `pismo-api-specs/published-apis` folder to view all OpenAPI files in YAML format.

The naming convention for the files follows the organization of the table of contents in the APIs section of the Developers Portal. For example, you find the endpoints in the **Platform setup - Programs** section in the file, `published-apis/Platform_setup_-_Programs.yaml`.

## Next steps

Many use cases exist with access to the OpenAPI YAML source files. You can:

* Generate SDKs and client libraries with your preferred OpenAPI tools.
* Create automated tests, mocks, and API collections for Postman (or another preferred API client).
* Build integration workflows that use OpenAPI specifications as contracts.
* Detect line-by-line changes to the OpenAPI files by viewing the Git commit history.
<!-- source:end -->

### Source 2: `api-specs/README.md`

Source URL: https://github.com/PismoDevEx/pismo-api-specs · updatedAt: 2026-10-13T20:51:51+00:00

<!-- source:begin path=api-specs/README.md part=0-end -->
# Pismo API Specifications

This repository contains OpenAPI 3.1 specifications for the Pismo APIs. With these OpenAPI files, you can generate SDKs, code examples, test cases, and reference documentation.

Pismo generates the public API reference documentation at  
https://developers.pismo.io/ using these files.

## 💻 Documentation

- **[Guides](https://developers.pismo.io/pismo-docs/docs/welcome)**  
  How to issue cards, set up core payments systems, settlement, and more.

- **[API Reference](https://developers.pismo.io/pismo-docs/reference/)**  
  Contains all reference information generated from these OpenAPI files.

- **[Events Reference](https://developers.pismo.io/events/docs/event-base-main-event)**  
  Descriptions of the JSON schema that provide platform processing actions from the Pismo platform.

- **[Changelog](https://developers.pismo.io/pismo-docs/changelog)**  
  Changes to the Pismo platform that might affect your implementation.

## 💬 Get Support

Pismo does not provide support for use cases with these files.

If you have a question, you can open a ticket in the  
**[Pismo Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk)**.

We welcome your input and feedback.

## ✅ Contributing

Since these files are automatically generated from internal sources, **we do not accept pull requests** on this repository.

If you want to report an issue, please submit a  
**[Pismo Service Desk ticket](https://developers.pismo.io/pismo-docs/docs/service-desk)**.
<!-- source:end -->

### Source 3: `docs/resources/access-pismo-postman-collections.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/access-pismo-postman-collections · updatedAt: 2026-08-05T17:19:27.000Z

<!-- source:begin path=docs/resources/access-pismo-postman-collections.md part=0-end -->

# Access Pismo Postman collections

Use the Pismo Developers Postman page to find collections and workspaces to test Pismo APIs. The <Anchor label="Pismo workspace" target="_blank" href="https://www.postman.com/pismo-io/workspace/pismo-apis/overview">Pismo workspace</Anchor> has these collections:

* All Pismo API collection
* Pismo card collection

## Prerequisites

* Work with your Pismo representative to set up your organization. You can use [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) to do a lot of this setup through a convenient UI.
* Ensure you have some basic data in your organization such as a [program](https://developers.pismo.io/pismo-docs/docs/program-types) configured that enables due dates. Refer to [Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview) for more information and to get started.
* Ensure you have [generated access keys using Control Center](https://developers.pismo.io/pismo-docs/docs/access-keys-for-basic-authentication) and saved both the server key and server secret in a safe place for authentication.
* **Make sure** you have the Pismo sandbox environment as the current environment and have updated the environment variables as needed.
* You must use a credit program to use the Pismo card collection. Some endpoints only work with programs that allow those configurations. For example, if the program does not allow cash-in transfers, the "Make a Cash-In transfer" request in this collection does not work with that program ID. Also, note that debit card programs do not require due dates, so `DEBITO` type programs do not work with this Pismo card collection.

## Fork Pismo Postman collections

The recommended way to work with a collection and environment is to fork them. This is similar to forking in GitHub. Forking enables you to pull in Pismo’s changes to the collection and environment over time.

<Callout icon="🚧" theme="warn">
  IMPORTANT: To keep your credentials, tokens, and sensitive data private, always fork into a **private** workspace.
</Callout>

1. Use the **Run in Postman** links in the table to access and fork the Pismo Postman collections in the <Anchor label="Pismo workspace" target="_blank" href="https://www.postman.com/pismo-io/workspace/pismo-apis/overview">Pismo workspace</Anchor>.

   When creating your fork, select the **Watch original collection** box to enable Postman to send you emails when Pismo updates the collection so you can pull the changes into your fork and always stay up to date with the latest version of the collections. The following table contains links to fork a collection into a sandbox environment which is used for all collections.

| Collection Name            | Fork link                                                                                                                                                                                                                       |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| All public Pismo endpoints | <PostmanRunButton collectionId="32342766-14c54b8c-2d9f-4295-8bbe-61dac8c9826c" collectionUrl="entityId=32342766-14c54b8c-2d9f-4295-8bbe-61dac8c9826c&entityType=collection&workspaceId=66cb9eed-4611-4e2e-8f42-4892a22af329" /> |
| Pismo cards collection     | <PostmanRunButton collectionId="32342766-8a069f00-2275-458e-99e5-e626ae6639d9" collectionUrl="entityId=32342766-8a069f00-2275-458e-99e5-e626ae6639d9&entityType=collection&workspaceId=66cb9eed-4611-4e2e-8f42-4892a22af329" /> |

2. Set up your environment variables in Postman. You must update the variables for your Pismo key and authenticate before any calls will work. All endpoints can use a variable for the URL.

When using OpenID authentication, update the `pismo.group` variable in the sandbox environment based on the endpoints you are testing. For more information on how to authenticate with OpenID, refer to [Authenticate with OpenID](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid).

<Image align="center" alt="Postman variables in sandbox environment" border={true} src="https://files.readme.io/6835069-image.png" className="border" />

## Next steps

With access to Postman collections, you have multiple options for trying API endpoints with a few different use cases:

* Mock up test data with real requests and responses using sandbox infrastructure.
* Create end-to-end workflow recipes to demonstrate and understand using multiple endpoints for a complete workflow.
* Build integration tests with Postman collections.
<!-- source:end -->

### Source 4: `docs/resources/pismo-api-testing-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pismo-api-testing-overview · updatedAt: 2026-08-05T17:26:03.000Z

<!-- source:begin path=docs/resources/pismo-api-testing-overview.md part=0-end -->

# Pismo API testing overview 

You have multiple options for testing Pismo APIs:

* **OpenAPI specifications**, from a public GitHub repo
* **Postman collections**, using the Postman software application for building, using, and managing APIs
* **Pismo Developers Portal** using the [interactive console](https://developers.pismo.io/pismo-docs/docs/get-started-with-pismo-apis#interactive-console)
* **curl** a command-line tool

Pismo updates the Pismo OpenAPI specifications and Postman collections through the same automated publication pipeline. Although we offer these files without Pismo support, if you find a problem with the files, you can open a [Pismo Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk) ticket.

## Prerequisites

You must have access to a sandbox account which includes `server_key` and `server_secret` values so that you can authenticate when using the sandbox with the interactive console, Postman collections, or using tools with OpenAPI files.

## OpenAPI specifications

You can download all OpenAPI files available on the Pismo Developers Portal by going to the GitHub repository at <Anchor label="github.com/PismoDevEx/pismo-api-specs" target="_blank" href="https://github.com/PismoDevEx/pismo-api-specs">github.com/PismoDevEx/pismo-api-specs</Anchor>.

This public repository contains the latest OpenAPI 3.1 specifications for Pismo APIs. Within minutes of publication, the updated OpenAPI file for every platform service appears. Because of this secure controlled pipeline, you cannot create outside commits or pull requests for this repository. We must ensure the published specifications remain synchronized with the authoritative source here in the Developers Portal.

## Postman collections

To help you with testing, Pismo provides Postman **collections** and an **environment**. A collection is a set of API requests that you can share with others. Postman also enables you to create an environment for use with a collection. When you load a collection in Postman, you can read from and write to variables. For more information, refer to the <Anchor label="Postman documentation" target="_blank" href="https://learning.postman.com/docs/getting-started/overview/">Postman documentation</Anchor>.

You can use the official Pismo Postman collections and environment to test the Pismo REST APIs without having to manually create the collections or environment. While you can test all these APIs through the Developers Portal, Postman provides a way for you to customize and streamline your testing environment. Pismo has created a public workspace with shared collections and an environment on the Postman Public API network.

The <Anchor label="Pismo Postman workspace" target="_blank" href="https://www.postman.com/pismo-io/pismo-apis/overview">Pismo Postman workspace</Anchor> has these collections:

* **All public Pismo endpoints**: This collection includes all the Pismo public APIs in a single collection.
* **Pismo cards collection**: This collection shows you the basic calls used in creating an account and a credit card.

### Related topics

[Access Pismo OpenAPI files on GitHub](https://developers.pismo.io/pismo-docs/docs/access-pismo-openapi-files-on-github)

[Access Pismo Postman collections](https://developers.pismo.io/pismo-docs/docs/access-pismo-postman-collections)
<!-- source:end -->

## Lifecycle status

- `docs/resources/access-pismo-openapi-files-on-github.md`: updatedAt 2026-08-11T22:34:13.000Z.
- `api-specs/README.md`: updatedAt 2026-10-13T20:51:51+00:00.
- `docs/resources/access-pismo-postman-collections.md`: updatedAt 2026-08-05T17:19:27.000Z.
- `docs/resources/pismo-api-testing-overview.md`: updatedAt 2026-08-05T17:26:03.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/resources/access-pismo-openapi-files-on-github.md` | whole document | https://developers.pismo.io/pismo-docs/docs/access-pismo-openapi-files-on-github | `25210cb68ac43293…` | 2026-08-11T22:34:13.000Z |
| `api-specs/README.md` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `5d9f9130a8396243…` | 2026-10-13T20:51:51+00:00 |
| `docs/resources/access-pismo-postman-collections.md` | whole document | https://developers.pismo.io/pismo-docs/docs/access-pismo-postman-collections | `80e2887c5f367342…` | 2026-08-05T17:19:27.000Z |
| `docs/resources/pismo-api-testing-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pismo-api-testing-overview | `ed864ea6d4a4e731…` | 2026-08-05T17:26:03.000Z |

## Related knowledge units

- `KU-AUTH-authentication-methods` — API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
- `KU-GS-program-types` — Program types
- `KU-GS-setup-overview` — Core objects
- `KU-GS-welcome` — Get started with the Pismo Developers Portal
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
