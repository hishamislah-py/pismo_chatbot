---
ku_id: KU-SUP-rate-limiting
title: Rate limiting on the Pismo platform
category: rate_limits_and_support
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/api-get-started/rate-limiting.md
  sha256: 799c1a6c3ff5a79a79e0f17b1470a6e9ff58124c5f15359c984b436238d5ecff
  url: https://developers.pismo.io/pismo-docs/reference/rate-limiting
  role: primary_guide
  updated_at: '2026-06-23T16:24:28.000Z'
operations: []
related_kus:
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Rate limiting on the Pismo platform

**KU ID:** `KU-SUP-rate-limiting` · **Category:** Rate limits and support · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/api-get-started/rate-limiting.md`:

> The Pismo platform uses **rate limiting** to maintain stable performance and prevent service degradation during peak usage. Rate limiting sets the maximum number of simultaneous requests allowed through an API. If requests exceed the limit, the platform returns error HTTP `429` (Too Many Requests), as defined in <Anchor label="RFC 6585, Section 4" target="_blank" href="https://datatracker.ietf.org/doc/html/rfc6585#section-4">RFC 6585, Section 4</Anchor>.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/api-get-started/rate-limiting.md`: Rate limiting on the Pismo platform; Preparing for high volume; Best practices

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/api-get-started/rate-limiting.md`

Source URL: https://developers.pismo.io/pismo-docs/reference/rate-limiting · updatedAt: 2026-06-23T16:24:28.000Z

<!-- source:begin path=docs/api-get-started/rate-limiting.md part=0-end -->

# Rate limiting on the Pismo platform

The Pismo platform uses **rate limiting** to maintain stable performance and prevent service degradation during peak usage. Rate limiting sets the maximum number of simultaneous requests allowed through an API. If requests exceed the limit, the platform returns error HTTP `429` (Too Many Requests), as defined in <Anchor label="RFC 6585, Section 4" target="_blank" href="https://datatracker.ietf.org/doc/html/rfc6585#section-4">RFC 6585, Section 4</Anchor>.

<Callout icon="📘" theme="info">
  Pismo adds rate limits to APIs once we identify performance needs.
</Callout>

# Preparing for high volume

If you expect to process a high volume of simultaneous requests, work with Pismo to define the best approach. Create a [ Pismo service desk](https://developers.pismo.io/pismo-docs/docs/service-desk) ticket to get the conversation started.

# Best practices

To keep from experiencing the rate limit error, follow these best practices:

* Prohibit load testing in the production environment is prohibited.
* Create a retry mechanism with an exponential backoff for when an error code is encountered. This involves creating a series of retry statements that send a decreasing amount of requests, spaced out in exponentially growing increments. For example, you can send a retry request after 2 minutes, then after 4 minutes, then after 8 minutes, and so on. Once you have determined an appropriate retry interval, follow this pattern until all requests are handled successfully.
<!-- source:end -->

## Lifecycle status

- `docs/api-get-started/rate-limiting.md`: updatedAt 2026-06-23T16:24:28.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/api-get-started/rate-limiting.md` | whole document | https://developers.pismo.io/pismo-docs/reference/rate-limiting | `799c1a6c3ff5a79a…` | 2026-06-23T16:24:28.000Z |

## Related knowledge units

- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
