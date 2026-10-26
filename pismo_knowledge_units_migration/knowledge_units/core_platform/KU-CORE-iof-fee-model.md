---
ku_id: KU-CORE-iof-fee-model
title: IOF fee model for Brazil
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/iof-fee-model.md
  sha256: 95912950a84c4f65d3f74b088cbb612d8314561462e6820c77d2a416b46a6da5
  url: https://developers.pismo.io/pismo-docs/docs/iof-fee-model
  role: primary_guide
  updated_at: '2026-04-24T02:07:09.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# IOF fee model for Brazil

**KU ID:** `KU-CORE-iof-fee-model` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/iof-fee-model.md`:

> The Imposto sobre Overações Financeiras (IOF) tax in Brazil is a tax on financial transactions. It is a federal tax applied to a wide range of financial transactions involving individuals and businesses. It bears some similarity to the capital gains tax in the United States. Like the capital gains tax, it is regressive, meaning investments that are held for a longer period of time are taxed at a lower rate than those held for a shorter period of time.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/iof-fee-model.md`: IOF fee model for Brazil; IOF fee model example

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/iof-fee-model.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/iof-fee-model · updatedAt: 2026-04-24T02:07:09.000Z

<!-- source:begin path=docs/core-platform/iof-fee-model.md part=0-end -->

# IOF fee model for Brazil

The Imposto sobre Overações Financeiras (IOF) tax in Brazil is a tax on financial transactions. It is a federal tax applied to a wide range of financial transactions involving individuals and businesses. It bears some similarity to the capital gains tax in the United States. Like the capital gains tax, it is regressive, meaning investments that are held for a longer period of time are taxed at a lower rate than those held for a shorter period of time.

According to the provisions of Decree 6,306/2007, the IOF on securities applies in accordance with a regressive table that varies proportionally to the period of the investment, with such period limited to 30 days. In other words, the IOF on securities only applies to the redemption, cession, or refinancing of investments before the above mentioned period.

The following table details how investment gains are taxed over a 30-day period:

| Aging of the investment | Percentage to be applied |
| :---------------------- | :----------------------- |
| 1                       | 96 %                     |
| 2                       | 93 %                     |
| 3                       | 90 %                     |
| 4                       | 86 %                     |
| 5                       | 83 %                     |
| 6                       | 80 %                     |
| 7                       | 76 %                     |
| 8                       | 73 %                     |
| 9                       | 70 %                     |
| 10                      | 66 %                     |
| 11                      | 63 %                     |
| 12                      | 60 %                     |
| 13                      | 56 %                     |
| 14                      | 53 %                     |
| 15                      | 50 %                     |
| 16                      | 46 %                     |
| 17                      | 43 %                     |
| 18                      | 40 %                     |
| 19                      | 36 %                     |
| 20                      | 33 %                     |
| 21                      | 30 %                     |
| 22                      | 26 %                     |
| 23                      | 23 %                     |
| 24                      | 20 %                     |
| 25                      | 16 %                     |
| 26                      | 13 %                     |
| 27                      | 10 %                     |
| 28                      | 6 %                      |
| 29                      | 3 %                      |
| 30                      | 0 %                      |

# IOF fee model example

The following is an example of how this an IOF fee calculation method would be applied.

**Investment:** $1000
**Interest:** 1% per day

| Day (Aging) | Income  | IOF rate | IOF tax | Income after tax |
| :---------- | :------ | :------- | :------ | :--------------- |
| 1           | R10     | 96%      | R9,60   | R0,4             |
| 10          | R104.62 | 66%      | R69,05  | R35,57           |
| 30          | R250    | 0%       | R0      | R250             |
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/iof-fee-model.md`: updatedAt 2026-04-24T02:07:09.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/iof-fee-model.md` | whole document | https://developers.pismo.io/pismo-docs/docs/iof-fee-model | `95912950a84c4f65…` | 2026-04-24T02:07:09.000Z |

## Related knowledge units

- None.
