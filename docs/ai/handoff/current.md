# Current Handoff

- Project: `vibecoding2labs`
- Runtime version: `vibe-runtime-0.1.0`
- Current phase: `acceptance`
- Current round: `infra_001`
- Current branch: `branch_vibe_coding_infra`
- Current tree: `docs/ai/tasks/branches/vibe-coding-infra/tree.yaml`
- Current mode: `pending_confirmation`
- Agency level: `controlled_execution`
- Current slice: `slice_004_capability_groups` pending developer acceptance

## Completed

- Readonly preflight found an empty repository except `.git`.
- Core runtime entries were created under `AGENTS.md` and `docs/ai/*`.
- Minimum knowledge and skills entries were created.
- Bootstrap verification passed; the legacy validator command has since been superseded by the Python validator.
- Human-facing docs were created for project overview, usage, maintenance, and Agent workflow.
- Runtime validation passed after the documentation slice.
- Runtime validator was replaced with `docs/ai/scripts/validate_runtime.py`.
- Task forest branching was introduced so Vibe Coding infrastructure work
  lives in `branch_vibe_coding_infra`, while future product or business ideas
  use `branch_mainline_idea`.
- The developer confirmed strategy A for capability infrastructure: create only
  capability directories, skills, knowledge, and dependency candidate lists; do
  not create an engineering skeleton or install dependencies.

## Unfinished

- Developer acceptance of the documentation, script replacement, task forest
  branching, and catalog-only capability slices is pending.
- Mode selection for future business implementation is still pending.

## Key Files

- `AGENTS.md`
- `docs/ai/runtime-rule-index.md`
- `docs/ai/status/current.yaml`
- `docs/ai/tasks/bootstrap-tree.yaml`
- `docs/ai/tasks/current-slice.yaml`
- `docs/ai/requirements/ledger.yaml`
- `docs/ai/evidence/index.md`
- `docs/ai/knowledge/index.md`
- `docs/ai/skills/index.md`
- `README.md`
- `docs/index.md`
- `docs/project-overview.md`
- `docs/usage-guide.md`
- `docs/maintenance-guide.md`
- `docs/agent-workflow-guide.md`
- `docs/ai/scripts/validate_runtime.py`
- `docs/ai/tasks/forest.yaml`
- `docs/ai/tasks/main-tree.yaml`
- `docs/ai/tasks/branches/vibe-coding-infra/tree.yaml`
- `docs/ai/analysis/task-forest-branching.md`
- `docs/ai/sandbox/sandbox_001_task_forest_branching.yaml`
- `docs/ai/capabilities/index.md`
- `docs/ai/capabilities/dependency-candidates.yaml`
- `docs/ai/architecture/capability-group-strategy.md`
- `docs/ai/research/research_001_capability_groups.md`
- `docs/ai/skills/capability-selection/SKILL.md`
- `docs/ai/knowledge/entries/kb_005_capability_groups.md`

## Next Condition

Ask the developer to accept the catalog-only A strategy outputs or request
edits. Do not start a mainline idea task tree until the active Vibe Coding
infrastructure branch slices are accepted, edited, migrated, or explicitly
closed.

## Forbidden Actions

- Do not read the original compiler prompt as a normal recovery path.
- Do not start a mainline idea task tree until `branch_vibe_coding_infra` active
  slices are accepted, migrated, discarded, or partially closed with
  confirmation.
- Do not create business implementation before requirement, research, task
  analysis, architecture, and mode confirmation.
- Do not create `package.json`, `pyproject.toml`, lockfiles, `src/`, `app/`,
  `components/`, or `tools/` from the capability catalog alone.
- Do not install dependencies from the candidate catalog without a future
  confirmed execution slice.
