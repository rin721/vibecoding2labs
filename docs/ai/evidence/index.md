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
- Command: legacy runtime validation command, superseded by `python docs/ai/scripts/validate_runtime.py`
- Result: `Runtime validation passed.`
- Summary: Required runtime artifacts exist, status points to the bootstrap
  slice, and no runtime entry requires reading the original compiler prompt.

## evidence_011: Validation Command Portability Fix

- Date: `2026-05-29T17:29:21+08:00`
- Type: `physical_readability_issue`
- Status: `resolved`
- Finding: `pwsh` was not available in the local Windows environment.
- Adjustment: Runtime validation now uses the Python validator.
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
  - `python docs/ai/scripts/validate_runtime.py` -> `Runtime validation passed.`
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
- Validation: `python docs/ai/scripts/validate_runtime.py` -> `Runtime validation passed.`

## evidence_014: Python Runtime Script Replacement

- Date: `2026-05-29T17:44:56+08:00`
- Type: `runtime_script_update`
- Status: `completed`
- Requirement: `req_round_001_python_scripts`
- Slice: `slice_002_python_scripts`
- Files:
  - `docs/ai/scripts/validate_runtime.py`
  - `README.md`
  - `docs/usage-guide.md`
  - `docs/maintenance-guide.md`
  - `docs/ai/manifest.yaml`
  - `docs/ai/quality/gates.md`
  - `docs/ai/schemas/core.schema.yaml`
  - `docs/ai/tasks/current-slice.yaml`
  - `docs/ai/tasks/slices/slice_002_python_scripts.yaml`
- Validation:
  - `python docs/ai/scripts/validate_runtime.py` -> `Runtime validation passed.`
  - `python -m py_compile docs/ai/scripts/validate_runtime.py` -> passed.
  - script inventory check under `docs/ai/scripts` -> only `validate_runtime.py` found.
  - Markdown local link check -> `Markdown local links OK`.
- Summary: Runtime validator was replaced with Python and command references were updated.

## evidence_015: Task Forest Branching

- Date: `2026-05-29T17:58:59+08:00`
- Type: `runtime_task_governance_update`
- Status: `completed`
- Requirement: `req_infra_003_task_forest_branching`
- Slice: `slice_003_task_forest_branching`
- Analysis:
  - `docs/ai/analysis/task-forest-branching.md`
- Sandbox:
  - `docs/ai/sandbox/sandbox_001_task_forest_branching.yaml`
- Files:
  - `docs/ai/tasks/forest.yaml`
  - `docs/ai/tasks/main-tree.yaml`
  - `docs/ai/tasks/branches/vibe-coding-infra/tree.yaml`
  - `docs/ai/tasks/tree.yaml`
  - `docs/ai/tasks/current-slice.yaml`
  - `docs/ai/tasks/slices/slice_003_task_forest_branching.yaml`
  - `docs/ai/status/current.yaml`
  - `docs/ai/runtime-rule-index.md`
  - `docs/ai/scripts/validate_runtime.py`
- Validation:
  - `python docs/ai/scripts/validate_runtime.py` -> `Runtime validation passed.`
  - task forest routing search for `branch_vibe_coding_infra`, `branch_mainline_idea`, and `TaskForest` -> matched status, task forest, branch tree, main tree, compatibility pointer, slices, and runtime rule index.
- Summary: Task forest and Vibe Coding infrastructure branch are implemented and validated.

## evidence_016: Catalog-Only Capability Groups

- Date: `2026-05-29T18:53:11+08:00`
- Type: `runtime_capability_catalog_update`
- Status: `completed`
- Requirement: `req_infra_004_capability_groups`
- Slice: `slice_004_capability_groups`
- Research:
  - `docs/ai/research/research_001_capability_groups.md`
- Architecture:
  - `docs/ai/architecture/capability-group-strategy.md`
- Files:
  - `docs/ai/capabilities/index.md`
  - `docs/ai/capabilities/dependency-candidates.yaml`
  - `docs/ai/capabilities/groups/ui-library.yaml`
  - `docs/ai/capabilities/groups/frontend-architecture.yaml`
  - `docs/ai/capabilities/groups/agent-script-tools.yaml`
  - `docs/ai/capabilities/groups/python-tooling.yaml`
  - `docs/ai/capabilities/groups/agent-frameworks.yaml`
  - `docs/ai/capabilities/groups/quality-verification.yaml`
  - `docs/ai/skills/capability-selection/SKILL.md`
  - `docs/ai/knowledge/entries/kb_005_capability_groups.md`
- Validation:
  - `python docs/ai/scripts/validate_runtime.py` -> `Runtime validation passed.`
  - `Test-Path package.json, pyproject.toml, requirements.txt, src, app, components, tools` -> all returned `False`.
  - `rg -n "capability_catalog_001|req_infra_004_capability_groups|slice_004_capability_groups|skill_capability_selection|kb_005" docs/ai` -> matched catalog, requirement, slice, skill, and knowledge entries.
  - Markdown local link check -> `Markdown local links OK`.
- Summary: Catalog-only capability groups were added without dependency
  installation, package manifests, lockfiles, or engineering skeleton creation.
