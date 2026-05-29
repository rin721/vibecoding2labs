# Slice Execution Skill

## Trigger Conditions

- A current execution slice has `status: not_started`, `in_progress`, or
  `pending_verification`.
- The user asks to continue implementation or verification.

## Inputs

- `docs/ai/tasks/current-slice.yaml`
- `docs/ai/status/current.yaml`
- Relevant requirements, decisions, research, architecture, and task records.

## Outputs

- Code or documentation changes only within `allowed_files`.
- Validation command output recorded in `docs/ai/evidence/index.md`.
- Updated status, current slice, knowledge, skills, and handoff when needed.

## Boundaries

- Do not expand `allowed_files`.
- Do not install dependencies, change lockfiles, touch production settings, or
  perform destructive work without explicit confirmation.
- Stop after three repeated failures for the same validation or semantic risk.

## Steps

1. Confirm the slice goal and allowed files.
2. Make the smallest useful change.
3. Run declared validation commands or a documented alternative.
4. Record evidence.
5. Update status and handoff.
6. Move to the next slice only when the current slice is completed or formally
   blocked, skipped, superseded, or moved with confirmation.

## Verification

- The validation result supports the new status.
- The slice remains inside its file and risk boundaries.

