$ErrorActionPreference = "Stop"

$required = @(
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
  "docs/ai/handoff/current.md"
)

$missing = @()
foreach ($path in $required) {
  if (-not (Test-Path -LiteralPath $path)) {
    $missing += $path
  }
}

if ($missing.Count -gt 0) {
  throw "Missing required runtime artifacts: $($missing -join ', ')"
}

$agents = Get-Content -LiteralPath "AGENTS.md" -Raw
if ($agents -notmatch "No Prompt Runtime Dependency") {
  throw "AGENTS.md must include the no prompt runtime dependency section."
}

$status = Get-Content -LiteralPath "docs/ai/status/current.yaml" -Raw
$slice = Get-Content -LiteralPath "docs/ai/tasks/current-slice.yaml" -Raw

$statusSliceMatch = [regex]::Match($status, "(?m)^current_slice:\s*([A-Za-z0-9_\-]+)\s*$")
if (-not $statusSliceMatch.Success) {
  throw "status/current.yaml must define current_slice."
}

$sliceIdMatch = [regex]::Match($slice, "(?m)^id:\s*([A-Za-z0-9_\-]+)\s*$")
if (-not $sliceIdMatch.Success) {
  throw "tasks/current-slice.yaml must define id."
}

if ($statusSliceMatch.Groups[1].Value -ne $sliceIdMatch.Groups[1].Value) {
  throw "status/current.yaml current_slice does not match tasks/current-slice.yaml id."
}

if ($status -notmatch "(?m)^next_allowed_phase:\s*\S+") {
  throw "status/current.yaml must define next_allowed_phase."
}

$runtimeText = Get-Content -LiteralPath "AGENTS.md","docs/ai/runtime-rule-index.md","docs/ai/handoff/current.md" -Raw
if ($runtimeText -match "(must|should|required to|requires)\s+read(ing)?\s+the\s+original\s+compiler\s+prompt") {
  throw "Runtime artifacts appear to require reading the original compiler prompt."
}

Write-Output "Runtime validation passed."
