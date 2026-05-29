# Capability Group Architecture Strategy

- Architecture id: `arch_001_capability_groups`
- Branch: `branch_vibe_coding_infra`
- Status: `candidate_catalog_ready`
- Updated at: `2026-05-29T18:50:41+08:00`

## Goal

Prepare selectable capability groups for the future `branch_mainline_idea`
without prematurely installing dependencies or creating a business application
skeleton.

## Architecture

```text
branch_vibe_coding_infra
  -> docs/ai/capabilities/index.md
  -> docs/ai/capabilities/dependency-candidates.yaml
  -> docs/ai/capabilities/groups/*.yaml
  -> docs/ai/research/research_001_capability_groups.md
  -> docs/ai/knowledge/entries/kb_005_capability_groups.md
  -> docs/ai/skills/capability-selection/SKILL.md

branch_mainline_idea
  -> future confirmed requirement
  -> choose capability groups
  -> create execution slice
  -> request hard confirmation for install/scaffold
```

## Selection Flow

1. Developer confirms a business mainline goal.
2. Agent reads the capability catalog.
3. Agent proposes only the groups needed by the goal.
4. Developer confirms selected groups and package manager.
5. Agent creates a new execution slice with install commands, allowed files,
   verification, rollback, and evidence targets.
6. Only then may dependencies or skeleton files be created.

## Non-Goals

- No `package.json`.
- No `pyproject.toml`.
- No `src/`, `app/`, `components/`, `tools/`, or `tests/` skeleton.
- No dependency installation.
- No lockfile.

## Quality Gates

- `python docs/ai/scripts/validate_runtime.py`
- Verify no forbidden skeleton or package files were created.
- Verify capability groups are referenced from knowledge, skills, and handoff.

