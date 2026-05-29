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
    "docs/ai/tasks/current-slice.yaml",
    "docs/ai/evidence/index.md",
    "docs/ai/knowledge/index.md",
    "docs/ai/skills/index.md",
    "docs/ai/handoff/current.md",
]


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def fail(message: str) -> None:
    print(f"Runtime validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def extract_yaml_scalar(text: str, field: str, source: str) -> str:
    match = re.search(rf"(?m)^{re.escape(field)}:\s*([A-Za-z0-9_\-\[\]]+)\s*$", text)
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
    slice_id = extract_yaml_scalar(
        current_slice, "id", "docs/ai/tasks/current-slice.yaml"
    )
    if status_slice != slice_id:
        fail(
            "docs/ai/status/current.yaml current_slice does not match "
            "docs/ai/tasks/current-slice.yaml id."
        )

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

