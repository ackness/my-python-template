# my-python-template

一个以本地开发为默认的 Python 应用 / CLI 起点：mise + uv + Ruff + Pyrefly + pytest，
GitHub Actions 在 Windows 和 Linux 上检查与构建。

## 快速开始

安装 [mise](https://mise.jdx.dev/getting-started.html)，在仓库根目录运行：

```sh
mise trust
mise install
mise run setup
mise run run
```

检查使用 `mise run check`，格式化使用 `mise run fmt`，打包使用 `mise run build`。
Python 和依赖由 uv 管理，无需手动激活 `.venv`。
保留并提交 `uv.lock`，让日常开发与 CI 按锁文件安装依赖。

需要更新 uv 和项目依赖时运行 `mise run upgrade`。Python、mise 本身及 Action 版本的
更新方式见 [工具链维护技能](.agents/skills/maintain-toolchain/SKILL.md)，不由该命令一并升级。

## 用 agent 开始项目

长期项目约定在 [AGENTS.md](AGENTS.md)，可复用流程在仓库内的 `.agents/skills/`：

| Skill | 用途 |
| --- | --- |
| [python-project-bootstrap](.agents/skills/python-project-bootstrap/SKILL.md) | 将模板改造成具体项目，处理命名、实现、测试和产品文档 |
| [maintain-toolchain](.agents/skills/maintain-toolchain/SKILL.md) | 按需升级工具与依赖，维护 CI 和多语言忽略规则 |

例如向 agent 提出：

```text
使用 $python-project-bootstrap，把这个模板改成一个名为 file-index 的本地文件索引 CLI。
支持扫描目录并输出 JSON，补充测试，把 README 重写为实际使用说明。
```

这些 skills 随仓库保存，无需复制到全局目录。如果当前 agent 没有发现新技能，
可直接让它读取上面链接的 `SKILL.md`。仓库内 skills 的加载方式见
[OpenAI 官方说明](https://developers.openai.com/zh-Hans/docs/build-skills)。

**开始实际项目后，可以直接重写本 README。** 项目约定和模板操作流程已经独立保存，
不依赖此文件；工作流改变时同步更新相应的 AGENTS 或 skill。
