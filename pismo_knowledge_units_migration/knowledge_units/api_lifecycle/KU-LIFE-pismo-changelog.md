---
ku_id: KU-LIFE-pismo-changelog
title: Pismo changelog
category: api_lifecycle
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/resources/pismo-changelog.md
  sha256: a120ba82ec16014d99f732fa232cb9fa526fa03a62874dc22b44f1e2c4f4738e
  url: https://developers.pismo.io/pismo-docs/docs/pismo-changelog
  role: primary_guide
  updated_at: '2026-06-29T19:47:05.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# Pismo changelog

**KU ID:** `KU-LIFE-pismo-changelog` · **Category:** API lifecycle · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/resources/pismo-changelog.md`:

> The [Pismo changelog](https://developers.pismo.io/pismo-docs/changelog) describes changes to the Pismo platform that might affect your implementation, including new features, changes to existing features, and fixed issues. Changelog posts are published monthly and include all changes that have gone live within that interval.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/resources/pismo-changelog.md`: Pismo changelog; Subscribe to the changelog RSS feed

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/resources/pismo-changelog.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pismo-changelog · updatedAt: 2026-06-29T19:47:05.000Z

<!-- source:begin path=docs/resources/pismo-changelog.md part=0-end -->

# Pismo changelog

The [Pismo changelog](https://developers.pismo.io/pismo-docs/changelog) describes changes to the Pismo platform that might affect your implementation, including new features, changes to existing features, and fixed issues. Changelog posts are published monthly and include all changes that have gone live within that interval.

Every changelog post begins with a set of **Tags**. These are keywords that indicate the topics covered by the changes.

The rest of the post consists of the following sections:

* **Highlights**—A list of changes that deliver value to customers
* **Updates and fixes**—A list of smaller changes or bug fixes

Each section contains one or more entries, which consist of the following:

* **Title**—Brief description of the feature that has changed
* **Description of the change**—Details about the change, including links to any relevant documentation

### Subscribe to the changelog RSS feed

You can use any RSS feed reader to subscribe to the changelog. For example, to subscribe from Microsoft Outlook, follow these steps.

1. Right-click the **RSS Feeds** folder and select **Add a New RSS Feed**. A new RSS Feed dialog box appears.
2. Enter the URL of the Pismo changelog RSS feed. This is the URL of the changelog with `.rss` appended to the end:\
   `<https://developers.pismo.io/pismo-docs/changelog.rss`>
3. Select **Add** > **OK**.

Gmail does not have a similar option for adding an RSS feed. However, Google provides an extension to its Chrome web browser that you can use to link up with the RSS feed tool of your choice. Follow these steps.

1. In Google Chrome, navigate to <Anchor label="RSS Subscription Extension (by Google)" target="_blank" href="https://chrome.google.com/webstore/detail/rss-subscription-extensio/nlbjncdgjeocebhnmkbbbdekmmmcbfjd">RSS Subscription Extension (by Google)</Anchor>, and follow the instructions to install the extension.
2. After installation, enter `https://developers.pismolabs.io/pismo-docs/changelog.rss` in the Chrome address bar and press **ENTER**. The browser recognizes the URL as an RSS feed and prompts you to select an RSS feed tool.
3. Follow any instructions provided by the feed reader.

<HTMLBlock>
  {`
  <div style="margin-top:-10px"></div>
  `}
</HTMLBlock>

<br />
<!-- source:end -->

## Lifecycle status

- `docs/resources/pismo-changelog.md`: updatedAt 2026-06-29T19:47:05.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/resources/pismo-changelog.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pismo-changelog | `a120ba82ec16014d…` | 2026-06-29T19:47:05.000Z |

## Related knowledge units

- None.
