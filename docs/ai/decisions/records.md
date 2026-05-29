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
