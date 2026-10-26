# Cleanup report: project consolidation (2026-10-16)

**Final project root:** `C:\Users\artlptp263user\Downloads\pismo_claude_code_handoff\`

The nested `pismo_claude_code_handoff\pismo_claude_code_handoff\`a folder no longer exists.

## Before and after

```
BEFORE  Downloads\
  pismo_claude_code_handoff\                 <- VS Code opened here
    pismo_dataset\                           99 files (duplicate)
    pismo_claude_code_handoff\               <- actual project
      CLAUDE_CODE_PROMPT.md                  0 bytes
      pismo_dataset.zip                      duplicate of pismo_work\ copy
      pismo_inventory_stage.zip              duplicate of pismo_work\ copy
      pismo_dataset_final\  pismo_kb_release\  pismo_signoff_results\
      pismo_validation\  pismo_work\
  pismo_download_handoff\pismo_download_handoff\
    CLAUDE_CODE_PROMPT_DOWNLOAD.md
    pismo_download_stage.zip                 duplicate
    pismo_signoff_results\                   10 files (duplicate)

AFTER   Downloads\
  pismo_claude_code_handoff\                 <- single project root
    README.md  CLEANUP_REPORT.md             (new)
    pismo_dataset_final\  pismo_kb_release\  pismo_signoff_results\
    pismo_validation\  pismo_work\           (contents unchanged)
  pismo_download_handoff\pismo_download_handoff\
    CLAUDE_CODE_PROMPT_DOWNLOAD.md           (kept; see below)
  pismo_claude_code_handoff_backup_20261016\ (backup)
