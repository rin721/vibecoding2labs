# vibecoding2labs

`vibecoding2labs` 是一个已经初始化 Vibe Coding 运行期基建的仓库。它当前的核心价值不是业务代码，而是一套让开发者和 AI Agent 可以稳定协作的项目运行层：状态、需求、任务树、执行切片、证据、知识库、项目技能和交接说明都已经落在物理文件里。

如果你只是想快速“食用”，从这里开始：

1. 读 [docs/index.md](docs/index.md) 了解文档入口。
2. 读 [docs/usage-guide.md](docs/usage-guide.md) 按步骤使用这个仓库。
3. 读 [docs/project-overview.md](docs/project-overview.md) 理解当前项目结构和运行期基建。
4. 后续让 Agent 继续工作时，先让它读取 [AGENTS.md](AGENTS.md)、[docs/ai/status/current.yaml](docs/ai/status/current.yaml) 和 [docs/ai/tasks/current-slice.yaml](docs/ai/tasks/current-slice.yaml)。

## 当前状态

- 已完成：Vibe Coding 最小运行期基建。
- 当前工作流：`branch_vibe_coding_infra`。
- 当前目标：建立 Vibe Coding 仓库基建支线，避免把基建迭代混入未来业务主线任务树。
- 当前模式：低风险文档治理，候选 `standard_light`。
- 重要规则：运行期恢复不能依赖原始大提示词。缺什么文件就补什么文件。

## 最常用命令

验证运行期入口是否完整：

```powershell
python docs/ai/scripts/validate_runtime.py
```

查看 Git 状态：

```powershell
git status --short --branch
```

## 关键目录

| 路径 | 用途 |
| --- | --- |
| `AGENTS.md` | Agent 短入口，告诉 Agent 该从哪些运行期文件恢复上下文。 |
| `docs/` | 面向人的长期文档。 |
| `docs/ai/` | 面向 Agent 的状态、证据、任务、知识库、skills 和交接资料。 |
| `docs/ai/status/current.yaml` | 当前状态第一入口。 |
| `docs/ai/tasks/forest.yaml` | 任务树林入口，用于区分业务主线和 Vibe Coding 基建支线。 |
| `docs/ai/tasks/main-tree.yaml` | 未来业务/产品想法主线任务树。 |
| `docs/ai/tasks/branches/vibe-coding-infra/tree.yaml` | Vibe Coding 仓库基建支线任务树。 |
| `docs/ai/tasks/current-slice.yaml` | 当前唯一合法执行切片。 |
| `docs/ai/evidence/index.md` | 验证、命令和审计证据入口。 |

## 下一步怎么推进

给 Agent 一个明确目标，例如：

```text
下一步：基于当前状态，为这个仓库设计第一个业务功能。
```

Agent 应先读取状态和当前切片，再进入需求确认、研究验证、任务分析、架构确认、模式确认和执行切片，不应该直接写业务代码。
