---
ku_id: KU-LIFE-api-deprecation-strategy
title: API lifecycle and deprecation strategy
category: api_lifecycle
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/resources/api-deprecation-strategy.md
  sha256: af6040a412ba3a8d3653562474011bdc60d3bec9399df4b3a9067b9c767203b2
  url: https://developers.pismo.io/pismo-docs/docs/api-deprecation-strategy
  role: primary_guide
  updated_at: '2026-07-01T16:06:39.000Z'
operations: []
related_kus:
- KU-GS-environments
- KU-LIFE-api-endpoint-deprecation-and-removal-schedule
- KU-LIFE-pismo-changelog
grouping_rationale: single source page
---

# API lifecycle and deprecation strategy

**KU ID:** `KU-LIFE-api-deprecation-strategy` · **Category:** API lifecycle · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/resources/api-deprecation-strategy.md`:

> To keep you up to date with the latest versions of APIs, Pismo must occasionally deprecate and decommission older versions of APIs. When an endpoint or API is deprecated, Pismo strongly recommends updating to the newest versions before the decommission date. This allows for a smooth upgrade path to a newer release.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/resources/api-deprecation-strategy.md`: API lifecycle and deprecation strategy; Terms and concepts; API lifecycle; Communication schedule; API upgrades; Backward-compatible changes

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/resources/api-deprecation-strategy.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/api-deprecation-strategy · updatedAt: 2026-07-01T16:06:39.000Z

<!-- source:begin path=docs/resources/api-deprecation-strategy.md part=0-end -->

# API lifecycle and deprecation strategy

To keep you up to date with the latest versions of APIs, Pismo must occasionally deprecate and decommission older versions of APIs. When an endpoint or API is deprecated, Pismo strongly recommends updating to the newest versions before the decommission date. This allows for a smooth upgrade path to a newer release.

> 📘 Deprecation and removal schedule
>
> For a current list of deprecated endpoints scheduled to be decommissioned, refer to the [API endpoint deprecation and removal schedule](https://developers.pismo.io/pismo-docs/docs/api-endpoint-deprecation-and-removal-schedule).

# Terms and concepts

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Term
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        API and endpoint
      </td>

      <td>
        Each product on the Pismo platform has a speciﬁc API, providing many services, known as endpoints. A Pismo API provides at least one endpoint. Endpoints represent the services that can be executed by an API product.

        Every endpoint belongs to a speciﬁc API. For example:

        <ul>
          <li>Products: Accounts API, Cards API</li>
          <li>Endpoints: Get account status, Create a card</li>
        </ul>

        <br />
      </td>
    </tr>

    <tr>
      <td>
        Deprecation
      </td>

      <td>
        A service has been ended (with or without a replacement becoming available). Support for this service is limited to bug fixes only.
      </td>
    </tr>

    <tr>
      <td>
        Sunsetting
      </td>

      <td>
        Period of time from the deprecation date to decommissioning. The sunsetting period is usually six months. However, endpoints presenting vulnerability issues are decommissioned within three months.
      </td>
    </tr>

    <tr>
      <td>
        Decommissioned
      </td>

      <td>
        Older version is no longer available and is removed from the Developers Portal. Requests sent to this version fail beginning on the decommission date.
      </td>
    </tr>
  </tbody>
</Table>

# API lifecycle

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Version Status
      </th>

      <th>
        Description
      </th>

      <th>
        Documentation
      </th>

      <th>
        Support
      </th>

      <th>
        Notification
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Active
      </td>

      <td>
        Most up-to-date and recommended API version
      </td>

      <td>
        Available on launch date.
      </td>

      <td>
        Fully supported. Updated with bug fixes and new features.
      </td>

      <td>
        Notifications of new, active APIs are made in the Changelog of the month of release.

        If a new API is a replacement for a decommissioned API, it is announced in a Pismo bulletin at the time of deprecation.
      </td>
    </tr>

    <tr>
      <td>
        Deprecated
      </td>

      <td>
        API is scheduled for decommissioning and may or may not be superseded by a newer version.

        New customers or new integrations by existing customers are denied access to deprecated APIs.
      </td>

      <td>
        The version is marked as *Deprecated* on the day of deprecation.
      </td>

      <td>
        Supported for six months from the deprecation date (bug fixes only).
      </td>

      <td>
        Notification via Pismo bulletin,  published on the deprecation date (also known as the sunset date).
      </td>
    </tr>

    <tr>
      <td>
        Decommissioned
      </td>

      <td>
        API is no longer available. The version is decommissioned six months after in the deprecated status.
      </td>

      <td>
        No documentation provided.
      </td>

      <td>
        No support provided.
      </td>

      <td>
        Bulletin reminder notifications published 90, 60, 30, and 7 days prior to decommissioning.

        Notification of decommissioning is made in the Changelog of the month of release.
      </td>
    </tr>
  </tbody>
</Table>

# Communication schedule

| Schedule                                      | Communication method                                |
| :-------------------------------------------- | :-------------------------------------------------- |
| New active date                               | [Changelog](https://developers.pismo.io/pismo-docs/docs/pismo-changelog)                    |
| Deprecation date                              | Pismo Bulletin and [Changelog](https://developers.pismo.io/pismo-docs/docs/pismo-changelog) |
| 90, 60, 30, and 7 days before decommissioning | Pismo Bulletin reminders                            |
| Decommission date                             | [Changelog](https://developers.pismo.io/pismo-docs/docs/pismo-changelog)                    |

# API upgrades

The URL for an endpoint includes an element specifying the version of the API it uses. For example, in the URL `https://api-sandbox.pismolabs.io/events/v1/timeline`, the **v1** element indicates that it uses version 1 of the API for that endpoint. For more information about endpoint structure, see [Environments](https://developers.pismo.io/pismo-docs/docs/environments).

Your API version controls what parameters you can send in requests and which ones you receive in the responses. So, if you’re using an older version of an API, you should upgrade to the latest version to take advantage of new functionality or improved processing. To check if there are any new API versions available, review the Pismo Changelog and the latest version of the documentation.

> 📘 Outdated API versions
>
> In exceptional cases, Pismo may maintain an outdated API alongside a current one. In these cases, you should use the **latest version** for all new development. This helps to avoid rework when the outdated API eventually is deprecated.

# Backward-compatible changes

Backward compatible changes in your version are available automatically. These changes typically introduce new features or improve performance, but do not disrupt your current implementation. To use a newer version, you shouldn't have to do anything to keep things working correctly.

The following changes are backward compatible.

* Adding API resources
* Adding optional request parameters to existing API methods
* Adding properties to existing API responses
<!-- source:end -->

## Lifecycle status

- `docs/resources/api-deprecation-strategy.md`: updatedAt 2026-07-01T16:06:39.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/resources/api-deprecation-strategy.md` | whole document | https://developers.pismo.io/pismo-docs/docs/api-deprecation-strategy | `af6040a412ba3a8d…` | 2026-07-01T16:06:39.000Z |

## Related knowledge units

- `KU-GS-environments` — Environments
- `KU-LIFE-api-endpoint-deprecation-and-removal-schedule` — API endpoint deprecation and removal schedule
- `KU-LIFE-pismo-changelog` — Pismo changelog
