# Full Project Lifecycle Skill

## Trigger Conditions

Use this skill when any of these are true:

- A developer provides a new product, business, application, feature, bugfix,
  upgrade, expansion, or refactor idea for the mainline task tree.
- A developer asks why the Vibe Coding flow did not fully drive an idea into a
  complete project.
- A developer asks to continue with `next step` and the physical state points
  to `branch_mainline_idea`, a future product branch, or a lifecycle gate.
- A repository infrastructure task asks to establish or repair the mainline
  full-project workflow.

## Purpose

Prevent the mainline flow from collapsing into a brief requirement summary.
Every mainline or future project task line must pass through detailed,
auditable gates before implementation and must keep looping through slices and
round `n+1` until the task tree is closed or the developer redirects it.

## Required Runtime Inputs

- `docs/ai/status/current.yaml`
- `docs/ai/tasks/forest.yaml`
- `docs/ai/tasks/main-tree.yaml`
- `docs/ai/tasks/current-slice.yaml`
- `docs/ai/requirements/ledger.yaml`
- `docs/ai/decisions/records.md`
- `docs/ai/evidence/index.md`
- `docs/ai/handoff/current.md`
- `docs/ai/templates/full-project-lifecycle-workflow-sop.md`
- `docs/ai/skills/project-requirement-discovery/SKILL.md`
- `docs/ai/templates/project-requirement-discovery-sop.md`
- `docs/ai/templates/project-requirement-discovery-record.yaml`

## Gate Order

1. Route the work to the correct task line before analysis:
   `branch_vibe_coding_infra`, `branch_mainline_idea`, or another confirmed
   branch.
2. Capture the developer's target idea for the current round.
3. Run project requirement discovery before treating the idea as a requirement
   baseline candidate: interpret the idea, map requirement domains, inventory
   developer-stated and AI-inferred requirements, build a question backlog,
   collect answers across rounds, persist the discovery record, plan remaining
   requirement work, and check baseline readiness.
4. Analyze requirements into problem, users, scope, non-goals, constraints,
   risks, acceptance criteria, and open questions.
5. Stop for hard confirmation of the requirement baseline.
6. Perform current-source research when technology stack, APIs, libraries,
   regulations, pricing, schedules, model choices, or other unstable facts
   affect the project. Use official or primary sources where possible.
7. Stop for research and technology-stack confirmation.
8. Analyze tasks into a complete work breakdown, dependency order, test plan,
   documentation plan, and closure criteria.
9. Stop for task-analysis confirmation.
10. Design architecture and stack, including data model, integration boundaries,
   risks, rollback, and quality gates.
11. Stop for architecture and stack confirmation.
12. Recommend an infrastructure mode:
   `standard_light_risk_escalated` or `enterprise_high_assurance`.
13. Explain why the recommendation fits the risk profile and stop for
    developer confirmation. Also explain why the other mode is not the best
    default for the current round and what would cause escalation.
14. Establish or update the Agent Vibe Coding driving facilities required for
    this round: skills, knowledge, context/rules, prompt surfaces, schemas,
    status, evidence, and handoff.
15. Create or update the task tree and execution slices.
16. For each slice, implement code, write and run tests, document changes,
    update state, record evidence, and expose the next allowed step.
17. When all slices are complete, close the task tree with validation and
    acceptance evidence.
18. Re-enter the lifecycle as `next_round_intake[n+1]` for the next developer
    idea, iteration, upgrade, expansion, or refactor.

## Hard Stops

Do not implement product code, install dependencies, create package manifests,
choose a technology stack, change production settings, or expand agent agency
before the relevant confirmation gate is satisfied and recorded.

Do not treat `next step` as permission to skip requirement, research, task
analysis, architecture, or mode confirmation. `next step` only advances to the
next permitted gate or active slice in physical state.

## Verification

A lifecycle step is complete only when the corresponding physical artifact and
evidence exist. Chat-only intent is not enough.
