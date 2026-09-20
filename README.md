# my-python-template

以本地开发为默认的 Python 应用 / CLI 模板，支持 Windows、Linux 和 macOS。

- **mise**：安装 uv，提供统一任务入口。
- **uv**：安装 Python，管理 `.venv`、项目依赖和 `uv.lock`，构建分发包。
- **Ruff**：代码检查、导入排序和格式化。
- **Pyrefly**：类型检查和编辑器语言服务。
- **pytest**：测试；GitHub Actions 在 Windows 和 Linux 执行相同检查。

## 快速开始

先安装最新版 [mise](https://mise.jdx.dev/getting-started.html)，然后在仓库根目录运行：

```sh
mise trust
mise install
mise run setup
mise run check
mise run run
```

无需单独安装 Python 或手动激活虚拟环境。项目 Python 版本记录在 `.python-version`，
由 uv 查找兼容解释器或自动下载；不要再在 mise 中重复管理项目 Python。`mise exec -- uv ...` 可用于没有
配置 shell 激活的终端，确保调用 mise 管理的 uv，而非系统中的旧版本。

## 常用命令

| 命令 | 用途 |
| --- | --- |
| `mise run setup` | 按锁文件安装项目及开发依赖 |
| `mise run run` | 运行 CLI |
| `mise run fmt` | 安全修复 lint 问题并格式化 |
| `mise run lint` | 只检查 lint 和格式 |
| `mise run typecheck` | 使用 Pyrefly 检查类型 |
| `mise run test` | 执行 pytest |
| `mise run check` | 检查锁文件、lint、格式、类型和测试 |
| `mise run build` | 构建 wheel 和源码分发包到 `dist/` |
| `mise run upgrade` | 更新 uv 和依赖锁文件，然后检查与构建 |

添加依赖使用 `mise exec -- uv add <package>`；添加开发工具使用
`mise exec -- uv add --dev <package>`。不预装应用框架、日志库或异步测试插件，按项目需要添加。

## 目录结构

```text
.github/
  dependabot.yml       # 每周提出依赖及 Actions 更新 PR
  workflows/ci.yml     # Windows / Linux 检查与构建
src/my_python_template/
  __init__.py
  __main__.py         # python -m my_python_template
  run.py              # 应用入口
tests/
  test_cli.py         # 在仓库外验证两种入口的输出和退出码
.python-version
.gitattributes        # 跨平台统一使用 LF
.gitignore
mise.toml
pyproject.toml
README.md
uv.lock
```

Docker、Compose、Dev Container 不作为基础模板依赖。需要系统级环境隔离或数据库服务时，
在具体项目中添加对应配置；基础模板不再发布个人 GHCR 开发镜像。

Ruff 和 pytest 的缓存统一写入 `.cache/`。`.venv/`、`.cache/`、`dist/` 等是运行时
生成的本地目录，均不提交。`.gitignore` 同时覆盖环境变量、常见凭据、日志、本地数据库、
编辑器状态、操作系统杂项，以及 JS/TS 依赖和缓存、Go 测试产物、Rust `target/` 和原生编译产物。
`.env.example`、`.env.template` 和共享项目配置保持可提交。
忽略规则只阻止未跟踪文件进入 Git，不会隐藏已经提交的文件，也不会改变资源管理器的显示。

保留 `uv.lock`、npm/pnpm/Yarn/Bun 锁文件、`Cargo.lock` 和 `go.sum`，保证本地与 CI 的依赖可复现。
当前 Python 工作流依赖 `uv.lock`，不应直接忽略它。Go 模块缓存通常在仓库外；`vendor/`
和 `go.work` 可能属于共享构建配置，因此不一概忽略。如果只是个人本地用途，可在
`.git/info/exclude` 添加项目专属规则。

VS Code 用户可自行安装 Python、Ruff 和 Pyrefly (`meta.pyrefly`) 扩展，选择 `.venv`
解释器；编辑器个人配置保存在被忽略的 `.vscode/` 中。

## 用作新项目

1. 通过 GitHub 模板功能或复制文件创建仓库。
2. 修改 `pyproject.toml` 中的项目名、描述和 `[project.scripts]` 入口。
3. 重命名 `src/my_python_template`，同步修改 Python 导入、入口、测试和 Ruff 的入口文件规则。
4. 修改 `mise.toml` 的运行命令，以及本 README。
5. 执行 `mise exec -- uv lock`、`mise run setup` 和 `mise run check`。

保留 `src/` 布局。`uv_build` 会从项目名推导默认模块名（连字符转为下划线）；
发布到 PyPI 前，按项目实际情况补充许可证和作者等元数据。

## 版本与更新

本次初始化于 2026-09-20 核验：Python 3.14.7、uv / uv_build 0.12.17、
Ruff 0.16.8、Pyrefly 1.3.1、pytest 9.1.1、mise 2026.9.11。
Pyrefly 已发布稳定版；模板使用 Pyrefly 作为唯一类型检查器。

- mise 中的 uv 使用 `latest`；已有安装通过 `mise upgrade uv` 更新。
- 项目依赖以 `uv.lock` 锁定。日常检查和 CI 使用 `--locked`，不会悄悄升级依赖。
- `mise run upgrade` 更新 uv 和项目依赖；审查锁文件变化后提交。
- mise 本身按原安装方式更新，例如 `mise self-update` 或对应包管理器。
- Python 补丁版本显式固定。升级前通过 `mise exec -- uv python list --only-downloads`
  查找最新稳定版，再运行 `mise exec -- uv python pin <version>`。
  如升级 Python 次版本，同时检查 `requires-python` 支持范围，并重新锁定、检查与构建。
- `uv_build` 的上界按官方建议限制在当前兼容系列；跨系列升级时同步调整 `[build-system]`。
- Dependabot 每周提出 uv 和 GitHub Actions 更新 PR；不会自动合并。

## CI

工作流定义在 [ci.yml](.github/workflows/ci.yml)，依赖更新策略定义在
[dependabot.yml](.github/dependabot.yml)。Action 使用明确的发布版本，由 Dependabot 每周提出
升级 PR；mise 本身使用 `latest`，uv 版本策略来自 `mise.toml`。
`mise run upgrade` 只升级 uv 和 Python 项目依赖，不会修改 Action 版本或升级 mise 本身。

GitHub Actions 在推送到 `main`、提交 PR 或手动触发时运行：

```sh
mise run setup
mise run check
mise run build
```

Windows / Linux 共用同一份 `mise.toml` 和 `uv.lock`。macOS 可以本地使用，当前未加入 CI 矩阵。
CI 只检查和构建，不发布包或镜像。更新默认分支名称时，也要调整 workflow 的分支过滤条件。
