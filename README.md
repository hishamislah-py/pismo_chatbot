# Pismo Client Implementation & Ramp-Up Assistant (UC-031)

This project builds a documentation-grounded assistant that helps client teams implement and ramp up on the Pismo platform. It holds three things:

- an offline snapshot of Pismo's public developer documentation and OpenAPI specifications;
- the structured tables derived from them;
- a curated knowledge-base (KB) corpus for the assistant, with the validation evidence behind each.

**Project root:** this folder (`Downloads\pismo_claude_code_handoff\`). Open it directly in VS Code and Claude Code. There is no inner project folder.

## Where things are

| Need | Location | Status |
| --- | --- | --- |
| Raw source data (426 Markdown pages, 71 OpenAPI YAML files) | `pismo_dataset_final_r2/raw/` (`markdown/`, `openapi/`) | **Authoritative** (r2) |
| Structured tables (operations, events, errors, examples) | `pismo_dataset_final_r2/structured/` | **Authoritative** (r2; identical to r1) |
| Dataset manifests, revision record, conflict register | `pismo_dataset_final_r2/metadata/`, `pismo_dataset_final_r2/registers/` | **Authoritative** (r2) |
| KB corpus for the assistant (503 files) | `pismo_kb_release_r2/kb_corpus/` | **Current release** (r2) |
| KB allowlist, source map, indexing policy, release notes | `pismo_kb_release_r2/internal/` | |
| Previous dataset and KB (r1: 538 files; 491-file corpus) | `pismo_dataset_final/`, `pismo_kb_release/` | **Superseded**; kept unchanged for rollback |
| Sign-off evidence | `pismo_signoff_results/` (also copied into `pismo_dataset_final/reports/signoff/`) | |
| Validation and audit reports | `pismo_validation/` | see below |
| Build history: inputs, intermediate datasets, run logs, prompts | `pismo_work/` | Provenance only |

### Current release: r2 (accepted 2026-10-19)

**What r2 adds:** r2 is r1 plus the 12 changelog posts from 2025 (title dates 3 January – 5 December 2025), backfilled from the Pismo changelog RSS feed. The changelog now runs from 3 January 2025 to 2 October 2026 (22 posts).

**How it was built:**
- **Posts:** byte-identical to the source; nothing was repaired or normalised.
- **Corpus:** every r1 corpus file is unchanged in r2.
- **Tools:** the unchanged, hash-pinned `build_kb_release.py` and `verify_kb_release.py`.

| Release | Path | Files | Fingerprint (P, path-inclusive) |
| --- | --- | --- | --- |
| Dataset r2 | `pismo_dataset_final_r2/` | 558 | `9c1cbd27cc1d1f9d183e0fb18042fd3fc19243eb192c608f119a7fa56201b49d` |
| KB r2 | `pismo_kb_release_r2/` | 516 | `ca455b2ef5404dfd39ef26d02cb90f2288f4a7a8bb40a36752f1001edbcf9a14` |
| KB r2 corpus | `pismo_kb_release_r2/kb_corpus/` | 503 | `7080b549e8160a2bc555ae1c0646b4d9a807414cd12dbd1943e712f5031f0e62` |
| Dataset r1 (superseded) | `pismo_dataset_final/` | 538 | `0db5fbb957010860c15378de1c68dbfda41ae25f4a47b74b3ccaead907c6f7cf` |
| KB r1 (superseded) | `pismo_kb_release/` | 504 | `4851fc17792047e8433a1ce12914370e4a2f8560a63ca5aa10457cb4aefe1933` |
| KB r1 corpus (superseded) | `pismo_kb_release/kb_corpus/` | 491 | `8211c8fd1813f20220b4160d3b8a5bc9a08484e1d1dc0dcec3baa1cb2857454b` |

**Provenance and caveats** are in `pismo_dataset_final_r2/metadata/PISMO_DATASET_MANIFEST.json`:
- `revisions[]`;
- the appended `processing_notes` and `known_limitations`;
- `metadata/changelog_backfill_20261019/`: the RSS pages, collection manifest, run log and robots.txt;
- register entry C5: an empty link in `7-february-2025.md`, kept as served;
- `reports/CHANGELOG_BACKFILL_PROMOTION.md`.

**Build records:**
- `pismo_kb_release_r2/internal/reports/RELEASE_NOTES_r2.md` and `verification_results.json`;
- the run logs `pismo_work/runs/promotion_run_dataset_20261019_081309/` and `promotion_run_kb_20261019_081526/`, plus the fingerprint checks in `promotion_checks_20261019_081307/` and `promotion_checks_kb_20261019_081524/`;
- plan and tests: `pismo_work/runs/promotion_plan_20261019_050359/`.

**Rollback:** point this README back to `pismo_dataset_final/` and `pismo_kb_release/`. Both are unchanged, and their recorded fingerprints remain valid.

### Validation and audit evidence (`pismo_validation/`)

- `PHASE_A_REPORT.md`: integrity and consistency audit of v2, the final dataset and the KB release.
- `phase_a_remediation/REMEDIATION_REPORT.md`: fixes to Phase A findings, built as *candidates*:
  - `corrected_dataset/` and `corrected_release_candidate/` are **not promoted** and are **not authoritative**;
  - `evidence/originals/` holds remediation evidence.
- `phase_b/PHASE_B_REPORT.md`: Markdown validation and the HTML-table conversion plan.
  - `converted_markdown/` holds the Phase B conversion output.
  - `b2_review_v2/` holds the parent-object review: 33 unresolved conflicts.
- `dataset_comparison/DATASET_COMPARISON_REPORT.md` (2026-10-16): KB coverage and readiness for a chatbot.

### What is in `pismo_work/` (do not use as the active dataset)

- `pismo_dataset/` and `pismo_dataset.zip`: the pre-download dataset (no Markdown) that v2 was built from.
- `pismo_dataset_v2/`: the assembled dataset. `pismo_dataset_final/` is v2 plus sign-off and finalisation.
- `pismo_download_stage/` and `pismo_inventory_stage/` (with `pismo_inventory_stage.zip`): the collection scripts.
- `pismo_changelog_stage/`: the 2025 changelog collector and the r2 promotion script.
- `runs/`: logs of the inventory, download, changelog backfill and r2 promotion runs.
- `provenance/prompts/`: the original download task prompt.

## Running the checks

Requires Python 3.11 and PyYAML. Run from this folder. The commands below were run successfully on 2026-10-16 after the folders were consolidated. The r2 fingerprints were added on 2026-10-19.

```powershell
# Fingerprint a folder (legacy method). Writes only the output file you name.
python -I pismo_signoff_results\fingerprint.py pismo_work\pismo_dataset_v2 $env:TEMP\v2_fp.txt
#   expected: 7573dc2f3e9804481617d10206f3d8f9edcb175f0b49c0b34cbf8e9668b18b99, 525 files

# Path-inclusive (P) fingerprints of the current (r2) and superseded (r1) trees. Writes only the output CSV.
python -I pismo_validation\phase_a_remediation\tools\fingerprint_tool.py $env:TEMP\fp.csv final_r2=pismo_dataset_final_r2 release_r2=pismo_kb_release_r2 kb_corpus_r2=pismo_kb_release_r2\kb_corpus final=pismo_dataset_final release=pismo_kb_release kb_corpus=pismo_kb_release\kb_corpus
#   compare with the table in "Current release: r2" above (r1 values also in pismo_validation\phase_b\validation\fingerprints_end.csv)
```

The KB verifier (`internal\tools\verify_kb_release.py <dataset> <kb_release>`) **writes `internal/reports/verification_results.json` inside the release it checks**. To check without changing the release, run it on a copy. Use a short path, because some files exceed the Windows 260-character limit when copied under deep folders:

```powershell
robocopy pismo_kb_release_r2 $env:TEMP\kbv /E
python -I pismo_kb_release_r2\internal\tools\verify_kb_release.py pismo_dataset_final_r2 $env:TEMP\kbv
```

**Do not run `pismo_dataset_final\scripts\validate_dataset.py` casually.** It overwrites `metadata/PISMO_DATASET_MANIFEST.json`, `openapi_manifest.csv` and `markdown_validation.csv`.

Scripts that read or write paths take them as arguments, or resolve them relative to their own location. None hard-codes the project root. Pass explicit paths. The other scripts under `pismo_validation/` and `pismo_work/` were not re-run during the consolidation.

## Open issues and next step

Open issues (details in `DATASET_COMPARISON_REPORT.md` §7 and `REMEDIATION_REPORT.md`):

- **Promotion decision pending.** Should `phase_a_remediation/corrected_dataset/` and `corrected_release_candidate/` be adopted? They differ from r1 only in two derived CSVs and their documentation; the raw Markdown and YAML are identical. They were built from r1, so they don't contain the r2 changelog backfill. Adopting them now means applying their two CSV corrections on top of r2.
- **Event payload pages were never collected.** robots.txt disallows `/events/`, and an owner decision on event content is needed.
- **426 example rows are unresolved `$ref` pointers.** Full API answers must read the YAML with `$ref` resolution.
- **33 conflicts are unresolved** in the `client-webhooks.md` tables and await Pismo. Register conflicts C1 and C2 are still open.
- **There are 7 duplicate "get started" page pairs.**
- **7 guide pages reference decommissioned marketplace endpoints** (found 2026-10-16; no KB change made).
  - **Evidence of removal**, both in the KB:
    - `kb_corpus/docs/resources/api-endpoints-removed.md` (lines 65–109) lists 7 marketplace endpoint paths removed on `10/6/26`;
    - `kb_corpus/changelog/2-october-2026.md` (lines 476–485) lists 8 decommissioned endpoint names.
  - **Affected pages**, under `kb_corpus/docs/`:
    - `get-started/get-started-building-seller-management.md` (L20, L24);
    - `seller-management/get-started-with-seller-management.md` (L20, L24);
    - `seller-management/seller-management-onboarding.md` (L38, L42);
    - `seller-management/seller-management-overview.md` (L59, L65);
    - `seller-management/managing-merchant-transactions.md` (L97, L101);
    - `seller-management/step-2-create-program-marketplace.md` (L24);
    - `data-and-reporting/marketplace-data-events.md` (L14).
  - **Endpoints referenced:**
    - Create marketplace V2 (`postmarketplacesv2`);
    - Link merchant and marketplace (`postlinkmerchanttomarketplacev1`);
    - List marketplace merchants V2 (`getmerchantsbymarketplaceidv2`);
    - Update marketplace (`putupdatemarketplacev1`).
  - **Matching method:** the slugs were matched to the removed endpoints by name; they are not in `llms.txt` or the YAML.
  - **No successor is confirmed** in any local source. "Create marketplace V3" exists, but nothing states that it replaces V2.
  - **Already correct:** the OpenAPI specs and the derived tables contain none of the removed paths.
  - **Requirement for the chatbot:** when it retrieves these pages, it must not present these endpoints as current without accounting for the removal evidence. It must not name a successor unless an official source confirms one.
- **Historical logs and reports cite the former root**, `...\pismo_claude_code_handoff\pismo_claude_code_handoff\`. They are kept unchanged because they are hash-covered evidence. The same relative paths now sit directly under this folder.

## Known retrieval test cases

- **"which pages were excluded from the corpus and why"** is a governance query in `verify_kb_release.py`, section D.
  - **Change:** its keyword-search top 3 changed between r1 and r2, because two of the new 2025 changelog posts now rank for it.

    | Release | Top 3 |
    | --- | --- |
    | r1 | `docs/resources/use-llms-with-pismo-developers-portal.md`, `api-specs/Platform_setup_-_Organizations.yaml`, `docs/data-and-reporting/event-filtering.md` |
    | r2 | `docs/resources/use-llms-with-pismo-developers-portal.md`, `changelog/8-august-2025.md`, `changelog/7-july-2025.md` |

  - **Why it's acceptable:** all results are Pismo documentation, and no internal project record surfaces. The governance-wording hits (section B) are identical in r1 and r2.
  - **Expected behaviour:** treat the r2 ranking as expected for this query. The corpus was **not** changed to restore the old ranking.
  - **Evidence:** `pismo_kb_release/internal/reports/verification_results.json` (r1) and `pismo_kb_release_r2/internal/reports/verification_results.json` (r2).

**Next step:** make the promotion decision for the corrected candidates. Then start the first assistant version on `pismo_kb_release_r2/kb_corpus/`, using `pismo_kb_release_r2/internal/provenance/source_map.csv` for citations.

See `CLEANUP_REPORT.md` for the 2026-10-16 folder consolidation.
