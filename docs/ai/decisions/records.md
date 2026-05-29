# Decision Records

## decision_001: Bootstrap Runtime Infrastructure

- Date: `2026-05-29T17:18:17+08:00`
- Status: `accepted_for_bootstrap`
- Source: developer compiler run request
- Decision: Create lightweight Vibe Coding runtime infrastructure in `AGENTS.md`
  and `docs/ai/*`.
- Rationale: The repository had no existing runtime entries, rules,
  dependency files, tests, CI, or business files. The bootstrap can safely stay
  within documentation and AI runtime infrastructure.
- Alternatives:
  - Do nothing: rejected because runtime state would remain only in chat.
  - Build business code immediately: rejected because core governance comes
    before business execution.
- Confirmation level: `auto_recordable` for bootstrap files only.
- Evidence: `evidence_001`, `evidence_010`
- No prompt runtime dependency: true

## decision_002: Human Documentation Slice

- Date: `2026-05-29T17:34:47+08:00`
- Status: `accepted_for_low_risk_execution`
- Source: developer goal, "当前项目的食用（使用）教程等相关详细概述文件"
- Decision: Create root and `docs/` human-facing documentation for project
  overview, usage, maintenance, and Agent workflow.
- Rationale: The repository had runtime infrastructure but no human tutorial or
  overview. Documentation is low risk and improves recoverability.
- Alternatives:
  - Ask for more detail before writing: not needed because the requested scope
    is clear and low risk.
  - Create only README: rejected because the user asked for detailed overview
    files.
- Confirmation level: `auto_recordable` within documentation and docs/ai
  status/evidence files.
- Evidence: `evidence_012`
- No prompt runtime dependency: true

## decision_003: Python Runtime Validator

- Date: `2026-05-29T17:43:05+08:00`
- Status: `accepted_for_low_risk_execution`
- Source: developer request, "将项目中脚本，替换成py"
- Decision: Replace the runtime validation script with
  `docs/ai/scripts/validate_runtime.py` and update command references.
- Rationale: Python is available in the local environment and is more portable
  across Windows, macOS, and Linux for this repository's lightweight validator.
- Alternatives:
  - Keep the PowerShell validator: rejected by developer request.
  - Add both PowerShell and Python validators: rejected because the request was
    to replace scripts with Python.
- Confirmation level: `auto_recordable` for low-risk runtime script
  maintenance.
- Evidence: `evidence_014`
- No prompt runtime dependency: true

## decision_004: Task Forest With Vibe Coding Infrastructure Branch

- Date: `2026-05-29T17:54:03+08:00`
- Status: `accepted_for_low_risk_execution`
- Source: developer request to analyze, sandbox, and implement a separate Vibe
  Coding task tree branch.
- Decision: Introduce `docs/ai/tasks/forest.yaml`, reserve
  `docs/ai/tasks/main-tree.yaml` for future product or business ideas, and route
  Vibe Coding repository infrastructure work to
  `docs/ai/tasks/branches/vibe-coding-infra/tree.yaml`.
- Rationale: Documentation, runtime validation scripts, schemas, state, evidence,
  knowledge, skills, and handoff changes iterate this repository's Vibe Coding
  infrastructure. They should not pollute the future mainline idea task tree.
- Alternatives:
  - Keep one task tree: rejected because it mixes infrastructure maintenance
    with product idea work.
  - Create a new mainline round for every infrastructure edit: rejected because
    these edits are not product idea rounds.
- Confirmation level: `auto_recordable` because the developer explicitly asked
  for this governance capability and the change is documentation/runtime-state
  scoped.
- Evidence: `evidence_015`
- No prompt runtime dependency: true

## decision_005: Catalog-Only Capability Groups

- Date: `2026-05-29T18:53:11+08:00`
- Status: `accepted_for_confirmed_A_execution`
- Source: developer confirmation, "确认 A，进入阶段二，只建立能力目录、skills、知识库、依赖候选清单，不创建工程骨架，不安装依赖。"
- Decision: Create `docs/ai/capabilities/`, grouped capability candidate
  files, a capability-selection skill, a knowledge entry, research notes, and
  architecture strategy notes as catalog-only infrastructure.
- Rationale: The developer confirmed the conservative A route: preserve
  future choice surfaces without committing the repository to a UI library,
  framework, Python toolchain, package manifest, lockfile, or application
  skeleton.
- Alternatives:
  - Create an engineering skeleton now: rejected by explicit developer
    constraint.
  - Install dependencies now: rejected by explicit developer constraint.
  - Keep only a chat recommendation: rejected because runtime recovery needs
    physical docs, skills, knowledge, and evidence.
- Confirmation level: `hard_confirmation` for the A strategy boundary,
  `auto_recordable` for low-risk docs/ai runtime artifacts inside that boundary.
- Evidence: `evidence_016`
- No prompt runtime dependency: true
