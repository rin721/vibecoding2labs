from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


REQUIRED_ARTIFACTS = [
    "AGENTS.md",
    "docs/ai/manifest.yaml",
    "docs/ai/runtime-rule-index.md",
    "docs/ai/status/current.yaml",
    "docs/ai/requirements/ledger.yaml",
    "docs/ai/tasks/bootstrap-tree.yaml",
    "docs/ai/tasks/forest.yaml",
    "docs/ai/tasks/main-tree.yaml",
    "docs/ai/tasks/branches/vibe-coding-infra/tree.yaml",
    "docs/ai/tasks/current-slice.yaml",
    "docs/ai/capabilities/index.md",
    "docs/ai/capabilities/dependency-candidates.yaml",
    "docs/ai/evidence/index.md",
    "docs/ai/knowledge/index.md",
    "docs/ai/skills/index.md",
    "docs/ai/skills/full-project-lifecycle/SKILL.md",
    "docs/ai/templates/full-project-lifecycle-workflow-sop.md",
    "docs/ai/analysis/mainline-full-project-lifecycle-gap-analysis.md",
    "docs/ai/architecture/full-project-lifecycle-workflow.md",
    "docs/ai/knowledge/entries/kb_007_full_project_lifecycle.md",
    "docs/ai/handoff/current.md",
]

CATALOG_ONLY_FORBIDDEN_ARTIFACTS = [
    "package.json",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "pyproject.toml",
    "requirements.txt",
    "src",
    "app",
    "components",
    "tools",
]


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def fail(message: str) -> None:
    print(f"Runtime validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def extract_yaml_scalar(text: str, field: str, source: str) -> str:
    match = re.search(
        rf"(?m)^{re.escape(field)}:\s*([A-Za-z0-9_./\-\[\]]+)\s*$", text
    )
    if not match:
        fail(f"{source} must define {field}.")
    return match.group(1)


def main() -> None:
    missing = [path for path in REQUIRED_ARTIFACTS if not (ROOT / path).exists()]
    if missing:
        fail(f"Missing required runtime artifacts: {', '.join(missing)}")

    agents = read_text("AGENTS.md")
    if "No Prompt Runtime Dependency" not in agents:
        fail("AGENTS.md must include the no prompt runtime dependency section.")

    status = read_text("docs/ai/status/current.yaml")
    current_slice = read_text("docs/ai/tasks/current-slice.yaml")

    status_slice = extract_yaml_scalar(
        status, "current_slice", "docs/ai/status/current.yaml"
    )
    status_branch = extract_yaml_scalar(
        status, "current_branch", "docs/ai/status/current.yaml"
    )
    status_tree = extract_yaml_scalar(
        status, "current_tree", "docs/ai/status/current.yaml"
    )
    slice_id = extract_yaml_scalar(
        current_slice, "id", "docs/ai/tasks/current-slice.yaml"
    )
    slice_branch = extract_yaml_scalar(
        current_slice, "branch_id", "docs/ai/tasks/current-slice.yaml"
    )
    if status_slice != slice_id:
        fail(
            "docs/ai/status/current.yaml current_slice does not match "
            "docs/ai/tasks/current-slice.yaml id."
        )
    if status_branch != slice_branch:
        fail(
            "docs/ai/status/current.yaml current_branch does not match "
            "docs/ai/tasks/current-slice.yaml branch_id."
        )
    if not (ROOT / status_tree).exists():
        fail(f"current_tree does not exist: {status_tree}")

    candidates = read_text("docs/ai/capabilities/dependency-candidates.yaml")
    if "install_allowed: false" not in candidates:
        fail("Capability candidates must keep install_allowed: false.")
    if "scaffold_allowed: false" not in candidates:
        fail("Capability candidates must keep scaffold_allowed: false.")
    forbidden_existing = [
        path for path in CATALOG_ONLY_FORBIDDEN_ARTIFACTS if (ROOT / path).exists()
    ]
    if forbidden_existing:
        fail(
            "Catalog-only strategy forbids these root artifacts: "
            + ", ".join(forbidden_existing)
        )

    lifecycle_text = "\n".join(
        [
            read_text("docs/ai/runtime-rule-index.md"),
            read_text("docs/ai/skills/full-project-lifecycle/SKILL.md"),
            read_text("docs/ai/templates/full-project-lifecycle-workflow-sop.md"),
            read_text("docs/ai/knowledge/entries/kb_007_full_project_lifecycle.md"),
        ]
    )
    required_lifecycle_terms = [
        "task_line_routing_gate",
        "idea_intake_gate",
        "requirement_analysis_gate",
        "requirement_baseline_confirmation_gate",
        "current_source_research_gate",
        "research_confirmation_gate",
        "task_analysis_gate",
        "task_analysis_confirmation_gate",
        "architecture_and_stack_design_gate",
        "architecture_confirmation_gate",
        "infra_mode_recommendation_gate",
        "infra_mode_confirmation_gate",
        "agent_driving_infra_gate",
        "task_tree_and_slice_gate",
        "standard_light_risk_escalated",
        "enterprise_high_assurance",
        "implementation_test_docs_state_loop",
        "next_step_protocol_gate",
        "round_closure_gate",
        "next_round_intake[n+1]",
    ]
    missing_lifecycle_terms = [
        term for term in required_lifecycle_terms if term not in lifecycle_text
    ]
    if missing_lifecycle_terms:
        fail(
            "Full-project lifecycle artifacts are missing required terms: "
            + ", ".join(missing_lifecycle_terms)
        )

    skills_index = read_text("docs/ai/skills/index.md")
    knowledge_index = read_text("docs/ai/knowledge/index.md")
    if "skill_full_project_lifecycle" not in skills_index:
        fail("Skill index must reference skill_full_project_lifecycle.")
    if "kb_007" not in knowledge_index:
        fail("Knowledge index must reference kb_007.")

    forest = read_text("docs/ai/tasks/forest.yaml")
    selected_tree = read_text(status_tree)
    if status_branch not in forest:
        fail("Task forest does not contain the current branch.")
    if status_tree not in forest:
        fail("Task forest does not reference the current tree path.")
    if f"branch_id: {status_branch}" not in selected_tree:
        fail("Current tree does not declare the current branch_id.")

    extract_yaml_scalar(
        status, "next_allowed_phase", "docs/ai/status/current.yaml"
    )

    runtime_text = "\n".join(
        [
            read_text("AGENTS.md"),
            read_text("docs/ai/runtime-rule-index.md"),
            read_text("docs/ai/handoff/current.md"),
        ]
    )
    forbidden_prompt_dependency = re.compile(
        r"(must|should|required to|requires)\s+read(ing)?\s+the\s+original\s+compiler\s+prompt",
        re.IGNORECASE,
    )
    if forbidden_prompt_dependency.search(runtime_text):
        fail("Runtime artifacts appear to require reading the original compiler prompt.")

    print("Runtime validation passed.")


if __name__ == "__main__":
    main()
