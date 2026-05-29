# Current Handoff

- Project: `vibecoding2labs`
- Runtime version: `vibe-runtime-0.1.0`
- Current phase: `acceptance`
- Current round: `infra_001`
- Current branch: `branch_vibe_coding_infra`
- Current tree: `docs/ai/tasks/branches/vibe-coding-infra/tree.yaml`
- Current mode: `project_requirement_discovery_completed_pending_acceptance`
- Agency level: `controlled_execution`
- Current slice: `slice_008_project_requirement_discovery` pending developer acceptance

## Completed

- Readonly preflight found an empty repository except `.git`.
- Core runtime entries were created under `AGENTS.md` and `docs/ai/*`.
- Minimum knowledge and skills entries were created.
- Bootstrap verification passed; the legacy validator command has since been
  superseded by the Python validator.
- Human-facing docs were created for project overview, usage, maintenance, and
  Agent workflow.
- Runtime validation passed after the documentation slice.
- Runtime validator was replaced with `docs/ai/scripts/validate_runtime.py`.
- Task forest branching was introduced so Vibe Coding infrastructure work lives
  in `branch_vibe_coding_infra`, while future product or business ideas use
  `branch_mainline_idea`.
- The developer confirmed strategy A for capability infrastructure: create only
  capability directories, skills, knowledge, and dependency candidate lists; do
  not create an engineering skeleton or install dependencies.
- The developer green-lit phase two for strategy A with the added rule that
  current official source research must derive the current year dynamically
  instead of hard-coding it.
- The capability catalog was refreshed against current official docs and now
  records `uv`, `Zod 4`, current shadcn/ui install paths, OpenAI Agents SDK
  sessions/tracing, and LangGraph persistence as candidate-only details.
- Added a trigger-bound Vibe infrastructure action workflow skill and canonical
  SOP template; the workflow binds the trigger suffix to
  `{{ optimization_action }}`, enforces phase-one four-dimensional diagnosis and
  red-light stop, and allows phase-two physical output only after explicit
  human authorization.
- Added a full-project lifecycle gap analysis, architecture note, project skill,
  canonical SOP, and knowledge entry so future mainline or project task lines
  must route the task line, analyze and confirm requirements, perform
  current-source research for technology choices, confirm research, analyze and
  confirm tasks, design and confirm architecture/stack, recommend and confirm
  infrastructure mode, establish Agent Vibe Coding driving infrastructure,
  create task trees and slices, implement, test, document, update state and
  evidence, use the `next step` protocol, close the task tree, and continue into
  round `n+1`.
- Added a compiler-runtime assimilation analysis, architecture note, project
  skill, canonical SOP, and knowledge entry so future compiler, generator, or
  macro governance specifications are routed to `branch_vibe_coding_infra` and
  distilled into local runtime artifacts instead of becoming `prompt.md` or a
  raw prompt runtime dependency.
- Added a project requirement discovery gap analysis, architecture note,
  project skill, canonical SOP, durable intake record template, and knowledge
  entry so future raw project ideas are interpreted, mapped into requirement
  domains, guided through question backlogs, persisted, planned, and checked for
  baseline readiness before requirement-baseline confirmation.

## Unfinished

- Developer acceptance of the documentation, script replacement, task forest
  branching, refreshed catalog-only capability, trigger-bound workflow SOP,
  full-project lifecycle workflow, compiler-runtime assimilation, and project
  requirement discovery slices is pending.
- No future mainline product implementation has started. A future mainline idea
  must use the full-project lifecycle workflow before implementation.

## Key Files

- `AGENTS.md`
- `docs/ai/runtime-rule-index.md`
- `docs/ai/status/current.yaml`
- `docs/ai/tasks/bootstrap-tree.yaml`
- `docs/ai/tasks/current-slice.yaml`
- `docs/ai/requirements/ledger.yaml`
- `docs/ai/authorizations/records.md`
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
- `docs/ai/skills/vibe-infra-action-workflow/SKILL.md`
- `docs/ai/templates/vibe-infra-action-workflow-sop.md`
- `docs/ai/knowledge/entries/kb_005_capability_groups.md`
- `docs/ai/knowledge/entries/kb_006_vibe_infra_action_workflow.md`
- `docs/ai/analysis/mainline-full-project-lifecycle-gap-analysis.md`
- `docs/ai/architecture/full-project-lifecycle-workflow.md`
- `docs/ai/skills/full-project-lifecycle/SKILL.md`
- `docs/ai/templates/full-project-lifecycle-workflow-sop.md`
- `docs/ai/knowledge/entries/kb_007_full_project_lifecycle.md`
- `docs/ai/analysis/compiler-runtime-assimilation.md`
- `docs/ai/architecture/compiler-runtime-assimilation.md`
- `docs/ai/skills/compiler-runtime-assimilation/SKILL.md`
- `docs/ai/templates/compiler-runtime-assimilation-sop.md`
- `docs/ai/knowledge/entries/kb_008_compiler_runtime_assimilation.md`
- `docs/ai/analysis/project-requirement-discovery-gap-analysis.md`
- `docs/ai/architecture/project-requirement-discovery-workflow.md`
- `docs/ai/skills/project-requirement-discovery/SKILL.md`
- `docs/ai/templates/project-requirement-discovery-sop.md`
- `docs/ai/templates/project-requirement-discovery-record.yaml`
- `docs/ai/requirements/intake/README.md`
- `docs/ai/knowledge/entries/kb_009_project_requirement_discovery.md`

## Next Condition

Ask the developer to accept the project requirement discovery workflow or
request edits. Do not start a mainline idea task tree until the active Vibe
Coding infrastructure branch slices are accepted, edited, migrated, or
explicitly closed.

## Forbidden Actions

- Do not read the original compiler prompt as a normal recovery path.
- Do not create `prompt.md` as a runtime authority when a compiler or generator
  specification is provided after bootstrap; distill it into local runtime
  artifacts through the compiler-runtime assimilation workflow.
- Do not start a mainline idea task tree until `branch_vibe_coding_infra`
  active slices are accepted, migrated, discarded, or partially closed with
  confirmation.
- Do not create business implementation before requirement, research, task
  analysis, architecture, and mode confirmation.
- Do not create `package.json`, `pyproject.toml`, lockfiles, `src/`, `app/`,
  `components/`, or `tools/` from the capability catalog alone.
- Do not install dependencies from the candidate catalog without a future
  confirmed execution slice.
- Do not hard-code a calendar year into future capability research prompts; use
  runtime date or source refresh timestamp.
- Do not treat the Vibe infrastructure action workflow trigger as
  authorization for phase-two physical output; it only starts phase-one
  diagnosis until explicit human confirmation is received.
- Do not let a future mainline idea skip the full-project lifecycle skill:
  task-line routing, requirement confirmation, current-source research,
  task-analysis confirmation, architecture confirmation, and mode confirmation
  must happen before implementation.
- Do not let a future raw project idea skip the project requirement discovery
  skill: idea interpretation, domain mapping, requirement inventory, question
  backlog, persistent intake record, requirement planning, and baseline
  readiness must happen before requirement-baseline confirmation.