```

## Moved

These five directories moved from `...\pismo_claude_code_handoff\pismo_claude_code_handoff\` to the outer root as same-volume renames:

- `pismo_dataset_final`
- `pismo_kb_release`
- `pismo_validation`
- `pismo_work`
- `pismo_signoff_results`

There were no name collisions. After the move, all 3,777 files were re-hashed, with 0 mismatches against the pre-move SHA-256 manifest.

## Removed, with evidence

All comparisons used SHA-256 plus relative path.

| Item | Evidence |
| --- | --- |
| `pismo_claude_code_handoff\pismo_dataset\` (99 files) | 99/99 identical to `pismo_work\pismo_dataset\` and to the 99 entries of `pismo_work\pismo_dataset.zip`. Re-checked just before deletion. |
| Inner-root `pismo_dataset.zip` | Same SHA-256 as `pismo_work\pismo_dataset.zip` (`4951F0BB…B564`). |
| Inner-root `pismo_inventory_stage.zip` | Same SHA-256 as `pismo_work\pismo_inventory_stage.zip` (`0E981E62…04B9`). Its 4 entries are identical to `pismo_work\pismo_inventory_stage\`. |
| Inner-root `CLAUDE_CODE_PROMPT.md` | 0 bytes (SHA-256 `E3B0C442…`, the hash of an empty file), so there was no content to keep. |
| Empty inner folder `pismo_claude_code_handoff\` | It was empty after the items above. |
| `pismo_download_handoff\…\pismo_signoff_results\` (10 files) | 10/10 identical to the project's `pismo_signoff_results\`. Re-checked just before deletion. |
| `pismo_download_handoff\…\pismo_download_stage.zip` | Its 3 entries are identical to `pismo_work\pismo_download_stage\`. Re-checked just before deletion. |

**Process note:** for the two inner-root ZIPs and the empty prompt, the re-check right before deletion was faulty. My helper function `H` was shadowed by PowerShell's built-in `H` alias (`Get-History`), so the comparison saw empty values. These items had already been proven identical in the inventory pass. After deletion, I compared their backup copies with real SHA-256 against the surviving copies: both ZIPs are identical, and the prompt is 0 bytes. No content was lost. The outer `pismo_dataset\` was not deleted in that faulty step; it was deleted later, after a correct check.

## Deliberately preserved

- **`pismo_work\pismo_dataset.zip` and `pismo_inventory_stage.zip`:** these are the inputs whose hashes are recorded in `runs\inventory_20261014_101459\RESULT.md`, and `INVENTORY_CHECK_RUNBOOK.md` references them as `../pismo_dataset.zip`.
- **`pismo_work\pismo_dataset\` and `pismo_dataset_v2\`:** documented build stages, and part of the recorded fingerprints.
- **`pismo_validation\phase_a_remediation\corrected_dataset\` and `corrected_release_candidate\`:** unpromoted candidates. They are kept separate and not merged with the release.
- **All 6 `__pycache__` folders:** the `.pyc` files are included in the recorded fingerprints (v2 and final), so deleting them would break the fingerprint checks.
- **Historical logs and reports that contain the old absolute path:** they are hash-covered evidence.
- **`Downloads\pismo_download_handoff\…\CLAUDE_CODE_PROMPT_DOWNLOAD.md`:** identical to `pismo_work\provenance\prompts\CLAUDE_CODE_PROMPT_DOWNLOAD.md` (SHA-256 `05662C7F…`), but it was not on the approved removal list.
- **`Downloads\pismo_download_handoff.zip`:** it contains that prompt and the download-stage ZIP. It is outside the project and was not on the list.

## Backup

`C:\Users\artlptp263user\Downloads\pismo_claude_code_handoff_backup_20261016\`

Made with robocopy before any change. It contains:

- the full outer folder;
- `pismo_download_handoff\`;
- `pismo_download_handoff.zip`;
- `pre_manifest.csv`: SHA-256 of all 3,891 original files;
- `zip_entries.csv`: SHA-256 of every ZIP entry.

**Verification:** all 3,891 files were re-hashed from the backup with long-path-aware reads, with 0 problems. Some backup paths exceed 260 characters, so restore with `robocopy`, not Explorer.

## Path and configuration changes

None were needed, and no script, configuration or data file was edited.

- All 53 scripts take paths as arguments or resolve them from `__file__`. None hard-codes the project root.
- Relative references, such as the runbook's `../pismo_dataset.zip`, still resolve, because the internal layout is unchanged.
- No `.vscode`, `.claude`, `CLAUDE.md` or user-settings file referenced the old paths.
- Absolute old-root paths remain only in historical outputs: `V2_PROVENANCE.json`, run logs, fingerprint files and Phase A/B results. Editing them would invalidate recorded hashes. The README explains how to map them.

## Validation (run 2026-10-16, after the move)

| Check | Result |
| --- | --- |
| Whole tree vs pre-move manifest | 3,777/3,777 present and identical; 0 new files besides the two reports |
| `fingerprint.py` on `pismo_work\pismo_dataset_v2` | `7573dc2f…8b99`, 525 files, equal to `v2_fingerprint_after.txt` |
| `fingerprint.py` on `pismo_work\pismo_dataset` | `bfc8c38c…f15f`, equal to `dataset_fingerprint_before_download.txt` |
| `fingerprint_tool.py` (P method) | v2, final, release, kb_corpus, signoff, corrected_dataset, corrected_release_candidate: all equal to `phase_b\validation\fingerprints_end.csv`. Raw Markdown `51e76922…` equals the Phase B record. |
| `openapi_manifest.csv` vs `raw\openapi\` | 71 rows, 71 YAML files; 0 hash or size mismatches |
| `PISMO_DOWNLOAD_MANIFEST.csv` vs `raw\markdown\` | 414 file paths, 0 missing, 0 SHA-256 mismatches, 0 unlisted files |
| KB allowlist vs `kb_corpus\` | 491/491, 0 mismatches |
| `verify_kb_release.py` (on a temp copy of the release) | exit 0; all five result sections identical to the recorded `verification_results.json` |
| Authoritative datasets and releases | one dataset (`pismo_dataset_final`), one release (`pismo_kb_release`); the candidates stay in `pismo_validation` |

**Not run:**

- `validate_dataset.py`: it overwrites the authoritative manifests.
- The download, collection and build scripts: they need network access or rewrite outputs.
- The other `pismo_validation` tools.

## Remaining risks

- Historical evidence files cite the former absolute root. That is accurate as history but not portable.
- `verify_kb_release.py` and `validate_dataset.py` write into the trees they check. Run them on copies.
- The old `Downloads\pismo_download_handoff\` folder and `pismo_download_handoff.zip` still exist outside the project. They hold only duplicates of preserved content and can be deleted once you approve.
- A failed KB-verifier copy, made during this work, is left in the Claude Code session scratchpad, outside the project. The harness blocked deleting its long path.
