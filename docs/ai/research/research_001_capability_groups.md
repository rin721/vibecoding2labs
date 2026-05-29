# research_001: Business Mainline Capability Groups

- Round: `infra_001`
- Branch: `branch_vibe_coding_infra`
- Checked at: `2026-05-29T18:50:41+08:00`
- Trigger: developer confirmed strategy A after phase-one red-light planning
- Status: `candidate_imported`

## Question

Which current UI, frontend architecture, AI Agent script, Python tooling, and
agent framework capabilities should be prepared as selectable capability groups
for the future business mainline?

## Sources

| Source | Trust | Used for |
| --- | --- | --- |
| https://react.dev/learn/start-a-new-react-project | official | React project direction and framework/build-tool framing |
| https://vite.dev/guide/ | official | Vite React TypeScript candidate baseline |
| https://v3.shadcn.com/docs/installation/vite | official | shadcn/ui Vite and Tailwind v4 setup path |
| https://www.radix-ui.com/primitives/docs | official | accessible primitive UI architecture |
| https://tailwindcss.com/docs/installation | official | Tailwind CSS installation direction |
| https://tanstack.com/query/docs/docs | official | server-state management candidate |
| https://reactrouter.com/start/data/routing | official | React routing candidate |
| https://storybook.js.org/docs/10/get-started | official | component workshop and UI state docs |
| https://docs.pytest.org/en/stable/getting-started.html | official | Python test framework |
| https://docs.astral.sh/ruff/linter/ | official | Python linting |
| https://docs.astral.sh/ruff/formatter/ | official | Python formatting |
| https://typer.tiangolo.com/ | official | Python CLI tooling |
| https://docs.pydantic.dev/latest/concepts/models/ | official | structured data validation |
| https://playwright.dev/python/docs/intro | official | browser automation candidate |
| https://openai.github.io/openai-agents-python/agents/ | official | OpenAI agent orchestration |
| https://pydantic.dev/docs/ai/overview/ | official | Python-first agent framework |
| https://docs.langchain.com/oss/python/langgraph/workflows-agents | official | graph/stateful agent workflows |

## Conclusion

Create candidate capability groups, not installed dependencies. The current
repository has no frontend or Python package boundary. Installing packages now
would create premature lockfiles and technical commitment before a business
mainline requirement exists.

## Recommended Catalog

1. UI library and design system: `shadcn/ui + Radix UI + Tailwind CSS`.
2. Frontend architecture: `React + TypeScript + Vite` with explicit module
   boundaries.
3. AI Agent script tools: Python CLI and validation scripts with typed IO.
4. Python tooling: `pytest + ruff + typer + pydantic`, with Playwright only when
   browser automation is needed.
5. Agent frameworks: `OpenAI Agents SDK` or `Pydantic AI` for agent runtime;
   `LangGraph` only when explicit stateful graph workflows are needed.
6. Quality verification: every capability adoption must add validation and
   evidence.

## Confirmation Boundary

This research supports strategy A. Installing dependencies, creating lockfiles,
or generating app/tool skeletons remains blocked until a future explicit
confirmation chooses strategy B or C.

