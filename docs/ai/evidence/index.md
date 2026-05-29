# Evidence Index

## evidence_001: Readonly Preflight

- Date: `2026-05-29T17:18:17+08:00`
- Type: `preflight_readonly`
- Status: `completed`
- Commands:
  - `Get-Location; Get-ChildItem -Force | Select-Object Mode,Length,Name`
  - `git status --short --branch`
  - `rg --files ...`
  - `rg -n "TODO|FIXME|Vibe Coding|prompt\.md|AGENTS|test|lint|build" ...`
- Summary: Repository initially contained only `.git`; no existing runtime
  rules, docs, dependencies, tests, CI, or business files were found.
- Related artifacts:
  - `docs/ai/reports/preflight-readonly.md`

## evidence_002: Bootstrap Write Scope

- Date: `2026-05-29T17:18:17+08:00`
- Type: `authorization`
- Status: `completed`
- Summary: Bootstrap writes are constrained to `AGENTS.md`, `docs/.cursorrules`,
  and `docs/ai/**`.

## evidence_010: Bootstrap Runtime Verification

- Date: `2026-05-29T17:29:21+08:00`
- Type: `runtime_validation`
- Status: `completed`
- Command: `powershell -NoProfile -ExecutionPolicy Bypass -File docs/ai/scripts/validate-runtime.ps1`
- Result: `Runtime validation passed.`
- Summary: Required runtime artifacts exist, status points to the bootstrap
  slice, and no runtime entry requires reading the original compiler prompt.

## evidence_011: Validation Command Portability Fix

- Date: `2026-05-29T17:29:21+08:00`
- Type: `physical_readability_issue`
- Status: `resolved`
- Finding: `pwsh` was not available in the local Windows environment.
- Adjustment: Runtime validation commands were changed to `powershell`.
- Related invariant: `INV-16`

## evidence_012: Human Documentation Slice

- Date: `2026-05-29T17:37:15+08:00`
- Type: `documentation_update`
- Status: `completed`
- Requirement: `req_round_001_docs`
- Slice: `slice_001_docs_guides`
- Files:
  - `README.md`
  - `docs/index.md`
  - `docs/project-overview.md`
  - `docs/usage-guide.md`
  - `docs/maintenance-guide.md`
  - `docs/agent-workflow-guide.md`
- Validation:
  - `powershell -NoProfile -ExecutionPolicy Bypass -File docs/ai/scripts/validate-runtime.ps1` -> `Runtime validation passed.`
  - File existence checks -> all six human documentation files returned `OK`.
  - Markdown local link check -> `Markdown local links OK`.
- Summary: Human-facing tutorial and overview documentation exists and runtime validation passes.

## evidence_013: Runtime Validator Generalized

- Date: `2026-05-29T17:37:15+08:00`
- Type: `quality_gate_update`
- Status: `completed`
- Finding: The validator still assumed the bootstrap slice was current.
- Adjustment: The validator now checks that `status/current.yaml` `current_slice`
  matches `tasks/current-slice.yaml` `id`.
- Validation: `powershell -NoProfile -ExecutionPolicy Bypass -File docs/ai/scripts/validate-runtime.ps1` -> `Runtime validation passed.`
