---
ku_id: KU-GS-ai-assisted-documentation
title: 'AI-assisted documentation: Ask AI and LLM access'
category: getting_started
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/get-started-with-ask-ai.md
  sha256: 5f253f63cc48f2f81201a5514f47535c1832a51f028474c81948603c11fd6e24
  url: https://developers.pismo.io/pismo-docs/docs/get-started-with-ask-ai
  role: primary_guide
  updated_at: '2026-07-07T11:05:46.000Z'
- path: docs/resources/use-llms-with-pismo-developers-portal.md
  sha256: c01d01eef8b9b340c67a15d730bd3f06aa2aa14d597684decdeeb17bc62ed0e7
  url: https://developers.pismo.io/pismo-docs/docs/use-llms-with-pismo-developers-portal
  role: primary_guide
  updated_at: '2026-08-03T18:39:57.000Z'
operations: []
related_kus: []
grouping_rationale: Both describe AI access to the documentation.
---

# AI-assisted documentation: Ask AI and LLM access

**KU ID:** `KU-GS-ai-assisted-documentation` · **Category:** Getting started · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Both describe AI access to the documentation.

Scope as stated in `docs/get-started/get-started-with-ask-ai.md`:

> Get answers to your questions and links to related content using Ask AI, the Pismo Developers Portal AI assistant.

Scope as stated in `docs/resources/use-llms-with-pismo-developers-portal.md`:

> The Pismo Developers Portal includes an llms.txt file to make it easier for large language models (LLMs) to parse and understand the documentation. The file provides a machine-friendly Markdown-based index of all documentation pages on the portal, and is kept in sync with site updates.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/get-started-with-ask-ai.md`: Get started with Ask AI; Data privacy; Feedback
- `docs/resources/use-llms-with-pismo-developers-portal.md`: Use LLMs with the Pismo Developers Portal; What is an llms.txt file?; Why Pismo provides an llms.txt file; Access documentation in Markdown

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/get-started-with-ask-ai.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-with-ask-ai · updatedAt: 2026-07-07T11:05:46.000Z

<!-- source:begin path=docs/get-started/get-started-with-ask-ai.md part=0-end -->

# Get started with Ask AI

Get answers to your questions and links to related content using Ask AI, the Pismo Developers Portal AI assistant.

<Image align="center" alt="screenshot showing the Ask AI sidebar chat window" border={true} src="https://files.readme.io/2de7f0b3d0706d786fb9aa749c4cf405bb8e84c350690e65f44a2ca3b2ae4922-ask-ai-sidebar.png" className="border" />

To start using Ask AI, do the following:

1. Select **Ask AI**.\
   The **Ask AI** sidebar opens with a prompt to start chatting.
2. Ask a question using natural language, and press **Enter**.\
   For example, enter "what are flex controls?" or "how do I get an authorization token?"\
   Ask AI searches the Developers Portal and generates an answer. You can ask follow-up questions for clarification.
3. When you're finished, you can do the following:
   * To delete the chat history, select the trash icon.
   * To close the sidebar, select the cross icon.

# Data privacy

Ask AI doesn't use your data to train public AI models and your search entries remain in the Developers Portal. Pismo reviews the questions periodically to improve the documentation.

# Feedback

Your feedback supports ongoing improvement at Pismo.

To give feedback on the Ask AI assistant, do either of the following:

* To mark an answer as helpful, select the thumbs-up icon.
* To mark an answer as unhelpful, select the thumbs-down icon.
<!-- source:end -->

### Source 2: `docs/resources/use-llms-with-pismo-developers-portal.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/use-llms-with-pismo-developers-portal · updatedAt: 2026-08-03T18:39:57.000Z

<!-- source:begin path=docs/resources/use-llms-with-pismo-developers-portal.md part=0-end -->

# Use LLMs with the Pismo Developers Portal

The Pismo Developers Portal includes an llms.txt file to make it easier for large language models (LLMs) to parse and understand the documentation. The file provides a machine-friendly Markdown-based index of all documentation pages on the portal, and is kept in sync with site updates.

# What is an llms.txt file?

An llms.txt file is an emerging AI convention designed to help LLMs understand a website's content, reducing the need for scraping HTML pages.

Instead of crawling the entire website, LLMs can parse a single file to understand the structure of the documentation and follow explicit links to source content in Markdown. This approach ensures LLMs are working with the most up-to-date first-party information.

To view the llms.txt file, do the following:

1. Go to the [Pismo Developers Portal](https://developers.pismo.io).
2. Scroll down to the page footer.
3. Select **<Anchor label="Read llms.txt" target="_blank" href="https://developers.pismo.io/llms.txt">Read llms.txt</Anchor>**.

<Image align="center" border={true} src="https://files.readme.io/98689c4a0ed766d60109d1066b03d8ae020d0f896908b0eefb73caaf7936d430-read-llms-txt.png" className="border" />

# Why Pismo provides an llms.txt file

The llms.txt file is designed to make Pismo's developer documentation more accessible and usable for LLM-based tools by:

* **Reducing the need for web scraping**—Websites contain complex HTML structures and boilerplate content, and without an explicit index, LLMs waste tokens parsing irrelevant HTML markup. The llms.txt file provides a singular, structured entry point to the portal.
* **Providing an authoritative content index**—The llms.txt file lists every documentation page published on the portal, as well as the most-recent changelog entries. This ensures LLMs work from the same single authoritative source as human users.
* **Helping LLMs understand the site structure**—The portal is designed for for human users, not LLMs. Navigation menus, breadcrumbs, and UI-driven grouping aren't always reliable signals for automated tools. The llms.txt file makes the structure explicit by clearly specifying the grouping of documentation pages, based on guides, APIs, events, and the changelog.
* **Improving accuracy**—The platform automatically updates the llms.txt file any time Pismo makes a change to the documentation. This means LLMs don't have to rely on old or cached data, reducing the risk of AI hallucinations.

# Access documentation in Markdown

The llms.txt file provides direct access to a Markdown version of every documentation page on the portal. Because the content is formatted in Markdown, it preserves the same information as HTML, but without any layout or styling. This makes it easier for LLMs to parse the content accurately and for you to manually copy and paste page content into LLM tools.

Markdown-formatted content offers the following advantages:

* Clear page and content structure defined with Markdown notation, reducing ambiguity in the page layout
* Improved token efficiency, allowing LLMs to process more meaningful information within the same context window
* Reduced risk of extracting incomplete content, as the content doesn't rely on client-side rendering or custom JavaScript functions to expose page sections
<!-- source:end -->

## Lifecycle status

- `docs/get-started/get-started-with-ask-ai.md`: updatedAt 2026-07-07T11:05:46.000Z.
- `docs/resources/use-llms-with-pismo-developers-portal.md`: updatedAt 2026-08-03T18:39:57.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/get-started-with-ask-ai.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-with-ask-ai | `5f253f63cc48f2f8…` | 2026-07-07T11:05:46.000Z |
| `docs/resources/use-llms-with-pismo-developers-portal.md` | whole document | https://developers.pismo.io/pismo-docs/docs/use-llms-with-pismo-developers-portal | `c01d01eef8b9b340…` | 2026-08-03T18:39:57.000Z |

## Related knowledge units

- None.
